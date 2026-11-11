# Slot Booking

## Source: WISEIN-SLOT-BOOKING-027.pdf

WISEIN — SLOT BOOKING  
Document ID: WISEIN-SLOT-BOOKING-027 
Feature: Slot Booking / Smart Slot Booking 
Platform: WiseIN 
1. SLOT BOOKING OVERVIEW 
Slot Booking is WiseIN's scheduling functionality that allows a user to make available time 
slots for professional conversations or meetings so that another person can select a 
suitable time and book a meeting. 
WiseIN describes this functionality as Smart Slot booking and currently lists it as a 
Premium feature. Its website describes the concept as: 
“Set your availability. Let others book you.” 
WiseIN's official app page also explicitly states that users can: 
• 
Manage their availability  
• 
Manage slot bookings  
• 
Book and join video calls  
• 
Get notified when someone books them.  
WiseIN's website also states that users can schedule a call in two taps and describes the 
platform as being centered around video-first professional conversations.  
 
2. WHAT IS A SLOT? 
A slot is a period of time that a WiseIN user makes available for another person to book for 
a meeting, consultation, networking conversation, or similar professional interaction. 
WiseIN's Terms specifically state that users can share their availability for: 
• 
Meetings  
• 
Consultations  
• 
Networking purposes.  
Therefore, the basic relationship is: 
Availability → Slot → Booking → Scheduled Meeting 

 
3. WHAT IS SLOT BOOKING? 
Slot Booking is the process through which a person selects an available time offered by 
another WiseIN user and books a meeting. 
Conceptually: 
Host/user: makes time available 
Visitor/booker: selects an available time 
WiseIN: creates the scheduled meeting 
Participants: join the meeting at the scheduled time 
WiseIN's official product positioning describes this as: 
“Set your availability. Let others book you. Zero back-and-forth.”  
 
4. SMART SLOT BOOKING 
WiseIN currently uses the term: 
Smart Slot booking 
The current India pricing page lists Smart Slot booking under Premium.  
The current homepage likewise lists Smart Slot booking among Premium features.  
Important chatbot rule 
Do not interpret the word Smart as proof of a particular AI algorithm. 
The public website does not document the internal algorithm used by WiseIN to determine 
or optimize slots. 
Therefore, do not claim that Smart Slot automatically: 
• 
predicts the best meeting time,  
• 
analyzes audience behavior,  
• 
maximizes engagement,  
• 
optimizes conversion,  
• 
uses machine learning to select slots,  

unless internal WiseIN documentation confirms those behaviors. 
 
5. SLOT BOOKING AND VIDEO-FIRST CONVERSATIONS 
Slot Booking is directly connected to WiseIN's video-first approach. 
WiseIN describes its platform as enabling users to: 
“Book a video call in 2 taps.” 
It positions video calls as a way to connect face-to-face rather than relying only on cold text 
messages.  
Therefore, a common WiseIN flow is: 
Discover professional → Open profile → Find session/availability → Select slot → Book → 
Video meeting 
 
6. AVAILABILITY 
Availability is the foundation of Slot Booking. 
A user first makes time available for others to book. 
WiseIN's official app documentation explicitly states: 
“Manage your availability and slot bookings.”  
The official demo page describes Smart scheduling as: 
“Set your availability. Let others book you.”  
 
7. WHY AVAILABILITY MATTERS 
Without available time, another user cannot select a slot. 
Conceptually: 
User makes time available 
        ↓ 
Bookable slot exists 
        ↓ 

Another user selects the slot 
        ↓ 
Booking is created 
        ↓ 
Meeting is scheduled 
The chatbot should explain this relationship when users ask how Slot Booking works. 
 
8. WHO CREATES THE SLOT? 
The user who wants to receive bookings makes their availability available. 
For example: 
Person A 
• 
wants to provide career discussions  
• 
makes certain times available  
• 
another person can select one of those times.  
The exact UI used to create the availability/slot should always be taken from the current 
WiseIN product rather than assumed. 
 
9. WHO BOOKS THE SLOT? 
Another WiseIN user can select an available slot and book it, subject to the current 
account and feature availability. 
WiseIN's official product language specifically describes the model as: 
“Let others book you.”  
 
