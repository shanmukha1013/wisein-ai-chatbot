# Profile

## Source: WISEIN-PROFILE-032.pdf

WISEIN—PROFILE 
CHATBOT KNOWLEDGE BASE & COMPLETE PRODUCT DOCUMENTATION 
Document ID: WISEIN-PROFILE-032 
Document Type: Product Knowledge Base / AI Customer Support / RAG Dataset 
Version: 1.0 
Platform: WiseIN 
Module: Profile 
1. PROFILE — OVERVIEW 
The Profile is a user's professional identity page on WiseIN. 
It allows a user to present information about their: 
• 
professional identity  
• 
current role  
• 
organization  
• 
professional introduction  
• 
About information  
• 
key skills  
• 
profile/introduction video  
• 
employment  
• 
education  
• 
certifications  
• 
courses  
• 
projects  
• 
professional links  
• 
Posts  
• 
Clips  
• 
Sessions  
• 
Webinars  

• 
availability/Slots  
• 
networking activity  
• 
other applicable professional information.  
The WiseIN product documentation defines the Profile as the central representation of a 
user's professional identity and explains that it supports professional discovery, 
networking, communication, and engagement.  
WiseIN's current public Privacy Policy also confirms that users may provide professional 
bio, skills, experience, education, projects, and social links to enhance their profile.  
 
2. PURPOSE OF THE PROFILE 
The Profile serves several purposes: 
Professional identity 
It tells other users who the person is professionally. 
Professional discovery 
Other users can discover professionals through WiseIN and access their profiles. 
Networking 
A profile gives other users information they can use to decide whether to follow, connect, 
communicate, or interact with the person. 
Professional presentation 
Users can showcase: 
• 
skills  
• 
education  
• 
employment  
• 
projects  
• 
certifications  
• 
professional interests  
• 
content  

• 
profile video.  
Availability and meetings 
The profile can be associated with: 
• 
Sessions  
• 
Slots  
• 
meetings  
• 
scheduling-related activities.  
Content and activity 
The profile can also provide access to the user's: 
• 
Posts  
• 
Clips  
• 
Webinars  
• 
Sessions.  
A complete profile may support professional discovery, networking, communication, and 
access to relevant opportunities depending on available WiseIN functionality.  
 
3. PROFILE STRUCTURE 
A WiseIN individual profile can be understood as these major areas: 
PROFILE 
│ 
├── Profile Header 
│   ├── Profile Photo 
│   ├── Name 
│   ├── Username 
│   ├── Current Role 
│   ├── Organization 

│   ├── Professional Tagline 
│   ├── Following 
│   ├── Followers 
│   ├── Conversations 
│   ├── Skills 
│   ├── Location 
│   └── Joined Information 
│ 
├── Open to 
│ 
├── About 
│ 
├── Key Skills 
│ 
├── Profile / Introduction Video 
│ 
├── Employment 
│ 
├── Education 
│ 
├── Projects 
│ 
├── Professional Website / Links 
│ 
├── Sessions 

│ 
├── Webinars 
│ 
├── Posts 
│ 
├── Clips 
│ 
├── Slots 
│ 
├── Profile Sharing 
│ 
├── Profile Analytics 
│ 
└── Recommended Profiles 
The supplied WiseIN application documentation identifies the same major profile 
categories.  
 
4. PROFILE HEADER 
The Profile Header is the top portion of the profile. 
The observed WiseIN interface contains: 
• 
profile photo  
• 
full name  
• 
username  
• 
current job title  
• 
current organization/professional information  
• 
short professional tagline/description  

• 
Following count  
• 
Followers count  
• 
Conversations count  
• 
skill tags/interests  
• 
location  
• 
joined information/date  
• 
profile actions such as editing or sharing where applicable.  
These elements are documented in the supplied application documentation.  
 
5. PROFILE PHOTO 
The profile header contains the user's profile photo. 
The photo represents the user's visual identity on WiseIN. 
The supplied documentation also notes that WiseIN's verification process can use a frame 
from verification video as the profile picture. WiseIN's current Privacy Policy describes this 
verification-video process and says a frame is taken from the video and added to the user's 
profile picture.  
Important chatbot rule 
Do not assume: 
• 
how many times a profile photo can be changed,  
• 
exact image dimensions,  
• 
exact image file size,  
• 
exact cropping rules,  
unless those details are confirmed by the current application. 
 
6. NAME 
The profile displays the user's full name. 
The name is part of the user's professional identity. 

The chatbot must distinguish between: 
Name 
and 
Username / handle. 
Do not treat them as interchangeable. 
 
7. USERNAME 
The profile also displays the user's WiseIN username. 
Example from the uploaded screenshot: 
@Shivaji 
The username is the account/profile identifier shown alongside the user's name. 
The chatbot should not assume that a username can be changed freely or that changing 
the display name automatically changes the username. 
Those behaviors require current application confirmation. 
 
8. CURRENT JOB TITLE 
The profile header can display the user's current professional role or job title. 
Example from the screenshot: 
AI Developer Intern At WiseIN 
This helps other users understand the person's current professional position. 
The supplied application documentation identifies current job title as part of the profile 
header.  
 
9. CURRENT ORGANIZATION 
The profile header may display the organization associated with the user's current 
professional role. 

The profile documentation identifies the current organization/professional information as 
part of the header.  
The chatbot must not infer the user's employer from: 
• 
email domain,  
• 
project names,  
• 
About text,  
• 
posts,  
• 
conversation content.  
Only the actual profile data should be treated as authoritative. 
 
10. PROFESSIONAL TAGLINE 
The profile header may contain a short professional tagline or description. 
Example visible in the screenshot: 
B.tech Cse Student | Ai & Full-Stack Developer | Python | Generative Ai | Sql 
This is different from the longer About section. 
Tagline 
Short professional positioning. 
About 
Longer professional description. 
The chatbot should understand both as separate profile components. 
 
11. FOLLOWING COUNT 
The profile header can show the number of users the profile is following. 
Example: 
4 Following 
The Following count represents users or organizations that the current user follows. 

The supplied application documentation identifies Following as a profile statistic.  
 
