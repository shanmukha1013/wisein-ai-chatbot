# Feed

## Source: WISEIN-FEED-ENGINE-011.pdf

WISEIN — FEED ENGINE & CONTENT STREAM CHATBOT KNOWLEDGE BASE 
Document ID: WISEIN-FEED-ENGINE-011 
Document Type: Product Knowledge Base & AI Chatbot Training Reference 
Version: 1.0 
Organization: Sanshi Network Tech Private Limited 
Platform: WiseIN 
Primary Area: Home / Feed 
 
1. PURPOSE OF THIS DOCUMENT 
This document explains how the WiseIN Feed works from a user-facing perspective and 
provides knowledge for the WiseIN AI chatbot. 
The chatbot should use this document to answer questions about: 
• 
What the WiseIN Feed is  
• 
How the Feed works  
• 
Trending  
• 
Following  
• 
Clips  
• 
Feed categories  
• 
All  
• 
Looking for  
• 
Opportunity  
• 
Ask  
• 
Post distribution  
• 
Feed visibility  
• 
Why posts may not appear  
• 
Feed troubleshooting  
• 
Post engagement  
• 
Content moderation  

• 
Reporting content  
• 
Privacy  
• 
Spam  
• 
Jobs and opportunities  
• 
Feed-related security  
• 
Differences between Feed and other WiseIN features  
The chatbot must not invent WiseIN's proprietary ranking algorithm or claim knowledge 
of internal ranking formulas that are not publicly documented. 
 
2. WHAT IS THE WISEIN FEED? 
The WiseIN Feed is the content stream through which users discover professional and 
community content on WiseIN. 
The current WiseIN Home page provides access to feed content and currently displays 
Trending, Following, and Clips views along with content/category controls. The public 
mobile-app information describes the Home Feed as supporting updates and events and 
says users can post updates, clips, and articles.  
The Feed can contain content such as: 
• 
Professional updates  
• 
Knowledge and experiences  
• 
Questions  
• 
Discussions  
• 
Opportunities  
• 
Jobs and internships  
• 
Events  
• 
Articles  
• 
Clips  
• 
Project-related content  

• 
Career-related information  
• 
Community content  
The Feed is part of WiseIN's broader verified professional-network experience. 
 
3. WISEIN'S FEED PHILOSOPHY 
WiseIN's public Content Policies describe the platform around authentic, useful and 
professional content. 
Examples of content WiseIN says users can post include: 
• 
What they are building or working on  
• 
What they have learned  
• 
Questions they need help with  
• 
Opportunities  
• 
Events  
• 
Achievements  
• 
Honest professional struggles  
• 
Knowledge that could help others  
The general principle is: 
If content is real, honest, useful, and appropriate for a professional network, it is more 
aligned with the purpose of WiseIN.  
The chatbot should therefore describe the Feed as a professional content and 
community stream, not simply as a generic social-media feed. 
 
4. IMPORTANT: WHAT IS VERIFIED ABOUT THE FEED ENGINE? 
The current public WiseIN website confirms the existence and user-facing behavior of the 
Feed and its views. 
However, the public website does not provide a complete technical specification of: 
• 
Ranking formulas  

• 
Recommendation weights  
• 
Engagement thresholds  
• 
Exact Trending algorithm  
• 
Exact Following ranking algorithm  
• 
Exact Clips ranking algorithm  
• 
Internal database/indexing architecture  
• 
Feed cache architecture  
• 
Exact distribution rules  
• 
Exact post propagation timing  
Therefore, the chatbot must never present these internal mechanisms as confirmed facts. 
For example, it should not say: 
"Trending posts are selected when they receive 50 likes within 10 minutes." 
unless an authorized internal source explicitly confirms that rule. 
 
5. FEED VIEWS 
The current WiseIN Home page exposes three important Feed views: 
1. Trending  
2. Following  
3. Clips  
These are different from the content-category filters: 
• 
All  
• 
Looking for  
• 
Opportunity  
• 
Ask  
The chatbot must understand this distinction. 
 

6. TRENDING FEED 
Trending is a Feed view for discovering content that is currently receiving attention across 
WiseIN. 
The WiseIN homepage publicly promotes discovering what is trending in the user's network 
and describes the platform as a place to discover verified individuals sharing insights, 
technology updates, and industry moments.  
Purpose of Trending 
Trending can help users discover: 
• 
Popular professional discussions  
• 
Interesting updates  
• 
Widely engaged content  
• 
Industry-related conversations  
• 
Content receiving attention across the network  
Important limitation 
WiseIN does not publicly document the exact algorithm or ranking weights used for 
Trending. 
Therefore, the chatbot should say: 
"Trending shows content that is currently receiving attention on WiseIN." 
It should not claim a precise ranking formula. 
 
7. FOLLOWING FEED 
Following is a Feed view focused on content associated with profiles or entities that the 
user follows, according to the relationships supported by the current application. 
The purpose is to help users keep up with the people and organizations they have chosen 
to follow. 
Example 
If a user asks: 
"How can I see posts from people I follow?" 

The chatbot should answer: 
"Open Home and select Following to view the Following Feed." 
Important limitation 
Do not claim that the Following Feed is strictly chronological unless current internal 
product documentation confirms this. 
Do not claim that it contains only direct connections if the application also supports 
following profiles or organizations. 
 
