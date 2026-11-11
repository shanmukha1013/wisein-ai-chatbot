# Terminology

## Source: WISEIN TERMINOLOGY & GLOSSARY 002.pdf

WISEIN TERMINOLOGY & GLOSSARY 
Document ID: WISEIN-TERM-002 
Document Type: Product Terminology & Knowledge Base Reference 
Version: 1.0 
Status: Draft for Product-Team Review 
Organization: Sanshi Network Tech Private Limited 
Platform: WiseIN 
 
1. Document Information 
Document Title: WiseIN Terminology & Glossary 
Document ID: WISEIN-TERM-002 
Version: 1.0 
Purpose: Standardize the terminology used across WiseIN product documentation, 
customer support, development, and AI customer-support systems. 
Primary Audience: 
• 
WiseIN users  
• 
Customer-support team  
• 
Product team  
• 
Development team  
• 
QA team  
• 
Documentation team  
• 
AI/ML team  
• 
AI Customer Support System  
Related Document: 
WISEIN-USER-001 – WiseIN Complete Platform User Guide & Operational Documentation 
 
2. Purpose of This Document 

This document defines important terms, feature names, concepts, and terminology used 
throughout the WiseIN platform. 
The purpose is to ensure that users, support representatives, developers, documentation 
writers, and AI systems use the same terminology when referring to WiseIN features. 
A standardized terminology system is particularly important for the WiseIN AI Customer 
Support System because users may ask the same question using different words. 
For example, a user may ask: 
"How do I find people?" 
"How can I search professionals?" 
"Where can I discover members?" 
These questions may refer to the Explore and Member Discovery functionality. 
The glossary helps the AI understand that different expressions can refer to the same 
WiseIN concept. 
 
 
 
 
 
 
3. Scope 
This glossary covers terminology related to: 
• 
WiseIN platform  
• 
User accounts  
• 
Profiles  
• 
Verification  
• 
Networking  
• 
Home and Feed  

• 
Explore  
• 
Waves  
• 
Jobs  
• 
Chat and Messaging  
• 
Meetings  
• 
Events  
• 
Organizations  
• 
Notifications  
• 
Settings  
• 
Subscriptions  
• 
Privacy and Safety  
• 
Customer Support  
• 
AI Customer Support  
• 
RAG and Knowledge Base systems  
This document is intended to be a terminology reference, not a complete user manual. 
Detailed user procedures should remain in the WiseIN User Guide. 
4. General WiseIN Terminology 
4.1 WiseIN 
Definition: 
WiseIN is a professional networking platform focused on verified identity, professional 
networking, recruitment, communication, events, and business interaction. 
The existing platform guide describes WiseIN as a trust-focused professional networking 
platform created by Sanshi Network Tech Private Limited.  
AI Interpretation: 
When users mention "WiseIn", "WiseIN platform", "WiseIN app", or "WiseIN website", they 
are referring to the WiseIN platform. 
 

4.2 Member 
Definition: 
A person who has an account on WiseIN. 
AI Interpretation: 
"User", "member", "WiseIN member", and "account holder" may refer to the same person 
depending on context. 
 
4.3 Verified Member 
Definition: 
A WiseIN member whose identity verification has been successfully completed. 
The platform guide describes government identity verification and assignment of a blue 
verified checkmark after successful verification.  
 
4.4 Verified Profile 
Definition: 
A member profile associated with a successfully verified WiseIN identity. 
 
4.5 Verified Checkmark 
Definition: 
The visual verification indicator displayed on an eligible verified member profile. 
 
4.6 Platform Access 
Definition: 
The features and functionality available to a user based on their account status, 
verification status, permissions, and platform rules. 
 
5. Account & User Terminology 
5.1 Account 

Definition: 
A user's registered identity and access record within WiseIN. 
 
 
5.2 Username 
Definition: 
The unique platform identifier selected by a user during registration. 
The current user guide describes username creation during sign-up and indicates that the 
username may be checked against identity naming requirements.  
 
5.3 Email Address 
Definition: 
The email address associated with a WiseIN account and used for account-related 
communication and verification. 
 
5.4 OTP 
Full Form: One-Time Password 
Definition: 
A temporary verification code used to confirm ownership or authorization of an account-
related action. 
The WiseIN guide describes a six-digit email OTP during account registration.  
 
5.5 Sign Up 
Definition: 
The process of creating a new WiseIN account. 
 
 
5.6 Sign In / Login 

Definition: 
The process of accessing an existing WiseIN account using the user's authentication 
credentials. 
 
5.7 Session 
Definition: 
An authenticated period during which a user is logged into WiseIN. 
 
5.8 Log Out 
Definition: 
The action used to terminate the current authenticated session. 
 
5.9 Deactivate Account 
Definition: 
An account-control action that temporarily pauses a user's profile activity. 
The existing guide describes deactivation as hiding the profile, posts, and comments until 
the user logs back in.  
 
5.10 Delete Account 
Definition: 
An account-control action intended to permanently remove the user's account and 
associated data according to WiseIN's applicable deletion process. 
The current guide describes a 30-day deletion grace period and permanent data purge 
afterward. This behavior should be confirmed against the production implementation 
before being treated as a final product specification. 
 
 
 
