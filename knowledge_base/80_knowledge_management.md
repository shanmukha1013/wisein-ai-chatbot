# Knowledge Management

## Source: 80.pdf

80. Knowledge Management 
Overview 
Knowledge Management defines how WiseIN creates, organizes, updates, reviews, and 
maintains the information used by the AI Assistant. 
For the WiseIN AI system, the knowledge base is the foundation of reliable customer support. 
The AI can only provide consistently accurate answers when the underlying documentation is 
correct, current, structured, and approved. 
Core Principle 
One trusted source of truth, continuously maintained and ready for AI 
retrieval. 
 
80.1 Purpose 
Knowledge Management should ensure that WiseIN's AI Assistant always has access to reliable 
information about: 
●​ WiseIN features 
●​ User workflows 
●​ Account management 
●​ Policies 
●​ Privacy and security 
●​ Troubleshooting 
●​ Error codes 
●​ FAQs 
●​ Subscriptions 
●​ Payments 
●​ Customer support 
●​ AI Assistant behavior 
●​ Platform changes 
The knowledge-management process should also make it easy for the WiseIN team to identify 
and fix missing or outdated information. 

 
80.2 Knowledge Management Lifecycle 
Knowledge should follow a controlled lifecycle: 
Create 
  ↓ 
Review 
  ↓ 
Approve 
  ↓ 
Publish 
  ↓ 
Index 
  ↓ 
Use in RAG 
  ↓ 
Monitor 
  ↓ 
Update 
  ↓ 
Review Again 
This ensures that documentation does not become outdated as WiseIN evolves. 
 
80.3 Knowledge Sources 
The WiseIN AI knowledge base should primarily contain approved WiseIN information. 
Main sources 
●​ Official WiseIN documentation 
●​ Feature documentation 
●​ User workflows 
●​ Troubleshooting guides 
●​ Error-code documentation 
●​ FAQs 
●​ Privacy information 
●​ Security information 

●​ Community Guidelines 
●​ Content Policies 
●​ Terms & Conditions 
●​ Customer-support procedures 
●​ Human-escalation procedures 
●​ AI Assistant documentation 
External information should not override official WiseIN documentation for WiseIN-specific 
functionality. 
 
80.4 Knowledge Categories 
The current WiseIN documentation structure can be organized into major categories. 
Platform & Features 
Documents covering WiseIN functionality and user workflows. 
Account Management 
Examples: 
●​ Privacy 
●​ Security 
●​ Account Deactivation 
●​ Account Deletion 
●​ Logout 
Content & Community 
Examples: 
●​ Reporting 
●​ Community Guidelines 
●​ Content Policies 
●​ Terms & Conditions 
Support 
Examples: 
●​ Troubleshooting 

●​ Error Codes 
●​ Customer Support 
●​ Human Escalation 
●​ FAQ 
AI 
Examples: 
●​ AI Assistant 
●​ AI Limitations 
●​ Conversation History 
●​ AI Tools 
●​ RAG Knowledge 
●​ Security for AI 
●​ AI Analytics 
●​ Knowledge Management 
 
80.5 Document Standards 
Every knowledge document should follow a consistent structure. 
Recommended format: 
Document ID 
Title 
Category 
Overview 
Purpose 
How It Works 
User Workflow 
Rules / Restrictions 
Troubleshooting 
FAQs 
Limitations 
Related Documents 
Last Updated 
Status 
A consistent format makes documents easier for both humans and the RAG system to 
understand. 

 
80.6 Document Identification 
Every document should have a unique identifier. 
For example: 
63 — Account Deactivation 
64 — Account Deletion 
65 — Logout 
66 — Troubleshooting 
67 — Error Codes 
68 — Customer Support 
69 — Human Escalation 
70 — FAQ 
73 — AI Assistant 
77 — RAG Knowledge 
80 — Knowledge Management 
The identifier makes it easier to reference, update, and retrieve specific documentation. 
 
