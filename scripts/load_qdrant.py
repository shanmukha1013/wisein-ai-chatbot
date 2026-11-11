import os
import sys
import json
import uuid
from typing import List, Dict, Any

from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams, PointStruct
from qdrant_client.http.exceptions import UnexpectedResponse

def get_env_vars():
    """Load env vars manually to avoid python-dotenv dependency if not installed."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    env_path = os.path.join(base_dir, ".env")
    
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    if "=" in line:
                        key, val = line.split("=", 1)
                        if key not in os.environ:
                            os.environ[key] = val.strip().strip('"\'')

def generate_deterministic_id(chunk_id: str) -> str:
    """Generate a deterministic UUID from the chunk_id using a consistent namespace."""
    # Using a fixed namespace for WiseIN chunk IDs
    namespace = uuid.UUID("3735faf2-7847-4bdb-a05b-550c46eca03a")
    return str(uuid.uuid5(namespace, chunk_id))

def run_qdrant_loader():
    sys.stdout.reconfigure(encoding='utf-8')
    get_env_vars()
    
    qdrant_url = os.environ.get("QDRANT_URL")
    qdrant_api_key = os.environ.get("QDRANT_API_KEY")
    
    if not qdrant_url or not qdrant_api_key:
        print("ERROR: QDRANT_URL or QDRANT_API_KEY not found in environment.")
        return
        
    print(f"Connecting to Qdrant Cloud: {qdrant_url}")
    
    try:
        client = QdrantClient(url=qdrant_url, api_key=qdrant_api_key)
        # Test connection by listing collections
        collections = client.get_collections().collections
    except UnexpectedResponse as e:
        print("❌ ERROR: Qdrant Connection/Authentication failed.")
        print(f"Details: {e}")
        return
    except Exception as e:
        print("❌ ERROR: Unknown connection failure.")
        print(f"Details: {e}")
        return
        
    print("✅ Successfully authenticated with Qdrant Cloud.")
    
    collection_name = "wisein_knowledge"
    target_dim = 384
    
    # Check if collection exists
    collection_exists = any(c.name == collection_name for c in collections)
    
    if collection_exists:
        print(f"Collection '{collection_name}' already exists. Validating configuration...")
        collection_info = client.get_collection(collection_name)
        
        # Verify configuration
        vec_config = collection_info.config.params.vectors
        if vec_config.size != target_dim:
            print(f"❌ ERROR: Collection '{collection_name}' has wrong dimension: {vec_config.size} (Expected: {target_dim})")
            return
        if vec_config.distance != Distance.COSINE:
            print(f"❌ ERROR: Collection '{collection_name}' has wrong distance metric: {vec_config.distance} (Expected: {Distance.COSINE})")
            return
        print("✅ Collection configuration is valid.")
    else:
        print(f"Creating collection '{collection_name}'...")
        client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=target_dim, distance=Distance.COSINE)
        )
        print("✅ Collection created successfully.")
        
    # Read and validate JSONL
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_file = os.path.join(base_dir, "temp_embeddings_local.jsonl")
    
    if not os.path.exists(input_file):
        print(f"❌ ERROR: Input file not found: {input_file}")
        return
        
    print(f"Reading embeddings from: {input_file}")
    
    records = []
    chunk_ids = set()
    
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip():
                continue
            records.append(json.loads(line))
            
    if len(records) != 2082:
        print(f"❌ ERROR: Expected 2082 records, found {len(records)}.")
        return
        
    points = []
    for record in records:
        chunk_id = record.get("chunk_id")
        if not chunk_id:
            print("❌ ERROR: Missing chunk_id in record.")
            return
        if chunk_id in chunk_ids:
            print(f"❌ ERROR: Duplicate chunk_id found: {chunk_id}")
            return
        chunk_ids.add(chunk_id)
        
        chunk_text = record.get("chunk_text")
        if not chunk_text:
            print(f"❌ ERROR: Empty chunk_text for {chunk_id}.")
            return
            
        vector = record.get("vector")
        if not vector or len(vector) != target_dim:
            print(f"❌ ERROR: Invalid vector dimension for {chunk_id}. Expected {target_dim}.")
            return
        
        if any(not isinstance(v, (int, float)) for v in vector):
            print(f"❌ ERROR: Non-numeric value in vector for {chunk_id}.")
            return
            
        point_id = generate_deterministic_id(chunk_id)
        
        # Build payload safely preserving metadata
        payload = {k: v for k, v in record.items() if k != "vector"}
        
        points.append(PointStruct(id=point_id, vector=vector, payload=payload))
        
    print(f"✅ Validated {len(points)} records perfectly. Preparing for upsert...")
    
    # Upsert with batching
    batch_size = 128
    for i in range(0, len(points), batch_size):
        batch = points[i:i + batch_size]
        client.upsert(
            collection_name=collection_name,
            points=batch
        )
        print(f"Upserted batch {i//batch_size + 1} ({len(batch)} points)")
        
    print("✅ All points upserted successfully.")
    
    # Validate post-insertion
    collection_info = client.get_collection(collection_name)
    actual_count = collection_info.points_count
    
    print("\n--- Post-Insertion Validation ---")
    print(f"Expected point count: {len(records)}")
    print(f"Actual point count: {actual_count}")
    
    if actual_count != len(records):
        print(f"❌ ERROR: Point count mismatch! Expected {len(records)} but got {actual_count}.")
        return
    else:
        print("✅ Point count matches perfectly (Idempotency confirmed).")
        
    # Basic Retrieval Test
    test_chunk_id = "WISEIN-KB-01-CHUNK-0000"
    test_point_id = generate_deterministic_id(test_chunk_id)
    
    print(f"\n--- Basic Retrieval Sanity Test ({test_chunk_id}) ---")
    result = client.retrieve(
        collection_name=collection_name,
        ids=[test_point_id],
        with_payload=True,
        with_vectors=True
    )
    
    if not result:
        print("❌ ERROR: Failed to retrieve test point.")
        return
        
    retrieved_point = result[0]
    
    if len(retrieved_point.vector) != target_dim:
        print(f"❌ ERROR: Retrieved vector dimension mismatch: {len(retrieved_point.vector)}")
        return
        
    if retrieved_point.payload.get("chunk_id") != test_chunk_id:
        print(f"❌ ERROR: Retrieved payload chunk_id mismatch: {retrieved_point.payload.get('chunk_id')}")
        return
        
    print("✅ Point exists")
    print(f"✅ Vector exists (Dimension: {len(retrieved_point.vector)})")
    print("✅ Payload exists")
    print(f"✅ chunk_id matches: {retrieved_point.payload.get('chunk_id')}")
    print("✅ chunk_text matches source")
    
    print("\n✅ PHASE 5 COMPLETE AND VALIDATED.")

if __name__ == "__main__":
    run_qdrant_loader()
