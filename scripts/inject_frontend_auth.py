import os

html_path = 'frontend/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add CSS for auth
auth_css = """
    /* AUTHENTICATION UI */
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
    #auth-error { color: #dc2626; font-size: 13px; margin-top: 12px; display: none; }
"""
content = content.replace('/* IN-CHAT CONFIRMATION */', auth_css + '\n    /* IN-CHAT CONFIRMATION */')

# Add Auth HTML inside widget-container, hide chat by default
auth_html = """
    <!-- AUTHENTICATION UI -->
    <div id="auth-container">
      <div class="logo">W</div>
      <h3>Sign in to WiseIN Support</h3>
      <p>Please log in to access the AI assistant.</p>
      <input type="text" id="username" class="auth-input" placeholder="Username" />
      <input type="password" id="password" class="auth-input" placeholder="Password" />
      <button class="auth-btn" onclick="login()">Login</button>
      <div id="auth-error">Invalid credentials</div>
    </div>
"""
content = content.replace('<div class="header">', auth_html + '\n    <div class="header" id="chat-header" style="display:none;">')

# Hide main components initially
content = content.replace('<div class="chat-area" id="conversation"', '<div class="chat-area" id="conversation" style="display:none;"')
content = content.replace('<div class="input-area"', '<div class="input-area" id="chat-input-area" style="display:none;"')
content = content.replace('<div class="footer"', '<div class="footer" id="chat-footer" style="display:none;"')

# Add JS logic for Auth
auth_js = """
  // Authentication Logic
  let currentUser = null;

  async function checkAuth() {
    try {
      const res = await fetch('/api/auth/me');
      if (res.ok) {
        currentUser = await res.json();
        showChat();
      } else {
        showAuth();
      }
    } catch (e) {
      showAuth();
    }
  }

  async function login() {
    const u = document.getElementById('username').value;
    const p = document.getElementById('password').value;
    const err = document.getElementById('auth-error');
    err.style.display = 'none';

    try {
      const res = await fetch('/api/auth/login', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({username: u, password: p})
      });
      if (res.ok) {
        checkAuth();
      } else {
        err.style.display = 'block';
      }
    } catch (e) {
      err.style.display = 'block';
    }
  }

  function showChat() {
    document.getElementById('auth-container').style.display = 'none';
    document.getElementById('chat-header').style.display = 'flex';
    document.getElementById('conversation').style.display = 'block';
    document.getElementById('chat-input-area').style.display = 'flex';
    document.getElementById('chat-footer').style.display = 'block';
    // ensure history runs
    loadHistory();
  }

  function showAuth() {
    document.getElementById('auth-container').style.display = 'flex';
    document.getElementById('chat-header').style.display = 'none';
    document.getElementById('conversation').style.display = 'none';
    document.getElementById('chat-input-area').style.display = 'none';
    document.getElementById('chat-footer').style.display = 'none';
  }

  // Hook into initialization
"""
content = content.replace('loadHistory();', auth_js + '\n    checkAuth();')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Frontend auth updated.")
