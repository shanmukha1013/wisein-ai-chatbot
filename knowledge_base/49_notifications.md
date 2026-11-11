# Notifications

## Source: WISEIN-NOTIFICATIONS-049.pdf

WISEIN — NOTIFICATIONS  
Document ID: WISEIN-NOTIFICATIONS-049 
Document Type: Product / Feature Knowledge Base for AI Chatbot and RAG 
Platform: WiseIN 
Feature: Notifications 
 
1. DOCUMENT PURPOSE 
This document defines the knowledge required for the WiseIN AI chatbot to answer 
questions about the Notifications feature. 
It combines: 
• 
Current official WiseIN website information  
• 
WiseIN Privacy Policy  
• 
WiseIN app/product documentation  
• 
WiseIN Terms and Content Policies  
• 
The supplied WiseIN Notifications UI screenshots  
• 
The supplied WiseIN Settings → Notifications screenshot  
• 
The supplied WiseIN meeting-confirmation email screenshot  
• 
Previously prepared WiseIN knowledge-base documents  
The chatbot must distinguish between: 
1. The Notifications center  
2. Notification settings  
3. Email notifications  
4. Meeting/booking notifications  
5. Network/activity notifications  
6. Current notification data  
Static RAG documentation can explain what notifications are and what categories exist, 
while live WiseIN data should determine which notifications a particular user currently has. 

 
2. WHAT ARE WISEIN NOTIFICATIONS? 
Notifications keep WiseIN users informed about relevant activity, conversations, 
meetings, network activity, community activity, account/security events, and important 
platform announcements. 
WiseIN's current Settings → Notifications interface describes notifications as providing 
real-time updates about messages, meeting invites, community activity, and 
important announcements. 
The official WiseIN app page also states that users can get notified when someone books 
you.  
WiseIN's Privacy Policy further states that it may use contact details to send important 
account updates, login notifications, security alerts, policy changes, new features, 
professional opportunities, and community updates.  
 
3. NOTIFICATIONS CENTER — CURRENT UI 
The supplied WiseIN screenshot shows a dedicated page titled: 
Notification 
At the top of the page there are two tabs: 
• 
Activity  
• 
My network  
The screenshot currently displays: 
“No notifications yet” 
This is an important current UI observation. 
Activity 
The Activity tab appears to be the area for activity-related notifications associated with the 
user's WiseIN account. 
My Network 
The My network tab provides a separate view related to the user's network. 

The exact notification categories displayed under each tab should be determined from the 
live application because the supplied screenshot shows the tabs but does not display 
populated notification examples. 
 
4. NOTIFICATION SETTINGS — CURRENT UI 
The supplied second screenshot shows: 
Settings → Notifications 
The main heading is: 
Notifications 
The page contains a section titled: 
“Stay in the loop with WiseIn” 
The displayed description says that users can turn on notifications to receive real-time 
updates about: 
• 
Messages  
• 
Meeting invites  
• 
Community activity  
• 
Important announcements  
The interface also says: 
“You're always in control.” 
and: 
“You can change or turn off notifications anytime in settings.” 
A toggle is displayed on the right side. 
The page asks: 
“Would you like to enable notifications?” 
This establishes that WiseIN provides a user-controlled notification setting. 
 
5. NOTIFICATION TOGGLE 

The Settings → Notifications screenshot shows a toggle switch. 
The toggle is currently displayed in the enabled/on position in the supplied screenshot. 
The user can use this setting to control whether WiseIN sends notifications. 
Important distinction 
The chatbot should distinguish between: 
Notification setting 
and 
individual notification records. 
Turning notifications on/off is a preference. 
The Notification center is where notification activity can be displayed. 
 
6. NOTIFICATION CATEGORIES 
Based on the current WiseIN Settings UI and official website, the chatbot can recognize the 
following broad categories. 
Messages 
Notifications may inform users about relevant message activity. 
Meeting invitations 
Notifications may inform users about meeting-related activity. 
Community activity 
Notifications may inform users about relevant community activity. 
Important announcements 
Notifications may communicate important WiseIN announcements. 
Booking activity 
WiseIN's official app page specifically says users can be notified when someone books 
them.  
Security/account notifications 

WiseIN's Privacy Policy states that it uses contact details for important account updates, 
login notifications, and security alerts.  
Platform updates 
The Privacy Policy states that WiseIN may notify users about new features, professional 
opportunities, and community updates.  
 
