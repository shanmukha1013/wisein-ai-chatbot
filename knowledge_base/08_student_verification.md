# Student Verification

## Source: WISEIN – STUDENT VERIFICATION DOCUMENTATION-008.pdf

WISEIN – STUDENT VERIFICATION DOCUMENTATION 
Document ID: WISEIN-STUDENT-VERIFY-008 
Document Type: Product Knowledge Base, Troubleshooting & AI Chatbot Training 
Reference 
Version: 1.0 
Organization: Sanshi Network Tech Pvt. Ltd. 
Platform: WiseIN 
Primary Feature: Student Verification 
Primary User Types: Students and fresh graduates 
Primary Trigger Queries: 
“Student verification”, “How do I verify as a student?”, “How to get student badge?”, “Verify 
college ID”, “Student ID verification”, “College ID + Aadhaar”, “Student verification failed”, 
“Why is my student verification pending?”, “Student plan”, “How can I verify my college?”, 
“Student badge not showing”, “College email verification”, “DigiLocker student verification” 
1. DOCUMENT PURPOSE 
This document defines the knowledge that the WiseIN AI chatbot should have about 
Student Verification. 
The chatbot should be able to: 
• 
Explain what Student Verification means.  
• 
Explain why WiseIN verifies students.  
• 
Explain the currently published student-verification requirements.  
• 
Guide students through the verification process.  
• 
Explain the Student Badge.  
• 
Explain the relationship between government identity verification and student 
verification.  
• 
Help users understand supported student verification information/documents.  
• 
Troubleshoot common verification problems.  
• 
Explain Student Plan eligibility and related features.  
• 
Distinguish Student Verification from email verification and government identity 
verification.  

• 
Protect sensitive identity and verification information.  
• 
Escalate cases that require human or engineering support.  
• 
Avoid inventing verification methods, processing times, OTP limits, document 
requirements, or benefits that are not confirmed by WiseIN.  
 
2. WHAT IS STUDENT VERIFICATION? 
Student Verification is WiseIN's process for establishing that a member qualifies as a 
student or recent graduate for WiseIN's student-focused features and services. 
The current WiseIN website specifically describes the Student plan as being for verified 
students and fresh graduates. 
For the India version of the Student plan, the published requirement is: 
Student Verification – College ID + Aadhaar 
The public WiseIN pricing page also lists the Student Badge on the user's profile and 
student-oriented features such as the internship/job board, campus communities, student 
networking events, and early access to student opportunities.  
The exact verification screens, backend workflow, document-review rules, and failure 
messages should be treated as implementation details and verified against the current 
WiseIN application before being presented as guaranteed behavior. 
 
3. WHY DOES WISEIN VERIFY STUDENTS? 
Student verification supports WiseIN's broader goal of maintaining a trusted network. 
WiseIN publicly describes itself as a verified professional network and emphasizes 
government-backed identity verification. Its website states that members can be verified 
through Aadhaar, PAN, or DigiLocker.  
For student users, verification can help WiseIN distinguish genuine student accounts from 
accounts that only claim to be students. 
Student verification can therefore support: 
• 
Trust between students and other members.  
• 
Student-specific platform access.  

• 
Student profile identification.  
• 
Student communities.  
• 
Student networking events.  
• 
Internship and job discovery.  
• 
Access to student-oriented opportunities.  
• 
Eligibility for the WiseIN Student plan.  
The AI should not claim that verification guarantees an internship, job, mentor, interview, 
admission, or selection. 
 
4. STUDENT VERIFICATION VS OTHER TYPES OF VERIFICATION 
The chatbot must understand that these concepts are related but not identical. 
4.1 Email Verification 
Email verification confirms access to an email address associated with an account. 
It does not automatically prove that the user is a student. 
A user can have a verified email without having a verified student status. 
 
4.2 Government Identity Verification 
Government identity verification establishes the user's identity. 
WiseIN's public website describes government verification through methods including 
Aadhaar, PAN, and DigiLocker.  
Government identity verification should not automatically be described as proof of current 
student enrollment. 
 
4.3 Student Verification 
Student verification establishes eligibility for WiseIN's student-specific experience. 
For the current India Student plan, WiseIN publicly specifies: 
College ID + Aadhaar 

The chatbot should therefore distinguish: 
Identity verification = Who you are 
from: 
Student verification = Whether you qualify for the student experience 
 
4.4 Student Badge 
The Student Badge is the profile indication associated with verified student status. 
The current WiseIN pricing page explicitly lists: 
Student Badge on Profile 
under the Student plan.  
The chatbot must not assume a particular badge color, icon, animation, or exact UI 
location unless that detail is confirmed in the current application. 
 
5. CURRENTLY PUBLISHED STUDENT PLAN INFORMATION 
The public WiseIN website currently describes the Student plan as: 
WiseIN Student – Learn, Connect & Launch Your Career 
It is intended for: 
• 
Students  
• 
Fresh graduates  
• 
People preparing for their next career move  
The published India pricing page currently shows the Student plan at ₹199/month. 
The listed Student plan features include: 
• 
Student Verification using College ID + Aadhaar.  
• 
Student Badge on Profile.  
• 
Internship & Job Board Access.  
• 
Campus Communities.  

