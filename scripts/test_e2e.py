import urllib.request
import json
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

questions = [
    "What is WiseIN?",
    "How do I create a WiseIN account?",
    "How do I log in?",
    "How do I verify my identity?",
    "How do I update my profile?",
    "How can I find jobs?",
    "How do I connect with other people?",
    "How do I book a meeting?",
    "Why am I not receiving my OTP?",
    "How do I delete my account?",
    "What is AI Search?",
    "What does the WiseIN AI Assistant do?",
    "How do I verify?", # Ambiguous
    "How do I trade stocks on WiseIN?", # Unsupported WiseIN
    "What is the weather today?" # Unrelated
]

url = "http://127.0.0.1:8000/api/chat"

print("Starting End-to-End API Test...\n")
for idx, q in enumerate(questions, 1):
    print(f"[{idx}/15] Q: {q}")
    data = json.dumps({"query": q}).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    try:
        t0 = time.time()
        resp = urllib.request.urlopen(req, timeout=300)
        t1 = time.time()
        result = json.loads(resp.read().decode())
        print(f"Time: {t1-t0:.1f}s")
        print(f"A: {result.get('answer')}")
        sources = [s['name'] for s in result.get('sources', [])]
        print(f"Sources: {sources}")
    except Exception as e:
        print(f"Error: {e}")
    print("-" * 50)
