# RAG Knowledge

## Source: 77.pdf

77. RAG Knowledge 
Overview 
RAG (Retrieval-Augmented Generation) is the core knowledge mechanism for the WiseIN AI 
Assistant. 
Instead of relying only on the AI model's built-in knowledge, the WiseIN Assistant should 
retrieve relevant information from the official WiseIN knowledge base and use that information 
to generate its response. 
This allows the chatbot to answer WiseIN-specific questions using documented information 
rather than guessing. 
Core Principle 
Retrieve first. Answer second. Never guess when the required information is 
unavailable. 
 
77.1 Purpose of RAG 
The RAG system is responsible for connecting the AI Assistant with WiseIN's documentation. 
It should help the AI: 
●​ Find relevant WiseIN information. 
●​ Answer feature-related questions. 
●​ Provide accurate navigation steps. 
●​ Explain policies. 
●​ Troubleshoot documented issues. 
●​ Answer FAQs. 
●​ Handle follow-up questions. 
●​ Reduce hallucinations. 
●​ Identify knowledge gaps. 
●​ Support human escalation. 
 

77.2 Why WiseIN Needs RAG 
A general AI model may know how chatbots and social platforms generally work, but that does 
not mean it knows the exact WiseIN workflow. 
For example, the AI model may know what account deletion generally means. 
However, WiseIN has its own documented workflow: 
Settings → Delete Account 
The RAG system retrieves WiseIN's actual documentation so the AI can provide the correct 
WiseIN-specific answer. 
 
77.3 RAG Architecture 
The basic WiseIN RAG flow is: 
               USER 
                  │ 
                  ▼ 
          User Question 
                  │ 
                  ▼ 
          Intent Detection 
                  │ 
                  ▼ 
       Query Understanding 
                  │ 
                  ▼ 
        Knowledge Retrieval 
                  │ 
                  ▼ 
       WiseIN Knowledge Base 
                  │ 
                  ▼ 
       Relevant Documents 
                  │ 
                  ▼ 
          AI Model / LLM 
                  │ 

                  ▼ 
        Context-Aware Answer 
                  │ 
                  ▼ 
                USER 
 
77.4 RAG Components 
The WiseIN RAG system consists of several major components. 
1. Knowledge Base 
Contains the approved WiseIN documentation. 
2. Document Processing 
Converts documentation into searchable pieces. 
3. Embeddings 
Converts text into numerical representations that allow semantic search. 
4. Vector Database 
Stores and searches the document embeddings. 
5. Retriever 
Finds the most relevant information for the user's question. 
6. LLM 
Uses the retrieved information to generate the final response. 
7. Conversation Context 
Provides relevant information from the current conversation. 
 

77.5 WiseIN Knowledge Base 
The knowledge base is the source of truth for WiseIN-specific customer support. 
The documentation we are creating should eventually form the foundation of this knowledge 
base. 
Examples include: 
●​ 01–50 platform features 
●​ 51 Saved Content 
●​ 52 Ads 
●​ 53 Subscriptions 
●​ 54 Payments 
●​ 55 Billing 
●​ 56 Privacy 
●​ 57 Security 
●​ 58 Blocking 
●​ 59 Reporting 
●​ 60 Community Guidelines 
●​ 61 Content Policies 
●​ 62 Terms & Conditions 
●​ 63 Account Deactivation 
●​ 64 Account Deletion 
●​ 65 Logout 
●​ 66 Troubleshooting 
●​ 67 Error Codes 
●​ 68 Customer Support 
●​ 69 Human Escalation 
●​ 70 FAQ 
●​ 71 Mobile App 
●​ 72 Website 
●​ 73 AI Assistant 
●​ 74 AI Limitations 
●​ 75 Conversation History 
●​ 76 AI Tools 
These documents can be processed into the RAG knowledge base. 
 
77.6 Document Structure 

For better retrieval, every document should have a consistent structure. 
Recommended structure: 
Document ID 
Title 
Category 
Description 
Features 
User Workflows 
Troubleshooting 
FAQs 
Limitations 
Escalation Information 
Related Documents 
Last Updated 
Example 
Document ID: 63 
Title: Account Deactivation 
Category: Account Management 
 
Purpose: 
Explain how users can temporarily deactivate their account. 
 
Workflow: 
Settings → Deactivate 
 
Behavior: 
Account is temporarily paused. 
 