• 
Student Networking Events.  
• 
Early Access to Student Opportunities.  
The pricing page also presents a global verification route as: 
College Email + Sumsub 
The AI must distinguish the India and global routes and should not tell an Indian user that 
the global workflow is automatically applicable to them.  
Important: Pricing, eligibility, features, and verification requirements may change. The 
chatbot should use the latest approved product documentation rather than hard-code old 
pricing or benefits. 
 
6. STUDENT VERIFICATION ELIGIBILITY 
The chatbot should first determine what the user means by “student.” 
Possible user categories include: 
• 
Current college/university student.  
• 
Undergraduate student.  
• 
Postgraduate student.  
• 
Diploma student.  
• 
Other formally enrolled student.  
• 
Fresh graduate.  
The current public website explicitly describes the Student plan as being for verified 
students and fresh graduates.  
However, the public website does not provide a complete authoritative list of every eligible 
degree type, institution type, age category, or graduation-year rule. 
Therefore, the chatbot should not invent eligibility rules. 
If eligibility is unclear, the chatbot should direct the user to the current Student Verification 
flow or human support. 
 
7. INDIA STUDENT VERIFICATION 

For users using the India version of WiseIN's Student plan, the currently published 
requirement is: 
College ID + Aadhaar 
This means the user should be prepared to provide the required college/student 
identification and complete the applicable Aadhaar-based verification process through the 
official WiseIN verification flow.  
The chatbot should not request the user's Aadhaar number, Aadhaar OTP, password, 
biometric information, or student ID image inside the chat. 
Instead, it should direct the user to the secure WiseIN verification interface. 
 
8. GLOBAL STUDENT VERIFICATION 
The public WiseIN pricing page currently describes the global Student plan verification 
method as: 
College Email + Sumsub 
This is different from the India Student plan requirement. 
Therefore, when a user is outside India, the chatbot should avoid automatically instructing 
them to complete Aadhaar verification. 
The chatbot should identify the user's applicable region and then provide the currently 
approved workflow. 
If the region cannot be determined, the chatbot should explain that verification 
requirements can differ by region and direct the user to the Student Verification flow. 
 
9. BASIC STUDENT VERIFICATION WORKFLOW 
The chatbot can explain the process at a high level as follows: 
Step 1 – Create or access a WiseIN account 
The user must have a WiseIN account. 
WiseIN's public registration page asks users for a username and email address and states 
that an email verification step follows registration.  
 

Step 2 – Complete required identity verification 
For the India student experience, Aadhaar is part of the published Student Verification 
requirement. 
The exact current screen and sequence should be followed inside WiseIN. 
 
Step 3 – Provide college/student verification information 
The user completes the Student Verification process and provides the required 
college/student credential. 
For India, the publicly stated requirement is: 
College ID + Aadhaar. 
 
Step 4 – Submit the verification 
The user submits the verification through the official WiseIN interface. 
 
Step 5 – Verification result 
Depending on the current implementation, the account may be: 
• 
Verified.  
• 
Pending review.  
• 
Asked to provide additional information.  
• 
Rejected.  
• 
Unable to complete verification because of a technical or verification issue.  
The chatbot should use the actual status shown by the application when available. 
 
Step 6 – Student status/profile 
Once the verification is successfully completed, the applicable Student Badge and 
Student-plan features should become available according to the current WiseIN 
implementation. 

The public pricing page confirms the Student Badge as a Student-plan feature.  
 
10. COLLEGE ID 
A College ID is an institutional identification document issued to a student by their college 
or university. 
It may typically contain information such as: 
• 
Student name.  
• 
Institution name.  
• 
Student/roll/registration number.  
• 
Photograph.  
• 
Academic information.  
• 
Validity information.  
However, WiseIN's public website does not currently publish a complete specification of 
exactly which fields must appear on the College ID. 
Therefore, the chatbot must not claim that every listed field is mandatory unless the 
application or approved internal documentation confirms it. 
 
11. AADHAAR AND STUDENT VERIFICATION 
Aadhaar is an important part of the published India Student Verification requirement. 
WiseIN's privacy policy states that Aadhaar information is collected for identity verification 
and describes security controls around the information. It states that WiseIN stores certain 
Aadhaar-related information, including the last four digits, name, date of birth, gender, 
address, and photograph, while stating that the full 12-digit Aadhaar number, Aadhaar PIN, 
biometric data, and verification OTP are not stored.  
The AI must therefore follow strict security rules. 
Never ask users to provide: 
• 
Full Aadhaar number.  
• 
Aadhaar OTP.  

• 
Aadhaar PIN.  
• 
Biometric information.  
• 
Password.  
• 
Authentication token.  
• 
Session token.  
The user should complete identity verification only through the official secure WiseIN 
workflow. 
 
