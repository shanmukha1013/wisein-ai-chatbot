"""Central configuration. Loads the project-root .env once, before anything else reads env vars.
Works both locally and on Vercel (where settings come from the project's Environment Variables)."""
import os
import secrets
import logging
from pathlib import Path

from dotenv import load_dotenv

BACKEND_DIR = Path(__file__).resolve().parent
ROOT_DIR = BACKEND_DIR.parent
FRONTEND_DIR = ROOT_DIR / "frontend"
KB_DIR = ROOT_DIR / "knowledge_base"
INDEX_CACHE_DIR = BACKEND_DIR / ".index_cache"
# Quantized (int8) bge-small embedding model shipped with the code: no download at startup, 34 MB.
EMBED_MODEL_DIR = ROOT_DIR / "models" / "bge-small-en-v1.5-int8"

load_dotenv(ROOT_DIR / ".env")

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
log = logging.getLogger("wisein.config")

ON_VERCEL = bool(os.environ.get("VERCEL"))

GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "").strip()

# Primary chat model (multimodal, so it also powers Screen Assist) plus fallbacks that take over instantly
# when the primary is rate-limited or down. Each Groq model has its own per-minute token quota.
LLM_MODEL = os.environ.get("LLM_MODEL", "qwen/qwen3.8-27b")
LLM_FALLBACK_MODELS = [m.strip() for m in os.environ.get(
    "LLM_FALLBACK_MODELS", "openai/gpt-oss-120b,openai/gpt-oss-20b").split(",") if m.strip()]
VISION_MODEL = os.environ.get("VISION_MODEL", LLM_MODEL)

# Used only if the bundled model folder is missing (downloaded from Hugging Face).
EMBED_MODEL = os.environ.get("EMBED_MODEL", "BAAI/bge-small-en-v1.5")
EMBED_FALLBACK_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Postgres in production (Vercel/Neon set DATABASE_URL or POSTGRES_URL); SQLite file locally.
DATABASE_URL = (os.environ.get("DATABASE_URL") or os.environ.get("POSTGRES_URL") or "").strip()

JWT_SECRET = os.environ.get("JWT_SECRET", "").strip()
if not JWT_SECRET:
    JWT_SECRET = secrets.token_urlsafe(48)
    log.warning("JWT_SECRET is not set; using a random one (admin logins reset on restart%s).",
                " and won't work across serverless instances" if ON_VERCEL else "")

ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "").strip()
COOKIE_SECURE = os.environ.get("COOKIE_SECURE", "true" if ON_VERCEL else "false").lower() == "true"
# Behind Vercel's proxy the visitor IP is in X-Forwarded-For; only trust it when actually behind a proxy.
TRUST_PROXY_HEADERS = os.environ.get("TRUST_PROXY_HEADERS", "true" if ON_VERCEL else "false").lower() == "true"

PORT = int(os.environ.get("PORT", "8000"))

SUPPORT_EMAIL = "support@wisein.in"
SUPPORT_PHONE = "+91 8008656641"
