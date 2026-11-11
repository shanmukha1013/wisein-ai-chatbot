# Profile Video

## Source: WISEIN-PROFILE-VIDEO-037.pdf

WISEIN — PROFILE VIDEO  
Document ID: WISEIN-PROFILE-VIDEO-037 
Document Type: Product Knowledge Base / RAG Dataset 
Product: WiseIN 
Module: Individual Profile → Profile Video 
 
1. PROFILE VIDEO — OVERVIEW 
Profile Video is a video section within an individual WiseIN profile that allows a user to 
introduce themselves and make their professional profile more personal and engaging. 
In the current WiseIN profile interface previously provided, the profile contains a Video 
section with an edit control and the message: 
“Upload a profile or introduction video to make your profile more engaging and personal.” 
The Profile Video is part of the user's profile presentation and is different from Posts, Clips, 
and the video used during identity verification. 
WiseIN's public product positioning is strongly focused on video-based professional 
interaction and verified profiles. The official WiseIN website describes video calls and face-
to-face professional conversations as core parts of the platform.  
 
2. PURPOSE OF PROFILE VIDEO 
The primary purpose of the Profile Video is to give a user an additional way to introduce 
themselves on their WiseIN profile. 
A profile video can help communicate information such as: 
• 
Professional introduction  
• 
Career background  
• 
Areas of interest  
• 
Skills  
• 
Professional goals  
• 
What the user works on  
• 
What the user is interested in discussing  

• 
A short personal introduction  
The profile video should complement, not replace, the written profile information. 
 
3. PROFILE VIDEO IN THE PROFILE 
The current profile UI previously provided shows the Profile Video area within the individual 
profile. 
The section includes: 
Video 
with an edit control. 
When no video has been uploaded, the interface displays guidance to upload: 
“a profile or introduction video” 
to make the profile more engaging and personal. 
This establishes that the feature is intended specifically for profile/introduction video 
content, rather than general feed content. 
 
4. PROFILE VIDEO VS OTHER WISEIN VIDEO FEATURES 
WiseIN contains multiple video-related concepts. 
The chatbot must keep them separate. 
PROFILE VIDEO 
    ↓ 
Video presented as part of an individual profile 
 
PROFILE / IDENTITY VERIFICATION VIDEO 
    ↓ 
Video submitted as part of identity verification 
 
CLIP 

    ↓ 
Video-oriented content published as platform content 
 
VIDEO CALL 
    ↓ 
Live conversation between users 
 
MEETING RECORDING 
    ↓ 
Recording associated with a video meeting/call 
These are different features and must not be treated as interchangeable. 
 
5. PROFILE VIDEO VS IDENTITY VERIFICATION VIDEO 
This distinction is especially important. 
WiseIN's Privacy Policy states that, as part of its verification process, users may be 
required to submit a video recording in which they recite AI-generated text. WiseIN states 
that this video is used for identity validation and that a frame is taken from the verification 
video and added to the user's profile picture.  
That verification video is not the same feature as the Profile Video. 
Identity Verification Video 
Purpose: 
Identity verification. 
Profile Video 
Purpose: 
Profile introduction and presentation. 
Therefore, the chatbot must never tell a user: 
“Upload your profile video to complete identity verification.” 

unless the current WiseIN application explicitly shows that requirement. 
 
6. PROFILE VIDEO VS CLIP 
A Profile Video belongs to the user's profile. 
A Clip is a video-oriented content format used as platform content. 
WiseIN's official app page states that users can: 
“Post updates, clips, and articles.”  
WiseIN's current Premium offering also includes the ability to publish Posts & Clips.  
Therefore: 
Profile Video 
→ Personal profile introduction 
 
Clip 
→ Published video content 
A user should not be instructed to create a Clip when they are specifically trying to add a 
Profile Video. 
 
7. PROFILE VIDEO VS VIDEO CALL 
A Profile Video is a prerecorded video associated with a profile. 
A Video Call is a live conversation. 
WiseIN's current website describes video calls as a core networking experience where 
users can schedule calls and communicate face-to-face.  
Therefore: 
Profile Video 
→ Recorded profile introduction 
 
Video Call 

→ Live interaction 
Uploading a Profile Video does not automatically initiate a video call. 
 
8. PROFILE VIDEO VS MEETING RECORDING 
A Profile Video should not be confused with a recording generated from a WiseIN meeting. 
WiseIN's platform separately provides video calls and AI meeting summaries/transcription 
for applicable plans/features.  
A user should not upload a meeting recording as their Profile Video unless they 
intentionally want to use appropriate content from that recording and have the necessary 
rights/permissions. 
WiseIN's Content Policies also contain specific privacy rules concerning meeting 
recordings, transcripts, and AI summaries.  
 
