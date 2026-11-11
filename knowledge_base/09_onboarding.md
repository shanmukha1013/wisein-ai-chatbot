# Onboarding

## Source: WISEIN USER ONBOARDING DOCUMENTATION009.pdf

DOCUMENT 009 — WISEIN USER 
ONBOARDING DOCUMENTATION 
WISEIN-ONB-009 
Draft 
Pending Product Verification 
Document Title: WiseIN User Onboarding Documentation 
Document ID: WISEIN-ONB-009 
Category: User Onboarding, Account Setup & Profile Completion 
Version: 1.0 
Prepared By: MSR 
Date: 17 September 2026 
Document Classification: Internal Documentation / AI Customer Support Knowledge Base 
Status: Draft — Pending Product, Engineering, QA, and Support-Team Approval 
1. Document Information 
Field 
Details 
Document 
Name 
WiseIN User Onboarding Documentation 
Document ID 
WISEIN-ONB-009 
Application 
WiseIN 

Website 
https://www.wisein.in  
Feature 
Category 
User Onboarding and Profile Setup 
Primary Users 
Newly registered users, verified members, students, professionals, and 
applicable organizations 
Intended Use 
Product documentation, QA testing, customer support, and RAG 
knowledge base 
Document 
Status 
Draft 
Verification 
Status 
Partially supported by the provided platform guide; detailed onboarding 
flow requires live verification 
Last Updated 
17 September 2026 
2. Purpose of This Document 
The purpose of this document is to explain the WiseIN user onboarding process, including the 
activities a newly registered user may need to complete before using the platform. 
This document is intended to help: 
1.​ New users understand how to set up their WiseIN account. 
2.​ Users complete their identity verification and profile setup. 
3.​ Users understand the difference between registration, verification, and onboarding. 
4.​ QA teams test the onboarding journey and identify issues. 
5.​ Customer support teams guide users through onboarding-related problems. 
6.​ The WiseIN AI chatbot answer onboarding questions using approved documentation. 

7.​ The RAG knowledge base retrieve accurate onboarding instructions and troubleshooting 
information. 
The exact onboarding screen sequence, mandatory fields, skip options, completion conditions, 
and platform-specific behavior must be confirmed through the current WiseIN application and 
approved product documentation. 
3. What Is User Onboarding? 
3.1 Definition 
User onboarding is the process through which a newly registered user completes the required 
account, identity, and profile setup activities needed to begin using the platform. 
On WiseIN, onboarding may include: 
●​ Completing account registration. 
●​ Verifying the registered email address. 
●​ Completing government identity verification. 
●​ Completing video liveness verification. 
●​ Adding profile information. 
●​ Adding professional experience. 
●​ Adding educational details. 
●​ Adding skills. 
●​ Preparing the profile for professional networking. 
●​ Understanding the available platform features. 
The exact sequence and mandatory status of these activities must be verified against the 
current WiseIN application. 
3.2 Simple Explanation 
Registration creates the account. 
Email verification confirms access to the registered email address. 
Identity verification validates the user's identity through the supported verification process. 
Onboarding prepares the user's account and profile for using WiseIN. 
High-Level Difference 

Process 
Main Purpose 
Registration 
Creates the initial user account 
Email Verification 
Confirms the user's registered email address 
Identity Verification 
Validates the user's identity using the supported verification 
process 
User Onboarding 
Guides the user through required account and profile setup 
Profile Management Allows users to update and maintain their profile after onboarding 
4. WiseIN Onboarding Overview 
According to the provided WiseIN platform guide, the initial account registration is followed by 
mandatory identity verification. 
The guide describes the following general journey: 
1. Account Registration 
Email verification 
2. Email Verification 
Initial account registration 
3. Identity Verification / KYC 
Identity and video liveness process 
4. Profile Setup 
Professional and educational information 

