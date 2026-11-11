# Calendar

## Source: WISEIN-CALENDAR-026.pdf

Document ID: WISEIN-CALENDAR-026 
Feature: Calendar 
Platform: WiseIN 
1. CALENDAR OVERVIEW 
WiseIN's Calendar functionality is connected to the platform's video meetings, sessions, 
events, availability, and scheduling features. 
WiseIN positions itself as a video-first professional networking platform where users can 
discover verified professionals and schedule video calls. Its current website describes the 
process as: 
“Schedule a call in 2 taps” 
and its public product information describes Smart Slot booking as a way to set 
availability and allow other people to book meetings.  
For organizations, WiseIN also describes Calendar Sync as part of its integrated 
scheduling and meeting functionality, allowing 1:1 or group meetings to be synced with a 
calendar.  
The Calendar knowledge base should therefore treat Calendar as part of a larger 
scheduling system rather than as an isolated date-viewing feature. 
 
2. CALENDAR — PRIMARY PURPOSE 
The Calendar helps users organize and manage scheduled WiseIN activities such as: 
• 
Video meetings  
• 
Booked conversations  
• 
Sessions  
• 
Events  
• 
Availability-related scheduling  
• 
Organization meetings  
• 
Calendar-synchronized meetings where supported  
The exact items displayed can depend on the user's account, role, feature availability, and 
current WiseIN implementation. 

The chatbot should not assume that every type of WiseIN activity appears in the same 
calendar view unless the current UI/API confirms it. 
 
3. WISEIN'S VIDEO-FIRST SCHEDULING MODEL 
Calendar functionality is closely connected with WiseIN's core video-first experience. 
WiseIN's official homepage explains that users can discover verified people and then meet 
face-to-face through scheduled video calls. It also states that users can schedule a call in 
two taps.  
The official demo page similarly describes: 
• 
Video-first connections  
• 
Booking a video call  
• 
Smart scheduling  
• 
Setting availability  
• 
Allowing others to book the user  
• 
AI meeting intelligence after calls.  
Therefore, the chatbot should understand these concepts as related: 
Profile → Availability/Slots → Booking → Calendar → Video Meeting → AI Meeting 
Summary 
 
4. CALENDAR AND SMART SLOT BOOKING 
WiseIN currently advertises Smart Slot booking. 
The official website describes this as: 
“Set your availability. Let others book you. Zero back-and-forth.” 
The Premium plan also lists Smart Slot booking among its features.  
This means the Calendar and scheduling system can be understood as supporting the 
transition from: 
Available time → Booked slot → Scheduled meeting 

The chatbot should distinguish: 
Availability 
Times when the user is willing to receive bookings. 
Slot 
A bookable time period made available for a conversation/meeting. 
Booking 
A person selecting an available time. 
Calendar event/meeting 
The resulting scheduled activity. 
 
5. CALENDAR AND USER AVAILABILITY 
WiseIN's official app documentation states that users can: 
“Manage your availability and slot bookings” 
through the app.  
Therefore, Calendar-related questions may involve availability. 
For example: 
User: 
“How do I let people book me?” 
Chatbot: 
“WiseIN provides availability and Smart Slot booking functionality. Set your available times 
so other users can book a video conversation with you.” 
Do not invent exact availability settings such as: 
• 
working hours,  
• 
recurring weekly schedules,  
• 
buffer time,  
• 
minimum notice,  
• 
maximum bookings per day,  

unless those values are confirmed by the actual UI or backend documentation. 
 
6. CALENDAR AND VIDEO MEETINGS 
WiseIN's primary scheduling use case is video meetings. 
The official website states that users can book video calls and meet face-to-face.  
The mobile-app documentation also states that users can: 
• 
Book video calls  
• 
Join video calls  
• 
Manage availability  
• 
Manage slot bookings.  
Therefore, a calendar entry may represent a scheduled conversation that can subsequently 
be joined through WiseIN. 
 
