import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import config  # noqa: E402  (loads .env before anything reads env vars)

import base64  # noqa: E402
import json  # noqa: E402
import logging  # noqa: E402
import re  # noqa: E402
import threading  # noqa: E402
import time  # noqa: E402
from collections import OrderedDict  # noqa: E402
from contextlib import asynccontextmanager  # noqa: E402
from typing import Optional  # noqa: E402

import uvicorn  # noqa: E402
from fastapi import FastAPI, HTTPException, Request  # noqa: E402
from fastapi.concurrency import run_in_threadpool  # noqa: E402
from fastapi.middleware.cors import CORSMiddleware  # noqa: E402
from fastapi.responses import FileResponse, RedirectResponse, StreamingResponse  # noqa: E402
from pydantic import BaseModel, Field  # noqa: E402

import llm  # noqa: E402
import store  # noqa: E402
from auth import ensure_admin, router as auth_router  # noqa: E402
from database import init_db  # noqa: E402
from features import load_published_documents, router as features_router, sync_published_documents  # noqa: E402
from knowledge import kb  # noqa: E402
from ratelimit import chat_limiter, screen_limiter  # noqa: E402

log = logging.getLogger("wisein.api")

TOP_K = 5
SSE_HEADERS = {"Cache-Control": "no-cache", "X-Accel-Buffering": "no"}


_started = threading.Event()
_start_lock = threading.Lock()


def startup():
    """Idempotent initialisation. Runs at server start locally; on serverless it runs on the first request
    of each instance (some platforms don't send ASGI lifespan events)."""
    if _started.is_set():
        return
    with _start_lock:
        if _started.is_set():
            return
        t0 = time.perf_counter()
        init_db()
        ensure_admin()
        kb.load()
        load_published_documents()
        if not llm.is_ready():
            log.error("GROQ_API_KEY is missing: the assistant cannot answer until it is set")
        _started.set()
        log.info("WiseIN AI Support initialised in %.1fs", time.perf_counter() - t0)


@asynccontextmanager
async def lifespan(_app: FastAPI):
    await run_in_threadpool(startup)
    if not config.ON_VERCEL:
        log.info("Ready: http://localhost:%d/support  (admin: http://localhost:%d/admin)", config.PORT, config.PORT)
    yield


app = FastAPI(title="WiseIN AI Support API", version="9.0", lifespan=lifespan)
app.include_router(auth_router)
app.include_router(features_router)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


@app.middleware("http")
async def ensure_started(request: Request, call_next):
    if not _started.is_set() and request.url.path not in ("/", "/support", "/admin"):
        await run_in_threadpool(startup)  # pages don't need the index; let them render during a cold start
    return await call_next(request)


# ---------------------------------------------------------------- request models

class HistoryItem(BaseModel):
    role: str
    content: str = ""


class ChatRequest(BaseModel):
    query: str = Field(min_length=1, max_length=2000)
    history: list[HistoryItem] = Field(default_factory=list, max_length=100)
    conversation_id: Optional[int] = None
    client_id: str = Field(default="", max_length=64)


class ScreenAnalysisRequest(BaseModel):
    image_base64: str = Field(min_length=100, max_length=8_000_000)
    question: str = Field(default="", max_length=2000)
    history: list[HistoryItem] = Field(default_factory=list, max_length=100)
    conversation_id: Optional[int] = None
    client_id: str = Field(default="", max_length=64)


# ---------------------------------------------------------------- instant replies (no LLM call)

_SMALLTALK = [
    (re.compile(r"^(hi+|hello+|hey+|hiya|namaste|good (morning|afternoon|evening))( there)?[\s!.,]*$", re.I),
     "Hi! I'm the WiseIN support assistant. What can I help you with today?"),
    (re.compile(r"^((ok(ay)?|great|cool|perfect|awesome)[,!. ]*)?(thanks?|thank you|thx|ty)( (so|very) much| a lot)?[\s!.]*$", re.I),
     "You're welcome! Is there anything else I can help you with?"),
    (re.compile(r"^(ok(ay)?|cool|great|got it|alright|perfect|nice)[\s!.]*$", re.I),
     "Great! Let me know if there's anything else you need help with."),
    (re.compile(r"^(bye|goodbye|see you|that'?s all)[\s!.]*$", re.I),
     "Thanks for contacting WiseIN Support. Have a great day!"),
]

