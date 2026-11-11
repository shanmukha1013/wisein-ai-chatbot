import os
import re
from dataclasses import dataclass
from typing import List, Optional
from load_documents import load_knowledge_base, KnowledgeDocument

@dataclass
class DocumentChunk:
    chunk_id: str
    document_id: str
    topic_number: str
    topic_name: str
    source_file: str
    section: str
    chunk_index: int
    chunk_text: str
    character_count: int

# Chunking Strategy Parameters
# Rationale: For customer support RAG, a context window usually takes a few paragraphs.
# 1500-2000 chars is roughly 300-400 words, which is ideal for a focused answer without diluting context.
# 100 chars is the minimum to avoid useless chunks (like just a header or a single word).
MAX_CHUNK_CHARS = 1500
MIN_CHUNK_CHARS = 100
OVERLAP_CHARS = 150  # Overlap between chunks within the same section to preserve context

def split_text_with_overlap(text: str, max_chars: int, overlap: int) -> List[str]:
    """Splits a long text into chunks, respecting paragraph boundaries where possible."""
    paragraphs = re.split(r'\n\s*\n', text)
    chunks = []
    current_chunk = ""
    
    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
            
        if len(current_chunk) + len(p) + 2 <= max_chars:
            current_chunk += ("\n\n" + p) if current_chunk else p
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
                # Start new chunk with overlap if possible (take last sentence or paragraph part)
                # For simplicity, we just keep the last part of the previous chunk up to 'overlap' chars
                overlap_text = current_chunk[-overlap:] if overlap > 0 and len(current_chunk) > overlap else ""
                # try to find a nice boundary for the overlap (e.g. start of a sentence)
                boundary = overlap_text.find('. ')
                if boundary != -1:
                    overlap_text = overlap_text[boundary+2:]
                
                current_chunk = (overlap_text + "\n\n" + p).strip() if overlap_text else p
            else:
                # The paragraph itself is larger than max_chars (rare but possible)
                # Split by newline or just hard slice
                lines = p.split('\n')
                for line in lines:
                    if len(current_chunk) + len(line) + 1 <= max_chars:
                        current_chunk += ("\n" + line) if current_chunk else line
                    else:
                        if current_chunk:
                            chunks.append(current_chunk.strip())
                        
                        # If a single line is still too long, hard slice it
                        if len(line) > max_chars:
                            start = 0
                            while start < len(line):
                                chunks.append(line[start:start+max_chars].strip())
                                start += max_chars - overlap
                            current_chunk = ""
                        else:
                            current_chunk = line
                            
    if current_chunk:
        chunks.append(current_chunk.strip())
        
    return chunks

def extract_sections(markdown_text: str) -> List[dict]:
    """
    Parses Markdown into sections based on headings (## or #).
    Returns a list of dicts: {"heading": str, "content": str}
    """
    # Split by any ATX heading (## Heading)
    # We will use regex to find headings and split
    # Pattern explanation: matches ^#+ Heading Text on a new line
    lines = markdown_text.split('\n')
    sections = []
    current_heading = "Overview" # Default for text before any heading
    current_content = []
    
    for line in lines:
        match = re.match(r'^(#{1,6})\s+(.*)', line)
        if match:
            # Save previous section if it has content
            if current_content:
                sections.append({
                    "heading": current_heading,
                    "content": '\n'.join(current_content).strip()
                })
            current_heading = match.group(2).strip()
            current_content = []
        else:
            current_content.append(line)
            
    # Add last section
    if current_content:
        sections.append({
            "heading": current_heading,
            "content": '\n'.join(current_content).strip()
        })
        
    return sections

