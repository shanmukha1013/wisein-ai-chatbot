# Organization Employees

## Source: WISEIN-ORGANIZATION-EMPLOYEES-041.pdf

WISEIN— ORGANIZATION EMPLOYEES  
Document ID: WISEIN-ORGANIZATION-EMPLOYEES-041 
Document Type: Product Knowledge Base / RAG Dataset 
Primary Domain: Organizations → Employees / Employee Directory / Team Profiles 
Platform: WiseIN 
 
1. DOCUMENT PURPOSE 
This document defines the knowledge required for an AI chatbot to answer questions about 
Organization Employees on WiseIN. 
It covers: 
• 
What Organization Employees are  
• 
Employee profiles associated with an Organization  
• 
Employee verification  
• 
Employee verification status  
• 
Employee Directory  
• 
Employee search and filtering  
• 
Employee roles, expertise, and availability  
• 
Organization-level employee visibility  
• 
Organization access and permissions  
• 
Verified vs Pending employees  
• 
Employee and Organization verification differences  
• 
Organization plan capabilities  
• 
Employee-related troubleshooting  
• 
Privacy and security considerations  
• 
AI chatbot intents and entities  
• 
RAG metadata  
• 
Unsupported information that the chatbot must not invent  

This document is intended to be used as a retrieval source for a WiseIN customer-
support chatbot. 
 
2. WHAT ARE ORGANIZATION EMPLOYEES ON WISEIN? 
An Organization Employee is a professional associated with an Organization's WiseIN 
presence. 
WiseIN's Organization platform is designed to provide organizations with a verified 
professional presence while allowing their associated employees and team members to 
appear through verified professional profiles. 
The official WiseIN Organization page demonstrates an Employees section within the 
Organization dashboard, alongside areas such as Meetings and Analytics.  
The public Organization example shows employees with: 
• 
Name  
• 
Professional role  
• 
Verification status  
For example, the current WiseIN Organization page displays sample employees such as: 
• 
Founder and CEO — Verified  
• 
Product Manager — Verified  
• 
Part-time UI/UX — Verified  
• 
Part-time Developer — Pending  
These are examples presented by WiseIN's website and should be treated as 
demonstration data rather than a guaranteed list of actual platform users.  
 
3. WHY ORGANIZATION EMPLOYEES MATTER 
The Organization employee system is intended to connect an organization's verified 
business identity with the professional identities of its people. 
The Organization offering emphasizes: 
• 
Verified company profiles  

• 
Verified employee profiles  
• 
Employee discovery  
• 
Role-based filtering  
• 
Expertise-based filtering  
• 
Availability-based filtering  
• 
Professional collaboration  
• 
Meetings and scheduling  
• 
Hiring and recruitment  
• 
Organization analytics  
WiseIN describes its Organization platform as providing a verified company and 
employee profile experience and a role-based company directory.  
 
4. ORGANIZATION VERIFICATION VS EMPLOYEE VERIFICATION 
These two concepts must not be confused. 
Organization Verification 
Organization verification validates the business/organization. 
WiseIN publicly states that organizations may be verified using information such as: 
• 
CIN  
• 
GST  
• 
PAN  
• 
Official business registration documents  
The WiseIN Organization page says these documents are verified before organizations can 
join.  
Employee Verification 
Employee verification relates to the individual professional associated with the 
organization. 
WiseIN's Organization page describes: 

“Verified Company & Employee Profiles” 
and states that company and employee profiles are verified through KYC processes with 
official business documents.  
Therefore: 
Organization verification = verification of the organization/business 
Employee verification = verification/authenticity of the associated professional 
A verified organization should not automatically be interpreted as meaning that every 
person associated with it has already completed individual verification. 
The public WiseIN Organization example itself demonstrates this distinction by showing 
some employees as Verified and another as Pending.  
 
5. EMPLOYEE VERIFICATION STATUS 
The public Organization dashboard example shows employee verification statuses. 
The currently demonstrated statuses include: 
Verified 
A Verified employee is shown as having completed the relevant verification process 
represented by the Organization platform. 
The public example shows several employees with a Verified status.  
Pending 
A Pending employee is shown as not yet having completed or received completion of the 
relevant verification process. 
The public example includes a part-time developer with a Pending status.  
Important chatbot rule 
The chatbot should not assume why a particular employee is Pending unless the live 
WiseIN system provides the reason. 
Possible reasons such as: 
• 
verification not started  
• 
documents under review  

