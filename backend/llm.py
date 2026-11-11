"""Groq LLM access: prompt assembly, streaming with instant multi-model failover, and screen analysis."""
from __future__ import annotations

import logging
import re
import threading
import time
from typing import Iterator

import groq
from groq import Groq

import config

log = logging.getLogger("wisein.llm")

# No SDK-level retries: on a rate limit we switch model instantly instead of sleeping 2-30s.
client = Groq(api_key=config.GROQ_API_KEY, timeout=20.0, max_retries=0) if config.GROQ_API_KEY else None

# Each Groq model has its own per-minute token quota, so spreading load over several models multiplies capacity.
MODEL_CHAIN = list(dict.fromkeys([config.LLM_MODEL, *config.LLM_FALLBACK_MODELS]))
MAX_WAIT_SECONDS = 12      # if every model is rate-limited, wait at most this long before giving up
MAX_TOKENS = 600
HISTORY_MESSAGES = 6       # last 3 exchanges are sent verbatim; older turns are dropped
HISTORY_CHARS = 1000

HANDOFF_TEXT = "I can connect you with the WiseIN support team. You can reach them using the options below."

SYSTEM_PROMPT = f"""You are WiseIN Support, the official AI support assistant for WiseIN, a professional networking platform (web, Android, iOS) by Sanshi Network Tech Private Limited.

Answer ONLY from the knowledge base excerpts below. They are internal documentation, so never mention excerpts, documents, IDs, versions, draft status or internal notes ("the AI must..."). If they don't cover the question, say you don't have information about that and offer to connect the user with the WiseIN support team. Never invent features, steps, prices or policies.

Style: start with the answer, no greeting or filler. How-to: short numbered steps. Options: bullets. Simple questions: 1-3 sentences. Under 150 words unless asked for detail. If steps differ by platform and the user didn't say which, give the common steps and note the difference. Reply in the user's language. Use the conversation to understand follow-ups.

If the user asks for a human/agent/customer care, or says the documented steps didn't fix their problem, reply exactly: "{HANDOFF_TEXT}"
"""

_NO_INFO = re.compile(r"(do not|don't|doesn't|does not) (have|include|contain|cover)[^.]{0,40}(information|details|documentation)", re.I)

_cooldown: dict[str, float] = {}
_cooldown_lock = threading.Lock()


class LLMError(Exception):
    pass


def is_ready() -> bool:
    return client is not None


def _plain(text: str) -> str:
    return text.replace("’", "'").replace("‘", "'").strip().lower()


def is_no_info(answer: str) -> bool:
    """The model said the knowledge base doesn't cover the question."""
    return bool(_NO_INFO.search(_plain(answer)[:300]))


def offers_handoff(answer: str) -> bool:
    """The answer mentions the support team handoff anywhere (show the contact card)."""
    return HANDOFF_TEXT[:40].lower() in _plain(answer)


def is_handoff(answer: str) -> bool:
    """The answer IS a handoff (not troubleshooting steps that end with an offer): open a ticket."""
    a = _plain(answer)
    return a.startswith(HANDOFF_TEXT[:40].lower()) or (offers_handoff(answer) and len(a) < len(HANDOFF_TEXT) + 60)


def build_messages(user_content, excerpts: list[str], history: list[dict]) -> list[dict]:
    kb = "\n\n".join(f"[{i}] {t}" for i, t in enumerate(excerpts, 1)) or "(no relevant excerpts found)"
    messages = [{"role": "system", "content": f"{SYSTEM_PROMPT}\n--- KNOWLEDGE BASE EXCERPTS ---\n{kb}"}]
    for m in history[-HISTORY_MESSAGES:]:
        role = "assistant" if m.get("role") in ("bot", "assistant") else "user"
        content = (m.get("content") or "").strip()
        if content:
            messages.append({"role": role, "content": content[:HISTORY_CHARS]})
    messages.append({"role": "user", "content": user_content})
    return messages


def _model_kwargs(model: str) -> dict:
    if model.startswith("qwen/"):
        return {"reasoning_effort": "none"}       # skip hidden reasoning: ~3x faster first token
    if model.startswith("openai/gpt-oss"):
        return {"reasoning_effort": "low"}
    return {}


