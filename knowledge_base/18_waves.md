# Waves

## Source: WISEIN WAVES DOCUMENTATION018.pdf

DOCUMENT 018 — WISEIN WAVES 
DOCUMENTATION 
Document ID 
WISEIN-WAV-018 
Module: Waves​
 Category: Core Product Features / Real-Time Audio​
 Version: 1.0​
 Status: Draft — Pending Product, Engineering, QA, Security, and Support Approval​
 Prepared By: MSR​
 Date: 17 September 2026​
 Intended Usage: Internal Documentation, Customer Support, QA, and AI/RAG Knowledge 
Base​
 Primary Source: WiseIN frontend codebase analysis (wisein-v2-client)​
 Backend Verification: Pending​
 Live Product Verification: Pending where explicitly stated 
 
1. Document Information 
This document provides structured documentation for the Waves module of WiseIN. 
The documentation covers: 
●​ Waves overview 
●​ Purpose and functionality 
●​ Access and navigation 
●​ Waves discovery 
●​ Search and tabs 
●​ Creating a Wave 
●​ Scheduling a Wave 
●​ Joining a Wave 
●​ Listener and Speaker workflows 
●​ Raise Hand functionality 
●​ Host controls 
●​ Audio controls 

●​ Chat 
●​ Reactions 
●​ Visibility and chat permissions 
●​ Roles and permissions 
●​ API references identified in the frontend 
●​ Loading and empty states 
●​ Error handling 
●​ Troubleshooting 
●​ Privacy and security considerations 
●​ Platform considerations 
●​ QA test cases 
●​ AI customer-support guidance 
●​ Human escalation 
●​ RAG knowledge-base requirements 
●​ Open questions and pending verification 
The Waves documentation is based primarily on the inspected frontend implementation. 
Therefore, frontend-defined behavior must not automatically be treated as confirmation of 
backend authorization, data retention, security enforcement, or production policy. 
 
2. Purpose of This Document 
The purpose of this document is to establish a reliable knowledge source for the WiseIN Waves 
module. 
It is intended to support four primary areas: 
2.1 User Support 
Provide accurate instructions for users who need help with: 
●​ Finding Waves 
●​ Joining a Wave 
●​ Creating a Wave 
●​ Scheduling a Wave 
●​ Requesting speaker access 
●​ Using the microphone 
●​ Using chat 
●​ Sending reactions 
●​ Leaving a Wave 

2.2 QA and Testing 
Provide testable workflows and expected behavior for QA teams. 
2.3 Engineering and Product 
Document the functionality identified in the frontend implementation while clearly identifying 
areas requiring backend or product confirmation. 
2.4 AI/RAG Knowledge Base 
Provide structured information that can be retrieved by the WiseIN AI customer-support chatbot 
without encouraging the AI to invent unsupported features or policies. 
 
3. Waves Module Overview 
Waves is WiseIN's real-time audio-room functionality. 
Based on the inspected frontend implementation, users can discover and participate in audio 
rooms and interact through: 
●​ Live audio 
●​ Text chat 
●​ Reactions 
●​ Speaker requests 
●​ Host moderation 
The frontend also contains functionality for creating and scheduling Waves with configurable 
room settings. 
3.1 Primary Purpose 
The Waves module is designed around live, audio-first professional conversations. 
Potential activities include: 
●​ Professional discussions 
●​ Community conversations 
●​ Founder discussions 
●​ Business discussions 
●​ Topic-based conversations 
●​ Interactive audio sessions 

The exact supported categories and business rules should be maintained according to the 
current WiseIN implementation. 
3.2 Communication Model 
The inspected implementation indicates the following communication model: 
Audio → Primary interaction 
Text chat → Supporting interaction 
Reactions → Real-time engagement 
Raise Hand → Request for speaking access 
Host controls → Moderation and participant management 
 
4. Waves Technology and Implementation 
The inspected frontend identifies the following implementation components: 
4.1 Main Components 
The Waves implementation includes components such as: 
●​ WavesCenterSection 
●​ WavesRightSidebar 
●​ WavesList 
●​ WaveCard 
●​ CreateAudioRoomModal 
●​ AudioRoomForm 
●​ LiveRoomView 
●​ RoomPermissionsSheet 
●​ ScheduleRoomSheet 
●​ SpeakersPicker 
4.2 Main Route 
The primary Waves page is implemented through: 
src/app/(ui)/waves/page.tsx 

Direct Wave room access is represented by: 
/waves/[id] 
4.3 State and API Handling 
Wave-related API interactions are handled through: 
src/hooks/waves/useWaves.ts 
4.4 Type Definitions 
Wave-specific types are maintained in: 
src/types/waves.ts 
The inspected implementation includes types associated with: 
●​ Wave visibility 
●​ Chat controls 
●​ Participant roles 
●​ Wave status 
4.5 Real-Time Audio 
The frontend integrates with GetStream through: 
@stream-io/video-react-sdk 
The inspected code therefore establishes a frontend integration with GetStream for the real-time 
audio experience. Backend configuration and production-level security behavior require 
separate verification. 
 
5. Accessing Waves 
5.1 Navigation 
Users access Waves through the main WiseIN navigation. 
Primary Route 

/waves 
Individual Wave Route 
/waves/[id] 
 
5.2 Authentication 
The inspected implementation relies on the WiseIN authentication context for user identity. 
Therefore, authenticated access is expected for interactive Wave actions. 
The exact authorization requirements for every Wave action must be verified against the 
backend implementation. 
 
6. Waves Main Interface 
The Waves interface is organized into two major areas: 
1.​ Wave Discovery Area 
2.​ Wave Creation / Information Sidebar 
 
6.1 Wave Discovery Area 
The discovery area contains Wave navigation and Wave cards. 
Available Tabs Identified 
●​ For You 
●​ Discover 
●​ Trending 
●​ Following 
●​ Completed 
These tabs are used to organize different Wave feeds. 
 

7. Waves Search 
The Waves interface contains a local search field. 
The inspected implementation indicates that Wave search can filter displayed Waves based on 
information associated with the Wave, including: 
●​ Wave title 
●​ Host name 
●​ Category 
Important 
The documented search behavior refers to the frontend filtering implementation. 
It should not be interpreted as confirmation that the backend performs global or server-side 
Wave search unless separately verified. 
 
8. Wave Card 
Each Wave can be represented through a Wave Card. 
A Wave Card may contain: 
●​ Wave title 
●​ Host avatar 
●​ Host information 
●​ Live status 
●​ Scheduled status 
●​ Category 
●​ Participant count 
●​ Join Room action 
●​ Set Reminder action 
●​ Share action 
The inspected frontend specifically identifies live and scheduled states and actions associated 
with Wave cards. 
 

8.1 Live Wave 
A live Wave can display: 
LIVE 
along with a visual live indicator. 
Users can use: 
Join Room 
to enter the Wave. 
 
8.2 Scheduled Wave 
A scheduled Wave can display: 
Scheduled 
and provide a: 
Set Reminder 
action. 
The exact notification delivery mechanism requires additional verification. 
 
9. Waves Discovery Tabs 
9.1 For You 
The For You tab is intended to provide a personalized Wave discovery experience. 
The exact personalization or recommendation algorithm is not established by the inspected 
frontend alone. 
Status 

Frontend functionality: Observed 
Recommendation logic: Pending Verification 
 
9.2 Discover 
The Discover tab provides a general Wave discovery feed. 
Users can browse available Waves and use the available search functionality. 
 
9.3 Trending 
The Trending tab is intended to display trending or popular Waves. 
The exact ranking criteria are not established by frontend inspection alone. 
Status 
Frontend tab: Confirmed 
Ranking algorithm: Pending Verification 
 
9.4 Following 
The Following tab is associated with Waves from followed users or relevant followed entities. 
The exact backend filtering rules should be verified. 
 
9.5 Completed 
The Completed tab is associated with Waves that have finished. 
The exact retention period and availability of completed Wave information require verification. 
 

10. Creating a Wave 
The Waves interface provides a: 
Start a Wave 
action. 
Selecting this action opens the Wave creation interface. 
The inspected implementation includes an AudioRoomForm for configuring the Wave. 
 
11. Wave Creation Form 
The creation form includes configuration areas such as: 
●​ Title 
●​ Category 
●​ Duration 
●​ Speakers 
●​ Visibility 
●​ Chat permissions 
●​ Start/Schedule controls 
The exact mandatory/optional status of each field should be verified through live QA. 
 
12. Wave Title 
The creator provides a title for the Wave. 
The title is used to identify the Wave in discovery interfaces. 
QA Requirements 
Verify: 
●​ Empty title behavior 
●​ Minimum title length 

●​ Maximum title length 
●​ Special characters 
●​ Duplicate titles 
●​ Unsupported characters 
●​ Validation messages 
Exact validation rules should not be assumed unless confirmed in code or live testing. 
 
13. Wave Category 
A category can be selected during Wave creation. 
The frontend documentation identifies categories as part of the Wave configuration. 
Examples identified in the implementation include areas such as: 
●​ Technology 
●​ Business 
●​ Design 
●​ Health 
The complete current category list should be verified against the live product or backend 
configuration. 
 
14. Wave Duration 
The inspected creation form provides duration options including: 
●​ 30 minutes 
●​ 1 hour 
●​ 2 hours 
●​ 3 hours 
These values should be treated as frontend-defined options and confirmed against backend 
enforcement before being presented as a product policy. 
 

15. Wave Visibility 
The frontend defines Wave visibility options: 
15.1 Public 
A Public Wave is intended to be accessible broadly. 
15.2 Followers Only 
A Followers Only Wave restricts access based on follower-related rules. 
15.3 Private 
A Private Wave is intended for restricted participation. 
Important 
The frontend defines these visibility values, but backend authorization must enforce the actual 
access restrictions. 
Therefore: 
Visibility settings shown in the UI must not be interpreted as proof of backend 
security enforcement until Engineering confirms the corresponding authorization 
rules. 
 
16. Chat Permissions 
The frontend defines chat-control options including: 
Anyone 
Chat participation is available to participants according to the configured rule. 
Followers Only 
Chat participation is restricted according to follower-related permissions. 
Speakers Only 

Only participants with speaker privileges can send messages. 
The exact backend enforcement must be verified. 
 
17. Starting a Wave Immediately 
A user can select the option to start a Wave immediately. 
General Workflow 
1.​ Open Waves. 
2.​ Select Start a Wave. 
3.​ Enter the Wave title. 
4.​ Select a category. 
5.​ Configure duration. 
6.​ Configure speakers and permissions if applicable. 
7.​ Select Start Now. 
8.​ The Wave is created. 
9.​ The creator enters the live Wave experience. 
10.​The creator acts as the host. 
The frontend identifies a startNow creation flow and corresponding Wave creation request. 
 
