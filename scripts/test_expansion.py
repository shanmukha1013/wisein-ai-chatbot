import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'scripts'))
from retrieve import RetrievalEngine
from generate_answer import expand_query

engine = RetrievalEngine()
query = "Who is Santosh?"
expanded = expand_query(query)
print(f"Original: {query}")
print(f"Expanded: {expanded}")

results = engine.retrieve(expanded, top_k=8)
for r in results:
    print(f"Score: {r['score']:.4f} | Topic: {r['topic_name']}")
    print(f"Text: {r['chunk_text'][:200]}")
    print("-" * 50)