5. Ready for Platform Usage 
Important: The sequence above combines the registration, identity verification, and profile setup 
stages documented in the source. The exact user interface and whether all activities are 
presented inside one dedicated onboarding flow require confirmation. 
Source: WiseIN platform guide, pages 1–3. 
WISEIN - COMPLETE PLATFORM USER GUIDE & OPERATIONAL DOCUMENTATION(1).pdf 
5. Onboarding Objectives 
The WiseIN onboarding process should help users achieve the following objectives. 
5.1 Account Readiness 
The user should be able to complete the initial account registration and access the next required 
setup stage. 
5.2 Identity and Trust 
The user should understand why identity verification is required and complete the supported 
verification process where applicable. 
5.3 Profile Completion 
The user should be able to add relevant professional and educational information to their profile. 
5.4 Platform Familiarization 
The user should understand the basic purpose of WiseIN and the major features available after 
account setup. 
5.5 Customer Support Readiness 
The user should have access to troubleshooting guidance and human support if onboarding 
cannot be completed. 

6. Accessing the Onboarding Process 
6.1 Entry Point 
According to the supplied platform guide: 
1.​ The user navigates to the WiseIN sign-up page. 
2.​ The user enters the required registration details. 
3.​ The user requests an email OTP. 
4.​ The user enters the six-digit OTP. 
5.​ The user selects Submit & Continue. 
6.​ The system registers the initial account. 
7.​ The system automatically directs the user to mandatory identity verification. 
Sign-Up URL: https://www.wisein.in/sign-up  
The guide also states that the Identity Verification Portal can be accessed through: 
Settings → Verification 
Source-supported information: registration and identity verification entry points. Dedicated 
onboarding entry screen: pending confirmation. 
WISEIN - COMPLETE PLATFORM USER GUIDE & OPERATIONAL DOCUMENTATION(1).pdf 
6.2 Onboarding Entry Scenarios 
The following scenarios should be tested in the live application: 
Scenario 
Expected Behavior 
Verification Status 
New user completes 
registration 
User proceeds to the next required 
setup stage 
Supported for KYC transition 
User has not verified 
email 
User is guided to email verification 
Verify current behavior 

User has not completed 
KYC 
User is directed to identity 
verification 
Supported by source 
User has completed 
KYC 
User may proceed to profile setup 
Profile sequence requires 
confirmation 
User leaves setup 
unfinished 
User can resume setup later 
Pending verification 
Existing user opens 
Settings 
User can access profile and 
verification controls 
Partially supported 
User logs in from 
another device 
User's onboarding progress is 
retained 
Pending verification 
7. Registration Stage 
Registration is the initial stage before identity verification and profile setup. 
7.1 Registration Requirements 
The supplied platform guide identifies the following registration fields: 
Field 
Description 
Username 
User's chosen username 
Email Address 
Valid personal or corporate email 
address 

Password 
Secure password 
Email OTP 
Six-digit OTP sent to the registered 
email 
Submit & Continue 
Completes the registration step 
7.2 Password Requirements 
The provided documentation specifies that the password must contain: 
●​ At least eight characters. 
●​ Uppercase letters. 
●​ Lowercase letters. 
●​ Numbers. 
●​ Symbols. 
The password should be entered into the password field during registration. 
7.3 Registration Workflow 
1.​ Open the WiseIN sign-up page. 
2.​ Enter a username. 
3.​ Enter a valid email address. 
4.​ Create a password according to the stated requirements. 
5.​ Select Send OTP / Verify Email. 
6.​ Retrieve the six-digit OTP from the registered email inbox. 
7.​ Enter the OTP in the verification modal. 
8.​ Select Submit & Continue. 
9.​ Wait for the system to register the initial account. 
10.​Continue to the next required verification stage. 
WISEIN - COMPLETE PLATFORM USER GUIDE & OPERATIONAL DOCUMENTATION(1).pdf 
7.4 Registration Error 
The source document identifies the following error: 

"Username unavailable or invalid format. Please match your Government ID name." 
Possible Documented Causes 
●​ Username is already taken. 
●​ Username does not follow the required format. 
●​ Username does not match the applicable identity naming rules. 
Recommended User Guidance 
1.​ Review the entered username. 
2.​ Check whether the name matches the applicable government ID naming requirement. 
3.​ Try an available and valid username. 
4.​ If the error continues, contact WiseIN support. 
The precise username validation rules should be confirmed with the product or engineering 
team. 
8. Email Verification Stage 
Email verification is the stage where WiseIN confirms access to the email address entered 
during registration. 
8.1 Email Verification Process 
1.​ The user enters a valid email address. 
2.​ The user selects Send OTP / Verify Email. 
3.​ WiseIN sends a six-digit OTP to the registered email address. 
4.​ The user enters the OTP in the verification modal. 
5.​ The user selects Submit & Continue. 
6.​ The system validates the OTP. 
7.​ The user proceeds to the next account setup stage. 
8.2 Email Verification Requirements 
The user needs: 
●​ Access to the registered email inbox. 
●​ A valid OTP. 
●​ A functioning internet connection. 
●​ Access to the WiseIN verification screen. 