18. Scheduling a Wave 
Users can also schedule a Wave for a future date and time. 
Workflow 
1.​ Open Waves. 
2.​ Select Start a Wave. 
3.​ Enter the Wave information. 
4.​ Select the scheduling option. 
5.​ Select the required date. 
6.​ Select the required time. 
7.​ Configure Wave permissions. 
8.​ Confirm scheduling. 
9.​ The Wave appears as scheduled. 

Pending Verification 
The following require confirmation: 
●​ Reminder delivery 
●​ Push notifications 
●​ Email notifications 
●​ Automatic transition to live 
●​ What happens if the host does not start the Wave 
●​ Automatic cancellation behavior 
●​ Scheduled Wave expiration 
The frontend contains scheduling functionality, but notification and backend lifecycle behavior 
require additional verification. 
 
19. Discovering and Joining a Live Wave 
19.1 User Workflow 
1.​ Log into WiseIN. 
2.​ Open Waves. 
3.​ Browse the available tabs. 
4.​ Find a live Wave. 
5.​ Select Join Room. 
6.​ Complete any join confirmation if displayed. 
7.​ The Wave room is initialized. 
8.​ The user enters the live room. 
9.​ The user joins as a participant according to the assigned role. 
10.​The user can listen and interact according to their permissions. 
The inspected implementation references a join operation and GetStream initialization as part of 
this flow. 
 
20. Listener Role 
A Listener is a participant who can participate in the Wave without transmitting audio. 

Based on the frontend role model, a Listener can: 
●​ Hear the Wave audio 
●​ View chat 
●​ Send permitted interactions such as reactions 
●​ Request speaker access 
A Listener does not automatically receive permission to transmit audio. 
 
21. Raise Hand / Speaker Request 
A Listener can request permission to speak. 
Workflow 
1.​ Join the Wave. 
2.​ Remain in Listener mode. 
3.​ Select the Raise Hand control. 
4.​ The speaker request is submitted. 
5.​ The host receives the request. 
6.​ The host can approve the request. 
7.​ If approved, the user's role/permissions are updated. 
8.​ The user can then enable the microphone. 
The frontend references a raise-hand request and host approval workflow. 
 
22. Speaker Role 
A Speaker is a participant who has permission to transmit audio. 
After receiving speaker access: 
1.​ The user receives the appropriate audio permission. 
2.​ The microphone control becomes available. 
3.​ The user manually enables the microphone. 
4.​ Audio can then be transmitted. 
Important 

Receiving Speaker status does not necessarily mean the microphone automatically turns on. 
The frontend implementation requires user interaction to enable microphone access because 
browser permission behavior requires explicit user interaction. 
 
23. Microphone Controls 
The live room provides a microphone control. 
The control is used to: 
●​ Enable microphone 
●​ Disable microphone 
If Microphone Does Not Work 
Possible causes include: 
●​ Browser microphone permission denied 
●​ Operating-system microphone permission denied 
●​ User is still a Listener 
●​ Browser/device microphone unavailable 
●​ Network or audio initialization issue 
The AI should first determine whether the user has Speaker access before treating the issue as 
a microphone hardware or browser problem. 
 
24. Live Room 
The Live Room is the primary interactive Wave experience. 
The inspected frontend identifies the following major interactions: 
●​ Audio 
●​ Microphone 
●​ Raise Hand 
●​ Chat 
●​ Reactions 
●​ Participant management 

●​ Host moderation 
The live room is integrated with the GetStream audio/video SDK. 
 
25. Text Chat 
The Wave room provides text chat. 
The inspected frontend uses an API-based polling mechanism for retrieving chat messages. 
The identified implementation uses a 3-second polling interval for chat retrieval. 
Important 
This is an implementation detail and not necessarily a permanent product architecture. 
If the implementation changes, this documentation must be updated. 
 
26. Reactions 
Users can send heart reactions during a Wave. 
The frontend uses real-time event functionality to communicate reaction interactions. 
The exact persistence, reaction counts, and retention behavior should be verified against 
backend implementation. 
 
27. Host Role 
The Host is the creator or controlling participant of the Wave. 
The frontend identifies Host-level functionality involving participant and room management. 
Potential Host actions include: 
●​ Approving speaker requests 

●​ Managing participant audio permissions 
●​ Muting participants 
●​ Blocking participants 
●​ Ending a Wave 
●​ Managing speakers 
●​ Managing room permissions 
The exact authorization must be enforced and confirmed by the backend. 
 
28. Co-Host Role 
The frontend defines a CO_HOST participant role. 
However, the exact difference between: 
HOST 
and 
CO_HOST 
requires backend and product confirmation. 
The AI must not invent Co-Host privileges. 
Until confirmed, the safe response is: 
“WiseIN supports a Co-Host role in Waves, but I don't have confirmed information 
about the complete set of Co-Host permissions.” 
 
29. Participant Roles 
The inspected frontend identifies the following participant roles: 
Role 
General Function 
HOST 
Controls the Wave and manages participants 
CO_HOST 
Elevated participant role; exact permissions pending confirmation 

SPEAKER 
Can transmit audio when permitted 
LISTENER 
Can listen and request speaker access 
The frontend role definitions should be treated as implementation evidence; backend 
authorization requires separate confirmation. 
 
30. Host Moderation 
Host moderation functionality identified in the frontend includes: 
Mute 
The host can mute a participant. 
Block 
The host can remove/block a participant according to the implemented moderation flow. 
Speaker Approval 
The host can approve a Listener's request to speak. 
End Wave 
The host can end the active session. 
Important 
Frontend availability of a moderation control does not independently prove that backend 
authorization is secure against unauthorized API requests. 
Engineering should verify all moderation endpoints server-side. 
 
31. Ending a Wave 
The Host can end the Wave. 

Expected Workflow 
1.​ Host opens the active Wave. 
2.​ Host selects the end/leave control. 
3.​ The end action is confirmed if confirmation is required. 
4.​ The Wave session ends. 
5.​ Participants are disconnected from the live session. 
6.​ The Wave transitions to its completed/ended state according to backend behavior. 
Exact post-session behavior requires live and backend verification. 
 
32. Leaving a Wave 
A participant can leave an active Wave. 
Workflow 
1.​ Select the Leave control. 
2.​ Leave the live audio session. 
3.​ Audio connection is disconnected. 
4.​ The participant is returned to the appropriate Waves interface. 
The frontend references a leave operation for participant state handling. 
 
33. Sharing a Wave 
Wave Cards contain a Share action. 
The inspected frontend indicates that sharing can use: 
●​ Native browser/device sharing where available 
●​ Clipboard link copying as a fallback 
The exact shared URL format should be verified during QA. 
 

34. Set Reminder 
Scheduled Waves can display a Set Reminder action. 
The frontend references a reminder operation. 
Pending Verification 
The following must be confirmed: 
●​ Reminder storage 
●​ Reminder delivery 
●​ Push notifications 
●​ Email notifications 
●​ Reminder cancellation 
●​ Duplicate reminder behavior 
●​ Notification timing 
The presence of the reminder UI should not be treated as confirmation that notifications are 
successfully delivered in production. 
 
35. Wave Statuses 
The inspected frontend identifies Wave statuses including: 
●​ SCHEDULED 
●​ LIVE 
●​ ENDED 
●​ CANCELLED 
The exact lifecycle transitions and backend rules should be confirmed. 
For example: 
SCHEDULED → LIVE → ENDED 
may represent the normal lifecycle, but cancellation and other transitions require 
product/backend confirmation. 
 

36. API and Backend References 
The following API endpoints were identified from frontend request definitions. 
Important: These represent endpoints referenced by the frontend. They should not be treated 
as complete backend API documentation until the backend is inspected and verified. 
Endpoint 
Method 
Frontend-Referenced Purpose 
/waves 
GET 
Retrieve Waves with filtering/pagination 
parameters 
/waves/live 
GET 
Retrieve active/live Waves 
/waves/trending 
GET 
Retrieve trending Waves 
/waves 
POST 
Create a Wave 
/waves/{id}/join 
POST 
Join a Wave 
/waves/{id}/leave 
POST 
Leave a Wave 
/waves/{id}/end 
POST 
End a Wave 
/waves/{id}/raise-hand 
POST 
Request speaker access 
/waves/speaker-request/a
pprove 
POST 
Approve speaker request 
/waves/{id}/mute/{userId
}/mute 
POST 
Host mute action 
/waves/{id}/reminder 
POST 
Set reminder 
/waves/toggle 
POST 
Toggle Wave reaction 
These endpoint references were extracted from the frontend implementation. Backend behavior 
and authorization remain subject to Engineering verification. 
 
37. API Security Requirements 

Every Wave-related backend endpoint should enforce authorization independently of the 
frontend. 
Examples: 
Host Actions 
A normal Listener should not be able to directly invoke Host-only operations. 
Speaker Approval 
Only an authorized Host/eligible moderator should be able to approve speaker requests. 
Mute 
Only authorized roles should be able to mute participants. 
End Wave 
Only authorized users should be able to terminate a Wave. 
Private Wave 
Access restrictions must be enforced server-side. 
Important Security Rule 
Hiding a frontend button is not sufficient authorization. 
Backend APIs must independently validate identity, role, Wave membership, and permission. 
 
38. Loading States 
The frontend includes loading states for Wave discovery. 
A WaveCardSkeleton is displayed while Wave data is being fetched. 
QA Should Verify 
●​ Skeleton appears during loading 
●​ Skeleton disappears after successful response 

●​ Skeleton disappears after failed response 
●​ Loading does not remain indefinitely 
●​ Switching tabs does not leave stale loading indicators 
 
39. Empty State 
When no Waves are returned, the frontend displays: 
“No waves found” 
along with a microphone-related visual. 
The interface also provides messaging encouraging users to start a Wave. 
QA Should Verify 
●​ Empty state appears correctly 
●​ Search with no matches produces an appropriate empty state 
●​ Correct tab is maintained 
●​ Empty state does not appear incorrectly during loading 
 
40. Error Handling 
The frontend contains error handling around Wave operations. 
Examples identified during code analysis include errors related to: 
●​ Joining a room 
●​ Microphone access 
●​ Speaker permissions 
●​ Missing room credentials 
●​ Audio initialization 
However, exact error messages should be confirmed through live testing because frontend 
fallback messages can differ depending on the backend error response. 
 

41. Troubleshooting — Cannot Speak 
Problem 
The user cannot speak in a Wave. 
Possible Cause 1: User Is a Listener 
The user may not yet have Speaker permission. 
Solution 
1.​ Ask the user to check their current role. 
2.​ If they are a Listener, select Raise Hand. 
3.​ Wait for the Host to approve the request. 
4.​ After approval, enable the microphone. 
 
