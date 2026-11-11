# Identity Verification

## Source: WISEIN IDENTITY VERIFICATION DOCUMENTATION007.pdf

DOCUMENT 007 — WISEIN IDENTITY 
VERIFICATION DOCUMENTATION 
WISEIN-VER-007 
Document Title: WiseIN Identity Verification Documentation 
Category: Identity Verification, KYC & Account Security 
Document Version: 1.0 
Document Status: Draft — Pending Product, Engineering, Security, and Support-Team Approval 
Prepared By: Marella Shanmukha Reddy (MSR) 
Created / Updated Date: 17 September 2026 
Classification: Internal Use / Customer Support Knowledge / AI-RAG Knowledge Source 
Primary Purpose: To document WiseIN's identity verification processes, requirements, 
verification methods, user workflows, error scenarios, troubleshooting, privacy and security 
considerations, and AI customer-support guidance. 
Authority Status: Draft documentation. The exact current verification methods, supported 
documents, review procedures, and account restrictions require validation against the current 
WiseIN application and official product documentation. 
1. Purpose of This Document 
This document provides structured information about the identity verification functionality 
available within the WiseIN platform. 
Identity verification is an important component of WiseIN's trust-focused professional networking 
ecosystem. The verification process is intended to support authentic professional identities, 
reduce identity fraud and impersonation, and establish trust between users and organizations. 
This document is designed to support: 
●​ WiseIN users completing identity verification. 
●​ Users experiencing KYC or verification problems. 

●​ Customer-support representatives. 
●​ QA testers. 
●​ Product and engineering teams. 
●​ Security and compliance stakeholders. 
●​ The WiseIN AI customer-support chatbot. 
●​ The Retrieval-Augmented Generation (RAG) knowledge base. 
The document covers the verification process from accessing the verification module through 
submitting the required information and reviewing the verification result. 
Important: The AI chatbot must not independently approve, reject, modify, or confirm a user's 
identity verification status. Verification status must be obtained from the authorized WiseIN 
verification system or authorized support team. 
2. Scope of the Document 
2.1 Included Scope 
This document covers: 
●​ Overview of WiseIN identity verification. 
●​ Purpose and objectives of verification. 
●​ Individual identity verification. 
●​ DigiLocker-based verification. 
●​ Aadhaar-related verification. 
●​ PAN-related verification. 
●​ Video liveness verification. 
●​ Verification access points. 
●​ Verification workflow. 
●​ Verification success and failure behavior. 
●​ Student verification overview. 
●​ Organization verification overview. 
●​ Verification status and badges. 
●​ Error scenarios. 
●​ Troubleshooting. 
●​ Privacy and security. 
●​ Third-party verification considerations. 
●​ Human-support escalation. 
●​ AI customer-support guidelines. 
●​ Source and verification tracking. 
●​ Pending product and engineering confirmation. 

2.2 Excluded or Separately Documented Topics 
The following areas should be documented in more detail in separate documents: 
●​ Complete user registration. 
●​ Email verification. 
●​ Complete login workflow. 
●​ Password reset and account recovery. 
●​ Detailed student verification. 
●​ Detailed organization verification. 
●​ Privacy policy and data-retention policy. 
●​ Security architecture. 
●​ Subscription-based verification eligibility. 
●​ Internal verification-provider implementation. 
●​ Backend review and approval processes. 
●​ Legal or regulatory interpretation of identity verification. 
This document may reference these topics when they are directly related to the verification 
process. 
3. Overview of WiseIN Identity Verification 
WiseIN is designed as a trust-focused professional networking platform. Its verification 
functionality is intended to help establish the authenticity of individuals, students, and 
organizations using approved verification methods. 
The reviewed WiseIN information refers to government-related identity verification methods, 
including Aadhaar, PAN, and DigiLocker. It also references video-based verification and 
third-party identity verification. 
The exact verification methods available to a user may depend on: 
●​ User category. 
●​ Country or region. 
●​ Account type. 
●​ Verification category. 
●​ Current WiseIN application version. 
●​ Available verification provider. 
●​ Product-specific eligibility requirements. 
The WiseIN team must confirm which verification methods are currently active and available for 
each user category. 