12. FOLLOWERS COUNT 
The profile header can display the number of followers. 
Example: 
2 Followers 
Followers are users who follow the profile. 
The chatbot should not assume that: 
Followers = Conversations 
or: 
Following = Connections. 
These are separate concepts. 
 
13. CONVERSATIONS COUNT 
The screenshot shows: 
4 conversations 
This is a profile-level activity/statistic visible in the observed interface. 
The supplied application documentation identifies Conversations alongside Following and 
Followers as profile statistics.  
The exact calculation/meaning of this count should not be invented unless the current 
WiseIN product definition confirms it. 
For example, do not automatically claim: 
"Conversations count means the number of people you have messaged." 
unless that behavior is explicitly verified. 
 
14. SKILL TAGS IN THE PROFILE HEADER 
The profile header can display skills/interests as tags. 

The screenshot shows: 
• 
Python  
• 
Java  
• 
JavaScript  
• 
Show more  
These are quick-view skill indicators. 
The full Key Skills section is a separate profile area. 
The chatbot should distinguish: 
Header skill tags 
from 
Key Skills section. 
 
15. LOCATION 
The profile header may display the user's location. 
The screenshot shows: 
India 
The supplied application documentation identifies location as profile metadata.  
Do not infer precise location from this field. 
For example: 
India 
does not mean the chatbot should infer the user's city, address, or coordinates. 
 
16. LANGUAGE 
The screenshot displays: 
English, Telugu 
This indicates language information associated with the profile. 

The exact profile-setting workflow for languages is not sufficiently documented in the 
supplied product documentation. 
Therefore the chatbot may explain the visible language field but should not invent: 
• 
maximum number of languages,  
• 
supported language list,  
• 
language ranking,  
• 
automatic language detection,  
unless confirmed by WiseIN. 
 
17. JOINED INFORMATION 
The profile can display information about when the user joined WiseIN. 
The screenshot shows: 
Joined Sep 2026 
The application documentation identifies Joined date as profile-header metadata.  
The chatbot should not infer: 
• 
exact account creation time,  
• 
verification date,  
• 
subscription start date,  
from the Joined date. 
 
18. VERIFIED PROFILE 
WiseIN is designed around verified professional identities. 
The current WiseIN website describes the platform as a professional network where every 
member is verified and presents government-verified profiles as a core part of the service.  
WiseIN's current pricing also lists a Verified profile with green badge for Basic users.  
Important distinction 
The chatbot must distinguish: 

Verification badge 
from 
Subscription badge 
from 
Student badge 
from 
Premium badge. 
The supplied documentation explicitly warns that subscription badges must not be treated 
as proof of identity verification.  
 
19. VERIFICATION BADGE 
A verified badge indicates that the user's applicable verification process has been 
approved. 
WiseIN's public website describes its professional network as government-verified and 
references identity verification using government-backed methods such as Aadhaar, 
DigiLocker, and PAN.  
Chatbot must NOT say: 
"The badge proves everything on the profile is verified." 
Instead: 
The verification badge indicates the user's applicable WiseIN verification status. It should 
not be treated as proof that every profile field, claim, skill, project, or achievement has 
independently been verified. 
This follows the supplied verification documentation.  
 
20. OPEN TO 
The profile interface includes: 
+ Add Open to 
This section is intended to communicate relevant professional intentions or availability. 

The supplied application documentation confirms the existence of Open to but states that 
its exact options and behavior require further verification.  
Therefore the chatbot can safely say: 
Open to is a profile section used to indicate relevant professional intentions or availability. 
But it must not invent an exact list of Open to categories. 
 
21. ABOUT 
The About section provides a longer professional introduction. 
It can contain information about: 
• 
professional background  
• 
interests  
• 
experience  
• 
skills  
• 
career direction  
• 
professional goals  
• 
other relevant information.  
The supplied documentation confirms that users can edit the About section through 
profile-editing controls.  
The screenshot demonstrates the About section appearing prominently on the profile. 
 
22. ABOUT VS PROFESSIONAL TAGLINE 
These should be treated separately. 
Professional tagline 
Short statement near the profile header. 
About 
Detailed professional description. 
Example: 

Tagline: 
AI & Full-Stack Developer | Python | Generative AI | SQL 
 
About: 
Longer description explaining professional background, 
skills, interests, experience and career goals. 
 
23. KEY SKILLS 
The Key Skills section displays skills associated with the user's professional profile. 
Skills are displayed as individual tags/labels. 
The supplied documentation gives examples such as: 
• 
Communication  
• 
Coding  
but the actual skills depend on what the user adds.  
The screenshot shows: 
• 
Python  
• 
Java  
• 
JavaScript  
• 
Show more  
 
24. WHY KEY SKILLS MATTER 
Skills can represent a user's professional capabilities. 
The supplied documentation states that skills may contribute to: 
• 
professional discovery  
• 
networking.  
WiseIN's public website also says users can discover verified professionals by skill.  

Therefore, the chatbot can explain: 
Key Skills help represent your professional capabilities and may help other users discover 
your profile through skill-based discovery. 
 
25. ADDING OR EDITING SKILLS 
The profile interface provides an edit control for Key Skills. 
The general workflow is: 
Open Profile 
↓ 
Open Key Skills 
↓ 
Select Edit 
↓ 
Add or update applicable skills 
↓ 
Save/confirm according to the current interface 
Do not invent: 
• 
maximum skill count,  
• 
exact skill taxonomy,  
• 
exact search behavior,  
• 
exact save-button wording,  
unless verified in the current interface. 
 
26. PROFILE VIDEO 
The profile includes a Video section. 
Its purpose is to allow the user to upload a profile or introduction video to make the 
profile more engaging and personal.  

The uploaded screenshot shows: 
Upload a profile or introduction video to make your profile more engaging and personal. 
 
27. PROFILE VIDEO — SUPPORTED FORMAT 
The supplied application documentation records the observed interface supporting: 
• 
MP4  
• 
WebM  
• 
MOV  
• 
AVI  
It also records: 
• 
maximum resolution: 1920 × 1080 px  
• 
maximum file size: 100 MB  
Important RAG rule 
These are observed interface requirements from the supplied WiseIN application 
documentation. 
They should be treated as authoritative only for the corresponding application version 
unless WiseIN confirms they remain current. 
If the live uploader displays different limits, the live/current product requirement should 
take precedence. 
 
