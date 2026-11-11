# Jobs

## Source: WISEIN JOBS MODULE DOCUMENTATION019.pdf

DOCUMENT 019 — WISEIN JOBS 
MODULE DOCUMENTATION 
WISEIN-JOB-019 
Draft — Pending Review 
Internal Documentation • AI/RAG Knowledge Base • Prepared by MSR 
1. Document Information 
Field 
Details 
Document Title 
WiseIN Jobs Module Documentation 
Document ID 
WISEIN-JOB-019 
Module 
Jobs 
Category 
Core Product Features 
Version 
1.0 
Prepared By 
MSR 
Date 
17 September 2026 
Status 
Draft — Pending Product, Engineering, QA, and Support-Team 
Approval 

Intended Usage 
Internal Documentation and AI/RAG Knowledge Base 
Primary Source 
WiseIN frontend source-code analysis 
Backend Verification 
Pending 
Live Application 
Testing 
Required 
Evidence Classification 
Information in this document should be classified using the following categories: 
●​ Confirmed in Frontend Code: Functionality identified through source-code analysis. 
●​ Observed in UI: Elements or behavior confirmed through interface observation. 
●​ Requires Backend Verification: Functionality inferred from API calls or frontend 
implementation but not verified on the server. 
●​ Requires Product or Security Confirmation: Features, policies, permissions, or security 
behavior that require approval from the relevant team. 
The frontend source code is not, by itself, sufficient to establish backend authorization, security 
guarantees, data retention policies, or final product policy. 
Pasted markdown.md 
2. Purpose of This Document 
The purpose of this document is to provide structured and accurate documentation of the 
WiseIN Jobs module. 
This document is intended to support: 
1.​ WiseIN Users — Help users understand job discovery, filtering, saving, and application 
workflows. 
2.​ AI Customer Support — Provide reliable answers to user questions about the Jobs 
module. 
3.​ Customer Support Team — Assist with troubleshooting and issue resolution. 

4.​ QA Team — Define test scenarios for functional and regression testing. 
5.​ Engineering Team — Document frontend implementation and identify backend 
verification requirements. 
6.​ Product Team — Understand the current user experience and identify improvements. 
7.​ AI/RAG Knowledge Base — Provide structured, verified information for chatbot retrieval 
and response generation. 
The document should be updated whenever the Jobs module changes or when previously 
pending behavior is confirmed by the relevant team. 
3. Jobs Module Overview 
3.1 What Is the WiseIN Jobs Module? 
The Jobs module is a career discovery and application feature within WiseIN. It allows 
authenticated users to explore available job opportunities, search and filter listings, save jobs for 
later, review job details, and submit applications through the platform. 
The frontend implementation includes job discovery, recommended jobs, saved jobs, applied 
jobs, job details, company information, application forms, and application-status indicators. 
3.2 Primary Purpose 
The Jobs module is designed to support the following activities: 
●​ Discovering job opportunities. 
●​ Searching for jobs by role. 
●​ Filtering jobs according to relevant criteria. 
●​ Viewing job and company information. 
●​ Saving jobs for future reference. 
●​ Applying directly through WiseIN. 
●​ Reviewing application-related status information. 
●​ Discovering similar job opportunities. 
Verification status: Core candidate-side functionality is identified in the frontend implementation. 
Backend workflows and employer-side functionality require additional verification. 
Pasted markdown.md 
4. Scope of the Document 

This document covers: 
●​ Accessing the Jobs module. 
●​ Jobs listing and discovery. 
●​ Jobs tabs. 
●​ Search functionality. 
●​ Filters. 
●​ Job cards. 
●​ Job details. 
●​ Company information. 
●​ Saving and unsaving jobs. 
●​ Application form. 
●​ Application submission. 
●​ Application status. 
●​ Similar jobs. 
●​ Loading and empty states. 
●​ Error scenarios. 
●​ Troubleshooting. 
●​ User roles and permissions. 
●​ Privacy and security considerations. 
●​ Responsive and mobile behavior. 
●​ QA test cases. 
●​ AI customer-support guidance. 
●​ Human support escalation. 
●​ Open questions and pending verification. 
Out of Scope 
The following areas are not confirmed as fully implemented through the available frontend 
analysis: 
●​ Complete employer job-posting workflow. 
●​ Employer job-management dashboard. 
●​ Candidate-management workflow for employers. 
●​ Backend authorization rules. 
●​ Backend HTML sanitization implementation. 
●​ Final resume-upload policy. 
●​ Application data-retention policy. 
●​ Final notification behavior. 
●​ Official job-ranking or recommendation algorithm. 
5. Accessing the Jobs Module 

5.1 Navigation 
Users can access the Jobs module through the main WiseIN navigation. 
Item 
Details 
Main Jobs Route 
/jobs 
Job Details Route 
/jobs/[id] 
Company Jobs 
Route 
/company/[id]/jobs 
Authentication 
Authentication is required for user-specific functionality 
Main Functionality 
Browse, filter, save, and apply for jobs 
The frontend uses the authentication provider to access profile information, pre-fill application 
fields, and manage user-specific saved and applied states. 
5.2 Authentication Requirement 
The Jobs module relies on authenticated user information for features such as: 
●​ Pre-filled application details. 
●​ Saved job information. 
●​ Applied job information. 
●​ Application status. 
●​ Ownership checks. 
●​ User-specific recommended jobs. 
The exact authorization behavior for every route and API endpoint must be verified against the 
backend implementation. 