9. ADDING A PROFILE VIDEO 
Based on the current profile UI previously provided, the general workflow is: 
1. Open the user's WiseIN profile.  
2. Locate the Video section.  
3. Select the available edit/upload control.  
4. Choose the profile or introduction video.  
5. Upload the video.  
6. Complete any validation shown by the current application.  
7. Save/submit the change.  
8. Confirm that the video appears on the profile.  
The exact button names and upload flow should always follow the current WiseIN 
application. 
Important chatbot rule 
Do not invent additional steps if the current interface has changed. 

 
10. PROFILE VIDEO FORMATS 
The current WiseIN profile UI previously provided for this documentation shows the 
following observed video formats: 
MP4 
WebM 
MOV 
AVI 
These are observed from the current profile interface supplied for the documentation. 
If the application changes its supported formats, the current application should take 
precedence over this document. 
 
11. PROFILE VIDEO RESOLUTION 
The current profile UI previously provided shows: 
1920 × 1080 px 
as the displayed Profile Video resolution information. 
This should be treated as the currently observed UI requirement rather than an eternal 
platform guarantee. 
If the application later displays different requirements, the new application behavior 
should replace this information in the knowledge base. 
 
12. PROFILE VIDEO SIZE 
The current profile interface previously provided shows: 
100 MB 
as the Profile Video size limit. 
Therefore, when the current UI still displays this value, the chatbot can tell users: 
“The current Profile Video interface supports videos up to 100 MB.” 

Do not silently change this number based on assumptions about other WiseIN video 
features. 
 
13. PROFILE VIDEO QUALITY 
Users should generally upload a clear and appropriately framed video. 
A good Profile Video should make it easy for viewers to: 
• 
See the speaker clearly.  
• 
Hear the speaker clearly.  
• 
Understand the introduction.  
• 
Identify the purpose of the profile.  
The chatbot should not claim that WiseIN requires a particular camera, microphone, 
bitrate, frame rate, or codec unless the application explicitly specifies it. 
 
14. PROFILE VIDEO CONTENT 
A Profile Video can be used as a professional introduction. 
A user could introduce: 
• 
Their professional background  
• 
Their current role  
• 
Their skills  
• 
Their areas of interest  
• 
Their projects  
• 
Their professional goals  
• 
What types of people or opportunities they want to connect with  
The content should accurately represent the user. 
 
15. RECOMMENDED PROFILE VIDEO STRUCTURE 
If a user asks: 

“What should I say in my Profile Video?” 
The chatbot can recommend a simple structure: 
1. Introduce yourself 
2. Mention your current role or background 
3. Mention your main skills/interests 
4. Briefly mention what you work on 
5. Explain what you are interested in connecting about 
6. End with a short professional closing 
This is general guidance, not a WiseIN-required script. 
The chatbot should not claim that WiseIN requires a specific introduction format. 
 
16. PROFILE VIDEO LENGTH 
The publicly available WiseIN pages reviewed do not currently document a specific Profile 
Video duration limit. 
Therefore, do not train the chatbot to state an exact duration such as: 
30 seconds 
60 seconds 
90 seconds 
2 minutes 
5 minutes 
unless the current application or approved internal documentation confirms it. 
If the user asks: 
“What is the maximum Profile Video duration?” 
the correct RAG behavior is: 
“The publicly documented WiseIN information I have does not specify a Profile Video 
duration limit. Please follow the limit shown in the current Profile Video upload interface.” 
 

17. PROFILE VIDEO AS PROFESSIONAL INTRODUCTION 
The Profile Video can provide information that is difficult to communicate through a short 
written profile. 
For example, it can allow the user to present: 
• 
Communication style  
• 
Professional introduction  
• 
Current focus  
• 
Interests  
• 
Career direction  
However, the chatbot should not claim that Profile Videos are used for automated 
personality assessment, hiring decisions, ranking, or skill verification unless WiseIN 
explicitly documents such functionality. 
 
18. PROFILE VIDEO AND VERIFIED PROFILE 
WiseIN positions itself as a verified professional networking platform. Its official website 
describes members as verified and emphasizes government-backed identity verification.  
However: 
A verified profile does not mean that the Profile Video itself has been independently 
verified for every statement it contains. 
Identity verification and Profile Video content are separate concepts. 
For example: 
Government Identity Verification 
→ verifies applicable identity 
 
Profile Video 
→ user-provided profile presentation 
The chatbot should preserve this distinction. 

 
19. PROFILE VIDEO AND AUTHENTICITY 
The Profile Video should accurately represent the user. 
WiseIN's Content Policies emphasize authentic content and prohibit fake credentials, fake 
expertise, impersonation, and misleading identity-related behavior.  
Therefore, the chatbot should recommend that users: 
• 
Use their own video.  
• 
Represent themselves accurately.  
• 
Avoid fake credentials.  
• 
Avoid impersonating another person.  
• 
Avoid misleading professional claims.  
 
