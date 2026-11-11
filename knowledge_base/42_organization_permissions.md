# Organization Permissions

## Source: WISEIN-ORGANIZATION-PERMISSIONS-042.pdf

WISEIN— ORGANIZATION PERMISSIONS  
Document ID: WISEIN-ORGANIZATION-PERMISSIONS-042 
Document Type: Product Knowledge Base / RAG Dataset 
Platform: WiseIN 
Category: Organizations → Permissions & Access Control 
 
 
1. DOCUMENT PURPOSE 
This document defines the available and currently documented knowledge about 
Organization Permissions on WiseIN. 
It covers: 
• 
Organization access control  
• 
Permissions  
• 
Visibility  
• 
Access levels  
• 
Teams  
• 
Departments  
• 
Stakeholders  
• 
Employee/team-member access  
• 
Organization-level vs individual-level permissions  
• 
People connected to an Organization  
• 
Privacy considerations  
• 
Permission-related troubleshooting  
• 
AI chatbot intents  
• 
RAG vs live API responsibilities  
• 
Unsupported permission details that the chatbot must not invent  
A key principle for this document is: 

WiseIN publicly confirms that Organization access, visibility, permissions, and access 
levels are part of the Organization experience, but the exact permission-role matrix is 
not currently documented publicly. 
Therefore, this document records confirmed functionality without inventing 
administrator/manager/member permission levels. 
 
2. WHAT ARE ORGANIZATION PERMISSIONS? 
Organization Permissions control what people associated with an Organization can 
access or manage within the Organization environment. 
The previously provided WiseIN Organization UI contains a Manage Access feature 
described as: 
“Control visibility, permissions, and access levels for teams, departments, and 
stakeholders.” 
This establishes three important areas of Organization access management: 
• 
Visibility  
• 
Permissions  
• 
Access levels  
and identifies the organizational groups to which access can apply: 
• 
Teams  
• 
Departments  
• 
Stakeholders  
The exact permission hierarchy is not shown in the supplied screenshot and is not currently 
described in sufficient detail on WiseIN's public Organization documentation. 
 
3. WHY ORGANIZATION PERMISSIONS EXIST 
Organization permissions are intended to help organizations control how people 
associated with the organization interact with its Organization environment. 
An Organization may contain different types of people, including: 

• 
Team members  
• 
Leadership  
• 
Contributors  
• 
Employees  
• 
Department members  
• 
Other stakeholders  
The supplied Organization UI explicitly describes the People area as allowing an 
organization to: 
“Add team members, leadership profiles, and contributors connected to your 
Organization.” 
This indicates that WiseIN's Organization model is not limited to a simple employee list. 
 
4. ORGANIZATION ACCESS MANAGEMENT 
WiseIN's Organization interface includes Manage Access as an Organization capability. 
The supplied Organization documentation describes Manage Access as controlling: 
Visibility 
Determines what information or Organization resources are visible to particular people or 
groups. 
Permissions 
Determines what actions or resources a person may be authorized to use. 
Access Levels 
Determines the level of access assigned to a person, team, department, or stakeholder. 
The chatbot should keep these concepts separate. 
For example: 
Visibility = what someone can see. 
Permission = what someone is allowed to do. 
Access level = the level/category of access assigned to them. 

 
5. ORGANIZATION PEOPLE AND PERMISSIONS 
The supplied Organization screenshot provides important context. 
The Organization's People section contains: 
• 
Organization profile information  
• 
Followers  
• 
Employees count  
• 
Department filters  
• 
People associated with the Organization  
The screenshot shows a People page with: 
All Departments 
followed by department categories including: 
• 
Executive  
• 
Engineering  
• 
Product  
• 
Sales  
• 
Marketing  
• 
Design  
• 
Human Resources  
The screenshot therefore demonstrates that WiseIN's Organization People experience can 
organize people by departments. 
Important 
These departments are visible in the supplied UI example. 
They should not automatically be interpreted as a fixed list of departments available to 
every WiseIN Organization. 
The exact departments available may depend on the Organization's configuration. 
 

