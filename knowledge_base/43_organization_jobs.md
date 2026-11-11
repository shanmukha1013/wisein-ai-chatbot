# Organization Jobs

## Source: WISEIN-ORGANIZATION-JOBS-043.pdf

WISEIN — ORGANIZATION JOBS  
Document ID: WISEIN-ORGANIZATION-JOBS-043 
Document Type: Product Knowledge Base / RAG Dataset 
Platform: WiseIN 
Category: Organizations → Jobs & Hiring 
 
 
1. DOCUMENT PURPOSE 
This document defines the knowledge required for an AI chatbot to answer questions about 
Organization Jobs on WiseIN. 
It covers: 
• 
Organization Jobs  
• 
Job listings  
• 
Hiring and recruitment  
• 
Internship opportunities  
• 
Job discovery  
• 
Job search  
• 
Job listing information  
• 
Organization job pages  
• 
Job posting  
• 
Genuine-opportunity requirements  
• 
Part-time and freelance opportunities  
• 
Remote opportunities  
• 
Job visibility  
• 
Job-related privacy and safety  
• 
Reporting job listings  
• 
Organization hiring capabilities  

• 
Job troubleshooting  
• 
RAG vs live API responsibilities  
• 
AI intents and entities  
• 
Unsupported details that must not be invented  
WiseIN's current Organization offering explicitly includes “Publish Jobs & Internship 
Opportunities”, “Access Verified Talent”, and “Hiring & Recruitment Tools.”  
 
2. WHAT ARE ORGANIZATION JOBS ON WISEIN? 
Organization Jobs are employment, internship, freelance, or other legitimate professional 
opportunities published by Organizations on WiseIN. 
WiseIN's Organization offering is designed to support: 
• 
Hiring  
• 
Job posting  
• 
Internship opportunities  
• 
Access to verified talent  
• 
Recruitment  
• 
Employer branding  
The current WiseIN homepage lists Publish Jobs & Internship Opportunities, Access 
Verified Talent, and Hiring & Recruitment Tools under the Organization plan.  
The Organization pricing page also lists Hiring & Job posting tools as part of the 
Organization plan.  
 
3. ORGANIZATION JOBS IN THE WISEIN ORGANIZATION PROFILE 
The supplied Organization screenshots show that an Organization profile can contain a 
dedicated: 
Jobs 
section. 

For example, the supplied screenshot of Feonix E-Retail Llp shows these Organization 
tabs: 
• 
About  
• 
Sessions  
• 
Posts  
• 
Clips  
• 
News  
• 
Jobs  
• 
People  
• 
Funding  
The Jobs tab is selected in the screenshot. 
The page contains a: 
Search Jobs 
search field. 
A currently listed example job is: 
Reel Editor (Part-Time / Freelance) 
with information including: 
• 
Remote  
• 
Part Time  
• 
Posted recently  
This demonstrates that Organization Jobs can appear directly within an Organization's 
public profile. 
 
4. ORGANIZATION JOBS PAGE 
An Organization's Jobs section functions as a place where visitors can discover 
opportunities associated with that Organization. 
The supplied UI demonstrates that the Jobs section can display: 

• 
Search Jobs  
• 
Job title  
• 
Work arrangement/location information  
• 
Employment type  
• 
Posting recency  
The exact fields displayed may vary depending on the job listing and current WiseIN 
implementation. 
 
5. ORGANIZATION WITH NO JOBS 
The supplied screenshot of Jnyan Cit Bajrang shows an Organization Jobs page with no 
currently displayed positions. 
The empty-state message says: 
“Open positions, hiring updates, and career opportunities will appear here once posted.” 
This is important for chatbot understanding. 
An Organization having a Jobs tab does not necessarily mean that it currently has open 
positions. 
Possible states include: 
Jobs available 
The Jobs section displays one or more open positions. 
No current jobs 
The Jobs section is available, but no current openings are displayed. 
The chatbot should therefore distinguish: 
Organization has a Jobs section 
from: 
Organization currently has an open job. 
 
6. JOB SEARCH 

The supplied Organization Jobs UI includes: 
Search Jobs 
This allows users to search within the Organization's job listings. 
A user may therefore ask: 
“Search jobs at this Organization.” 
“Does this Organization have any developer jobs?” 
“Find jobs posted by this company.” 
The chatbot should use the current WiseIN job data/API when answering questions about 
currently available positions. 
 