6. Profile Terminology 

6.1 Profile 
Definition: 
The professional identity page representing a WiseIN member. 
 
6.2 Profile Avatar / Profile Photo 
Definition: 
The primary image representing a user's profile. 
 
6.3 Cover Banner 
Definition: 
The background or banner image displayed on a user's profile. 
 
6.4 Headline 
Definition: 
A short professional description displayed on a user's profile. 
 
6.5 Bio 
Definition: 
A short description of the user's professional background, interests, skills, or role. 
 
6.6 About Section 
Definition: 
A more detailed section containing information about the user's professional background. 
 
6.7 Experience 
Definition: 
The section of a profile containing professional employment or work history. 

The current guide identifies Job Title, Company Name, Employment Type, and Start/End 
Dates as experience information.  
 
6.8 Education 
Definition: 
The section containing a user's academic information. 
Typical fields described in the guide include degree, field of study, and institution.  
 
6.9 Skills 
Definition: 
Professional or technical abilities listed on a member's profile. 
 
6.10 Verified Employment Tag 
Definition: 
A professional employment indicator associated with an organization registered on WiseIN, 
as described in the current user guide. 
This behavior should be confirmed against the current implementation. 
 
 
 
 
7. Networking Terminology 
7.1 Network 
Definition: 
The collection of professional connections associated with a WiseIN member. 
 
7.2 My Network 

Definition: 
The WiseIN area where members can manage and interact with their professional 
connections. 
The current guide describes My Network as the place to accept incoming connection 
requests.  
 
7.3 Connection 
Definition: 
A professional relationship established between two WiseIN members. 
 
7.4 Connection Request 
Definition: 
A request sent from one member to another to establish a connection. 
 
7.5 Connect 
Definition: 
The action used to send or establish a professional connection with another member. 
 
7.6 Follower 
Definition: 
A member who follows another member's public activity or content. 
Product-Team Verification Required: 
The exact behavior and permissions associated with following should be confirmed against 
the current WiseIN implementation. 
 
7.7 Following 
Definition: 
The relationship created when a member follows another member. 
 

7.8 Member Discovery 
Definition: 
The process of finding relevant professional members through WiseIN's discovery and 
search functionality 
 
8. Home & Feed Terminology 
8.1 Home 
Definition: 
The primary area from which users access their WiseIN content and platform activity. 
Product-Team Verification Required: 
The exact current Home-page functionality should be confirmed from the production 
application. 
 
8.2 Feed 
Definition: 
A stream of content displayed to a user. 
 
8.3 Post 
Definition: 
A piece of content published by a WiseIN member or organization. 
 
8.4 Engagement 
Definition: 
User interaction with content, such as likes, comments, or other supported actions. 
The existing guide specifically references post engagement through likes and comments.  
 
8.5 Like 
Definition: 
An interaction indicating that a user appreciates or engages with a post. 

 
8.6 Comment 
Definition: 
A response or message posted in relation to content. 
 
8.7 Saved Content 
Definition: 
Content that a user has bookmarked for later access. 
The current guide identifies saved posts, saved Waves, and saved jobs.  
 
8.8 Saved Post 
Definition: 
A bookmarked post stored for later access. 
 
 
 
 
9. Explore Terminology 
9.1 Explore 
Definition: 
WiseIN's member-discovery area used to search for relevant professionals. 
 
9.2 Search Query 
Definition: 
The text entered by a user to search for relevant members. 
 
9.3 Role Filter 

Definition: 
A filter used to narrow member results according to professional role. 
 
9.4 Location Filter 
Definition: 
A filter used to narrow search results according to location. 
 
9.5 Skills Filter 
Definition: 
A filter used to find members based on listed skills. 
 
9.6 Verified Status Filter 
Definition: 
A filter used to identify members based on verification status. 
 
9.7 Meeting Availability 
Definition: 
A discovery filter indicating whether a member is available for 1:1 video meetings. 
The existing guide identifies role, location, skills, verification status, and 1:1 video-call 
availability as Explore filters.  
 
 
 
 
 
 
 
 

 
 
 
10. Waves Terminology 
10.1 Wave 
Definition: 
A short-form vertical video published on WiseIN. 
The existing guide identifies Waves as the platform's short-form video hub.  
 
10.2 Create Wave 
Definition: 
The action used to create and publish a new Wave. 
 
10.3 Wave Upload 
Definition: 
The process of selecting and uploading a video for publication as a Wave. 
 
10.4 Wave Title 
Definition: 
The title associated with a Wave. 
 
10.5 Wave Hashtag 
Definition: 
A hashtag associated with a Wave to describe or categorize its content. 
 
10.6 Published Wave 
Definition: 
A Wave that has successfully been published and made available through the Waves 
experience. 
 
 

11. Jobs Terminology 
11.1 Jobs 
Definition: 
The WiseIN recruitment area where users can discover job opportunities. 
 
11.2 Job Seeker 
Definition: 
A WiseIN member using the platform to discover or apply for employment opportunities. 
 
