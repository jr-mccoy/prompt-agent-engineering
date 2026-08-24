---
title: "Pinecone Vector Database Playbook"
category: AI-ML/genai-llm-engineering
description: "Design a RAG/embedding retrieval layer on Pinecone — index/namespace design, metric matching, metadata filtering, upserts, hybrid search, and a retrieval-quality vs. infra-health evaluation plan — without inventing version-specific API behavior, pod/pricing specs, or benchmark numbers."
techniques:
  - ST-02
  - CM-02
  - RT-02
  - DS-02
  - QA-01
difficulty: intermediate
tags:
  - pinecone
  - vector-database
  - rag
  - metadata-filtering
  - retrieval
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/genai-llm-engineering/genai_rag_system_design.md
  - domain-AI-ML/genai-llm-engineering/genai_embedding_model_selection.md
  - domain-AI-ML/genai-llm-engineering/genai_rag_retrieval_quality_debug.md
---

# Pinecone Vector Database Playbook

**Objective:** Turn a RAG/embedding retrieval need into a concrete Pinecone setup — index and namespace design, distance metric matched to the embedding model, metadata schema for filtering, upsert/ingestion strategy, hybrid (dense + sparse) search where supported, and an evaluation plan that separates retrieval quality from infrastructure health and cost.

**When to Use:**
- You have chosen Pinecone (managed vector database) and need an opinionated setup walkthrough.
- You want managed scaling/serving and multi-tenant isolation (namespaces) without operating your own vector store.
- You need metadata-filtered semantic search at scale.

**When NOT to Use:**
- You haven't designed the retrieval/RAG approach — start with `genai_rag_system_design.md`.
- Retrieval quality is poor and needs diagnosis — use `genai_rag_retrieval_quality_debug.md`.
- You'd rather co-locate vectors with relational data — see `genai_pgvector_vector_db_playbook.md`; coordinate infra with `domain-software-engineering/devops/`.

## Inputs / Context

Provide what you can:
- **Pinecone offering/tier** in use and SDK/API version.
- **Embedding model**, its **dimensionality**, and the distance metric it was trained for (cosine, dotproduct, euclidean).
- **Corpus size** and growth, query rate, and latency SLO.
- **Tenancy** — single corpus vs. many tenants/users (drives namespace design).
- **Filtering needs** — metadata fields for filtering; whether sparse/keyword signals matter (hybrid).

## Constraints

**Must:**
- Ask for the embedding dimension and intended metric before creating the index — the index metric must match the model.
- Use namespaces (or separate indexes) deliberately for tenant/data isolation; state the partition strategy.
- Define retrieval-quality evaluation (recall@k/nDCG on a labeled set) distinct from infra-health and cost metrics.

**Must Not:**
- Invent Pinecone API signatures, index/pod/serverless specs, quotas, or pricing, or quote benchmark recall/latency — mark "verify against current Pinecone docs and your account; measure on your data."
- Mismatch the index metric to the embedding model.
- Put high-cardinality or large free-text blobs in metadata used for filtering without considering filter cost/limits.

**Instructions:**

1. **Match metric and dimension.** Confirm the embedding dimension and the metric the model expects; create the index with that exact metric. Flag metric/normalization requirements (e.g., dotproduct often expects normalized vectors) as verify-in-docs.

2. **Design index & namespace layout.** Decide one index with namespaces (per tenant/source) vs. multiple indexes, based on isolation, query patterns, and limits. State the chosen partition strategy and why.

3. **Design the metadata schema.** Define metadata fields used for filtering (categorical/low-cardinality preferred for filters), and keep large text out of filter-critical metadata. Document the filter expressions queries will use.

4. **Plan ingestion & upserts.** Define batch upsert sizing, ID conventions (stable IDs for re-embedding), and the update/delete path when documents change. Note re-embedding implications when the model changes.

5. **Configure hybrid search (if needed).** Where supported, combine dense vectors with sparse/keyword signals; define how scores are weighted and when hybrid beats pure dense for your query mix.

6. **Tune top-k and filtering for the target.** Specify the retrieval `top_k`, filter usage, and how to sweep them against the labeled set to meet recall@k within the latency SLO; account for filter selectivity effects on recall.

7. **Separate quality, health, and cost.** Define retrieval-quality metrics (recall@k, nDCG, grounding) on a labeled set; infra-health (p99 latency, error rate); and cost drivers (vector count, query volume, tier). Keep them distinct.

