"""
Local hybrid retrieval over the WiseIN knowledge base.

Replaces the remote Qdrant Cloud dependency: the KB is small (80 topic files), so an
in-memory index answers in a few milliseconds with no network hop and no external
service that can go down. Retrieval combines dense embeddings (semantic match) with
BM25 (exact keyword match, e.g. feature names and error codes) via reciprocal-rank fusion.

Embeddings for the Markdown KB are cached on disk, keyed by a hash of the chunk texts,
so restarts are fast and the cache rebuilds itself whenever a KB file changes.
Admin-published documents (from the database) are indexed live on top of the KB.
"""
from __future__ import annotations

import hashlib
import json
import logging
import math
import re
import threading
import time
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np

import config

log = logging.getLogger("wisein.knowledge")

CHUNKER_VERSION = "v2"
TARGET_CHARS = 1000      # aim for ~250 tokens: fits the embedding model's window fully
MAX_CHARS = 1400
MIN_BREAK_CHARS = 350    # start a new chunk at a section heading once this much is collected
MIN_CHUNK_CHARS = 80
RRF_K = 60
CANDIDATES = 40
TOPIC_BOOST = 0.01       # tuned on a 40-question eval: hit@5 39 -> 40/40, hit@1 25 -> 28/40
QUERY_CACHE_SIZE = 1024

# ---------------------------------------------------------------- text cleanup

_BULLET_ONLY = re.compile(r"^[•●▪◦‣∙·\-\*]$")
_HEADING = re.compile(r"^(\d{1,2}(?:\.\d{1,2})*)\.?\s+([A-Z][^\n]{1,90})$")
_MD_HEADING = re.compile(r"^#{1,6}\s+(.+)$")
_SOURCE_SPLIT = re.compile(r"^## Source:.*$", re.M)


def clean_text(text: str) -> str:
    """Repair PDF-extraction artifacts: lone bullet glyphs, hard-wrapped lines, spacing."""
    text = text.replace("\r\n", "\n").replace(" ", " ")
    lines: list[str] = []
    pending_bullet = False
    for raw in text.split("\n"):
        s = raw.strip()
        if _BULLET_ONLY.match(s):
            pending_bullet = True
            continue
        if pending_bullet:
            if not s:
                continue
            lines.append("- " + s)
            pending_bullet = False
            continue
        lines.append(s)

    joined: list[str] = []
    for s in lines:
        prev = joined[-1] if joined else ""
        if prev and s and s[0].islower() and not prev.startswith("#") and not re.search(r"[.:!?]$", prev):
            joined[-1] = prev + " " + s  # hard-wrapped continuation line
        else:
            joined.append(s)
    out = "\n".join(joined)
    out = re.sub(r"[ \t]{2,}", " ", out)
    out = re.sub(r"\n{3,}", "\n\n", out)
    return out.strip()


def _heading_of(line: str) -> str | None:
    line = line.strip()
    m = _MD_HEADING.match(line)
    if m:
        return m.group(1).strip()
    m = _HEADING.match(line)
    if m and not re.search(r"[.,;]$", line) and len(m.group(2).split()) <= 12:
        return m.group(2).strip()
    return None


def _blocks(text: str) -> list[str]:
    """Split into paragraph blocks, starting a new block at every heading line."""
    blocks: list[str] = []
    for para in re.split(r"\n\s*\n", text):
        cur: list[str] = []
        for line in para.split("\n"):
            if _heading_of(line) and cur:
                blocks.append("\n".join(cur))
                cur = []
            cur.append(line)
        if cur:
            blocks.append("\n".join(cur))
    out: list[str] = []
    for b in blocks:
        b = b.strip()
        if not b:
            continue
        while len(b) > MAX_CHARS:  # oversized block: cut at a line or sentence boundary
            cut = b.rfind("\n", 0, MAX_CHARS)
            if cut < MAX_CHARS // 2:
                cut = b.rfind(". ", 0, MAX_CHARS) + 1
            if cut < MAX_CHARS // 2:
                cut = MAX_CHARS
            out.append(b[:cut].strip())
            b = b[cut:].strip()
        if b:
            out.append(b)
    return out


@dataclass
class Chunk:
    id: str
    topic: str
    section: str
    body: str
    source: str  # "kb:<filename>" or "db:<document id>"

    @property
    def llm_text(self) -> str:
        return f"[{self.topic} > {self.section}]\n{self.body}" if self.section else f"[{self.topic}]\n{self.body}"

    @property
    def embed_text(self) -> str:
        return f"{self.topic}. {self.section}. {self.body}"


