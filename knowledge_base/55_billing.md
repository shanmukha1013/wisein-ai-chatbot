# Billing

## Source: 55.pdf

55. BILLING 
Document ID: WI-KB-054​
 Module: Settings / Account​
 Feature: Billing​
 Platform: WiseIN Web Application​
 Document Type: Product Knowledge Base​
 Status: Draft — Requires UI Verification​
 Purpose: RAG Knowledge Base / AI Customer Support 
 
1. FEATURE OVERVIEW 
The Billing section contains information related to charges, subscription billing, and financial 
records associated with a user's WiseIN plan. 
Billing is closely related to Subscriptions and Payments, but the three features serve different 
purposes: 
Feature 
Purpose 
Subscription
s 
Manage the user's current WiseIN plan 
Payments 
Process and verify payment transactions 
Billing 
Manage billing information, charges, invoices, and billing records 
 
2. BILLING AND SUBSCRIPTION 
RELATIONSHIP 
A user's billing information is generally associated with their selected subscription plan. 
The currently reviewed WiseIN subscription interface shows: 
WiseIN Go 

₹0/month 
Premium 
₹499/month 
Student Premium 
₹199/month 
The interface also provides an Annual billing option for Premium. 
The reviewed Premium annual price is: 
₹5,988/year 
These prices are based on the currently observed WiseIN interface and may 
change. The AI Assistant should use the current application data rather than 
permanently assuming these prices. 
 
3. BILLING CYCLE 
The subscription interface provides two billing-cycle options: 
●​ Monthly 
●​ Annual 
Monthly Billing 
The user is charged according to the monthly subscription price associated with the selected 
plan. 
Annual Billing 
The user is charged according to the annual price displayed for the selected plan. 
For the currently observed Premium plan: 
Monthly: ₹499/month​
 Annual: ₹5,988/year 
 

4. BILLING INFORMATION 
A billing record may be associated with information such as: 
●​ Subscription plan 
●​ Billing cycle 
●​ Amount 
●​ Payment status 
●​ Payment date 
●​ Payment provider 
●​ Transaction/reference information 
●​ Invoice/receipt information, where available 
The exact billing fields available to users require verification from the WiseIN Billing interface. 
 
5. CURRENT SUBSCRIPTION BILLING 
INFORMATION 
The reviewed WiseIN Subscriptions screen displays information including: 
Plan 
WiseIN Go FREE 
Status 
Active 
Source 
FREE 
Next Payment 
The screen currently displays: 
Oct 21st, 2026 
This information is displayed within the user's subscription information. 

 
6. BILLING FLOW 
The relationship between subscription, payment, and billing can be represented as: 
User 
  ↓ 
Selects Subscription Plan 
  ↓ 
Chooses Billing Cycle 
  ↓ 
Payment 
  ↓ 
Payment Provider 
  ↓ 
Payment Confirmation 
  ↓ 
Subscription Activated / Updated 
  ↓ 
Billing Record 
 
7. BILLING QUESTIONS USERS MAY ASK 
Q1. What is my current plan? 
The user's current subscription plan can be viewed from the Subscriptions section. 
 
Q2. How much does Premium cost? 
The currently displayed Premium price is: 
₹499/month 
The annual Premium price currently displayed is: 
₹5,988/year 
Prices should always be confirmed against the current WiseIN subscription page. 

 
Q3. Is annual billing available? 
Yes. The currently reviewed subscription interface provides a Monthly / Annual billing-cycle 
selector for Premium. 
 
Q4. When will I be charged? 
The billing date depends on the user's subscription and billing cycle. 
The user's subscription page should be used to determine the applicable payment/billing date. 
 
Q5. Where can I check my subscription? 
Go to: 
Settings → Subscriptions 
The page displays the user's current plan and associated subscription information. 
 
8. BILLING ISSUE: WRONG CHARGE 
If a user reports: 
"I was charged the wrong amount." 
The AI Assistant should: 
1.​ Ask which plan the user selected. 
2.​ Ask whether they selected monthly or annual billing. 
3.​ Ask for the amount that was charged. 
4.​ Ask for the transaction/reference information where appropriate. 
5.​ Compare the charge with the currently displayed plan pricing. 
6.​ Escalate if the charge cannot be verified. 
The AI should not immediately confirm that the user was incorrectly charged without 
verifying the transaction. 

 
9. BILLING ISSUE: UNEXPECTED 
CHARGE 
If a user reports an unexpected charge: 
"Why was I charged?" 
The AI should determine: 
●​ Current subscription 
●​ Billing cycle 
●​ Date of charge 
●​ Amount charged 
●​ Whether the user recently changed plans 
●​ Whether the payment was associated with a WiseIN subscription 
If the charge cannot be identified from available information, escalate to human support. 
 
10. BILLING ISSUE: SUBSCRIPTION NOT 
UPDATED 
If a user says: 
"I paid for Premium but my account still shows Free." 
The AI should: 
1.​ Ask the user to check Settings → Subscriptions. 
2.​ Confirm the displayed plan. 
3.​ Ask whether the payment was completed. 
4.​ Ask whether money was deducted. 
5.​ Collect the relevant transaction information. 
6.​ Escalate the case if payment and subscription status do not match. 
 