def chunk_document(doc: KnowledgeDocument) -> List[DocumentChunk]:
    sections = extract_sections(doc.content)
    document_chunks = []
    chunk_index = 0
    
    for sec in sections:
        heading = sec["heading"]
        content = sec["content"]
        
        if not content:
            continue
            
        # If the entire section is reasonably sized, keep it as one chunk
        if len(content) <= MAX_CHUNK_CHARS:
            raw_chunks = [content]
        else:
            # Need to split this section
            raw_chunks = split_text_with_overlap(content, MAX_CHUNK_CHARS, OVERLAP_CHARS)
            
        for rc in raw_chunks:
            rc = rc.strip()
            if len(rc) < MIN_CHUNK_CHARS:
                # Too small! Let's try to append it to the last chunk if it belongs to the same doc
                # Or if it's the only text in this section, we might keep it if it's highly relevant.
                # For now, if there's a previous chunk, merge it if possible, else just keep it.
                if len(document_chunks) > 0 and len(document_chunks[-1].chunk_text) + len(rc) < MAX_CHUNK_CHARS:
                    # Merge with previous chunk to avoid micro-chunks
                    document_chunks[-1].chunk_text += f"\n\n[{heading}]\n{rc}"
                    document_chunks[-1].character_count = len(document_chunks[-1].chunk_text)
                    continue
                else:
                    # Just keep it, maybe it's an important short note.
                    pass
            
            # Prepend heading to the chunk text so the LLM knows the context even in isolation
            chunk_text_with_context = f"Section: {heading}\n\n{rc}"
            
            chunk_id = f"{doc.document_id}-CHUNK-{chunk_index:04d}"
            document_chunks.append(DocumentChunk(
                chunk_id=chunk_id,
                document_id=doc.document_id,
                topic_number=doc.topic_number,
                topic_name=doc.topic_name,
                source_file=doc.filename,
                section=heading,
                chunk_index=chunk_index,
                chunk_text=chunk_text_with_context,
                character_count=len(chunk_text_with_context)
            ))
            chunk_index += 1
            
    return document_chunks

def run_chunking_pipeline(kb_dir: str) -> List[DocumentChunk]:
    docs = load_knowledge_base(kb_dir)
    all_chunks = []
    for doc in docs:
        all_chunks.extend(chunk_document(doc))
    return all_chunks

if __name__ == "__main__":
    import statistics
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    kb_path = os.path.join(base_dir, "knowledge_base")
    
    print(f"Starting chunking validation from: {kb_path}")
    docs = load_knowledge_base(kb_path)
    
    all_chunks = []
    zero_chunk_docs = []
    
    for doc in docs:
        chunks = chunk_document(doc)
        if not chunks:
            zero_chunk_docs.append(doc.filename)
        all_chunks.extend(chunks)
        
    print("\n--- Validation Results ---")
    print(f"Total documents processed: {len(docs)}")
    print(f"Total chunks created: {len(all_chunks)}")
    
    if len(docs) > 0:
        print(f"Average chunks per document: {len(all_chunks) / len(docs):.1f}")
        
    if all_chunks:
        sizes = [c.character_count for c in all_chunks]
        print(f"Minimum chunk size: {min(sizes)} chars")
        print(f"Maximum chunk size: {max(sizes)} chars")
        print(f"Average chunk size: {statistics.mean(sizes):.1f} chars")
        
        small_chunks = [c for c in all_chunks if c.character_count < MIN_CHUNK_CHARS]
        large_chunks = [c for c in all_chunks if c.character_count > MAX_CHUNK_CHARS + 200]
        
        print(f"Suspiciously small chunks (<{MIN_CHUNK_CHARS} chars): {len(small_chunks)}")
        print(f"Suspiciously large chunks (>{MAX_CHUNK_CHARS + 200} chars): {len(large_chunks)}")
    
    print(f"Documents producing zero chunks: {len(zero_chunk_docs)}")
    if zero_chunk_docs:
        print(f" -> {zero_chunk_docs}")
        
    print("\n--- Sample Chunks ---")
    # Show 3 sample chunks from different topics
    import random
    random.seed(42) # fixed seed for reproducibility in output
    if all_chunks:
        # Group by topic
        topics = list(set([c.topic_number for c in all_chunks]))
        sample_topics = random.sample(topics, min(3, len(topics)))
        
        for t in sample_topics:
            topic_chunks = [c for c in all_chunks if c.topic_number == t]
            sample = random.choice(topic_chunks)
            print(f"\n[Sample from Topic {t} - {sample.topic_name}]")
            print(f"Chunk ID: {sample.chunk_id}")
            print(f"Section: {sample.section}")
            print(f"Length: {sample.character_count} chars")
            print(f"--- TEXT START ---")
            print(sample.chunk_text[:300] + ("..." if len(sample.chunk_text) > 300 else ""))
            print(f"--- TEXT END ---")

    print("\nValidation Complete. Ready for Embeddings phase.")
