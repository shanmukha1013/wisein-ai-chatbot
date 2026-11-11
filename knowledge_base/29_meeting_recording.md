# Meeting Recording

## Source: WISEIN-MEETING-RECORDING-029.pdf

WISEIN — MEETING RECORDING  
Document ID: WISEIN-MEETING-RECORDING-029 
Purpose: AI Chatbot / RAG Knowledge Base / Customer Support 
Platform: WiseIN 
 
1. MEETING RECORDING — OVERVIEW 
Meeting Recording refers to the recording of a WiseIN video meeting or call. 
WiseIN is a video-first professional networking platform. Its current website describes 
video calls as a core interaction and states that its meeting-intelligence system generates 
summaries after calls. The website also has a historical product update titled “AI 
Summary Recordings”, describing intelligent summaries of video meetings and calls.  
The current WiseIN Content Policies explicitly recognize meeting recordings as platform 
content and provide specific rules for recording consent, privacy, sharing, transcripts, and 
AI summaries.  
Therefore, the Meeting Recording knowledge base should cover: 
• 
recording of video meetings  
• 
recording consent  
• 
privacy  
• 
recording access  
• 
meeting recordings versus AI summaries  
• 
transcription  
• 
sharing restrictions  
• 
recording-related troubleshooting  
• 
retention/deletion considerations  
• 
permissions and authorization  
• 
AI chatbot handling of recording questions.  
 
2. WISEIN MEETING INTELLIGENCE 

WiseIN's current homepage describes Meeting Intelligence. 
The website states that after a call, AI produces a summary containing: 
• 
key points  
• 
follow-ups  
• 
action items.  
WiseIN presents this as part of its video-first meeting experience.  
The current India-facing Premium offering explicitly lists: 
AI Meeting Summaries & Transcription 
as a Premium feature.  
The global pricing page similarly describes Premium as including unlimited video calls with 
AI summaries.  
Important distinction 
Meeting Recording ≠ Meeting Summary ≠ Transcription 
These are related but different concepts. 
Meeting Recording 
The captured audio/video content of a meeting, where recording is supported and 
authorized. 
Transcription 
A text representation of spoken meeting content. 
AI Meeting Summary 
An AI-generated condensed representation of the meeting, potentially containing: 
• 
key points  
• 
follow-ups  
• 
action items.  
The chatbot must not treat these three objects as interchangeable. 
 
3. WISEIN'S HISTORICAL AI RECORDING UPDATE 

WiseIN's public homepage contains a product-history update dated March 2025 titled: 
“AI Summary Recordings” 
The update describes automatically generating intelligent summaries of video meetings 
and calls to save time and avoid missing important details.  
This provides historical evidence that recording/meeting intelligence has been part of 
WiseIN's product development. 
However, historical product updates should not automatically be interpreted as a 
complete specification of the current recording interface. 
For current behavior, the chatbot should prioritize: 
1. current WiseIN product/API behavior  
2. current official policies  
3. current official website  
4. approved internal documentation.  
 
4. VIDEO CALLS AND MEETING RECORDINGS 
WiseIN's current website describes the platform as video-first and says users can book a 
video call and talk face-to-face.  
The official mobile-app page also states that users can: 
• 
book and join video calls  
• 
read AI meeting summaries after calls  
• 
manage availability and slot bookings.  
Meeting Recording belongs to this broader meeting/video-call ecosystem. 
However, not every video call should automatically be assumed to be recorded. 
The chatbot must not say: 
“All WiseIN calls are recorded.” 
unless current product/API documentation explicitly confirms that behavior. 
 

5. RECORDING CONSENT — CRITICAL RULE 
WiseIN's Content Policies explicitly state: 
If a call is being recorded, both people must know. 
WiseIN prohibits secretly recording another person.  
This is one of the most important rules for the Meeting Recording chatbot. 
Chatbot rule 
If a user asks: 
“Can I record a WiseIN meeting without telling the other person?” 
The chatbot should answer: 
WiseIN's Content Policies require both participants to know when a call is being recorded. 
Secretly recording another person is not permitted.  
Do not provide instructions for secretly recording a meeting. 
 
6. PRIVACY OF MEETING RECORDINGS 
WiseIN treats conversations and meeting content as private. 
Its Content Policies state that what happens on a WiseIN video call stays between the 
people on that call and prohibit sharing, publishing, or posting recordings, transcripts, or AI 
summaries without explicit permission from the other person.  
WiseIN's Terms also prohibit unauthorized recording, screenshotting, or sharing of private 
conversations, meetings, or content without permission.  
Therefore, a meeting recording should be treated as potentially private meeting content. 
 
