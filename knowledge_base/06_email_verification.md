# Email Verification

## Source: WISEIN EMAIL VERIFICATION DOCUMENTATION006.pdf

DOCUMENT 006 — WISEIN EMAIL 
VERIFICATION DOCUMENTATION 
WISEIN-AUTH-006 
Document Title: WiseIN Email Verification Documentation 
Category: Authentication & Account Management 
Document Version: 1.0 
Document Status: Draft — Pending Product Review and Approval 
Prepared By: Marella Shanmukha Reddy (MSR) 
Created / Updated Date: 17 September 2026 
Classification: Internal Use / Customer Support Knowledge / AI-RAG Knowledge Source 
Primary Purpose: To document the email-based OTP verification processes used during WiseIN 
registration and login, including workflows, requirements, errors, troubleshooting, security, and 
AI customer-support guidance. 
Authority Status: Draft documentation. Product, engineering, and support-team validation are 
required before the document is treated as an authoritative source. 
1. Purpose of This Document 
This document provides detailed documentation of the email verification mechanisms used by 
the WiseIN platform during user registration and login. 
Email verification is an important part of the authentication process because it helps confirm that 
users have access to the email address associated with their account. WiseIN uses a One-Time 
Password (OTP) as part of the verification process. 
This document is designed to support: 
●​ WiseIN users who experience email verification issues. 
●​ Customer-support representatives handling authentication-related queries. 
●​ QA testers documenting verification behavior and errors. 

●​ Developers responsible for authentication and OTP functionality. 
●​ The WiseIN AI customer-support chatbot. 
●​ The Retrieval-Augmented Generation (RAG) knowledge base. 
The document separates information into the following categories: 
1.​ Source-derived information from available WiseIN documentation. 
2.​ Behavior observed during live application testing. 
3.​ Information requiring product or engineering confirmation. 
4.​ Proposed guidance for AI customer support. 
Only verified and approved information should be used by the AI chatbot as an authoritative 
response. 
2. Scope of the Document 
2.1 Included Scope 
This document covers: 
●​ Email verification during new-user registration. 
●​ Email OTP verification during user login. 
●​ Entering a registered email address. 
●​ OTP delivery through email. 
●​ OTP entry and submission. 
●​ OTP validity and expiry information. 
●​ Invalid OTP errors. 
●​ Basic troubleshooting procedures. 
●​ Security and privacy requirements. 
●​ Human support escalation. 
●​ AI chatbot response guidelines. 
●​ Source tracking and verification status. 
●​ Pending QA and product-validation requirements. 
2.2 Excluded Scope 
The following topics are not covered in detail in this document: 
●​ Government identity verification and KYC. 
●​ Aadhaar verification. 
●​ PAN verification. 
●​ DigiLocker verification. 

●​ Video liveness verification. 
●​ Complete login documentation. 
●​ Password reset and account recovery. 
●​ Internal OTP generation logic. 
●​ Backend implementation and database operations. 
●​ Internal security infrastructure. 
●​ Unverified OTP retry and account-lockout policies. 
These topics should be documented separately or referenced through their approved 
documentation. 
3. Email Verification Overview 
WiseIN uses an OTP-based verification process in which a user receives a one-time password 
through email and enters it into the application. 
The email verification process is relevant in two primary situations: 
Verification Type 
Purpose 
Registration Email 
Verification 
Verifies the email address during the account registration 
process. 
Login Email Verification 
Verifies the user during login using the registered email 
address. 
Although both processes use email-based OTP verification, their workflows may differ. 
The registration workflow is documented in the available WiseIN platform guide. The login 
workflow and specific email content were observed during live testing and require confirmation 
from the WiseIN product or engineering team. 
3.1 Main Objectives 
The email verification process is intended to: 
●​ Confirm access to the user's email address. 
●​ Add a verification step to account registration. 

●​ Support email-based login authentication. 
●​ Reduce unauthorized access. 
●​ Provide an additional security check during login. 
●​ Inform users when the submitted OTP is not accepted. 
4. Accessing the Email Verification 
Process 
4.1 Registration 
The registration process can be accessed through the WiseIN sign-up page: 
URL: https://www.wisein.in/sign-up  
The user enters the required registration details and requests an OTP through the available 
email-verification action. 
4.2 Login 
During login, the user enters their registered email address. 
After the email address is submitted, WiseIN sends an OTP to the registered email address. 
The user must enter the received OTP into the login verification interface. 
The exact login URL, complete UI layout, and successful-login redirect should be documented 
and verified in the separate WiseIN Login Documentation. 
5. Registration Email Verification 
Requirements 
According to the available WiseIN platform guide, the registration process includes the following 
requirements: 
Requirement 
Documented Details 
Verification 
Status 

Username 
The user must enter a username. 
Source-derived 
Email 
Address 
A valid personal or corporate email address is required. 
Source-derived 
Password 
Minimum 8 characters, including uppercase letters, 
lowercase letters, numbers, and symbols. 
Source-derived 
OTP 
A six-digit OTP is sent to the registered email address. 
Source-derived 
OTP Entry 
The OTP is entered in the verification modal. 
Source-derived 
Submission 
The user selects Submit & Continue. 
Source-derived 
Next Stage 
After successful validation, the initial account is registered 
and the user is directed to mandatory identity 
verification/KYC. 
Source-derived 
5.1 Password Requirement 
The registration password must contain: 
●​ At least 8 characters. 
●​ Uppercase letters. 
●​ Lowercase letters. 
●​ Numbers. 
●​ Symbols. 
The exact password-validation error messages and password policy exceptions require 
additional verification. 
5.2 OTP Requirement 

The available registration documentation states that: 
●​ The OTP is sent to the registered email address. 
●​ The OTP contains six digits. 
●​ The OTP is entered through a verification modal. 
●​ The user selects Submit & Continue after entering the OTP. 
The following details require further confirmation: 
●​ OTP expiry duration. 
●​ OTP resend availability. 
●​ Maximum number of attempts. 
●​ Rate limits. 
●​ Whether older OTPs become invalid after a new OTP is generated. 
●​ Account restrictions after repeated incorrect attempts. 
6. Registration Email Verification Workflow 
The documented registration workflow is as follows: 
1.​ Open the WiseIN sign-up page. 
2.​ Enter a username. 
3.​ Enter a valid personal or corporate email address. 
4.​ Create a password that satisfies the documented password requirements. 
5.​ Select Send OTP / Verify Email. 
6.​ Open the registered email inbox. 
7.​ Retrieve the six-digit OTP sent by WiseIN. 
8.​ Enter the OTP into the verification modal. 
9.​ Select Submit & Continue. 
10.​WiseIN validates the OTP. 
11.​After successful validation, the initial account is registered. 
12.​The user is automatically directed to the mandatory identity-verification/KYC process. 
6.1 Registration Verification Outcome 
Outcome 
Behavior 
Successful OTP 
Validation 
The email OTP is validated, the initial account is registered, and the 
user proceeds to mandatory KYC. 

Incorrect OTP 
The exact registration error message requires confirmation. 
Expired OTP 
Expiry behavior requires confirmation. 
OTP Not Received 
Delivery and resend troubleshooting must be verified. 
Repeated Invalid 
OTP 
Retry and lockout behavior requires confirmation. 
7. Login Email Verification Overview 
During live testing, the WiseIN login process was observed to use the user's registered email 
address. 
The observed login flow is: 
1.​ The user enters their registered email address. 
2.​ The user submits the email address. 
3.​ WiseIN sends an OTP to the registered email address. 
4.​ The user opens the OTP email. 
5.​ The user enters the OTP into the login verification field. 
6.​ WiseIN validates the entered OTP. 
7.​ The user proceeds if the OTP is accepted. 
8.​ If the OTP is rejected, an error message is displayed. 
The complete successful-login behavior, including redirection, session creation, and 
device/session management, requires additional testing. 
8. Login Email Verification — Live Testing 
Observations 
The following behavior was observed during live testing of WiseIN login email verification. 

Item 
Observation 
Verification Type 
Login email OTP verification 
Email Used 
User's registered email address 
OTP Delivery 
Method 
Email 
OTP Format 
Six-digit OTP observed 
Delivery Time 
Approximately 10 seconds / almost immediate according to the live 
observation 
OTP Expiry 
The login email states that the code expires in 10 minutes 
Security Message 
Users are instructed to contact support if they did not initiate the login 
request 
Verification Status 
Observed During Live Testing 
8.1 Important Verification Note 
The 10-minute expiry statement was observed in the login email received during testing. 
The approximate 10-second delivery time was also observed during testing. 
These observations should not automatically be treated as official service-level guarantees. The 
following details must be confirmed by the WiseIN product or engineering team: 
●​ Official OTP validity duration. 

●​ Whether the expiry period is always 10 minutes. 
●​ Whether the delivery time varies by email provider. 
●​ OTP resend rules. 
●​ OTP retry limits. 
●​ Rate-limiting behavior. 
●​ Whether a new OTP invalidates the previous OTP. 
9. Login Verification Email Content 
During live testing, the login verification email included the following elements: 
9.1 Email Purpose 
The email was related to secure login verification for WiseIN. 
9.2 Personalized Greeting 
The email included a personalized greeting using the user's name. 
The exact name of the user must not be included in public documentation or examples. 
9.3 OTP Verification Instruction 
The email instructed the user to verify their account by using the OTP. 
For documentation purposes, the actual OTP must never be recorded. 
Use the following placeholder instead: 
[6-DIGIT OTP] 
9.4 OTP Expiry Message 
The observed email stated that the OTP would expire in 10 minutes. 
This should be recorded as a live observation until the expiry policy is confirmed by the product 
or engineering team. 
9.5 Security Alert 

