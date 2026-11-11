# Topics

## Source: WISEIN TOPICS DOCUMENTATION017.pdf

DOCUMENT 017 — WISEIN TOPICS 
DOCUMENTATION 
Draft 
Pending Verification 
Internal / AI-RAG 
Document ID: WISEIN-TOP-017 
1. Document Information 
Field 
Details 
Document Title 
WiseIN Topics Documentation 
Document ID 
WISEIN-TOP-017 
Document 
Category 
Explore, Search & Content Discovery 
Document 
Version 
1.0 
Document Status 
Draft — Pending Product, Engineering, and Support-Team Approval 
Prepared By 
Marella Shanmukha Reddy (MSR) 
Reviewed By 
To Be Assigned 

Approved By 
To Be Assigned 
Date Created 
17 September 2026 
Last Updated 
17 September 2026 
Document 
Classification 
Internal Use / Customer Support Knowledge / AI-RAG Knowledge 
Source 
Primary Purpose 
Document the Topics feature, visible interface elements, topic discovery, 
possible filtering behavior, troubleshooting, and AI customer-support 
guidance 
Source of 
Information 
WiseIN application screenshots, available WiseIN product 
documentation, application observations, and information requiring 
product-team confirmation 
Authority Status 
Not yet authoritative; requires verification and approval 
1.1 Document Ownership 
Responsibility 
Assigned To 
Document Preparation 
Marella Shanmukha Reddy 
Content Verification 
To Be Assigned 
Product Validation 
WiseIN Product Team 

Technical Validation 
WiseIN Engineering Team 
Customer Support Validation WiseIN Customer Support Team 
Final Approval 
Authorized WiseIN Management / Product Owner 
1.2 Document Control Notes 
●​ This document describes the Topics functionality based on currently available WiseIN 
interface observations and product documentation. 
●​ The topic names visible in the current interface should be treated as observed UI 
information. 
●​ The exact behavior after selecting a topic must be verified through application testing. 
●​ The document must not assume that selecting a topic automatically filters people, 
organizations, posts, events, or other content unless this behavior is confirmed. 
●​ Any unverified information must be clearly marked and must not be added to the 
authoritative AI/RAG knowledge base. 
●​ Changes to the Topics interface, available categories, filtering behavior, or navigation 
must be recorded in the version history. 
2. Purpose of This Document 
The purpose of this document is to provide a structured and accurate explanation of the Topics 
feature available within the WiseIN Explore and discovery experience. 
This document is intended to help: 
1.​ WiseIN users understand the purpose of Topics. 
2.​ Users discover professional interests and relevant areas of discussion. 
3.​ Customer-support personnel answer topic-related questions. 
4.​ The Product and Engineering teams verify topic functionality and behavior. 
5.​ The WiseIN AI Customer Support System provide accurate guidance. 
6.​ The documentation team build an approved knowledge base for Retrieval-Augmented 
Generation (RAG). 
The document also identifies areas that require additional testing, such as topic selection 
behavior, filtering logic, topic availability, and platform-specific differences. 

3. Scope of This Document 
This document covers the following areas: 
●​ Definition and purpose of Topics. 
●​ Relationship between Topics and the Explore module. 
●​ Accessing the Topics section. 
●​ Visible Topics interface elements. 
●​ Currently observed topic names. 
●​ Topic selection and discovery workflow. 
●​ Relationship between Topics and People. 
●​ Relationship between Topics and Organizations. 
●​ Relationship between Topics and posts or other content. 
●​ Search and filtering behavior. 
●​ Loading, empty, and error states. 
●​ Privacy and security considerations. 
●​ Platform-specific behavior. 
●​ AI customer-support guidance. 
●​ Human support escalation. 
●​ QA testing requirements. 
●​ Source and verification tracking. 
3.1 Out of Scope 
The following items are not fully defined in this document because they require separate 
documentation or product confirmation: 
●​ Internal topic-ranking algorithms. 
●​ Recommendation and personalization logic. 
●​ Backend search implementation. 
●​ Exact topic-to-content mapping. 
●​ Topic creation or administration. 
●​ Topic-following functionality, unless confirmed. 
●​ AI Search implementation. 
●​ Regular Search implementation. 
●​ Detailed People Search. 
●​ Detailed Organization Search. 
●​ Search result ranking and relevance. 
●​ Internal database structure and APIs. 
4. Overview of WiseIN Topics 
Topics are visible categories or areas of professional interest within the WiseIN discovery 
experience. 

They are presented in the Explore interface through a section labelled “Find by topic.” The 
purpose of this section is to help users navigate toward professional areas and interests that 
may be relevant to their discovery activity. 
Based on the currently observed WiseIN interface, Topics are displayed alongside 
search-related elements such as: 
●​ Regular Search. 
●​ AI Search. 
●​ People. 
●​ Organizations. 
●​ Search input. 
●​ Recent Searches. 
●​ Suggested for you. 
The current interface confirms that topic-related controls are available within the Explore 
experience. However, the exact behavior of each topic selection requires separate verification. 
4.1 Documentation Definition 
Topics are predefined areas of professional interest within WiseIN that help 
organize and support content and user discovery. The available topics and their 
exact filtering behavior must be verified against the current WiseIN application and 
approved product documentation. 
4.2 Important Verification Note 
The presence of a topic label in the interface confirms that the topic is displayed to the user. It 
does not, by itself, confirm: 
●​ What results will appear after selecting the topic. 
●​ Whether the topic filters people, organizations, posts, or events. 
●​ Whether the topic changes the search query. 
●​ Whether multiple topics can be selected. 
●​ Whether topics are personalized. 
●​ Whether topic selection is available on every platform. 
●​ Whether topics can be followed or saved. 
These behaviors must be tested and approved before being used as definitive AI knowledge. 
5. Purpose of the Topics Feature 
The Topics feature may support professional discovery by organizing areas of interest into 
recognizable categories. 

