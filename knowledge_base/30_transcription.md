# Transcription

## Source: WISEIN-TRANSCRIPTION-030.pdf

WISEIN  — TRANSCRIPTION  
Document ID: WISEIN-TRANSCRIPTION-030 
Purpose: AI Chatbot / RAG / Customer Support / Product Knowledge 
Platform: WiseIN 
 
1. WHAT IS TRANSCRIPTION? 
Transcription is the conversion of spoken conversation from a WiseIN meeting or call into 
written text. 
Conceptually: 
WiseIN Video Meeting 
        ↓ 
     Spoken Audio 
        ↓ 
   Transcription 
        ↓ 
 Written Conversation 
Transcription is different from an AI summary. 
Transcription 
Attempts to represent what was said during the meeting in written form. 
AI Meeting Summary 
Condenses meeting information into useful highlights such as: 
• 
key points  
• 
follow-ups  
• 
action items.  
WiseIN's homepage describes its Meeting Intelligence as generating summaries containing 
these elements.  
Meeting Recording 

The recorded audio/video content of a meeting, where recording is supported. 
These three concepts should remain separate in the chatbot knowledge base. 
 
2. WISEIN'S CURRENT TRANSCRIPTION FEATURE 
WiseIN's current India-facing homepage lists: 
AI Meeting Summaries & Transcription 
under its Premium plan.  
The global WiseIN pricing page also lists Premium as providing: 
Unlimited video calls with AI summaries.  
The official WiseIN mobile-app page states that users can: 
• 
book and join video calls  
• 
read AI meeting summaries after calls  
• 
manage availability and slot bookings.  
Therefore, transcription belongs to WiseIN's broader AI-powered meeting intelligence 
functionality. 
 
3. TRANSCRIPTION AND MEETING INTELLIGENCE 
WiseIN's homepage presents the meeting experience as: 
Video Call 
    ↓ 
Meeting Intelligence 
    ↓ 
AI-generated meeting information 
    ├── Key Points 
    ├── Follow-ups 
    └── Action Items 

WiseIN describes this as a way for users to participate in conversations without having to 
manually take notes.  
Transcription can be considered a separate layer of the meeting-intelligence system: 
Meeting 
   │ 
   ├── Recording 
   │ 
   ├── Transcription 
   │ 
   └── AI Summary 
          ├── Key Points 
          ├── Follow-ups 
          └── Action Items 
The chatbot must not assume that availability of one automatically proves availability of 
the others. 
 
4. TRANSCRIPTION VS AI SUMMARY 
This distinction is critical. 
Example 
Suppose two people have a 30-minute career discussion. 
The transcript may contain the conversation in written form. 
The AI summary may instead contain: 
Key Points: 
- Discussed software engineering opportunities. 
 
Follow-ups: 

- Review the candidate's profile. 
 
Action Items: 
- Schedule another discussion. 
The summary is therefore not a replacement for the complete transcript. 
The exact format and content of WiseIN's current transcript output are not publicly 
documented and should not be invented. 
 
5. TRANSCRIPTION VS MEETING RECORDING 
A recording is media. 
A transcript is text. 
Conceptually: 
Recording 
   ↓ 
Audio / Video 
   ↓ 
Speech 
   ↓ 
Transcription 
   ↓ 
Text 
A transcript may be generated from a supported meeting recording or meeting-audio 
processing workflow, but the public WiseIN documentation does not establish the exact 
current technical pipeline. 
Therefore, the chatbot should not state that: 
“Every recording automatically produces a transcript.” 
unless the live product/API confirms it. 

 
6. DOES WISEIN SUPPORT TRANSCRIPTION? 
Yes. 
WiseIN's current official website explicitly lists AI Meeting Summaries & Transcription as 
a Premium feature.  
A safe chatbot response is: 
WiseIN supports AI meeting transcription as part of its Premium meeting-intelligence 
features. The exact availability and behavior for an individual meeting should be 
checked against the current meeting and account state. 
 
7. WHO GETS TRANSCRIPTION? 
The current India-facing WiseIN homepage lists AI Meeting Summaries & Transcription 
under Premium.  
The public pricing page lists Basic, Premium, Student, and Organization plans, but it does 
not provide a complete transcription entitlement matrix for every plan and meeting type.  
Therefore: 
Confirmed 
Premium currently advertises AI Meeting Summaries & Transcription. 
Not confirmed 
The public documentation does not establish whether: 
• 
Basic users receive transcription  
• 
Student users receive transcription  
• 
Organization users receive transcription under every meeting type  
• 
guests receive transcription  
• 
every meeting automatically receives transcription.  
The chatbot must verify account-specific entitlement through authorized product data 
when required. 
 

