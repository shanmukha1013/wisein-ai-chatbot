# Leadership Conversations

## Source: WISEIN-LEADERSHIP-CONVERSATIONS-048.pdf

WISEIN (WISEIN.IN) — LEADERSHIP CONVERSATIONS KNOWLEDGE BASE DATASET 
Document ID: WISEIN-LEADERSHIP-CONVERSATIONS-048 
Document Type: Product / Feature Knowledge Base for AI Chatbot and RAG 
Platform: WiseIN 
Feature: Leadership Conversations 
 
1. DOCUMENT PURPOSE 
This document defines how the WiseIN AI chatbot should understand and answer 
questions about Leadership Conversations. 
WiseIN's core product is a verified professional network designed around real, face-to-
face professional conversations rather than cold direct messaging. The official website 
specifically describes connecting with founders, developers, creators, and other verified 
professionals and scheduling video calls with them.  
The supplied WiseIN profile screenshot also shows a Sessions → Schedule a 
Conversation interface containing different conversation offerings, including founder-
focused, career-focused, discovery, and general conversation sessions. 
However, during current official-site research, no separate public WiseIN page or official 
documentation specifically titled “Leadership Conversations” was found. 
Therefore, this document deliberately distinguishes: 
1. Verified WiseIN conversation functionality  
2. Leadership-focused conversation use cases  
3. UI observations from the supplied screenshot  
4. Information that must be obtained from live WiseIN session data  
This prevents the RAG chatbot from turning an assumed feature into an unsupported 
product fact. 
 
2. WHAT ARE LEADERSHIP CONVERSATIONS? 
A Leadership Conversation can be understood as a professional one-to-one or small-
group conversation focused on leadership, management, decision-making, professional 
growth, organizational challenges, or leadership experience. 

Typical discussion areas may include: 
• 
Leadership experience  
• 
Managing teams  
• 
Decision-making  
• 
Communication  
• 
Career growth  
• 
Building organizations  
• 
Managing challenges  
• 
Professional development  
• 
Entrepreneurship  
• 
Company culture  
• 
Strategy  
• 
Lessons learned from leadership  
These are potential conversation topics, not a guaranteed WiseIN agenda. 
The chatbot should not state that every Leadership Conversation covers all of these 
subjects unless the specific session description confirms them. 
 
3. IMPORTANT PRODUCT STATUS 
What is officially verified 
WiseIN officially supports: 
• 
Verified professional profiles  
• 
Video-first professional conversations  
• 
Scheduled video calls  
• 
Profile availability/slot booking  
• 
Professional networking  
• 
AI meeting summaries  

• 
Events and conversations.  
What is not currently publicly verified 
The current official WiseIN website does not provide a dedicated public specification for a 
feature called: 
“Leadership Conversations.” 
No public source found during this research establishes: 
• 
a dedicated Leadership Conversations page  
• 
a universal Leadership Conversation format  
• 
a standard duration  
• 
a universal price  
• 
mandatory approval  
• 
a specific eligibility requirement  
• 
a dedicated Leadership Conversations category  
• 
a standard participant limit  
• 
a dedicated Leadership Conversations API  
Therefore, these details must not be invented. 
 
4. WISEIN'S CONVERSATION-FIRST MODEL 
Leadership Conversations fit naturally within WiseIN's broader conversation model. 
WiseIN describes itself as: 
“The Individual network where every member is verified.” 
Its homepage promotes connecting face-to-face with founders, developers, and creators 
who are verified. It describes the workflow as discovering the right person and scheduling a 
video call.  
WiseIN's app documentation similarly lists: 
• 
Book and join video calls  
• 
Manage availability and slot bookings  

• 
Discover verified professionals  
• 
Read AI meeting summaries  
• 
Chat with conversations  
• 
Join events and audio rooms.  
Therefore, a Leadership Conversation should be represented in the chatbot as a 
professional conversation/session, unless live WiseIN data identifies it as an event or 
another feature. 
 
