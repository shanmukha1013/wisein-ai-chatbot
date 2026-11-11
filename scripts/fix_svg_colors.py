with open('frontend/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Launcher button SVG: white icon on dark gray background
#    Line ~350 - the launcher div SVG
text = text.replace(
    '<div id="w-launcher" class="w-launcher" role="button" tabindex="0" aria-label="Open WiseIN Support Chat">\n    <svg viewBox="0 0 52 44" fill="none">\n      <path d="M4 10 C4 6 7 4 10 4 C13 4 15 6 16 9 L20 26 L26 10 C27 6.5 29.5 4 33 4 C36.5 4 38.5 6.5 39.5 10 L44 26 L47.5 9 C48.5 6 50 4 52 4 L52 4 C50.5 8 48.5 16 46 28 C45 32 43 36 40 38 C37.5 39.5 35 39 33 37 C31 35 30 33 29 30 L26 20 L23 30 C22 33 21 35 19 37 C17 39 14.5 39.5 12 38 C9 36 7 32 6 28 C3.5 16 1.5 8 0 4 L2 4 C3 4 4 6 4 10 Z" fill="#495057"/>\n    </svg>\n  </div>',
    '<div id="w-launcher" class="w-launcher" role="button" tabindex="0" aria-label="Open WiseIN Support Chat">\n    <svg viewBox="0 0 52 44" fill="none">\n      <path d="M4 10 C4 6 7 4 10 4 C13 4 15 6 16 9 L20 26 L26 10 C27 6.5 29.5 4 33 4 C36.5 4 38.5 6.5 39.5 10 L44 26 L47.5 9 C48.5 6 50 4 52 4 L52 4 C50.5 8 48.5 16 46 28 C45 32 43 36 40 38 C37.5 39.5 35 39 33 37 C31 35 30 33 29 30 L26 20 L23 30 C22 33 21 35 19 37 C17 39 14.5 39.5 12 38 C9 36 7 32 6 28 C3.5 16 1.5 8 0 4 L2 4 C3 4 4 6 4 10 Z" fill="#FFFFFF"/>\n    </svg>\n  </div>'
)

# 2. Header icon SVG: blue accent color
text = text.replace('fill="#495057"/></svg></div>', 'fill="#2563eb"/></svg></div>')

# 3. Bot avatar SVG in JS: blue accent
text = text.replace(
    'fill="#495057"/></svg></div>`; }',
    'fill="#2563eb"/></svg></div>`; }'
)

# 4. Source card icons: blue accent  
text = text.replace('stroke="#495057" stroke-width="2" stroke-linejoin="round"/>', 'stroke="#2563eb" stroke-width="2" stroke-linejoin="round"/>')
text = text.replace('stroke="#495057" stroke-width="2" stroke-linejoin', 'stroke="#2563eb" stroke-width="2" stroke-linejoin')

with open('frontend/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('SVG colors updated successfully')
