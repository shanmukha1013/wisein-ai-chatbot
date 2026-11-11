# WiseIN AI Support

AI customer-support assistant for WiseIN. It answers from the WiseIN knowledge base (`knowledge_base/`, 80 topic
files), can look at a user's screen (Screen Assist), hands off to the human support team, and has an admin console.

## Run it

```bash
pip install -r requirements.txt
python backend/api.py
```

- Chat widget: http://localhost:8000/support
- Admin console: http://localhost:8000/admin (user `admin`, password from `ADMIN_PASSWORD` in `.env`)
- Health check: http://localhost:8000/health

Configuration lives in `.env` (see `.env.example`). Only `GROQ_API_KEY` is required. If port 8000 is taken by
another program the server refuses to start and says so — set `PORT=8080` (or any free port) in `.env`.

## How it works

1. **Retrieval (local, ~3 ms).** The KB is split into ~3,700 passages and indexed in memory: semantic search
   (`bge-small-en-v1.5` via ONNX Runtime) fused with keyword search (BM25). Embeddings are cached in
   `backend/.index_cache/`; editing a KB file only re-embeds the passages that changed. No external vector DB.
2. **Answering (streamed).** The top 5 passages go to Groq (`qwen/qwen3.8-27b`, reasoning disabled for speed).
   The first words typically appear in 0.2–0.6 s.
3. **Instant paths.** Greetings/thanks, "talk to a human", and repeated first questions (answer cache) reply in
   under 20 ms without calling the model.
4. **Escalation.** Asking for a human (or the assistant handing off) shows the contact card and opens a ticket in
   the admin console. When the KB doesn't cover a question, the assistant says so and the question is listed under
   "Questions the assistant couldn't answer".

## Admin console

- **Analytics** — conversations, response speed, helpful ratings, top topics, unanswered questions.
- **Conversations** — full transcripts.
- **Support Tickets** — escalations with status (Open / In progress / Resolved) and the chat that led to them.
- **Knowledge Base** — write articles; publishing makes them answerable immediately, unpublishing removes them.
  "Reload knowledge_base folder" picks up edits to the Markdown files without a restart.

## Groq rate limits

On Groq's free tier each model allows about 8,000 tokens per minute (roughly 3–4 answers per minute per model).
The server fails over instantly between `qwen/qwen3.8-27b`, `openai/gpt-oss-120b` and `openai/gpt-oss-20b`, and
caches repeated questions, which covers light traffic. For real traffic, upgrade the Groq account to the Developer
tier; nothing in the code needs to change.

## Project layout

```
backend/    api.py (chat + screen assist), knowledge.py (retrieval), llm.py (Groq), features.py (admin API),
            auth.py, store.py (persistence), database.py / models.py (SQLite: backend/wisein.db)
frontend/   index.html (chat widget), admin.html (admin console)
knowledge_base/  80 topic files + manifest.json
scripts/    one-off scripts from the original build (PDF extraction, old Qdrant loaders); not used at runtime
```