8. CLIPS FEED 
Clips is a Feed view focused on supported short-form video/clip content. 
The public WiseIN mobile-app page explicitly says users can post updates, clips, and 
articles, and the current Home page exposes Clips as a Feed view.  
Purpose 
Clips can be used for: 
• 
Short professional videos  
• 
Project demonstrations  
• 
Visual updates  
• 
Educational content  
• 
Other supported clip content  
Important limitation 
The public documentation does not establish exact: 
• 
Clip duration  
• 
File size  
• 
Resolution  
• 
Aspect ratio  
• 
Encoding format  
• 
Ranking formula  

The chatbot must not invent these specifications. 
 
9. FEED CATEGORY FILTERS 
The Home Feed also provides category/intent controls. 
The currently documented categories are: 
• 
All  
• 
Looking for  
• 
Opportunity  
• 
Ask  
These categories help users narrow the content they see. 
 
10. ALL 
All represents the general Feed without restricting the content to one specific intent 
category. 
Use All when: 
• 
The user wants to see the general feed.  
• 
A selected filter is empty.  
• 
The user wants to reset a category filter.  
• 
The user is unsure which category to choose.  
Example 
"If you want to return to the general Home Feed, select All." 
 
 
11. LOOKING FOR 
Looking for is intended for posts where the author is looking for something. 
Examples can include: 

• 
People  
• 
Talent  
• 
Co-founders  
• 
Professional help  
• 
Collaboration  
• 
Services  
• 
Mentorship  
• 
Advice  
The chatbot should not automatically equate Looking for with hiring. 
For example: 
"Looking for a co-founder" 
is different from: 
"We are hiring a software developer." 
 
12. OPPORTUNITY 
Opportunity is intended for professional opportunity-related content. 
Examples include: 
• 
Jobs  
• 
Internships  
• 
Projects  
• 
Freelance work  
• 
Partnerships  
• 
Other professional opportunities  
WiseIN's Content Policies specifically address jobs, gigs, internships and opportunities 
and require such opportunities to be genuine and accurately represented.  
 

13. ASK 
Ask is intended for questions and discussions. 
Examples include: 
• 
Technical questions  
• 
Career questions  
• 
Requests for advice  
• 
Professional discussions  
• 
Requests for help  
• 
Community questions  
Example 
"I don't understand how React state works. Can someone explain it?" 
This is naturally suited to an Ask type of post. 
 
14. DIFFERENCE BETWEEN FEED VIEWS AND FEED FILTERS 
This distinction is important for the chatbot. 
Feed Views 
Trending 
→ Discover content receiving attention. 
Following 
→ View content related to profiles/entities the user follows. 
Clips 
→ View supported clip/video content. 
Feed Categories 
All 
→ General content. 
Looking for 
→ People/help/collaboration/services being sought. 

Opportunity 
→ Professional opportunities being offered. 
Ask 
→ Questions and discussions. 
A user may therefore be using both a Feed view and a content category, depending on the 
current application interface. 
 
15. HOW CONTENT ENTERS THE FEED 
At a high level, the Feed works like this: 
1. A user creates supported content.  
2. The content is submitted to WiseIN.  
3. The platform processes the content.  
4. The content becomes available according to the platform's publishing, visibility, 
moderation, and distribution rules.  
5. Eligible users may encounter the content through relevant Feed views.  
6. Users can interact with supported content.  
7. Content may continue to receive engagement or become less prominent over time.  
The exact internal processing, indexing, ranking and distribution implementation is 
proprietary and should not be invented by the chatbot. 
 
16. POST LIFECYCLE — USER-FACING MODEL 
For chatbot purposes, the Feed lifecycle can be understood as: 
Stage 1 — Create 
The user creates a supported post/update/clip/article. 
Stage 2 — Submit 
The user submits the content through the relevant WiseIN interface. 
Stage 3 — Validation 

WiseIN may apply applicable account, content, security and platform rules. 
Stage 4 — Publication 
If successfully published, the content becomes available according to WiseIN's platform 
behavior. 
Stage 5 — Distribution 
Eligible users may encounter the content through appropriate Feed views. 
Stage 6 — Engagement 
Users may interact with the content through supported actions. 
Stage 7 — Moderation 
Content can be reported or reviewed when policy violations are suspected. 
Stage 8 — Removal or Restriction 
Content that violates WiseIN policies may be removed or the account may face restrictions 
or other enforcement actions.  
 
17. IMPORTANT CORRECTION TO THE ORIGINAL FEED REFERENCE 
The supplied reference stated: 
"Every post published on WiseIN passes through a 5-stage lifecycle." 
and described exact behavior such as: 
• 
Immediate injection into followers' feeds  
• 
Engagement thresholds  
• 
Automatic promotion to Trending  
• 
Specific metadata stamping  
• 
Verified employment tags  
• 
Exact archival behavior  
These details are not publicly documented sufficiently to treat them as confirmed 
product behavior. 
Therefore, the chatbot should use the safer user-facing lifecycle described above. 

This is important because otherwise the AI could give users false information about how 
WiseIN's internal Feed algorithm works. 
 
18. FEED RANKING 
Users may ask: 
"How does WiseIN decide what I see?" 
The correct general answer is: 
"WiseIN provides different Feed views such as Trending, Following, and Clips. The exact 
ranking and recommendation logic used internally is not publicly documented, so the 
chatbot should not claim specific ranking weights or formulas." 
If internal WiseIN engineering documentation later provides approved ranking information, 
that documentation can be added to the RAG knowledge base. 
 