7. SHARING A MEETING RECORDING 
A recording should not be treated as ordinary public content. 
WiseIN's policy specifically prohibits sharing or publishing recordings without appropriate 
permission.  
The chatbot should not recommend: 

• 
uploading another person's meeting recording as a public post  
• 
sharing a recording publicly without consent  
• 
publishing a private recording as a Clip  
• 
sending a private recording to unrelated users  
• 
posting meeting footage to communities without permission.  
Safe answer 
Meeting recordings can contain private conversations. WiseIN's policies require 
appropriate consent before sharing or publishing recordings. 
 
8. RECORDING VS AI SUMMARY 
This distinction is essential for RAG. 
Recording 
The actual captured meeting media. 
Transcript 
The written representation of spoken content. 
AI Summary 
A condensed AI-generated interpretation of the meeting. 
WiseIN's current website promotes AI meeting summaries and transcription as Premium 
functionality.  
However, the chatbot must not claim that: 
“The transcript is the recording.” 
or: 
“Deleting the summary deletes the recording.” 
Those behaviors require product/API confirmation. 
 
9. AI MEETING SUMMARIES ARE PERSONAL 

WiseIN's Content Policies explicitly state that the AI meeting summary is for the user and 
should not be posted publicly or shared without the other person's consent.  
Therefore: 
AI summary 
• 
should be treated as private meeting information  
• 
should not automatically be posted to the feed  
• 
should not automatically be shared with other users  
• 
should not be assumed to be visible to all participants.  
Chatbot answer 
WiseIN's policy treats AI meeting summaries as personal meeting information. Do not 
publish or share a meeting summary without the appropriate consent.  
 
10. TRANSCRIPTION 
WiseIN currently advertises AI Meeting Summaries & Transcription in its India Premium 
offering.  
The global pricing page also lists AI summaries with Premium video calls.  
Therefore, transcription is a documented WiseIN capability associated with supported 
Premium meeting experiences. 
However, the public sources do not establish: 
• 
exact transcription language support  
• 
transcription accuracy  
• 
whether transcription begins automatically  
• 
whether participants can manually start/stop transcription  
• 
whether every meeting is transcribed  
• 
exact transcript retention period  
• 
transcript download format  
• 
transcript export behavior.  

The chatbot must not invent these details. 
 
11. AUTOMATIC RECORDING 
The public website confirms AI meeting intelligence and refers historically to AI Summary 
Recordings, but it does not provide enough current public documentation to establish that 
every meeting is automatically recorded. 
Therefore: 
Do not tell users that every WiseIN meeting is automatically recorded. 
Instead: 
Recording availability and behavior depend on the meeting functionality currently provided 
by WiseIN. The exact recording controls should be verified from the current meeting 
interface or authorized backend. 
 
12. RECORDING START/STOP CONTROLS 
The previously supplied WiseIN product documentation explicitly identifies Meeting 
Recording as an area requiring separate verification and says the available screenshots do 
not establish the complete behavior of meeting recording, transcription, or AI summaries.  
Therefore, this knowledge base should not invent exact button names such as: 
• 
Start Recording  
• 
Stop Recording  
• 
Record  
• 
Recording  
• 
Pause Recording.  
If these controls are present in the current application, the exact labels should be taken 
from the current UI. 
 
13. RECORDING INDICATOR 

Because WiseIN requires both participants to know when a call is being recorded, the 
actual product should communicate recording status appropriately. 
However, the public documentation available for this knowledge base does not specify the 
exact visual indicator. 
Do not claim that WiseIN uses: 
• 
a red recording dot  
• 
a banner  
• 
a notification sound  
• 
a timer  
• 
a popup  
• 
a specific recording icon  
unless confirmed by current product UI/API documentation. 
 
14. WHO CAN ACCESS A RECORDING? 
Access to a meeting recording should be treated as permission-controlled information. 
The chatbot should distinguish: 
Public information 
Information about the WiseIN platform's general recording policy. 
Private meeting information 
Actual recordings, transcripts, summaries, participants, meeting details, and other 
account-specific content. 
Private information must only be retrieved through authorized backend services. 
The AI must never expose another user's recording simply because the user knows the 
meeting title or participant name. 
 
15. RECORDING AND MEETING PARTICIPANTS 
A recording can contain information belonging to multiple meeting participants. 