20. PROFILE VIDEO AND PRIVACY 
Users should only include information in their Profile Video that they are comfortable 
sharing according to their profile visibility and applicable privacy settings. 
The WiseIN Privacy Policy explains that users may provide profile information and that 
certain profile information may be visible to other users depending on privacy settings.  
The chatbot should therefore avoid claiming that every Profile Video is: 
• 
Public to the entire internet.  
• 
Visible only to connections.  
• 
Visible only to verified users.  
unless the current application explicitly confirms that behavior. 
 
21. PRIVATE OR CONFIDENTIAL INFORMATION 
Users should not include sensitive or confidential information in a Profile Video. 
Examples include: 
• 
Passwords  

• 
OTPs  
• 
API keys  
• 
Authentication tokens  
• 
Private customer information  
• 
Confidential company information  
• 
Private addresses  
• 
Financial credentials  
• 
Internal documents  
• 
Sensitive personal information belonging to another person  
The chatbot should recommend keeping Profile Videos professional and safe for the 
intended profile audience. 
 
22. PROFILE VIDEO AND COMPANY INFORMATION 
If a user discusses an employer, client, or organization in their Profile Video, they should 
only share information they are authorized to disclose. 
For example, users should avoid revealing: 
• 
Confidential product roadmaps  
• 
Private source code  
• 
Internal systems  
• 
Confidential business metrics  
• 
Customer data  
• 
Internal documents  
WiseIN's Content Policies contain rules concerning privacy, unauthorized information, and 
confidential content.  
 
23. PROFILE VIDEO AND COPYRIGHT 
Users should use video content they own or have permission to use. 

The chatbot should not recommend: 
• 
Uploading someone else's video.  
• 
Using copyrighted music without permission.  
• 
Reusing another person's introduction.  
• 
Uploading copyrighted footage without authorization.  
WiseIN's Content Policies address copyright and ownership of content.  
 
24. PROFILE VIDEO AND IMPERSONATION 
The Profile Video must represent the actual profile owner. 
The chatbot should not help a user create a Profile Video that impersonates: 
• 
Another person  
• 
A company representative  
• 
A celebrity  
• 
A professional they are not  
• 
A fake employer  
• 
A fake credential holder  
WiseIN's Content Policies prohibit impersonation and fake expertise/credentials.  
 
25. PROFILE VIDEO AND AI-GENERATED CONTENT 
The public WiseIN documentation reviewed does not establish a specific rule that all AI-
generated Profile Videos are prohibited or allowed. 
Therefore, do not state a universal AI-video policy unless the current WiseIN policy or 
internal documentation explicitly confirms it. 
However, the video should not be used to misrepresent the user's identity or credentials. 
A safe chatbot response is: 
“Your Profile Video should accurately represent you and comply with WiseIN's content and 
authenticity policies.” 

 
26. PROFILE VIDEO AND PROFESSIONAL CLAIMS 
Users should avoid exaggerated or false claims. 
For example, a user should not claim: 
“I am a certified expert in every technology shown on my profile.” 
unless that statement is accurate. 
WiseIN's Terms and Content Policies require authentic and accurate professional 
information and prohibit misrepresentation.  
 
27. PROFILE VIDEO AND SKILLS 
A user can use their Profile Video to introduce their skills. 
For example: 
“I work primarily with Python and AI applications.” 
The Profile Video and Key Skills section serve different purposes: 
Key Skills 
→ Structured profile information 
 
Profile Video 
→ Video-based personal/professional introduction 
The chatbot should not automatically add skills based on statements made in a Profile 
Video unless the WiseIN application explicitly provides such functionality. 
 
28. PROFILE VIDEO AND PROJECTS 
A user can mention projects in their Profile Video. 
For example: 
“I recently worked on a full-stack application.” 
But the Profile Video does not automatically create a Project entry. 

These are separate profile features: 
Projects 
→ Structured project information 
 
Profile Video 
→ Video introduction 
 
29. PROFILE VIDEO AND EDUCATION 
Users may mention their educational background in their Profile Video. 
For example: 
“I am a Computer Science student.” 
However, the Profile Video does not replace the Education section. 
Education 
→ Structured academic information 
 
Profile Video 
→ Personal introduction 
 
30. PROFILE VIDEO AND EXPERIENCE 
Users may mention their current or previous professional experience. 
However, a statement in a video does not automatically create an Experience entry. 
If a user wants to update their formal profile information, they should use the relevant 
profile section. 
 
31. PROFILE VIDEO AND DISCOVERY 
WiseIN's platform emphasizes professional discovery based on information such as: 

• 
Skill  
• 
Industry  
• 
Experience  
The official WiseIN website states that users can explore individuals by these categories.  
The Profile Video provides additional profile context, but the public documentation 
reviewed does not establish that the video itself directly determines search ranking or 
discovery ranking. 
Therefore, do not tell users: 
“Uploading a Profile Video will increase your search ranking.” 
unless WiseIN's internal product documentation confirms this. 
 