Related: 
64 Account Deletion 
65 Logout 
56 Privacy 
This structure makes the information easier to retrieve and maintain. 
 
77.7 Document Chunking 

Large documents should not necessarily be inserted into the vector database as one large 
block. 
They should be divided into meaningful chunks. 
For example: 
63 Account Deactivation 
    │ 
    ├── Purpose 
    ├── How to Deactivate 
    ├── What Happens After Deactivation 
    ├── Reactivation 
    ├── FAQ 
    └── Limitations 
Each section can become an individual searchable unit while retaining its document metadata. 
 
77.8 Why Chunking Matters 
Suppose a user asks: 
"Can I temporarily stop using WiseIN without deleting my account?" 
The system should retrieve the specific information about deactivation, rather than loading the 
entire account-management documentation. 
Better retrieval means: 
Smaller relevant context → Less unnecessary information → More focused AI response 
 
77.9 Metadata 
Every knowledge chunk should contain metadata. 
Recommended metadata fields include: 
Field 
Example 

Document ID 
63 
Title 
Account Deactivation 
Category 
Account Management 
Section 
How to Deactivate 
Platform 
Website 
Source 
WiseIN Documentation 
Version 
1.0 
Status 
Active 
Last Updated 
June 2026 
Metadata allows the retrieval system to filter and organize information more effectively. 
 
77.10 Embeddings 
An embedding converts a piece of text into a numerical representation. 
For example: 
"How can I temporarily disable my account?" 
and: 
"How do I deactivate my WiseIN account?" 
use different words but have a similar meaning. 
Semantic embeddings allow the retrieval system to recognize that relationship. 
 
77.11 Vector Database 
The generated embeddings can be stored in a vector database. 

The vector database allows the system to search for documentation based on semantic 
similarity. 
Possible technologies for implementation include: 
●​ Qdrant 
●​ PostgreSQL with pgvector 
●​ Pinecone 
●​ Weaviate 
●​ Other suitable vector databases 
The final technology should be selected based on WiseIN's infrastructure and project 
requirements. 
 
77.12 Retrieval Process 
When a user asks a question: 
Step 1 — User Query 
"I don't want to permanently delete my WiseIN account. Can I disable it?" 
Step 2 — Query Processing 
The system identifies concepts such as: 
●​ Account 
●​ Temporary 
●​ Disable 
●​ Delete 
Step 3 — Retrieval 
The system searches the knowledge base. 
Step 4 — Relevant Document 
It retrieves: 
63 — Account Deactivation 
Step 5 — Context Construction 

The retrieved content is provided to the AI model. 
Step 6 — Response 
The AI generates: 
"Yes. If you want to temporarily stop using WiseIN without permanently deleting 
your account, go to Settings → Deactivate." 
 
77.13 Hybrid Search 
For a production customer-support system, the RAG system can use both: 
Semantic Search 
Understands meaning. 
Keyword Search 
Matches exact words and phrases. 
This is especially useful for: 
●​ Error messages 
●​ Feature names 
●​ Policy names 
●​ Navigation labels 
●​ Exact terminology 
Example 
User enters: 
"Failed to fetch" 
Keyword matching can identify the exact error while semantic search can retrieve related 
Google Sign-In troubleshooting information. 
 

77.14 Retrieval Ranking 
The system may retrieve multiple relevant chunks. 
These should be ranked according to relevance before being provided to the AI. 
For example: 
1. 67 Error Codes — Failed to fetch 
2. 70 FAQ — Login Problems 
3. 72 Website — Google Sign-In 
4. 68 Customer Support 
The most relevant information should receive the highest priority. 
 
77.15 Context Construction 
The AI model should receive: 
1.​ The user's current question. 
2.​ Relevant conversation history. 
3.​ Retrieved WiseIN documentation. 
4.​ Appropriate instructions for answering. 
Conceptually: 
SYSTEM INSTRUCTIONS 
        + 
CONVERSATION CONTEXT 
        + 
RETRIEVED WISEIN DOCUMENTATION 
        + 
USER QUESTION 
        ↓ 
       LLM 
        ↓ 
   FINAL ANSWER 
 

77.16 RAG Grounding 
The AI should ground WiseIN-specific answers in retrieved documentation. 
Example 
Retrieved information: 
Settings → Delete Account​
 Account deletion is permanent and cannot be undone. 