_WANTS_HUMAN = re.compile(
    r"\b(talk|speak|chat|connect)( me)? (to|with) (a |an |the |your )?(human|person|someone|somebody|agent|representative|"
    r"executive|customer care|support( team)?|team)\b"
    r"|\b(want|need|get) (a |an )?(human|real person|live agent|agent|representative)\b"
    r"|\bcustomer (care|service)\b|\bhuman (support|agent|help)\b|\breal person\b|\blive (agent|chat|support)\b"
    r"|\bcontact (customer )?support\b|\bcall (me|support)\b", re.I)

_FOLLOWUP = re.compile(r"\b(it|its|that|this|those|these|they|them|there|same|again|still|instead|also|else|"
                       r"didn'?t|doesn'?t|not working|what about|how about)\b", re.I)


def _smalltalk_reply(query: str) -> str | None:
    for pattern, reply in _SMALLTALK:
        if pattern.match(query):
            return reply
    return None


# ---------------------------------------------------------------- answer cache
# First-turn questions repeat a lot (suggestion chips, FAQs). Serving them from memory is instant and saves
# the Groq per-minute token quota. Entries expire after 6h and whenever the knowledge index changes.

_CACHE_TTL = 6 * 3600
_CACHE_MAX = 500
_cache: "OrderedDict[str, tuple[float, str, list, bool]]" = OrderedDict()
_cache_lock = threading.Lock()


def _cache_key(query: str) -> str:
    return f"{kb.version}|" + re.sub(r"[^a-z0-9]+", " ", query.lower()).strip()


def _cache_get(query: str):
    with _cache_lock:
        hit = _cache.get(_cache_key(query))
        if hit and time.time() - hit[0] < _CACHE_TTL:
            return hit
    return None


def _cache_put(query: str, answer: str, sources: list, card: bool):
    with _cache_lock:
        _cache[_cache_key(query)] = (time.time(), answer, sources, card)
        while len(_cache) > _CACHE_MAX:
            _cache.popitem(last=False)


# ---------------------------------------------------------------- helpers

def _clean_history(history: list[HistoryItem], query: str) -> list[dict]:
    items = [h.model_dump() for h in history if (h.content or "").strip()]
    if items and items[-1]["role"] == "user" and items[-1]["content"].strip() == query.strip():
        items.pop()  # older clients sent the current question inside history too
    return items


def _retrieve(query: str, history: list[dict]) -> list[dict]:
    """Search the KB. Follow-ups ("it still doesn't work") are also searched together with the previous question."""
    results = kb.search(query, TOP_K)
    prev = next((h["content"] for h in reversed(history) if h["role"] == "user"), None)
    if prev and (len(query.split()) <= 8 or _FOLLOWUP.search(query)):
        combined = kb.search(f"{prev[:300]} {query}", TOP_K)
        merged, seen = [], set()
        for pair in zip(combined, results):
            for r in pair:
                if r["chunk"].id not in seen:
                    seen.add(r["chunk"].id)
                    merged.append(r)
        results = merged[:TOP_K + 1]
    return results


def _sources(results: list[dict]) -> list[dict]:
    out, seen = [], set()
    for r in results:
        c = r["chunk"]
        if c.topic not in seen:
            seen.add(c.topic)
            out.append({"name": c.topic, "section": c.section})
    return out[:3]


def _sse(obj: dict) -> str:
    return f"data: {json.dumps(obj)}\n\n"


def _instant_reply(conv_id, query: str, text: str, sources=(), card: bool = False):
    yield _sse({"type": "meta", "conversation_id": conv_id})
    yield _sse({"type": "token", "content": text})
    if card:
        yield _sse({"type": "escalation"})
    msg_id = store.save_exchange(conv_id, query, text, list(sources), None)  # no LLM call: keep out of latency stats
    yield _sse({"type": "done", "message_id": msg_id, "sources": list(sources)})


