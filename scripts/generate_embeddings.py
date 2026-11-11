import os
import json
import time
import urllib.request
import urllib.error
import random
from abc import ABC, abstractmethod
from typing import List, Dict, Any

# Ensure we can import from the same directory
import sys
sys.path.append(os.path.dirname(__file__))
from chunk_documents import run_chunking_pipeline, DocumentChunk

class EmbeddingProvider(ABC):
    @abstractmethod
    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        pass
    
    @abstractmethod
    def get_dimension(self) -> int:
        pass
    
    @abstractmethod
    def get_model_name(self) -> str:
        pass

class MockEmbeddingProvider(EmbeddingProvider):
    """Fallback provider when no API key is available. Generates synthetic vectors for validation."""
    def __init__(self, dimension: int = 1536):
        self.dimension = dimension
        
    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        # Simulate network latency
        time.sleep(0.1)
        return [[random.uniform(-1.0, 1.0) for _ in range(self.dimension)] for _ in texts]

    def get_dimension(self) -> int:
        return self.dimension
        
    def get_model_name(self) -> str:
        return "mock-embedding-model-1536 (local-validation)"

class OpenAIEmbeddingProvider(EmbeddingProvider):
    """OpenAI Embedding API client using standard urllib (no external dependencies required)."""
    def __init__(self, api_key: str, model: str = "text-embedding-3-small"):
        self.api_key = api_key
        self.model = model
        self.dimension = 1536
        
    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        url = "https://api.openai.com/v1/embeddings"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        data = {
            "input": texts,
            "model": self.model
        }
        
        req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers, method='POST')
        
        try:
            with urllib.request.urlopen(req) as response:
                result = json.loads(response.read().decode('utf-8'))
                # Extract embeddings maintaining the original order
                sorted_data = sorted(result['data'], key=lambda x: x['index'])
                return [item['embedding'] for item in sorted_data]
        except urllib.error.URLError as e:
            if hasattr(e, 'read'):
                print(f"API Error details: {e.read().decode('utf-8')}")
            raise e
            
    def get_dimension(self) -> int:
        return self.dimension
        
    def get_model_name(self) -> str:
        return self.model

class LocalSentenceTransformerEmbeddingProvider(EmbeddingProvider):
    """Local provider using sentence-transformers."""
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        from sentence_transformers import SentenceTransformer
        self.model_name = model_name
        print(f"Loading local model: {self.model_name}...")
        self.model = SentenceTransformer(self.model_name)
        # Verify dimension
        self.dimension = self.model.get_sentence_embedding_dimension()
        
    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        # sentence-transformers outputs numpy arrays
        embeddings = self.model.encode(texts, show_progress_bar=False)
        return embeddings.tolist()

    def get_dimension(self) -> int:
        return self.dimension
        
    def get_model_name(self) -> str:
        return self.model_name


