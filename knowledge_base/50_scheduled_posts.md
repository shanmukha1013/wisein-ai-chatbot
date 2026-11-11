# Scheduled Posts

## Source: WISEIN-SCHEDULED-POSTS-050.pdf

WISEIN — SCHEDULED POSTS  
Document ID: WISEIN-SCHEDULED-POSTS-050 
Feature: Scheduled Posts 
Platform: WiseIN 
 
1. FEATURE OVERVIEW 
Scheduled Posts allows a WiseIN user to prepare a post in advance and choose a future 
date and time for publishing it. 
The feature is accessible through the post composer using the Schedule option rather than 
publishing the post immediately. 
The supplied WiseIN UI shows a dedicated Scheduled posts section under account 
Settings where scheduled posts can be managed. 
The current Settings interface shown in the supplied screenshot contains: 
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
When no posts have been scheduled, the Scheduled posts page displays: 
“Schedule your first post to get started” 

and a Delete posts button appears at the top right, currently disabled when there are no 
scheduled posts. 
Important: The exact scheduling behavior, publication timing, limits, editing capabilities, 
and failure handling should be treated as UI/product behavior rather than assumed from 
general social-media functionality. 
 
2. WHAT IS A SCHEDULED POST? 
A Scheduled Post is a WiseIN post that is prepared now but configured to be published at 
a selected future date and time. 
Instead of selecting Post immediately, the user can select Schedule from the post 
composer. 
The scheduling flow shown in the supplied UI contains: 
1. Create the post.  
2. Select Schedule.  
3. Choose a date.  
4. Choose a time.  
5. Select a time zone.  
6. Preview the post.  
7. Select Schedule Post.  
This separates creating content from publishing content. 
 
3. WHERE TO MANAGE SCHEDULED POSTS 
The supplied WiseIN UI shows: 
Settings → Scheduled post 
Inside this section, users can view their scheduled posts. 
Empty state 
When the user has no scheduled posts, the interface displays: 

Schedule your first post to get started 
The screenshot also shows a Delete posts control. 
Because the supplied screenshot shows no scheduled posts, the exact list-card design 
and available actions for an existing scheduled post should not be inferred. 
 
4. CREATING A POST BEFORE SCHEDULING 
The supplied post composer shows the following interface. 
Top controls 
• 
Cancel  
• 
Schedule  
• 
Post  
Selecting Post is the immediate publishing path. 
Selecting Schedule opens the scheduling interface. 
Audience 
The composer currently shows: 
Everyone can interact 
This represents the interaction/audience setting visible in the supplied UI. 
Post categories 
The supplied composer shows four post categories: 
• 
Update  
• 
Looking for  
• 
Opportunity  
• 
Ask  
These categories should remain part of the scheduled-post knowledge base because 
scheduling occurs from the same post composer. 
 
5. POST TYPES AVAILABLE IN THE COMPOSER 

5.1 Update 
The Update category is used for sharing updates such as recent work, achievements, or 
other professional information. 
The supplied UI displays the placeholder: 
Share your recent work or achievement 
 
5.2 Looking for 
The Looking for category can be selected when the post is intended to communicate 
something the user is looking for. 
Examples may include professional connections, opportunities, collaborators, or other 
relevant requests. 
The exact permitted use should follow WiseIN's current content policies. 
 
5.3 Opportunity 
The Opportunity category is intended for opportunity-related posts. 
WiseIN's Content Policies specifically state that jobs, gigs, internships, and other 
opportunities posted on the platform must be genuine. Unpaid, equity-only, and part-time 
opportunities should be clearly disclosed.  
 
5.4 Ask 
The Ask category is intended for questions or requests for help from the WiseIN 
community. 
WiseIN's Content Policies explicitly describe questions users need help with as 
appropriate content.  
 
6. POST COMPOSER CHARACTER COUNT 
The supplied screenshot shows: 
0/700 

Therefore, the currently observed post composer supports a 700-character counter for the 
text field shown in the supplied UI. 
Important knowledge-base rule 
Do not generalize this value to every WiseIN content type unless the current product UI 
confirms it. 
The earlier Posts documentation may contain different limits for other post 
implementations or versions. For the chatbot, the current observed UI should take 
precedence when answering questions specifically about this composer. 
 