def _answer_stream(*, t0: float, conv_id, user_text: str, log_text: str, messages: list[dict],
                   results: list[dict], kind: str = "chat", cache_query: str | None = None):
    """Streams LLM tokens, then decides on the contact card / ticket, persists the exchange and logs timing."""
    answer, first_ms = "", None
    try:
        for tok in llm.stream_answer(messages):
            if first_ms is None:
                first_ms = int((time.perf_counter() - t0) * 1000)
            answer += tok
            yield _sse({"type": "token", "content": tok})
    except llm.LLMError as e:
        store.log_event("llm_error", error=str(e), kind=kind)
        yield _sse({"type": "error", "message": f"{e} Please try again in a moment."})
        if not answer:
            return

    sources = _sources(results)
    card = False
    if llm.is_no_info(answer):
        card, sources = True, []  # KB didn't cover it: offer contact options, hide unrelated sources
        store.log_event("no_answer", conversation_id=conv_id, query=user_text[:300])
    elif llm.is_handoff(answer):
        card = True
        store.open_ticket(conv_id, user_text)
        store.log_event("escalation", conversation_id=conv_id, reason="assistant_handoff")
    elif llm.offers_handoff(answer):
        card = True  # troubleshooting steps that end by offering human help: show contact options, no ticket
    if card:
        yield _sse({"type": "escalation"})
    msg_id = store.save_exchange(conv_id, log_text, answer, sources, first_ms)
    yield _sse({"type": "done", "message_id": msg_id, "sources": sources})
    if cache_query and not llm.is_handoff(answer):
        _cache_put(cache_query, answer, sources, card)
    log.info("[%s] first_token=%sms total=%dms chunks=%d chars=%d q=%r", kind, first_ms,
             (time.perf_counter() - t0) * 1000, len(results), len(answer), user_text[:60])


# ---------------------------------------------------------------- endpoints

@app.post("/api/chat")
def chat(req: ChatRequest, request: Request):
    chat_limiter.check(request)
    query = req.query.strip()
    if not query:
        raise HTTPException(status_code=400, detail="Query cannot be empty.")
    if not llm.is_ready():
        raise HTTPException(status_code=503, detail="The assistant is not configured (missing GROQ_API_KEY).")
    t0 = time.perf_counter()

    def stream():
        conv_id = store.get_or_create_conversation(req.conversation_id, req.client_id, query) if req.client_id else None
        history = _clean_history(req.history, query)

        canned = _smalltalk_reply(query)
        if canned:
            yield from _instant_reply(conv_id, query, canned)
            return
        if _WANTS_HUMAN.search(query):
            recent = [h["content"] for h in history if h["role"] == "user"][-2:] + [query]
            store.open_ticket(conv_id, " | ".join(recent))
            store.log_event("escalation", conversation_id=conv_id, reason="user_requested")
            yield from _instant_reply(conv_id, query, llm.HANDOFF_TEXT, card=True)
            return
        if not history:
            hit = _cache_get(query)
            if hit:
                _, answer, sources, card = hit
                store.log_event("cache_hit")
                log.info("[chat] cache hit q=%r", query[:60])
                yield from _instant_reply(conv_id, query, answer, sources, card)
                return

        sync_published_documents()  # picks up articles published on other instances (cheap, throttled)
        results = _retrieve(query, history)
        yield _sse({"type": "meta", "conversation_id": conv_id})
        messages = llm.build_messages(query, [r["chunk"].llm_text for r in results], history)
        yield from _answer_stream(t0=t0, conv_id=conv_id, user_text=query, log_text=query, messages=messages,
                                  results=results, cache_query=None if history else query)

    return StreamingResponse(stream(), media_type="text/event-stream", headers=SSE_HEADERS)


_DATA_URL_HEADER = re.compile(r"^data:image/(png|jpe?g|webp);base64$")