8.3 Email OTP Security 
The AI chatbot must not: 
●​ Ask users to share their OTP. 
●​ Ask users to share their password. 
●​ Request screenshots containing OTPs. 
●​ Store or expose actual OTP values. 
●​ Claim that it can manually verify an OTP. 
●​ Ask users for unnecessary sensitive information. 
The chatbot may guide users to check their inbox, verify the entered email address, and contact 
support if the OTP issue continues. 
8.4 Email Verification Troubleshooting 
Problem 
Suggested Guidance 
OTP not received 
Check the inbox, spam folder, and whether the email address is 
correct 
Invalid OTP 
Ask the user to check whether the entered OTP is correct and 
current 
OTP expired 
Request a new OTP if a resend option is available; exact 
behavior must be verified 
Verification screen not 
loading 
Refresh the page or retry after checking the connection 
Repeated verification 
failure 
Escalate to human support without requesting the OTP 
The exact resend limits, expiry rules, lockout behavior, and retry limits must be verified against 
the current WiseIN implementation. 

9. Identity Verification Stage 
Identity verification is a documented part of the WiseIN account setup process. 
The supplied guide states that after registration, the system automatically directs the user to 
mandatory identity verification (KYC). 
The verification portal can also be accessed through: 
Settings → Verification 
WISEIN - COMPLETE PLATFORM USER GUIDE & OPERATIONAL DOCUMENTATION(1).pdf 
9.1 Purpose of Identity Verification 
Based on the platform guide, identity verification supports WiseIN's trust-focused professional 
networking model. 
Its stated purposes include: 
●​ Validating user identity. 
●​ Supporting authenticated professional profiles. 
●​ Reducing identity fraud and impersonation. 
●​ Supporting trusted interactions between members. 
●​ Enabling access to applicable verified platform features. 
The exact verification eligibility requirements, review process, and restrictions must be 
confirmed with the WiseIN product and compliance teams. 
9.2 Available Verification Methods in the Source 
The platform guide identifies the following methods: 
1.​ DigiLocker Gateway. 
2.​ Aadhaar Card OTP. 
3.​ PAN Card Verification. 
4.​ Video Liveness Check. 
The current availability of each method may depend on the user's account type, implementation, 
or applicable eligibility rules. This must be verified before the AI chatbot provides 
method-specific instructions. 

10. DigiLocker Verification 
10.1 Documented Workflow 
According to the platform guide: 
1.​ Open the Identity Verification Portal. 
2.​ Select Verify with DigiLocker. 
3.​ Log in to DigiLocker using Aadhaar or mobile-based access. 
4.​ Grant the required document access. 
5.​ Continue with the WiseIN verification process. 
6.​ Complete any additional required verification steps. 
10.2 User Requirements 
The user may need: 
●​ Access to their DigiLocker account. 
●​ Aadhaar-linked or supported login access. 
●​ Permission to share the required documents. 
●​ A stable internet connection. 
●​ Access to the WiseIN verification page. 
10.3 Support Considerations 
The chatbot should not request DigiLocker login credentials, Aadhaar OTPs, or passwords. 
If DigiLocker authentication fails, the chatbot should provide only verified troubleshooting steps 
and escalate the issue when necessary. 
11. Aadhaar OTP Verification 
11.1 Documented Workflow 
The supplied guide describes the following steps: 
1.​ Select the Aadhaar verification option. 
2.​ Enter the 12-digit Aadhaar number. 
3.​ Select Send Aadhaar OTP. 
4.​ Receive the OTP on the Aadhaar-linked mobile number. 

