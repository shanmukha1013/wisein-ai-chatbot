import os
import re

# Update api.py
api_path = 'backend/api.py'
with open(api_path, 'r', encoding='utf-8') as f:
    api_content = f.read()

# Add history field to ChatRequest
req_model = """class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    query: str
    history: list[Message] = []
"""
api_content = re.sub(r'class ChatRequest\(BaseModel\):\n\s*query: str\n', req_model, api_content)

# Update generate_answer_stream call to include history
api_content = api_content.replace(
    'for token in generate_answer_stream(query, results):',
    'history_dict = [{"role": msg.role, "content": msg.content} for msg in req.history]\n            for token in generate_answer_stream(query, results, history=history_dict):'
)

with open(api_path, 'w', encoding='utf-8') as f:
    f.write(api_content)


# Update index.html
html_path = 'frontend/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Update welcome message
old_welcome = "I'm the WiseIN Support Assistant. How can I help you today?"
new_welcome = "Hi! I'm WiseIN AI Support. I can help you with WiseIN features, account issues, verification, meetings, jobs, and more.<br><br>What can I help you with?"
html_content = html_content.replace(old_welcome, new_welcome)

# Send chatHistory in fetch request
fetch_call = """const res = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: text, history: chatHistory })
      });"""
html_content = re.sub(r"const res = await fetch\('/api/chat', \{[\s\S]*?body: JSON\.stringify\(\{ query: text \}\)\s*\}\);", fetch_call, html_content)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Updated backend API and frontend for context and concise behavior.")