32. PROFILE VIDEO AND PROFILE ENGAGEMENT 
The current profile UI itself describes the Profile Video as a way to make the profile: 
“more engaging and personal.” 
Therefore, the chatbot can explain that the feature is intended to make a profile more 
engaging and personal. 
However, do not promise a measurable increase in: 
• 
Profile views  
• 
Followers  
• 
Connections  
• 
Calls  
• 
Job offers  
• 
Recruiter messages  
unless WiseIN has verified data or documentation supporting those claims. 
 
33. PROFILE VIDEO AND VIDEO-FIRST NETWORKING 
Profile Video fits within WiseIN's broader video-oriented networking model. 

WiseIN describes its platform as focused on face-to-face professional conversations and 
video calls rather than only text-based networking.  
The Profile Video provides a prerecorded introduction, while WiseIN video calls provide live 
interaction. 
 
34. REPLACING A PROFILE VIDEO 
If the current Profile Video interface provides an edit or replace option: 
1. Open the profile.  
2. Open the Video section.  
3. Select the available edit option.  
4. Upload the new video.  
5. Save the changes.  
6. Confirm that the new video appears.  
Do not claim that WiseIN maintains multiple Profile Videos simultaneously unless the 
application confirms that behavior. 
 
35. DELETING A PROFILE VIDEO 
If the current interface provides a delete/remove option: 
1. Open the Profile Video section.  
2. Open the available action/edit controls.  
3. Select delete/remove.  
4. Confirm if prompted.  
If the interface does not provide a delete option, do not invent one. 
WiseIN's Privacy Policy states generally that users can edit or delete certain information 
through account settings, subject to restrictions.  
 
36. PROFILE VIDEO NOT UPLOADING 

If the user says: 
“My Profile Video is not uploading.” 
Use this troubleshooting sequence. 
Step 1 — Check file requirements 
Check the requirements currently displayed by WiseIN. 
The previously supplied profile UI shows: 
MP4 
WebM 
MOV 
AVI 
 
1920 × 1080 px 
 
Maximum size: 100 MB 
Step 2 — Check the file 
Confirm that the video: 
• 
Uses a supported format.  
• 
Does not exceed the displayed size limit.  
• 
Meets the displayed resolution requirement.  
Step 3 — Check connection 
Ensure the user has a stable internet connection. 
Step 4 — Retry 
Retry the upload. 
Step 5 — Refresh 
Refresh the application and reopen the profile. 
Step 6 — Try another supported environment 

If appropriate: 
• 
Try a current supported browser.  
• 
Try the WiseIN mobile application if the feature is available there.  
Step 7 — Escalate 
If the video still cannot be uploaded, contact WiseIN support. 
The official WiseIN Contact page currently states that the team replies within 24 hours.  
 
37. PROFILE VIDEO FORMAT ERROR 
If the user receives a format-related error: 
Check whether the file uses one of the formats currently accepted by the Profile Video 
uploader. 
Based on the previously supplied current UI: 
MP4 
WebM 
MOV 
AVI 
Do not tell the user that another format is supported unless the current application 
confirms it. 
 
38. PROFILE VIDEO SIZE ERROR 
If the user receives a file-size error: 
Check the file size against the limit currently shown by the Profile Video upload interface. 
The previously supplied interface displays: 
100 MB 
as the limit. 
If the current application displays a different limit, use the current value. 
 

39. PROFILE VIDEO QUALITY ERROR 
If the application rejects a video based on resolution: 
Check the resolution shown by the current uploader. 
The previously supplied Profile Video UI displays: 
1920 × 1080 px 
Do not infer additional requirements such as: 
• 
Minimum FPS  
• 
Maximum FPS  
• 
Codec  
• 
Bitrate  
• 
Aspect ratio  
unless explicitly displayed by the current application. 
 
40. PROFILE VIDEO UPLOAD STUCK 
If the upload remains stuck: 
1. Check the internet connection.  
2. Wait for the upload to finish.  
3. Avoid repeatedly submitting the same file.  
4. Refresh/reopen the profile if the application becomes unresponsive.  
5. Try again.  
6. If the issue persists, contact WiseIN support.  
The chatbot should not claim a specific upload timeout unless WiseIN documents one. 
 
41. PROFILE VIDEO UPLOADED BUT NOT DISPLAYING 
If the user says: 
“My Profile Video uploaded but isn't visible.” 

Use: 
1. Refresh the profile.  
2. Reopen the profile.  
3. Check whether the video appears in the Video section.  
4. Check whether the upload actually completed.  
5. Check the profile from the appropriate viewing mode if possible.  
6. If the video remains missing, escalate to support.  
Do not immediately claim that WiseIN deleted the video. 
 