Possible Cause 2: Microphone Permission 
The browser may be blocking microphone access. 
Solution 
1.​ Open the browser permission controls. 
2.​ Find the microphone permission for WiseIN. 
3.​ Set it to Allow. 
4.​ Refresh/rejoin if required. 
5.​ Try the microphone again. 
The frontend documentation specifically associates microphone failures with browser 
permission and participant role conditions. 
 
42. Troubleshooting — Wave Will Not 
Connect 
Possible Causes 

●​ Network instability 
●​ Audio service initialization failure 
●​ Authentication/session problem 
●​ Backend failure 
●​ GetStream connection issue 
Recommended Steps 
1.​ Check the user's internet connection. 
2.​ Leave the Wave. 
3.​ Reopen the Wave. 
4.​ Try joining again. 
5.​ If the issue persists, capture the exact error message. 
6.​ Escalate if repeated attempts fail. 
Do not instruct users to manually call undocumented API endpoints. 
 
43. Troubleshooting — Microphone 
Permission Denied 
User Guidance 
Ask the user to: 
1.​ Check browser microphone permissions. 
2.​ Allow microphone access for WiseIN. 
3.​ Check operating-system microphone permissions. 
4.​ Ensure another application is not exclusively using the microphone. 
5.​ Rejoin the Wave if required. 
6.​ Test the microphone again. 
If the microphone remains unavailable after permissions are correctly configured, escalate the 
issue. 
 
44. Troubleshooting — User Cannot Join 
Check: 

1.​ Is the user logged in? 
2.​ Is the Wave still active? 
3.​ Is the Wave restricted? 
4.​ Does the user have permission to access it? 
5.​ Is the user's network connection stable? 
6.​ Is there an error message? 
7.​ Does the problem occur with other Waves? 
If the issue appears to affect multiple users or multiple Waves, escalate to Engineering. 
 
45. Troubleshooting — Chat Not Updating 
Because the inspected implementation uses periodic polling for incoming chat messages, 
messages may not necessarily appear instantaneously. 
Recommended Steps 
1.​ Wait briefly for the chat to refresh. 
2.​ Check network connectivity. 
3.​ Reopen/rejoin the Wave if appropriate. 
4.​ Determine whether the problem affects one user or multiple users. 
5.​ Capture the time and Wave ID. 
6.​ Escalate persistent failures. 
The frontend implementation identifies a 3-second polling interval for chat retrieval. 
 
46. Privacy and Security 
Waves involve real-time audio communication and participant information. 
Important areas requiring appropriate protection include: 
●​ User identity 
●​ Audio communication 
●​ Participant roles 
●​ Chat messages 
●​ Wave visibility 
●​ Speaker permissions 

●​ Moderation information 
●​ Authentication credentials 
●​ Session information 
 
47. Audio Recording 
The inspected frontend does not establish that Waves are recorded automatically. 
There is no confirmed frontend recording indicator identified in the analyzed implementation. 
Therefore: 
The AI must not tell users that every Wave is recorded, stored, or transcribed. 
Recording, retention, transcription, and deletion policies require explicit confirmation from 
WiseIN Product, Engineering, and Security teams. 
This is specifically identified as a pending area in the reference documentation. 
 
48. Chat Data and Retention 
The frontend indicates that Wave chat messages are retrieved through the application API. 
However, the following require backend/security confirmation: 
●​ Where messages are stored 
●​ How long messages are retained 
●​ Whether messages are encrypted at rest 
●​ Whether deleted Waves remove associated messages 
●​ Who can access historical chat 
●​ Whether administrators can access chat 
●​ Whether chat is included in user data exports 
The AI must not invent retention periods. 
 

49. Platform Differences 
49.1 Desktop Web 
The inspected implementation is primarily based on the WiseIN web React frontend. 
Desktop behavior should be tested for: 
●​ Navigation 
●​ Wave cards 
●​ Creation modal 
●​ Live room 
●​ Audio controls 
●​ Chat 
●​ Sidebar 
●​ Sharing 
●​ Scheduling 
 
49.2 Mobile Web 
Responsive behavior should be verified separately. 
QA should test: 
●​ Small-screen layout 
●​ Wave cards 
●​ Start Wave interface 
●​ Live room controls 
●​ Chat 
●​ Microphone controls 
●​ Host controls 
●​ Sidebar behavior 
●​ Horizontal scrolling 
●​ Modal usability 
 
49.3 Native Mobile Applications 
Native Android/iOS behavior is not confirmed by this frontend analysis. 

Native application documentation should be created or updated after inspecting the 
corresponding mobile codebase or live applications. 
 
50. Accessibility Considerations 
QA should verify: 
●​ Keyboard navigation 
●​ Focus states 
●​ Button labels 
●​ Screen-reader compatibility 
●​ Color contrast 
●​ Icon meaning 
●​ Accessible modal behavior 
●​ Microphone control labeling 
●​ Raise Hand accessibility 
●​ Chat accessibility 
●​ Error-message accessibility 
Accessibility behavior should be confirmed through dedicated QA testing. 
 
51. QA Test Cases 
The following test cases should be executed against a staging or approved testing environment. 
Test ID 
Test Scenario 
Preconditions 
Expected Result 
Status 
WAV-0
01 
Open Waves 
Logged-in user 
Waves page loads 
successfully 
Not 
Tested 
WAV-0
02 
View For You 
Waves available 
Appropriate Wave list 
appears 
Not 
Tested 
WAV-0
03 
View Discover 
Waves available 
Discover list loads 
Not 
Tested 

WAV-0
04 
View Trending 
Trending data 
available 
Trending Waves load 
Not 
Tested 
WAV-0
05 
View Following 
Followed accounts 
exist 
Following Waves load 
Not 
Tested 
WAV-0
06 
View Completed 
Completed Waves 
exist 
Completed Waves load 
Not 
Tested 
WAV-0
07 
Search Wave 
Waves available 
Matching Waves are 
displayed 
Not 
Tested 
WAV-0
08 
Search No Results 
Search term has no 
match 
Empty state displayed 
Not 
Tested 
WAV-0
09 
Start Instant Wave 
Logged-in user 
Creation interface opens 
Not 
Tested 
WAV-0
10 
Create Instant Wave 
Valid Wave data 
Wave is created 
Not 
Tested 
WAV-0
11 
Create Wave With 
Invalid Title 
Invalid input 
Appropriate validation 
shown 
Not 
Tested 
WAV-0
12 
Schedule Wave 
Valid future 
date/time 
Wave is scheduled 
Not 
Tested 
WAV-0
13 
Set Reminder 
Scheduled Wave 
exists 
Reminder action completes 
appropriately 
Not 
Tested 
WAV-0
14 
Join Live Wave 
Live Wave available User enters room 
Not 
Tested 
WAV-0
15 
Join Restricted 
Wave 
Restricted Wave 
Access follows configured 
permission 
Not 
Tested 
WAV-0
16 
Listener Audio 
User is Listener 
User can hear permitted 
audio 
Not 
Tested 
WAV-0
17 
Raise Hand 
User is Listener 
Speaker request is 
submitted 
Not 
Tested 
WAV-0
18 
Approve Speaker 
Host + pending 
request 
Speaker access granted 
Not 
Tested 
WAV-0
19 
Enable Microphone 
Speaker + 
permission 
User can transmit audio 
Not 
Tested 

WAV-0
20 
Deny Microphone 
Browser blocks mic 
Appropriate guidance/error 
shown 
Not 
Tested 
WAV-0
21 
Mute Participant 
Authorized Host 
Participant audio is muted 
Not 
Tested 
WAV-0
22 
Unauthorized Mute 
Listener 
Action rejected 
Not 
Tested 
WAV-0
23 
Block Participant 
Authorized Host 
Moderation action executes 
Not 
Tested 
WAV-0
24 
End Wave 
Host 
Wave ends correctly 
Not 
Tested 
WAV-0
25 
Leave Wave 
Participant 
User leaves room 
Not 
Tested 
WAV-0
26 
Send Chat 
Chat permission 
available 
Message is sent 
Not 
Tested 
WAV-0
27 
Receive Chat 
Another user sends 
message 
Message appears 
Not 
Tested 
WAV-0
28 
Send Reaction 
User inside Wave 
Reaction is displayed 
Not 
Tested 
WAV-0
29 
Share Wave 
Wave available 
Share/copy action works 
Not 
Tested 
WAV-0
30 
Empty State 
No matching 
Waves 
“No waves found” appears 
Not 
Tested 
WAV-0
31 
Loading State 
Slow response 
Skeleton/loading state 
appears 
Not 
Tested 
WAV-0
32 
Join Failure 
Simulated service 
failure 
User receives appropriate 
error 
Not 
Tested 
WAV-0
33 
Network Disconnect 
Active Wave 
Connection behavior is 
handled 
Not 
Tested 
WAV-0
34 
Reconnect 
Connection 
restored 
User can recover/rejoin 
appropriately 
Not 
Tested 
WAV-0
35 
Mobile Web 
Mobile browser 
Layout remains usable 
Not 
Tested 

WAV-0
36 
Keyboard 
Navigation 
Desktop 
Controls accessible by 
keyboard 
Not 
Tested 
WAV-0
37 
Permission 
Enforcement 
Different user roles 
Unauthorized actions are 
rejected server-side 
Not 
Tested 
WAV-0
38 
Private Wave 
Restricted user 
Access is correctly restricted Not 
Tested 
WAV-0
39 
Chat Permission 
Restricted chat 
Unauthorized chat is 
blocked 
Not 
Tested 
WAV-0
40 
Host Controls 
Host account 
Host controls are available 
Not 
Tested 
 
52. Security QA Test Cases 
Additional security testing should verify: 
WAV-SEC-001 — Unauthorized Host Action 
Attempt a Host-only action using a non-Host account. 
Expected: Backend rejects the request. 
WAV-SEC-002 — Private Wave Access 
Attempt to access a Private Wave without authorization. 
Expected: Backend denies access. 
WAV-SEC-003 — Unauthorized Speaker Access 
Attempt to transmit audio without Speaker permission. 
Expected: Audio transmission is denied. 
WAV-SEC-004 — Unauthorized Participant Mutation 
Attempt to mute/block another participant without authorization. 
Expected: Backend rejects the action. 

WAV-SEC-005 — Direct API Access 
Attempt restricted Wave actions without appropriate authentication. 
Expected: Request is rejected. 
 
53. AI Customer-Support Guidance 
The WiseIN AI chatbot may use this document to answer questions related to Waves. 
The AI can explain: 
●​ What Waves are 
●​ How to access Waves 
●​ How to discover Waves 
●​ How to search Waves 
●​ How to create a Wave 
●​ How to schedule a Wave 
●​ How to join a Wave 
●​ How Raise Hand works 
●​ Listener vs Speaker behavior 
●​ Basic microphone troubleshooting 
●​ Basic chat and reaction functionality 
●​ General Host controls 
●​ Known limitations 
 
