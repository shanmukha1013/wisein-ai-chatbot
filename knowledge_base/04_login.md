# Login

## Source: WISEIN – LOGIN & ACCOUNT ACCESS 004.pdf

WISEIN – LOGIN & ACCOUNT ACCESS DOCUMENTATION 
Document ID: WISEIN-LOGIN-003 
Document Type: Product Knowledge & AI Customer Support Documentation 
Version: 1.0 
Status: Draft – Pending Product, Engineering, QA, Security and Support Verification 
Platform: WiseIN 
1. Document Purpose 
This document defines WiseIN login, sign-in, authentication, account access, account 
recovery, session management, login troubleshooting, security requirements, and 
customer-support escalation procedures. 
The primary purpose of this document is to provide reliable knowledge for the WiseIN AI 
Customer Support System. 
The AI should use this document to understand questions such as: 
• 
How do I login to WiseIN?  
• 
How do I sign in?  
• 
I cannot login.  
• 
My login is not working.  
• 
I forgot my password.  
• 
I did not receive my OTP.  
• 
My OTP is not working.  
• 
Google login is not working.  
• 
I cannot access my account.  
• 
I see an unknown device.  
• 
How do I logout?  
• 
How can I check active sessions?  
• 
Someone may have accessed my account.  
• 
I tried everything but I still cannot login.  

The AI must use verified WiseIN information and must not invent unsupported login 
procedures or technical explanations. 
 
2. Login Definition 
Login, also called Sign In, is the process through which an existing WiseIN user accesses 
their account. 
Login is different from Sign Up. 
Sign Up is used to create a new WiseIN account. 
Login / Sign In is used to access an existing WiseIN account. 
A user generally needs a valid WiseIN account and the required authentication method to 
access account-protected functionality. 
 
3. WiseIN Access Platforms 
WiseIN is accessible through: 
• 
Web application  
• 
Android application  
• 
iOS application  
The exact login workflow may differ between platforms. 
The AI must ask the user which platform they are using when platform-specific 
troubleshooting may be required. 
The AI must not assume that a feature or login behavior is identical across Web, Android, 
and iOS. Complete web/mobile feature parity still requires product and QA verification.  
 
4. General Login Requirements 
Before troubleshooting a login issue, the AI should consider the following general 
requirements: 
• 
The user should have an existing WiseIN account.  
• 
The user should use the official WiseIN application or website.  

• 
The user should have a stable internet connection.  
• 
The user should use a supported platform.  
• 
The user should provide the required authentication information.  
• 
The user should satisfy any account, verification, permission, or security 
requirements that apply.  
For web access, the current documentation identifies a supported browser, stable internet 
connection, valid WiseIN account where authentication is required, and required 
permissions or eligibility for restricted features.  
 
5. Supported Login and Authentication Methods 
The exact currently supported login methods must be verified against the current WiseIN 
application. 
Authentication areas that should be covered by the final product documentation include: 
• 
Standard account sign-in  
• 
Password-based authentication, where applicable  
• 
OTP-based authentication, where applicable  
• 
Google authentication, where applicable  
• 
Additional supported authentication methods  
• 
Account recovery  
• 
Security verification  
• 
Two-factor authentication where enabled  
The AI must not claim that a particular authentication method is available unless that 
method has been verified in the current WiseIN application. 
 
6. Login Process 
The final exact login steps must be verified by the Product and Engineering teams. 
The general login process is: 

1. Open the official WiseIN platform.  
2. Select the available Sign In or Login option.  
3. Enter the required authentication information.  
4. Complete any required OTP, verification, or authentication step.  
5. After successful authentication, the user is granted access to their WiseIN account.  
The exact button names, fields, authentication sequence, redirects, error messages, and 
platform-specific behavior must be verified before being treated as authoritative 
instructions. 
The AI must not invent a button name or navigation path that is not present in the approved 
documentation. 
 
7. When a User Says "I Cannot Login" 
This is one of the most important chatbot support scenarios. 
When a user says: 
"I cannot login." 
or: 
"I am unable to sign in." 
the AI should not immediately provide a long generic response. 
The AI should first identify the problem. 
The recommended conversation flow is: 
Step 1 – Identify the Platform 
Ask: 
"Are you using WiseIN on the web, Android, or iOS?" 
Step 2 – Identify the Login Problem 
Determine whether the issue involves: 
• 
Password  
• 
OTP  

