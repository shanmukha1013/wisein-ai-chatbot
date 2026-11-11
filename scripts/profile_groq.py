import sys
import os
import time

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from retrieve import RetrievalEngine
from generate_answer import build_prompt, client, MODEL_NAME

def run_profiler():
    query = "How do I create a WiseIN account?"
    print("Initializing engine...")
    
    engine = RetrievalEngine(collection_name="wisein_knowledge", top_k=3)
    
    print("\n--- MEASURING STAGES ---")
    
    # 1. Query embedding generation
    t0 = time.perf_counter()
    query_vector = engine.provider.embed_texts([query])[0]
    t1 = time.perf_counter()
    t_embed = t1 - t0
    
    # 2. Qdrant retrieval
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
    
    # 3. Context construction
    t0 = time.perf_counter()
    prompt = build_prompt(query, chunks)
    t1 = time.perf_counter()
    t_context = t1 - t0
    
    # 4. Groq LLM (Streaming TTFT)
    t0 = time.perf_counter()
    stream = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model=MODEL_NAME,
        temperature=0.2,
        max_tokens=512,
        stream=True,
        stop=["User question:", "User:", "\n\nUser"]
    )
    
    first_token_time = None
    tokens = 0
    full_answer = ""
    for chunk in stream:
        if first_token_time is None:
            first_token_time = time.perf_counter()
        
        content = chunk.choices[0].delta.content
        if content is not None:
            full_answer += content
            tokens += 1
            
    t1 = time.perf_counter()
    
    t_groq_ttft = first_token_time - t0 if first_token_time else 0
    t_groq_total = t1 - t0
    t_total = t_embed + t_qdrant + t_context + t_groq_total
    
    ttft_total = t_embed + t_qdrant + t_context + t_groq_ttft
    
    print("\n==============================================")
    print("GROQ LATENCY REPORT")
    print("==============================================")
    print(f"1. Query embedding generation:  {t_embed:.4f}s")
    print(f"2. Qdrant retrieval:            {t_qdrant:.4f}s")
    print(f"3. Context construction:        {t_context:.6f}s")
    print(f"4. Groq TTFT (Time to 1st tok): {t_groq_ttft:.4f}s")
    print(f"5. Groq full generation time:   {t_groq_total:.4f}s")
    print("----------------------------------------------")
    print(f"-> TOTAL TTFT (App felt delay): {ttft_total:.4f}s")
    print(f"-> TOTAL FULL RESPONSE TIME:    {t_total:.4f}s")
    print("==============================================")
    print(f"Model Name:       {MODEL_NAME}")
    print(f"Generated Tokens: {tokens}")
    if t_groq_total > t_groq_ttft:
        print(f"Tokens/Second:    {tokens / (t_groq_total - t_groq_ttft):.2f}")

if __name__ == '__main__':
    run_profiler()