AI Response: 
"Go to Settings → Delete Account. WiseIN states that account deletion is 
permanent and cannot be undone." 
The answer is directly grounded in the retrieved information. 
 
77.17 Preventing Hallucinations 
RAG helps reduce hallucinations, but RAG alone does not guarantee that the AI will never 
hallucinate. 
The system should therefore include an instruction such as: 
Answer using the retrieved WiseIN information. If the required information is 
not available, do not invent an answer. State that the information is 
unavailable and provide the appropriate support path. 
This follows the principles defined in 74 — AI Limitations. 
 
77.18 Handling Unknown Questions 
If retrieval returns no sufficiently relevant information: 
User Question 
      ↓ 
Knowledge Search 

      ↓ 
No Reliable Result 
      ↓ 
Do Not Guess 
      ↓ 
Ask Clarifying Question 
or 
Human Escalation 
Example 
User: 
"Can I transfer my WiseIN subscription to another person?" 
If the knowledge base does not contain this information: 
"I don't have confirmed WiseIN information about transferring subscriptions to 
another person, so I don't want to guess. Please contact WiseIN support for 
confirmation." 
 
77.19 RAG & Conversation History 
RAG should work together with conversation history. 
Example 
User: 
"I can't save my education information." 
The AI retrieves relevant documentation. 
User: 
"The OTP never arrives." 
The AI should combine: 
Conversation Context 
●​ 

OTP Documentation 
to understand that the user is now describing a specific part of the original problem. 
 
77.20 RAG & Human Escalation 
If the RAG system cannot provide enough information to resolve an issue, the AI should 
escalate. 
Flow 
User Question 
      ↓ 
RAG Search 
      ↓ 
Relevant Information? 
   /          \ 
 YES           NO 
  │             │ 
  ▼             ▼ 
Answer      Don't Guess 
                │ 
                ▼ 
        Clarify / Escalate 
 
77.21 Knowledge Sources 
The RAG system should prioritize trusted WiseIN sources. 
Recommended priority: 
1. Official WiseIN Documentation 
Primary source. 
2. Approved Internal Documentation 
Information created and approved by the WiseIN team. 

3. Official Policies 
Examples: 
●​ Privacy Policy 
●​ Content Policies 
●​ Community Guidelines 
●​ Terms & Conditions 
4. Approved Support Documentation 
Troubleshooting guides and support procedures. 
External information should not override official WiseIN documentation for WiseIN-specific 
functionality. 
 
77.22 Knowledge Versioning 
WiseIN documentation will change over time. 
The RAG system should therefore support document versions. 
Example: 
Account Deactivation 
Version: 1.0 
Status: Archived 
 
Account Deactivation 
Version: 2.0 
Status: Active 
Only the currently active documentation should normally be used for current user responses. 
 
77.23 Knowledge Updates 
When WiseIN changes a feature: 
Product Change 

↓ 
Documentation Updated 
↓ 
Old Information Marked Outdated 
↓ 
New Document Indexed 
↓ 
RAG Retrieval Uses Updated Information 
This helps prevent the AI from continuing to provide outdated instructions. 
 
77.24 Knowledge Quality 
The quality of the RAG system depends heavily on the quality of the documentation. 
Poor Knowledge Base 
Incomplete information​
 ↓​
 Poor retrieval​
 ↓​
 Poor AI responses 
Good Knowledge Base 
Clear documentation​
 ↓​
 Better retrieval​
 ↓​
 More accurate AI responses 
Therefore: 
The knowledge base is not just supporting material—it is a core component 
of the WiseIN AI Assistant. 

 
77.25 Knowledge Gaps 
The RAG system should help identify questions that cannot be answered from existing 
documentation. 
Examples: 
●​ Frequently asked undocumented questions. 
●​ New features without documentation. 
●​ Missing troubleshooting procedures. 
●​ Ambiguous workflows. 
●​ Outdated documentation. 
These questions should be collected and reviewed by the WiseIN team. 
 
77.26 RAG Evaluation 
The RAG system should be tested using real and representative WiseIN questions. 
Evaluation should include: 
Retrieval Accuracy 
Did the system retrieve the correct document? 
Answer Accuracy 
Did the AI answer using the retrieved information? 
Grounding 
Is the answer supported by the retrieved content? 
Completeness 
Did the answer contain the important information? 
Hallucination Rate 

Did the AI introduce unsupported information? 
Escalation Accuracy 
Did the AI escalate when it should? 
 