7. MEETING CONFIRMATION 
A previously supplied WiseIN meeting-confirmation screenshot provides an important 
example of how a scheduled meeting is communicated. 
The confirmation email shown in the supplied UI contained: 
“Your Meeting is Confirmed” 
and included: 
• 
Meeting participants  
• 
Date  
• 
Time  
• 
Duration  
• 
Information that the meeting can be joined directly from WiseIN at the scheduled 
time.  
The supplied example showed: 

Date: Wednesday, September 2, 2026 at 05:30 AM 
Duration: 30 minutes 
These values are an example from the supplied screenshot and must not be treated as 
fixed meeting defaults. 
Knowledge-base rule 
The chatbot may explain that meeting confirmations can contain: 
• 
Meeting participant  
• 
Date  
• 
Time  
• 
Duration  
• 
Join information  
but should not claim that every WiseIN meeting has a fixed 30-minute duration. 
 
8. CALENDAR AND MEETING DURATION 
The supplied meeting confirmation demonstrated a 30-minute meeting. 
Previously supplied WiseIN profile screenshots also showed several Sessions with: 
Video meeting • 30 mins 
This establishes that 30-minute sessions are used in the observed WiseIN product. 
However, this does not prove that all WiseIN meetings are 30 minutes. 
Therefore: 
“WiseIN supports 30-minute sessions/meetings, as shown in the supplied product UI, but 
the duration of a particular meeting depends on the session or booking configuration.” 
Do not hard-code 30 minutes as the universal meeting duration. 
 
9. CALENDAR AND SESSIONS 
The previously supplied WiseIN profile screenshot showed a Sessions section. 
Example sessions included: 

• 
Career Discussion  
• 
Discovery Call  
• 
Founder Connect  
• 
General Conversation  
The displayed sessions were video meetings with stated durations and pricing information. 
This establishes an important relationship: 
Profile → Sessions → Booking → Scheduled Meeting → Calendar 
The chatbot should not automatically describe every Session as a Calendar event unless 
the actual calendar implementation confirms that behavior. 
 
10. CALENDAR AND EVENTS 
WiseIN also has an Events feature. 
The official website currently includes: 
• 
Public events  
• 
Student Networking Events  
• 
Communities  
• 
Audio rooms  
• 
Organization webinars.  
A publicly indexed WiseIN event page provides an example of an event interface containing: 
• 
Event title  
• 
Organizer  
• 
Online format  
• 
Event date range  
• 
Subscribe  
• 
Events  
• 
Calendar  

The indexed example is WiseIn Founder Conversations, shown as an online event running 
from January to June 2026.  
Important date rule 
That particular event is historical relative to the current date and should not be presented 
to users as a current or upcoming event. 
The page is useful as evidence of WiseIN's event/calendar interface structure. 
 
11. EVENT CALENDAR 
The public event example demonstrates a calendar associated with event activity. 
The page displays: 
Events 
and: 
Calendar 
along with a calendar-style date interface.  
The chatbot can therefore explain: 
“WiseIN provides calendar functionality associated with its event experience.” 
However, do not claim that the public event calendar and a user's personal meeting 
calendar are necessarily the same calendar system. 
They should be treated as separate contexts unless the product/API confirms integration. 
 
12. CALENDAR AND ORGANIZATIONS 
WiseIN's organization documentation provides stronger evidence of calendar integration. 
The official WiseIN organization page describes: 
Calendar Sync 
under its integrated scheduling and meetings functionality. 
It states that organizations can: 
• 
Book 1:1 meetings  

• 
Book group meetings  
• 
Sync meetings to a calendar  
• 
Use WiseIN without relying on external meeting tools for the WiseIN meeting 
workflow.  
This is particularly relevant for organization users. 
Chatbot answer 
User: 
“Does WiseIN support calendar synchronization for organizations?” 
Answer: 
“Yes. WiseIN's organization documentation describes Calendar Sync for integrated 
scheduling and meetings, including 1:1 and group meetings.” 
 