10. SLOT BOOKING FOR MEETINGS 
WiseIN Terms state that users can share availability for meetings, consultations, or 
networking purposes.  

Therefore, Slot Booking should not be restricted in the chatbot's knowledge to only one 
type of conversation. 
Potential use cases include: 
• 
Professional networking  
• 
Career conversations  
• 
Consultations  
• 
Discovery conversations  
• 
Founder conversations  
• 
Other supported WiseIN sessions.  
The exact types available to a particular account depend on the sessions/booking 
configuration. 
 
11. SLOT BOOKING AND SESSIONS 
The previously supplied WiseIN profile screenshot showed a Sessions section. 
The observed profile included examples such as: 
• 
Career Discussion  
• 
Discovery Call  
• 
Founder Connect  
• 
General Conversation  
The sessions were shown as: 
Video meeting • 30 mins 
and some displayed pricing such as complimentary sessions. 
This demonstrates an important product relationship: 
Profile → Session → Slot/Availability → Booking → Video Meeting 
Important 
The screenshot is evidence of the supplied current UI, but it does not establish that: 
• 
every session is 30 minutes,  

• 
every session is free,  
• 
every user has the same sessions,  
• 
every session uses identical booking rules.  
 
12. SLOT DURATION 
The supplied WiseIN profile screenshot showed several 30-minute sessions. 
The supplied meeting-confirmation screenshot also showed a meeting with: 
Duration: 30 minutes 
Therefore, 30-minute meetings are clearly supported by the observed WiseIN experience. 
However: 
30 minutes should not be treated as a universal Slot Booking duration. 
The actual duration can depend on the particular session or booking configuration. 
Do not tell users: 
“Every WiseIN slot is 30 minutes.” 
unless the live product explicitly establishes that rule. 
 
13. SLOT BOOKING AND MEETING CONFIRMATION 
The previously supplied WiseIN meeting confirmation showed: 
Your Meeting is Confirmed 
and included: 
• 
Meeting participant  
• 
Date  
• 
Time  
• 
Duration  
• 
Joining information.  

The message stated that the user would be able to join directly from WiseIN at the 
scheduled time. 
This provides an example of what happens after a successful booking. 
Conceptual flow 
Available Slot 
      ↓ 
User books slot 
      ↓ 
Booking confirmed 
      ↓ 
Meeting details available 
      ↓ 
Participants join at scheduled time 
 
14. SLOT BOOKING AND CALENDAR 
Slot Booking is closely related to WiseIN's Calendar functionality. 
The Calendar document should be understood as the broader scheduling layer, while Slot 
Booking is the mechanism through which available meeting times are offered and 
selected. 
Relationship 
Availability 
→ defines when the user can meet 
Slot 
→ represents a bookable time 
Booking 
→ reserves that time 
Calendar 

→ represents scheduled activities 
Meeting 
→ takes place at the booked time 
 
15. SLOT BOOKING AND NOTIFICATIONS 
WiseIN's official app page explicitly states: 
“Get notified when someone books you.”  
Therefore, a successful booking can generate relevant notification activity for the person 
whose slot was booked. 
The previously supplied Notifications documentation also establishes meeting-related 
notifications and notification settings. 
Important 
The public documentation does not establish exact: 
• 
notification timing,  
• 
reminder intervals,  
• 
push notification behavior,  
• 
SMS behavior,  
• 
WhatsApp behavior.  
Do not invent these. 
 
16. SLOT BOOKING AND MEETING INVITES 
A booking represents a scheduled interaction between users. 
The chatbot can safely describe the booking result as a scheduled meeting when the 
product confirms the booking. 
However, do not assume that every booking automatically generates: 
• 
a Google Calendar invitation,  
• 
Outlook invitation,  

• 
ICS file,  
• 
external calendar event,  
unless the relevant integration is confirmed. 
 
17. ORGANIZATION SLOT BOOKING 
WiseIN also provides scheduling functionality for Organizations. 
The official organization platform describes: 
Instant Meeting Booking 
and states that organizations can: 
“Book 1:1 or group meetings instantly, synced to your calendar.”  
This means Slot Booking and meeting scheduling are also relevant in the Organization 
environment. 
The organization experience can connect: 
Organization → Employee → Availability → Meeting → Calendar Sync 
 
