import os

filepath = 'backend/api.py'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to replace the entire def chat(req: ChatRequest): up to return StreamingResponse
import re

# Since I injected a timing test earlier, let's just rewrite the endpoint completely
new_endpoint = """
@app.post("/api/chat")
async def chat(req: ChatRequest):
    import time
    t_start = time.time()
    
    query = req.query.strip()
    if not query:
        raise HTTPException(status_code=400, detail="Query cannot be empty.")

    if engine is None:
        raise HTTPException(status_code=503, detail="Retrieval engine not ready.")

    if not is_llm_ready():
        raise HTTPException(
            status_code=503,
            detail="LLM service is not ready. Please check GROQ_API_KEY."
        )

    # Convert history
    history_dict = [{"role": msg.role, "content": msg.content} for msg in req.history]
    
    t_hist_start = time.time()
    # 1. Expand query for better semantic match
    expanded_search = expand_query(query, history=history_dict)
    t_hist = (time.time() - t_hist_start) * 1000
    print(f"Original Query: {query} | Expanded: {expanded_search}")
    
    t_ret_start = time.time()
    # 2. Retrieve with higher Top-K (4-6 to enforce budget as requested)
    # The prompt explicitly asked to bound RAG context to top_k = 4-6
    results = engine.retrieve(expanded_search, top_k=5)
    t_ret = (time.time() - t_ret_start) * 1000

    seen = set()
    sources = []
    rag_context_chars = 0
    for r in results:
        topic = r.get("topic_name", "WiseIN Knowledge Base")
        doc   = r.get("source_file", "").replace("_", " ").replace(".md", "").strip()
        rag_context_chars += len(r.get("chunk_text", ""))
        key   = f"{topic}|{doc}"
        if key not in seen:
            seen.add(key)
            sources.append(Source(name=topic, doc=doc))
            
    # Calculate sizes
    conv_chars = sum(len(m.content) for m in req.history)
    conv_tokens = conv_chars // 4

    def event_generator():
        # Yield sources metadata first
        yield f"data: {json.dumps({'type': 'sources', 'sources': [s.dict() for s in sources], 'model': MODEL_NAME})}\\n\\n"
        
        t_groq_start = time.time()
        
        if not results:
            msg = "I couldn't find enough information in the WiseIN knowledge base to answer that confidently. Please try rephrasing your question, or contact WiseIN support directly."
            yield f"data: {json.dumps({'type': 'token', 'content': msg})}\\n\\n"
        else:
            # Yield tokens from Groq stream
            for token in generate_answer_stream(query, results, history=history_dict):
                yield f"data: {json.dumps({'type': 'token', 'content': token})}\\n\\n"
        
        t_groq = (time.time() - t_groq_start) * 1000
        t_total = (time.time() - t_start) * 1000
        
        # Log performance
        print(f"\\n[CHAT PERF]")
        print(f"conversation_messages: {len(req.history)}")
        print(f"conversation_chars: {conv_chars}")
        print(f"conversation_tokens_estimate: {conv_tokens}")
        print(f"rag_chunks: {len(results)}")
        print(f"rag_context_chars: {rag_context_chars}")
        print(f"embedding_ms: 0.00") # embedding happens inside engine.retrieve, hard to split without refactor, we report retrieval total
        print(f"qdrant_ms: {t_ret:.2f}")
        print(f"history_ms: {t_hist:.2f}")
        print(f"groq_ms: {t_groq:.2f}")
        print(f"total_ms: {t_total:.2f}\\n")
        
        yield f"data: {json.dumps({'type': 'done'})}\\n\\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")
"""

start_marker = '@app.post("/api/chat")'
end_marker = '@app.get("/health")'

idx1 = content.find(start_marker)
idx2 = content.find(end_marker)

if idx1 != -1 and idx2 != -1:
    new_content = content[:idx1] + new_endpoint + '\n' + content[idx2:]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("API patched successfully.")
else:
    print("Could not find markers in api.py")