def _retry_after(err: Exception) -> float:
    try:
        return max(1.0, min(60.0, float(err.response.headers.get("retry-after", 5))))
    except Exception:
        return 5.0


def _ready_models(models: list[str]) -> tuple[list[str], float]:
    """Models not cooling down after a rate limit, plus seconds until the earliest one frees up."""
    now = time.monotonic()
    with _cooldown_lock:
        ready = [m for m in models if _cooldown.get(m, 0) <= now]
        wait = min((_cooldown[m] - now for m in models if _cooldown.get(m, 0) > now), default=0.0)
    return ready, wait


def _call_with_failover(models: list[str], make_call, max_wait: float = MAX_WAIT_SECONDS):
    """Runs make_call(model) on the first usable model; on 429/5xx/timeouts moves to the next one immediately.
    Only when every model is cooling down after a rate limit does it wait (at most max_wait) for one to free up."""
    deadline = time.monotonic() + max_wait
    last_err: Exception | None = None
    while True:
        ready, _ = _ready_models(models)
        for model in ready:
            try:
                return make_call(model)
            except groq.RateLimitError as e:
                log.warning("Rate limited on %s (free in %.0fs); failing over", model, _retry_after(e))
                with _cooldown_lock:
                    _cooldown[model] = time.monotonic() + _retry_after(e)
                last_err = e
            except groq.APIError as e:
                log.warning("LLM error on %s: %s", model, e)
                last_err = e
        ready, wait = _ready_models(models)
        if ready:
            break  # the remaining models failed with real errors: waiting won't help
        if time.monotonic() + wait > deadline:
            break
        time.sleep(max(0.2, wait))
    if last_err is None or isinstance(last_err, groq.RateLimitError):
        raise LLMError("The assistant is handling a lot of requests right now.") from last_err
    raise LLMError("The AI service is temporarily unavailable.") from last_err


def stream_answer(messages: list[dict]) -> Iterator[str]:
    """Streams answer tokens, failing over across MODEL_CHAIN before the first token if a model is limited or down."""
    if client is None:
        raise LLMError("GROQ_API_KEY is not configured.")

    def open_stream(model: str):
        it = iter(client.chat.completions.create(
            model=model, messages=messages, temperature=0.2, max_tokens=MAX_TOKENS, stream=True, **_model_kwargs(model)))
        return model, next(it, None), it  # pulling the first chunk surfaces 429s before anything reaches the user

    model, first, rest = _call_with_failover(MODEL_CHAIN, open_stream)
    if model != MODEL_CHAIN[0]:
        log.info("Answered by fallback model %s", model)

    def chunks():
        if first is not None:
            yield first
        yield from rest

    started = in_think = False
    try:
        for chunk in chunks():
            if not chunk.choices:
                continue
            text = chunk.choices[0].delta.content
            if not text:
                continue
            # Guard against reasoning text leaking into the answer on models that inline it.
            if not started and text.lstrip().startswith("<think>"):
                in_think = True
            if in_think:
                if "</think>" not in text:
                    continue
                in_think = False
                text = text.split("</think>", 1)[1].lstrip()
                if not text:
                    continue
            started = True
            yield text
    except Exception as e:
        log.warning("Stream interrupted on %s: %s", model, e)
        raise LLMError("The answer was interrupted.") from e


def describe_screen(image_data_url: str, question: str) -> str:
    """Short factual description of a screenshot; used both to retrieve KB content and to ground the answer."""
    if client is None:
        raise LLMError("GROQ_API_KEY is not configured.")
    prompt = (
        "A WiseIN user shared this screenshot while asking for support."
        + (f' Their question: "{question}".' if question else "")
        + " In 2-5 sentences: which WiseIN screen or feature is shown, the main buttons/links/menus visible (use their"
        " exact labels), and any error or warning messages (quote them exactly). Do not repeat personal data such as"
        " names, emails or phone numbers."
    )

    def call(model: str) -> str:
        res = client.chat.completions.create(
            model=model, temperature=0.1, max_tokens=220, **_model_kwargs(model),
            messages=[{"role": "user", "content": [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": {"url": image_data_url}},
            ]}],
        )
        return (res.choices[0].message.content or "").strip()

    # Only the vision model can read images, so allow a slightly longer wait if it is momentarily rate-limited.
    return _call_with_failover([config.VISION_MODEL], call, max_wait=25)