7. ACTIVITY NOTIFICATIONS 
The Activity tab is visible in the supplied Notifications interface. 
Activity notifications can conceptually represent events that occur around the user's 
WiseIN account and interactions. 
Examples may include: 
• 
Relevant interaction activity  
• 
Meeting-related activity  
• 
Messages  
• 
Booking activity  
• 
Community activity  
• 
Other platform activity  
However, the exact notification types and wording should be obtained from the live 
notification system. 
The chatbot should not invent a notification category simply because it is common on 
other social platforms. 
 
8. MY NETWORK NOTIFICATIONS 
The supplied UI contains a separate: 
My network 
tab. 
This indicates that WiseIN separates network-related notification information from the 
general Activity view. 

WiseIN's broader product is built around verified professional networking, including 
discovering professionals and connecting through conversations.  
The chatbot can therefore explain the purpose of the My network section, but should not 
claim a specific list of notification events unless those events are confirmed by the live 
application. 
 
9. MEETING NOTIFICATIONS 
Meeting-related notifications are an important part of WiseIN. 
The Settings → Notifications UI explicitly mentions: 
Meeting invites 
as a notification category. 
WiseIN's official app page also confirms: 
• 
Booking and joining video calls  
• 
Managing availability and slot bookings  
• 
Notifications when someone books you.  
Therefore, meeting-related notification activity can include booking/invitation events. 
 
10. MEETING CONFIRMATION EMAIL — SUPPLIED UI EVIDENCE 
The supplied email screenshot shows a WiseIN email with the heading: 
“  Your Meeting is Confirmed” 
The email says: 
“Hi Cheduruvelli Shivaji,” 
and: 
“Your meeting with Marella Shanmukha Reddy is confirmed.” 
The visible meeting details are: 
• 
Date: Wednesday, September 2, 2026 at 05:30 AM  
• 
Duration: 30 minutes  

The email also says: 
“You'll be able to join directly from WiseIN at the scheduled time.” 
This demonstrates that WiseIN can send an email notification when a meeting is 
confirmed. 
Important limitation 
This screenshot proves the behavior for the supplied meeting confirmation example. 
It does not establish: 
• 
Every meeting is exactly 30 minutes  
• 
Every confirmation uses exactly the same email template  
• 
Every meeting generates an email  
• 
Exact email delivery timing  
• 
Exact reminder schedule  
• 
Exact cancellation/rescheduling email behavior  
Those details must come from current product behavior or internal documentation. 
 
11. MEETING CONFIRMATION VS NOTIFICATION CENTER 
The chatbot should distinguish between: 
In-app notification 
Appears in WiseIN's notification interface. 
Email notification 
Can be delivered to the user's registered email address. 
Meeting confirmation 
A specific notification/event confirming that a meeting booking exists. 
The supplied screenshot demonstrates an email confirmation. 
Therefore, a user may receive meeting-related information through more than one 
communication channel, depending on the current WiseIN implementation. 
 

12. BOOKING NOTIFICATIONS 
WiseIN's official app page specifically states: 
“Get notified when someone books you.”  
This is important for users who make their availability or conversation slots bookable. 
A booking notification can therefore inform a user that another person has booked a 
conversation or meeting. 
Chatbot example 
User: 
“Will I know if someone books a meeting with me?” 
Answer: 
“Yes. WiseIN's official app documentation says users can get notified when someone 
books them. The exact notification channel and current notification details should be 
checked from your account.”  
 
13. MESSAGE NOTIFICATIONS 
The WiseIN Notifications settings page explicitly identifies: 
Messages 
as one of the notification categories. 
WiseIN's platform includes messaging/conversation functionality, while its privacy policy 
also recognizes messages as user-generated platform content.  
Therefore, notification settings can be used to control notification behavior associated with 
messages. 
The chatbot should not claim that every message necessarily generates a push 
notification, email, or in-app notification unless the current implementation confirms it. 
 
14. COMMUNITY ACTIVITY NOTIFICATIONS 
The current Settings → Notifications interface explicitly mentions: 
Community activity 

as a notification category. 
WiseIN currently offers communities as part of its networking ecosystem, including 
campus communities for students.  
Community-related notifications may therefore keep users informed about relevant 
activity. 
However, the exact triggers should not be invented. 
For example, do not automatically state that users are notified for: 
• 
Every new community post  
• 
Every comment  
• 
Every member joining  
• 
Every community event  
unless those notification triggers are confirmed by the live system. 
 