The email included a security alert advising the user to contact the WiseIN support team if they 
did not initiate the login request. 
This security message should be preserved in the approved support guidance after product and 
security-team validation. 
10. Login Email Verification Workflow 
The recommended documented login workflow is: 
1.​ Open the WiseIN login page. 
2.​ Enter the registered email address. 
3.​ Submit the email address to request an OTP. 
4.​ Open the registered email inbox. 
5.​ Locate the latest WiseIN login OTP email. 
6.​ Review the email without sharing the OTP with anyone. 
7.​ Enter the OTP into the login verification field. 
8.​ Submit the OTP. 
9.​ If the OTP is valid, continue to the login-success flow. 
10.​If the OTP is rejected, review the displayed error and follow the approved 
troubleshooting process. 
10.1 User Guidance 
Users should use the latest OTP received for the current login request. 
Users should not share their OTP with: 
●​ The AI chatbot. 
●​ Customer-support representatives through unofficial channels. 
●​ Other users. 
●​ Unknown individuals. 
●​ Any person claiming to provide account verification assistance. 
11. Invalid OTP Error — Live Testing 
11.1 Observed Error 
During login testing, an incorrect OTP was entered into the verification field. 
The WiseIN application displayed the following error message: 

Invalid OTP 
The error message appeared in red text. 
11.2 Error Details 
Field 
Observation 
Feature 
Login Email Verification 
Trigger 
Incorrect OTP entered 
Displayed 
Message 
“Invalid OTP” 
Display Format 
Red text 
Error Type 
OTP validation error 
User Impact 
The user cannot continue using the incorrect 
OTP 
Verification Status 
Observed During Live Testing 
11.3 Observed Behavior 
1.​ The user enters their registered email address. 
2.​ WiseIN sends an OTP to the registered email address. 
3.​ The user enters an incorrect OTP. 
4.​ WiseIN displays “Invalid OTP” in red. 
5.​ The user must enter an accepted OTP to continue. 

The exact behavior after repeated incorrect attempts requires additional testing. 
12. Error Scenario Register 
Error Scenario 
Description 
Status 
Invalid OTP 
The application displays “Invalid OTP” in red 
when an incorrect login OTP is entered. 
Observed 
Expired OTP 
The login email states that the OTP expires in 10 
minutes; application behavior after expiry is not 
yet confirmed. 
Partially observed / 
Pending 
OTP Not 
Received 
The user does not receive the OTP email. 
Troubleshooting 
requires validation 
Delayed OTP 
The OTP email arrives after a delay. 
Pending testing 
Multiple OTP 
Requests 
The user requests more than one OTP. 
Pending testing 
Old OTP Used 
The user enters an OTP received before the 
latest OTP. 
Pending testing 
Repeated Invalid 
OTP 
The user enters incorrect OTPs multiple times. 
Pending testing 
Unauthorized 
OTP 
The user receives a login OTP without initiating 
login. 
Security escalation 
required 

Empty OTP 
The user submits the verification form without 
entering an OTP. 
Pending testing 
Incorrect OTP 
Length 
The user enters fewer or more digits than 
expected. 
Pending testing 
13. Email OTP Troubleshooting 
13.1 User Receives “Invalid OTP” 
If a user receives the “Invalid OTP” message, the AI or support representative should guide the 
user through the following steps: 
1.​ Confirm that the user is entering the OTP for the current login request. 
2.​ Ask the user to check whether a newer OTP email has arrived. 
3.​ Advise the user to use the latest OTP received. 
4.​ Ask the user to enter the OTP carefully. 
5.​ Ask the user to check that no digits are missing. 
6.​ Ask the user to verify whether the OTP has expired. 
7.​ Do not ask the user to share the OTP. 
8.​ If the correct and unexpired OTP continues to be rejected, escalate the issue to human 
support. 
The AI must not assume the retry limit, resend behavior, or lockout rules without verified 
documentation. 
13.2 User Does Not Receive the OTP 
Recommended basic troubleshooting: 
1.​ Confirm that the user entered the registered email address. 
2.​ Ask the user to check their inbox. 
3.​ Ask the user to check the spam or junk folder. 
4.​ Ask the user to check the promotions or other filtered folders, where applicable. 
5.​ Ask the user to wait briefly for email delivery. 
6.​ Check whether a newer OTP email was received. 
7.​ Escalate if the OTP is not received after the approved troubleshooting process. 

The AI should not claim that a resend option exists unless the option has been verified on the 
platform. 
13.3 User Receives Multiple OTP Emails 
The user should be advised to use the latest OTP received for the current request. 
The following behavior requires confirmation: 
●​ Whether only the latest OTP remains valid. 
●​ Whether earlier OTPs are invalidated. 
●​ Whether multiple OTP requests trigger rate limits. 
●​ Whether multiple OTP emails indicate a technical issue. 
13.4 User Reports an Expired OTP 
The login email observed during testing states that the code expires in 10 minutes. 
The AI should explain that the user needs to use a valid, unexpired OTP and follow the 
approved process for requesting a new OTP, if such a process is available. 
The AI must not invent the resend process or claim a specific number of retries without 
confirmation. 
14. OTP Expiry and Delivery Behavior 
14.1 Observed Information 
The login verification email observed during testing contained a statement that the OTP expires 
in 10 minutes. 
OTP delivery was reported as almost immediate, approximately 10 seconds after the login 
request. 
14.2 Pending Confirmation 
The following information must be verified: 
●​ Official OTP expiry duration. 
●​ Whether registration and login use the same expiry duration. 
●​ Whether OTP expiry begins when the OTP is generated or delivered. 

●​ Whether an expired OTP displays a separate error message. 
●​ Whether the user can request a new OTP. 
●​ Whether there is a cooldown period between OTP requests. 
●​ Whether there is a maximum number of OTP requests. 
●​ Whether the system blocks repeated OTP requests. 
●​ Whether the latest OTP invalidates previously generated OTPs. 
14.3 Documentation Rule 
The observed 10-minute expiry must be described as an observed email statement until it is 
officially confirmed. 
Recommended wording: 
“The login verification email observed during testing states that the OTP expires in 
10 minutes. The official OTP expiry policy requires confirmation from the WiseIN 
product or engineering team.” 
15. Security and Privacy Requirements 
Email OTPs are sensitive authentication credentials. They must be handled securely throughout 
the application, support process, and AI chatbot. 
15.1 OTP Protection 
●​ Never ask users to share their OTP. 
●​ Never store actual OTPs in documentation. 
●​ Never include real OTPs in screenshots or QA reports. 
●​ Use placeholders such as [6-DIGIT OTP]. 
●​ Do not repeat a user's OTP in chatbot responses. 
●​ Do not claim that the AI can view or validate a user's OTP. 
●​ Do not request passwords or other authentication credentials. 
15.2 Login Security Alert 
If a user receives a login OTP without initiating a login request: 
1.​ Advise the user not to share the OTP. 
2.​ Ask the user to contact official WiseIN support. 
3.​ Treat the report as a potential account-security concern. 
4.​ Escalate according to the approved security-support procedure. 

5.​ Do not make assumptions about whether the account has been compromised. 
15.3 Sensitive Information 
The AI and support staff must not request the following information through an unsecured chat: 
●​ Passwords. 
●​ OTP values. 
●​ Aadhaar numbers. 
●​ PAN numbers. 
●​ Payment-card information. 
●​ Authentication tokens. 
●​ Full identity documents unless an approved secure process requires them. 
15.4 Screenshot Handling 
If a screenshot is required for troubleshooting: 
●​ Ask the user to hide the OTP. 
●​ Hide email addresses where unnecessary. 
●​ Hide personal identifiers. 
●​ Hide account numbers or sensitive information. 
●​ Use approved support channels. 
●​ Do not store screenshots containing exposed authentication credentials. 
16. Email OTP and Aadhaar-Linked Mobile 
OTP 
Email OTP verification and Aadhaar-linked mobile OTP verification are different processes. 
Feature 
Email OTP 
Aadhaar-Linked Mobile OTP 
Purpose 
Registration or login verification 
Identity verification/KYC 
Delivery Method 
Registered email address 
Mobile number linked to Aadhaar 

Context 
Account registration or login 
Government identity verification 
Related Process 
Email verification 
KYC / identity verification 
AI Guidance 
Use email OTP instructions 
Use approved KYC documentation 
The AI chatbot must distinguish between these two OTP types. 
For example, if a user asks about a login OTP, the AI should not provide Aadhaar verification 
instructions unless the user specifically indicates that they are completing the KYC process. 
The AI must not request or collect the user's Aadhaar number, PAN details, or OTP. 
17. Platform Differences 
Email verification should be tested on each officially supported platform. 
17.1 Web Testing 
Test the following on the web application: 
●​ Email entry field. 
●​ OTP entry field. 
●​ OTP submission. 
●​ Invalid OTP error display. 
●​ Error-message color and placement. 
●​ Browser autofill behavior. 
●​ Copy-and-paste behavior. 
●​ Page refresh behavior. 
●​ OTP verification after browser navigation. 
17.2 Mobile Testing 
Test the following on mobile devices: 
●​ Email input behavior. 
●​ OTP field layout. 

