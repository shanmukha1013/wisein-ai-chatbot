import os
import re

# ==========================================
# 1. UPDATE generate_answer.py (Premium Prompt)
# ==========================================

new_prompt = '''SYSTEM_PROMPT = """You are the official WiseIN AI Support Assistant.
You act like a real, helpful human support agent, NOT a robotic documentation reader.

CORE PRINCIPLES:
1. Be concise, friendly, and natural. Provide the minimum information required to successfully help the user.
2. Maintain conversation context. Understand what the user already tried (e.g., if they say "it's not working", know they mean the previous steps).
3. Do not force numbered lists unless you are explaining a specific step-by-step procedure.
4. For simple factual questions, reply in 1-3 natural sentences.
5. For troubleshooting, give the 3-5 most relevant steps first. Do not dump the entire document.
6. Never invent WiseIN features, policies, or workflows. Use ONLY the provided excerpts.

HUMAN ESCALATION (CRITICAL):
If the user explicitly requests a human, customer care, a representative, or expresses that troubleshooting failed (e.g., "still not working", "I tried everything"), DO NOT troubleshoot further.
Respond EXACTLY with:
"Absolutely. I can help you reach the WiseIN support team. You can contact them directly using the options below."
(The system will automatically attach the contact card).

FORMATTING & TONE:
- Use natural language: "Got it.", "Let's fix that.", "Creating an account is simple:"
- Use bold for UI elements (e.g., **Profile**).
- Use clean numbered lists (1., 2., 3.) ONLY for sequential procedures.
- Never expose internal terms (Qdrant, chunks, embeddings, vector).
- If the excerpts lack the answer, say: "I don't have enough information to give you a reliable answer to that. Would you like me to help you contact WiseIN Support?"
"""
'''