7. JOB TITLE 
A job listing has a job title. 
The supplied UI provides an example: 
Reel Editor (Part-Time / Freelance) 
The chatbot should reproduce the job title exactly as provided by the current listing. 
It should not rewrite a title in a way that changes its meaning. 
For example: 
If the listing says: 
“Reel Editor (Part-Time / Freelance)” 
the chatbot should not describe it as: 
“Full-time Video Editor” 
unless the listing itself states that. 
 
8. EMPLOYMENT TYPE 
The supplied Organization Jobs screenshot demonstrates employment-type information. 
The example job shows: 

PART TIME 
and the title identifies: 
Part-Time / Freelance 
WiseIN's Content Policies explicitly require job posters to be honest about the nature of an 
opportunity. If a position is: 
• 
unpaid  
• 
equity-only  
• 
part-time  
the listing must make that clear.  
Therefore, the chatbot should preserve the employment type provided in the job listing. 
 
9. REMOTE WORK 
The supplied Organization Jobs screenshot demonstrates: 
Remote 
for the example Reel Editor opportunity. 
This means job listings can communicate remote work arrangements. 
The chatbot should not assume every Organization job is remote. 
The current listing should be checked for its actual work arrangement. 
Possible values may include whatever the current WiseIN job system provides, but the 
chatbot should not invent a fixed list unless confirmed by the live product. 
 
10. JOB POSTING RECENCY 
The supplied screenshot displays: 
Posted recently 
This indicates that job listings can communicate posting recency. 
The chatbot should use the current listing's displayed date/recency information when 
available. 

It should not invent an exact posting date when only a relative label such as “Posted 
recently” is available. 
 
11. JOB DESCRIPTION 
A complete job listing may provide additional information about the opportunity. 
However, the public WiseIN Organization pages reviewed do not provide a complete public 
specification of every job-posting field. 
Therefore, the chatbot should not claim a fixed required job-posting schema unless it is 
verified from the actual WiseIN application. 
Potential information may include things such as: 
• 
Job title  
• 
Description  
• 
Employment type  
• 
Work arrangement  
• 
Skills  
• 
Qualifications  
• 
Responsibilities  
• 
Compensation  
• 
Application information  
But only information actually present in the listing should be presented as factual. 
 
12. JOB AND INTERNSHIP OPPORTUNITIES 
WiseIN explicitly supports both: 
• 
Jobs  
• 
Internship opportunities  
The current Organization offering lists: 
“Publish Jobs & Internship Opportunities” 

as a hiring capability.  
Therefore, the chatbot should recognize: 
Job 
Internship 
Hiring opportunity 
Career opportunity 
Professional opportunity 
as related Organization hiring concepts. 
 
13. FREELANCE AND PART-TIME OPPORTUNITIES 
The supplied UI provides a real product example of a: 
Part-Time / Freelance 
job. 
WiseIN's Content Policies also explicitly state that job posters must disclose if an 
opportunity is: 
• 
unpaid  
• 
equity-only  
• 
part-time.  
Therefore, the chatbot should preserve these distinctions. 
It should not automatically classify: 
• 
freelance as full-time employment  
• 
part-time as full-time  
• 
unpaid as paid  
• 
equity-only as salaried  
 
14. JOB POSTING REQUIREMENTS 

WiseIN's Content Policies provide important requirements for Jobs, Hiring & Opportunities. 
The policy states that every: 
• 
job  
• 
gig  
• 
internship  
• 
opportunity  
posted on WiseIN must be genuine. 
The policy specifically emphasizes: 
• 
Real role  
• 
Real company  
• 
Real compensation  
and prohibits fake jobs used to collect data or leads.  
This is a core part of the Organization Jobs knowledge base. 
 
15. GENUINE JOB REQUIREMENT 
A WiseIN job listing should represent a genuine opportunity. 
The chatbot should therefore treat claims such as: 
“This is a guaranteed job.” 
“This job will definitely pay ₹X.” 
“This company guarantees placement.” 
as claims that must come from the actual job listing or Organization—not assumptions. 
WiseIN's policy requires genuine job opportunities but does not mean the chatbot should 
independently guarantee employment outcomes.  
 