●​ Mobile keyboard behavior. 
●​ OTP auto-fill functionality. 
●​ Copy-and-paste functionality. 
●​ Error-message placement. 
●​ Screen responsiveness. 
●​ OTP submission behavior. 
●​ Navigation after successful verification. 
17.3 Pending Platform Validation 
The following details require live testing: 
●​ Whether web and mobile use the same OTP workflow. 
●​ Whether the expiry duration is the same across platforms. 
●​ Whether error messages are identical. 
●​ Whether OTP auto-fill is supported. 
●​ Whether the user can paste the OTP. 
●​ Whether the application behaves differently across browsers and devices. 
Until these differences are verified, the AI should provide platform-neutral instructions. 
18. Additional QA Test Cases 
The following test cases should be executed and documented by the QA team. 
Test Case 
Action 
Expected Result 
Status 
Valid OTP 
Enter the correct OTP 
User proceeds to the next 
step 
Pending 
testing 
Invalid OTP 
Enter an incorrect OTP 
“Invalid OTP” appears in red 
Observed 
Expired OTP 
Enter OTP after the 
expiry period 
Exact error behavior requires 
testing 
Pending 

Empty OTP 
Submit without entering 
OTP 
Validation message should 
appear 
Pending 
Short OTP 
Enter fewer digits 
Validation behavior requires 
testing 
Pending 
Long OTP 
Enter more digits 
Validation behavior requires 
testing 
Pending 
Multiple 
Requests 
Request OTP multiple 
times 
Rate-limit behavior requires 
testing 
Pending 
Previous OTP 
Enter an older OTP 
Validity behavior requires 
testing 
Pending 
Repeated Errors 
Enter incorrect OTP 
repeatedly 
Retry/lockout behavior 
requires testing 
Pending 
Delayed Email 
Receive OTP after a 
delay 
Delivery and expiry behavior 
require testing 
Pending 
Spam Folder 
Check OTP in spam 
folder 
Email delivery behavior 
documented 
Pending 
Unauthorized 
Request 
Receive OTP without 
initiating login 
Security guidance and 
escalation 
Guidance 
proposed 
Refresh Page 
Refresh during OTP 
verification 
Session and OTP behavior 
require testing 
Pending 

Multiple Devices 
Request login from 
multiple devices 
Session and OTP behavior 
require testing 
Pending 
19. Human Support Escalation 
The issue should be escalated to human support when it cannot be resolved through approved 
troubleshooting instructions. 
19.1 Escalation Conditions 
Escalate the issue when: 
●​ A correct and unexpired OTP is repeatedly rejected. 
●​ The user does not receive an OTP after basic troubleshooting. 
●​ The user receives OTPs without initiating a login. 
●​ The user reports suspicious login activity. 
●​ The account appears blocked or restricted. 
●​ The user experiences repeated authentication failures. 
●​ The issue is account-specific. 
●​ The application displays an undocumented error. 
●​ The knowledge base does not contain a verified solution. 
●​ The user requests human assistance. 
●​ The issue may involve a security or privacy concern. 
19.2 Information to Collect 
Collect only the minimum information necessary to investigate the issue: 
●​ Feature where the issue occurred. 
●​ Verification stage. 
●​ Approximate time of the issue. 
●​ Device type. 
●​ Browser or application platform. 
●​ Exact error message. 
●​ Steps already attempted. 
●​ Redacted screenshot, if required. 
●​ Registered email address only through an approved support process. 
19.3 Information Not to Collect 

Do not request: 
●​ OTP values. 
●​ Passwords. 
●​ Aadhaar numbers. 
●​ PAN numbers. 
●​ Authentication tokens. 
●​ Payment-card details. 
●​ Unredacted identity documents. 
19.4 Support Resources 
The available WiseIN platform guide lists the following support resources: 
●​ Support portal: https://www.wisein.in/help-support  
●​ Email: support@wisein.in 
●​ Live chat. 
●​ Official Instagram direct messages. 
The guide also mentions a target response time of within 24 hours and a support form requiring 
details such as full name, email address, mobile number, optional company information, and 
message. 
These support details and the response-time commitment should be reconfirmed with the 
WiseIN support owner before being treated as final operational policy. 
20. AI Customer Support Guidance 
The WiseIN AI chatbot must provide accurate, secure, and context-aware assistance for email 
verification issues. 
20.1 Identify the User's Verification Stage 
Before providing instructions, the AI should identify whether the user is: 
●​ Registering a new account. 
●​ Logging into an existing account. 
●​ Waiting for an OTP. 
●​ Entering an OTP. 
●​ Receiving an invalid OTP error. 
●​ Reporting an expired OTP. 
●​ Reporting an unauthorized login OTP. 

●​ Experiencing an account-specific problem. 
20.2 General Response Structure 
The AI should follow this response structure: 
1.​ Acknowledge the user's issue. 
2.​ Identify the relevant verification stage. 
3.​ Provide the verified information available in the knowledge base. 
4.​ Give clear troubleshooting instructions. 
5.​ Avoid requesting sensitive information. 
6.​ Confirm whether the issue has been resolved. 
7.​ Escalate if the issue remains unresolved or involves security concerns. 
20.3 Recommended Response — Invalid OTP 
The “Invalid OTP” message means that the OTP entered was not accepted. Please 
check that you are using the latest OTP sent to your registered email address and 
enter it carefully. The login email observed during testing states that the OTP 
expires in 10 minutes. Please do not share your OTP with anyone. If the correct 
and unexpired OTP continues to show as invalid, the issue should be escalated to 
WiseIN support. 
20.4 Recommended Response — OTP Not Received 
Please check that you entered your registered email address correctly. Also check 
your inbox, spam, junk, and other filtered folders for the WiseIN OTP email. If you 
still cannot find the OTP, please share the issue details through the official WiseIN 
support channel. Do not share your OTP or password with anyone. 
20.5 Recommended Response — Unauthorized OTP 
If you received a WiseIN login OTP without initiating a login request, do not share 
the OTP with anyone. Please contact the official WiseIN support team immediately 
so that the issue can be reviewed securely. 
20.6 AI Restrictions 
The AI must not: 
●​ Request a user's OTP. 

●​ Request a user's password. 
●​ Invent error messages. 
●​ Invent OTP expiry rules. 
●​ Invent resend options. 
●​ Invent retry limits. 
●​ Invent account-lockout policies. 
●​ Guarantee that an OTP will arrive within a specific time. 
●​ Claim to validate an OTP directly. 
●​ Claim to create a support ticket unless the integration actually performs that action. 
●​ Provide unverified security or account-recovery instructions. 
●​ Combine registration, login, and KYC instructions incorrectly. 
●​ Continue repetitive troubleshooting when escalation is appropriate. 
21. AI and RAG Knowledge Base 
Requirements 
This document may be used as a knowledge source for the WiseIN AI customer-support chatbot 
after approval and validation. 
21.1 Required Metadata 
The document should contain: 
●​ Document ID. 
●​ Document title. 
●​ Version number. 
●​ Source information. 
●​ Verification status. 
●​ Last updated date. 
●​ Owner or responsible team. 
●​ Approval status. 
●​ Related documents. 
●​ Applicable platform. 
●​ Feature category. 
●​ Error scenarios. 
●​ Escalation conditions. 
21.2 Source Classification 
Each piece of information should be classified as one of the following: 

Classification 
Meaning 
Source-Derived 
Taken from available WiseIN documentation. 
Observed During Live Testing 
Behavior directly observed while testing the application. 
Product-Confirmed 
Confirmed by the WiseIN product team. 
Engineering-Confirmed 
Confirmed by the engineering team. 
Support-Confirmed 
Confirmed by the support team. 
Pending Verification 
Information that has not yet been validated. 
Proposed Guidance 
Recommended behavior that requires approval. 
21.3 RAG Response Rule 
The chatbot should use approved and current information when responding to user questions. 
If the knowledge base does not contain a verified answer, the AI should state that the 
information requires confirmation and escalate the issue when appropriate. 
The AI must not treat unverified assumptions as official WiseIN functionality. 
22. Source and Verification Register 
Source ID 
Source 
Information Used 
Status 

SRC-AUT
H-006-01 
WiseIN Complete 
Platform User Guide 
Registration email OTP workflow and 
post-validation KYC transition 
Source-derived; 
approval 
pending 
SRC-AUT
H-006-02 
Live Login Email 
Observation 
Registered email login, OTP email, 
10-minute expiry statement, security 
alert, approximate delivery time 
Observed 
During Live 
Testing 
SRC-AUT
H-006-03 
Live Login UI 
Testing 
Red “Invalid OTP” message after 
incorrect OTP entry 
Observed 
During Live 
Testing 
SRC-AUT
H-006-04 
Product / 
Engineering 
Confirmation 
OTP expiry, resend, retry limits, rate 
limits, lockout, and login success 
behavior 
Pending 
SRC-AUT
H-006-05 
Support Team 
Confirmation 
Official support workflow, 
response-time commitment, and 
escalation process 
Pending 
23. Pending Verification Items 
The following items require additional testing or confirmation: 
1.​ Official login page URL. 
2.​ Exact login UI elements. 
3.​ Official OTP expiry duration. 
4.​ Whether registration and login OTPs have the same expiry period. 
5.​ OTP resend button and workflow. 
6.​ OTP retry limits. 
7.​ Rate limits. 
8.​ Account-lockout behavior. 
9.​ Behavior after multiple incorrect OTP attempts. 
10.​Behavior after requesting multiple OTPs. 
11.​Whether old OTPs become invalid after a new OTP is generated. 