• 
verification failed  
• 
invitation not accepted  
• 
organization association not completed  
must not be stated as the actual reason unless WiseIN's authorized backend data confirms 
it. 
 
6. EMPLOYEE DIRECTORY 
WiseIN publicly describes an Employee Directory as part of its Organization platform. 
The directory is intended to help users discover employees associated with organizations. 
WiseIN specifically states that employees can be filtered by: 
• 
Role  
• 
Expertise  
• 
Availability  
and describes this as a role-based company directory.  
Example use cases 
A user may want to find: 
• 
Employees working in a particular role  
• 
Professionals with a particular area of expertise  
• 
Employees available for collaboration  
• 
People suitable for a business conversation  
• 
Professionals within a particular organization  
The chatbot should understand queries such as: 
“Find employees from this organization.” 
“Who works as a Product Manager?” 
“Show employees with UI/UX expertise.” 
“Which employees are available?” 

“How can I find employees by role?” 
 
7. EMPLOYEE SEARCH AND FILTERING 
The official Organization page specifically mentions advanced search and filters for the 
employee directory.  
The publicly documented filtering dimensions are: 
Role 
Users can search/filter employees according to their professional role. 
Examples: 
• 
Founder  
• 
CEO  
• 
Product Manager  
• 
Developer  
• 
UI/UX professional  
The exact available role values may depend on the employee's profile information. 
Expertise 
Employees can be filtered according to expertise. 
For example, an organization may have professionals with different technical or business 
skills. 
The chatbot should not claim a fixed list of expertise categories unless the current 
application/API provides one. 
Availability 
WiseIN's Organization page also mentions employee availability as a filtering dimension.  
Availability should not be interpreted as permanent employment status. 
It may refer to availability for professional interaction, meetings, or collaboration 
depending on the implementation. 

If the live application does not provide the exact meaning, the chatbot should avoid 
inventing a specific definition. 
 
8. EMPLOYEE PROFESSIONAL PROFILE 
An Organization employee should be treated as an individual WiseIN professional profile 
associated with an organization. 
WiseIN's general privacy policy states that profile information may include: 
• 
Professional bio  
• 
Skills  
• 
Experience  
• 
Education  
• 
Projects  
• 
Social links  
depending on what the user chooses to provide.  
Therefore, an employee profile may contain professional information that helps other users 
understand the employee's role and expertise. 
The chatbot should distinguish between: 
Organization information 
and 
Employee's personal professional information. 
 
9. EMPLOYEE ROLE 
An employee may be associated with a professional role within an organization. 
The Organization page's example employee dashboard demonstrates role information such 
as: 
• 
Founder and CEO  
• 
Product Manager  

• 
Part-time UI/UX  
• 
Part-time Developer   
The chatbot should use the role shown by the current WiseIN profile or Organization data. 
It must not infer an employee's role from: 
• 
their skills alone  
• 
their education  
• 
their posts  
• 
their previous employer  
• 
their username  
• 
their email address  
unless the platform explicitly provides that information. 
 
10. EMPLOYEE ASSOCIATION WITH AN ORGANIZATION 
An employee profile can be represented as part of an organization's employee/team 
ecosystem. 
However, the public WiseIN website does not currently document the exact technical 
workflow for: 
• 
inviting an employee  
• 
accepting an employee invitation  
• 
assigning an employee to an organization  
• 
removing an employee  
• 
changing an employee's organization  
• 
changing employee roles  
• 
approving employee requests  
• 
transferring an employee between organizations  
Therefore, the chatbot must not invent a specific button sequence or workflow. 
Correct chatbot behavior 

If asked: 
“How do I add an employee to my organization?” 
A safe answer is: 
“WiseIN provides organization employee and team-management capabilities, but the exact 
employee invitation or addition workflow is not fully documented on the public website. If 
you share what you see in your Organization dashboard, I can guide you through the 
available options.” 
If an authorized WiseIN API later exposes the actual workflow, the chatbot can provide the 
current UI instructions based on that live data. 
 