13. CALENDAR AND ORGANIZATION MEETINGS 
The organization platform currently describes: 
• 
Employees  
• 
Meetings  
• 
Analytics  
as part of the organization dashboard.  
It also describes integrated scheduling and calendar synchronization. 
Therefore, organization Calendar knowledge should be connected to: 
Organization → Employees → Meeting booking → Calendar Sync → Meeting → Analytics 
Do not assume that every individual-user calendar capability is available to organization 
accounts. 
 
14. CALENDAR AND GROUP MEETINGS 
The official organization documentation explicitly mentions: 
“Book 1:1 or group meetings instantly, synced to your calendar.” 

Therefore, the chatbot can safely state that WiseIN's organization functionality supports 
1:1 and group meetings with calendar synchronization. 
For ordinary individual accounts, do not automatically claim group-meeting functionality 
unless the current account/UI confirms it. 
 
15. CALENDAR AND AI MEETING INTELLIGENCE 
Calendar scheduling is connected to WiseIN's AI meeting functionality. 
WiseIN states that after calls, AI can produce meeting intelligence including: 
• 
Summary  
• 
Key points  
• 
Follow-ups  
• 
Action items  
The homepage describes AI meeting summaries, while the Premium plan includes AI 
meeting summaries and transcription.  
The relationship can be represented conceptually as: 
Calendar/Booking → Video Meeting → Meeting Intelligence → Summary/Action Items 
The chatbot should not claim that a meeting summary is created before a meeting takes 
place. 
 
16. CALENDAR AND NOTIFICATIONS 
WiseIN's app documentation states: 
“Get notified when someone books you.” 
Therefore, Calendar/booking activity can be related to notifications. 
The previously supplied WiseIN Notifications screenshots also showed a notification 
settings area describing updates related to: 
• 
Messages  
• 
Meeting invites  

• 
Community activity  
• 
Important announcements.  
Important 
Do not invent exact notification timing. 
For example, do not state: 
“WiseIN always sends a reminder 15 minutes before every meeting” 
unless the current product/API explicitly confirms this. 
 
17. CALENDAR AND MEETING INVITATIONS 
Meeting-related calendar activity may originate from a booking or invitation. 
The previously supplied UI/documentation establishes meeting confirmations and 
meeting-related notifications. 
A safe chatbot answer is: 
“When a WiseIN meeting is booked or confirmed, relevant meeting information can include 
the participants, date, time, duration, and joining information.” 
Do not claim support for: 
• 
automatic email invitations to every attendee,  
• 
Google Calendar invitations,  
• 
Outlook invitations,  
• 
ICS attachments,  
unless the relevant integration is confirmed. 
 
18. CALENDAR TIME AND TIME ZONE 
Time-zone handling is important for scheduled activities. 
The previously supplied Scheduled Post UI explicitly showed a Time Zone selector, 
demonstrating that WiseIN uses timezone-aware scheduling in at least that scheduling 
workflow. 

For meetings, the chatbot should not automatically assume that the same exact timezone 
implementation is used unless the meeting/calendar UI confirms it. 
Recommended response 
“For a scheduled WiseIN activity, always verify the displayed date, time, and time-zone 
information before confirming the booking.” 
 
19. CALENDAR AND SCHEDULED POSTS 
Scheduled Posts are a separate feature from the meeting calendar. 
The previously supplied Scheduled Posts documentation establishes: 
Settings → Scheduled post 
with a scheduling screen containing: 
• 
Date  
• 
Time  
• 
Time Zone  
• 
Preview Post  
• 
Schedule Post.  
Therefore: 
Scheduled Posts 
Used for future content publication. 
Calendar/Meeting scheduling 
Used for meetings, sessions, events, and availability-based bookings. 
Do not merge these features into a single generic scheduling concept. 
 
20. CALENDAR AND PUBLIC EVENTS 
The WiseIN Basic plan currently includes: 
• 
Join Communities  
• 
Attend public events  