5.​ Enter the OTP into the applicable verification field. 
6.​ Submit the verification request. 
7.​ Continue to the video liveness stage if required. 
WISEIN - COMPLETE PLATFORM USER GUIDE & OPERATIONAL DOCUMENTATION(1).pdf 
11.2 Security Rules 
The chatbot must not: 
●​ Ask the user to send their Aadhaar number in chat. 
●​ Ask the user to share their Aadhaar OTP. 
●​ Request a photograph of the user's Aadhaar card unless an approved secure support 
process explicitly requires it. 
●​ Store sensitive identity information in the conversation history. 
●​ Claim to perform Aadhaar verification itself. 
11.3 Troubleshooting Areas 
The following issues should be tested and documented: 
●​ Aadhaar number validation error. 
●​ OTP not received. 
●​ Incorrect OTP. 
●​ OTP expiration. 
●​ Aadhaar-linked mobile number unavailable. 
●​ Verification service unavailable. 
●​ Identity information mismatch. 
●​ Repeated failed attempts. 
The exact error messages and retry policies require live verification. 
12. PAN Card Verification 
12.1 Documented Workflow 
The provided guide states that the user should: 
1.​ Select PAN Card Verification. 
2.​ Enter the 10-digit PAN number. 
3.​ Enter the full legal name as recorded on the PAN record. 

4.​ Submit the information for verification. 
5.​ Continue with any additional verification step requested by WiseIN. 
WISEIN - COMPLETE PLATFORM USER GUIDE & OPERATIONAL DOCUMENTATION(1).pdf 
12.2 Information Matching 
The user's entered legal name may need to match the name associated with the submitted 
identity document. 
Possible issues include: 
●​ Incorrect PAN number. 
●​ Incorrect legal name. 
●​ Spelling differences. 
●​ Name mismatch between account and document. 
●​ Invalid or unsupported document details. 
The precise validation logic and permitted corrections must be confirmed with the WiseIN 
product team. 
12.3 AI Support Restrictions 
The AI chatbot must not: 
●​ Request the user to post their PAN number in chat. 
●​ Request a complete identity document image in an unsecured conversation. 
●​ Confirm verification success without an authorized system response. 
●​ Independently approve or reject identity verification. 
●​ Recommend unsupported methods to bypass verification. 
13. Video Liveness Verification 
13.1 Purpose 
The video liveness check is used as part of the identity verification workflow described in the 
supplied platform guide. 
The source states that the user performs a short face liveness scan using a webcam or mobile 
camera. 

13.2 Documented Workflow 
1.​ Open the identity verification process. 
2.​ Allow camera access when prompted by the browser. 
3.​ Position the face in front of the webcam or mobile camera. 
4.​ Perform the short, approximately three-second face liveness scan. 
5.​ Select Complete Verification. 
6.​ Wait for the system's verification response. 
WISEIN - COMPLETE PLATFORM USER GUIDE & OPERATIONAL DOCUMENTATION(1).pdf 
13.3 Required Permissions 
The user may need to provide: 
●​ Camera permission. 
●​ Browser permission to access the camera. 
●​ Adequate lighting. 
●​ A functioning camera. 
●​ A stable internet connection. 
The exact technical requirements, browser compatibility, and camera permission behavior 
require testing. 
13.4 Documented Verification Failure 
The source provides the following error message: 
"Verification Failed: Document details do not match account profile. Please retry." 
The guide indicates that verification may fail because of a name mismatch or an unclear camera 
scan. 
13.5 Video Verification Troubleshooting 
Issue 
Recommended Guidance 
Camera permission denied 
Check browser camera permissions and retry 

Camera not detected 
Confirm that the camera works and is not being used by 
another application 
Face not detected 
Improve lighting and position the face within the camera 
frame 
Liveness scan fails 
Retry only if the application provides a retry option 
Identity mismatch 
Check that the account information matches the identity 
document 
Repeated failure 
Escalate to human support 
User is uncomfortable sharing 
identity information 
Explain the purpose only using approved documentation 
and provide the official support route 
The AI chatbot must not promise that a retry will definitely resolve the problem. 
14. Verification Completion Response 
The platform guide describes the following expected success response: 
●​ The system validates the user's name and face scan against government records. 
●​ A blue verified checkmark is assigned to the profile. 
●​ The guide states that full platform access is granted. 
WISEIN - COMPLETE PLATFORM USER GUIDE & OPERATIONAL DOCUMENTATION(1).pdf 
14.1 AI Chatbot Guidance 
The AI chatbot should not independently confirm that a user is verified. 
It may explain: 

