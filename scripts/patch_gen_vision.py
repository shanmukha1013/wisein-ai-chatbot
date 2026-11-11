import os

gen_path = 'scripts/generate_answer.py'
with open(gen_path, 'r', encoding='utf-8') as f:
    content = f.read()

vision_func = """
def analyze_screen_with_vision(image_base64: str, context: str) -> str:
    \"\"\"
    Sends the base64 image to Groq's Vision model to understand the visible UI.
    \"\"\"
    if not client:
        return "Error: GROQ_API_KEY is missing."
        
    if image_base64.startswith('data:image'):
        # Just safely grab the pure base64 if it has the data URI prefix
        pass
    else:
        # Prepend the data URI if missing (Groq requires URL format for images)
        image_base64 = f"data:image/jpeg;base64,{image_base64}"
        
    prompt = f"Analyze this screenshot of the WiseIN application. {context}\\nDescribe the main UI elements visible, any open menus, and any error messages shown. Be concise."
    
    try:
        # We attempt to use llama-3.2-11b-vision-preview
        res = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {"type": "image_url", "image_url": {"url": image_base64}}
                    ]
                }
            ],
            model="llama-3.2-11b-vision-preview",
            temperature=0.1,
            max_tokens=200
        )
        return res.choices[0].message.content.strip()
    except Exception as e:
        error_str = str(e)
        if "not found" in error_str.lower() or "does not exist" in error_str.lower():
            return "Error: The configured Vision model (llama-3.2-11b-vision-preview) is not available on this Groq account. Please provision a vision-capable model to enable Screen Assist."
        return f"Error: Vision analysis failed - {error_str}"
"""

if 'def analyze_screen_with_vision' not in content:
    content += '\n' + vision_func
    with open(gen_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Vision function added to generate_answer.py")