16. HONEST COMPENSATION DISCLOSURE 
WiseIN's Content Policies require job posters to be honest about the opportunity. 

If a role is: 
• 
Unpaid  
• 
Equity-only  
• 
Part-time  
the listing should say so clearly.  
Therefore, the chatbot should never change or hide compensation conditions. 
Example 
If the listing says: 
“Unpaid Internship” 
the chatbot should not summarize it as: 
“Internship with compensation.” 
If the listing says: 
“Equity only” 
the chatbot should preserve that condition. 
 
17. NO SCAM JOB OFFERS 
WiseIN explicitly prohibits scam job offers. 
Its Content Policies prohibit: 
• 
Fake earning schemes  
• 
Multi-level marketing  
• 
Pyramid schemes  
• 
“Pay us first to get the job” scams  
• 
Unrealistic job offers designed to deceive users.  
Therefore, the chatbot should recognize potentially suspicious job-related requests and 
direct users toward reporting/support mechanisms rather than endorsing suspicious 
opportunities. 
 

18. JOB POSTING AND VERIFIED ORGANIZATIONS 
WiseIN's Organization platform emphasizes verified Organizations. 
The Organization page states that WiseIN verifies: 
• 
CIN  
• 
GST  
• 
PAN  
• 
Business registration documents  
before Organizations can join.  
The Organization platform also advertises verified company and employee profiles.  
This creates a trust-oriented hiring environment. 
However: 
Organization verification should not be interpreted as a guarantee that every 
individual job listing is suitable, legitimate in every respect, or guaranteed to result in 
employment. 
The chatbot should still rely on the actual job listing and WiseIN's reporting/content-policy 
mechanisms. 
 
19. ACCESS TO VERIFIED TALENT 
WiseIN's Organization offering includes: 
Access Verified Talent 
as a hiring capability.  
This indicates that Organizations can use WiseIN for talent discovery in addition to 
publishing jobs. 
The chatbot should distinguish: 
Job Posting 
Organization publishes an opportunity. 
Talent Discovery 

Organization searches/discovers professionals. 
These are complementary but different hiring functions. 
 
20. ORGANIZATION JOBS VS EMPLOYEE DIRECTORY 
These should not be confused. 
Organization Jobs 
Shows opportunities currently offered by an Organization. 
Organization People 
Shows people connected with the Organization. 
Employee Directory 
Helps discover employees by role, expertise, and availability. 
WiseIN's Organization page specifically describes an Employee Directory with filtering by 
role, expertise, and availability.  
A person listed under People is not automatically a job applicant. 
Likewise, a job listing is not automatically an employee record. 
 
21. ORGANIZATION JOBS VS WISEIN GENERAL JOB BOARD 
WiseIN's public individual pricing page also lists: 
Browse Jobs & Opportunities 
for the Basic plan and: 
Job & Internship board 
for the Student plan.  
Therefore, WiseIN has broader job/opportunity discovery beyond an individual 
Organization's Jobs tab. 
The chatbot should distinguish: 
Organization Jobs 
Jobs associated with a particular Organization. 

General Jobs & Opportunities 
Jobs/opportunities available through WiseIN's broader platform. 
Student Job & Internship Board 
Job/internship access associated with the Student offering. 
 
22. JOB DISCOVERY 
A user may discover Organization Jobs through an Organization's profile. 
The supplied screenshots demonstrate: 
Organization Profile 
       ↓ 
Jobs 
       ↓ 
Search Jobs 
       ↓ 
Open Positions 
The current WiseIN homepage also positions Organizations as providing hiring and 
recruitment capabilities.  
 
23. JOB SEARCH QUESTIONS 
The chatbot should understand: 
“Does this company have jobs?” 
“What jobs are open at this Organization?” 
“Show me the Organization's vacancies.” 
“Are there any internships?” 
“Does this company hire part-time employees?” 
“Are there remote jobs?” 

“Find developer jobs from this Organization.” 
“Search jobs at this company.” 
For these questions, live job data should be preferred over static RAG content. 
 