54. AI Must Not Invent 
The AI must not invent or assume: 
●​ Maximum Wave participants 
●​ Recording policy 
●​ Transcription availability 
●​ Audio retention period 
●​ Chat retention period 
●​ Notification guarantees 
●​ Subscription restrictions 
●​ Exact Co-Host permissions 

●​ Backend authorization behavior 
●​ Unsupported mobile features 
●​ Unconfirmed error codes 
●​ Unconfirmed cancellation rules 
●​ Hidden administrative controls 
●​ Internal GetStream credentials 
●​ API credentials 
●​ Private user information 
 
55. AI Response Rules for Waves 
Rule 1 — Use Approved Knowledge 
Answer from the latest approved Waves documentation. 
Rule 2 — Distinguish Confirmed and Pending Information 
If functionality is still under verification, say so. 
Rule 3 — Never Request Sensitive Information 
The chatbot must not ask users for: 
●​ Passwords 
●​ OTPs 
●​ Authentication tokens 
●​ API keys 
●​ Private credentials 
Rule 4 — Do Not Claim Backend Actions 
The AI must not claim: 
“I have enabled your microphone.” 
unless an authorized tool actually performs that action. 
Rule 5 — Escalate Unresolved Problems 
Persistent technical issues should be escalated to human support. 

 
56. Sample AI Response — What Are 
Waves? 
Waves are WiseIN's real-time audio rooms where users can participate in live 
professional conversations. Depending on their permissions, users can 
listen, request to speak, participate in chat, and send reactions. Hosts can 
manage participants and control the room. 
 
57. Sample AI Response — How Do I 
Speak? 
If you're currently a Listener, use the Raise Hand option to request 
permission to speak. The Host needs to approve your request. Once you're 
granted Speaker access, you can enable your microphone. If your 
microphone still doesn't work, check that your browser has permission to use 
your microphone. 
 
58. Sample AI Response — My 
Microphone Isn't Working 
First, check whether you have Speaker access. If you're a Listener, use Raise 
Hand and wait for the Host to approve your request. If you're already a 
Speaker, check your browser's microphone permission for WiseIN and make 
sure microphone access is allowed. If the problem continues after permission 
is enabled, I can help you troubleshoot further or guide you to support. 
 

59. Sample AI Response — Are Waves 
Recorded? 
I don't have confirmed information that WiseIN automatically records Waves. 
The current documentation does not confirm Wave recording or transcription 
behavior. Please contact WiseIN Support if you need confirmation about 
recording or data-retention policies. 
This response is important because recording behavior is explicitly pending verification. 
 
60. Human Support Escalation 
The AI should escalate when: 
●​ The user repeatedly cannot join Waves. 
●​ Audio repeatedly disconnects. 
●​ Microphone permissions are correct but audio still fails. 
●​ Multiple users experience the same Wave problem. 
●​ A Host cannot end a Wave. 
●​ Speaker permissions appear incorrect. 
●​ Private Wave access behaves incorrectly. 
●​ Moderation controls fail. 
●​ Chat repeatedly fails. 
●​ A security/privacy issue is reported. 
●​ A user reports harassment or serious abuse. 
●​ The user needs account-specific investigation. 
●​ The AI cannot confidently answer the question from approved documentation. 
 
61. Information Required for Escalation 
Where appropriate and permitted by WiseIN support procedures, collect: 
●​ Module: Waves 
●​ Wave ID 
●​ Wave title 
●​ User's role 

●​ Host username 
●​ Approximate date/time 
●​ Device 
●​ Browser/app version 
●​ Network condition 
●​ Action being performed 
●​ Expected result 
●​ Actual result 
●​ Exact error message 
●​ Screenshot, if permitted 
●​ Whether the issue is reproducible 
●​ Whether the issue affects other Waves 
Security Rule 
Do not request: 
●​ Password 
●​ OTP 
●​ Authentication token 
●​ API key 
●​ Unnecessary identity documents 
 
62. Known Limitations 
Based on the inspected frontend implementation, the following areas require additional 
verification: 
1.​ Maximum participant capacity 
2.​ Recording functionality 
3.​ Transcription functionality 
4.​ Audio retention 
5.​ Chat retention 
6.​ Push notifications 
7.​ Email notifications 
8.​ Scheduled Wave lifecycle 
9.​ Exact Co-Host permissions 
10.​Subscription restrictions 
11.​Backend authorization 
12.​Private Wave enforcement 
13.​Mobile application behavior 

14.​Mobile responsive behavior 
15.​Reporting functionality 
16.​Abuse-management workflow 
17.​Completed Wave retention 
18.​Reminder delivery 
19.​Rejoin behavior 
20.​Backend data deletion 
These items must not be converted into confirmed product facts until the responsible team 
verifies them. 
 
63. Open Questions for WiseIN Product 
and Engineering 
Product 
1.​ What is the maximum number of participants allowed in a Wave? 
2.​ Are Waves recorded? 
3.​ Are Waves transcribed? 
4.​ Are recordings available to users? 
5.​ How long are completed Waves retained? 
6.​ What happens when a scheduled Wave is never started? 
7.​ Are reminders delivered through push notifications? 
8.​ Are email notifications supported? 
9.​ Are there subscription restrictions for creating Waves? 
10.​What exactly differentiates Co-Host from Host? 
Engineering 
11.​Are all Wave permissions enforced server-side? 
12.​Are Private Wave restrictions enforced through backend authorization? 
13.​Is the chat polling mechanism intended to remain at the current interval? 
14.​What is the exact reconnect/rejoin mechanism? 
15.​What happens when GetStream authentication fails? 
16.​What data is stored in WiseIN versus GetStream? 
17.​What data is deleted when a Wave is permanently deleted? 
Security 
18.​How is Wave audio protected? 

19.​Is Wave chat encrypted at rest? 
20.​What are the retention and deletion policies? 
21.​Can administrators access Wave chat? 
22.​What privacy controls apply to Wave participation? 
QA 
23.​Which browsers are officially supported? 
24.​Which mobile browsers are supported? 
25.​What happens under poor network conditions? 
26.​What is the expected behavior after a connection interruption? 
 
64. Related Documentation 
The Waves document should be connected with the following WiseIN documentation: 
Authentication 
●​ WiseIN User Registration Documentation 
●​ WiseIN Login Documentation 
●​ WiseIN Email Verification Documentation 
●​ WiseIN Identity Verification Documentation 
●​ WiseIN Account Security Documentation 
Product 
●​ WiseIN Application Overview 
●​ WiseIN Explore Documentation 
●​ WiseIN Regular Search Documentation 
●​ WiseIN Topics Documentation 
●​ WiseIN Jobs Documentation 
●​ WiseIN Meetings Documentation 
●​ WiseIN Chat Documentation 
●​ WiseIN Events Documentation 
●​ WiseIN Profile Documentation 
●​ WiseIN Notifications Documentation 
Support 
●​ WiseIN Customer Support Documentation 
●​ WiseIN Privacy & Safety Documentation 

●​ WiseIN AI Customer Support Documentation 
 
65. Source and Verification Register 
Information 
Source 
Status 
Waves route 
src/app/(ui)/waves/page.tsx 
Frontend Confirmed 
Wave components 
Waves component files 
Frontend Confirmed 
Wave hooks 
src/hooks/waves/useWaves.ts 
Frontend Confirmed 
Participant roles 
src/types/waves.ts 
Frontend Confirmed 
GetStream integration 
LiveRoomView / SDK imports 
Frontend Confirmed 
Wave tabs 
Waves UI implementation 
Frontend Confirmed 
Wave search 
Waves UI implementation 
Frontend Confirmed 
Wave creation UI 
CreateAudioRoomModal / 
AudioRoomForm 
Frontend Confirmed 
Scheduling UI 
ScheduleRoomSheet 
Frontend Confirmed 
Visibility values 
Wave type definitions/UI 
Frontend Confirmed 
Chat controls 
Wave type definitions/UI 
Frontend Confirmed 
Raise Hand 
Live room implementation 
Frontend Confirmed 
Host controls 
Live room implementation 
Frontend Confirmed 
Chat polling 
useWaves.ts 
Frontend Confirmed 
API endpoint 
references 
Frontend API calls 
Frontend 
Referenced 
Backend authorization 
Backend 
Pending 
Maximum participants 
Backend/configuration 
Pending 
Recording 
Backend/Product 
Pending 

Transcription 
Backend/Product 
Pending 
Push notifications 
Backend/Notification system 
Pending 
Chat retention 
Backend/Security 
Pending 
Audio retention 
Backend/Security/GetStream configuration Pending 
Mobile native behavior 
Mobile implementation 
Pending 
The reference analysis explicitly distinguishes frontend implementation evidence from areas 
requiring backend confirmation. 
 
66. AI/RAG Knowledge Base 
Requirements 
This document is intended to become part of the WiseIN AI customer-support knowledge base. 
The ingestion system should preserve the distinction between: 
CONFIRMED-FRONTEND 
Functionality directly identified in the inspected frontend implementation. 
OBSERVED-LIVE 
Behavior confirmed through actual live application testing. 
BACKEND-CONFIRMED 
Behavior verified against backend implementation or API behavior. 
PRODUCT-CONFIRMED 
Behavior explicitly approved by WiseIN Product. 
PENDING-VERIFICATION 
Information that still requires confirmation. 

DEPRECATED 
Information that was previously valid but is no longer applicable. 
 
67. RAG Chunking Recommendations 
The Waves document should be divided into independent knowledge chunks. 
Recommended chunks: 
1.​ What are Waves? 
2.​ How to access Waves 
3.​ Waves tabs 
4.​ Wave search 
5.​ Wave cards 
6.​ How to create a Wave 
7.​ How to schedule a Wave 
8.​ Wave visibility 
9.​ Chat permissions 
10.​How to join a Wave 
11.​Listener role 
12.​Raise Hand 
13.​Speaker role 
14.​Microphone troubleshooting 
15.​Host controls 
16.​Chat 
17.​Reactions 
18.​Leaving a Wave 
19.​Ending a Wave 
20.​Troubleshooting 
21.​Privacy 
22.​Recording policy 
23.​Notifications 
24.​Human support escalation 
 
68. RAG Metadata 
Recommended metadata: 

document_id: WISEIN-WAV-018 
module: Waves 
version: 1.0 
status: draft 
source: frontend-code-analysis 
platform: web 
knowledge_type: product-documentation 
verification_status: mixed 
prepared_by: MSR 
last_updated: 17-09-2026 
Each knowledge chunk should additionally identify whether the information is: 
confirmed_frontend 
observed_live 
backend_confirmed 
product_confirmed 
pending_verification 
deprecated 
 