18. EMPLOYEE AVAILABILITY 
WiseIN's organization platform states that its Employee Directory can filter employees by: 
• 
Role  
• 
Expertise  
• 
Availability  
with verified profiles.  
This makes availability an important part of organizational discovery and meeting booking. 
However, the public documentation does not specify exactly how an organization 
employee configures or exposes availability. 
Do not invent the UI workflow. 
 
19. 1:1 SLOT BOOKING 

A 1:1 booking involves two participants. 
The organization documentation explicitly supports 1:1 meetings.  
A typical individual WiseIN interaction may therefore look like: 
Person A offers availability 
↓ 
Person B selects an available slot 
↓ 
1:1 meeting is booked 
↓ 
Both participants receive relevant meeting information 
↓ 
Meeting takes place 
 
20. GROUP MEETINGS 
WiseIN's organization documentation explicitly mentions: 
“Book 1:1 or group meetings instantly, synced to your calendar.”  
Therefore, group meetings are documented in the Organization context. 
Do not automatically claim that every individual Slot Booking configuration supports group 
bookings unless the individual user's current product UI/API confirms it. 
 
21. SLOT BOOKING AND PREMIUM 
This is one of the most important current product facts. 
WiseIN's current pricing page lists: 
Smart slot booking system 
under Premium.  
The India pricing section on the homepage also lists: 

Smart Slot booking 
under WiseIN Premium.  
Therefore, the current public pricing information supports the statement: 
Smart Slot Booking is a Premium feature for individual users. 
Important distinction 
The Basic plan currently lists: 
• 
Verified Profile Badge  
• 
Discover Verified Individuals  
• 
Join Communities  
• 
Attend public events  
• 
Browse Jobs & Opportunities  
• 
3 conversations per month  
• 
Basic profile analytics  
• 
Limited AI Assistant access.  
Smart Slot booking is listed under Premium rather than Basic.  
 
22. STUDENT PLAN AND SLOT BOOKING 
The current India pricing information lists Student features such as: 
• 
Student verification  
• 
Student badge  
• 
Internship & Job Board  
• 
Campus Communities  
• 
Student Networking Events  
• 
Early access to student opportunities.  
The public page does not explicitly list Smart Slot booking under the Student plan. 

Therefore, the chatbot should not tell a Student-plan user that Smart Slot booking is 
included unless the current product/account configuration confirms it. 
 
23. ORGANIZATION PLAN AND SLOT BOOKING 
The Organization plan includes: 
• 
Everything in Premium  
• 
Organization verification  
• 
Teams  
• 
Hiring tools  
• 
Analytics  
• 
Dedicated support  
• 
Organization badge.  
The Organization product separately documents instant meeting booking and Calendar 
Sync.  
Therefore, organization scheduling should be handled using the Organization-specific 
product documentation when the question concerns company/team meetings. 
 
24. SLOT BOOKING VS CALENDAR 
These features should not be treated as identical. 
Slot Booking 
Answers: 
“When can someone book me?” 
and: 
“Which available time do I want to reserve?” 
Calendar 
Answers: 
“What meetings/events are scheduled?” 

Availability 
Answers: 
“When am I available?” 
Meeting 
Answers: 
“What conversation is taking place at the booked time?” 
 
25. SLOT BOOKING VS SCHEDULED POSTS 
This distinction is critical for the chatbot. 
Slot Booking 
Used to schedule meetings/conversations. 
Scheduled Posts 
Used to schedule content publication. 
For example: 
“I want to schedule something tomorrow.” 
This is ambiguous. 
The chatbot should determine whether the user means: 
• 
Schedule a meeting/slot, or  
• 
Schedule a post.  
 
26. SLOT BOOKING — GENERAL USER FLOW 
A safe conceptual workflow is: 
Step 1 — User offers availability 
The user makes suitable time available. 
Step 2 — Slot becomes bookable 
The available period can be selected by another user. 

Step 3 — Visitor selects a slot 
The visitor chooses a suitable available time. 
Step 4 — Booking is created 
The selected slot becomes a scheduled interaction. 
Step 5 — Meeting details become available 
The participants receive relevant meeting information. 
Step 6 — Meeting takes place 
The participants join through WiseIN at the scheduled time. 
Step 7 — Meeting intelligence 
WiseIN's platform can provide AI meeting summaries after calls where the relevant feature 
is available.  
 
