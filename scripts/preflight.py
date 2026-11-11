import os, sys, json
sys.stdout.reconfigure(encoding='utf-8')
from qdrant_client import QdrantClient

base_dir = r'c:\Users\marel\OneDrive\Desktop\wisein-ai-support'
env_path = os.path.join(base_dir, '.env')
with open(env_path, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith('#') and '=' in line:
            k, v = line.split('=', 1)
            os.environ[k] = v.strip().strip('"\'')

sys.path.insert(0, os.path.join(base_dir, 'scripts'))
from retrieve import RetrievalEngine

print("\n--- 1. KB Topics Check ---")
kb_dir = os.path.join(base_dir, 'knowledge_base')
kb_files = [f for f in os.listdir(kb_dir) if f.endswith('.md') and f != 'README.md']
print(f'KB topics count: {len(kb_files)} (Expected 80)')

print("\n--- 2 & 3. Local Chunks Check ---")
jsonl_file = os.path.join(base_dir, 'temp_embeddings_local.jsonl')
with open(jsonl_file, 'r', encoding='utf-8') as f:
    chunks = [json.loads(line) for line in f if line.strip()]
print(f'Chunk dataset count: {len(chunks)} (Expected 2335)')

dims = [len(c.get('vector', [])) for c in chunks]
valid_dims = all(d == 384 for d in dims)
print(f'All vectors 384-dimensional: {valid_dims}')

print("\n--- 4 & 5. Qdrant Verification ---")
client = QdrantClient(url=os.environ['QDRANT_URL'], api_key=os.environ['QDRANT_API_KEY'])
collections = client.get_collections().collections
exists = any(c.name == 'wisein_knowledge' for c in collections)
print(f'Qdrant collection exists: {exists}')
if exists:
    count = client.count('wisein_knowledge').count
    print(f'Qdrant precise point count: {count} (Expected 2335)')

print("\n--- 6, 7, 8 & 9. Retrieval Test ---")
engine = RetrievalEngine()
print(f'Engine model: {engine.embedding_provider.model_name}')

test_queries = [
    "How do I create a WiseIN account?",
    "How do I log in to WiseIN?",
    "How do I verify my identity?",
    "How do I update my profile?",
    "How can I find jobs?",
    "How do I connect with other people?",
    "How do I book a meeting?",
    "How do I delete my account?"
]

for q in test_queries:
    print(f"\nQuery: {q}")
    res = engine.retrieve(q, top_k=2)
    for i, r in enumerate(res):
        print(f"  [{i+1}] Score: {r['score']:.4f} | Topic: {r['payload'].get('topic_name')} | Source: {r['payload'].get('source_file')}")
        text = r['payload'].get('chunk_text', '').replace('\n', ' ')
        print(f"      Text: {text[:80]}...")