24. LIVE JOB DATA VS RAG 
This is particularly important for the chatbot. 
RAG should answer: 
• 
What are Organization Jobs?  
• 
Where do Organization Jobs appear?  
• 
What types of opportunities are supported?  
• 
What are WiseIN's job-content rules?  
• 
What does Remote mean when shown on a listing?  
• 
What does Part Time mean when shown?  
• 
What is the difference between Jobs and People?  
• 
What are the rules against fake/scam jobs?  
Live API should answer: 
• 
Which jobs are currently open?  
• 
Is this job still available?  
• 
What is the current job title?  
• 
Who posted the job?  
• 
When was it posted?  
• 
What is the current application status?  
• 
What is the job's current location?  
• 
Is the job currently accepting applications?  
• 
Which Organization currently has this opening?  
 

25. GOLDEN RULE FOR CURRENT JOB QUESTIONS 
Static RAG explains the job feature. Live APIs provide current job listings. 
For example: 
User: 
“Does Feonix E-Retail currently have any jobs?” 
The chatbot should query the current Organization Jobs data. 
It should not answer solely from this documentation. 
The supplied screenshot provides a historical/current UI observation, but a static 
screenshot cannot guarantee that the position is still open. 
 
26. JOB APPLICATIONS 
The supplied screenshots demonstrate job discovery, but they do not provide sufficient 
evidence for the complete application workflow. 
Therefore, the chatbot must not invent: 
• 
Apply button behavior  
• 
Application form fields  
• 
Resume-upload rules  
• 
Application status stages  
• 
Recruiter notification process  
• 
Application deadline behavior  
• 
Interview workflow  
• 
Applicant tracking workflow  
unless confirmed by the current WiseIN application or internal product documentation. 
 
27. SAFE ANSWER — HOW TO APPLY 
If the user asks: 
“How do I apply for an Organization job?” 

Recommended answer: 
“Open the Organization's Jobs section and select the relevant job listing. The exact 
application flow depends on the current job listing and WiseIN's application interface. 
Follow the application option provided on the job page.” 
If the actual listing exposes a specific application mechanism, the chatbot should describe 
that current mechanism. 
 
28. JOB APPLICATION STATUS 
The public Organization documentation reviewed does not specify a complete applicant-
status system. 
Therefore, do not invent statuses such as: 
Applied 
Under Review 
Shortlisted 
Interview 
Selected 
Rejected 
unless the live application or internal documentation confirms them. 
 
29. JOB EXPIRATION 
The public Organization documentation does not currently establish a universal job-
expiration period. 
Therefore, the chatbot should not state: 
“Jobs automatically expire after 30 days.” 
or any other fixed duration unless confirmed. 
If a job listing contains a closing date, the chatbot can report that date. 
 

30. JOB EDITING 
The public Organization documentation does not sufficiently document the exact process 
for editing a posted job. 
Therefore, the chatbot should not invent: 
Jobs → three dots → Edit 
or another specific workflow. 
If the current Organization dashboard exposes an Edit action, the chatbot can guide the 
user based on the live UI/API. 
 
31. JOB DELETION / CLOSING 
Likewise, the public documentation does not sufficiently document the exact workflow for: 
• 
deleting a job  
• 
closing a job  
• 
pausing a job  
• 
reopening a job  
Therefore, these actions should be handled using the actual current Organization controls 
rather than invented instructions. 
 
32. JOB VISIBILITY 
Organization Jobs are visible through the Organization's Jobs section in the supplied UI. 
However, the public documentation does not provide a complete specification of: 
• 
public/private jobs  
• 
follower-only jobs  
• 
employee-only jobs  
• 
department-only jobs  
• 
scheduled jobs  
• 
hidden jobs  

Therefore, the chatbot must not invent these visibility states. 
 
33. JOBS AND ORGANIZATION PERMISSIONS 
The previous Organization Permissions document is directly relevant here. 
Job management may require Organization-level access. 
However, the exact permission mapping is not publicly documented. 
For example, the chatbot should not assume: 
“Only Organization Admins can create jobs.” 
unless the actual WiseIN permission system confirms this. 
Instead: 
“WiseIN provides Organization hiring and job-posting tools. The exact permission required 
to create or manage a job depends on the Organization's current access configuration.” 
 
34. JOBS AND ORGANIZATION EMPLOYEES 
Organization employees and job applicants are different. 
Employee 
A person connected with the Organization. 
Job Applicant 
A person applying for a job opportunity. 
Job Seeker 
A professional searching for opportunities. 
Recruiter / Hiring User 
A person using Organization hiring functionality. 
These roles should not be automatically merged. 
 