5. LEADERSHIP CONVERSATIONS AND SESSIONS 
The supplied WiseIN profile screenshot provides important UI context. 
The profile contains tabs including: 
• 
About  
• 
Sessions  
• 
Webinars  
• 
Posts  
• 
Clips  
• 
Slots  
Under Sessions, the interface displays: 
Schedule a Conversation 
The screenshot shows several conversation offerings. 
Examples include: 
Career Discussion with Santhosh... 
“Looking for a Job? Let's Talk” 
Discovery Call with Santhosh... 
“Open Conversation on How Companies Work & Grow” 
Founder Connect: Let's Talk 
“Open conversation on building, ideas, and challenges” 

Let's Connect & Have a Conversation 
“1:1 General Conversation to exchange ideas” 
The displayed cards show: 
Video meeting · 30 mins 
and: 
Complimentary 
These are observations from the supplied WiseIN UI screenshot. 
 
6. LEADERSHIP CONVERSATION AS A SESSION TYPE 
If the WiseIN application contains a session titled something such as: 
Leadership Conversation 
or 
Leadership Discussion 
the chatbot should treat it as an individual session when the live session metadata 
identifies it as such. 
Conceptually: 
Profile → Sessions → Schedule a Conversation → Leadership Conversation → Booking → 
Video Meeting 
The exact UI workflow must come from the current application. 
The chatbot must not assume that every profile has a Leadership Conversation session. 
 
7. POSSIBLE LEADERSHIP CONVERSATION PURPOSES 
A Leadership Conversation may be useful for discussing: 
Leadership experience 
A participant may want to learn about another professional's leadership experience. 
Team management 

Possible discussion topics include managing teams, delegation, communication, and 
collaboration. 
Career development 
A user may seek guidance about progressing toward leadership responsibilities. 
Decision-making 
A conversation may involve lessons learned from difficult professional decisions. 
Entrepreneurship 
Founder or organizational leaders may discuss building products, companies, teams, or 
professional communities. 
Organizational challenges 
Participants may discuss practical challenges involved in leading teams or organizations. 
Professional networking 
The conversation may simply provide an opportunity to connect with an experienced 
professional. 
These should be treated as use-case examples, not promises about what a specific 
WiseIN session covers. 
 
8. LEADERSHIP CONVERSATIONS AND FOUNDERS 
Leadership and Founder Conversations can overlap, but they are not necessarily the same 
feature. 
Founder Conversation 
Usually centers around: 
• 
Building a company  
• 
Entrepreneurship  
• 
Product/business ideas  
• 
Founder experience  
• 
Startup challenges  

Leadership Conversation 
Can have a broader scope: 
• 
Leading teams  
• 
Management  
• 
Decision-making  
• 
Career leadership  
• 
Organizational culture  
• 
Professional growth  
• 
Business leadership  
A founder can host a Leadership Conversation, but the chatbot should not assume that 
every founder session is a Leadership Conversation. 
 
9. LEADERSHIP CONVERSATIONS AND CAREER DISCUSSIONS 
The supplied screenshot also shows a: 
Career Discussion with Santhosh 
described as: 
“Looking for a Job? Let's Talk” 
This demonstrates that WiseIN's Sessions system can support career-oriented 
conversations. 
However: 
Leadership Conversation ≠ Career Discussion 
A Leadership Conversation may discuss career development, but it should not 
automatically be classified as a job-related session. 
Likewise, a Leadership Conversation does not guarantee: 
• 
employment  
• 
an interview  
• 
a referral  

• 
a promotion  
• 
mentorship  
• 
recruitment  
unless the specific session description states so. 
 
