# AI Analytics

## Source: 79.pdf

79. AI Analytics 
Overview 
AI Analytics defines how WiseIN can measure, understand, and improve the performance of 
the AI Assistant. 
The purpose of AI Analytics is not only to count how many people use the chatbot. It should 
help the WiseIN team understand: 
●​ What users are asking. 
●​ Which questions the AI can answer. 
●​ Which questions remain unresolved. 
●​ Which topics require human support. 
●​ Which documentation is frequently used. 
●​ Where the knowledge base has gaps. 
●​ Whether users are satisfied with the AI responses. 
●​ Where the AI experience needs improvement. 
Core Principle 
AI Analytics should turn support conversations into actionable insights 
without exposing unnecessary user information. 
 
79.1 Purpose of AI Analytics 
AI Analytics can help WiseIN: 
●​ Measure AI Assistant usage. 
●​ Identify common support questions. 
●​ Measure resolution performance. 
●​ Track human escalations. 
●​ Identify knowledge gaps. 
●​ Evaluate RAG performance. 
●​ Monitor user feedback. 
●​ Improve WiseIN documentation. 
●​ Identify recurring product problems. 
●​ Improve the overall customer-support experience. 

 
79.2 AI Analytics Overview 
A conceptual analytics flow is: 
                   AI ASSISTANT 
                         │ 
                         ▼ 
                 User Conversations 
                         │ 
          ┌──────────────┼──────────────┐ 
          ▼              ▼              ▼ 
       Questions      AI Answers     Escalations 
          │              │              │ 
          └──────────────┼──────────────┘ 
                         ▼ 
                  Analytics Layer 
                         │ 
          ┌──────────────┼──────────────┐ 
          ▼              ▼              ▼ 
       Metrics       Insights       Reports 
          │              │              │ 
          └──────────────┼──────────────┘ 
                         ▼ 
                   WiseIN Team 
 
79.3 Main Analytics Categories 
AI Analytics can be divided into: 
1.​ Usage Analytics 
2.​ Conversation Analytics 
3.​ Question Analytics 
4.​ Resolution Analytics 
5.​ Escalation Analytics 
6.​ RAG Analytics 
7.​ Knowledge Gap Analytics 
8.​ User Feedback Analytics 
9.​ Performance Analytics 

10.​Security Analytics 
 
79.4 Usage Analytics 
Usage analytics measures how frequently the AI Assistant is being used. 
Possible metrics include: 
●​ Number of conversations. 
●​ Number of users interacting with AI. 
●​ Number of questions. 
●​ Daily conversations. 
●​ Weekly conversations. 
●​ Monthly conversations. 
●​ Average questions per conversation. 
●​ Repeat usage. 
Example 
Daily AI Conversations: 245 
Weekly AI Conversations: 1,420 
Monthly AI Conversations: 5,830 
These numbers are examples of the type of information the analytics system could display; they 
are not current WiseIN statistics. 
 
79.5 Conversation Analytics 
Conversation analytics examines how support conversations progress. 
Useful metrics include: 
●​ Average conversation length. 
●​ Average number of user messages. 
●​ Average number of AI responses. 
●​ Conversations resolved by AI. 
●​ Conversations escalated to humans. 
●​ Conversations abandoned. 
●​ Conversations requiring repeated clarification. 

Example 
Conversation 
    ↓ 
Question 
    ↓ 
AI Response 
    ↓ 
Follow-up 
    ↓ 
Resolution 
Analytics can identify where users commonly leave the conversation. 
 
79.6 Question Analytics 
The system can categorize questions based on their intent. 
Example categories: 
Category 
Example 
Login 
"I can't log in" 
OTP 
"I didn't receive my OTP" 
Profile 
"How do I edit my profile?" 
Jobs 
"How do I find jobs?" 
Meetings 
"How do meetings work?" 
Subscription 
"How do subscriptions work?" 
Account 
"How do I delete my account?" 
Reporting 
"How do I report someone?" 
Privacy 
"How is my information handled?" 
Technical 
Issue 
"The page isn't loading" 
This helps WiseIN understand which areas generate the most support questions. 

 
79.7 Most Asked Questions 
The analytics system can identify frequently asked questions. 
For example: 
Top Questions 
 