11. BILLING ISSUE: PAYMENT 
SUCCESSFUL BUT NO BILLING RECORD 
If the user reports that payment was successful but the billing information has not updated: 
AI should: 
●​ Verify the subscription status. 
●​ Verify the payment status. 
●​ Ask for the transaction/reference ID if necessary. 
●​ Avoid asking for sensitive payment credentials. 
●​ Escalate the issue if the records cannot be reconciled. 
 
12. BILLING DOCUMENTS 
A billing system may provide documents such as: 
●​ Payment receipts 
●​ Invoices 
●​ Billing statements 
●​ Transaction records 
However, the availability of these documents in WiseIN has not yet been verified. 
The AI Assistant must not tell users that an invoice or receipt is available unless that 
functionality has been confirmed. 
 
13. BILLING SECURITY 
Billing information can contain sensitive financial information. 
The AI Assistant must never request: 
●​ Card number 
●​ CVV 
●​ UPI PIN 

●​ Banking password 
●​ Payment OTP 
●​ Full payment credentials 
Only information required for legitimate transaction/support verification should be requested. 
 
14. BILLING SUPPORT ESCALATION 
Billing issues should be escalated when: 
●​ The charged amount cannot be identified. 
●​ A successful payment is not reflected in the subscription. 
●​ The user reports a duplicate charge. 
●​ The user disputes a charge. 
●​ Billing information conflicts with payment information. 
●​ A refund or billing adjustment requires manual verification. 
●​ The payment provider and WiseIN show different transaction states. 
 
15. AI CUSTOMER SUPPORT EXAMPLES 
Example 1 — Current Plan 
User: 
What plan am I currently on? 
AI: 
You can check your current plan by going to Settings → Subscriptions. The page 
shows your active plan, subscription status, and related billing information. 
 
Example 2 — Premium Price 
User: 
How much is WiseIN Premium? 

AI: 
The currently displayed Premium plan is ₹499 per month. An annual billing option 
is also available, currently displayed as ₹5,988 per year. Please check the current 
subscription page for the latest pricing. 
 
Example 3 — Unexpected Charge 
User: 
Why did WiseIN charge me? 
AI: 
Let's check your subscription and billing details first. Please verify your current plan, 
billing cycle, charge amount, and payment date. If the charge still cannot be 
identified, I can help you escalate it to customer support. 
 
Example 4 — Payment but Plan Not Updated 
User: 
I paid for Premium but I'm still seeing the Free plan. 
AI: 
Please check Settings → Subscriptions and confirm which plan is currently 
displayed. If your payment was completed but your plan hasn't been updated, the 
transaction may need to be verified by WiseIN support. 
 
16. AI RESPONSE RULES 
The AI SHOULD 
●​ Explain the difference between billing, payments, and subscriptions. 
●​ Direct users to Settings → Subscriptions when checking their current plan. 
●​ Use the current pricing shown by WiseIN. 
●​ Explain monthly and annual billing where applicable. 

●​ Help users identify basic billing issues. 
●​ Escalate unresolved billing discrepancies. 
●​ Protect sensitive financial information. 
The AI SHOULD NOT 
●​ Guarantee a refund. 
●​ Confirm an incorrect charge without verification. 
●​ Claim that an invoice exists unless verified. 
●​ Invent billing dates. 
●​ Invent billing statuses. 
●​ Request card numbers, CVV, UPI PIN, or OTP. 
●​ Expose another user's billing information. 
 
17. VERIFIED INFORMATION 
Information 
Status 
Subscription has billing-related information 
✅ Verified 
Monthly billing option 
✅ Verified 
Annual billing option 
✅ Verified 
Premium ₹499/month 
✅ Currently observed 
Premium ₹5,988/year 
✅ Currently observed 
Student Premium ₹199/month 
✅ Currently observed 
WiseIN Go ₹0/month 
✅ Currently observed 
Subscription status displayed 
✅ Verified 
Payment provider information 
✅ Verified 
Dedicated Billing page 
⚠️ Requires verification 
Billing history 
⚠️ Requires verification 
Invoice generation 
⚠️ Requires verification 

Receipt download 
⚠️ Requires verification 
Refund management 
⚠️ Requires verification 
Billing address management 
⚠️ Requires verification 
 
18. RELATED WISEIN MODULES 
Related Documents: 
●​ 53 — Subscriptions 
●​ 54 — Billing 
●​ 55 — Privacy 
●​ 56 — Security 
●​ 68 — Customer Support 
●​ 69 — Human Escalation 
Important: If your numbering has 54 = Billing, then the next document should be 
55 = Privacy. The earlier list you gave had "54 Payments, 55 Billing", so we've now 
corrected the sequence according to your latest numbering: 54 Billing. 
 
19. KNOWLEDGE BASE SUMMARY 
Feature: Billing​
 Navigation: Settings → Subscriptions / Billing-related information​
 Purpose: Manage and understand subscription-related charges and billing information.​
 Billing Cycles: Monthly / Annual​
 Observed Premium Pricing: ₹499/month or ₹5,988/year​
 Payment Provider: Razorpay​
 Escalation: Required for unresolved billing discrepancies or transaction issues. 
Document Status: 🟡 Partially Verified — Billing-specific UI requires confirmation 
 



---