69. Hallucination Prevention Rules 
The Waves knowledge base must prevent the AI from making unsupported claims. 
Example 
If a user asks: 
“How many people can join a Wave?” 
The AI should not invent a number. 
Correct response: 
“I don't have a confirmed participant limit for Waves in the current documentation.” 
 
If the user asks: 
“Are Waves recorded?” 
The AI should not say yes or no unless Product/Security has confirmed the policy. 

Correct response: 
“Wave recording is not confirmed in my current documentation. Please contact 
WiseIN Support for the current recording and retention policy.” 
 
If the user asks: 
“Why was I not allowed to speak?” 
The AI can explain the documented Listener → Raise Hand → Host Approval → Speaker 
workflow. 
It should not claim to know the user's specific account or role unless an authorized system 
provides that information. 
 
70. Documentation Maintenance 
This document must be updated whenever there are significant changes to: 
●​ Wave UI 
●​ Wave creation 
●​ Scheduling 
●​ Wave permissions 
●​ Participant roles 
●​ Audio provider 
●​ Chat architecture 
●​ Reactions 
●​ API endpoints 
●​ Moderation 
●​ Notifications 
●​ Recording 
●​ Data retention 
●​ Mobile support 
Every update should include: 
●​ Version number 
●​ Date 
●​ Author 
●​ Change description 

●​ Verification status 
 
71. Version History 
Versio
n 
Date 
Author 
Changes 
Status 
1.0 
17 Sep 
2026 
MSR 
Initial Waves documentation based on 
frontend implementation analysis 
Draft — Pending 
Review 
 
72. Documentation Completion Checklist 
General 
●​ Waves overview documented 
●​ Purpose documented 
●​ Access route documented 
●​ UI documented 
●​ Tabs documented 
●​ Search documented 
●​ Wave cards documented 
Creation 
●​ Instant Wave workflow documented 
●​ Scheduled Wave workflow documented 
●​ Duration documented 
●​ Category documented 
●​ Visibility documented 
●​ Chat permissions documented 
Live Room 
●​ Joining documented 
●​ Listener role documented 
●​ Raise Hand documented 
●​ Speaker role documented 
●​ Microphone documented 

●​ Chat documented 
●​ Reactions documented 
●​ Host controls documented 
●​ Leaving documented 
●​ Ending documented 
Technical 
●​ Frontend components identified 
●​ Routes identified 
●​ API references identified 
●​ Roles identified 
●​ Loading states documented 
●​ Empty states documented 
●​ Error states documented 
Support 
●​ Troubleshooting documented 
●​ AI guidance documented 
●​ Escalation rules documented 
●​ Sensitive information rules documented 
QA 
●​ Functional test cases created 
●​ Permission test cases created 
●​ Security test cases created 
●​ Mobile testing identified 
●​ Accessibility testing identified 
RAG 
●​ Knowledge chunks defined 
●​ Verification states defined 
●​ Metadata defined 
●​ Hallucination controls defined 
●​ Pending information identified 
 
73. Final Documentation Status 

Document: WISEIN-WAV-018​
 Module: Waves​
 Version: 1.0​
 Current Status: Draft — Pending Cross-Functional Review 
Frontend Documentation 
Status: Documented 
Backend Authorization 
Status: Pending Verification 
Product Rules 
Status: Partially Confirmed / Pending Verification 
QA 
Status: Test Cases Prepared — Execution Pending 
Security 
Status: Review Required 
Mobile 
Status: Pending Verification 
AI/RAG 
Status: Ready for controlled ingestion after approval 
 
74. Final Notes 
This document should be treated as the Waves knowledge baseline, but not every statement 
has the same verification level. 
The most important rule for the WiseIN AI chatbot is: 

Frontend implementation confirms what the application is designed to do; 
backend, Product, Security, and live QA verification determine what WiseIN 
officially guarantees. 
The current source analysis confirms the existence of the Waves frontend architecture, Wave 
discovery, creation/scheduling interfaces, live-room interactions, participant roles, 
chat/reactions, and multiple Wave-related API references. Backend authorization, retention, 
notification, recording, capacity, and several policy-level behaviors remain areas for 
confirmation. 
Recommended next step: Engineering should verify the backend authorization and lifecycle 
behavior, QA should execute the WAV test suite, and Product/Security should confirm recording, 
retention, notification, privacy, and participant-limit policies before this document is marked 
Approved for Production RAG. 
 



---

## Source: _WISEIN WAVES DOCUMENTATION018.pdf

DOCUMENT 018 — WISEIN WAVES 
DOCUMENTATION 
Document ID: WISEIN-WAV-018​
 Module: Waves​
 Category: Real-Time Audio, Social Networking & Professional Communication​
 Version: 1.0​
 Status: Draft — Pending Product, Engineering, QA, Security & Support Approval​
 Prepared By: MSR​
 Date: 17 September 2026​
 Document Type: Internal Product & AI Knowledge Base Documentation​
 Primary Platform Reviewed: WiseIN Web Application​
 Source: WiseIN frontend codebase analysis and product observation 
 
1. Document Purpose 
This document provides complete functional and operational documentation for the Waves 
module in WiseIN. 
The purpose of this document is to provide a reliable reference for: 
●​ WiseIN users 
●​ Customer-support teams 
●​ QA teams 
●​ Product teams 
●​ Engineering teams 
●​ Documentation teams 
●​ AI customer-support systems 
●​ RAG/knowledge-base systems 
The document explains how users discover, create, schedule, join, participate in, moderate, and 
leave Waves. 
It also documents known UI behavior, user roles, troubleshooting procedures, security 
considerations, QA scenarios, and information that still requires confirmation. 
 

2. What Are Waves? 
Waves are real-time audio rooms within WiseIN that allow users to participate in live 
professional conversations. 
A Wave provides an audio-first environment where participants can: 
●​ Listen to live conversations 
●​ Speak when they have the required permission 
●​ Request permission to speak 
●​ Participate in text chat 
●​ Send reactions 
●​ Interact with the host and other participants 
Hosts can manage the live room and participant permissions. 
The inspected WiseIN frontend integrates the Waves experience with GetStream's real-time 
communication SDK. 
 
3. Purpose of Waves 
The Waves module provides a real-time communication environment for professional and 
community interaction. 
Possible uses include: 
●​ Professional discussions 
●​ Founder conversations 
●​ Business discussions 
●​ Career discussions 
●​ Community conversations 
●​ Topic-based discussions 
●​ Interactive audio sessions 
●​ Networking conversations 
The exact official use cases and supported categories should be maintained according to the 
current WiseIN Product documentation. 
 

4. Waves Technology Overview 
The inspected WiseIN frontend contains a dedicated Waves implementation. 
Relevant frontend components include: 
●​ WavesCenterSection 
●​ WavesRightSidebar 
●​ WavesList 
●​ WaveCard 
●​ CreateAudioRoomModal 
●​ AudioRoomForm 
●​ LiveRoomView 
●​ RoomPermissionsSheet 
●​ ScheduleRoomSheet 
●​ SpeakersPicker 
Related implementation files include: 
src/app/(ui)/waves/page.tsx 
src/hooks/waves/useWaves.ts 
src/types/waves.ts 
Real-Time Communication 
The frontend uses: 
@stream-io/video-react-sdk 
for the real-time communication experience. 
Verification Status: Frontend implementation confirmed. Backend configuration and production 
authorization require separate verification. 
 
5. Accessing Waves 
5.1 Main Navigation 
Users can access Waves from the main WiseIN navigation. 

Main Route 
/waves 
 
5.2 Individual Wave 
An individual Wave can be accessed through a Wave-specific route. 
Route Pattern 
/waves/[id] 
The [id] represents the unique identifier of the Wave. 
 
6. Waves Main Interface 
The Waves interface provides users with a central discovery area where available Waves are 
displayed. 
The interface contains: 
●​ Navigation tabs 
●​ Search 
●​ Wave cards 
●​ Wave status indicators 
●​ Participant information 
●​ Join actions 
●​ Reminder actions 
●​ Sharing actions 
●​ Start a Wave functionality 
The exact layout may change as the WiseIN interface evolves. 
 
7. Waves Navigation Tabs 
The inspected implementation contains the following Waves tabs: 
1.​ For You 

2.​ Discover 
3.​ Trending 
4.​ Following 
5.​ Completed 
 
7.1 For You 
The For You section is intended to provide a personalized selection of Waves. 
The exact recommendation and personalization logic is not established from frontend inspection 
alone. 
Status: UI confirmed; recommendation logic pending verification. 
 
7.2 Discover 
The Discover section provides a general discovery experience for available Waves. 
Users can browse Waves and identify conversations that may be relevant to them. 
 
7.3 Trending 
The Trending section is intended to display Waves considered trending or popular. 
The exact ranking criteria are not confirmed. 
Possible ranking inputs may include activity or participation, but the AI must not state these as 
official rules unless Product confirms them. 
 
7.4 Following 
The Following section is intended to display Waves associated with accounts or entities the 
user follows. 
The exact backend filtering logic requires confirmation. 

 
7.5 Completed 
The Completed section provides access to Waves that have finished. 
The exact retention period and availability of completed Wave information require confirmation. 
 
8. Wave Search 
The Waves interface provides a search field for discovering Waves. 
Users can enter a search term to narrow the displayed results. 
The frontend implementation indicates local filtering/search behavior. 
Search Testing Should Include: 
●​ Exact title search 
●​ Partial title search 
●​ Host-name search 
●​ Category search 
●​ Uppercase/lowercase search 
●​ Empty search 
●​ No-result search 
●​ Special characters 
●​ Rapid search changes 
Important 
Frontend search behavior should not automatically be interpreted as backend/global search 
behavior. 
 
9. Wave Card 
A Wave is represented in the discovery interface through a Wave Card. 
A Wave Card may display: 

●​ Wave title 
●​ Host information 
●​ Host avatar 
●​ Category 
●​ Participant count 
●​ Live status 
●​ Scheduled status 
●​ Join Room 
●​ Set Reminder 
●​ Share 
 
10. Live Wave Status 
A currently active Wave can be identified through a LIVE indicator. 
A user can select: 
Join Room 
to enter the live session. 
The exact visual presentation of the live status may change with future UI updates. 
 
11. Scheduled Wave Status 
A future Wave can be displayed as scheduled. 
A scheduled Wave may provide: 
Set Reminder 
for users who want to be reminded about the upcoming session. 
The exact notification mechanism requires verification. 
 

12. Starting a Wave 
The Waves interface provides a: 
Start a Wave 
action. 
This opens the Wave creation interface. 
The creation experience includes configuration options for the new Wave. 
 
13. Wave Creation Information 
The Wave creation form contains configuration areas including: 
●​ Title 
●​ Category 
●​ Duration 
●​ Visibility 
●​ Chat permissions 
●​ Speakers 
●​ Start/scheduling options 
The exact required and optional fields must be verified through current product behavior. 
 