11. ORGANIZATION EMPLOYEE MANAGEMENT 
The previously provided WiseIN Organization UI documentation includes a Manage Access 
capability. 
The Organization page shown in the provided UI describes it as: 
“Control visibility, permissions, and access levels for teams, departments, and 
stakeholders.” 
This indicates that Organization management includes access-control concepts. 
However, the exact permission roles and permission matrix are not publicly documented 
sufficiently to define them as fixed product behavior. 
Therefore, the chatbot should not invent roles such as: 
• 
Organization Owner  
• 
Admin  
• 
HR Admin  
• 
Manager  
• 
Employee  
• 
Viewer  
unless those roles are confirmed by the current application or internal WiseIN 
documentation. 

 
12. TEAMS AND EMPLOYEE PROFILES 
WiseIN's current Organization pricing information states that the Organization plan 
includes: 
“Up to 5 teams verified profiles.”  
The wording on the public pricing page is somewhat ambiguous. 
Therefore, the chatbot should not reinterpret this statement as a detailed employee-
limit rule. 
In particular, do not automatically answer: 
“An organization can have only five employees.” 
That is not supported. 
The public page says “Up to 5 teams verified profiles,” not “five employees.” 
The exact relationship between: 
• 
teams  
• 
verified profiles  
• 
employees  
• 
departments  
should be confirmed from the actual Organization product implementation before being 
used as a hard chatbot rule. 
 
13. EMPLOYEE DIRECTORY AND ORGANIZATION DISCOVERY 
WiseIN positions Organizations as a way for verified businesses and professionals to 
connect. 
The Organization platform includes: 
• 
Company profiles  
• 
Employee Directory  
• 
Verified employee profiles  

• 
Organization discovery  
• 
Role-based employee filtering  
• 
Expertise filtering  
• 
Availability filtering  
• 
Collaboration and partnership requests   
This means the employee directory can function as a bridge between: 
Organization → Employees → Professional expertise → Collaboration 
 
14. EMPLOYEES AND MEETINGS 
WiseIN's Organization platform also provides meeting functionality. 
The official Organization page describes: 
“Book 1:1 or group meetings instantly, synced to your calendar.”  
This allows Organization employees to be part of professional meeting and collaboration 
workflows. 
However, the chatbot must not claim that: 
• 
every employee is automatically available for meetings  
• 
every employee can be booked  
• 
every employee has public availability  
• 
meetings are automatically enabled for every employee  
unless the live application confirms it. 
 
15. EMPLOYEES AND RECRUITMENT 
Organization accounts are also designed for hiring and recruitment. 
The public WiseIN Organization offering includes: 
• 
Publish Jobs & Internship Opportunities  
• 
Access Verified Talent  

• 
Hiring & Recruitment Tools  
• 
Employer Branding Features   
The employee directory and verified professional profiles can therefore support 
organizational talent discovery. 
However, an existing organization employee and an external candidate/talent profile 
are different concepts. 
The chatbot should not describe every person appearing in an employee directory as a job 
candidate. 
 
16. EMPLOYEE VERIFICATION AND TRUST 
WiseIN's Organization offering is built around verification. 
The official website states that WiseIN verifies: 
• 
CIN  
• 
GST  
• 
PAN  
• 
business registration documents  
for Organizations.  
The Organization page also describes verified company and employee profiles and states 
that verification uses KYC processes with official business documents.  
The platform's broader positioning is based on verified professional identities rather than 
purely self-reported identities.  
Important distinction 
Verification is intended to establish authenticity. 
It does not mean the chatbot should make additional claims about an employee's: 
• 
competence  
• 
performance  
• 
employment quality  

• 
seniority beyond the displayed role  
• 
trustworthiness in every context  
• 
qualifications beyond documented profile information  
 
17. EMPLOYEE PRIVACY 
Employee information must be treated as personal/professional data. 
WiseIN's Privacy Policy states that users can provide profile information such as: 
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
social links  
and that public profile information may be visible to other WiseIN users depending on 
privacy settings.  
The Privacy Policy also states that users have control over their information through 
account settings and can request access, modification, or deletion subject to applicable 
limitations.  
Chatbot privacy rule 
The chatbot must not reveal private employee information simply because someone asks 
for it. 
For example, it should not provide: 
• 
private phone numbers  
• 
private email addresses  
• 
government ID information  
• 
verification documents  
• 
private addresses  

