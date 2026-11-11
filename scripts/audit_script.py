import os
import re
import json
import hashlib
from collections import defaultdict
from pypdf import PdfReader
import difflib

dirs = [
    r"c:\Users\marel\OneDrive\Desktop\wisein-ai-support\temp_80files\80files",
    r"c:\Users\marel\OneDrive\Desktop\wisein-ai-support\temp_wiseindocs\wisein docs"
]
kb_dir = r"c:\Users\marel\OneDrive\Desktop\wisein-ai-support\knowledge_base"

# Load KB contents
kb_contents = {}
if os.path.exists(kb_dir):
    for f in os.listdir(kb_dir):
        if f.endswith('.md') and f != 'README.md':
            with open(os.path.join(kb_dir, f), 'r', encoding='utf-8') as file:
                topic_num_match = re.search(r'^(\d{2})_', f)
                if topic_num_match:
                    num = topic_num_match.group(1)
                else:
                    # try getting from manifest
                    pass
                kb_contents[f] = file.read().lower()
                
# Get chunks from temp_embeddings_local.jsonl
chunks_metadata = []
chunks_file = r"c:\Users\marel\OneDrive\Desktop\wisein-ai-support\temp_embeddings_local.jsonl"
if os.path.exists(chunks_file):
    with open(chunks_file, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                data = json.loads(line)
                chunks_metadata.append(data)
            except: pass

def get_file_hash(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

def extract_pdf(path):
    text = ""
    try:
        reader = PdfReader(path)
        for page in reader.pages:
            t = page.extract_text()
            if t: text += t + "\n"
    except Exception as e:
        text = str(e)
    return text

pdf_files = []
for d in dirs:
    if not os.path.exists(d): continue
    for f in os.listdir(d):
        if f.lower().endswith('.pdf'):
            path = os.path.join(d, f)
            pdf_files.append({"name": f, "path": path})

report = {
    "summary": {
        "total_source_files_discovered": len(pdf_files),
        "total_source_files_inspected": 0,
        "total_pages_sections_inspected": 0,
    },
    "file_mapping": [],
    "duplicates": [],
    "extraction_problems": [],
    "missing_content_suspects": [],
    "conflicts": []
}

hashes = {}
unique_pdfs = []

# Deduplicate identical files
for p in pdf_files:
    h = get_file_hash(p["path"])
    if h in hashes:
        report["duplicates"].append({"file1": p["name"], "file2": hashes[h]["name"], "type": "exact duplicate"})
    else:
        hashes[h] = p
        unique_pdfs.append(p)

report["summary"]["total_source_files_inspected"] = len(unique_pdfs)

# Process unique PDFs
for p in unique_pdfs:
    print(f"Inspecting {p['name']}...", flush=True)
    text = extract_pdf(p["path"])
    
    # check for extraction problems
    if len(text) < 50 and "pypdf" not in text.lower():
        report["extraction_problems"].append({"file": p["name"], "issue": "Very little text extracted, possible image-based PDF or extraction failure."})
    if "cid:" in text:
        report["extraction_problems"].append({"file": p["name"], "issue": "Contains cid: artifacts, font encoding issues."})
    
    # Estimate pages/sections (roughly by form feeds or just arbitrary length)
    pages = 1
    try:
        reader = PdfReader(p["path"])
        pages = len(reader.pages)
    except: pass
    report["summary"]["total_pages_sections_inspected"] += pages
    
    # Find mapped topics based on ID in text or filename
    ids = re.findall(r'Document ID:\s*WISEIN-[A-Z\-]+(\d{3})', text)
    ids += re.findall(r'WISEIN-[A-Z\-]+0*(\d{2,3})', text)
    m = re.search(r'(?<!\d)(\d{2,3})(?!\d)', p["name"])
    if m:
        ids.append(m.group(1))
    
    unique_ids = list(set([str(int(i)).zfill(2) for i in ids if 1 <= int(i) <= 80]))
    
    # Verify content in KB
    # For every paragraph in the PDF, check if it's broadly present in any KB file
    paragraphs = [pr.strip() for pr in text.split('\n\n') if len(pr.strip()) > 30]
    
    mapped_kb_files = []
    mapped_chunks = []
    
    # check chunks for mapping
    for ch in chunks_metadata:
        for uid in unique_ids:
            if ch.get("topic_number") == uid or str(uid) in ch.get("source_file", ""):
                mapped_chunks.append(ch.get("chunk_id"))
                if ch.get("source_file") not in mapped_kb_files:
                    mapped_kb_files.append(ch.get("source_file"))
                    
    missing_paragraphs = []
    text_lower = text.lower()
    kb_combined_text = "".join(kb_contents.values())
    
    for para in paragraphs:
        # Simplistic check: if a chunk of the paragraph (e.g. first 50 chars) isn't anywhere in KB
        para_clean = re.sub(r'\s+', ' ', para.lower())
        if len(para_clean) > 50:
            sample = para_clean[:50]
            if sample not in kb_combined_text:
                missing_paragraphs.append(para[:100] + "...")
                
    if missing_paragraphs:
        report["missing_content_suspects"].append({
            "source_file": p["name"],
            "missing_snippets_count": len(missing_paragraphs),
            "samples": missing_paragraphs[:3]
        })
        
    report["file_mapping"].append({
        "source_file": p["name"],
        "mapped_kb_topics": unique_ids,
        "mapped_kb_files": list(set(mapped_kb_files)),
        "mapped_chunks_count": len(set(mapped_chunks))
    })

# Output report
os.makedirs(r"c:\Users\marel\OneDrive\Desktop\wisein-ai-support\scripts\reports", exist_ok=True)
with open(r"c:\Users\marel\OneDrive\Desktop\wisein-ai-support\scripts\reports\wisein_source_coverage_audit.json", "w", encoding="utf-8") as f:
    json.dump(report, f, indent=2)

print("Audit script completed.")