• 
Google Sign-In  
• 
Authentication error  
• 
Account recovery  
• 
Session problem  
• 
Application or browser issue  
• 
Unknown error  
Step 3 – Ask for the Exact Error 
If an error appears, ask: 
"What exact error message do you see when you try to log in?" 
Step 4 – Provide Verified Troubleshooting 
Use the relevant approved troubleshooting instructions from the knowledge base. 
Step 5 – Confirm the Result 
After providing the steps, ask: 
"Did this resolve the login issue?" 
Step 6 – Escalate if Required 
If the problem continues, direct the user to the official WiseIN customer-support process. 
The general WiseIN troubleshooting process follows issue identification, relevant context 
collection, approved knowledge-base retrieval, verified guidance, result confirmation, and 
human escalation when necessary. 
8. Basic Login Troubleshooting 
When a user cannot login, the AI may provide the following general troubleshooting steps 
where applicable: 
1. Check that the internet connection is stable.  
2. Confirm that the user is using the correct WiseIN account.  
3. Confirm that the required login information is entered correctly.  
4. If OTP authentication is being used, check the registered contact information and 
use the available resend option if supported.  

5. If using Google Sign-In, retry the authentication process and note the exact error 
message if it fails.  
6. If using the web application, retry using a supported browser.  
7. If using the mobile application, ensure the application is updated if an update is 
available.  
8. Close and reopen the application or browser and retry.  
9. If the problem continues, collect the exact error message and platform information.  
10. Escalate the issue to WiseIN customer support when the documented 
troubleshooting does not resolve it.  
The AI should only provide steps that have been verified for the relevant WiseIN platform 
and current application version. 
 
9. Login Troubleshooting – Platform Identification 
The AI should identify the user's platform before giving platform-specific instructions. 
The user may be using: 
Web 
The AI should consider browser compatibility, internet connection, login page behavior, 
and web-specific errors. 
Android 
The AI should consider the installed application version, network connection, 
authentication behavior, and Android-specific errors. 
iOS 
The AI should consider the installed application version, network connection, 
authentication behavior, and iOS-specific errors. 
The AI must not assume that the same troubleshooting steps apply identically to every 
platform.  
 
10. Password Problems 

If password-based authentication is supported, users may experience problems such as: 
• 
Incorrect password  
• 
Forgotten password  
• 
Password reset problem  
• 
Password change problem  
• 
Password-related authentication failure  
The exact password-reset and password-change workflows must be verified by the WiseIN 
Product and Engineering teams. 
Until verified, the AI must not invent: 
• 
Password reset URLs  
• 
Password requirements  
• 
Password expiry periods  
• 
Reset-token validity  
• 
Password recovery methods  
• 
Password retry limits  
 
11. Forgotten Password 
If a user says: 
"I forgot my password." 
the AI should identify the officially supported password-recovery process. 
Once the exact WiseIN workflow has been verified, the AI should provide clear ordered 
instructions. 
The final approved process should cover: 
1. Where the user starts password recovery.  
2. What information the user provides.  
3. How the user verifies account ownership.  
4. How the user creates a new password.  

5. What confirmation is displayed.  
6. How the user returns to the login screen.  
7. What to do if the recovery process fails.  
The AI must not ask the user to provide their current password. 
 
12. OTP 
OTP means One-Time Password. 
An OTP is a temporary authentication or verification code. 
OTP-related login problems may include: 
• 
OTP not received  
• 
OTP delayed  
• 
Incorrect OTP  
• 
Expired OTP  
• 
OTP resend problem  
• 
Too many OTP requests  
• 
OTP verification failure  
The exact OTP expiry period, resend limits, retry limits, delivery method, and error 
messages must be verified by the Product and Engineering teams. 
 
13. User Did Not Receive OTP 
If the user says: 
"I didn't receive my OTP." 
the AI should: 
1. Confirm which WiseIN platform the user is using.  
2. Confirm that the user is using the correct registered contact information.  
3. Suggest the officially supported resend option if available.  

4. Ask the user to wait according to the officially documented OTP behavior.  
5. Ask for the exact error message if one appears.  
6. Provide additional verified troubleshooting if available.  
7. Escalate if the OTP continues to fail.  
The AI must never ask the user to send or paste their OTP. 
 
14. Incorrect or Expired OTP 
If the user says: 
"My OTP is not working." 
the AI should determine whether the OTP is: 
• 
Incorrect  
• 
Expired  
• 
Not received  
• 
Rejected  
• 
Blocked because of retry limits  
The AI should provide only verified instructions for the specific condition. 
The AI must not guess the OTP expiry duration or retry limit. 
 