12.​Error message for expired OTP. 
13.​Error message for an unregistered email address. 
14.​Empty OTP validation. 
15.​Invalid OTP length validation. 
16.​OTP auto-fill behavior. 
17.​OTP paste behavior. 
18.​Login success redirect. 
19.​Session creation and session persistence. 
20.​Differences between web and mobile login. 
21.​Official security escalation procedure. 
22.​Final support SLA and operating hours. 
23.​Official ownership of OTP-related incidents. 
24. Related Documents 
The following documents are related to email verification: 
Document 
Document ID 
Relationship 
WiseIN User Registration / Sign-Up 
Documentation 
WISEIN-AUTH
-003 
Describes the registration workflow 
and initial email OTP verification 
WiseIN User Login Documentation 
To Be 
Assigned 
Describes the complete login process 
WiseIN Identity Verification / KYC 
Documentation 
To Be 
Assigned 
Covers government identity 
verification after registration 
WiseIN Account Recovery / 
Password Reset Documentation 
To Be 
Assigned 
Covers account access recovery 
WiseIN Account Security 
Documentation 
To Be 
Assigned 
Covers security, sessions, and 
account protection 

WiseIN Customer Support & 
Escalation Documentation 
To Be 
Assigned 
Covers human support and issue 
escalation 
25. Completion Checklist 
25.1 Documentation Checklist 
●​ Document ID assigned. 
●​ Document title and category added. 
●​ Registration email verification documented. 
●​ Login email verification documented. 
●​ Registration and login workflows separated. 
●​ OTP delivery process documented. 
●​ OTP expiry observation recorded. 
●​ Approximate delivery time recorded. 
●​ “Invalid OTP” error documented. 
●​ Troubleshooting guidance added. 
●​ Security and privacy guidance added. 
●​ Human escalation conditions documented. 
●​ AI chatbot guidance added. 
●​ Related documents identified. 
●​ Pending verification items recorded. 
25.2 QA Checklist 
●​ Valid OTP tested. 
●​ Invalid OTP tested. 
●​ Expired OTP tested. 
●​ OTP resend tested. 
●​ Repeated invalid OTP tested. 
●​ Multiple OTP requests tested. 
●​ Old OTP behavior tested. 
●​ Empty OTP tested. 
●​ Invalid OTP length tested. 
●​ OTP delivery delay tested. 
●​ Spam-folder delivery checked. 
●​ Web behavior tested. 
●​ Mobile behavior tested. 
●​ Login success behavior verified. 

●​ Security alert behavior verified. 
25.3 AI/RAG Checklist 
●​ Document reviewed for factual accuracy. 
●​ Observations separated from confirmed policies. 
●​ Sensitive OTP values removed. 
●​ Source metadata added. 
●​ Document approved by the responsible team. 
●​ Document version recorded. 
●​ Knowledge base ingestion completed. 
●​ Retrieval testing completed. 
●​ Invalid OTP response tested. 
●​ OTP security response tested. 
●​ Escalation response tested. 
●​ Hallucination and unsupported-answer checks completed. 
26. Document Status and Summary 
Current Status: Draft — Registration email verification and login OTP behavior documented. 
This document currently includes: 
●​ The source-derived registration email OTP workflow. 
●​ The login workflow observed during live testing. 
●​ The observed login email containing a 10-minute expiry statement. 
●​ Approximate OTP delivery time of 10 seconds. 
●​ The security alert included in the login email. 
●​ The red “Invalid OTP” error message. 
●​ Troubleshooting and security guidance. 
●​ Human support escalation requirements. 
●​ AI chatbot response guidelines. 
●​ Pending product, engineering, support, and QA validation items. 
The document should not be considered final or authoritative until the relevant WiseIN teams 
confirm the remaining OTP policies, error behaviors, support process, and platform-specific 
differences. 
 



---

## Source: WISEIN-EMAIL-VERIFICATION-006.pdf

WISEIN – EMAIL VERIFICATION DOCUMENTATION 
Document ID: WISEIN-EMAIL-VERIFICATION-006 
Document Type: Product Knowledge, Troubleshooting & AI Customer Support 
Documentation 
Version: 1.0 
Platform: WiseIN 
 
1. Document Purpose 
This document defines the complete WiseIN email-verification process and the 
terminology, workflows, troubleshooting procedures, security rules, and customer-support 
escalation requirements associated with email verification. 
The document is intended to serve as an authoritative knowledge source for: 
• 
WiseIN users  
• 
Customer-support teams  
• 
QA teams  
• 
Product teams  
• 
Engineering teams  
• 
Documentation teams  
• 
The WiseIN AI Customer Support System  
• 
The WiseIN RAG knowledge base  
The objective is to enable the AI Customer Support System to correctly understand and 
answer questions related to email verification without inventing unsupported information. 
 
2. Purpose of Email Verification 
Email verification is an account-security and account-validation process used to confirm 
that the email address associated with a WiseIN account can be accessed by the user. 
Email verification can help WiseIN: 

• 
Confirm ownership or access to an email address.  
• 
Reduce invalid or incorrectly entered email addresses.  
• 
Support account security.  
• 
Support account communication.  
• 
Improve the reliability of account information.  
• 
Help prevent certain types of fake or disposable account registrations.  
• 
Support account recovery and authentication processes where applicable.  
The exact role of email verification in account creation, login, feature access, and account 
recovery must be confirmed against the current WiseIN implementation. 
 
3. Email Verification and Other Verification Types 
The AI must clearly distinguish between different types of verification. 
Email Verification 
Confirms access to or ownership of an email address. 
Mobile Verification 
Confirms access to a mobile number where mobile verification is supported. 
Identity Verification 
Used to verify an individual's identity through the applicable WiseIN verification process. 
Student Verification 
Used to establish student eligibility through the applicable WiseIN student-verification 
process. 
Organization Verification 
Used to verify an organization through the applicable WiseIN organization-verification 
process. 
These verification types are not interchangeable. 
Completing email verification does not automatically mean that a user's identity, student 
status, or organization has been verified. 

WiseIN documentation treats email/account verification separately from identity, student, 
and organization verification.  
 
4. Where Email Verification Fits in the WiseIN User Journey 
Email verification may occur during or after account registration depending on the current 
WiseIN implementation. 
A general user journey may be: 
Open WiseIN → Sign Up → Enter Account Information → Submit Registration → Receive 
Verification Email → Open Verification Message → Complete Verification → Continue 
Account Setup 
The exact sequence must be verified against the current application. 
The AI must not assume that every user follows exactly the same sequence. 
Some users may encounter email verification during: 
• 
Initial registration  
• 
Account activation  
• 
Email-address changes  
• 
Account recovery  
• 
Security verification  
• 
Reverification  
• 
Other account-management workflows  
Only verified WiseIN workflows should be presented as official instructions. 
 
5. Email Verification Terminology 
The AI should understand the following terminology. 
Email Address 
The email address associated with the user's WiseIN account. 
Registered Email 

The email address currently associated with a WiseIN account. 
Email Verification 
The process of confirming access to the registered email address. 
Verification Email 
An email sent by WiseIN for the purpose of completing an email-verification action. 
Verification Link 
A link contained in a verification email that may be used to complete verification. 
Verification Code 
A code sent through an approved verification process, if WiseIN uses code-based email 
verification. 
OTP 
One-Time Password or One-Time Passcode. If WiseIN uses an OTP during email 
verification, the exact terminology shown in the application should be used. 
Verified Email 
An email address for which the applicable WiseIN verification process has been 
successfully completed. 
Unverified Email 
An email address for which the required verification process has not yet been successfully 
completed. 
Verification Status 
The current state of the email-verification process. 
Resend Verification 
An action that requests another verification email or code, if supported. 
Verification Link Expired 
A verification link that is no longer valid. 
Verification Code Expired 
A verification code that is no longer valid, if code-based verification is supported. 

Verification Token 
A temporary technical value used by a verification system to associate a verification 
request with an account or email address. 
The AI must never expose internal verification tokens. 
 
6. Email Verification Statuses 
The final WiseIN implementation should define the exact statuses displayed to users. 
Potential states may include: 
• 
Email verification required  
• 
Verification pending  
• 
Verification email sent  
• 
Verification completed  
• 
Verification failed  
• 
Verification link expired  
• 
Verification code expired  
• 
Verification request unavailable  
• 
Verification temporarily restricted  
• 
Unknown verification error  
These are documentation categories and must not be treated as confirmed WiseIN status 
labels until verified against the application. 
The AI must use the exact status displayed by the current WiseIN application whenever 
available. 
 
7. Basic Email Verification Process 
The exact interface should be verified by Product and Engineering. 
The general process is: 
1. User creates or updates an account using an email address.  

2. WiseIN initiates the email-verification process where required.  
3. WiseIN sends a verification message to the relevant email address.  
4. User opens the verification message.  
5. User completes the verification action using the provided link or code.  
6. WiseIN validates the verification request.  
7. The email address is marked as verified if the verification succeeds.  
8. The user continues with the applicable WiseIN workflow.  
The AI must not invent exact button labels or navigation paths. 
 
