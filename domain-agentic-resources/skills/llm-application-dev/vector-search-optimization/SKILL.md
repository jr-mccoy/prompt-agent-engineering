---
name: vector-search-optimization
description: Implement and optimize vector database search for production systems. Covers vector DB implementations (Pinecone, Qdrant, pgvector, Weaviate, Elasticsearch), HNSW index tuning, quantization strategies, hybrid search with keyword fusion, and performance benchmarking. Use when building semantic search, tuning vector indexes, implementing hybrid search, or scaling to millions of vectors. Triggers on "vector database", "HNSW tuning", "quantization", "hybrid search", "RRF", "similarity search", "pgvector", "Pinecone", "Qdrant".
metadata:
  tags:
    - ai-applications
    - hybrid-search
    - index
    - llm
    - optimization
    - performance
    - search
    - similarity
    - vector
    - vector-db
    - vector-search
  updated: "2026-04-11"
---
# Vector Search Optimization

Production patterns for vector database implementation, index tuning, hybrid search, and performance optimization.

## Purpose

This skill covers everything below the RAG retrieval layer: choosing and configuring vector databases, tuning index parameters for recall/latency/memory trade-offs, combining vector search with keyword search (hybrid), and benchmarking performance. Use `rag-architecture` for the RAG pipeline above this layer.

## When to Use This Skill

- Choosing and configuring a vector database
- Implementing semantic search or nearest neighbor queries
- Tuning HNSW parameters for recall vs latency
- Implementing quantization to reduce memory
- Combining vector and keyword search (hybrid/fusion)
- Scaling vector search to millions of vectors
- Benchmarking search performance (latency, recall, QPS)
- Building recommendation engines

## When NOT to Use This Skill

- Designing end-to-end RAG pipelines (use `rag-architecture`)
- Choosing embedding models (use `embedding-strategies`)
- Optimizing LangChain chains (use `langchain-optimization`)
- Writing E2E tests for search (use `e2e-testing-patterns`)

---

## Core Concepts

### Distance Metrics

| Metric | Formula | Best For |
|--------|---------|----------|
| **Cosine** | 1 - (A.B)/(||A||||B||) | Normalized embeddings |
| **Euclidean (L2)** | sqrt(sum((a-b)^2)) | Raw embeddings |
| **Dot Product** | A.B | Magnitude matters |
| **Manhattan (L1)** | sum(|a-b|) | Sparse vectors |

### Index Type Selection

```
Data Size           Recommended Index
────────────────────────────────────────
< 10K vectors  →    Flat (exact search)
10K - 1M       →    HNSW
1M - 100M      →    HNSW + Quantization
> 100M         →    IVF + PQ or DiskANN
```

### HNSW Parameters

| Parameter | Default | Effect |
|-----------|---------|--------|
| **M** | 16 | Connections per node. Higher = better recall, more memory |
| **efConstruction** | 100 | Build quality. Higher = better index, slower build |
| **efSearch** | 50 | Search quality. Higher = better recall, slower search |

### Quantization Types

```
Full Precision (FP32): 4 bytes x dimensions
Half Precision (FP16): 2 bytes x dimensions
INT8 Scalar:           1 byte x dimensions
Product Quantization:  ~32-64 bytes total
Binary:                dimensions/8 bytes
```

---

## Vector Database Implementations

### Pinecone

```python
from pinecone import Pinecone, ServerlessSpec
from typing import List, Dict, Optional

class PineconeVectorStore:
    def __init__(self, api_key: str, index_name: str, dimension: int = 1536, metric: str = "cosine"):
        self.pc = Pinecone(api_key=api_key)
        if index_name not in self.pc.list_indexes().names():
            self.pc.create_index(
                name=index_name, dimension=dimension, metric=metric,
                spec=ServerlessSpec(cloud="aws", region="us-east-1")
            )
        self.index = self.pc.Index(index_name)

    def upsert(self, vectors: List[Dict], namespace: str = "") -> int:
        batch_size = 100
        total = 0
        for i in range(0, len(vectors), batch_size):
            batch = vectors[i:i + batch_size]
            self.index.upsert(vectors=batch, namespace=namespace)
            total += len(batch)
        return total

    def search(self, query_vector: List[float], top_k: int = 10,
               namespace: str = "", filter: Optional[Dict] = None) -> List[Dict]:
        results = self.index.query(
            vector=query_vector, top_k=top_k, namespace=namespace,
            filter=filter, include_metadata=True
        )
        return [{"id": m.id, "score": m.score, "metadata": m.metadata} for m in results.matches]
```

### Qdrant

