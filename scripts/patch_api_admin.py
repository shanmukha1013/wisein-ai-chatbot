import os

with open('backend/api.py', 'r', encoding='utf-8') as f:
    content = f.read()

admin_route = """@app.get("/admin", response_class=HTMLResponse)
async def serve_admin():
    html_path = os.path.join(os.path.dirname(__file__), '..', 'frontend', 'admin.html')
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"<h1>Error loading Admin UI</h1><p>{e}</p>"
"""

if '@app.get("/admin", response_class=HTMLResponse)' not in content:
    content = content.replace(
        '@app.get("/support", response_class=HTMLResponse)',
        admin_route + '\n@app.get("/support", response_class=HTMLResponse)'
    )
    with open('backend/api.py', 'w', encoding='utf-8') as f:
        f.write(content)
