import sys
import os
import time

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from retrieve import RetrievalEngine
from generate_answer import generate_answer

def run_evaluation():
    engine = RetrievalEngine()
    
    questions = [
        # Categories
        "What is WiseIN?", # 1. Intro
        "How do I sign up for an account?", # 2. Sign Up
        "How do I log in to my account?", # 3. Login
        "How do I verify my identity?", # 4. Identity Verification
        "How does student verification work?", # 5. Student Verification
        "What happens during onboarding?", # 6. Onboarding
        "Where can I update my profile?", # 7. Profile
        "How can I find jobs?", # 8. Jobs
        "How do I connect with people?", # 9. My Network
        "How do I book a meeting?", # 10. Meetings
        "What are organizations on WiseIN?", # 11. Organizations
        "How do I join a community?", # 12. Communities
        "How can I create an event?", # 13. Events
        "Why am I getting so many notifications?", # 14. Notifications
        "How do I make a payment?", # 15. Payments
        "Where is my billing history?", # 16. Billing
        "What are my privacy settings?", # 17. Privacy
        "How do I secure my account?", # 18. Security
        "I am not receiving my OTP. What should I do?", # 19. Troubleshooting
        "How do I delete my account?", # 20. Account Deletion
        "How do I use AI search?", # 21. AI Search
        "How do I use the AI Assistant?", # 22. AI Assistant
        
        # Behaviors
        "Where can I find the settings?", # Navigation
        "How do I verify?", # Ambiguous
        "How do I trade stocks on WiseIN?", # Unsupported WiseIN
        "What is the weather today?" # Unrelated
    ]

    report_path = r"C:\Users\marel\.gemini\antigravity\brain\3735faf2-7847-4bdb-a05b-550c46eca03a\evaluation_report.md"
    
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# WiseIN AI Support Evaluation Report\n\n")
        f.write("## Configuration\n")
        f.write("- **Ollama model used**: phi3.5\n")
        f.write("- **Model size**: 3.8B parameters (2.17GB)\n")
        f.write("- **Retrieval configuration**: top_k=3 (optimized for CPU processing time and context window)\n")
        f.write("- **Similarity threshold**: None applied for this test (relying on LLM grounding)\n\n")
        
    for q in questions:
        start_time = time.time()
        results = engine.retrieve(q, top_k=3)
        
        with open(report_path, "a", encoding="utf-8") as f:
            f.write(f"## Question: {q}\n")
            f.write("### Retrieved Topics:\n")
            for r in results:
                f.write(f"- {r.get('topic_name')} (Chunk: {r.get('chunk_id')}, Score: {r['score']:.4f})\n")
                
        try:
            answer = generate_answer(q, results)
        except Exception as e:
            answer = f"ERROR GENERATING ANSWER: {e}"
            
        elapsed = time.time() - start_time
            
        with open(report_path, "a", encoding="utf-8") as f:
            f.write("\n### Generated Answer:\n")
            f.write(f"{answer}\n")
            f.write(f"\n*(Generation took {elapsed:.1f}s)*\n")
            f.write("\n---\n\n")
            
    print("Evaluation complete.")

if __name__ == "__main__":
    run_evaluation()