```python
from qdrant_client import QdrantClient
from qdrant_client.http import models

class QdrantVectorStore:
    def __init__(self, url: str = "localhost", port: int = 6333,
                 collection_name: str = "documents", vector_size: int = 1536):
        self.client = QdrantClient(url=url, port=port)
        self.collection_name = collection_name
        collections = self.client.get_collections().collections
        if collection_name not in [c.name for c in collections]:
            self.client.create_collection(
                collection_name=collection_name,
                vectors_config=models.VectorParams(size=vector_size, distance=models.Distance.COSINE),
                quantization_config=models.ScalarQuantization(
                    scalar=models.ScalarQuantizationConfig(
                        type=models.ScalarType.INT8, quantile=0.99, always_ram=True
                    )
                )
            )

    def search(self, query_vector: List[float], limit: int = 10,
               filter: Optional[models.Filter] = None) -> List[Dict]:
        results = self.client.search(
            collection_name=self.collection_name, query_vector=query_vector,
            limit=limit, query_filter=filter
        )
        return [{"id": r.id, "score": r.score, "payload": r.payload} for r in results]
```

### pgvector (PostgreSQL)

```python
import asyncpg
from typing import List, Dict, Optional
import numpy as np

class PgVectorStore:
    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    async def init(self):
        self.pool = await asyncpg.create_pool(self.connection_string)
        async with self.pool.acquire() as conn:
            await conn.execute("CREATE EXTENSION IF NOT EXISTS vector")
            await conn.execute("""
                CREATE TABLE IF NOT EXISTS documents (
                    id TEXT PRIMARY KEY, content TEXT,
                    metadata JSONB, embedding vector(1536)
                )
            """)
            await conn.execute("""
                CREATE INDEX IF NOT EXISTS documents_embedding_idx
                ON documents USING hnsw (embedding vector_cosine_ops)
                WITH (m = 16, ef_construction = 64)
            """)

    async def search(self, query_embedding: List[float], limit: int = 10,
                     filter_metadata: Optional[Dict] = None) -> List[Dict]:
        query = """
            SELECT id, content, metadata,
                   1 - (embedding <=> $1::vector) as similarity
            FROM documents
        """
        params = [query_embedding]
        if filter_metadata:
            conditions = []
            for key, value in filter_metadata.items():
                params.append(value)
                conditions.append(f"metadata->>'{key}' = ${len(params)}")
            query += " WHERE " + " AND ".join(conditions)
        query += f" ORDER BY embedding <=> $1::vector LIMIT ${len(params) + 1}"
        params.append(limit)

        async with self.pool.acquire() as conn:
            rows = await conn.fetch(query, *params)
        return [{"id": row["id"], "content": row["content"],
                 "metadata": row["metadata"], "score": row["similarity"]} for row in rows]
```

---

## HNSW Index Tuning

### Parameter Benchmarking

```python
import numpy as np
import time

def benchmark_hnsw_parameters(vectors, queries, ground_truth,
    m_values=[8, 16, 32, 64], ef_construction_values=[64, 128, 256],
    ef_search_values=[32, 64, 128, 256]) -> list:
    """Benchmark different HNSW configurations."""
    import hnswlib
    results = []
    dim = vectors.shape[1]
    n = vectors.shape[0]

    for m in m_values:
        for ef_construction in ef_construction_values:
            index = hnswlib.Index(space='cosine', dim=dim)
            index.init_index(max_elements=n, M=m, ef_construction=ef_construction)
            build_start = time.time()
            index.add_items(vectors)
            build_time = time.time() - build_start

            for ef_search in ef_search_values:
                index.set_ef(ef_search)
                search_start = time.time()
                labels, distances = index.knn_query(queries, k=10)
                search_time = time.time() - search_start
                recall = calculate_recall(labels, ground_truth, k=10)

                results.append({
                    "M": m, "ef_construction": ef_construction,
                    "ef_search": ef_search, "build_time_s": build_time,
                    "search_time_ms": search_time * 1000 / len(queries),
                    "recall@10": recall
                })
    return results

def recommend_hnsw_params(num_vectors: int, target_recall: float = 0.95) -> dict:
    """Recommend HNSW parameters based on requirements."""
    if num_vectors < 100_000:
        m, ef_construction = 16, 100
    elif num_vectors < 1_000_000:
        m, ef_construction = 32, 200
    else:
        m, ef_construction = 48, 256

    ef_search = 256 if target_recall >= 0.99 else 128 if target_recall >= 0.95 else 64

    return {"M": m, "ef_construction": ef_construction, "ef_search": ef_search}
```

### Quantization Strategies