Based on the visible interface and WiseIN's professional networking context, Topics may help 
users explore areas related to: 
●​ Product development. 
●​ Business and finance. 
●​ Career growth. 
●​ Founder-related advice. 
●​ Fundraising. 
●​ Hiring and team building. 
●​ Startup development. 
●​ Marketing and go-to-market activities. 
The exact purpose and result behavior of each topic must be validated against the current 
application. 
5.1 Potential User Objectives 
Users may use Topics to: 
1.​ Discover professional areas of interest. 
2.​ Identify discussions or content related to a particular subject. 
3.​ Explore people or organizations associated with a professional area. 
4.​ Navigate the Explore experience without entering a complete search query. 
5.​ Find opportunities for learning, networking, and professional engagement. 
Verification status: The topic names and topic section are observed in the interface. The specific 
user outcomes listed above require confirmation through application testing. 
6. Accessing Topics 
6.1 Observed Navigation Area 
Topics are displayed within the Explore experience. 
A high-level navigation path is: 
WiseIN → Explore → Find by Topic → Select a Topic 
The exact button names, navigation transitions, and resulting screens must be confirmed 
through live testing. 
6.2 Access Requirements 
The following items require verification: 

Requirement 
Verification Status 
User must be logged in 
To Be Confirmed 
Topics available to all account types 
To Be Confirmed 
Topics available to verified users only 
To Be Confirmed 
Topics available to free-plan users 
To Be Confirmed 
Topics available to paid-plan users 
To Be Confirmed 
Topics available on web 
Interface observation 
available 
Topics available on Android 
Requires testing 
Topics available on iOS 
Requires testing 
Topics require profile completion 
To Be Confirmed 
Topics depend on user interests 
To Be Confirmed 
The AI must not claim that a specific account type, subscription, or verification status is required 
unless the requirement is documented and approved. 
7. Topics User Interface 

7.1 Observed Interface Elements 
The available Explore interface documentation identifies the following topic-related elements: 
●​ Find by topic. 
●​ All Topics. 
●​ Building Product. 
●​ Business & Money. 
●​ Career Advancement. 
●​ Founder Advice. 
●​ Fundraising 101. 
●​ Hiring & Team Building. 
●​ Idea to Launch. 
●​ Marketing & GTM. 
These labels are based on observed interface information. 
7.2 Topic Interface Structure 
The topic section can be documented at a high level as follows: 
Interface Element 
Description 
Status 
Find by topic 
Section for discovering topics 
Observed 
All Topics 
General topic option 
Observed 
Building Product 
Topic label related to product building 
Label observed; behavior 
pending 
Business & Money 
Topic label related to business and finance 
Label observed; behavior 
pending 
Career 
Advancement 
Topic label related to professional growth 
Label observed; behavior 
pending 

Founder Advice 
Topic label related to founder-oriented 
discussions 
Label observed; behavior 
pending 
Fundraising 101 
Topic label related to fundraising 
Label observed; behavior 
pending 
Hiring & Team 
Building 
Topic label related to hiring and teams 
Label observed; behavior 
pending 
Idea to Launch 
Topic label related to developing an idea 
into a launch 
Label observed; behavior 
pending 
Marketing & GTM 
Topic label related to marketing and 
go-to-market activities 
Label observed; behavior 
pending 
8. Observed Topic List 
The following topics were identified in the available WiseIN Explore interface. 
8.1 All Topics 
Description: A general topic option displayed in the Topics section. 
The exact function of All Topics must be verified. Possible behaviors that require testing include: 
●​ Displaying all available topics. 
●​ Removing a selected topic filter. 
●​ Returning the user to an unfiltered discovery view. 
●​ Showing all topic-related content. 
●​ Resetting the current topic selection. 
The AI must not state which behavior occurs until the application has been tested. 
8.2 Building Product 
Observed label: Building Product 

This topic label appears in the Find by Topic section. 
The label may relate to product development and product-building discussions. However, the 
exact content, people, organizations, and results associated with this topic must be confirmed 
through the application. 
Verification requirements: 
●​ Select the topic. 
●​ Record the resulting screen. 
●​ Identify whether people, organizations, posts, or other results are displayed. 
●​ Check whether the selected topic remains highlighted. 
●​ Verify whether the URL or search state changes. 
●​ Confirm whether the topic can be cleared. 
8.3 Business & Money 
Observed label: Business & Money 
This topic label appears in the Find by Topic section. 
The label may relate to business and finance-related professional interests. Its exact result 
mapping and available content require verification. 
Verification requirements: 
●​ Test the topic selection. 
●​ Record the displayed results. 
●​ Check whether results are relevant to the topic. 
●​ Verify whether the topic works with People and Organizations. 
●​ Check whether the topic is available on other platforms. 
8.4 Career Advancement 
Observed label: Career Advancement 
This topic label appears in the Find by Topic section. 
The label may relate to professional development, career growth, and advancement-related 
interests. The actual content and filtering behavior must be confirmed. 
Verification requirements: 
●​ Select Career Advancement. 
●​ Record the displayed results. 
●​ Check whether the results include people, organizations, posts, or other items. 