80.7 Knowledge Ownership 
Each major knowledge area should have an appropriate owner. 
For example: 
Knowledge Area 
Possible Owner 
Product Features 
Product Team 
Technical Troubleshooting 
Engineering 
Policies 
Appropriate Policy/Management Owner 
Customer Support 
Support Team 
AI Documentation 
AI/Engineering Team 
Security 
Security/Engineering Team 

The exact ownership structure should be defined by WiseIN. 
 
80.8 Knowledge Approval 
Information should be reviewed before becoming an official AI knowledge source. 
Recommended workflow 
Draft 
 ↓ 
Subject-Matter Review 
 ↓ 
Correction 
 ↓ 
Approval 
 ↓ 
Published 
 ↓ 
RAG Indexing 
This helps prevent unverified information from reaching users through the AI Assistant. 
 
80.9 Draft vs Published Knowledge 
The RAG system should distinguish between different document states. 
Draft 
Still being prepared. 
Under Review 
Waiting for approval. 
Published 
Approved and available for AI retrieval. 

Archived 
No longer current. 
Deprecated 
Should not be used for new answers. 
Only appropriate published and active knowledge should normally be available to the 
production AI Assistant. 
 
80.10 Version Control 
WiseIN documentation will change as the product evolves. 
Each document should therefore support versioning. 
Example: 
Account Deactivation 
Version 1.0 — Initial documentation 
Version 1.1 — Updated navigation 
Version 2.0 — New deactivation workflow 
The system should clearly identify which version is currently active. 
 
80.11 Last Updated Information 
Every important document should include a last-updated date. 
Example: 
Document: Account Deletion 
Status: Active 
Version: 2.0 
Last Updated: June 2026 
This makes it easier for the team to identify potentially outdated information. 

 
80.12 Updating Knowledge 
Knowledge should be updated whenever WiseIN changes: 
●​ UI 
●​ Navigation 
●​ Features 
●​ Policies 
●​ Account workflows 
●​ Error handling 
●​ Subscription functionality 
●​ Payment processes 
●​ Support procedures 
Example 
If WiseIN changes: 
Settings → Account → Delete 
to: 
Profile → Account Management → Delete Account 
the corresponding documentation must be updated before or alongside the product release. 
 
80.13 Product Change → Knowledge 
Update 
A product change should trigger a documentation review. 
Product Change 
      ↓ 
Identify Affected Documentation 
      ↓ 
Update Documentation 
      ↓ 

Review 
      ↓ 
Approve 
      ↓ 
Re-index RAG 
      ↓ 
Test AI 
      ↓ 
Release 
This reduces the chance that the AI provides old instructions after a product update. 
 
80.14 Knowledge Deprecation 
Old information should not simply remain active forever. 
When information becomes obsolete: 
Active 
  ↓ 
Updated 
  ↓ 
Old Version Archived 
The RAG system should prioritize the active version. 
 
80.15 Duplicate Knowledge 
Duplicate or conflicting documentation can cause incorrect retrieval. 
For example: 
Document A 
Account deletion is permanent. 
Document B 
Account deletion can be reversed. 

If both remain active, the AI may retrieve conflicting information. 
Therefore, the knowledge-management process should identify and resolve duplicate or 
contradictory information before it reaches production RAG. 
 
80.16 Single Source of Truth 
For each WiseIN feature or policy, there should ideally be one authoritative document or clearly 
defined authoritative source. 
For example: 
Account Deletion 
Primary source:​
 64 — Account Deletion 
Other documents may link to it rather than maintaining conflicting copies of the same workflow. 
 
80.17 Cross-References 
Documents should reference related knowledge where useful. 
Example: 
63 — Account Deactivation 
Related: 
●​ 64 — Account Deletion 
●​ 65 — Logout 
●​ 56 — Privacy 
●​ 68 — Customer Support 
This helps both human support staff and the retrieval system understand relationships between 
topics. 
 

