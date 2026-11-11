import os

html_path = 'frontend/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Human Escalation Card in index.html to have a real Submit flow
old_escalation = """        <div class="escalation-card" id="streaming-escalation">
          <h3>Contact Support</h3>
          <p>Would you like to connect with a human support agent?</p>
          <div class="contact-links">
            <a href="mailto:support@wisein.com">✉ support@wisein.com</a>
            <a href="tel:+1800WISEIN">+1 (800) WISEIN</a>
          </div>
        </div>"""

new_escalation = """        <div class="escalation-card" id="streaming-escalation">
          <h3>Contact Support</h3>
          <p>Your conversation will be shared with the WiseIN support team so they can understand the issue without making you repeat everything.</p>
          <div class="confirm-actions" id="support-actions">
            <button class="btn-cancel" onclick="document.getElementById('streaming-escalation').remove()">Cancel</button>
            <button class="btn-confirm" onclick="submitSupportTicket()">Send Request</button>
          </div>
          <p id="support-status" style="font-size:12px; margin-top:10px; font-weight:600; display:none;"></p>
        </div>"""

if 'submitSupportTicket()' not in content:
    content = content.replace(old_escalation, new_escalation)

# 2. Add JS logic for the Support Ticket and Screen Assist
additional_js = """
  let activeConversationId = null;

  async function ensureConversation() {
    if (!activeConversationId) {
      const res = await fetch('/api/features/conversations', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({title: chatHistory[0]?.content.substring(0,20) || 'New Conversation'})
      });
      const data = await res.json();
      activeConversationId = data.id;
    }
  }

  async function submitSupportTicket() {
    const btnBox = document.getElementById('support-actions');
    const status = document.getElementById('support-status');
    btnBox.style.display = 'none';
    status.style.display = 'block';
    status.innerText = "Submitting...";

    await ensureConversation();
    
    try {
      const res = await fetch('/api/features/support/tickets', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
          conversation_id: activeConversationId,
          issue_summary: chatHistory.filter(m => m.role === 'user').pop()?.content || 'General Support Request'
        })
      });
      if(res.ok) {
        const data = await res.json();
        status.innerText = `Your support request has been submitted. (Ticket #` + data.ticket_id + `)`;
        status.style.color = 'green';
      } else {
        status.innerText = "Failed to submit request.";
        status.style.color = 'red';
      }
    } catch(e) {
      status.innerText = "Error connecting to support API.";
      status.style.color = 'red';
    }
  }

  async function logEvent(eventType) {
    try {
      await fetch('/api/features/analytics/event', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({event_type: eventType})
      });
    } catch (e) {}
  }

  async function startScreenAssist() {
    const chatBox = document.getElementById('chat-history');
    
    const warnHtml = `
      <div class="msg-row bot-row" id="screen-assist-warning">
        <div class="avatar bot-avatar">W</div>
        <div class="msg-bubble bot-bubble">
          <p><b>Screen Assist</b> lets me look at your current screen to help you. Only share a screen that doesn't contain sensitive information such as passwords, OTPs, or private messages.</p>
          <div class="confirm-actions" style="margin-top:10px;">
            <button class="btn-cancel" onclick="document.getElementById('screen-assist-warning').remove(); logEvent('screen_assist_cancelled')">Cancel</button>
            <button class="btn-confirm" onclick="executeScreenAssist()">Share Screen</button>
          </div>
        </div>
      </div>
    `;
    chatBox.insertAdjacentHTML('beforeend', warnHtml);
    forceScrollBottom();
    logEvent('screen_assist_started');
  }

  async function executeScreenAssist() {
    document.getElementById('screen-assist-warning').remove();
    
    let stream;
    try {
      stream = await navigator.mediaDevices.getDisplayMedia({ video: true });
    } catch(err) {
      appendMsg('bot', "That's okay. Screen Assist needs permission to view the selected screen. You can continue without it.");
      logEvent('screen_assist_denied');
      return;
    }
    
    appendMsg('bot', "Screen captured successfully. (Note: Vision LLM backend integration is mocked in this phase pending Groq Vision model provision).");
    stream.getTracks().forEach(track => track.stop());
    logEvent('screen_assist_completed');
  }
"""

if 'function submitSupportTicket()' not in content:
    content = content.replace('function showAuth() {', additional_js + '\n  function showAuth() {')
    
# Hook Screen Assist button into UI header
header_btn = '<button type="button" onclick="startScreenAssist()" title="Screen Assist" aria-label="Screen Assist" style="background:none; border:none; cursor:pointer; font-size:16px;">📷</button>'
content = content.replace('<button type="button" onclick="clearChatConfirm()"', header_btn + '\n      <button type="button" onclick="clearChatConfirm()"')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Frontend UI patched for Phase 3 & 6.")