19. TRENDING ALGORITHM 
The chatbot must not claim that Trending is based on a specific combination of: 
• 
Likes  
• 
Comments  
• 
Reposts  
• 
Engagement velocity  
• 
Author authority  
• 
Recency  
• 
Completion rate  
unless these factors are explicitly confirmed by WiseIN's current internal documentation. 
It is safe to say: 
"Trending is designed to help users discover content receiving attention on WiseIN." 
 
20. FOLLOWING ALGORITHM 

The chatbot must not claim: 
• 
Strict reverse chronological order  
• 
Exact personalization formula  
• 
Exact affinity scoring  
• 
Exact connection weighting  
unless confirmed internally. 
Safe answer: 
"Following helps you see content associated with profiles or entities you follow." 
21. CLIPS ALGORITHM 
The chatbot must not claim exact ranking factors such as: 
• 
Watch time  
• 
Completion rate  
• 
Rewatch rate  
• 
Engagement velocity  
• 
Creator score  
unless these are officially documented. 
Safe answer: 
"Clips is a Feed view focused on supported video/clip content." 
 
22. WHY DON'T I SEE A PARTICULAR POST? 
There can be many possible reasons. 
The chatbot should not automatically assume one cause. 
Possible explanations include: 
• 
The post is not part of the selected Feed view.  
• 
A category filter is active.  
• 
The user does not follow the relevant profile.  

• 
The content is not currently surfaced to the user.  
• 
The post was removed.  
• 
The post was deleted.  
• 
The account/content has restrictions.  
• 
There is a temporary Feed or network issue.  
The chatbot should ask a short clarifying question if necessary. 
 
23. POST NOT APPEARING IN FOLLOWING 
If a user says: 
"I follow this person but I don't see their post." 
Recommended troubleshooting: 
1. Check that the user is actually following the profile.  
2. Open Following.  
3. Check All to see whether the post appears elsewhere.  
4. Check whether the post is still available.  
5. Refresh the Feed.  
6. If other posts are also missing, troubleshoot the Feed itself.  
7. If only one post is missing, the post may no longer be available or may not be 
surfaced in that view.  
Do not claim that privacy settings are definitely responsible unless the application shows 
that information. 
 
24. POST NOT APPEARING IN TRENDING 
A post not appearing in Trending does not automatically mean that the post is broken. 
Trending is a discovery view. 
The chatbot should say: 

"Not every post is necessarily displayed in every Feed view. Trending is intended for content 
receiving attention across the network." 
Do not promise that every published post will appear in Trending. 
 
25. POST NOT APPEARING IN CLIPS 
A normal text post should not automatically be expected to appear in Clips. 
If a user asks: 
"Why isn't my text post showing in Clips?" 
Answer: 
"Clips is the Feed view for supported clip/video content. A normal text post may not appear 
there." 
 
26. POST NOT APPEARING UNDER OPPORTUNITY 
If the user created a post but cannot find it under Opportunity: 
Possible reasons include: 
• 
The post was not categorized as Opportunity.  
• 
The post was published under another category.  
• 
The Feed has not refreshed.  
• 
The post is not currently surfaced in that view.  
The chatbot should not automatically claim an indexing failure. 
 
27. POST NOT APPEARING UNDER ASK 
The same principle applies to Ask. 
If the user expects a post to appear under Ask: 
1. Check the selected post category.  
2. Check All.  
3. Refresh Home.  

4. Verify the post was successfully published.  
 
28. FEED IS NOT LOADING 
If the Feed does not load: 
Step 1 
Check the internet connection. 
WiseIN's mobile-app documentation lists a stable internet connection as a requirement.  
Step 2 
Refresh Home. 
Step 3 
Try another Feed view. 
For example: 
• 
Trending  
• 
Following  
• 
Clips  
Step 4 
Select All if a category filter is active. 
Step 5 
If using the web: 
• 
Refresh the browser.  
• 
If necessary, try another browser/private window.  
Step 6 
If using the mobile app: 
• 
Close and reopen the app.  
• 
Check that the app is updated if an update is available.  
Step 7 

If the entire application is affected: 
Contact WiseIN Support. 
 
29. FEED IS STUCK 
If the user says: 
"My Feed is stuck." 
The chatbot should avoid claiming a specific cause. 
Recommended response: 
"Try refreshing Home and switching between Trending, Following, or Clips. Also check your 
internet connection. If the Feed remains stuck across multiple views, contact WiseIN 
Support." 
 
30. FEED SHOWS OLD CONTENT 
Possible explanations include: 
• 
Feed has not refreshed.  
• 
Network connection issue.  
• 
Temporary application issue.  
• 
The selected Feed view currently has limited new content.  
Recommended steps: 
1. Refresh Home.  
2. Switch Feed views.  
3. Select All.  
4. Reopen WiseIN if necessary.  
5. Contact support if the Feed remains stale.  
Do not claim that browser cache is definitely the cause. 
31. FEED IS BLANK 
If the Feed is blank: 

1. Check internet connection.  
2. Refresh Home.  
3. Try Trending.  
4. Try Following.  
5. Try Clips.  
6. Select All.  
7. Check whether other WiseIN sections work.  
8. Reopen the application/browser.  
9. Contact Support if the issue persists.  
If all WiseIN sections fail, this is broader than a Feed-specific issue. 
 