28. PROFILE VIDEO — UPLOAD WORKFLOW 
General workflow: 
Open Profile 
↓ 
Find Video section 
↓ 
Select Edit / Upload 

↓ 
Choose profile or introduction video 
↓ 
Ensure the file meets the currently displayed requirements 
↓ 
Upload 
↓ 
Wait for processing 
↓ 
Confirm video appears on profile 
Do not invent an exact processing time. 
 
29. PROFILE VIDEO TROUBLESHOOTING 
If the video cannot be uploaded: 
Check: 
1. Supported file format.  
2. Maximum resolution.  
3. Maximum file size.  
4. Internet connection.  
5. Browser/app state.  
6. Camera/media permissions if applicable.  
7. Whether the current uploader displays a different requirement.  
Do not automatically claim the cause is a server issue. 
 
30. EMPLOYMENT 
The Employment section represents professional work experience. 

The supplied documentation says it can contain: 
• 
work experience  
• 
roles  
• 
organizations  
• 
career achievements.  
The profile provides an Add employment action.  
 
31. EMPLOYMENT — WHAT IT IS FOR 
Users can use Employment to present their professional career history. 
Possible information can include: 
• 
employer/organization  
• 
role  
• 
professional experience  
• 
career achievements.  
The exact fields and validation rules should be taken from the current employment 
interface. 
 
32. ADDING EMPLOYMENT 
General workflow: 
Open Profile 
↓ 
Go to Employment 
↓ 
Select Add employment 
↓ 
Enter the required professional information 

↓ 
Save 
↓ 
Review the employment entry on the profile 
The supplied application documentation explicitly uses this high-level workflow.  
 
33. EMPLOYMENT — CHATBOT RULE 
Do not invent exact fields such as: 
• 
employment start date  
• 
employment end date  
• 
employment type  
• 
location  
• 
description  
• 
current-job checkbox  
unless those fields are confirmed in the current WiseIN employment interface. 
 
34. EDUCATION 
The Education section allows users to present their academic background. 
The supplied application documentation identifies support for: 
• 
academic background  
• 
certifications  
• 
courses  
• 
learning accomplishments.  
It also shows an Add education action.  
 
35. EDUCATION — PURPOSE 

Education can be used to present: 
• 
academic qualifications  
• 
educational institutions  
• 
courses  
• 
certifications  
• 
learning accomplishments.  
The exact fields should be based on the current interface. 
 
36. ADDING EDUCATION 
General workflow: 
Open Profile 
↓ 
Education 
↓ 
Add education 
↓ 
Enter academic information 
↓ 
Add certifications/courses if supported 
↓ 
Save 
↓ 
Review the education entry 
 
37. PROJECTS 
The Projects section allows users to showcase relevant projects. 

The supplied documentation states that projects can represent: 
• 
practical work  
• 
professional accomplishments  
• 
academic work  
• 
other relevant activities.  
The profile provides an Add Projects action.  
 
38. WHY PROJECTS MATTER 
Projects allow a user to demonstrate what they have actually worked on rather than only 
listing skills. 
Examples can include: 
• 
software projects  
• 
academic projects  
• 
research work  
• 
professional projects  
• 
personal projects  
• 
other relevant work.  
Do not assume WiseIN verifies every project merely because it appears on a verified 
profile. 
 
39. ADDING PROJECTS 
General workflow: 
Open Profile 
↓ 
Projects 
↓ 
Select Add Projects 

↓ 
Enter project information 
↓ 
Save 
↓ 
Review project on profile 
The exact project fields must come from the current interface. 
 
40. EDUCATION VS PROJECTS VS EMPLOYMENT 
The chatbot should understand the difference: 
Education 
Academic background, courses, certifications, learning accomplishments. 
Employment 
Professional work experience, roles, organizations, career achievements. 
Projects 
Practical, academic, professional, or personal work showcased by the user. 
 
41. PROFESSIONAL WEBSITE / LINKS 
The uploaded profile screenshot shows a Website area in the profile's side panel. 
It says: 
Add your personal website, portfolio, or professional links to share with others. 
WiseIN's Privacy Policy also explicitly says users may provide social links as part of profile 
information.  
Therefore, the profile may contain professional external links such as: 
• 
personal website  
• 
portfolio  

• 
professional links  
• 
social/professional profiles.  
 
42. WEBSITE / PROFESSIONAL LINKS — CHATBOT RULE 
The chatbot should not assume that every user has a website. 
If no website is present, it should say that no website is currently displayed rather than 
inventing one. 
Do not infer a website from: 
• 
LinkedIn,  
• 
GitHub,  
• 
email address,  
• 
organization,  
• 
username.  
 
43. PROFILE TABS 
The uploaded screenshot shows the following profile tabs: 
About 
Sessions 
Webinars 
Posts 
Clips 
Slots 
The supplied WiseIN application documentation independently identifies these same 
observed profile activity sections.  
 
44. ABOUT TAB 
The About tab contains the user's professional profile information. 

It can include the profile's: 
• 
About  
• 
Key Skills  
• 
Video  
• 
Education  
• 
Employment  
• 
Projects  
• 
other profile information.  
 
45. SESSIONS TAB 
The Sessions tab provides access to applicable sessions associated with the user's 
profile. 
The exact session types, creation workflow, availability rules, and display behavior should 
be documented in the dedicated Sessions documentation. 
The profile documentation confirms the tab exists but does not establish all session 
behavior.  
 
46. WEBINARS TAB 
The Webinars tab displays applicable webinars associated with the profile. 
Webinars are also available through the broader Meetings module. 
Do not assume that every profile automatically has a webinar. 
 
47. POSTS TAB 
The Posts tab displays posts associated with the user. 
This connects the Profile module to the Posts/content module. 
If a user asks: 
"Where can I find my posts?" 

