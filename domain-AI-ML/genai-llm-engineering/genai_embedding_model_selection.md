---
title: "Embedding Model Selection for Retrieval"
category: AI-ML/genai-llm-engineering
description: "Select an embedding model for retrieval by evaluating candidates on your own queries and corpus — domain fit, dimensionality, cost, and latency — rather than trusting a public leaderboard rank."
techniques:
  - RT-02
  - DS-02
  - DS-06
  - QA-12
  - ST-03
difficulty: intermediate
tags:
  - embeddings
  - retrieval
  - model-selection
  - mteb
  - benchmarking
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/genai-llm-engineering/genai_rag_system_design.md
  - domain-AI-ML/genai-llm-engineering/genai_chunking_strategy.md
  - domain-AI-ML/genai-llm-engineering/genai_rag_evaluation_harness.md
---

# Embedding Model Selection for Retrieval

**Objective:** Choose an embedding model for a retrieval/RAG system by running an MTEB-style evaluation on the user's own queries and corpus — comparing domain fit (retrieval quality on a labeled set), dimensionality/storage, cost, and latency — so the pick is grounded in measured performance on the real workload rather than a public leaderboard position.

**When to Use:**
- Standing up retrieval and choosing (or re-evaluating) the embedding model.
- Retrieval quality is mediocre and the embedder is a suspected cause.
- Considering a cheaper/smaller embedding model and needing to quantify the quality tradeoff.

**When NOT to Use:**
- Designing the whole RAG system (use `genai_rag_system_design.md`; this is the embedder sub-decision).
- The retrieval problem is actually chunking (use `genai_chunking_strategy.md`).

## Inputs / Context

Provide what you can:
- **Corpus** — domain, vocabulary (technical/medical/legal/general), language(s), document length.
- **Query distribution** — example real queries with known relevant documents (or note a labeled set must be built).
- **Constraints** — embedding cost ceiling, storage/dimensionality limits, latency SLA, on-prem vs API, max sequence length needs.
- **Candidate models** — any shortlist already in mind (API and/or open-weights).
- **Existing index** — current embedder and its measured retrieval quality, if any.

## Constraints

**Must:**
- Evaluate candidates on the user's own queries + corpus with a labeled relevance set — not on leaderboard rank alone.
- Compare on retrieval quality (recall@k / MRR / nDCG), dimensionality/storage, cost, and latency together.
- Account for query/document length vs the model's max sequence length and any domain-language fit.

**Must Not:**
- Recommend a model because it tops MTEB or a leaderboard; public benchmarks may not reflect the user's domain or query style.
- Mix embedding spaces — querying an index built with model A using model B's embeddings is invalid.
- Fabricate benchmark scores or dimensions; require evaluation on the user's data and verification of specs against current model docs.

**Instructions:**

1. **Build a labeled retrieval eval set.** Sample representative queries; for each, mark the known-relevant documents/passages. Include domain-jargon and exact-term queries. This set is the arbiter — leaderboards are only for shortlisting.

2. **Shortlist candidates.** Use leaderboards (e.g., MTEB) only to pick 3–5 plausible candidates spanning size/cost tiers, then verify each model's dimensionality, max sequence length, and cost against current docs.

3. **Evaluate retrieval quality on your data.** Embed the corpus and queries with each candidate, run retrieval, and measure recall@k, MRR, nDCG against the labeled relevances at the k your system will use.

4. **Measure cost, storage, and latency.** Compute embedding cost (per corpus + per query at volume), index storage (driven by dimensionality), and query-time embedding latency. Higher dimensions cost more storage and may add little quality.