12. DIGILOCKER 
DigiLocker is part of WiseIN's broader government-backed identity verification ecosystem. 
WiseIN publicly states that DigiLocker integration was launched for secure document 
verification and that users can use official government-backed digital documents for 
verification.  
However, the current public Student Plan pricing page specifically identifies the India 
Student Verification requirement as: 
College ID + Aadhaar 
Therefore, the chatbot should not automatically tell every student that an ABC ID, 
marksheet, or DigiLocker academic record is a currently supported Student Verification 
method unless the current application or approved product documentation confirms it. 
This is an important correction to the supplied draft: ABC ID/DigiLocker academic 
verification should be treated as an implementation item requiring confirmation, not 
as a guaranteed current Student Verification method. 
 
13. ABC ID 
ABC ID means Academic Bank of Credits ID. 
The supplied reference document proposes ABC ID/DigiLocker as a student verification 
method. 
However, the currently accessible public WiseIN website does not provide sufficient detail 
to verify that ABC ID is currently an official Student Verification option. 

Therefore: 
The chatbot should not promise ABC ID verification unless the live WiseIN product or 
approved internal documentation confirms that the feature is currently enabled. 
If the application displays an ABC/DigiLocker academic verification option, the chatbot 
may explain that option using the current approved product documentation. 
 
14. COLLEGE EMAIL VERIFICATION 
The supplied reference describes college email OTP verification. 
However, the current public WiseIN Student Plan information specifies: 
India: College ID + Aadhaar 
Global: College Email + Sumsub 
Therefore, the chatbot should not present “college email OTP” as the universal India 
Student Verification method. 
College email verification may be relevant to certain regions or product implementations, 
but the exact current workflow must be confirmed. 
This distinction is important because the chatbot must not give users an outdated 
verification procedure. 
 
15. STUDENT VERIFICATION STATUS 
The AI should recognize the following possible conceptual states: 
Not Started 
The user has not initiated Student Verification. 
In Progress 
The user has started the verification process but has not completed it. 
Pending 
The submitted information requires processing or review. 
Verified 
The Student Verification process has successfully completed. 

Failed 
The verification could not be completed. 
Rejected 
The submitted information did not satisfy the applicable verification requirements. 
Technical Error 
The verification could not complete because of a technical/system problem. 
The exact status names should be taken from the live application if available. 
 
16. STUDENT BADGE 
The Student Badge indicates that the account has qualified for the applicable WiseIN 
student status. 
The public WiseIN Student plan specifically lists: 
Student Badge on Profile.  
A chatbot response should therefore say: 
“Once your Student Verification is successfully completed, your applicable student status 
and Student Badge should be reflected according to the current WiseIN account and plan.” 
The AI should not guarantee the exact time at which a badge appears unless that behavior 
is documented. 
 
17. STUDENT VERIFICATION FAILED 
If a user says: 
“My student verification failed.” 
The chatbot should first identify why it failed. 
Possible categories include: 
• 
College ID problem.  
• 
Identity mismatch.  
• 
Invalid or unsupported document.  

• 
Verification provider error.  
• 
Technical error.  
• 
Incomplete submission.  
• 
Account information mismatch.  
• 
Region-specific verification issue.  
• 
Verification service unavailable.  
The chatbot should not automatically claim that the failure was caused by a particular 
reason. 
 
18. COLLEGE ID REJECTED 
If the application rejects a College ID, the chatbot should advise the user to: 
1. Check that the document belongs to them.  
2. Ensure the document is readable.  
3. Ensure the submitted information matches the WiseIN account.  
4. Check that the institution information is correct.  
5. Follow the exact re-upload or retry instructions shown by WiseIN.  
6. If the issue continues, contact WiseIN support.  
The chatbot should not invent an exact number of retries or a guaranteed review time. 
 
19. BLURRY COLLEGE ID 
If the user says: 
“My college ID is blurry.” 
Recommended response: 
“Please make sure the College ID image is clear and readable, with the important student 
and institution details visible. Use the Student Verification section in WiseIN to submit the 
document again. If the application continues to reject it, contact WiseIN support.” 
The AI should not ask the user to upload the ID into the chatbot. 

 
20. COLLEGE ID EXPIRED 
If the user says: 
“My college ID is expired.” 
The AI should not automatically assume that an expired card is accepted or rejected. 
Instead: 
“If your College ID is expired, check the current Student Verification requirements shown in 
WiseIN. If the application rejects the document, use another currently accepted 
verification option if the platform provides one, or contact support.” 
The exact accepted alternatives must come from the current product implementation. 
21. NAME MISMATCH 
A name mismatch can occur when: 
• 
WiseIN account name differs from identity document.  
• 
College ID uses a shortened name.  
• 
College ID uses initials.  
• 
Government identity uses a different spelling.  
• 
Typographical errors exist.  
The chatbot should explain that identity information should be accurate and consistent. 
WiseIN's Terms state that users must provide accurate, complete, and up-to-date 
information and that WiseIN may verify identity using government-issued IDs, official email 
domains, or other authentication methods.  
The chatbot should not tell the user to manipulate or alter official documents. 
 