Therefore, a user's ability to access, download, share, or delete a recording should not be 
assumed solely from the fact that the user participated in the meeting. 
The current product documentation does not establish the exact recording permission 
model. 
Do not invent: 
• 
host-only access  
• 
participant access  
• 
organizer access  
• 
automatic access for all attendees  
• 
organization administrator access.  
These must be verified through the actual WiseIN permission model. 
 
16. RECORDING OWNERSHIP 
The available public documentation does not define a complete legal or technical 
ownership model for meeting recordings. 
Therefore, the chatbot should not state: 
“The meeting host owns the recording.” 
or: 
“Every participant owns a copy.” 
unless WiseIN's approved legal/product documentation explicitly states this. 
Instead: 
Access and control of meeting recordings depend on WiseIN's applicable product 
permissions and policies. 
 
17. RECORDING RETENTION 
WiseIN's Privacy Policy explains that information is retained according to the type of data 
and its purpose. It states that posts, messages, and content may be retained until 

deletion/account closure, with some deleted content potentially remaining temporarily in 
backups for technical or legal reasons.  
However, this does not establish a specific retention period for meeting recordings. 
Do not invent: 
• 
30-day recording retention  
• 
90-day retention  
• 
permanent storage  
• 
automatic deletion after a meeting  
• 
automatic cloud archival.  
Chatbot answer 
WiseIN's public Privacy Policy does not specify a universal retention period specifically for 
meeting recordings. The exact retention behavior should be verified through current WiseIN 
product documentation or support. 
 
18. DELETING A MEETING RECORDING 
The current public sources do not establish the exact recording deletion workflow. 
Therefore, do not claim: 
Settings → Meetings → Recordings → Delete 
unless the current UI confirms it. 
If a user asks: 
“How do I delete a recording?” 
The chatbot should check the current authorized recording API/UI. 
If no verified workflow exists: 
“I don't have a verified current WiseIN workflow for deleting a meeting recording. I can 
guide you based on the current recording interface or direct the issue to WiseIN support.” 
 
19. RECORDING DOWNLOAD 

The available official sources do not confirm a universal recording download feature. 
Therefore, do not claim that users can download recordings as: 
• 
MP4  
• 
WebM  
• 
MOV  
• 
audio files  
• 
ZIP archives.  
Do not invent a download button or file format. 
If a download feature exists, document it separately after product verification. 
 
20. RECORDING EXPORT 
Similarly, the current public documentation does not confirm: 
• 
transcript export  
• 
PDF summary export  
• 
DOCX transcript export  
• 
MP3 audio export  
• 
MP4 video export  
• 
external storage integration.  
These should remain unverified. 
 
21. RECORDING AND PROFILE VIDEO 
Meeting Recording must be distinguished from Profile Video. 
Profile Video 
A video uploaded by a user to their professional profile for introduction/presentation 
purposes. 
Meeting Recording 

A recording associated with a video meeting or call. 
A profile video is intended to represent the user's professional identity. 
A meeting recording captures an actual conversation. 
The chatbot must never tell a user that their meeting recording automatically becomes 
their profile video. 
 
22. RECORDING AND CLIPS 
WiseIN Clips are a separate video-oriented content format. 
A meeting recording should not automatically become a Clip. 
If a user asks: 
“Can I post my meeting recording as a Clip?” 
The chatbot should emphasize privacy and consent first. 
WiseIN's Content Policies prohibit publicly sharing meeting recordings without appropriate 
permission.  
Therefore: 
A meeting recording should not be published as a Clip unless the necessary permissions 
and consent requirements are satisfied. 
 
23. RECORDING AND POSTS 
Meeting recordings are private meeting content, while Posts are platform content. 
The chatbot must distinguish: 
Meeting 
   ↓ 
Meeting Recording 
   ↓ 
Private meeting content 
 

Post 
   ↓ 
Published platform content 
A meeting recording should not automatically be considered a Post. 
 
24. RECORDING AND WEBINARS 
Webinars and Meetings are distinct WiseIN feature areas. 
The previously supplied WiseIN application documentation explicitly says Meetings and 
Webinars should be treated separately in the knowledge base.  
Therefore: 
Meeting Recording 
→ recording associated with a supported meeting/call. 
Webinar Recording 
→ only if the specific webinar functionality supports recording. 
Do not automatically assume that every webinar has a recording. 
The previously supplied product documentation specifically says recording availability for 
events should be verified for each applicable event category.  
 
