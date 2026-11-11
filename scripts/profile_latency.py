import sys
import os
import time
import json
import urllib.request
import psutil

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from retrieve import RetrievalEngine
from generate_answer import build_prompt, MODEL_NAME, OLLAMA_URL

def run_profiler():
    query = "How do I create a WiseIN account?"
    print("Initializing engine...")
    
    # Pre-load to avoid first-run penalty in measurements
    engine = RetrievalEngine(collection_name="wisein_knowledge", top_k=3)
    
    # 1. Total API call (for total and frontend-backend delta)
    print("\n--- MEASURING STAGES ---")
    
    # We will simulate the internal pipeline precisely
    
    # 2. Query embedding generation
    t0 = time.perf_counter()
    query_vector = engine.provider.embed_texts([query])[0]
    t1 = time.perf_counter()
    t_embed = t1 - t0
    
    # 3. Qdrant retrieval
    t0 = time.perf_counter()
    search_result = engine.client.query_points(
        collection_name=engine.collection_name,
        query=query_vector,
        limit=3
    ).points
    
    chunks = []
    for scored_point in search_result:
        chunks.append({
            "topic_name": scored_point.payload.get("topic_name", ""),
            "section": scored_point.payload.get("section", ""),
            "chunk_text": scored_point.payload.get("chunk_text", "")
        })
    t1 = time.perf_counter()
    t_qdrant = t1 - t0
    
    # 4. Context construction
    t0 = time.perf_counter()
    prompt = build_prompt(query, chunks)
    t1 = time.perf_counter()
    t_context = t1 - t0
    
    # 5, 6, 7. Ollama LLM
    payload = json.dumps({
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.2,
            "num_predict": 512,
            "stop": ["User question:", "User:", "\n\nUser"],
        }
    }).encode("utf-8")
    
    req = urllib.request.Request(OLLAMA_URL, data=payload, headers={"Content-Type": "application/json"}, method="POST")
    
    t0 = time.perf_counter()
    with urllib.request.urlopen(req, timeout=300) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    t1 = time.perf_counter()
    
    ns_to_s = 1e9
    t_load = data.get("load_duration", 0) / ns_to_s
    t_prompt_eval = data.get("prompt_eval_duration", 0) / ns_to_s
    t_gen = data.get("eval_duration", 0) / ns_to_s
    
    eval_count = data.get("eval_count", 0)
    tokens_per_sec = eval_count / t_gen if t_gen > 0 else 0
    
    # Now hit the actual API for total time and frontend overhead
    t0 = time.perf_counter()
    api_req = urllib.request.Request("http://127.0.0.1:8000/api/chat", data=json.dumps({"query": query}).encode("utf-8"), headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(api_req, timeout=300) as resp:
            resp.read()
        t1 = time.perf_counter()
        t_total = t1 - t0
    except Exception as e:
        print(f"API Error: {e}")
        t_total = (t_embed + t_qdrant + t_context + t_load + t_prompt_eval + t_gen)
        
    # Frontend -> backend overhead is approximately Total - Internal sums
    internal_sum = t_embed + t_qdrant + t_context + t_load + t_prompt_eval + t_gen
    t_frontend_backend = max(0.001, t_total - internal_sum)
    
    # Metrics
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory()
    
    print("\n==============================================")
    print("LATENCY REPORT")
    print("==============================================")
    print(f"1. Frontend request -> backend: {t_frontend_backend:.4f}s")
    print(f"2. Query embedding generation:  {t_embed:.4f}s")
    print(f"3. Qdrant retrieval:            {t_qdrant:.4f}s")
    print(f"4. Context construction:        {t_context:.6f}s")
    print(f"5. Ollama model loading/startup:{t_load:.4f}s")
    print(f"6. Ollama prompt processing:    {t_prompt_eval:.4f}s")
    print(f"7. Ollama token generation:     {t_gen:.4f}s")
    print("----------------------------------------------")
    print(f"8. Total response time (API):   {t_total:.4f}s")
    print("==============================================")
    print("\nSYSTEM & LLM METRICS")
    print(f"Model Name:       {MODEL_NAME}")
    print(f"Model Size:       3.8B (2.17 GB)")
    print(f"Generated Tokens: {eval_count}")
    print(f"Tokens/Second:    {tokens_per_sec:.2f}")
    print(f"CPU Usage:        {cpu_usage}%")
    print(f"RAM Usage:        {ram_usage.percent}% ({ram_usage.used / (1024**3):.1f}GB / {ram_usage.total / (1024**3):.1f}GB)")

if __name__ == '__main__':
    run_profiler()