• 
Browse Jobs & Opportunities.  
The Student plan includes: 
• 
Campus Communities  
• 
Student Networking Events  
• 
Internship & Job Board access.  
Therefore, event-related calendar content may differ depending on the user's account and 
plan. 
The chatbot should not imply that every account can create or host every event type. 
 
21. CALENDAR AND COMMUNITY EVENTS 
WiseIN's public product information connects communities and public events with the 
platform's networking experience.  
A calendar may help users discover or organize event-related activity, but the current 
public documentation does not provide enough information to specify: 
• 
community calendar layout,  
• 
event filtering,  
• 
recurring events,  
• 
event reminders,  
• 
RSVP states,  
• 
attendance tracking,  
• 
calendar export.  
These should not be invented. 
 
22. CALENDAR AND WEBINARS 
WiseIN's current India Organization plan includes Webinar Hosting.  
The organization experience therefore connects: 
Organization → Webinar → Scheduling → Calendar/Meeting 

However, the public documentation does not establish the exact calendar interface for 
webinars. 
Do not claim a specific webinar calendar workflow without product/API evidence. 
 
23. CALENDAR — USER FLOW 
A general WiseIN meeting scheduling flow can be represented as: 
1. Discover a verified person 
↓ 
2. Open profile/session 
↓ 
3. View available session or slot 
↓ 
4. Select an available time 
↓ 
5. Book the meeting 
↓ 
6. Meeting is scheduled 
↓ 
7. Calendar/meeting information is available 
↓ 
8. User joins at the scheduled time 
↓ 
9. AI meeting intelligence may be generated after the meeting 
This is a conceptual product flow based on WiseIN's documented scheduling and meeting 
features. Exact screens and button names should be taken from the current product UI. 
 
24. CALENDAR — AVAILABILITY FLOW 

For a user who wants others to book them: 
Set Availability 
↓ 
Create/enable bookable slots 
↓ 
Another user selects an available slot 
↓ 
Booking is created 
↓ 
Meeting becomes scheduled 
↓ 
Relevant calendar/notification information 
↓ 
Meeting takes place 
WiseIN officially describes this concept as: 
“Set your availability. Let others book you.” 
 
25. CALENDAR — WHAT USERS SHOULD CHECK BEFORE A MEETING 
Before confirming or joining a scheduled meeting, the chatbot should recommend 
checking: 
• 
Participant  
• 
Date  
• 
Start time  
• 
Duration  
• 
Time zone if shown  
• 
Meeting type/session  

• 
Join option/link  
• 
Any relevant booking information  
The previously supplied meeting confirmation email demonstrates the importance of date, 
time, duration, participant, and joining information. 
 
26. CALENDAR — COMMON USER QUESTIONS 
Q: What is WiseIN Calendar? 
“WiseIN's calendar functionality is connected to its scheduling, video meetings, sessions, 
events, and organization meeting workflows. WiseIN allows users to set availability, book 
video conversations, and manage scheduled meetings.” 
 
Q: Can I schedule a video call on WiseIN? 
“Yes. WiseIN is designed around video-first professional conversations, and its website 
describes booking video calls and Smart Slot booking.” 
 
Q: Can people book time with me? 
“Yes. WiseIN's Smart scheduling functionality lets you set your availability so other users 
can book available times.” 
 
Q: Does WiseIN have calendar synchronization? 
“WiseIN's organization documentation explicitly describes Calendar Sync for 1:1 and group 
meetings.” 
 
Q: Will I be notified when someone books me? 
“WiseIN's official app documentation says users can get notified when someone books 
them.” 
 
Q: Can I join the meeting from WiseIN? 

“Yes. The supplied WiseIN meeting confirmation indicates that users can join the meeting 
directly from WiseIN at the scheduled time.” 
 
Q: Are all WiseIN meetings 30 minutes? 
“No fixed universal duration should be assumed. The supplied WiseIN UI shows several 30-
minute sessions, but the duration can depend on the particular session or booking.” 
 