15. IMPORTANT ANNOUNCEMENTS 
The Settings → Notifications screenshot explicitly mentions: 
Important announcements 
as a type of notification. 
WiseIN's Privacy Policy also says that significant policy changes may be communicated 
through: 
• 
Email notifications  
• 
Announcements on the WiseIN website or app  
• 
Policy updates.  
This means announcements are not necessarily limited to the in-app notification center. 
 
16. SECURITY NOTIFICATIONS 
WiseIN's Privacy Policy states that the platform may send: 
• 
Login notifications  

• 
Security alerts  
• 
Important account updates  
• 
Policy-change notifications.  
These should be treated differently from ordinary social/network activity. 
Security notifications may concern: 
• 
Account security  
• 
Login activity  
• 
Security-related changes  
• 
Important account events  
The chatbot must not expose sensitive security information to an unauthenticated user. 
 
17. PROFESSIONAL OPPORTUNITY NOTIFICATIONS 
WiseIN's Privacy Policy says it may notify users about: 
new features, professional opportunities, and community updates.  
This provides an official basis for opportunity-related notifications. 
However, the chatbot should not assume that every job, internship, or opportunity 
automatically generates a notification. 
 
18. NOTIFICATIONS AND WISEIN PRIVACY 
Notification data can reveal information about: 
• 
Messages  
• 
Connections  
• 
Meetings  
• 
Bookings  
• 
Community activity  
• 
Professional activity  

• 
Account activity  
WiseIN's Privacy Policy states that it collects and processes information related to content 
users share or interact with, including posts, messages, booking a call, job postings, 
comments, and other platform activity.  
Therefore, notification information should be treated as user-specific data. 
 
19. USER CONTROL 
WiseIN's Settings UI explicitly communicates that: 
“You're always in control.” 
and users can: 
“change or turn off notifications anytime in settings.” 
This means the chatbot can safely explain that notification preferences are user-
controlled. 
Golden answer 
“You can manage WiseIN notifications from Settings → Notifications. The current interface 
provides a notification toggle and states that notifications can be changed or turned off 
from Settings.” 
 
20. NOTIFICATION CENTER EMPTY STATE 
The supplied Notification screenshot displays: 
“No notifications yet” 
This is the empty-state message visible when there are no notifications shown in that view. 
Chatbot response 
If a user says: 
“My notifications are empty.” 
The chatbot should first distinguish between: 
1. There genuinely being no notification records.  

2. Notifications being disabled.  
3. The selected tab containing no notifications.  
4. Notifications failing to load.  
5. A temporary application/network problem.  
It should not automatically conclude that the user's account has no activity. 
 
21. ACTIVITY TAB VS MY NETWORK TAB 
The current UI shows: 
Notification 
 
[ Activity ] [ My network ] 
 
No notifications yet 
The chatbot should preserve these exact UI labels when helping users navigate the feature. 
Recommended wording 
“Open Notifications and check the Activity and My network tabs. A notification may 
appear in the relevant tab depending on the type of activity.” 
Do not invent a third notification tab unless the current UI provides one. 
 
22. SETTINGS NAVIGATION 
The supplied Settings screenshot shows the following left-side options: 
• 
Edit Profile  
• 
Notifications  
• 
Sign in & Security  
• 
Subscriptions  
• 
Data Privacy  

• 
Scheduled post  
• 
Saved Content  
• 
My Ads  
• 
Blocked  
• 
Deactivate  
• 
Delete Account  
• 
Log Out  
The selected item is: 
Notifications 
This provides current UI evidence that Notifications is accessible from Settings. 
Important UI rule 
Use the current visible path: 
Settings → Notifications 
rather than inventing a different navigation route. 
 
23. NOTIFICATIONS AND SIGN-IN & SECURITY 
Notifications and security settings are related but distinct. 
Notifications 
Controls general notification preferences. 
Sign in & Security 
Handles account/security-related settings. 
The chatbot should not tell users to change security credentials from the Notifications 
page. 
If a notification concerns suspicious login activity, the chatbot should direct the user 
toward the security/account controls and, where necessary, WiseIN support. 
 
24. NOTIFICATION CHANNELS 