6. Jobs Module User Interface 
The Jobs interface is divided into the following main areas: 
1.​ Main job-discovery feed. 
2.​ Search bar. 
3.​ Job-category tabs. 
4.​ Filter panel. 
5.​ Job cards. 
6.​ Job details page. 
7.​ Similar jobs section. 
8.​ Application form. 
6.1 Main Job Tabs 
The frontend provides the following primary tabs: 
Tab 
Description 
Verification 
All Jobs 
Displays available job 
listings 
Confirmed in frontend 
Recommende
d 
Displays jobs 
recommended for the user 
Endpoint and UI identified; recommendation 
logic requires verification 
Saved 
Displays jobs saved by the 
user 
Confirmed in frontend 
Applied 
Displays jobs the user has 
applied for 
Confirmed in frontend 
The exact sorting, ranking, pagination, and recommendation logic must be confirmed by the 
Engineering and Product teams. 
6.2 Search Bar 

The Jobs page includes an inline search bar for searching by role. 
Observed or Implemented Behavior 
●​ The search field is focused on role-based searching. 
●​ The user can enter a role or job title. 
●​ Pressing Enter triggers the search request. 
●​ The search query is passed to the Jobs API. 
●​ Search results depend on the API response and applied filters. 
Example Search Queries 
●​ Python Developer 
●​ Data Analyst 
●​ Software Engineer 
●​ Machine Learning Engineer 
●​ Frontend Developer 
●​ Backend Developer 
The available search syntax, partial matching, case sensitivity, and result-ranking rules require 
confirmation. 
7. Job Filters 
The Jobs module provides a filter panel for narrowing job results. 
7.1 Available Filters 
Filter 
Frontend Details 
Roles 
Supports up to three role entries 
Job Type 
Filters by employment type 
Skills 
Supports up to five skills 

Experience 
Filters according to experience 
range 
Location 
Filters based on location 
Remote Only Checkbox/toggle for remote roles 
Clear 
Resets the selected filters 
Search 
Applies selected filters 
The frontend passes filter information through query parameters such as role, jobType, 
skills, experience, location, and remote. 
Pasted markdown.md 
7.2 Filter Workflow 
1.​ Open the Jobs module. 
2.​ Locate the filter panel. 
3.​ Enter or select the required role. 
4.​ Select the job type, if required. 
5.​ Add relevant skills. 
6.​ Select an experience range. 
7.​ Enter or select a location. 
8.​ Enable Remote Only, if applicable. 
9.​ Click Search. 
10.​Review the filtered results. 
7.3 Clearing Filters 
The Clear button is intended to reset active filter selections. 
The following behavior should be verified during QA: 
●​ All fields are reset. 

●​ The remote toggle is disabled. 
●​ Previous search parameters are removed. 
●​ The job list refreshes. 
●​ The UI correctly reflects the cleared state. 
8. Job Cards 
Each job listing is displayed through a job card. 
8.1 Job Card Information 
The job card may display: 
●​ Company logo. 
●​ Company initial or placeholder logo. 
●​ Job title. 
●​ Location. 
●​ Employment type. 
●​ Skill tags. 
●​ Number of additional skills. 
●​ Posting recency. 
●​ Bookmark/save icon. 
●​ Application-status badge, when applicable. 
The frontend displays up to four skill tags and may show a +X indicator for additional skills. 
8.2 Employment Information 
The card may show employment types such as: 
●​ Full-Time. 
●​ Internship. 
●​ Other types supported by the job data. 
The complete list of employment types and their official definitions should be confirmed with the 
Product team. 
8.3 Posting Recency 
Job cards may display posting recency, for example: 
●​ 5 days ago. 

●​ 10 days ago. 
●​ Other relative date formats. 
The frontend also contains logic that filters out jobs older than 30 days from the active listing 
view. This should be treated as a frontend implementation behavior rather than an established 
employer-side retention or expiration policy. 
Pasted markdown.md 
9. Thirty-Day Job Visibility Behavior 
9.1 Frontend Behavior 
The source-code analysis identifies a frontend function that filters jobs based on their 
createdAt or updatedAt timestamps. 
Jobs older than 30 days may be removed from the active displayed list by the frontend. 
9.2 Important Clarification 
The 30-day behavior should not automatically be interpreted as: 
●​ Permanent deletion of the job. 
●​ Guaranteed backend expiration. 
●​ Confirmation that the employer has closed the job. 
●​ Confirmation that the job can never be accessed again. 
●​ Confirmation that applications are no longer accepted through other routes. 
The frontend visibility rule and backend job-status rules must be checked separately. 
9.3 AI Support Guidance 
When a user cannot find a previously viewed job, the AI may explain: 
“The job may no longer appear in the active Jobs feed because of its current status 
or the frontend’s job-visibility filtering. Please check your Saved or Applied section if 
you previously interacted with the job. If the issue continues, I can help you raise it 
with WiseIN Support.” 
The AI should not definitively claim that a job has been deleted or closed without an authorized 
live data source. 