5. **Check domain and length fit.** Verify the model handles your vocabulary (technical terms shouldn't collapse to generic vectors) and that document/query lengths fit max sequence length without silent truncation.

6. **Weigh the tradeoff.** Score candidates across quality, cost, storage, latency using the user's constraints as weights. A small quality gain rarely justifies a large cost/storage increase.

7. **Recommend and define re-evaluation.** Recommend the model, state the runner-up and why it lost, and define when to re-evaluate (corpus drift, new model releases, quality regression).

**Output Format:**

A markdown selection report:
- **Eval Set** — query/relevance composition + how built
- **Candidates** — table: Model | Dim | Max seq | Cost | (specs to verify)
- **Retrieval Results** — table: Model | recall@k | MRR | nDCG (on user data, with CIs)
- **Cost/Storage/Latency** — table per candidate
- **Domain/Length Fit Notes**
- **Recommendation** — chosen model + runner-up + why
- **Re-evaluation Triggers**

## Verification

- [ ] Candidates are evaluated on the user's own labeled queries/corpus, not just leaderboard rank.
- [ ] Retrieval quality, cost, storage, and latency are compared together.
- [ ] Dimensionality, max sequence length, and cost are verified against current docs, not recalled.
- [ ] Query/document length vs max sequence length (truncation risk) is checked.
- [ ] The recommendation weighs quality gains against cost/storage increases.
- [ ] No benchmark scores are fabricated; results trace to the user's eval set.

## False-Positive Prevention

❌ **DON'T:**
- Pick the top MTEB model and assume it's best for your domain — benchmark corpora may not resemble yours.
- Equate higher dimensionality with better retrieval; it raises storage/latency and often adds little.
- Compare models on retrieval quality alone and ignore that one costs 10x at your volume.
- Silently truncate long documents that exceed the model's max sequence length.

✅ **DO:**
- Let a labeled eval set on your own queries decide; use leaderboards only to shortlist.
- Verify dimensions, max sequence length, and pricing against current model documentation.
- Score quality against cost, storage, and latency jointly, weighted by your constraints.
- Re-evaluate when the corpus drifts or strong new models ship.

## Example Output

```markdown
## Embedding Selection: Legal Clause Retrieval

### Eval Set
90 queries with SME-labeled relevant clauses; includes 25 exact-citation queries (e.g., "Section 4.2(b)").

### Candidates (specs to verify vs current docs)
| Model | Dim | Max seq | Cost tier |
|---|---|---|---|
| API-large | 3072 | 8k | high |
| API-small | 1536 | 8k | low |
| Open-weights-base | 768 | 512 | self-host |

### Retrieval Results (recall@5 on our data)
| Model | recall@5 | MRR | nDCG@5 |
|---|---|---|---|
| API-large | 0.91 ±0.03 | 0.84 | 0.88 |
| API-small | 0.88 ±0.03 | 0.80 | 0.85 |
| Open-base | 0.79 ±0.04 | 0.71 | 0.76 (truncation on long clauses) |

### Cost/Storage/Latency
API-small: ~1/4 the storage of API-large, ~1/3 the cost, +2pt quality loss only.

### Recommendation
API-small. The 3-pt recall gap to API-large doesn't justify 3x cost + 2x storage at our volume.
Open-base rejected: 512 max-seq truncates long clauses, costing recall. Hybrid BM25 added for
exact-citation queries.

### Re-evaluation Triggers
New corpus domain added, or a new model claims a material gain — re-run this eval set.
```

**Techniques Used:**
- **RT-02 (Multi-Dimensional Analysis Framework):** quality, cost, storage, latency weighed together.
- **DS-02 (Metric Specification):** retrieval metrics at a defined k on the user's labeled set.
- **DS-06 (Prioritization & Severity Guidance):** the recommendation ranks by weighted tradeoff.
- **QA-12 (False Positives Identification):** guards against leaderboard-rank and high-dimension fallacies.
- **ST-03 (Output Format Specification):** structured comparison tables drive the decision.

**Related Prompts:**
- `genai_rag_system_design.md` — the system this embedder slots into.
- `genai_chunking_strategy.md` — chunking and embedder choice interact (length, truncation).
- `genai_rag_evaluation_harness.md` — the harness whose retrieval layer this selection feeds.