the chatbot can explain that the profile contains a Posts section/tab. 
The exact filtering and sorting behavior should come from the current Posts 
documentation. 
 
48. CLIPS TAB 
The Clips tab displays Clips associated with the user. 
This connects the Profile module to the Clips/content module. 
The current WiseIN website also confirms that users can post clips, while Premium 
explicitly includes publishing Clips.  
 
49. SLOTS TAB 
The Slots tab provides access to applicable booking/availability slots associated with the 
profile. 
WiseIN's public product pages describe smart slot booking as part of the platform's 
meeting/scheduling experience.  
The exact slot creation, availability, booking, cancellation, and timezone behavior should 
be handled by the dedicated Slots documentation. 
 
50. PROFILE SHARING 
The profile interface includes a Share your profile area. 
The observed interface provides: 
• 
profile link  
• 
Copy Link action.  
The screenshot also visibly shows a profile sharing card containing a profile URL and Copy 
Link button. 
 
51. HOW TO SHARE A PROFILE 
General workflow: 

Open your Profile 
↓ 
Find Share your profile 
↓ 
Select Copy Link 
↓ 
Share the copied WiseIN profile link 
The exact sharing options beyond Copy Link may vary between platforms. 
 
52. PROFILE LINK 
A profile link allows another person to access the user's WiseIN profile, subject to WiseIN 
access and visibility rules. 
The chatbot should not assume that every field displayed to the profile owner is visible to 
every other user. 
 
53. PROFILE ANALYTICS 
The screenshot shows an: 
Analytics Dashboard 
button. 
The supplied application documentation also confirms that the profile interface provides 
access to an Analytics Dashboard in the observed interface.  
WiseIN's current pricing states that: 
• 
Basic includes basic profile analytics.  
• 
Premium includes advanced profile analytics.   
 
54. BASIC VS ADVANCED PROFILE ANALYTICS 
Current public pricing distinguishes: 

Basic 
Basic profile analytics. 
Premium 
Advanced profile analytics. 
 
The chatbot should not invent the exact metrics contained in Basic or Advanced analytics 
unless those metrics are documented separately. 
 
55. PROFILE ANALYTICS — IMPORTANT RULE 
Do not claim: 
"Your profile received 500 views." 
unless the chatbot has an authorized live analytics tool. 
Profile analytics are account-specific information. 
The supplied application documentation explicitly says that detailed analytics data should 
be handled separately from general profile documentation.  
 
56. RECOMMENDED PROFILES 
The uploaded screenshot shows a Recommended Profiles section on the profile 
page/sidebar. 
It contains suggested professionals with profile information and follow actions. 
The exact recommendation algorithm is not documented in the sources reviewed. 
Therefore, the chatbot should not claim: 
"WiseIN recommends profiles based exactly on X." 
unless an official product source confirms the algorithm. 
 
57. PROFILE DISCOVERY 
WiseIN's current website says users can discover verified professionals by: 

• 
skill  
• 
industry  
• 
experience.  
 
This means profile information can play a role in professional discovery. 
The chatbot must distinguish: 
Documented discovery inputs 
from 
undocumented recommendation algorithms. 
 
58. PROFILE AND EXPLORE 
Profile and Explore are connected. 
The documented user journey is: 
Explore 
↓ 
Discover People 
↓ 
Open Profile 
↓ 
Review Professional Information 
↓ 
Follow / Interact / Communicate 
The supplied application documentation describes Explore as the area for finding people, 
organizations, topics, and relevant professional content, and explains that users can open 
relevant profiles from Explore.  
 
59. PROFILE AND MY NETWORK 

Profiles connect to networking functionality. 
A user can use profile information to understand another professional before interacting 
with them. 
My Network manages: 
• 
Following  
• 
Followers  
• 
Follow Requests  
• 
Requests Sent  
• 
Conversations  
• 
Recently Joined.  
 
60. PROFILE AND CHAT 
A profile can lead into communication with another user where the relevant functionality is 
available. 
The chatbot should not promise that every profile automatically allows messaging. 
Messaging permissions may depend on WiseIN's current rules, account state, relationship, 
or subscription. 
 
61. PROFILE AND MEETINGS 
WiseIN is designed around video-first professional interactions. 
The current public website says users can discover professionals and schedule a call.  
The profile can therefore connect with: 
• 
Sessions  
• 
Slots  
• 
Meetings  
• 
Webinars.  
The exact booking rules belong to the dedicated Meetings/Slots documentation. 

 
62. PROFILE AND POSTS 
A user's Posts are associated with the profile. 
The Profile therefore acts as both: 
Professional identity 
and 
Professional content history. 
Do not assume that every post appears on every profile view if visibility or content 
restrictions apply. 
 
63. PROFILE AND CLIPS 
The profile's Clips section provides access to clips associated with the user. 
Clips are a separate content type and should not be confused with the profile introduction 
video. 
Important distinction 
Profile Video 
= introductory/professional identity video. 
Clip 
= platform content published as a Clip. 
 
64. PROFILE VIDEO VS CLIP 
This distinction is important for chatbot training. 
Profile Video 
Located in the Profile's Video section. 
Purpose: 
Introduce yourself professionally. 
Clip 

Located under Clips/content. 
Purpose: 
Publish video-oriented content to the WiseIN ecosystem. 
Do not tell users that uploading a profile video automatically creates a Clip. 
 
65. PROFILE COMPLETENESS 
A profile can be developed progressively. 
Users may add: 
• 
About  
• 
Key Skills  
• 
Video  
• 
Employment  
• 
Education  
• 
Projects  
• 
Website  
• 
Open to  
• 
Sessions  
• 
Webinars  
• 
Posts  
• 
Clips  
• 
Slots.  
The chatbot should not claim that all fields are mandatory. 
The supplied documentation specifically says only fields verified in the application should 
be treated as mandatory.  
 
66. EDITING THE PROFILE 

The observed profile interface provides edit controls for: 
• 
profile information  
• 
About  
• 
Key Skills  
• 
Video.  
Additional sections such as Employment, Education, and Projects have their own Add 
actions. Some profile information may also be managed through: 
Settings → Edit Profile 
 