35. JOB CONTENT POLICY 

Every Organization job must follow WiseIN's Content Policies. 
Important requirements include: 
Genuine opportunity 
Jobs must be real. 
Honest terms 
Unpaid, equity-only, and part-time conditions must be disclosed. 
No scams 
No pyramid schemes, MLM, or pay-to-get-a-job schemes. 
No fake companies 
Users must not impersonate companies or falsely represent an organization. 
No fake credentials 
Job-related claims should not rely on fabricated credentials. 
 
36. JOB PRIVACY 
WiseIN's Content Policies prohibit posting other people's personal information without 
permission. 
This includes: 
• 
Phone number  
• 
Email  
• 
Address  
• 
Personal details  
The policy also prohibits publicly sharing sensitive information such as: 
• 
Financial data  
• 
ID proofs  
• 
Salary details  
• 
Internal company information  

• 
Business strategies  
without appropriate authorization.  
Therefore, job listings should not expose unnecessary private information. 
 
37. JOB SCAM REPORTING 
WiseIN allows users to report job listings that violate its policies. 
Its Content Policies explicitly list job listings among reportable content.  
The policy states that reports are confidential and that WiseIN reviews reports within 24 
hours.  
The chatbot can therefore guide users who encounter suspicious jobs toward WiseIN's 
reporting mechanism. 
 
38. WHAT TO DO IF A JOB LOOKS FAKE 
Recommended chatbot response: 
“If you believe a WiseIN job listing is fake, misleading, or violates WiseIN's job policies, 
report the job listing through the available reporting option. WiseIN's Content Policies 
require jobs and internships to be genuine and prohibit scam offers, fake opportunities, 
MLM/pyramid schemes, and pay-to-get-a-job scams.”  
 
39. JOB MODERATION 
WiseIN's Content Policies establish enforcement for policy violations. 
For minor violations, the stated progression can include: 
1. Content removal + warning  
2. Temporary feature restriction  
3. Account review  
Serious violations can receive immediate action, while severe violations such as 
fraud/scams, identity fraud, data theft, or posting private information can result in 
permanent bans.  

The chatbot should not promise a particular moderation outcome for an individual report. 
 
40. JOBS AND EMPLOYER BRANDING 
WiseIN's Organization plan includes: 
• 
Employer branding features  
• 
Showcase Organization culture  
• 
Organization profile  
• 
Hiring and recruitment tools  
The homepage explicitly lists Showcase Organization Culture and Employer Branding 
Features under Organization Hiring & Recruitment.  
This means Organization Jobs can be part of a broader employer presence rather than 
functioning as isolated listings. 
 
41. JOBS AND VERIFIED TALENT 
WiseIN positions Organization hiring around access to verified talent. 
The Organization offering includes: 
Access Verified Talent 
and the Organization page describes verified employee profiles and role-based employee 
discovery.  
Therefore, the chatbot should understand two related recruitment workflows: 
Organization 
    │ 
    ├── Publish Jobs 
    │       ↓ 
    │   Attract Applicants 
    │ 
    └── Discover Verified Talent 

            ↓ 
        Find Professionals 
These should not be presented as the same feature. 
 
42. ORGANIZATION JOBS AND SEARCH 
The supplied UI demonstrates that an Organization's Jobs section can include a search 
field. 
The chatbot should recognize variations such as: 
Search Jobs 
Find Jobs 
Find Openings 
Search Open Positions 
Look for Opportunities 
Find Vacancies 
as related job-search intents. 
 
43. SAMPLE JOB-RELATED CHATBOT ANSWERS 
Q: Where can I find an Organization's jobs? 
Open the Organization's profile and go to its Jobs section. The Organization Jobs page can 
display current openings and includes a job search field in the current UI. 
 
Q: Does every Organization have jobs? 
An Organization can have a Jobs section, but that does not mean it currently has an open 
position. If there are no active openings, WiseIN can show an empty state indicating that 
open positions and career opportunities will appear once posted. 
 
Q: Can Organizations post internships? 

Yes. WiseIN's Organization offering explicitly includes Publish Jobs & Internship 
Opportunities.  
 
Q: Can Organizations post part-time jobs? 
Part-time opportunities can be listed. The supplied WiseIN Organization UI shows a “Part-
Time / Freelance” opportunity, and WiseIN's Content Policies require part-time status to be 
disclosed honestly.  
 