10. LEADERSHIP CONVERSATIONS AND JOBS 
Leadership Conversations are not job listings. 
This distinction is especially important for the chatbot because WiseIN separately provides 
job and internship functionality. 
WiseIN's current plans include access to Jobs & Opportunities, while the Organization 
offering includes job and internship publishing and hiring/recruitment tools.  
Therefore: 
A Leadership Conversation should not be interpreted as a job opportunity simply because 
the discussion may involve careers, hiring, or leadership roles. 
Example 
If a user asks: 
“Is this Leadership Conversation a job interview?” 
The chatbot should answer: 
“Not necessarily. A Leadership Conversation is a professional conversation/session. It 
should only be treated as an interview or recruitment activity if the specific session 
information explicitly identifies it that way.” 
 
11. VIDEO MEETING FORMAT 
WiseIN's public product information confirms that the platform uses video-first 
conversations. 
The homepage describes users booking video calls and talking face-to-face.  
The app page also explicitly lists: 
Book and join video calls on the go.  

The supplied Sessions screenshot displays the conversation offerings as: 
Video meeting · 30 mins 
Therefore, when a Leadership Conversation appears in the Sessions interface as a video 
meeting, the chatbot can explain it as a scheduled video conversation. 
 
12. SESSION DURATION 
The supplied screenshot shows the displayed conversation offerings as: 
30 mins 
However, this should not become a universal rule. 
Do not store the following as a factual product rule: 
“Every Leadership Conversation lasts 30 minutes.” 
Instead: 
“The supplied WiseIN Sessions interface shows the displayed conversation sessions as 30-
minute video meetings. The duration of a particular Leadership Conversation should be 
taken from its current session listing.” 
This is important because individual session creators may potentially configure different 
offerings. 
 
13. COMPLIMENTARY SESSIONS 
The supplied screenshot shows the displayed sessions as: 
Complimentary 
This means those particular displayed sessions were offered without a listed session 
charge at the time of the screenshot. 
The chatbot must not infer: 
“All Leadership Conversations are free.” 
WiseIN's pricing model includes different levels of access to conversations. 
The current India-facing homepage lists 3 conversations per month on Basic and 
unlimited meaningful conversations on Premium, while the global pricing page describes 

Basic as including 3 video calls per month and Premium as including unlimited video calls 
with AI summaries.  
Therefore, account plan and current session data should determine actual eligibility. 
 
14. SMART SLOT BOOKING 
WiseIN publicly promotes scheduling and availability management. 
The homepage describes: 
“Schedule a call in 2 taps” 
and the Premium plan includes: 
Smart Slot booking.  
The app page also states that users can: 
Manage your availability and slot bookings.  
Therefore, Leadership Conversations may be scheduled through WiseIN's broader 
session/slot infrastructure when the relevant session supports booking. 
Do not invent a specific booking workflow if the current UI differs. 
 
15. LEADERSHIP CONVERSATIONS AND PROFILE SLOTS 
The supplied profile screenshot contains a separate: 
Slots 
tab. 
This should be distinguished from: 
Sessions 
Sessions 
Represents conversation offerings that can be scheduled. 
Slots 
Represents availability/scheduling information. 

A Leadership Conversation may depend on available slots, but the exact relationship 
should be obtained from the current application/API. 
 
16. LEADERSHIP CONVERSATIONS AND VERIFIED PROFILES 
Trust is central to WiseIN. 
The homepage says that members are verified and describes government-verified 
professional identities.  
WiseIN's public Terms also state that conversations are based on verified profiles and that 
users are expected to interact professionally and respectfully.  
Therefore, the chatbot can explain: 
“WiseIN is designed around verified professional profiles, so Leadership Conversations 
take place within the platform's verified networking environment.” 
But the chatbot should not claim a particular person's current verification status unless live 
profile data confirms it. 
 
17. LEADERSHIP CONVERSATIONS AND MEETING INTELLIGENCE 
WiseIN promotes AI-powered meeting intelligence. 
The official homepage says that after a call, AI can produce: 
• 
Meeting summary  
• 
Key points  
• 
Follow-ups  
• 
Action items.  
The app page similarly says users can read AI meeting summaries after calls.  
Therefore, where the user's account and plan support the functionality, a Leadership 
Conversation may be followed by AI meeting intelligence. 
Do not claim that every Leadership Conversation necessarily produces an AI summary 
unless the current account/session configuration confirms it. 
 

