import os
import json
import glob
from dataclasses import dataclass
from typing import List

@dataclass
class KnowledgeDocument:
    document_id: str
    topic_number: str
    topic_name: str
    filename: str
    source_path: str
    content: str

def load_knowledge_base(kb_dir: str) -> List[KnowledgeDocument]:
    """
    Loads exactly 80 numbered Markdown knowledge-base documents from the given directory.
    Validates that all documents are present and non-empty.
    Returns a list of structured KnowledgeDocument objects.
    """
    manifest_path = os.path.join(kb_dir, 'manifest.json')
    if not os.path.exists(manifest_path):
        raise FileNotFoundError(f"Manifest file missing at {manifest_path}")

    # Load manifest for metadata mapping
    with open(manifest_path, 'r', encoding='utf-8') as f:
        manifest_data = json.load(f)
        
    manifest_map = {item['topic_number']: item for item in manifest_data}

    documents = []

    for i in range(1, 81):
        topic_num_str = f"{i:02d}"
        
        # Search for the corresponding markdown file (e.g., 01_*.md)
        pattern = os.path.join(kb_dir, f"{topic_num_str}_*.md")
        matching_files = glob.glob(pattern)
        
        if len(matching_files) == 0:
            raise FileNotFoundError(f"Validation Error: Missing document for topic {topic_num_str}")
        if len(matching_files) > 1:
            raise ValueError(f"Validation Error: Multiple files found for topic {topic_num_str}: {matching_files}")
            
        file_path = matching_files[0]
        filename = os.path.basename(file_path)
        
        # Read content handling UTF-8 correctly
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if len(content.strip()) == 0:
            raise ValueError(f"Validation Error: Document is empty - {filename}")
            
        # Get metadata from manifest
        meta = manifest_map.get(topic_num_str)
        if not meta:
            # Fallback if manifest is incomplete (it shouldn't be based on prior steps)
            doc_id = f"WISEIN-KB-{topic_num_str}"
            topic_name = filename[3:-3].replace('_', ' ').title()
        else:
            doc_id = meta['document_id']
            topic_name = meta['topic_name']

        # Create structured document
        doc = KnowledgeDocument(
            document_id=doc_id,
            topic_number=topic_num_str,
            topic_name=topic_name,
            filename=filename,
            source_path=file_path,
            content=content
        )
        documents.append(doc)

    return documents


if __name__ == "__main__":
    # Test and Validation capability
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    kb_path = os.path.join(base_dir, "knowledge_base")
    
    print(f"Starting document loading and validation from: {kb_path}")
    
    try:
        docs = load_knowledge_base(kb_path)
        
        print("\n--- Validation Results ---")
        print(f"1. Exactly 80 documents loaded: {'PASS' if len(docs) == 80 else 'FAIL'} ({len(docs)} loaded)")
        
        # Validation checks (they would have raised an error in the function, but good to explicitly state)
        print("2. No numbered document is missing: PASS (Validated in loader)")
        print("3. No numbered document is empty: PASS (Validated in loader)")
        
        # Filename mappings
        correct_mappings = all(d.filename.startswith(d.topic_number) for d in docs)
        print(f"4. Filenames correctly mapped: {'PASS' if correct_mappings else 'FAIL'}")
        
        # Total character count
        total_chars = sum(len(d.content) for d in docs)
        print(f"5. Total character count across all documents: {total_chars:,} characters")
        
        print("\nAll validations passed successfully!")
        
        # Show a sample of the first document to verify structure
        if docs:
            print(f"\nSample metadata for first document ({docs[0].filename}):")
            print(f"  - Document ID: {docs[0].document_id}")
            print(f"  - Topic Number: {docs[0].topic_number}")
            print(f"  - Topic Name: {docs[0].topic_name}")
            print(f"  - Content Length: {len(docs[0].content)} chars")
            
    except Exception as e:
        print(f"\n❌ Validation FAILED: {str(e)}")