8. TRANSCRIPTION AND PREMIUM 
Current WiseIN India pricing presents Premium at ₹499/month and lists: 
• 
Unlimited meaningful conversations  
• 
AI Meeting Summaries & Transcription  
• 
Smart Slot Booking  
• 
Advanced profile analytics  
• 
AI Discovery in Search  
• 
Audio Rooms Hosting  
• 
Publish Posts & Clips  
• 
Premium Profile Badge  
• 
Priority Support.  
The global pricing page presents Premium at $10/month and includes unlimited video calls 
with AI summaries.  
The chatbot should use the pricing configuration applicable to the user's current 
region/account rather than mixing India and global prices. 
 
9. TRANSCRIPTION AND VIDEO CALLS 
WiseIN describes itself as a video-first networking platform. 
Its official website says users can book a video call and talk face-to-face.  
The mobile application page also states that users can book and join video calls and read 
AI meeting summaries after calls.  
Therefore: 
Profile / Slot 
      ↓ 
Meeting 
      ↓ 
Video Call 

      ↓ 
Meeting Intelligence 
      ├── Transcription 
      └── AI Summary 
The exact conditions under which transcription begins must be obtained from the current 
product behavior. 
 
10. IS TRANSCRIPTION AUTOMATIC? 
The public WiseIN pages confirm the existence of transcription but do not provide a 
sufficiently detailed current specification of whether transcription: 
• 
starts automatically  
• 
requires a user action  
• 
requires recording  
• 
requires participant consent  
• 
is generated after the meeting  
• 
is available only for selected meeting types.  
Therefore the chatbot must not claim any of these as universal behavior. 
Safe response 
WiseIN currently offers AI meeting transcription, but the exact transcription workflow for a 
particular meeting depends on the current meeting functionality and account access. 
 
11. TRANSCRIPTION CONSENT AND PRIVACY 
This is a critical section. 
WiseIN's Content Policies state that: 
• 
WiseIN calls are private.  
• 
Recordings, transcripts, and AI summaries must not be shared or published without 
explicit permission from the other person.  

• 
If a call is recorded, both people must know.  
Therefore, transcripts should be treated as potentially private meeting information. 
Chatbot rule 
Never tell users: 
“You can freely publish your transcript.” 
Instead: 
WiseIN treats meeting transcripts as private meeting content. Do not share or publish 
a transcript without the appropriate permission from the people involved.  
 
12. TRANSCRIPTION AND RECORDING CONSENT 
WiseIN's Content Policies specifically state: 
If a call is being recorded, both people must know. 
They prohibit secretly recording another person.  
The chatbot should therefore distinguish between: 
• 
transcription  
• 
recording  
• 
consent.  
It must not assume that transcription removes the need to respect meeting privacy. 
 
13. TRANSCRIPT PRIVACY 
A transcript can contain: 
• 
names  
• 
career information  
• 
personal information  
• 
business discussions  
• 
company information  

• 
confidential plans  
• 
salary information  
• 
project information  
• 
private opinions  
• 
contact details.  
WiseIN's Content Policies prohibit publicly sharing private conversations and sensitive 
information without appropriate permission.  
Therefore, transcripts should be treated as sensitive information when they contain such 
content. 
 
14. CAN I SHARE A TRANSCRIPT? 
A user should not assume that because they participated in a meeting they can publicly 
distribute the complete transcript. 
WiseIN's Content Policies explicitly state that recordings, transcripts, and AI summaries of 
a call should not be shared or published without explicit permission from the other person.  
Recommended chatbot answer 
You should not publicly share a WiseIN meeting transcript without the appropriate 
permission from the other participant. WiseIN's Content Policies treat transcripts of calls 
as private meeting content.  
 
15. CAN I POST A TRANSCRIPT AS A WISEIN POST? 
Not automatically. 
A transcript is derived from a private conversation. 
WiseIN's Content Policies prohibit publicly posting private conversations without consent.  
Therefore: 
Meeting Transcript 
       ↓ 
Private meeting content 

       ↓ 
Permission required 
       ↓ 
Potentially shareable only when appropriate consent exists 
The chatbot must not encourage users to copy and paste private transcripts into Posts, 
Communities, Clips, or other public areas. 
 
16. TRANSCRIPTION AND AI SUMMARY ARE NOT PUBLIC CONTENT 
Both should be treated as meeting-related information. 
The Content Policies specifically say the AI meeting summary is for the user and should not 
be publicly posted or shared without consent.  
The same privacy principle applies to transcripts because the policy explicitly includes 
transcripts among private meeting content.  
 
17. TRANSCRIPTION LANGUAGE SUPPORT 
The current public WiseIN website does not document a complete list of supported 
transcription languages. 
Therefore, the chatbot must not claim that WiseIN transcription supports: 
• 
English  
• 
Telugu  
• 
Hindi  
• 
Tamil  
• 
Telugu + English mixed speech  
• 
automatic language detection  
as confirmed product capabilities unless current product/API documentation establishes 
them. 
Safe answer 

