"""Vercel entry point: exposes the FastAPI app from backend/api.py (chat, screen assist, admin, pages).

backend/api.py is loaded under a unique module name so it can't collide with this `api/` folder."""
import importlib.util
import sys
from pathlib import Path

BACKEND = Path(__file__).resolve().parent.parent / "backend"
sys.path.insert(0, str(BACKEND))

_spec = importlib.util.spec_from_file_location("wisein_backend_api", BACKEND / "api.py")
_module = importlib.util.module_from_spec(_spec)
sys.modules["wisein_backend_api"] = _module
_spec.loader.exec_module(_module)

app = _module.app
