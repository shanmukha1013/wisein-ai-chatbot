with open('frontend/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace blue SVG fill with gray accent
text = text.replace('fill="#2F80ED"', 'fill="#495057"')
# Also update source icon stroke color from blue to gray
text = text.replace('stroke="#2F80ED"', 'stroke="#495057"')

with open('frontend/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('SVG fill and stroke colors updated.')
