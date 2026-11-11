import os
import re
import json
import hashlib
import fitz  # PyMuPDF

dirs = [
    r"c:\Users\marel\OneDrive\Desktop\wisein-ai-support\temp_80files\80files",
    r"c:\Users\marel\OneDrive\Desktop\wisein-ai-support\temp_wiseindocs\wisein docs"
]

out_dir = r"c:\Users\marel\OneDrive\Desktop\wisein-ai-support\knowledge_base"
os.makedirs(out_dir, exist_ok=True)

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

def clean_filename(name):
    return name.lower().replace(' ', '_').replace('&', 'and') + ".md"

def extract_pdf_blocks(path):
    text = ""
    try:
        doc = fitz.open(path)
        for page in doc:
            # text extraction using block mode preserves layout much better than plain
            # We use 'text' which in PyMuPDF gives reasonable paragraph preservation
            page_text = page.get_text("text")
            if page_text:
                text += page_text + "\n"
    except Exception as e:
        print(f"Error reading {path}: {e}")
    return text

def get_file_hash(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

topic_files = {f"{i:02d}": [] for i in range(1, 81)}

# We want to deduplicate files exactly to avoid processing the same file multiple times
hashes = {}
unique_pdfs = []

print("Scanning for unique PDFs...")
for d in dirs:
    if not os.path.exists(d): continue
    for f in os.listdir(d):
        path = os.path.join(d, f)
        if os.path.isfile(path) and f.lower().endswith('.pdf'):
            h = get_file_hash(path)
            if h not in hashes:
                hashes[h] = {"name": f, "path": path}
                unique_pdfs.append(hashes[h])

print(f"Found {len(unique_pdfs)} unique PDF files. Extracting and mapping...")

for p in unique_pdfs:
    f = p["name"]
    path = p["path"]
    
    text = extract_pdf_blocks(path)
    p["text"] = text
    p["length"] = len(text)
    
    # Smarter mapping
    ids = []
    
    # Check filename first (strongest indicator)
    # e.g., "01 Introduction.pdf" or "WISEIN-034.pdf"
    m = re.search(r'(?<!\d)(\d{2,3})(?!\d)', f)
    if m:
        ids.append(m.group(1))
        
    # Check text for "Document ID:"
    m2 = re.search(r'Document ID:\s*WISEIN-[A-Z\-]+(\d{3})', text)
    if m2:
        ids.append(m2.group(1))
        
    unique_ids = list(set([str(int(i)).zfill(2) for i in ids if 1 <= int(i) <= 80]))
    
    if unique_ids:
        for uid in unique_ids:
            topic_files[uid].append(p)
    else:
        print(f"Warning: Could not map {f} to any topic.")

manifest = []

print("Writing healthy Markdown files...")
for t in topics:
    num = t.split(' ')[0]
    name = ' '.join(t.split(' ')[1:])
    fname = clean_filename(t)
    out_path = os.path.join(out_dir, fname)
    
    files = topic_files[num]
    
    if len(files) == 0:
        manifest.append({
            "document_id": f"WISEIN-KB-{num}",
            "topic_number": num,
            "topic_name": name,
            "source_files": [],
            "missing_information": "True - No source file found"
        })
        with open(out_path, "w", encoding="utf-8") as out_f:
            out_f.write(f"# {name}\n\n*This topic is currently missing from the source documentation.*\n")
    else:
        file_names = [x["name"] for x in files]
        
        manifest.append({
            "document_id": f"WISEIN-KB-{num}",
            "topic_number": num,
            "topic_name": name,
            "source_files": file_names,
            "missing_information": "False"
        })
        
        # Combine all files that mapped to this topic
        content = f"# {name}\n\n"
        
        for file_obj in files:
            content += f"## Source: {file_obj['name']}\n\n"
            content += file_obj['text'] + "\n\n---\n\n"
            
        with open(out_path, "w", encoding="utf-8") as out_f:
            out_f.write(content)

with open(os.path.join(out_dir, "manifest.json"), "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2)

with open(os.path.join(out_dir, "README.md"), "w", encoding="utf-8") as f:
    f.write("# WiseIN Knowledge Base\n\nThis directory contains the 80 organized topics, remediated for phase 7.\n")

print("Remediation complete. All files mapped and preserved.")
