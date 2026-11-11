import os

html_path = 'frontend/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'widget-container' in l or 'auth-container' in l or 'Sign in to' in l:
        print(f'{i}: {l.strip()}')