WiseIN publicly confirms AI meeting transcription, but its public documentation does not 
currently specify the complete list of supported transcription languages. 
 
18. MULTILINGUAL TRANSCRIPTION 
Do not assume that a conversation containing multiple languages will automatically be 
transcribed correctly. 
For example: 
English + Telugu 
English + Hindi 
English + Hindi + Telugu 
may require language-specific processing. 
The current public documentation does not establish WiseIN's exact multilingual 
transcription behavior. 
Therefore, the chatbot should not promise multilingual accuracy. 
 
19. TRANSCRIPTION ACCURACY 
No public WiseIN source located for this documentation provides a guaranteed 
transcription accuracy percentage. 
Therefore, never state: 
“WiseIN transcription is 99% accurate.” 
or any other unsupported accuracy number. 
Transcription can potentially be affected by: 
• 
audio quality  
• 
background noise  
• 
microphone quality  
• 
overlapping speakers  
• 
pronunciation  

• 
language  
• 
accents  
• 
connection quality.  
These are general technical considerations, not claims about WiseIN's measured accuracy. 
 
20. SPEAKER IDENTIFICATION 
A transcript may conceptually distinguish speakers, for example: 
Speaker 1: 
... 
 
Speaker 2: 
... 
However, the current public WiseIN documentation does not establish whether its 
transcription system provides: 
• 
speaker labels  
• 
participant names  
• 
speaker diarization  
• 
automatic participant identification.  
Therefore, do not promise speaker identification. 
 
21. TIMESTAMPS 
The current public WiseIN sources do not establish whether transcripts contain: 
• 
timestamps  
• 
clickable timestamps  
• 
speaker timestamps  
• 
chapter markers.  

Therefore, the chatbot should not claim that transcripts contain timestamps. 
 
22. TRANSCRIPT EDITING 
The public WiseIN documentation does not establish whether users can manually: 
• 
edit transcript text  
• 
correct words  
• 
rename speakers  
• 
delete transcript sections  
• 
search within transcripts  
• 
highlight transcript sections.  
These should remain unverified. 
 
23. TRANSCRIPT SEARCH 
Do not claim that WiseIN currently provides a global transcript-search feature. 
A transcript may exist without being indexed for platform-wide search. 
If a user asks: 
“Can I search all my meeting transcripts?” 
the chatbot should check the current product/API capability rather than inventing a 
workflow. 
 
24. TRANSCRIPT DOWNLOAD 
The public WiseIN documentation does not establish a universal transcript-download 
feature. 
Do not claim that users can download transcripts as: 
• 
TXT  
• 
PDF  
• 
DOCX  

• 
CSV  
• 
JSON  
• 
SRT  
• 
VTT.  
These formats require explicit product verification. 
 
25. TRANSCRIPT EXPORT 
Similarly, there is currently no verified public specification establishing integrations such 
as: 
• 
Google Docs  
• 
Google Drive  
• 
Notion  
• 
Microsoft Word  
• 
OneDrive  
• 
Dropbox  
• 
CRM systems.  
Do not invent integrations. 
 
26. TRANSCRIPTION PROCESSING 
A transcription system may need to process meeting audio before a transcript becomes 
available. 
However, WiseIN's public documentation does not establish an exact processing time. 
Do not promise: 
“Your transcript will be ready within five minutes.” 
Instead: 

If a transcript is still processing, its availability depends on the current WiseIN 
meeting system. Check the meeting status or contact support if it remains 
unavailable. 
 
27. TRANSCRIPTION STATUS 
The following are useful conceptual states for the chatbot/API architecture: 
Not Available 
Processing 
Ready 
Failed 
Restricted 
Deleted 
These are not confirmed WiseIN status labels. 
The actual backend status values must be used if WiseIN exposes them. 
 
28. TRANSCRIPT NOT AVAILABLE 
A missing transcript does not automatically mean that: 
• 
the meeting was not recorded  
• 
the transcript was deleted  
• 
the user is not eligible  
• 
the participant refused consent  
• 
the system failed.  
The chatbot must first verify the actual meeting state. 
Possible causes may include: 
Meeting not eligible 
       OR 
Transcription not enabled 

       OR 
Still processing 
       OR 
Permission restriction 
       OR 
Technical failure 
       OR 
No transcript generated 
Only verified product data should determine the actual cause. 
 