6. PEOPLE CONNECTED TO AN ORGANIZATION 
The current supplied Organization People UI states: 
“Add team members, leadership profiles, and contributors connected to your 
Organization.” 
This means the Organization People concept can include different categories of 
organizational participants. 
The chatbot should therefore avoid treating the terms: 
• 
Employee  
• 
Team member  
• 
Leadership  
• 
Contributor  
• 
Stakeholder  
as automatically identical. 
Their exact permissions may differ depending on the Organization's configuration and the 
access-control implementation. 
 
7. ORGANIZATION PERMISSIONS VS EMPLOYEE VERIFICATION 
These are separate concepts. 
Employee Verification 
Determines whether an employee/professional is shown as verified. 
WiseIN's public Organization page demonstrates employee statuses such as: 
• 
Verified  
• 
Pending  
 
Organization Permissions 
Determine what a person can see or access within the Organization environment. 
Therefore: 

Being verified does not by itself define a person's Organization permissions. 
Similarly: 
Having Organization access does not automatically mean that a person has 
completed individual verification. 
The chatbot must not combine these two concepts. 
 
8. ORGANIZATION PERMISSIONS VS ORGANIZATION VERIFICATION 
Organization verification validates the Organization. 
WiseIN's public Organization documentation states that it verifies business information 
including: 
• 
CIN  
• 
GST  
• 
PAN  
• 
Official business registration documents  
before Organizations can join.  
Permissions are different. 
They concern access to Organization resources and management functions. 
Therefore: 
Organization Verification 
→ establishes the verified Organization identity. 
Organization Permissions 
→ control authorized access and actions within the Organization. 
A verified Organization does not mean every person connected to it automatically receives 
the same permissions. 
 
9. DEPARTMENT-BASED ACCESS 
The supplied Organization People screenshot demonstrates department filtering. 

Visible example categories include: 
All Departments 
Executive 
Engineering 
Product 
Sales 
Marketing 
Design 
Human Resources 
This suggests that departments can be used to organize people within an Organization. 
The public Organization documentation also describes role-based employee discovery and 
filtering by: 
• 
Role  
• 
Expertise  
• 
Availability  
 
However, WiseIN does not currently publicly document exactly how department 
membership affects permissions. 
Therefore, the chatbot must not say: 
“Engineering employees can only access engineering information.” 
unless this is confirmed by the actual product. 
 
10. TEAM-BASED ACCESS 
WiseIN's Organization product is designed for teams and organizational collaboration. 
The official Organization page describes the product as helping organizations maintain a 
verified professional presence and collaborate with authentic companies.  
The Organization UI also includes a Manage Access concept covering teams. 

Therefore, teams are relevant to Organization access management. 
However, the exact team-permission model is not publicly documented. 
Do not invent: 
• 
Team Owner  
• 
Team Admin  
• 
Team Manager  
• 
Team Member  
• 
Team Viewer  
as official WiseIN roles unless the application or internal documentation confirms them. 
 
11. STAKEHOLDER ACCESS 
The supplied Organization documentation explicitly includes stakeholders within the 
Manage Access description. 
This indicates that Organization access management is not necessarily limited to 
employees. 
Possible organizational relationships may include people who participate in an 
Organization without necessarily being ordinary employees. 
However, WiseIN does not publicly define the complete stakeholder permission model. 
Therefore: 
A stakeholder may be part of an Organization's access-management structure, but the 
exact rights assigned to stakeholders must come from the current Organization 
configuration. 
 
12. LEADERSHIP AND CONTRIBUTORS 
The supplied People UI specifically states: 
“Add team members, leadership profiles, and contributors connected to your 
Organization.” 

This establishes that leadership and contributors can be represented in the Organization's 
People ecosystem. 
However, the public documentation does not establish that: 
• 
Leadership automatically receives administrative access.  
• 
Contributors automatically receive posting access.  
• 
Team members automatically receive management access.  
The chatbot must not infer permissions from someone's title or relationship. 
 
13. PERMISSION PRINCIPLE 
The chatbot should follow this rule: 
A person's organizational relationship and their permission level are separate pieces 
of information. 
For example: 
A person may be: 
Employee → Verified → Engineering 
without the chatbot being able to conclude that they can: 
• 
edit Organization information  
• 
manage employees  
• 
publish Organization posts  
• 
manage permissions  
• 
view private Organization information  
Those capabilities should only be stated when the user's actual permissions or official 
documentation confirms them. 
 