10. Job Details Page 
The job details page is accessed through the route: 
/jobs/[id] 
10.1 Job Information 
The details page may display: 
●​ Job title. 
●​ Closed status, where applicable. 
●​ Company logo. 
●​ Job location. 
●​ Employment type. 
●​ Posting date or relative posting time. 
●​ Required or must-have skills. 
●​ Job description. 
●​ Company details. 
●​ Company website. 
●​ Company location. 
●​ Company founding year. 
●​ Company description. 
10.2 Job Description 
The frontend renders job-description content as HTML. 
Security Consideration 
Because the frontend uses HTML rendering, the Engineering and Security teams must confirm 
that the backend properly sanitizes user-generated or externally supplied HTML before it is 
stored or rendered. 
Potential risks to review include: 
●​ Cross-site scripting. 
●​ Malicious links. 
●​ Unsafe HTML elements. 
●​ Script injection. 
●​ Unsafe attributes. 
●​ Content submitted by unauthorized users. 

This is a security review requirement, not confirmation that a vulnerability has been exploited. 
10.3 Similar Jobs 
The job details page includes a section for similar jobs. 
The available frontend analysis indicates that the page can display up to five similar jobs. 
The following aspects require verification: 
●​ How similarity is calculated. 
●​ Whether similarity is based on role, skill, location, or job type. 
●​ Whether closed jobs are included. 
●​ Whether the list is personalized. 
●​ Whether similar jobs are available on mobile. 
11. Applying for a Job 
11.1 Application Overview 
WiseIN provides a platform-based application workflow through which candidates can submit 
information and answers for a job listing. 
The application process includes profile-derived information, employment-related details, 
employer-defined screening questions, and a cover letter. 
11.2 Conditions That May Hide the Apply Button 
The Apply now button is hidden when one of the following conditions is identified in the frontend: 
1.​ The user has already applied for the job. 
2.​ The job is closed or inactive. 
3.​ The authenticated user owns the company or job posting. 
The exact backend eligibility checks must be verified independently. 
12. Application Form 
12.1 Pre-Filled Fields 

The application form pre-fills the following information from the authenticated user’s profile: 
●​ First Name. 
●​ Last Name. 
●​ Email. 
●​ Mobile Number. 
These fields are displayed as read-only in the frontend application form. 
12.2 Required Application Fields 
The form includes the following information: 
Field 
Description 
First Name 
Retrieved from the user profile 
Last Name 
Retrieved from the user profile 
Email 
Retrieved from the user profile 
Mobile 
Retrieved from the user profile 
Work Experience 
Candidate selects or provides experience information 
Notice Period 
Candidate provides notice-period information 
Holding Offer 
Candidate indicates whether they currently hold another 
offer 
In-Office Availability 
Candidate indicates whether they can work in-office 

Screening Questions 
Employer-defined questions, when available 
Cover Letter 
Text-based cover letter 
The frontend analysis indicates that the application form contains a text cover letter and does 
not contain a resume file-upload component in the reviewed implementation. Whether resume 
upload is planned or supported through another workflow requires Product confirmation. 
Pasted markdown.md 
13. Application Submission Workflow 
13.1 Step-by-Step Process 
1.​ Open the WiseIN Jobs module. 
2.​ Select a job from the listing. 
3.​ Open the job details page. 
4.​ Review the job description, skills, and company information. 
5.​ Click Apply now. 
6.​ Review the pre-filled personal information. 
7.​ Complete Work Experience. 
8.​ Complete Notice Period. 
9.​ Select the Holding Offer response. 
10.​Provide in-office availability. 
11.​Answer any custom screening questions. 
12.​Enter a cover letter. 
13.​Review the information. 
14.​Click Submit Application. 
15.​Wait for the submission response. 
16.​Review the success message or error. 
17.​Confirm whether the application status changes to APPLIED. 
13.2 Frontend Validation 
The frontend validates certain fields before submission, including: 
●​ Name. 
●​ Email format. 

●​ Work Experience. 
●​ Notice Period. 
The frontend may display validation messages such as: 
●​ Required 
●​ Invalid email 
The complete validation rules and backend validation requirements must be confirmed. 
13.3 Application Success Behavior 
The source analysis identifies the following expected frontend behavior after successful 
submission: 
●​ A success toast appears. 
●​ The application form closes. 
●​ The Apply now button is replaced by an APPLIED status indicator. 
The success message identified in the source is: 
Job applied successfully 
This message should be confirmed through live testing before being used as a guaranteed 
customer-support statement. 
14. Application Status 
14.1 Status Indicators 
The frontend displays application-status badges on job cards. 
The statuses identified in the implementation include: 
Status 
UI Indication 
APPLIED 
Blue badge 