Based on official WiseIN sources and supplied evidence, notification-related 
communication can involve: 
In-app notifications 
Shown in the Notification center. 
Email 
The supplied meeting confirmation demonstrates an email notification. 
WiseIN's Privacy Policy explicitly states that email can be used for important account 
updates, security alerts, features, opportunities, and community updates.  
Other device/app notification behavior 
The current Settings UI refers broadly to enabling notifications, but the public sources 
reviewed here do not fully specify the exact push-notification architecture. 
Therefore, do not claim: 
• 
Firebase is used  
• 
FCM is used  
• 
browser push is always supported  
• 
SMS notifications are supported  
• 
WhatsApp notifications are supported  
unless internally verified. 
 
25. NOTIFICATION PREFERENCES 
The supplied Settings interface shows a general notification toggle. 
The public screenshot does not show separate toggles for: 
• 
Messages  
• 
Meetings  
• 
Communities  
• 
Announcements  
• 
Security  

• 
Jobs  
Therefore, the chatbot should not claim that users can individually disable each category 
unless the live interface exposes such controls. 
Safe statement 
“The current WiseIN Settings interface provides a notification enable/disable control. The 
visible screen does not establish separate category-level switches.” 
 
26. NOTIFICATIONS AND MEETING REMINDERS 
The supplied evidence confirms meeting confirmation notifications. 
It does not establish a specific reminder schedule. 
Therefore, do not state: 
“WiseIN always sends a reminder 24 hours before the meeting.” 
or: 
“WiseIN sends reminders 15 minutes before every call.” 
unless current product documentation verifies those rules. 
 
27. NOTIFICATIONS AND MEETING CANCELLATIONS 
A meeting may potentially change after booking, but the public sources reviewed here do 
not establish the exact notification behavior for: 
• 
Cancellation  
• 
Rescheduling  
• 
Rejection  
• 
No-show  
• 
Host cancellation  
• 
Participant cancellation  
The chatbot should retrieve current booking data and notification records when available. 
 

28. NOTIFICATIONS AND SCHEDULED CONVERSATIONS 
WiseIN's product supports scheduled conversations and smart slot booking. 
The homepage describes: 
“Schedule a call in 2 taps” 
and the Premium plan includes Smart Slot booking.  
The app page also states that users can manage availability and slot bookings and receive 
notifications when someone books them.  
Therefore, notifications are an important part of the booking workflow. 
 
29. NOTIFICATIONS AND EVENTS 
WiseIN supports public events and community-related activities. 
The homepage currently lists: 
Attend public events 
for Basic users and: 
Student Networking Events 
for the Student plan.  
The Notifications settings screen also explicitly mentions community activity and 
important announcements. 
The chatbot should not claim that every event automatically produces a notification. 
 
30. NOTIFICATIONS AND JOBS 
WiseIN provides Jobs & Opportunities functionality. 
The current homepage lists: 
Browse Jobs & Opportunities 
for Basic users and: 
Internship & Job Board Access 
for Student users.  

The Privacy Policy also says WiseIN may notify users about professional opportunities.  
Therefore, opportunity-related notifications are supported at a general level. 
But the chatbot must not assume: 
“Every new job automatically sends a notification.” 
That behavior requires live or internal product confirmation. 
 
31. NOTIFICATIONS AND COMMUNITIES 
WiseIN's current product includes communities, and the Settings → Notifications UI 
specifically mentions: 
Community activity 
The chatbot can therefore explain that community-related activity may generate 
notification information. 
For detailed community notification triggers, use the current application/API rather than 
guessing. 
 
32. NOTIFICATIONS AND POSTS 
WiseIN's homepage currently includes: 
New Post 
in the Home interface.  
The current public sources establish that WiseIN supports posts, but they do not provide a 
complete notification-trigger specification for: 
• 
Likes  
• 
Comments  
• 
Reposts  
• 
Shares  
• 
Mentions  

Therefore, those should not automatically be documented as notification triggers unless 
the live product confirms them. 
 
33. NOTIFICATIONS AND NETWORK ACTIVITY 
The My network tab indicates that WiseIN provides a separate notification view associated 
with the user's network. 
WiseIN's product is built around: 
• 
Discovering verified people  
• 
Professional connections  
• 
Conversations  
• 
Networking.  
The chatbot should use live notification records to identify the exact network event. 
 
34. EMAIL NOTIFICATION — MEETING CONFIRMATION 
The supplied meeting confirmation email provides a useful knowledge-base example. 
Visible structure 
Your Meeting is Confirmed 
Greeting: 
Hi Cheduruvelli Shivaji, 
Confirmation: 
Your meeting with Marella Shanmukha Reddy is confirmed. 
Meeting Details: 
Date: Wednesday, September 2, 2026 at 05:30 AM 
Duration: 30 minutes 
Instruction: 
You'll be able to join directly from WiseIN at the scheduled time. 
Signature: 