14. VISIBILITY CONTROLS 
Visibility is explicitly included in WiseIN's Organization access-management concept. 

Visibility concerns what information or Organization resources are accessible to particular 
people or groups. 
This can be relevant to: 
• 
Teams  
• 
Departments  
• 
Stakeholders  
as identified by the supplied Organization UI. 
Important limitation 
The public WiseIN website does not currently specify: 
• 
exact visibility levels  
• 
exact visibility options  
• 
private vs internal vs public Organization categories  
• 
whether individual employees can override Organization visibility  
• 
whether department-level visibility is configurable  
• 
whether visibility can be applied separately to every Organization feature  
Therefore, the chatbot should not invent these options. 
 
15. PERMISSIONS 
Permissions are the authorization layer. 
A permission may conceptually determine whether a person can perform an action or 
access a resource. 
Examples of areas where Organization permissions may become relevant include: 
• 
Organization profile management  
• 
People/team management  
• 
Content management  
• 
Jobs  
• 
Meetings  

• 
Analytics  
• 
Organization settings  
• 
Access management  
However, these examples should be treated as areas where permissions may matter, not 
as confirmed individual permission assignments. 
The public WiseIN site does not currently provide a complete permission matrix. 
 
16. ACCESS LEVELS 
WiseIN's Organization UI explicitly refers to access levels. 
An access level represents the level of authorization assigned to an organizational 
participant. 
However, WiseIN's public website does not currently document the names or number of 
access levels. 
Therefore, the chatbot must not invent a fixed hierarchy such as: 
Owner 
Admin 
Manager 
Member 
Viewer 
unless this is later verified from the actual WiseIN product. 
 
17. DO NOT INFER ACCESS FROM JOB TITLE 
The chatbot must not assume that a person's professional title determines their WiseIN 
Organization permissions. 
For example: 
“CEO” does not automatically mean the chatbot can assume full Organization 
administrator privileges. 

Similarly: 
“Developer” does not automatically mean the person has limited permissions. 
“HR” does not automatically mean the person can manage all employees. 
The actual Organization access configuration must determine permissions. 
 
18. ORGANIZATION PROFILE MANAGEMENT 
WiseIN Organizations have dedicated Organization profiles. 
The official Organization offering includes an Individual Organization Profile and 
Organization branding capabilities.  
The supplied Organization creation UI includes fields such as: 
• 
Organization Name  
• 
Organization Email  
• 
Organization CIN  
• 
Bio  
• 
Organization Logo  
• 
Organization URL Name  
Permissions may determine which people are authorized to manage such information. 
However, the public documentation does not specify which access level is responsible for 
each field. 
Therefore, the chatbot should not claim: 
“Only the Owner can edit the Organization Name.” 
unless verified. 
 
19. ORGANIZATION CONTENT PERMISSIONS 
Organizations can publish professional/company-related content. 
The supplied Organization UI describes a Post Updates capability for sharing: 
• 
Company news  

• 
Achievements  
• 
Product launches  
• 
Announcements  
The current WiseIN website also supports Organization profiles and professional 
networking features.  
However, the public documentation does not specify which Organization roles can publish 
or edit Organization content. 
Therefore, if a user asks: 
“Who can post for the Organization?” 
the chatbot should not guess. 
A safe answer is: 
“WiseIN provides Organization content and access-management capabilities, but the 
public documentation does not specify which Organization permission level can publish or 
manage Organization posts. The current Organization access configuration determines 
this.” 
 
20. JOB AND RECRUITMENT PERMISSIONS 
WiseIN's Organization offering includes: 
• 
Publish Jobs & Internship Opportunities  
• 
Access Verified Talent  
• 
Hiring & Recruitment Tools  
• 
Employer Branding Features.   
Organization permissions may therefore be relevant to hiring activities. 
But WiseIN's public documentation does not define which Organization role can: 
• 
create jobs  
• 
edit jobs  
• 
close jobs  