18. PRIVACY OF LEADERSHIP CONVERSATIONS 
Leadership conversations may involve sensitive professional discussions. 
WiseIN's Content Policies state that: 
• 
Video calls are private.  
• 
Recordings, transcripts, and AI summaries should not be shared publicly without 
explicit permission.  
• 
Private conversations should not be posted publicly without consent.  
• 
Sensitive information should not be publicly shared.  
This is particularly important for leadership-related discussions because they could 
involve: 
• 
Internal company matters  
• 
Team information  
• 
Business strategies  
• 
Financial information  
• 
Employee information  
• 
Confidential decisions  
The chatbot should encourage users to keep confidential information private. 
 
19. RECORDING CONSENT 
WiseIN's Content Policies explicitly state: 
If a call is being recorded, both people must know. 
Secret recording is prohibited.  
Golden chatbot answer 
If the user asks: 
“Can I record a Leadership Conversation?” 
Answer: 

“If a WiseIN call is being recorded, both participants must know. WiseIN's Content Policies 
prohibit secretly recording someone. Recordings, transcripts, and AI summaries should 
also not be shared without the other participant's permission.”  
 
20. AI SUMMARY PRIVACY 
WiseIN describes AI meeting summaries as part of its meeting intelligence. 
However, the Content Policies explicitly state that AI summaries are personal and should 
not be publicly shared without the other participant's consent.  
Therefore: 
AI-generated summary ≠ public content 
A Leadership Conversation summary should not automatically be: 
• 
posted to the feed  
• 
shared with other users  
• 
sent to an organization  
• 
published as a post  
unless the appropriate participant permissions exist. 
 
21. PROFESSIONAL CONDUCT 
Leadership Conversations should follow WiseIN's professional conduct expectations. 
WiseIN states that conversations should be professional and respectful, and inappropriate 
behavior can result in account action.  
The chatbot should recognize the following as inappropriate uses: 
• 
Harassment  
• 
Threats  
• 
Fraud  
• 
Impersonation  
• 
Misrepresentation  

• 
Scams  
• 
Abusive behavior  
• 
Unauthorized recording  
• 
Unauthorized disclosure of confidential information  
 
22. NO GUARANTEE OF MENTORSHIP 
A Leadership Conversation should not automatically be represented as: 
Mentorship 
unless the specific session is explicitly described as a mentor/mentee session. 
For example: 
“Can I get a mentor through Leadership Conversations?” 
Safe answer: 
“A Leadership Conversation can provide an opportunity to speak with an experienced 
professional, but WiseIN does not publicly establish that every Leadership Conversation is 
a formal mentorship arrangement. Check the specific session description for its stated 
purpose.” 
 
23. NO GUARANTEE OF CAREER OUTCOME 
Leadership Conversations can potentially support professional learning and networking, 
but the chatbot must not promise: 
• 
promotion  
• 
employment  
• 
salary increase  
• 
referral  
• 
placement  
• 
internship  
• 
funding  

• 
investment  
• 
business partnership  
unless the specific session or event explicitly states such an outcome. 
 
24. LEADERSHIP CONVERSATIONS AND ORGANIZATIONS 
WiseIN also provides Organization functionality. 
The official Organization pages describe: 
• 
Verified organizations  
• 
Employee profiles  
• 
Employee directory  
• 
Meetings  
• 
Hiring and recruitment  
• 
Organization analytics  
• 
Collaboration.  
This creates potential overlap between Leadership Conversations and organizational 
networking. 
For example, a Leadership Conversation could conceptually involve: 
• 
Company leaders  
• 
Founders  
• 
Managers  
• 
Product leaders  
• 
Organization representatives  
However, the chatbot should not claim that Leadership Conversations are an Organization-
only feature. 
 
25. LEADERSHIP CONVERSATIONS AND ORGANIZATION MEETINGS 
WiseIN's Organization platform supports: 

