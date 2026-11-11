"""Convenience launcher. The backend serves everything: the chat UI (/support), the admin console (/admin)
and the API. This used to start a UI-only server whose chat could not work, so it now starts the real one."""
import os
import runpy
import sys

BACKEND = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "backend")
sys.path.insert(0, BACKEND)
os.chdir(BACKEND)
runpy.run_path(os.path.join(BACKEND, "api.py"), run_name="__main__")