• 
private employment information  
• 
private account information  
unless the platform explicitly authorizes the information to be displayed. 
 
18. EMPLOYEE DATA THAT SHOULD NOT BE EXPOSED 
The chatbot must follow WiseIN's privacy and content rules. 
WiseIN's Content Policies prohibit sharing another person's phone number, email, address, 
or personal details without explicit permission.  
Therefore, if a user asks: 
“Give me the employee's personal phone number.” 
The chatbot should not expose it. 
A safe response would be: 
“I can help you use the employee's available WiseIN profile or approved contact/meeting 
options, but I can't provide private contact information.” 
 
19. VERIFIED EMPLOYEE VS ORGANIZATION MEMBER 
The chatbot should distinguish between: 
Organization member 
A person associated with an organization. 
Verified employee 
A person whose relevant verification status is shown as verified. 
Pending employee 
A person whose employee/verification status is currently pending. 
External professional 
A WiseIN professional who is not necessarily associated with the organization. 
These terms should not be treated as interchangeable. 
 

20. EMPLOYEE STATUS QUESTIONS 
The chatbot may receive questions such as: 
“Is this employee verified?” 
“Why does this employee show Pending?” 
“How many verified employees does the organization have?” 
“Who are the verified employees?” 
Correct behavior 
For a live employee-status question, the chatbot should use an authorized WiseIN API/tool 
if available. 
The RAG knowledge base can explain what Verified and Pending mean, but it cannot 
know an individual's current status from static documentation. 
Architecture rule 
Static RAG → explain the meaning of status 
Authorized live API → retrieve the current employee status 
 
21. EMPLOYEE DIRECTORY QUESTIONS 
The chatbot should recognize these intents: 
Search Employees 
“Find employees in this organization.” 
Filter by Role 
“Show developers.” 
Filter by Expertise 
“Find employees with AI experience.” 
Filter by Availability 
“Who is available for a meeting?” 
Employee Verification 
“Is this employee verified?” 

Employee Profile 
“Tell me about this employee.” 
Organization Membership 
“Is this person part of the organization?” 
Employee Count 
“How many employees does this organization have?” 
Employee Management 
“How do I add an employee?” 
Employee Access 
“How do I manage employee access?” 
Employee Permissions 
“Who can manage organization employees?” 
 
22. LIVE DATA VS RAG DATA 
This distinction is important for the WiseIN chatbot. 
RAG KNOWLEDGE BASE SHOULD ANSWER 
• 
What is an Organization Employee?  
• 
What is the Employee Directory?  
• 
What employee filters are supported?  
• 
What does Verified mean?  
• 
What does Pending mean?  
• 
What employee-related features are publicly documented?  
• 
What privacy rules apply?  
• 
What is the Organization plan?  
• 
What is the difference between organization and employee verification?  
LIVE API SHOULD ANSWER 

When authorized APIs are available: 
• 
Current employee list  
• 
Current employee count  
• 
Current employee verification status  
• 
Current employee role  
• 
Current employee availability  
• 
Current organization membership  
• 
Current employee permissions  
• 
Current employee invitation status  
• 
Current employee profile information  
• 
Current Organization employee data  
Golden architecture principle 
RAG explains the product. APIs provide the current user's/product data. 
 
23. EMPLOYEE DIRECTORY — CHATBOT ANSWER EXAMPLE 
User: 
“What is the Organization Employee Directory?” 
Recommended answer: 
“WiseIN's Organization Employee Directory is designed to help discover employees 
associated with an organization. WiseIN describes filtering employees by role, expertise, 
and availability, allowing users to find relevant professionals for collaboration. Employee 
profiles can also have verification statuses such as Verified or Pending.”  
 
24. VERIFIED EMPLOYEE — CHATBOT ANSWER EXAMPLE 
User: 
“What does Verified mean for an employee?” 
Recommended answer: 

“A Verified employee is shown as having completed the relevant verification represented by 
WiseIN's Organization platform. WiseIN describes its Organization offering as providing 
verified company and employee profiles. The exact verification details for an individual 
should be taken from the employee's current WiseIN status rather than inferred.”  
 