11.3 Employer 
Definition: 
An organization or authorized representative using WiseIN to publish recruitment 
opportunities. 
 
11.4 Job Listing 
Definition: 
A published recruitment opportunity containing information about a role. 
 
11.5 Job Posting 
Definition: 
The process of publishing a job opportunity on WiseIN. 
 
11.6 Job Requirements 
Definition: 
The qualifications, skills, experience, or other conditions associated with a job. 
 
 
11.7 Screening Questions 
Definition: 
Questions included by an employer to collect additional information from applicants. 
 

11.8 Easy Apply 
Definition: 
The WiseIN application process allowing a job seeker to apply using their verified profile. 
The existing guide describes job seekers searching a listing and using Easy Apply with their 
verified profile.  
 
11.9 Job Recommendation 
Definition: 
A job opportunity recommended to a user based on the platform's available 
recommendation functionality. 
Product-Team Verification Required: 
Exact recommendation logic should be confirmed. 
 
 
 
 
 
 
 
 
 
 
12. Chat & Messaging Terminology 
12.1 Chat 
Definition: 
The WiseIN communication area used for direct messaging between eligible members. 
 
12.2 Direct Chat 
Definition: 
A direct communication channel between WiseIN members. 
 

12.3 Message 
Definition: 
A communication item sent through the WiseIN chat system. 
 
12.4 Verified Chat 
Definition: 
Chat functionality associated with verified WiseIN members. 
The existing guide describes Chat as a way to message connected verified members.  
 
12.5 Chat Notification 
Definition: 
A notification informing a user about a new or relevant chat message. 
 
12.6 Spam-Free Messaging 
Definition: 
WiseIN's approach to professional communication intended to reduce unwanted or bot-
generated messaging through verification and platform controls. 
 
13. Meetings Terminology 
13.1 Meeting 
Definition: 
A scheduled interaction between WiseIN members, including supported 1:1 or group video 
meetings. 
The platform guide identifies 1:1 and group video meetings as part of WiseIN's platform 
capabilities.  
 
13.2 1:1 Video Meeting 
Definition: 
A video meeting involving two participants. 
 
13.3 Group Video Meeting 

Definition: 
A video meeting involving multiple participants. 
 
13.4 Book Meeting 
Definition: 
The action used to request or schedule a meeting with an eligible member. 
 
13.5 Meeting Invite 
Definition: 
An invitation associated with a video meeting. 
 
 
 
 
13.6 Meeting Eligibility 
Definition: 
The conditions determining who can request or book a meeting with a member. 
The current settings guide describes meeting eligibility options including Everyone, Verified 
Members Only, and Connections Only.  
 
13.7 Meeting Summary 
Definition: 
A summary associated with a completed meeting. 
 
13.8 Meeting Transcription 
Definition: 
A text representation generated from meeting audio. 
The WiseIN platform guide describes automated post-meeting transcription and 
summaries as part of its AI collaboration capabilities.  
 
13.9 Action Items 

Definition: 
Tasks or follow-up activities identified from a meeting. 
 
13.10 Executive Summary 
Definition: 
A concise summary of important information from a meeting. 
 
 
 
 
14. Events & Conversations Terminology 
14.1 Event 
Definition: 
A WiseIN activity or organized session made available for users to discover or participate 
in. 
Product-Team Verification Required: 
Exact event types and workflows should be confirmed against the current application. 
 
14.2 Event Registration 
Definition: 
The process of registering to participate in an event. 
 
14.3 Event Organizer 
Definition: 
The person or organization responsible for an event. 
 
14.4 Event Participant 
Definition: 
A user registered to participate in an event. 
 
14.5 Event Notification 

Definition: 
A notification related to an event, such as an invitation, update, reminder, or 
announcement. 
 
14.6 Conversation 
Definition: 
A communication or discussion associated with a supported WiseIN interaction. 
Product-Team Verification Required: 
The exact meaning of "Conversation" as a named WiseIN feature should be confirmed 
before using it as a specific AI intent. 
15. Organizations Terminology 
15.1 Organization 
Definition: 
A business or corporate entity represented on WiseIN. 
The platform guide describes WiseIN for Business through organization pages and 
corporate verification.  
 
15.2 Organization Page 
Definition: 
A WiseIN page representing an organization. 
 
15.3 Organization Profile 
Definition: 
The professional information associated with an organization page. 
 
15.4 Corporate Verification 
Definition: 
The process used to verify an organization's business identity. 
The current guide describes verification using information such as CIN, GSTIN, company 
PAN, and corporate email-domain verification.  
 
 

15.5 Verified Business Badge 
Definition: 
The verification indicator associated with an organization that has successfully completed 
the applicable corporate verification process. 
 
15.6 Corporate Email Domain 
Definition: 
An organization's official email domain used as part of corporate verification. 
 
15.7 Organization Admin 
Definition: 
An authorized person responsible for managing an organization page. 
Product-Team Verification Required: 
Exact organization-admin permissions should be confirmed. 
 
16. Verification Terminology 
16.1 Identity Verification 
Definition: 
The process of validating a member's identity using supported government identity 
verification methods. 
 
