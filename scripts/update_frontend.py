import re

with open('frontend/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_send = '''  async function send() {
    const text = inputEl.value.trim();
    if (!text || busy) return;
    busy = true;

    if (!chatStarted) {
      chatStarted = true;
      welcomeEl.style.display = 'none';
      conversEl.style.display = 'flex';
    }

    inputEl.value = '';
    inputEl.style.height = 'auto';
    sendBtnEl.disabled = true;

    addUser(text);
    showTyping();

    try {
      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: text })
      });

      hideTyping();

      if (!res.ok) {
        const err = await res.json().catch(() => ({}));
        addBot(err.detail || 'Something went wrong. Please try again.');
        busy = false;
        inputEl.focus();
        return;
      }

      const row = document.createElement('div');
      row.className = 'msg-row';
      row.innerHTML = `
        ${botAvatar()}
        <div class="bubble-col">
          <div class="bubble-bot" id="streaming-bubble"></div>
        </div>`;
      conversEl.appendChild(row);
      const bubble = row.querySelector('#streaming-bubble');
      let fullText = '';
      let sources = [];

      const reader = res.body.getReader();
      const decoder = new TextDecoder();

      while (true) {
        const { value, done } = await reader.read();
        if (done) break;

        const chunkStr = decoder.decode(value, {stream: true});
        const lines = chunkStr.split('\\n\\n');

        for (const line of lines) {
          if (line.startsWith('data: ')) {
            const data = JSON.parse(line.substring(6));
            if (data.type === 'sources') {
              sources = data.sources;
            } else if (data.type === 'token') {
              fullText += data.content;
              bubble.innerHTML = esc(fullText);
              scrollBottom();
            }
          }
        }
      }

      if (sources.length > 0) {
        const cards = sources.map(s => `
          <div class="source-card">
            <div class="source-icon">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none">
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" stroke="#2F80ED" stroke-width="2" stroke-linejoin="round"/>
                <polyline points="14 2 14 8 20 8" stroke="#2F80ED" stroke-width="2" stroke-linejoin="round"/>
              </svg>
            </div>
            <div class="source-details">
              <div class="source-title">${esc(s.name)}</div>
              <div class="source-sub">WiseIN Knowledge Base</div>
            </div>
          </div>`).join('');

        const srcHtml = `
          <button class="sources-btn" onclick="toggleSrc(this)">
            <svg class="sources-chevron" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><polyline points="6 9 12 15 18 9"/></svg>
            Sources
          </button>
          <div class="sources-list">${cards}</div>`;

        row.querySelector('.bubble-col').innerHTML += srcHtml;
        scrollBottom();
      }
      
      bubble.removeAttribute('id');

    } catch (e) {
      hideTyping();
      addBot('Unable to reach the WiseIN support service. Please check your connection and try again.');
    }

    busy = false;
    inputEl.focus();
  }'''

content = re.sub(r'  async function send\(\) \{.*\}', new_send, content, flags=re.DOTALL)

with open('frontend/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated frontend logic successfully.')