25. RECORDING AND EVENTS 
WiseIN's event documentation framework includes completed-event handling and 
specifically identifies recordings as something that must be verified for each event type.  
Therefore: 
A completed event does not automatically mean a recording is available. 
If a user asks: 
“Where is the recording of this event?” 
The chatbot should check the actual event/recording data rather than assuming that a 
recording exists. 

 
26. RECORDING AND AI SUMMARIES 
The relationship can be represented as: 
WiseIN Video Meeting 
        │ 
        ├── Recording 
        │ 
        ├── Transcript 
        │ 
        └── AI Meeting Summary 
                ├── Key Points 
                ├── Follow-ups 
                └── Action Items 
The existence of one does not automatically prove the existence of the others. 
For example: 
• 
recording available ≠ transcript guaranteed  
• 
transcript available ≠ public sharing permitted  
• 
AI summary available ≠ recording publicly available  
• 
completed meeting ≠ recording available.  
 
27. MEETING RECORDING PRIVACY POLICY 
WiseIN's current Content Policies provide three particularly important rules: 
Rule 1 — Calls are private 
Meeting conversations should remain private. 
Rule 2 — AI summaries are personal 

AI-generated meeting summaries should not be publicly shared without appropriate 
consent. 
Rule 3 — Recording requires awareness 
If a call is recorded, both participants must know. 
These should be treated as high-priority RAG facts. 
 
28. UNAUTHORIZED RECORDING 
WiseIN's Terms explicitly prohibit unauthorized recording, screenshotting, or sharing of 
private conversations, meetings, or content without permission.  
The chatbot should therefore refuse to provide instructions designed to secretly capture 
another participant's WiseIN meeting. 
Instead, it should explain the platform's consent requirement. 
 
29. RECORDING CONFIDENTIAL INFORMATION 
WiseIN's Content Policies prohibit publicly sharing sensitive information such as: 
• 
financial data  
• 
ID proofs  
• 
salary details  
• 
internal company information  
• 
business strategies.  
They also prohibit publicly posting private conversations.  
Because meeting recordings can contain such information, users should treat recordings 
as sensitive content. 
 
30. RECORDING AND COPYRIGHT 
Meeting recordings can contain: 
• 
presentations  

• 
documents  
• 
demonstrations  
• 
third-party material  
• 
company content  
• 
copyrighted media.  
WiseIN's Content Policies require users to share content they created or have permission 
to use and prohibit stolen/copyright-infringing content.  
Therefore, recording a meeting does not automatically grant permission to redistribute 
every piece of content shown during that meeting. 
 
31. RECORDING AND ORGANIZATION MEETINGS 
WiseIN provides organization-level meeting and collaboration functionality. 
Its Organization platform describes 1-to-1 and group meetings and calendar 
synchronization.  
However, organization-level permissions for meeting recordings are not fully documented 
publicly. 
Do not assume that an Organization administrator can automatically access every 
employee's recording. 
Access must be based on the actual WiseIN authorization model. 
 
32. RECORDING AND PREMIUM 
WiseIN's current India-facing homepage lists: 
AI Meeting Summaries & Transcription 
under Premium.  
The global pricing page similarly describes Premium as providing unlimited video calls with 
AI summaries.  
Important distinction 
This confirms Premium access to AI meeting intelligence. 

It does not, by itself, establish that: 
• 
Premium users can record every meeting  
• 
recording is unlimited  
• 
recording storage is unlimited  
• 
every participant gets recording access  
• 
recording files can be downloaded.  
Those details require separate verification. 
 
33. RECORDING AND BASIC PLAN 
The current global pricing page lists Basic with: 
• 
verified profile  
• 
browsing verified professionals  
• 
three video calls per month  
• 
communities/public events  
• 
basic profile analytics  
• 
limited AI assistant.  
It does not explicitly list meeting recording as a Basic feature. 
Therefore, do not tell a Basic user that recording is included unless the current 
account/product data confirms it. 
 
34. RECORDING AND STUDENT PLAN 
The current pricing information lists the Student plan with student verification, mentor 
sessions, campus community access, job/internship board, and student badge.  
The public pricing information does not explicitly document Meeting Recording as a 
Student-plan feature. 
Do not assume Student users receive recording capabilities based only on their student 
status. 

 
35. RECORDING NOTIFICATIONS 
WiseIN supports platform notifications, but the public documentation does not provide a 
complete recording-specific notification specification. 
Do not invent: 
• 
“Recording started” email  
• 
“Recording ready” notification  
• 
recording completion push notification  
• 
automatic participant notification  
• 
transcript-ready notification.  
If the current application exposes these notifications, the live notification system should be 
treated as the source of truth. 
 
