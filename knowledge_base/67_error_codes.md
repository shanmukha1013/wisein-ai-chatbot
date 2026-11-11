# Error Codes

## Source: 67.pdf

67. Error Codes 
Overview 
The Error Codes section documents the errors that users may encounter while using WiseIN. It 
helps users and the AI customer-support chatbot understand what an error means, what the 
user can try, and when the issue should be escalated to human support. 
Purpose 
The Error Codes knowledge base should help the chatbot: 
●​ Identify common WiseIN errors. 
●​ Explain errors in simple language. 
●​ Provide relevant troubleshooting steps. 
●​ Avoid giving users incorrect technical explanations. 
●​ Collect useful information when an error persists. 
●​ Escalate unresolved or repeated errors to WiseIN support. 
 
1. Error Code Categories 
WiseIN errors can be organized according to the feature where they occur: 
Category 
Examples 
Authentication 
Login and sign-in errors 
OTP 
OTP delivery or verification errors 
Google Sign-In 
Google authentication errors 
Profile 
Profile update/save errors 
Verification 
Identity or profile verification errors 
Video 
Recording/submission errors 
AI Agent 
AI Agent errors 
Chat 
Messaging errors 

Meetings 
Meeting/video-call errors 
Notifications 
Notification delivery errors 
Posts 
Post creation/publishing errors 
Jobs 
Job-related errors 
Payments 
Payment/transaction errors 
Subscriptions 
Subscription-related errors 
Account 
Deactivation, deletion, or logout errors 
Network 
Connection/request errors 
 
2. Confirmed WiseIN Errors 
Based on the WiseIN issues documented during testing, the following errors/issues have been 
observed. 
67.1 Google Sign-In — "Failed to fetch" 
Error message: 
Failed to fetch 
Area: Login / Google Sign-In 
Description:​
 The user encounters a "Failed to fetch" error while attempting to log in using Google. 
Suggested troubleshooting: 
1.​ Check the internet connection. 
2.​ Refresh the WiseIN page. 
3.​ Try Google Sign-In again. 
4.​ Try another browser. 
5.​ If the problem continues, report the issue to WiseIN support. 
Escalation information: 
The user should provide: 

●​ Screenshot of the error. 
●​ Browser/device information. 
●​ Approximate time the error occurred. 
●​ Steps performed before the error. 
 
67.2 OTP Not Received 
Error: OTP is not received. 
Area: Authentication / Profile 
Description:​
 The user does not receive the OTP required to complete an action. 
Possible troubleshooting: 
1.​ Verify the phone number/email. 
2.​ Check network connectivity. 
3.​ Wait briefly for the OTP. 
4.​ Request another OTP if available. 
5.​ Check the email spam/junk folder when applicable. 
6.​ Try the operation again. 
Escalation:​
 If the OTP still does not arrive, the issue should be escalated to WiseIN support. 
 
67.3 Video Recording — "Some error!" 
Error message: 
Some error! 
Area: Video Recording 
Description:​
 An error popup appears after the user submits a recorded video. 
Suggested troubleshooting: 
1.​ Check the internet connection. 
2.​ Verify camera and microphone permissions. 
3.​ Try recording the video again. 

4.​ Refresh the page. 
5.​ Retry the submission. 
6.​ Try another browser if the issue continues. 
Escalation:​
 If the recorded video repeatedly fails to submit, report the issue with a screenshot or other 
available evidence. 
 
67.4 AI Agent — Incomplete Video Guidance 
Error/Issue:​
 The AI Agent does not provide complete video guidance. 
Area: AI Agent 
Description:​
 The user receives incomplete guidance while interacting with the AI Agent. 
Suggested troubleshooting: 
1.​ Retry the interaction. 
2.​ Refresh the page. 
3.​ Check the internet connection. 
4.​ Repeat the process. 
5.​ Report the issue if the AI Agent continues to provide incomplete guidance. 
 
