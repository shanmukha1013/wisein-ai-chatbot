"""Tiny in-memory sliding-window rate limiter (per client IP) to protect the public endpoints and LLM credits."""
import threading
import time
from collections import defaultdict, deque

from fastapi import HTTPException, Request

import config


def client_ip(request: Request) -> str:
    if config.TRUST_PROXY_HEADERS:
        fwd = request.headers.get("x-forwarded-for") or request.headers.get("x-real-ip")
        if fwd:
            return fwd.split(",")[0].strip()
    return request.client.host if request.client else "unknown"


class RateLimiter:
    """Per-process limiter. On serverless each instance counts separately, which is fine as a best-effort guard."""

    def __init__(self, limit: int, window_seconds: int):
        self.limit = limit
        self.window = window_seconds
        self._hits: dict[str, deque] = defaultdict(deque)
        self._lock = threading.Lock()

    def check(self, request: Request):
        key = client_ip(request)
        now = time.monotonic()
        with self._lock:
            q = self._hits[key]
            while q and now - q[0] > self.window:
                q.popleft()
            if len(q) >= self.limit:
                raise HTTPException(status_code=429, detail="Too many requests. Please wait a moment and try again.")
            q.append(now)


chat_limiter = RateLimiter(limit=30, window_seconds=60)
screen_limiter = RateLimiter(limit=6, window_seconds=60)
login_limiter = RateLimiter(limit=10, window_seconds=300)