36. RECORDING READY STATUS 
If the backend provides a recording status, the chatbot may report it. 
Possible conceptual states could include: 
Not Available 
Recording 
Processing 
Ready 
Failed 
Deleted 
Restricted 
These are conceptual states only. 
The chatbot must use the actual WiseIN backend status values rather than assuming these 
are official WiseIN status names. 
 

37. RECORDING PROCESSING 
A recorded meeting may require processing before a recording, transcript, or AI summary 
becomes available. 
However, the public WiseIN documentation does not specify: 
• 
exact processing time  
• 
maximum processing time  
• 
processing stages  
• 
retry behavior  
• 
storage pipeline.  
Therefore, do not promise: 
“Your recording will be ready in 5 minutes.” 
Instead: 
“If WiseIN is still processing the recording, availability may depend on the current meeting 
system. Check the recording status or contact support if it remains unavailable.” 
 
38. RECORDING TROUBLESHOOTING 
Problem: “My meeting recording is missing.” 
The chatbot should check: 
1. Was the meeting completed?  
2. Was recording actually enabled/supported?  
3. Does the user have permission to access it?  
4. Is the recording still processing?  
5. Is the meeting associated with the correct account?  
6. Is there an error status?  
7. Is the recording available through the current meeting interface?  
The chatbot should not automatically conclude that the recording was deleted. 
 

39. “THE MEETING ENDED BUT THERE IS NO RECORDING” 
Recommended answer: 
A completed meeting does not by itself confirm that a recording is available. Recording 
availability depends on whether recording was supported/enabled and whether the user 
has access to the recording. Please check the meeting's available recording information or 
the current meeting interface. 
This follows the product documentation rule that recording availability must be verified 
rather than assumed.  
 
40. “I CANNOT PLAY THE RECORDING” 
Recommended troubleshooting: 
1. Refresh the meeting/recording page.  
2. Check the internet connection.  
3. Reopen the meeting from the correct account.  
4. Confirm that the recording is marked as available/ready.  
5. Try the current supported WiseIN web/app experience.  
6. If the recording remains unavailable, capture the exact error and escalate to 
support.  
Do not invent a codec or browser-specific cause without evidence. 
 
41. “RECORDING IS STUCK PROCESSING” 
The chatbot should ask for only useful diagnostic information: 
• 
meeting date/time  
• 
meeting identifier if visible  
• 
displayed recording status  
• 
exact error message  
• 
web/app platform  

• 
relevant screenshot, if voluntarily provided.  
Do not ask for: 
• 
password  
• 
OTP  
• 
authentication token  
• 
payment credentials.  
The broader WiseIN product documentation explicitly instructs the AI not to request 
sensitive credentials.  
 
42. “I CANNOT SHARE THE RECORDING” 
First determine whether the user means: 
1. they cannot technically share it, or  
2. they are asking whether sharing is permitted.  
For technical problems: 
• 
check whether a sharing control exists  
• 
check permissions  
• 
check recording availability.  
For policy questions: 
WiseIN's Content Policies require appropriate permission before sharing or publishing 
meeting recordings.  
 
43. “CAN I POST MY MEETING RECORDING?” 
Recommended answer: 
Meeting recordings can contain private conversations. WiseIN's Content Policies prohibit 
sharing or publishing recordings without explicit permission from the other person. Make 
sure the necessary consent and content rights are in place before publishing any recording.  
 

44. “CAN I SHARE THE AI SUMMARY INSTEAD?” 
Recommended answer: 
The AI meeting summary is also treated as personal meeting information under WiseIN's 
Content Policies. It should not be publicly posted or shared without the other person's 
consent.  
 
45. “CAN I RECORD SOMEONE SECRETLY?” 
Recommended answer: 
No. WiseIN's Content Policies state that if a call is being recorded, both people must know. 
Secretly recording another participant is not permitted.  
 
46. MEETING RECORDING AND ACCOUNT SECURITY 
Meeting recordings can contain sensitive professional information. 
The chatbot must therefore: 
• 
authenticate users before retrieving private recording information  
• 
authorize access to individual recordings  
• 
avoid exposing participant information  
• 
avoid exposing private transcripts  
• 
avoid revealing recording URLs without authorization  
• 
never expose backend storage paths  
• 
never expose access tokens or signed URLs.  
 
47. RAG VS LIVE API FOR MEETING RECORDINGS 
This is one of the most important implementation sections for the WiseIN AI chatbot. 
RAG should answer: 
• 
What is Meeting Recording?  
• 
Does WiseIN support meeting intelligence?  