7. MEDIA OPTIONS 
The supplied composer shows media/action icons at the bottom, including options 
represented visually for: 
• 
Images  
• 
Video  
• 
Other post/content options  
• 
People/community-related interaction  
• 
Additional post functionality  
The composer also displays: 
Images wider than 4:5 will be cropped. 
Therefore, when answering from the supplied current UI: 
Wide images may be cropped to fit the supported display format. 
Do not invent exact image file-size limits, video duration limits, codecs, or resolution 
requirements unless they are confirmed by the current WiseIN product or internal 
documentation. 
 
8. SCHEDULING A POST 
The current supplied UI provides a dedicated scheduling workflow. 
Step 1 — Prepare the post 

Create the post normally. 
Choose the required category: 
• 
Update  
• 
Looking for  
• 
Opportunity  
• 
Ask  
Enter the content and add supported media if required. 
 
Step 2 — Select Schedule 
Instead of selecting Post, select: 
Schedule 
The scheduling interface opens. 
 
9. SCHEDULE POST SCREEN 
The supplied screenshot shows a screen titled: 
Schedule Post 
The interface contains: 
• 
Date selector  
• 
Time selector  
• 
Time Zone selector  
• 
Preview Post  
• 
Schedule Post  
 
10. SELECTING THE DATE 
The scheduling interface contains a calendar/date field. 
The supplied screenshot shows an example: 

Tue, Sep 22 
This is only an example from the supplied UI and should not be stored as a fixed scheduling 
date. 
The user can select the intended future publication date through the date selector. 
Chatbot rule 
If a user asks: 
“What date can I schedule my post for?” 
The chatbot should explain that the scheduling screen allows the user to select a date, but 
should not invent an unsupported maximum scheduling horizon. 
For example: 
“You can select the publication date from the Schedule Post screen. WiseIN's current 
public documentation does not specify a maximum number of days or months ahead that 
a post can be scheduled.” 
 
11. SELECTING THE TIME 
The scheduling screen also contains a time selector. 
The supplied screenshot shows: 
12:44 PM 
with a label: 
Recommended time 
This indicates that the current scheduling interface can display a recommended time. 
Important 
Do not tell users that WiseIN guarantees better reach or engagement when using a 
recommended time. 
The screenshot establishes that the interface provides a recommended time; it does not 
establish the algorithm, calculation, expected reach improvement, or recommendation 
criteria. 
 

12. RECOMMENDED TIME 
The UI displays: 
Recommended time 
next to the selected time. 
The chatbot should describe this conservatively: 
“WiseIN's scheduling interface may show a recommended time for your post. The current 
public documentation does not explain the algorithm or criteria used to generate the 
recommendation.” 
Do not claim: 
• 
highest engagement time  
• 
follower activity calculation  
• 
AI-generated optimal time  
• 
guaranteed increased reach  
• 
guaranteed impressions  
• 
guaranteed engagement  
unless WiseIN's internal product documentation confirms these behaviors. 
 
13. TIME ZONE 
The scheduling screen contains a dedicated: 
Time Zone 
field. 
The supplied screenshot shows: 
Asia/Calcutta 
as the selected time zone. 
This means the user can explicitly select a time zone when scheduling a post. 
Chatbot answer 
If a user asks: 

“Does scheduled post support time zones?” 
Answer: 
“Yes. The Schedule Post screen includes a Time Zone selector, allowing the scheduled 
publication time to be associated with a selected time zone.” 
The exact list of available time zones is not documented publicly and should not be 
invented. 
 
14. WHY TIME ZONE MATTERS 
A scheduled publication time is meaningful only when its associated time zone is clear. 
For example, a user scheduling a post for a professional audience in another region should 
verify the selected time zone before confirming the schedule. 
The chatbot should recommend checking: 
1. Date  
2. Time  
3. Time zone  
before selecting Schedule Post. 
 
15. PREVIEW POST 
The Schedule Post screen provides: 
Preview Post 
The user can use the preview before final scheduling. 
The purpose of previewing is to allow the user to check the post before confirming its 
scheduled publication. 
The chatbot should recommend reviewing: 
• 
Post text  
• 
Category  
• 
Media  