80.18 Knowledge for RAG 
Knowledge Management and RAG are closely connected. 
Knowledge Management 
Controls: 
What information exists and whether it is trusted. 
RAG 
Controls: 
How relevant information is retrieved for the AI. 
AI Assistant 
Controls: 
How the retrieved information is explained to the user. 
Therefore: 
Good Knowledge Management 
          ↓ 
Good Knowledge Base 
          ↓ 
Good RAG Retrieval 
          ↓ 
Better AI Responses 
 
80.19 Knowledge Chunking 
Documents should be structured so that important sections can be retrieved independently. 
For example: 
64 Account Deletion 
    │ 
    ├── Overview 
    ├── Eligibility 

    ├── Steps 
    ├── What Happens After Deletion 
    ├── Important Warnings 
    └── FAQ 
This allows RAG to retrieve only the relevant section instead of unnecessarily loading the entire 
document. 
 
80.20 Knowledge Metadata 
Each knowledge item should contain useful metadata. 
Recommended fields: 
Metadata 
Example 
Document ID 
64 
Title 
Account Deletion 
Category 
Account 
Version 
1.0 
Status 
Active 
Source 
WiseIN 
Platform 
Website 
Language 
English 
Last Updated 
June 2026 
Owner 
Product Team 
Metadata can improve filtering, retrieval, and document management. 
 
80.21 Knowledge Quality Checks 

Before publishing a document, the team should check: 
Accuracy 
Is the information correct? 
Completeness 
Does it contain the necessary information? 
Clarity 
Can a normal user understand it? 
Consistency 
Does it agree with other WiseIN documentation? 
Currency 
Does it reflect the current WiseIN product? 
AI Readability 
Can the RAG system retrieve and interpret the information effectively? 
 
80.22 Knowledge Gap Management 
AI Analytics can identify questions that are not adequately covered by the knowledge base. 
The workflow should be: 
User Question 
      ↓ 
AI Cannot Reliably Answer 
      ↓ 
Knowledge Gap Recorded 
      ↓ 
Team Reviews Question 
      ↓ 
Determine Correct Answer 

      ↓ 
Create / Update Documentation 
      ↓ 
Approve 
      ↓ 
Add to RAG 
This creates a continuous feedback loop between users and documentation. 
 
80.23 Example Knowledge Gap 
User Question 
"Can I transfer my WiseIN subscription to another account?" 
RAG Result 
No relevant approved information. 
Action 
Record: 
Knowledge Gap 
Category: Subscriptions 
Question: Subscription transfer 
Status: Needs Review 
The responsible team can determine whether the feature exists and document the official 
behavior. 
 
80.24 FAQ Management 
The FAQ should not become a random collection of questions. 
Frequently asked questions should be identified from: 
●​ Customer support 

●​ AI conversations 
●​ User feedback 
●​ Product teams 
●​ Common troubleshooting cases 
●​ Analytics 
Frequently repeated questions can then be converted into official FAQ entries. 
 
80.25 Troubleshooting Knowledge 
Troubleshooting documentation should be structured around: 
Problem 
What is happening? 
Possible Cause 
What could cause the issue? 
Steps 
What should the user try? 
Result 
What should happen after the fix? 
Escalation 
What should happen if the problem continues? 
Example: 
Problem: 
Google Sign-In shows "Failed to fetch" 
 
Steps: 
1. Check internet connection. 
2. Refresh the page. 
3. Retry Google Sign-In. 

4. Try another supported browser. 
 
If unresolved: 
Contact WiseIN support. 
 
80.26 Error Knowledge 
Error codes and error messages should have dedicated documentation. 
Recommended structure: 
Error Code / Message 
Feature 
Meaning 
Possible Cause 
Recommended Steps 
Known Status 
Escalation Requirement 
Related Documents 
This allows the AI to quickly identify the correct troubleshooting procedure. 
 
80.27 Policy Knowledge 
Policies should be treated differently from general product documentation. 
Examples: 
●​ Privacy 
●​ Security 
●​ Community Guidelines 
●​ Content Policies 
●​ Terms & Conditions 
The AI should use the current approved version of these documents when answering 
policy-related questions. 
 