• 
What are the recording privacy rules?  
• 
What does WiseIN say about recording consent?  
• 
What is an AI meeting summary?  
• 
What is transcription?  
• 
What are the general content/privacy restrictions?  
Live API should answer: 
• 
Does this meeting have a recording?  
• 
Is the recording ready?  
• 
Who can access the recording?  
• 
Is the user's recording available?  
• 
What is the current meeting status?  
• 
Is a transcript available?  
• 
Is the AI summary available?  
• 
Has the recording failed?  
• 
Has the recording been deleted?  
• 
What is the actual meeting/recording URL?  
The previously supplied WiseIN product documentation explicitly says account-specific 
meeting questions should use available live WiseIN data where appropriate tools and 
permissions exist and that the AI must not invent meeting details.  
 
48. RECOMMENDED CHATBOT ARCHITECTURE 
User 
  ↓ 
WiseIN Chat UI 
  ↓ 
Chat API 
  ↓ 

Authentication 
  ↓ 
Authorization 
  ↓ 
Intent Detection 
  ↓ 
 ┌─────────────────────────────┐ 
 │                             │ 
 ↓                             ↓ 
RAG Knowledge Base        Meeting API 
 │                             │ 
 │                             ├── Meeting status 
 │                             ├── Recording status 
 │                             ├── Recording access 
 │                             ├── Transcript status 
 │                             └── Summary status 
 │ 
 └──────────────┬──────────────┘ 
                ↓ 
              LLM 
                ↓ 
        Safe Customer Response 
The LLM should never receive unrestricted access to the database. 
 
49. RECOMMENDED RECORDING API CONCEPT 

The following is an architecture example only, not a claim about actual WiseIN API 
endpoints: 
GET /api/meetings/{meetingId} 
GET /api/meetings/{meetingId}/recording 
GET /api/meetings/{meetingId}/transcript 
GET /api/meetings/{meetingId}/summary 
Potential response concepts: 
meeting_id 
recording_available 
recording_status 
recording_url 
recording_created_at 
transcript_available 
summary_available 
access_permission 
The actual WiseIN engineering/API contract must determine: 
• 
endpoint names  
• 
HTTP methods  
• 
authentication  
• 
authorization  
• 
response schema  
• 
status values  
• 
expiration behavior.  
 
50. MEETING RECORDING ENTITY MODEL 
Recommended RAG/API entities: 

meeting 
meeting_id 
meeting_status 
meeting_participant 
participant_id 
host_id 
recording 
recording_id 
recording_status 
recording_available 
recording_created_at 
recording_duration 
recording_url 
transcript 
transcript_id 
transcript_status 
summary 
summary_id 
summary_status 
consent 
consent_status 
privacy 
access_permission 
Only populate fields actually supported by the WiseIN backend. 
 
51. RECOMMENDED RAG METADATA 

document_type = meeting_recording 
module = meetings 
feature = meeting_recording 
source = wisein_official 
content_type = static_policy / product_documentation 
audience = individual / organization 
plan = applicable_plan 
privacy_level = private 
last_verified = YYYY-MM-DD 
For actual recordings, metadata should come from the live meeting system rather than 
static RAG. 
 
52. AI INTENTS FOR MEETING RECORDING 
The chatbot should recognize at least these intents. 
General 
• 
What is meeting recording?  
• 
Does WiseIN record meetings?  
• 
What is AI meeting intelligence?  
• 
What is a meeting transcript?  
• 
What is an AI meeting summary?  
Availability 
• 
Is my meeting recorded?  
• 
Does this meeting have a recording?  
• 
Where is my recording?  
• 
Is my recording ready?  
Access 

• 
Who can see my recording?  
• 
Can the other participant see it?  
• 
Can I access an old recording?  
• 
Why can't I access the recording?  
Privacy 
• 
Can I share a recording?  
• 
Can I post a recording?  
• 
Can I record secretly?  
• 
Can I send a recording to someone else?  
Transcription 
• 
Is there a transcript?  
• 
Where is the transcript?  
• 
Is transcription available?  
• 
Why is the transcript missing?  
AI summary 
• 
Where is my AI summary?  
• 
Why didn't I get a summary?  
• 
Can I share the summary?  
• 
Can I delete the summary?  
Troubleshooting 
• 
Recording missing  
• 
Recording stuck processing  
• 
Recording won't play  
• 
Recording link doesn't work  
• 
Transcript missing  
• 
Summary missing.  

 
53. GOLDEN CHATBOT ANSWERS 
Q: Does WiseIN support meeting recordings? 
WiseIN supports meeting-related AI intelligence and has documented recording-related 
functionality, but the exact current recording workflow and availability for a particular 
meeting should be verified through the current meeting interface or authorized backend. 
WiseIN's policies explicitly address meeting recordings and recording consent.  
 