def chunk_text(text: str, topic: str, source: str, id_prefix: str) -> list[Chunk]:
    chunks: list[Chunk] = []
    section = ""
    cur: list[str] = []
    cur_section = ""

    def emit():
        body = "\n\n".join(cur).strip()
        if len(body) >= MIN_CHUNK_CHARS:
            chunks.append(Chunk(f"{id_prefix}-{len(chunks):04d}", topic, cur_section, body, source))

    for block in _blocks(clean_text(text)):
        head = _heading_of(block.split("\n", 1)[0])
        if head:
            section = head
        size = sum(len(c) for c in cur)
        if cur and (size + len(block) > MAX_CHARS or size >= TARGET_CHARS or (head and size >= MIN_BREAK_CHARS)):
            emit()
            # carry a short trailing block forward so steps that straddle a boundary keep context
            tail = cur[-1] if len(cur[-1]) < 250 and not head else None
            cur = [tail] if tail else []
            cur_section = section
        if not cur:
            cur_section = section
        cur.append(block)
    if cur:
        emit()
    return chunks


def _norm_key(text: str) -> str:
    return hashlib.sha1(re.sub(r"[^a-z0-9]+", "", text.lower()).encode()).hexdigest()


def load_kb_chunks(kb_dir: Path = config.KB_DIR) -> list[Chunk]:
    manifest = {}
    mpath = kb_dir / "manifest.json"
    if mpath.exists():
        manifest = {m["topic_number"]: m for m in json.loads(mpath.read_text(encoding="utf-8"))}

    docs = []
    for path in sorted(kb_dir.glob("*.md")):
        if path.name.lower() == "readme.md":
            continue
        raw = path.read_text(encoding="utf-8")
        num = path.name.split("_", 1)[0]
        topic = manifest.get(num, {}).get("topic_name") or path.stem.split("_", 1)[-1].replace("_", " ").title()
        parts = [p for p in _SOURCE_SPLIT.split(raw)[1:] if p.strip()] or [_MD_HEADING.sub("", raw, count=1)]
        docs.append((len(parts), path.name, topic, parts))

    # Several source PDFs were extracted twice (e.g. the Login doc lives in both 03 and 04).
    # Index each source once, preferring the topic file where it is the only source.
    docs.sort(key=lambda d: (d[0], d[1]))
    seen: set[str] = set()
    chunks: list[Chunk] = []
    dupes = 0
    for _, fname, topic, parts in docs:
        for pi, part in enumerate(parts):
            for c in chunk_text(part, topic, f"kb:{fname}", f"{fname[:2]}-{pi}"):
                key = _norm_key(c.body)
                if key in seen:
                    dupes += 1
                    continue
                seen.add(key)
                chunks.append(c)
    chunks.sort(key=lambda c: c.id)
    log.info("Knowledge base: %d chunks from %d files (%d duplicate chunks skipped)", len(chunks), len(docs), dupes)
    return chunks


# ---------------------------------------------------------------- BM25

_STOP = set("""a an and are as at be but by can could did do does doing for from had has have how i if in into is it its
me my of on or our should so than that the their them then there these they this to too up us was we were what when where
which who why will with would you your yours am been being i'm im wisein""".split())
_TOKEN = re.compile(r"[a-z0-9]+")


def _stem(w: str) -> str:
    for root in ("verif", "notif", "subscri", "deactivat", "delet", "recover", "transcri"):
        if w.startswith(root):
            return root  # verify / verified / verification -> verif, etc.
    if len(w) > 4 and w.endswith("ies"):
        return w[:-3] + "y"
    if len(w) > 5 and w.endswith("ing"):
        return w[:-3]
    if len(w) > 4 and w.endswith("ed"):
        return w[:-2]
    if len(w) > 3 and w.endswith("s") and not w.endswith("ss"):
        return w[:-1]
    return w


# Multi-word terms whose meaning is lost once split ("log in" -> stopword "in" + "log", which matches "log out").
_PHRASES = [
    (re.compile(r"\b(log|sign)[\s-]?in(to)?\b"), " login "),
    (re.compile(r"\b(log|sign)[\s-]?out\b"), " logout "),
    (re.compile(r"\bsign[\s-]?up\b|\bregister\b|\bregistration\b"), " signup "),
    (re.compile(r"\be[\s-]mail\b"), " email "),
    (re.compile(r"\bone[\s-]time (password|passcode|code)\b"), " otp "),
    (re.compile(r"\b2fa\b|\btwo[\s-]factor\b"), " twofactor "),
]


