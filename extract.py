import os
import re
import json
from pypdf import PdfReader
import shutil

dirs = [
    r"c:\Users\marel\OneDrive\Desktop\wisein-ai-support\temp_80files\80files",
    r"c:\Users\marel\OneDrive\Desktop\wisein-ai-support\temp_wiseindocs\wisein docs"
]

topics = [
    "01 Introduction", "02 Terminology", "03 Sign Up", "04 Login",
    "05 Password & Account Recovery", "06 Email Verification", "07 Identity Verification",
    "08 Student Verification", "09 Onboarding", "10 Home", "11 Feed", "12 Posts",
    "13 Clips", "14 Explore", "15 Regular Search", "16 AI Search", "17 Topics",
    "18 Waves", "19 Jobs", "20 My Network", "21 Follow System", "22 Connections",
    "23 Chat", "24 Messaging", "25 Meetings", "26 Calendar", "27 Slot Booking",
    "28 Webinars", "29 Meeting Recording", "30 Transcription", "31 AI Meeting Summaries",
    "32 Profile", "33 Employment", "34 Education", "35 Projects", "36 Skills",
    "37 Profile Video", "38 Profile Analytics", "39 Organizations",
    "40 Organization Verification", "41 Organization Employees", "42 Organization Permissions",
    "43 Organization Jobs", "44 Organization Analytics", "45 Communities", "46 Events",
    "47 Founder Conversations", "48 Leadership Conversations", "49 Notifications",
    "50 Scheduled Posts", "51 Saved Content", "52 Ads", "53 Subscriptions",
    "54 Payments", "55 Billing", "56 Privacy", "57 Security", "58 Blocking",
    "59 Reporting", "60 Community Guidelines", "61 Content Policies",
    "62 Terms & Conditions", "63 Account Deactivation", "64 Account Deletion",
    "65 Logout", "66 Troubleshooting", "67 Error Codes", "68 Customer Support",
    "69 Human Escalation", "70 FAQ", "71 Mobile App", "72 Website", "73 AI Assistant",
    "74 AI Limitations", "75 Conversation History", "76 AI Tools", "77 RAG Knowledge",
    "78 Security for AI", "79 AI Analytics", "80 Knowledge Management"
]

topic_map = {t.split(' ')[0]: t for t in topics}

def extract_text_from_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            t = page.extract_text()
            if t: text += t + "\n"
        return text
    except Exception as e:
        return str(e)
        
def extract_text_from_docx(docx_path):
    # fallback for docx if any
    return ""

results = []

for d in dirs:
    if not os.path.exists(d): continue
    for f in os.listdir(d):
        path = os.path.join(d, f)
        if os.path.isfile(path):
            text = ""
            if f.lower().endswith('.pdf'):
                print(f"Processing PDF: {f}", flush=True)
                text = extract_text_from_pdf(path)
            elif f.lower().endswith('.docx'):
                print(f"Processing DOCX: {f}", flush=True)
                # just put a placeholder, we might not need to parse it if we can find topic from filename
                text = "DOCX file"
            
            # Find topic number
            # 1. From filename
            m = re.search(r'(?<!\d)(\d{2,3})(?!\d)', f)
            topic_num = None
            if m:
                num = int(m.group(1))
                if 1 <= num <= 80:
                    topic_num = f"{num:02d}"
            
            # 2. From text (e.g. Document ID: ...-002)
            if not topic_num:
                m = re.search(r'ID:.*?(\d{2,3})', text)
                if m:
                    num = int(m.group(1))
                    if 1 <= num <= 80:
                        topic_num = f"{num:02d}"
            
            # 3. Look for topic names in the first 500 chars
            if not topic_num:
                first_part = text[:1000].lower()
                for t_num, t_name in topic_map.items():
                    name_clean = ' '.join(t_name.split(' ')[1:]).lower()
                    if name_clean in first_part:
                        topic_num = t_num
                        break
                        
            results.append({
                "file": f,
                "path": path,
                "topic_num": topic_num,
                "text_preview": text[:200].replace('\n', ' '),
                "text_length": len(text)
            })

with open(r"c:\Users\marel\OneDrive\Desktop\wisein-ai-support\extraction_report.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print("Extraction complete. Processed", len(results), "files.")