25. PENDING EMPLOYEE — CHATBOT ANSWER EXAMPLE 
User: 
“Why is an employee showing Pending?” 
Recommended answer: 
“Pending indicates that the employee's relevant verification status has not yet reached 
Verified. WiseIN's public Organization example shows both Verified and Pending employee 
statuses. The public documentation does not specify the exact reason for every Pending 
status, so the specific reason should be checked in the current Organization dashboard or 
authorized WiseIN support/API.”  
 
26. ADDING AN EMPLOYEE — CHATBOT ANSWER 
User: 
“How can I add an employee?” 
Recommended answer: 
“WiseIN provides Organization employee and team-management capabilities, but the 
public website does not document the complete employee invitation/addition workflow. 
The exact steps should be based on the options available in your current Organization 
dashboard.” 
Do not invent: 
• 
“Click Add Employee”  
• 
“Enter employee email”  
• 
“Send invitation”  
• 
“Employee receives OTP”  
• 
“Employee accepts invitation”  

unless these steps are confirmed by the actual WiseIN application or internal 
documentation. 
 
27. REMOVING AN EMPLOYEE 
The public website does not currently provide enough information to document the exact 
employee-removal workflow. 
Therefore, do not invent a sequence such as: 
Employee → three dots → Remove → Confirm 
unless this is verified in the application. 
If the user asks how to remove someone: 
“The exact employee-removal workflow is not documented in WiseIN's public Organization 
documentation. Please check the Organization management controls available in your 
dashboard.” 
 
28. EMPLOYEE ROLE CHANGES 
The public website demonstrates employee roles but does not document the exact 
workflow for changing them. 
Therefore, the chatbot should not claim that an administrator can definitely: 
• 
edit employee roles  
• 
assign departments  
• 
change job titles  
• 
change employment type  
unless the current product/API confirms those operations. 
 
29. EMPLOYEE ACCESS AND PERMISSIONS 
The previously provided Organization UI includes a Manage Access concept for 
controlling: 
• 
Visibility  

• 
Permissions  
• 
Access levels  
• 
Teams  
• 
Departments  
• 
Stakeholders  
This indicates that access management is part of the Organization experience. 
However, the exact permission hierarchy is not sufficiently documented publicly. 
Therefore: 
“WiseIN provides Organization access-management capabilities, but the exact permission 
levels and role hierarchy depend on the current Organization implementation.” 
This should be the chatbot's default answer until detailed internal documentation is 
available. 
 
30. ORGANIZATION PLAN AND EMPLOYEES 
The current public Organization pricing page lists the Organization plan as being for teams 
and talent agencies. 
The Organization plan includes: 
• 
CIN & GST verification  
• 
Up to 5 teams verified profiles  
• 
Organization branding page  
• 
Hiring & job posting tools  
• 
Company-wide analytics dashboard  
• 
Dedicated support  
• 
Organization badge on profile   
The homepage also describes Organization capabilities including: 
• 
CIN verification in India  
• 
Global Organization verification through Sumsub  

• 
Verified Organization Badge  
• 
Individual Organization Profile  
• 
Hiring and recruitment  
• 
Access to verified talent  
• 
Organization analytics  
• 
Dedicated support  
• 
Organization success sessions   
Important 
The chatbot should not convert the pricing statement “Up to 5 teams verified profiles” 
into a claim that an Organization can have only five employees. 
That relationship is not clearly specified by the public pricing page. 
 
31. EMPLOYEES AND ORGANIZATION ANALYTICS 
The Organization dashboard publicly demonstrates an Analytics section alongside 
Employees and Meetings.  
The Organization plan also includes a company-wide analytics dashboard.  
However, the public documentation does not specify the exact employee analytics 
metrics. 
Therefore, do not invent metrics such as: 
• 
employee engagement rate  
• 
employee activity score  
• 
employee productivity  
• 
employee performance ranking  
• 
employee response rate  
unless the live dashboard or internal product documentation confirms them. 
 
32. EMPLOYEES AND ORGANIZATION CONTENT 