14. Creating an Immediate Wave 
A user can configure a Wave to start immediately. 
Workflow 
1.​ Open Waves. 
2.​ Select Start a Wave. 
3.​ Enter the Wave title. 
4.​ Select a category. 
5.​ Select the duration. 
6.​ Configure visibility. 

7.​ Configure chat permissions. 
8.​ Configure speakers if applicable. 
9.​ Select the immediate-start option. 
10.​Submit the Wave. 
11.​The Wave is created. 
12.​The creator enters the live Wave. 
13.​The creator acts as the Host. 
 
15. Wave Title 
The Wave creator provides a title to identify the conversation. 
The title is displayed in the Wave discovery interface and inside the room. 
QA Should Verify 
●​ Empty title 
●​ Short title 
●​ Long title 
●​ Special characters 
●​ Numbers 
●​ Duplicate titles 
●​ Unsupported characters 
Do not document a specific minimum or maximum title length unless confirmed by the 
implementation. 
 
16. Wave Category 
A Wave can be associated with a category. 
Categories help classify the conversation. 
The current frontend contains category-selection functionality. 
Important 

The complete category list should be taken from the current application rather than hard-coded 
into AI responses. 
 
17. Wave Duration 
The inspected frontend provides duration choices including: 
●​ 30 minutes 
●​ 1 hour 
●​ 2 hours 
●​ 3 hours 
These should currently be treated as frontend-defined options. 
Backend enforcement and Product policy should be verified before describing these as 
permanent platform limits. 
 
18. Wave Visibility 
The Wave creation interface provides visibility options. 
18.1 Public 
A Public Wave is intended to be broadly discoverable/accesssible according to WiseIN's access 
rules. 
18.2 Followers Only 
A Followers Only Wave applies follower-based access restrictions. 
18.3 Private 
A Private Wave is intended for restricted participation. 
Security Requirement 
The backend must independently enforce these restrictions. 

A frontend visibility selector alone must never be treated as proof of authorization. 
 
19. Wave Chat Permissions 
The Wave creation interface provides chat permission settings. 
The identified options include: 
●​ Anyone 
●​ Followers Only 
●​ Speakers Only 
These options determine who can participate in Wave chat according to the configured 
permission. 
The exact enforcement must be verified against backend authorization. 
 
20. Scheduling a Wave 
A user can configure a Wave for a future date and time. 
Scheduling Workflow 
1.​ Open Waves. 
2.​ Select Start a Wave. 
3.​ Enter Wave information. 
4.​ Configure category. 
5.​ Configure duration. 
6.​ Select visibility. 
7.​ Configure chat permissions. 
8.​ Select scheduling. 
9.​ Select the desired date. 
10.​Select the desired time. 
11.​Confirm the scheduled Wave. 
12.​The Wave is displayed as scheduled. 
 

21. Scheduled Wave Reminders 
Scheduled Waves can provide a Set Reminder option. 
The frontend contains reminder functionality. 
However, the following require confirmation: 
●​ Push notification behavior 
●​ Email notification behavior 
●​ Reminder timing 
●​ Reminder cancellation 
●​ Duplicate reminders 
●​ Reminder persistence 
●​ Notification failure handling 
The AI must not guarantee notification delivery unless Product confirms the behavior. 
 
22. Joining a Wave 
A user can join a live Wave through the Join Room action. 
Standard Workflow 
1.​ Open Waves. 
2.​ Locate a live Wave. 
3.​ Select Join Room. 
4.​ The application initializes the room. 
5.​ The user enters the Wave. 
6.​ The user receives an appropriate participant role. 
7.​ The user can interact according to that role. 
 
23. Wave Participant Roles 
The frontend identifies four participant roles: 
Role 
Description 

HOST 
Controls and manages the Wave 
CO_HOST 
Elevated participant role; exact permissions require confirmation 
SPEAKER 
Can transmit audio when permitted 
LISTENER 
Can listen and request speaker access 
Important 
These role definitions are based on the frontend implementation. 
Backend authorization must be separately verified. 
 
24. Listener 
A Listener participates in the Wave primarily by listening. 
Depending on the Wave configuration, a Listener may be able to: 
●​ Hear the conversation 
●​ View chat 
●​ Send permitted reactions 
●​ Request permission to speak 
●​ Leave the Wave 
A Listener does not automatically have permission to transmit audio. 
 
25. Requesting Permission to Speak 
Listeners can use the Raise Hand functionality to request speaking access. 
Workflow 
1.​ Join a Wave as a Listener. 
2.​ Select Raise Hand. 
3.​ The request is submitted. 
4.​ The Host receives the request. 

5.​ The Host reviews the request. 
6.​ The Host approves or rejects it according to the available controls. 
7.​ If approved, the participant receives Speaker access. 
8.​ The participant can then enable the microphone. 
 
26. Speaker 
A Speaker is a participant who has permission to transmit audio. 
After Speaker access is granted: 
1.​ The user receives the required speaking permission. 
2.​ The microphone control becomes available. 
3.​ The user enables the microphone. 
4.​ Audio can be transmitted. 
Important 
Speaker access does not necessarily mean the microphone automatically turns on. 
The user may need to explicitly enable the microphone and grant browser permission. 
 
27. Microphone Permission 
Microphone functionality requires appropriate device/browser permission. 
Possible permission states include: 
●​ Allowed 
●​ Denied 
●​ Not yet requested 
If permission is denied, the user may not be able to transmit audio. 
 
28. Microphone Troubleshooting 

If a Speaker cannot use the microphone: 
Step 1 — Verify Role 
Check whether the user is actually a Speaker. 
If the user is a Listener: 
Use Raise Hand and wait for the Host to approve the request. 
Step 2 — Check Browser Permission 
Confirm that the browser allows microphone access for WiseIN. 
Step 3 — Check Device Permission 
Verify operating-system microphone permission. 
Step 4 — Check Microphone Availability 
Confirm that: 
●​ The microphone is connected. 
●​ The correct microphone is selected. 
●​ Another application is not exclusively using it. 
Step 5 — Rejoin 
Leave and rejoin the Wave if appropriate. 
Step 6 — Escalate 
If the problem continues, collect diagnostic information and escalate to support. 
 
29. Live Wave Room 
The Live Wave Room is the main real-time interaction environment. 
The implementation contains functionality associated with: 
●​ Audio 
●​ Microphone 

●​ Participant roles 
●​ Raise Hand 
●​ Chat 
●​ Reactions 
●​ Host moderation 
The room uses the integrated real-time communication infrastructure. 
 
30. Audio Interaction 
The primary communication method in Waves is live audio. 
Participants hear audio from authorized speakers. 
Speakers can transmit audio when they have the necessary permission and microphone 
access. 
 
31. Text Chat 
Waves include text chat functionality. 
Users can send messages according to the configured chat permissions. 
The inspected frontend retrieves chat messages through periodic requests. 
The current implementation uses a 3-second polling interval for chat retrieval. 
Important 
This is an implementation detail, not a permanent product guarantee. 
 
32. Chat Permissions During a Wave 
Chat access depends on the Wave's configured permissions. 

Possible configurations include: 
Anyone 
Participants allowed by the configuration can send messages. 
Followers Only 
Access is restricted according to follower status. 
Speakers Only 
Only users with speaker permissions can send messages. 
 
33. Reactions 
The Wave experience supports reaction functionality. 
The inspected implementation includes a heart-style reaction. 
Reactions provide lightweight interaction without requiring the participant to speak. 
The exact reaction persistence and retention behavior require backend confirmation. 
 
34. Host 
The Host is the primary controller of a Wave. 
The Host can manage aspects of the live room and participants. 
The inspected implementation provides Host-oriented controls associated with: 
●​ Speaker requests 
●​ Participant audio 
●​ Participant moderation 
●​ Wave lifecycle 
 

35. Host — Speaker Management 
A Host can review speaker requests. 
Workflow 
1.​ Listener raises their hand. 
2.​ Request appears to the Host. 
3.​ Host reviews the request. 
4.​ Host approves the request if appropriate. 
5.​ User receives Speaker access. 
6.​ User can enable the microphone. 
 
36. Host — Mute 
The frontend includes functionality for muting participants. 
The Host can use the relevant moderation control when authorized. 
Security Requirement 
The backend must verify that the requester has permission to perform the mute operation. 
 
37. Host — Participant Blocking 
The frontend includes participant blocking functionality. 
Blocking behavior should be verified against the current backend and Product rules. 
The AI should not claim specific consequences of blocking unless those consequences are 
documented and approved. 
 
38. Host — Ending a Wave 

The Host can end the active Wave. 
Workflow 
1.​ Host opens the active Wave. 
2.​ Host selects the end control. 
3.​ Confirmation is performed if required. 
4.​ The Wave ends. 
5.​ Participants leave the active session. 
6.​ The Wave transitions to its completed/ended state. 
The exact post-session behavior requires verification. 
 
39. Leaving a Wave 
Any participant can leave a Wave according to the available controls. 
Workflow 
1.​ Select the Leave control. 
2.​ The user exits the live session. 
3.​ Audio participation ends. 
4.​ The user returns to the appropriate WiseIN interface. 
 
40. Wave Lifecycle 
The frontend identifies Wave states including: 
●​ Scheduled 
●​ Live 
●​ Ended 
●​ Cancelled 
A typical lifecycle may be: 
Scheduled 
    ↓ 
Live 

    ↓ 
Ended 
A Wave may also be cancelled according to applicable rules. 
Exact lifecycle transitions and cancellation rules require backend/Product confirmation. 
 
41. Wave Sharing 
Wave Cards include a Share action. 
Depending on browser/device support, sharing may use: 
●​ Native sharing 
●​ Link copying 
The exact URL and sharing behavior should be verified during QA. 
 
42. Wave Loading State 
When Wave data is being loaded, the frontend contains loading/skeleton UI. 
A Wave Card skeleton can be displayed while data is being retrieved. 
QA Requirements 
Verify that: 
●​ Loading UI appears correctly. 
●​ Loading UI disappears after success. 
●​ Loading UI disappears after failure. 
●​ No infinite loading occurs. 
●​ Switching tabs does not leave stale loading states. 
 
43. Wave Empty State 

When no matching Waves are available, the interface displays: 
No waves found 
The interface also provides an appropriate empty-state presentation. 
Possible Causes 
●​ No Waves currently available 
●​ Search returned no results 
●​ Selected tab has no data 
●​ Network/API issue 
●​ Backend returned an empty response 
The AI should distinguish a genuine empty state from a data-loading failure. 
 
44. Error Handling 
Wave operations may fail because of: 
●​ Authentication problems 
●​ Authorization problems 
●​ Network failures 
●​ Backend errors 
●​ Real-time communication failures 
●​ Microphone permissions 
●​ Invalid room state 
●​ Missing room information 
Exact error messages should be documented only after confirming them through the current 
implementation or live testing. 
 
