# Conversation History

## Source: 75.pdf

75. Conversation History 
Overview 
The Conversation History feature allows the WiseIN AI Assistant to maintain the context of an 
ongoing conversation so that users do not have to repeat the same information multiple times. 
For the WiseIN AI customer-support system, conversation history is important because many 
support issues require multiple questions, troubleshooting steps, and follow-ups before the 
problem is resolved or escalated to human support. 
 
75.1 Purpose 
Conversation history should help the AI Assistant: 
●​ Understand what the user has already explained. 
●​ Remember relevant details during the current conversation. 
●​ Avoid asking the same questions repeatedly. 
●​ Track troubleshooting steps already attempted. 
●​ Understand follow-up questions. 
●​ Provide context-aware responses. 
●​ Prepare relevant information for human escalation. 
Core Principle 
The AI should remember relevant conversation context without making the 
user repeatedly explain the same problem. 
 
75.2 Example Conversation 
Without Conversation History 
User:​
 "I can't log in." 

AI:​
 "What problem are you experiencing?" 
User:​
 "I already told you. I can't log in." 
This creates a poor support experience. 
With Conversation History 
User:​
 "I can't log in." 
AI:​
 "Are you using Google Sign-In or another login method?" 
User:​
 "Google." 
AI:​
 "Are you seeing any error message?" 
User:​
 "Yes, it says 'Failed to fetch.'" 
The AI now knows: 
●​ The issue is login-related. 
●​ The user is using Google Sign-In. 
●​ The error is "Failed to fetch." 
It can directly provide the documented troubleshooting steps. 
 
75.3 What Should Be Remembered 
The AI should retain information that is relevant to solving the user's current issue. 
Examples: 
●​ User's current problem. 
●​ Feature involved. 
●​ Error message. 
●​ Steps already attempted. 

●​ Relevant answers provided by the user. 
●​ Troubleshooting already completed. 
●​ Whether the issue was resolved. 
●​ Whether the user requested human support. 
●​ Information required for escalation. 
 
75.4 What Should Not Be Repeated 
The AI should avoid asking the user for information they have already provided in the current 
conversation. 
Example 
User:​
 "I'm unable to receive my OTP." 
AI:​
 "Please check your contact information and request another OTP." 
User:​
 "I already checked it and requested another OTP." 
The AI should recognize that these steps have already been attempted. 
It should move to the next relevant step or human escalation instead of repeating: 
"Please check your contact information and request another OTP." 
 
75.5 Conversation Context 
The AI should understand references such as: 
●​ "It still doesn't work." 
●​ "I already tried that." 
●​ "What about the other option?" 
●​ "Can I delete it instead?" 
●​ "How do I undo that?" 
●​ "What should I do next?" 

Example 
User:​
 "How do I deactivate my account?" 
AI:​
 "Go to Settings → Deactivate." 
User:​
 "What if I want to permanently remove everything?" 
The AI should understand that "permanently remove everything" refers to the account and 
explain the Delete Account workflow. 
 
75.6 Conversation History During 
Troubleshooting 
Conversation history is particularly important for troubleshooting. 
The AI should track: 
Problem 
What the user initially reported. 
Troubleshooting 
What instructions were provided. 
User Actions 
Which instructions the user says they completed. 
Result 
Whether the problem remains. 
Next Step 
The next appropriate troubleshooting step or escalation. 

 
Example 
User:​
 "My video isn't submitting." 
AI:​
 "Please check your internet connection and camera/microphone permissions." 
User:​
 "I checked both." 
AI:​
 "Please try recording the video again." 
User:​
 "I tried again and I still get 'Some error!'" 
The AI should now recognize that: 
●​ Internet was checked. 
●​ Permissions were checked. 
●​ Recording was retried. 
●​ The error persists. 
The next response should move toward support escalation, rather than restarting the 
troubleshooting process. 
 
75.7 Conversation History & RAG 
Conversation history and the WiseIN knowledge base serve different purposes. 
Knowledge Base / RAG 
Provides WiseIN's documented information. 
Conversation History 
Provides context about the user's current situation. 
Together: 

User Question 
↓ 
Conversation Context 
↓ 
Retrieve Relevant WiseIN Documentation 
↓ 
Generate Context-Aware Answer 
 
Example 
Knowledge Base:​
 Google Sign-In → "Failed to fetch" troubleshooting. 
Conversation History:​
 User already refreshed the page and tried another browser. 
The AI should combine both pieces of information and avoid repeating steps already completed. 
 
75.8 Conversation History for Human 
Escalation 
Conversation history becomes especially valuable when a conversation is transferred to human 
support. 
The support representative should ideally be able to understand: 
●​ What the user originally asked. 
●​ What problem occurred. 
●​ What troubleshooting was attempted. 
●​ What errors appeared. 
●​ What the AI recommended. 
●​ What the user tried. 
●​ Why the issue was escalated. 

Example Escalation Summary 
Issue: Google Sign-In failure​
 Error: "Failed to fetch"​
 Troubleshooting attempted: 
●​ Internet connection checked 
●​ Page refreshed 
●​ Google Sign-In retried 
●​ Another browser tested 
Result: Issue persists. 
This prevents the user from having to repeat the entire conversation. 
 
75.9 User Confirmation 
The AI should confirm important information when there is uncertainty. 
Example 
User:​
 "I can't access my account." 
Instead of assuming the issue is login-related, the AI can ask: 
"Are you unable to log in, or can you log in but cannot access a particular feature?" 
This prevents the conversation history from being built around an incorrect assumption. 
 
75.10 Context Boundaries 
The AI should distinguish between information relevant to the current conversation and 
unrelated previous context. 
For example: 
Earlier:​
 User asks about deleting an account. 

Later:​
 User asks about creating a post. 
