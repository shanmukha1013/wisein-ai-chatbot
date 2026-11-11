import sys, os, time
import requests

url = "http://localhost:8000/api/chat"

queries = [
    "how to create account",
    "how to create account in wiesin",
    "how do I sign up",
    "how do I register",
    "I want to create a new WiseIN account",
    "what is WiseIN",
    "who is Santosh",
    "how do I verify my email",
    "I didn't receive my OTP",
    "how do I login"
]

print("Testing 10 Queries for Regression and Fixes...\n")
for i, q in enumerate(queries, 1):
    print(f"--- Q{i}: {q} ---")
    req_data = {'query': q, 'history': []}
    try:
        r = requests.post(url, json=req_data, stream=True)
        content = ""
        for chunk in r.iter_content(chunk_size=None):
            if chunk:
                content += chunk.decode('utf-8')
        
        # parse the stream events to just print tokens
        text = ""
        sources = []
        for line in content.split('\\n\\n'):
            if line.startswith('data: '):
                import json
                try:
                    data = json.loads(line[6:])
                    if data.get('type') == 'token':
                        text += data.get('content', '')
                    elif data.get('type') == 'sources':
                        sources = [s['name'] for s in data.get('sources', [])]
                except:
                    pass
        print(f"Sources: {', '.join(sources)}")
        print(f"Answer: {text[:200]}...")
        if "I don't have enough information" in text:
            print("FAILED: Fallback triggered.")
    except Exception as e:
        print(f"Error: {e}")
    print()
    time.sleep(1) # don't rate limit