45. Troubleshooting — Cannot Join a 
Wave 
If a user cannot join: 

Check 1 
Confirm the user is logged in. 
Check 2 
Confirm the Wave still exists. 
Check 3 
Confirm the Wave is still active if attempting to join a live room. 
Check 4 
Check whether the Wave has restricted visibility. 
Check 5 
Check the user's network connection. 
Check 6 
Capture the exact error message. 
Check 7 
Try another available Wave. 
If multiple Waves cannot be joined, escalate for technical investigation. 
 
46. Troubleshooting — Audio Not Working 
Check: 
1.​ Is the user inside the Wave? 
2.​ Is the user a Listener or Speaker? 
3.​ If Listener, has Raise Hand been used? 
4.​ Has the Host approved the request? 
5.​ Is microphone permission enabled? 
6.​ Is the correct microphone selected? 
7.​ Is the device microphone functioning? 

8.​ Is the network stable? 
9.​ Does leaving and rejoining resolve the issue? 
If the issue continues, escalate. 
 
47. Troubleshooting — Chat Not Updating 
If chat messages are not appearing: 
1.​ Wait briefly for the next update. 
2.​ Check network connectivity. 
3.​ Check whether the chat permission allows the user to participate. 
4.​ Reopen or rejoin the Wave if appropriate. 
5.​ Check whether other participants are experiencing the same issue. 
6.​ Record the Wave ID and approximate time. 
7.​ Escalate if the issue persists. 
 
48. Troubleshooting — Raise Hand Not 
Working 
Check: 
●​ User is inside an active Wave. 
●​ User is a Listener. 
●​ Raise Hand control is visible. 
●​ Network connection is working. 
●​ Request submission does not return an error. 
If the request appears to submit but the Host does not receive it, investigate as a possible 
backend or real-time synchronization issue. 
 
49. Troubleshooting — Scheduled Wave 
If a scheduled Wave does not appear correctly: 

1.​ Refresh Waves. 
2.​ Check the appropriate tab. 
3.​ Search for the Wave. 
4.​ Verify the scheduled date/time. 
5.​ Confirm whether the Wave was cancelled. 
6.​ Check whether the user has access. 
7.​ Escalate if the Wave exists but is not displayed correctly. 
 
50. Privacy Considerations 
Waves involve potentially sensitive communication data. 
Relevant information includes: 
●​ User identity 
●​ Participant identity 
●​ Audio communication 
●​ Chat messages 
●​ Wave participation 
●​ Participant roles 
●​ Moderation activity 
●​ Wave visibility 
The system must apply appropriate privacy and access controls. 
 
51. Recording Policy 
The current frontend analysis does not establish that Waves are automatically recorded. 
Therefore, the AI must not tell users: 
“All Waves are recorded.” 
or: 
“Waves are never recorded.” 
unless WiseIN Product/Security documentation explicitly confirms the policy. 

Recording, transcription, storage, and retention require separate confirmation. 
 
52. Chat Retention 
The frontend confirms that chat functionality exists, but it does not establish the official retention 
policy. 
The following require confirmation: 
●​ Storage duration 
●​ Deletion policy 
●​ User access to historical messages 
●​ Administrative access 
●​ Data export behavior 
●​ Deletion after Wave removal 
The AI must not invent retention periods. 
 
53. Audio Data 
The exact handling of Wave audio requires Security and Engineering confirmation. 
Items requiring confirmation include: 
●​ Whether audio is stored 
●​ Whether audio is recorded 
●​ Whether audio is transmitted only in real time 
●​ Encryption 
●​ Retention 
●​ Deletion 
●​ Provider-side storage 
 
54. Backend Authorization 
All Wave permissions must be enforced server-side. 

Examples include: 
●​ Private Wave access 
●​ Speaker approval 
●​ Participant mute 
●​ Participant blocking 
●​ Ending a Wave 
●​ Chat restrictions 
●​ Wave creation 
●​ Wave modification 
A user must not be able to gain unauthorized permissions simply by modifying frontend 
requests. 
 
55. API References 
The frontend analysis identifies references to Wave-related API endpoints. 
These should be treated as frontend API references, not complete backend API 
documentation. 
Method 
Endpoint 
Purpose Indicated by 
Frontend 
GET 
/waves 
Retrieve Waves 
GET 
/waves/live 
Retrieve live Waves 
GET 
/waves/trending 
Retrieve trending Waves 
POST 
/waves 
Create a Wave 
POST 
/waves/{id}/join 
Join a Wave 
POST 
/waves/{id}/leave 
Leave a Wave 
POST 
/waves/{id}/end 
End a Wave 
POST 
/waves/{id}/raise-hand 
Raise Hand / speaker request 
POST 
/waves/speaker-request/a
pprove 
Approve speaker request 

POST 
/waves/{id}/mute/{userId
}/mute 
Mute participant 
POST 
/waves/{id}/reminder 
Set reminder 
POST 
/waves/toggle 
Toggle reaction 
Status: Frontend referenced. Backend implementation, authorization, response schemas, and 
error contracts require Engineering verification. 
 
56. API Security Requirements 
The backend should validate: 
●​ Authentication 
●​ User identity 
●​ Wave existence 
●​ Wave state 
●​ Participant membership 
●​ Participant role 
●​ Host privileges 
●​ Visibility permissions 
●​ Chat permissions 
●​ Speaker permissions 
Example 
A Listener must not be able to call a Host-only API successfully simply because the frontend 
does not prevent the request. 
 
57. Platform Compatibility 
57.1 Desktop Web 
The inspected implementation primarily represents the WiseIN web application. 

Desktop QA should cover: 
●​ Navigation 
●​ Wave discovery 
●​ Search 
●​ Wave creation 
●​ Scheduling 
●​ Live room 
●​ Audio 
●​ Chat 
●​ Host controls 
●​ Sharing 
 
57.2 Mobile Web 
Responsive behavior requires dedicated testing. 
Test: 
●​ Wave cards 
●​ Search 
●​ Tabs 
●​ Start Wave modal 
●​ Live room 
●​ Audio controls 
●​ Chat 
●​ Host controls 
●​ Scheduling 
●​ Sharing 
 
57.3 Native Android/iOS 
Native mobile behavior has not been confirmed through this frontend analysis. 
Separate Android/iOS testing should be performed if native WiseIN applications are available. 
 
58. Accessibility 

The Waves interface should be tested for: 
●​ Keyboard navigation 
●​ Focus visibility 
●​ Screen-reader labels 
●​ Button accessibility 
●​ Modal accessibility 
●​ Chat accessibility 
●​ Microphone control accessibility 
●​ Raise Hand accessibility 
●​ Error-message accessibility 
●​ Adequate contrast 
Accessibility compliance should be confirmed by dedicated QA testing. 
 
59. AI Customer-Support Scope 
The WiseIN AI assistant can answer general Waves questions such as: 
●​ What are Waves? 
●​ How do I access Waves? 
●​ How do I join? 
●​ How do I create a Wave? 
●​ How do I schedule a Wave? 
●​ How do I request to speak? 
●​ Why can't I speak? 
●​ How do I enable my microphone? 
●​ How does Wave chat work? 
●​ How do I leave a Wave? 
●​ What can a Host do? 
 
60. AI Must Not Assume 
The AI must not assume: 
●​ Participant limits 
●​ Recording 
●​ Transcription 

●​ Data-retention periods 
●​ Notification guarantees 
●​ Subscription requirements 
●​ Co-Host permissions 
●​ Backend authorization rules 
●​ Mobile availability 
●​ Exact error codes 
●​ Cancellation policies 
●​ Audio storage 
●​ Chat storage 
unless these are explicitly confirmed in approved documentation. 
 
61. AI Example — “What Are Waves?” 
Recommended answer: 
Waves are WiseIN's real-time audio rooms for live professional conversations. 
Depending on their permissions, participants can listen, request to speak, 
participate in chat, and send reactions. Hosts can manage participants and control 
the room. 
 
62. AI Example — “How Can I Speak?” 
Recommended answer: 
If you're currently a Listener, use Raise Hand to request permission to speak. The 
Host needs to approve the request. Once you receive Speaker access, you can 
enable your microphone. If the microphone still doesn't work, check your browser 
and device microphone permissions. 
 
63. AI Example — “Why Can't I Speak?” 
Recommended answer: 

You may currently be a Listener. Try using Raise Hand and wait for the Host to 
approve your request. If you've already been given Speaker access, check that 
your browser and device allow microphone access. If the issue continues, I can 
guide you through additional troubleshooting. 
 
64. AI Example — “Are Waves Recorded?” 
Recommended answer: 
The current documentation does not confirm whether Waves are recorded or 
retained. I don't want to give you incorrect information. Please contact WiseIN 
Support for the current recording and data-retention policy. 
 
65. AI Example — “How Many People Can 
Join?” 
Recommended answer: 
I don't have a confirmed participant limit for Waves in the current documentation. I 
don't want to provide an unverified number. WiseIN Support can confirm the current 
limit. 
 
66. Human Support Escalation 
The AI should escalate when: 
●​ A user repeatedly cannot join a Wave. 
●​ Audio repeatedly fails. 
●​ Microphone permission is correct but audio still does not work. 
●​ Speaker requests are not processed. 
●​ Host controls do not work. 
●​ Private Wave access appears incorrect. 
●​ Chat consistently fails. 

●​ Multiple users report the same Wave problem. 
●​ A user reports a privacy/security issue. 
●​ A user reports harassment or abuse. 
●​ Account-specific investigation is required. 
●​ The AI cannot answer confidently using approved documentation. 
 
67. Escalation Information 
Where permitted by WiseIN's support process, the support team should receive: 
●​ User identifier through approved internal systems 
●​ Wave ID 
●​ Wave title 
●​ User role 
●​ Host information 
●​ Platform 
●​ Browser/app version 
●​ Device 
●​ Date/time 
●​ Action performed 
●​ Expected result 
●​ Actual result 
●​ Exact error message 
●​ Screenshot where permitted 
●​ Reproduction steps 
●​ Frequency of occurrence 
●​ Troubleshooting already attempted 
Never Request 
The AI must not request: 
●​ Passwords 
●​ OTPs 
●​ Authentication tokens 
●​ API keys 
●​ Unnecessary identity documents 
 

