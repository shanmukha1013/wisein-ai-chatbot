import os
import re

# ==========================================
# 1. UPDATE generate_answer.py for System Prompt and Intent/Expansion
# ==========================================
with open('scripts/generate_answer.py', 'r', encoding='utf-8') as f:
    content = f.read()

new_system_prompt = '''SYSTEM_PROMPT = """You are the WiseIN AI Support Assistant.
Your knowledge comes from the provided WiseIN knowledge base excerpts.

Answer questions about WiseIN broadly, including the company, platform, people, features, workflows, policies, support, and troubleshooting when supported by the retrieved knowledge.
Use the retrieved information as your source of truth.

CORE PRINCIPLES:
1. Do not limit yourself to feature/how-to questions. General questions (e.g., "What is WiseIN?", "Who is Santosh?") are completely valid.
2. For general questions, provide a concise natural answer (1-3 sentences).
3. For procedures, provide clear numbered steps.
4. For lists of concepts, use bullets.
5. Maintain conversational context. If the user says "it didn't work", they mean the previous instructions.
6. Never dump the raw knowledge base text into the answer. Synthesize a natural response.
7. Never invent information that is not supported by the excerpts.

HUMAN ESCALATION (CRITICAL):
If the user explicitly requests human support (e.g., "I want a human", "customer care", "talk to someone"), or if troubleshooting fails, DO NOT troubleshoot further.
Respond EXACTLY with:
"Absolutely. I can help you reach the WiseIN support team. You can contact them directly using the options below."
(The system will automatically attach the contact card).

If the available knowledge is truly insufficient after reviewing the excerpts, say so honestly: "I don't have enough information to give you a reliable answer to that." and offer human support.
"""
'''

# Replace SYSTEM_PROMPT
start_idx = content.find('SYSTEM_PROMPT = """')
if start_idx != -1:
    end_idx = content.find('"""\n', start_idx) + 4
    content = content[:start_idx] + new_system_prompt + content[end_idx:]

# Add query expansion function
expansion_func = '''
def expand_query(query: str, history: List[Dict[str, str]] = None) -> str:
    """Uses the fast Groq model to rewrite/expand the query for better semantic retrieval."""
    if not client:
        return query
    
    # Simple history context
    hist_text = ""
    if history:
        for m in history[-3:]:
            role = "Assistant" if m.get("role") == "bot" else "User"
            hist_text += f"{role}: {m.get('content')}\\n"
            
    prompt = f"""You are a search query expansion tool for the WiseIN knowledge base.
Your job is to take the user's query and generate a rich, semantic search string that will retrieve the best documents.

User Query: {query}
Recent Context: {hist_text}

Instructions:
1. Identify the core intent (e.g., general_company, founder_leadership, troubleshooting, feature_how_to).
2. Generate 3-5 keywords or concepts related to this intent.
3. Output ONLY the expanded search string. Do not include labels or conversational text.
4. Format: [original query] + [concept 1], [concept 2], [concept 3]

Example 1:
Query: Who is Santosh?
Output: Who is Santosh? Santosh, Founder, CEO, WiseIN leadership, Sanshi Network Tech

Example 2:
Query: What is WiseIN?
Output: What is WiseIN? WiseIN company overview, platform purpose, networking, professional platform

Generate the output for the current query:"""
    
    try:
        res = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="qwen/qwen3.8-27b",
            temperature=0.1,
            max_tokens=50
        )
        expanded = res.choices[0].message.content.strip()
        # Fallback if the model gets chatty
        if len(expanded) > 200:
            return query
        return expanded
    except Exception as e:
        print(f"Expansion failed: {e}")
        return query
'''

# insert before is_llm_ready
idx = content.find('def is_llm_ready()')
content = content[:idx] + expansion_func + "\n" + content[idx:]

with open('scripts/generate_answer.py', 'w', encoding='utf-8') as f:
    f.write(content)

# ==========================================
# 2. UPDATE api.py to use expansion and Top-K = 8
# ==========================================
with open('backend/api.py', 'r', encoding='utf-8') as f:
    api_content = f.read()

# Add import for expand_query
api_content = api_content.replace(
    'from generate_answer import generate_answer_stream, is_llm_ready, MODEL_NAME',
    'from generate_answer import generate_answer_stream, expand_query, is_llm_ready, MODEL_NAME'
)

# Update retrieval call
old_retrieve = "results = engine.retrieve(query, top_k=3)"
new_retrieve = """
    # 1. Expand query for better semantic match
    history_dict = [{"role": msg.role, "content": msg.content} for msg in req.history]
    expanded_search = expand_query(query, history=history_dict)
    print(f"Original Query: {query} | Expanded: {expanded_search}")
    
    # 2. Retrieve with higher Top-K (8) to capture broad and specific chunks
    results = engine.retrieve(expanded_search, top_k=8)
"""
api_content = api_content.replace(old_retrieve, new_retrieve)

with open('backend/api.py', 'w', encoding='utf-8') as f:
    f.write(api_content)

print("Applied General Knowledge and Expansion logic successfully.")