• 
Audience/interaction setting  
• 
Date  
• 
Time  
• 
Time zone  
before final confirmation. 
 
16. FINAL SCHEDULING 
After selecting the date, time, and time zone, the user can select: 
Schedule Post 
This confirms the scheduling action. 
A scheduled post should then appear in the user's Settings → Scheduled post section, 
subject to the current product implementation. 
 
17. SCHEDULED POSTS MANAGEMENT 
The supplied Settings screenshot establishes that WiseIN provides a dedicated Scheduled 
posts management page. 
The page is designed to manage scheduled content separately from ordinary published 
content. 
The screenshot currently shows: 
Scheduled posts 
and: 
Delete posts 
Current empty-state behavior 
When there are no scheduled posts: 
Schedule your first post to get started 
is displayed. 

The exact controls available for an individual scheduled post are not visible in the supplied 
empty-state screenshot. 
Therefore, the chatbot must not invent actions such as: 
• 
Edit scheduled post  
• 
Reschedule  
• 
Duplicate  
• 
Publish immediately  
• 
Cancel individual schedule  
• 
Change media  
• 
Change audience  
unless those controls are confirmed in the actual product UI or internal API 
documentation. 
 
18. DELETE POSTS 
The Scheduled posts page contains a: 
Delete posts 
control. 
In the supplied screenshot, the button appears disabled because there are no scheduled 
posts. 
Therefore, the knowledge base can safely state: 
“The Scheduled posts management screen includes a Delete posts control. Its enabled 
behavior depends on whether there are scheduled posts available to delete.” 
Do not invent whether deletion: 
• 
requires confirmation,  
• 
supports individual deletion,  
• 
supports bulk deletion,  
• 
immediately removes content,  

• 
restores deleted schedules,  
• 
deletes the underlying draft.  
These behaviors require product verification. 
 
19. SCHEDULED POST VS IMMEDIATE POST 
Immediate Post 
User creates content → selects Post → content is published according to the current WiseIN 
publishing flow. 
Scheduled Post 
User creates content → selects Schedule → chooses date → chooses time → chooses time 
zone → previews → selects Schedule Post. 
The two flows begin from the same post composer but have different publishing actions. 
 
20. SCHEDULED POST VS DRAFT 
Do not automatically describe a scheduled post as a draft. 
A draft generally means content that has not yet been configured for publication. 
A scheduled post has a future publication configuration. 
For chatbot purposes: 
Draft: content being prepared and not necessarily scheduled. 
Scheduled post: content that has been configured for a future date and time through 
WiseIN's scheduling interface. 
If WiseIN later provides explicit Draft functionality, it should be documented separately. 
 
21. SCHEDULED POSTS AND POST CONTENT 
Scheduled posts remain subject to WiseIN's content rules. 

WiseIN's current Content Policies apply to posts, comments, clips, job listings, events, 
messages, and meeting recordings. They require content to be real, useful, respectful, and 
authentic.  
Users should not use scheduled posting to automate spam or repetitive content. 
WiseIN explicitly prohibits: 
• 
Copy-paste posts across multiple communities  
• 
Repetitive messages  
• 
Posting the same thing repeatedly  
• 
Irrelevant links  
• 
Fake opportunities  
• 
Scams  
• 
Fake credentials  
• 
Impersonation  
• 
Privacy violations  
• 
Copyright infringement.  
 
22. SCHEDULED JOB AND OPPORTUNITY POSTS 
Scheduled posting may be used for content categorized as an Opportunity, but the 
content must still comply with WiseIN's policies. 
WiseIN states that every job, gig, internship, or opportunity posted on the platform must be 
genuine. 
If an opportunity is: 
• 
unpaid,  
• 
equity-only,  
• 
part-time,  
that information should be disclosed honestly.  
Chatbot example 

User: 
“Can I schedule an internship opportunity post?” 
Answer: 
“Yes. If the Opportunity post is available to your account, you can prepare it in the post 
composer and use Schedule to select a future date and time. Make sure the opportunity is 
genuine and clearly disclose important conditions such as whether it is unpaid, equity-
only, or part-time.” 
 