15. Google Sign-In 
Google authentication is identified as an authentication topic in the WiseIN 
documentation. 
However, the exact Google Sign-In workflow and availability must be verified against the 
current application. 
The AI should not assume: 
• 
Google Sign-In is available to every user.  
• 
Google Sign-In behaves identically on all platforms.  
• 
Google authentication automatically creates an account.  

• 
Google authentication bypasses other WiseIN verification requirements.  
 
16. Google Login Error 
If a user says: 
"Google login is not working." 
the AI should: 
1. Ask whether they are using Web, Android, or iOS.  
2. Ask for the exact error message.  
3. Provide approved Google-login troubleshooting.  
4. Ask the user to retry.  
5. Escalate if the problem continues.  
The AI must not claim a specific technical cause without verification. 
 
17. "Failed to Fetch" During Login 
If the user reports: 
"Failed to Fetch" 
during Google authentication or another login operation, the AI should not immediately 
claim a specific technical cause. 
The error may indicate a connection or service-related problem, but the exact technical 
cause requires investigation. 
The AI should: 
1. Identify the platform.  
2. Record the exact error message.  
3. Ask whether the problem occurs repeatedly.  
4. Check approved troubleshooting documentation.  
5. Provide verified steps.  
6. Escalate if unresolved.  

 
18. Account Recovery 
Account recovery is the process of helping an existing user regain access to their WiseIN 
account when normal login is not possible. 
Possible account-recovery situations include: 
• 
Forgotten password  
• 
Lost access to registered contact information  
• 
OTP problems  
• 
Authentication problems  
• 
Suspicious account activity  
• 
Locked or restricted account  
• 
Session problems  
• 
Other documented access problems  
The exact recovery process must be verified by the WiseIN team. 
 
19. Session 
A session represents an authenticated period during which a user is signed in to WiseIN. 
WiseIN's Settings documentation identifies Sign in & Security and Active Sessions as 
account-security functionality. 
The AI should distinguish between: 
Login: Starting an authenticated account session. 
Session: The period during which the user remains authenticated. 
Logout: Ending the current authenticated session. 
 
20. Active Sessions 
WiseIN Settings includes an Active Sessions area under Sign in & Security. 
Active Sessions allows users to review active login sessions associated with their account. 

The current documentation also identifies individual session logout functionality. 
The AI should use the verified WiseIN navigation when explaining this feature and must not 
invent additional session-management controls.  
 
21. Logout 
WiseIN provides a Log Out option. 
Selecting Log Out opens a confirmation dialog. 
The documented confirmation contains: 
"Logout from your account?" 
The available actions are: 
Cancel 
Closes the confirmation without logging the user out. 
Logout 
Confirms the action and logs the user out. 
 
22. Sign In & Security 
WiseIN Settings includes a Sign in & Security section. 
The documented security area includes: 
• 
SMS text-message security options  
• 
Authenticator application codes  
• 
Active Sessions  
• 
Individual session logout  
The exact setup and authentication behavior should be verified against the current 
application before being used for detailed AI instructions. 
 
23. Two-Factor Authentication 
Two-Factor Authentication, or 2FA, provides an additional layer of account protection. 

WiseIN documentation identifies authentication-security controls involving SMS and 
authenticator applications. 
The AI should explain 2FA only according to the currently approved WiseIN 
implementation. 
The AI must not provide instructions for bypassing or disabling security controls unless an 
authorized WiseIN workflow explicitly supports the action. 
 
24. Suspicious Login 
A suspicious login may involve: 
• 
An unfamiliar device  
• 
An unfamiliar active session  
• 
Unexpected account activity  
• 
An unexpected security change  
• 
A user believing another person accessed their account  
If a user reports suspicious activity, the AI should treat the issue as security-sensitive. 
The AI should direct the user toward verified security controls and human support when 
required. 
 
25. Suspected Account Compromise 
If the user says: 
"Someone accessed my account." 
or: 
"I think someone logged into my account." 
the AI should: 
1. Treat the issue as a security concern.  
2. Never request the user's password.  
3. Never request an OTP or authentication code.  

4. Direct the user to verified security controls.  
5. Recommend reviewing Active Sessions where available.  
6. Follow the approved account-security process.  
7. Escalate to human support if required.  
The AI must not claim that the account has been secured unless an authorized system 
confirms the action. 
 