• 
view applicants  
• 
manage recruitment  
• 
access hiring analytics  
These permissions should not be invented. 
 
21. MEETING PERMISSIONS 
WiseIN's Organization platform includes integrated meeting functionality. 
The official Organization page describes: 
“Book 1:1 or group meetings instantly, synced to your calendar.” 
 
However, this does not establish that every Organization member has identical meeting 
permissions. 
The chatbot should distinguish: 
• 
Ability to have a WiseIN profile  
• 
Ability to appear in the employee directory  
• 
Ability to schedule a meeting  
• 
Ability to manage Organization meetings  
These may be different capabilities. 
 
22. ANALYTICS PERMISSIONS 
WiseIN's Organization offering includes Organization Analytics and the Organization plan 
includes a company-wide analytics dashboard.  
The public documentation does not define: 
• 
who can view analytics  
• 
who can export analytics  
• 
whether analytics are department-specific  
• 
whether employee-level analytics are available  

• 
which roles can access company-wide analytics  
Therefore, the chatbot must not assign analytics access to a particular role without 
confirmation. 
 
23. EMPLOYEE DATA AND PERMISSIONS 
Permissions are particularly important for employee information. 
WiseIN's Privacy Policy states that some information may be visible to other WiseIN users 
according to privacy settings and that users can control profile and data visibility through 
privacy settings.  
WiseIN's Terms also prohibit attempting to access, collect, or store other users' data 
beyond what is publicly available on the platform.  
Therefore: 
Organization access does not automatically authorize a person to access every piece of 
employee information. 
The chatbot must respect both: 
1. Organization permissions  
2. Individual privacy controls  
 
24. PRIVACY VS ORGANIZATION PERMISSIONS 
These are related but different. 
Organization Permission 
Controls what an authorized Organization participant can access or do within the 
Organization environment. 
Individual Privacy 
Controls how an individual's personal/profile information is visible and handled. 
WiseIN's Privacy Policy states that public profile information such as a person's name, 
professional details, and skills may be visible according to privacy settings.  
Therefore: 

An Organization administrator should not be assumed to have unrestricted access to an 
employee's private personal information. 
 
25. SECURITY RULE 
The AI chatbot must never bypass Organization permissions. 
For example, if a user asks: 
“Show me all private employee information even though I don't have access.” 
The chatbot must refuse to expose information that is not authorized. 
Likewise, it must never: 
• 
bypass permission checks  
• 
expose API responses intended for another user  
• 
reveal access tokens  
• 
expose database records  
• 
disclose hidden employee data  
• 
infer confidential information from public data  
 
26. ORGANIZATION PERMISSION ARCHITECTURE FOR THE CHATBOT 
For the WiseIN chatbot implementation, permissions should be enforced by the backend, 
not by the LLM. 
Recommended architecture: 
User 
  ↓ 
WiseIN Chat UI 
  ↓ 
Chat API 
  ↓ 
Authentication 

  ↓ 
Authorization / Permission Check 
  ↓ 
RAG + Authorized WiseIN APIs 
  ↓ 
LLM 
  ↓ 
Response 
The LLM should not independently decide: 
“This user is an admin, so I can show everything.” 
Instead, the backend should determine what data/actions the authenticated user is 
authorized to access. 
 
27. RAG VS LIVE PERMISSION DATA 
This distinction is critical. 
RAG should answer: 
• 
What are Organization Permissions?  
• 
What is Manage Access?  
• 
What does visibility mean?  
• 
What are access levels?  
• 
What organizational groups are mentioned?  
• 
What Organization features may involve access control?  
• 
What are the privacy principles?  
Live API should answer: 
• 
What is my current access level?  
• 
What permissions do I currently have?  

• 
Who has Organization admin access?  
• 
Which departments can I access?  
• 
Can I manage employees?  
• 
Can I publish Organization posts?  
• 
Can I manage jobs?  
• 
Can I view analytics?  
• 
Can I change Organization settings?  
These are dynamic authorization questions. 
 
