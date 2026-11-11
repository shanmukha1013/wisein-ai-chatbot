# Payments

## Source: 54.pdf

54. PAYMENTS 
Document ID: WI-KB-054​
 Module: Payments​
 Feature: Payments​
 Platform: WiseIN Web Application​
 Document Type: Product Knowledge Base​
 Status: Draft — Requires UI Verification​
 Last Reviewed: September 2026 
 
1. FEATURE OVERVIEW 
The Payments section is responsible for handling and/or displaying payment-related 
information associated with WiseIN services. 
Payment functionality may be associated with actions such as: 
●​ Purchasing a subscription plan 
●​ Processing subscription payments 
●​ Viewing payment status 
●​ Identifying payment transactions 
●​ Handling payment-related issues 
●​ Processing payments through the configured payment provider 
The subscription interface previously reviewed shows Razorpay as the payment provider. 
 
2. PAYMENT PROVIDER 
The WiseIN subscription interface currently displays: 
Payment Provider: Razorpay 
The payment information section can contain payment-related identifiers such as: 
●​ Payment Order ID 
●​ Plan ID 
●​ Organization ID 
●​ Razorpay Order ID 

●​ Razorpay Payment ID 
These values may vary depending on the user's subscription and transaction. 
 
3. PAYMENT INFORMATION 
The previously reviewed WiseIN subscription screen contains a Payment details section. 
The displayed fields include: 
Field 
Purpose 
Payment Order ID 
Identifies the payment order 
Plan ID 
Identifies the associated subscription plan 
Organization ID 
Identifies an associated organization where 
applicable 
Razorpay Order ID 
Payment-provider order identifier 
Razorpay Payment ID 
Payment-provider payment identifier 
For the test account reviewed, several fields displayed N/A, while the Plan ID displayed 
FREE_PLAN_ID. 
Security: Payment IDs and transaction identifiers should be treated as sensitive 
account information and should not be exposed unnecessarily by the AI Assistant. 
 
4. PAYMENT FLOW 
Based on the currently verified subscription interface, the general relationship between 
subscriptions and payments is: 
User 
  ↓ 
Subscriptions 
  ↓ 
Select Paid Plan 
  ↓ 

Payment Process 
  ↓ 
Razorpay 
  ↓ 
Payment Result 
  ↓ 
Subscription Status Updated 
The exact payment screens and confirmation workflow still need to be verified directly. 
 
5. PAYMENT STATUS 
The exact list of WiseIN payment statuses has not yet been verified. 
Therefore, the chatbot should not assume that WiseIN uses statuses such as: 
●​ Successful 
●​ Failed 
●​ Pending 
●​ Refunded 
●​ Cancelled 
until these states are confirmed through the application or official documentation. 
 
6. PAYMENT-RELATED USER QUESTIONS 
Q1. What payment provider does WiseIN use? 
The currently reviewed subscription interface displays Razorpay as the payment provider. 
 
Q2. Where can I find my payment information? 
Payment-related information is displayed within the subscription/payment section of WiseIN 
where applicable. 
The exact location of a dedicated Payments page needs to be verified. 

 
Q3. I made a payment but my subscription hasn't changed. What should I 
do? 
The AI Assistant should first ask the user to verify: 
1.​ Which plan they selected. 
2.​ Whether the payment was completed. 
3.​ Whether WiseIN still shows the previous plan. 
4.​ Whether an error message appeared. 
5.​ Whether they received a payment confirmation. 
If the payment was completed but the subscription has not updated, the issue should be 
escalated for payment verification. 
 
Q4. My payment failed. What should I do? 
The AI should ask the user for: 
●​ Selected plan 
●​ Payment attempt time 
●​ Error message 
●​ Payment status shown by the payment provider 
●​ Whether money was deducted 
The assistant should not instruct the user to make another payment immediately when the 
previous transaction's status is unclear. 
 
7. PAYMENT TROUBLESHOOTING 
7.1 Payment Failed 
Recommended initial checks: 
1.​ Check whether the payment provider reported a failure. 
2.​ Check whether WiseIN updated the subscription. 
3.​ Check whether the user's bank/payment method was charged. 
4.​ Record any displayed error. 

5.​ Escalate if the payment status is unclear. 
 
7.2 Money Deducted but Subscription Not Activated 
This is a potentially important payment-support case. 
The AI should collect: 
●​ Plan selected 
●​ Approximate payment time 
●​ Payment confirmation 
●​ Transaction/reference information 
●​ Current WiseIN subscription status 
●​ Screenshot of the payment confirmation, if available 
The issue should be escalated to human support/payment support for verification. 
 
7.3 Payment Status Is Unknown 
If the user says: 
"Money was deducted but I don't know if the payment went through." 
The AI should not assume the payment succeeded or failed. 
Instead, it should guide the user to verify the transaction status and escalate if the status cannot 
be confirmed. 
 
7.4 Duplicate Payment 
If a user reports being charged more than once: 
1.​ Do not ask them to make another payment. 
2.​ Collect the relevant transaction information. 
3.​ Ask whether both transactions appear as successful. 
4.​ Escalate the issue to human/payment support. 
 

8. PAYMENT SECURITY 
Payment information must be handled carefully. 
The AI Assistant should never unnecessarily request or expose: 
●​ Card numbers 
●​ CVV 
●​ OTPs 
●​ Banking passwords 
●​ UPI PIN 
●​ Payment credentials 
If payment verification requires transaction information, the assistant should request only the 
minimum information needed according to WiseIN's support process. 
 