27. SLOT BOOKING — HOST PERSPECTIVE 
The person offering slots should think of the process as: 
My availability 
      ↓ 
Bookable time 
      ↓ 
Someone selects a slot 
      ↓ 
Booking confirmed 
      ↓ 
Scheduled meeting 
      ↓ 
Join meeting 
WiseIN's Smart scheduling description directly supports this model.  

 
28. SLOT BOOKING — BOOKER PERSPECTIVE 
The person booking another user's slot should think of the process as: 
Find verified professional 
        ↓ 
Open profile/session 
        ↓ 
View available time 
        ↓ 
Select suitable slot 
        ↓ 
Book 
        ↓ 
Receive confirmation/details 
        ↓ 
Join at scheduled time 
WiseIN's official website describes discovery of verified professionals followed by 
scheduling a video call.  
 
29. SLOT BOOKING AND VERIFIED PROFILES 
WiseIN positions itself as a verified professional network. 
Its homepage states that every member is verified and describes government-verified 
profiles.  
Therefore, Slot Booking occurs within the context of WiseIN's verified professional network. 
The chatbot should not, however, claim that a booked meeting guarantees: 
• 
professional expertise,  
• 
quality of advice,  

• 
employment,  
• 
business results,  
• 
successful collaboration.  
Verification establishes platform/account verification, not guaranteed outcomes. 
 
30. SLOT BOOKING AND PROFESSIONAL USE CASES 
WiseIN describes professional conversations involving founders, developers, creators, and 
other professionals.  
Slot Booking can therefore support use cases such as: 
Career discussions 
A professional can offer time for career-oriented conversations. 
Networking 
A user can make time available for professional networking. 
Consultations 
WiseIN Terms explicitly mention consultations as a use case for availability slots.  
Discovery conversations 
Users can schedule conversations to explore professional or business opportunities. 
Founder conversations 
Founder-oriented conversations can use scheduled video meetings where supported. 
 
31. SLOT BOOKING RESPONSIBILITIES 
WiseIN's Terms contain an important rule: 
Scheduling is managed by users. 
The Terms state that WiseIN does not guarantee or take responsibility for missed, 
rescheduled, or unfulfilled appointments between users. 
Both parties are responsible for confirming and honoring their scheduled commitments.  
Chatbot rule 

When a user asks about a missed appointment, the chatbot should not imply that WiseIN 
guarantees attendance by either participant. 
 
32. MISSED MEETING 
If someone does not attend a booked meeting, a safe chatbot response is: 
“WiseIN's Terms state that users are responsible for confirming and honoring their 
scheduled commitments, and WiseIN does not guarantee or take responsibility for missed 
or unfulfilled appointments.” 
Do not accuse the other participant of intentionally missing the meeting. 
 
33. RESCHEDULED MEETING 
WiseIN's Terms explicitly mention rescheduled appointments, but do not provide enough 
public detail to document the exact rescheduling workflow. 
Therefore: 
“WiseIN's Terms acknowledge that appointments may be rescheduled, but the exact 
rescheduling controls and workflow are not sufficiently documented in the public product 
documentation.” 
Do not invent a reschedule button or specific rescheduling rules. 
 
34. CANCELLED BOOKING 
The current public documentation does not provide a sufficiently detailed Slot Booking 
cancellation workflow. 
Therefore, the chatbot should not invent: 
• 
cancellation windows,  
• 
cancellation fees,  
• 
refund rules,  
• 
cancellation buttons,  
• 
automatic cancellation notifications.  

If a current product UI/API exposes these features, the internal documentation should be 
added to this knowledge base. 
 
35. SLOT AVAILABILITY 
A slot can only be booked if it is currently available. 
The chatbot should distinguish: 
Available 
The time can be selected. 
Booked 
The time has already been reserved. 
Unavailable 
The user is not offering that time for booking. 
Past 
The time has already passed. 
These are conceptual scheduling states. Exact backend status names should come from 
the WiseIN API if available. 
 