Q: Can I see public events on WiseIN? 
“Yes. WiseIN provides public events, and its current Basic plan includes attendance at 
public events.” 
 
Q: Does WiseIN have a calendar for events? 
“WiseIN has event pages that include a Calendar section. The exact relationship between 
the public event calendar and an individual's personal meeting calendar should be 
determined from the current product interface.” 
 
27. TROUBLESHOOTING 
Problem: My booked meeting is not visible 
Recommended checks: 
1. Refresh WiseIN.  
2. Check the relevant Calendar/meeting area.  
3. Check your meeting/session information.  
4. Verify the booking confirmation.  
5. Check the date and time.  
6. Check notifications or confirmation messages.  
7. If still missing, contact WiseIN support.  
Do not tell the user that a particular calendar location exists unless confirmed by the 
current UI. 

 
Problem: Someone booked me but I cannot find the meeting 
Check: 
• 
Booking confirmation  
• 
Date  
• 
Time  
• 
Participant  
• 
Availability/slot information  
• 
Notifications  
• 
Calendar/meeting section  
If the booking was confirmed but is not visible, escalate to WiseIN support. 
 
Problem: Meeting time looks incorrect 
Check: 
• 
displayed date,  
• 
displayed time,  
• 
timezone,  
• 
booking confirmation,  
• 
device/system time if relevant.  
Do not assume a timezone conversion rule without product confirmation. 
 
Problem: I cannot book a slot 
Possible causes include: 
• 
The slot may no longer be available.  
• 
Another person may have booked it.  
• 
The user's availability may have changed.  

• 
The session may no longer be bookable.  
• 
A temporary application/network problem may have occurred.  
These are troubleshooting possibilities, not confirmed WiseIN error codes. 
 
Problem: Calendar synchronization is not working 
For organization users: 
1. Verify the meeting was successfully booked.  
2. Verify that calendar synchronization is available for the organization/account.  
3. Check the calendar connection/integration if exposed by the current UI.  
4. Refresh/retry.  
5. Contact support if synchronization remains unsuccessful.  
Do not invent the names of external calendar providers or synchronization APIs. 
 
28. SUPPORT ESCALATION 
WiseIN's official Contact page states that users can send a support message and that the 
team aims to respond within 24 hours.  
For Calendar problems, the chatbot should collect non-sensitive information such as: 
• 
What the user attempted  
• 
Meeting/session/event name  
• 
Date  
• 
Time  
• 
Participant, where appropriate  
• 
Whether the booking was confirmed  
• 
Error message  
• 
Screenshot  
• 
Device/browser/app context  

Never ask for: 
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
Other credentials  
 
29. CALENDAR AND PRIVACY 
Calendar information can contain professional and personal scheduling information. 
The chatbot should treat: 
• 
meeting participants,  
• 
meeting dates,  
• 
meeting times,  
• 
booking details,  
• 
private conversations,  
• 
meeting recordings,  
as potentially sensitive information. 
WiseIN's Content Policies specifically address privacy and prohibit sharing private 
conversations, screenshots without consent, and sensitive personal or company 
information.  
Therefore, the chatbot should never expose one user's private calendar information to 
another user without proper authorization. 
 
30. AUTHORIZATION FOR CALENDAR DATA 
Calendar information is user-specific live data. 

Therefore: 
“What meetings do I have today?” 
should not be answered from RAG documentation. 
The correct architecture is: 
User authentication 
↓ 
Authorization 
↓ 
Calendar/meeting API 
↓ 
Retrieve only the current user's permitted events 
↓ 
LLM formats the response 
The LLM should never have unrestricted access to the database. 
 
31. RAG VS LIVE DATA 
RAG/static knowledge 
Use RAG for: 
• 
What Calendar means  
• 
Scheduling concepts  
• 
Smart Slot booking  
• 
Availability  
• 
Meeting workflow  
• 
Event/calendar concepts  
• 
Calendar Sync documentation  
• 
General troubleshooting  