1. How do I edit my profile? 
2. Why am I not receiving OTP? 
3. How do I delete my account? 
4. How does verification work? 
5. How do I report a user? 
This information can help the team decide which documentation and product workflows need 
clearer explanations. 
 
79.8 Resolution Analytics 
One of the most important metrics is whether the AI actually helped the user. 
Possible categories: 
AI Resolved 
The user received an answer and did not require further support. 
Human Escalated 
The AI could not resolve the issue and transferred it to support. 
Unresolved 
The conversation ended without a confirmed resolution. 
Abandoned 
The user stopped interacting before resolution could be determined. 

 
79.9 Resolution Rate 
A possible metric is: 
AI Resolution Rate 
AI-resolved conversations 
────────────────────────── × 100 
Total eligible conversations 
The exact definition should be finalized by WiseIN before this metric is used as an official KPI. 
A conversation should not automatically be classified as resolved simply because the AI 
generated an answer. 
 
79.10 Human Escalation Analytics 
The system should track when users require human support. 
Possible metrics: 
●​ Total escalations. 
●​ Escalation percentage. 
●​ Most common escalation categories. 
●​ Escalations by feature. 
●​ Escalations caused by missing documentation. 
●​ Escalations caused by account-specific issues. 
●​ Escalations caused by technical problems. 
Example 
Login Issues 
     ↓ 
AI Troubleshooting 
     ↓ 
Still unresolved 
     ↓ 
Human Support 

If a large number of users are escalated for the same issue, the team can investigate the 
underlying problem. 
 
79.11 Escalation Reasons 
Escalations should ideally have structured reasons. 
Examples: 
●​ Information unavailable. 
●​ User requested human support. 
●​ Account-specific issue. 
●​ Payment issue. 
●​ Security issue. 
●​ Technical issue. 
●​ AI confidence too low. 
●​ Repeated troubleshooting failure. 
●​ Policy-related issue. 
This makes escalation analytics much more useful. 
 
79.12 RAG Analytics 
RAG analytics measures how effectively the knowledge-retrieval system is working. 
Potential metrics include: 
●​ Documents retrieved. 
●​ Frequently retrieved documents. 
●​ Retrieval relevance. 
●​ Queries with no useful results. 
●​ Queries with weak retrieval. 
●​ Frequently used knowledge sections. 
●​ Retrieval latency. 
 

79.13 Most Retrieved Documents 
Analytics can show which knowledge documents are being used most often. 
For example: 
Most Retrieved Knowledge 
 
63 Account Deactivation 
67 Error Codes 
70 FAQ 
68 Customer Support 
64 Account Deletion 
These are examples of possible results, not actual WiseIN analytics. 
This can help identify the areas users most frequently need assistance with. 
 
79.14 Knowledge Gap Analytics 
One of the most valuable uses of AI Analytics is identifying knowledge gaps. 
A knowledge gap occurs when: 
A user asks a legitimate WiseIN question, but the knowledge base does not contain 
enough information to answer it confidently. 
Example 
User: 
"Can I change the email associated with my WiseIN account?" 
If the knowledge base contains no documented procedure, the system can record: 
Knowledge Gap 
Category: Account 
Question: Change registered email 
Status: Documentation required 
The documentation team can then investigate and add an official answer if appropriate. 

 
79.15 Unknown Question Analytics 
The system should track questions that the AI cannot confidently classify. 
Examples: 
●​ Unknown intent. 
●​ No relevant RAG result. 
●​ Ambiguous question. 
●​ Unsupported feature. 
●​ New product functionality. 
These queries can be reviewed periodically. 
 
79.16 AI Feedback Analytics 
Users can provide feedback on AI answers. 
A simple implementation could be: 
Was this answer helpful? 
👍 Yes​
 👎 No 
Analytics can then show: 
Helpful: 82% 
Not Helpful: 18% 
The actual percentages would come from WiseIN's collected data. 
 
79.17 Negative Feedback Analysis 
A negative response should not simply be counted. 