Santhosh 
WiseIN 
RAG interpretation 
This demonstrates a WiseIN email confirmation workflow for a meeting. 
Do not treat the specific participant names, date, or time as reusable knowledge. 
 
35. NOTIFICATION DATA MODEL 
For implementation, notification records may conceptually contain: 
notification_id 
user_id 
type 
category 
title 
message 
actor_id 
actor_name 
target_id 
target_type 
read_status 
created_at 
updated_at 
action_url 
metadata 
These are recommended architecture fields, not confirmed WiseIN database fields. 
The implementation team should use the actual WiseIN backend schema. 
 

36. RECOMMENDED NOTIFICATION TYPES 
If the backend needs a normalized notification taxonomy, possible categories include: 
MESSAGE 
MEETING_INVITE 
MEETING_BOOKED 
MEETING_CONFIRMED 
MEETING_UPDATED 
MEETING_CANCELLED 
COMMUNITY_ACTIVITY 
NETWORK_ACTIVITY 
ANNOUNCEMENT 
SECURITY_ALERT 
ACCOUNT_UPDATE 
PROFESSIONAL_OPPORTUNITY 
SYSTEM_UPDATE 
These are implementation recommendations, not a claim that WiseIN currently uses 
exactly these enum values. 
 
37. READ / UNREAD STATUS 
A notification system commonly needs read/unread state. 
However, the supplied screenshot does not show a notification with a visible read/unread 
indicator. 
Therefore, the chatbot documentation should not claim a particular read/unread UI or 
“mark all as read” feature unless the live application confirms it. 
If the backend exposes notification read state, it can be used for personalized responses. 
 
38. NOTIFICATION CLICK ACTIONS 

A notification may logically lead a user to a relevant WiseIN object, such as: 
• 
Message  
• 
Profile  
• 
Meeting  
• 
Booking  
• 
Community  
• 
Announcement  
However, the supplied screenshots do not expose the exact click behavior. 
Therefore, do not hard-code a specific navigation path without confirming the current UI. 
 
39. SECURITY AND PRIVACY 
Notifications may contain sensitive information. 
The chatbot must never reveal another user's: 
• 
Private meeting details  
• 
Meeting link  
• 
Messages  
• 
Booking information  
• 
Private community activity  
• 
Account security information  
• 
Personal contact information  
unless the authenticated user is authorized to access it. 
WiseIN's Privacy Policy states that the company uses information for account 
management, meetings, discussions, security, personalization, and communication, while 
stating that it does not sell personal information.  
 
40. NOTIFICATION SECURITY ALERTS 
If a user receives a suspicious notification, the chatbot should not ask them to provide: 

• 
Password  
• 
OTP  
• 
Authentication code  
• 
Session token  
• 
API key  
• 
Payment credentials  
Instead, it should direct them toward WiseIN's account/security controls and official 
support. 
WiseIN's Privacy Policy states that login attempts and session activity are monitored for 
security purposes.  
 
41. COMMON USER QUESTIONS 
Q: Where can I see my notifications? 
Answer: 
“Open WiseIN's Notification section. The current interface has Activity and My network 
tabs.” 
 
Q: How do I turn notifications on? 
Answer: 
“Go to Settings → Notifications and use the notification toggle. The current WiseIN 
settings page says you can change or turn off notifications from Settings.” 
 
Q: How do I turn notifications off? 
Answer: 
“Go to Settings → Notifications and turn off the notification toggle.” 
 
Q: What notifications does WiseIN support? 

Answer: 
“WiseIN's current notification settings mention messages, meeting invites, community 
activity, and important announcements. WiseIN also documents notifications for bookings 
and uses email for certain account, security, feature, opportunity, and community 
updates.”  
 
Q: Will I get notified when someone books me? 
Answer: 
“Yes. WiseIN's official app information says users can get notified when someone books 
them.”  
 
Q: Will I get a meeting confirmation? 
Answer: 
“WiseIN can send meeting confirmation notifications. The supplied WiseIN email example 
shows a ‘Your Meeting is Confirmed’ email containing the meeting date and duration.” 
 