32. DIFFERENCE BETWEEN EMPTY FEED AND BROKEN FEED 
An empty Feed is not necessarily an error. 
Empty Feed 
The application loads normally but there is no content displayed. 
Broken Feed 
The application fails to load, displays an error, continuously loads, or behaves incorrectly. 
The chatbot should distinguish these cases. 
 
33. REPORTING A POST 
WiseIN's Content Policies state that users can report: 
• 
Posts  
• 
Comments  
• 
Job listings  
• 
Events  
• 
Messages  

when they believe the content violates WiseIN policies.  
The exact reporting button/location may vary by current application version. 
Therefore, safe guidance is: 
"Open the available options menu on the content and use the Report option if it is 
provided." 
Do not promise an exact menu label or position if the current UI has changed. 
 
34. WHAT SHOULD BE REPORTED? 
Examples include: 
• 
Hate speech  
• 
Harassment  
• 
Scam content  
• 
Fake jobs  
• 
Fake credentials  
• 
Impersonation  
• 
Privacy violations  
• 
Fraud  
• 
Threats  
• 
Explicit prohibited content  
• 
Misinformation  
• 
Other serious policy violations  
Users should report genuine policy violations rather than simply disagreeing with 
someone's opinion.  
 
35. REPORTING IS CONFIDENTIAL 
WiseIN's current Content Policy states that reports are confidential and that the reported 
person will not know who submitted the report. 

The same policy states that reports are reviewed within 24 hours.  
Therefore the chatbot may state: 
"WiseIN says reports are confidential and are reviewed within 24 hours." 
This is a current policy statement and should be treated as such rather than as a guarantee 
of a particular outcome. 
 
36. DO NOT MISUSE REPORTING 
Users should not: 
• 
Mass-report someone as revenge  
• 
Report content simply because they disagree with it  
• 
Abuse the reporting system  
WiseIN states that false or abusive reporting can itself violate its policies.  
 
37. CONTENT MODERATION 
WiseIN's Content Policies govern content appearing on the platform. 
They cover: 
• 
Posts  
• 
Comments  
• 
Clips  
• 
Job listings  
• 
Events  
• 
Messages  
• 
Meeting recordings  
and other forms of user-generated content.  
The chatbot should explain moderation in terms of policy compliance, not claim specific 
hidden moderation technology. 
 

38. WHAT CONTENT IS ALLOWED? 
WiseIN explicitly gives examples of useful content: 
• 
Work/project updates  
• 
Learning  
• 
Questions  
• 
Opportunities  
• 
Events  
• 
Achievements  
• 
Honest struggles  
• 
Useful knowledge  
The chatbot can use these examples when helping a user decide whether something is 
appropriate to post.  
 
39. WHAT CONTENT IS NOT ALLOWED? 
WiseIN's Content Policies prohibit or restrict: 
• 
Violence  
• 
Hate speech  
• 
Discrimination  
• 
Sexually explicit content  
• 
Harassment  
• 
False claims  
• 
Misinformation  
• 
Fake credentials  
• 
Impersonation  
• 
Spam  
• 
Scam offers  

• 
Fake jobs  
• 
Pyramid schemes  
• 
Privacy violations  
• 
Unauthorized private conversations  
• 
Sensitive personal information  
• 
Copyright infringement  
• 
Stolen content  
• 
Plagiarism  
The exact enforcement depends on the violation.  
 
40. FAKE JOBS AND OPPORTUNITIES 
This is especially important for Feed-related chatbot responses. 
WiseIN states: 
Jobs, gigs, internships, and opportunities posted on WiseIN must be genuine. 
The author should accurately represent: 
• 
The role  
• 
Organization  
• 
Compensation  
• 
Paid/unpaid status  
• 
Equity-only status  
• 
Part-time/full-time nature  
WiseIN prohibits fake job offers and scams involving payment to obtain employment. 
41. SPAM 
WiseIN's Content Policies prohibit spam. 
Examples include: 
• 
Repeated copy-paste posts  

• 
Posting the same content multiple times  
• 
Repetitive messages  
• 
Irrelevant links  
Self-promotion is allowed when it is relevant and provides value. 
For example: 
"I built this project and here's what I learned" 
is substantially different from repetitive promotional advertising. 
 
42. MISINFORMATION 
Users should not publish: 
• 
False claims  
• 
Exaggerated statistics  
• 
Rumours presented as facts  
• 
Manipulated screenshots  
• 
Edited conversations presented misleadingly  
The chatbot should encourage users to verify important claims before posting them.  
 
43. IDENTITY AND CREDENTIALS 
WiseIN emphasizes verified identities. 
Users must not: 
• 
Impersonate another person  
• 
Pretend to represent a company without authorization  
• 
Use another person's identity  
• 
Post fake certificates  
• 
Fabricate qualifications  
• 
Claim work experience they do not have  

• 
Manipulate documents  
 
44. PRIVACY IN THE FEED 
Users should not publicly share another person's: 
• 
Phone number  
• 
Email  
• 
Address  
• 
Personal details  
without permission. 
Users should also not publicly post: 
• 
Private conversations  
• 
DM screenshots  
• 
Meeting chats  
• 
Financial data  
• 
Identity documents  
• 
Salary details  
• 
Confidential company information  
• 
Business strategies  
without appropriate authorization.  
 