22. WRONG STUDENT INFORMATION 
If the user entered incorrect information such as: 
• 
Institution.  
• 
Course.  

• 
Student number.  
• 
Graduation information.  
The chatbot should direct them to the appropriate profile/verification editing flow if the 
current application provides one. 
If the information cannot be changed after submission, the chatbot should direct the user 
to support. 
It should never advise the user to submit false information. 
 
23. COLLEGE OR UNIVERSITY NOT FOUND 
If a user says: 
“My college is not available.” 
The chatbot should: 
1. Ask the user to check whether they are searching using the institution's official 
name.  
2. Check whether the application provides an “Other,” “Not Listed,” or similar option.  
3. If such an option exists, guide the user through it.  
4. If there is no such option, direct them to WiseIN support.  
The AI should not promise that WiseIN will add the institution within 24 hours unless 
that SLA is confirmed by the product/support team. 
 
24. STUDENT VERIFICATION STILL PENDING 
If a user says: 
“My student verification is pending.” 
The chatbot should explain: 
“Your verification may still be processing or awaiting review. Please check the verification 
status shown in your WiseIN account. If the status remains pending beyond the officially 
documented processing period, contact WiseIN support.” 
Do not invent a 12-hour, 24-hour, 48-hour, or other processing guarantee. 

 
25. STUDENT BADGE NOT SHOWING 
If the user says: 
“I completed verification but my Student Badge is not showing.” 
The chatbot should: 
1. Confirm that the application reports verification as successful.  
2. Ask the user to refresh/reopen the profile if appropriate.  
3. Check whether the Student plan/status has been activated.  
4. Ask the user to check the verification status again.  
5. If the verification says successful but the badge remains missing, treat this as a 
possible account-status synchronization issue.  
6. Escalate to support if it persists.  
The chatbot should not claim that the badge is manually added unless that is confirmed. 
 
26. STUDENT VERIFICATION AND STUDENT PLAN 
Student Verification is related to WiseIN's Student plan. 
The current public website lists the Student plan at ₹199/month in India and describes it for 
verified students and fresh graduates.  
Published Student plan features include: 
• 
Student Badge.  
• 
Internship & Job Board Access.  
• 
Campus Communities.  
• 
Student Networking Events.  
• 
Early Access to Student Opportunities.  
The chatbot should always use current pricing rather than permanently storing a fixed price 
in its response logic. 
 

27. STUDENT VERIFICATION AND INTERNSHIPS 
A Verified Student may have access to WiseIN's student-oriented job and internship 
features according to the applicable plan. 
The website currently lists Internship & Job Board Access under the Student plan.  
However: 
Student verification does not guarantee an internship, interview, recruiter response, or job 
offer. 
The AI must never promise employment. 
 
28. STUDENT VERIFICATION AND MENTORING 
The current public Student plan information mentions access to student-oriented 
networking and career features. The older supplied reference additionally mentions mentor 
sessions. 
The chatbot may describe mentor-related access only when the current user's 
plan/product UI confirms it. 
It should not guarantee: 
• 
A mentor match.  
• 
A specific mentor.  
• 
A free mentor call.  
• 
A successful mentorship outcome.  
 
29. STUDENT VERIFICATION AND CAMPUS COMMUNITIES 
The current WiseIN Student plan lists: 
Campus Communities 
as a Student feature.  
The chatbot can explain this as student-oriented community access. 
It should not claim that every college has a WiseIN campus community. 

 
30. STUDENT NETWORKING EVENTS 
The current Student plan lists: 
Student Networking Events 
as a Student feature.  
The AI can explain that verified/student-plan users may receive access to applicable 
student networking opportunities. 
Event availability can change. 
31. EARLY ACCESS TO STUDENT OPPORTUNITIES 
The current public Student plan lists: 
Early Access to Student Opportunities.  
The AI should explain this as a platform feature and must not interpret “early access” as a 
guarantee of selection. 
 
32. COMMON USER QUESTIONS 
“How do I get student verified?” 
Answer: 
“For the India Student experience, WiseIN currently lists Student Verification using College 
ID + Aadhaar. Start the Student Verification process from your WiseIN account and follow 
the verification instructions shown there. Once successfully verified, the applicable 
Student Badge and Student-plan features can become available.” 
 
“How do I get the Student Badge?” 
“The Student Badge is associated with WiseIN's Student plan. Complete the applicable 
Student Verification process first. For India, WiseIN currently lists College ID + Aadhaar as 
the Student Verification requirement.” 
 
“Can I verify with my college ID?” 

“Yes. WiseIN currently lists a valid College ID as part of Student Verification for the India 
Student plan. Complete the process through the official WiseIN verification flow.” 
 
“Can I verify with Aadhaar?” 
“For the India Student plan, WiseIN currently lists College ID + Aadhaar as the Student 
Verification requirement. Please complete Aadhaar verification only through the official 
WiseIN verification flow.” 
 