Organizations can use WiseIN to publish company-related content. 
The previously provided Organization UI describes: 
Post Updates 
Share company news, achievements, product launches, and announcements with the 
community. 
The current WiseIN Home page also describes Company Pages as supporting company 
bios, teams, testimonials, jobs, and analytics.  
Employees may therefore be associated with an organization's professional presence, but 
the chatbot should not assume that every employee automatically has permission to 
publish Organization content. 
Content-publishing permissions should be determined by the current Organization access 
controls. 
 
33. EMPLOYEE CONTENT AND PRIVACY 
Employees remain individual users with their own professional profiles and privacy 
considerations. 
WiseIN's Privacy Policy states that public profile information may be visible according to 
privacy settings, while users retain control over their information.  
The chatbot must therefore avoid treating Organization membership as permission to 
expose all employee information. 
For example: 
Allowed when publicly available: 
“What role does this employee list on their WiseIN profile?” 
Not automatically allowed: 
“Give me their private email address.” 
 
34. EMPLOYEE SECURITY RULES FOR THE AI CHATBOT 
The AI assistant must never request or expose: 

• 
Passwords  
• 
Login credentials  
• 
OTPs  
• 
Government ID numbers  
• 
Aadhaar details  
• 
PAN details  
• 
Verification documents  
• 
Session tokens  
• 
API keys  
• 
Private employee contact details  
• 
Private employee data  
The WiseIN Privacy Policy states that sensitive information is protected through access 
controls and security measures and that only authorized personnel should have access to 
sensitive information.  
 
35. EMPLOYEE INFORMATION HIERARCHY 
When answering employee-related questions, use this information hierarchy: 
Level 1 — Live Authorized WiseIN Data 
Use this for: 
• 
Employee status  
• 
Employee membership  
• 
Employee role  
• 
Employee availability  
• 
Current employee count  
• 
Current employee list  
• 
Organization relationship  
Level 2 — Internal WiseIN Product Documentation 

Use this for: 
• 
Exact employee workflows  
• 
Invitation process  
• 
Access roles  
• 
Permission levels  
• 
Employee management actions  
• 
UI instructions  
Level 3 — Official WiseIN Public Website 
Use this for: 
• 
Employee Directory concept  
• 
Role/expertise/availability filtering  
• 
Organization employee verification concept  
• 
Organization plan features  
• 
General Organization functionality  
Level 4 — General Knowledge 
Use only when the question is not asking about an actual WiseIN feature. 
 
36. IMPORTANT UNSUPPORTED DETAILS 
The following should not be presented as confirmed WiseIN functionality unless additional 
internal documentation or live application evidence is available: 
• 
Exact “Add Employee” button  
• 
Exact employee invitation workflow  
• 
Exact employee acceptance workflow  
• 
Employee invitation OTP  
• 
Employee invitation email format  
• 
Employee invitation expiration time  

• 
Maximum number of employees  
• 
Exact number of administrators  
• 
Exact employee permission levels  
• 
Exact employee roles available in the system  
• 
Exact employee-removal process  
• 
Employee transfer workflow  
• 
Employee department assignment workflow  
• 
Automatic employee verification after Organization verification  
• 
Automatic employee approval  
• 
Employee verification SLA  
• 
Exact verification documents required from every employee  
• 
Employee verification rejection reasons  
• 
Employee verification retry limits  
• 
Exact Employee Directory UI layout  
• 
Exact Employee Directory URL  
• 
Exact employee availability algorithm  
• 
Exact employee ranking algorithm  
• 
Employee performance scoring  
• 
Employee productivity analytics  
• 
Automatic employee role extraction  
• 
Automatic employment verification from company email  
• 
Automatic synchronization with HR systems  
• 
Automatic synchronization with LinkedIn  
• 
Automatic employee import from company databases  
These are not confirmed by the public WiseIN documentation reviewed for this 
document. 

 
37. AI INTENTS 
The chatbot should classify Organization Employee questions into the following intents: 
organization_employee_overview 
organization_employee_directory 
organization_employee_search 
organization_employee_filter_role 
organization_employee_filter_expertise 
organization_employee_filter_availability 
organization_employee_verification 
organization_employee_pending_status 
organization_employee_profile 
organization_employee_membership 
organization_employee_count 
organization_employee_add 
organization_employee_invite 
organization_employee_remove 
organization_employee_role 
organization_employee_department 
organization_employee_permissions 
organization_employee_access 
organization_employee_privacy 
organization_employee_contact 
organization_employee_meeting 
organization_employee_hiring 
organization_employee_analytics 