16.2 Government ID 
Definition: 
An identity document or government-backed identity source used for verification. 
 
16.3 DigiLocker Verification 
Definition: 
A verification method described in the WiseIN guide using the DigiLocker gateway. 
 
16.4 Aadhaar Verification 
Definition: 
A government identity verification method using Aadhaar information and OTP. 

 
16.5 PAN Verification 
Definition: 
A verification method using PAN information and the user's legal name. 
 
16.6 Video Liveness Check 
Definition: 
A camera-based identity verification step used to confirm that the person completing 
verification is physically present. 
The current guide describes a short face-liveness scan as part of the verification process.  
 
16.7 Verification Failure 
Definition: 
A condition in which the identity verification process cannot be successfully completed. 
Possible causes described by the guide include name mismatch or an unclear camera 
scan.  
 
16.8 Identity Mismatch 
Definition: 
A situation where identity information supplied during verification does not sufficiently 
match the account or verification records. 
 
 
17. Subscription Terminology 
17.1 Subscription 
Definition: 
A paid or free service plan associated with an eligible WiseIN account. 
 
17.2 Subscription Plan 
Definition: 
A defined level of WiseIN service associated with specific features or billing conditions. 
 

17.3 Free Trial 
Definition: 
A trial subscription state where applicable. 
 
17.4 Professional Plan 
Definition: 
A subscription tier identified in the existing platform documentation. 
 
17.5 Enterprise Plan 
Definition: 
A subscription tier identified in the existing platform documentation. 
 
17.6 Billing Cycle 
Definition: 
The period over which a subscription is billed. 
The current guide identifies monthly and annual billing options.  
 
17.7 Payment Method 
Definition: 
A supported method used to pay for a subscription. 
 
17.8 Invoice 
Definition: 
A billing document associated with a subscription or payment. 
 
17.9 Upgrade 
Definition: 
The process of moving from one subscription level to another with additional or different 
capabilities. 
 
17.10 Downgrade 

Definition: 
The process of moving to a lower subscription level 
 
18. Privacy & Safety Terminology 
18.1 Data Privacy 
Definition: 
The controls and practices governing how user information, profile visibility, and related 
data are handled. 
 
18.2 Profile Visibility 
Definition: 
A setting controlling who can view a user's profile. 
The current guide identifies Public and Network Only visibility options.  
 
18.3 Search Engine Indexing 
Definition: 
The setting controlling whether a profile may be indexed by external search engines. 
 
18.4 Connection List Privacy 
Definition: 
A setting controlling who can view a user's connections. 
 
18.5 Blocked User 
Definition: 
A member whose interaction with another user has been restricted through the blocking 
functionality. 
 
18.6 Block 
Definition: 
The action used to restrict another member's interactions. 
 
18.7 Unblock 

Definition: 
The action used to restore interaction permissions with a previously blocked member. 
The current guide describes a Blocked Users List and Unblock action.  
 
18.8 Two-Factor Authentication 
Abbreviation: 2FA 
Definition: 
An additional authentication layer used to improve account security. 
The existing guide identifies SMS OTP and authenticator-app options.  
 
18.9 Login Session 
Definition: 
An active authenticated session associated with a user's account. 
 
18.10 Revoke Session 
Definition: 
The action used to terminate a specific active login session. 
 
18.11 Data Export 
Definition: 
The process of requesting or downloading a copy of user-associated data, where 
supported. 
The current guide describes a "Download My Data Archive" function. 
 
19. Notifications Terminology 
19.1 Notification 
Definition: 
An alert informing a user about relevant activity or updates on WiseIN. 
 
19.2 In-App Notification 

Definition: 
A notification displayed inside the WiseIN application. 
 
19.3 Push Notification 
Definition: 
A notification delivered through the supported device notification system. 
 
19.4 Email Digest 
Definition: 
A collection of notifications or updates delivered through email. 
 
19.5 Connection Notification 
Definition: 
An alert related to connection requests or connection activity. 
 
19.6 Meeting Notification 
Definition: 
An alert related to a meeting invitation or meeting activity. 
 
19.7 Job Recommendation Notification 
Definition: 
An alert related to recommended job opportunities. 
The existing settings documentation identifies these notification categories.  
 
20. Settings Terminology 
The current WiseIN user guide identifies a Settings module containing multiple account-
management areas.  
20.1 Edit Profile 
Used to manage profile information. 
20.2 Notifications 
Used to manage notification preferences. 

20.3 Sign In & Security 
Used to manage password, 2FA, sessions, and security settings. 
20.4 Subscriptions 
Used to manage subscription and billing information. 
20.5 Data Privacy 
Used to manage profile visibility and privacy controls. 
20.6 Scheduled Post 
Used to manage scheduled content. 
20.7 Saved Content 
Used to access saved posts, Waves, and jobs. 
20.8 My Ads 
Used for advertising and campaign management where applicable. 
20.9 Blocked 
Used to manage blocked members. 
20.10 Deactivate 
Used to temporarily deactivate an account. 
20.11 Delete Account 
Used to initiate account deletion. 
20.12 Log Out 
Used to end the current session. 
 