23. SCHEDULED POSTS AND SPAM 
Scheduling should not be used to repeatedly publish the same content. 
WiseIN's Content Policies explicitly prohibit repetitive posting and copy-paste spam.  
Chatbot answer 
User: 
“Can I schedule the same post multiple times?” 
Recommended answer: 
“WiseIN's Content Policies prohibit repetitive spam and posting the same content 
repeatedly. Avoid using scheduled posts to repeatedly publish identical or low-value 
content.” 
Do not invent a specific numerical posting limit. 
 
24. SCHEDULED POSTS AND PRIVACY 
WiseIN's Privacy Policy states that posts and other content are part of the information 
users create or interact with on the platform. Users can edit or delete certain information 
through account settings.  
Users should therefore review the content before scheduling it, especially when it 
contains: 
• 
Personal information  
• 
Contact details  
• 
Professional information  

• 
Images of other people  
• 
Company information  
• 
Confidential material  
• 
Sensitive documents  
WiseIN's Content Policies prohibit publicly sharing sensitive information such as financial 
data, ID proofs, salary details, and internal company information.  
 
25. COPYRIGHT AND SCHEDULED POSTS 
Scheduling does not remove the user's responsibility for the content. 
WiseIN's policies state that users should only post content they created or have 
permission to use. 
Users should not schedule: 
• 
copied articles,  
• 
stolen designs,  
• 
pirated documents,  
• 
unauthorized copyrighted media,  
• 
someone else's work presented as their own.  
 
26. PREMIUM AND POSTING CAPABILITIES 
WiseIN's current pricing page states that Premium includes: 
Post unlimited articles, Clips & waves 
However, this does not establish that Scheduled Posts themselves are a Premium-only 
feature. 
The supplied UI shows the scheduling interface, but the public pricing page does not 
explicitly identify scheduling as a separate Premium-only feature. 
Chatbot rule 
Do not answer: 

“Scheduled Posts are only available to Premium users.” 
unless current product documentation confirms this. 
Instead: 
“WiseIN provides a Scheduled Post feature through the post composer. Availability and any 
plan-specific restrictions should be checked against the user's current account and 
subscription.” 
 
27. MOBILE AND WEB EXPERIENCE 
WiseIN officially supports a mobile application and describes the app as providing: 
• 
video calls,  
• 
slot booking,  
• 
chat,  
• 
events,  
• 
posts,  
• 
clips,  
• 
articles,  
• 
notifications.  
However, the current public app page does not provide detailed documentation for the 
Scheduled Posts interface. 
Therefore, the chatbot should not assume that every scheduling control shown in the 
supplied web UI is identical on Android or iOS. 
 
28. NOTIFICATION RELATIONSHIP 
Scheduled posts are different from notifications. 
A scheduled post concerns future content publication. 
Notifications concern alerts and updates. 

The current WiseIN app documentation confirms that WiseIN provides notifications, 
including notifications when someone books the user.  
However, the public documentation does not explicitly confirm: 
• 
whether a notification is sent immediately after scheduling,  
• 
whether a reminder is sent before publication,  
• 
whether a notification is sent after publication,  
• 
whether failed scheduled posts generate notifications.  
Therefore, these should not be presented as guaranteed behavior. 
 
29. SCHEDULED POST LIFECYCLE 
For chatbot/RAG purposes, model the feature conceptually as: 
Create → Schedule → Configure → Preview → Confirm → Scheduled → Publication 
Potential states may include: 
• 
Scheduled  
• 
Published  
• 
Deleted/Cancelled  
• 
Failed  
However, only Scheduled and the scheduling workflow are directly supported by the 
supplied UI. 
The other states should be treated as conceptual unless the backend/API exposes them 
explicitly. 
 
30. TROUBLESHOOTING 
Problem: Schedule option is not visible 
Possible causes may include: 
• 
UI/version differences  
• 
account capability differences  

• 
temporary product issue  
• 
post composer not fully loaded  
• 
feature availability differences  
Recommended response 
“If the Schedule option is missing, refresh WiseIN and reopen the post composer. If it 
remains unavailable, check whether the feature is available for your current account and 
contact WiseIN support if necessary.” 
Do not tell the user that scheduling is definitely restricted to a particular subscription 
unless verified. 
 