9. AI CUSTOMER SUPPORT GUIDELINES 
User: 
"I paid for Premium but I'm still on the free plan." 
AI: 
"I can help you troubleshoot that. Please check whether the payment was 
completed successfully and whether WiseIN still shows your previous plan. If the 
payment was completed but your subscription hasn't updated, the transaction may 
need to be verified by customer support." 
 
User: 
"What payment system does WiseIN use?" 
AI: 
"The WiseIN subscription interface currently shows Razorpay as the payment 
provider." 
 

User: 
"I was charged twice." 
AI: 
"Please don't make another payment. We should first verify the transaction details 
and payment status. If two successful charges appear, the issue should be 
escalated to customer support for investigation." 
 
10. AI RESPONSE RULES 
The AI SHOULD 
●​ Explain the documented payment process. 
●​ Identify Razorpay as the currently observed payment provider. 
●​ Help users troubleshoot payment-related issues. 
●​ Collect relevant non-sensitive transaction information. 
●​ Escalate unresolved payment issues. 
●​ Distinguish between payment status and subscription status. 
The AI SHOULD NOT 
●​ Ask for card numbers, CVV, UPI PIN, passwords, or OTPs. 
●​ Claim a payment succeeded without confirmation. 
●​ Claim a refund has been issued without verification. 
●​ Promise a refund. 
●​ Expose another user's payment information. 
●​ Invent payment statuses. 
●​ Invent payment fees. 
●​ Tell users to make another payment when the previous transaction is unresolved. 
 
11. PAYMENT ESCALATION 
Payment issues should be escalated when: 
●​ Money was deducted but the subscription was not activated. 

●​ Payment status cannot be determined. 
●​ A payment appears to have been duplicated. 
●​ A refund is disputed. 
●​ Payment was successful but WiseIN does not reflect it. 
●​ The payment provider and WiseIN show conflicting statuses. 
●​ The user encounters a persistent payment error. 
Information to Collect 
Where appropriate: 
●​ WiseIN account 
●​ Selected subscription plan 
●​ Approximate transaction time 
●​ Payment status 
●​ Transaction/reference ID 
●​ Error message 
●​ Screenshot/payment confirmation 
 
12. VERIFIED INFORMATION 
Information 
Status 
Razorpay displayed as payment 
provider 
✅ Verified 
Payment details section exists 
✅ Verified 
Payment Order ID field 
✅ Verified 
Plan ID field 
✅ Verified 
Organization ID field 
✅ Verified 
Razorpay Order ID field 
✅ Verified 
Razorpay Payment ID field 
✅ Verified 
Complete payment checkout flow 
⚠️ Requires verification 
Payment success screen 
⚠️ Requires verification 

Payment failure screen 
⚠️ Requires verification 
Refund workflow 
⚠️ Requires verification 
Payment history 
⚠️ Requires verification 
Dedicated Payments page 
⚠️ Requires verification 
Payment status values 
⚠️ Requires verification 
 
13. INFORMATION REQUIRING 
VERIFICATION 
To complete Document 54 — Payments, we should inspect the actual Payments 
page/workflow in WiseIN. 
We need to verify: 
Payment History 
●​ Whether users can see previous payments 
●​ Transaction list 
●​ Date/time 
●​ Amount 
●​ Payment status 
●​ Payment method 
●​ Receipt/invoice 
Payment Processing 
●​ Razorpay checkout 
●​ Payment confirmation 
●​ Failed payment handling 
●​ Pending payment handling 
●​ Retry mechanism 
Refunds 
●​ Refund eligibility 
●​ Refund process 

●​ Refund status 
●​ Refund timeline 
Payment Support 
●​ Payment dispute process 
●​ Failed transaction support 
●​ Duplicate payment handling 
 
14. KNOWLEDGE BASE ENTRY 
Feature 
Payments 
Related Module 
Subscriptions 
Payment Provider 
Razorpay — observed in the WiseIN subscription interface 
Primary Purpose 
Handle and provide information related to payments associated with WiseIN services and 
subscriptions. 
User Intent Examples 
"How do I pay for Premium?" 
"What payment method does WiseIN use?" 
"My payment failed." 
"I paid but my Premium isn't active." 
"Money was deducted but my plan didn't change." 
"I was charged twice." 
"Where can I see my payment?" 
"Can I get a refund?" 
"Why is my payment pending?" 
Primary AI Response 

WiseIN's subscription interface currently shows Razorpay as its payment 
provider. If you're experiencing a payment issue, tell me what 
happened—such as a failed payment, a deducted amount without 
subscription activation, or a duplicate charge—and I can guide you through 
the next steps. 
 
15. DOCUMENT STATUS 
Status: 🟡 Draft — Partially Verified 
Verified 
●​ Razorpay integration display. 
●​ Payment Details section. 
●​ Payment-related identifier fields. 
Pending Verification 
●​ Dedicated Payments page. 
●​ Payment history. 
●​ Complete checkout process. 
●​ Payment statuses. 
●​ Failed payments. 
●​ Refunds. 
●​ Receipts/invoices. 
●​ Duplicate payments. 
●​ Payment retry process. 
 



---

