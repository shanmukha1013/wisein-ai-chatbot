# Regular Search

## Source: WISEIN REGULAR SEARCH DOCUMENTATION015.pdf

DOCUMENT 015 — WISEIN REGULAR 
SEARCH DOCUMENTATION 
WISEIN-SRC-015 
Draft 
Pending Verification 
Document Title: WiseIN Regular Search Documentation 
Document ID: WISEIN-SRC-015 
Category: Search, Discovery & Navigation 
Version: 1.0 
Prepared By: MSR 
Date: 17 September 2026 
Document Classification: Internal Documentation / AI Customer Support Knowledge Base 
Status: Draft — Pending Product and Engineering Verification 
1. Purpose of This Document 
The purpose of this document is to describe the regular search functionality available in the 
WiseIN application. 
Regular Search allows users to search for relevant people, enterprises, or other supported 
information through the application's search interface. 
Based on the current observation, Regular Search and the search functionality inside the 
Explore module appear to provide a similar discovery experience. The primary observed 
difference is the location of the search entry point within the application interface. 
The exact relationship between both search interfaces must be confirmed through application 
testing and engineering documentation. 

2. Relationship Between Regular Search 
and Explore Search 
2.1 Initial Observation 
Regular Search and Explore Search appear to be related features. 
Both may support the discovery of: 
●​ People. 
●​ Professionals. 
●​ Enterprises. 
●​ Relevant topics or interests. 
●​ Search-based results. 
The difference currently observed is that the search access point is positioned differently in the 
application. 
2.2 Preliminary Comparison 
Feature 
Regular Search 
Explore Search 
Main purpose 
Search for relevant information 
or members 
Discover people, enterprises, and topics 
Search entry 
point 
Search button or search icon 
located elsewhere in the 
application 
Search field available within Explore 
People 
discovery 
Requires verification 
Observed and supported by the Explore 
interface 
Enterprise 
discovery 
Requires verification 
Observed through the Enterprises tab 

Topic 
discovery 
Requires verification 
Topic buttons visibly available 
Filters 
Requires verification 
Role, location, skills, verified status, and 
1:1 video availability are listed in the 
platform guide 
Search results Requires live testing 
People and enterprise results observed 
Functional 
difference 
Pending confirmation 
Pending confirmation 
Important: The table represents the current documentation status. It does not confirm that both 
search interfaces use the exact same backend API, search algorithm, ranking logic, or filter 
system. 
3. Regular Search Access Point 
The exact position of the Regular Search button should be documented after confirming it on 
the current WiseIN mobile and web applications. 
The following details should be recorded: 
●​ Location of the search icon. 
●​ Page or module where the search icon is visible. 
●​ Search icon appearance. 
●​ Placeholder text. 
●​ Whether the search field opens as a new page, overlay, or expandable field. 
●​ Whether search is available to logged-in users only. 
●​ Whether search is available before account verification. 
Current Verification Status 
Pending live verification: The provided Explore screenshot confirms a search field inside 
Explore, but it does not independently establish the complete Regular Search interface. 

4. Regular Search Workflow 
The following is a proposed test workflow and must be validated against the live application. 
1.​ Open the WiseIN application. 
2.​ Locate and select the regular search icon or search button. 
3.​ Confirm that the search interface opens. 
4.​ Enter a search term. 
5.​ Submit the search using the available search control or keyboard action. 
6.​ Wait for the search results to load. 
7.​ Review the displayed results. 
8.​ Select a relevant person, enterprise, or available result. 
9.​ Return to the search results page. 
10.​Confirm whether the search query and previous results are retained. 
5. Search Input 
The search input should be tested to determine which types of information are supported. 
5.1 Search Types to Test 
Search Type 
Example 
Verification Status 
Person name 
Rahul 
Pending testing 
Username 
@username 
Pending testing 
Professional 
role 
Software 
Engineer 
Listed in Explore guide as a search example 
Company name 
Sanshi 
Network 
Pending testing 

Skill 
Python 
Pending testing 
Topic 
Founder 
Advice 
Topic discovery observed in Explore 
Location 
Hyderabad 
Listed as an Explore filter; regular search behavior 
pending 
Partial keyword 
Soft 
Pending testing 
The Explore guide provides Senior Software Engineer as an example of a search query. 
WISEIN - COMPLETE PLATFORM USER GUIDE & OPERATIONAL DOCUMENTATION(1).pdf 
6. Search Results 
The search results page should be tested to identify the categories and information displayed. 
6.1 People Results 
Possible information to verify includes: 
●​ Profile image. 
●​ Name. 
●​ Username. 
●​ Professional title. 
●​ Organization. 
●​ Location. 
●​ Verification status. 
●​ Follow action. 
●​ Connect action. 
●​ View Profile action. 
●​ Meeting-related actions. 
These fields must be confirmed based on the actual search results and the user's permissions. 

6.2 Enterprise Results 
Possible information to verify includes: 
●​ Company logo. 
●​ Company name. 
●​ Industry. 
●​ Location. 
●​ Verification status. 
●​ Follow action. 
●​ Following status. 
●​ View action. 
The Enterprises tab in the supplied screenshot displays company cards with Follow, Following, 
and View actions. These observations relate to Explore and should be compared with Regular 
Search results during testing. 
7. Difference in Search Button Position 
7.1 Current Understanding 
The current understanding is: 
Regular Search and Explore Search may provide the same or closely related 
search functionality, while the search entry points are located in different parts of 
the WiseIN interface. 
7.2 What Must Be Confirmed 
The QA and Engineering teams should verify: 
1.​ Whether both interfaces call the same backend search service. 
2.​ Whether both interfaces return the same result categories. 
3.​ Whether the same search keywords are supported. 
4.​ Whether both interfaces display people and enterprises. 
5.​ Whether topic selection is available in Regular Search. 
6.​ Whether filters are available in Regular Search. 
7.​ Whether search results are ranked identically. 
8.​ Whether the search history is shared between both interfaces. 
9.​ Whether the same loading and error states are used. 
10.​Whether the same search permissions and restrictions apply. 

