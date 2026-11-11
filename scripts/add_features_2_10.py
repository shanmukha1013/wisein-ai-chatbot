import sys

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
    /* DESIGN TOKENS */
    :root {
      --blue:        #2F80ED;
      --blue-dark:   #1a65c5;
      --blue-light:  #EBF4FF;
      --white:       #FFFFFF;
      --bg:          #F8FAFC;
      --text-dark:   #111827;
      --text-mid:    #374151;
      --text-muted:  #64748B;
      --border:      #E5E7EB;
      --shadow-widget: 0 12px 40px rgba(0,0,0,0.12), 0 4px 12px rgba(0,0,0,0.08);
      --shadow-launcher: 0 4px 12px rgba(0,0,0,0.15);
      --font:        'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    
    body {
      font-family: var(--font);
      background: #E2E8F0;
      height: 100vh;
      overflow: hidden;
      color: var(--text-dark);
      -webkit-font-smoothing: antialiased;
    }

    button { cursor: pointer; border: none; background: none; font-family: var(--font); }
    textarea { font-family: var(--font); }
    ::-webkit-scrollbar { width: 4px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 8px; }

    /* LAUNCHER BUTTON */
    .w-launcher {
      position: fixed;
      width: 60px;
      height: 60px;
      background: var(--white);
      border-radius: 50%;
      box-shadow: var(--shadow-launcher);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: grab;
      z-index: 10000;
      transition: transform 0.2s ease, box-shadow 0.2s ease;
      user-select: none;
      touch-action: none;
    }
    .w-launcher:active { cursor: grabbing; transform: scale(0.95); }
    .w-launcher svg { width: 28px; height: 24px; pointer-events: none; }

    /* WIDGET CONTAINER */
    .widget-container {
      position: fixed;
      width: 440px;
      min-width: 320px;
      height: 680px;
      min-height: 400px;
      max-width: calc(100vw - 40px);
      max-height: calc(100vh - 40px);
      background: var(--white);
      border-radius: 20px;
      box-shadow: var(--shadow-widget);
      border: 1px solid var(--border);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      z-index: 9999;
      resize: both;
      opacity: 0;
      transform: scale(0.95) translateY(10px);
      pointer-events: none;
      transition: opacity 0.2s ease, transform 0.2s ease;
    }
    .widget-container.open {
      opacity: 1;
      transform: scale(1) translateY(0);
      pointer-events: auto;
    }

    @media (max-width: 500px) {
      .widget-container {
        width: calc(100vw - 20px) !important;
        height: calc(100vh - 20px) !important;
        left: 10px !important;
        bottom: 10px !important;
        top: 10px !important;
        right: auto !important;
        border-radius: 16px;
        resize: none;
      }
    }

    /* HEADER */
    .header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 16px 20px;
      background: var(--white);
      border-bottom: 1px solid var(--border);
      flex-shrink: 0;
      cursor: grab;
    }
    .header:active { cursor: grabbing; }

    .header-left { display: flex; align-items: center; gap: 12px; }
    .header-icon {
      width: 36px; height: 36px;
      background: #F8FAFC; border: 1px solid var(--border);
      border-radius: 50%; display: flex; align-items: center; justify-content: center;
    }
    .header-icon svg { width: 18px; height: 16px; }

    .header-info { display: flex; flex-direction: column; gap: 2px; }
    .header-title {
      font-size: 15px; font-weight: 600; color: var(--text-dark);
      display: flex; align-items: center; gap: 6px; line-height: 1.1;
    }
    .status-dot { width: 6px; height: 6px; border-radius: 50%; background: #22C55E; }
    .header-subtitle { font-size: 12px; color: var(--text-muted); font-weight: 400; }

    .header-actions { display: flex; align-items: center; gap: 12px; color: var(--text-muted); }
    .header-actions button {
      display: flex; align-items: center; justify-content: center;
      color: var(--text-muted); transition: color 0.2s;
    }
    .header-actions button:hover { color: var(--text-dark); }
    .header-actions svg { width: 16px; height: 16px; pointer-events: none; }

    /* CHAT AREA */
    .chat-area {
      flex: 1;
      overflow-y: auto;
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 20px;
      background: var(--bg);
    }

    .welcome-msg { text-align: center; margin-bottom: 10px; }
    .welcome-msg h3 { font-size: 15px; margin-bottom: 6px; color: var(--text-dark); }
    .welcome-msg p { font-size: 13px; color: var(--text-muted); margin-bottom: 16px; }

    .suggestions {
      display: flex;
      flex-direction: column;
      gap: 8px;
      align-items: center;
    }
    .suggestion-chip {
      background: var(--white);
      border: 1px solid var(--border);
      color: var(--text-dark);
      font-size: 13px;
      padding: 8px 14px;
      border-radius: 20px;
      box-shadow: 0 1px 2px rgba(0,0,0,0.02);
      transition: all 0.2s;
      width: 100%;
      max-width: 280px;
      text-align: center;
    }
    .suggestion-chip:hover {
      background: var(--blue-light);
      border-color: #BFDBFE;
      color: var(--blue-dark);
    }

    .msg-row { display: flex; align-items: flex-start; gap: 10px; max-width: 92%; }
    .msg-row.user-row { align-self: flex-end; flex-direction: row-reverse; }

    .avatar {
      width: 28px; height: 28px; border-radius: 50%;
      display: flex; align-items: center; justify-content: center; flex-shrink: 0;
    }
    .avatar-bot { background: var(--blue-light); border: 1px solid #BFDBFE; }
    .avatar-user { background: var(--blue); }

    .bubble-col { display: flex; flex-direction: column; gap: 6px; width: 100%; }
    .bubble-bot, .bubble-user {
      padding: 12px 16px; border-radius: 16px; font-size: 14px; line-height: 1.5; word-wrap: break-word;
    }
    .bubble-bot { background: var(--white); color: var(--text-dark); border: 1px solid var(--border); border-top-left-radius: 4px; }
    .bubble-user { background: var(--blue); color: var(--white); border-top-right-radius: 4px; }
    .bubble-error { background: #FEF2F2; color: #991B1B; border: 1px solid #FCA5A5; }

    /* MARKDOWN STYLES */
    .bubble-bot p { margin-bottom: 0.75em; }
    .bubble-bot p:last-child { margin-bottom: 0; }
    .bubble-bot strong { font-weight: 600; color: #000; }
    .bubble-bot em { font-style: italic; }
    .bubble-bot ul { margin-left: 1.5em; margin-bottom: 0.75em; list-style-type: disc; }
    .bubble-bot ol { margin-left: 1.5em; margin-bottom: 0.75em; list-style-type: decimal; }
    .bubble-bot li { margin-bottom: 0.25em; }
    .bubble-bot li:last-child { margin-bottom: 0; }
    .bubble-bot h1, .bubble-bot h2, .bubble-bot h3 { font-size: 1.1em; font-weight: 600; margin: 1em 0 0.5em 0; }
    .bubble-bot h1:first-child, .bubble-bot h2:first-child, .bubble-bot h3:first-child { margin-top: 0; }
    .bubble-bot code { background: #F1F5F9; padding: 2px 4px; border-radius: 4px; font-family: monospace; font-size: 0.9em; }
    .bubble-bot pre { background: #F1F5F9; padding: 10px; border-radius: 6px; overflow-x: auto; margin-bottom: 0.75em; }
    .bubble-bot pre code { background: none; padding: 0; }
    .bubble-bot a { color: var(--blue); text-decoration: none; }
    .bubble-bot a:hover { text-decoration: underline; }

    /* BOT ACTIONS (Sources, Feedback, Escalation) */
    .bot-actions-row {
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 6px;
      margin-top: 2px;
    }
    .sources-btn, .action-btn {
      display: inline-flex; align-items: center; gap: 4px;
      background: var(--white); border: 1px solid var(--border);
      padding: 4px 10px; border-radius: 20px;
      font-size: 12px; font-weight: 500; color: var(--text-mid);
      transition: background 0.2s;
    }
    .sources-btn:hover, .action-btn:hover { background: #F8FAFC; }
    .sources-chevron { transition: transform 0.2s; }
    .sources-btn.open .sources-chevron { transform: rotate(180deg); }
    
    .action-btn.primary { background: var(--blue-light); color: var(--blue-dark); border-color: #BFDBFE; }
    .action-btn.primary:hover { background: #DBEAFE; }

    .feedback-btn {
      display: inline-flex; align-items: center; justify-content: center;
      width: 26px; height: 26px; border-radius: 50%;
      background: transparent; color: var(--text-light);
      transition: all 0.2s;
    }
    .feedback-btn:hover { background: var(--white); color: var(--text-dark); box-shadow: 0 1px 2px rgba(0,0,0,0.05); }
    .feedback-btn.active { color: var(--blue); background: var(--blue-light); }
    .feedback-btn svg { width: 14px; height: 14px; }

    .sources-list { display: none; flex-direction: column; gap: 6px; margin-top: 2px; }
    .sources-list.visible { display: flex; }
    .source-card {
      display: flex; align-items: center; gap: 10px; padding: 8px 12px;
      background: var(--white); border: 1px solid var(--border); border-radius: 12px;
    }
    .source-icon {
      width: 24px; height: 24px; background: #eff6ff; border-radius: 6px;
      display: flex; align-items: center; justify-content: center;
    }
    .source-details { display: flex; flex-direction: column; }
    .source-title { font-size: 12px; font-weight: 600; color: var(--text-dark); }
    .source-sub { font-size: 10px; color: var(--text-muted); }

    /* TYPING */
    .typing-row { display: flex; align-items: flex-end; gap: 10px; }
    .typing-bubble {
      background: var(--white); border: 1px solid var(--border);
      padding: 12px 16px; border-radius: 16px; border-bottom-left-radius: 4px;
      display: flex; align-items: center; gap: 8px;
    }
    .dots { display: flex; gap: 4px; }
    .dot { width: 6px; height: 6px; background: var(--blue); border-radius: 50%; animation: bounce 1.4s infinite ease-in-out both; }
    .dot:nth-child(1) { animation-delay: -0.32s; }
    .dot:nth-child(2) { animation-delay: -0.16s; }
    @keyframes bounce { 0%, 80%, 100% { transform: scale(0); } 40% { transform: scale(1); } }
    .typing-label { font-size: 12px; color: var(--text-muted); }

    /* INPUT AREA */
    .input-area { padding: 12px 20px; background: var(--white); border-top: 1px solid var(--border); flex-shrink: 0; }
    .input-wrapper {
      position: relative; display: flex; align-items: flex-end;
      background: var(--bg); border: 1px solid var(--border); border-radius: 20px; padding: 6px 6px 6px 16px;
    }
    .input-wrapper:focus-within { border-color: var(--blue); box-shadow: 0 0 0 2px rgba(47, 128, 237, 0.1); }
    
    textarea {
      width: 100%; background: transparent; border: none; outline: none; resize: none;
      font-size: 14px; padding: 6px 0; height: 32px; max-height: 100px;
      color: var(--text-dark); line-height: 1.4;
    }
    textarea::placeholder { color: var(--text-muted); }
    textarea:disabled { opacity: 0.6; cursor: not-allowed; }

    .send-btn {
      width: 32px; height: 32px; background: var(--blue); border-radius: 16px;
      display: flex; align-items: center; justify-content: center;
      color: var(--white); flex-shrink: 0; transition: background 0.2s;
    }
    .send-btn:hover:not(:disabled) { background: var(--blue-dark); }
    .send-btn:disabled { background: #cbd5e1; cursor: not-allowed; }

    .footer { text-align: center; padding-top: 10px; padding-bottom: 4px; }
    .footer-text { font-size: 11px; color: var(--text-muted); }
  </style>
</head>
<body>

  <!-- DRAGGABLE W LAUNCHER -->
  <div id="w-launcher" class="w-launcher">
    <svg viewBox="0 0 52 44" fill="none">
      <path d="M4 10 C4 6 7 4 10 4 C13 4 15 6 16 9 L20 26 L26 10 C27 6.5 29.5 4 33 4 C36.5 4 38.5 6.5 39.5 10 L44 26 L47.5 9 C48.5 6 50 4 52 4 L52 4 C50.5 8 48.5 16 46 28 C45 32 43 36 40 38 C37.5 39.5 35 39 33 37 C31 35 30 33 29 30 L26 20 L23 30 C22 33 21 35 19 37 C17 39 14.5 39.5 12 38 C9 36 7 32 6 28 C3.5 16 1.5 8 0 4 L2 4 C3 4 4 6 4 10 Z" fill="#2F80ED"/>
    </svg>
  </div>

  <!-- FLOATING WIDGET -->
  <div id="widget-container" class="widget-container">
    
    <!-- Header -->
    <div class="header">
      <div class="header-left">
        <div class="header-icon">
          <svg viewBox="0 0 52 44" fill="none"><path d="M4 10 C4 6 7 4 10 4 C13 4 15 6 16 9 L20 26 L26 10 C27 6.5 29.5 4 33 4 C36.5 4 38.5 6.5 39.5 10 L44 26 L47.5 9 C48.5 6 50 4 52 4 L52 4 C50.5 8 48.5 16 46 28 C45 32 43 36 40 38 C37.5 39.5 35 39 33 37 C31 35 30 33 29 30 L26 20 L23 30 C22 33 21 35 19 37 C17 39 14.5 39.5 12 38 C9 36 7 32 6 28 C3.5 16 1.5 8 0 4 L2 4 C3 4 4 6 4 10 Z" fill="#2F80ED"/></svg>
        </div>
        <div class="header-info">
          <div class="header-title">WiseIN AI Agent <div class="status-dot"></div></div>
          <div class="header-subtitle">Our team can also help</div>
        </div>
      </div>
      <div class="header-actions">
        <!-- New Chat -->
        <button type="button" onclick="clearChatConfirm()" title="New Chat">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a9 9 0 0 0-9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/><path d="M3 12a9 9 0 0 0 9 9 9.75 9.75 0 0 0 6.74-2.74L21 16"/><path d="M16 21v-5h5"/></svg>
        </button>
        <!-- Minimize / Close -->
        <button type="button" onclick="closeWidget()" title="Close">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
        </button>
      </div>
    </div>

    <!-- Chat Area -->
    <div class="chat-area" id="conversation">
      <div class="welcome-msg" id="welcome">
        <h3>Hi there! 👋</h3>
        <p>I'm the WiseIN Support Assistant. How can I help you today?</p>
        <div class="suggestions">
          <button class="suggestion-chip" onclick="askSuggestion('How do I verify my identity on WiseIN?')">How do I verify my identity?</button>
          <button class="suggestion-chip" onclick="askSuggestion('How do I create or update my profile?')">How do I update my profile?</button>
          <button class="suggestion-chip" onclick="askSuggestion('How do I book a meeting?')">How do I book a meeting?</button>
          <button class="suggestion-chip" onclick="askSuggestion('How can I find jobs on WiseIN?')">How can I find jobs?</button>
          <button class="suggestion-chip" onclick="askSuggestion('I found a problem. What should I do?')">Report a problem</button>
        </div>
      </div>
    </div>

    <!-- Input Area -->
    <div class="input-area">
      <div class="input-wrapper">
        <textarea id="chatInput" placeholder="Ask a question..." rows="1" oninput="onInput(this)" onkeydown="onKey(event)"></textarea>
        <button id="sendBtn" class="send-btn" onclick="send()" disabled>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
        </button>
      </div>
      <div class="footer">
        <div class="footer-text">By chatting with us, you agree to our Privacy Policy</div>
      </div>
    </div>

  </div>

<script>
  /* --- SETUP MARKED --- */
  marked.setOptions({ breaks: true, gfm: true });

  /* --- GLOBALS --- */
  const conversEl = document.getElementById('conversation');
  const welcomeEl = document.getElementById('welcome');
  const inputEl   = document.getElementById('chatInput');
  const sendBtnEl = document.getElementById('sendBtn');
  const launcher  = document.getElementById('w-launcher');
  const widget    = document.getElementById('widget-container');
  
  let busy = false;
  let chatStarted = false;
  let chatHistory = []; // format: { role: 'user'|'bot', content: '...', sources: [], isError: bool }

  /* --- INIT HISTORY --- */
  function loadHistory() {
    const saved = localStorage.getItem('wisein_chat_history');
    if (saved) {
      try {
        const hist = JSON.parse(saved);
        if (hist && hist.length > 0) {
          chatStarted = true;
          welcomeEl.style.display = 'none';
          hist.forEach(msg => {
            if (msg.role === 'user') {
              addUser(msg.content, false);
            } else if (msg.role === 'bot') {
              if (msg.isError) {
                addBotError(msg.content, msg.failedQuery, false);
              } else {
                addBot(msg.content, msg.sources || [], false);
              }
            }
          });
          chatHistory = hist;
          scrollBottom();
        }
      } catch(e) {}
    }
  }

  function saveHistory() {
    localStorage.setItem('wisein_chat_history', JSON.stringify(chatHistory));
  }

  function clearChatConfirm() {
    if (!chatStarted || chatHistory.length === 0) return;
    if (confirm("Are you sure you want to start a new chat and clear the current conversation?")) {
      chatHistory = [];
      saveHistory();
      
      // Remove all msg-rows
      const msgs = document.querySelectorAll('.msg-row');
      msgs.forEach(m => m.remove());
      
      chatStarted = false;
      welcomeEl.style.display = 'block';
      hideTyping();
      busy = false;
      inputEl.value = '';
      onInput(inputEl);
      inputEl.disabled = false;
    }
  }

  loadHistory();

  /* --- DRAGGABLE LAUNCHER LOGIC --- */
  let isDragging = false, dragThresholdHit = false, startX, startY, initialLeft, initialTop;
  const MARGIN = 20;

  function restoreLauncherPosition() {
    const saved = localStorage.getItem('wisein_launcher_pos');
    if (saved) {
      try {
        const pos = JSON.parse(saved);
        const maxL = window.innerWidth - 60 - MARGIN;
        const maxT = window.innerHeight - 60 - MARGIN;
        let l = parseInt(pos.left), t = parseInt(pos.top);
        l = Math.max(MARGIN, Math.min(l, maxL));
        t = Math.max(MARGIN, Math.min(t, maxT));
        launcher.style.left = l + 'px'; launcher.style.top = t + 'px';
        launcher.style.right = 'auto'; launcher.style.bottom = 'auto';
      } catch (e) { defaultLauncherPosition(); }
    } else { defaultLauncherPosition(); }
  }

  function defaultLauncherPosition() {
    launcher.style.right = MARGIN + 'px'; launcher.style.bottom = MARGIN + 'px';
    launcher.style.left = 'auto'; launcher.style.top = 'auto';
  }

  window.addEventListener('resize', restoreLauncherPosition);
  restoreLauncherPosition();

  function onDragStart(e) {
    if (e.target.closest('svg')) e.preventDefault();
    const cX = e.touches ? e.touches[0].clientX : e.clientX;
    const cY = e.touches ? e.touches[0].clientY : e.clientY;
    startX = cX; startY = cY;
    const rect = launcher.getBoundingClientRect();
    initialLeft = rect.left; initialTop = rect.top;
    isDragging = true; dragThresholdHit = false;
    launcher.style.transition = 'none';
  }

  function onDragMove(e) {
    if (!isDragging) return;
    const cX = e.touches ? e.touches[0].clientX : e.clientX;
    const cY = e.touches ? e.touches[0].clientY : e.clientY;
    const dx = cX - startX, dy = cY - startY;
    
    if (Math.abs(dx) > 3 || Math.abs(dy) > 3) dragThresholdHit = true;

    if (dragThresholdHit) {
      e.preventDefault();
      const maxL = window.innerWidth - 60 - MARGIN, maxT = window.innerHeight - 60 - MARGIN;
      let newL = Math.max(MARGIN, Math.min(initialLeft + dx, maxL));
      let newT = Math.max(MARGIN, Math.min(initialTop + dy, maxT));
      launcher.style.left = newL + 'px'; launcher.style.top = newT + 'px';
      launcher.style.right = 'auto'; launcher.style.bottom = 'auto';
    }
  }

  function onDragEnd() {
    if (!isDragging) return;
    isDragging = false;
    launcher.style.transition = 'transform 0.2s ease, box-shadow 0.2s ease';
    if (dragThresholdHit) localStorage.setItem('wisein_launcher_pos', JSON.stringify({ left: launcher.style.left, top: launcher.style.top }));
  }

  launcher.addEventListener('mousedown', onDragStart);
  document.addEventListener('mousemove', onDragMove, {passive: false});
  document.addEventListener('mouseup', onDragEnd);
  launcher.addEventListener('touchstart', onDragStart, {passive: false});
  document.addEventListener('touchmove', onDragMove, {passive: false});
  document.addEventListener('touchend', onDragEnd);
  launcher.addEventListener('click', (e) => { if (dragThresholdHit) { e.preventDefault(); return; } openWidget(); });

  /* --- WIDGET POSITIONING & DRAGGING --- */
  function openWidget() {
    if (window.innerWidth > 500) {
      const rect = launcher.getBoundingClientRect();
      const cx = rect.left + rect.width / 2, cy = rect.top + rect.height / 2;
      const wWidth = widget.offsetWidth || 440, wHeight = widget.offsetHeight || 680;
      let wLeft = (cx > window.innerWidth / 2) ? rect.right - wWidth : rect.left;
      let wTop = (cy > window.innerHeight / 2) ? rect.top - wHeight - 10 : rect.bottom + 10;
      wLeft = Math.max(10, Math.min(wLeft, window.innerWidth - wWidth - 10));
      wTop = Math.max(10, Math.min(wTop, window.innerHeight - wHeight - 10));
      widget.style.left = wLeft + 'px'; widget.style.top = wTop + 'px';
      widget.style.right = 'auto'; widget.style.bottom = 'auto';
    }
    widget.classList.add('open');
    launcher.style.opacity = '0';
    launcher.style.pointerEvents = 'none';
    setTimeout(() => { if(!busy) inputEl.focus(); }, 100);
  }

  function closeWidget() {
    widget.classList.remove('open');
    launcher.style.opacity = '1';
    launcher.style.pointerEvents = 'auto';
  }
  
  const headerEl = document.querySelector('.header');
  let isWidgetDragging = false, wStartX, wStartY, wInitialLeft, wInitialTop;
  function onWidgetDragStart(e) {
    if (e.target.closest('button')) return;
    const cX = e.touches ? e.touches[0].clientX : e.clientX, cY = e.touches ? e.touches[0].clientY : e.clientY;
    isWidgetDragging = true; wStartX = cX; wStartY = cY;
    wInitialLeft = widget.offsetLeft; wInitialTop = widget.offsetTop;
    widget.style.transition = 'none';
  }
  function onWidgetDragMove(e) {
    if (!isWidgetDragging) return;
    const cX = e.touches ? e.touches[0].clientX : e.clientX, cY = e.touches ? e.touches[0].clientY : e.clientY;
    let newLeft = Math.max(0, Math.min(wInitialLeft + (cX - wStartX), window.innerWidth - widget.offsetWidth));
    let newTop = Math.max(0, Math.min(wInitialTop + (cY - wStartY), window.innerHeight - widget.offsetHeight));
    widget.style.left = newLeft + 'px'; widget.style.top = newTop + 'px';
  }
  function onWidgetDragEnd() {
    if (isWidgetDragging) { isWidgetDragging = false; widget.style.transition = 'opacity 0.2s ease, transform 0.2s ease'; }
  }
  headerEl.addEventListener('mousedown', onWidgetDragStart);
  document.addEventListener('mousemove', onWidgetDragMove, {passive: false});
  document.addEventListener('mouseup', onWidgetDragEnd);
  headerEl.addEventListener('touchstart', onWidgetDragStart, {passive: false});
  document.addEventListener('touchmove', onWidgetDragMove, {passive: false});
  document.addEventListener('touchend', onWidgetDragEnd);

  /* --- CHAT LOGIC --- */
  function onInput(el) {
    el.style.height = 'auto'; el.style.height = Math.min(el.scrollHeight, 100) + 'px';
    sendBtnEl.disabled = !el.value.trim();
  }
  function onKey(e) {
    if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); send(); }
  }
  function scrollBottom() { conversEl.scrollTo({ top: conversEl.scrollHeight, behavior: 'smooth' }); }
  function esc(str) {
    return (str || '').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/\n/g,'<br>');
  }

  function botAvatar() {
    return `<div class="avatar avatar-bot"><svg width="14" height="12" viewBox="0 0 52 44" fill="none"><path d="M4 10 C4 6 7 4 10 4 C13 4 15 6 16 9 L20 26 L26 10 C27 6.5 29.5 4 33 4 C36.5 4 38.5 6.5 39.5 10 L44 26 L47.5 9 C48.5 6 50 4 52 4 L52 4 C50.5 8 48.5 16 46 28 C45 32 43 36 40 38 C37.5 39.5 35 39 33 37 C31 35 30 33 29 30 L26 20 L23 30 C22 33 21 35 19 37 C17 39 14.5 39.5 12 38 C9 36 7 32 6 28 C3.5 16 1.5 8 0 4 L2 4 C3 4 4 6 4 10 Z" fill="#2F80ED"/></svg></div>`;
  }
  function userAvatar() {
    return `<div class="avatar avatar-user"><svg width="14" height="14" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="8" r="4" fill="#FFFFFF"/><path d="M4 20c0-4 3.58-7 8-7s8 3 8 7" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/></svg></div>`;
  }

  function addUser(text, save = true) {
    const row = document.createElement('div');
    row.className = 'msg-row user-row';
    row.innerHTML = `${userAvatar()}<div class="bubble-col"><div class="bubble-user">${esc(text)}</div></div>`;
    conversEl.appendChild(row);
    scrollBottom();
    if (save) {
      chatHistory.push({ role: 'user', content: text });
      saveHistory();
    }
  }

  function toggleFeedback(btn, type) {
    const parent = btn.parentElement;
    parent.querySelectorAll('.feedback-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    // In a real app, send feedback to backend here.
  }

  function triggerContactSupport() {
    alert('This would navigate to the WiseIN Support Portal or open an email draft.');
  }

  function addBot(text, sources = [], save = true) {
    let srcHtml = '';
    if (sources && sources.length) {
      const cards = sources.map(s => `<div class="source-card"><div class="source-icon"><svg width="13" height="13" viewBox="0 0 24 24" fill="none"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" stroke="#2F80ED" stroke-width="2" stroke-linejoin="round"/><polyline points="14 2 14 8 20 8" stroke="#2F80ED" stroke-width="2" stroke-linejoin="round"/></svg></div><div class="source-details"><div class="source-title">${esc(s.name)}</div><div class="source-sub">WiseIN Knowledge Base</div></div></div>`).join('');
      srcHtml = `<button class="sources-btn" onclick="toggleSrc(this)"><svg class="sources-chevron" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><polyline points="6 9 12 15 18 9"/></svg>Sources</button><div class="sources-list">${cards}</div>`;
    }

    const safeHtml = DOMPurify.sanitize(marked.parse(text));
    
    // Evaluate fallback condition
    let fallbackHtml = '';
    if (text.toLowerCase().includes("couldn't find enough information") || text.toLowerCase().includes("contact wisein support")) {
      fallbackHtml = `<button class="action-btn primary" onclick="triggerContactSupport()">Contact Support</button>`;
    }

    const row = document.createElement('div');
    row.className = 'msg-row';
    row.innerHTML = `
      ${botAvatar()}
      <div class="bubble-col">
        <div class="bubble-bot">${safeHtml}</div>
        <div class="bot-actions-row">
          ${srcHtml}
          ${fallbackHtml}
          <button class="feedback-btn" onclick="toggleFeedback(this, 'up')" title="Helpful"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"></path></svg></button>
          <button class="feedback-btn" onclick="toggleFeedback(this, 'down')" title="Not helpful"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 15v4a3 3 0 0 0 3 3l4-9V2H5.72a2 2 0 0 0-2 1.7l-1.38 9a2 2 0 0 0 2 2.3zm7-13h2a2 2 0 0 1 2 2v7a2 2 0 0 1-2 2h-2"></path></svg></button>
        </div>
      </div>`;
    conversEl.appendChild(row);
    scrollBottom();
    
    if (save) {
      chatHistory.push({ role: 'bot', content: text, sources: sources, isError: false });
      saveHistory();
    }
  }

  function addBotError(text, failedQuery, save = true) {
    const row = document.createElement('div');
    row.className = 'msg-row';
    const escapedQuery = (failedQuery || '').replace(/'/g, "\\'").replace(/"/g, '&quot;');
    
    row.innerHTML = `
      ${botAvatar()}
      <div class="bubble-col">
        <div class="bubble-bot bubble-error">${esc(text)}</div>
        <div class="bot-actions-row">
           <button class="action-btn" onclick="askSuggestion('${escapedQuery}')">↻ Retry</button>
        </div>
      </div>`;
    conversEl.appendChild(row);
    scrollBottom();

    if (save) {
      chatHistory.push({ role: 'bot', content: text, isError: true, failedQuery: failedQuery });
      saveHistory();
    }
  }

  function showTyping() {
    const row = document.createElement('div');
    row.className = 'typing-row'; row.id = 'typing';
    row.innerHTML = `${botAvatar()}<div class="typing-bubble"><div class="dots"><div class="dot"></div><div class="dot"></div><div class="dot"></div></div><span class="typing-label">Checking WiseIN...</span></div>`;
    conversEl.appendChild(row);
    scrollBottom();
  }
  function hideTyping() { const el = document.getElementById('typing'); if (el) el.remove(); }
  function toggleSrc(btn) { const panel = btn.nextElementSibling; btn.classList.toggle('open', panel.classList.toggle('visible')); }

  function askSuggestion(q) {
    if (busy) return;
    inputEl.value = q;
    onInput(inputEl);
    send();
  }

  async function send() {
    const text = inputEl.value.trim();
    if (!text || busy) return;
    busy = true;

    if (!chatStarted) {
      chatStarted = true;
      welcomeEl.style.display = 'none';
    }

    inputEl.value = '';
    inputEl.style.height = '32px';
    sendBtnEl.disabled = true;
    inputEl.disabled = true;

    addUser(text);
    showTyping();

    let fullText = '';
    let sources = [];

    try {
      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: text })
      });

      hideTyping();

      if (!res.ok) {
        const err = await res.json().catch(() => ({}));
        addBotError(err.detail || 'Something went wrong while connecting to the AI service. Please try again.', text);
        return;
      }

      const row = document.createElement('div');
      row.className = 'msg-row';
      row.innerHTML = `${botAvatar()}<div class="bubble-col"><div class="bubble-bot" id="streaming-bubble"></div><div class="bot-actions-row" id="streaming-actions"></div></div>`;
      conversEl.appendChild(row);
      
      const bubble = row.querySelector('#streaming-bubble');
      const actionsRow = row.querySelector('#streaming-actions');
      
      const reader = res.body.getReader();
      const decoder = new TextDecoder();

      while (true) {
        const { value, done } = await reader.read();
        if (done) break;
        const chunkStr = decoder.decode(value, {stream: true});
        const lines = chunkStr.split('\n\n');
        for (const line of lines) {
          if (line.startsWith('data: ')) {
            const data = JSON.parse(line.substring(6));
            if (data.type === 'sources') {
              sources = data.sources;
            } else if (data.type === 'token') {
              fullText += data.content;
              bubble.innerHTML = DOMPurify.sanitize(marked.parse(fullText));
              scrollBottom();
            }
          }
        }
      }

      // STREAM FINISHED - Render actions
      let srcHtml = '';
      if (sources && sources.length > 0) {
        const cards = sources.map(s => `<div class="source-card"><div class="source-icon"><svg width="13" height="13" viewBox="0 0 24 24" fill="none"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" stroke="#2F80ED" stroke-width="2" stroke-linejoin="round"/><polyline points="14 2 14 8 20 8" stroke="#2F80ED" stroke-width="2" stroke-linejoin="round"/></svg></div><div class="source-details"><div class="source-title">${esc(s.name)}</div><div class="source-sub">WiseIN Knowledge Base</div></div></div>`).join('');
        srcHtml = `<button class="sources-btn" onclick="toggleSrc(this)"><svg class="sources-chevron" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><polyline points="6 9 12 15 18 9"/></svg>Sources</button><div class="sources-list">${cards}</div>`;
      }

      let fallbackHtml = '';
      if (fullText.toLowerCase().includes("couldn't find enough information") || fullText.toLowerCase().includes("contact wisein support")) {
        fallbackHtml = `<button class="action-btn primary" onclick="triggerContactSupport()">Contact Support</button>`;
      }

      actionsRow.innerHTML = `
        ${srcHtml}
        ${fallbackHtml}
        <button class="feedback-btn" onclick="toggleFeedback(this, 'up')" title="Helpful"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"></path></svg></button>
        <button class="feedback-btn" onclick="toggleFeedback(this, 'down')" title="Not helpful"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 15v4a3 3 0 0 0 3 3l4-9V2H5.72a2 2 0 0 0-2 1.7l-1.38 9a2 2 0 0 0 2 2.3zm7-13h2a2 2 0 0 1 2 2v7a2 2 0 0 1-2 2h-2"></path></svg></button>
      `;
      bubble.removeAttribute('id');
      actionsRow.removeAttribute('id');

      chatHistory.push({ role: 'bot', content: fullText, sources: sources, isError: false });
      saveHistory();

    } catch (e) {
      hideTyping();
      addBotError('Unable to reach the WiseIN support service. Please check your connection and try again.', text);
    } finally {
      busy = false;
      inputEl.disabled = false;
      onInput(inputEl);
      setTimeout(() => inputEl.focus(), 10);
    }
  }
</script>
</body>
</html>
"""

with open(r'C:\Users\marel\OneDrive\Desktop\wisein-ai-support\frontend\index.html', 'w', encoding='utf-8') as f:
    f.write(HTML_CONTENT)

print("All features 2-10 added successfully!")