●​ Verify whether the selection affects the search input. 
●​ Test clearing and changing the selected topic. 
8.5 Founder Advice 
Observed label: Founder Advice 
This topic label appears in the Find by Topic section. 
The label may relate to founder experiences, startup-related guidance, and entrepreneurship 
discussions. The exact meaning and supported results must be verified through the relevant 
WiseIN content. 
The topic name alone should not be used to guarantee that a user will find a particular founder, 
advisor, event, or discussion. 
8.6 Fundraising 101 
Observed label: Fundraising 101 
This topic label appears in the Find by Topic section. 
The label may relate to introductory fundraising-related information or professional discussions. 
The following must be verified: 
●​ Whether it displays posts or discussions. 
●​ Whether it displays relevant people or organizations. 
●​ Whether it connects to Founder Conversations or Events. 
●​ Whether content is educational, community-generated, or categorized through another 
system. 
●​ Whether the topic is available to all users. 
8.7 Hiring & Team Building 
Observed label: Hiring & Team Building 
This topic label appears in the Find by Topic section. 
The label may relate to recruitment, hiring, collaboration, and building professional teams. The 
actual behavior and result categories require confirmation. 
The AI must not claim that selecting this topic guarantees access to job listings, candidates, 
recruiters, or hiring services. 
8.8 Idea to Launch 

Observed label: Idea to Launch 
This topic label appears in the Find by Topic section. 
The label may relate to the process of developing an idea into a product, project, or launched 
initiative. 
The exact topic definition and supported content must be verified from the current WiseIN 
application and approved documentation. 
8.9 Marketing & GTM 
Observed label: Marketing & GTM 
This topic label appears in the Find by Topic section. 
“GTM” commonly refers to Go-to-Market, but the exact meaning and official terminology used by 
WiseIN should be confirmed before this explanation is added to the authoritative knowledge 
base. 
The topic's actual result behavior, related content, and supported discovery categories require 
testing. 
9. Topic Selection Workflow 
The following is a proposed high-level workflow and must be verified against the current 
application. 
9.1 Expected Workflow for Testing 
1.​ Log in to the WiseIN application. 
2.​ Navigate to the Explore section. 
3.​ Locate the Find by Topic section. 
4.​ Review the available topic options. 
5.​ Select one topic. 
6.​ Observe the interface response. 
7.​ Record the displayed results or page transition. 
8.​ Check whether the selected topic is visually indicated. 
9.​ Check whether the search input changes. 
10.​Test whether the user can change or clear the topic. 
11.​Record any errors or unexpected behavior. 
9.2 Workflow Documentation Template 

Ste
p 
Action 
Expected Result 
Verificatio
n 
1 
Open WiseIN 
Application loads successfully 
Pending 
2 
Open Explore 
Explore section is displayed 
Pending 
3 
Locate Find by 
Topic 
Topic section is visible 
Observed 
4 
Select a topic 
Application responds to selection 
Pending 
5 
Review results 
Relevant results or content are displayed, if 
supported 
Pending 
6 
Change topic 
Results or selection state updates, if supported 
Pending 
7 
Clear topic 
Selection is removed or reset, if supported 
Pending 
10. Topic Filtering Behavior 
The exact filtering behavior of Topics is not fully confirmed by the available interface 
observations. 
The following questions must be answered through product and QA testing. 
10.1 Filtering Questions 
1.​ Does selecting a topic filter the current Explore results? 
2.​ Does selecting a topic automatically enter a search query? 
3.​ Does a topic filter People? 
4.​ Does a topic filter Organizations? 

5.​ Does a topic filter posts or feed content? 
6.​ Does a topic filter Events or Conversations? 
7.​ Does a topic filter Jobs? 
8.​ Can users select more than one topic? 
9.​ Can users combine a topic with keyword search? 
10.​Can users combine a topic with People or Organizations? 
11.​Does selecting All Topics remove other filters? 
12.​Is the topic selection retained when navigating away from Explore? 
13.​Does the topic selection appear in the URL? 
14.​Can users share a topic-filtered page? 
15.​Does the topic selection affect AI Search? 
10.2 Verification Table 
Behavior 
Current Status 
Single-topic selection 
Requires 
testing 
Multi-topic selection 
Requires 
testing 
Topic + keyword search 
Requires 
testing 
Topic + People filter 
Requires 
testing 
Topic + Organizations filter 
Requires 
testing 
Topic + AI Search 
Requires 
testing 

Topic + Regular Search 
Requires 
testing 
Topic + content filtering 
Requires 
testing 
Topic reset behavior 
Requires 
testing 
Topic persistence 
Requires 
testing 
Topic URL state 
Requires 
testing 
Until these behaviors are verified, the AI should use cautious language such as: 
“The Topics section is available in Explore. The exact results and filtering behavior 
may depend on the current WiseIN implementation. Please share what you see 
after selecting the topic, or contact support if the topic is not working as expected.” 
11. Relationship Between Topics and People 
The Explore interface includes a People selection option alongside the Topics section. 
Topics may be related to professional discovery, but it has not yet been confirmed whether 
selecting a topic displays: 
●​ People associated with the selected topic. 
●​ People who have listed relevant skills. 
●​ People who create content related to the topic. 
●​ People recommended by WiseIN. 
●​ People ranked through a search or recommendation system. 
The AI must not promise that a particular person will appear after selecting a topic. 

11.1 Required Testing 
●​ Select a topic and choose People, if the interface supports this combination. 
●​ Record the number and type of results. 
●​ Check whether the displayed profiles contain topic-related information. 
●​ Verify whether the results are keyword-based, profile-based, or recommendation-based. 
●​ Check whether the Follow and View actions remain available. 
●​ Record empty-result behavior. 
12. Relationship Between Topics and Organizations 
The Explore interface includes an Organizations selection option. 
The exact relationship between Topics and Organizations must be confirmed. 
Potential behaviors that require testing include: 
●​ Displaying organizations related to a selected topic. 
●​ Displaying organizations whose descriptions contain topic-related information. 
●​ Displaying organizations recommended by the platform. 
●​ Displaying organizations that publish topic-related content. 
The AI must not state that a topic selection provides a complete list of organizations in that 
industry or category. 
12.1 Required Testing 
●​ Select a topic. 
●​ Select Organizations, if supported. 
●​ Record the displayed organizations. 
●​ Verify whether organization names, descriptions, industries, and locations are shown. 
●​ Check whether Follow and View actions work. 
●​ Verify whether the results change when another topic is selected. 
13. Relationship Between Topics and Content 
The available documentation confirms that Topics are visible in the Explore experience. It does 
not fully establish whether topic selection filters or displays: 
●​ Posts. 
●​ Clips. 
●​ Events. 
●​ Founder Conversations. 
●​ Leadership and Career Conversations. 