with open('scripts/generate_answer.py', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('SYSTEM_PROMPT = """')
if start_idx != -1:
    end_idx = content.find('"""\n', start_idx) + 4
    content = content[:start_idx] + new_prompt + content[end_idx:]
    with open('scripts/generate_answer.py', 'w', encoding='utf-8') as f:
        f.write(content)
        
# ==========================================
# 2. UPDATE index.html (Premium UI & Accessibility)
# ==========================================
HTML_CONTENT = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>WiseIN - AI Support</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/dompurify/dist/purify.min.js"></script>
  <style>
    /* PREMIUM DESIGN TOKENS */
    :root {
      --blue:        #2F80ED;
      --blue-dark:   #1a65c5;
      --blue-light:  #eff6ff;
      --white:       #FFFFFF;
      --bg:          #F8FAFC;
      --text-dark:   #0f172a;
      --text-mid:    #334155;
      --text-muted:  #64748b;
      --border:      #e2e8f0;
      --shadow-widget: 0 20px 40px rgba(0,0,0,0.08), 0 8px 16px rgba(0,0,0,0.04);
      --shadow-launcher: 0 8px 24px rgba(47,128,237,0.25);
      --font:        'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    
    body {
      font-family: var(--font);
      background: #e2e8f0;
      height: 100vh;
      overflow: hidden;
      color: var(--text-dark);
      -webkit-font-smoothing: antialiased;
    }

    button { cursor: pointer; border: none; background: none; font-family: var(--font); }
    button:focus-visible, textarea:focus-visible, a:focus-visible { outline: 2px solid var(--blue); outline-offset: 2px; }
    textarea { font-family: var(--font); }
    ::-webkit-scrollbar { width: 5px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 10px; }
    ::-webkit-scrollbar-thumb:hover { background: #94a3b8; }

    /* PREMIUM ANIMATIONS */
    @keyframes slideUpFadeIn {
      from { opacity: 0; transform: translateY(12px); }
      to { opacity: 1; transform: translateY(0); }
    }
    @keyframes pulseSoft {
      0% { box-shadow: 0 0 0 0 rgba(47, 128, 237, 0.4); }
      70% { box-shadow: 0 0 0 10px rgba(47, 128, 237, 0); }
      100% { box-shadow: 0 0 0 0 rgba(47, 128, 237, 0); }
    }

    /* LAUNCHER BUTTON */
    .w-launcher {
      position: fixed;
      width: 60px; height: 60px;
      background: var(--white);
      border-radius: 50%;
      box-shadow: var(--shadow-launcher);
      display: flex; align-items: center; justify-content: center;
      cursor: grab; z-index: 10000;
      transition: transform 0.25s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.2s ease;
      user-select: none; touch-action: none;
      animation: pulseSoft 3s infinite;
    }
    .w-launcher:hover { transform: scale(1.05); }
    .w-launcher:active { cursor: grabbing; transform: scale(0.95); }
    .w-launcher svg { width: 28px; height: 24px; pointer-events: none; }

    /* WIDGET CONTAINER */
    .widget-container {
      position: fixed;
      width: 440px; min-width: 320px;
      height: 680px; min-height: 400px;
      max-width: calc(100vw - 40px); max-height: calc(100vh - 40px);
      background: var(--white);
      border-radius: 20px;
      box-shadow: var(--shadow-widget);
      border: 1px solid var(--border);
      display: flex; flex-direction: column;
      overflow: hidden; z-index: 9999; resize: both;
      
      opacity: 0; transform: scale(0.96) translateY(15px); pointer-events: none;
      transition: opacity 0.25s ease, transform 0.25s cubic-bezier(0.2, 0.8, 0.2, 1);
    }
    .widget-container.open { opacity: 1; transform: scale(1) translateY(0); pointer-events: auto; }

    @media (max-width: 500px) {
      .widget-container {
        width: calc(100vw - 20px) !important; height: calc(100vh - 20px) !important;
        left: 10px !important; bottom: 10px !important; top: 10px !important; right: auto !important;
        border-radius: 16px; resize: none;
      }
    }

    /* HEADER */
    .header {
      display: flex; align-items: center; justify-content: space-between;
      padding: 16px 20px; background: var(--white);
      border-bottom: 1px solid var(--border); flex-shrink: 0; cursor: grab;
    }
    .header:active { cursor: grabbing; }

    .header-left { display: flex; align-items: center; gap: 12px; }
    .header-icon {
      width: 36px; height: 36px; background: var(--blue-light); border: 1px solid #dbeafe;
      border-radius: 50%; display: flex; align-items: center; justify-content: center;
    }
    .header-icon svg { width: 18px; height: 16px; }

    .header-info { display: flex; flex-direction: column; gap: 2px; }
    .header-title { font-size: 15px; font-weight: 600; color: var(--text-dark); display: flex; align-items: center; gap: 6px; line-height: 1.1; }
    .status-dot { width: 6px; height: 6px; border-radius: 50%; background: #10b981; }
    .header-subtitle { font-size: 12px; color: var(--text-muted); font-weight: 400; }

    .header-actions { display: flex; align-items: center; gap: 12px; color: var(--text-muted); }
    .header-actions button {
      display: flex; align-items: center; justify-content: center;
      width: 30px; height: 30px; border-radius: 8px;
      color: var(--text-muted); transition: all 0.2s;
    }
    .header-actions button:hover { background: #f1f5f9; color: var(--text-dark); }
    .header-actions svg { width: 16px; height: 16px; pointer-events: none; }

    /* CHAT AREA */
    .chat-area {
      flex: 1; overflow-y: auto; overflow-x: hidden;
      padding: 24px 20px; display: flex; flex-direction: column; gap: 20px;
      background: var(--bg); position: relative; scroll-behavior: smooth;
    }

    .welcome-msg { text-align: center; margin-bottom: 10px; animation: slideUpFadeIn 0.4s ease forwards; }
    .welcome-msg h3 { font-size: 16px; margin-bottom: 8px; color: var(--text-dark); font-weight: 600; }
    .welcome-msg p { font-size: 14px; color: var(--text-mid); margin-bottom: 20px; line-height: 1.5; }

    .suggestions { display: flex; flex-direction: column; gap: 8px; align-items: center; }
    .suggestion-chip {
      background: var(--white); border: 1px solid var(--border); color: var(--text-mid);
      font-size: 13px; font-weight: 500; padding: 10px 16px; border-radius: 20px;
      box-shadow: 0 1px 2px rgba(0,0,0,0.02); transition: all 0.2s cubic-bezier(0.2, 0.8, 0.2, 1);
      width: 100%; max-width: 300px; text-align: left; position: relative;
    }
    .suggestion-chip:hover {
      background: var(--white); border-color: var(--blue); color: var(--blue);
      transform: translateY(-1px); box-shadow: 0 4px 12px rgba(47,128,237,0.1);
    }
    .suggestion-chip::after { content: '→'; position: absolute; right: 16px; opacity: 0; transition: opacity 0.2s, transform 0.2s; transform: translateX(-5px); }
    .suggestion-chip:hover::after { opacity: 1; transform: translateX(0); }

    .msg-row { display: flex; align-items: flex-start; gap: 10px; max-width: 92%; animation: slideUpFadeIn 0.3s ease forwards; }
    .msg-row.user-row { align-self: flex-end; flex-direction: row-reverse; }

    .avatar {
      width: 30px; height: 30px; border-radius: 50%;
      display: flex; align-items: center; justify-content: center; flex-shrink: 0;
    }
    .avatar-bot { background: var(--blue-light); border: 1px solid #bfdbfe; }
    .avatar-bot svg { width: 15px; height: 13px; }
    .avatar-user { background: var(--blue); }
    .avatar-user svg { width: 14px; height: 14px; }

    .bubble-col { display: flex; flex-direction: column; gap: 6px; width: 100%; }
    .bubble-bot, .bubble-user {
      padding: 12px 16px; border-radius: 16px; font-size: 14px; line-height: 1.5; word-wrap: break-word;
    }
    .bubble-bot { background: var(--white); color: var(--text-dark); border: 1px solid var(--border); border-top-left-radius: 4px; box-shadow: 0 1px 2px rgba(0,0,0,0.02); }
    .bubble-user { background: var(--blue); color: var(--white); border-top-right-radius: 4px; box-shadow: 0 2px 4px rgba(47,128,237,0.2); }
    .bubble-error { background: #fef2f2; color: #991b1b; border: 1px solid #fca5a5; }

    /* PREMIUM MARKDOWN STYLES */
    .bubble-bot p { margin-bottom: 0.75em; }
    .bubble-bot p:last-child { margin-bottom: 0; }
    .bubble-bot strong { font-weight: 600; color: #0f172a; }
    .bubble-bot em { font-style: italic; }
    .bubble-bot ul { margin-left: 1.2em; margin-bottom: 0.75em; list-style-type: disc; }
    .bubble-bot ol { margin-left: 1.2em; margin-bottom: 0.75em; list-style-type: decimal; }
    .bubble-bot li { margin-bottom: 0.35em; padding-left: 0.2em; }
    .bubble-bot li:last-child { margin-bottom: 0; }
    .bubble-bot h1, .bubble-bot h2, .bubble-bot h3 { font-size: 1.05em; font-weight: 600; margin: 1em 0 0.5em 0; color: var(--text-dark); }
    .bubble-bot h1:first-child, .bubble-bot h2:first-child, .bubble-bot h3:first-child { margin-top: 0; }
    .bubble-bot code { background: #f1f5f9; padding: 2px 5px; border-radius: 4px; font-family: ui-monospace, monospace; font-size: 0.9em; color: #db2777; }
    .bubble-bot a { color: var(--blue); text-decoration: none; font-weight: 500; }
    .bubble-bot a:hover { text-decoration: underline; }

    /* BOT ACTIONS */
    .bot-actions-row { display: flex; align-items: center; flex-wrap: wrap; gap: 6px; margin-top: 2px; }
    
    .sources-btn, .action-btn {
      display: inline-flex; align-items: center; gap: 6px;
      background: var(--white); border: 1px solid var(--border);
      padding: 6px 12px; border-radius: 20px;
      font-size: 12px; font-weight: 500; color: var(--text-mid);
      transition: all 0.2s; box-shadow: 0 1px 2px rgba(0,0,0,0.02);
    }
    .sources-btn:hover, .action-btn:hover { background: #f8fafc; border-color: #cbd5e1; color: var(--text-dark); }
    .sources-chevron { transition: transform 0.2s; }
    .sources-btn.open .sources-chevron { transform: rotate(180deg); }
    
    .action-btn.primary { background: var(--blue); color: var(--white); border-color: var(--blue-dark); box-shadow: 0 2px 4px rgba(47,128,237,0.2); }
    .action-btn.primary:hover { background: var(--blue-dark); color: var(--white); }

    .feedback-btn {
      display: inline-flex; align-items: center; justify-content: center;
      width: 28px; height: 28px; border-radius: 50%;
      background: transparent; color: var(--text-muted); transition: all 0.2s;
    }
    .feedback-btn:hover { background: var(--white); color: var(--text-dark); box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .feedback-btn.active { color: var(--blue); background: var(--blue-light); }
    .feedback-btn svg { width: 14px; height: 14px; }

    .sources-list { display: none; flex-direction: column; gap: 8px; margin-top: 6px; }
    .sources-list.visible { display: flex; animation: slideUpFadeIn 0.2s ease forwards; }
    .source-card {
      display: flex; align-items: center; gap: 10px; padding: 10px 12px;
      background: var(--white); border: 1px solid var(--border); border-radius: 12px;
    }
    .source-icon {
      width: 28px; height: 28px; background: #eff6ff; border-radius: 8px;
      display: flex; align-items: center; justify-content: center; flex-shrink: 0;
    }
    .source-details { display: flex; flex-direction: column; gap: 2px; }
    .source-title { font-size: 13px; font-weight: 600; color: var(--text-dark); line-height: 1.2; }
    .source-sub { font-size: 11px; color: var(--text-muted); }

    /* SUPPORT ESCALATION CARD */
    .support-card {
      background: var(--white); border: 1px solid var(--border);
      border-radius: 12px; padding: 16px; margin-top: 8px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.05); width: 100%;
    }
    .support-card h4 { font-size: 14px; font-weight: 600; margin-bottom: 4px; color: var(--text-dark); }
    .support-card p { font-size: 12px; color: var(--text-muted); margin-bottom: 12px; }
    .support-links { display: flex; flex-direction: column; gap: 8px; }
    .support-links a {
      display: flex; align-items: center; gap: 8px; font-size: 13px; color: var(--text-mid);
      text-decoration: none; padding: 8px 12px; background: #f8fafc; border-radius: 8px; transition: background 0.2s;
    }
    .support-links a:hover { background: #f1f5f9; color: var(--blue); }
    .support-links a.primary-link { background: var(--blue); color: var(--white); justify-content: center; font-weight: 500; margin-top: 4px; }
    .support-links a.primary-link:hover { background: var(--blue-dark); }

    /* TYPING */
    .typing-row { display: flex; align-items: flex-end; gap: 10px; animation: slideUpFadeIn 0.2s ease; }
    .typing-bubble {
      background: var(--white); border: 1px solid var(--border);
      padding: 14px 16px; border-radius: 16px; border-bottom-left-radius: 4px;
      display: flex; align-items: center; gap: 10px; box-shadow: 0 1px 2px rgba(0,0,0,0.02);
    }
    .dots { display: flex; gap: 4px; }
    .dot { width: 6px; height: 6px; background: var(--text-muted); border-radius: 50%; animation: typingBounce 1.4s infinite ease-in-out both; }
    .dot:nth-child(1) { animation-delay: -0.32s; }
    .dot:nth-child(2) { animation-delay: -0.16s; }
    @keyframes typingBounce { 0%, 80%, 100% { transform: translateY(0); opacity: 0.5; } 40% { transform: translateY(-4px); opacity: 1; } }

    /* INPUT AREA */
    .input-area { padding: 16px 20px 12px; background: var(--white); border-top: 1px solid var(--border); flex-shrink: 0; }
    .input-wrapper {
      position: relative; display: flex; align-items: flex-end;
      background: #f1f5f9; border: 1px solid transparent; border-radius: 24px; padding: 6px 6px 6px 16px;
      transition: background 0.2s, border-color 0.2s, box-shadow 0.2s;
    }
    .input-wrapper:focus-within { background: var(--white); border-color: var(--blue); box-shadow: 0 0 0 3px rgba(47, 128, 237, 0.15); }
    
    textarea {
      width: 100%; background: transparent; border: none; outline: none; resize: none;
      font-size: 14px; padding: 8px 0; height: 36px; max-height: 120px;
      color: var(--text-dark); line-height: 1.4;
    }
    textarea::placeholder { color: #94a3b8; }
    textarea:disabled { opacity: 0.6; cursor: not-allowed; }

    .send-btn {
      width: 36px; height: 36px; background: var(--blue); border-radius: 50%;
      display: flex; align-items: center; justify-content: center;
      color: var(--white); flex-shrink: 0; transition: all 0.2s cubic-bezier(0.2, 0.8, 0.2, 1);
    }
    .send-btn:hover:not(:disabled) { background: var(--blue-dark); transform: scale(1.05); }
    .send-btn:disabled { background: #cbd5e1; cursor: not-allowed; transform: scale(1); }

    .footer { text-align: center; padding-top: 12px; }
    .footer-text { font-size: 11px; color: #94a3b8; }

    /* SCROLL TO BOTTOM BTN */
    .scroll-btn {
      position: absolute; bottom: 80px; left: 50%; transform: translateX(-50%) translateY(10px);
      background: var(--white); border: 1px solid var(--border); box-shadow: 0 4px 12px rgba(0,0,0,0.1);
      padding: 6px 12px; border-radius: 20px; font-size: 12px; color: var(--blue); font-weight: 500;
      display: flex; align-items: center; gap: 4px; opacity: 0; pointer-events: none; transition: all 0.2s;
    }
    .scroll-btn.visible { opacity: 1; pointer-events: auto; transform: translateX(-50%) translateY(0); }
    .scroll-btn:hover { background: #f8fafc; }
  </style>
</head>
<body>

  <div id="w-launcher" class="w-launcher" role="button" tabindex="0" aria-label="Open WiseIN Support Chat">
    <svg viewBox="0 0 52 44" fill="none">
      <path d="M4 10 C4 6 7 4 10 4 C13 4 15 6 16 9 L20 26 L26 10 C27 6.5 29.5 4 33 4 C36.5 4 38.5 6.5 39.5 10 L44 26 L47.5 9 C48.5 6 50 4 52 4 L52 4 C50.5 8 48.5 16 46 28 C45 32 43 36 40 38 C37.5 39.5 35 39 33 37 C31 35 30 33 29 30 L26 20 L23 30 C22 33 21 35 19 37 C17 39 14.5 39.5 12 38 C9 36 7 32 6 28 C3.5 16 1.5 8 0 4 L2 4 C3 4 4 6 4 10 Z" fill="#2F80ED"/>
    </svg>
  </div>

  <div id="widget-container" class="widget-container" role="dialog" aria-label="WiseIN Support Chat">
    <div class="header">
      <div class="header-left">
        <div class="header-icon"><svg viewBox="0 0 52 44" fill="none"><path d="M4 10 C4 6 7 4 10 4 C13 4 15 6 16 9 L20 26 L26 10 C27 6.5 29.5 4 33 4 C36.5 4 38.5 6.5 39.5 10 L44 26 L47.5 9 C48.5 6 50 4 52 4 L52 4 C50.5 8 48.5 16 46 28 C45 32 43 36 40 38 C37.5 39.5 35 39 33 37 C31 35 30 33 29 30 L26 20 L23 30 C22 33 21 35 19 37 C17 39 14.5 39.5 12 38 C9 36 7 32 6 28 C3.5 16 1.5 8 0 4 L2 4 C3 4 4 6 4 10 Z" fill="#2F80ED"/></svg></div>
        <div class="header-info">
          <div class="header-title">WiseIN AI Agent <div class="status-dot"></div></div>
          <div class="header-subtitle">Our team can also help</div>
        </div>
      </div>
      <div class="header-actions">
        <button type="button" onclick="clearChatConfirm()" title="New Chat" aria-label="Start new chat">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a9 9 0 0 0-9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/><path d="M3 12a9 9 0 0 0 9 9 9.75 9.75 0 0 0 6.74-2.74L21 16"/><path d="M16 21v-5h5"/></svg>
        </button>
        <button type="button" onclick="closeWidget()" title="Close" aria-label="Close chat">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
        </button>
      </div>
    </div>

    <div class="chat-area" id="conversation" onscroll="checkScroll()">
      <div class="welcome-msg" id="welcome">
        <h3>Hi! I'm WiseIN AI Support. 👋</h3>
        <p>I can help you with your account, verification, profile, jobs, meetings, and other WiseIN features.<br><br>What can I help you with?</p>
        <div class="suggestions">
          <button class="suggestion-chip" onclick="askSuggestion('How do I create an account?')">How do I create an account?</button>
          <button class="suggestion-chip" onclick="askSuggestion('How do I verify my profile?')">How do I verify my profile?</button>
          <button class="suggestion-chip" onclick="askSuggestion('How do I book a meeting?')">How do I book a meeting?</button>
          <button class="suggestion-chip" onclick="askSuggestion('I\'m having a problem.')">I'm having a problem</button>
        </div>
      </div>
      <button class="scroll-btn" id="scrollBtn" onclick="forceScrollBottom()">↓ New message</button>
    </div>

    <div class="input-area">
      <div class="input-wrapper">
        <textarea id="chatInput" placeholder="Ask me anything about WiseIN..." rows="1" oninput="onInput(this)" onkeydown="onKey(event)" aria-label="Message composer"></textarea>
        <button id="sendBtn" class="send-btn" onclick="send()" disabled aria-label="Send message">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
        </button>
      </div>
      <div class="footer"><div class="footer-text">By chatting with us, you agree to our Privacy Policy</div></div>
    </div>
  </div>

<script>
  marked.setOptions({ breaks: true, gfm: true });

  const conversEl = document.getElementById('conversation');
  const welcomeEl = document.getElementById('welcome');
  const inputEl   = document.getElementById('chatInput');
  const sendBtnEl = document.getElementById('sendBtn');
  const launcher  = document.getElementById('w-launcher');
  const widget    = document.getElementById('widget-container');
  const scrollBtn = document.getElementById('scrollBtn');
  
  let busy = false;
  let chatStarted = false;
  let chatHistory = [];
  let userScrolledUp = false;

  function checkScroll() {
    const isAtBottom = conversEl.scrollHeight - conversEl.scrollTop - conversEl.clientHeight < 50;
    userScrolledUp = !isAtBottom;
    if (isAtBottom) scrollBtn.classList.remove('visible');
  }

  function scrollBottom() {
    if (!userScrolledUp) forceScrollBottom();
    else scrollBtn.classList.add('visible');
  }

  function forceScrollBottom() {
    conversEl.scrollTo({ top: conversEl.scrollHeight, behavior: 'smooth' });
    scrollBtn.classList.remove('visible');
    userScrolledUp = false;
  }

  function loadHistory() {
    const saved = localStorage.getItem('wisein_chat_history');
    if (saved) {
      try {
        const hist = JSON.parse(saved);
        if (hist && hist.length > 0) {
          chatStarted = true; welcomeEl.style.display = 'none';
          hist.forEach(msg => {
            if (msg.role === 'user') addUser(msg.content, false);
            else if (msg.role === 'bot') {
              if (msg.isError) addBotError(msg.content, msg.failedQuery, false);
              else addBot(msg.content, msg.sources || [], false);
            }
          });
          chatHistory = hist; forceScrollBottom();
        }
      } catch(e) {}
    }
  }
  function saveHistory() { localStorage.setItem('wisein_chat_history', JSON.stringify(chatHistory)); }

  function clearChatConfirm() {
    if (!chatStarted || chatHistory.length === 0) return;
    if (confirm("Start a new conversation?")) {
      chatHistory = []; saveHistory();
      document.querySelectorAll('.msg-row').forEach(m => m.remove());
      chatStarted = false; welcomeEl.style.display = 'block';
      hideTyping(); busy = false; inputEl.value = ''; onInput(inputEl); inputEl.disabled = false;
    }
  }

  loadHistory();

  let isDragging = false, dragThresholdHit = false, startX, startY, initialLeft, initialTop;
  const MARGIN = 20;

  function restoreLauncherPosition() {
    const saved = localStorage.getItem('wisein_launcher_pos');
    if (saved) {
      try {
        const pos = JSON.parse(saved);
        const maxL = window.innerWidth - 60 - MARGIN, maxT = window.innerHeight - 60 - MARGIN;
        launcher.style.left = Math.max(MARGIN, Math.min(parseInt(pos.left), maxL)) + 'px';
        launcher.style.top = Math.max(MARGIN, Math.min(parseInt(pos.top), maxT)) + 'px';
        launcher.style.right = 'auto'; launcher.style.bottom = 'auto';
      } catch (e) { defaultLauncherPosition(); }
    } else { defaultLauncherPosition(); }
  }
  function defaultLauncherPosition() { launcher.style.right = MARGIN + 'px'; launcher.style.bottom = MARGIN + 'px'; launcher.style.left = 'auto'; launcher.style.top = 'auto'; }
  window.addEventListener('resize', restoreLauncherPosition); restoreLauncherPosition();

  function onDragStart(e) {
    if (e.target.closest('svg')) e.preventDefault();
    startX = e.touches ? e.touches[0].clientX : e.clientX;
    startY = e.touches ? e.touches[0].clientY : e.clientY;
    const rect = launcher.getBoundingClientRect(); initialLeft = rect.left; initialTop = rect.top;
    isDragging = true; dragThresholdHit = false; launcher.style.transition = 'none';
  }
  function onDragMove(e) {
    if (!isDragging) return;
    const cX = e.touches ? e.touches[0].clientX : e.clientX, cY = e.touches ? e.touches[0].clientY : e.clientY;
    if (Math.abs(cX - startX) > 3 || Math.abs(cY - startY) > 3) dragThresholdHit = true;
    if (dragThresholdHit) {
      e.preventDefault();
      const maxL = window.innerWidth - 60 - MARGIN, maxT = window.innerHeight - 60 - MARGIN;
      launcher.style.left = Math.max(MARGIN, Math.min(initialLeft + (cX - startX), maxL)) + 'px';
      launcher.style.top = Math.max(MARGIN, Math.min(initialTop + (cY - startY), maxT)) + 'px';
      launcher.style.right = 'auto'; launcher.style.bottom = 'auto';
    }
  }
  function onDragEnd() {
    if (!isDragging) return;
    isDragging = false; launcher.style.transition = 'transform 0.25s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.2s ease';
    if (dragThresholdHit) localStorage.setItem('wisein_launcher_pos', JSON.stringify({ left: launcher.style.left, top: launcher.style.top }));
  }

  launcher.addEventListener('mousedown', onDragStart); document.addEventListener('mousemove', onDragMove, {passive: false}); document.addEventListener('mouseup', onDragEnd);
  launcher.addEventListener('touchstart', onDragStart, {passive: false}); document.addEventListener('touchmove', onDragMove, {passive: false}); document.addEventListener('touchend', onDragEnd);
  launcher.addEventListener('click', (e) => { if (dragThresholdHit) { e.preventDefault(); return; } openWidget(); });
  launcher.addEventListener('keydown', (e) => { if(e.key === 'Enter' || e.key === ' ') openWidget(); });

  function openWidget() {
    if (window.innerWidth > 500) {
      const rect = launcher.getBoundingClientRect();
      const cx = rect.left + rect.width / 2, cy = rect.top + rect.height / 2;
      const wWidth = widget.offsetWidth || 440, wHeight = widget.offsetHeight || 680;
      let wLeft = (cx > window.innerWidth / 2) ? rect.right - wWidth : rect.left;
      let wTop = (cy > window.innerHeight / 2) ? rect.top - wHeight - 10 : rect.bottom + 10;
      widget.style.left = Math.max(10, Math.min(wLeft, window.innerWidth - wWidth - 10)) + 'px';
      widget.style.top = Math.max(10, Math.min(wTop, window.innerHeight - wHeight - 10)) + 'px';
      widget.style.right = 'auto'; widget.style.bottom = 'auto';
    }
    widget.classList.add('open'); launcher.style.opacity = '0'; launcher.style.pointerEvents = 'none';
    setTimeout(() => { if(!busy) inputEl.focus(); }, 150);
  }
  function closeWidget() { widget.classList.remove('open'); launcher.style.opacity = '1'; launcher.style.pointerEvents = 'auto'; }
  
  const headerEl = document.querySelector('.header');
  let isWidgetDragging = false, wStartX, wStartY, wInitialLeft, wInitialTop;
  function onWidgetDragStart(e) {
    if (e.target.closest('button')) return;
    isWidgetDragging = true; wStartX = e.touches ? e.touches[0].clientX : e.clientX; wStartY = e.touches ? e.touches[0].clientY : e.clientY;
    wInitialLeft = widget.offsetLeft; wInitialTop = widget.offsetTop; widget.style.transition = 'none';
  }
  function onWidgetDragMove(e) {
    if (!isWidgetDragging) return;
    const cX = e.touches ? e.touches[0].clientX : e.clientX, cY = e.touches ? e.touches[0].clientY : e.clientY;
    widget.style.left = Math.max(0, Math.min(wInitialLeft + (cX - wStartX), window.innerWidth - widget.offsetWidth)) + 'px';
    widget.style.top = Math.max(0, Math.min(wInitialTop + (cY - wStartY), window.innerHeight - widget.offsetHeight)) + 'px';
  }
  function onWidgetDragEnd() { if (isWidgetDragging) { isWidgetDragging = false; widget.style.transition = 'opacity 0.25s ease, transform 0.25s cubic-bezier(0.2, 0.8, 0.2, 1)'; } }
  headerEl.addEventListener('mousedown', onWidgetDragStart); document.addEventListener('mousemove', onWidgetDragMove, {passive: false}); document.addEventListener('mouseup', onWidgetDragEnd);
  headerEl.addEventListener('touchstart', onWidgetDragStart, {passive: false}); document.addEventListener('touchmove', onWidgetDragMove, {passive: false}); document.addEventListener('touchend', onWidgetDragEnd);

  function onInput(el) { el.style.height = 'auto'; el.style.height = Math.min(el.scrollHeight, 120) + 'px'; sendBtnEl.disabled = !el.value.trim(); }
  function onKey(e) { if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); send(); } }
  function esc(str) { return (str || '').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/\n/g,'<br>'); }

  function botAvatar() { return `<div class="avatar avatar-bot"><svg viewBox="0 0 52 44" fill="none"><path d="M4 10 C4 6 7 4 10 4 C13 4 15 6 16 9 L20 26 L26 10 C27 6.5 29.5 4 33 4 C36.5 4 38.5 6.5 39.5 10 L44 26 L47.5 9 C48.5 6 50 4 52 4 L52 4 C50.5 8 48.5 16 46 28 C45 32 43 36 40 38 C37.5 39.5 35 39 33 37 C31 35 30 33 29 30 L26 20 L23 30 C22 33 21 35 19 37 C17 39 14.5 39.5 12 38 C9 36 7 32 6 28 C3.5 16 1.5 8 0 4 L2 4 C3 4 4 6 4 10 Z" fill="#2F80ED"/></svg></div>`; }
  function userAvatar() { return `<div class="avatar avatar-user"><svg viewBox="0 0 24 24" fill="none"><circle cx="12" cy="8" r="4" fill="#FFFFFF"/><path d="M4 20c0-4 3.58-7 8-7s8 3 8 7" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/></svg></div>`; }

  function addUser(text, save = true) {
    const row = document.createElement('div'); row.className = 'msg-row user-row';
    row.innerHTML = `${userAvatar()}<div class="bubble-col"><div class="bubble-user">${esc(text)}</div></div>`;
    conversEl.appendChild(row); scrollBottom();
    if (save) { chatHistory.push({ role: 'user', content: text }); saveHistory(); }
  }

  function toggleFeedback(btn, type) {
    const parent = btn.parentElement;
    parent.querySelectorAll('.feedback-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
  }

  function generateSupportCard() {
    return `
      <div class="support-card">
        <h4>Contact WiseIN Support</h4>
        <p>We reply within 24 hours. Usually faster.</p>
        <div class="support-links">
          <a href="mailto:support@wisein.in">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
            support@wisein.in
          </a>
          <a href="tel:+918008656641">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
            +91 8008656641
          </a>
          <a href="https://instagram.com/santhosh_wisein" target="_blank">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
            @santhosh_wisein
          </a>
          <a href="https://www.wisein.in/contact" target="_blank" class="primary-link">Contact Form ↗</a>
        </div>
      </div>
    `;
  }

  function addBot(text, sources = [], save = true) {
    let srcHtml = '';
    if (sources && sources.length) {
      const cards = sources.map(s => `<div class="source-card"><div class="source-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" stroke="#2F80ED" stroke-width="2" stroke-linejoin="round"/><polyline points="14 2 14 8 20 8" stroke="#2F80ED" stroke-width="2" stroke-linejoin="round"/></svg></div><div class="source-details"><div class="source-title">${esc(s.name)}</div><div class="source-sub">WiseIN Knowledge Base</div></div></div>`).join('');
      srcHtml = `<button class="sources-btn" onclick="toggleSrc(this)"><svg class="sources-chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><polyline points="6 9 12 15 18 9"/></svg>Sources</button><div class="sources-list">${cards}</div>`;
    }

    const safeHtml = DOMPurify.sanitize(marked.parse(text));
    
    // Human Escalation Check (triggered by the AI prompt outputting the exact keyword)
    let fallbackHtml = '';
    if (text.toLowerCase().includes("contact them directly using the options below") || text.toLowerCase().includes("couldn't find enough information") || text.toLowerCase().includes("contact wisein support")) {
      fallbackHtml = generateSupportCard();
    }

    const row = document.createElement('div'); row.className = 'msg-row';
    row.innerHTML = `
      ${botAvatar()}
      <div class="bubble-col">
        <div class="bubble-bot">${safeHtml}</div>
        ${fallbackHtml}
        <div class="bot-actions-row">
          ${srcHtml}
          <button class="feedback-btn" onclick="toggleFeedback(this, 'up')" title="Helpful" aria-label="Mark helpful"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"></path></svg></button>
          <button class="feedback-btn" onclick="toggleFeedback(this, 'down')" title="Not helpful" aria-label="Mark not helpful"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 15v4a3 3 0 0 0 3 3l4-9V2H5.72a2 2 0 0 0-2 1.7l-1.38 9a2 2 0 0 0 2 2.3zm7-13h2a2 2 0 0 1 2 2v7a2 2 0 0 1-2 2h-2"></path></svg></button>
        </div>
      </div>`;
    conversEl.appendChild(row); scrollBottom();
    if (save) { chatHistory.push({ role: 'bot', content: text, sources: sources, isError: false }); saveHistory(); }
  }

  function addBotError(text, failedQuery, save = true) {
    const row = document.createElement('div'); row.className = 'msg-row';
    const escapedQuery = (failedQuery || '').replace(/'/g, "\\'").replace(/"/g, '&quot;');
    row.innerHTML = `
      ${botAvatar()}
      <div class="bubble-col">
        <div class="bubble-bot bubble-error">${esc(text)}</div>
        <div class="bot-actions-row"><button class="action-btn" onclick="askSuggestion('${escapedQuery}')">↻ Retry</button></div>
      </div>`;
    conversEl.appendChild(row); scrollBottom();
    if (save) { chatHistory.push({ role: 'bot', content: text, isError: true, failedQuery: failedQuery }); saveHistory(); }
  }

  function showTyping() {
    const row = document.createElement('div'); row.className = 'typing-row'; row.id = 'typing';
    row.innerHTML = `${botAvatar()}<div class="typing-bubble"><div class="dots"><div class="dot"></div><div class="dot"></div><div class="dot"></div></div></div>`;
    conversEl.appendChild(row); scrollBottom();
  }
  function hideTyping() { const el = document.getElementById('typing'); if (el) el.remove(); }
  function toggleSrc(btn) { const panel = btn.nextElementSibling; btn.classList.toggle('open', panel.classList.toggle('visible')); }

  function askSuggestion(q) { if (busy) return; inputEl.value = q; onInput(inputEl); send(); }

  async function send() {
    const text = inputEl.value.trim(); if (!text || busy) return; busy = true;
    if (!chatStarted) { chatStarted = true; welcomeEl.style.display = 'none'; }
    inputEl.value = ''; inputEl.style.height = '36px'; sendBtnEl.disabled = true; inputEl.disabled = true;

    addUser(text); showTyping();
    let fullText = '', sources = [];

    try {
      const res = await fetch('/api/chat', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: text, history: chatHistory })
      });
      hideTyping();
      if (!res.ok) {
        const err = await res.json().catch(() => ({}));
        addBotError(err.detail || 'Sorry, I couldn\'t complete that request right now. Please try again.', text); return;
      }

      const row = document.createElement('div'); row.className = 'msg-row';
      row.innerHTML = `${botAvatar()}<div class="bubble-col"><div class="bubble-bot" id="streaming-bubble"></div><div id="streaming-escalation"></div><div class="bot-actions-row" id="streaming-actions"></div></div>`;
      conversEl.appendChild(row);
      const bubble = row.querySelector('#streaming-bubble'), actionsRow = row.querySelector('#streaming-actions'), escRow = row.querySelector('#streaming-escalation');
      const reader = res.body.getReader(), decoder = new TextDecoder();

      while (true) {
        const { value, done } = await reader.read(); if (done) break;
        const chunkStr = decoder.decode(value, {stream: true}), lines = chunkStr.split('\n\n');
        for (const line of lines) {
          if (line.startsWith('data: ')) {
            const data = JSON.parse(line.substring(6));
            if (data.type === 'sources') sources = data.sources;
            else if (data.type === 'token') {
              fullText += data.content;
              bubble.innerHTML = DOMPurify.sanitize(marked.parse(fullText));
              scrollBottom();
            }
          }
        }
      }

      let srcHtml = '';
      if (sources && sources.length > 0) {
        const cards = sources.map(s => `<div class="source-card"><div class="source-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" stroke="#2F80ED" stroke-width="2" stroke-linejoin="round"/><polyline points="14 2 14 8 20 8" stroke="#2F80ED" stroke-width="2" stroke-linejoin="round"/></svg></div><div class="source-details"><div class="source-title">${esc(s.name)}</div><div class="source-sub">WiseIN Knowledge Base</div></div></div>`).join('');
        srcHtml = `<button class="sources-btn" onclick="toggleSrc(this)"><svg class="sources-chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><polyline points="6 9 12 15 18 9"/></svg>Sources</button><div class="sources-list">${cards}</div>`;
      }

      if (fullText.toLowerCase().includes("contact them directly using the options below") || fullText.toLowerCase().includes("couldn't find enough information") || fullText.toLowerCase().includes("contact wisein support")) {
        escRow.innerHTML = generateSupportCard();
      }

      actionsRow.innerHTML = `${srcHtml}<button class="feedback-btn" onclick="toggleFeedback(this, 'up')" aria-label="Mark helpful"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"></path></svg></button><button class="feedback-btn" onclick="toggleFeedback(this, 'down')" aria-label="Mark not helpful"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 15v4a3 3 0 0 0 3 3l4-9V2H5.72a2 2 0 0 0-2 1.7l-1.38 9a2 2 0 0 0 2 2.3zm7-13h2a2 2 0 0 1 2 2v7a2 2 0 0 1-2 2h-2"></path></svg></button>`;
      bubble.removeAttribute('id'); actionsRow.removeAttribute('id'); escRow.removeAttribute('id');
      chatHistory.push({ role: 'bot', content: fullText, sources: sources, isError: false }); saveHistory();

    } catch (e) {
      hideTyping(); addBotError('Sorry, I couldn\'t complete that request right now. Please try again.', text);
    } finally {
      busy = false; inputEl.disabled = false; onInput(inputEl); setTimeout(() => inputEl.focus(), 10);
    }
  }
</script>
</body>
</html>
"""

with open('frontend/index.html', 'w', encoding='utf-8') as f:
    f.write(HTML_CONTENT)

print("Upgraded to premium AI bot and UI.")