Instant Meeting Booking 
and describes the ability to book: 
1:1 or group meetings instantly, with calendar synchronization.  
This is related to, but not necessarily identical to, Leadership Conversations. 
The chatbot should distinguish: 
Leadership Conversation 
→ conversation/session purpose 
Organization Meeting 
→ organization-related meeting capability 
Profile Session 
→ individual conversation offering 
Event 
→ event-level activity 
 
26. LEADERSHIP CONVERSATIONS VS FOUNDER CONVERSATIONS 
These features may overlap conceptually. 
Founder Conversations 
Focus may include: 
• 
Founders  
• 
Startups  
• 
Building companies  
• 
Entrepreneurship  
• 
Product/business challenges  
Leadership Conversations 
Focus may include: 
• 
Leadership  

• 
Management  
• 
Decision-making  
• 
Team building  
• 
Career growth  
• 
Organizational challenges  
A founder can participate in both. 
The chatbot must use the specific session/event metadata to determine the actual 
category. 
 
27. LEADERSHIP CONVERSATIONS VS EVENTS 
A Leadership Conversation may be an individual session, while an event is a larger 
scheduled activity. 
WiseIN publicly supports events and conversations as separate parts of its ecosystem. Its 
homepage and app describe events alongside video conversations and audio rooms.  
The public WiseIn Founder Conversations page is an example of an event-level experience 
with: 
• 
Event title  
• 
Online format  
• 
Date range  
• 
Approval-based conversations  
• 
Subscribe  
• 
Calendar.  
Therefore, if WiseIN later exposes a Leadership Conversations Event, it should be 
represented as an event rather than automatically as an individual session. 
 
28. LEADERSHIP CONVERSATIONS AND PUBLIC EVENTS 
WiseIN Basic currently includes access to public events, while the India-facing homepage 
includes Attend public events.  

However, the chatbot should verify the current event status before telling a user: 
• 
an event is active  
• 
registration is open  
• 
attendance is available  
• 
a specific leader will participate.  
 
29. DISCOVERY OF LEADERS 
WiseIN's official product description says users can: 
Discover the right people 
and explore verified individuals by: 
• 
Skill  
• 
Industry  
• 
Experience.  
This discovery model can support finding professionals with leadership experience. 
However, the chatbot should not claim that WiseIN currently has a dedicated Leadership 
search filter unless the live application/API exposes one. 
 
30. CURRENT AVAILABILITY MUST COME FROM LIVE DATA 
The RAG chatbot can explain what Leadership Conversations are. 
It cannot determine from static documentation: 
• 
Which leaders currently offer conversations  
• 
Which Leadership Conversations are open  
• 
Available dates  
• 
Available times  
• 
Current session prices  
• 
Whether a session is complimentary  

• 
Current booking capacity  
• 
Approval status  
• 
Cancellation status  
• 
Meeting links  
• 
Whether the conversation is currently active  
Those should come from authorized WiseIN APIs. 
 
31. RECOMMENDED LIVE DATA 
If WiseIN provides appropriate APIs, the chatbot should retrieve fields such as: 
conversation_id 
session_id 
title 
description 
host_id 
host_name 
host_role 
category 
conversation_type 
duration 
price 
currency 
availability 
date 
start_time 
end_time 
approval_required 

approval_status 
booking_status 
meeting_type 
meeting_link 
created_at 
updated_at 
Only fields actually exposed by WiseIN should be implemented. 
 
32. RECOMMENDED ARCHITECTURE 
The chatbot architecture should be: 
Chat UI 
→ Backend Chat API 
→ Authentication 
→ Intent Detection 
→ RAG Knowledge Base 
→ Authorized WiseIN APIs 
→ LLM 
RAG should handle 
• 
Leadership Conversation definition  
• 
Conversation concepts  
• 
WiseIN networking model  
• 
Privacy  
• 
Recording rules  
• 
Professional conduct  
• 
General booking concepts  
• 
Relationship with Sessions  