"Your verification status must be confirmed through the WiseIN application or an 
authorized WiseIN system. Please check your profile or verification section for the 
status displayed by the platform." 
If the chatbot is later connected to an authorized WiseIN verification-status API, it may provide 
account-specific status information only when the user has the required permissions and the 
system returns an approved result. 
15. Profile Setup Stage 
After the identity verification stage, the WiseIN platform guide describes a profile setup process 
called the Verified Portfolio Builder. 
15.1 Purpose 
The purpose of profile setup is to help users create a professional profile containing information 
relevant to networking, professional discovery, and potential collaboration. 
The documented profile setup activities include: 
●​ Uploading a profile image. 
●​ Uploading a cover banner. 
●​ Adding a headline. 
●​ Adding a bio. 
●​ Adding professional experience. 
●​ Adding educational details. 
●​ Adding skills. 
15.2 Accessing Profile Setup 
The source guide provides the following entry point: 
1.​ Click the user's profile avatar. 
2.​ Select Edit Profile. 
WISEIN - COMPLETE PLATFORM USER GUIDE & OPERATIONAL DOCUMENTATION(1).pdf 
The exact onboarding screen where the user first enters profile setup must be verified. 
16. Profile Picture and Cover Banner 

16.1 Profile Picture 
The user can upload a professional headshot as the profile image. 
Information to Verify 
●​ Supported image formats. 
●​ Maximum file size. 
●​ Minimum and maximum image dimensions. 
●​ Image cropping behavior. 
●​ Whether the image is mandatory. 
●​ Whether the user can skip this step. 
●​ Whether the user can replace the image later. 
●​ Error messages for unsupported files. 
16.2 Cover Banner 
The user can upload a background cover banner for their profile. 
Information to Verify 
●​ Supported image formats. 
●​ Recommended dimensions. 
●​ Maximum file size. 
●​ Cropping and positioning behavior. 
●​ Whether the cover image is optional. 
●​ Whether the cover image is visible publicly. 
●​ Upload failure behavior. 
AI Guidance: The chatbot must not invent image size requirements or claim that a particular file 
format is supported until these requirements are confirmed. 
17. Headline and Bio 
17.1 Headline 
The user can add a headline describing their current role, professional identity, or area of 
interest. 
Examples of possible information include: 

●​ Current job title. 
●​ Professional role. 
●​ Industry. 
●​ Primary specialization. 
The exact character limit and validation rules for the onboarding headline field must be 
confirmed. 
17.2 Bio 
The user can add a bio describing: 
●​ Current role. 
●​ Skills. 
●​ Industry focus. 
●​ Professional background. 
●​ Areas of interest. 
The platform guide also identifies a Bio field in Settings → Edit Profile with a character counter 
of up to 150 characters. The relationship between this field and the onboarding bio field should 
be confirmed through live testing. 
WISEIN - COMPLETE PLATFORM USER GUIDE & OPERATIONAL DOCUMENTATION(1).pdf 
Fields to Test 
Test Area 
Verification Requirement 
Empty headline 
Determine whether the field is mandatory 
Empty bio 
Determine whether the user can continue 
Maximum characters Confirm the character limit 
Special characters 
Check accepted characters 

Save behavior 
Confirm whether changes are saved immediately 
Validation 
Record exact error messages 
Edit later 
Confirm whether the user can update the 
information 
18. Professional Experience 
18.1 Documented Workflow 
The supplied guide describes the following process: 
1.​ Open the Experience section. 
2.​ Select + Add Experience. 
3.​ Enter the job title. 
4.​ Enter the company name. 
5.​ Select or enter the employment type. 
6.​ Enter the start date. 
7.​ Enter the end date, where applicable. 
8.​ Save the experience entry. 
WISEIN - COMPLETE PLATFORM USER GUIDE & OPERATIONAL DOCUMENTATION(1).pdf 
18.2 Documented Fields 
Field 
Description 
Job Title 
The user's professional position 
Company Name 
The organization where the user worked or 
works 