29. TRANSCRIPTION TROUBLESHOOTING 
If a user says: 
“My transcript is missing.” 
The chatbot should check: 
1. Was the meeting completed?  
2. Was transcription supported for that meeting?  
3. Does the account have the required feature entitlement?  
4. Is the transcript still processing?  
5. Does the user have permission to access it?  
6. Is there an error message?  
7. Is the meeting associated with the correct account?  
If live backend access exists, use it. 
Otherwise, do not guess. 
 
30. “MY MEETING ENDED BUT THERE IS NO TRANSCRIPT” 
Recommended answer: 

A completed meeting does not by itself confirm that a transcript is available. WiseIN 
supports AI meeting transcription, but transcript availability depends on the applicable 
meeting and account functionality. Please check the meeting's current status or the 
available meeting-intelligence information. 
 
31. “TRANSCRIPTION IS STUCK” 
Recommended troubleshooting: 
1. Check whether the meeting is fully completed.  
2. Refresh the meeting information.  
3. Check whether a processing status is displayed.  
4. Confirm the correct account is being used.  
5. Record the exact error message if one is shown.  
6. If the transcript remains unavailable, escalate to WiseIN support.  
Do not promise a processing deadline unless WiseIN provides one. 
 
32. “TRANSCRIPT IS WRONG” 
The chatbot should avoid claiming that the platform has malfunctioned solely because a 
user identifies an incorrect word. 
A transcription can contain recognition errors. 
The chatbot can say: 
AI-generated transcripts may contain inaccuracies. If WiseIN provides a transcript 
correction feature in the current interface, use that feature; otherwise report the specific 
issue through the available support process. 
Do not invent a correction button or workflow. 
 
33. “TRANSCRIPT HAS THE WRONG SPEAKER” 
If speaker labels are available, the chatbot should use the actual product functionality. 
If they are not confirmed: 

WiseIN's public documentation does not currently specify the exact speaker-identification 
behavior of meeting transcription. 
Do not claim that the system automatically identifies every participant by name. 
 
34. “TRANSCRIPT IS IN THE WRONG LANGUAGE” 
Recommended response: 
WiseIN publicly confirms AI meeting transcription, but its public documentation does not 
currently specify the complete supported-language or language-switching behavior. If the 
transcript is incorrect, provide the meeting details and displayed issue to WiseIN support. 
 
35. “CAN I TRANSCRIBE AN OLD MEETING?” 
Do not automatically promise that old meetings can be transcribed. 
The current public documentation does not establish: 
• 
whether historical meetings can be reprocessed  
• 
how long recordings remain available  
• 
whether users can request transcription after a meeting  
• 
whether transcription can be regenerated.  
Use live product information if available. 
 
36. “CAN I TRANSCRIBE A MEETING THAT WAS NOT RECORDED?” 
Do not assume yes or no without the actual WiseIN implementation. 
The public documentation does not establish whether WiseIN can independently process 
a meeting's audio without a recording being available. 
Safe answer: 
The current public WiseIN documentation does not specify whether a transcript can be 
generated for a meeting that has no accessible recording. This depends on the actual 
meeting-processing workflow. 
 

37. TRANSCRIPTION AND MEETING RECORDING DOCUMENT 
The relationship between the two documents should be: 
Meeting Recording Documentation 
        ↓ 
Recording 
Privacy 
Consent 
Access 
Storage 
Recording troubleshooting 
 
Transcription Documentation 
        ↓ 
Transcript 
AI transcription 
Privacy 
Language 
Processing 
Transcript troubleshooting 
They should not be merged into one feature because a recording and a transcript are 
different data objects. 
 
38. TRANSCRIPTION AND AI MEETING SUMMARY 
The relationship should be: 
Meeting 
  │ 

  ├───────────────┐ 
  ↓               ↓ 
Transcript      AI Summary 
  │               │ 
  │               ├── Key Points 
  │               ├── Follow-ups 
  │               └── Action Items 
  │ 
  └── Detailed written conversation 
WiseIN publicly describes the AI summary as containing key points, follow-ups, and action 
items.  
 
39. TRANSCRIPTION AND NOTIFICATIONS 
WiseIN has a notification system and its app supports notifications related to platform 
activity. 
However, the public sources do not establish a dedicated notification specification for: 
• 
transcript ready  
• 
transcript failed  
• 
transcript processing  
• 
summary ready.  
Therefore, the chatbot must not promise that users will always receive a notification when 
a transcript becomes available. 
If the current live notification API confirms such a notification, the API should be the source 
of truth. 
 
40. TRANSCRIPTION AND PRIVACY POLICY 

WiseIN's Privacy Policy states that the platform collects information users provide and 
information generated through their use of the platform, including content and usage 
information. It also states that WiseIN uses security measures, encryption, and access 
controls to protect sensitive information.  
The policy says users have control over certain information and can request deletion, 
subject to legal, security, backup, and other retention requirements.  
However, the Privacy Policy does not establish a separate exact retention period 
specifically for meeting transcripts. 
Therefore, do not invent a transcript-specific retention period. 
 