●​ Waves. 
●​ Jobs. 
●​ Other professional activities. 
Therefore, topic-to-content relationships must be verified separately. 
13.1 Required Product Confirmation 
The Product or Engineering team should confirm: 
1.​ Which content types are assigned to topics. 
2.​ Whether users can discover posts through topics. 
3.​ Whether events or conversations have topic labels. 
4.​ Whether topics are used in recommendation systems. 
5.​ Whether topics are searchable through Regular Search. 
6.​ Whether topics are supported by AI Search. 
7.​ Whether users can create or assign topics to their own content. 
8.​ Whether topic categories are maintained by administrators or generated automatically. 
14. Topics and Regular Search 
Regular Search and Explore appear to provide related discovery functionality. The available 
documentation distinguishes topic controls from search methods. 
The current Explore interface includes: 
●​ Regular Search. 
●​ AI Search. 
●​ People. 
●​ Organizations. 
●​ Find by Topic. 
The exact technical relationship between Regular Search and Topics requires confirmation. 
14.1 Questions for Verification 
●​ Does selecting a topic modify the Regular Search query? 
●​ Can a user enter a keyword after selecting a topic? 
●​ Does Regular Search return topic-related results? 
●​ Are topic labels searchable as keywords? 
●​ Does Regular Search use the same results page as topic discovery? 
●​ Are the same filters available in both experiences? 
14.2 AI Response Guidance 

The AI may explain that Topics are available within Explore, but it must not claim that Regular 
Search and topic selection use the same backend, ranking algorithm, or filtering system unless 
Engineering confirms it. 
15. Topics and AI Search 
AI Search is documented as a separate search experience that may interpret natural-language 
discovery intent. 
Topics are visible as separate topic controls in Explore. The current documentation does not 
establish whether Topics are integrated with AI Search. 
15.1 Verification Requirements 
The following should be tested or confirmed: 
●​ Whether users can select a topic while using AI Search. 
●​ Whether AI Search understands topic names. 
●​ Whether AI Search uses topic metadata in retrieval. 
●​ Whether AI Search can answer questions about topic-related people or organizations. 
●​ Whether AI Search returns the same results as topic selection. 
●​ Whether the AI Search interface provides topic suggestions. 
15.2 Important Distinction 
Feature 
Documented Understanding 
Topics 
Visible topic-based discovery controls in Explore 
Regular Search 
Keyword-oriented search experience 
AI Search 
Natural-language or intent-oriented search 
experience 
Relationship Between 
Them 
Requires Engineering and Product confirmation 

The AI must not describe Topics as an AI-powered feature merely because they appear near 
the AI Search tab. 
16. Topic Selection State 
The selection state of Topics must be documented after live testing. 
16.1 Items to Verify 
●​ Whether a selected topic changes color or appearance. 
●​ Whether the selected topic displays a checkmark. 
●​ Whether the selected topic remains selected after scrolling. 
●​ Whether a user can select only one topic. 
●​ Whether a user can select multiple topics. 
●​ Whether selecting a new topic removes the previous selection. 
●​ Whether an active topic filter has a clear or close button. 
●​ Whether the topic selection remains active after navigating to another section. 
●​ Whether refreshing the page preserves the selected topic. 
16.2 Expected Documentation Format 
The final approved documentation should include screenshots or descriptions of: 
●​ Unselected topic state. 
●​ Selected topic state. 
●​ Multiple selected topics, if supported. 
●​ Cleared topic state. 
●​ Loading state after topic selection. 
●​ Empty-result state. 
●​ Error state. 
17. Loading, Empty, and Error States 
The exact error messages and loading behavior for Topics have not been fully verified. 
The following test scenarios should be included in QA. 
17.1 Loading Scenarios 
Scenario 
Expected Behavior to Verify 

Topics section initially loads 
Loading indicator or placeholder appears, if 
implemented 
Topic selected 
Results load without unnecessary delay 
Slow internet connection 
Loading state remains understandable 
Network interruption 
User receives a suitable error or retry option 
Page refresh 
Topics load correctly 
17.2 Empty-Result Scenarios 
Test whether the application displays an appropriate message when: 
●​ A topic has no matching results. 
●​ A selected topic is unavailable. 
●​ A user has no access to the relevant content. 
●​ Search and topic filters return no results. 
●​ The backend returns an empty response. 
The exact empty-state message must be recorded from the application rather than invented. 
17.3 Error Scenarios 
Potential scenarios include: 
●​ Topic selection does not respond. 
●​ Topic selection results in a blank screen. 
●​ Topic content fails to load. 
●​ A selected topic disappears. 
●​ Topics are unavailable after page refresh. 
●​ The application displays an unexpected error. 
●​ A topic redirects to an incorrect page. 
●​ Topic filtering produces unrelated results. 
For every error, document: 