26. Information the AI May Request During Troubleshooting 
The AI should collect only the minimum information required to understand the problem. 
Relevant information may include: 
• 
Platform  
• 
Device type  
• 
Operating system  
• 
Browser or application version  
• 
Feature affected  
• 
Exact error message  
• 
Steps already attempted  
• 
Whether the issue is temporary or recurring  
• 
Relevant non-sensitive screenshots  
The WiseIN troubleshooting documentation specifically recommends collecting the 
feature/page, reproduction steps, error message or visible behavior, device/platform 
information, and whether the problem is temporary, recurring, or persistent.  
 
27. Information the AI Must Never Request 
The AI must never ask users to provide: 
• 
Passwords  
• 
OTPs  

• 
Authentication codes  
• 
Private keys  
• 
Payment credentials  
• 
Sensitive authentication tokens  
• 
Unnecessary identity documents  
• 
Other confidential security information  
The AI must not request passwords, OTPs, or biometric information through customer-
support chat.  
 
28. Login Error Handling 
When the user reports a login error, the AI should follow this process: 
Identify → Understand → Retrieve → Troubleshoot → Confirm → Escalate 
Identify 
Determine the affected platform and login method. 
Understand 
Determine what the user was trying to do and what happened. 
Retrieve 
Search the approved WiseIN knowledge base for the relevant login error or troubleshooting 
procedure. 
Troubleshoot 
Provide clear, ordered, verified steps. 
Confirm 
Ask whether the issue has been resolved. 
Escalate 
If the problem remains unresolved, direct the user to human support. 
The AI should avoid repeatedly providing the same unsuccessful instructions.  
 

29. When Login Issues Require Human Support 
The AI should escalate a login issue when: 
• 
The documented troubleshooting steps do not resolve the issue.  
• 
The problem requires account-specific information.  
• 
Backend investigation is required.  
• 
The account appears compromised.  
• 
The issue involves security or privacy.  
• 
The user cannot complete account recovery.  
• 
The error is not documented.  
• 
The AI does not have enough verified information.  
• 
The problem appears to be a recurring or widespread application failure.  
These conditions are consistent with WiseIN's documented human-support escalation 
process.  
 
30. Customer Support Details 
If the AI cannot resolve a login problem, it should provide the official WiseIN customer-
support channels. 
The final approved document must contain the actual verified WiseIN support details: 
Official WiseIN Support Page: 
[TO BE VERIFIED] 
Support Email: 
[TO BE VERIFIED] 
Phone / WhatsApp: 
[TO BE VERIFIED] 
Live Chat: 
[TO BE VERIFIED] 
Support Hours: 
[TO BE VERIFIED] 

Support Ticket System: 
[TO BE VERIFIED] 
Only officially verified contact information should be added. 
The AI must never invent a support email address, phone number, WhatsApp number, 
support URL, ticket number, or support operating hours. 
31. Login Support Conversation Flow 
A standard conversation should follow this pattern. 
User: 
"I am unable to login." 
AI: 
"I can help you troubleshoot your WiseIN login issue. Are you using WiseIN on the web, 
Android, or iOS?" 
User: 
"Android." 
AI: 
"What happens when you try to sign in? If you see an error message, please share the exact 
message. Please do not share your password, OTP, or authentication code." 
User: 
"It says login failed." 
AI: 
"Please check that your internet connection is stable and that you are using the correct 
login information. If WiseIN requests an OTP, use the available OTP process and request a 
new code if the resend option is available. Then try signing in again." 
AI: 
"Did this resolve the issue?" 
User: 
"No." 
AI: 
"If the issue continues after the documented troubleshooting steps, this requires further 
support. Please contact WiseIN through the official support channel: [VERIFIED SUPPORT 
DETAILS]." 

This flow is intended as a knowledge-base pattern. The exact troubleshooting steps should 
be selected based on the verified error and platform. 
 
32. Login Support – Common User Questions 
The AI should understand different ways users may describe the same problem. 
Users may say: 
• 
"I can't login."  
• 
"I can't log in."  
• 
"I am unable to login."  
• 
"I cannot sign in."  
• 
"Sign in isn't working."  
• 
"Login failed."  
• 
"Why can't I access my account?"  
• 
"My account isn't opening."  
• 
"I cannot access WiseIN."  
• 
"I am stuck on the login page."  
• 
"My login keeps failing."  
• 
"The login page isn't working."  
• 
"I am not receiving the login OTP."  
• 
"Google sign in isn't working."  
• 
"I forgot my password."  
• 
"I can't recover my account."  
• 
"Someone logged into my account."  
• 
"I don't recognize this device."  
These expressions should map to the appropriate login-support intent. 
 