8. Search Filters 
The platform guide identifies the following filters for Explore member discovery: 
●​ Role. 
●​ Location. 
●​ Skills. 
●​ Verified Status. 
●​ Availability for 1:1 Video Calls. 
WISEIN - COMPLETE PLATFORM USER GUIDE & OPERATIONAL DOCUMENTATION(1).pdf 
It is not yet confirmed whether these filters are also available in Regular Search. 
8.1 Filter Verification Table 
Filter 
Available in Explore 
Available in Regular 
Search 
Role 
Listed in platform guide 
Pending verification 
Location 
Listed in platform guide 
Pending verification 
Skills 
Listed in platform guide 
Pending verification 
Verified Status 
Listed in platform guide 
Pending verification 
1:1 Video Call Availability 
Listed in platform guide 
Pending verification 
Topic Selection 
Observed in screenshot Pending verification 
9. Search Error Scenarios 

The following issues should be tested in Regular Search. 
Error Scenario 
Expected Behavior to Verify 
Empty search 
Application response must be 
recorded 
No matching results 
Appropriate empty-state message 
Search service failure 
Error message or retry option 
Slow search response 
Loading indicator 
Invalid input 
Validation behavior 
Network disconnection 
Error or retry behavior 
Repeated search 
Previous results and query handling 
Search result selection 
failure 
Appropriate error response 
Unauthorized access 
Authentication or permission response 
Search screen not loading 
Recovery and support guidance 
The exact error messages must be recorded from the live application and should not be 
invented in the AI knowledge base. 

10. AI Customer Support Guidance 
The WiseIN AI chatbot should explain Regular Search and Explore Search as related discovery 
features, while clearly communicating any uncertainty about their exact differences. 
10.1 Approved Response Example 
"WiseIN provides search and discovery functionality for finding relevant people and 
enterprises. The regular search option and the search option inside Explore may be 
related, but their exact functionality and available filters depend on the current 
application implementation. Please use the search option visible on your screen. If 
you experience an issue, share the general steps you followed without sharing 
passwords, OTPs, or sensitive personal information." 
10.2 AI Restrictions 
The chatbot must not: 
●​ Claim that Regular Search and Explore definitely use the same backend service without 
confirmation. 
●​ Invent search filters. 
●​ Claim that all users appear in search results. 
●​ Confirm a user's verification status without an authorized data source. 
●​ Claim that a search result is complete or exhaustive. 
●​ Request passwords, OTPs, or unnecessary identity information. 
●​ Claim that it performed a search unless the chatbot has an authorized search tool. 
●​ Promise that a particular person or enterprise will appear in search results. 
11. QA Test Plan 
11.1 Functional Testing 
●​ Open Regular Search. 
●​ Enter a valid search term. 
●​ Submit the search. 
●​ Verify that results are displayed. 
●​ Search for a person. 
●​ Search for an enterprise. 
●​ Search using a professional role. 
●​ Search using a partial keyword. 

●​ Open a search result. 
●​ Return to the search results. 
●​ Verify whether search history or the previous query is retained. 
11.2 UI Testing 
●​ Verify search icon placement. 
●​ Verify search field alignment. 
●​ Verify placeholder text. 
●​ Verify search field responsiveness. 
●​ Verify results card layout. 
●​ Verify Follow and View buttons. 
●​ Verify text truncation. 
●​ Verify mobile keyboard behavior. 
●​ Verify light and dark theme behavior, if supported. 
●​ Verify layout on different screen sizes. 
11.3 Performance Testing 
●​ Test search with a fast network. 
●​ Test search with a slow network. 
●​ Test search during temporary network loss. 
●​ Check the loading indicator. 
●​ Check whether repeated search requests are prevented. 
●​ Check whether results load within an acceptable time. 
●​ Check whether the application freezes during search. 
11.4 Security and Privacy Testing 
●​ Verify whether search respects profile visibility settings. 
●​ Verify whether blocked users appear in results. 
●​ Verify whether private information is hidden. 
●​ Verify whether restricted profiles are handled correctly. 
●​ Verify whether search results depend on account permissions. 
●​ Confirm that sensitive account information is not exposed. 
12. Source and Verification Register 
Information 
Source 
Status 

Explore search exists 
WiseIN platform guide 
Supported 
Explore search example 
WiseIN platform guide 
Supported 
Explore filters 
WiseIN platform guide 
Supported as documented 
Topic buttons 
Provided Explore 
screenshot 
Visually observed 
People and Enterprises tabs 
Provided Explore 
screenshots 
Visually observed 
Regular Search location 
User observation 
Requires screenshot/live 
verification 
Regular Search and Explore use the 
same backend 
Not confirmed 
Pending Engineering 
verification 
Regular Search and Explore have 
identical functionality 
Not confirmed 
Pending QA verification 
Search result ranking 
No confirmed source 
Pending verification 
Search history behavior 
No confirmed source 
Pending verification 
13. Current Status 
Document Status: Draft 

Current Finding: Regular Search and Explore Search appear to be related discovery 
functionalities with different search entry-point locations. 
Pending Confirmation: Whether both search interfaces use the same backend functionality, 
result categories, filters, ranking system, and permissions. 
Required Next Step: Test Regular Search and compare its behavior with the Explore search 
interface before marking this document as verified. 
 



---