The AI should not assume the post-related question is connected to account deletion unless the 
user indicates that it is. 
 
75.11 Privacy Considerations 
Conversation history may contain information provided by the user during support interactions. 
The AI system should therefore handle conversation history according to WiseIN's applicable 
privacy and security requirements. 
The AI should not unnecessarily expose conversation information to other users. 
 
75.12 Sensitive Information 
The AI should not encourage users to place sensitive credentials into the conversation history. 
Users should never be asked to provide: 
●​ Passwords 
●​ OTPs 
●​ Authentication codes 
●​ Recovery codes 
The AI should also avoid unnecessarily requesting sensitive personal information. 
 
75.13 Conversation History & Data 
Retention 
The currently available WiseIN documentation does not specify: 
●​ How long AI conversations are stored. 

●​ Whether users can manually delete AI conversation history. 
●​ Whether conversation history is stored permanently. 
●​ The exact database/storage system used. 
●​ Whether conversation history is used for AI model training. 
●​ Exact encryption mechanisms. 
●​ Exact retention/deletion schedules. 
Therefore, the AI documentation should not invent these details. 
If WiseIN establishes an official conversation-retention policy, it should be added to this section. 
 
75.14 Conversation History & Account 
Deletion 
The AI should not make assumptions about what happens to stored AI conversations when a 
user deletes their WiseIN account. 
Unless WiseIN's official documentation specifies the behavior, the AI should say: 
"I don't have confirmed information about how conversation history is handled after 
account deletion. Please contact WiseIN support for clarification." 
 
75.15 Conversation History & Deactivation 
Similarly, the AI should not claim that conversation history is: 
●​ Deleted 
●​ Preserved 
●​ Hidden 
●​ Archived 
after account deactivation unless this behavior is officially documented. 
 
75.16 AI Memory vs Conversation History 

These concepts should be kept separate. 
Conversation History 
Information from the current support conversation that helps the AI understand the ongoing 
issue. 
Long-Term Memory 
Information retained across separate conversations. 
The current WiseIN documentation confirms the need for conversation history, but it does not 
establish a specific long-term memory system or policy. 
Therefore, the AI should not claim that it permanently remembers users across different 
conversations unless such functionality is officially implemented and documented. 
 
75.17 Conversation History in the AI 
Architecture 
A conceptual support architecture can be: 
User 
↓ 
Chat Interface 
↓ 
Conversation History 
↓ 
Intent Detection 
↓ 
RAG Knowledge Retrieval 
↓ 

AI Response Generation 
↓ 
Response 
↓ 
Conversation History Updated 
If unresolved: 
↓ 
Human Escalation 
 
75.18 Conversation Context Example 
User 
"My OTP isn't coming." 
AI 
"Please check that your registered contact information is correct and request 
another OTP if available." 
User 
"I already did that." 
AI 
"Understood. Since you've already verified the information and requested another 
OTP, please check your email's spam/junk folder if you're using email verification. If 
the OTP still doesn't arrive, this may require support assistance." 
The AI uses the previous response to determine the next step instead of restarting the 
troubleshooting flow. 
 

75.19 When Conversation History Should 
Be Used 
The AI should use conversation history when: 
●​ Answering follow-up questions. 
●​ Troubleshooting an ongoing issue. 
●​ Tracking attempted solutions. 
●​ Clarifying user intent. 
●​ Preparing a support escalation. 
●​ Avoiding repetitive questions. 
●​ Summarizing an unresolved issue. 
 
75.20 When the AI Should Ask Again 
The AI should ask the user again when: 
●​ The previous information is unclear. 
●​ The information may have changed. 
●​ Multiple issues are being discussed. 
●​ The previous answer does not contain enough information. 
●​ The AI needs explicit confirmation before proceeding. 
Example 
AI:​
 "Are you using Google Sign-In?" 
User:​
 "Yes." 
Later: 
User:​
 "I'm trying to log in from another account." 
The AI should clarify which account/login method the user is referring to rather than blindly 
applying the previous context. 
 

75.21 Conversation Summary 
For long conversations, the system can maintain a structured summary of the issue. 
Suggested format 
User Issue:​
 Unable to submit recorded video. 
Feature:​
 Video Recording. 
Error:​
 "Some error!" 
Steps Attempted: 
●​ Checked internet. 
●​ Checked camera permission. 
●​ Checked microphone permission. 
●​ Retried recording. 
Current Status:​
 Issue unresolved. 
Escalation:​
 Required. 
This structured information can help both the AI and human support team. 
 
75.22 AI Conversation History Rules 
The AI Assistant should follow these rules: 
1.​ Remember relevant context. 
2.​ Do not repeatedly ask for information already provided. 
3.​ Track troubleshooting steps. 
4.​ Understand follow-up questions. 
5.​ Clarify ambiguous information. 
6.​ Do not assume unrelated conversations are connected. 
7.​ Protect conversation information. 

8.​ Never request passwords or OTPs. 
9.​ Use conversation context together with RAG. 
10.​Pass relevant context during human escalation. 
 
75.23 Recommended Conversation Flow 
Normal Conversation 
User → Question → AI Answer → Follow-up → Context retained → Answer 
Troubleshooting 
Problem → Troubleshooting → User result → Next step → Resolution/Escalation 
Human Escalation 
Conversation → Issue Summary → Troubleshooting History → Escalation → Human 
Support 
 
75.24 Final Principle 
Conversation history should make the WiseIN AI Assistant feel like a continuous support 
conversation, not a series of disconnected questions. 
The system should remember what matters, avoid unnecessary repetition, protect user 
information, and use the accumulated context to provide better answers. 
Remember the problem. Track what was tried. Understand what changed. Use 
the context. Escalate when necessary. 
 



---