45. MEETING CONTENT AND FEED 
WiseIN's Content Policies state that video calls are private. 
Users should not publicly post: 
• 
Call recordings  
• 
Transcripts  
• 
Meeting chats  

• 
AI meeting summaries  
without appropriate consent. 
If a user asks: 
"Can I post my AI meeting summary on the Feed?" 
the chatbot should respond: 
"WiseIN's Content Policies state that AI meeting summaries and other meeting content 
should not be shared publicly without the appropriate consent from the people involved." 
 
46. COPYRIGHT 
Users should only post content they created or have permission to use. 
Do not encourage: 
• 
Plagiarism  
• 
Stolen designs  
• 
Pirated documents  
• 
Copied articles  
• 
Unauthorized use of logos or brand assets  
WiseIN's Content Policies explicitly address ownership and copyright.  
 
47. COMMUNITY CONTENT 
WiseIN communities may have additional rules. 
Users should: 
• 
Follow community rules.  
• 
Stay on topic.  
• 
Respect community moderators.  
• 
Avoid unrelated promotional content.  
The Feed chatbot should recognize that platform-wide Content Policies and community-
specific rules can both apply.  

 
48. MODERATION CONSEQUENCES 
WiseIN's Content Policies describe possible consequences including: 
• 
Content removal  
• 
Warning  
• 
Temporary feature restriction  
• 
Account review  
• 
Suspension  
• 
Permanent ban  
Serious violations can result in stronger action, including suspension or permanent 
banning.  
The chatbot must not tell a user: 
"You will definitely receive a 3-day ban" 
unless that exact action has been returned by an authorized account system. 
 
49. POST REMOVED 
If a user says: 
"My post was removed." 
The chatbot should say: 
"WiseIN may remove content that violates its Content Policies. Review the policy relevant 
to your post. If you believe the removal was incorrect, contact WiseIN Support." 
The chatbot should not invent the reason for removal without an actual moderation 
message or authorized account data. 
 
50. POST HIDDEN 
If a user says: 
"Why is my post hidden?" 

Possible causes include: 
• 
Content moderation  
• 
Content availability  
• 
Temporary application issue  
• 
Post deletion  
• 
Account/content restrictions  
The chatbot should ask for the visible message or status rather than assuming the cause. 
51. POST DELETED 
If the user deleted their own post, it may no longer be available in the Feed. 
If the user says someone else's post disappeared, possible causes include: 
• 
Author deleted it  
• 
Content was removed  
• 
Feed availability changed  
• 
Temporary loading issue  
The chatbot must not claim which one happened without evidence. 
 
52. POST VISIBILITY 
The chatbot should avoid promising that every post is visible to every user. 
Feed visibility can depend on: 
• 
Feed view  
• 
Category  
• 
Relationship with the author  
• 
Content availability  
• 
Moderation  
• 
Platform behavior  
• 
Account state  

Exact visibility rules should come from current product documentation or authorized APIs. 
 
53. FEED VS PROFILE 
The Feed is for discovering content. 
A user's profile is the appropriate place to find information about that user and their profile-
level content where the application provides it. 
If a user says: 
"I can't find my old post in Feed." 
the chatbot should not automatically say that the post was deleted. 
The post may no longer be prominent in the Feed while remaining accessible elsewhere, 
depending on the application's current behavior. 
 
54. FEED VS JOBS 
The Opportunity Feed category and the Jobs area are related but not identical. 
Opportunity Feed 
Used to discover opportunity-related posts. 
Jobs 
Dedicated area for job and internship functionality. 
If a user says: 
"I need internships." 
the chatbot should consider directing them to Jobs rather than relying only on the Home 
Feed Opportunity filter. 
WiseIN's public site lists Job & Internship Board access as a platform feature.  
 
55. FEED VS EXPLORE 
Feed 
Used primarily for consuming and discovering published content. 

Explore 
Used for discovering professionals and other platform content. 
If the user says: 
"I want to find a software developer." 
the chatbot should consider Explore rather than simply searching the Feed. 
 
56. FEED VS CHAT 
Feed 
Public/community-oriented content. 
Chat 
Private communication functionality. 
If the user wants to contact someone privately, direct them to Chat rather than suggesting a 
public Feed comment. 
 
57. FEED VS MEETINGS 
Feed 
Posts, discussions, updates, clips, opportunities and other content. 
Meetings 
Video meetings and scheduling. 
If a user wants to arrange a professional conversation, the chatbot should guide them 
toward the appropriate meeting functionality. 
 
58. FEED VS WAVES 
The previously supplied WiseIN User Guide describes Waves as a separate short-
form/video-oriented platform area. 
The current public Home page separately exposes Clips. 
Therefore, the chatbot must not automatically treat: 

Waves = Clips = Home Feed 
as identical concepts. 
If the user asks specifically about Waves, switch to the Waves knowledge base. 
If the user asks about Clips within Home, use the Home/Feed knowledge base. 
 
59. MOBILE FEED 
WiseIN provides a mobile application. 
The official mobile information states that users can: 
• 
View Home Feed  
• 
Post updates  
• 
Post clips  
• 
Post articles  
• 
Join events  
• 
Use chat  
• 
Make video calls  
• 
Receive notifications  
It also states that a stable internet connection is required.  
The chatbot should account for platform differences when giving navigation instructions. 
 