4. Purpose of the Verification Module 
The verification module is intended to support the authenticity and trustworthiness of users and 
organizations on WiseIN. 
4.1 Main Objectives 
The verification module may be used to: 
1.​ Validate the identity associated with a user account. 
2.​ Support the creation of authentic professional profiles. 
3.​ Reduce the risk of fake, misleading, or impersonated profiles. 
4.​ Establish trust between professionals and organizations. 
5.​ Support the display of verification badges or status indicators. 
6.​ Support access to features that require verification. 
7.​ Verify student eligibility where applicable. 
8.​ Validate organization identity and business information. 
9.​ Provide users with information about their verification status. 
10.​Support troubleshooting and escalation for verification-related issues. 
These objectives describe the general purpose of verification. Specific feature access, 
privileges, restrictions, and eligibility requirements must be confirmed through official WiseIN 
documentation. 
5. Verification Categories 
The verification categories identified from the reviewed WiseIN information include the following: 
Verification 
Category 
Description 
Status 
Individual 
Verification 
Verification of a person's identity through an 
approved verification process. 
Requires current product 
confirmation 
Student Verification 
Verification that a user meets the applicable 
student eligibility requirements. 
Requires product and 
regional confirmation 

Organization 
Verification 
Verification of an organization's identity and 
business information. 
Requires product and 
engineering confirmation 
Employee / Member 
Verification 
Verification status associated with an 
individual connected to an organization, 
where applicable. 
Requires product 
confirmation 
The exact naming, availability, and workflow of each category must be confirmed in the current 
WiseIN application. 
6. Individual Identity Verification 
6.1 Overview 
Individual identity verification is intended to validate the identity of a person associated with a 
WiseIN account. 
The reviewed WiseIN information references the following possible verification methods: 
●​ Aadhaar-based verification. 
●​ PAN-related verification. 
●​ DigiLocker-based verification. 
●​ Video-based verification. 
●​ Third-party identity verification. 
The actual verification methods available to a particular user must be confirmed based on the 
current application, account type, location, and product configuration. 
6.2 Purpose of Individual Verification 
Individual verification may help WiseIN: 
●​ Confirm that an account is associated with a real individual. 
●​ Validate identity information against approved documents. 
●​ Support a verified profile badge. 
●​ Improve trust between professional users. 
●​ Reduce impersonation and identity fraud. 
●​ Support verification-based features. 

The AI chatbot must not describe a particular verification method as mandatory unless it is 
confirmed for the user's account and current platform version. 
7. Accessing the Verification Module 
According to the available WiseIN platform guide, the verification portal may open automatically 
after initial account registration. 
The verification process may also be accessed through: 
Settings → Verification 
7.1 Documented Access Options 
Access Method 
Description 
Status 
Automatic Access The verification portal opens after initial account 
registration. 
Source-derived 
Settings 
The user can access the verification process 
through Settings → Verification. 
Source-derived 
Profile or 
Onboarding 
Additional access points may exist through profile 
or onboarding workflows. 
Requires live 
verification 
7.2 Pending Confirmation 
The following details must be tested: 
●​ Exact verification page URL. 
●​ Whether verification is mandatory immediately after registration. 
●​ Whether verification can be skipped or postponed. 
●​ Whether the user can access verification later. 
●​ Whether the verification page is available on web and mobile. 
●​ Whether the verification screen differs based on user category. 
●​ Whether the user can change the selected verification method. 

8. Verification Requirements 
Verification requirements may vary depending on the selected method and user category. 
The following information should be documented and confirmed for each verification workflow. 
Requirement Category 
Information to Document 
Personal Information 
Name and other required account information 
Identity Document 
Accepted government-issued identity documents 
Document Validity 
Document validity, expiry, legibility, and completeness 
Identity Matching 
Whether account information must match the submitted 
document 
Video Verification 
Whether a video or live verification step is required 
Third-Party Provider 
Verification provider and information transferred 
User Consent 
Required consent, disclosures, and permissions 
Technical Requirements Camera, microphone, browser, device, and internet requirements 
Review Process 
Automated review, manual review, or a combination 