42. PROFILE VIDEO PLAYBACK PROBLEM 
If the video appears but does not play: 
Check: 
• 
Internet connection.  
• 
Browser/app state.  
• 
Whether other videos play.  
• 
Whether refreshing resolves the problem.  
• 
Whether the problem occurs on another supported device/browser.  
If the problem continues, report it to WiseIN support. 
Do not invent specific codec requirements unless the application documents them. 
 
43. PROFILE VIDEO HAS NO SOUND 
If the video plays but has no audio: 
Check: 
• 
Device volume.  
• 
Browser/app volume.  
• 
Video file itself.  

• 
Whether the original file contains an audio track.  
• 
Whether the problem occurs with another video.  
If the original video has no audio, the issue may be with the uploaded file rather than 
WiseIN. 
 
44. PROFILE VIDEO CAMERA/MICROPHONE ISSUES 
Uploading an existing Profile Video is different from recording a video for identity 
verification. 
Therefore, if the user says: 
“My microphone doesn't work while uploading my Profile Video,” 
the chatbot should first determine whether they are: 
• 
Uploading an existing file, or  
• 
Recording a video inside WiseIN.  
Do not assume that the Profile Video uploader necessarily records video directly inside the 
application. 
 
45. PROFILE VIDEO NOT SHOWING AFTER EDIT 
If a user replaced a video but the previous video still appears: 
1. Refresh the profile.  
2. Close and reopen the application.  
3. Check whether the update was saved.  
4. Check the profile again.  
5. Escalate if the old video continues to appear despite a successful update.  
Do not assume caching unless the application behavior confirms it. 
 
46. PROFILE VIDEO PRIVACY AND OTHER PEOPLE 

A user should not upload a video containing another person without appropriate 
permission, especially if the video reveals private or sensitive information. 
WiseIN's Content Policies prohibit privacy violations and unauthorized sharing of private 
information.  
 
47. PROFILE VIDEO CONTENT POLICY 
Profile Video content should follow WiseIN's applicable authenticity, privacy, copyright, 
and safety requirements. 
The WiseIN Content Policies cover platform content including posts, comments, clips, job 
listings, events, messages, and meeting recordings.  
The chatbot should apply the same general principles of: 
• 
Authenticity  
• 
Privacy  
• 
Copyright  
• 
No impersonation  
• 
No fraud  
• 
No misleading credentials  
• 
No harmful prohibited content  
where applicable to profile video content. 
 
48. PROFILE VIDEO AND SELF-PROMOTION 
A Profile Video may introduce the user's professional work and interests. 
WiseIN's Content Policies permit relevant self-promotion while discouraging hard-selling 
and spam-like behavior.  
Therefore, users can introduce their: 
• 
Work  
• 
Skills  

• 
Projects  
• 
Professional interests  
but should avoid turning their Profile Video into misleading or aggressive promotional 
content. 
 
49. PROFILE VIDEO AND CONTACT INFORMATION 
Users should think carefully before including personal contact information in a Profile 
Video. 
The chatbot should not require users to publish: 
• 
Personal phone numbers  
• 
Personal email addresses  
• 
Home addresses  
• 
Private social accounts  
A user can use the profile's supported professional links/contact mechanisms where 
available. 
 
50. PROFILE VIDEO AND PROFESSIONAL LINKS 
If a user wants to direct viewers to their portfolio or professional website, they can use the 
appropriate profile link/website functionality if available. 
The Profile Video itself should not be assumed to support clickable links. 
Do not claim that links inside uploaded Profile Videos are automatically clickable. 
 
51. PROFILE VIDEO AND SUBSCRIPTIONS 
The publicly available WiseIN pricing information reviewed does not explicitly list a 
separate Profile Video feature as a Premium-only capability. 
The Basic plan includes a verified profile and other networking features, while Premium 
includes additional features such as unlimited conversations, advanced analytics, AI 
discovery, and Posts/Clips.  

Therefore, the chatbot should not tell users that: 
“You need Premium to upload a Profile Video” 
unless the current application explicitly enforces that restriction. 
 
52. PROFILE VIDEO AND STUDENT ACCOUNTS 
The public WiseIN site provides a Student plan with student verification and career-
oriented features.  
The public documentation reviewed does not establish a separate Profile Video restriction 
specifically for Student accounts. 
Therefore, do not invent student-specific Profile Video rules. 
 
53. PROFILE VIDEO AND ORGANIZATION PROFILES 
WiseIN also provides organization-related profiles and features. 
The individual Profile Video documentation should not automatically be applied to 
Organization Video features. 
The WiseIN organization pages may use different terminology and workflows. 
For example, the current WiseIN organization page shows an Organization Video concept 
separately.  
Therefore: 
Individual Profile Video 
≠ 
Organization Video 
 
54. PROFILE VIDEO AND PROFILE PHOTO 
The Profile Video is separate from the Profile Photo. 
WiseIN's Privacy Policy states that a frame from the identity verification video is used for 
the user's profile picture.  