Employment Type Type of employment 
Start Date 
Date employment began 
End Date 
Date employment ended, if applicable 
18.3 Fields Requiring Confirmation 
The following details must be tested: 
●​ Whether experience is mandatory during onboarding. 
●​ Whether current employment can be selected. 
●​ Whether end date can be left blank. 
●​ Available employment type options. 
●​ Date format. 
●​ Company search or selection behavior. 
●​ Whether company names are validated against WiseIN organizations. 
●​ Duplicate experience handling. 
●​ Save and edit behavior. 
●​ Error messages. 
18.4 Verified Employment Tags 
The platform guide states that the profile may be updated live with verified employment tags if 
the user's company is registered on WiseIN. 
This behavior requires confirmation in the current application, including: 
●​ When the employment tag appears. 
●​ Whether company verification is required. 
●​ Whether the tag is automatic or reviewed. 
●​ Whether the user can remove or edit the tag. 
●​ What happens when the company is not registered. 
WISEIN - COMPLETE PLATFORM USER GUIDE & OPERATIONAL DOCUMENTATION(1).pdf 
19. Education Details 

19.1 Documented Workflow 
The source guide describes the following steps: 
1.​ Open the Education section. 
2.​ Select + Add Education. 
3.​ Enter the degree. 
4.​ Enter the field of study. 
5.​ Enter the institution. 
6.​ Save the education details. 
WISEIN - COMPLETE PLATFORM USER GUIDE & OPERATIONAL DOCUMENTATION(1).pdf 
19.2 Documented Fields 
Field 
Description 
Degree 
Degree or qualification obtained or pursued 
Field of Study 
Subject or specialization 
Institution 
College, university, or educational institution 
19.3 Education Testing Requirements 
The following must be verified: 
●​ Whether education details are mandatory. 
●​ Whether users can add multiple educational entries. 
●​ Whether institution names are selected from a list or entered manually. 
●​ Whether current education can be added without an end date. 
●​ Whether dates are required. 
●​ Whether the institution is verified. 
●​ Whether users can edit or delete entries. 
●​ Validation messages for missing or invalid information. 

20. Skills 
20.1 Documented Process 
The supplied guide states that users can list their core skills and save them. 
20.2 Skills Setup 
The onboarding process should be tested for: 
1.​ Opening the Skills section. 
2.​ Searching for a skill. 
3.​ Selecting a skill. 
4.​ Adding multiple skills. 
5.​ Removing a selected skill. 
6.​ Saving the skill list. 
20.3 Information Requiring Confirmation 
Test Area 
Requirement 
Maximum number of skills 
Confirm the limit 
Skill selection 
Determine whether skills come from a predefined list 
Custom skills 
Verify whether users can add new skills 
Duplicate skills 
Test duplicate prevention 
Empty skill list 
Confirm whether the section is mandatory 

Save behavior 
Verify the save response 
Skill visibility 
Confirm whether skills are publicly visible 
Editing 
Confirm whether skills can be modified later 
The source confirms that skills can be listed and saved but does not provide the complete skill 
selection rules. 
21. Settings-Based Profile Setup 
The platform guide contains additional profile management fields under Settings → Edit Profile. 
These fields should be documented separately from the initial onboarding flow unless live 
testing confirms that they are displayed during onboarding. 
21.1 Documented Profile Fields 
The source identifies the following fields and controls: 
●​ Change Photo. 
●​ Username display. 
●​ Phone number with country code. 
●​ Current job title. 
●​ Website. 
●​ Current organization. 
●​ Bio. 
●​ About section. 
●​ Gender selector. 
●​ Show Account Suggestions on Profiles toggle. 
●​ Submit button. 
The guide states that the gender field is private and is not shown on the public profile. 
WISEIN - COMPLETE PLATFORM USER GUIDE & OPERATIONAL DOCUMENTATION(1).pdf 
21.2 Onboarding Classification 

Feature 
Classification 
Profile photo 
Included in documented profile setup 
Cover banner 
Included in documented profile setup 
Headline 
Included in documented profile setup 
Bio 
Included in documented profile setup 
Experience 
Included in documented profile setup 
Education 
Included in documented profile setup 
Skills 
Included in documented profile setup 
Phone 
number 
Documented in Settings; onboarding inclusion 
pending 
Website 
Documented in Settings; onboarding inclusion 
pending 
About section 
 
 



---

