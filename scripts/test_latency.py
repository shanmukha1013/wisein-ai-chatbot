import requests
import time
import json

url = "http://127.0.0.1:8000/api/chat"

history = []

for i in range(1, 21):
    req_data = {
        "query": f"Question {i}: What is WiseIN? Tell me more.",
        "history": history
    }
    
    t0 = time.time()
    try:
        # Stream the response to get full time
        with requests.post(url, json=req_data, stream=True) as r:
            content = ""
            for chunk in r.iter_content(chunk_size=None):
                if chunk:
                    content += chunk.decode('utf-8')
    except Exception as e:
        print(f"Failed at {i}: {e}")
        break
    t1 = time.time()
    
    elapsed = t1 - t0
    print(f"Q{i} (History: {len(history)} messages) -> {elapsed:.3f}s")
    
    # Fake a short bot response for history
    history.append({"role": "user", "content": f"Question {i}: What is WiseIN? Tell me more."})
    history.append({"role": "bot", "content": f"Answer {i}: WiseIN is a platform. It is very fast."})
