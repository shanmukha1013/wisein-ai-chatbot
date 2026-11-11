# Organization Analytics

## Source: WISEIN-ORGANIZATION-ANALYTICS-044.pdf

WISEIN (WISEIN.IN) — ORGANIZATION ANALYTICS KNOWLEDGE BASE DATASET 
Document ID: WISEIN-ORGANIZATION-ANALYTICS-044 
Document Type: Product / Feature Knowledge Base 
Feature: Organization Analytics 
Platform: WiseIN 
 
1. OVERVIEW 
Organization Analytics is the analytics area associated with a WiseIN Organization. It 
provides an organization-level view of activity and meeting-related performance through 
summary metrics, revenue trends, and meeting records. 
WiseIN's current public Organization offering explicitly lists Organization Analytics as a 
Growth & Operations feature. The global pricing page describes this as a company-wide 
analytics dashboard, while the Organization page shows Analytics as one of the main 
dashboard areas alongside Employees and Meetings.  
The supplied Analytics screenshot shows a dashboard containing: 
• 
Monthly Revenue  
• 
New Meetings  
• 
Total Revenue  
• 
Total Meetings  
• 
Month Wise Revenue chart  
• 
Revenue-period controls  
• 
Meeting records  
• 
Pagination and rows-per-page controls  
This document defines what the chatbot can safely explain about Organization Analytics 
and clearly separates verified product information from information that is not publicly 
documented. 
 
2. PURPOSE OF ORGANIZATION ANALYTICS 

Organization Analytics is intended to help an Organization monitor activity associated with 
its WiseIN presence, particularly: 
• 
Meeting activity  
• 
Paid meeting/bookings revenue  
• 
Recent meeting creation  
• 
Overall meeting totals  
• 
Revenue trends over time  
• 
Individual meeting records  
The public WiseIN Organization material positions Analytics as part of the organization's 
broader growth and operations functionality.  
Important clarification 
The term Revenue in the supplied Analytics UI should not automatically be interpreted as 
the organization's overall business revenue. 
The screenshot specifically describes: 
“Regular paid bookings” 
under Total Revenue, indicating that the displayed revenue is associated with WiseIN's 
meeting/booking activity rather than necessarily representing the organization's external 
business revenue. 
The chatbot should therefore describe this as WiseIN meeting/booking revenue shown 
by the analytics dashboard, unless the backend documentation confirms a different 
definition. 
 
3. WHERE ORGANIZATION ANALYTICS FITS IN WISEIN 
WiseIN's current Organization experience includes several connected areas: 
• 
Organization Profile  
• 
Organization Verification  
• 
Employees / People  
• 
Posts  

• 
Clips  
• 
News  
• 
Jobs  
• 
Funding  
• 
Meetings  
• 
Analytics  
• 
Organization access and permissions  
The official WiseIN Organization page presents a dashboard containing Employees, 
Meetings, and Analytics.  
The current WiseIN home page also describes Company Pages as supporting company 
bios, teams, testimonials, jobs, and analytics.  
 
4. ORGANIZATION ANALYTICS DASHBOARD 
The supplied screenshot shows the Analytics dashboard with four summary cards at the 
top. 
These cards provide a quick overview before the user examines the revenue chart or 
meeting records. 
The four visible metrics are: 
1. Monthly Revenue  
2. New Meetings  
3. Total Revenue  
4. Total Meetings  
 
5. MONTHLY REVENUE 
Dashboard label 
Monthly Revenue 
Screenshot behavior 

The supplied screenshot shows: 
₹0.00 
with the description: 
“Last 30 days” 
and supporting text: 
“Regular meetings for the last 30 days” 
Meaning 
This metric represents the revenue associated with regular meetings during the displayed 
recent period. 
Based on the current UI, the period shown is the last 30 days. 
Chatbot answer 
If a user asks: 
“What is Monthly Revenue in Organization Analytics?” 
Recommended answer: 
Monthly Revenue shows the revenue associated with regular meetings during the last 30 
days. 
If the dashboard currently displays a different value, the chatbot should obtain the current 
value from the organization's authorized analytics data rather than relying on the 
knowledge base. 
Important 
Do not describe Monthly Revenue as: 
• 
total company sales  
• 
organization profit  
• 
salary revenue  
• 
annual revenue  
• 
external business revenue  
unless WiseIN's backend documentation explicitly defines it that way. 

 
6. NEW MEETINGS 
Dashboard label 
New Meetings 
Screenshot behavior 
The supplied screenshot shows: 
0 
with: 
“Last 30 days” 
and supporting text: 
“Regular meetings created recently” 
Meaning 
New Meetings represents regular meetings created during the recent 30-day period 
displayed by the dashboard. 
Chatbot answer 
New Meetings shows the number of regular meetings created during the last 30 days. 
Important distinction 
New Meetings is a recent-period metric. 
It should not be confused with Total Meetings, which represents the all-time meeting total 
shown in the supplied UI. 
 