def normalize_terms(text: str) -> str:
    text = text.lower()
    for pattern, repl in _PHRASES:
        text = pattern.sub(repl, text)
    return text


def tokenize(text: str) -> list[str]:
    return [_stem(w) for w in _TOKEN.findall(normalize_terms(text)) if w not in _STOP and len(w) > 1]


def _embedding_query(query: str) -> str:
    """Disambiguate short queries the embedding model confuses (e.g. 'log in' vs 'log out')."""
    q = query
    low = query.lower()
    if re.search(r"\b(log|sign)[\s-]?in\b", low) and not re.search(r"\b(log|sign)[\s-]?out\b", low):
        q += " (sign in / login to my account)"
    elif re.search(r"\b(log|sign)[\s-]?out\b", low):
        q += " (sign out / logout)"
    return q


@dataclass
class _Index:
    chunks: list[Chunk]
    vectors: np.ndarray                      # (n, d), L2-normalised
    postings: dict[str, tuple[np.ndarray, np.ndarray]] = field(default_factory=dict)  # term -> (doc idx, bm25 weight)
    topic_terms: list[set[str]] = field(default_factory=list)

    @classmethod
    def build(cls, chunks: list[Chunk], vectors: np.ndarray, token_counts: list[Counter]) -> "_Index":
        n = len(chunks)
        k1, b = 1.4, 0.75
        lengths = np.array([sum(tc.values()) for tc in token_counts], dtype=np.float32)
        avgdl = float(lengths.mean()) if n else 1.0
        tmp: dict[str, tuple[list[int], list[float]]] = {}
        for i, tc in enumerate(token_counts):
            for term, tf in tc.items():
                norm = tf * (k1 + 1) / (tf + k1 * (1 - b + b * lengths[i] / avgdl))
                ids, ws = tmp.setdefault(term, ([], []))
                ids.append(i)
                ws.append(norm)
        postings = {}
        for term, (ids, ws) in tmp.items():
            idf = math.log(1 + (n - len(ids) + 0.5) / (len(ids) + 0.5))
            postings[term] = (np.array(ids, dtype=np.int32), np.array(ws, dtype=np.float32) * idf)
        topic_cache: dict[str, set[str]] = {}
        topic_terms = [topic_cache.setdefault(c.topic, set(tokenize(c.topic))) for c in chunks]
        return cls(chunks, vectors, postings, topic_terms)

    def bm25(self, terms: list[str]) -> np.ndarray:
        scores = np.zeros(len(self.chunks), dtype=np.float32)
        for t in set(terms):
            p = self.postings.get(t)
            if p is not None:
                scores[p[0]] += p[1]
        return scores


# ---------------------------------------------------------------- embedders

def _hf_file(repo: str, filename: str) -> str:
    from huggingface_hub import hf_hub_download
    try:
        return hf_hub_download(repo, filename, local_files_only=True)  # no network round-trips when cached
    except Exception:
        return hf_hub_download(repo, filename)


class _OnnxEmbedder:
    """ONNX Runtime embedder: ~1s startup and ~12 ms/query vs ~50s / ~47 ms with torch on this machine."""

    def __init__(self, source: str | Path):
        """source: a local folder with model.onnx + tokenizer.json, or a Hugging Face repo id."""
        import onnxruntime as ort
        from tokenizers import Tokenizer

        if isinstance(source, Path):
            tok_path, model_path = source / "tokenizer.json", source / "model.onnx"
            if not model_path.exists():
                raise FileNotFoundError(model_path)
        else:
            tok_path, model_path = _hf_file(source, "tokenizer.json"), _hf_file(source, "onnx/model.onnx")
        self.tokenizer = Tokenizer.from_file(str(tok_path))
        self.tokenizer.enable_truncation(512)
        self.tokenizer.enable_padding()
        opts = ort.SessionOptions()
        opts.intra_op_num_threads = 4
        self.session = ort.InferenceSession(str(model_path), opts, providers=["CPUExecutionProvider"])
        self.input_names = {i.name for i in self.session.get_inputs()}
        self.cls_pooling = "bge" in str(source).lower()

    def encode(self, texts: list[str], batch_size: int) -> np.ndarray:
        order = sorted(range(len(texts)), key=lambda i: len(texts[i]))  # similar lengths -> less padding
        out = np.zeros((len(texts), 0), np.float32)
        parts = []
        for s in range(0, len(order), batch_size):
            enc = self.tokenizer.encode_batch([texts[i] for i in order[s:s + batch_size]])
            ids = np.array([e.ids for e in enc], dtype=np.int64)
            mask = np.array([e.attention_mask for e in enc], dtype=np.int64)
            feeds = {"input_ids": ids, "attention_mask": mask}
            if "token_type_ids" in self.input_names:
                feeds["token_type_ids"] = np.zeros_like(ids)
            hidden = self.session.run(None, feeds)[0]
            if self.cls_pooling:
                vec = hidden[:, 0]
            else:
                m = mask[..., None].astype(np.float32)
                vec = (hidden * m).sum(1) / np.clip(m.sum(1), 1e-9, None)
            parts.append(vec / np.linalg.norm(vec, axis=1, keepdims=True))
        if parts:
            stacked = np.vstack(parts).astype(np.float32)
            out = np.empty_like(stacked)
            out[order] = stacked
        return out


