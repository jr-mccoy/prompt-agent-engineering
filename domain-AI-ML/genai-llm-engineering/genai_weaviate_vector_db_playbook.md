---
title: "Weaviate Vector Database Playbook"
category: AI-ML/genai-llm-engineering
description: "Design a RAG/embedding retrieval layer on Weaviate — collection schema, vectorizer vs. bring-your-own-vectors, metric matching, native hybrid (BM25 + vector) search, multi-tenancy, and retrieval-quality vs. infra-health evaluation — without inventing version-specific behavior or benchmarks."
techniques:
  - ST-02
  - CM-02
  - RT-02
  - DS-02
  - QA-01
difficulty: intermediate
tags:
  - weaviate
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

# Weaviate Vector Database Playbook

**Objective:** Turn a RAG/embedding retrieval need into a concrete Weaviate setup — collection schema and properties, the choice between a built-in vectorizer module and bring-your-own-vectors, distance metric matching, native hybrid search (BM25 + vector), multi-tenancy, and an evaluation plan that separates retrieval quality from infrastructure health.

**When to Use:**
- You have chosen Weaviate and need an opinionated setup walkthrough.
- You want native hybrid search (keyword BM25 fused with vector) and/or built-in vectorizer modules.
- You need multi-tenant isolation and an object+vector data model in one store.

**When NOT to Use:**
- You haven't designed the retrieval/RAG approach — start with `genai_rag_system_design.md`.
- Retrieval quality is poor and needs diagnosis — use `genai_rag_retrieval_quality_debug.md`.
- A simpler Postgres-resident store fits better — see `genai_pgvector_vector_db_playbook.md`; coordinate infra with `domain-software-engineering/devops/`.

## Inputs / Context

Provide what you can:
- **Weaviate deployment** (self-hosted vs. managed) and **version**.
- **Vector source** — a Weaviate vectorizer module vs. bring-your-own (BYO) vectors from your own embedding model.
- **Embedding model**, **dimensionality**, and the distance metric it expects (cosine, dot, l2).
- **Corpus size**, query rate, latency SLO, and **multi-tenancy** needs.
- **Hybrid needs** — how much keyword/BM25 matters vs. pure semantic for your queries.

## Constraints

**Must:**
- Decide vectorizer-module vs. BYO vectors explicitly, and if BYO, match the collection's distance metric to the embedding model.
- Use Weaviate multi-tenancy for tenant isolation when applicable; state the tenancy model.
- Define retrieval-quality evaluation (recall@k/nDCG on a labeled set) separate from infra-health metrics; for hybrid, tune the fusion weight (alpha) on that set.

**Must Not:**
- Invent Weaviate schema fields, GraphQL/REST/client API, module config, or quote benchmark numbers — mark "verify against your Weaviate version's docs; measure on your data."
- Mix a vectorizer module and BYO vectors for the same collection without a clear, consistent choice.
- Treat hybrid search as strictly better than dense without measuring the alpha tradeoff for your query mix.

**Instructions:**

1. **Choose the vector source.** Decide vectorizer module (Weaviate embeds on ingest/query) vs. BYO vectors (you embed and provide them). State the implication: BYO gives full control and requires metric matching; modules simplify ops but couple you to the module.

2. **Match metric (BYO) or confirm module.** For BYO, set the collection's distance metric to the embedding model's; for a module, confirm the module's metric and dimension. Mark exact config as verify-in-docs.

3. **Design the collection schema.** Define the collection and properties (text, metadata for filtering), the vector configuration, and index settings (e.g., HNSW parameters). Keep filterable metadata typed and lean.

4. **Set up multi-tenancy (if needed).** Enable tenant isolation and define how tenants map to data; this affects indexing, deletes, and query routing.

5. **Configure hybrid search.** Use native hybrid (BM25 + vector) and define the fusion weight (alpha) and fusion method; decide per-query-type defaults. Hybrid is a key Weaviate strength — make alpha a tuned parameter, not a guess.

6. **Plan ingestion & updates.** Define batch import sizing, object IDs, and the update/delete path; for BYO, the embedding step; note re-import/re-embed when the model changes.

7. **Tune and separate metrics.** Sweep top-k and alpha against a labeled set to hit recall@k within the latency SLO. Track retrieval-quality metrics separately from infra-health (p99 latency, import time, memory). Cross-link `genai_rag_retrieval_quality_debug.md`.

