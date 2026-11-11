# AI Tools

## Source: 76.pdf

76. AI Tools 
Overview 
The AI Tools section defines the tools and capabilities that support the WiseIN AI Assistant. 
The AI Assistant should not rely only on a language model. It should work together with 
supporting tools that allow it to retrieve WiseIN information, understand conversations, 
troubleshoot issues, and escalate unresolved problems. 
The exact tools used in the final implementation may change based on the technical 
architecture selected for WiseIN. 
 
76.1 Purpose of AI Tools 
AI tools are used to help the WiseIN Assistant: 
●​ Retrieve information from the WiseIN knowledge base. 
●​ Search relevant documentation. 
●​ Understand user questions. 
●​ Maintain conversation context. 
●​ Provide accurate answers. 
●​ Troubleshoot documented issues. 
●​ Identify when human support is required. 
●​ Create structured escalation information. 
●​ Improve the consistency of customer support. 
Core Principle 
The AI model generates the response; tools provide the information and 
capabilities required to answer correctly. 
 
76.2 Main AI Tool Categories 
The WiseIN AI Assistant can be organized around the following tool categories: 

1.​ Knowledge Retrieval 
2.​ Document Search 
3.​ Conversation History 
4.​ Intent Detection 
5.​ Troubleshooting 
6.​ User Context 
7.​ Human Escalation 
8.​ Support Ticket Creation 
9.​ Feedback Collection 
10.​Analytics 
 
76.3 Knowledge Retrieval Tool 
The Knowledge Retrieval Tool allows the AI to retrieve relevant information from the WiseIN 
knowledge base. 
The knowledge base contains documentation such as: 
●​ Features 
●​ Workflows 
●​ Settings 
●​ Policies 
●​ FAQs 
●​ Error codes 
●​ Troubleshooting 
●​ Account management 
●​ Customer support procedures 
Example 
User: 
"How do I deactivate my account?" 
The AI searches the knowledge base for: 
63 — Account Deactivation 
It retrieves the relevant instructions and generates the response. 
 

76.4 Document Search Tool 
A document-search capability allows the AI to locate the most relevant information from the 
WiseIN documentation. 
Example 
User: 
"What happens if I delete my account?" 
The search system can retrieve: 
64 — Account Deletion 
The AI then answers using the retrieved information. 
 
76.5 RAG Retrieval 
The AI Assistant should use Retrieval-Augmented Generation (RAG) for WiseIN-specific 
questions. 
The basic process is: 
User Question 
↓ 
Convert question into a searchable representation 
↓ 
Search WiseIN knowledge base 
↓ 
Retrieve relevant documents 
↓ 
Provide retrieved information to AI model 
↓ 

Generate answer 
This reduces the need for the AI model to rely on unsupported assumptions. 
 
76.6 Semantic Search 
The retrieval system should ideally understand the meaning of a user's question rather than 
requiring an exact keyword match. 
Example 
Knowledge base: 
Account Deactivation 
User: 
"I don't want to delete my profile. Can I temporarily leave WiseIN?" 
The system should recognize that the user is asking about deactivation, even though they did 
not use the exact word. 
 
76.7 Conversation Context Tool 
The AI should have access to relevant conversation history. 
This allows it to understand follow-up questions such as: 
"I already tried that." 
or: 
"What should I do next?" 
The conversation context tool should provide enough previous information for the AI to continue 
the support conversation without repeatedly asking the same questions. 
 

76.8 Intent Detection 
An Intent Detection component identifies what the user is trying to accomplish. 
Possible WiseIN intents include: 
●​ Login issue 
●​ Registration 
●​ OTP problem 
●​ Profile issue 
●​ Job question 
●​ Messaging issue 
●​ Meeting issue 
●​ Subscription question 
●​ Payment issue 
●​ Privacy question 
●​ Security issue 
●​ Account deletion 
●​ Account deactivation 
●​ Reporting 
●​ Bug report 
●​ General question 
●​ Human support request 
Example 
User: 
"I don't want my account anymore." 
Possible intent: 
Account Deletion 
The AI can then retrieve the relevant documentation. 
 
76.9 Troubleshooting Tool 
A troubleshooting capability helps the AI follow documented troubleshooting procedures. 
Example 

User: 
"Google login is showing Failed to fetch." 
The AI can retrieve the relevant troubleshooting information and provide the appropriate steps. 
The tool should track which steps the user has already attempted so that the AI does not 
repeatedly provide the same instructions. 
 