67. GENERAL PROFILE EDITING WORKFLOW 
Open Profile 
↓ 
Identify the section you want to change 
↓ 
Select the section's Edit / Add control 
↓ 
Enter or update information 
↓ 
Save/confirm using the current interface 
↓ 
Review the updated profile 
The exact button labels should be taken from the current application rather than invented. 
 
68. SETTINGS → EDIT PROFILE 
The supplied documentation identifies: 
Settings → Edit Profile 

as another area where profile information may be managed.  
Therefore, if the user cannot find a profile edit control directly on the profile page, the 
chatbot can direct them to: 
Settings → Edit Profile 
provided this path is still present in the current application. 
 
69. PROFILE VISIBILITY 
Profile information may be visible to other users according to WiseIN's applicable privacy 
and visibility controls. 
The supplied documentation explicitly instructs the AI not to assume that every profile 
field is publicly visible.  
WiseIN's current Privacy Policy says some public profile information such as name, 
professional details, and skills may be visible to other WiseIN users, subject to privacy 
settings.  
 
70. PRIVATE PROFILE INFORMATION 
The chatbot must not assume that every field on a profile is public. 
For questions such as: 
Can other users see my phone number? 
Can everyone see my education? 
Can I hide my employment? 
Who can see my profile? 
the chatbot must use the current WiseIN privacy/visibility rules. 
Do not guess. 
 
71. PROFILE DATA AND PRIVACY 
WiseIN's current Privacy Policy says users may edit or delete certain information through 
their account settings and that profile information can include: 

• 
professional bio  
• 
skills  
• 
experience  
• 
education  
• 
projects  
• 
social links.  
 
The same policy says some public profile information may be visible to other WiseIN users 
according to privacy settings.  
 
72. PROFILE DATA IS USER-SPECIFIC 
The chatbot must distinguish between: 
General profile knowledge 
"What is the About section?" 
and 
User-specific profile information 
"What is my About section?" 
The second requires authorized account data. 
The supplied documentation explicitly states that actual profile information is account-
specific.  
 
73. LIVE DATA REQUIREMENT 
If the chatbot has an authorized WiseIN profile API/tool, it may retrieve: 
• 
current name  
• 
username  
• 
job title  
• 
organization  

• 
About  
• 
skills  
• 
education  
• 
employment  
• 
projects  
• 
followers  
• 
following  
• 
profile activity  
• 
sessions  
• 
webinars  
• 
slots.  
Without live access, the chatbot must not pretend it knows the user's current profile 
information.  
 
74. EXAMPLES OF QUESTIONS REQUIRING LIVE DATA 
These require an authorized profile/account tool: 
What is my current job title? 
How many followers do I have? 
What skills are on my profile? 
Show me my projects. 
What is my latest Clip? 
How many conversations do I have? 
What slots are currently available? 
What is my profile analytics? 
The chatbot must not guess these values. 
 

75. GENERAL QUESTIONS THAT RAG CAN ANSWER 
These can be answered from static documentation: 
What is a WiseIN Profile? 
What is the About section? 
What are Key Skills? 
How do I add education? 
What is the profile video? 
What is Open to? 
What are the profile tabs? 
How do I share my profile? 
What are Slots? 
What is Profile Analytics? 
 
76. PROFILE COMPLETION — AI GUIDANCE 
If a user asks: 
"How can I improve my WiseIN profile?" 
The chatbot can provide a factual checklist: 
Complete your professional identity 
↓ 
Add a clear About section 
↓ 
Add relevant Key Skills 
↓ 
Add Education 
↓ 
Add Employment 

↓ 
Add relevant Projects 
↓ 
Add a professional profile/introduction video 
↓ 
Add professional website/links if applicable 
↓ 
Configure Open to if available 
↓ 
Use Sessions/Slots where applicable 
↓ 
Keep Posts and Clips relevant and professional 
Do not assign an unsupported "profile completion percentage." 
 
77. PROFILE QUALITY 
WiseIN's Content Policies require users to be honest about their identity and professional 
claims. 
Users should not: 
• 
claim expertise they do not have,  
• 
impersonate another person,  
• 
fabricate credentials,  
• 
fabricate work history,  
• 
exaggerate achievements,  
• 
upload fake certificates.  
WiseIN explicitly prohibits fake credentials and fabricated work history in its Content 
Policies.  
 

78. PROFILE AND FAKE CREDENTIALS 
If a user asks: 
"Can I add a certificate I didn't actually earn?" 
The chatbot should answer: 
No. WiseIN's Content Policies prohibit fake certificates, fabricated work history, false 
qualifications, and manipulated documents. 
 
 
79. PROFILE AND IDENTITY 
The profile should represent the actual user. 
WiseIN's Content Policies state that users should be honest about who they are and should 
not impersonate others.  
Therefore: 
A verified profile does not give permission to misrepresent professional experience, 
qualifications, or identity. 
 
80. PROFILE AND PROFESSIONAL CONTENT 
The profile may connect to: 
• 
Posts  
• 
Clips  
• 
Sessions  
• 
Webinars  
• 
meetings  
• 
professional networking.  
Users should maintain professional and truthful information across these areas. 
 
81. PROFILE AND RECOMMENDATIONS 

The screenshot shows Recommended Profiles. 
WiseIN's public website describes discovery of professionals by: 
• 
skill  
• 
industry  
• 
experience.  
 
The chatbot may explain that recommendations can help users discover professionals, but 
must not invent the exact recommendation algorithm. 
 
82. PROFILE AND SUBSCRIPTIONS 
Some profile-related capabilities vary by subscription. 
Current WiseIN public pricing identifies: 
Basic 
• 
verified profile with green badge  
• 
browse verified professionals  
• 
basic profile analytics  
• 
limited AI assistant access.  
Premium 
Includes: 
• 
advanced profile analytics  
• 
priority in AI-powered discovery  
• 
Premium badge on Profile  
• 
other premium capabilities.  
 
 
83. PREMIUM BADGE 

The current pricing page explicitly lists: 
Premium badge on Profile 
for Premium.  
This must not be confused with the identity verification badge. 
Verification badge 
Identity/verification-related. 
Premium badge 
Subscription-related. 
 