7. TOTAL REVENUE 
Dashboard label 
Total Revenue 
Screenshot behavior 
The supplied screenshot shows: 
₹0.00 

with: 
“All time” 
and: 
“Regular paid bookings” 
Meaning 
Total Revenue represents the all-time revenue associated with regular paid bookings 
shown by the Organization Analytics dashboard. 
Chatbot answer 
Total Revenue shows the all-time revenue from regular paid bookings recorded by the 
dashboard. 
Important 
The chatbot should not interpret this as the organization's complete business revenue. 
The UI specifically connects this metric to regular paid bookings. 
 
8. TOTAL MEETINGS 
Dashboard label 
Total Meetings 
Screenshot behavior 
The supplied screenshot shows: 
0 
with: 
“All time” 
and: 
“Regular meetings total” 
Meaning 
Total Meetings represents the all-time count of regular meetings shown by the analytics 
dashboard. 

Chatbot answer 
Total Meetings shows the total number of regular meetings recorded by the organization 
over the available all-time period. 
 
9. MONTH WISE REVENUE 
Below the summary cards, the supplied screenshot contains a chart titled: 
Month Wise Revenue 
The subtitle says: 
“Total for the last 3 months” 
The chart displays dates along the horizontal axis. 
The supplied screenshot shows dates including: 
• 
Sep 17  
• 
Sep 18  
• 
Sep 19  
• 
Sep 20  
• 
Sep 21  
• 
Sep 22  
The chart currently contains a flat line because the displayed revenue is ₹0.00. 
Purpose 
The chart provides a visual representation of revenue over time. 
Chatbot answer 
The Month Wise Revenue chart shows the revenue trend for the selected analytics period. 
In the current UI, it is presented as a recent three-month revenue view. 
 
10. REVENUE PERIOD CONTROLS 
The supplied screenshot shows three controls in the Month Wise Revenue section: 
• 
30 days  

• 
7 days  
• 
day  
These controls allow the user to change the time granularity or period displayed in the 
revenue visualization. 
Current UI observation 
The exact internal calculation or aggregation logic for each option is not publicly 
documented. 
Therefore, the chatbot should not invent statements such as: 
• 
“30 days always means exactly 30 calendar days”  
• 
“7 days always starts on Monday”  
• 
“day means today's revenue”  
• 
“day displays hourly revenue”  
unless the application/backend documentation confirms those behaviors. 
Safe chatbot answer 
The revenue chart provides 30-day, 7-day, and day-based viewing options. The exact 
aggregation logic for each option depends on the current analytics implementation. 
 
11. MEETING ANALYTICS TABLE 
The lower part of the supplied dashboard contains a meeting data table. 
The visible column headings are: 
• 
Meeting  
• 
Price  
• 
Status  
• 
Duration  
• 
In Meet Time  
• 
Date  
This provides a more detailed view of individual meeting records. 

 
12. MEETING 
The Meeting column identifies the meeting associated with a particular analytics record. 
The exact format of the meeting identifier or title is not established by the supplied 
screenshot because the screenshot currently contains no meeting records. 
Therefore, the chatbot should not invent a particular meeting-name format. 
 
13. PRICE 
The Price column represents the price associated with the meeting record. 
Because the screenshot contains no meeting rows, the exact behavior for: 
• 
free meetings  
• 
discounted meetings  
• 
currency conversion  
• 
refunds  
• 
cancelled paid meetings  
• 
payment failures  
is not established by the available sources. 
Safe chatbot answer 
The Price column displays the price associated with each meeting record. 
 
14. STATUS 
The Status column displays the status associated with a meeting. 
The screenshot does not contain populated meeting rows, so the exact list of possible 
status values is not verified. 
Do not invent statuses such as: 
• 
Completed  
• 
Cancelled  