21. Advertising Terminology 
21.1 My Ads 
Definition: 
The advertising management area described in the current WiseIN settings documentation. 
 
21.2 Campaign 
Definition: 
A collection of advertising activities created for a specific promotional objective. 

 
21.3 Sponsored Post 
Definition: 
A promoted piece of content used as part of an advertising campaign. 
 
21.4 Targeting 
Definition: 
The process of selecting the audience for promotional content. 
 
21.5 Campaign Budget 
Definition: 
The amount allocated to an advertising campaign. 
 
21.6 Campaign Schedule 
Definition: 
The time period during which an advertising campaign runs. 
 
21.7 CTR 
Full Form: Click-Through Rate 
Definition: 
A metric representing the proportion of impressions that result in clicks. 
 
21.8 ROI 
Full Form: Return on Investment 
Definition: 
A measurement used to evaluate the return generated relative to the investment made. 
The current guide identifies campaign targeting, budget, schedule, CTR, conversion costs, 
and ROI.  
 
22. Customer Support Terminology 
22.1 Help & Support 

Definition: 
The WiseIN area providing customer assistance, support requests, documentation, FAQs, 
and related support resources. 
The existing guide identifies Help & Support as providing direct support, ticketing, live chat, 
and documentation.  
 
22.2 Support Ticket 
Definition: 
A support request submitted by a user to report an issue or request assistance. 
 
22.3 Support Request 
Definition: 
A request submitted to the WiseIN support team. 
 
22.4 FAQ 
Full Form: Frequently Asked Questions 
Definition: 
A collection of commonly asked questions and answers about WiseIN. 
 
22.5 Live Chat 
Definition: 
A real-time support communication channel where available. 
 
22.6 Support SLA 
Full Form: Service Level Agreement 
Definition: 
The target timeframe associated with responding to a support request. 
The current guide states a target response within 24 hours and Monday-Friday support 
availability. These details should be verified against the current support policy before being 
treated as contractual commitments.  
 
23. AI Customer Support Terminology 

This section defines terminology used specifically for the future WiseIN AI Customer 
Support System. 
23.1 AI Customer Support System 
Definition: 
An AI-powered system designed to answer WiseIN user questions and assist users with 
platform information and supported workflows. 
 
23.2 AI Assistant 
Definition: 
The conversational AI interface through which users interact with the WiseIN support 
system. 
 
23.3 Chatbot 
Definition: 
A conversational software interface that receives user questions and generates responses. 
 
23.4 User Query 
Definition: 
A question, request, or statement submitted by a WiseIN user to the AI assistant. 
 
23.5 Intent 
Definition: 
The underlying purpose of a user's query. 
Examples: 
• 
Account help  
• 
Profile help  
• 
Verification help  
• 
Job search  
• 
Meeting booking  
• 
Chat help  
• 
Organization help  

• 
Support request  
• 
Documentation request  
 
23.6 Entity 
Definition: 
A specific object or concept identified within a user query. 
Examples: 
• 
User  
• 
Job  
• 
Organization  
• 
Event  
• 
Wave  
• 
Meeting  
• 
Profile  
• 
Account  
 
23.7 Context 
Definition: 
Information from the current conversation or authorized application data that helps the AI 
understand the user's request. 
 
23.8 Conversation History 
Definition: 
Previous messages exchanged during an AI-chat session that may be used to understand 
follow-up questions. 
 
23.9 Grounded Response 
Definition: 
An AI response based on approved WiseIN information rather than unsupported 
assumptions. 
 

23.10 Hallucination 
Definition: 
An AI-generated statement that is incorrect, unsupported, or not present in the approved 
knowledge sources. 
 
23.11 Fallback Response 
Definition: 
A controlled response provided when the AI cannot confidently answer a question. 
Example: 
"I couldn't find this information in the available WiseIN documentation. Please contact 
WiseIN Support for assistance." 
 
24. Documentation & RAG Terminology 
24.1 Knowledge Base 
Definition: 
A collection of approved information used by the AI system to answer WiseIN-related 
questions. 
 
24.2 Knowledge Source 
Definition: 
An individual document, webpage, FAQ, product specification, support article, or other 
approved source used to build the knowledge base. 
 
24.3 RAG 
Full Form: Retrieval-Augmented Generation 
Definition: 
An AI architecture in which relevant information is retrieved from a knowledge source 
before the language model generates an answer. 
 
24.4 Retrieval 
Definition: 
The process of finding relevant information from the knowledge base based on a user's 
question. 

 
24.5 Embedding 
Definition: 
A numerical representation of text that allows semantically similar content to be searched. 
 
24.6 Vector Database 
Definition: 
A database or storage system designed to store and search vector embeddings. 
 
24.7 Document Chunk 
Definition: 
A smaller section of a document created so that relevant information can be retrieved 
efficiently. 
 
24.8 Semantic Search 
Definition: 
A search method that finds information based on meaning and context rather than only 
exact keyword matching. 
 