1.​ Error title or message. 
2.​ Date and time of observation. 
3.​ Browser or device. 
4.​ User account type, where relevant. 
5.​ Steps to reproduce. 
6.​ Expected behavior. 
7.​ Actual behavior. 
8.​ Screenshot or screen recording. 
9.​ Frequency of occurrence. 
10.​Suggested area for technical investigation. 
18. Troubleshooting Guidance 
The following guidance should be used only after the relevant behavior has been verified. 
18.1 Topics Are Not Visible 
Suggested troubleshooting steps: 
1.​ Refresh the Explore page. 
2.​ Check whether the user is on the correct application section. 
3.​ Check the internet connection. 
4.​ Test using a supported browser or application version. 
5.​ Check whether the issue occurs across devices. 
6.​ Record the user's platform and application version. 
7.​ Escalate the issue if the Topics section remains unavailable. 
The AI must not claim that the Topics feature is restricted to a particular plan or verification 
status without approved documentation. 
18.2 Selecting a Topic Does Nothing 
Suggested troubleshooting steps: 
1.​ Confirm that the topic is visible and selectable. 
2.​ Ask the user to refresh the page. 
3.​ Check whether other topics respond. 
4.​ Check whether Regular Search or other Explore controls work. 
5.​ Record the exact behavior after selection. 
6.​ Request a screenshot or screen recording if appropriate. 
7.​ Escalate to human support if the issue persists. 
The AI must not claim that the topic selection was successfully applied unless an authorized 
system or user confirmation supports that statement. 

18.3 Topic Results Are Not Relevant 
The AI should: 
●​ Ask the user what topic they selected. 
●​ Ask what type of result they expected. 
●​ Clarify whether the issue concerns People, Organizations, posts, or another content 
type. 
●​ Avoid claiming that the search or recommendation algorithm is incorrect without 
evidence. 
●​ Record the result examples and escalate when necessary. 
18.4 Topic Is Missing 
The AI should: 
1.​ Confirm the exact topic name. 
2.​ Ask which platform the user is using. 
3.​ Confirm whether other topics are visible. 
4.​ Check the latest approved topic list. 
5.​ Avoid claiming that the topic has been permanently removed. 
6.​ Escalate if the missing topic may be related to a release, account restriction, or technical 
issue. 
19. Privacy and Security Considerations 
Topics may be associated with users' discovery activity, search behavior, or content interactions. 
The actual data collection and retention rules must be confirmed through WiseIN's approved 
privacy and engineering documentation. 
19.1 AI Privacy Rules 
The AI 
continue 
18.4 Topic Is Missing 
The AI should: 
1.​ Confirm the exact topic name. 
2.​ Ask which platform the user is using. 
3.​ Confirm whether other topics are visible. 
4.​ Check the latest approved topic list. 

5.​ Avoid claiming that the topic has been permanently removed. 
6.​ Escalate if the topic is missing despite being documented as available. 
Example AI response: 
“The available topics may vary depending on the current WiseIN interface. Please 
check whether other topics are visible in the Explore section. If a specific topic is 
missing, share the topic name and the platform you are using so our support team 
can investigate further.” 
19. Privacy and Security Considerations 
The Topics feature may involve discovery of professional content, users, or organizations. Its 
privacy and visibility behavior must be consistent with WiseIN's approved privacy and 
access-control policies. 
19.1 Privacy Requirements 
The following areas require verification: 
●​ Whether topic-related results respect profile visibility settings. 
●​ Whether private profiles appear in topic-based discovery. 
●​ Whether restricted organizations are visible. 
●​ Whether topic-related posts follow content visibility settings. 
●​ Whether blocked users or organizations appear in results. 
●​ Whether topic selections are stored in user activity history. 
●​ Whether topic preferences are used for personalization. 
●​ Whether search and topic activity is included in analytics. 
●​ Whether topic-related information is shared with third parties. 
19.2 AI Security Rules 
The AI Customer Support System must not: 
●​ Reveal private user information through topic-related searches. 
●​ Confirm whether a private account exists. 
●​ Expose internal topic-ranking logic or restricted metadata. 
●​ Bypass profile, organization, or content visibility settings. 
●​ Claim that all topic-related results are publicly accessible. 
●​ Provide information about another user's private activity. 
●​ Treat a topic label as proof of a user's professional expertise. 
●​ Assume that a user's topic selection represents their verified qualifications. 
19.3 Source-of-Truth Rule 

The AI must use: 
1.​ Approved WiseIN documentation for general Topics functionality. 
2.​ Authorized live systems for user-specific or real-time information. 
3.​ Human support for restricted, unresolved, or sensitive issues. 
If the AI does not have an approved source for a particular topic behavior, it must communicate 
the limitation rather than invent an answer. 
20. Platform-Specific Differences 
The Topics feature must be tested independently on each supported platform. 
20.1 Platforms for Verification 
Platform 
Verification Status 
Web Application 
Topic section 
observed 
Android Application 
Requires testing 
iOS Application 
Requires testing 
20.2 Platform Testing Areas 
The following must be compared across platforms: 
●​ Location of the Explore section. 
●​ Visibility of the Find by Topic section. 
●​ Number of available topics. 
●​ Topic names and spelling. 
●​ Topic layout and design. 
●​ Topic selection behavior. 
●​ Search and filtering functionality. 
●​ Loading performance. 
●​ Error messages. 
●​ Accessibility. 

●​ Screen responsiveness. 
●​ Topic persistence after navigation. 
●​ Compatibility with different screen sizes. 
20.3 Documentation Rule 
If the Topics feature behaves differently across platforms, each difference must be documented 
separately. 
The AI must not provide web-specific navigation instructions to a mobile user unless the 
instructions have been confirmed for that platform. 
21. AI Customer Support Guidance 
The WiseIN AI Customer Support System should assist users with general questions about 
Topics, navigation, and documented topic-related behavior. 
The approved WiseIN knowledge base must be the primary source for answering product 
questions. The AI must not generate unsupported information about topic availability, filtering, 
ranking, or recommendations. 
21.1 Questions the AI May Answer 
After approval and verification, the AI may answer questions such as: 
●​ “What are Topics in WiseIN?” 
●​ “Where can I find Topics?” 
●​ “What topics are available?” 
●​ “How do I open the Explore section?” 
●​ “What is the purpose of the Find by Topic section?” 
●​ “Why is a topic not visible?” 
●​ “What should I do if selecting a topic does not work?” 
●​ “How can I report an issue with Topics?” 
21.2 Questions Requiring Verified Information 
The AI must refer to approved documentation before answering: 
●​ “Which people are included under this topic?” 
●​ “Why am I seeing these organizations?” 
●​ “Does this topic filter posts?” 
●​ “Can I follow a topic?” 
●​ “Can I select multiple topics?” 
●​ “Does topic selection affect AI Search?” 

