import os
import re

api_path = 'backend/api.py'
with open(api_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add dependencies and router
import_replacement = """from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, StreamingResponse
from pydantic import BaseModel
import uvicorn

from retrieve import RetrievalEngine
from generate_answer import generate_answer_stream, expand_query, is_llm_ready, MODEL_NAME

from auth import router as auth_router, get_current_user
from models import User
"""

content = content.replace(
    'from fastapi import FastAPI, HTTPException, Request\nfrom fastapi.middleware.cors import CORSMiddleware\nfrom fastapi.responses import HTMLResponse, StreamingResponse\nfrom pydantic import BaseModel\nimport uvicorn\n\nfrom retrieve import RetrievalEngine\nfrom generate_answer import generate_answer_stream, expand_query, is_llm_ready, MODEL_NAME',
    import_replacement
)

# Register router
router_replacement = """app = FastAPI(title="WiseIN AI Support API", version="8.0")

app.include_router(auth_router)
"""

content = content.replace('app = FastAPI(title="WiseIN AI Support API", version="8.0")', router_replacement)

# Protect the chat route
route_replacement = """@app.post("/api/chat")
async def chat(req: ChatRequest, current_user: User = Depends(get_current_user)):
"""

content = content.replace('@app.post("/api/chat")\nasync def chat(req: ChatRequest):', route_replacement)

with open(api_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Auth integrated into api.py successfully.")