60. WEB FEED 
The WiseIN website provides a Home page containing Feed functionality. 
If a user is using the browser: 
1. Open WiseIN.  
2. Sign in.  
3. Open Home.  
4. Use the available Feed controls.  

If the exact current UI differs, the chatbot should follow the visible application rather than 
relying on old screenshots. 
61. COMMON USER PROBLEMS 
The chatbot should recognize these common Feed questions: 
Navigation 
• 
"Where is my feed?"  
• 
"How do I open Home?"  
• 
"Where are my posts?"  
Trending 
• 
"What is Trending?"  
• 
"Why isn't my post trending?"  
• 
"Show popular posts."  
Following 
• 
"Why can't I see my friend's post?"  
• 
"Where are posts from people I follow?"  
Clips 
• 
"Where are videos?"  
• 
"How do I see clips?"  
Filters 
• 
"What is Opportunity?"  
• 
"What is Looking for?"  
• 
"What is Ask?"  
• 
"Why is my filter empty?"  
Posting 
• 
"How do I create a post?"  
• 
"Why can't I post?"  

• 
"My post failed."  
Moderation 
• 
"Why was my post removed?"  
• 
"How do I report a post?"  
• 
"Is this post allowed?"  
Troubleshooting 
• 
"Feed is blank."  
• 
"Feed isn't loading."  
• 
"Feed isn't refreshing."  
• 
"I see old posts."  
• 
"My post disappeared."  
 
62. USER LANGUAGE / SLANG MAPPING 
The chatbot should normalize informal expressions. 
"Feed" 
→ intent.feed.view 
"My feed" 
→ intent.feed.view 
"Main feed" 
→ intent.feed.view 
"What's trending?" 
→ intent.feed.trending 
"Popular posts" 
→ intent.feed.trending 
"Why don't I see my friend's posts?" 
→ intent.feed.following 

"People I follow" 
→ intent.feed.following 
"Show videos" 
→ intent.feed.clips 
"Short videos" 
→ intent.feed.clips 
"How does the algorithm work?" 
→ intent.feed.explain 
"Why don't I see a post?" 
→ intent.feed.visibility 
"Why is my feed empty?" 
→ intent.feed.troubleshoot 
"Feed stuck" 
→ intent.feed.troubleshoot 
"Feed isn't refreshing" 
→ intent.feed.refresh 
"Report this post" 
→ intent.feed.report 
"Flag this" 
→ intent.feed.report 
"This is spam" 
→ intent.feed.report 
"Why was my post removed?" 
→ intent.feed.moderation 
 
63. AI INTENT TAXONOMY 

The following intents should be supported. 
intent.feed.explain 
Explains the general Feed system. 
intent.feed.view 
Navigation to Home/Feed. 
intent.feed.trending 
Questions about Trending. 
intent.feed.following 
Questions about Following. 
intent.feed.clips 
Questions about Clips. 
intent.feed.filter 
General Feed filtering. 
intent.feed.filter_all 
All category. 
intent.feed.filter_looking_for 
Looking for category. 
intent.feed.filter_opportunity 
Opportunity category. 
intent.feed.filter_ask 
Ask category. 
intent.feed.visibility 
Questions about why content is or isn't visible. 
intent.feed.troubleshoot 
General Feed problems. 
intent.feed.refresh 

Feed not updating. 
intent.feed.create_post 
Creating Feed content. 
intent.feed.interact 
Like/comment/share/repost interactions. 
intent.feed.report 
Reporting content. 
intent.feed.moderation 
Content removal/restrictions. 
intent.feed.privacy 
Privacy questions. 
intent.feed.spam 
Spam questions. 
intent.feed.opportunity_safety 
Job/internship/opportunity safety. 
 
64. ENTITY TAXONOMY 
@Entity.FeedView 
Values: 
• 
Trending  
• 
Following  
• 
Clips  
@Entity.FeedCategory 
Values: 
• 
All  
• 
Looking for  

• 
Opportunity  
• 
Ask  
@Entity.ContentType 
Values: 
• 
Post  
• 
Update  
• 
Article  
• 
Clip  
• 
Job  
• 
Internship  
• 
Opportunity  
• 
Event  
• 
Question  
@Entity.FeedAction 
Values: 
• 
View  
• 
Like  
• 
Comment  
• 
Repost  
• 
Share  
• 
Save  
• 
Report  
@Entity.FeedProblem 
Values: 
• 
Blank  
• 
Loading  

• 
Stale  
• 
Missing  
• 
Filter failure  
• 
Post failure  
• 
Post removed  
• 
Post unavailable  
@Entity.ReportReason 
Values may include policy categories such as: 
• 
Spam  
• 
Harassment  
• 
False information  
• 
Inappropriate content  
• 
Scam  
• 
Privacy violation  
• 
Impersonation  
The chatbot should only expose reporting reasons actually available in the current 
interface. 
 
65. AI SECURITY GUARDRAILS 
Rule 1 — Never invent the algorithm 
Do not provide confidential or unsupported ranking formulas. 
 
Rule 2 — Do not promise Trending placement 
Never tell users: 
"Your post will become Trending if you get X likes." 
No such rule should be invented. 

 
Rule 3 — Do not claim guaranteed visibility 
Never say: 
"Everyone who follows you will definitely see your post." 
unless current platform documentation explicitly guarantees it. 
 
Rule 4 — Do not claim why a post disappeared without evidence 
A missing post may have multiple explanations. 
 