8. Verification Email 
A verification email is a system-generated message associated with an email-verification 
request. 
The email may contain information such as: 
• 
WiseIN branding  
• 
Verification instructions  
• 
Verification link  
• 
Verification code, if applicable  
• 
Security information  
• 
Expiration information, if applicable  
• 
Support information  
The exact contents of WiseIN's verification email must be verified by the Engineering and 
Product teams. 
 
9. User Did Not Receive the Verification Email 
This is one of the most important support scenarios. 
If a user says: 
"I didn't receive the verification email." 

the AI should not immediately assume that WiseIN failed to send the email. 
The AI should guide the user through the following checks. 
Step 1 – Check the Email Address 
Ask the user to confirm that they entered the correct email address during registration or 
account setup. 
The AI must not request the user's password or OTP. 
Step 2 – Check Spam or Junk 
Ask the user to check: 
• 
Inbox  
• 
Spam  
• 
Junk  
• 
Promotions  
• 
Other filtered folders  
depending on their email provider. 
Step 3 – Search the Mailbox 
Ask the user to search their mailbox for the official WiseIN sender or verification-related 
subject. 
The exact sender address and subject should be added after Product/Engineering 
verification. 
Step 4 – Wait for Delivery 
If WiseIN officially documents an expected delivery delay, the AI may communicate it. 
The AI must not invent a delivery time. 
Step 5 – Resend 
If the application provides a Resend Verification or equivalent option, the AI should guide 
the user to use it. 
The exact resend limits must be verified. 
Step 6 – Escalate 

If the user still does not receive the message, collect the required troubleshooting 
information and escalate the issue if necessary. 
 
10. Important Rule for Missing Verification Emails 
The AI must distinguish between: 
Email was not received 
and 
Email was received but verification failed. 
These are different support problems. 
For example: 
"I didn't get the email." 
should trigger EMAIL_NOT_RECEIVED troubleshooting. 
Whereas: 
"I clicked the email but it says verification failed." 
should trigger EMAIL_VERIFICATION_FAILED troubleshooting. 
11. Spam, Junk and Filtering 
Verification messages may be affected by email-provider filtering. 
If a user cannot find the WiseIN verification email, the AI may suggest checking: 
• 
Spam  
• 
Junk  
• 
Promotions  
• 
Updates  
• 
Other filtered folders  
The AI may also recommend searching the mailbox using the verified WiseIN sender or 
relevant subject. 
The AI must not tell users to mark an email as safe unless this is an approved WiseIN 
support recommendation. 

 
12. Incorrect Email Address 
A user may accidentally enter the wrong email address during registration. 
Examples include: 
• 
Typographical error  
• 
Missing character  
• 
Incorrect domain  
• 
Wrong personal email  
• 
Wrong work email  
• 
Wrong college email  
• 
Extra spaces  
• 
Using an old email address  
If the application provides an approved method for correcting the email address, the AI 
should explain that process. 
If no verified correction process exists in the knowledge base, the AI should escalate rather 
than invent one. 
 
13. User Entered the Wrong Email 
If the user says: 
"I entered the wrong email address." 
the AI should determine whether the account is: 
• 
Still being registered  
• 
Awaiting verification  
• 
Already created  
• 
Already verified  
• 
Accessible through another authentication method  
The appropriate solution depends on the current WiseIN workflow. 

The AI must not claim that an email can be changed unless the application or approved 
documentation confirms that capability. 
 
14. Resend Verification Email 
If WiseIN provides a resend function, the user may request another verification message. 
The AI should explain the approved resend process. 
The AI must know, once verified: 
• 
Where the resend option appears.  
• 
How frequently it can be used.  
• 
Whether there is a cooldown period.  
• 
Whether previous links become invalid.  
• 
Whether only the latest email remains valid.  
• 
What error appears when resend limits are reached.  
Until verified, these values must not be invented. 
 
15. Multiple Verification Emails 
A user may request more than one verification email. 
The AI should explain the verified WiseIN behavior. 
Important questions for Product/Engineering verification include: 
• 
Does each resend generate a new verification token?  
• 
Does a new verification email invalidate the previous email?  
• 
Is only the latest link valid?  
• 
Is there a maximum number of resend attempts?  
• 
Is there a cooldown?  
• 
Does repeated requesting temporarily restrict verification?  
The AI must not guess these behaviors. 

 
16. Verification Link 
If WiseIN uses link-based email verification, the verification link is used to complete the 
email-verification process. 
The AI should be able to explain: 
• 
Where the link is found.  
• 
What happens after clicking it.  
• 
What happens if the link is expired.  
• 
What happens if the link has already been used.  
• 
What happens if the link is invalid.  
• 
What happens if the link opens the wrong page.  
• 
What happens if the link does not work.  
These exact behaviors must be verified. 
 
17. Expired Verification Link 
If the user says: 
"My verification link expired." 
the AI should: 
1. Explain that the link is no longer valid if the application confirms that state.  
2. Guide the user to the approved resend process.  
3. Ask them to use the newly generated verification link.  
4. Escalate if a new verification link cannot be generated.  
The AI must not invent the expiration period. 
 
18. Verification Link Already Used 
If the user receives an error indicating that the verification link has already been used, the 
AI should explain that a verification link may be single-use if this behavior is confirmed. 

The AI should then: 
1. Check whether the account now shows the email as verified.  
2. Ask the user to return to the appropriate WiseIN screen.  
3. If the account remains unverified, provide the approved recovery process.  
4. Escalate if required.  
The AI must not claim that a link is single-use unless the implementation confirms it. 
 
19. Invalid Verification Link 
If the user reports: 
"The verification link is invalid." 
the AI should determine: 
• 
Whether the link is from an official WiseIN message.  
• 
Whether the link is expired.  
• 
Whether the link has already been used.  
• 
Whether the user requested a newer verification email.  
• 
Whether the application displays a specific error.  
The AI should provide only documented troubleshooting steps. 
 
20. Verification Code 
If WiseIN uses an email verification code, the AI must understand the distinction between: 
• 
Verification code  
• 
Login OTP  
• 
Password-reset code  
• 
Two-factor authentication code  
These may serve different purposes. 

The AI must not assume that a code received for one workflow can be used in another 
workflow. 
 
21. Incorrect Verification Code 
If the user says: 
"My verification code is not working." 
the AI should determine whether: 
• 
The code was entered incorrectly.  
• 
The code has expired.  
• 
A newer code was requested.  
• 
The user is entering a code for a different WiseIN workflow.  
• 
The application is reporting another error.  
The AI should provide the verified solution for the identified condition. 
The AI must never ask the user to send the verification code to the chatbot. 
 
22. Verification Code Expired 
If the application confirms that a verification code has expired, the AI should guide the user 
through the approved process for requesting a new code. 
The AI must not invent: 
• 
Code validity duration.  
• 
Maximum retry count.  
• 
Resend limits.  
• 
Cooldown duration.  
These values must come from approved WiseIN documentation. 
 
23. User Did Not Receive Verification Code 

If email verification uses a code and the user does not receive it, the same email-delivery 
troubleshooting process applies. 
The AI should check: 
1. Correct email address.  
2. Inbox.  
3. Spam/junk.  
4. Email filtering.  
5. Resend option.  
6. Whether the application displays a delivery error.  
7. Whether the issue persists.  
If unresolved, escalate. 
 
24. Email Verification Failed 
If the user says: 
"Email verification failed." 
the AI should ask for the exact error message. 
Possible categories include: 
• 
Invalid verification link  
• 
Expired verification link  
• 
Invalid code  
• 
Expired code  
• 
Verification request not found  
• 
Verification service error  
• 
Account already verified  
• 
Account not found  
• 
Network error  

• 
Unknown error  
These categories should be mapped to actual WiseIN error messages after Engineering 
verification. 
The AI must not invent error codes. 
 
25. "Verification Failed" Error 
When the user reports a generic verification failure, the AI should not immediately identify a 
technical cause. 
Instead: 
1. Ask which platform the user is using.  
2. Ask what they were doing when the error appeared.  
3. Ask for the exact error message.  
4. Determine whether they received the email.  
5. Determine whether they clicked a link or entered a code.  
6. Check the approved knowledge base.  
7. Provide the verified troubleshooting steps.  
8. Escalate if the issue remains unresolved.  
 
26. Network Error During Email Verification 
A user may encounter a network-related error while opening a verification link or 
completing verification. 
The AI may suggest checking: 
• 
Internet connection.  
• 
Browser or application connectivity.  
• 
Whether the problem occurs repeatedly.  
• 
Whether another supported connection works, if appropriate and approved.  
The AI must not automatically conclude that WiseIN's servers are down. 

If the problem persists, it should be escalated for technical investigation. 
 
27. Verification Page Does Not Open 
If the verification link does not open: 
The AI should ask: 
• 
Are they using the WiseIN web application or mobile application?  
• 
What happens after clicking the link?  
• 
Does a browser open?  
• 
Does an error appear?  
• 
Does the page remain blank?  
• 
Does the link redirect somewhere unexpected?  
The AI should then use platform-specific approved troubleshooting. 
 
28. Verification Page Loads but Does Not Complete 
If the verification page opens but the verification does not complete, the AI should collect: 
• 
Platform  
• 
Browser or application  
• 
Exact error message  
• 
Whether the link was newly generated  
• 
Whether the user has already used another verification link  
• 
Whether the problem happens repeatedly  
The AI should not claim that the user's email has been verified unless the application or 
authorized backend confirms it. 
 