organization_employee_troubleshooting 
organization_employee_security 
 
38. AI ENTITIES 
Important entities for RAG/query understanding: 
organization 
organization_id 
employee 
employee_id 
employee_name 
employee_role 
employee_status 
verification_status 
role 
expertise 
skill 
availability 
department 
team 
permission 
access_level 
organization_profile 
employee_profile 
employee_directory 
meeting 
job 

analytics 
privacy_setting 
 
39. SAMPLE USER QUESTIONS 
The chatbot should understand natural-language variations such as: 
General 
“What are Organization Employees?” 
“How do employees work on WiseIN?” 
“What is an employee profile?” 
Directory 
“What is the Employee Directory?” 
“How can I find employees?” 
“Can I search organization employees?” 
Filtering 
“Can I filter employees by role?” 
“Can I find employees by skills?” 
“Can I find available employees?” 
Verification 
“What does Verified mean?” 
“Why is an employee Pending?” 
“Are organization employees verified?” 
“Does organization verification verify all employees?” 
Management 
“How do I add an employee?” 
“How do I invite my employees?” 
“How can I remove an employee?” 

“Can I change an employee's role?” 
Access 
“Who can manage employees?” 
“How do employee permissions work?” 
“Can I control employee access?” 
Privacy 
“Can I see an employee's personal information?” 
“Can I get an employee's phone number?” 
Meetings 
“Can I book a meeting with an employee?” 
“Can I find employees available for meetings?” 
 
40. GOLDEN ANSWERS FOR THE CHATBOT 
Q: What is an Organization Employee? 
Answer: 
An Organization Employee is a professional associated with an Organization's WiseIN 
presence. WiseIN provides an employee-focused Organization dashboard and describes 
verified employee profiles and an Employee Directory for discovering professionals by role, 
expertise, and availability.  
 
Q: Are Organization Employees verified? 
Answer: 
WiseIN describes its Organization platform as providing verified company and employee 
profiles. The public Organization example shows employees with statuses such as Verified 
and Pending, so an organization's verification should not automatically be treated as 
confirmation that every employee is already verified.  
 
Q: What is the Employee Directory? 

Answer: 
The Employee Directory is an Organization feature designed to help discover employees. 
WiseIN says employees can be filtered by role, expertise, and availability.  
 
Q: Can I search employees by role? 
Answer: 
Yes. WiseIN's Organization documentation describes a role-based Employee Directory with 
filtering by role, expertise, and availability.  
 
Q: Can I search employees by expertise? 
Answer: 
Yes. WiseIN describes employee filtering by expertise as part of its Organization Employee 
Directory.  
 
Q: Can I search employees by availability? 
Answer: 
WiseIN's Organization page lists availability as one of the Employee Directory filtering 
options. The exact meaning and availability data shown for an individual should be taken 
from the current WiseIN application.  
 
Q: What does Pending mean? 
Answer: 
Pending indicates that the employee's relevant verification status is not currently shown as 
Verified. WiseIN's public Organization example demonstrates both Verified and Pending 
employee statuses. The exact reason for a specific Pending status is not publicly 
documented.  
 
Q: Does verifying the Organization automatically verify all employees? 

Answer: 
Not necessarily. WiseIN presents Organization verification and employee verification as 
separate concepts, and its Organization example shows employees with different 
verification statuses.  
 
Q: Can I see an employee's private contact details? 
Answer: 
Only information that WiseIN makes available according to the user's profile and privacy 
settings should be displayed. Private contact information should not be disclosed without 
authorization. WiseIN's Content Policies specifically prohibit sharing another person's 
phone number, email, address, or personal details without permission.  
 
41. RAG METADATA 
Recommended metadata for this document: 
document_id: 
WISEIN-ORGANIZATION-EMPLOYEES-001 
 
title: 
WiseIN Organization Employees Knowledge Base Dataset 
 
category: 
Organization 
 
subcategory: 
Employees 
 
topics: 

organization employees 
employee directory 
employee verification 
verified employees 
pending employees 
employee roles 
employee expertise 
employee availability 
employee access 
employee permissions 
organization teams 
employee privacy 
organization meetings 
organization hiring 
 