8. **Define validation.** Provide a smoke test: upsert a sample corpus into a test namespace, run the labeled query set with and without filters, confirm recall@k and correct filter scoping at acceptable p99.

**Output Format:**

A markdown setup playbook:
- **Metric & Dimension Match** — model metric → index metric/normalization
- **Index & Namespace Layout** — partition strategy + rationale
- **Metadata Schema** — filter fields + example filter expressions
- **Ingestion & Upserts** — batch sizing, ID convention, re-embedding
- **Hybrid Search** — dense + sparse strategy (if used)
- **Tuning Plan** — top_k / filter sweep → recall@k vs. latency
- **Quality / Health / Cost Metrics** — three separate sets
- **Smoke Test** — recall + filter validation
- **Verify-in-Docs** — version/pricing/quota items flagged

## Verification

- [ ] The index metric matches the embedding model's metric (with normalization noted where required).
- [ ] Namespace/index partitioning is chosen deliberately for isolation and query patterns.
- [ ] Metadata filter fields are designed for filterability (no large free-text in filter-critical fields).
- [ ] Retrieval-quality metrics are defined on a labeled set, separate from health and cost.
- [ ] A tuning plan accounts for filter selectivity's effect on recall.
- [ ] API/pod/serverless specs, quotas, pricing, and benchmarks are flagged "verify/measure," not asserted.

## False-Positive Prevention

❌ **DON'T:**
- Create an index with a metric that differs from the embedding model's — recall silently drops while queries still return.
- Judge retrieval by latency or by eyeballing a few queries instead of recall@k on a labeled set.
- Quote pod sizes, serverless limits, quotas, or pricing from memory — they change and are account-specific.
- Apply aggressive metadata filters and assume recall is unaffected — filtering can exclude relevant neighbors.

✅ **DO:**
- Match the index metric to the model and normalize vectors when the metric requires it.
- Measure recall@k/nDCG on a labeled query set as the primary quality signal.
- Direct the user to current Pinecone docs/pricing for any spec, quota, or cost figure.
- Evaluate recall with the actual filters in place, since filter selectivity affects results.

## Example Output

```markdown
## Pinecone Playbook: Multi-Tenant Docs Search

### Metric & Dimension Match
- Model dim = 1536, metric = cosine → index metric cosine. (Verify normalization rules if switching to dotproduct.)

### Index & Namespace Layout
One index, namespace per tenant (`tenant_{id}`) for isolation + cheap per-tenant deletes. Rationale: strong isolation, simple routing.

### Metadata Schema
{doc_type, lang, source_id, updated_at}. Filters: doc_type, lang. Large text stays in payload, not filter fields.

### Ingestion & Upserts
Batch upserts (sized per docs guidance); stable IDs = hash(doc_id+chunk_idx); delete-by-id on doc removal; full re-embed + re-upsert if model changes.

### Hybrid Search
Dense primary; add sparse signal for code/keyword-heavy queries where supported; weight tuned on labeled set.

### Tuning Plan
Sweep top_k ∈ {5,10,20} with production filters; pick smallest meeting recall@10 ≥ target under p99 SLO.

### Quality / Health / Cost Metrics
Quality: recall@10, nDCG@10, grounding (labeled set). Health: p99, error rate. Cost: vector count, QPS, tier.

### Smoke Test
Upsert sample into tenant_test → labeled queries with/without filters → recall@10 meets target, filters scope correctly, p99 acceptable.

### Verify-in-Docs
- Index creation metric/normalization, namespace limits, upsert batch limits.
- Serverless/pod options, quotas, pricing.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** metric match → index/namespace → metadata → ingestion → hybrid → tuning → validation.
- **CM-02 (Constraint Specification):** no-fabrication, metric-match, and quality/health/cost separation constraints govern the design.
- **RT-02 (Multi-Dimensional Analysis):** layout and tuning weigh isolation, recall, latency, and cost together.
- **DS-02 (Metric Specification):** recall@k/nDCG, health, and cost metrics are defined explicitly and separately.
- **QA-01 (Self-Verification):** the smoke test validates recall and filter scoping under realistic filters.

**Related Prompts:**
- `genai_rag_system_design.md` — design the RAG approach before provisioning Pinecone.
- `genai_embedding_model_selection.md` — choose the embedding model whose metric the index must match.
- `genai_rag_retrieval_quality_debug.md` — diagnose retrieval quality when recall is below target.