“Can I use my college email?” 
“WiseIN's currently published Student Verification requirements differ by region. The India 
Student plan lists College ID + Aadhaar, while the global listing mentions College Email + 
Sumsub. Please follow the verification method shown for your account and region.” 
 
“My student verification failed.” 
“Please check the exact error shown in WiseIN and verify that your submitted information 
and College ID are correct and readable. If the verification continues to fail, contact WiseIN 
support so the team can check the account-specific issue.” 
 
33. STUDENT VERIFICATION SECURITY 
Student Verification involves sensitive personal information. 
The AI must follow these rules. 
The AI MUST NOT request: 
• 
Password.  
• 
Aadhaar OTP.  
• 
Aadhaar PIN.  
• 
Full Aadhaar number.  
• 
Biometric information.  
• 
Authentication tokens.  

• 
Session tokens.  
• 
Private API keys.  
• 
Verification-provider credentials.  
• 
Payment credentials.  
WiseIN's privacy policy specifically states that it does not store the full 12-digit Aadhaar 
number, Aadhaar PIN, biometric data, or Aadhaar verification OTP.  
 
34. DO NOT UPLOAD DOCUMENTS INTO CHAT 
The chatbot should not ask the student to upload their College ID, Aadhaar, marksheet, 
passport, or other identity document directly into a normal AI chat conversation. 
Instead: 
“Please complete document submission through the official WiseIN Student Verification 
flow.” 
This keeps sensitive verification information inside the intended secure verification 
process. 
 
35. AI MUST NOT CLAIM TO VERIFY THE USER 
The chatbot cannot independently decide: 
“You are definitely a verified student.” 
unless it has access to an authorized WiseIN backend verification status. 
The chatbot should distinguish between: 
Knowledge-based answer 
and 
Real-time account status. 
Correct: 
“According to WiseIN's Student plan requirements, College ID + Aadhaar are currently 
listed for India.” 

Incorrect: 
“I checked your account and you are verified.” 
unless an authorized backend tool actually performed that check. 
 
36. AI REAL-TIME ACCOUNT CHECKING 
If WiseIN later provides an authorized Student Verification API/tool, the chatbot may use it 
to retrieve information such as: 
• 
Student verification status.  
• 
Verification stage.  
• 
Student badge status.  
• 
Verification failure reason.  
• 
Student plan status.  
The backend must enforce authorization so one user cannot access another user's 
verification information. 
 
37. TROUBLESHOOTING DECISION FLOW 
The chatbot should follow this sequence: 
Step 1 – Identify the user's problem 
Is the user asking about: 
• 
How to verify?  
• 
Eligibility?  
• 
College ID?  
• 
Aadhaar?  
• 
College email?  
• 
DigiLocker?  
• 
Verification failure?  
• 
Pending verification?  

• 
Badge missing?  
• 
Student plan?  
• 
Internship access?  
Step 2 – Identify region 
Determine whether the user is using: 
• 
India Student flow.  
• 
Global Student flow.  
Step 3 – Identify verification status 
Determine whether the user is: 
• 
Not started.  
• 
In progress.  
• 
Pending.  
• 
Verified.  
• 
Failed.  
• 
Rejected.  
• 
Experiencing a technical problem.  
Step 4 – Provide verified guidance 
Use only the current approved WiseIN documentation. 
Step 5 – Protect sensitive information 
Never ask for passwords, OTPs, Aadhaar PINs, biometric data, or private credentials. 
Step 6 – Escalate when necessary 
If the problem requires account-specific investigation, send the user to WiseIN support. 
 
38. STUDENT VERIFICATION AI INTENTS 
The RAG system should classify Student Verification questions into clear intents. 
Recommended intents: 

STUDENT_VERIFICATION_GENERAL 
General questions about student verification. 
STUDENT_VERIFICATION_ELIGIBILITY 
Questions about who can become a verified student. 
STUDENT_VERIFICATION_START 
How to start verification. 
STUDENT_VERIFICATION_INDIA 
India-specific College ID + Aadhaar workflow. 
STUDENT_VERIFICATION_GLOBAL 
Global College Email + Sumsub workflow. 
STUDENT_COLLEGE_ID 
Questions about College ID. 
STUDENT_COLLEGE_ID_REJECTED 
Rejected or invalid College ID. 
STUDENT_COLLEGE_ID_UNREADABLE 
Blurry, cropped, unclear, or unreadable ID. 
STUDENT_AADHAAR 
Questions about Aadhaar requirements. 
STUDENT_COLLEGE_EMAIL 
Questions about institutional email verification. 
STUDENT_DIGILOCKER 
Questions about DigiLocker. 
STUDENT_ABC_ID 
Questions about ABC ID. 
STUDENT_VERIFICATION_PENDING 
Verification remains pending. 