source_type: 
official_website + product_ui_reference 
 
primary_source: 
https://www.wisein.in/teams 
 
secondary_sources: 
https://www.wisein.in/pricing 
https://www.wisein.in/privacy 
https://www.wisein.in/content-policies 
https://www.wisein.in/ 

 
status: 
current_public_documentation 
 
confidence: 
high for publicly documented capabilities 
medium/low for undocumented workflows 
 
requires_live_api: 
yes, for current employee status, membership, availability and employee-specific 
information 
 
42. CHATBOT GUARDRAILS 
The WiseIN AI assistant must follow these rules when answering Organization Employee 
questions: 
Rule 1 — Do not confuse Organization and Employee verification 
Organization verification does not automatically prove that every employee is individually 
verified. 
Rule 2 — Do not invent employee workflows 
If the public documentation does not describe how employees are added, removed, 
invited, or transferred, do not invent UI instructions. 
Rule 3 — Use live data for live employee information 
Current employee status, role, membership, availability, and counts should come from an 
authorized WiseIN API where available. 
Rule 4 — Respect employee privacy 
Never expose private employee information. 
Rule 5 — Do not infer employment status 

A profile appearing in an Organization directory should not automatically be interpreted as 
proof of current employment unless WiseIN explicitly identifies the person as an employee. 
Rule 6 — Do not infer competence from verification 
Verification establishes identity/authenticity according to the platform's process; it does 
not independently establish professional skill or performance. 
Rule 7 — Do not invent permission levels 
Only describe permission roles confirmed by the current WiseIN product documentation. 
Rule 8 — Do not invent employee limits 
Do not interpret the Organization plan's “Up to 5 teams verified profiles” as a five-employee 
limit.  
Rule 9 — Protect sensitive information 
Never request or reveal: 
• 
Passwords  
• 
OTPs  
• 
Government ID numbers  
• 
Verification documents  
• 
API keys  
• 
Session tokens  
• 
Private contact details  
Rule 10 — Escalate when live data is required 
If the user asks about a specific employee's current status or organization membership and 
no authorized live API is available, explain that the chatbot's static knowledge cannot verify 
the current status. 
 
43. FINAL PRODUCT UNDERSTANDING 
The current public WiseIN documentation establishes the following Organization Employee 
model: 
Organization 

↓ 
Verified Organization Profile 
↓ 
Employees / Employee Profiles 
↓ 
Employee Verification Status 
• 
Verified  
• 
Pending  
↓ 
Employee Directory 
↓ 
Discover by 
• 
Role  
• 
Expertise  
• 
Availability  
↓ 
Professional Collaboration 
• 
Meetings  
• 
Networking  
• 
Hiring  
• 
Partnerships  
This model is supported by WiseIN's current Organization documentation.  
The most important implementation distinction for the chatbot is: 
The knowledge base should explain how Organization Employees and the Employee 
Directory work, while authorized WiseIN APIs should provide current employee-
specific information. 
 

44. OFFICIAL SOURCE REFERENCES 
WiseIN — Organizations 
WiseIN for Organizations 
This is the primary source for the Organization Employee Directory, employee verification 
examples, role/expertise/availability filtering, Organization dashboard concepts, and 
employee profiles.  
WiseIN — Pricing 
WiseIN Pricing 
Used for the current Organization plan and Organization-related capabilities.  
WiseIN — Privacy Policy 
WiseIN Privacy Policy 
Used for employee/profile privacy, data visibility, and personal-data handling.  
WiseIN — Content Policies 
WiseIN Content Policies 
Used for restrictions on sharing other people's personal information and Organization/job-
related content.  
 
DOCUMENT STATUS 
Document: WISEIN-ORGANIZATION-EMPLOYEES-001 
Purpose: RAG / AI chatbot training 
Coverage: Organization Employees, Employee Directory, verification status, filtering, 
access, privacy, meetings, hiring 
Primary evidence: Current official WiseIN Organization pages 
UI evidence: Previously supplied Organization screenshots and documentation 
Important limitation: Exact employee invitation, removal, role-management, permission, 
and verification workflows are not sufficiently documented on the public website and 
should be added only after they are confirmed from the actual WiseIN application or 
internal product documentation. 
 
 



---