84. STUDENT BADGE 
WiseIN's current public pricing also lists a Student badge on profile for the Student plan.  
The chatbot must distinguish: 
• 
Verified badge  
• 
Student badge  
• 
Premium badge  
and must not say that one badge automatically proves the meaning of another. 
 
85. PROFILE AND STUDENT VERIFICATION 
For India, WiseIN's current public pricing states: 
Student Verification — College ID + Aadhaar 
and the Student plan includes a Student Badge on the profile.  
Detailed student-verification behavior should remain in the dedicated Student 
Verification knowledge document rather than being duplicated here. 
 
86. PROFILE AND IDENTITY VERIFICATION 
Individual verification is a separate feature from profile editing. 

The profile may display verification indicators, but the chatbot must not claim: 
"Editing your profile verifies your identity." 
Verification must be handled using the dedicated verification documentation and 
authorized verification status. 
 
87. PROFILE SECURITY 
The profile contains potentially sensitive information. 
The chatbot must: 
• 
respect authentication,  
• 
respect authorization,  
• 
protect private profile information,  
• 
avoid exposing account-specific information,  
• 
avoid revealing another user's private information.  
 
88. NEVER ASK FOR SENSITIVE CREDENTIALS 
The profile chatbot must never ask a user for: 
• 
password  
• 
OTP  
• 
authentication token  
• 
session token  
• 
full Aadhaar number  
• 
biometric information  
• 
private verification credentials.  
The supplied WiseIN verification documentation explicitly prohibits requesting passwords, 
OTPs, full Aadhaar numbers, or unnecessary identity documents through customer 
support.  
 

89. PROFILE ERROR TROUBLESHOOTING 
Common profile issues may include: 
• 
profile information not saving  
• 
About not updating  
• 
skill not appearing  
• 
education not appearing  
• 
employment missing  
• 
project missing  
• 
profile video upload failure  
• 
website not appearing  
• 
profile link not working  
• 
follower/following count appearing incorrect  
• 
profile tabs not loading  
• 
analytics unavailable  
• 
profile not visible as expected.  
 
90. PROFILE INFORMATION NOT SAVING 
Recommended chatbot flow: 
Check whether the required field is completed 
↓ 
Check for validation errors 
↓ 
Check network connection 
↓ 
Retry save 
↓ 

Refresh/reopen profile 
↓ 
Check whether the information appears 
↓ 
If still missing → escalate 
Do not invent a backend error unless logs confirm it. 
 
91. PROFILE VIDEO NOT UPLOADING 
Check: 
1. Current supported format.  
2. File size.  
3. Resolution.  
4. Internet connection.  
5. Current application error.  
6. Browser/app permissions.  
7. Whether the current uploader has changed requirements.  
The supplied interface documentation records MP4, WebM, MOV and AVI, 1920×1080 
maximum resolution and 100 MB maximum size, but explicitly says these requirements 
should be updated if the product changes.  
 
92. PROFILE NOT VISIBLE TO ANOTHER USER 
Do not immediately conclude that the account is blocked or deleted. 
Possible categories include: 
• 
visibility settings,  
• 
account state,  
• 
verification/access restrictions,  
• 
platform issue,  

• 
profile URL issue,  
• 
user relationship,  
• 
temporary loading issue.  
The chatbot should investigate using verified data. 
 
93. PROFILE ANALYTICS NOT SHOWING 
Do not claim a specific cause. 
Check: 
• 
subscription/access,  
• 
whether analytics are available,  
• 
whether the dashboard loads,  
• 
whether the account has activity,  
• 
current platform behavior.  
Current pricing distinguishes Basic profile analytics from Advanced profile analytics under 
Premium.  
 
94. PROFILE DATA IS WRONG 
If the user says: 
"My name/job/education is incorrect." 
The chatbot should guide them to the relevant profile editing control. 
If the incorrect information relates to identity verification and cannot be edited normally, 
the issue should be handled through the appropriate verification/support workflow. 
Do not tell the user to bypass verification controls. 
 
95. PROFILE VS SETTINGS 
The user can manage some profile information directly through the Profile interface. 
The supplied documentation also identifies: 

Settings → Edit Profile 
as another profile-management route.  
Simple distinction 
Profile 
= view and manage professional identity. 
Settings 
= broader account, privacy, security, subscription, and account-management controls. 
 
96. PROFILE VS ANALYTICS 
Profile 
Shows professional identity and public/profile information. 
Analytics 
Provides available insights into profile activity, visibility, or engagement. 
The screenshot shows an Analytics Dashboard from the profile sidebar. 
The exact analytics metrics belong to the Analytics documentation. 
 
97. PROFILE VS MY NETWORK 
Profile 
Represents who you are professionally. 
My Network 
Manages your professional relationships. 
My Network includes: 
• 
followers  
• 
following  
• 
follow requests  
• 
sent requests  

• 
conversations  
• 
recently joined users.  
 
98. PROFILE VS EXPLORE 
Explore 
Find people, organizations, topics, and content. 
Profile 
View the selected professional's identity and information. 
Typical flow: 
Explore 
↓ 
Search/Discover Person 
↓ 
Open Profile 
↓ 
Review Profile 
↓ 
Follow / Communicate / Interact 
 
99. PROFILE VS ORGANIZATION PROFILE 
An individual profile represents a person. 
An organization profile represents an organization. 
Do not mix individual-profile fields with organization-profile fields such as: 
• 
CIN  
• 
GST  
• 
organization verification  

• 
employee directory.  
Those belong to organization functionality. 
 
100. PROFILE DOCUMENTATION — AI INTENTS 
Recommended RAG intents: 
profile_definition 
profile_overview 
profile_header 
profile_photo 
profile_name 
profile_username 
profile_job_title 
profile_organization 
profile_tagline 
profile_followers 
profile_following 
profile_conversations 
profile_location 
profile_language 
profile_joined_date 
profile_open_to 
profile_about 
profile_key_skills 
profile_add_skill 
profile_edit_skill 
profile_video 