24.9 Retrieved Context 
Definition: 
The information retrieved from the knowledge base and provided to the AI model before 
generating an answer. 
 
24.10 Source Citation 
Definition: 
A reference identifying the source from which information used in an AI response was 
obtained. 
 
24.11 Ground Truth 
Definition: 
An approved and verified answer or piece of product information used as the reference for 
evaluating AI responses. 

 
24.12 Knowledge Base Update 
Definition: 
The process of adding, modifying, or removing approved information from the AI knowledge 
base when WiseIN functionality changes. 
 
25. AI Query Understanding Examples 
The AI should recognize that users may use different words for the same WiseIN concept. 
User Expression 
Possible WiseIN Concept 
"My account" 
Account 
"My profile" 
Profile 
"Verify my identity" 
Identity Verification 
"Blue tick" 
Verified Checkmark 
"Find professionals" 
Explore / Member Discovery 
"Connect with someone" 
Connection 
"Send connection request" 
Connection Request 
"Short videos" 
Waves 
"Find jobs" 
Jobs 
"Apply for a job" 
Easy Apply / Job Application 
"Message someone" 
Chat / Direct Chat 
"Video call" 
1:1 Video Meeting 
"Company page" 
Organization Page 
"Verify my company" 
Corporate Verification 
"Help me" 
Help & Support 
"Frequently asked questions" 
FAQ 
"My saved posts" 
Saved Content 

User Expression 
Possible WiseIN Concept 
"Who blocked me / blocked users" Blocked 
"Turn off my account" 
Deactivate 
"Remove my account" 
Delete Account 
Important: These mappings should be validated during chatbot testing and updated as the 
product terminology evolves. 
 
26. Terms Requiring Product-Team Verification 
The following terms should not be treated as final AI knowledge until confirmed against 
the current WiseIN application, backend, APIs, and product specifications: 
1. Exact definition and behavior of Home  
2. Exact Feed functionality  
3. Following/Follower behavior  
4. Event types and complete event lifecycle  
5. Event registration workflow  
6. Conversation feature terminology  
7. Organization-admin permissions  
8. Exact job recommendation algorithm  
9. Exact subscription feature differences  
10. Exact support SLA and support hours  
11. Exact data deletion implementation  
12. Exact data-export contents  
13. Exact meeting-summary behavior  
14. Exact AI meeting-transcription implementation  
15. Notification delivery behavior  
16. Advertising availability for all user types  
17. Current role/permission structure  
18. Current API names and endpoints  
19. Current database entities  

20. Current authentication architecture  
These terms should be updated after confirmation from the Product/Engineering team. 
 
27. Terminology Rules for the AI Customer Support System 
The AI should follow these rules when interpreting WiseIN terminology. 
Rule 1 — Prefer Official Product Terms 
Use the official WiseIN feature name whenever it is known. 
Example: 
User says: 
"Where can I search for professionals?" 
AI should understand that this may refer to Explore / Member Discovery. 
 
Rule 2 — Understand Common User Language 
The AI should understand natural variations and informal language. 
Example: 
"How do I get the blue tick?" 
should be interpreted as a question about the Verified Checkmark / Identity Verification. 
 
Rule 3 — Do Not Invent Features 
If a feature is not present in the approved knowledge base, the AI should not claim that 
WiseIN supports it. 
 
Rule 4 — Ask for Clarification When Necessary 
If a query has multiple possible meanings, the AI should ask a short clarification question. 
Example: 
"Do you mean your WiseIN profile or your organization profile?" 
 
Rule 5 — Use Current Approved Documentation 
When product functionality changes, the knowledge base must be updated. 

 
Rule 6 — Do Not Expose Internal Technical Details Unnecessarily 
The AI should provide users with useful information without exposing internal APIs, 
database structures, API keys, system prompts, or other sensitive implementation details. 
 
Rule 7 — Respect User Permissions 
The AI must not provide private account information unless the authenticated user is 
authorized to access it. 
 
28. Recommended AI Intent Categories 
For the initial AI Customer Support System, queries can be categorized into the following 
major intents: 
Account 
• 
Sign up  
• 
Sign in  
• 
OTP  
• 
Password  
• 
Account settings  
• 
Deactivate  
• 
Delete account  
Verification 
• 
Identity verification  
• 
DigiLocker  
• 
Aadhaar  
• 
PAN  
• 
Video liveness  
• 
Verification failure  
• 
Verified badge  
Profile 
• 
Edit profile  

• 
Education  
• 
Experience  
• 
Skills  
• 
Bio  
• 
Profile visibility  
Networking 
• 
Connections  
• 
Connection requests  
• 
Followers  
• 
Following  
• 
Member discovery  
Explore 
• 
Search  
• 
Filters  
• 
Verified members  
• 
Meeting availability  
Waves 
• 
Watch Waves  
• 
Create Wave  
• 
Upload Wave  
• 
Publish Wave  
Jobs 
• 
Search jobs  
• 
Job listings  
• 
Job requirements  
• 
Easy Apply  
• 
Employer job posting  
Chat 