This should not be confused with the user-uploaded Profile Video. 
Profile Photo 
→ Profile image 
 
Profile Video 
→ Profile/introduction video 
 
Verification Video 
→ Identity verification process 
 
55. PROFILE VIDEO AND AUTOMATIC PROFILE PHOTO 
Do not tell users: 
“Your Profile Video will automatically become your profile picture.” 
That is not the documented Profile Video behavior. 
The Privacy Policy specifically describes a frame being taken from the verification video 
for the profile picture.  
 
56. PROFILE VIDEO AND AUTOMATIC TRANSCRIPTION 
The current public documentation does not state that WiseIN automatically transcribes 
Profile Videos. 
Do not tell users that: 
• 
Their Profile Video is automatically transcribed.  
• 
Speech is automatically converted into Skills.  
• 
The video is automatically summarized.  
• 
AI automatically extracts their job title.  
unless the current application or internal documentation confirms these features. 

AI meeting summaries are documented for applicable WiseIN video meetings, but that is a 
separate feature.  
 
57. PROFILE VIDEO AND AI ANALYSIS 
Do not claim that WiseIN automatically evaluates: 
• 
Facial expressions  
• 
Personality  
• 
Communication ability  
• 
Intelligence  
• 
Confidence  
• 
Employability  
• 
Skill level  
from a Profile Video unless official internal documentation explicitly establishes such 
functionality. 
 
58. PROFILE VIDEO AND SEARCH RANKING 
Do not tell users that uploading a Profile Video automatically improves: 
• 
Search ranking  
• 
AI discovery ranking  
• 
Profile ranking  
• 
Recommendation ranking  
The official site confirms discovery features, but the public sources reviewed do not 
document Profile Video as a ranking factor.  
 
59. PROFILE VIDEO AND PROFILE ANALYTICS 
WiseIN's current plans include profile analytics features.  

However, the public documentation reviewed does not establish a specific Profile Video 
views/watch-time analytics feature. 
Therefore, do not promise: 
• 
Video views  
• 
Watch time  
• 
Completion rate  
• 
Viewer list  
• 
Video engagement analytics  
unless confirmed by the current application. 
 
60. PROFILE VIDEO AND RECOMMENDATIONS 
WiseIN's Privacy Policy says profile/activity information may be used for personalization, 
including job recommendations and connection suggestions.  
However, the chatbot should not claim that the Profile Video specifically controls these 
recommendations. 
Use: 
“WiseIN may use profile and activity information for personalization.” 
Avoid: 
“The AI analyzes your Profile Video and recommends jobs based on it.” 
unless internally confirmed. 
 
61. PROFILE VIDEO — COMMON USER QUESTIONS 
“What is a Profile Video?” 
A Profile Video is a video section on your WiseIN profile where you can upload a personal or 
professional introduction to make your profile more engaging and personal. 
“Where do I add my Profile Video?” 

Open your WiseIN profile and locate the Video section. Use the available edit/upload 
control to add your profile or introduction video. 
“What formats are supported?” 
The Profile Video interface previously showed MP4, WebM, MOV, and AVI as supported 
formats. Follow the formats currently displayed by the WiseIN uploader. 
“What is the maximum size?” 
The current Profile Video interface previously showed a maximum size of 100 MB. Follow 
the limit currently displayed by the uploader. 
“What resolution should I use?” 
The current interface previously displayed 1920 × 1080 px. Follow the current uploader 
requirements if they have changed. 
“How long should my Profile Video be?” 
WiseIN's public documentation does not currently specify a Profile Video duration limit. 
Follow the limit displayed by the current uploader. 
“Is the Profile Video used for verification?” 
No. Do not confuse the Profile Video with the separate identity-verification video process. 
“Is my Profile Video a Clip?” 
No. A Profile Video is part of your profile, while a Clip is a video-oriented content format. 
 
62. AI INTENTS FOR PROFILE VIDEO 
Use the following intents for RAG/intent classification: 
profile_video_overview 
profile_video 
add_profile_video 
upload_profile_video 
edit_profile_video 
replace_profile_video 

delete_profile_video 
remove_profile_video 
view_profile_video 
profile_video_format 
profile_video_size 
profile_video_resolution 
profile_video_duration 
profile_video_content 
profile_video_script 
profile_video_privacy 
profile_video_visibility 
profile_video_verification 
profile_video_vs_verification_video 
profile_video_vs_clip 
profile_video_vs_video_call 
profile_video_vs_meeting_recording 
profile_video_vs_profile_photo 
profile_video_not_uploading 
profile_video_upload_error 
profile_video_format_error 
profile_video_size_error 
profile_video_resolution_error 
profile_video_upload_stuck 
profile_video_not_visible 
profile_video_not_playing 
profile_video_no_audio 

