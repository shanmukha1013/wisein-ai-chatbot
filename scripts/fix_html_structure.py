import os
import re

html_path = 'frontend/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# I know EXACTLY what text is left over. 
# Let's strip it completely.

to_remove = """
    <h3>Sign in to WiseIN Support</h3>
    <p>Please log in to access the AI assistant.</p>
    <input type="text" id="username" class="auth-input" placeholder="Username" />
    <input type="password" id="password" class="auth-input" placeholder="Password" />
    <button class="auth-btn" onclick="login()">Login</button>
    <div id="auth-error">Invalid credentials</div>
  </div>"""

content = content.replace(to_remove, '')

# Wait, there's another thing: the CSS for auth might be present, which is harmless but dirty. Let's remove it if we can safely.
auth_css = """    /* AUTHENTICATION UI */
    #auth-container {
      display: flex; flex-direction: column; align-items: center; justify-content: center;
      height: 100%; padding: 24px; text-align: center;
    }
    #auth-container h3 { margin-bottom: 8px; color: var(--text-dark); }
    #auth-container p { font-size: 13px; color: var(--text-muted); margin-bottom: 24px; }
    .auth-input {
      width: 100%; padding: 12px; border: 1px solid var(--border); border-radius: 8px;
      margin-bottom: 12px; font-size: 14px; outline: none;
    }
    .auth-input:focus { border-color: var(--blue); }
    .auth-btn {
      width: 100%; padding: 12px; border: none; border-radius: 8px;
      background: var(--blue); color: white; font-weight: 600; cursor: pointer;
    }
    .auth-btn:hover { background: var(--blue-dark); }
    #auth-error { color: #dc2626; font-size: 13px; margin-top: 12px; display: none; }"""

content = content.replace(auth_css, '')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Auth HTML fragments completely purged.")
