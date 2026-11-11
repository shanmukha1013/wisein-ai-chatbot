import re
with open('frontend/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I am looking for the literal string that has literal newlines
import re
content = re.sub(r"chunkStr\.split\('[\r\n\s]+'\);", "chunkStr.split('\\\\n\\\\n');", content)

with open('frontend/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
