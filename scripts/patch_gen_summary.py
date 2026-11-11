import os

filepath = 'scripts/generate_answer.py'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add SUMMARY_CACHE and get_conversation_summary function
summary_code = """
import hashlib
import json

SUMMARY_CACHE = {}

def get_bounded_history(history: List[Dict[str, str]]) -> tuple[str, List[Dict[str, str]]]:
    \"\"\"
    Returns (summary_text, recent_history).
    Keeps the last 6 messages (3 turns) as recent.
    Summarizes everything before that, updating the summary in blocks of 6 to avoid extra LLM calls.
    \"\"\"
    if not history or len(history) <= 6:
        return "", history
        
    # We keep the last 6 messages as raw context.
    # We summarize history[:-6].
    # To avoid summarizing on EVERY message, we only update the summary when the slice to summarize grows by 6.
    # N is the number of messages to summarize.
    N = ((len(history) - 6) // 6) * 6
    
    if N <= 0:
        return "", history
        
    messages_to_summarize = history[:N]
    recent_messages = history[N:]
    
    # Create a cache key for these exact N messages
    cache_key = hashlib.md5(json.dumps(messages_to_summarize, sort_keys=True).encode('utf-8')).hexdigest()
    
    if cache_key in SUMMARY_CACHE:
        summary = SUMMARY_CACHE[cache_key]
    else:
        # Generate summary
        text_to_summarize = ""
        for m in messages_to_summarize:
            role = "Assistant" if m.get("role") == "bot" else "User"
            text_to_summarize += f"{role}: {m.get('content')}\\n"
            
        prompt = f"Summarize the following conversation compactly. Focus on the user's main goals, issues, and what has already been resolved or discussed. Keep it under 3-4 sentences.\\n\\nConversation:\\n{text_to_summarize}\\n\\nSummary:"
        
        try:
            res = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="qwen/qwen3.8-27b",
                temperature=0.1,
                max_tokens=150
            )
            summary = res.choices[0].message.content.strip()
            SUMMARY_CACHE[cache_key] = summary
        except Exception as e:
            print("Summarization failed:", e)
            summary = ""
            
    return summary, recent_messages
"""

if 'SUMMARY_CACHE = {}' not in content:
    # Inject imports and logic
    content = content.replace('def generate_answer_stream', summary_code + '\ndef generate_answer_stream')

# 2. Update generate_answer_stream to use the bounded history
old_history_logic = """
    if history:
        for msg in history[-6:]: # Keep last 6 messages for context
            # We filter out UI specific things like isError, sources, failedQuery
            # Just push role and content
            role = "assistant" if msg.get("role") == "bot" else "user"
            messages.append({"role": role, "content": msg.get("content", "")})
"""

new_history_logic = """
    if history:
        summary, recent_messages = get_bounded_history(history)
        if summary:
            messages.append({"role": "system", "content": f"Previous Conversation Summary: {summary}"})
            
        for msg in recent_messages: 
            role = "assistant" if msg.get("role") == "bot" else "user"
            messages.append({"role": role, "content": msg.get("content", "")})
"""

content = content.replace(old_history_logic, new_history_logic)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch applied to generate_answer.py")