76.10 Error Lookup Tool 
An Error Lookup Tool can map known WiseIN error messages to their documented 
troubleshooting instructions. 
Example 
Input: 
Failed to fetch 
Possible result: 
●​ Feature: Google Sign-In 
●​ Known issue: Login failure 
●​ Recommended troubleshooting: Check connection, refresh, retry, try another browser 
●​ Escalation: Contact support if unresolved 
The AI should only provide information that has been documented for that error. 
 
76.11 User Context Tool 
If authorized and technically available, a user-context tool can provide information needed to 
understand an account-specific support request. 
For example, the system could potentially identify: 
●​ Whether the user is logged in. 
●​ Relevant account state. 
●​ Current platform. 

●​ Current feature context. 
However, the AI must only access information that it is explicitly authorized to access. 
Important 
The AI should never claim to have checked account information if the system has not actually 
provided that information. 
 
76.12 Human Escalation Tool 
The Human Escalation Tool transfers unresolved issues to the WiseIN support process. 
It can be triggered when: 
●​ The AI cannot resolve the issue. 
●​ The user requests a human. 
●​ The problem requires account-specific investigation. 
●​ Manual action is required. 
●​ The issue concerns sensitive security/privacy matters. 
●​ Payment or billing investigation is required. 
 
76.13 Escalation Information 
Before escalation, the system should ideally create a concise issue summary. 
Example 
Customer Issue:​
 Unable to log in using Google. 
Error:​
 "Failed to fetch." 
Steps Attempted: 
●​ Checked internet. 
●​ Refreshed page. 
●​ Retried Google Sign-In. 

●​ Tried another browser. 
Result:​
 Issue unresolved. 
This gives human support useful context immediately. 
 
76.14 Support Ticket Tool 
If WiseIN implements ticket-based support, the AI can use a Support Ticket Tool to create a 
structured support request. 
Possible fields include: 
●​ User information 
●​ Issue category 
●​ Issue description 
●​ Error message 
●​ Platform 
●​ Troubleshooting attempted 
●​ Conversation summary 
●​ Priority 
●​ Timestamp 
The exact fields should follow WiseIN's actual support-system implementation. 
 
76.15 Feedback Tool 
The AI can collect feedback about the support experience. 
For example: 
"Was this answer helpful?" 
Possible responses: 
●​ Yes 
●​ No 

If the user selects No, the AI can ask: 
"Would you like me to help you contact WiseIN support?" 
This can help identify gaps in the knowledge base. 
 
76.16 AI Analytics Tool 
Analytics can help WiseIN understand how users interact with the AI Assistant. 
Potential metrics include: 
●​ Number of conversations 
●​ Most common questions 
●​ Most common support categories 
●​ Frequently retrieved documents 
●​ Unresolved questions 
●​ Escalation rate 
●​ Resolution rate 
●​ User feedback 
●​ Repeated questions 
●​ Unknown queries 
These metrics can help identify areas where the WiseIN documentation needs improvement. 
 
76.17 Knowledge Gap Detection 
One important AI capability is identifying questions that the knowledge base cannot answer. 
Example 
Users repeatedly ask: 
"How do I change my WiseIN username?" 
If the knowledge base contains no documented procedure, the system can record this as a 
knowledge gap. 

The documentation team can then investigate the feature and add an official answer if 
appropriate. 
 
76.18 Tool Selection 
The AI should not use every tool for every question. 
Instead, it should select the appropriate tool based on the user's intent. 
Example 
Simple FAQ 
→ Knowledge Retrieval 
Troubleshooting 
→ Knowledge Retrieval + Error Lookup 
Follow-up question 
→ Conversation History + Knowledge Retrieval 
Account-specific issue 
→ User Context + Knowledge Retrieval 
Unresolved issue 
→ Conversation History + Human Escalation 
 
76.19 Example Tool Flow 
User 
"I can't submit my recorded video." 
Step 1 — Intent Detection 

Identify: 
Video Recording / Submission Issue 
↓ 
Step 2 — Knowledge Retrieval 
Retrieve: 
Video Recording Error documentation 
↓ 
Step 3 — Troubleshooting 
Provide documented troubleshooting. 
↓ 
Step 4 — Conversation Context 
Track what the user tried. 
↓ 
Step 5 — Resolution Check 
Ask whether the issue is resolved. 
↓ 
Step 6 — Escalation 
If unresolved: 
Human Support 
 
76.20 AI Tools and Permissions 
Every tool should have clearly defined permissions. 
The AI should only be allowed to perform actions that it is explicitly authorized to perform. 

