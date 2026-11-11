import os
import re

html_path = 'frontend/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the camera icon with the new proper Screen Assist icon
camera_btn = '<button type="button" onclick="startScreenAssist()" title="Screen Assist" aria-label="Screen Assist" style="background:none; border:none; cursor:pointer; font-size:16px;">📸</button>'
new_btn = """
        <button type="button" class="header-action-btn" onclick="startScreenAssistFlow()" title="Analyze my screen" aria-label="Analyze my screen">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect>
            <line x1="8" y1="21" x2="16" y2="21"></line>
            <line x1="12" y1="17" x2="12" y2="21"></line>
          </svg>
        </button>"""

if camera_btn in content:
    content = content.replace(camera_btn, new_btn)

# Add CSS for the new btn and preview
new_css = """
    .header-action-btn { background: none; border: none; cursor: pointer; color: var(--text-mid); padding: 4px; display: flex; align-items: center; justify-content: center; border-radius: 4px; transition: color 0.2s, background 0.2s; }
    .header-action-btn:hover { color: var(--blue); background: var(--bg); }
    .screen-preview { margin-top: 10px; border-radius: 8px; border: 1px solid var(--border); max-width: 100%; height: auto; }
    .screen-assist-active { border: 2px solid var(--blue) !important; background: var(--blue-light) !important; }
"""
content = content.replace('/* PREMIUM ANIMATIONS */', new_css + '\n    /* PREMIUM ANIMATIONS */')


# Remove the old startScreenAssist logic and replace it with the robust state machine
old_js_regex = re.compile(r'async function startScreenAssist\(\).*?logEvent\(\'screen_assist_completed\'\);\s*\}', re.DOTALL)
content = re.sub(old_js_regex, '', content)

new_js = """
  let activeScreenStream = null;
  let activeScreenFrameBase64 = null;

  async function startScreenAssistFlow() {
    if (activeScreenStream) {
      stopScreenAssist();
      return;
    }
    
    const warnHtml = `
      <div class="msg-row bot-row" id="screen-assist-consent">
        ${botAvatar()}
        <div class="bubble-col">
          <div class="bubble-bot">
            <p><strong>Need help with something on your screen?</strong></p>
            <p style="margin-top: 6px;">Screen Assist can look at the WiseIN page you're viewing and guide you step by step.</p>
            <p style="margin-top: 6px; font-size: 13px; color: var(--text-muted);">Only share what you're comfortable sharing. Do not include passwords, OTPs, payment details, or private messages.</p>
            <div class="confirm-actions" style="margin-top:12px; display:flex; gap:8px;">
              <button class="btn-cancel" onclick="document.getElementById('screen-assist-consent').remove(); logEvent('screen_assist_cancelled')">Cancel</button>
              <button class="btn-confirm" onclick="requestScreenPermission()">Analyze My Screen</button>
            </div>
          </div>
        </div>
      </div>
    `;
    conversEl.insertAdjacentHTML('beforeend', warnHtml);
    scrollBottom();
  }

  async function requestScreenPermission() {
    const consentNode = document.getElementById('screen-assist-consent');
    if (consentNode) consentNode.remove();

    if (!navigator.mediaDevices || !navigator.mediaDevices.getDisplayMedia) {
      addBotError("Screen Assist isn't available in this browser. You can still describe what you're seeing and I'll help you.", "screen_assist_unsupported", false);
      return;
    }

    try {
      activeScreenStream = await navigator.mediaDevices.getDisplayMedia({ video: true, audio: false });
      
      const track = activeScreenStream.getVideoTracks()[0];
      const imageCapture = new ImageCapture(track);
      
      // Capture a single frame
      const bitmap = await imageCapture.grabFrame();
      
      const canvas = document.createElement('canvas');
      canvas.width = bitmap.width;
      canvas.height = bitmap.height;
      const ctx = canvas.getContext('2d');
      ctx.drawImage(bitmap, 0, 0, canvas.width, canvas.height);
      
      // Compress frame as JPEG
      activeScreenFrameBase64 = canvas.toDataURL('image/jpeg', 0.6);
      
      // Stop the stream tracks immediately since we only need one frame
      track.stop();
      activeScreenStream = null;

      showScreenPreviewAndAnalyze();

    } catch (err) {
      activeScreenStream = null;
      addBotError("No problem. Screen Assist needs permission to view the screen you choose. You can continue describing the issue here and I'll help you.", "screen_assist_denied", false);
    }
  }

  function stopScreenAssist() {
    if (activeScreenStream) {
      activeScreenStream.getTracks().forEach(t => t.stop());
      activeScreenStream = null;
    }
    activeScreenFrameBase64 = null;
    const previewNode = document.getElementById('active-screen-preview');
    if (previewNode) previewNode.remove();
  }

  async function showScreenPreviewAndAnalyze() {
    // Inject the preview card
    const previewHtml = `
      <div class="msg-row user-row" id="active-screen-preview">
        <div class="bubble-col" style="align-items: flex-end;">
          <div class="bubble-user" style="background: var(--blue-light); border: 1px solid var(--blue); color: var(--text-dark);">
            <div style="font-weight: 600; font-size: 13px; margin-bottom: 8px;">Screen shared for this analysis</div>
            <img src="${activeScreenFrameBase64}" class="screen-preview" alt="Captured screen preview" />
            <div style="margin-top: 10px; text-align: right;">
              <button onclick="stopScreenAssist()" style="font-size: 12px; color: var(--blue); font-weight: 500; cursor: pointer; border:none; background:none;">Stop Screen Assist</button>
            </div>
          </div>
        </div>
      </div>
    `;
    conversEl.insertAdjacentHTML('beforeend', previewHtml);
    scrollBottom();

    // Now trigger the backend analysis
    await triggerScreenAnalysis();
  }

  async function triggerScreenAnalysis() {
    showTyping();
    const typingNode = document.getElementById('typing');
    if(typingNode) {
        typingNode.innerHTML = `${botAvatar()}<div class="bubble-col"><div class="bubble-bot" style="font-style:italic; font-size:13px; color:var(--text-mid);">Looking at the WiseIN page...</div></div>`;
    }

    try {
      const res = await fetch('/api/screen-assist/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          image_base64: activeScreenFrameBase64,
          history: chatHistory
        })
      });

      hideTyping();
      
      if (!res.ok) {
        const err = await res.json().catch(() => ({}));
        addBotError(err.detail || "I couldn't analyze that screen right now. You can try again or describe what you're seeing, and I'll help you from there.", "", false);
        return;
      }

      const data = await res.json();
      const row = document.createElement('div'); row.className = 'msg-row bot-row';
      row.innerHTML = `${botAvatar()}<div class="bubble-col"><div class="bubble-bot">${DOMPurify.sanitize(marked.parse(data.answer))}</div></div>`;
      conversEl.appendChild(row);
      scrollBottom();
      
      chatHistory.push({ role: 'bot', content: data.answer });
      saveHistory();

    } catch (err) {
      hideTyping();
      addBotError("I couldn't analyze that screen right now. You can try again or describe what you're seeing, and I'll help you from there.", "", false);
    } finally {
      // Discard image memory
      activeScreenFrameBase64 = null;
    }
  }
"""

content = content.replace('let activeConversationId = null;', new_js + '\n  let activeConversationId = null;')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Screen Assist UI fully patched.")