41. TRANSCRIPTION DATA RETENTION 
WiseIN's general Privacy Policy says: 
• 
account information may be retained while an account is active  
• 
posts/messages/content may be retained until deletion/account closure  
• 
deleted content may remain temporarily in backups for technical or legal reasons  
• 
some information may be retained for legal, tax, compliance, fraud prevention, or 
security purposes.  
These general rules should not automatically be interpreted as a specific transcript 
retention policy. 
The chatbot should say: 
WiseIN's public Privacy Policy does not currently specify a dedicated retention period for 
meeting transcripts. 
 
42. USER DATA CONTROL 
WiseIN states that users can access, update, or request deletion of their information, 
subject to applicable retention requirements.  
If a user asks: 
“Delete my transcript.” 
The chatbot must determine whether WiseIN provides a transcript-specific deletion action. 

If no verified workflow exists: 
I don't have a verified current WiseIN transcript-deletion workflow. WiseIN's Privacy 
Policy provides general data-control and deletion mechanisms, subject to applicable 
exceptions. 
 
43. TRANSCRIPTION AND SENSITIVE INFORMATION 
A transcript may contain sensitive information. 
WiseIN's Content Policies prohibit public sharing of: 
• 
financial information  
• 
ID proofs  
• 
salary details  
• 
internal company information  
• 
business strategies  
• 
other private information.  
Therefore: 
A transcript should not be treated as ordinary public content. 
 
44. TRANSCRIPTION AND CONFIDENTIAL BUSINESS INFORMATION 
A professional meeting may involve: 
• 
product plans  
• 
customer information  
• 
internal strategy  
• 
hiring discussions  
• 
salary information  
• 
technical designs  
• 
business negotiations.  

The chatbot should advise users to respect confidentiality and WiseIN's privacy/content 
policies. 
Do not reproduce or expose confidential meeting information in an AI support response 
unless it is necessary and authorized. 
 
45. TRANSCRIPTION AND COPYRIGHT 
A meeting may contain copyrighted: 
• 
presentations  
• 
documents  
• 
images  
• 
videos  
• 
demonstrations  
• 
third-party content.  
WiseIN's Content Policies require users to share content they created or have permission 
to use and prohibit stolen or copyrighted content from being presented as one's own.  
Therefore, a transcript does not automatically grant permission to redistribute copyrighted 
material discussed during the meeting. 
 
46. TRANSCRIPTION AND ORGANIZATION MEETINGS 
WiseIN's Organization platform supports professional meetings and organization-level 
collaboration. 
The exact organization-level transcription permissions are not publicly documented. 
Therefore, do not assume: 
• 
organization admins can read all employee transcripts  
• 
managers automatically receive transcripts  
• 
all meeting participants automatically receive transcripts  
• 
organization owners can delete employee transcripts.  

These must be determined from the actual authorization system. 
 
47. TRANSCRIPTION AND WEBINARS 
Webinars are a separate WiseIN feature area. 
The previously provided WiseIN product documentation explicitly requires Meetings and 
Webinars to be treated as distinct feature areas.  
Therefore: 
Meeting Transcription 
        ≠ 
Webinar Transcription 
Do not automatically state that every webinar receives a transcript. 
If a particular webinar supports transcription, the chatbot should use the verified webinar-
specific documentation/API. 
 
48. TRANSCRIPTION AND EVENTS 
The previously supplied WiseIN product documentation says that post-event resources 
such as recordings and summaries must be verified for each applicable event category.  
Therefore, the chatbot must not assume: 
Event completed → transcript available. 
Instead: 
Check the specific event type and available post-event resources. 
 
49. TRANSCRIPTION AND SLOT BOOKING 
Slot Booking determines availability for meetings. 
It does not itself guarantee transcription. 
Conceptually: 
Slot Booking 

     ↓ 
Meeting Scheduled 
     ↓ 
Video Meeting 
     ↓ 
Meeting Intelligence 
     ├── Transcription 
     └── AI Summary 
A booked slot therefore does not mean that a transcript already exists. 
 
50. TRANSCRIPTION AND CALENDAR 
Calendar information describes scheduling. 
A transcript is meeting-content information. 
Therefore: 
Calendar 
  ↓ 
When is the meeting? 
 
Meeting 
  ↓ 
What meeting occurred? 
 
Transcription 
  ↓ 
What was said? 
 

AI Summary 
  ↓ 
What were the important points? 
The chatbot should retrieve these from separate data sources. 
 
