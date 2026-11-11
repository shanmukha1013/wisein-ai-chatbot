import os
import re

html_path = 'frontend/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the hidden styles from the main UI
content = content.replace('<div class="header" id="chat-header" style="display:none;">', '<div class="header" id="chat-header">')
content = content.replace('<div class="chat-area" id="conversation" style="display:none;"', '<div class="chat-area" id="conversation"')
content = content.replace('<div class="input-area" id="chat-input-area" style="display:none;">', '<div class="input-area" id="chat-input-area">')
content = content.replace('<div class="footer" id="chat-footer" style="display:none;">', '<div class="footer" id="chat-footer">')

# 2. Remove the auth-container block
auth_container_regex = re.compile(r'<!-- AUTHENTICATION UI -->\s*<div id="auth-container">.*?</div>', re.DOTALL)
content = re.sub(auth_container_regex, '', content)

# 3. Remove auth JS logic
auth_js_regex = re.compile(r'// Authentication Logic.*?function showAuth\(\) \{.*?\}', re.DOTALL)
content = re.sub(auth_js_regex, '', content)

# Restore standard initialization
content = content.replace('    checkAuth();\n', '    loadHistory();\n')
content = content.replace('    checkAuth();', '    loadHistory();')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Frontend login wall fully removed.")