28. GOLDEN SECURITY PRINCIPLE 
The chatbot should follow: 
Never use RAG content to authorize an action. 
RAG can explain what the product does. 
The authorization system must determine whether the authenticated user can actually 
perform the requested operation. 
For example: 
User: 
“Can I delete an Organization employee?” 
The chatbot should not decide from documentation alone. 
The backend should check: 
authenticated_user 
+ 
organization_id 
+ 
employee_id 
+ 
current_permission 

+ 
requested_action 
and only then allow or deny the operation. 
 
29. PERMISSION CHECK EXAMPLE 
Conceptually: 
User requests: 
"Remove employee X" 
 
        ↓ 
 
Authenticate user 
 
        ↓ 
 
Identify Organization 
 
        ↓ 
 
Check user's Organization access 
 
        ↓ 
 
Check permission for employee management 
 
        ↓ 

 
If authorized: 
    perform action 
 
If unauthorized: 
    deny action 
 
        ↓ 
 
Return safe response 
The LLM should not directly execute the database operation. 
 
30. ORGANIZATION PERMISSION QUESTIONS 
The chatbot should understand questions such as: 
General 
“What are Organization Permissions?” 
“What does Manage Access mean?” 
“How does Organization access work?” 
Visibility 
“Who can see our Organization information?” 
“Can I control visibility?” 
“Can I restrict access by department?” 
Permissions 
“Who can manage employees?” 
“Who can edit the Organization?” 
“Who can post updates?” 

“Who can manage jobs?” 
Access Levels 
“What is an access level?” 
“How can I change someone's access?” 
“What access level do I have?” 
Teams 
“Can permissions be assigned to teams?” 
“Can I control access for a team?” 
Departments 
“Can I manage permissions by department?” 
“Can Engineering have different access?” 
Stakeholders 
“Can stakeholders have Organization access?” 
“What can a stakeholder access?” 
 
31. CURRENTLY CONFIRMED VS NOT CONFIRMED 
Confirmed 
WiseIN's Organization experience includes: 
• 
Employees  
• 
Meetings  
• 
Analytics  
• 
Employee Directory  
• 
Employee filtering by role  
• 
Employee filtering by expertise  
• 
Employee filtering by availability  
• 
Verified employee profiles  

• 
Organization collaboration  
• 
Organization access-management concept  
• 
Visibility controls  
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
The first group is confirmed by WiseIN's public Organization page; the access-management 
details are additionally grounded in the previously supplied Organization 
UI/documentation.  
 
Not publicly documented in sufficient detail 
The following are not confirmed as fixed WiseIN permission rules: 
• 
Owner role  
• 
Admin role  
• 
Manager role  
• 
Member role  
• 
Viewer role  
• 
Exact permission hierarchy  
• 
Exact access-level names  
• 
Exact permission matrix  
• 
Exact department permission rules  
• 
Exact team permission rules  
• 
Exact stakeholder permission rules  
• 
Exact employee-management permissions  
• 
Exact Organization-post permissions  

• 
Exact job-management permissions  
• 
Exact analytics permissions  
• 
Exact meeting-management permissions  
• 
Exact Organization-setting permissions  
• 
Permission inheritance rules  
• 
Custom roles  
• 
Permission cloning  
• 
Permission templates  
• 
Bulk permission assignment  
• 
Permission audit logs  
These must be added only after confirmation from the actual WiseIN application or internal 
product documentation. 
 
32. IMPORTANT CHATBOT GUARDRAILS 
Guardrail 1 — Never invent roles 
Do not claim that WiseIN officially has Owner/Admin/Manager/Member roles unless 
verified. 
Guardrail 2 — Never infer permissions 
Do not infer permissions from: 
• 
job title  
• 
employee status  
• 
department  
• 
verification status  
• 
organization membership  
Guardrail 3 — Never bypass authorization 
Every private Organization operation must go through backend authorization. 
Guardrail 4 — Protect employee privacy 

Organization access does not automatically mean access to private employee information. 
Guardrail 5 — Explain, don't authorize 
The chatbot can explain the permission system, but backend authorization must determine 
actual access. 
Guardrail 6 — Use live data for current permissions 
Questions such as: 
“What permissions do I have?” 
must be answered using authorized live account/Organization data. 
Guardrail 7 — Do not expose permission internals unnecessarily 
Do not reveal backend authorization logic, security tokens, API credentials, database 
queries, or internal security mechanisms. 
Guardrail 8 — Deny safely 
If the backend says the user is unauthorized, provide a simple explanation without 
exposing restricted information. 
 