• 
Pending  
• 
Paid  
• 
Refunded  
• 
No-show  
unless those values are confirmed from the live application or backend documentation. 
Safe chatbot answer 
The Status column shows the current status recorded for the meeting. 
 
15. DURATION 
The Duration column provides the meeting duration. 
The available screenshot does not show an actual populated value. 
Therefore, the chatbot should not claim a specific duration format such as: 
• 
minutes only  
• 
HH:MM:SS  
• 
scheduled duration  
• 
actual duration  
unless verified. 
Safe chatbot answer 
The Duration column displays the duration associated with the meeting record. 
 
16. IN MEET TIME 
The dashboard contains a column explicitly labelled: 
In Meet Time 
This appears to represent meeting participation or time spent in the meeting. 
However, the supplied screenshot does not contain populated rows, and the public WiseIN 
website does not provide a formal definition of this field. 

Therefore, the chatbot should not claim that it definitively means: 
• 
exact attendance time  
• 
actual call duration  
• 
participant join time  
• 
host duration  
• 
billable duration  
unless the application or backend documentation confirms it. 
Safe chatbot answer 
“In Meet Time” is a meeting analytics field shown in the Organization dashboard. Its exact 
calculation should be taken from the current WiseIN implementation. 
 
17. DATE 
The Date column displays the date associated with the meeting record. 
The screenshot does not establish whether this refers to: 
• 
meeting creation date  
• 
scheduled date  
• 
meeting start date  
• 
completion date  
• 
payment date  
Therefore, the chatbot should simply describe it as the date recorded for the meeting until 
the backend definition is verified. 
 
18. EMPTY ANALYTICS STATE 
The supplied screenshot currently shows: 
• 
Monthly Revenue: ₹0.00  
• 
New Meetings: 0  
• 
Total Revenue: ₹0.00  

• 
Total Meetings: 0  
• 
No populated meeting rows  
The meeting table shows: 
“0 of 0 row(s) selected” 
and: 
“Page 1 of 0” 
This indicates that the current organization has no meeting records available in the 
displayed analytics view. 
Recommended chatbot response 
Your Organization Analytics currently shows no recorded regular meetings or paid 
bookings. As a result, revenue is ₹0.00 and meeting counts are 0 in the displayed 
dashboard. 
This answer is appropriate when the chatbot has access to the user's current analytics 
data and those values actually match the current dashboard. 
 
19. PAGINATION 
The meeting table includes pagination controls. 
The supplied UI shows: 
Rows per page: 10 
and navigation controls for moving between pages. 
The screenshot currently shows: 
Page 1 of 0 
because there are no records. 
Important 
The screenshot establishes that a rows-per-page control exists and currently defaults to 10 
in the observed UI. 
It does not establish that 10 is permanently the only available page size. 

Do not claim additional values such as 25, 50, or 100 unless they are observed or 
documented. 
 
20. ORGANIZATION ANALYTICS AND MEETINGS 
Organization Analytics is closely related to WiseIN's meeting functionality. 
WiseIN publicly describes video meetings, smart scheduling, and AI-generated meeting 
summaries as core platform capabilities. The Organization offering also presents 
integrated scheduling and meetings as part of the organization experience.  
The Organization dashboard therefore provides a way to monitor meeting-related activity. 
However, the chatbot should distinguish between: 
Meeting functionality 
and 
Analytics about meetings. 
For example: 
“How do I schedule a meeting?” 
is a meeting/scheduling question. 
“How many meetings did my organization have?” 
is an analytics question. 
 
21. ORGANIZATION ANALYTICS VS ORGANIZATION MEETINGS 
Organization Meetings 
Concerned with the actual meeting process, such as: 
• 
scheduling  
• 
joining  
• 
conducting meetings  
• 
meeting details  
Organization Analytics 

Concerned with recorded metrics and historical information, such as: 
• 
recent meeting count  
• 
total meeting count  
• 
booking revenue  
• 
revenue trends  
• 
meeting records  
The chatbot should route questions to the correct knowledge area. 
 
22. ORGANIZATION ANALYTICS VS PROFILE ANALYTICS 
WiseIN also advertises analytics for individual profiles. 
The current pricing page lists: 
• 
Basic — Basic profile analytics  
• 
Premium — Advanced profile analytics  
• 
Organization — Company-wide analytics dashboard.  
These should not be treated as the same feature. 
Profile Analytics 
Concern an individual user's profile and its activity/visibility. 
Organization Analytics 
Concern the Organization's company-wide dashboard and organization-related activity. 
Example 
User: 
“How many meetings did my company have?” 
Route to: 
Organization Analytics 
User: 
“How many people viewed my profile?” 