29. Email Shows Verified but Account Still Shows Unverified 
This is an important account-state inconsistency. 

If a user says: 
"I verified my email but WiseIN still says unverified." 
the AI should: 
1. Ask the user to refresh or reopen the relevant WiseIN page where appropriate.  
2. Check whether the application shows a verification confirmation.  
3. Ask for the exact displayed status.  
4. Avoid claiming that the verification has succeeded without system confirmation.  
5. Escalate if the verified and displayed states remain inconsistent.  
An inconsistent verification status across application screens is an appropriate reason for 
human support escalation.  
 
30. Verification Email Received but Account Not Updated 
If the user successfully completes the verification action but the account does not update, 
this may require backend or account-specific investigation. 
The AI should collect: 
• 
Platform  
• 
Verification method  
• 
Exact displayed status  
• 
Exact error message  
• 
Approximate time of verification  
• 
Steps completed  
The AI should escalate if the issue cannot be resolved through approved instructions. 
31. Email Verification During Registration 
If email verification is part of account registration, the AI should understand that 
registration and verification are related but separate stages. 
A possible flow is: 

Registration Started → Account Information Entered → Registration Submitted → Email 
Verification → Account Activation/Continuation 
The exact state transitions must be confirmed against the current WiseIN application. 
The AI must not claim that an account is fully active solely because registration information 
was submitted. 
 
32. Email Verification and Login 
Email verification may affect account access depending on WiseIN's authentication and 
account policies. 
If a user says: 
"I cannot login because my email isn't verified." 
the AI should determine: 
• 
Whether email verification is required before login.  
• 
Whether login is allowed while email verification is pending.  
• 
Whether the user can resend verification.  
• 
Whether account recovery is available.  
• 
Whether the account is restricted for another reason.  
These rules must be verified. 
The AI must not assume that every unverified account is unable to log in. 
 
33. Email Verification and Account Recovery 
Email verification may be relevant to account recovery. 
However, email verification and password recovery are different processes. 
The AI should not tell a user to use a password-reset process simply because their email 
verification failed. 
It should identify the user's actual objective first. 
 

34. Email Verification and Security 
Email verification is a security-sensitive process. 
The AI must prioritize account security. 
The AI must: 
• 
Use approved verification instructions.  
• 
Avoid exposing internal verification mechanisms.  
• 
Avoid exposing verification tokens.  
• 
Avoid requesting authentication secrets.  
• 
Avoid confirming sensitive account information to unauthorized users.  
• 
Escalate suspicious or compromised-account situations.  
 
35. Information the AI May Request 
During troubleshooting, the AI may request only information necessary to understand the 
issue. 
Useful information may include: 
• 
Platform  
• 
Device type  
• 
Browser  
• 
Application version  
• 
Approximate time of the issue  
• 
Exact error message  
• 
Whether the verification email was received  
• 
Whether the email was found in spam  
• 
Whether the verification link was clicked  
• 
Whether the verification process was completed  
• 
Whether the problem is recurring  

The AI should follow the general WiseIN troubleshooting principle of collecting only the 
information necessary to understand and resolve the issue.  
 
36. Information the AI Must Never Request 
The AI must never request users to provide: 
• 
Password  
• 
OTP  
• 
Verification code  
• 
Authentication code  
• 
Private key  
• 
Session token  
• 
Access token  
• 
Payment credentials  
• 
Full sensitive identity information unless an approved secure workflow explicitly 
requires it  
• 
Internal verification token  
WiseIN's AI-support documentation explicitly prohibits requesting passwords, OTPs, 
biometric information, and unnecessary sensitive verification information through 
customer-support chat.  
 
37. Email Verification Security Warning 
The AI should remind users: 
"Never share your password, OTP, verification code, or authentication code with anyone, 
including customer support." 
The AI should never ask users to forward private verification messages or expose security 
credentials through chat unless an approved secure support process specifically requires 
non-sensitive evidence. 
 

38. Suspicious Verification Email 
A user may report receiving an email that appears to be from WiseIN but seems suspicious. 
The AI should not ask the user to click the suspicious link. 
The AI should: 
1. Advise the user not to enter credentials into an unverified page.  
2. Ask them to use the official WiseIN application or website.  
3. Follow the approved WiseIN security/reporting process.  
4. Escalate when required.  
The AI must not confirm that an email is legitimate unless it has an approved mechanism 
for doing so. 
 
39. Verification Email Sent to the Wrong Person 
If a user reports receiving a WiseIN verification email for an account they did not create, the 
AI should treat it as a potential account or security issue. 
The AI should not reveal account information about another person. 
The issue should be escalated through the approved security/support process when 
necessary. 
 
40. User Changed Their Email Address 
If WiseIN supports changing a registered email address, the AI should explain the approved 
process. 
The AI must verify: 
• 
Where the email can be changed.  
• 
Whether the current email must be verified.  
• 
Whether the new email must be verified.  
• 
Whether the old email remains active until verification.  
• 
Whether changing the email logs the user out.  

• 
Whether additional security verification is required.  
None of these behaviors should be assumed without product verification. 
41. New Email Address Is Not Verified 
If a user changes their email address and the new email remains unverified, the AI should 
distinguish this from initial account registration. 
The troubleshooting flow should be: 
Confirm email-change workflow → Confirm new email → Check verification message → 
Resend if available → Complete verification → Confirm account status → Escalate if 
unresolved. 
 
42. Already Verified Email 
If the application says the email is already verified, the AI should not instruct the user to 
repeatedly verify it. 
Instead, the AI should determine the user's actual problem. 
For example: 
"My email is already verified but I still can't log in." 
This is a login/account-access issue, not necessarily an email-verification issue. 
The AI should transfer the conversation to the appropriate login-support intent. 
 
43. Verification Email Expired 
If the user says: 
"The verification email expired." 
the AI should: 
1. Confirm whether the application indicates expiration.  
2. Guide the user to the approved resend process.  
3. Ask them to use the newest verification message.  
4. Escalate if the resend process does not work.  

The exact expiration period must be verified before being included in AI responses. 
 
44. Verification Request Expired 
A verification request itself may have a limited lifetime depending on the implementation. 
If WiseIN supports this behavior, the AI should distinguish: 
Expired Email 
from 
Expired Verification Link 
from 
Expired Verification Code 
from 
Expired Verification Request 
These may represent different technical states. 
The exact definitions must be confirmed by Engineering. 
 
45. Multiple Accounts and Same Email 
The AI should not assume whether WiseIN allows: 
• 
One email per account  
• 
Multiple accounts using the same email  
• 
Reuse of a previously verified email  
• 
Organization and individual accounts using the same email  
These rules must be documented by the Product team. 
If a user reports an email conflict, the AI should ask for the exact application message and 
escalate if the behavior is not documented. 
 
46. Temporary Email and Disposable Email Addresses 

The AI should follow the official WiseIN policy regarding temporary, disposable, or 
restricted email addresses. 
The AI must not invent a list of blocked email providers. 
If WiseIN has an approved policy, the AI should retrieve it from the latest documentation. 
 
47. Work, College and Personal Email 
Users may use different types of email addresses depending on WiseIN's supported 
account and verification requirements. 
Examples may include: 
• 
Personal email  
• 
Work email  
• 
College email  
• 
Organization email  
The AI must not state that a particular email type is accepted or rejected unless this is 
documented. 
For student verification specifically, WiseIN's broader documentation identifies college 
email as part of some global student-verification information, but email verification for 
account access should not be confused with student verification.  
 
48. Email Verification and Student Verification 
The AI must clearly distinguish these processes. 
Email Verification 
Confirms access to an email address. 
Student Verification 
Confirms eligibility as a student through the applicable WiseIN student-verification 
process. 
A user may have a verified email but still need to complete student verification. 

Likewise, student-verification requirements should not automatically be presented as 
email-verification requirements. 
 
49. Email Verification and Identity Verification 
Email verification does not independently establish a user's government identity. 
Identity verification is a separate WiseIN process. 
The AI must not tell a user: 
"Your email is verified, so your identity is verified." 
That statement is incorrect unless an approved WiseIN process explicitly establishes such 
a relationship. 
 
50. Email Verification and Verified Badge 
An email verification status should not automatically be treated as equivalent to a WiseIN 
verified profile badge. 
The AI must distinguish: 
• 
Email verified  
• 
Identity verified  
• 
Student verified  
• 
Organization verified  
• 
Verified badge  
The broader WiseIN documentation states that verification badges represent the 
applicable approved verification status and must not be interpreted beyond their verified 
scope.  
51. Email Verification Troubleshooting Decision Flow 
The AI should use the following decision process. 
User reports an email-verification problem 
↓ 

Identify the platform 
Web / Android / iOS 
↓ 
Identify the problem 
Did not receive email / received email but link failed / code failed / expired / wrong email / 
verification status not updated / unknown error 
↓ 
Ask for exact error message where relevant 
↓ 
Check approved knowledge base 
↓ 
Provide verified troubleshooting 
↓ 
Ask whether the problem is resolved 
↓ 
If resolved: 
End the support flow 
If unresolved: 
Collect minimum required diagnostic information 
↓ 
Escalate to human support 
This follows the WiseIN AI-support troubleshooting model of identifying the issue, 
collecting relevant context, retrieving approved documentation, providing verified 
guidance, confirming the result, and escalating unresolved issues.  
 
52. AI Intent Categories for Email Verification 
The RAG system should classify email-verification questions into appropriate intents. 