33. SAFE RESPONSE FOR UNKNOWN PERMISSION DETAILS 
If a user asks: 
“What are the exact Organization permission levels?” 
Recommended response: 
“WiseIN provides Organization access management for visibility, permissions, and access 
levels across teams, departments, and stakeholders. However, the public WiseIN 
documentation does not currently specify the complete permission-level hierarchy or 
exact role matrix. The exact options available depend on the current Organization 
configuration.” 
This should be the default response until internal documentation provides the complete 
matrix. 
 
34. SAFE RESPONSE FOR CURRENT USER PERMISSIONS 

If the user asks: 
“What permissions do I have?” 
Recommended behavior: 
1. Authenticate the user.  
2. Identify the current Organization.  
3. Query the authorized Organization permissions endpoint.  
4. Return only the permissions allowed for that user.  
5. Do not infer missing permissions.  
If no permission API exists: 
“I can explain WiseIN's Organization access-management features, but I can't determine 
your current Organization permissions from the static knowledge base.” 
 
35. SAFE RESPONSE FOR MANAGING EMPLOYEE ACCESS 
User: 
“How can I change an employee's access?” 
Recommended response: 
“WiseIN provides Organization access management for visibility, permissions, and access 
levels across teams, departments, and stakeholders. The public documentation does not 
currently specify the exact steps for changing an individual employee's access. If the 
current Organization dashboard exposes the relevant Manage Access controls, those 
controls should be used.” 
 
36. SAFE RESPONSE FOR DEPARTMENT PERMISSIONS 
User: 
“Can I give Engineering different permissions?” 
Recommended response: 
“WiseIN's Organization access-management concept includes teams and departments, 
but the public documentation does not currently confirm the exact department-level 

permission configuration. The available controls in your Organization's Manage Access 
section determine whether this can be configured.” 
 
37. SAFE RESPONSE FOR ADMIN ACCESS 
User: 
“Who is the Organization admin?” 
Recommended response: 
“WiseIN's public Organization documentation does not currently define a specific 
Organization Admin role or public administrator directory. If your Organization dashboard 
provides access-management information, the current authorized Organization data 
should be used to determine who has administrative access.” 
 
38. AI INTENTS 
Recommended intent classification: 
organization_permissions_overview 
organization_manage_access 
organization_visibility 
organization_access_levels 
organization_permission_roles 
organization_permission_assignment 
organization_permission_change 
organization_permission_remove 
organization_team_permissions 
organization_department_permissions 
organization_stakeholder_permissions 
organization_employee_permissions 
organization_employee_access 

organization_content_permissions 
organization_job_permissions 
organization_meeting_permissions 
organization_analytics_permissions 
organization_profile_permissions 
organization_permission_current_user 
organization_permission_troubleshooting 
organization_permission_denied 
organization_permission_privacy 
organization_permission_security 
 
39. AI ENTITIES 
organization 
organization_id 
user 
user_id 
employee 
employee_id 
team 
team_id 
department 
department_id 
stakeholder 
role 
permission 
access_level 

visibility 
resource 
action 
organization_profile 
employee_profile 
post 
job 
meeting 
analytics 
 
40. EXAMPLE USER QUERIES 
The chatbot should understand natural variations such as: 
“What are Organization permissions?” 
“What does Manage Access do?” 
“Can I control who sees our Organization?” 
“How do access levels work?” 
“Can I assign permissions to teams?” 
“Can I give different permissions to departments?” 
“Who can manage employees?” 
“Who can edit the Organization profile?” 
“Who can post for the company?” 
“Who can manage jobs?” 
“Who can view analytics?” 
“Can a stakeholder access the Organization?” 
“What permissions do I have?” 
“Why can't I access this Organization feature?” 

“How do I change an employee's permissions?” 
 
41. RAG METADATA 
document_id: 
WISEIN-ORGANIZATION-PERMISSIONS-001 
 