• 
Privacy rules  
• 
Support guidance  
Live API 
Use an authorized backend API for: 
• 
Today's meetings  
• 
Upcoming meetings  
• 
Past meetings  
• 
Current bookings  
• 
User availability  
• 
Available slots  
• 
Event registrations  
• 
Calendar synchronization status  
• 
Meeting status  
• 
Participant information  
• 
Join information  
• 
User-specific calendar entries  
This distinction is essential for an accurate WiseIN chatbot. 
 
32. RECOMMENDED CALENDAR API ARCHITECTURE 
For a question such as: 
“What meetings do I have tomorrow?” 
the chatbot should use: 
Chat UI 
↓ 
Chat API 
↓ 

Authentication 
↓ 
Authorization 
↓ 
Calendar/Meetings API 
↓ 
User's calendar data 
↓ 
LLM 
↓ 
Natural-language answer 
For: 
“How does WiseIN scheduling work?” 
the chatbot can answer directly from RAG. 
 
33. CALENDAR AI INTENTS 
Recommended intent taxonomy: 
General 
calendar_overview 
what_is_calendar 
calendar_help 
calendar_navigation 
Meetings 
upcoming_meetings 
todays_meetings 
past_meetings 

meeting_details 
meeting_duration 
meeting_date 
meeting_time 
join_meeting 
meeting_confirmation 
Scheduling 
schedule_meeting 
book_meeting 
book_video_call 
smart_slot_booking 
availability 
manage_availability 
available_slots 
Events 
calendar_events 
public_events 
event_calendar 
event_schedule 
student_events 
organization_events 
webinars 
Synchronization 
calendar_sync 
organization_calendar 
meeting_calendar_sync 

calendar_integration 
Troubleshooting 
calendar_missing_meeting 
booking_missing 
wrong_meeting_time 
timezone_issue 
calendar_sync_error 
cannot_book_slot 
meeting_join_issue 
 
34. IMPORTANT ENTITIES 
The RAG system should recognize: 
• 
Calendar  
• 
Meeting  
• 
Video Call  
• 
Session  
• 
Slot  
• 
Availability  
• 
Smart Slot  
• 
Booking  
• 
Event  
• 
Public Event  
• 
Student Networking Event  
• 
Webinar  
• 
Organization  
• 
Calendar Sync  

• 
Participant  
• 
Date  
• 
Time  
• 
Time Zone  
• 
Meeting Duration  
• 
Meeting Confirmation  
• 
Join Meeting  
• 
AI Meeting Summary  
 
35. CALENDAR DOCUMENT RELATIONSHIPS 
The Calendar document should link conceptually to the other WiseIN knowledge-base 
documents. 
Profile 
Users can discover sessions and available professional conversations through profiles. 
Sessions 
Sessions can represent bookable conversations. 
Slots 
Slots represent available meeting times. 
Meetings 
A successful booking results in a scheduled meeting. 
Notifications 
Users can receive booking-related notifications. 
Events 
Public/community events can have calendar-related information. 
Organizations 
Organization meetings can use Calendar Sync. 

Analytics 
Organization meetings may contribute to meeting analytics. 
Scheduled Posts 
Scheduled content publication is separate from meeting/event scheduling. 
 
36. CALENDAR VS SCHEDULED POSTS 
This distinction is especially important for the AI chatbot. 
Calendar 
Used primarily for: 
• 
Meetings  
• 
Sessions  
• 
Availability  
• 
Bookings  
• 
Events  
• 
Organization scheduling  
• 
Calendar synchronization  
Scheduled Posts 
Used for: 
• 
Future publication of content.  
A user asking: 
“How do I schedule something?” 
is ambiguous. 
The chatbot should determine whether they mean: 
Schedule a meeting 
or 
Schedule a post 
before giving a detailed workflow if context does not resolve it. 

 
37. CALENDAR VS EVENTS 
Calendar 
Personal or organization scheduling context involving meetings, bookings, and availability. 
Events 
Community/public/organization activities that users can discover or attend. 
An event can have calendar-related information, but an event should not automatically be 
treated as a personal meeting. 
 