51. RAG VS LIVE API 
This is one of the most important implementation rules. 
RAG should answer: 
• 
What is transcription?  
• 
Does WiseIN support transcription?  
• 
Which plan currently advertises transcription?  
• 
What is the difference between transcript and summary?  
• 
What are WiseIN's transcript privacy rules?  
• 
Can a transcript be publicly shared?  
• 
What does WiseIN say about meeting privacy?  
Live API should answer: 
• 
Does this specific meeting have a transcript?  
• 
Is the transcript ready?  
• 
Is it still processing?  
• 
Does the current user have access?  
• 
Is transcription available for this meeting?  
• 
Is the transcript deleted?  
• 
What is the transcript's current status?  
• 
Is the transcript associated with the correct meeting?  
The supplied WiseIN product documentation explicitly says account-specific meeting 
questions should use reliable live WiseIN data where appropriate tools and permissions 
exist and that the AI must not invent meeting information.  

 
52. RECOMMENDED CHATBOT ARCHITECTURE 
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
RAG Knowledge Base       Meeting API 
 │                             │ 
 │                             ├── Meeting 
 │                             ├── Transcript 
 │                             ├── Transcript Status 
 │                             ├── Access Permission 
 │                             └── AI Summary 
 │ 
 └──────────────┬──────────────┘ 

                ↓ 
               LLM 
                ↓ 
        Safe Final Response 
The LLM should never receive unrestricted database access. 
 
53. RECOMMENDED TRANSCRIPTION API CONCEPT 
The following is an architecture example only, not an assertion about actual WiseIN API 
endpoints: 
GET /api/meetings/{meetingId}/transcript 
GET /api/meetings/{meetingId}/transcript/status 
GET /api/meetings/{meetingId}/summary 
Possible conceptual response: 
meeting_id 
transcript_id 
transcript_status 
transcript_available 
transcript_text 
language 
created_at 
updated_at 
access_permission 
These field names are examples. 
The actual WiseIN backend contract must determine the real API. 
 
54. TRANSCRIPTION ENTITY MODEL 

Recommended entities for the chatbot: 
meeting 
meeting_id 
participant 
participant_id 
 
transcription 
transcript_id 
transcript_status 
transcript_available 
transcript_text 
language 
created_at 
updated_at 
 
summary 
summary_id 
summary_status 
 
permission 
access_permission 
 
privacy 
consent 
Only fields actually supported by the WiseIN backend should be populated. 
 

55. RAG METADATA 
Recommended metadata: 
document_type = transcription 
module = meetings 
feature = transcription 
source = wisein_official 
content_type = product_documentation / policy 
audience = individual / organization 
privacy_level = private 
plan = premium / applicable_plan 
last_verified = 2026-09 
For an actual transcript, use live meeting metadata rather than static RAG content. 
 
56. AI INTENTS FOR TRANSCRIPTION 
The chatbot should recognize at least these intents. 
General 
• 
What is transcription?  
• 
What is a meeting transcript?  
• 
Does WiseIN support transcription?  
• 
How does transcription relate to AI summaries?  
Availability 
• 
Is transcription available?  
• 
Does my meeting have a transcript?  
• 
Can I transcribe this meeting?  
• 
Is transcription included in my plan?  
Status 

• 
Is my transcript ready?  
• 
Why is my transcript processing?  
• 
Where is my transcript?  
• 
Why is my transcript missing?  
Privacy 
• 
Can I share a transcript?  
• 
Can I publish a transcript?  
• 
Can someone else see my transcript?  
• 
Is my transcript private?  
Language 
• 
What languages does WiseIN transcription support?  
• 
Can I transcribe Telugu?  
• 
Can I transcribe Hindi?  
• 
Can I transcribe a multilingual meeting?  
Only answer language-specific questions from verified product data. 
Quality 
• 
Why is the transcript inaccurate?  
• 
Why are words missing?  
• 
Why are speakers incorrect?  
Data management 
• 
Can I edit the transcript?  
• 
Can I delete it?  
• 
Can I download it?  
• 
Can I export it?  
Only answer these from verified current functionality. 
 

57. GOLDEN CHATBOT ANSWERS 
Q: What is transcription? 
Transcription converts spoken meeting content into written text. On WiseIN, transcription 
is part of the platform's AI meeting-intelligence offering. 
 
Q: Does WiseIN support transcription? 
Yes. WiseIN currently lists AI Meeting Summaries & Transcription as a Premium feature.  
 
Q: What is the difference between transcription and AI summary? 
A transcript represents the meeting conversation in written form, while an AI summary 
condenses the meeting into important information such as key points, follow-ups, and 
action items.  
 
Q: Is transcription available on Premium? 
Yes. WiseIN's current India Premium offering explicitly includes AI Meeting Summaries & 
Transcription.  
 