```python
import numpy as np
from typing import Tuple

class VectorQuantizer:
    @staticmethod
    def scalar_quantize_int8(vectors: np.ndarray) -> Tuple[np.ndarray, dict]:
        """Scalar quantization to INT8 (1 byte per dimension)."""
        min_val, max_val = vectors.min(), vectors.max()
        scale = 255.0 / (max_val - min_val)
        quantized = np.clip(np.round((vectors - min_val) * scale), 0, 255).astype(np.uint8)
        return quantized, {"min_val": min_val, "max_val": max_val, "scale": scale}

    @staticmethod
    def product_quantize(vectors: np.ndarray, n_subvectors: int = 8, n_centroids: int = 256):
        """Product quantization for aggressive compression."""
        from sklearn.cluster import KMeans
        n, dim = vectors.shape
        subvector_dim = dim // n_subvectors
        codebooks, codes = [], np.zeros((n, n_subvectors), dtype=np.uint8)

        for i in range(n_subvectors):
            subvectors = vectors[:, i * subvector_dim:(i + 1) * subvector_dim]
            kmeans = KMeans(n_clusters=n_centroids, random_state=42)
            codes[:, i] = kmeans.fit_predict(subvectors)
            codebooks.append(kmeans.cluster_centers_)
        return codes, {"codebooks": codebooks}

    @staticmethod
    def binary_quantize(vectors: np.ndarray) -> np.ndarray:
        """Binary quantization (sign of each dimension)."""
        binary = (vectors > 0).astype(np.uint8)
        n, dim = vectors.shape
        packed = np.zeros((n, (dim + 7) // 8), dtype=np.uint8)
        for i in range(dim):
            packed[:, i // 8] |= (binary[:, i] << (i % 8))
        return packed

def estimate_memory_usage(num_vectors: int, dimensions: int,
    quantization: str = "fp32", index_type: str = "hnsw", hnsw_m: int = 16) -> dict:
    """Estimate memory usage for different configurations."""
    bytes_per_dim = {"fp32": 4, "fp16": 2, "int8": 1, "pq": 0.05, "binary": 0.125}
    vector_bytes = num_vectors * dimensions * bytes_per_dim[quantization]
    index_bytes = num_vectors * hnsw_m * 2 * 4 if index_type == "hnsw" else 0
    total = vector_bytes + index_bytes
    return {"vector_mb": vector_bytes / 1024**2, "index_mb": index_bytes / 1024**2,
            "total_mb": total / 1024**2, "total_gb": total / 1024**3}
```

### Qdrant Optimization Profiles

```python
from qdrant_client import QdrantClient
from qdrant_client.http import models

def create_optimized_collection(client: QdrantClient, collection_name: str,
    vector_size: int, optimize_for: str = "balanced"):
    """Create collection with optimized settings: 'recall', 'speed', 'balanced', 'memory'."""
    hnsw = {
        "recall": models.HnswConfigDiff(m=32, ef_construct=256),
        "speed": models.HnswConfigDiff(m=16, ef_construct=64),
        "balanced": models.HnswConfigDiff(m=16, ef_construct=128),
        "memory": models.HnswConfigDiff(m=8, ef_construct=64)
    }
    quant = {
        "recall": None,
        "speed": models.ScalarQuantization(scalar=models.ScalarQuantizationConfig(
            type=models.ScalarType.INT8, quantile=0.99, always_ram=True)),
        "balanced": models.ScalarQuantization(scalar=models.ScalarQuantizationConfig(
            type=models.ScalarType.INT8, quantile=0.99, always_ram=False)),
        "memory": models.ProductQuantization(product=models.ProductQuantizationConfig(
            compression=models.CompressionRatio.X16, always_ram=False))
    }
    client.create_collection(
        collection_name=collection_name,
        vectors_config=models.VectorParams(size=vector_size, distance=models.Distance.COSINE),
        hnsw_config=hnsw[optimize_for],
        quantization_config=quant[optimize_for]
    )
```

---

## Hybrid Search (Vector + Keyword Fusion)

### Fusion Methods

| Method | Description | Best For |
|--------|-------------|----------|
| **RRF** | Reciprocal Rank Fusion | General purpose, no tuning needed |
| **Linear** | Weighted sum of normalized scores | Tunable balance |
| **Cross-encoder** | Neural reranking after fusion | Highest quality |
| **Cascade** | Filter with keywords, rerank with vectors | Efficiency |

### Reciprocal Rank Fusion (RRF)

```python
from collections import defaultdict
from typing import List, Tuple

def reciprocal_rank_fusion(
    result_lists: List[List[Tuple[str, float]]],
    k: int = 60,
    weights: List[float] = None
) -> List[Tuple[str, float]]:
    """Combine multiple ranked lists using RRF."""
    if weights is None:
        weights = [1.0] * len(result_lists)
    scores = defaultdict(float)
    for result_list, weight in zip(result_lists, weights):
        for rank, (doc_id, _) in enumerate(result_list):
            scores[doc_id] += weight * (1.0 / (k + rank + 1))
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)
```

### PostgreSQL Hybrid Search

