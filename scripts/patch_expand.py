import os

filepath = 'scripts/generate_answer.py'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace expand_query instructions
old_instructions = """Instructions:
1. Identify the core intent (e.g., general_company, founder_leadership, troubleshooting, feature_how_to).
2. Generate 3-5 keywords or concepts related to this intent.
3. Output ONLY the expanded search string. Do not include labels or conversational text.
4. Format: [original query] + [concept 1], [concept 2], [concept 3]"""

new_instructions = """Instructions:
1. Identify the core intent and fix any spelling mistakes (e.g., "wiesin" -> "WiseIN").
2. Generate exactly 3-5 highly relevant retrieval keywords.
3. Output ONLY the clean search string without any prefixes, labels, or conversational text. Do not over-expand.
4. Format: [corrected original query] [keyword1] [keyword2] [keyword3]"""

content = content.replace(old_instructions, new_instructions)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Expanded query logic patched.")