profile_video_upload 
profile_video_requirements 
profile_employment 
profile_add_employment 
profile_edit_employment 
profile_education 
profile_add_education 
profile_edit_education 
profile_projects 
profile_add_project 
profile_edit_project 
profile_website 
profile_social_links 
profile_sessions 
profile_webinars 
profile_posts 
profile_clips 
profile_slots 
profile_share 
profile_copy_link 
profile_analytics 
profile_recommended_profiles 
profile_edit 
profile_visibility 
profile_privacy 
profile_badge 

profile_verified_badge 
profile_student_badge 
profile_premium_badge 
profile_not_visible 
profile_not_updating 
profile_video_upload_error 
profile_analytics_error 
profile_data_error 
profile_completion 
profile_security 
 
101. PROFILE ENTITIES 
Recommended entities: 
profile 
user 
username 
name 
job_title 
organization 
tagline 
about 
skill 
location 
language 
joined_date 
open_to 

profile_video 
employment 
education 
certification 
course 
project 
website 
social_link 
session 
webinar 
post 
clip 
slot 
follower 
following 
conversation 
analytics 
verification_badge 
student_badge 
premium_badge 
profile_visibility 
 
102. RAG METADATA 
Recommended metadata: 
module: Profile 
feature: Individual Profile 

subfeature: Profile Header 
subfeature: About 
subfeature: Key Skills 
subfeature: Profile Video 
subfeature: Employment 
subfeature: Education 
subfeature: Projects 
subfeature: Profile Sharing 
subfeature: Profile Analytics 
subfeature: Sessions 
subfeature: Webinars 
subfeature: Posts 
subfeature: Clips 
subfeature: Slots 
subfeature: Profile Privacy 
subfeature: Profile Verification 
source_type: official_product_documentation 
audience: WiseIN_users 
requires_live_data: sometimes 
sensitivity: user_profile_data 
 
103. LIVE DATA CLASSIFICATION 
Static RAG can answer: 
What is a profile? 
What is Key Skills? 
How do I add education? 

What is the profile video? 
What are the profile tabs? 
How do I share my profile? 
What is Open to? 
Live API required: 
What is my job title? 
How many followers do I have? 
What skills are currently on my profile? 
What projects are on my profile? 
What is my latest Clip? 
What are my available Slots? 
What is my profile analytics? 
Who follows me? 
Who am I following? 
 
104. PROFILE API SECURITY MODEL 
For account-specific profile questions: 
User 
 ↓ 
Chat UI 
 ↓ 
Authenticated Chat API 
 ↓ 
Authorization 
 ↓ 
WiseIN Profile API 

 ↓ 
Retrieve only authorized user's data 
 ↓ 
LLM 
 ↓ 
Response 
Never: 
User 
 ↓ 
LLM 
 ↓ 
Entire Profile Database 
The AI should only retrieve information the authenticated user is authorized to access. 
 
105. EXAMPLE — USER ASKS ABOUT THEIR PROFILE 
User: 
What skills are on my profile? 
Correct architecture: 
Authenticate user 
↓ 
Call authorized Profile API 
↓ 
Retrieve current Key Skills 
↓ 
Return current skills 
Without API: 

I don't have access to your current profile data. You can open your Profile and check the 
Key Skills section. 
Do not invent skills. 
 
106. EXAMPLE — USER ASKS HOW TO ADD SKILLS 
User: 
How do I add skills? 
Chatbot: 
Open your WiseIN Profile, go to the Key Skills section, select the available edit option, add 
the relevant skills, and save using the current profile interface. 
 
107. EXAMPLE — USER ASKS HOW TO ADD EDUCATION 
Chatbot: 
Open your Profile and go to Education. Select Add education, enter the required academic 
information, and save it. The exact fields available may depend on the current WiseIN 
Education interface. 
 
108. EXAMPLE — USER ASKS HOW TO ADD A PROJECT 
Chatbot: 
Open your Profile, go to Projects, select Add Projects, enter the project information 
requested by WiseIN, and save it. 
 
109. EXAMPLE — USER ASKS HOW TO ADD EMPLOYMENT 
Chatbot: 
Open your Profile and go to Employment. Select Add employment, enter the requested 
work-experience information, and save it. 
 
110. EXAMPLE — USER ASKS HOW TO SHARE PROFILE 

Chatbot: 
Open your Profile and use the Share your profile section. WiseIN's observed interface 
provides a profile link and Copy Link option. Copy the link and share it with the person you 
want to connect with. 
 
111. EXAMPLE — USER ASKS ABOUT PROFILE VIDEO 
Chatbot: 
WiseIN provides a Video section where you can upload a profile or introduction video. The 
currently documented interface supports MP4, WebM, MOV and AVI, with an observed 
maximum resolution of 1920×1080 and maximum file size of 100 MB. These limits should 
be checked against the current uploader because product requirements can change.  
 
112. EXAMPLE — USER ASKS ABOUT PROFILE BADGES 
Chatbot: 
WiseIN can display different profile indicators, including a verification badge, Student 
badge, and Premium badge. These badges have different meanings. A subscription badge 
should not be treated as identity verification. 
 
113. EXAMPLE — USER ASKS "IS MY PROFILE VERIFIED?" 
The chatbot must not infer this from the presence or absence of a screenshot or profile 
information. 
If a live verification/profile API exists: 
Check verified status 
↓ 
Return confirmed status 
Otherwise: 
I can't confirm your current verification status without access to your WiseIN account data. 
You can check the verification indicator on your profile or the Verification section in your 
account. 

 
114. EXAMPLE — USER ASKS "WHY IS MY PROFILE NOT SHOWING?" 
The chatbot should first determine whether they mean: 
1. Their own profile page does not load.  
2. Their profile is not visible to another person.  
3. Their profile does not appear in Explore.  
4. A particular profile section is missing.  
These are different problems. 
 
115. EXAMPLE — PROFILE DOES NOT APPEAR IN SEARCH 
Do not automatically say: 
"Your profile has been hidden." 
Possible factors may include: 
• 
search indexing,  
• 
profile visibility,  
• 
account state,  
• 
verification/access rules,  
• 
search filters,  
• 
temporary application issues.  
Only confirmed causes should be presented as facts. 
 