REJECTED 
Red badge 
SHORTLIST
ED 
Green badge 
14.2 AI Support Restrictions 
The AI chatbot must not: 
●​ Guess a user’s application status. 
●​ Manually confirm that a user has been shortlisted. 
●​ Claim that an employer has rejected an application without authorized data. 
●​ Modify application status. 
●​ Promise an interview or response. 
●​ Claim that an employer has reviewed an application. 
Users should be directed to the Applied tab to review the status displayed by the application. 
If the displayed status appears incorrect, the issue should be escalated to WiseIN Support. 
15. Saving and Unsaving Jobs 
15.1 Save Job Feature 
Candidates can save jobs for later review using the bookmark icon on a job card. 
15.2 Save Workflow 
1.​ Open the Jobs module. 
2.​ Locate a job card. 
3.​ Click the bookmark icon. 
4.​ Wait for the save request to complete. 
5.​ Confirm the bookmark state. 
6.​ Open the Saved tab. 
7.​ Check whether the job appears in the saved list. 

15.3 Unsave Workflow 
1.​ Open a previously saved job. 
2.​ Click the filled bookmark icon. 
3.​ Wait for the removal request to complete. 
4.​ Confirm the bookmark state changes. 
5.​ Check whether the job is removed from the Saved tab. 
15.4 Frontend-Referenced API Operations 
Operation 
Method 
Endpoint 
Save job 
POST 
/jobs/{id}/s
ave 
Unsave 
job 
DELETE 
/jobs/{id}/s
ave 
The API paths are based on frontend request definitions. Backend authorization, response 
structure, and persistence behavior require verification. 
Pasted markdown.md 
16. API and Backend Reference 
Important: The following endpoints were identified through frontend API definitions. 
They should not be treated as complete or authoritative backend API 
documentation until confirmed by Engineering. 
Endpoint 
Method 
Purpose 
/jobs 
GET 
Fetches job listings 

/jobs/recomme
nded 
GET 
Fetches recommended jobs 
/jobs/saved 
GET 
Fetches saved jobs 
/jobs/me/appl
ied 
GET 
Fetches jobs applied for by the user 
/jobs/{id} 
GET 
Fetches job details and company 
information 
/jobs/{id}/sa
ve 
POST 
Saves a job 
/jobs/{id}/sa
ve 
DELETE 
Removes a saved job 
/jobs/{id}/ap
ply 
POST 
Submits a job application 
16.1 Referenced Query Parameters 
The Jobs listing request may use the following parameters: 
role 
jobType 
skills 
experience 
location 
remote 

16.2 Application Payload 
The frontend analysis identifies application data such as: 
firstName 
lastName 
email 
mobile 
workExperience 
noticePeriod 
holdingOffer 
canJoinInOffice 
coverLetter 
answers 
The answers field may contain question identifiers and candidate responses. 
The exact API schema, authentication requirements, validation rules, rate limits, and error 
responses must be confirmed by the Backend Engineering team. 
17. User Roles and Permissions 
17.1 Candidate 
An authenticated candidate may be able to: 
●​ Browse jobs. 
●​ Search for jobs. 
●​ Apply filters. 
●​ View job details. 
●​ Save jobs. 
●​ Apply for jobs. 
●​ View application-related information. 
The exact eligibility requirements must be confirmed against backend authorization rules. 
17.2 Employer or Job Owner 
The frontend checks whether the authenticated user is associated with the company that owns 
a job posting. 
When the user is identified as the owner, the Apply now button is hidden. 

The employer-side job-posting and job-management workflow is not fully established by the 
reviewed frontend implementation. 
17.3 Closed Jobs 
The frontend identifies inactive jobs and may display a Closed badge. 
The following points require backend verification: 
●​ Whether closed jobs remain visible in Saved. 
●​ Whether closed jobs remain visible in Applied. 
●​ Whether closed jobs can be reopened. 
●​ Whether an application can be submitted through a direct URL. 
●​ Whether the closure is permanent or temporary. 
18. Loading, Empty, and Error States 
18.1 Loading State 
The frontend includes loading skeleton components, including: 
●​ JobCardSkeleton 
●​ JobDetailSkeleton 
These components display placeholder layouts while requests are processing. 
18.2 Empty State 
When a job-list request returns no results, the frontend displays: 
No jobs found. 
This message should be distinguished from an API failure. A blank result may indicate that no 
jobs match the current search or filters. 
18.3 Job Details Error 
When the job-details request fails, the frontend displays an error message similar to: 
Failed to load job details. Please try again. 

18.4 Application Validation Errors 
Validation errors may be displayed beneath the relevant fields, including: 
Required 
Invalid email 
Exact error messages should be verified through live testing and should not be expanded with 
invented error codes. 
19. Troubleshooting Guide 
19.1 User Cannot Find a Previously Viewed Job 
Possible Causes 
●​ The job is no longer active. 
●​ The job is outside the frontend’s 30-day visibility filtering period. 
●​ Search criteria are too restrictive. 
●​ Filters remain active. 
●​ The user is viewing a different tab. 
●​ The job listing has changed. 
●​ An API or loading error occurred. 
Recommended Steps 
1.​ Open the All Jobs tab. 
2.​ Clear all active filters. 
3.​ Search using the job title or role. 
4.​ Check the Saved tab if the job was bookmarked. 
5.​ Check the Applied tab if the user applied. 
6.​ Try refreshing the page. 
7.​ If the issue continues, escalate with the job URL or job ID, if available. 
The AI must not automatically claim that the employer deleted the job. 
19.2 Apply Now Button Is Missing 
Possible Causes 
●​ The user has already applied. 