Rule 5 — Do not claim moderation action without evidence 
Only authorized moderation/account data can establish that a specific post was removed 
or restricted. 
 
Rule 6 — Do not request sensitive information 
Never ask for: 
• 
Password  
• 
OTP  
• 
Aadhaar number  
• 
PAN number  
• 
Session token  
• 
API key  
• 
Access token  
• 
Payment information  
 
Rule 7 — Do not request private documents through chat 
If verification is needed, direct the user to the official secure WiseIN verification flow. 

 
Rule 8 — Protect user privacy 
Never encourage publishing: 
• 
Personal contact details  
• 
Identity documents  
• 
Private conversations  
• 
Financial information  
• 
Confidential company information  
 
66. ACCOUNT-SPECIFIC INFORMATION 
The chatbot must distinguish between general Feed knowledge and real-time account 
information. 
General knowledge 
The chatbot can say: 
"WiseIN has Trending, Following and Clips Feed views." 
Account-specific 
The chatbot must not say: 
"Your post was removed." 
or: 
"Your account is restricted." 
unless an authorized backend system has provided that information. 
Similarly, it cannot claim: 
• 
Number of views  
• 
Likes  
• 
Comments  
• 
Followers  

• 
Current post status  
• 
Moderation status  
• 
Account restriction  
• 
Feed personalization  
without authorized data. 
 
67. WHEN THE CHATBOT SHOULD USE BACKEND TOOLS 
If WiseIN exposes authorized APIs/tools, the chatbot may use them for account-specific 
operations such as: 
• 
Retrieve user's own posts  
• 
Check whether a post exists  
• 
Check post status  
• 
Retrieve user's own Feed-related data  
• 
Retrieve notifications  
• 
Check account verification state  
• 
Retrieve supported content metadata  
All such operations must enforce: 
• 
Authentication  
• 
Authorization  
• 
User ownership  
• 
Data minimization  
• 
Logging  
• 
Rate limiting  
The AI must never receive unrestricted database access. 
 
68. FEED SECURITY ARCHITECTURE PRINCIPLE 

The LLM should not directly access WiseIN's database. 
Recommended architecture: 
User → Chat UI → Backend Chat API → Authentication/Authorization → Approved 
Feed/API tools + RAG → LLM → Response 
The LLM should receive only the information required to answer the question. 
 
69. EXAMPLE: USER ASKS ABOUT THEIR POST 
User: 
"Why can't I see my post?" 
Correct approach: 
1. Determine whether the user means:  
o Home Feed  
o Profile  
o Following  
o Trending  
o Opportunity/Ask filter  
2. If backend access exists, retrieve the user's authorized post status.  
3. Otherwise provide general troubleshooting.  
4. Do not invent a reason.  
 
70. EXAMPLE: USER ASKS WHY THEY ARE NOT TRENDING 
User: 
"Why isn't my post trending?" 
Correct response: 
"Not every post is necessarily shown in Trending. WiseIN does not publicly document a 
specific threshold or ranking formula for Trending, so I can't give you a guaranteed 

engagement number that makes a post trend. You can continue creating useful, relevant 
professional content and follow WiseIN's Content Policies." 
This response avoids pretending to know the proprietary algorithm. 
71. EXAMPLE: USER ASKS WHY THEIR FRIEND'S POST IS MISSING 
"Why can't I see my friend's post?" 
Recommended response: 
"First check that you're following the profile and that you're viewing the appropriate Feed. 
Try All and refresh Home. If the post is still missing, it may no longer be available or may not 
currently be surfaced in that Feed. If you can share the exact message you're seeing, I can 
narrow down the issue." 
 
72. EXAMPLE: USER ASKS HOW TO REPORT 
"How do I report a bad post?" 
Recommended response: 
"Open the post and use the available options menu to find Report, if it is provided in your 
current WiseIN version. Choose the applicable reason and submit the report. WiseIN's 
Content Policy says reports are confidential and should be used for genuine policy 
violations." 
 
73. EXAMPLE: USER REPORTS SCAM JOB 
"I found a fake job on WiseIN." 
Recommended response: 
"If you believe the job is fake or violates WiseIN's policies, report the job/post using the 
available Report option. Don't send money or sensitive personal information to the poster. 
WiseIN's Content Policies prohibit fake jobs, scam offers, and 'pay us first to get the job' 
schemes." 
 
74. EXAMPLE: USER WANTS TO POST PRIVATE INFORMATION 
"Can I post someone's phone number?" 

Correct response: 
"You should not publicly post another person's phone number, email address, address, or 
personal details without their explicit permission. WiseIN's Content Policies require users 
to respect other people's privacy." 
 
75. EXAMPLE: USER WANTS TO POST MEETING RECORDING 
"Can I upload my WiseIN meeting recording to Feed?" 
Correct response: 
"WiseIN's Content Policies state that video calls are private. Do not publicly share 
recordings, transcripts, or AI meeting summaries without the appropriate consent from the 
people involved." 
 
76. EXAMPLE: USER REPORTS BLANK FEED 
"My WiseIN Feed is blank." 
Recommended response: 
"First check your internet connection and refresh Home. Then try All, Trending, Following, 
or Clips. If other WiseIN sections are also not loading, reopen the app or website. If the 
Feed remains blank, contact WiseIN Support so the issue can be investigated." 
 