title: 
WiseIN Organization Permissions Knowledge Base Dataset 
 
category: 
Organization 
 
subcategory: 
Permissions and Access Control 
 
topics: 
organization permissions 
manage access 
organization access 
visibility 
access levels 
teams 
departments 
stakeholders 
employee permissions 
organization privacy 

organization security 
access control 
 
primary_source: 
https://www.wisein.in/teams 
 
secondary_sources: 
https://www.wisein.in/privacy 
https://www.wisein.in/terms%26conditions 
https://www.wisein.in/pricing 
https://www.wisein.in/ 
 
source_type: 
official website + supplied product UI 
 
current_status: 
current_public_documentation 
 
confidence: 
high for documented Organization capabilities 
limited for exact permission hierarchy 
 
requires_live_api: 
yes, for current user permissions and authorization decisions 
 
42. SOURCE PRIORITY FOR THIS DOCUMENT 

For permission-related chatbot answers, use this priority: 
Priority 1 — Live WiseIN authorization/API 
For: 
• 
Current permissions  
• 
Current access level  
• 
Current Organization membership  
• 
Current employee permissions  
• 
Current access status  
Priority 2 — Internal WiseIN product documentation 
For: 
• 
Exact roles  
• 
Permission matrix  
• 
UI workflows  
• 
Manage Access implementation  
• 
Permission assignment  
Priority 3 — Official WiseIN website 
For: 
• 
Organization capabilities  
• 
Employee Directory  
• 
Teams  
• 
Organization collaboration  
• 
General Organization functionality  
Priority 4 — Supplied WiseIN UI screenshots 
For: 
• 
Current observed labels  
• 
Current navigation  

• 
Current People/Department presentation  
• 
Current Manage Access terminology  
 
43. FINAL KNOWLEDGE MODEL 
The current evidence supports the following conceptual model: 
WISEIN ORGANIZATION 
        │ 
        ├── Organization Profile 
        │ 
        ├── People 
        │     │ 
        │     ├── Team Members 
        │     ├── Leadership 
        │     ├── Contributors 
        │     └── Employees 
        │ 
        ├── Teams 
        │ 
        ├── Departments 
        │ 
        ├── Stakeholders 
        │ 
        └── Manage Access 
              │ 
              ├── Visibility 

              ├── Permissions 
              └── Access Levels 
The Organization People screenshot additionally demonstrates department-oriented 
organization of people, with an All Departments option and department categories such 
as Executive, Engineering, Product, Sales, Marketing, Design, and Human Resources. 
 
44. MOST IMPORTANT IMPLEMENTATION RULE 
For the WiseIN AI chatbot: 
Do not let the LLM decide permissions. 
The correct architecture is: 
                    ┌──────────────────────┐ 
                    │      WiseIN User     │ 
                    └──────────┬───────────┘ 
                               │ 
                               ▼ 
                    ┌──────────────────────┐ 
                    │      Chat UI         │ 
                    └──────────┬───────────┘ 
                               │ 
                               ▼ 
                    ┌──────────────────────┐ 
                    │   Chat Backend/API   │ 
                    └──────────┬───────────┘ 
                               │ 
                    ┌──────────▼───────────┐ 
                    │ Authentication +     │ 

                    │ Authorization        │ 
                    └──────────┬───────────┘ 
                               │ 
                ┌──────────────┴──────────────┐ 
                │                             │ 
                ▼                             ▼ 
       ┌─────────────────┐          ┌──────────────────┐ 
       │ RAG Knowledge   │          │ WiseIN Live APIs │ 
       │ Base            │          │                  │ 
       └────────┬────────┘          └────────┬─────────┘ 
                │                            │ 
                │ Explanation                │ Current 
                │                            │ permissions 
                └──────────────┬─────────────┘ 
                               ▼ 
                         ┌────────────┐ 
                         │    LLM     │ 
                         └────────────┘ 
RAG tells the AI what WiseIN's permission system means. 
The authorization layer determines what the user is actually allowed to access. 
Live APIs provide current permission and Organization data. 
That separation is essential for preventing the chatbot from accidentally exposing 
restricted Organization or employee information. 
 
 



---