Route to: 
Profile Analytics 
 
23. ORGANIZATION PLAN 
The current WiseIN pricing page lists Organization as a dedicated plan and includes: 
• 
CIN & GST verification  
• 
Up to 5 teams verified profiles  
• 
Organization branding page  
• 
Hiring & Job posting tools  
• 
Company-wide analytics dashboard  
• 
Dedicated support  
• 
Organization badge on profile.  
The India-facing WiseIN homepage also lists Organization Analytics under the Growth & 
Operations section of the Organization offering.  
Chatbot answer 
If asked: 
“Does WiseIN Organization include analytics?” 
Yes. WiseIN currently lists Organization Analytics as part of the Organization offering, and 
the pricing page describes a company-wide analytics dashboard.  
 
24. WHAT THE PUBLIC WEBSITE CONFIRMS 
The following Organization Analytics facts are currently supported by official WiseIN 
sources: 
• 
Organization Analytics is an Organization feature.  
• 
WiseIN lists it under Organization Growth & Operations.  
• 
The Organization plan includes a company-wide analytics dashboard.  

• 
WiseIN's Organization dashboard includes Analytics alongside Employees and 
Meetings.  
• 
WiseIN's Organization experience includes meeting functionality.  
• 
The supplied UI shows revenue and meeting analytics.  
• 
The supplied UI shows Monthly Revenue.  
• 
The supplied UI shows New Meetings.  
• 
The supplied UI shows Total Revenue.  
• 
The supplied UI shows Total Meetings.  
• 
The supplied UI shows a Month Wise Revenue chart.  
• 
The supplied UI shows 30-day, 7-day, and day controls.  
• 
The supplied UI shows a meeting-record table.  
• 
The supplied UI shows Meeting, Price, Status, Duration, In Meet Time, and Date 
columns.  
• 
The supplied UI shows pagination and a rows-per-page control.  
Official WiseIN sources confirm the broader Organization Analytics capability, while the 
detailed metric definitions above come from the supplied current UI.  
 
25. INFORMATION NOT CURRENTLY VERIFIED 
The following should NOT be presented as confirmed chatbot knowledge unless internal 
WiseIN documentation or live application behavior verifies them: 
• 
Exact revenue calculation formula  
• 
Whether refunds are deducted from revenue  
• 
Whether cancelled meetings affect revenue  
• 
Whether taxes or platform fees are included  
• 
Exact currency conversion rules  
• 
Exact meaning of every meeting status  
• 
Exact meaning of “In Meet Time”  

• 
Whether Duration means scheduled or actual duration  
• 
Exact meaning of the “day” chart option  
• 
Exact timezone used for analytics  
• 
Whether analytics update instantly or periodically  
• 
Analytics refresh interval  
• 
Historical data retention period  
• 
Export to CSV/Excel/PDF  
• 
Download reports  
• 
Email analytics reports  
• 
Scheduled reports  
• 
Custom date-range filtering  
• 
Employee-level analytics  
• 
Department-level analytics  
• 
Job analytics  
• 
Post analytics  
• 
Follower analytics  
• 
Organization profile views  
• 
Conversion rates  
• 
Hiring funnel metrics  
• 
Revenue forecasting  
• 
AI-generated analytics insights  
• 
Custom dashboards  
• 
Admin-only analytics permissions  
• 
Exact Organization Analytics API endpoints  
• 
Exact formulas used by backend aggregation  
• 
Exact maximum historical period  

This is especially important for the RAG chatbot: do not fill these gaps using 
assumptions. 
 
26. CURRENT DATA VS KNOWLEDGE BASE DATA 
Organization Analytics requires a clear distinction between static documentation and live 
organization data. 
RAG / Knowledge Base should answer: 
• 
What is Organization Analytics?  
• 
What does Monthly Revenue mean?  
• 
What is New Meetings?  
• 
What is Total Revenue?  
• 
What is Total Meetings?  
• 
What does the Month Wise Revenue chart show?  
• 
What columns are available in the meeting analytics table?  
• 
What is the purpose of the analytics dashboard?  
• 
Is Organization Analytics available as part of the Organization offering?  
Live API / Backend should answer: 
• 
What is my current Monthly Revenue?  
• 
How many meetings did my organization have?  
• 
What is my current Total Revenue?  
• 
What meetings were recorded today?  
• 
What was the revenue yesterday?  
• 
Show my latest meeting records.  
• 
What is the status of a specific meeting?  
• 
What is the current meeting price?  
• 
What is the current analytics value for a selected period?  
This distinction is critical. 