• 
Relationship with Founder Conversations  
• 
Relationship with Jobs and Events  
Live APIs should handle 
• 
Current leadership sessions  
• 
Host details  
• 
Current availability  
• 
Current prices  
• 
Current bookings  
• 
Current approvals  
• 
Current meeting links  
• 
User-specific eligibility.  
 
33. SECURITY REQUIREMENTS 
The chatbot must never expose another person's private: 
• 
Availability  
• 
Meeting link  
• 
Booking  
• 
Conversation history  
• 
Transcript  
• 
AI summary  
• 
Recording  
• 
Email  
• 
Phone number  
• 
Personal information  
unless the authenticated WiseIN authorization system explicitly allows it. 
The LLM should not have unrestricted database access. 

Use controlled backend tools such as: 
get_public_sessions() 
get_session_details() 
get_available_slots() 
get_my_bookings() 
get_my_meeting_details() 
get_my_approval_status() 
These are architecture examples only, not confirmed WiseIN API endpoint names. 
 
34. RAG VS LIVE API RULE 
This is one of the most important parts of the document. 
RAG can answer: 
“What is a Leadership Conversation?” 
“What is WiseIN's conversation model?” 
“Can WiseIN conversations be video meetings?” 
“What are the privacy rules?” 
“Can calls be recorded?” 
“What is the difference between Sessions and Events?” 
Live API should answer: 
“Who is available for a Leadership Conversation today?” 
“What Leadership Conversations are available?” 
“What times are available?” 
“How much does this session cost?” 
“Did my booking succeed?” 
“What is my meeting link?” 
“Has my request been approved?” 

This separation prevents stale RAG information from being presented as live information. 
 
35. AI INTENTS 
Recommended chatbot intents: 
leadership_conversations_overview 
leadership_conversation_definition 
leadership_session 
leadership_booking 
leadership_availability 
leadership_duration 
leadership_price 
leadership_host 
leadership_event 
leadership_approval 
leadership_eligibility 
leadership_video_meeting 
leadership_slot_booking 
leadership_privacy 
leadership_recording 
leadership_ai_summary 
leadership_reschedule 
leadership_cancel 
leadership_meeting_link 
leadership_vs_founder 
leadership_vs_job 
leadership_vs_event 

leadership_vs_mentorship 
leadership_support 
 
36. IMPORTANT ENTITIES 
The chatbot should recognize: 
• 
Leadership Conversation  
• 
Leadership Session  
• 
Leader  
• 
Founder  
• 
Executive  
• 
Manager  
• 
Professional  
• 
Host  
• 
Participant  
• 
Session  
• 
Video Meeting  
• 
Slot  
• 
Availability  
• 
Booking  
• 
Event  
• 
Approval  
• 
Meeting  
• 
AI Summary  
• 
Transcript  
• 
Recording  
• 
Career  

• 
Management  
• 
Team  
• 
Organization  
• 
Leadership Development  
• 
Networking  
 
37. RAG METADATA 
Recommended metadata: 
document_id: WISEIN-LEADERSHIP-CONVERSATIONS-001 
feature: Leadership Conversations 
category: Conversations / Sessions / Professional Networking 
platform: WiseIN 
content_type: Product Knowledge Base 
source_priority: Official Website + Current UI Observation 
requires_live_data: true 
transactional_feature: true 
booking_related: true 
privacy_sensitive: true 
event_related: potentially 
last_verified: 2026-09 
 
38. GOLDEN CHATBOT ANSWERS 
Q: What are Leadership Conversations? 
“Leadership Conversations are professional conversations focused on topics such as 
leadership, management, professional growth, decision-making, and organizational 
experience. WiseIN supports video-first professional conversations and scheduled 

sessions. I would use the current session information to confirm the exact purpose of a 
particular Leadership Conversation.” 
 
Q: Does WiseIN have Leadership Conversations? 
“WiseIN publicly documents video-first professional conversations and scheduled 
sessions, but I couldn't find a dedicated public WiseIN page specifically defining a feature 
named ‘Leadership Conversations.’ If your WiseIN application shows a Leadership 
Conversation session, its exact details should be taken from the current session data.” 
This is the preferred answer because it does not turn an unverified feature name into a 
confirmed public product specification. 
 