```python
class PostgresHybridSearch:
    """Hybrid search with pgvector + full-text search + RRF fusion."""

    async def hybrid_search(self, query: str, query_embedding: List[float],
                            limit: int = 10, vector_weight: float = 0.5) -> List[Dict]:
        async with self.pool.acquire() as conn:
            results = await conn.fetch(f"""
                WITH vector_search AS (
                    SELECT id, content, metadata,
                           ROW_NUMBER() OVER (ORDER BY embedding <=> $1::vector) as vector_rank,
                           1 - (embedding <=> $1::vector) as vector_score
                    FROM documents
                    ORDER BY embedding <=> $1::vector LIMIT $3
                ),
                keyword_search AS (
                    SELECT id, content, metadata,
                           ROW_NUMBER() OVER (ORDER BY ts_rank(ts_content, websearch_to_tsquery('english', $2)) DESC) as keyword_rank
                    FROM documents
                    WHERE ts_content @@ websearch_to_tsquery('english', $2)
                    LIMIT $3
                )
                SELECT COALESCE(v.id, k.id) as id,
                       COALESCE(v.content, k.content) as content,
                       COALESCE(1.0 / (60 + v.vector_rank), 0) * $4::float +
                       COALESCE(1.0 / (60 + k.keyword_rank), 0) * (1 - $4::float) as rrf_score
                FROM vector_search v
                FULL OUTER JOIN keyword_search k ON v.id = k.id
                ORDER BY rrf_score DESC LIMIT $3 / 3
            """, query_embedding, query, limit * 3, vector_weight)
            return [dict(row) for row in results]
```

### Elasticsearch Hybrid Search (8.x RRF)

```python
def hybrid_search_rrf(es, index_name, query, query_embedding, limit=10, window_size=100):
    """Hybrid search using Elasticsearch 8.x native RRF."""
    return es.search(index=index_name, body={
        "size": limit,
        "sub_searches": [
            {"query": {"match": {"content": query}}},
            {"query": {"knn": {"field": "embedding", "query_vector": query_embedding,
                               "k": window_size, "num_candidates": window_size * 2}}}
        ],
        "rank": {"rrf": {"window_size": window_size, "rank_constant": 60}}
    })
```

---

## Performance Monitoring

```python
import time
from dataclasses import dataclass
import numpy as np

@dataclass
class SearchMetrics:
    latency_p50_ms: float
    latency_p95_ms: float
    latency_p99_ms: float
    recall: float
    qps: float

class VectorSearchMonitor:
    def measure_search(self, search_fn, query_vectors, k=10, num_iterations=100) -> SearchMetrics:
        """Benchmark search performance."""
        latencies = []
        for _ in range(num_iterations):
            for query in query_vectors:
                start = time.perf_counter()
                search_fn(query, k=k)
                latencies.append((time.perf_counter() - start) * 1000)

        latencies = np.array(latencies)
        total_time = sum(latencies) / 1000
        return SearchMetrics(
            latency_p50_ms=np.percentile(latencies, 50),
            latency_p95_ms=np.percentile(latencies, 95),
            latency_p99_ms=np.percentile(latencies, 99),
            recall=0,  # Calculate separately with ground truth
            qps=len(latencies) / total_time
        )
```

---

## Best Practices

### Do's
- **Benchmark with real queries** - Synthetic may not represent production
- **Use appropriate index** - HNSW for most cases, Flat for <10K
- **Implement hybrid search** - Combine with keyword search for better recall
- **Monitor recall continuously** - Can degrade with data drift
- **Use RRF for simplicity** - Works well without tuning
- **Tune weights empirically** - Test on your data
- **Use quantization** - Significant memory savings with minimal recall loss

### Don'ts
- **Don't over-optimize early** - Profile first, tune only when needed
- **Don't skip evaluation** - Measure before optimizing
- **Don't ignore latency** - P99 matters for UX
- **Don't forget costs** - Vector storage adds up at scale
- **Don't assume one size fits all** - Different queries need different weights

## Verification

To validate your vector search system is production-ready:

1. **Recall**: Recall@10 >= 0.95 on representative test queries with known ground truth
2. **Latency**: p95 search latency < 200ms; p99 < 500ms
3. **Memory**: Estimate with `estimate_memory_usage()` fits within available RAM
4. **Hybrid Search**: If implemented, A/B test shows improvement over vector-only search
5. **Index Parameters**: Benchmarked at least 3 HNSW configurations on your data
6. **Quantization**: If used, recall drop < 2% compared to full precision
7. **Scale Test**: Tested with 2x expected data volume

## Related Skills

- `rag-architecture` - End-to-end RAG pipeline design (chunking, retrieval, evaluation)
- `embedding-strategies` - Embedding model selection and optimization
- `langchain-optimization` - Optimizing LangChain-based applications