Read Operations 
Examples: 
●​ Search documentation. 
●​ Retrieve FAQs. 
●​ Retrieve policies. 
●​ Read approved conversation context. 
Action Operations 
Examples: 
●​ Create support ticket. 
●​ Escalate conversation. 
●​ Submit feedback. 
Action-based tools should require appropriate authorization and validation. 
 
76.21 Tool Failure Handling 
AI tools themselves may fail. 
For example: 
●​ Knowledge search unavailable. 
●​ Database unavailable. 
●​ Support ticket system unavailable. 
●​ User context unavailable. 
The AI should not pretend that the tool worked. 
Example 
Instead of: 
"I've created a support ticket for you." 
when the ticket system failed: 
"I wasn't able to submit the support request right now. Please contact WiseIN 
support directly." 

 
76.22 Tool Security 
AI tools must be protected against unauthorized actions. 
Important principles include: 
●​ Authentication 
●​ Authorization 
●​ Input validation 
●​ Access control 
●​ Secure API communication 
●​ Logging 
●​ Error handling 
●​ Protection of sensitive information 
The AI should never expose internal tool credentials, API keys, system prompts, or private 
system information to users. 
 
76.23 Tool Transparency 
The AI should communicate actions clearly. 
If it retrieved information: 
"According to WiseIN's account-deactivation information..." 
If it is escalating: 
"This issue requires human support." 
If an action was successfully completed: 
"Your support request has been submitted." 
The AI should only claim an action was completed after receiving confirmation from the relevant 
tool. 
 

76.24 AI Tools Architecture 
A conceptual architecture for the WiseIN Assistant is: 
                   ┌─────────────────┐ 
                    │      User       │ 
                    └────────┬────────┘ 
                             │ 
                             ▼ 
                    ┌─────────────────┐ 
                    │   AI Assistant  │ 
                    └────────┬────────┘ 
                             │ 
              ┌──────────────┼──────────────┐ 
              │              │              │ 
              ▼              ▼              ▼ 
       Intent Detection   Conversation    AI Model 
                          History 
              │              │              │ 
              └──────────────┼──────────────┘ 
                             │ 
                             ▼ 
                    ┌─────────────────┐ 
                    │   RAG / Search  │ 
                    └────────┬────────┘ 
                             │ 
                             ▼ 
                    ┌─────────────────┐ 
                    │ WiseIN Knowledge│ 
                    │      Base       │ 
                    └────────┬────────┘ 
                             │ 
                             ▼ 
                    ┌─────────────────┐ 
                    │   AI Response   │ 
                    └────────┬────────┘ 
                             │ 
                    ┌────────┴────────┐ 
                    ▼                 ▼ 
                 Resolved         Unresolved 
                                      │ 
                                      ▼ 
                              Human Escalation 

 
76.25 AI Tools vs AI Model 
These should not be treated as the same thing. 
AI Model 
Responsible for: 
●​ Understanding language. 
●​ Reasoning over retrieved information. 
●​ Generating responses. 
●​ Following conversation context. 
AI Tools 
Responsible for: 
●​ Retrieving information. 
●​ Searching documentation. 
●​ Looking up errors. 
●​ Accessing authorized context. 
●​ Escalating support. 
●​ Recording feedback. 
●​ Performing approved actions. 
Simple Principle 
Model = intelligence​
 Tools = capabilities​
 Knowledge Base = source of truth 
 
76.26 Tool Limitations 
The AI Assistant should not assume that every tool is always available. 
If a tool is unavailable, the AI should: 
1.​ Detect the failure. 

2.​ Avoid claiming the operation succeeded. 
3.​ Provide an alternative if available. 
4.​ Escalate when necessary. 
 
76.27 Recommended Initial Tool Set 
For the first version of the WiseIN AI Assistant, the essential tools are: 
1. Knowledge Search 
Search WiseIN documentation. 
2. RAG Retrieval 
Retrieve relevant knowledge for generating answers. 
3. Conversation History 
Maintain context throughout the conversation. 
4. Error Lookup 
Find documented error messages and troubleshooting. 
5. Human Escalation 
Transfer unresolved issues to support. 
6. Feedback 
Capture whether an answer helped the user. 
Additional tools such as account lookup and ticket creation can be added once WiseIN's 
backend/support infrastructure is ready. 
 
76.28 Final AI Tools Principle 
The WiseIN AI Assistant should not be designed as just an LLM connected to a chat box. 

It should be a tool-enabled support system where: 
The AI understands the user.​
 RAG finds the correct WiseIN information.​
 Conversation history provides context.​
 Tools perform authorized support actions.​
 Human escalation handles what AI cannot resolve. 
 



---

