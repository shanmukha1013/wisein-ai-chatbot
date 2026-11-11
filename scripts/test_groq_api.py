import sys
import json
import urllib.request
import time

sys.stdout.reconfigure(encoding='utf-8')

# Wait for API to be healthy
print("Waiting for API to start...")
while True:
    try:
        resp = urllib.request.urlopen("http://127.0.0.1:8000/health", timeout=2)
        if resp.status == 200:
            print("API is healthy!")
            break
    except Exception:
        pass
    time.sleep(1)

questions = [
    "What is WiseIN?",
    "How do I create a WiseIN account?",
    "How do I verify my identity?",
    "How do I update my profile?",
    "How can I find jobs?",
    "How do I book a meeting?",
    "How do I delete my account?",
    "Why am I not receiving my OTP?",
    "What is the capital of France?"  # Out of bounds
]

print("\nRunning E2E Groq streaming tests...")

for q in questions:
    print(f"\nQ: {q}")
    req = urllib.request.Request(
        "http://127.0.0.1:8000/api/chat",
        data=json.dumps({"query": q}).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    
    t0 = time.perf_counter()
    try:
        resp = urllib.request.urlopen(req, timeout=30)
        t_first = None
        full_ans = ""
        sources = []
        for line in resp:
            line = line.decode("utf-8").strip()
            if line.startswith("data: "):
                data_str = line[6:]
                try:
                    data = json.loads(data_str)
                    if data.get("type") == "sources":
                        sources = [s["name"] for s in data.get("sources", [])]
                    elif data.get("type") == "token":
                        if t_first is None:
                            t_first = time.perf_counter()
                        full_ans += data["content"]
                except json.JSONDecodeError:
                    pass
        
        t_end = time.perf_counter()
        ttft = (t_first - t0) if t_first else 0
        total = t_end - t0
        
        print(f"TTFT: {ttft:.3f}s | Total: {total:.3f}s")
        print(f"Sources: {sources}")
        print(f"A: {full_ans.strip()[:150]}...")
        if "capital" in q:
            print(f"Full out-of-bounds answer: {full_ans.strip()}")
            
    except Exception as e:
        print(f"Failed: {e}")