class _TorchEmbedder:
    """Fallback when onnxruntime isn't installed."""

    def __init__(self, repo: str):
        import torch
        from sentence_transformers import SentenceTransformer
        torch.set_num_threads(4)
        try:
            self.model = SentenceTransformer(repo, device="cpu", local_files_only=True)
        except Exception:
            self.model = SentenceTransformer(repo, device="cpu")

    def encode(self, texts: list[str], batch_size: int) -> np.ndarray:
        return np.asarray(self.model.encode(texts, batch_size=batch_size, normalize_embeddings=True,
                                            show_progress_bar=False, convert_to_numpy=True), dtype=np.float32)


# ---------------------------------------------------------------- public API

class KnowledgeBase:
    def __init__(self):
        self._lock = threading.Lock()
        self._model = None
        self._model_name = ""
        self._query_prefix = ""
        self._base: tuple[list[Chunk], np.ndarray, list[Counter]] | None = None
        self._dynamic: dict[int, tuple[list[Chunk], np.ndarray, list[Counter]]] = {}
        self._index: _Index | None = None
        self._query_cache: dict[str, np.ndarray] = {}
        self.version = 0

    # -- model
    def _load_model(self):
        # 1) the model bundled in models/ (no network), 2) Hugging Face download, 3) torch fallback.
        candidates = [(config.EMBED_MODEL_DIR.name, _OnnxEmbedder, config.EMBED_MODEL_DIR)]
        for name in dict.fromkeys([config.EMBED_MODEL, config.EMBED_FALLBACK_MODEL]):
            candidates += [(name, _OnnxEmbedder, name), (name, _TorchEmbedder, name)]
        errors = []
        for name, loader, source in candidates:
            try:
                self._model = loader(source)
                self._model_name = name
                self._query_prefix = "Represent this sentence for searching relevant passages: " if "bge" in name.lower() else ""
                log.info("Embedding model loaded: %s (%s)", name, loader.__name__)
                return
            except Exception as e:  # missing files / runtime / offline: try the next option
                errors.append(f"{name} via {loader.__name__}: {e}")
        raise RuntimeError("No embedding model could be loaded: " + " | ".join(errors))

    def _embed(self, texts: list[str], batch_size: int = 32) -> np.ndarray:
        return self._model.encode(texts, batch_size)

    # -- building
    def load(self):
        t0 = time.time()
        if self._model is None:
            self._load_model()
        chunks = load_kb_chunks()
        vectors = self._cached_vectors(chunks)
        counts = [Counter(tokenize(c.embed_text)) for c in chunks]
        with self._lock:
            self._base = (chunks, vectors, counts)
            self._rebuild()
        self.embed_query("warm up")
        log.info("Knowledge index ready: %d chunks in %.1fs", len(chunks), time.time() - t0)

    def _cached_vectors(self, chunks: list[Chunk]) -> np.ndarray:
        """Per-chunk embedding cache keyed by text hash: editing one KB file only re-embeds its changed chunks."""
        slug = re.sub(r"[^a-z0-9]+", "-", self._model_name.lower()).strip("-")
        cache = config.INDEX_CACHE_DIR / f"kb_{slug}.npz"
        keys = [hashlib.sha1(c.embed_text.encode("utf-8")).hexdigest() for c in chunks]
        stored: dict[str, np.ndarray] = {}
        if cache.exists():
            try:
                with np.load(cache, allow_pickle=False) as data:
                    stored = dict(zip(data["keys"].tolist(), data["vectors"]))
            except Exception as e:
                log.warning("Ignoring unreadable embedding cache: %s", e)
        missing = [i for i, k in enumerate(keys) if k not in stored]
        if missing:
            log.info("Embedding %d new/changed chunks (cached afterwards)...", len(missing))
            for i, vec in zip(missing, self._embed([chunks[i].embed_text for i in missing])):
                stored[keys[i]] = vec
        vectors = np.stack([stored[k] for k in keys]).astype(np.float32) if keys else np.zeros((0, 384), np.float32)
        if missing or len(stored) != len(set(keys)):
            try:
                config.INDEX_CACHE_DIR.mkdir(exist_ok=True)
                np.savez(cache, keys=np.array(keys), vectors=vectors)
            except OSError as e:  # read-only filesystem (serverless): keep the vectors in memory only
                log.warning("Could not write embedding cache (%s); commit an up-to-date cache for fast cold starts.", e)
        return vectors

    def _rebuild(self):
        parts = [self._base] + list(self._dynamic.values())
        chunks = [c for p in parts for c in p[0]]
        vectors = np.vstack([p[1] for p in parts if len(p[0])]) if chunks else np.zeros((0, 384), np.float32)
        counts = [tc for p in parts for tc in p[2]]
        self._index = _Index.build(chunks, vectors, counts)
        self.version += 1  # lets answer caches know the knowledge changed

    def upsert_document(self, doc_id: int, title: str, topic: str, content: str):
        """Index (or re-index) an admin-published document so the bot can answer from it immediately."""
        chunks = chunk_text(f"# {title}\n\n{content}", topic or title, f"db:{doc_id}", f"db{doc_id}")
        if not chunks and content.strip():
            chunks = [Chunk(f"db{doc_id}-0000", topic or title, title, content.strip(), f"db:{doc_id}")]
        vecs = self._embed([c.embed_text for c in chunks]) if chunks else np.zeros((0, self._index.vectors.shape[1]), np.float32)
        counts = [Counter(tokenize(c.embed_text)) for c in chunks]
        with self._lock:
            self._dynamic[doc_id] = (chunks, vecs, counts)
            self._rebuild()

    def remove_document(self, doc_id: int):
        with self._lock:
            if self._dynamic.pop(doc_id, None) is not None:
                self._rebuild()

    # -- querying
    @property
    def ready(self) -> bool:
        return self._index is not None

    @property
    def size(self) -> int:
        return len(self._index.chunks) if self._index else 0

    def embed_query(self, query: str) -> np.ndarray:
        key = query.strip().lower()
        vec = self._query_cache.get(key)
        if vec is None:
            vec = self._embed([self._query_prefix + query], batch_size=1)[0]
            with self._lock:
                if len(self._query_cache) >= QUERY_CACHE_SIZE:
                    self._query_cache.pop(next(iter(self._query_cache)))
                self._query_cache[key] = vec
        return vec

    def search(self, query: str, top_k: int = 5) -> list[dict]:
        """Returns the top chunks with their dense cosine score (used as a relevance signal)."""
        idx = self._index
        if idx is None or not query.strip() or not idx.chunks:
            return []
        dense = idx.vectors @ self.embed_query(_embedding_query(query))
        sparse = idx.bm25(tokenize(query))

        n = len(idx.chunks)
        c = min(CANDIDATES, n)
        def top(scores: np.ndarray) -> np.ndarray:
            cand = np.argpartition(-scores, c - 1)[:c]
            return cand[np.argsort(-scores[cand])]

        fused: dict[int, float] = {}
        for rank, i in enumerate(top(dense)):
            fused[int(i)] = fused.get(int(i), 0.0) + 1.0 / (RRF_K + rank)
        if sparse.any():
            for rank, i in enumerate(top(sparse)):
                if sparse[i] > 0:
                    fused[int(i)] = fused.get(int(i), 0.0) + 1.0 / (RRF_K + rank)

        # Boost chunks whose topic name the user mentioned ("report a profile" -> Reporting).
        q_terms = set(tokenize(query))
        if q_terms:
            for i in fused:
                t_terms = idx.topic_terms[i]
                if t_terms:
                    fused[i] += TOPIC_BOOST * len(t_terms & q_terms) / len(t_terms)

        best = sorted(fused, key=fused.get, reverse=True)[:top_k]
        return [{"chunk": idx.chunks[i], "score": float(dense[i]), "fused": fused[i]} for i in best]


kb = KnowledgeBase()