36. LIVE SLOT AVAILABILITY 
Questions such as: 
“What slots does Shivaji have available tomorrow?” 
require live product data. 
RAG documentation cannot determine the person's current availability. 
The chatbot should use: 
Authentication → Authorization → Availability/Slot API → Current slots 
if WiseIN exposes an authorized endpoint. 
Never invent a time slot. 
 

37. RAG VS LIVE SLOT DATA 
RAG should answer: 
• 
What is Slot Booking?  
• 
What is Smart Slot booking?  
• 
How does availability work?  
• 
What is the general booking flow?  
• 
Is Smart Slot booking a Premium feature?  
• 
What are the responsibilities of users?  
• 
What does WiseIN say about missed appointments?  
Live API should answer: 
• 
Which slots are available?  
• 
Who booked my slot?  
• 
Which slots have been booked?  
• 
What is my next meeting?  
• 
What is my current availability?  
• 
Is a slot still available?  
• 
What is the booking status?  
• 
Which meeting belongs to a particular slot?  
This separation is essential for the chatbot. 
 
38. RECOMMENDED CHATBOT ARCHITECTURE 
For: 
“How does Slot Booking work?” 
Use: 
Chat UI 
   ↓ 

Chat API 
   ↓ 
RAG 
   ↓ 
WiseIN Slot Booking Knowledge Base 
   ↓ 
LLM 
   ↓ 
Answer 
For: 
“What slots are available tomorrow?” 
Use: 
Chat UI 
   ↓ 
Chat API 
   ↓ 
Authentication 
   ↓ 
Authorization 
   ↓ 
WiseIN Availability API 
   ↓ 
Current slot data 
   ↓ 
LLM 
   ↓ 

Answer 
The LLM should never guess live availability from static documentation. 
 
39. SLOT BOOKING AND SECURITY 
Slot information can expose private scheduling information. 
The chatbot must enforce authorization before returning: 
• 
another person's private availability,  
• 
private bookings,  
• 
participant information,  
• 
meeting details,  
• 
organization scheduling data.  
For example: 
User: 
“Show me all of my available slots.” 
→ authorized live API. 
User: 
“Show me another user's private calendar.” 
→ only provide information that WiseIN explicitly makes public and that the user is 
authorized to access. 
 
40. SLOT BOOKING AND PRIVACY 
The chatbot should treat booking information as potentially sensitive. 
Do not expose: 
• 
private participant information,  
• 
private meeting details,  
• 
private availability,  
• 
personal contact information,  

without appropriate authorization. 
WiseIN's content/privacy policies also place restrictions on sharing private conversations 
and sensitive information. 
 
41. SLOT BOOKING AND NOTIFICATIONS 
The current official app documentation supports booking notifications: 
“Get notified when someone books you.”  
Therefore: 
Slot booked → relevant booking notification 
is a documented product relationship. 
However, the chatbot should not invent the exact delivery channel or timing. 
 
42. SLOT BOOKING AND AI MEETING SUMMARIES 
WiseIN's homepage states that after a call, AI generates: 
• 
Key points  
• 
Follow-ups  
• 
Action items.  
The pricing page also includes AI meeting summaries and transcription under Premium.  
Therefore, a completed Slot Booking can lead to a video meeting, after which meeting 
intelligence may be available depending on the relevant feature/account. 
Do not claim that every slot automatically produces a transcript or summary. 
 
43. SLOT BOOKING TROUBLESHOOTING 
Problem: I cannot find Slot Booking 
The current public pricing page lists Smart Slot booking as a Premium feature.  
Recommended response: 

“Smart Slot booking is currently listed as a Premium feature. If you are using a plan that 
does not include it, the feature may not be available. If you are already on a supported plan 
and cannot access it, refresh WiseIN and contact support if the issue continues.” 
 
Problem: I cannot create a slot 
Check: 
1. Whether the account has access to Smart Slot booking.  
2. Whether availability configuration is available.  
3. Whether the required fields have been completed.  
4. Whether there is a temporary application/network problem.  
5. Refresh and retry.  
Do not invent exact required fields unless confirmed by the current UI. 
 
Problem: My slot disappeared 
Possible explanations may include: 
• 
another user booked it,  
• 
availability was changed,  
• 
the slot passed,  
• 
the slot was removed.  
These are possible scheduling explanations, not confirmed WiseIN-specific error states. 
If the live API is available, use it to determine the actual status. 
 
