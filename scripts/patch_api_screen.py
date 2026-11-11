import os

api_path = 'backend/api.py'
with open(api_path, 'r', encoding='utf-8') as f:
    content = f.read()

screen_endpoint = """
class ScreenAnalysisRequest(BaseModel):
    image_base64: str
    history: list[Message] = []

@app.post("/api/screen-assist/analyze")
async def analyze_screen(req: ScreenAnalysisRequest):
    if not is_llm_ready():
        raise HTTPException(status_code=503, detail="LLM service is not ready.")
    
    # Extract the user's last issue from history if available
    user_context = "User shared their screen for assistance."
    if req.history:
        for msg in reversed(req.history):
            if msg.role == 'user':
                user_context = f"User's last question: {msg.content}"
                break
                
    # 1. Vision Model processing
    from generate_answer import analyze_screen_with_vision
    
    vision_description = analyze_screen_with_vision(req.image_base64, user_context)
    if vision_description.startswith("Error:"):
        raise HTTPException(status_code=500, detail=vision_description)
        
    # 2. RAG Retrieval using the vision context
    # Create a synthetic query representing what we see and what the user asked
    synthetic_query = f"{user_context}. Visible on screen: {vision_description[:200]}"
    results = engine.retrieve(synthetic_query, top_k=5)
    
    # 3. Final AI Answer using text model
    from generate_answer import generate_answer
    final_answer = generate_answer(
        query=f"I have shared my screen. {user_context}\\n\\nScreen Analysis: {vision_description}\\n\\nPlease give me concise, step-by-step instructions based on what is visible on my screen and the WiseIN knowledge base.", 
        chunks=results, 
        history=[{"role": m.role, "content": m.content} for m in req.history]
    )
    
    return {"answer": final_answer}
"""

if '/api/screen-assist/analyze' not in content:
    content = content.replace('@app.post("/api/chat")', screen_endpoint + '\n\n@app.post("/api/chat")')
    with open(api_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Screen Assist endpoint added to api.py")