Q: Can I talk to a leader on WiseIN? 
“WiseIN is designed to help users discover verified professionals and schedule face-to-
face video conversations. If a leader has published a relevant conversation session, you 
can use the current session listing to check its availability and booking details.”  
 
Q: Are Leadership Conversations video calls? 
“WiseIN supports video-first conversations and scheduled video calls. If the Leadership 
Conversation is listed as a video session, it can be booked as a video meeting.”  
 
Q: How long is a Leadership Conversation? 
“The supplied WiseIN Sessions interface shows the displayed conversation offerings as 30-
minute video meetings. That does not establish a universal duration for every Leadership 
Conversation, so the specific session listing should be checked.” 
 
Q: Are Leadership Conversations free? 
“Some conversation sessions shown in the supplied WiseIN interface are marked 
‘Complimentary,’ but that does not establish that every Leadership Conversation is free. 
The current session and your account plan should determine the applicable access and 
pricing.” 

 
Q: Is a Leadership Conversation a job interview? 
“Not automatically. A Leadership Conversation is a professional conversation/session. It 
should only be treated as a recruitment interview if the specific session information says 
that it is.” 
 
Q: Is it mentorship? 
“Not automatically. A Leadership Conversation may provide professional guidance or 
networking, but it should only be described as formal mentorship when the specific WiseIN 
session is explicitly presented as a mentorship offering.” 
 
Q: Can I record a Leadership Conversation? 
“If a WiseIN call is recorded, both participants must know. WiseIN's Content Policies 
prohibit secretly recording calls, and recordings, transcripts, or AI summaries should not 
be shared without the other participant's permission.”  
 
Q: Does WiseIN create an AI summary? 
“WiseIN provides AI meeting intelligence that can generate meeting summaries, key points, 
follow-ups, and action items. Availability can depend on the applicable WiseIN experience 
or plan.”  
 
39. TROUBLESHOOTING 
Leadership Conversation is not visible 
Possible reasons include: 
• 
No current Leadership Conversation has been published.  
• 
The session has ended.  
• 
The host has removed or changed the session.  
• 
The user is not eligible.  

• 
The application failed to load the session.  
• 
The session is restricted.  
The chatbot should check live session data before selecting a specific reason. 
 
Booking is unavailable 
The chatbot should check, where supported: 
1. Whether the session exists.  
2. Whether the session is currently active.  
3. Whether the user is eligible.  
4. Whether the host has available slots.  
5. Whether approval is required.  
6. Whether the user already has a booking.  
 
Meeting link is missing 
The chatbot should verify: 
1. Whether the booking exists.  
2. Whether the user is an authorized participant.  
3. Whether the meeting details have been generated.  
4. Whether the session has started.  
5. Whether WiseIN currently exposes the meeting link.  
Never expose a meeting link belonging to another user. 
 
40. UNSUPPORTED DETAILS — DO NOT INVENT 
The chatbot must not claim without supporting WiseIN documentation or live data: 
• 
Every Leadership Conversation lasts 30 minutes.  
• 
Every Leadership Conversation is complimentary.  

• 
Every leader offers Leadership Conversations.  
• 
Leadership Conversations are a separate official WiseIN product category.  
• 
Leadership Conversations always require approval.  
• 
Leadership Conversations are available to every user.  
• 
Leadership Conversations are only for founders.  
• 
Leadership Conversations are only for executives.  
• 
Leadership Conversations guarantee mentorship.  
• 
Leadership Conversations guarantee career guidance.  
• 
Leadership Conversations guarantee a job.  
• 
Leadership Conversations guarantee referrals.  
• 
Leadership Conversations guarantee investment.  
• 
Leadership Conversations guarantee business partnerships.  
• 
Every Leadership Conversation is recorded.  
• 
Every Leadership Conversation is transcribed.  
• 
Every Leadership Conversation receives an AI summary.  
• 
Leadership Conversations have a fixed participant limit.  
• 
Leadership Conversations have a fixed cancellation policy.  
• 
Leadership Conversations have a fixed approval SLA.  
• 
Leadership Conversations have a dedicated public event page.  
• 
Leadership Conversations are always public.  
 