Q: Does WiseIN record every meeting? 
The public WiseIN documentation does not establish that every meeting is automatically 
recorded. Recording availability should be checked for the specific meeting. 
 
Q: What is an AI meeting summary? 
WiseIN describes its meeting intelligence as generating summaries containing key points, 
follow-ups, and action items after calls.  
 
Q: Does WiseIN provide transcription? 
Yes. WiseIN's current Premium offering explicitly lists AI Meeting Summaries & 
Transcription.  
 
Q: Can I record a WiseIN call secretly? 
No. WiseIN's Content Policies state that both people must know if a call is being recorded. 
Secret recording is not permitted.  
 
Q: Can I share my meeting recording? 
Meeting recordings can contain private conversations. WiseIN's policies prohibit sharing or 
publishing recordings without appropriate permission from the people involved.  
 

Q: Can I post my AI meeting summary? 
WiseIN's Content Policies state that AI meeting summaries are personal and should not be 
publicly posted or shared without the other person's consent.  
 
Q: My meeting ended but I don't see a recording. 
A completed meeting does not automatically confirm that a recording is available. 
Recording availability, processing status, and access permissions should be checked for 
that specific meeting. 
 
Q: How long are meeting recordings stored? 
WiseIN's public Privacy Policy does not specify a universal retention period specifically for 
meeting recordings. The exact retention behavior should be verified through current WiseIN 
product documentation or support.  
 
54. WHAT THE CHATBOT MUST NOT INVENT 
The chatbot must not fabricate: 
• 
automatic recording for every meeting  
• 
exact recording button names  
• 
recording start/stop workflow  
• 
recording duration limits  
• 
maximum recording size  
• 
recording resolution  
• 
recording file format  
• 
recording download format  
• 
recording storage limit  
• 
recording retention period  
• 
automatic deletion  

• 
participant recording permissions  
• 
host ownership  
• 
administrator access  
• 
recording processing time  
• 
transcript processing time  
• 
summary processing time  
• 
transcript language support  
• 
recording export  
• 
Google Drive integration  
• 
OneDrive integration  
• 
Dropbox integration  
• 
automatic email delivery  
• 
recording reminder notifications  
• 
automatic recording notifications  
• 
exact recording URL structure  
• 
recording API endpoints  
• 
backend storage provider.  
This is especially important because the previously provided product documentation 
explicitly says that the screenshots do not establish the complete behavior of meeting 
recording, transcription, AI summaries, permissions, or related technical functionality.  
 
55. SECURITY GUARDRAILS FOR THE AI 
The Meeting Recording chatbot must follow these rules: 
Never ask for: 
• 
password  
• 
OTP  
• 
authentication token  

• 
private API key  
• 
payment credentials.  
Never expose: 
• 
another user's recording  
• 
private transcript  
• 
private meeting URL  
• 
signed storage URL  
• 
participant private information  
• 
organization-private meeting data.  
Never infer: 
• 
recording availability  
• 
participant consent  
• 
recording ownership  
• 
recording status  
• 
deletion  
• 
access permissions.  
Always verify: 
• 
meeting identity  
• 
authenticated user  
• 
access permission  
• 
current recording status.  
 
56. PRIVACY-CRITICAL RESPONSE LOGIC 
When the user asks: 
“Show me my recording.” 
The chatbot should: 

1. Authenticate the user. 
2. Identify the meeting. 
3. Query authorized meeting data. 
4. Check recording availability. 
5. Check recording permission. 
6. Return the recording only if authorized. 
If no recording exists: 
“No accessible recording is currently available for this meeting.” 
Do not say: 
“The host deleted it.” 
unless the backend confirms deletion. 
 
57. IF A RECORDING IS NOT FOUND 
The chatbot should distinguish between: 
Recording does not exist 
        ≠ 
Recording still processing 
        ≠ 
Recording inaccessible 
        ≠ 
Recording deleted 
        ≠ 
