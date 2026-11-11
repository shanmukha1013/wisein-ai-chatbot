import sys, os
sys.path.insert(0, 'backend')
sys.path.insert(0, 'scripts')
from retrieve import RetrievalEngine

print("Initializing Retrieval Engine...")
engine = RetrievalEngine('wisein_knowledge')

queries = [
    "how to create account",
    "how to create account in wiesin",
    "sign up",
    "register WiseIN"
]

for q in queries:
    print(f"\n--- QUERY: {q} ---")
    results = engine.retrieve(q, top_k=10)
    for i, r in enumerate(results):
        score = r.get("score", 0)
        topic = r.get("topic_name", "Unknown")
        text = r.get("chunk_text", "").replace('\n', ' ')
        print(f"[{i}] {score:.4f} | {topic} | {text[:100]}...")
