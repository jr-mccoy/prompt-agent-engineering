---
title: "pgvector Vector Search Playbook"
category: AI-ML/genai-llm-engineering
description: "Stand up vector search in PostgreSQL with pgvector for RAG/embedding workloads — schema and index choice (HNSW/IVFFlat), distance metric matching, hybrid search, ingestion, and retrieval-quality vs. infra-health evaluation — without inventing version-specific behavior or benchmarks."
techniques:
  - ST-02
  - CM-02
  - RT-02
  - DS-02
  - QA-01
difficulty: intermediate
tags:
  - pgvector
  - vector-database
  - rag
  - hybrid-search
  - retrieval
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/genai-llm-engineering/genai_rag_system_design.md
  - domain-AI-ML/genai-llm-engineering/genai_embedding_model_selection.md
  - domain-AI-ML/genai-llm-engineering/genai_rag_retrieval_quality_debug.md
---

# pgvector Vector Search Playbook

**Objective:** Turn a RAG/embedding retrieval need into a concrete pgvector setup inside PostgreSQL — table schema, the right index type (HNSW vs. IVFFlat) and distance metric matched to the embedding model, hybrid (vector + keyword/metadata) search, ingestion, and an evaluation plan that separates retrieval quality from infrastructure health.

**When to Use:**
- You want vector search co-located with relational data and already run (or prefer) PostgreSQL.
- Corpus scale and ops constraints favor "Postgres + pgvector" over a dedicated vector database.
- You need hybrid search (semantic + metadata/keyword filters) in one query path.

**When NOT to Use:**
- You haven't designed the retrieval/RAG approach yet — start with `genai_rag_system_design.md`.
- Retrieval quality is already poor and you need to diagnose it — use `genai_rag_retrieval_quality_debug.md`.
- Scale/latency clearly exceeds Postgres's comfort zone — compare a dedicated store (`genai_pinecone_*`, `genai_weaviate_*`, `genai_milvus_*`) and coordinate with `domain-software-engineering/devops/`.

## Inputs / Context

Provide what you can:
- **PostgreSQL version** and **pgvector version** (index types available differ by version).
- **Embedding model** and its **dimensionality** and the distance metric it was trained for (cosine, inner product, L2).
- **Corpus size** (rows) and growth, plus query rate and latency SLO.
- **Filtering needs** — metadata fields used to constrain results; keyword/full-text needs.
- **Update pattern** — bulk load vs. continuous upserts; how often embeddings change.

## Constraints

**Must:**
- Ask for the embedding model's dimension and intended distance metric before choosing an index/operator; the index distance must match the model.
- Choose the index type (HNSW vs. IVFFlat) and parameters from corpus size, recall target, and build/latency tradeoffs.
- Define a retrieval-quality evaluation (recall@k / nDCG on a labeled set) separate from infra-health metrics.

**Must Not:**
- Invent pgvector operators, index parameters, or PostgreSQL settings, or quote benchmark recall/latency numbers — mark "verify against your pgvector/PostgreSQL version and measure on your data."
- Mismatch the distance metric (e.g., index for L2 while the model expects cosine) — it silently degrades recall.
- Treat low query latency as evidence of good retrieval quality.

**Instructions:**

1. **Match the metric to the model.** Confirm the embedding dimension and the distance metric the model was trained for; the column type, index, and query operator must all use that metric. State the chosen operator/opclass as verify-in-docs.

2. **Design the schema.** Define the table: the vector column (with dimension), the chunk/text, and metadata columns used for filtering. Decide normalization (if using inner product) up front.

3. **Choose the index.** Compare HNSW (higher recall/lower query latency, slower build, more memory) vs. IVFFlat (faster build, needs good `lists`/probes tuning) against corpus size and recall target. Recommend one and state parameters to tune.

4. **Plan ingestion & upserts.** Define batch loading, embedding generation, and the upsert path for changing documents; note index maintenance implications (rebuild/repack) for heavy update workloads.

5. **Design hybrid search.** Combine vector similarity with metadata filters and (where needed) Postgres full-text search; decide pre-filter vs. post-filter ordering and how the two scores are combined or ranked.

6. **Tune for the recall/latency target.** Specify the search-time parameters (e.g., HNSW `ef_search` or IVFFlat probes) and how to sweep them against the labeled set to hit the recall@k target within the latency SLO.

7. **Separate quality from health metrics.** Define retrieval-quality metrics (recall@k, nDCG, answer-grounding) on a labeled eval set, and infra-health metrics (p99 latency, index build time, memory, bloat) separately. Cross-link `genai_rag_retrieval_quality_debug.md`.