STUDENT_VERIFICATION_FAILED 
Verification failure. 
STUDENT_VERIFICATION_REJECTED 
Verification rejection. 
STUDENT_NAME_MISMATCH 
Name mismatch between account and documents. 
STUDENT_INSTITUTION_NOT_FOUND 
College/university is not listed. 
STUDENT_BADGE 
Questions about Student Badge. 
STUDENT_BADGE_MISSING 
Verification completed but badge is missing. 
STUDENT_PLAN 
Questions about the Student plan. 
STUDENT_INTERNSHIPS 
Student job/internship access. 
STUDENT_COMMUNITIES 
Campus community access. 
STUDENT_EVENTS 
Student networking events. 
STUDENT_SECURITY 
Security and privacy questions. 
STUDENT_ESCALATION 
Problems requiring human support. 
 
39. ENTITY EXTRACTION 

The chatbot should identify entities such as: 
Institution 
Examples: 
• 
College.  
• 
University.  
• 
Institute.  
• 
Campus.  
Course 
Examples: 
• 
B.Tech.  
• 
MBA.  
• 
B.Sc.  
• 
M.Tech.  
• 
Diploma.  
Student Identifier 
Examples: 
• 
College ID.  
• 
Roll number.  
• 
Registration number.  
Graduation Information 
Examples: 
• 
Graduation year.  
• 
Expected graduation.  
• 
Batch.  
Verification Method 
Examples: 

• 
College ID.  
• 
Aadhaar.  
• 
College email.  
• 
DigiLocker.  
• 
Sumsub.  
Verification Status 
Examples: 
• 
Pending.  
• 
Failed.  
• 
Rejected.  
• 
Verified.  
 
40. USER LANGUAGE / SLANG MAPPING 
The AI should understand informal expressions. 
“How can I get student verified?” 
→ STUDENT_VERIFICATION_GENERAL 
“How do I get the student badge?” 
→ STUDENT_BADGE 
“How to verify my college ID?” 
→ STUDENT_COLLEGE_ID 
“My college ID got rejected.” 
→ STUDENT_COLLEGE_ID_REJECTED 
“Why is my student verification pending?” 
→ STUDENT_VERIFICATION_PENDING 
“Can I use Aadhaar?” 
→ STUDENT_AADHAAR 

“Can I use college email?” 
→ STUDENT_COLLEGE_EMAIL 
“My college isn't showing.” 
→ STUDENT_INSTITUTION_NOT_FOUND 
“Student badge is not visible.” 
→ STUDENT_BADGE_MISSING 
“Where can I find internships?” 
→ STUDENT_INTERNSHIPS 
“Is there a student plan?” 
→ STUDENT_PLAN 
“Do students get campus communities?” 
→ STUDENT_COMMUNITIES 
41. STUDENT VERIFICATION AND PROFILE INFORMATION 
The user's WiseIN profile may contain education information such as: 
• 
Institution.  
• 
Course.  
• 
Academic background.  
• 
Graduation information.  
The AI must distinguish between: 
Self-entered education information 
and: 
Verified education/student status. 
A user entering “B.Tech Computer Science” into a profile does not by itself prove that the 
person is currently enrolled. 
 
42. STUDENT VERIFICATION AND FRESH GRADUATES 

The current WiseIN Student plan is described as being for: 
verified students and fresh graduates.  
The chatbot should therefore recognize queries such as: 
• 
“I graduated recently. Can I use the student plan?”  
• 
“I am a fresh graduate.”  
• 
“I just completed college.”  
• 
“Can freshers get student verification?”  
For cases where the exact graduation eligibility period is not documented, the AI should not 
invent a cutoff such as “within six months” or “within one year.” 
 
43. STUDENT VERIFICATION AND JOBS 
The Student plan currently includes access to the: 
Job & Internship Board / Internship & Job Board Access.  
The chatbot can help users understand where student opportunities are available. 
However, it should not claim: 
• 
Guaranteed jobs.  
• 
Guaranteed internships.  
• 
Guaranteed interviews.  
• 
Guaranteed recruiter responses.  
• 
Guaranteed selection.  
 
44. STUDENT VERIFICATION AND TRUST 
WiseIN's overall platform positioning is based on verified identities. 
The public website describes the platform as a network where members are verified and 
emphasizes government-backed identity verification.  
Student Verification extends this trust model to the student experience. 

The chatbot should explain this as a trust and eligibility mechanism, not as a guarantee 
that every interaction or opportunity on the platform is risk-free. 
 
45. PRIVACY AND DATA HANDLING 
WiseIN's Privacy Policy states that it collects information needed to provide a secure and 
verified networking experience. 
It also describes: 
• 
Account information.  
• 
Verification information.  
• 
Aadhaar-related information.  
• 
Third-party identity verification.  
• 
Verification data retention.  
• 
Security controls.  
• 
User data deletion rights.  
The chatbot should direct privacy-specific questions to the official WiseIN Privacy Policy 
and support channels when the answer depends on current legal or implementation 
details. 
 