●​ “How are topics ranked?” 
●​ “Why are certain topics recommended to me?” 
●​ “Can I create my own topic?” 
If the documentation does not answer the question, the AI must clearly state that the behavior 
requires confirmation. 
21.3 AI Response Principles 
The AI should: 
1.​ Provide concise and understandable explanations. 
2.​ Use the official names of interface elements. 
3.​ Ask clarifying questions when the user's issue is unclear. 
4.​ Distinguish confirmed functionality from pending behavior. 
5.​ Avoid making assumptions about search or recommendation algorithms. 
6.​ Provide only approved troubleshooting steps. 
7.​ Escalate unresolved problems to human support. 
8.​ Avoid requesting passwords, OTPs, or unnecessary sensitive information. 
9.​ Avoid confirming account-specific information without an authorized data source. 
10.​Use the latest approved documentation. 
21.4 Example: General Topics Question 
User: “What are Topics in WiseIN?” 
Suggested AI Response: 
“Topics are predefined areas of professional interest available in the WiseIN 
Explore experience. They help organize professional discovery through categories 
such as Building Product, Business & Money, Career Advancement, and Founder 
Advice. The exact results displayed after selecting a topic depend on the current 
WiseIN implementation.” 
21.5 Example: Topic Not Working 
User: “I clicked a topic, but nothing happened.” 
Suggested AI Response: 
“Please try refreshing the Explore page and selecting the topic again. If the issue 
continues, check whether other topics respond correctly. Please share the topic 
name, the device or browser you are using, and what happens after you select it. If 
the issue remains unresolved, our support team can investigate further.” 

21.6 Prohibited AI Assumptions 
The AI must not: 
●​ Invent topics that are not listed in the approved knowledge base. 
●​ Claim that a topic filters a particular content type without verification. 
●​ State that a topic is personalized unless documented. 
●​ Claim that a topic guarantees specific people, organizations, jobs, or events. 
●​ Invent error messages. 
●​ Confirm that a topic was applied without evidence. 
●​ Claim that a topic has been removed without an approved source. 
●​ Provide unsupported information about ranking or recommendation logic. 
22. Human Support Escalation 
Topics-related issues should be escalated to human customer support when the AI cannot 
provide a verified resolution. 
22.1 Escalation Conditions 
Escalation may be required when: 
●​ The Topics section is unavailable for a user who should have access. 
●​ A documented topic is missing. 
●​ Selecting a topic does not produce the expected behavior. 
●​ Topic results are blank or unrelated. 
●​ Topic selection causes a page error. 
●​ The feature behaves differently across platforms. 
●​ A topic appears to expose restricted information. 
●​ A user reports a privacy or visibility issue. 
●​ The issue continues after approved troubleshooting. 
●​ The AI does not have sufficient information to answer accurately. 
●​ The issue may involve backend search or recommendation logic. 
●​ The issue requires account-specific investigation. 
22.2 Information to Include in an Escalation 
The escalation should include: 
Information 
Description 

User Identifier 
Use approved internal systems only 
Issue Category 
Topics / Explore / Search / Filtering 
Topic Name 
Name of the affected topic 
Platform 
Web, Android, or iOS 
Browser or App Version 
Where applicable 
Date and Time 
Approximate time of issue 
Steps to Reproduce 
Actions taken by the user 
Expected Behavior 
What the user expected 
Actual Behavior 
What happened 
Error Message 
Exact message, if displayed 
Screenshot 
Only when appropriate and permitted 
Frequency 
One-time, intermittent, or repeated 
Troubleshooting Completed Steps already attempted 

Conversation Context 
Relevant details from the support interaction 
Sensitive personal information must not be requested or attached unless the approved WiseIN 
process explicitly requires it through a secure channel. 
22.3 Support Channels 
The support channels and response expectations must be confirmed against the latest 
approved customer-support documentation. 
The available WiseIN support information identifies: 
●​ Support portal: https://www.wisein.in/help-support 
●​ Email: support@wisein.in 
●​ Live chat, where available 
●​ Official social media support channel, where applicable 
The AI should not guarantee a response time unless the current support policy confirms it. 
23. QA Test Cases 
The following test cases should be executed and documented before this document is 
approved. 
23.1 Access and Visibility Testing 
Test ID 
Test Case 
Expected Result 
Status 
TOP-00
1 
Open Explore after login 
Explore loads successfully 
Pending 
TOP-00
2 
Locate Find by Topic 
Topic section is visible 
Observe
d 
TOP-00
3 
Review all topic labels 
Available topics are displayed 
correctly 
Pending 

TOP-00
4 
Refresh Explore page 
Topics load correctly after refresh 
Pending 
TOP-00
5 
Test topic visibility on another 
account 
Behavior matches approved 
access rules 
Pending 
23.2 Topic Selection Testing 
Test ID 
Test Case 
Expected Result 
Status 
TOP-00
6 
Select All Topics 
Approved All Topics behavior occurs 
Pendin
g 
TOP-00
7 
Select Building Product 
Approved response is displayed 
Pendin
g 
TOP-00
8 
Select Business & Money 
Approved response is displayed 
Pendin
g 
TOP-00
9 
Select Career Advancement 
Approved response is displayed 
Pendin
g 
TOP-01
0 
Select Founder Advice 
Approved response is displayed 
Pendin
g 
TOP-01
1 
Select Fundraising 101 
Approved response is displayed 
Pendin
g 