Problem: Someone cannot book my slot 
Check: 
• 
whether the slot is still available,  
• 
whether the account supports Slot Booking,  
• 
whether the slot has already been booked,  

• 
whether the booking date/time is valid,  
• 
whether there is a temporary product issue.  
 
44. SLOT BOOKING SUPPORT ESCALATION 
If the problem cannot be resolved, WiseIN's Contact page provides support and states that 
the team aims to respond within 24 hours.  
Useful non-sensitive information for escalation: 
• 
Account email, if WiseIN support requests it  
• 
Problem description  
• 
Approximate date/time  
• 
Slot date/time  
• 
Session name  
• 
Error message  
• 
Screenshot  
• 
Browser/app information  
Never ask users to provide: 
• 
Password  
• 
OTP  
• 
Authentication token  
• 
Session token  
• 
API key  
• 
Payment PIN  
• 
Verification code  
 
45. COMMON CHATBOT QUESTIONS 
Q: What is Slot Booking? 

“Slot Booking lets a WiseIN user make available times bookable so another user can select 
a suitable time for a professional meeting or conversation.” 
 
Q: What is Smart Slot Booking? 
“Smart Slot booking is WiseIN's scheduling feature that lets users set their availability and 
allow others to book available times. WiseIN currently lists Smart Slot booking as a 
Premium feature.” 
 
Q: Is Smart Slot Booking free? 
“WiseIN's current pricing page lists Smart Slot booking under Premium rather than Basic.” 
 
Q: Can people book me? 
“Yes. WiseIN describes Smart scheduling as allowing you to set your availability and let 
others book you.” 
 
Q: What can I use slots for? 
“WiseIN's Terms describe availability slots for meetings, consultations, and networking 
purposes.” 
 
Q: Will I get notified when someone books me? 
“Yes. WiseIN's official app documentation says users can get notified when someone 
books them.” 
 
Q: Are all slots 30 minutes? 
“No universal 30-minute rule should be assumed. The WiseIN UI you provided shows 
several 30-minute sessions, but meeting duration can depend on the specific session or 
booking configuration.” 
 

Q: Can I book someone else's slot? 
“If that person's availability and slot are available for booking, you can select an available 
time and complete the booking through WiseIN.” 
 
Q: What happens after I book a slot? 
“The selected time becomes a scheduled meeting/interaction, and relevant meeting 
details and booking notifications may be provided through WiseIN.” 
 
Q: What happens if someone doesn't attend? 
“WiseIN's Terms state that users are responsible for confirming and honoring their 
scheduled commitments. WiseIN does not guarantee or take responsibility for missed, 
rescheduled, or unfulfilled appointments.” 
 
46. AI CHATBOT INTENTS 
General 
slot_booking 
what_is_slot_booking 
smart_slot_booking 
slot_booking_help 
slot_booking_overview 
Availability 
set_availability 
manage_availability 
my_availability 
available_slots 
create_slot 
edit_availability 

Booking 
book_slot 
book_meeting 
select_slot 
confirm_slot 
booking_confirmation 
booking_status 
Host 
let_others_book_me 
share_availability 
receive_slot_booking 
someone_booked_my_slot 
Meeting 
slot_to_meeting 
meeting_details 
meeting_duration 
join_booked_meeting 
meeting_confirmation 
Plan/access 
slot_booking_plan 
smart_slot_premium 
slot_booking_availability 
subscription_slot_booking 
Troubleshooting 
slot_not_available 
cannot_create_slot 

cannot_book_slot 
slot_disappeared 
booking_failed 
booking_missing 
wrong_booking_time 
Policy 
missed_booking 
missed_meeting 
rescheduled_meeting 
booking_responsibility 
slot_booking_privacy 
 
47. IMPORTANT ENTITIES FOR RAG 
The knowledge base should recognize: 
• 
Slot  
• 
Slot Booking  
• 
Smart Slot Booking  
• 
Availability  
• 
Available Slot  
• 
Booking  
• 
Booked Slot  
• 
Meeting  
• 
Video Meeting  
• 
Session  
• 
Consultation  
• 
Networking  