Q: Can I share my transcript publicly? 
Meeting transcripts are treated as private meeting content. WiseIN's Content Policies say 
recordings, transcripts, and AI summaries should not be shared or published without 
explicit permission from the other person.  
 
Q: Can I post my transcript as a WiseIN Post? 
Not without considering the privacy and consent requirements. WiseIN prohibits publicly 
sharing private meeting conversations without appropriate consent.  
 
Q: Can I share my AI summary? 

WiseIN's Content Policies state that AI meeting summaries are personal and should not be 
publicly posted or shared without the other person's consent.  
 
Q: My transcript is missing. What should I do? 
First check whether the meeting has completed and whether a transcript is available or still 
processing. If the transcript remains unavailable, check the displayed meeting status or 
contact WiseIN support. The public documentation does not establish a universal 
transcript-generation or processing time. 
 
Q: What languages does WiseIN transcription support? 
WiseIN publicly confirms AI meeting transcription, but its current public documentation 
does not specify the complete list of supported transcription languages. 
 
Q: Can I download my transcript? 
The current public WiseIN documentation does not confirm a universal transcript-
download feature. Check the current meeting interface for an available export/download 
option. 
 
Q: How long does WiseIN keep transcripts? 
WiseIN's public Privacy Policy does not specify a dedicated retention period specifically for 
meeting transcripts. General data-retention rules apply according to the type and purpose 
of the information.  
 
58. WHAT THE CHATBOT MUST NOT INVENT 
The AI must not fabricate: 
• 
transcription accuracy percentage  
• 
supported languages  
• 
automatic language detection  
• 
automatic transcription for every meeting  

• 
exact transcription start time  
• 
transcript processing time  
• 
transcript retention period  
• 
transcript file format  
• 
transcript download feature  
• 
transcript export feature  
• 
speaker identification  
• 
speaker names  
• 
timestamps  
• 
searchable transcripts  
• 
transcript editing  
• 
transcript correction  
• 
transcript deletion workflow  
• 
transcript sharing workflow  
• 
organization-admin transcript access  
• 
transcript ownership  
• 
external transcript integrations  
• 
API endpoints  
• 
backend transcription provider  
• 
transcription model  
• 
AI model used for transcription.  
These are implementation details that are not established by the current public WiseIN 
sources. 
 
59. SECURITY GUARDRAILS 
The transcription chatbot must never request: 

• 
password  
• 
OTP  
• 
authentication code  
• 
API key  
• 
session token  
• 
payment credentials.  
The chatbot must never expose: 
• 
another person's transcript  
• 
private meeting content  
• 
participant private information  
• 
private meeting URLs  
• 
backend storage locations  
• 
signed download URLs  
• 
internal API credentials.  
For account-specific transcript requests, authentication and authorization must happen 
before retrieving the transcript. 
 
60. PRIVATE TRANSCRIPT ACCESS FLOW 
If a user asks: 
“Show me the transcript from yesterday's meeting.” 
The system should follow: 
1. Authenticate user 
        ↓ 
2. Identify meeting 
        ↓ 
3. Retrieve meeting record 

        ↓ 
4. Check transcript availability 
        ↓ 
5. Check user authorization 
        ↓ 
6. Retrieve transcript 
        ↓ 
7. Return authorized content 
If authorization fails: 
Do not reveal the transcript or private meeting information. 
 
61. TRANSCRIPTION PRIVACY INCIDENT 
If a user reports: 
“Someone shared my WiseIN transcript without my permission.” 
The chatbot should treat this as a privacy issue. 
Recommended response: 
WiseIN's Content Policies state that recordings, transcripts, and AI summaries of calls 
should not be shared or published without explicit permission from the other person. You 
should report the issue through WiseIN's available support/reporting process.  
WiseIN's Content Policies state that reports are confidential and are reviewed within 24 
hours.  
 
62. HUMAN ESCALATION 
Escalate when: 
• 
transcript is missing despite confirmed availability  
• 
transcript processing appears stuck  
• 
transcript access is incorrectly denied  

• 
transcript contains serious technical errors  
• 
privacy has potentially been violated  
• 
unauthorized transcript sharing is reported  
• 
account entitlement cannot be verified  
• 
the user asks for information unavailable in approved documentation  
• 
a backend/API problem is suspected.  
Collect only necessary diagnostic information: 
• 
meeting name/ID if visible  
• 
approximate meeting date/time  
• 
transcript status  
• 
displayed error  
• 
platform/device when relevant  
• 
steps already attempted  
• 
screenshot if voluntarily supplied.  
Never request passwords or OTPs. 
 
63. TRANSCRIPTION TROUBLESHOOTING DECISION TREE 
User reports transcript issue 
          ↓ 