def get_api_key(base_dir: str) -> str:
    """Attempts to retrieve the API key from environment variables or .env file securely."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if api_key:
        return api_key
        
    env_path = os.path.join(base_dir, ".env")
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip() and not line.startswith("#") and "OPENAI_API_KEY" in line:
                    parts = line.strip().split("=", 1)
                    if len(parts) == 2:
                        return parts[1].strip().strip('"\'')
    return ""

def create_env_example(base_dir: str):
    env_example_path = os.path.join(base_dir, ".env.example")
    if not os.path.exists(env_example_path):
        with open(env_example_path, "w", encoding="utf-8") as f:
            f.write("# Environment Variables for WiseIN AI Chatbot\n")
            f.write("OPENAI_API_KEY=your-api-key-here\n")

def generate_embeddings(chunks: List[DocumentChunk], provider: EmbeddingProvider, output_file: str, batch_size: int = 100) -> int:
    """
    Generates embeddings in batches and saves them to a temporary JSONL format,
    preserving all chunk metadata alongside the generated vector.
    """
    failed_embeddings = 0
    
    with open(output_file, 'w', encoding='utf-8') as f_out:
        for i in range(0, len(chunks), batch_size):
            batch = chunks[i:i + batch_size]
            texts = [chunk.chunk_text for chunk in batch]
            
            try:
                vectors = provider.embed_texts(texts)
                
                # Write each vector and metadata immediately to avoid massive memory buildup
                for chunk, vector in zip(batch, vectors):
                    record = {
                        "chunk_id": chunk.chunk_id,
                        "document_id": chunk.document_id,
                        "topic_number": chunk.topic_number,
                        "topic_name": chunk.topic_name,
                        "source_file": chunk.source_file,
                        "section": chunk.section,
                        "chunk_index": chunk.chunk_index,
                        "chunk_text": chunk.chunk_text,
                        "character_count": chunk.character_count,
                        "embedding_model": provider.get_model_name(),
                        "vector": vector
                    }
                    f_out.write(json.dumps(record) + '\n')
            except Exception as e:
                print(f"Error processing batch {i} to {i+batch_size}: {e}")
                failed_embeddings += len(batch)
                
    return failed_embeddings

def validate_embeddings(output_file: str, expected_count: int, expected_dim: int):
    print("\n--- Embeddings Validation ---")
    if not os.path.exists(output_file):
        print("❌ Validation Failed: Output file does not exist.")
        return
        
    processed_count = 0
    invalid_vectors = 0
    chunk_ids = set()
    duplicate_ids = 0
    model_name = "Unknown"
    
    sample_record = None

    with open(output_file, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip():
                continue
            record = json.loads(line)
            processed_count += 1
            
            if processed_count == 1:
                sample_record = record
                model_name = record.get("embedding_model", "Unknown")
            
            c_id = record.get("chunk_id")
            if c_id in chunk_ids:
                duplicate_ids += 1
            chunk_ids.add(c_id)
            
            vec = record.get("vector", [])
            if len(vec) != expected_dim or any(not isinstance(v, (int, float)) for v in vec):
                invalid_vectors += 1

    print(f"Model/Provider used: {model_name}")
    print(f"Expected chunks: {expected_count}")
    print(f"Embeddings generated: {processed_count}")
    print(f"Duplicate chunk IDs: {duplicate_ids}")
    print(f"Missing chunk IDs: {expected_count - len(chunk_ids)}")
    print(f"Vectors with invalid dimensions/values (expected {expected_dim}): {invalid_vectors}")
    
    if processed_count == expected_count and invalid_vectors == 0 and duplicate_ids == 0:
        print("✅ Validation Passed: 1-to-1 mapping between chunks and valid vectors achieved.")
    else:
        print("❌ Validation Failed: Discrepancies found.")

    if sample_record:
        print("\n--- Sample Embedding Record Metadata ---")
        print(f"Chunk ID: {sample_record['chunk_id']}")
        print(f"Document ID: {sample_record['document_id']}")
        print(f"Topic: {sample_record['topic_number']} - {sample_record['topic_name']}")
        print(f"Vector Dimension: {len(sample_record['vector'])}")
        print(f"Sample Vector Values (first 3): {sample_record['vector'][:3]}")

if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    kb_path = os.path.join(base_dir, "knowledge_base")
    # Configuration to explicitly use local provider
    output_file = os.path.join(base_dir, "temp_embeddings_local.jsonl")
    
    print("Using LocalSentenceTransformerEmbeddingProvider (sentence-transformers/all-MiniLM-L6-v2)...")
    provider = LocalSentenceTransformerEmbeddingProvider()

    # 2. Get Chunks
    print("Loading chunks from pipeline...")
    chunks = run_chunking_pipeline(kb_path)
    total_chunks = len(chunks)
    print(f"Successfully loaded {total_chunks} chunks.")
    
    # 3. Generate Embeddings
    print(f"Generating embeddings and saving to {output_file}...")
    start_time = time.time()
    failed = generate_embeddings(chunks, provider, output_file)
    end_time = time.time()
    
    print(f"Embedding generation completed in {end_time - start_time:.2f} seconds.")
    if failed > 0:
        print(f"⚠️ Failed embeddings: {failed}")
        
    # 4. Validate
    validate_embeddings(output_file, expected_count=total_chunks, expected_dim=provider.get_dimension())
