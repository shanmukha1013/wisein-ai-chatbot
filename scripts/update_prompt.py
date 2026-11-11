import os

with open('scripts/generate_answer.py', 'r', encoding='utf-8') as f:
    content = f.read()

new_system_prompt = """SYSTEM_PROMPT = \"\"\"You are the official WiseIN AI Support Assistant.

Your role is to answer questions from WiseIN users clearly, accurately, and professionally, using ONLY the information provided in the WiseIN Knowledge Base excerpts below.

RESPONSE STYLE RULES:
1. Keep normal support responses SHORT and conversational.
2. Prefer 2-5 sentences or 3-5 concise steps.
3. Do not dump documentation into the answer. Only provide information directly relevant to the user's question.
4. Do not repeat information the user already knows. Do not introduce unrelated features.
5. Do not list every possible troubleshooting category. Give the most relevant steps first.
6. Do not give long explanations unless the user explicitly asks for details or "why".
7. Use simple, natural customer-support language.
8. Ask at most ONE clarifying question when necessary.
9. Maintain conversation context from previous messages. Understand follow-ups like "no, it's not working".

HUMAN ESCALATION:
- If the user explicitly asks for a human, support person, customer care, or says the troubleshooting did not work, DO NOT give a long explanation.
- Respond briefly with: "Absolutely. I can help you reach WiseIN Support. Would you like to contact a support representative?"

RESTRICTIONS:
- DO NOT invent WiseIN features, UI elements, settings, policies, or workflows.
- DO NOT expose internal systems (e.g., "chunks", "Qdrant", "embeddings").
- If the retrieved documentation lacks sufficient info, politely say you don't have enough information and offer to connect them to WiseIN support.
\"\"\"
"""

# Replace SYSTEM_PROMPT
start_idx = content.find('SYSTEM_PROMPT = """')
if start_idx != -1:
    end_idx = content.find('"""\n', start_idx) + 4
    content = content[:start_idx] + new_system_prompt + content[end_idx:]

new_funcs = """def generate_answer_stream(query: str, chunks: List[Dict[str, Any]], history: List[Dict[str, str]] = None):
    \"\"\"
    Yields tokens from the Groq API as they are generated.
    \"\"\"
    if not client:
        yield "Error: GROQ_API_KEY is missing."
        return

    knowledge_block = ""
    for i, chunk in enumerate(chunks, 1):
        topic   = chunk.get("topic_name", "WiseIN")
        section = chunk.get("section", "")
        text    = chunk.get("chunk_text", "").strip()
        knowledge_block += f"\\n[Excerpt {i} - {topic} / {section}]\\n{text}\\n"
        
    system_message = SYSTEM_PROMPT + "\\n\\n--- WISEIN KNOWLEDGE BASE EXCERPTS ---\\n" + knowledge_block
    
    messages = [{"role": "system", "content": system_message}]
    
    if history:
        for msg in history[-6:]: # Keep last 6 messages for context
            # We filter out UI specific things like isError, sources, failedQuery
            # Just push role and content
            role = "assistant" if msg.get("role") == "bot" else "user"
            messages.append({"role": role, "content": msg.get("content", "")})
            
    messages.append({"role": "user", "content": query})

    try:
        stream = client.chat.completions.create(
            messages=messages,
            model=MODEL_NAME,
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS,
            stream=True
        )
        for chunk in stream:
            content = chunk.choices[0].delta.content
            if content is not None:
                yield content
    except Exception as e:
        yield f"I'm sorry, I encountered an error communicating with the AI service: {e}"

def generate_answer(query: str, chunks: List[Dict[str, Any]], history: List[Dict[str, str]] = None) -> str:
    return "".join(list(generate_answer_stream(query, chunks, history)))

def is_llm_ready() -> bool:
    return client is not None
"""

funcs_start = content.find('def build_prompt')
if funcs_start != -1:
    content = content[:funcs_start] + new_funcs

with open('scripts/generate_answer.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated prompt successfully!")