Problem: Cannot select a date 
Recommended checks: 
1. Reopen the Schedule Post screen.  
2. Check whether the date picker is responding.  
3. Verify the selected date.  
4. Refresh the page/app if necessary.  
5. Retry from a fresh post.  
Do not invent a specific minimum or maximum scheduling period. 
 
Problem: Time is incorrect 
Ask the user to check: 
• 
selected time,  
• 
selected time zone,  
• 
device/browser time,  
• 
WiseIN's displayed scheduling time.  
The scheduling UI explicitly contains a Time Zone selector. 
 

Problem: Wrong time zone selected 
Open the scheduling screen and review the Time Zone field before confirming the 
schedule. 
If the scheduled post has already been confirmed and the UI does not provide a 
reschedule/edit control, do not instruct the user to assume that it can be changed. 
 
Problem: Scheduled post does not appear 
Check: 
1. Settings → Scheduled post  
2. Refresh the page.  
3. Confirm that the scheduling action was completed.  
4. Check whether the schedule date/time has already passed.  
5. Retry if the post was never successfully scheduled.  
If the issue persists, escalate with: 
• 
account identifier that support requires,  
• 
approximate scheduling time,  
• 
selected date,  
• 
selected time,  
• 
selected time zone,  
• 
screenshot/error message.  
Never ask the user for their password, OTP, authentication token, or other secrets. 
 
31. IF A SCHEDULED POST DOES NOT PUBLISH 
The current public WiseIN documentation does not specify a formal failure-state workflow 
for scheduled posts. 
Therefore, the chatbot should not invent a specific cause. 
Recommended answer: 

“If a scheduled post did not publish as expected, first check Settings → Scheduled post and 
confirm the scheduled date, time, and time zone. If the schedule was configured correctly 
but the post still did not publish, contact WiseIN support with the relevant schedule details 
and any error message.” 
 
32. SUPPORT ESCALATION 
WiseIN provides a Contact page and support channels for product questions.  
For a scheduled-post issue, the chatbot should collect only non-sensitive diagnostic 
information such as: 
• 
what the user was trying to do,  
• 
date/time selected,  
• 
time zone,  
• 
whether Schedule Post was pressed,  
• 
visible error message,  
• 
screenshot if useful,  
• 
browser/app context.  
Never request: 
• 
Password  
• 
OTP  
• 
Verification code  
• 
Session token  
• 
API key  
• 
Payment PIN  
• 
Authentication credentials  
 
33. AI CHATBOT INTENTS 
The chatbot should recognize these Scheduled Post intents. 

Scheduling 
• 
schedule_post  
• 
create_scheduled_post  
• 
how_to_schedule_post  
• 
schedule_post_later  
• 
schedule_post_for_future  
Date and time 
• 
select_schedule_date  
• 
select_schedule_time  
• 
schedule_time_zone  
• 
recommended_schedule_time  
Management 
• 
view_scheduled_posts  
• 
manage_scheduled_posts  
• 
delete_scheduled_post  
• 
scheduled_posts_settings  
Troubleshooting 
• 
schedule_option_missing  
• 
schedule_date_error  
• 
schedule_time_error  
• 
schedule_timezone_issue  
• 
scheduled_post_missing  
• 
scheduled_post_not_published  
• 
schedule_post_error  
Policy 
• 
scheduled_post_spam  

• 
scheduled_opportunity_post  
• 
scheduled_post_privacy  
• 
scheduled_post_copyright  
 
34. IMPORTANT ENTITIES FOR RAG 
Useful entities include: 
• 
Scheduled Post  
• 
Schedule Post  
• 
Post  
• 
Post Composer  
• 
Update  
• 
Looking for  
• 
Opportunity  
• 
Ask  
• 
Date  
• 
Time  
• 
Time Zone  
• 
Recommended time  
• 
Preview Post  
• 
Schedule Post button  
• 
Settings  
• 
Scheduled post  
• 
Delete posts  
• 
Content Policies  
• 
Privacy  
• 
Premium  

• 
Articles  
• 
Clips  
• 
Waves  
 