38. CALENDAR VS AVAILABILITY 
These are related but different. 
Availability answers: 
“When can someone book me?” 
Calendar answers: 
“What scheduled activities do I have?” 
Booking answers: 
“Which available slot did someone select?” 
Meeting answers: 
“What scheduled conversation will take place?” 
 
39. CALENDAR VS MEETING ANALYTICS 
A calendar contains scheduling information. 
Analytics contains historical or aggregated information about activity. 
For example, WiseIN's organization platform exposes Meetings and Analytics as separate 
dashboard areas.  
Therefore, do not use analytics data as a substitute for a user's current calendar. 
 

40. UNSUPPORTED DETAILS — DO NOT INVENT 
The following Calendar details are not sufficiently documented by the current public 
WiseIN sources: 
• 
Exact personal Calendar page URL  
• 
Exact Calendar navigation path in the current UI  
• 
Exact calendar layout  
• 
Month/week/day view availability  
• 
Exact calendar filters  
• 
Drag-and-drop scheduling  
• 
Recurring meetings  
• 
Recurring events  
• 
Google Calendar integration  
• 
Microsoft Outlook integration  
• 
Apple Calendar integration  
• 
ICS export  
• 
ICS import  
• 
Exact synchronization frequency  
• 
Automatic timezone conversion rules  
• 
Calendar sharing  
• 
Calendar permissions  
• 
Delegate calendars  
• 
Team calendar permissions  
• 
Exact reminder intervals  
• 
SMS reminders  
• 
WhatsApp reminders  
• 
Email reminder timing  

• 
Meeting cancellation rules  
• 
Rescheduling rules  
• 
Waiting-list functionality  
• 
Conflict-detection behavior  
• 
Maximum meetings per day  
• 
Maximum booking duration  
• 
Minimum notice period  
• 
Buffer time  
• 
Exact availability recurrence rules  
• 
Calendar API endpoints  
• 
Calendar webhook behavior  
• 
Calendar export format  
• 
Exact event RSVP states.  
The chatbot should not guess these details. 
 
41. SOURCE PRIORITY 
For Calendar questions, use this hierarchy. 
Priority 1 — Current WiseIN UI 
Use current product UI for: 
• 
Calendar layout  
• 
Buttons  
• 
Navigation  
• 
Meeting controls  
• 
Date/time controls  
• 
Current terminology.  
Priority 2 — Official WiseIN website 

Use official sources for: 
• 
Smart scheduling  
• 
Availability  
• 
Video calls  
• 
Events  
• 
Calendar Sync  
• 
Plans  
• 
Organization functionality.  
Priority 3 — Internal API/product documentation 
Use internal documentation for: 
• 
Calendar states  
• 
Permissions  
• 
Integrations  
• 
Exact APIs  
• 
Sync behavior  
• 
Limits  
• 
Notifications  
• 
Reminder rules.  
Priority 4 — General assumptions 
Do not use generic Google/Outlook/social-network calendar behavior to fill WiseIN 
documentation gaps. 
 
42. RAG METADATA 
document_id: WISEIN-CALENDAR-001 
feature: Calendar 
category: Scheduling & Meetings 

platform: WiseIN 
content_type: Product Knowledge Base 
audience: Users, Support, AI Chatbot 
source_priority: Current UI + Official WiseIN Documentation 
status: Active 
Retrieval tags 
calendar 
wisein calendar 
meeting calendar 
calendar sync 
meeting schedule 
schedule meeting 
book meeting 
video call 
video meeting 
availability 
smart slot 
slot booking 
sessions 
meeting confirmation 
upcoming meeting 
meeting date 
meeting time 
meeting duration 
public events 
event calendar 