@app.post("/api/screen-assist/analyze")
def analyze_screen(req: ScreenAnalysisRequest, request: Request):
    screen_limiter.check(request)
    if not llm.is_ready():
        raise HTTPException(status_code=503, detail="The assistant is not configured (missing GROQ_API_KEY).")
    image = req.image_base64.strip()
    if not image.startswith("data:"):
        image = "data:image/jpeg;base64," + image
    header, _, payload = image.partition(",")
    try:
        if not _DATA_URL_HEADER.match(header) or len(base64.b64decode(payload, validate=True)) > 6_000_000:
            raise ValueError
    except ValueError:
        raise HTTPException(status_code=400, detail="Please share a PNG, JPEG or WebP screenshot under 6 MB.")
    t0 = time.perf_counter()

    def stream():
        history = _clean_history(req.history, "")
        question = req.question.strip()
        context_q = question or next((h["content"] for h in reversed(history) if h["role"] == "user"), "")
        conv_id = (store.get_or_create_conversation(req.conversation_id, req.client_id, question or "Screen Assist")
                   if req.client_id else None)
        yield _sse({"type": "meta", "conversation_id": conv_id})
        try:
            description = llm.describe_screen(image, context_q)
        except llm.LLMError as e:
            log.warning("Screen analysis failed: %s", e)
            store.log_event("llm_error", error=str(e)[:300], kind="screen_assist")
            yield _sse({"type": "error", "message": "I couldn't analyze your screen right now. Please try again, or describe what you see."})
            return
        store.log_event("screen_assist", conversation_id=conv_id)

        # The image is sent once (to describe it); the answer is grounded on that description plus the KB.
        # Images cost ~800 tokens each against Groq's per-minute quota, so this keeps Screen Assist fast.
        sync_published_documents()
        results = kb.search(f"{context_q} {description}".strip(), TOP_K)
        ask = f"My question: {question}" if question else (
            f"I was asking: {context_q}" if context_q else "Please help me with what I'm seeing.")
        text = f"I shared a screenshot of my WiseIN screen. {ask}\nWhat's on my screen: {description}"
        messages = llm.build_messages(text, [r["chunk"].llm_text for r in results], history)
        yield from _answer_stream(t0=t0, conv_id=conv_id, user_text=context_q or "Screen Assist",
                                  log_text=f"[Shared screen] {question}\nScreen summary: {description}".strip(),
                                  messages=messages, results=results, kind="screen")

    return StreamingResponse(stream(), media_type="text/event-stream", headers=SSE_HEADERS)


@app.get("/health")
def health():
    ok = kb.ready and llm.is_ready()
    return {
        "status": "ok" if ok else "degraded",
        "knowledge_index": kb.ready,
        "knowledge_chunks": kb.size,
        "llm_ready": llm.is_ready(),
        "models": llm.MODEL_CHAIN,
    }


def _page(name: str) -> FileResponse:
    return FileResponse(config.FRONTEND_DIR / name, media_type="text/html", headers={"Cache-Control": "no-cache"})


@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse("/support")


@app.get("/support", include_in_schema=False)
def serve_ui():
    return _page("index.html")


@app.get("/admin", include_in_schema=False)
def serve_admin():
    return _page("admin.html")


def _port_in_use(port: int) -> bool:
    import socket
    with socket.socket() as s:
        s.settimeout(0.5)
        return s.connect_ex(("127.0.0.1", port)) == 0


if __name__ == "__main__":
    # On Windows another program bound to 127.0.0.1:<port> silently receives all localhost traffic
    # even though this server starts fine on 0.0.0.0, so fail loudly instead of looking broken.
    if _port_in_use(config.PORT):
        log.error("Port %d is already used by another program, so http://localhost:%d would not reach this app. "
                  "Stop that program or set PORT=<free port> in .env (e.g. PORT=8080).", config.PORT, config.PORT)
        sys.exit(1)
    uvicorn.run("api:app", host="0.0.0.0", port=config.PORT, reload=False)