TOP-01
2 
Select Hiring & Team Building 
Approved response is displayed 
Pendin
g 
TOP-01
3 
Select Idea to Launch 
Approved response is displayed 
Pendin
g 
TOP-01
4 
Select Marketing & GTM 
Approved response is displayed 
Pendin
g 
TOP-01
5 
Change from one topic to 
another 
Selection and results update correctly 
Pendin
g 
TOP-01
6 
Clear selected topic 
Topic is cleared or reset correctly 
Pendin
g 
TOP-01
7 
Select multiple topics, if 
supported 
Multiple selection behaves as 
documented 
Pendin
g 
23.3 Search and Result Testing 
Test ID 
Test Case 
Expected Result 
Status 
TOP-01
8 
Select topic with People filter 
Approved People behavior occurs 
Pendin
g 
TOP-01
9 
Select topic with Organizations 
filter 
Approved Organizations behavior 
occurs 
Pendin
g 

TOP-02
0 
Select topic and enter a 
keyword 
Combined behavior matches 
documentation 
Pendin
g 
TOP-02
1 
Check whether posts are filtered Behavior is recorded accurately 
Pendin
g 
TOP-02
2 
Check whether events are 
filtered 
Behavior is recorded accurately 
Pendin
g 
TOP-02
3 
Check whether jobs are filtered 
Behavior is recorded accurately 
Pendin
g 
TOP-02
4 
Test topic with Regular Search 
Relationship is documented 
Pendin
g 
TOP-02
5 
Test topic with AI Search 
Relationship is documented 
Pendin
g 
23.4 Error and Performance Testing 
Test ID 
Test Case 
Expected Result 
Status 
TOP-02
6 
Select topic during slow network 
Loading state is understandable 
Pendin
g 
TOP-02
7 
Disconnect network during selection 
Error or retry behavior is 
documented 
Pendin
g 

TOP-02
8 
Select topic with no results 
Approved empty state is 
displayed 
Pendin
g 
TOP-02
9 
Open Explore on mobile screen size 
Layout remains usable 
Pendin
g 
TOP-03
0 
Select topic repeatedly 
No duplicate or unexpected 
behavior 
Pendin
g 
TOP-03
1 
Refresh after topic selection 
State behavior is documented 
Pendin
g 
TOP-03
2 
Open topic-related results in a new 
session 
Access behavior is documented 
Pendin
g 
23.5 Privacy and Access Testing 
Test ID 
Test Case 
Expected Result 
Status 
TOP-03
3 
Test topic discovery with 
restricted profile 
Visibility rules are respected 
Pendin
g 
TOP-03
4 
Check blocked-user visibility 
Approved blocking rules are respected 
Pendin
g 
TOP-03
5 
Test topic-related organization 
visibility 
Organization permissions are 
respected 
Pendin
g 

TOP-03
6 
Check private content visibility 
Content access rules are respected 
Pendin
g 
TOP-03
7 
Verify topic activity tracking 
Behavior is documented according to 
privacy policy 
Pendin
g 
24. Known Limitations and Open Questions 
The following points remain unresolved and require confirmation. 
No. 
Open Question 
Responsible Team 
1 
What is the exact purpose of each topic? 
Product 
2 
Which content types are connected to Topics? 
Product / Engineering 
3 
Do Topics filter People? 
Engineering / QA 
4 
Do Topics filter Organizations? 
Engineering / QA 
5 
Do Topics filter posts or clips? 
Product / Engineering 
6 
Do Topics filter Events or Conversations? 
Product 
7 
Can users select multiple topics? 
Engineering / QA 
8 
Can users follow or save topics? 
Product 

9 
Are topics personalized? 
Product / Engineering 
10 
How are topic results ranked? 
Engineering 
11 
Can users create custom topics? 
Product 
12 
Are topics available on Android and iOS? 
Mobile Team 
13 
Are topics available to every subscription plan? 
Product 
14 
Does topic selection affect Regular Search? 
Engineering 
15 
Does topic selection affect AI Search? 
AI / Engineering 
16 
What happens when a topic has no results? 
Product / QA 
17 
Can a topic selection be shared through a URL? 
Engineering 
18 
Are topic selections saved in user history? 
Engineering / Privacy 
19 
What is the process for adding or removing 
topics? 
Product 
20 
What are the official topic definitions? 
Product 
25. Related Documentation 

Related Document 
Purpose 
WiseIN Application Overview 
Provides a high-level overview of WiseIN modules and 
navigation 
Explore Documentation 
Documents Explore search, People, Organizations, and 
discovery functionality 
Regular Search Documentation Describes keyword-based search and related behaviors 
AI Search Documentation 
Describes the proposed AI-powered search and retrieval 
functionality 
People Search Documentation 
Documents people discovery and profile results 
Organization Documentation 
Describes organization discovery and profiles 
Posts / Feed Documentation 
Documents content discovery and content visibility 
Events / Conversations 
Documentation 
Covers event and professional conversation discovery 
Privacy & Safety 
Documentation 
Defines visibility, privacy, and content access rules 
Mobile Application 
Documentation 
Covers Android and iOS behavior 

Customer Support 
Documentation 
Defines support channels and issue-handling procedures 
AI Customer Support 
Documentation 
Defines AI response rules and escalation processes 
26. Source and Verification Register 
Information 
Source 
Verification 
Status 
Topics are displayed in Explore 
WiseIN interface observation 
Observed 
Find by Topic section 
WiseIN interface observation 
Observed 
All Topics label 
WiseIN interface observation 
Observed 
Building Product label 
WiseIN interface observation 
Observed 
Business & Money label 
WiseIN interface observation 
Observed 
Career Advancement label 
WiseIN interface observation 
Observed 
Founder Advice label 
WiseIN interface observation 
Observed 
Fundraising 101 label 
WiseIN interface observation 
Observed 