●​ The job is closed. 
●​ The user owns the job or company. 
●​ The user is not authenticated. 
●​ The job is no longer eligible for applications. 
●​ A frontend or backend error occurred. 
Recommended Steps 
1.​ Check for the APPLIED badge. 
2.​ Check whether a Closed badge is displayed. 
3.​ Confirm that the user is logged in. 
4.​ Verify whether the job belongs to the user’s company. 
5.​ Refresh the job-details page. 
6.​ Escalate if the button is missing despite meeting the expected conditions. 
19.3 Application Form Cannot Be Submitted 
Possible Causes 
●​ Required fields are incomplete. 
●​ Email format is invalid. 
●​ Work Experience is not selected. 
●​ Notice Period is missing. 
●​ Screening questions are incomplete. 
●​ Network request failed. 
●​ The job became inactive. 
●​ Backend validation rejected the request. 
Recommended Steps 
1.​ Review the entire application form. 
2.​ Look for red validation messages. 
3.​ Complete Work Experience. 
4.​ Complete Notice Period. 
5.​ Check the email format. 
6.​ Answer all required screening questions. 
7.​ Check the internet connection. 
8.​ Try submitting again once. 
9.​ Escalate if the issue continues. 
The AI should not instruct users to bypass required fields or modify request payloads. 
19.4 Incorrect Pre-Filled Personal Information 

Possible Cause 
The application form retrieves personal information from the authenticated user profile. 
Recommended Steps 
1.​ Ask the user to review their main WiseIN profile. 
2.​ Direct them to the relevant profile or account settings. 
3.​ Ask them to update incorrect information through the supported profile workflow. 
4.​ If the information remains incorrect or cannot be edited, escalate to Human Support. 
The AI must not request passwords, OTPs, or unnecessary personal identity documents. 
19.5 Malicious or Broken Content in a Job Description 
Possible Causes 
●​ Unsafe HTML content. 
●​ Malicious links. 
●​ Incorrectly sanitized content. 
●​ Broken formatting. 
●​ Invalid content submitted by a job owner. 
Recommended Steps 
1.​ Do not click suspicious links. 
2.​ Record the job URL or job ID. 
3.​ Capture a screenshot if safe and permitted. 
4.​ Report the issue to WiseIN Support. 
5.​ Escalate the case to the Security or Engineering team when appropriate. 
20. Privacy and Security Considerations 
20.1 Personal Information 
The application form uses profile-derived information such as: 
●​ Name. 
●​ Email. 
●​ Mobile number. 
This information should be handled according to WiseIN’s privacy and security requirements. 

The frontend’s read-only fields prevent ordinary editing through the visible form, but read-only UI 
fields alone do not guarantee backend integrity or authorization. 
20.2 Backend Validation 
The backend should independently validate: 
●​ Authenticated user identity. 
●​ Application ownership. 
●​ Job status. 
●​ Required fields. 
●​ Email and phone information. 
●​ Screening-question data. 
●​ Duplicate applications. 
●​ Authorization to submit an application. 
These controls require confirmation from Backend Engineering. 
20.3 HTML Rendering 
The frontend uses HTML rendering for job and company descriptions. 
The Security team should confirm: 
●​ HTML sanitization. 
●​ Script prevention. 
●​ Link safety. 
●​ Allowed HTML tags. 
●​ Content moderation. 
●​ Storage-level validation. 
●​ Output encoding. 
20.4 Data Exposure 
The AI chatbot must not expose: 
●​ Another candidate’s application information. 
●​ Employer-private data. 
●​ Internal API responses. 
●​ Hidden application fields. 
●​ Personal information without authorization. 
●​ Internal debugging information. 
●​ Authentication tokens or request headers. 

21. Platform and Responsive Behavior 
21.1 Desktop Web 
The desktop layout includes: 
●​ Main job feed. 
●​ Filter sidebar. 
●​ Job details section. 
●​ Similar jobs section. 
The reviewed frontend analysis identifies a fixed-width filter area of approximately 320 pixels in 
the desktop layout. 
21.2 Mobile Web 
The frontend uses responsive layout rules in which the advanced filter panel and the right-side 
Similar Jobs section are hidden at smaller breakpoints. 
Observed Limitation 
The advanced filter sidebar may not be available on mobile web in the reviewed 
implementation. Users may still have access to the inline role search bar. 
This behavior should be confirmed through live testing on different screen sizes and devices. 
21.3 Platform Verification Questions 
●​ Is the filter panel intentionally hidden on mobile? 
●​ Is there a mobile replacement for advanced filters? 
●​ Are all job details available on mobile? 
●​ Can users apply for jobs through mobile web? 
●​ Are saved and applied tabs fully responsive? 
●​ Is a native mobile application available? 
●​ Do mobile and desktop use the same backend behavior? 
22. Employer-Side Jobs Functionality 
22.1 Current Frontend Finding 

