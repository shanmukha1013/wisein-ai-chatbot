import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'scripts'))
from retrieve import RetrievalEngine
engine = RetrievalEngine()
results = engine.retrieve('Who is Santosh?', top_k=5)
for r in results:
    print(f"Score: {r['score']:.4f} | Topic: {r['topic_name']}")
    print(f"Text: {r['chunk_text'][:300]}")
    print("-" * 50)
