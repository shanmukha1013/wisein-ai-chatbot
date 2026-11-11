import os

html_path = 'frontend/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# The HTML string for the overlay
overlay_html = """
      <div id="confirm-overlay" class="confirm-overlay">
        <div class="confirm-card">
          <h4>Start a new conversation?</h4>
          <p>Your current conversation will be cleared and you'll start with a fresh chat.</p>
          <div class="confirm-actions">
            <button class="btn-cancel" onclick="closeConfirm()">Cancel</button>
            <button class="btn-confirm" onclick="executeClearChat()">Start New Chat</button>
          </div>
        </div>
      </div>"""

# Remove the overlay from its current position
content = content.replace(overlay_html, "")

# Insert the overlay right before the closing tag of widget-container
# The widget container ends with:
#     <div class="footer"><div class="footer-text">By chatting with us, you agree to our Privacy Policy</div></div>
#   </div>
target = '    </div>\n  </div>'
if target in content:
    content = content.replace(target, '    </div>\n' + overlay_html + '\n  </div>')
else:
    # fallback
    target2 = 'By chatting with us, you agree to our Privacy Policy</div></div>\n    </div>'
    content = content.replace(target2, target2 + overlay_html)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Overlay moved to widget-container root.")