The reviewed source analysis identifies the company Jobs component: 
src/components/company/jobs/JobsPage.tsx 
The available analysis describes this area as containing static or placeholder job-management 
UI. 
22.2 Pending Verification 
The following employer-side functionality must be confirmed: 
●​ Creating a job. 
●​ Editing a job. 
●​ Closing a job. 
●​ Reopening a job. 
●​ Deleting a job. 
●​ Viewing applicants. 
●​ Shortlisting candidates. 
●​ Rejecting candidates. 
●​ Managing screening questions. 
●​ Managing company job listings. 
●​ Employer permissions. 
●​ Admin portal integration. 
The placeholder UI should not be documented as an active, fully operational employer feature 
until Product and Engineering confirm its status. 
23. Human Support Escalation 
The AI chatbot should escalate a Jobs-related issue when: 
1.​ The user cannot submit an application despite completing all required fields. 
2.​ The application status appears incorrect. 
3.​ Profile information is incorrect and cannot be updated. 
4.​ A job description contains suspicious or malicious content. 
5.​ The user reports unauthorized access to application information. 
6.​ A saved job disappears unexpectedly. 
7.​ The user reports an unexplained job-visibility issue. 
8.​ An employer cannot create or manage job listings. 
9.​ A backend error continues after basic troubleshooting. 
10.​The issue requires account-specific data that the AI cannot access. 
11.​The user reports a potential security or privacy issue. 

23.1 Information to Include in an Escalation 
The support ticket should include, where available: 
●​ User’s name. 
●​ Registered email address through an authorized support workflow. 
●​ Job title. 
●​ Job ID or job URL. 
●​ Date and approximate time of the issue. 
●​ Steps performed by the user. 
●​ Error message shown. 
●​ Screenshot, where appropriate. 
●​ Whether the issue occurs on desktop or mobile. 
●​ Whether the issue is reproducible. 
●​ Relevant request or correlation ID, if provided through approved diagnostic tools. 
The AI must not request passwords, OTPs, authentication tokens, or unnecessary identity 
documents. 
24. AI Customer-Support Guidance 
24.1 What the AI Can Explain 
The AI chatbot may explain: 
●​ How to open the Jobs module. 
●​ How to search for roles. 
●​ How to use available filters. 
●​ How to open job details. 
●​ How to save and unsave jobs. 
●​ How to apply for a job. 
●​ Which fields appear in the application form. 
●​ How to review the Applied tab. 
●​ Possible reasons the Apply now button is unavailable. 
●​ Basic troubleshooting steps. 
●​ How to contact Human Support. 
24.2 What the AI Must Not Assume 
The AI must not: 
●​ Invent job listings. 

●​ Claim a job is available without a live authorized source. 
●​ Confirm that an employer has reviewed an application. 
●​ Predict whether a candidate will be selected. 
●​ Guarantee an interview or job offer. 
●​ Change application status. 
●​ Claim that a job was permanently deleted without verified information. 
●​ Provide unsupported resume-upload instructions. 
●​ Claim that all mobile features are available. 
●​ Reveal private employer or candidate data. 
●​ Ask for passwords or OTPs. 
●​ Claim to have submitted an application unless an authorized action actually confirms it. 
●​ Claim to have contacted an employer or support representative unless the action was 
completed and confirmed. 
24.3 Source-of-Truth Hierarchy 
For Jobs-related responses, the AI should follow this hierarchy: 
1.​ Authorized live account or application data — For user-specific application status or 
account information. 
2.​ Approved WiseIN documentation — For supported workflows and product explanations. 
3.​ Approved backend/API responses — For current job data and authorized operations. 
4.​ Human Support — When the information is unavailable, sensitive, contradictory, or 
unresolved. 
The AI should clearly communicate uncertainty instead of creating an answer from assumptions. 
25. Sample AI Support Responses 
25.1 “Why Can’t I See the Apply Now Button?” 
“The Apply now button may not be visible if you have already applied for the job, if 
the job is closed, or if you are viewing a job posted by your own company. Please 
check whether an APPLIED badge or Closed badge is displayed. If neither applies, 
try refreshing the page and contact WiseIN Support if the issue continues.” 
25.2 “How Do I Apply for a Job?” 
“Open the Jobs section and select the job you are interested in. Review the job 
details, then select Apply now if it is available. Complete the required information, 
including Work Experience, Notice Period, in-office availability, screening questions 

if provided, and your Cover Letter. Review your details and select Submit 
Application.” 
25.3 “Where Can I Check My Application?” 
“Open the Jobs section and select the Applied tab. This section is intended to show 
jobs you have applied for and the application-status information available on the 
platform.” 
25.4 “I Cannot Find a Job I Previously Viewed.” 
“Try opening the All Jobs tab, clearing your filters, and searching for the role again. 
If you saved or applied for the job, also check the Saved or Applied tab. If you still 
cannot find it, share the job title or URL with WiseIN Support so the issue can be 
investigated.” 
25.5 “My Application Information Is Incorrect.” 
“The application form uses information from your WiseIN profile. Please review and 
update your profile information through the supported profile settings. If the 
information is still incorrect or cannot be changed, I recommend escalating the 
issue to WiseIN Support.” 
26. QA Test Cases 
The following test cases are based on frontend findings and require execution in the appropriate 
test environment. 
Test 
ID 
Test Scenario 
Preconditions 
Expected Result 
Status 
JOB-
001 
30-Day 
Visibility 
Jobs exist with 
different dates 
Jobs outside the frontend visibility 
period are handled according to 
the implemented rule 
Not 
Tested 