68. QA Test Plan 
Test ID 
Test Case 
Expected Result 
WAV-001 
Open Waves 
Waves page loads 
WAV-002 
Open For You 
Appropriate feed loads 
WAV-003 
Open Discover 
Discover feed loads 
WAV-004 
Open Trending 
Trending feed loads 
WAV-005 
Open Following 
Following feed loads 
WAV-006 
Open Completed 
Completed Waves load 
WAV-007 
Search existing Wave 
Matching result appears 
WAV-008 
Search nonexistent Wave 
Empty state appears 
WAV-009 
Open Wave Card 
Correct Wave information displayed 
WAV-010 
Start Wave 
Creation interface opens 
WAV-011 
Create valid Wave 
Wave is created 
WAV-012 
Create invalid Wave 
Validation/error appears 
WAV-013 
Schedule Wave 
Wave is scheduled 
WAV-014 
Set Reminder 
Reminder behavior works 
WAV-015 
Join Live Wave 
User enters room 
WAV-016 
Join restricted Wave 
Access follows permission 
WAV-017 
Listener audio 
Listener can hear permitted audio 
WAV-018 
Raise Hand 
Request is submitted 
WAV-019 
Host approves speaker 
User receives Speaker access 
WAV-020 
Enable microphone 
Speaker can transmit audio 
WAV-021 
Deny microphone permission Appropriate error/guidance 
WAV-022 
Send chat 
Message is submitted 
WAV-023 
Receive chat 
Message appears 

WAV-024 
Send reaction 
Reaction appears 
WAV-025 
Host mute 
Participant is muted 
WAV-026 
Unauthorized mute 
Action rejected 
WAV-027 
Host block 
Moderation action executes 
WAV-028 
End Wave 
Wave ends 
WAV-029 
Leave Wave 
User exits room 
WAV-030 
Share Wave 
Share/copy works 
WAV-031 
Loading state 
Skeleton appears correctly 
WAV-032 
Empty state 
“No waves found” appears 
WAV-033 
Network interruption 
Failure/recovery handled 
WAV-034 
Rejoin after interruption 
Rejoin behavior works 
WAV-035 
Mobile web 
Layout usable 
WAV-036 
Keyboard navigation 
Controls accessible 
WAV-037 
Private Wave authorization 
Unauthorized user blocked 
WAV-038 
Chat permission 
Unauthorized chat blocked 
WAV-039 
Speaker authorization 
Unauthorized audio blocked 
WAV-040 
Host authorization 
Only authorized Host can perform Host actions 
 
69. Security Test Cases 
WAV-SEC-001 — Unauthorized Host Action 
Attempt Host functionality using a Listener account. 
Expected Result: Backend rejects the operation. 
WAV-SEC-002 — Private Wave Access 
Attempt to access a Private Wave without authorization. 

Expected Result: Access is denied. 
WAV-SEC-003 — Unauthorized Speaker Access 
Attempt audio transmission without Speaker permission. 
Expected Result: Audio transmission is blocked. 
WAV-SEC-004 — Unauthorized Wave Termination 
Attempt to end a Wave without Host authorization. 
Expected Result: Backend rejects the request. 
WAV-SEC-005 — Unauthorized Chat 
Attempt to send chat when the user does not satisfy the configured chat permission. 
Expected Result: Backend rejects the message. 
 
70. Known Limitations 
The following information requires confirmation: 
1.​ Maximum participant capacity 
2.​ Exact Co-Host permissions 
3.​ Recording availability 
4.​ Transcription availability 
5.​ Audio retention 
6.​ Chat retention 
7.​ Push notifications 
8.​ Email notifications 
9.​ Reminder delivery 
10.​Scheduled Wave lifecycle 
11.​Cancellation rules 
12.​Completed Wave retention 
13.​Mobile native behavior 
14.​Backend authorization 
15.​Private Wave enforcement 
16.​Subscription restrictions 
17.​Rejoin behavior 
18.​Data deletion behavior 

19.​Reporting functionality 
20.​Abuse-management workflow 
 
71. Product Questions 
The Product team should confirm: 
1.​ What are Waves officially intended for? 
2.​ What is the maximum number of participants? 
3.​ What are the official Wave categories? 
4.​ What are the exact Host permissions? 
5.​ What are the exact Co-Host permissions? 
6.​ Can users record Waves? 
7.​ Are Waves automatically recorded? 
8.​ Are Waves transcribed? 
9.​ Are completed Waves accessible later? 
10.​What happens to a scheduled Wave that is not started? 
11.​Are reminders sent by push notification? 
12.​Are reminders sent by email? 
13.​Are Waves available to all users or only specific account types? 
14.​Are there subscription restrictions? 
 
72. Engineering Questions 
Engineering should verify: 
1.​ Backend authorization for every Wave action 
2.​ Participant-limit enforcement 
3.​ Private Wave authorization 
4.​ Speaker permission enforcement 
5.​ Host permission enforcement 
6.​ Chat permission enforcement 
7.​ Wave lifecycle 
8.​ Audio-provider configuration 
9.​ Reconnection behavior 
10.​Rejoin behavior 
11.​API error responses 
12.​API rate limits 

13.​Chat storage 
14.​Audio storage 
15.​Wave deletion behavior 
 
73. Security Questions 
Security should verify: 
1.​ Audio transmission security 
2.​ Authentication 
3.​ Authorization 
4.​ Private Wave protection 
5.​ Chat protection 
6.​ Data retention 
7.​ Data deletion 
8.​ Provider-side data handling 
9.​ Recording policy 
10.​Administrative access 
11.​User privacy controls 
 
74. Related Documentation 
This document should be linked with: 
Core Product 
●​ WISEIN-INTRO-001 — WiseIN Application Overview 
●​ WISEIN-EXP-014 — WiseIN Explore Documentation 
●​ WISEIN-SRC-015 — WiseIN Regular Search Documentation 
●​ WISEIN-AIS-016 — WiseIN AI Search Documentation 
●​ WISEIN-TOP-017 — WiseIN Topics Documentation 
Authentication 
●​ WISEIN-AUTH-003 — WiseIN Registration 
●​ WISEIN-AUTH-006 — WiseIN Email Verification 
●​ WISEIN-VER-007 — WiseIN Identity Verification 
●​ WiseIN Login Documentation 

●​ WiseIN Security Documentation 
Other Product Modules 
●​ Jobs 
●​ Chat 
●​ Meetings 
●​ Events 
●​ Profile 
●​ Organizations 
●​ Notifications 
●​ Subscriptions 
Support 
●​ Customer Support 
●​ Privacy & Safety 
●​ AI Customer Support 
 
75. RAG Knowledge-Base Classification 
Each Waves knowledge item should contain a verification state. 
CONFIRMED-FRONTEND 
Directly identified in the inspected frontend. 
OBSERVED-LIVE 
Confirmed through live application testing. 
BACKEND-CONFIRMED 
Verified through backend implementation or API testing. 
PRODUCT-CONFIRMED 
Approved by WiseIN Product. 
SECURITY-CONFIRMED 

Approved by Security. 
PENDING-VERIFICATION 
Requires confirmation. 
DEPRECATED 
Previously valid but no longer applicable. 
 
76. Recommended RAG Knowledge Units 
The document should be chunked into independent knowledge units such as: 
1.​ Waves Overview 
2.​ Accessing Waves 
3.​ Waves Tabs 
4.​ Wave Search 
5.​ Wave Cards 
6.​ Creating a Wave 
7.​ Wave Categories 
8.​ Wave Duration 
9.​ Wave Visibility 
10.​Chat Permissions 
11.​Scheduling 
12.​Joining 
13.​Listener Role 
14.​Raise Hand 
15.​Speaker Role 
16.​Microphone 
17.​Live Room 
18.​Chat 
19.​Reactions 
20.​Host Controls 
21.​Ending a Wave 
22.​Leaving a Wave 
23.​Troubleshooting 
24.​Privacy 
25.​Recording 
26.​Notifications 
27.​Security 

28.​Support Escalation 
 
77. RAG Metadata 
Recommended metadata: 
document_id: WISEIN-WAV-018 
module: Waves 
version: 1.0 
platform: Web 
source: Frontend Code Analysis 
status: Draft 
verification_status: Mixed 
knowledge_type: Product Documentation 
prepared_by: MSR 
last_updated: 17-09-2026 
Individual chunks should also contain their own verification status. 
 
78. AI Hallucination Prevention 
The AI must follow these rules when answering Waves-related questions: 
Rule 1 
Use the latest approved documentation. 
Rule 2 
Never invent missing information. 
Rule 3 
Never provide unsupported workarounds. 
Rule 4 
Never expose internal API credentials or implementation secrets. 

Rule 5 
Never request passwords or OTPs. 
Rule 6 
Never claim to have performed an action unless an authorized tool actually performed it. 
Rule 7 
Never reveal private participant information. 
Rule 8 
When documentation is insufficient, clearly communicate uncertainty. 
Rule 9 
Escalate account-specific or unresolved issues. 
Rule 10 
Use Product-confirmed policies for user-facing guarantees. 
 
79. Documentation Maintenance 
This document must be reviewed whenever there is a change to: 
●​ Waves UI 
●​ Wave creation 
●​ Scheduling 
●​ Visibility 
●​ Chat 
●​ Roles 
●​ Host controls 
●​ Audio infrastructure 
●​ APIs 
●​ Notifications 
●​ Recording 
●​ Data retention 
●​ Privacy 

●​ Mobile support 
Each revision should update: 
●​ Version 
●​ Date 
●​ Author 
●​ Changed sections 
●​ Verification status 
 
80. Version History 
Version 
Date 
Author 
Change 
Statu
s 
1.0 
17 Sep 
2026 
MSR 
Initial comprehensive Waves 
documentation 
Draft 
 
81. Final Documentation Status 
Document ID: WISEIN-WAV-018​
 Module: Waves​
 Version: 1.0 
Area 
Status 
Waves Overview 
Documented 
Navigation 
Documented 
Search 
Documented 
Wave Creation 
Documented 
Scheduling 
Documented 
Joining 
Documented 
Listener/Speaker Flow Documented 

Raise Hand 
Documented 
Host Controls 
Documented 
Chat 
Documented 
Reactions 
Documented 
Troubleshooting 
Documented 
QA 
Test Cases Prepared 
Security 
Review Required 
Backend 
Verification Required 
Product Policies 
Verification Required 
Mobile 
Verification Required 
AI/RAG 
Prepared for Controlled Ingestion 
Production Approval 
Pending 
 
82. Final Documentation Principle 
The Waves documentation must maintain a strict distinction between what the frontend 
implements, what has been observed in the live product, and what WiseIN officially 
guarantees. 
The frontend analysis confirms the existence of the Waves interface, Wave discovery, creation 
and scheduling functionality, live-room interactions, participant roles, chat, reactions, and 
Wave-related API references. Product policies, backend authorization, data retention, recording, 
notification behavior, participant limits, and other security-sensitive behavior require explicit 
confirmation before being presented to users as guaranteed functionality. 
This document should therefore be approved by Product, Engineering, QA, Security, and 
Support before being treated as the final production source of truth for the WiseIN AI 
customer-support chatbot. 
 



---