Q: Can Organizations post remote jobs? 
Remote opportunities can be represented in Organization job listings; the supplied WiseIN 
UI shows a job marked “Remote.” The work arrangement should always be taken from the 
individual listing. 
 
Q: Can Organizations hire through WiseIN? 
Yes. WiseIN's Organization offering includes hiring and recruitment capabilities, including 
publishing jobs and internships, accessing verified talent, and hiring/recruitment tools.  
 
Q: Are WiseIN Organization jobs genuine? 
WiseIN's Content Policies require every job, gig, internship, and opportunity posted on the 
platform to be genuine and prohibit fake jobs, scam offers, MLM/pyramid schemes, and 
pay-to-get-a-job schemes.  
Important: this policy requirement should not be converted into a guarantee that every 
individual listing is suitable or that an applicant will receive a job. 
 
44. AI INTENTS 
Recommended intent classification: 
organization_jobs_overview 
organization_job_listing 
organization_job_search 

organization_job_details 
organization_job_openings 
organization_job_internship 
organization_job_full_time 
organization_job_part_time 
organization_job_freelance 
organization_job_remote 
organization_job_location 
organization_job_compensation 
organization_job_requirements 
organization_job_application 
organization_job_application_status 
organization_job_deadline 
organization_job_edit 
organization_job_delete 
organization_job_close 
organization_job_visibility 
organization_job_permissions 
organization_job_hiring 
organization_job_recruitment 
organization_job_verified_talent 
organization_job_scam 
organization_job_report 
organization_job_policy 
organization_job_troubleshooting 
 

45. AI ENTITIES 
organization 
organization_id 
organization_name 
 
job 
job_id 
job_title 
job_description 
job_type 
employment_type 
work_arrangement 
location 
remote_status 
salary 
compensation 
currency 
experience 
skills 
qualifications 
responsibilities 
job_status 
posting_date 
closing_date 
 
internship 

freelance 
part_time 
full_time 
 
applicant 
application 
application_status 
 
recruiter 
hiring_manager 
department 
team 
 
job_visibility 
job_permission 
report 
policy_violation 
 
46. RAG METADATA 
document_id: 
WISEIN-ORGANIZATION-JOBS-001 
 
title: 
WiseIN Organization Jobs Knowledge Base Dataset 
 
category: 

Organization 
 
subcategory: 
Jobs & Hiring 
 
topics: 
organization jobs 
job listings 
job posting 
internships 
hiring 
recruitment 
verified talent 
remote jobs 
part-time jobs 
freelance jobs 
job search 
job applications 
job reporting 
job safety 
job content policies 
employer branding 
 
primary_sources: 
https://www.wisein.in/teams 
https://www.wisein.in/ 

https://www.wisein.in/pricing 
https://www.wisein.in/content-policies 
 
source_type: 
official website + supplied product UI 
 
requires_live_api: 
yes 
 
live_data_required_for: 
current jobs 
current openings 
job status 
posting date 
application status 
current job details 
organization-specific vacancies 
 
confidence: 
high for documented capabilities 
limited for undocumented workflows 
 
47. CHATBOT GUARDRAILS 
Guardrail 1 — Never invent a job 
Only report jobs returned by the current WiseIN job data or explicitly supplied by the user. 
Guardrail 2 — Do not claim a job is still open from an old screenshot 

A screenshot is evidence of the UI at that time, not proof of current availability. 
Guardrail 3 — Preserve employment type 
Do not convert: 
• 
Part-time → Full-time  
• 
Freelance → Full-time  
• 
Unpaid → Paid  
• 
Equity-only → Salaried  
Guardrail 4 — Preserve compensation information 
Never hide or alter compensation conditions. 
Guardrail 5 — Do not guarantee employment 
A WiseIN job listing does not mean the user will be hired. 
Guardrail 6 — Do not invent application workflows 
Use the current job page/API for application instructions. 
Guardrail 7 — Do not invent application statuses 
Only report statuses actually provided by WiseIN. 
Guardrail 8 — Protect personal information 
Do not expose private recruiter, employee, or applicant information. 
Guardrail 9 — Treat suspicious jobs carefully 
Direct users toward WiseIN reporting mechanisms rather than endorsing suspicious 
opportunities. 
Guardrail 10 — Do not infer permission levels 
The chatbot should not assume who can post/manage jobs based only on job title or 
employee status. 
 
