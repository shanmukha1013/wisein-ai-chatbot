import sys
import os
from typing import List, Dict, Any
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None

MODEL_NAME = "qwen/qwen3.8-27b"
MAX_TOKENS = 384
TEMPERATURE = 0.2

SYSTEM_PROMPT = """You are the WiseIN AI Support Assistant.
Your knowledge comes from the provided WiseIN knowledge base excerpts.

Answer questions about WiseIN broadly, including the company, platform, people, features, workflows, policies, support, and troubleshooting when supported by the retrieved knowledge.
Use the retrieved information as your source of truth.

CORE PRINCIPLES:
1. Do not limit yourself to feature/how-to questions. General questions (e.g., "What is WiseIN?", "Who is Santosh?") are completely valid.
2. For general questions, provide a concise natural answer (1-3 sentences).
3. Provide direct, concise, and fast answers. Avoid conversational filler or introductory pleasantries (e.g., do not say 'Certainly! I would be happy to help with that'). Get straight to the point.
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


import hashlib
import json

SUMMARY_CACHE = {}

def get_bounded_history(history: List[Dict[str, str]]) -> tuple[str, List[Dict[str, str]]]:
    """
    Returns (summary_text, recent_history).
    Keeps the last 6 messages (3 turns) as recent.
    Summarizes everything before that, updating the summary in blocks of 6 to avoid extra LLM calls.
    """
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
            text_to_summarize += f"{role}: {m.get('content')}\n"
            
        prompt = f"Summarize the following conversation compactly. Focus on the user's main goals, issues, and what has already been resolved or discussed. Keep it under 3-4 sentences.\n\nConversation:\n{text_to_summarize}\n\nSummary:"
        
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

def generate_answer_stream(query: str, chunks: List[Dict[str, Any]], history: List[Dict[str, str]] = None):
    """
    Yields tokens from the Groq API as they are generated.
    """
    if not client:
        yield "Error: GROQ_API_KEY is missing."
        return

    knowledge_block = ""
    for i, chunk in enumerate(chunks, 1):
        topic   = chunk.get("topic_name", "WiseIN")
        section = chunk.get("section", "")
        text    = chunk.get("chunk_text", "").strip()
        knowledge_block += f"\n[Excerpt {i} - {topic} / {section}]\n{text}\n"
        
    system_message = SYSTEM_PROMPT + "\n\n--- WISEIN KNOWLEDGE BASE EXCERPTS ---\n" + knowledge_block
    
    messages = [{"role": "system", "content": system_message}]
    
    if history:
        summary, recent_messages = get_bounded_history(history)
        if summary:
            messages.append({"role": "system", "content": f"Previous Conversation Summary: {summary}"})
            
        for msg in recent_messages: 
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


def expand_query(query: str, history: List[Dict[str, str]] = None) -> str:
    """Uses the fast Groq model to rewrite/expand the query for better semantic retrieval."""
    if not client:
        return query
    
    # Simple history context
    hist_text = ""
    if history:
        for m in history[-3:]:
            role = "Assistant" if m.get("role") == "bot" else "User"
            hist_text += f"{role}: {m.get('content')}\n"
            
    prompt = f"""You are a search query expansion tool for the WiseIN knowledge base.
Your job is to take the user's query and generate a rich, semantic search string that will retrieve the best documents.

User Query: {query}
Recent Context: {hist_text}

Instructions:
1. Identify the core intent and fix any spelling mistakes (e.g., "wiesin" -> "WiseIN").
2. Generate exactly 3-5 highly relevant retrieval keywords.
3. Output ONLY the clean search string without any prefixes, labels, or conversational text. Do not over-expand.
4. Format: [corrected original query] [keyword1] [keyword2] [keyword3]

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

def is_llm_ready() -> bool:
    return client is not None


def analyze_screen_with_vision(image_base64: str, context: str) -> str:
    """
    Sends the base64 image to Groq's Vision model to understand the visible UI.
    """
    if not client:
        return "Error: GROQ_API_KEY is missing."
        
    if image_base64.startswith('data:image'):
        # Just safely grab the pure base64 if it has the data URI prefix
        pass
    else:
        # Prepend the data URI if missing (Groq requires URL format for images)
        image_base64 = f"data:image/jpeg;base64,{image_base64}"
        
    prompt = f"Analyze this screenshot of the WiseIN application. {context}\nDescribe the main UI elements visible, any open menus, and any error messages shown. Be concise."
    
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