Q: I received a meeting confirmation email. What does it mean? 
Answer: 
“It indicates that the meeting booking has been confirmed. The supplied WiseIN 
confirmation email shows the meeting participant, date, and duration and says the meeting 
can be joined directly from WiseIN at the scheduled time.” 
 
Q: Why don't I have any notifications? 
Answer: 
“First check the Activity and My network tabs in Notifications. Then check Settings → 
Notifications to make sure notifications are enabled. If you expect a specific meeting, 
message, or booking notification and it still isn't visible, the current account/activity data 
should be checked.” 
 

Q: My notification setting is ON but I don't see notifications. 
Answer: 
“An enabled notification setting does not necessarily mean that there is a notification to 
display. Check both Activity and My network, refresh the page/app, and verify that the 
expected activity actually occurred. If a specific notification is still missing, the notification 
record should be checked.” 
 
Q: Can I disable notifications? 
Answer: 
“Yes. The current WiseIN Settings → Notifications page says you can change or turn off 
notifications anytime in Settings.” 
 
Q: Can I disable only meeting notifications? 
Answer: 
“The supplied Settings screen shows a general notification toggle, but it does not establish 
separate switches for each notification category. Check the current WiseIN settings 
interface for any category-specific controls available to your account.” 
 
42. NOTIFICATION TROUBLESHOOTING FLOW 
When a user says: 
“I am not receiving notifications.” 
The chatbot should follow: 
Step 1 — Check notification setting 
Ask/verify whether: 
Settings → Notifications 
is enabled. 
Step 2 — Check Notification center 
Open: 

Notifications → Activity 
and: 
Notifications → My network 
Step 3 — Identify notification type 
Determine whether the missing notification concerns: 
• 
Meeting  
• 
Message  
• 
Network  
• 
Community  
• 
Announcement  
• 
Security  
• 
Opportunity  
Step 4 — Verify source activity 
Check whether the underlying activity actually occurred. 
For example: 
Missing meeting notification 
→ Check whether a booking actually exists. 
Step 5 — Check live data 
If the user expects a specific notification, query the authorized notification/booking 
system. 
Step 6 — Check email if applicable 
For meeting confirmations or account notifications, verify whether an email was generated 
or delivered. 
Step 7 — Escalate 
If the expected notification exists in backend data but is not displayed/delivered, treat it as 
a potential notification delivery or UI issue. 
 

43. NOTIFICATION FAILURE SCENARIOS 
Notification setting is disabled 
Expected behavior: 
Notifications may not be delivered/displayed according to the user's settings. 
 
Notification center is empty 
Possible explanations: 
• 
No notification activity  
• 
Wrong tab selected  
• 
Notifications not loaded  
• 
Notification setting disabled  
• 
Temporary network/application issue  
Do not assume one cause without checking. 
 
Meeting was booked but notification is missing 
Check: 
1. Booking status  
2. User identity  
3. Notification preference  
4. Notification record  
5. Email notification record if applicable  
 
Meeting confirmation email was received but notification center is empty 
These are separate channels. 
The chatbot should not assume that an email confirmation must always correspond to a 
visible in-app notification unless the backend establishes that relationship. 

 
44. NOTIFICATION CENTER VS EMAIL 
The chatbot should use this distinction: 
Notification Center 
Interactive WiseIN UI containing: 
• 
Activity  
• 
My network  
Notification Settings 
Controls notification preference. 
Email Notifications 
Messages delivered to the user's registered email address. 
Meeting Confirmation 
A specific type of meeting-related communication. 
 
45. NOTIFICATIONS AND ACCOUNT COMMUNICATION 
WiseIN's Privacy Policy states that the platform uses contact information to communicate: 
• 
Important account updates  
• 
Login notifications  
• 
Security alerts  
• 
Policy changes  
• 
New features  
• 
Professional opportunities  
• 
Community updates  
• 
Customer support responses  
• 
Marketing emails/newsletters, with an opt-out option.  
The chatbot should therefore avoid saying: 

“All WiseIN notifications appear only in the Notification tab.” 
Some communications can occur through email or other channels. 
 
46. NOTIFICATIONS AND POLICY CHANGES 
WiseIN states that if significant Privacy Policy changes occur, users may be notified by: 
• 
Email  
• 
Website/app announcement  
• 
Updated policy information.  
This should be classified as an important platform/account communication, rather than 
ordinary social activity. 
 