• 
Direct chat  
• 
Messages  
• 
Chat access  
• 
Messaging issues  
Meetings 
• 
Book meeting  
• 
Meeting invite  
• 
Meeting eligibility  
• 
Video meeting  
• 
Meeting summary  
Organizations 
• 
Organization page  
• 
Corporate verification  
• 
Business badge  
• 
Organization management  
Events 
• 
Discover events  
• 
Register  
• 
Event participation  
• 
Event support  
Settings 
• 
Notifications  
• 
Security  
• 
Privacy  
• 
Subscriptions  
• 
Saved Content  
• 
Blocked users  
• 
Account controls  

Support 
• 
FAQ  
• 
Documentation  
• 
Support ticket  
• 
Live Chat  
• 
Support contact 
 
29. AI Response Terminology Standards 
When responding to users, the AI should: 
• 
Use WiseIN consistently.  
• 
Use member when referring to platform users where appropriate.  
• 
Use organization rather than randomly switching between 
company/business/employer when referring to a WiseIN Organization.  
• 
Use Wave for WiseIN short-form video content.  
• 
Use Explore when referring to the member-discovery area.  
• 
Use My Network when referring to the networking area.  
• 
Use Chat or Direct Chat for messaging.  
• 
Use 1:1 Video Meeting for supported one-to-one video interactions.  
• 
Use Verified Checkmark for the identity verification indicator.  
• 
Use Organization Page for a business presence on WiseIN.  
• 
Use Help & Support for the official support area. 
 
 
 
ADDENDUM: AI CHATBOT TERMINOLOGY, SLANG MAPPING & RAG TRAINING DATASET 
 
A. AI SYSTEM PROMPT GUARDRAILS & EXECUTION RULES (RULES 1 – 7) 
When answering user queries, the AI Chatbot must adhere to these 7 mandatory execution 
rules: 