8. **Define validation.** Provide a smoke test: load a sample corpus, run the labeled query set, confirm recall@k meets target at acceptable p99, and confirm metadata filters return correctly scoped results.

**Output Format:**

A markdown setup playbook:
- **Metric & Dimension Match** — model metric → column/index/operator
- **Schema** — vector column, text, metadata
- **Index Decision** — HNSW vs. IVFFlat + parameters (table)
- **Ingestion & Upserts** — load path + maintenance
- **Hybrid Search** — vector + filter/keyword strategy
- **Tuning Plan** — search params → recall@k vs. latency sweep
- **Quality vs. Health Metrics** — two separate metric sets
- **Smoke Test** — recall + filter validation
- **Verify-in-Docs** — version-sensitive items flagged

## Verification

- [ ] The index/operator distance metric matches the embedding model's metric.
- [ ] The index type and parameters are justified against corpus size and recall target.
- [ ] Hybrid search defines filter ordering and score combination, not just vector search.
- [ ] Retrieval-quality metrics (recall@k/nDCG) are defined on a labeled set, separate from latency/health.
- [ ] A tuning plan sweeps search params to hit recall@k within the latency SLO.
- [ ] pgvector operators/params and any benchmark numbers are flagged "verify/measure," not asserted.

## False-Positive Prevention

❌ **DON'T:**
- Index with a distance metric different from the one the embedding model was trained for — recall degrades silently while queries still "work."
- Conclude retrieval is good because p99 latency is low — fast wrong answers are still wrong.
- Quote HNSW/IVFFlat recall or latency figures from memory; they depend on data, dimension, and parameters.
- Add an ANN index and assume default parameters hit your recall target without measuring.

✅ **DO:**
- Align column type, index opclass, and query operator to the model's metric (and normalize if using inner product).
- Evaluate recall@k/nDCG on a labeled query set as the primary quality signal, latency as a separate constraint.
- Measure recall/latency on your own corpus and sweep search-time parameters.
- Mark every pgvector operator, index parameter, and Postgres setting as "verify against your version."

## Example Output

```markdown
## pgvector Playbook: Support-KB RAG (Postgres + pgvector)

### Metric & Dimension Match
- Embedding model dim = 1024, trained for cosine → use cosine opclass + cosine query operator (verify operator names for your pgvector version). Normalize if switching to inner product.

### Schema
chunks(id, doc_id, chunk_text, embedding vector(1024), product, lang, updated_at). Metadata: product, lang for filtering.

### Index Decision
| Option | Recall | Build | Memory | Verdict |
|---|---|---|---|---|
| HNSW | high | slower | higher | ✅ Chosen (read-heavy, recall priority) |
| IVFFlat | tunable | fast | lower | ❌ recall variance without careful lists/probes |
Params to tune: HNSW build (m, ef_construction) + query ef_search.

### Ingestion & Upserts
Batch embed + COPY load; upsert on doc change; schedule index maintenance for heavy churn.

### Hybrid Search
Pre-filter by product/lang (WHERE) then vector order-by similarity; optional full-text rank blended for keyword-heavy queries.

### Tuning Plan
Sweep ef_search against labeled set; pick smallest value meeting recall@10 ≥ target under p99 SLO.

### Quality vs. Health Metrics
Quality: recall@10, nDCG@10, answer-grounding on 200 labeled queries.
Health: p99 latency, index build time, memory, table/index bloat.

### Smoke Test
Load sample corpus → run labeled queries → recall@10 meets target at acceptable p99 → confirm product/lang filters scope results correctly.

### Verify-in-Docs
- Cosine/inner-product/L2 operator + opclass names for your pgvector version.
- HNSW/IVFFlat parameter names and defaults.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** metric match → schema → index → ingestion → hybrid → tuning → validation.
- **CM-02 (Constraint Specification):** no-fabrication, metric-match, and quality-vs-health separation constraints govern the design.
- **RT-02 (Multi-Dimensional Analysis):** index choice weighs recall, build time, memory, and latency together.
- **DS-02 (Metric Specification):** recall@k/nDCG and latency/health metrics are defined explicitly and separately.
- **QA-01 (Self-Verification):** the smoke test validates recall and filter scoping, not just that queries return.

**Related Prompts:**
- `genai_rag_system_design.md` — design the overall RAG approach before standing up the store.
- `genai_embedding_model_selection.md` — choose the embedding model whose metric this index must match.
- `genai_rag_retrieval_quality_debug.md` — diagnose retrieval quality when recall is below target.