JOB-
002 
Save Job 
User is logged in 
Bookmark changes and job 
appears in Saved 
Not 
Tested 
JOB-
003 
Unsave Job 
Job is already 
saved 
Bookmark changes and job is 
removed from Saved 
Not 
Tested 
JOB-
004 
Apply 
Validation 
User opens 
application form 
Missing required fields show 
validation messages 
Not 
Tested 
JOB-
005 
Invalid Email 
Application form is 
open 
Invalid email format is rejected 
Not 
Tested 
JOB-
006 
Successful 
Application 
Valid application 
data 
Success response is shown and 
status changes appropriately 
Not 
Tested 
JOB-
007 
Own Job 
User owns the job’s 
company 
Apply now button is not displayed 
Not 
Tested 
JOB-
008 
Closed Job 
Job is inactive 
Closed indicator is displayed and 
application access is handled 
correctly 
Not 
Tested 
JOB-
009 
Applied Job 
User has already 
applied 
Applied status is displayed and 
duplicate application behavior is 
handled 
Not 
Tested 
JOB-
010 
Empty Search 
Search returns no 
results 
No jobs found message is 
displayed 
Not 
Tested 

JOB-
011 
Detail Error 
Job-details request 
fails 
Appropriate error message is 
displayed 
Not 
Tested 
JOB-
012 
Filter Reset 
Filters are active 
Clear button resets the filter state 
Not 
Tested 
JOB-
013 
Mobile Layout 
User accesses Jobs 
on a small screen 
Responsive layout behaves as 
designed 
Not 
Tested 
JOB-
014 
HTML Safety 
Job description 
contains HTML 
Unsafe content is sanitized or 
safely handled 
Not 
Tested 
JOB-
015 
Unauthorized 
Access 
User is not 
authenticated 
Access is handled according to 
approved authorization rules 
Not 
Tested 
27. Security and Negative Test Cases 
The QA and Security teams should also test the following scenarios: 
●​ Attempting to submit an application without authentication. 
●​ Submitting an application for a closed job. 
●​ Submitting an application multiple times. 
●​ Modifying read-only profile information in the browser. 
●​ Sending another user’s profile ID in an application request. 
●​ Submitting invalid screening-question identifiers. 
●​ Injecting HTML or script content into a cover letter. 
●​ Opening a job that the user is not authorized to access. 
●​ Accessing another user’s Saved or Applied data. 
●​ Modifying application status through unauthorized requests. 
●​ Sending malformed or unexpected API payloads. 
●​ Replaying application requests. 
●​ Submitting requests after the session expires. 
These tests must be conducted only in authorized testing environments. 

28. Known Limitations 
28.1 Confirmed or Frontend-Identified Limitations 
●​ The advanced filter panel is hidden at smaller responsive breakpoints in the reviewed 
implementation. 
●​ The application form does not include a resume file-upload component in the reviewed 
frontend. 
●​ The application form uses profile-derived information for selected personal fields. 
●​ The frontend applies a 30-day visibility filtering rule to job listings. 
28.2 Pending Verification 
●​ Backend job-expiration behavior. 
●​ Employer-side job creation and management. 
●​ Candidate-management functionality for employers. 
●​ Backend HTML sanitization. 
●​ Resume upload support or future implementation. 
●​ Complete mobile filter experience. 
●​ Recommendation algorithm. 
●​ Application-status update process. 
●​ Notification behavior. 
●​ Backend authorization and access-control rules. 
29. Related Documentation 
The following documents may be linked to the Jobs module: 
Document 
Relationship 
WiseIN Application Overview 
Provides overall WiseIN platform context 
Authentication Documentation 
Explains login and user authentication 

User Profile Documentation 
Explains the source of pre-filled profile data 
Company Profile Documentation 
Explains company information displayed in job listings 
Privacy and Security 
Documentation 
Provides relevant privacy and security guidance 
Customer Support Documentation 
Defines escalation and support workflows 
Notifications Documentation 
Explains any job or application-related notifications 
AI Chatbot Documentation 
Defines chatbot behavior, RAG, and escalation 
30. Source and Verification Register 
Information 
Source 
Evidence Type 
Status 
Jobs main 
route 
src/app/(ui)/jobs/page.tsx 
Frontend route 
Confirmed in 
source 
Job details 
route 
src/app/(ui)/jobs/[id]/page.tsx 
Frontend route 
Confirmed in 
source 
Company 
Jobs 
component 
src/components/company/jobs/Job
sPage.tsx 
Frontend 
component 
Confirmed in 
source 

Jobs API 
references 
Frontend Axios definitions 
API reference 
Backend 
verification 
pending 
Job tabs 
Jobs page implementation 
UI/code 
Confirmed in 
source 
Search by 
role 
Jobs page implementation 
UI/code 
Confirmed in 
source 
Filter fields 
Jobs page implementation 
UI/code 
Confirmed in 
source 
Application 
fields 
Job details/application component 
UI/code 
Confirmed in 
source 
Application 
statuses 
Jobs page implementation 
UI/code 
Confirmed in 
source 
30-day 
visibility rule 
Frontend filtering logic 
Business-logic 
implementation 
Requires 
Product 
confirmation 
HTML 
rendering 
Job details component 
Frontend 
implementation 
Security 
review 
required 
Employer-sid
e job 
management 
Company Jobs component 
Frontend UI 
Pending 
verification 

