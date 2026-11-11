import os
import sys
from typing import List, Dict, Any, Optional

from qdrant_client import QdrantClient
from qdrant_client.http.exceptions import UnexpectedResponse

# Ensure we can import existing code
sys.path.append(os.path.dirname(__file__))
from generate_embeddings import LocalSentenceTransformerEmbeddingProvider
from load_qdrant import get_env_vars

class RetrievalEngine:
    def __init__(self, collection_name: str = "wisein_knowledge", top_k: int = 5):
        self.collection_name = collection_name
        self.default_top_k = top_k
        self.client = None
        self.provider = None
        self._initialize()

    def _initialize(self):
        print("Initializing Retrieval Engine...")
        get_env_vars()
        
        qdrant_url = os.environ.get("QDRANT_URL")
        qdrant_api_key = os.environ.get("QDRANT_API_KEY")
        
        if not qdrant_url or not qdrant_api_key:
            raise ValueError("QDRANT_URL or QDRANT_API_KEY not found in environment.")
            
        print(f"Connecting to Qdrant Cloud: {qdrant_url}")
        self.client = QdrantClient(url=qdrant_url, api_key=qdrant_api_key)
        
        # Verify collection exists
        try:
            collections = self.client.get_collections().collections
            if not any(c.name == self.collection_name for c in collections):
                raise ValueError(f"Collection '{self.collection_name}' does not exist in Qdrant.")
        except Exception as e:
            raise RuntimeError(f"Failed to connect to Qdrant or verify collection: {e}")
            
        # Initialize embedding provider once (reusable)
        print("Loading local embedding model...")
        self.provider = LocalSentenceTransformerEmbeddingProvider()
        print("Retrieval Engine successfully initialized.")

    def retrieve(self, query: str, top_k: Optional[int] = None) -> List[Dict[str, Any]]:
        if not query or not isinstance(query, str) or not query.strip():
            print("Validation Error: Query must be a non-empty string.")
            return []
            
        k = top_k if top_k is not None else self.default_top_k
        if not isinstance(k, int) or k <= 0:
            print(f"Validation Error: top_k must be a positive integer, got {k}.")
            return []
            
        query = query.strip()
        
        try:
            # Generate query embedding
            vectors = self.provider.embed_texts([query])
            query_vector = vectors[0]
            
            if len(query_vector) != 384:
                print(f"Error: Query vector dimension mismatch. Expected 384, got {len(query_vector)}.")
                return []
                
            # Perform search
            response = self.client.query_points(
                collection_name=self.collection_name,
                query=query_vector,
                limit=k,
                with_payload=True
            )
            search_result = response.points
            
            results = []
            for i, scored_point in enumerate(search_result):
                payload = scored_point.payload or {}
                result = {
                    "rank": i + 1,
                    "score": scored_point.score,
                    "chunk_id": payload.get("chunk_id", ""),
                    "document_id": payload.get("document_id", ""),
                    "topic_number": payload.get("topic_number", ""),
                    "topic_name": payload.get("topic_name", ""),
                    "source_file": payload.get("source_file", ""),
                    "section": payload.get("section", ""),
                    "chunk_index": payload.get("chunk_index", 0),
                    "chunk_text": payload.get("chunk_text", "")
                }
                # Preserve additional metadata safely
                for key, val in payload.items():
                    if key not in result:
                        result[key] = val
                        
                results.append(result)
                
            return results
            
        except Exception as e:
            print(f"Error during retrieval: {e}")
            return []

def run_retrieval_tests():
    sys.stdout.reconfigure(encoding='utf-8')
    print("==================================================")
    print("WISEIN RETRIEVAL TEST")
    print("==================================================\n")
    
    try:
        engine = RetrievalEngine()
    except Exception as e:
        print(f"Failed to initialize engine: {e}")
        return

    test_queries = [
        "How do I log in to WiseIN?",
        "How can I verify my identity on WiseIN?",
        "How do I update my profile information?",
        "How can I find jobs on WiseIN?",
        "How do I connect with other people on WiseIN?",
        "How do I book a meeting?",
        "Why am I receiving notifications from WiseIN?",
        "How can I delete my WiseIN account?"
    ]
    
    for query in test_queries:
        print("==================================================")
        print(f"Query:\n{query}\n")
        print("Query vector:\n384 dimensions\n")
        print("Results:\n")
        
        results = engine.retrieve(query, top_k=5)
        
        if not results:
            print("No results returned.\n")
            continue
            
        for res in results:
            print(f"{res['rank']}. Score: {res['score']:.4f}")
            print(f"   Topic: {res['topic_name']}")
            print(f"   Chunk ID: {res['chunk_id']}")
            print(f"   Section: {res['section']}")
            
            # Print a snippet of the text to keep output readable but verify content
            text_snippet = res['chunk_text']
            print("   Text:")
            print(f"   {text_snippet}\n")

    print("==================================================")

if __name__ == "__main__":
    run_retrieval_tests()