80.28 Knowledge Security 
Not every document should automatically be available to the AI. 
The knowledge-management system should classify information according to its intended 
audience. 
Example: 
Public 
   ↓ 
User Support 
   ↓ 
Internal 
   ↓ 
Restricted 
The RAG system should respect these access boundaries. 
 
80.29 Knowledge Change Audit 
Important documentation changes should be traceable. 
A change record can include: 
Document: 
64 Account Deletion 
 
Previous Version: 
1.0 
 
New Version: 
2.0 
 
Changed By: 
Authorized Team Member 
 
Reason: 
Updated account deletion workflow 
 
Date: 

[Date] 
This helps the team understand why information changed. 
 
80.30 Knowledge Testing 
Before updated documentation is released to the AI, it should be tested with representative 
questions. 
Document 
64 — Account Deletion 
Test Questions 
●​ "How do I delete my account?" 
●​ "Can I permanently remove my WiseIN account?" 
●​ "What happens after deleting my account?" 
●​ "Is deletion reversible?" 
The team should confirm that RAG retrieves the correct document and that the AI produces 
answers supported by it. 
 
80.31 Regression Testing for Knowledge 
Whenever a major document changes, previously working questions should be tested again. 
Example: 
Knowledge Update 
      ↓ 
Run Existing Test Questions 
      ↓ 
Check Retrieval 
      ↓ 
Check AI Answers 
      ↓ 
Approve 

This prevents a documentation update from accidentally breaking existing AI responses. 
 
80.32 Knowledge Analytics 
Knowledge Management should use the analytics described in 79 — AI Analytics. 
Useful signals include: 
●​ Frequently retrieved documents. 
●​ Documents with poor retrieval. 
●​ Questions with no results. 
●​ Frequently escalated topics. 
●​ Negative feedback. 
●​ Repeated questions. 
●​ Outdated documents. 
●​ Knowledge gaps. 
This provides evidence for deciding what documentation needs attention. 
 
80.33 Knowledge Maintenance Schedule 
Knowledge should be reviewed regularly. 
A practical model is: 
Continuous 
Update documentation when important product or policy changes occur. 
Periodic 
Review major knowledge categories for accuracy. 
Trigger-Based 
Immediately review documentation after: 
●​ Major feature releases. 

●​ UI redesigns. 
●​ Policy changes. 
●​ Security changes. 
●​ Support-process changes. 
●​ Frequently reported issues. 
The exact review frequency should be decided by WiseIN. 
 
80.34 Knowledge Management Roles 
A possible responsibility structure is: 
Product Team 
     │ 
     ├── Feature Documentation 
     │ 
Engineering 
     │ 
     ├── Technical Documentation 
     ├── Error Codes 
     └── Troubleshooting 
     │ 
Support Team 
     │ 
     ├── FAQs 
     ├── Support Workflows 
     └── Escalation 
     │ 
AI Team 
     │ 
     ├── RAG 
     ├── Retrieval Testing 
     └── AI Evaluation 
     │ 
Authorized Management 
     │ 
     └── Policy Approval 
This is a suggested organizational model; WiseIN can define the final ownership structure. 
 

80.35 Knowledge Management Dashboard 
An internal dashboard could provide: 
┌─────────────────────────────────────────────┐ 
│          WISEIN KNOWLEDGE MANAGEMENT        │ 
├──────────────┬──────────────┬───────────────┤ 
│ Active Docs  │ Draft Docs   │ Knowledge Gaps│ 
│     80       │      6       │      14       │ 
├──────────────┴──────────────┴───────────────┤ 
│                                             │ 
│ Documents Requiring Review                  │ 
│                                             │ 
│ • Error Codes                               │ 
│ • Subscriptions                             │ 
│ • Troubleshooting                           │ 
│                                             │ 
├─────────────────────────────────────────────┤ 
│ Frequently Asked Topics                     │ 
│                                             │ 
│ • OTP Issues                                │ 
│ • Login                                     │ 
│ • Profile                                   │ 
│ • Account Deletion                          │ 
│                                             │ 
└─────────────────────────────────────────────┘ 
The numbers shown above are illustrative, not current WiseIN data. 
 