profile_video_replace_error 
profile_video_delete_error 
profile_video_content_policy 
profile_video_copyright 
profile_video_impersonation 
profile_video_confidentiality 
profile_video_ai 
profile_video_search 
profile_video_discovery 
profile_video_analytics 
profile_video_support 
 
63. ENTITIES 
Useful entities for Profile Video intent detection: 
profile_video 
video 
introduction_video 
profile 
profile_section 
profile_photo 
verification_video 
identity_verification 
clip 
video_call 
meeting 
meeting_recording 

skills 
projects 
education 
experience 
professional_profile 
video_format 
file_size 
resolution 
duration 
privacy 
visibility 
copyright 
authentication 
verification 
 
64. LIVE DATA VS RAG DATA 
The chatbot should distinguish general Profile Video information from user-specific Profile 
Video information. 
RAG can answer: 
• 
What Profile Video is.  
• 
Why it exists.  
• 
How it differs from Clips.  
• 
How it differs from verification video.  
• 
General upload guidance.  
• 
Supported formats documented by the current UI.  
• 
General troubleshooting.  

• 
Privacy and content guidance.  
Authorized live APIs should answer: 
• 
Whether the user currently has a Profile Video.  
• 
Current Profile Video URL/reference.  
• 
Upload status.  
• 
Whether the user's Profile Video exists.  
• 
Whether an update succeeded.  
• 
Whether deletion succeeded.  
• 
Current profile video metadata if exposed by the API.  
The LLM should not directly access the database. 
 
65. RECOMMENDED CHATBOT FLOW — VIEW PROFILE VIDEO 
For: 
“Do I have a Profile Video?” 
Use: 
User 
 ↓ 
Intent Detection 
 ↓ 
view_profile_video 
 ↓ 
Authenticated User 
 ↓ 
Authorized Profile API 
 ↓ 
Check current Profile Video 

 ↓ 
LLM 
 ↓ 
Response 
The chatbot should not guess based on old profile information. 
 
66. RECOMMENDED CHATBOT FLOW — ADD PROFILE VIDEO 
For: 
“How do I add a Profile Video?” 
Use: 
User 
 ↓ 
Intent Detection 
 ↓ 
add_profile_video 
 ↓ 
RAG 
 ↓ 
Current Profile UI guidance 
 ↓ 
LLM 
 ↓ 
Response 
If the user asks: 
“Did my upload succeed?” 
then use an authorized live API rather than RAG. 

 
67. RECOMMENDED CHATBOT FLOW — UPLOAD FAILURE 
User 
 ↓ 
Intent Detection 
 ↓ 
profile_video_upload_error 
 ↓ 
Check current requirements 
 ↓ 
Format / size / resolution 
 ↓ 
Basic troubleshooting 
 ↓ 
Retry 
 ↓ 
Support escalation if unresolved 
 
68. PROFILE VIDEO SECURITY 
The chatbot must never ask the user to provide: 
• 
WiseIN password  
• 
OTP  
• 
Session token  
• 
API key  
• 
Authentication token  
• 
Private database credentials  

to troubleshoot a Profile Video. 
If the user needs account-level assistance, use the authenticated WiseIN session or direct 
the user to official support. 
 
69. PROFILE VIDEO — SOURCE-OF-TRUTH RULE 
For Profile Video questions, use: 
1. Current authenticated WiseIN application 
        ↓ 
2. Current authorized WiseIN API 
        ↓ 
3. Approved internal WiseIN documentation 
        ↓ 
4. Current official WiseIN website 
        ↓ 
5. Current WiseIN UI screenshots 
        ↓ 
6. Older documentation 
If the current application displays a different upload requirement from this document, the 
current application takes precedence. 
 
70. UNSUPPORTED PROFILE VIDEO CLAIMS — DO NOT TRAIN AS FACTS 
Unless confirmed by the current WiseIN application or approved internal documentation, 
do not state that Profile Video supports: 
A specific maximum duration 
Automatic transcription 
Automatic subtitles 
Automatic translation 

Automatic skill extraction 
Automatic job matching 
Automatic personality analysis 
Automatic facial analysis 
Automatic resume generation 
Automatic profile ranking 
Automatic search ranking 
Video-specific recommendations 
Video views 
Video watch-time analytics 
Viewer lists 
Likes 
Comments 
Shares 
Video reactions 
Multiple simultaneous Profile Videos 
Scheduled Profile Videos 
Profile Video drafts 
Automatic thumbnail selection 
Automatic AI editing 
Automatic background removal 
Automatic video compression 
Automatic face enhancement 
Specific codecs 
Specific FPS requirements 
Specific bitrate requirements 

Specific audio requirements 
Only add these features after verification. 
 
71. IMPORTANT AI DISTINCTIONS 
The chatbot should maintain the following distinctions: 
PROFILE VIDEO 
    ↓ 