46. WHEN TO ESCALATE TO HUMAN SUPPORT 
Escalate when: 
• 
Student verification repeatedly fails.  
• 
The account shows conflicting verification statuses.  
• 
Student status is verified but the badge is missing.  
• 
The verification provider reports an unexpected error.  
• 
The user's identity information requires correction.  
• 
The user's College ID cannot be accepted despite meeting documented 
requirements.  

• 
A user believes another person is using their identity.  
• 
There is suspected account compromise.  
• 
The user reports a security/privacy incident.  
• 
The issue requires backend/account investigation.  
• 
The chatbot does not have sufficient verified information to answer.  
WiseIN's public contact information provides email and phone support, and its contact 
page states that the team responds within 24 hours.  
 
47. SUPPORT INFORMATION 
Current public WiseIN contact information includes: 
Email: support/contact email shown on the official WiseIN website 
Phone: +91 8008656641 
The official contact page states that users can submit a message and that the team 
responds within 24 hours.  
The chatbot should use the current official contact/support information stored in the 
production knowledge base rather than hard-coding potentially outdated addresses. 
 
48. EXAMPLE CHATBOT RESPONSE – GENERAL VERIFICATION 
“For the India Student plan, WiseIN currently lists Student Verification using College ID + 
Aadhaar. Start the Student Verification process from your WiseIN account and follow the 
instructions shown on the verification screen. After successful verification, the applicable 
Student Badge and student-plan features can become available.” 
 
49. EXAMPLE CHATBOT RESPONSE – COLLEGE ID REJECTED 
“If your College ID was rejected, first check that the document is clear, readable, belongs 
to you, and that the information matches your WiseIN account and identity details. Please 
retry through the official Student Verification flow. If it continues to fail, contact WiseIN 
support so the team can investigate your account-specific verification issue.” 
 

50. EXAMPLE CHATBOT RESPONSE – BADGE NOT SHOWING 
“If your Student Verification shows as successful but the Student Badge is not appearing, 
refresh your profile and check the current verification/Student plan status. If the badge is 
still missing, this may require an account-status check by WiseIN support.” 
 
51. EXAMPLE CHATBOT RESPONSE – COLLEGE EMAIL 
“The Student Verification method depends on your region. WiseIN currently lists College ID 
+ Aadhaar for the India Student plan and College Email + Sumsub for the global Student 
plan. Please follow the method shown for your account rather than using a different 
verification route.” 
 
52. EXAMPLE CHATBOT RESPONSE – ABC ID 
“WiseIN's current public Student Plan information does not provide enough detail to 
confirm ABC ID as a current Student Verification method. Please check whether 
ABC/DigiLocker academic verification is actually offered in your WiseIN verification screen. 
If it is not shown, use the currently available verification method or contact support.” 
This response is important because the chatbot should not invent a feature simply 
because it appears in an older or proposed knowledge document. 
 
53. EXAMPLE CHATBOT RESPONSE – STUDENT PLAN 
“WiseIN currently offers a Student plan for verified students and fresh graduates. The India 
listing shows Student Verification using College ID + Aadhaar and includes a Student 
Badge, Internship & Job Board Access, Campus Communities, Student Networking Events, 
and Early Access to Student Opportunities.” 
 
54. AI SECURITY GUARDRAILS 
The Student Verification chatbot must follow these rules: 
Rule 1 – Never collect secrets 
Never ask for: 
• 
Passwords.  

• 
OTPs.  
• 
Aadhaar PIN.  
• 
Authentication tokens.  
• 
API keys.  
• 
Session cookies.  
Rule 2 – Never request sensitive documents in ordinary chat 
Do not ask the user to upload: 
• 
Aadhaar.  
• 
College ID.  
• 
Passport.  
• 
Marksheets.  
• 
Identity documents.  
inside the chatbot. 
Rule 3 – Use the official verification flow 
Direct users to the secure WiseIN verification interface. 
Rule 4 – Never fabricate verification status 
Only an authorized backend integration can provide account-specific status. 
Rule 5 – Never fabricate processing times 
Do not say “it will definitely be verified within 24 hours” unless the current official workflow 
specifies that SLA. 
Rule 6 – Never guarantee opportunities 
Student verification does not guarantee internships, jobs, interviews, mentors, or 
selection. 
Rule 7 – Protect regional differences 
Do not provide the global verification workflow to Indian users unless applicable. 
 
55. RAG KNOWLEDGE STRUCTURE 

Each Student Verification knowledge entry should contain: 
Knowledge ID 
Example: 
WISEIN-STUDENT-VERIFY-001 
Feature 
Student Verification 
User Intent 
Example: Student Verification Failed 
User Question 
“My college ID was rejected.” 
User Situation 
Student attempted verification but the College ID was rejected. 
Symptoms 
Verification failed/rejected message. 
Expected Behavior 
The application should provide an appropriate verification status or error. 
Resolution 
Follow the current approved retry/troubleshooting process. 
Platform 
Web / Android / iOS, where applicable. 
Region 
India / Global. 
Verification Method 
College ID + Aadhaar / College Email + Sumsub / other currently supported method. 
Security Level 
Sensitive identity information. 