The system can categorize why users were dissatisfied. 
Possible reasons: 
●​ Incorrect answer. 
●​ Incomplete answer. 
●​ Answer was difficult to understand. 
●​ Information was outdated. 
●​ User needed human support. 
●​ RAG retrieved incorrect information. 
●​ Technical issue. 
This helps identify the underlying problem. 
 
79.18 AI Performance Analytics 
The system can measure technical performance. 
Potential metrics include: 
●​ Average response time. 
●​ RAG retrieval time. 
●​ AI generation time. 
●​ API failures. 
●​ Tool failures. 
●​ Timeout rate. 
●​ Error rate. 
Example 
User Question 
      ↓ 
RAG Retrieval: 300 ms 
      ↓ 
LLM Generation: 1.8 sec 
      ↓ 
Response 
These values are examples only. 
 

79.19 AI Availability 
Analytics can track whether the AI Assistant is functioning correctly. 
Possible metrics: 
●​ Successful AI requests. 
●​ Failed AI requests. 
●​ API errors. 
●​ Knowledge-base errors. 
●​ Tool errors. 
●​ Service availability. 
If failures increase suddenly, the technical team can investigate. 
 
79.20 Cost Analytics 
If WiseIN uses paid AI APIs, analytics may also track AI usage and associated costs. 
Potential metrics include: 
●​ Number of AI requests. 
●​ Token usage. 
●​ Embedding usage. 
●​ Retrieval requests. 
●​ AI API costs. 
●​ Average cost per conversation. 
Cost information should be visible to authorized administrators rather than ordinary users. 
 
79.21 AI Analytics Dashboard 
An internal AI Analytics dashboard could contain: 
┌─────────────────────────────────────────────┐ 
│             WISEIN AI ANALYTICS             │ 
├──────────────┬──────────────┬───────────────┤ 
│ Conversations│ Resolution   │ Escalations   │ 

│     5,830    │     72%      │      18%      │ 
├──────────────┴──────────────┴───────────────┤ 
│                                             │ 
│          Top Support Categories             │ 
│                                             │ 
│ Login          ███████████                  │ 
│ OTP            █████████                    │ 
│ Profile        ███████                      │ 
│ Account        ██████                       │ 
│ Meetings       █████                        │ 
│                                             │ 
├─────────────────────────────────────────────┤ 
│        Knowledge Gaps / Failed Queries      │ 
│                                             │ 
│ • Change registered email                   │ 
│ • Subscription transfer                     │ 
│ • New feature questions                     │ 
│                                             │ 
└─────────────────────────────────────────────┘ 
The displayed numbers above are illustrative. 
 
79.22 AI Analytics for Documentation 
Analytics should directly support the documentation process. 
Example 
Analytics shows: 
18% of OTP-related conversations are escalated. 
The documentation team investigates. 
They discover that the existing OTP documentation does not explain one common failure 
scenario. 
They update: 
67 — Error Codes​
 70 — FAQ​
 66 — Troubleshooting 

The updated documents are then indexed into the RAG system. 
 
79.23 Continuous Improvement Loop 
AI Analytics should create a continuous improvement cycle: 
User Questions 
      ↓ 
AI Conversations 
      ↓ 
Analytics 
      ↓ 
Identify Problems 
      ↓ 
Improve Documentation 
      ↓ 
Update RAG 
      ↓ 
Improve AI Responses 
      ↓ 
New User Conversations 
      ↓ 
Analytics 
This allows the AI Assistant to improve as WiseIN learns more about its users' support needs. 
 
79.24 Security Analytics 
AI Analytics should also help identify suspicious behavior. 
Possible indicators: 
●​ Repeated prompt-injection attempts. 
●​ Excessive requests. 
●​ Repeated attempts to access restricted information. 
●​ Unusual tool usage. 
●​ Repeated authentication failures. 

Security analytics should be restricted to authorized personnel. 
 
79.25 Privacy in AI Analytics 
Analytics should follow WiseIN's applicable privacy requirements. 
The system should avoid collecting unnecessary personal information. 
Where detailed conversation data is not required, analytics should use aggregated or 
appropriately protected information. 
For example, instead of exposing: 
Full user conversation 
an analytics dashboard might show: 
OTP issues: 143 conversations 
 