116. PROFILE PRIVACY GUARDRAILS 
The chatbot must never disclose another user's: 
• 
private contact information  
• 
private profile information  
• 
private employment details  

• 
private education information  
• 
private account data  
• 
private analytics  
• 
private sessions  
• 
private slots  
• 
private conversations.  
Profile visibility must follow WiseIN's actual privacy controls. 
 
117. PROFILE CONTENT POLICY 
The profile and associated content should represent the real user. 
WiseIN prohibits: 
• 
impersonation  
• 
fake credentials  
• 
fabricated work history  
• 
false qualifications  
• 
manipulated documents.  
 
 
118. PROFILE DATA RETENTION 
WiseIN's current Privacy Policy states that account information is generally retained while 
the account is active, and users can request deletion subject to legal, security, fraud-
prevention, and other applicable retention requirements.  
Do not tell users that every profile field is immediately and permanently erased in every 
circumstance after deletion. 
 
119. PROFILE DATA CONTROL 

WiseIN's Privacy Policy says users can access, update, or request deletion of their 
information, subject to applicable restrictions.  
Therefore: 
Profile information can generally be managed by the user through the account/profile 
controls, while certain verification-related information may have additional restrictions. 
 
120. WHAT THE CHATBOT MUST NEVER INVENT 
Do not invent: 
• 
maximum number of skills  
• 
maximum About length  
• 
maximum number of projects  
• 
maximum employment entries  
• 
maximum education entries  
• 
exact profile completion score  
• 
exact profile ranking algorithm  
• 
exact recommended-profile algorithm  
• 
exact follower limits  
• 
exact profile visibility defaults  
• 
exact privacy settings  
• 
exact profile-view count  
• 
exact analytics metrics  
• 
exact Open to categories  
• 
exact Sessions categories  
• 
exact Slots limits  
• 
exact Webinar limits  
• 
profile video processing time  
• 
profile video duration  

• 
profile image specifications  
• 
username-change rules  
• 
profile URL-change rules  
unless those values are verified in current WiseIN product documentation. 
 
121. IMPORTANT CURRENT WEBSITE FACTS 
The current WiseIN website confirms several profile-related concepts: 
• 
WiseIN positions itself as a verified professional network.  
• 
Users can discover verified professionals by skill, industry, and experience.  
• 
WiseIN provides verified profiles.  
• 
Basic includes basic profile analytics.  
• 
Premium includes advanced profile analytics.  
• 
Premium includes a Premium profile badge.  
• 
Student plans include a Student badge.  
• 
Users can manage availability and slot bookings.  
• 
WiseIN's Privacy Policy allows users to provide professional bio, skills, experience, 
education, projects, and social links.   
 
122. PROFILE MODULE — MASTER USER JOURNEY 
Create WiseIN Account 
        ↓ 
Verify Account / Identity 
        ↓ 
Complete Professional Profile 
        ↓ 
Add About 

        ↓ 
Add Key Skills 
        ↓ 
Add Employment 
        ↓ 
Add Education 
        ↓ 
Add Projects 
        ↓ 
Add Profile / Introduction Video 
        ↓ 
Add Professional Website / Links 
        ↓ 
Configure Open to 
        ↓ 
Configure Sessions / Slots where applicable 
        ↓ 
Publish Posts / Clips 
        ↓ 
Attend / Host applicable Webinars 
        ↓ 
Share Profile 
        ↓ 
Discover Professionals 
        ↓ 
Network / Communicate / Meet 

The supplied WiseIN application documentation describes profile completion as part of 
the wider journey from account creation and verification into professional networking.  
 
123. PROFILE KNOWLEDGE BASE RULE 
For RAG purposes, Profile should be connected to these modules: 
Profile 
│ 
├── Verification 
│ 
├── Settings 
│ 
├── Explore 
│ 
├── My Network 
│ 
├── Chat 
│ 
├── Meetings 
│ 
├── Analytics 
│ 
├── Posts 
│ 
├── Clips 
│ 
├── Sessions 

│ 
├── Webinars 
│ 
└── Slots 
This is important because many user questions cross multiple modules. 
For example: 
"How can someone book a call with me?" 
may involve: 
Profile → Slots → Meetings 
while: 
"Why can't people see my profile?" 
may involve: 
Profile → Privacy → Verification → Account Status 
 
124. FINAL CHATBOT MASTER DEFINITION 
The chatbot should retain this as the core definition: 
A WiseIN Profile is the user's professional identity page. It allows the user to present 
their name, username, professional role, organization, professional description, key 
skills, location, profile video, employment, education, projects, professional links, 
and applicable activity such as Sessions, Webinars, Posts, Clips, and Slots. The 
profile supports professional discovery, networking, communication, and 
engagement. Some capabilities and profile information may depend on account 
status, verification, subscription, privacy settings, activity, and current product 
configuration. The chatbot must use live authorized WiseIN data for account-specific 
profile information and must never invent or expose private profile data.  
 
125. FINAL AI GUARDRAILS FOR PROFILE 
The Profile chatbot MUST: 

1. Explain every documented profile section.  
2. Distinguish profile fields from activity tabs.  
3. Distinguish verification badges from subscription badges.  
4. Protect private profile information.  
5. Use live data for user-specific profile questions when available.  
6. Never invent a user's profile information.  
7. Never invent analytics.  
8. Never invent follower/following counts.  
9. Never invent profile visibility.  
10. Never expose another user's private profile data.  
11. Use current UI labels when giving navigation instructions.  
12. Clearly identify when a workflow is only high-level.  
13. Treat observed video specifications as version-dependent.  
14. Escalate account-specific problems when live access is unavailable.  
15. Never request passwords, OTPs, full Aadhaar numbers, or biometric information.  
16. Never claim that a profile field is verified merely because the profile has a 
verification badge.  
17. Never claim that a profile is public in its entirety.  
18. Never promise profile analytics or recommendation behavior that is not 
documented.  
19. Never invent Open to categories.  
20. Never invent profile completion requirements. 
 
 



---