80.36 Knowledge Management + AI 
Analytics 
These two systems should work together. 
AI Analytics discovers: 
Users repeatedly ask a question that the AI cannot answer. 
Knowledge Management responds: 

Create or update the relevant documentation. 
RAG receives: 
New approved knowledge. 
AI Assistant improves: 
It can now answer the question using the updated source. 
AI Analytics 
     ↓ 
Knowledge Gap 
     ↓ 
Knowledge Management 
     ↓ 
Documentation Update 
     ↓ 
Approval 
     ↓ 
RAG Index 
     ↓ 
AI Assistant 
     ↓ 
Better Support 
 
80.37 Knowledge Management + Security 
Knowledge Management must also work with the security requirements defined in 78 — 
Security for AI. 
Before information enters the production knowledge base, the team should determine: 
●​ Is this information intended for users? 
●​ Does it contain sensitive information? 
●​ Should it be publicly accessible? 
●​ Does it contain internal architecture? 
●​ Does it contain credentials or secrets? 
●​ Who should be allowed to retrieve it? 
Sensitive internal information should not be placed into a user-accessible RAG collection. 
 

80.38 Knowledge Management + 
Conversation History 
Conversation History provides user-specific context. 
Knowledge Management provides WiseIN-specific knowledge. 
They should remain conceptually separate. 
Conversation History 
        + 
WiseIN Knowledge Base 
        ↓ 
Context-Aware AI Response 
The AI uses the user's conversation to understand the situation and the knowledge base to 
understand how WiseIN works. 
 
80.39 Knowledge Management + Human 
Support 
Human support should also contribute to knowledge improvement. 
When support agents repeatedly solve the same problem manually, that information can be 
reviewed for possible inclusion in the knowledge base. 
Example: 
Repeated Support Issue 
        ↓ 
Support Team Identifies Pattern 
        ↓ 
Documentation Created 
        ↓ 
Approved 
        ↓ 
RAG Updated 
        ↓ 
AI Can Answer Future Questions 

This can gradually reduce repetitive support work. 
 
80.40 Knowledge Management Best 
Practices 
The WiseIN knowledge system should follow these principles: 
1.​ Use official sources as the primary source of truth. 
2.​ Keep documentation structured and consistent. 
3.​ Assign ownership to important knowledge areas. 
4.​ Review information before publishing it. 
5.​ Maintain document versions. 
6.​ Archive outdated information. 
7.​ Avoid conflicting duplicate documentation. 
8.​ Use metadata for effective retrieval. 
9.​ Track knowledge gaps. 
10.​Test documentation through real user questions. 
11.​Update knowledge when the product changes. 
12.​Use AI analytics to identify documentation problems. 
13.​Protect internal and sensitive information. 
14.​Continuously improve the knowledge base. 
 
80.41 Final Knowledge Management 
Principle 
The WiseIN AI Assistant should not be treated as a system that is built once and left alone. 
WiseIN will continue to change: 
New Features → New Workflows → New Errors → New Policies → New User Questions 
Therefore, the knowledge base must evolve with the product. 
The complete lifecycle is: 

Create → Review → Approve → Publish → Index → Retrieve → Measure → 
Improve → Repeat 
And the relationship between our final AI documentation sections is: 
73 AI Assistant 
       ↓ 
74 AI Limitations 
       ↓ 
75 Conversation History 
       ↓ 
76 AI Tools 
       ↓ 
77 RAG Knowledge 
       ↓ 
78 Security for AI 
       ↓ 
79 AI Analytics 
       ↓ 
80 Knowledge Management 
Final Goal 
Build a knowledge system that keeps the WiseIN AI Assistant accurate, 
current, secure, measurable, and continuously improving. 
 



---