41. CONTENT SAFETY FOR LEADERSHIP DISCUSSIONS 
Leadership conversations may involve sensitive information. 
WiseIN's Content Policies prohibit publicly sharing: 
• 
Private conversations  
• 
Meeting chats  

• 
Financial data  
• 
ID proofs  
• 
Salary details  
• 
Internal company information  
• 
Business strategies  
• 
Private recordings  
• 
Transcripts  
• 
AI summaries without consent.  
Therefore, the chatbot should never encourage a user to upload or publish confidential 
leadership discussions merely to obtain AI assistance. 
 
42. SOURCE PRIORITY 
For Leadership Conversations, use the following hierarchy: 
Priority 1 — Live WiseIN application/API 
Use for: 
• 
Current sessions  
• 
Current leaders  
• 
Availability  
• 
Prices  
• 
Bookings  
• 
Meeting links  
• 
Approval  
• 
Current event status  
Priority 2 — Official WiseIN website 
Use for: 
• 
Platform capabilities  

• 
Video conversations  
• 
Verified networking  
• 
Slot booking  
• 
AI meeting intelligence  
• 
Pricing  
• 
Policies  
Priority 3 — Current WiseIN UI screenshots 
Use for: 
• 
Sessions layout  
• 
Conversation cards  
• 
Visible labels  
• 
Duration displayed  
• 
Complimentary status displayed  
Priority 4 — Internal WiseIN documentation 
Use when an authoritative internal specification is available. 
Priority 5 — General model knowledge 
Use only for general explanations and never to override WiseIN-specific information. 
 
43. CRITICAL DISTINCTION FOR THE RAG SYSTEM 
The chatbot must distinguish between: 
“Leadership Conversations as a concept” 
and 
“A currently available Leadership Conversation on WiseIN.” 
For example: 
Static/RAG: 
“WiseIN supports scheduled video conversations between verified professionals.” 

Live/API: 
“There is a Leadership Conversation with [host] available tomorrow at [time].” 
The second statement must never be generated from the first. 
 
44. FINAL KNOWLEDGE SUMMARY 
WiseIN is a verified professional networking platform built around authentic, face-to-face 
conversations. Its official website promotes discovering verified professionals and 
scheduling video calls, while its app documentation confirms video calls, availability/slot 
booking, and AI meeting summaries.  
The supplied WiseIN profile screenshot shows that profiles can contain a Sessions section 
where people can publish conversation offerings such as Founder Connect, Discovery 
Calls, Career Discussions, and general one-to-one conversations. The displayed examples 
are presented as video meetings and show 30-minute durations and complimentary labels. 
Leadership Conversations can therefore be represented in the chatbot as a leadership-
focused professional conversation/session when the actual WiseIN application provides 
such a session. 
However, current public WiseIN pages do not provide a dedicated official specification for a 
feature named Leadership Conversations. The chatbot must therefore avoid claiming 
unsupported universal rules about duration, pricing, approval, eligibility, mentorship, or 
availability. 
WiseIN's verified-network model, video-first conversations, smart scheduling, and AI 
meeting intelligence provide the surrounding product context.  
All Leadership Conversations must also follow WiseIN's privacy and meeting-content 
policies. Calls are private, secret recording is prohibited, and recordings, transcripts, and 
AI summaries should not be shared without appropriate consent.  
Core chatbot rule 
RAG explains WiseIN's verified conversation and scheduling model. Live WiseIN data 
determines whether a specific Leadership Conversation exists, who hosts it, its 
purpose, duration, price, availability, approval status, booking status, and meeting 
details. 
 

 



---

