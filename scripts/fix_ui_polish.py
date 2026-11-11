import os
import re

html_path = 'frontend/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# ---------------------------------------------------------
# 1. FIX THE BLUE RECTANGLE OUTLINE ISSUE
# ---------------------------------------------------------
# We will replace `button:focus-visible, textarea:focus-visible, a:focus-visible`
# with just `button:focus-visible, a:focus-visible`
content = content.replace(
    'button:focus-visible, textarea:focus-visible, a:focus-visible { outline: 2px solid var(--blue); outline-offset: 2px; }',
    'button:focus-visible, a:focus-visible { outline: 2px solid var(--blue); outline-offset: 2px; }'
)
# Add explicit rule for textarea just in case
content = content.replace(
    'textarea { font-family: var(--font); }',
    'textarea { font-family: var(--font); }\n    textarea:focus, textarea:focus-visible { outline: none !important; box-shadow: none !important; }'
)


# ---------------------------------------------------------
# 2. ADD CSS FOR IN-CHAT CONFIRMATION CARD
# ---------------------------------------------------------
confirm_css = """
    /* IN-CHAT CONFIRMATION */
    .confirm-overlay {
      position: absolute; top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(248, 250, 252, 0.85); backdrop-filter: blur(2px);
      display: flex; align-items: center; justify-content: center;
      z-index: 100; padding: 20px;
      opacity: 0; pointer-events: none; transition: opacity 0.2s ease;
    }
    .confirm-overlay.visible { opacity: 1; pointer-events: auto; }
    .confirm-card {
      background: var(--white); border: 1px solid var(--border);
      border-radius: 16px; padding: 24px; text-align: center;
      box-shadow: 0 10px 25px rgba(0,0,0,0.05);
      transform: translateY(10px) scale(0.95); transition: transform 0.2s cubic-bezier(0.2, 0.8, 0.2, 1);
      width: 100%; max-width: 300px;
    }
    .confirm-overlay.visible .confirm-card { transform: translateY(0) scale(1); }
    .confirm-card h4 { font-size: 16px; color: var(--text-dark); margin-bottom: 8px; font-weight: 600; }
    .confirm-card p { font-size: 13px; color: var(--text-muted); margin-bottom: 20px; line-height: 1.5; }
    .confirm-actions { display: flex; gap: 10px; justify-content: center; }
    .confirm-actions button { flex: 1; padding: 10px 16px; border-radius: 10px; font-size: 13px; font-weight: 500; transition: all 0.2s; }
    .btn-cancel { background: var(--white); border: 1px solid var(--border); color: var(--text-mid); }
    .btn-cancel:hover { background: #f8fafc; color: var(--text-dark); }
    .btn-confirm { background: var(--blue); border: 1px solid var(--blue-dark); color: var(--white); }
    .btn-confirm:hover { background: var(--blue-dark); }
"""
# Insert CSS before </style>
content = content.replace('</style>', confirm_css + '\n  </style>')


# ---------------------------------------------------------
# 3. ADD HTML FOR IN-CHAT CONFIRMATION CARD
# ---------------------------------------------------------
confirm_html = """
      <div id="confirm-overlay" class="confirm-overlay">
        <div class="confirm-card">
          <h4>Start a new conversation?</h4>
          <p>Your current conversation will be cleared and you'll start with a fresh chat.</p>
          <div class="confirm-actions">
            <button class="btn-cancel" onclick="closeConfirm()">Cancel</button>
            <button class="btn-confirm" onclick="executeClearChat()">Start New Chat</button>
          </div>
        </div>
      </div>
"""
# Insert inside <div class="chat-area"> after welcome-msg
content = content.replace(
    '<button class="scroll-btn" id="scrollBtn" onclick="forceScrollBottom()">↓ New message</button>',
    '<button class="scroll-btn" id="scrollBtn" onclick="forceScrollBottom()">↓ New message</button>\n' + confirm_html
)


# ---------------------------------------------------------
# 4. REPLACE JS window.confirm() LOGIC
# ---------------------------------------------------------
old_js = """  function clearChatConfirm() {
    if (!chatStarted || chatHistory.length === 0) return;
    if (confirm("Start a new conversation?")) {
      chatHistory = []; saveHistory();
      document.querySelectorAll('.msg-row').forEach(m => m.remove());
      chatStarted = false; welcomeEl.style.display = 'block';
      hideTyping(); busy = false; inputEl.value = ''; onInput(inputEl); inputEl.disabled = false;
    }
  }"""

new_js = """  function clearChatConfirm() {
    if (!chatStarted || chatHistory.length === 0) return;
    document.getElementById('confirm-overlay').classList.add('visible');
  }

  function closeConfirm() {
    document.getElementById('confirm-overlay').classList.remove('visible');
  }

  function executeClearChat() {
    chatHistory = []; saveHistory();
    document.querySelectorAll('.msg-row').forEach(m => m.remove());
    chatStarted = false; welcomeEl.style.display = 'block';
    hideTyping(); busy = false; inputEl.value = ''; onInput(inputEl); inputEl.disabled = false;
    closeConfirm();
    document.getElementById('streaming-escalation')?.remove();
  }"""

content = content.replace(old_js, new_js)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("UI Polish Fixed: Removed blue focus outline and native confirm popup.")