EMAIL_VERIFICATION_GENERAL 
User asks what email verification is. 
EMAIL_VERIFICATION_REQUIRED 
User asks whether email verification is required. 
EMAIL_VERIFICATION_PROCESS 
User asks how to verify their email. 
EMAIL_NOT_RECEIVED 
User did not receive the verification email. 
EMAIL_IN_SPAM 
User found or expects the verification message in spam/junk. 
EMAIL_WRONG_ADDRESS 
User entered the wrong email address. 
EMAIL_CHANGE_VERIFICATION 
User changed their email and needs to verify the new address. 
EMAIL_RESEND 
User wants another verification email. 
EMAIL_VERIFICATION_LINK 
User has a problem with the verification link. 
EMAIL_LINK_EXPIRED 
Verification link has expired. 
EMAIL_LINK_INVALID 
Verification link is invalid. 
EMAIL_LINK_ALREADY_USED 
Verification link has already been used. 
EMAIL_CODE_FAILED 
Verification code does not work. 

EMAIL_CODE_EXPIRED 
Verification code has expired. 
EMAIL_CODE_NOT_RECEIVED 
Verification code was not received. 
EMAIL_VERIFICATION_FAILED 
Generic verification failure. 
EMAIL_VERIFICATION_STATUS 
User wants to know whether their email is verified. 
EMAIL_VERIFICATION_NOT_UPDATED 
User completed verification but account still shows unverified. 
EMAIL_VERIFICATION_SECURITY 
User reports a suspicious verification email or security concern. 
EMAIL_VERIFICATION_UNKNOWN_ERROR 
User reports an undocumented error. 
EMAIL_VERIFICATION_ESCALATION 
User needs human support after troubleshooting fails. 
 
53. Example User Questions the AI Must Understand 
The AI should understand different natural-language versions of the same request. 
Examples: 
• 
"How do I verify my email?"  
• 
"Where is the verification email?"  
• 
"I didn't get the email."  
• 
"WiseIN didn't send me the verification email."  
• 
"The verification mail isn't coming."  
• 
"I checked spam but nothing is there."  

• 
"Can you resend the verification email?"  
• 
"My verification link doesn't work."  
• 
"The link expired."  
• 
"The verification link is invalid."  
• 
"I already clicked the link."  
• 
"My email says verified but WiseIN says unverified."  
• 
"I entered the wrong email."  
• 
"Can I change my email?"  
• 
"My verification code isn't working."  
• 
"I didn't get the verification code."  
• 
"My verification code expired."  
• 
"Email verification failed."  
• 
"Why do I need to verify my email?"  
• 
"Is email verification mandatory?"  
• 
"I verified my email but can't login."  
• 
"Someone else received a WiseIN verification email."  
• 
"I received a suspicious WiseIN email."  
• 
"My account is stuck on email verification."  
• 
"I cannot complete email verification."  
 
54. Example AI Response – Email Not Received 
User: 
"I didn't receive the WiseIN verification email." 
AI: 
"I can help you troubleshoot that. First, please check that the email address entered during 
registration is correct. Then check your Inbox, Spam/Junk, Promotions, or other filtered 
folders for the WiseIN verification message. If WiseIN shows a Resend Verification option, 

you can request another verification email. If you still do not receive it, tell me the exact 
message shown on the WiseIN screen and whether you're using the web, Android, or iOS 
version so I can guide you with the appropriate verified troubleshooting steps." 
The AI should not claim a specific delivery time unless WiseIN has officially documented 
one. 
 
55. Example AI Response – Link Expired 
User: 
"My WiseIN verification link expired." 
AI: 
"If WiseIN is showing that the verification link has expired, please use the available Resend 
Verification option to request a new verification message and use the latest verification 
link. If you don't see a resend option or the new link also fails, please share the exact error 
message and the platform you're using so the issue can be investigated." 
 
56. Example AI Response – Verification Completed but Status Not Updated 
User: 
"I clicked the verification link but my account still says unverified." 
AI: 
"If you completed the verification process but WiseIN still shows your email as unverified, 
please check the exact status currently displayed and refresh or reopen the relevant 
WiseIN page if appropriate. If the status remains inconsistent, this may require account-
specific investigation. I can help collect the relevant details for WiseIN Support." 
The AI must not say: 
"Your email is definitely verified." 
unless an authorized system confirms it. 
 
57. Example AI Response – Wrong Email 
User: 

"I entered the wrong email while signing up." 
AI: 
"I can help you determine the next step. Are you still on the registration process, or has the 
WiseIN account already been created? The available options may differ depending on the 
current account state. Please don't share your password or verification code." 
 
58. Example AI Response – Verification Code 
User: 
"My verification code isn't working." 
AI: 
"Please check whether WiseIN shows an error such as an invalid or expired code. If a new-
code or resend option is available, use the latest verification code. Please do not send the 
verification code to me or anyone else. If the issue continues, share the exact error 
message and the platform you're using." 
 
59. Example AI Response – Escalation 
User: 
"I tried everything and still can't verify my email." 
AI: 
"I've gone through the available troubleshooting steps. Since the issue is still unresolved, it 
may require account-specific investigation by WiseIN Support. Please use the official 
WiseIN support channel: [VERIFIED SUPPORT DETAILS]. When contacting support, include 
the exact error message, platform, approximate time of the issue, and the steps you 
already tried. Do not include your password, OTP, or verification code." 
 
60. Human Support Escalation 
Email-verification issues should be escalated when: 
• 
The verification email is repeatedly not received.  
• 
Resend functionality does not work.  

• 
The verification link repeatedly fails.  
• 
The verification code repeatedly fails.  
• 
The verification status does not update.  
• 
The application displays an undocumented error.  
• 
The account appears to be in an inconsistent state.  
• 
The user entered incorrect account information and cannot correct it through the 
approved workflow.  
• 
The issue requires backend investigation.  
• 
The issue involves suspicious activity.  
• 
The issue involves another person's account.  
• 
The AI does not have sufficient verified information.  
• 
The user has followed the approved troubleshooting process without resolution.  
WiseIN's support framework requires human escalation when documented 
troubleshooting is insufficient, when account-specific information or technical 
investigation is required, or when the knowledge base does not contain enough information 
to provide an accurate answer. 
61. Information to Include in an Escalation 
A support escalation should contain only the information necessary for investigation. 
Recommended information includes: 
• 
Account identifier through an authorized internal system.  
• 
Platform.  
• 
Device.  
• 
Browser or application version.  
• 
Email-verification stage.  
• 
Exact error message.  
• 
Approximate date and time.  
• 
Steps already attempted.  

• 
Whether the verification email was received.  
• 
Whether the user checked spam/junk.  
• 
Whether resend was attempted.  
• 
Whether the problem is recurring.  
• 
Relevant conversation context.  
• 
Non-sensitive diagnostic information.  
Sensitive information should not be attached unless the official WiseIN support process 
explicitly requires it through a secure channel.  
 
62. AI Customer Support Boundaries 
The WiseIN AI Customer Support System may: 
• 
Explain email verification.  
• 
Explain the difference between email verification and other verification types.  
• 
Guide users through approved email-verification workflows.  
• 
Troubleshoot documented email-verification problems.  
• 
Identify likely support categories.  
• 
Ask relevant troubleshooting questions.  
• 
Provide verified support information.  
• 
Escalate unresolved issues.  
The AI must not: 
• 
Verify an email manually.  
• 
Mark an account as verified.  
• 
Modify account verification status.  
• 
Approve or reject identity verification.  
• 
Bypass email verification.  
• 
Generate or reveal verification codes.  

• 
Reveal verification tokens.  
• 
Request passwords.  
• 
Request OTPs.  
• 
Request authentication codes.  
• 
Claim verification is complete without system confirmation.  
• 
Invent verification requirements.  
• 
Invent error codes.  
• 
Invent support contact details.  
The broader WiseIN AI-support framework requires the AI to use verified knowledge, avoid 
unsupported claims, and escalate issues beyond its authority.  
 
63. Backend and Real-Time Verification 
If the future WiseIN AI chatbot is connected to authorized backend tools, it may be able to 
retrieve account-specific information such as: 
• 
Current email-verification status.  
• 
Account state.  
• 
Verification workflow state.  
• 
Available account actions.  
Such access must be controlled through authentication and authorization. 
The AI should only access information that the authenticated user is authorized to see. 
The AI must never directly access the database without an approved application/API layer. 
The AI must never claim to have checked an account when no authorized backend tool has 
actually returned the information. 
 
64. Privacy Requirements 
Email addresses are personal information and should be handled carefully. 
The AI should: 

• 
Collect only necessary information.  
• 
Avoid exposing email addresses unnecessarily.  
• 
Avoid revealing another user's email address.  
• 
Avoid storing unnecessary sensitive information in support conversations.  
• 
Follow WiseIN's privacy and retention policies.  
• 
Use authorized backend systems for account-specific information.  
 
65. Security Requirements 
The email-verification system should be protected against: 
• 
Verification-token leakage  
• 
Account takeover attempts  
• 
Unauthorized verification  
• 
Verification-link abuse  
• 
Brute-force code attempts  
• 
Automated resend abuse  
• 
Enumeration of registered accounts  
• 
Phishing  
• 
Session abuse  
• 
Unauthorized account changes  
The exact technical security controls must be documented by Engineering and Security. 
The AI must not expose internal security mechanisms that could help users bypass or 
attack the verification system. 
 