33. AI Login Intent Categories 
The AI knowledge system should classify login-related questions into appropriate intents. 
LOGIN_ACCESS 
User wants to know how to access WiseIN. 
LOGIN_FAILED 
User cannot log in. 
PASSWORD_HELP 
User has a password-related problem. 
PASSWORD_RECOVERY 
User forgot their password or needs account recovery. 
OTP_NOT_RECEIVED 
User has not received an OTP. 
OTP_FAILED 
User's OTP is invalid, expired, or rejected. 
GOOGLE_LOGIN 
User has an issue with Google authentication. 
AUTHENTICATION_ERROR 
User receives an authentication-related error. 
ACCOUNT_RECOVERY 
User needs to regain access to their account. 
SESSION_ISSUE 
User has a problem involving an authenticated session. 
ACTIVE_SESSIONS 
User wants to know about active login sessions. 
LOGOUT 
User wants to log out. 

SUSPICIOUS_LOGIN 
User reports an unfamiliar login or device. 
ACCOUNT_COMPROMISED 
User believes their account has been accessed by someone else. 
LOGIN_PLATFORM_ISSUE 
Login behaves differently or fails on a particular platform. 
UNKNOWN_LOGIN_ERROR 
User reports an undocumented login problem. 
 
34. Account-Specific Login Information 
The AI may provide account-specific information only through authorized WiseIN backend 
systems or approved tools. 
Examples may include: 
• 
Account status  
• 
Active sessions  
• 
Authentication status  
• 
Verification status  
• 
Account restrictions  
The AI must verify authorization before accessing private account information. 
The AI must never claim that it checked an account, database, session, or backend system 
unless an authorized system actually returned that information.  
 
35. AI Security Boundaries 
The WiseIN AI Customer Support System is a support assistant. 
It is not an unrestricted account administrator. 
The AI may: 
• 
Explain login procedures.  

• 
Explain authentication concepts.  
• 
Guide users through verified workflows.  
• 
Troubleshoot documented login problems.  
• 
Identify the appropriate support category.  
• 
Escalate unresolved problems.  
The AI must not: 
• 
Bypass authentication.  
• 
Disable security controls without an authorized workflow.  
• 
Request passwords.  
• 
Request OTPs.  
• 
Request authentication codes.  
• 
Reveal private account information.  
• 
Change account-security settings without authorization.  
• 
Claim that an account has been secured without confirmation.  
• 
Claim that a support ticket was created without system confirmation.  
The AI's role as a first-level support system and its restriction from acting as an unrestricted 
account administrator are defined in the WiseIN AI-support documentation.  
 
36. Login Issue Escalation Information 
When a login issue is escalated to human support, the system should include the 
minimum relevant information required for investigation. 
This may include: 
• 
User account identifier through an authorized internal system  
• 
Platform  
• 
Device  
• 
Application/browser version  
• 
Login method  

• 
Exact error message  
• 
Approximate time of the issue  
• 
Steps already attempted  
• 
Whether the problem is recurring  
• 
Relevant conversation context  
• 
Non-sensitive diagnostic information  
The system must not include passwords, OTPs, authentication codes, or unnecessary 
sensitive information. 
 
37. Login Troubleshooting Knowledge Entry Requirements 
Every confirmed login issue added to the AI knowledge base should contain: 
Knowledge ID 
A unique identifier for the login knowledge entry. 
Feature 
Login, Sign In, OTP, Password, Google Authentication, Session, or Account Recovery. 
User Problem 
The user's reported problem. 
Symptoms 
The visible behavior or error message. 
Cause 
The confirmed technical cause, if known. 
Resolution 
The approved solution or troubleshooting procedure. 
Prerequisites 
Any required account, platform, permission, or authentication conditions. 
Platform 

Web, Android, iOS, or other supported platform. 
Escalation Criteria 
Conditions under which human support is required. 
Source 
Official documentation, application testing, engineering confirmation, or approved internal 
reference. 
Verification Status 
Draft, Reviewed, Approved, or Deprecated. 
Last Updated 
The date on which the information was last verified. 
These structured knowledge-entry principles align with the WiseIN AI support knowledge-
base requirements.  
 