48. CURRENTLY CONFIRMED 
Based on the current official WiseIN website and supplied UI evidence, the following can 
be treated as supported: 

• 
Organizations can publish jobs and internship opportunities.  
• 
WiseIN provides hiring and recruitment tools for Organizations.  
• 
Organizations can access verified talent.  
• 
Organization profiles have a Jobs section, as shown in the supplied UI.  
• 
Organization Jobs can be searched, as shown in the supplied UI.  
• 
Job listings can display work arrangement and employment type, as shown in the 
supplied UI.  
• 
A current UI example shows a Remote, Part-Time/Freelance opportunity.  
• 
An Organization can have no current openings, as shown by the supplied empty-
state UI.  
• 
WiseIN requires jobs, gigs, internships, and opportunities to be genuine.  
• 
Unpaid, equity-only, and part-time conditions must be disclosed honestly.  
• 
Scam job offers, MLM/pyramid schemes, and pay-to-get-a-job offers are prohibited.  
• 
Job listings can be reported.  
• 
Organization hiring is part of the Organization plan.  
 
49. DETAILS NOT CURRENTLY CONFIRMED 
Do not add these as fixed WiseIN facts without further application/internal documentation: 
• 
Exact job-post creation form  
• 
Required job-post fields  
• 
Maximum job description length  
• 
Maximum number of active jobs  
• 
Job posting fee per listing  
• 
Exact application form  
• 
Resume file-size limit  
• 
Resume file-format limit  
• 
Automatic resume parsing  

• 
Applicant tracking stages  
• 
Automatic recruiter notifications  
• 
Job expiration period  
• 
Automatic job closure  
• 
Job editing workflow  
• 
Job deletion workflow  
• 
Job pause/reopen workflow  
• 
Exact job visibility levels  
• 
Job scheduling  
• 
Salary range validation  
• 
Automatic salary normalization  
• 
Guaranteed applicant verification  
• 
Guaranteed employer response  
• 
Exact job-search filters beyond those actually visible/documented  
• 
Exact job recommendation algorithm  
• 
Exact ranking algorithm  
• 
Exact job permission roles  
• 
Exact recruiter permission roles  
• 
Exact hiring-manager permission roles  
 
50. RECOMMENDED CHATBOT DATA FLOW 
For a question such as: 
“Show me remote developer jobs from this Organization.” 
The chatbot architecture should work approximately as: 
User 
 ↓ 

Chat UI 
 ↓ 
Chat API 
 ↓ 
Authenticate User 
 ↓ 
Identify Organization 
 ↓ 
Authorized Job API 
 ↓ 
Retrieve current jobs 
 ↓ 
Filter: 
   Organization 
   + Developer 
   + Remote 
 ↓ 
RAG 
 ↓ 
Explain job fields/policies if needed 
 ↓ 
LLM 
 ↓ 
Answer 
The RAG database should not be used as the source of truth for current job openings. 
 

51. FINAL KNOWLEDGE MODEL 
The Organization Jobs feature can be represented as: 
WISEIN ORGANIZATION 
        │ 
        ├── Organization Profile 
        │ 
        ├── Jobs 
        │     │ 
        │     ├── Open Positions 
        │     ├── Internships 
        │     ├── Part-Time Opportunities 
        │     ├── Freelance Opportunities 
        │     └── Remote Opportunities 
        │ 
        ├── People 
        │     └── Employee / Professional Directory 
        │ 
        ├── Hiring & Recruitment 
        │     ├── Publish Jobs 
        │     ├── Publish Internships 
        │     └── Access Verified Talent 
        │ 
        └── Employer Branding 
              ├── Organization Profile 
              └── Organization Culture 

The most important distinction for the chatbot is: 
Organization Jobs are current hiring opportunities published by Organizations, while 
Organization People represents people associated with the Organization. 
 
52. MOST IMPORTANT CHATBOT RULE 
For Organization Jobs: 
RAG explains the Jobs feature and its rules. 
The live WiseIN job API provides current job listings. 
The backend authorization layer determines who can create, edit, manage, or access 
restricted job information. 
This prevents the chatbot from answering outdated job questions from static 
documentation or screenshots. 
 
 



---