77.27 Example Evaluation 
Question 
"How do I delete my WiseIN account?" 
Expected Retrieval 
64 — Account Deletion 
Expected Answer 
"Go to Settings → Delete Account. Account deletion is permanent and cannot be 
undone." 
Incorrect Retrieval 
63 — Account Deactivation 
This could lead to the wrong workflow. 
Therefore, retrieval quality must be tested independently from the AI's response quality. 
 
77.28 Recommended RAG Pipeline 
For the WiseIN project, the conceptual pipeline is: 
WiseIN Documentation 
        ↓ 
Document Cleaning 
        ↓ 
Document Chunking 

        ↓ 
Metadata Creation 
        ↓ 
Embedding Generation 
        ↓ 
Vector Database 
        ↓ 
Retriever 
        ↓ 
Relevant Context 
        ↓ 
LLM 
        ↓ 
Grounded Response 
 
77.29 RAG Technology Layer 
A possible implementation stack could be: 
Component 
Possible Technology 
Documentation 
Markdown / structured documents 
Backend 
Python / FastAPI 
Embeddings 
Embedding Model 
Vector Store 
Qdrant / pgvector 
Retrieval 
Semantic + Keyword Search 
LLM 
Approved AI API 
Conversation 
Storage 
Application Database 
Support Integration 
WiseIN Support System 
These are implementation options, not confirmed WiseIN production technologies. 
The final stack should be decided based on WiseIN's technical requirements and infrastructure. 
 

77.30 RAG Security 
The RAG system must prevent unauthorized information from being retrieved. 
The knowledge base should distinguish between: 
●​ Public information 
●​ User-facing support information 
●​ Internal documentation 
●​ Sensitive/internal information 
The AI should only retrieve information appropriate for the user's context. 
 
77.31 RAG Data Protection 
The knowledge base should not contain unnecessary sensitive user information. 
It should primarily contain product and support documentation, rather than personal 
customer data. 
User-specific information should be accessed only through authorized systems when required 
for a support case. 
 
77.32 RAG + AI Assistant + Tools 
The complete WiseIN AI system can be represented as: 
                        USER 
                           │ 
                           ▼ 
                  ┌─────────────────┐ 
                  │  AI ASSISTANT   │ 
                  └────────┬────────┘ 
                           │ 
             ┌─────────────┼─────────────┐ 
             │             │             │ 
             ▼             ▼             ▼ 
       Conversation     Intent       AI Tools 

         History       Detection 
             │             │             │ 
             └─────────────┼─────────────┘ 
                           │ 
                           ▼ 
                    ┌─────────────┐ 
                    │ RAG SYSTEM  │ 
                    └──────┬──────┘ 
                           │ 
                           ▼ 
                 ┌──────────────────┐ 
                 │ WiseIN Knowledge  │ 
                 │      Base         │ 
                 └────────┬─────────┘ 
                          │ 
                          ▼ 
                 Relevant Information 
                          │ 
                          ▼ 
                    ┌─────────────┐ 
                    │     LLM     │ 
                    └──────┬──────┘ 
                           │ 
                           ▼ 
                     AI RESPONSE 
                           │ 
                    ┌──────┴──────┐ 
                    │             │ 
                 Resolved      Unresolved 
                    │             │ 
                    ▼             ▼ 
                  USER     Human Escalation 
 
77.33 RAG Golden Rules 
The WiseIN RAG system should follow these rules: 
1.​ Use WiseIN documentation as the primary source of truth. 
2.​ Retrieve relevant information before answering WiseIN-specific questions. 
3.​ Use semantic and keyword retrieval where appropriate. 
4.​ Preserve document metadata and version information. 
5.​ Use conversation history as supporting context. 

6.​ Do not retrieve or expose unauthorized information. 
7.​ Do not invent information when retrieval fails. 
8.​ Escalate unresolved questions when necessary. 
9.​ Regularly update outdated documentation. 
10.​Evaluate retrieval quality separately from answer quality. 
 
77.34 Final Principle 
The WiseIN RAG system is the knowledge layer connecting the AI model to WiseIN's actual 
product documentation. 
The overall relationship is: 
Knowledge Base = Source of Truth​
 RAG = Finds the Truth​
 LLM = Explains the Truth​
 Conversation History = Provides Context​
 AI Tools = Provide Capabilities​
 Human Support = Handles What AI Cannot Resolve 
 



---