38. QA Login Testing Requirements 
Before this document becomes an authoritative AI knowledge source, QA should test: 
Basic Login 
• 
Valid login  
• 
Invalid login  
• 
Empty fields  
• 
Incorrect credentials  
• 
Login failure  
• 
Successful login  
• 
Login redirect  
• 
Login cancellation  
Password 
• 
Correct password  
• 
Incorrect password  

• 
Forgotten password  
• 
Password recovery  
• 
Password reset  
• 
Password validation  
OTP 
• 
OTP delivery  
• 
OTP entry  
• 
Incorrect OTP  
• 
Expired OTP  
• 
OTP resend  
• 
Multiple OTP requests  
• 
OTP failure  
Google Authentication 
• 
Successful Google authentication  
• 
Cancelled Google authentication  
• 
Failed Google authentication  
• 
Existing account  
• 
New account  
• 
"Failed to Fetch"  
Sessions 
• 
Session creation  
• 
Session persistence  
• 
Session expiry  
• 
Logout  
• 
Active Sessions  
• 
Individual session logout  

Security 
• 
2FA  
• 
SMS authentication  
• 
Authenticator application  
• 
Suspicious login  
• 
Account recovery  
• 
Account compromise  
Platforms 
• 
Web  
• 
Android  
• 
iOS  
The master documentation specifically calls for sign-up/login, OTP, and verification 
workflows to be tested across supported platforms.  
 
39. Product-Team Verification Requirements 
Before this document is marked Approved, the WiseIN team should verify: 
1. Official login URL.  
2. Login button name.  
3. Login fields.  
4. Supported authentication methods.  
5. Password requirements.  
6. Forgot-password workflow.  
7. Password-reset workflow.  
8. OTP usage.  
9. OTP delivery method.  
10. OTP expiry.  

11. OTP resend behavior.  
12. OTP retry limits.  
13. Google authentication availability.  
14. Other authentication methods.  
15. Account-recovery workflow.  
16. Session duration.  
17. Session-expiry behavior.  
18. Active Sessions behavior.  
19. Logout behavior.  
20. Two-factor authentication.  
21. SMS authentication.  
22. Authenticator application.  
23. Suspicious-login behavior.  
24. Account-lock behavior.  
25. Login error messages.  
26. Login rate limits.  
27. Web login behavior.  
28. Android login behavior.  
29. iOS login behavior.  
30. Official customer-support contact details.  
 
40. Important AI Rules 
The WiseIN AI Customer Support System must follow these rules for login-related 
questions: 
Rule 1: Use the latest approved WiseIN documentation. 
Rule 2: Do not invent login steps. 

Rule 3: Ask for the platform when troubleshooting may differ. 
Rule 4: Ask for the exact error message when necessary. 
Rule 5: Give troubleshooting steps in a clear order. 
Rule 6: Do not repeatedly provide the same failed solution. 
Rule 7: Never request passwords, OTPs, authentication codes, or other confidential 
credentials. 
Rule 8: Never claim a technical cause unless it has been verified. 
Rule 9: Never claim that an account was checked unless an authorized backend system 
actually provided the information. 
Rule 10: Escalate unresolved, account-specific, security-sensitive, or undocumented 
problems. 
Rule 11: Provide only verified official WiseIN customer-support details. 
Rule 12: Never invent support contact information. 
Rule 13: Never claim that a support ticket has been created unless the support system 
confirms it. 
Rule 14: Never promise a resolution time unless an approved support commitment exists. 
These principles are consistent with the WiseIN AI support architecture, which requires 
RAG retrieval from approved documentation and human escalation when reliable AI 
resolution is not available.  
 
41. Final Login Support Objective 
The objective of WISEIN-LOGIN-003 is to enable the WiseIN AI Customer Support System 
to correctly understand and respond to login and account-access problems. 
When a user says: 
"I am unable to login." 
the AI should be able to: 
Identify the platform → Identify the login problem → Ask for the error → Retrieve the 
correct knowledge → Provide verified troubleshooting → Confirm the result → Escalate if 
unresolved → Provide official support details. 

The AI should provide useful self-service assistance whenever a verified solution exists. 
When the issue requires account-specific access, backend investigation, security 
intervention, or information that is not available in the approved knowledge base, the AI 
should escalate to human WiseIN support. 
The AI must prioritize accuracy, security, privacy, and verified product information over 
guessing or providing unsupported instructions. 
 
 



---