Hiring & Team Building label 
WiseIN interface observation 
Observed 
Idea to Launch label 
WiseIN interface observation 
Observed 
Marketing & GTM label 
WiseIN interface observation 
Observed 
Topic filtering behavior 
Requires application testing 
Pending 
Topic-to-People relationship 
Requires application testing 
Pending 
Topic-to-Organization 
relationship 
Requires application testing 
Pending 
Topic-to-Post relationship 
Requires product confirmation 
Pending 
Topic-to-Event relationship 
Requires product confirmation 
Pending 
Multi-topic selection 
Requires application testing 
Pending 
Topic-following functionality 
Requires product confirmation 
Pending 
Topic personalization 
Requires Engineering confirmation 
Pending 
Mobile feature parity 
Requires Android and iOS testing 
Pending 

Topic ranking algorithm 
Requires Engineering confirmation 
Pending 
Privacy and visibility behavior 
Requires privacy and product 
confirmation 
Pending 
26.1 Source Validation Rules 
Before final approval: 
●​ All topic names must be checked against the current WiseIN interface. 
●​ The behavior of every topic must be tested. 
●​ Product and Engineering teams must confirm the topic data model and filtering logic. 
●​ Any unsupported assumptions must be removed or clearly marked. 
●​ Only verified information should be added to the authoritative AI/RAG knowledge base. 
●​ The document must be updated whenever topics are added, renamed, removed, or 
redesigned. 
27. AI/RAG Knowledge Base Requirements 
The Topics documentation should be prepared for retrieval by the WiseIN AI Customer Support 
System. 
27.1 Recommended Knowledge Units 
The following information should be stored as separate knowledge units where appropriate: 
1.​ Topics definition. 
2.​ Topics navigation path. 
3.​ Official topic list. 
4.​ Individual topic descriptions. 
5.​ Topic selection workflow. 
6.​ Supported filtering behavior. 
7.​ Supported content types. 
8.​ Topic-related errors. 
9.​ Topic troubleshooting. 
10.​Platform-specific differences. 
11.​Privacy and visibility rules. 
12.​Human escalation instructions. 
27.2 RAG Content Rules 

The knowledge base must distinguish between: 
●​ Confirmed: Verified through the application, approved documentation, or authorized 
team confirmation. 
●​ Observed: Seen in the interface but not fully verified as a permanent product behavior. 
●​ Pending: Requires Product, Engineering, QA, Security, or Support confirmation. 
●​ Proposed: Suggested implementation or documentation structure, not an existing 
feature. 
●​ Deprecated: Previously documented behavior that is no longer supported. 
27.3 Retrieval and Answering Guidance 
When a user asks about Topics, the AI should: 
1.​ Identify whether the user needs an explanation, navigation instruction, or 
troubleshooting. 
2.​ Retrieve the relevant approved topic documentation. 
3.​ Confirm the user's platform when platform-specific behavior matters. 
4.​ Provide only verified instructions. 
5.​ Avoid treating topic names as proof of a user's skills or qualifications. 
6.​ Escalate if the issue requires backend investigation or account-specific information. 
7.​ Use the latest approved documentation version. 
28. Completion Checklist 
Documentation Checklist 
●​ Document title and ID are added. 
●​ Purpose and scope are documented. 
●​ Topics definition is included. 
●​ Explore navigation is documented. 
●​ Observed topic names are recorded. 
●​ Topic interface elements are documented. 
●​ Topic selection workflow is tested. 
●​ Filtering behavior is verified. 
●​ People relationship is verified. 
●​ Organization relationship is verified. 
●​ Post and content relationship is verified. 
●​ All Topics behavior is confirmed. 
●​ Multi-topic selection is tested. 
●​ Loading states are documented. 
●​ Empty states are documented. 
●​ Error scenarios are tested. 
●​ Troubleshooting steps are approved. 

●​ Web behavior is verified. 
●​ Android behavior is tested. 
●​ iOS behavior is tested. 
●​ Privacy and visibility rules are confirmed. 
●​ AI response guidance is reviewed. 
●​ Human escalation procedure is approved. 
●​ Related documents are linked. 
●​ Source and verification register is completed. 
●​ Product team review is completed. 
●​ Engineering team review is completed. 
●​ QA review is completed. 
●​ Support team review is completed. 
●​ Final approval is received. 
●​ Approved content is added to the AI/RAG knowledge base. 
29. Version History 
Versio
n 
Date 
Changes 
Author 
Approval 
Status 
1.0 
17 
September 
2026 
Initial Topics documentation created 
based on available interface observations 
and product information 
MSR 
Draft — 
Pending 
Approval 
30. Final Documentation Status 
Status: Draft — Pending Product, Engineering, QA, Privacy, and Customer Support Verification 
This document provides a structured overview of the WiseIN Topics feature based on the 
currently available interface observations. The visible topic labels have been documented, but 
the exact filtering behavior, supported content types, ranking logic, topic personalization, and 
platform-specific functionality require additional validation. 
Before this document is used as an authoritative source for the WiseIN AI Customer Support 
System, all pending behaviors must be tested, confirmed by the relevant teams, and updated in 
the approved knowledge base. 
Final Approval Required From: 
●​ WiseIN Product Team 

●​ WiseIN Engineering Team 
●​ WiseIN QA Team 
●​ WiseIN Customer Support Team 
●​ WiseIN Privacy/Security Team, where applicable 
●​ Authorized WiseIN Management / Product Owner 
 



---