35. RAG KNOWLEDGE VS LIVE PRODUCT DATA 
The chatbot should separate static documentation from live user-specific information. 
RAG/static knowledge 
Store: 
• 
What Scheduled Posts are  
• 
Scheduling workflow  
• 
Date/time/time-zone concepts  
• 
Composer categories  
• 
Current UI terminology  
• 
Content policies  
• 
Privacy rules  
• 
Copyright rules  
• 
Spam rules  
• 
Troubleshooting guidance  
• 
Known limitations  
Live API/backend information 
If WiseIN provides authorized APIs, retrieve dynamically: 
• 
User's actual scheduled posts  
• 
Scheduled post IDs  
• 
Scheduled dates  
• 
Scheduled times  
• 
Current status  

• 
User's account permissions  
• 
User's subscription  
• 
Whether a post exists  
• 
Whether a schedule operation succeeded  
• 
Whether a scheduled post was published  
• 
Deletion/cancellation status  
The LLM should not fabricate live scheduled-post information from RAG content. 
 
36. RECOMMENDED CHATBOT ARCHITECTURE 
For a user question such as: 
“What scheduled posts do I have?” 
the system should not answer from documentation. 
Instead: 
Chat UI → Chat API → Authentication → Authorized Scheduled-Posts API → Current user 
data → LLM → Response 
For: 
“How do I schedule a post?” 
the system can answer primarily from the RAG knowledge base. 
This distinction is important because a knowledge document can explain the feature but 
cannot know the user's current scheduled posts. 
 
37. GOLDEN ANSWERS FOR THE CHATBOT 
Q: How do I schedule a post? 
“Create your post and select Schedule instead of Post. On the Schedule Post screen, 
choose the date, time, and time zone, then use Preview Post to review it and select 
Schedule Post to confirm.” 
 

Q: Where can I see my scheduled posts? 
“Open Settings → Scheduled post. Your scheduled-posts page is where scheduled 
content can be managed.” 
 
Q: Can I choose a time zone? 
“Yes. The Schedule Post screen includes a Time Zone selector.” 
 
Q: What is the recommended time? 
“The scheduling interface can display a Recommended time. WiseIN's public 
documentation does not currently explain the criteria or algorithm used for that 
recommendation.” 
 
Q: Can I preview a scheduled post? 
“Yes. The Schedule Post screen includes a Preview Post option before you confirm the 
schedule.” 
 
Q: Can I schedule an Opportunity post? 
“If the Opportunity category is available in your post composer, you can prepare the post 
and use the scheduling workflow. Make sure the opportunity is genuine and clearly 
disclose important conditions such as unpaid, equity-only, or part-time work.” 
 
Q: Can I schedule spam? 
“Scheduled posting should not be used for repetitive or spam content. WiseIN's Content 
Policies prohibit repetitive posts and copy-paste spam.”  
 
Q: My scheduled post did not publish. What should I do? 
“First check Settings → Scheduled post and verify the scheduled date, time, and time 
zone. If the schedule was configured correctly but the post did not publish, contact WiseIN 
support with the relevant details and any error message.” 

 
38. UNSUPPORTED DETAILS — DO NOT INVENT 
The following details are not sufficiently confirmed by the current public WiseIN 
sources or supplied screenshots: 
• 
Maximum number of scheduled posts  
• 
Minimum scheduling interval  
• 
Maximum scheduling horizon  
• 
Exact scheduling API  
• 
Exact backend scheduler  
• 
Exact publication queue  
• 
Exact publication timestamp precision  
• 
Automatic retry behavior  
• 
Failure/retry mechanism  
• 
Exact scheduled-post status values  
• 
Individual scheduled-post editing  
• 
Rescheduling  
• 
Publish-now functionality  
• 
Individual cancellation  
• 
Bulk scheduling  
• 
Recurring posts  
• 
Scheduling across multiple accounts  
• 
Cross-posting  
• 
Exact notification/reminder behavior  
• 
Exact algorithm behind Recommended time  
• 
Engagement prediction  
• 
Best-time calculation  

• 
Exact Premium restriction for scheduling  
• 
Exact mobile scheduling UI  
• 
Exact timezone list  
• 
Exact media limits specifically for scheduled posts  
• 
Exact character limit for every post type  
• 
Automatic timezone conversion behavior  
• 
Scheduled-post analytics  
• 
Scheduling API availability for third-party integrations  
The chatbot must respond with “not currently documented” or escalate rather than 
inventing an answer. 
 