Technical failure 
These are different states. 
Only the actual WiseIN backend or verified support information should determine which 
state applies. 

 
58. HUMAN ESCALATION 
The AI should escalate when: 
• 
recording is missing despite confirmed recording availability  
• 
recording processing appears stuck  
• 
recording access is incorrectly denied  
• 
transcript is missing despite confirmed availability  
• 
AI summary is missing despite confirmed entitlement  
• 
recording playback fails repeatedly  
• 
recording privacy appears compromised  
• 
unauthorized recording/sharing is reported  
• 
the issue involves another user's private data  
• 
account-specific permissions cannot be verified.  
When escalating, collect only necessary information: 
• 
meeting name/ID if visible  
• 
approximate date/time  
• 
platform  
• 
exact error  
• 
steps already attempted  
• 
screenshot if voluntarily provided.  
Never request passwords or OTPs. 
 
59. RECORDING PRIVACY INCIDENT 
If a user reports: 
“Someone shared my WiseIN meeting recording without permission.” 
This should be treated as a privacy-related issue. 

The chatbot should: 
1. Avoid asking the user to expose additional private information publicly.  
2. Explain that WiseIN policies prohibit unauthorized sharing of private meetings.  
3. Direct the user to the official reporting/support process.  
4. Escalate when appropriate.  
WiseIN's Content Policies provide reporting mechanisms and state that reports are 
confidential.  
 
60. CONTENT POLICY ENFORCEMENT 
WiseIN's Content Policies describe enforcement actions that can include: 
• 
content removal and warning for minor violations  
• 
temporary feature restrictions  
• 
account review  
• 
immediate action for serious violations  
• 
permanent bans for severe violations such as fraud, identity fraud, data theft, 
threats, or posting private information.  
The chatbot should explain these rules when relevant but should not independently 
determine the enforcement outcome for a specific user. 
 
61. RELATIONSHIP WITH OTHER WISEIN DOCUMENTS 
This document should connect with: 
Meetings 
    ↓ 
Meeting Recording 
    ├── Transcription 
    ├── AI Meeting Summary 
    ├── Privacy 

    ├── Notifications 
    └── Troubleshooting 
 
Meetings 
    ├── Calendar 
    ├── Slot Booking 
    ├── Video Calls 
    ├── Webinars 
    └── Completed Meetings 
The previously supplied WiseIN application documentation recommends separating 
Meetings, Calendar, Webinars, scheduling, and related troubleshooting into distinct 
knowledge areas.  
 
62. DOCUMENTATION BOUNDARY 
Confirmed/current 
WiseIN publicly confirms: 
• 
video-first meetings/calls  
• 
AI meeting intelligence  
• 
AI-generated meeting summaries  
• 
key points/follow-ups/action items  
• 
Premium AI meeting summaries and transcription  
• 
recording-related privacy requirements  
• 
recording consent requirements  
• 
restrictions on sharing recordings  
• 
restrictions on sharing AI summaries.  
Requires product/API verification 

The following remain implementation-dependent: 
• 
exact recording UI  
• 
exact recording controls  
• 
recording storage  
• 
recording retention  
• 
recording download  
• 
recording ownership  
• 
recording access model  
• 
recording status values  
• 
processing time  
• 
transcript UI  
• 
transcript export  
• 
summary UI  
• 
deletion workflow  
• 
recording notifications.  
The supplied WiseIN product documentation explicitly marks these areas as requiring 
verification rather than treating them as confirmed behavior.  
 
63. FINAL KNOWLEDGE BASE SUMMARY 
WiseIN Meeting Recording is part of the platform's video-meeting and meeting-intelligence 
ecosystem. 
 
WiseIN's current website describes video-first conversations and Meeting Intelligence. 
After a call, WiseIN describes AI-generated meeting summaries containing key points, 
follow-ups, and action items. The current Premium offering explicitly includes AI Meeting 
Summaries & Transcription. 
 

WiseIN's Content Policies specifically recognize meeting recordings as platform content. 
They state that WiseIN calls are private, AI meeting summaries are personal, and if a call is 
recorded, both people must know. Secretly recording another participant is not permitted. 
 
Meeting recordings, transcripts, and AI summaries are different concepts and must not be 
treated as interchangeable. 
 
The chatbot must not assume that every meeting is automatically recorded. It must not 
invent recording buttons, recording limits, retention periods, download formats, ownership 
rules, participant permissions, processing times, or technical implementation details. 
 
For general questions, the chatbot should use RAG based on approved WiseIN 
documentation and policies. 
 
For account-specific questions such as whether a particular meeting has a recording, 
whether a recording is ready, whether a transcript exists, or whether the user has access, 
the chatbot should use authorized live WiseIN APIs where available. 
 
Private recordings, transcripts, summaries, participant information, and meeting URLs 
must nev 
 
 



---