66. QA Testing Requirements 
Before this document becomes authoritative RAG knowledge, QA should test the complete 
email-verification workflow. 
Registration Testing 

• 
New account with valid email.  
• 
New account with invalid email.  
• 
New account with incorrectly entered email.  
• 
Registration without completing verification.  
• 
Registration followed by successful verification.  
Email Delivery Testing 
• 
Verification email received.  
• 
Verification email delayed.  
• 
Verification email sent to correct address.  
• 
Email found in spam.  
• 
Email not received.  
• 
Resend verification.  
Link Testing 
• 
Valid link.  
• 
Expired link.  
• 
Invalid link.  
• 
Already-used link.  
• 
Multiple verification links.  
• 
Old link after requesting a new link.  
Code Testing 
If code-based verification exists: 
• 
Correct code.  
• 
Incorrect code.  
• 
Expired code.  
• 
Resend code.  
• 
Multiple code requests.  

• 
Invalid code format.  
• 
Retry limits.  
Account-State Testing 
• 
Verified email.  
• 
Unverified email.  
• 
Pending verification.  
• 
Verification completed but status not updated.  
• 
Already verified email.  
• 
Account recovery involving email verification.  
Platform Testing 
• 
Web.  
• 
Android.  
• 
iOS.  
WiseIN's platform documentation specifically requires QA validation of sign-up, login, OTP, 
and verification workflows across supported platforms.  
 
67. Product and Engineering Verification Checklist 
Before marking this document Approved, the WiseIN team should verify: 
1. Whether email verification is mandatory.  
2. When email verification occurs.  
3. Exact registration workflow.  
4. Exact email-verification screen.  
5. Exact button names.  
6. Exact email-verification message.  
7. Official sender email address.  
8. Email subject.  

9. Verification-link behavior.  
10. Verification-code behavior, if applicable.  
11. Code expiry time.  
12. Link expiry time.  
13. Resend behavior.  
14. Resend cooldown.  
15. Maximum resend attempts.  
16. Maximum verification attempts.  
17. Behavior after multiple verification requests.  
18. Behavior of old verification links.  
19. Behavior of old verification codes.  
20. Wrong-email correction process.  
21. Email-change workflow.  
22. Already-verified behavior.  
23. Account state before verification.  
24. Account state after verification.  
25. Login behavior for unverified accounts.  
26. Password-recovery relationship.  
27. Platform-specific differences.  
28. Exact error messages.  
29. Error codes, if any.  
30. Account-security behavior.  
31. Rate limiting.  
32. Abuse prevention.  
33. Official support process.  
34. Official support email.  

35. Official support phone/WhatsApp if applicable.  
36. Official support URL.  
37. Support hours.  
38. Support escalation procedure.  
 
68. Knowledge-Base Requirements for RAG 
Every email-verification knowledge entry should contain: 
Knowledge ID 
Unique identifier. 
Feature 
Email Verification. 
User Intent 
The reason the user is asking for help. 
User Problem 
The user's reported problem. 
Symptoms 
What the user sees. 
Expected Behavior 
What should happen. 
Actual Behavior 
What happened instead. 
Resolution 
Verified solution. 
Platform 
Web, Android, iOS, or all supported platforms. 
Authentication Context 

Registration, login, account recovery, email change, or other workflow. 
Security Level 
Normal support or security-sensitive. 
Escalation Criteria 
When human support is required. 
Source 
Approved WiseIN documentation, application testing, engineering confirmation, or support 
documentation. 
Verification Status 
Draft, Reviewed, Approved, Deprecated. 
Last Verified 
Date of the latest product verification. 
This structure allows the RAG system to retrieve the most relevant troubleshooting 
information instead of returning unrelated email-verification content. 
 
69. Suggested RAG Retrieval Examples 
When a user asks: 
"I didn't receive my verification email." 
The system should retrieve: 
EMAIL_NOT_RECEIVED 
and relevant knowledge about: 
• 
Correct email  
• 
Spam/junk  
• 
Resend  
• 
Delivery troubleshooting  
• 
Escalation  
When a user asks: 

"My verification link expired." 
The system should retrieve: 
EMAIL_LINK_EXPIRED 
and relevant information about: 
• 
Expiration  
• 
Resend  
• 
Latest verification link  
• 
Escalation  
When a user asks: 
"I verified my email but it still says unverified." 
The system should retrieve: 
EMAIL_VERIFICATION_NOT_UPDATED 
and relevant information about: 
• 
Account state  
• 
Status refresh  
• 
Verification inconsistency  
• 
Human escalation  
When a user asks: 
"I entered the wrong email." 
The system should retrieve: 
EMAIL_WRONG_ADDRESS 
and the approved email-correction workflow. 
 
70. Relationship With Other WiseIN Documents 
This document should work together with: 

WISEIN-OVERVIEW-001 
WiseIN Complete Platform User Guide & Operational Documentation. 
WISEIN-TERM-002 
WiseIN Terminology & Glossary. 
WISEIN-LOGIN-003 
WiseIN Login & Account Access Documentation. 
WISEIN-SIGNUP-005 
WiseIN Sign-Up Documentation. 
WISEIN-VERIFICATION-006 
WiseIN Identity, Student and Organization Verification Documentation. 
WISEIN-SECURITY-007 
WiseIN Security & Privacy Documentation. 
WISEIN-SUPPORT-008 
WiseIN Customer Support & Troubleshooting Documentation. 
WISEIN-AI-009 
WiseIN AI Customer Support System Documentation. 
The AI should retrieve the appropriate document based on the user's actual intent. 
For example: 
"I can't log in" 
→ Login Documentation. 
"I didn't receive the verification email" 
→ Email Verification Documentation. 
"Why do I need Aadhaar verification?" 
→ Identity Verification Documentation. 
"How do I prove I'm a student?" 
→ Student Verification Documentation. 
 
 

71. Important AI Decision Rules 
The AI should follow these rules for all email-verification conversations. 
Rule 1: Identify the user's actual problem before giving instructions. 
Rule 2: Distinguish email verification from identity, student, and organization verification. 
Rule 3: Ask for the platform when troubleshooting may differ. 
Rule 4: Ask for the exact error message when necessary. 
Rule 5: Use only approved WiseIN information. 
Rule 6: Never invent a button name. 
Rule 7: Never invent an error code. 
Rule 8: Never invent an expiration period. 
Rule 9: Never invent resend limits. 
Rule 10: Never invent support contact information. 
Rule 11: Never ask for passwords. 
Rule 12: Never ask for OTPs or verification codes. 
Rule 13: Never expose verification tokens. 
Rule 14: Never claim that an email is verified without confirmation. 
Rule 15: Never claim that another user's email or account exists. 
Rule 16: Never bypass verification. 
Rule 17: Do not repeatedly provide troubleshooting steps that have already failed. 
Rule 18: Escalate unresolved or account-specific problems. 
Rule 19: Provide the minimum necessary information to human support. 
Rule 20: Always use the latest approved documentation. 
These rules follow the broader WiseIN AI-support requirement that the AI use current 
authoritative information, distinguish similar concepts, and avoid inventing product 
behavior.  
 
72. Common User Problem → AI Action Mapping 

User: "How do I verify my email?" 
AI Action: Explain the verified email-verification workflow. 
User: "I didn't receive the email." 
AI Action: Check email address → inbox/spam → resend if available → escalate if 
unresolved. 
User: "The link doesn't work." 
AI Action: Ask for the exact error → determine whether expired/invalid/already used → 
provide verified solution. 
User: "The link expired." 
AI Action: Use the approved resend process. 
User: "I entered the wrong email." 
AI Action: Determine account state → provide approved correction workflow or escalate. 
User: "My verification code isn't working." 
AI Action: Determine invalid/expired/new-code issue → provide verified troubleshooting. 
User: "It says verified but my account still says unverified." 
AI Action: Treat as verification-status inconsistency → troubleshoot → escalate if 
unresolved. 
User: "I verified my email but can't login." 
AI Action: Switch from email-verification intent to login/account-access troubleshooting. 
User: "I received a suspicious WiseIN verification email." 
AI Action: Treat as security-sensitive → do not encourage clicking suspicious links → use 
approved security/support process. 
 
73. Final Email Verification Objective 
The objective of WISEIN-EMAIL-VERIFICATION-004 is to enable the WiseIN AI Customer 
Support System to understand the complete lifecycle of email verification. 
When a user reports an email-verification problem, the AI should be able to: 

Identify the user's platform → Identify the verification stage → Identify the exact 
problem → Retrieve the relevant knowledge → Provide verified troubleshooting → 
Protect sensitive information → Confirm whether the problem is resolved → Escalate 
when required. 
The AI should be capable of handling common situations such as: 
• 
Email not received.  
• 
Email in spam.  
• 
Incorrect email address.  
• 
Resend verification.  
• 
Expired verification link.  
• 
Invalid verification link.  
• 
Already-used verification link.  
• 
Verification code failure.  
• 
Expired verification code.  
• 
Verification failure.  
• 
Verification status not updated.  
• 
Email change verification.  
• 
Login blocked by an unresolved verification issue.  
• 
Suspicious verification email.  
• 
Account-specific verification problems.  
The AI must prioritize: 
Accuracy → Security → Privacy → Verified Product Information → Clear Troubleshooting 
→ Human Escalation 
rather than guessing when product information is unavailable 
 



---

