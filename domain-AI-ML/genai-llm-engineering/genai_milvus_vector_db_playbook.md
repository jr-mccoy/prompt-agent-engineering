---
title: "Milvus Vector Database Playbook"
category: AI-ML/genai-llm-engineering
description: "Design a high-scale RAG/embedding retrieval layer on Milvus — collection schema and partitions, index type selection (HNSW/IVF/DiskANN-family), metric matching, scalar filtering, sharding/consistency, and retrieval-quality vs. infra-health evaluation — without inventing version-specific behavior or benchmarks."
techniques:
  - ST-02
  - CM-02
  - RT-02
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - milvus
  - vector-database
  - rag
  - ann-index
  - retrieval
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/genai-llm-engineering/genai_rag_system_design.md
  - domain-AI-ML/genai-llm-engineering/genai_embedding_model_selection.md
  - domain-AI-ML/genai-llm-engineering/genai_rag_retrieval_quality_debug.md
---

# Milvus Vector Database Playbook

**Objective:** Turn a high-scale RAG/embedding retrieval need into a concrete Milvus setup — collection schema and partitions, the right ANN index family (HNSW, IVF variants, or disk-based) and metric matched to the embedding model, scalar filtering, sharding/consistency choices, and an evaluation plan separating retrieval quality from infrastructure health.

**When to Use:**
- You have chosen Milvus and need an opinionated setup walkthrough, often at large corpus scale (tens of millions+ of vectors).
- You need to choose among multiple ANN index types for a recall/latency/memory tradeoff.
- You need scalar filtering, partitions, and tunable consistency at scale.

**When NOT to Use:**
- You haven't designed the retrieval/RAG approach — start with `genai_rag_system_design.md`.
- Retrieval quality is poor and needs diagnosis — use `genai_rag_retrieval_quality_debug.md`.
- Scale is modest and a simpler store suffices — see `genai_pgvector_vector_db_playbook.md`; coordinate infra with `domain-software-engineering/devops/`.

## Inputs / Context

Provide what you can:
- **Milvus version** and deployment mode (standalone, cluster, or managed); object/metadata store backing it.
- **Embedding model**, **dimensionality**, and metric it expects (IP, COSINE, L2).
- **Corpus size** and growth, query rate, latency SLO, and recall target.
- **Memory vs. disk budget** — drives index family (in-memory vs. disk-based).
- **Filtering & partitioning** — scalar fields for filtering; natural partition key (tenant, time, source).

## Constraints

**Must:**
- Ask for the embedding dimension and metric before creating the collection; the index metric must match the model.
- Choose the ANN index family from corpus size, recall target, and the memory/disk budget; state search params to tune.
- Define retrieval-quality evaluation (recall@k/nDCG on a labeled set) distinct from infra-health metrics, and sweep search params to hit the recall target within the latency SLO.