Additional Information 
Information requested after an unsuccessful verification attempt 
The exact document types, fields, age requirements, provider rules, and verification conditions 
require confirmation from the WiseIN product team. 
9. DigiLocker Verification 
9.1 Overview 
The available WiseIN platform guide describes a DigiLocker-based verification option. 
DigiLocker verification is documented as one of the methods that may be used during the 
WiseIN identity verification process. 
9.2 Documented Workflow 
According to the available guide: 
1.​ Open the WiseIN verification portal. 
2.​ Select the option to verify through DigiLocker. 
3.​ Sign in using the requested Aadhaar or mobile-related details. 
4.​ Grant the required document-access permission. 
5.​ Continue with the verification process as instructed by the platform. 
9.3 DigiLocker Requirements 
The following items require confirmation: 
●​ Whether DigiLocker is currently available for all users. 
●​ Whether DigiLocker is mandatory or optional. 
●​ Exact login and authentication steps. 
●​ Exact information requested by the DigiLocker interface. 
●​ Documents retrieved through DigiLocker. 
●​ Consent and permission wording. 
●​ Whether the verification is automated. 
●​ Whether the user can cancel the DigiLocker process. 
●​ Error messages generated by DigiLocker. 
●​ Whether the process differs on web and mobile. 

9.4 AI Support Guidance 
The AI chatbot should: 
●​ Direct the user to the official WiseIN verification workflow. 
●​ Explain only the DigiLocker steps available in the approved knowledge base. 
●​ Avoid asking the user to share Aadhaar details, OTPs, or identity documents in chat. 
●​ Avoid claiming that DigiLocker verification has been completed without an authorized 
system response. 
●​ Escalate unexplained DigiLocker errors when basic approved troubleshooting is 
unsuccessful. 
10. Aadhaar-Based Verification 
10.1 Overview 
The available WiseIN platform guide documents an Aadhaar-related verification process. 
The documented workflow involves entering an Aadhaar number and submitting an OTP sent to 
the mobile number linked to Aadhaar. 
10.2 Documented Workflow 
The available guide describes the following steps: 
1.​ Open the identity verification process. 
2.​ Enter the required 12-digit Aadhaar number. 
3.​ Select the option to send an Aadhaar OTP. 
4.​ Receive the OTP on the mobile number linked to Aadhaar. 
5.​ Enter the OTP in the verification interface. 
6.​ Continue with the verification process. 
The exact screen names, field labels, OTP expiry, retry rules, and error messages require 
additional testing. 
10.3 Aadhaar Verification Requirements 
The following items require confirmation: 
●​ Whether Aadhaar verification is available to all users. 
●​ Whether Aadhaar is mandatory for individual verification. 

●​ Whether Aadhaar is required for student verification. 
●​ Exact consent and disclosure requirements. 
●​ OTP delivery and expiry rules. 
●​ Maximum OTP attempts. 
●​ Aadhaar validation errors. 
●​ Handling of mismatched information. 
●​ Whether the user can restart the process. 
●​ Data storage and retention rules. 
●​ Whether a third-party verification provider is involved. 
10.4 Security Requirements 
Aadhaar information is sensitive identity information. 
The AI chatbot must not: 
●​ Ask users to share their full Aadhaar number in chat. 
●​ Ask users to share their Aadhaar OTP. 
●​ Request screenshots containing unredacted Aadhaar details. 
●​ Ask users to send identity documents through unofficial channels. 
●​ Claim to verify Aadhaar details independently. 
●​ Confirm verification completion without an authorized system response. 
Users should be directed to the official WiseIN verification interface or an approved secure 
support channel. 
11. PAN-Based Verification 
11.1 Overview 
The available WiseIN platform guide documents a PAN-related verification step. 
11.2 Documented Workflow 
The guide describes the following information requirements: 
1.​ Enter the 10-digit PAN. 
2.​ Enter the user's full legal name. 
3.​ Submit the information through the verification interface. 
4.​ Continue with the remaining verification steps as directed by WiseIN. 

11.3 PAN Verification Requirements 
The following details require confirmation: 
●​ Whether PAN verification is required for all users. 
●​ Whether PAN verification is optional or mandatory. 
●​ Exact name format required. 
●​ Whether the legal name must match the account profile. 
●​ Whether the PAN must be valid and active. 
●​ How mismatched PAN information is handled. 
●​ Whether PAN verification is performed through a third-party provider. 
●​ Whether the user can correct submitted information. 
●​ Whether the user can retry after failure. 
●​ Exact error messages. 
11.4 AI Support Guidance 
The AI chatbot should provide only the approved steps for the PAN verification workflow. 
The chatbot must not: 
●​ Request the user's PAN number in ordinary chat. 
●​ Ask the user to share a photo of their PAN card unless an approved secure process 
explicitly requires it. 
 



---