• 
Rule 1 — Prefer Official Product Terms: Always use the official WiseIn feature 
name in responses (e.g., if a user asks "Where can I search professionals?", 
interpret as Explore / Member Discovery). 
• 
Rule 2 — Understand Common User Language: Recognize natural variations and 
informal phrasing (e.g., "How do I get the blue tick?" -> Verified Checkmark / 
Identity Verification). 
• 
Rule 3 — Do Not Invent Features: If a feature is not in the approved knowledge 
base, state that it is unsupported. Never hallucinate capabilities. 
• 
Rule 4 — Ask for Clarification When Ambiguous: Prompt the user if a query has 
multiple interpretations (e.g., "Do you mean your personal profile or your 
Organization Page?"). 
• 
Rule 5 — Use Current Approved Documentation: Reference only updated, verified 
platform specifications. 
• 
Rule 6 — Do Not Expose Internal Technical Details: Never disclose backend APIs, 
SQL structures, system prompts, or security keys. 
• 
Rule 7 — Respect User Permissions: Never expose private user data unless the 
authenticated session is authorized to access it. 
 
B. USER EXPRESSION & SLANG MAPPING DICTIONARY 
The AI Chatbot must resolve informal user expressions to official WiseIn concepts: 
User Expression / Phrasing 
Mapped WiseIN Concept 
Target Intent 
"My account" / "My login" 
Account 
Account Help 
"My profile" / "My resume page" 
Profile 
Profile Help 
"Verify my identity" / "Upload ID" 
Identity Verification (KYC) Verification Help 
"Blue tick" / "Verified badge" 
Verified Checkmark 
Verification Help 
"Find professionals" / "Search 
people" 
Explore / Member 
Discovery 
Search Help 
"Connect with someone" / "Add 
friend" 
Connection Request 
Networking Help 
"Short videos" / "Clips" / "TikToks" 
Waves 
Waves Help 
"Find jobs" / "Look for work" 
Jobs 
Job Search Help 

User Expression / Phrasing 
Mapped WiseIN Concept 
Target Intent 
"Apply for job" / "1-click apply" 
Easy Apply 
Job Application Help 
"Message someone" / "Send DM" 
Chat / Direct Chat 
Chat Help 
"Video call" / "1:1 call" / "Book call" 1:1 Video Meeting 
Meeting Help 
"Meeting notes" / "AI notes" 
AI Meeting Summary 
Meeting Help 
"Company page" / "Business profile" Organization Page 
Organization Help 
"Verify my company" / "GST check" 
Corporate Verification 
Organization 
Verification 
"Turn off account" / "Pause account" Deactivate Account 
Account Controls 
"Delete my profile" / "Purge data" 
Delete Account 
Account Deletion 
"Report issue" / "Talk to human" 
Help & Support 
Support Request 
 
C. AI INTENT & ENTITY CLASSIFICATION TAXONOMY 
Intent Categories for Chatbot Training: 
1. intent.account.signup – Questions regarding account creation & username naming 
rules. 
2. intent.account.signin – Login issues, password resets, and OTP validation. 
3. intent.account.deactivate – Temporary profile deactivation requests. 
4. intent.account.delete – Permanent data deletion instructions & 30-day grace 
period. 
5. intent.verification.kyc – Identity verification process (DigiLocker, Aadhaar, PAN). 
6. intent.verification.liveness – Camera face scan guidelines. 
7. intent.verification.status – Blue checkmark status inquiries. 
8. intent.profile.edit – Editing headline, bio, experience, education, and photo. 
9. intent.explore.search – Member search and filter criteria. 
10. intent.waves.create – Recording and uploading vertical short videos. 
11. intent.meetings.book – Scheduling 1:1 calls and setting calendar availability. 
12. intent.meetings.aisummary – Accessing post-call AI summaries and action items. 

13. intent.jobs.apply – Easy Apply process using verified resumes. 
14. intent.jobs.post – Employer job posting & recruiter screening. 
15. intent.org.verify – Corporate verification via CIN, GSTIN, PAN, and corporate email. 
16. intent.support.ticket – Submitting a support request form. 
Recognized Entities: 
• 
@Entity.User (Member, Username, Profile) 
• 
@Entity.VerificationDoc (DigiLocker, Aadhaar, PAN, Video Liveness) 
• 
@Entity.Meeting (1:1 Meeting, Group Call, AI Summary, Action Items) 
• 
@Entity.Job (Job Listing, Easy Apply, Recruiter AMS) 
• 
@Entity.Wave (Wave Video, Creator Studio, Hashtags) 
• 
@Entity.Organization (Company Page, CIN, GSTIN, Corporate Email Domain) 
 
D. AI & RAG TECHNICAL TERMINOLOGY DEFINITIONS 
• 
AI Customer Support System: An AI-powered conversational system designed to 
answer WiseIn user questions and assist with platform workflows. 
• 
AI Assistant / Chatbot: The conversational software interface through which 
members interact with WiseIn support. 
• 
User Query: A question, request, or statement submitted by a WiseIn user to the 
chatbot. 
• 
Context: Information from the active conversation or authorized application session 
that helps the AI understand user intent. 
• 
Conversation History: Previous messages exchanged during a chat session used to 
resolve follow-up questions. 
• 
Grounded Response: An AI answer strictly derived from approved WiseIn 
documentation rather than unverified assumptions. 
• 
Hallucination: An incorrect or unsupported statement generated by the AI that is 
not present in approved knowledge sources. 
• 
Fallback Response: A controlled default response provided when the AI cannot 
confidently answer a query (e.g., "I couldn't find this information in official WiseIn 
documentation. Please contact support@wisein.in"). 
• 
Knowledge Base: The collection of approved documents, FAQs, and product specs 
used by the RAG system. 

• 
Knowledge Source: An individual webpage, FAQ, or document chunk used to train 
the chatbot. 
• 
RAG (Retrieval-Augmented Generation): An AI architecture that retrieves relevant 
knowledge chunks before generating a response. 
• 
Embedding: A numerical vector representation of text enabling semantic search 
over user queries. 
• 
Vector Database: Storage system designed to index and search text embeddings. 
• 
Document Chunk: A segmented section of a document processed for efficient AI 
retrieval. 
• 
Semantic Search: Searching content based on contextual meaning rather than 
exact keyword matching. 
• 
Source Citation: A reference link indicating the knowledge source used in an AI 
response. 
• 
Ground Truth: Approved, verified product documentation used to benchmark AI 
response accuracy. 
• 
Knowledge Base Update: The maintenance workflow of adding or modifying 
knowledge sources when features change. 
 
E. 20 TERMS REQUIRING PRODUCT-TEAM VERIFICATION 
The following 20 implementation details must be confirmed with the engineering team 
before locking into final chatbot responses: 
1. Exact definition and tab behavior of Home feed ranking algorithms. 
2. Exact Feed filtering logic for Looking for, Opportunity, and Ask. 
3. Follower vs. Connection permission differences. 
4. Event types and complete event lifecycle workflows. 
5. Event registration workflow integration with DigiLocker. 
6. Conversation feature naming vs. Direct Chat. 
7. Organization-admin permission roles (Owner, Editor, Recruiter). 
8. Exact job recommendation algorithm logic. 
9. Feature breakdown across Free, Professional, and Enterprise subscription tiers. 
10. Support SLA commitments (target: 24h response, Mon-Fri). 
11. Technical implementation of account data deletion. 

12. Data Export Archive contents format (.zip payload). 
13. AI Meeting Summary processing time (target: 2–5 mins post-call). 
14. AI speech-to-text transcription language support. 
15. Notification delivery rules & push batching. 
16. Advertising campaign eligibility for individual vs. corporate accounts. 
17. Current Role-Based Access Control (RBAC) permissions structure. 
18. Production API endpoint names and schemas. 
19. Database entity relation schemas. 
20. Single Sign-On (SSO) and OAuth authentication architecture. 
 
F. STANDARD FALLBACK & DISAMBIGUATION TEMPLATES 
Fallback Template (Confidence Score < 70%): 
"I couldn't find this specific information in official WiseIn documentation. Please submit 
your question via our Help & Support Portal or contact support@wisein.in for direct 
assistance." 
Disambiguation Template (Vague Query): 
"Could you please clarify whether you are asking about your personal member profile or 
your company's Organization Page?" 
 
 
 
 



---