organization calendar 
organization meetings 
webinar 
calendar synchronization 
 
43. GOLDEN ANSWERS 
“What is the WiseIN Calendar?” 
“WiseIN's calendar and scheduling functionality is connected to video meetings, sessions, 
bookings, events, availability, and organization meetings. WiseIN's platform is designed 
around scheduling verified professional conversations and meetings.” 
 
“How do I schedule a meeting?” 
“Open the relevant WiseIN profile or session, select an available time/slot, and complete 
the booking. WiseIN describes Smart Slot booking as a way to set your availability and let 
others book you.” 
 
“Can people book me?” 
“Yes. WiseIN's Smart scheduling functionality allows you to set your availability so other 
people can book available times.” 
 
“Does WiseIN sync with a calendar?” 
“WiseIN's organization documentation describes Calendar Sync for 1:1 and group 
meetings. The exact external calendar integrations should be checked against the current 
product configuration.” 
 
“Will I know when someone books me?” 
“Yes. WiseIN's official app documentation states that users can get notified when someone 
books them.” 

 
“Can I see events in a calendar?” 
“WiseIN provides event pages with a Calendar section. The exact relationship between the 
event calendar and your personal meeting calendar depends on the current product 
implementation.” 
 
“How long are WiseIN meetings?” 
“WiseIN supports sessions with defined durations. The supplied WiseIN UI shows several 
30-minute sessions, but 30 minutes should not be treated as a universal duration for every 
meeting.” 
 
“I can't find my meeting.” 
“First check the booking confirmation and verify the date, time, participant, and meeting 
details. Then refresh WiseIN and check the relevant meeting/calendar area. If the meeting 
was confirmed but is still missing, contact WiseIN support with the booking details and any 
error message.” 
 
44. FINAL CHATBOT GUARDRAILS 
The WiseIN Calendar chatbot must: 
1. Treat Calendar as part of WiseIN's scheduling and meeting ecosystem.  
2. Distinguish Calendar from Scheduled Posts.  
3. Distinguish Calendar from Events.  
4. Distinguish Availability from Calendar.  
5. Use Smart Slot terminology when explaining WiseIN's booking model.  
6. Recognize that users can set availability and allow others to book them.  
7. Recognize WiseIN's video-first meeting model.  
8. Recognize organization Calendar Sync as an officially documented feature.  
9. Never invent external calendar providers.  

10. Never invent reminder intervals.  
11. Never invent timezone-conversion rules.  
12. Never claim every meeting has the same duration.  
13. Never expose another user's calendar information.  
14. Use live authorized APIs for user-specific calendar questions.  
15. Use RAG for general Calendar explanations.  
16. Treat supplied screenshots as current UI observations rather than permanent API 
guarantees.  
17. Never request passwords, OTPs, authentication tokens, or other secrets.  
18. Escalate undocumented product behavior instead of guessing.  
19. Use current official WiseIN information when it conflicts with older documentation.  
20. Keep meeting, event, organization, and scheduled-post data logically separated.  
 
45. FINAL KNOWLEDGE SUMMARY 
WiseIN Calendar is part of the platform's broader scheduling ecosystem for verified 
professional conversations, video meetings, sessions, availability, bookings, events, and 
organization meetings. WiseIN's current website describes video-first conversations where 
users can schedule calls, while its Smart scheduling functionality allows users to set 
availability and let others book them. The official app documentation confirms that users 
can manage availability and slot bookings, book and join video calls, and receive 
notifications when someone books them. WiseIN's organization documentation 
additionally describes Calendar Sync for 1:1 and group meetings. Public WiseIN event 
pages also provide a Calendar section for event-related scheduling. Exact personal-
calendar UI, external calendar providers, synchronization frequency, reminder timing, 
recurring events, timezone conversion, and other advanced calendar behaviors are not 
sufficiently documented publicly and must not be invented by the chatbot.  
 



---

