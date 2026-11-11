import os
import re

html_path = 'frontend/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the broken auth chunk
regex = re.compile(r'<h3>Sign in to WiseIN Support</h3>.*?<div id="auth-error">Invalid credentials</div>\s*</div>', re.DOTALL)
content = re.sub(regex, '', content)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Auth chunk removed using regex.")