47. NOTIFICATIONS AND MARKETING EMAILS 
The Privacy Policy states that WiseIN may send marketing emails and newsletters and that 
users can opt out.  
The chatbot should distinguish these from transactional notifications such as: 
• 
Meeting confirmation  
• 
Security alert  
• 
Account update  
Do not tell a user that disabling the in-app notification toggle necessarily unsubscribes 
them from every email/newsletter. 
The available sources do not establish that relationship. 
 
48. NOTIFICATIONS AND PRIVACY 
The chatbot should treat notification content as potentially private. 
For example, a notification saying: 
“Your meeting with [person] is confirmed” 
contains information about the user's professional interaction. 

Therefore: 
• 
Don't expose notifications to another account.  
• 
Don't reveal private notification contents without authorization.  
• 
Don't provide meeting links to unauthorized users.  
• 
Don't expose security alerts through an unauthenticated chatbot.  
 
49. RAG VS LIVE API 
This is a critical implementation rule. 
RAG should answer: 
• 
What are WiseIN notifications?  
• 
Where are notification settings?  
• 
What does Activity mean?  
• 
What does My network mean?  
• 
What types of notifications does WiseIN document?  
• 
How can users enable/disable notifications?  
• 
What is a meeting confirmation?  
• 
Does WiseIN notify users about bookings?  
• 
What are WiseIN's notification/privacy principles?  
Live API should answer: 
• 
Do I have a new notification?  
• 
What is my latest notification?  
• 
Who booked me?  
• 
When was the meeting booked?  
• 
What meetings are confirmed?  
• 
Is my notification read?  
• 
What is my meeting link?  

• 
Did a particular notification get generated?  
• 
Which notifications do I currently have?  
• 
What is my current notification preference?  
 
50. RECOMMENDED NOTIFICATION API ARCHITECTURE 
For the chatbot, use controlled backend functions such as: 
get_my_notifications() 
get_my_unread_notifications() 
get_notification_details() 
get_notification_preferences() 
update_notification_preferences() 
get_my_recent_bookings() 
get_my_meeting_details() 
These are architecture examples only and are not verified WiseIN API endpoint names. 
The LLM should never directly access the notification database. 
 
51. AI INTENTS 
Recommended chatbot intents: 
notifications_overview 
notifications_center 
notifications_activity 
notifications_my_network 
notifications_settings 
notifications_enable 
notifications_disable 
notifications_preferences 

notifications_messages 
notifications_meeting 
notifications_meeting_invite 
notifications_meeting_confirmed 
notifications_meeting_booked 
notifications_community 
notifications_announcements 
notifications_security 
notifications_opportunities 
notifications_email 
notifications_missing 
notifications_empty 
notifications_read_status 
notifications_troubleshooting 
notifications_privacy 
notifications_support 
 
52. IMPORTANT ENTITIES 
The chatbot should recognize: 
• 
Notification  
• 
Notifications  
• 
Activity  
• 
My Network  
• 
Message  
• 
Meeting  
• 
Meeting Invite  

• 
Meeting Confirmation  
• 
Booking  
• 
Community  
• 
Announcement  
• 
Security Alert  
• 
Account Update  
• 
Professional Opportunity  
• 
Email  
• 
Notification Setting  
• 
Notification Toggle  
• 
Read  
• 
Unread  
• 
Meeting Date  
• 
Meeting Duration  
 
53. RAG METADATA 
Recommended metadata: 
document_id: WISEIN-NOTIFICATIONS-001 
feature: Notifications 
category: Notifications / Account / Communication 
platform: WiseIN 
content_type: Product Knowledge Base 
source_priority: Official Website + Current UI Observation 
requires_live_data: true 
user_specific: true 
privacy_sensitive: true 

transactional: true 
booking_related: true 
last_verified: 2026-09 
 
54. GOLDEN ANSWERS FOR THE CHATBOT 
“What are WiseIN Notifications?” 
“WiseIN Notifications keep you informed about activity such as messages, meeting invites, 
community activity, and important announcements. WiseIN also documents notifications 
when someone books you.”  
“Where are notification settings?” 
“Go to Settings → Notifications. The current WiseIN interface provides a notification toggle 
and says you can change or turn off notifications from Settings.” 
“What are the Activity and My network tabs?” 
“The Notifications page currently has Activity and My network tabs. Activity is for general 
account activity, while My network provides a separate view related to network activity. The 
exact notification records should be taken from your current WiseIN account.” 
“Will I know when someone books me?” 
“Yes. WiseIN's official app documentation says users can get notified when someone 
books them.”  
“I got a ‘Your Meeting is Confirmed’ email.” 
“That indicates your WiseIN meeting booking has been confirmed. The confirmation email 
contains the scheduled date and meeting duration and says you can join directly from 
WiseIN at the scheduled time.” 
“Why are there no notifications?” 
“Check both Activity and My network, then make sure notifications are enabled under 
Settings → Notifications. If you're expecting a specific meeting, booking, message, or 
other activity, the underlying account activity should also be checked.” 
 