The chatbot must not answer a live analytics question from a static screenshot or 
documentation example. 
 
27. EXAMPLE: STATIC VS LIVE ANSWER 
User 
“What does Total Revenue mean?” 
RAG can answer: 
Total Revenue represents the all-time revenue from regular paid bookings shown by the 
Organization Analytics dashboard. 
User 
“What is our Total Revenue right now?” 
The chatbot must query the authorized analytics backend. 
It should not answer: 
₹0.00 
merely because the supplied screenshot shows ₹0.00. 
The screenshot is an example/current UI observation, not proof of the user's current live 
organization value. 
 
28. RECOMMENDED ANALYTICS API DESIGN 
For the WiseIN AI chatbot implementation, Organization Analytics should ideally be 
exposed through controlled backend APIs rather than allowing the LLM direct database 
access. 
A conceptual API structure could include: 
GET /organization/{organization_id}/analytics/summary 
GET /organization/{organization_id}/analytics/revenue 
GET /organization/{organization_id}/analytics/meetings 
Possible backend response categories: 

summary 
monthly_revenue 
new_meetings 
total_revenue 
total_meetings 
Revenue history could return: 
date 
revenue 
period 
Meeting analytics could return: 
meeting 
price 
status 
duration 
in_meet_time 
date 
These are recommended architectural examples, not claims about WiseIN's existing API 
endpoints. 
The actual WiseIN API names and schemas must be obtained from the development 
team/backend implementation. 
 
29. AUTHORIZATION REQUIREMENTS 
Organization Analytics contains organization-specific information. 
Therefore, the chatbot should verify that the authenticated user is authorized to access the 
organization's analytics before returning live values. 
The system should validate: 
Authenticated user 

        ↓ 
Organization membership 
        ↓ 
Analytics permission 
        ↓ 
Requested organization 
        ↓ 
Analytics API 
        ↓ 
Chatbot response 
The LLM should never be allowed to freely query arbitrary organizations. 
 
30. SECURITY RULES 
The chatbot should never: 
• 
expose another organization's analytics  
• 
reveal internal database identifiers  
• 
reveal API credentials  
• 
reveal backend query syntax  
• 
expose payment credentials  
• 
expose private meeting information without authorization  
• 
provide another organization's revenue  
• 
provide another organization's meeting records without permission  
• 
fabricate analytics values  
Analytics responses should be scoped to the authenticated user's authorized organization. 
 
31. PRIVACY CONSIDERATIONS 

Meeting and organization analytics can contain business-sensitive information. 
WiseIN's Content Policies explicitly prohibit publicly posting financial data, ID proofs, 
salary details, internal company information, or business strategies. The policy also treats 
meeting conversations, recordings, transcripts, and AI summaries as private content 
requiring appropriate consent before sharing.  
Therefore, the chatbot should treat organization analytics as potentially sensitive 
information. 
For example, it should not respond to an unauthorized user asking: 
“How much revenue did Company X make through WiseIN?” 
unless the system has an authorized mechanism to provide that data. 
 
32. TROUBLESHOOTING — ANALYTICS SHOWS ₹0.00 
If a user says: 
“My Organization Analytics shows ₹0.00 revenue.” 
The chatbot should first explain: 
The Analytics dashboard shows revenue associated with regular paid bookings. If there are 
no qualifying paid bookings in the selected period, the displayed revenue can be ₹0.00. 
Then, if live backend access exists, check: 
• 
selected period  
• 
organization ID  
• 
paid booking records  
• 
booking status  
• 
payment status  
• 
analytics data availability  
Do not immediately claim that a payment system is broken. 
 
33. TROUBLESHOOTING — MEETINGS SHOW 0 

If the dashboard shows: 
New Meetings: 0 
and/or: 
Total Meetings: 0 
the chatbot should explain that the current analytics view has no qualifying regular meeting 
records. 
If the user says they definitely had meetings, the chatbot should investigate through 
authorized live data rather than assuming the analytics dashboard is correct or incorrect. 
Possible investigation areas: 
• 
correct Organization selected  
• 
selected analytics period  
• 
meeting type  
• 
meeting creation status  
• 
data synchronization  
• 
analytics refresh  
• 
backend record availability  
Exact synchronization behavior is not publicly documented and should not be invented. 
 