Resume 
upload 
Application component 
Frontend 
inspection 
Not identified 
in reviewed 
component; 
Product 
confirmation 
required 
Mobile filters 
Responsive frontend classes 
Frontend 
implementation 
Live testing 
required 
31. AI/RAG Knowledge Base 
Requirements 
31.1 Recommended Knowledge Chunks 
This document should be divided into focused knowledge chunks, such as: 
1.​ Jobs module overview. 
2.​ Accessing Jobs. 
3.​ Jobs tabs. 
4.​ Searching for jobs. 
5.​ Applying filters. 
6.​ Understanding job cards. 
7.​ Opening job details. 
8.​ Saving and unsaving jobs. 
9.​ Applying for a job. 
10.​Application form fields. 
11.​Application validation. 
12.​Application status. 
13.​Missing Apply now button. 
14.​Job visibility and 30-day filtering. 
15.​Mobile Jobs limitations. 
16.​Job-related troubleshooting. 
17.​Human support escalation. 
18.​Privacy and security guidance. 
19.​Employer-side functionality status. 

31.2 Metadata 
Each knowledge-base chunk should include: 
Metadata 
Example 
Module 
Jobs 
Document ID 
WISEIN-JOB-019 
Feature 
Job Application 
User Type 
Candidate 
Platform 
Web 
Source Type 
Frontend Code / UI Observation 
Verification Status 
Confirmed / Pending 
Version 
1.0 
Last Reviewed 
17 September 2026 
Sensitivity 
Internal Product Knowledge 
31.3 RAG Safety Rules 

The AI must: 
●​ Retrieve information from the latest approved document. 
●​ Distinguish confirmed behavior from pending behavior. 
●​ Avoid presenting frontend assumptions as official policies. 
●​ Avoid inventing API responses. 
●​ Avoid exposing internal source code to users. 
●​ Escalate unresolved account-specific issues. 
●​ Use authorized live data for current application status. 
●​ Avoid requesting sensitive authentication information. 
●​ Preserve document version and verification metadata. 
32. Product and Engineering Questions 
The following questions should be reviewed before this document is marked as approved. 
Product Questions 
1.​ Is the 30-day job visibility rule an official product policy? 
2.​ Are jobs older than 30 days archived, hidden, or still available through other views? 
3.​ Is resume upload planned for the application workflow? 
4.​ Should advanced filters be available on mobile? 
5.​ What is the official list of supported job types? 
6.​ How are recommended jobs selected? 
7.​ Are application-status labels officially defined? 
8.​ Are employers able to manage jobs through WiseIN or another portal? 
9.​ Are job notifications available? 
10.​What happens when an employer closes a job after applications are submitted? 
Engineering Questions 
1.​ What are the authoritative API schemas? 
2.​ What backend authorization checks are applied? 
3.​ How are duplicate applications prevented? 
4.​ Is application status retrieved from a live backend source? 
5.​ What are the official error codes and error messages? 
6.​ How is HTML content sanitized? 
7.​ What pagination and sorting rules are used? 
8.​ How are saved jobs persisted? 
9.​ What is the behavior when a job becomes inactive during application submission? 
10.​Are all API endpoints protected against unauthorized access? 

Security Questions 
1.​ Is job-description HTML sanitized on the backend? 
2.​ Are application fields validated server-side? 
3.​ Can users access another candidate’s application data? 
4.​ Are sensitive application fields protected in API responses? 
5.​ Are application requests protected against replay or duplicate submission? 
6.​ What data-retention policies apply to job applications? 
7.​ Are suspicious job links or malicious descriptions reported and moderated? 
33. Documentation Completion Checklist 
●​ Jobs overview documented. 
●​ Source-code locations identified. 
●​ Main routes documented. 
●​ Job tabs documented. 
●​ Search functionality documented. 
●​ Filters documented. 
●​ Job cards documented. 
●​ Job details documented. 
●​ Application workflow documented. 
●​ Application fields documented. 
●​ Save and unsave behavior documented. 
●​ Application statuses documented. 
●​ Loading and empty states documented. 
●​ Error scenarios documented. 
●​ Troubleshooting guidance documented. 
●​ Privacy and security considerations documented. 
●​ Platform differences documented. 
●​ QA test cases prepared. 
●​ AI customer-support guidance prepared. 
●​ Human support escalation documented. 
●​ Known limitations listed. 
●​ Source and verification register prepared. 
●​ RAG knowledge-base requirements prepared. 
●​ Backend behavior verified. 
●​ Live application testing completed. 
●​ Product review completed. 
●​ Engineering review completed. 
●​ QA review completed. 
●​ Security review completed. 
●​ Support-team approval completed. 

34. Version History 
Versio
n 
Date 
Author 
Changes 
Review Status 
1.0 
17 September 
2026 
MSR 
Initial documentation based on 
frontend source-code analysis 
Draft — Pending 
Review 
 



---