**Must Not:**
- Invent Milvus index types, params, API signatures, or consistency-level names, or quote benchmark recall/latency — mark "verify against your Milvus version's docs; measure on your data."
- Pick an in-memory index when corpus size exceeds the memory budget (or a disk index when latency can't tolerate it) without stating the tradeoff.
- Treat strong consistency as free — note its latency cost vs. bounded/eventual options.

**Instructions:**

1. **Match metric and dimension.** Confirm the embedding dimension and metric; create the collection's vector field and index with that metric. Mark exact metric names as verify-in-docs.

2. **Design schema & partitions.** Define the collection schema (vector field + scalar fields for filtering) and a partition strategy (e.g., by tenant/time/source) to prune the search space and speed filtered queries.

3. **Select the ANN index family.** Compare options (e.g., HNSW for in-memory high recall/low latency; IVF variants for memory/build tradeoffs; disk-based for very large corpora beyond RAM) against corpus size, recall target, and memory/disk budget. Recommend one with parameters to tune.

4. **Plan ingestion, load, and updates.** Define batch insert sizing, the build-index-then-load flow, ID conventions, and the delete/upsert + compaction path. Note re-embed/re-index when the model changes.

5. **Design filtered search.** Specify scalar filter expressions combined with vector search and how partitions are leveraged for selective queries; account for filter selectivity's effect on recall.

6. **Choose consistency & sharding.** Pick a consistency level appropriate to freshness needs (stronger = higher latency) and a shard/replica layout for the query/throughput target. State the tradeoff explicitly.

7. **Tune and separate metrics.** Sweep index/search params (e.g., HNSW `ef`, IVF `nprobe`) against a labeled set to hit recall@k within the latency SLO. Track retrieval-quality metrics separately from infra-health (p99 latency, index build/load time, memory/disk). Cross-link `genai_rag_retrieval_quality_debug.md`.

8. **Define validation.** Provide a smoke test: create the collection, insert a representative sample, build/load the index, run the labeled query set (with filters), confirm recall@k and correct filtering at acceptable p99, and confirm consistency behavior matches expectations.

**Output Format:**

A markdown setup playbook:
- **Metric & Dimension Match** — model metric → collection/index metric
- **Schema & Partitions** — fields + partition strategy
- **Index Decision** — index family + params (table: option | recall | memory/disk | latency | verdict)
- **Ingestion & Updates** — insert/load flow, IDs, compaction
- **Filtered Search** — scalar filters + partition pruning
- **Consistency & Sharding** — level + replica/shard layout + tradeoffs
- **Tuning & Metrics** — param sweep; quality vs. health metrics
- **Smoke Test** — recall + filter + consistency validation
- **Verify-in-Docs** — version-sensitive items flagged

## Verification

- [ ] The collection/index metric matches the embedding model's metric.
- [ ] The ANN index family fits the corpus size and memory/disk budget, with a stated tradeoff.
- [ ] Partitioning and scalar filters are designed to prune the search space.
- [ ] The consistency level is chosen against freshness needs with its latency cost acknowledged.
- [ ] Retrieval-quality metrics are tracked separately and swept to the recall target within the latency SLO.
- [ ] Milvus index types/params/API and benchmarks are flagged "verify/measure," not asserted.

## False-Positive Prevention

❌ **DON'T:**
- Choose an index with a metric different from the embedding model's — recall degrades silently.
- Select an in-memory index for a corpus that exceeds the memory budget (OOM/cost) or a disk index when latency can't absorb it — without naming the tradeoff.
- Quote HNSW/IVF/disk-index recall or latency numbers from memory; they depend on data, params, and hardware.
- Default to the strongest consistency level and then miss the latency SLO.

✅ **DO:**
- Match the index metric to the model and confirm the exact metric name for your version.
- Pick the index family from a recall/memory/disk/latency matrix and measure on your own data.
- Choose a consistency level that balances freshness against the latency SLO, and state the tradeoff.
- Sweep search params (ef/nprobe/etc.) against a labeled set to hit recall@k within the SLO.

## Example Output

```markdown
## Milvus Playbook: 80M-Vector Enterprise Search (cluster)

### Metric & Dimension Match
- Model dim = 1024, cosine → collection metric COSINE (verify metric name/normalization for your version).

### Schema & Partitions
Fields: pk, embedding(1024), tenant_id, doc_type, ts. Partition by tenant_id to prune per-tenant queries.

### Index Decision
| Option | Recall | Memory/Disk | Latency | Verdict |
|---|---|---|---|---|
| HNSW (in-memory) | high | high RAM | low | ❌ 80M exceeds RAM budget |
| IVF variant | tunable | moderate | moderate | △ fallback |
| Disk-based ANN | high | disk-backed | higher | ✅ Chosen (scale > RAM) |
Params to tune per chosen family.

### Ingestion & Updates
Batch insert → build index → load; stable pk; delete+compaction for churn; re-index on model change.

### Filtered Search
expr filters on tenant_id/doc_type + vector search; partition pruning by tenant; recall measured with filters applied.

### Consistency & Sharding
Bounded-staleness consistency (freshness ok, lower latency than strong); shards/replicas sized to QPS target. Tradeoff stated.

### Tuning & Metrics
Sweep search param against 300 labeled queries → recall@10 ≥ target under p99 SLO.
Quality: recall@10, nDCG@10. Health: p99, build/load time, memory/disk.

### Smoke Test
Create collection → insert sample → build/load → labeled queries with filters → recall@10 + filtering correct at acceptable p99 → confirm consistency behavior.

### Verify-in-Docs
- Metric names, index types + params, consistency levels for your Milvus version.
- Compaction, sharding/replica configuration.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** metric match → schema/partitions → index → ingestion → filtering → consistency → tuning → validation.
- **CM-02 (Constraint Specification):** no-fabrication, metric-match, and budget/consistency-tradeoff constraints govern the design.
- **RT-02 (Multi-Dimensional Analysis):** index and consistency choices weigh recall, memory/disk, latency, and freshness together.
- **DS-02 (Metric Specification):** recall@k/nDCG and health metrics are defined explicitly and swept to a target.
- **QA-01 (Self-Verification):** the smoke test validates recall, filtering, and consistency at scale.

**Related Prompts:**
- `genai_rag_system_design.md` — design the RAG approach before provisioning Milvus.
- `genai_embedding_model_selection.md` — choose the embedding model the index metric must match.
- `genai_rag_retrieval_quality_debug.md` — diagnose retrieval quality when recall is below target.