34. TROUBLESHOOTING — CHART HAS NO DATA 
If the Month Wise Revenue chart is empty or flat: 
1. Check the selected period.  
2. Check whether qualifying paid bookings exist.  
3. Check whether the organization has recorded meeting revenue.  
4. Verify the live analytics response.  
5. If the underlying data exists but the chart remains empty, escalate as a possible 
UI/data-rendering issue.  

The chatbot should not automatically tell the user to reinstall the application or clear 
browser data unless there is evidence of a client-side issue. 
 
35. TROUBLESHOOTING — MEETING TABLE IS EMPTY 
If the meeting table shows: 
0 of 0 row(s) selected 
and no records: 
The meeting analytics table currently has no records for the available analytics data. 
If the user expects records: 
I can help check the current organization meeting data and selected analytics period. 
If a live API is unavailable, the chatbot should clearly state that it cannot verify the current 
records rather than inventing them. 
 
36. COMMON USER QUESTIONS 
“What is Organization Analytics?” 
Organization Analytics is the organization-level analytics dashboard used to view meeting 
activity and related booking revenue. WiseIN currently lists Organization 
Analytics/company-wide analytics as part of its Organization offering.  
“What is Monthly Revenue?” 
Monthly Revenue shows revenue associated with regular meetings during the last 30 days, 
according to the current dashboard UI. 
“What is New Meetings?” 
New Meetings shows regular meetings created during the last 30 days. 
“What is Total Revenue?” 
Total Revenue shows all-time revenue from regular paid bookings shown by the analytics 
dashboard. 
“What is Total Meetings?” 
Total Meetings shows the all-time total of regular meetings recorded by the dashboard. 

“What is Month Wise Revenue?” 
It is the revenue trend chart shown in Organization Analytics. 
“Can I see individual meetings?” 
The current Organization Analytics UI includes a meeting table with Meeting, Price, Status, 
Duration, In Meet Time, and Date columns. 
“Why is my revenue zero?” 
The dashboard currently shows ₹0.00 when there is no qualifying revenue in the displayed 
analytics data. If you expect paid bookings but the value remains zero, the current 
organization and analytics period should be checked. 
“Why does my dashboard show zero meetings?” 
The current analytics view does not have qualifying meeting records. If you expect meetings 
to appear, the organization, selected period, and current meeting data should be checked. 
 
37. AI INTENT CATEGORIES 
The chatbot should recognize the following Organization Analytics intents. 
Analytics Overview 
Examples: 
• 
What is Organization Analytics?  
• 
What does the Analytics dashboard do?  
• 
Explain Organization Analytics.  
Revenue 
Examples: 
• 
What is Monthly Revenue?  
• 
What is Total Revenue?  
• 
How is revenue shown?  
• 
Why is revenue zero?  
Meeting Metrics 

Examples: 
• 
What is New Meetings?  
• 
What is Total Meetings?  
• 
How many meetings do we have?  
Revenue Chart 
Examples: 
• 
What is Month Wise Revenue?  
• 
What does the revenue graph show?  
• 
What is the 30 days option?  
Meeting Records 
Examples: 
• 
Show my meeting analytics.  
• 
What columns are in the meeting table?  
• 
What does Price mean?  
• 
What does Status mean?  
• 
What is In Meet Time?  
Current Analytics 
Examples: 
• 
How much revenue do we have?  
• 
How many meetings have we had?  
• 
What are our latest meetings?  
• 
What is our revenue this month?  
These require authorized live data. 
Troubleshooting 
Examples: 
• 
Analytics is empty.  

• 
Revenue isn't updating.  
• 
Meetings are not showing.  
• 
My analytics are incorrect.  
 
38. ENTITY EXTRACTION 
Useful entities for Organization Analytics include: 
organization 
organization_id 
analytics 
revenue 
monthly_revenue 
total_revenue 
meeting 
meetings 
new_meetings 
total_meetings 
paid_booking 
month_wise_revenue 
period 
date 
status 
price 
duration 
in_meet_time 
Example: 
“How much revenue did my organization make in the last 30 days?” 

Extract: 
intent = current_organization_revenue 
organization = authenticated organization 
metric = monthly_revenue 
period = last_30_days 
data_source = live_analytics_api 
 
