import urllib.request, json
req = urllib.request.Request('http://127.0.0.1:8000/api/chat', data=json.dumps({'query': 'What is WiseIN?'}).encode('utf-8'), headers={'Content-Type': 'application/json'})
try:
    resp = urllib.request.urlopen(req, timeout=10)
    for line in resp:
        if line.decode('utf-8').strip().startswith('data: {"type": "sources"'):
            print('Success!')
            break
except Exception as e:
    print('Error:', e)