Is the meeting identifiable? 
      ┌───┴───┐ 
     No       Yes 
     ↓         ↓ 
 Ask for     Check meeting 
 meeting     completion 
 details         ↓ 

             Is transcript available? 
              ┌───┴───┐ 
             No       Yes 
             ↓         ↓ 
       Check status   Check 
       / entitlement access 
             ↓         ↓ 
         Processing?  Authorized? 
          ┌──┴──┐     ┌──┴──┐ 
         Yes    No    Yes   No 
          ↓     ↓      ↓     ↓ 
       Wait/   Escalate Return Do not 
       status  issue   data   expose 
The exact backend states should replace the conceptual states once WiseIN API 
documentation is available. 
 
64. TRANSCRIPTION KNOWLEDGE CLASSIFICATION 
Recommended RAG classification: 
module: Meetings 
 
feature: Transcription 
feature: Meeting Transcript 
feature: AI Meeting Intelligence 
feature: AI Meeting Summary 
 
policy: Transcript Privacy 

policy: Meeting Privacy 
policy: Recording Consent 
 
troubleshooting: Missing Transcript 
troubleshooting: Transcript Processing 
troubleshooting: Transcript Access 
troubleshooting: Transcript Quality 
 
subscription: Premium Transcription 
This makes retrieval more accurate. 
 
65. RELATIONSHIP WITH RELATED DOCUMENTS 
The Transcription document should link conceptually to: 
Meetings 
   ↓ 
Meeting Recording 
   ↓ 
Transcription 
   ↓ 
AI Meeting Summary 
and also: 
Meetings 
 ├── Calendar 
 ├── Slot Booking 
 ├── Notifications 
 ├── Webinars 

 ├── Events 
 └── Meeting Recording 
The previously provided WiseIN product documentation specifically recommends keeping 
Meetings, Calendar, Webinars, recording, transcription, and AI summaries as separately 
verified areas rather than assuming the screenshots establish their complete workflows.  
 
66. SOURCE PRIORITY FOR TRANSCRIPTION 
When the AI answers a transcription question, use this hierarchy: 
Priority 1 — Live WiseIN API 
For: 
• 
transcript availability  
• 
transcript status  
• 
account entitlement  
• 
meeting-specific access  
• 
private transcript data.  
Priority 2 — Current WiseIN product UI 
For: 
• 
current buttons  
• 
navigation  
• 
status labels  
• 
current workflow.  
Priority 3 — Official WiseIN website 
For: 
• 
feature availability  
• 
plan information  
• 
public product descriptions.  

Priority 4 — Official WiseIN policies 
For: 
• 
privacy  
• 
consent  
• 
sharing  
• 
security  
• 
content rules.  
Priority 5 — Approved internal documentation 
For: 
• 
verified product workflows  
• 
API behavior  
• 
support procedures.  
Never use 
• 
guesses  
• 
invented API behavior  
• 
old screenshots as current behavior without verification  
• 
generic AI assumptions presented as WiseIN facts.  
 
67. FINAL AUTHORITATIVE KNOWLEDGE BASE SUMMARY 
WISEIN TRANSCRIPTION 
 
WiseIN supports AI meeting transcription as part of its meeting-intelligence 
functionality. The current WiseIN India Premium offering explicitly lists 
"AI Meeting Summaries & Transcription." 
 
Transcription and AI meeting summaries are separate concepts. 

 
A transcript represents spoken meeting content in written form, while an 
AI summary condenses meeting information into useful elements such as key 
points, follow-ups, and action items. 
 
WiseIN's public website describes its Meeting Intelligence as generating 
AI summaries after calls, and its mobile-app page states that users can read 
AI meeting summaries after calls. 
 
WiseIN's Content Policies treat meeting recordings, transcripts, and AI 
summaries as private meeting content. Users must not share or publish 
recordings, transcripts, or AI summaries of calls without appropriate 
permission from the other person. 
 
If a call is recorded, both people must know. Secretly recording another 
person is prohibited. 
 
The chatbot must not assume that every meeting automatically produces a 
transcript. It must also not invent transcription languages, processing 
times, accuracy percentages, speaker identification, timestamps, download 
formats, retention periods, editing features, export integrations, or API 
behavior unless these are verified through current WiseIN documentation or 
live product data. 
 
General questions about transcription should be answered through the RAG 
knowledge base. 

 
Account-specific questions such as whether a particular meeting has a 
transcript, whether the transcript is ready, or whether the current user 
has access must use authorized live WiseIN data where available. 
 
Private transcripts must never be exposed without authentication and 
authorization. 
 
If a transcript is missing, the chatbot should verify meeting completion, 
transcription availability, processing status, entitlement, and access 
permission before concluding that there is a problem. 
 
Privacy violations, unauthorized sharing, persistent processing failures, 
and account-specific permission problems should be escalated to human 
support. 
 
 



---