Escalation Required 
Yes/No. 
Source 
Official WiseIN documentation / verified product implementation. 
Verification Status 
Verified / Needs Product Confirmation. 
Last Verified 
Date of last product verification. 
 
56. IMPORTANT RAG RULE: CURRENT PRODUCT OVER OLD DOCUMENT 
The chatbot knowledge base may contain multiple documents created at different times. 
Therefore, when information conflicts: 
1. Current production implementation should be checked.  
2. Current official WiseIN documentation should be preferred.  
3. Current approved internal product documentation should be preferred.  
4. Older documents should not automatically override newer information.  
5. Unsupported assumptions must not be presented as facts.  
For example, the supplied reference describes multiple Student Verification methods 
including: 
• 
Edu Email.  
• 
DigiLocker/ABC ID.  
• 
Student ID upload.  
The current public WiseIN website currently publishes: 
India: College ID + Aadhaar 
Global: College Email + Sumsub.  
Therefore, the AI knowledge base should mark the other methods as “requires current 
product verification” unless the live application confirms them. 

 
57. QA TEST CASES FOR STUDENT VERIFICATION 
QA should test at least: 
Positive cases 
• 
Valid College ID.  
• 
Valid Aadhaar verification.  
• 
Correct student information.  
• 
Successful Student Verification.  
• 
Student Badge appearing after verification.  
• 
Student plan activation.  
Negative cases 
• 
Invalid College ID.  
• 
Unreadable College ID.  
• 
Incorrect student information.  
• 
Name mismatch.  
• 
Unsupported verification method.  
• 
Verification provider failure.  
• 
Invalid account state.  
• 
Expired/invalid document where applicable.  
Account-state cases 
• 
Verification not started.  
• 
Verification in progress.  
• 
Verification pending.  
• 
Verification successful.  
• 
Verification failed.  
• 
Verification rejected.  

• 
Badge missing after successful verification.  
Security cases 
• 
User asks chatbot to verify their Aadhaar manually.  
• 
User sends an OTP.  
• 
User sends a password.  
• 
User attempts to upload an identity document to chat.  
• 
User asks for another person's verification status.  
The chatbot must refuse to process secrets and redirect sensitive verification actions to 
the secure application flow. 
 
58. MOBILE AND WEB CONSIDERATIONS 
Student Verification may be accessed through WiseIN's web or mobile experience. 
The public WiseIN website confirms an official mobile application and describes identity 
verification as one of its capabilities.  
The chatbot should therefore identify whether the user is using: 
• 
Web.  
• 
Android.  
• 
iOS.  
If an issue occurs only on one platform, the AI should capture that information before 
escalation. 
 
59. STUDENT VERIFICATION TROUBLESHOOTING QUESTIONS 
Before escalating, the chatbot can ask non-sensitive questions such as: 
• 
“Are you using the WiseIN website or mobile app?”  
• 
“Which country/region is your account using?”  
• 
“What verification method does the screen show?”  
• 
“What status do you see: pending, failed, rejected, or verified?”  

• 
“What exact error message is displayed?”  
• 
“Have you already submitted the verification?”  
• 
“Is the Student Badge visible on your profile?”  
The chatbot should not ask: 
• 
“What is your Aadhaar number?”  
• 
“What is your Aadhaar OTP?”  
• 
“What is your password?”  
• 
“Send me your College ID here.”  
• 
“Send me your verification code.”  
 
60. WHAT THE CHATBOT SHOULD KNOW ABOUT STUDENT VERIFICATION 
The final AI knowledge model should understand: 
Student Verification is different from ordinary email verification. 
Student Verification is different from government identity verification. 
For India's currently published Student plan, College ID + Aadhaar are required. 
The global Student listing currently describes College Email + Sumsub. 
Student Badge is associated with the Student plan. 
Student-plan features currently include internship/job board access, campus 
communities, student networking events, and early access to student opportunities. 
Verification does not guarantee jobs, internships, interviews, mentors, or selection. 
Exact verification workflows and supported documents can change. 
The AI must use the current production workflow when available. 
The AI must never request passwords, OTPs, Aadhaar PINs, biometric data, or private 
credentials. 
The AI must never claim to have checked account status unless it has an authorized 
backend integration. 
Account-specific verification problems should be escalated to WiseIN support. 

61. FINAL STUDENT VERIFICATION OBJECTIVE 
The Student Verification chatbot should follow this complete reasoning sequence: 
Identify the user's region → identify the verification method → identify the current 
verification status → understand the user's problem → retrieve the latest approved 
WiseIN documentation → provide verified troubleshooting → protect sensitive 
information → check whether account-specific investigation is required → escalate 
when necessary. 
The ultimate objective is to help genuine students complete the WiseIN Student 
Verification process safely while preventing misinformation, unnecessary collection of 
sensitive identity information, and unsupported claims about student benefits. 
 



---