39. SOURCE PRIORITY FOR THIS FEATURE 
When answering Scheduled Posts questions, use the following priority: 
Priority 1 — Current WiseIN product UI 
The supplied screenshots are especially important for: 
• 
Settings → Scheduled post  
• 
Schedule option  
• 
Schedule Post screen  
• 
Date selector  
• 
Time selector  
• 
Recommended time  
• 
Time Zone  
• 
Preview Post  
• 
Schedule Post  
• 
Delete posts  
• 
Current post categories  

• 
Current composer terminology  
Priority 2 — Official WiseIN documentation 
Use official WiseIN policies and public product pages for: 
• 
Content rules  
• 
Privacy  
• 
Posting capabilities  
• 
Subscription information  
• 
General WiseIN functionality  
WiseIN's current pricing page confirms Premium posting capabilities including unlimited 
articles, Clips and Waves.  
WiseIN's current app page confirms that users can post updates, Clips and articles and 
manage their WiseIN activity through the app.  
Priority 3 — Internal product/API documentation 
Use internal documentation when available for: 
• 
exact API behavior,  
• 
scheduling states,  
• 
limits,  
• 
permissions,  
• 
cancellation,  
• 
editing,  
• 
publication jobs,  
• 
error codes.  
Priority 4 — General assumptions 
Do not use generic social-media behavior to fill gaps in WiseIN's documentation. 
 
40. RAG METADATA 
Recommended metadata: 

document_id: WISEIN-SCHEDULED-POSTS-001 
feature: Scheduled Posts 
category: Content Publishing 
platform: WiseIN 
content_type: Product Knowledge Base 
audience: Users, Support, AI Chatbot 
source_priority: Current UI + Official WiseIN Documentation 
status: Active 
Suggested retrieval tags: 
scheduled post 
scheduled posts 
schedule post 
schedule a post 
post later 
future post 
post scheduling 
schedule date 
schedule time 
time zone 
recommended time 
preview post 
delete posts 
settings scheduled post 
update 
looking for 
opportunity 

ask 
post composer 
content publishing 
 
41. FINAL CHATBOT RULES 
The WiseIN chatbot should follow these rules: 
1. Use “Scheduled post” as the current Settings terminology shown in the UI.  
2. Explain the scheduling flow using the actual visible sequence: 
Schedule → Date → Time → Time Zone → Preview Post → Schedule Post.  
3. Mention Recommended time only as a UI feature, not as a guaranteed engagement 
optimization.  
4. Treat Asia/Calcutta in the screenshot as an example selected time zone, not a fixed 
requirement.  
5. Do not claim a specific maximum scheduling period.  
6. Do not invent scheduled-post limits.  
7. Do not invent automatic reminders or notifications.  
8. Do not assume scheduled posts are Premium-only.  
9. Apply WiseIN Content Policies to scheduled content.  
10. Do not encourage repetitive or spam scheduling.  
11. For live questions about a user's actual schedules, use an authorized backend/API 
rather than RAG alone.  
12. Never request passwords, OTPs, tokens, or authentication credentials.  
13. When an exact behavior is undocumented, clearly say so instead of guessing.  
14. Prefer the current WiseIN UI over older documentation when the two differ.  
15. Treat supplied screenshots as current UI observations, not as permanent 
guarantees of future UI behavior.  
 

42. ONE-PARAGRAPH KNOWLEDGE SUMMARY 
WiseIN Scheduled Posts allows users to prepare a post and publish it at a selected future 
date and time. From the WiseIN post composer, users can select Schedule instead of 
Post, then choose a date, time, and time zone, review the content using Preview Post, 
and confirm using Schedule Post. The current supplied WiseIN UI also displays a 
Recommended time option. Scheduled posts can be accessed from Settings → 
Scheduled post, where the interface displays scheduled content and provides a Delete 
posts control. Scheduled content remains subject to WiseIN's Content Policies, including 
rules against spam, misinformation, fake opportunities, impersonation, privacy violations, 
and copyright infringement. WiseIN's public documentation does not currently establish 
exact scheduling limits, maximum scheduling horizon, reminder behavior, rescheduling 
rules, failure/retry behavior, or whether scheduling is restricted to a particular subscription, 
so the chatbot must not invent these details.  
 
 



---