User's profile/introduction video 
 
PROFILE PHOTO 
    ↓ 
User's profile image 
 
VERIFICATION VIDEO 
    ↓ 
Video used as part of identity verification 
 
CLIP 
    ↓ 
Video-oriented platform content 
 
VIDEO CALL 
    ↓ 
Live professional conversation 
 
MEETING RECORDING 

    ↓ 
Recording associated with a meeting 
This distinction is critical for correct chatbot answers. 
 
72. GOLDEN ANSWER — WHAT IS PROFILE VIDEO? 
If the user asks: 
“What is Profile Video on WiseIN?” 
Use: 
Profile Video is a video section on your WiseIN profile where you can upload a 
personal or professional introduction. WiseIN's profile interface describes it as a way 
to make your profile more engaging and personal. 
 
73. GOLDEN ANSWER — HOW TO ADD PROFILE VIDEO 
Open your WiseIN profile and locate the Video section. Use the available edit/upload 
option to add your profile or introduction video, then save the change. Follow the 
requirements currently shown by the uploader. 
 
74. GOLDEN ANSWER — PROFILE VIDEO VS VERIFICATION VIDEO 
They are different. A Profile Video is an introduction displayed as part of your profile. 
WiseIN separately uses a video during its identity-verification process to validate the user's 
identity. The verification video should not be confused with the Profile Video.  
 
75. GOLDEN ANSWER — PROFILE VIDEO VS CLIP 
A Profile Video is part of your individual profile and is intended as an introduction. A Clip is 
a video-oriented piece of content that can be published on WiseIN. They are separate 
features.  
 
76. GOLDEN ANSWER — PROFILE VIDEO REQUIREMENTS 

The current Profile Video interface previously showed MP4, WebM, MOV, and AVI, with 
1920 × 1080 px and a 100 MB maximum file size. Because upload requirements can 
change, follow the requirements currently displayed by the WiseIN uploader. 
 
77. GOLDEN ANSWER — PROFILE VIDEO DURATION 
WiseIN's currently published public documentation does not specify a Profile Video 
duration limit. Check the current Profile Video uploader for the applicable limit rather than 
relying on an assumed duration. 
 
78. GOLDEN ANSWER — PROFILE VIDEO VERIFICATION 
A Profile Video should not automatically be treated as a verified credential or identity proof. 
WiseIN's identity-verification process is separate from the profile-introduction video. 
 
79. GOLDEN ANSWER — PROFILE VIDEO NOT UPLOADING 
First check the requirements shown by the current Profile Video uploader, including file 
format, size, and resolution. Then retry the upload and refresh your profile. If the problem 
continues, contact WiseIN support through the official Contact page. 
 
80. GOLDEN ANSWER — WHAT SHOULD I SAY? 
A good Profile Video can briefly introduce who you are, your current role or background, 
your main skills or interests, what you work on, and what kinds of professional connections 
you're interested in. Keep it authentic and avoid sharing confidential information. 
 
81. GOLDEN ANSWER — DOES PROFILE VIDEO IMPROVE SEARCH RANKING? 
WiseIN provides professional discovery based on information such as skills, industry, and 
experience, but the public documentation does not establish that uploading a Profile Video 
directly improves search or AI-discovery ranking.  
 
82. RAG SUMMARY 

WiseIN Profile Video is a video section on an individual profile intended for a personal or 
professional introduction. 
 
The current profile UI describes the feature as a way to make the profile more engaging and 
personal. 
 
The current observed Profile Video interface supports MP4, WebM, MOV, and AVI, displays 
1920 × 1080 px, and displays a 100 MB maximum file size. 
 
These technical requirements should be treated as current UI observations and replaced if 
the application changes them. 
 
WiseIN's public documentation does not currently specify a Profile Video duration limit. 
 
Profile Video is different from the identity-verification video. 
 
WiseIN's Privacy Policy states that a video may be required during identity verification and 
that a frame from that verification video is used for the profile picture. This is separate from 
the user-uploaded Profile Video. 
 
Profile Video is also different from Clips, video calls, and meeting recordings. 
 
Profile Videos should accurately represent the user and should not contain fake 
credentials, impersonation, confidential information, private customer information, 
passwords, API keys, or other sensitive information. 
 
Users should only upload video content they own or have permission to use. 
 

WiseIN's platform emphasizes verified professional networking and video-based 
conversations, but the public documentation does not establish that Profile Video directly 
controls search ranking, AI discovery ranking, job recommendations, or connection 
recommendations. 
 
The chatbot must not invent Profile Video duration limits, analytics, automatic 
transcription, AI analysis, ranking behavior, codecs, FPS requirements, or other 
unsupported functionality. 
 
For user-specific Profile Video information, the chatbot should use an authenticated and 
authorized WiseIN profile API. 
 
The LLM must not have unrestricted database access. 
 
 
 



---

