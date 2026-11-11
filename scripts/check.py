with open('frontend/index.html', encoding='utf-8') as f:
    content = f.read()
import sys
idx = content.find('widget-container')
if idx != -1:
    print(content[idx-10:idx+400])