• 
Participant  
• 
Host  
• 
Booker  
• 
Date  
• 
Time  
• 
Time Zone  
• 
Duration  
• 
Calendar  
• 
Calendar Sync  
• 
Notification  
• 
Premium  
• 
Organization  
• 
Employee  
• 
Group Meeting  
• 
AI Meeting Summary  
 
48. SLOT BOOKING KNOWLEDGE RELATIONSHIPS 
The RAG system should connect this document with: 
Profile 
Profiles expose professional information and may provide sessions/booking opportunities. 
Sessions 
Sessions describe specific conversations that can be booked. 
Calendar 
Calendar organizes scheduled meetings and events. 
Meetings 
A successful booking leads to a scheduled meeting. 

Notifications 
Users can be notified when someone books them. 
Organizations 
Organizations can book 1:1 or group meetings and synchronize them with calendars. 
AI Meeting Intelligence 
After supported meetings, AI can generate summaries and action items. 
Scheduled Posts 
Completely separate scheduling use case for future content publication. 
 
49. UNSUPPORTED DETAILS — DO NOT INVENT 
The following Slot Booking details are not sufficiently documented by current public 
WiseIN sources or the previously supplied screenshots: 
• 
Exact slot creation screen  
• 
Exact slot creation fields  
• 
Exact slot duration options  
• 
Minimum slot duration  
• 
Maximum slot duration  
• 
Maximum slots per day  
• 
Maximum bookings per day  
• 
Maximum number of availability windows  
• 
Recurring availability  
• 
Weekly availability rules  
• 
Buffer time  
• 
Minimum booking notice  
• 
Maximum booking horizon  
• 
Booking cutoff time  

• 
Automatic conflict detection  
• 
Automatic conflict resolution  
• 
Waitlists  
• 
Slot cancellation workflow  
• 
Slot rescheduling workflow  
• 
Booking cancellation window  
• 
Cancellation fees  
• 
Refund rules  
• 
Automatic reminders  
• 
SMS reminders  
• 
WhatsApp reminders  
• 
Google Calendar integration for individual accounts  
• 
Microsoft Outlook integration  
• 
Apple Calendar integration  
• 
ICS export/import  
• 
Exact calendar synchronization frequency  
• 
Exact slot ranking algorithm  
• 
AI algorithm behind “Smart”  
• 
Automatic timezone conversion rules  
• 
Exact booking API endpoints  
• 
Webhook events  
• 
Exact booking status names  
• 
Exact permissions for organization employees  
• 
Automatic recurring bookings.  
Never fabricate these details in chatbot responses. 
 

50. SOURCE PRIORITY 
For Slot Booking questions, use this priority order. 
Priority 1 — Current WiseIN UI 
Use current UI screenshots/product behavior for: 
• 
Slot creation  
• 
Availability controls  
• 
Booking controls  
• 
Session selection  
• 
Date/time controls  
• 
Confirmation  
• 
Cancellation/rescheduling controls.  
Priority 2 — Official WiseIN website 
Use official sources for: 
• 
Smart Slot Booking  
• 
Availability  
• 
Professional meetings  
• 
Video calls  
• 
Pricing  
• 
Notifications  
• 
Organization meeting booking.  
Priority 3 — WiseIN Terms 
Use the Terms for: 
• 
Availability-slot responsibilities  
• 
Missed appointments  
• 
Rescheduling responsibilities  
• 
User obligations.  

Priority 4 — Internal APIs/product documentation 
Use internal documentation for: 
• 
exact backend states,  
• 
limits,  
• 
permissions,  
• 
API behavior,  
• 
calendar integrations,  
• 
booking rules.  
Priority 5 — General assumptions 
Do not use generic Calendly/Google Calendar behavior to fill WiseIN-specific gaps. 
 
51. RAG METADATA 
document_id: WISEIN-SLOT-BOOKING-001 
feature: Slot Booking 
alternate_names: 
  - Smart Slot Booking 
  - Smart Slot booking system 
category: Scheduling & Meetings 
platform: WiseIN 
content_type: Product Knowledge Base 
audience: 
  - Users 
  - Support 
  - AI Chatbot 
source_priority: 
  - Current UI 

  - Official WiseIN Website 
  - WiseIN Terms 
  - Internal Product/API Documentation 