55. UNSUPPORTED DETAILS — DO NOT INVENT 

The chatbot must not claim unsupported details such as: 
• 
Exact notification retention period  
• 
Maximum number of notifications stored  
• 
Exact notification database schema  
• 
Exact notification delivery latency  
• 
Exact push notification provider  
• 
Firebase/FCM implementation  
• 
Browser push implementation  
• 
SMS notification support  
• 
WhatsApp notification support  
• 
Exact notification sound  
• 
Exact badge-count behavior  
• 
Exact unread indicator  
• 
“Mark all as read” unless verified  
• 
Exact notification deletion workflow  
• 
Exact email delivery SLA  
• 
Exact reminder timing  
• 
24-hour reminder  
• 
1-hour reminder  
• 
15-minute reminder  
• 
Email for every notification  
• 
Push notification for every notification  
• 
Notification for every like/comment/follow  
• 
Notification for every job posting  
• 
Notification for every community action  
• 
Notification for every event  

• 
Category-specific toggles unless visible/current  
• 
Automatic notification synchronization across every device  
• 
Exact notification ordering algorithm  
 
56. SOURCE PRIORITY 
For notification questions, use this order: 
Priority 1 — Live WiseIN notification/account API 
For: 
• 
Current notifications  
• 
Read/unread state  
• 
Current preferences  
• 
Current meeting notifications  
• 
Current booking notifications  
Priority 2 — Official WiseIN website 
For: 
• 
Notification capabilities  
• 
Communication policies  
• 
Booking notifications  
• 
Security/account communications  
• 
Product functionality  
Priority 3 — Current WiseIN UI screenshots 
For: 
• 
Notification page layout  
• 
Activity tab  
• 
My network tab  
• 
Empty state  

• 
Settings → Notifications  
• 
Notification toggle  
• 
Current wording  
Priority 4 — Supplied email evidence 
For: 
• 
Meeting confirmation email structure  
• 
Example meeting details  
• 
Join-from-WiseIN wording  
Priority 5 — Internal WiseIN documentation 
Use whenever it is authoritative and more current. 
 
57. CRITICAL CHATBOT RULE 
The chatbot must distinguish between: 
“How WiseIN Notifications work” 
and: 
“What notifications this user has right now.” 
For example: 
RAG answer 
“WiseIN supports notifications for messages, meeting invites, community activity, and 
important announcements.” 
Live-data answer 
“You currently have 3 unread notifications, including a meeting confirmation.” 
The second answer must never be generated from static RAG. 
 
58. FINAL KNOWLEDGE SUMMARY 
WiseIN provides a dedicated Notifications experience with two visible tabs: 

Activity and My network. 
The supplied current UI screenshot shows an empty-state message: 
“No notifications yet.” 
WiseIN also provides Settings → Notifications, where the current interface allows users to 
enable or turn off notifications. The interface specifically describes real-time updates for 
messages, meeting invites, community activity, and important announcements. 
WiseIN's official app information additionally confirms that users can get notified when 
someone books them, alongside its video-call and slot-booking functionality.  
The supplied WiseIN meeting-confirmation email demonstrates that a confirmed meeting 
can also generate an email notification containing the participant, date, and duration, with 
an instruction to join through WiseIN at the scheduled time. 
WiseIN's Privacy Policy further documents account/security communications, including 
login notifications, security alerts, important account updates, new features, professional 
opportunities, community updates, and certain email communications.  
Notifications therefore form an important communication layer connecting WiseIN's: 
• 
Messaging  
• 
Professional network  
• 
Meetings  
• 
Sessions  
• 
Slot booking  
• 
Communities  
• 
Events  
• 
Opportunities  
• 
Security  
• 
Platform announcements  
Core chatbot rule 
RAG explains the WiseIN notification system and its documented categories. Live 
WiseIN data must determine the user's actual notifications, read status, preferences, 

booking activity, meeting confirmations, and other current account-specific 
information. 
 
 



---