79.26 Data Access 
AI analytics should have role-based access. 
Regular User 
Should see their own relevant support experience where applicable. 
Support Team 
May need access to support conversations and escalation information. 
Documentation Team 
May need aggregated questions and knowledge-gap information. 
Administrators 
May require broader operational analytics. 

The exact permissions should be defined by WiseIN. 
 
79.27 Analytics Retention 
The provided WiseIN documentation does not specify an exact retention period for AI analytics 
data. 
Therefore, the AI system should not claim a specific retention period until WiseIN defines one. 
The final policy should determine: 
●​ What analytics data is stored. 
●​ How long it is stored. 
●​ Who can access it. 
●​ When it is deleted. 
●​ Whether data is anonymized or aggregated. 
 
79.28 Important Metrics 
A practical first version of the AI Analytics system can focus on: 
Metric 
Purpose 
Total Conversations 
Measure AI usage 
Total Questions 
Measure interaction volume 
Resolution Rate 
Measure support 
effectiveness 
Escalation Rate 
Identify unresolved issues 
Top Intents 
Understand user needs 
Failed Queries 
Find unsupported questions 
Knowledge Gaps 
Improve documentation 
Helpful/Not Helpful 
Measure user feedback 

Response Time 
Monitor performance 
Tool Errors 
Monitor system reliability 
RAG Retrieval Quality 
Evaluate knowledge retrieval 
 
79.29 What AI Analytics Should Not Do 
AI Analytics should not be used to: 
●​ Expose private user conversations unnecessarily. 
●​ Reveal sensitive personal information. 
●​ Give unauthorized users access to support data. 
●​ Automatically make decisions about users without appropriate authorization. 
●​ Treat an AI-generated answer as proof that an issue was resolved. 
●​ Hide failures or unsuccessful conversations. 
Analytics should represent the system's actual behavior as accurately as possible. 
 
79.30 Recommended AI Analytics 
Workflow 
User Interaction 
       ↓ 
Conversation Recorded 
       ↓ 
Intent Identified 
       ↓ 
RAG Retrieval 
       ↓ 
AI Response 
       ↓ 
Resolution / Escalation 
       ↓ 
Feedback 
       ↓ 
Analytics Processing 
       ↓ 

Dashboard 
       ↓ 
WiseIN Team 
       ↓ 
Documentation / Product Improvements 
 
79.31 Example End-to-End Scenario 
User 
"I can't receive my OTP." 
AI 
Provides documented OTP troubleshooting. 
User 
"I already tried everything." 
AI 
Checks conversation history and determines that the documented steps were already 
attempted. 
AI 
Escalates the issue to human support. 
Analytics Records 
Intent: 
OTP Issue 
 
Resolution: 
Human Escalation 
 
Reason: 
Troubleshooting unsuccessful 
 
Knowledge Used: 
OTP Troubleshooting 

 
User Feedback: 
Not available 
If this happens frequently, WiseIN can investigate whether: 
●​ The OTP system has a technical problem. 
●​ Documentation needs improvement. 
●​ More troubleshooting steps are required. 
●​ A product change is needed. 
 
79.32 AI Analytics Golden Rules 
The WiseIN AI Analytics system should follow these principles: 
1.​ Measure AI usage. 
2.​ Track support outcomes. 
3.​ Measure escalations. 
4.​ Identify common user questions. 
5.​ Identify unanswered questions. 
6.​ Monitor RAG performance. 
7.​ Track user feedback. 
8.​ Monitor technical performance. 
9.​ Protect analytics data. 
10.​Use analytics to improve documentation and the product. 
11.​Do not expose unnecessary personal information. 
12.​Do not treat generated answers as automatically resolved issues. 
 
79.33 Final Principle 
AI Analytics should turn the WiseIN AI Assistant from a static chatbot into an continuously 
improving support system. 
The complete cycle is: 
Users ask questions → AI responds → Analytics measures the interaction → 
Knowledge gaps are identified → Documentation improves → RAG improves 
→ AI support improves. 

 



---