77. EXAMPLE: USER REPORTS STALE FEED 
"My Feed isn't updating." 
Recommended response: 
"Refresh Home and check your internet connection. You can also switch between Trending, 
Following, and Clips and then return to the Feed. If the content still doesn't update across 
multiple Feed views, contact WiseIN Support." 
 
78. EXAMPLE: USER WANTS INTERNSHIPS 
"Where can I find internships?" 

The chatbot should distinguish: 
Home Feed 
→ Use Opportunity to discover opportunity-related posts. 
Jobs 
→ Use the dedicated Jobs area for job and internship functionality. 
The current WiseIN public website lists Job & Internship Board access among its platform 
features.  
 
79. EXAMPLE: USER WANTS A DEVELOPER 
"I need a developer." 
The chatbot should determine the user's intention. 
If they want to find someone: 
→ Explore / networking. 
If they want to announce that they are looking for a developer: 
→ Home Feed → Looking for. 
If they want to hire for a formal job: 
→ Jobs / Organization hiring functionality may be more appropriate. 
 
80. EXAMPLE: USER WANTS TO ASK A TECHNICAL QUESTION 
"I want to ask developers for help." 
The chatbot can recommend: 
"You can create a Home Feed post and use the Ask category if that option is available in 
your current composer." 
 
81. RAG KNOWLEDGE CHUNK STRUCTURE 
For implementation, each Feed document chunk should ideally contain: 
Knowledge ID 

Example: 
WISEIN-FEED-001 
Feature 
Feed 
Subfeature 
Trending 
Intent 
intent.feed.trending 
User Query 
Example: 
Why isn't my post trending? 
Approved Answer 
Grounded response. 
Platform 
Web / Mobile / Both 
Authentication 
Required / Not required / Account-specific 
Security Level 
Public / Account-specific / Sensitive 
Source 
Official WiseIN documentation 
Verification Status 
Verified / Requires current application verification 
Last Verified 
Date of verification 
 

82. RECOMMENDED FEED RAG DOCUMENTS 
The chatbot knowledge base should eventually contain separate chunks/documents for: 
WISEIN-FEED-OVERVIEW 
WISEIN-FEED-TRENDING 
WISEIN-FEED-FOLLOWING 
WISEIN-FEED-CLIPS 
WISEIN-FEED-ALL-FILTER 
WISEIN-FEED-LOOKING-FOR 
WISEIN-FEED-OPPORTUNITY 
WISEIN-FEED-ASK 
WISEIN-FEED-CREATE-POST 
WISEIN-FEED-POST-INTERACTION 
WISEIN-FEED-VISIBILITY 
WISEIN-FEED-TROUBLESHOOTING 
WISEIN-FEED-MODERATION 
WISEIN-FEED-REPORTING 
WISEIN-FEED-PRIVACY 
WISEIN-FEED-SPAM 
WISEIN-FEED-JOBS 
WISEIN-FEED-SECURITY 
85. FINAL FEED AI DECISION TREE 
When a user mentions Feed, classify the question. 
"What is the Feed?" 
→ intent.feed.explain 
"Show me trending posts." 
→ intent.feed.trending 

"Show posts from people I follow." 
→ intent.feed.following 
"Where are videos?" 
→ intent.feed.clips 
"What is Looking for?" 
→ intent.feed.filter_looking_for 
"What is Opportunity?" 
→ intent.feed.filter_opportunity 
"What is Ask?" 
→ intent.feed.filter_ask 
"How does the algorithm work?" 
→ intent.feed.explain 
→ Explain only publicly supported behavior. 
"Why don't I see this post?" 
→ intent.feed.visibility 
"Feed is blank." 
→ intent.feed.troubleshoot 
"Feed isn't refreshing." 
→ intent.feed.refresh 
"My post failed." 
→ intent.feed.post_troubleshoot 
"Why was my post removed?" 
→ intent.feed.moderation 
"How do I report this?" 
→ intent.feed.report 
"This is a scam job." 

→ intent.feed.report + intent.feed.opportunity_safety 
"Can I post this person's phone number?" 
→ intent.feed.privacy 
"Can I post my meeting recording?" 
→ intent.feed.privacy 
"Where can I find internships?" 
→ intent.feed.opportunity + potentially Jobs 
 
86. FINAL CHATBOT RULE FOR FEED 
The WiseIN Feed is a professional content-discovery system within the Home experience. 
Users can access different Feed views such as Trending, Following, and Clips, and can 
use content categories such as All, Looking for, Opportunity, and Ask. 
The chatbot should explain the user-facing behavior of these Feed features accurately 
while avoiding unsupported claims about WiseIN's proprietary ranking algorithms, 
database architecture, engagement thresholds, or internal moderation systems. 
For troubleshooting, the chatbot should diagnose based on the user's actual symptoms 
rather than guessing the cause. 
For moderation, privacy, jobs, scams, and inappropriate content, the chatbot must follow 
WiseIN's current Content Policies. WiseIN explicitly emphasizes authentic content, 
prohibits spam, fake opportunities, impersonation, privacy violations and other harmful 
content, and provides reporting mechanisms for policy violations.  
For account-specific Feed information, the chatbot should only provide real-time answers 
when an authorized WiseIN backend/API supplies the relevant information. 
Primary product principle: 
Explain what the user can see and do, but never invent what the Feed engine does 
internally. 
 
 



---