8. **Define validation.** Provide a smoke test: create the collection (with a test tenant), import a sample corpus, run the labeled query set across alpha values, confirm recall@k and correct tenant/metadata scoping at acceptable p99.

**Output Format:**

A markdown setup playbook:
- **Vector Source Decision** — module vs. BYO + implications
- **Metric & Dimension** — collection metric matched to model (BYO) or module config
- **Collection Schema** — properties, vector config, index settings
- **Multi-Tenancy** — tenancy model (if used)
- **Hybrid Search** — alpha + fusion method + per-query defaults
- **Ingestion & Updates** — import sizing, IDs, re-embed path
- **Tuning & Metrics** — top-k/alpha sweep; quality vs. health metrics
- **Smoke Test** — recall + tenancy/filter validation
- **Verify-in-Docs** — version-sensitive items flagged

## Verification

- [ ] Vector source (module vs. BYO) is chosen explicitly and consistently per collection.
- [ ] For BYO, the collection distance metric matches the embedding model.
- [ ] Multi-tenancy is configured when isolation is required.
- [ ] Hybrid alpha is a tuned parameter validated on a labeled set, not a default guess.
- [ ] Retrieval-quality metrics are tracked separately from infra-health.
- [ ] Schema/API/module config and benchmarks are flagged "verify/measure," not asserted.

## False-Positive Prevention

❌ **DON'T:**
- Provide BYO vectors while the collection's distance metric differs from the model's — recall degrades silently.
- Assume hybrid search always beats dense; the right alpha is query-mix-dependent and must be measured.
- Quote Weaviate schema keys, client methods, or module config from memory as version-stable.
- Judge quality by latency or a handful of sample queries instead of recall@k on a labeled set.

✅ **DO:**
- Pick module vs. BYO deliberately and, for BYO, match the metric to the model.
- Tune alpha (and top-k) on a labeled set; report recall@k/nDCG as the quality signal.
- Mark all schema/API/module specifics as "verify against your Weaviate version."
- Validate tenant and metadata scoping explicitly in the smoke test.

## Example Output

```markdown
## Weaviate Playbook: Knowledge-Base RAG (BYO vectors, hybrid)

### Vector Source Decision
BYO vectors from in-house embedding model (control + consistency with offline eval). Module not used.

### Metric & Dimension
Model dim = 768, cosine → collection distance = cosine. (Verify config key for your version.)

### Collection Schema
Collection `KBChunk`: properties {text, doc_type, lang, source_id}; vector dim 768; HNSW index params to tune.

### Multi-Tenancy
Enabled; tenant per customer for isolation + per-tenant deletes.

### Hybrid Search
Native BM25 + vector; alpha tuned (0=keyword, 1=vector); default alpha set from labeled-set sweep; fusion method per docs.

### Ingestion & Updates
Batch import (sized per docs); object IDs = stable hash; embed before import; re-embed + re-import on model change.

### Tuning & Metrics
Sweep top-k × alpha on 200 labeled queries → pick best recall@10 under p99 SLO.
Quality: recall@10, nDCG@10. Health: p99, import time, memory.

### Smoke Test
Create collection + test tenant → import sample → run labeled set across alpha → recall@10 meets target; tenant/metadata scoping correct; p99 acceptable.

### Verify-in-Docs
- Distance-metric config, HNSW params, hybrid alpha/fusion API for your version.
- Multi-tenancy setup specifics.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** vector source → metric → schema → tenancy → hybrid → ingestion → tuning → validation.
- **CM-02 (Constraint Specification):** no-fabrication, metric-match, and quality-vs-health constraints govern the design.
- **RT-02 (Multi-Dimensional Analysis):** module-vs-BYO and hybrid alpha weigh control, recall, latency, and ops together.
- **DS-02 (Metric Specification):** recall@k/nDCG and health metrics are defined explicitly; alpha is tuned to a metric.
- **QA-01 (Self-Verification):** the smoke test validates recall, tenancy, and filter scoping.

**Related Prompts:**
- `genai_rag_system_design.md` — design the RAG approach before provisioning Weaviate.
- `genai_embedding_model_selection.md` — choose the embedding model the collection metric must match.
- `genai_rag_retrieval_quality_debug.md` — diagnose retrieval quality when recall is below target.