67.5 Profile Information — OTP Not Received 
Issue:​
 The user cannot save education/profile information because the required OTP is not received. 
Area: Profile / Education Information 
Description:​
 The user attempts to save information but cannot complete the process because the OTP does 
not arrive. 
Suggested troubleshooting: 
1.​ Check the registered contact information. 
2.​ Check network connectivity. 
3.​ Request another OTP if available. 

4.​ Wait and retry the operation. 
5.​ Contact support if the problem continues. 
 
3. Generic Error Messages 
The following are general categories, not confirmed WiseIN error codes unless the actual 
platform displays them. 
Network Error 
Meaning:​
 The request may not have completed because of a network or connectivity problem. 
User action: 
●​ Check internet connection. 
●​ Refresh the page. 
●​ Retry the operation. 
 
Request Failed 
Meaning:​
 The requested operation was not successfully completed. 
User action: 
●​ Retry the operation. 
●​ Refresh the page. 
●​ If the error persists, report it to support. 
 
Something Went Wrong 
Meaning:​
 The platform encountered an unspecified problem while processing the request. 
User action: 
1.​ Retry. 

2.​ Refresh. 
3.​ Check the internet connection. 
4.​ Capture the error message/screenshot. 
5.​ Contact support if the issue continues. 
 
Unauthorized / Session Expired 
Meaning:​
 The user's current login session may no longer be valid. 
User action: 
1.​ Log out. 
2.​ Log in again. 
3.​ Retry the operation. 
Important: This should only be presented as an official WiseIN error if the platform actually 
displays this message. 
 
4. Error Handling Flow for the AI Chatbot 
The chatbot should follow a consistent process whenever a user reports an error. 
Step 1 — Identify the Error 
Ask: 
"What error message are you seeing?" 
If the user provides an exact error message, use that message to identify the relevant 
troubleshooting article. 
Step 2 — Identify the Feature 
Determine where the error occurred: 
●​ Login 
●​ OTP 
●​ Profile 
●​ Verification 

●​ Video 
●​ AI Agent 
●​ Chat 
●​ Meetings 
●​ Jobs 
●​ Payments 
●​ Subscription 
●​ Other 
Step 3 — Provide Troubleshooting 
Give only the steps relevant to that error. 
Step 4 — Ask the User to Retry 
For example: 
"Please try the steps above and let me know whether the issue is resolved." 
Step 5 — Escalate 
If the issue continues: 
"This issue may require assistance from WiseIN support. Please provide the error 
message, the affected feature, and a screenshot if available." 
 
5. Error Report Information 
When escalating an error, the chatbot should try to collect: 
Required: 
●​ Error message 
●​ Feature where the error occurred 
●​ What the user was trying to do 
●​ Steps that caused the error 
Useful additional information: 
●​ Screenshot 
●​ Browser/device 
●​ Approximate time 

●​ Whether the problem happens repeatedly 
 
6. Important Rule for the WiseIN Chatbot 
The chatbot must not invent an error code or technical cause. 
For example, if the user says: 
"I am getting some error while uploading." 
The chatbot should not claim: 
"This is error code WISEIN-500." 
unless WiseIN's official documentation actually defines that code. 
Instead, it should ask: 
"What exact error message do you see? If possible, please share a screenshot." 
 
7. Error Code Knowledge-Base Format 
For future WiseIN errors, use this structure: 
Error Code / Error Name 
Error message:​
 Exact message displayed by WiseIN 
Area:​
 Feature/module 
Description:​
 What the user experiences. 
Possible cause:​
 Only include if confirmed by WiseIN documentation or technical investigation. 
Troubleshooting: 

1.​ Step one 
2.​ Step two 
3.​ Step three 
Escalation:​
 When the user should contact support. 
Information to collect: 
●​ Error screenshot 
●​ Feature 
●​ Steps performed 
●​ Device/browser 
●​ Time of occurrence 
 



---