39. RAG METADATA 
Recommended metadata: 
document_id: 
WISEIN-ORGANIZATION-ANALYTICS-001 
 
feature: 
Organization Analytics 
 
category: 
Organization 
 
subcategory: 
Analytics 
 
entities: 
revenue, meetings, bookings, analytics, organization 
 
source_type: 
official_website + supplied_ui 

 
audience: 
organization_user 
 
requires_live_data: 
true 
 
sensitivity: 
organization_private 
 
version: 
current 
 
last_reviewed: 
2026-09 
 
40. GOLDEN ANSWERS FOR THE CHATBOT 
Golden Answer 1 — Overview 
Organization Analytics provides an organization-level view of meeting activity and related 
booking revenue. The current dashboard includes Monthly Revenue, New Meetings, Total 
Revenue, Total Meetings, a revenue trend chart, and meeting records. 
Golden Answer 2 — Monthly Revenue 
Monthly Revenue represents revenue from regular meetings during the last 30 days, 
according to the current Analytics dashboard. 
Golden Answer 3 — Total Revenue 
Total Revenue represents all-time revenue from regular paid bookings shown by the 
Analytics dashboard. 

Golden Answer 4 — New Meetings 
New Meetings represents regular meetings created during the last 30 days. 
Golden Answer 5 — Total Meetings 
Total Meetings represents the all-time total of regular meetings recorded by the dashboard. 
Golden Answer 6 — Live Data 
I can explain what each Organization Analytics metric means, but current revenue and 
meeting totals must come from your organization's live analytics data. 
Golden Answer 7 — Zero Data 
Your current Analytics view shows no qualifying meeting or paid-booking data for the 
displayed period. If you expect records to appear, I can help check the selected period and 
current organization data. 
 
41. CHATBOT GUARDRAILS 
The chatbot MUST: 
• 
distinguish Organization Analytics from Profile Analytics  
• 
distinguish meeting revenue from general company revenue  
• 
use live APIs for current analytics values  
• 
verify organization authorization  
• 
respect organization privacy  
• 
explain UI labels using verified documentation  
• 
preserve the exact terminology used in the interface  
• 
identify unsupported behavior as undocumented  
• 
avoid inventing formulas  
• 
avoid inventing analytics filters  
• 
avoid inventing report/export functionality  
The chatbot MUST NOT: 
• 
fabricate revenue  

• 
fabricate meeting counts  
• 
fabricate meeting records  
• 
claim that ₹0.00 is the current value unless live data confirms it  
• 
expose another organization's analytics  
• 
claim exact revenue formulas without backend confirmation  
• 
claim unsupported status values  
• 
claim unsupported export/report functionality  
• 
claim unsupported analytics refresh intervals  
• 
treat the screenshot as a live data source  
 
42. SOURCE PRIORITY 
For Organization Analytics questions, use this priority: 
Priority 1 — Live WiseIN backend/API 
Use for: 
• 
current revenue  
• 
current meeting counts  
• 
current meeting records  
• 
current status  
• 
current prices  
• 
current dates  
• 
current analytics values  
Priority 2 — Current WiseIN official website 
Use for: 
• 
Organization Analytics availability  
• 
Organization plan  
• 
company-wide analytics dashboard  

• 
broader Organization functionality  
WiseIN's current pricing page explicitly lists the company-wide analytics dashboard, and 
the Organization page lists Organization Analytics under Growth & Operations.  
Priority 3 — Current WiseIN UI 
Use for: 
• 
exact labels  
• 
visible dashboard fields  
• 
chart controls  
• 
table columns  
• 
pagination  
• 
current UI wording  
Priority 4 — Internal WiseIN product/developer documentation 
Use when available for: 
• 
metric formulas  
• 
database definitions  
• 
API schemas  
• 
permission rules  
• 
refresh behavior  
• 
status definitions  
Priority 5 — Older documentation 
Use only when current sources do not contradict it. 
 
43. FINAL KNOWLEDGE RULE 
The most important rule for Organization Analytics is: 
The knowledge base explains the analytics feature; the live backend provides the 
organization's actual analytics. 
For example: 

Knowledge Base: 
“Total Revenue represents all-time revenue from regular paid bookings.” 
Live API: 
“Your organization's current Total Revenue is ₹X.” 
The chatbot must never replace the second with a value taken from a screenshot, example, 
cached document, or another organization. 
 
 



---

