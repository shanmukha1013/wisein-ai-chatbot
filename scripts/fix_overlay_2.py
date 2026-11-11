import os

html_path = 'frontend/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the CSS z-index
content = content.replace('z-index: 100; padding: 20px;', 'z-index: 10000; padding: 20px;')

# Remove the overly strict block in clearChatConfirm
# Let it trigger even if they just clicked it, but if nothing is there, just clear gracefully.
old_js = """  function clearChatConfirm() {
    if (!chatStarted || chatHistory.length === 0) return;
    document.getElementById('confirm-overlay').classList.add('visible');
  }"""
new_js = """  function clearChatConfirm() {
    document.getElementById('confirm-overlay').classList.add('visible');
  }"""
content = content.replace(old_js, new_js)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("CSS and JS fixed for the overlay button.")