status: Active 
Retrieval tags 
slot 
slot booking 
smart slot 
smart slot booking 
slot booking system 
availability 
available slots 
book slot 
book meeting 
meeting slot 
profile slots 
profile time slots 
video call 
video meeting 
session booking 
consultation 
networking 
smart scheduling 
set availability 
let others book you 
booking confirmation 

meeting confirmation 
calendar 
calendar sync 
notifications 
premium 
organization meeting 
group meeting 
1:1 meeting 
 
52. GOLDEN ANSWERS 
“What is Slot Booking?” 
“Slot Booking is WiseIN's scheduling functionality that lets a user make available times 
bookable so another person can select a suitable time for a meeting, consultation, or 
professional networking conversation.” 
 
“What is Smart Slot Booking?” 
“Smart Slot booking lets you set your availability and allow others to book you. WiseIN 
currently lists Smart Slot booking as a Premium feature.” 
 
“How do I let people book me?” 
“Use WiseIN's availability and Smart Slot booking functionality to make suitable times 
available for others to book.” 
 
“Can slots be used for consultations?” 
“Yes. WiseIN's Terms specifically mention availability slots for meetings, consultations, 
and networking purposes.” 
 

“Will I receive a notification when someone books me?” 
“Yes. WiseIN's official app documentation says users can get notified when someone 
books them.” 
 
“Is Smart Slot Booking included in Premium?” 
“Yes. WiseIN's current pricing page lists Smart Slot booking under Premium.” 
 
“What happens after someone books my slot?” 
“The selected availability becomes a scheduled interaction/meeting. WiseIN provides 
booking and meeting information, and its app documentation states that users can be 
notified when someone books them.” 
 
“Does WiseIN guarantee that the other person will attend?” 
“No. WiseIN's Terms state that users are responsible for confirming and honoring their 
scheduled commitments, and WiseIN does not guarantee or take responsibility for missed, 
rescheduled, or unfulfilled appointments.” 
 
53. FINAL CHATBOT GUARDRAILS 
The WiseIN Slot Booking chatbot must: 
1. Treat Slot Booking and Smart Slot Booking as the scheduling feature.  
2. Explain the relationship between availability → slot → booking → meeting.  
3. Recognize meetings, consultations, and networking as documented availability-slot 
use cases.  
4. Recognize Smart Slot booking as a currently listed Premium feature.  
5. Explain that users can set availability and allow others to book them.  
6. Distinguish Slot Booking from Calendar.  
7. Distinguish Slot Booking from Scheduled Posts.  
8. Distinguish Slots from Sessions.  

9. Use live APIs for questions about actual current availability.  
10. Never fabricate available times.  
11. Never reveal private booking information without authorization.  
12. Never assume all meetings have a fixed duration.  
13. Never invent cancellation or rescheduling rules.  
14. Never invent external calendar integrations.  
15. Never invent notification timing.  
16. Treat organization 1:1/group booking separately from individual-user functionality 
where appropriate.  
17. Explain WiseIN's user responsibility for missed/unfulfilled appointments.  
18. Never request passwords, OTPs, session tokens, API keys, or other secrets.  
19. Treat supplied screenshots as current UI evidence, not permanent API guarantees.  
20. When a product behavior is undocumented, clearly state that it is not currently 
documented instead of guessing.  
 
54. FINAL KNOWLEDGE SUMMARY 
WiseIN Slot Booking is the platform's availability-based scheduling mechanism for 
professional conversations and meetings. WiseIN describes Smart Slot booking as allowing 
users to set their availability and let others book them, and its official app 
documentation confirms that users can manage availability and slot bookings, book and 
join video calls, and receive notifications when someone books them. WiseIN's Terms 
specifically recognize availability slots for meetings, consultations, and networking and 
state that users are responsible for honoring their scheduled commitments. The current 
WiseIN pricing page lists Smart Slot booking as a Premium feature. WiseIN's 
Organization platform separately supports instant 1:1 and group meeting booking with 
calendar synchronization. Exact slot durations, recurring availability, booking limits, 
cancellation/rescheduling workflows, reminders, external calendar integrations, and 
backend status values are not sufficiently documented publicly and should not be invented 
by the AI chatbot.  
 

 



---

