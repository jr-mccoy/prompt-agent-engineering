---
title: "Reranking Strategy"
category: AI-ML/genai-llm-engineering
description: "Add a reranking stage to a retrieval pipeline — verifying first that recall is high enough for reranking to help, choosing the reranker against the latency budget, and measuring the position of the correct document rather than aggregate relevance."
techniques:
  - ST-02
  - DS-02
  - RT-02
  - CM-02
  - QA-12
difficulty: advanced
tags:
  - reranking
  - cross-encoder
  - retrieval
  - rag
  - two-stage-retrieval
updated: "2026-08-22"
related_prompts:
  - domain-AI-ML/genai-llm-engineering/genai_rag_retrieval_quality_debug.md
  - domain-AI-ML/genai-llm-engineering/genai_query_rewriting_expansion.md
  - domain-AI-ML/genai-llm-engineering/genai_vector_index_tuning.md
  - domain-AI-ML/specialized-ml/recommender-systems/recsys_candidate_ranking_design.md
---

# Reranking Strategy

**Objective:** Decide whether a reranking stage will help and design it if so — establishing first that first-stage recall is high enough for reordering to have anything to work with, choosing a reranker against the latency budget rather than a leaderboard, and measuring where the correct document lands.

**When to Use:**
- The correct document is retrieved in the top-50 but not the top-5 that reach the generator.
- Retrieval recall is acceptable while precision at small k is not.
- Context window limits force a small number of passages and the wrong ones are being selected.

**When NOT to Use:**
- First-stage recall is poor — reranking cannot promote a document that was never retrieved. Fix retrieval first.
- The failure is query-side — use `genai_query_rewriting_expansion.md`.
- The latency budget has no room for a second scoring pass over candidates.

## Inputs / Context

- **First-stage recall at various k** — recall@10, @50, @100. This determines the ceiling on what reranking can achieve.
- **Passages the generator can consume** — the k that actually reaches it after reranking.
- **Latency budget remaining** after retrieval.
- **Query and passage characteristics** — length, since cross-encoder cost scales with both.
- **Domain specificity** — whether general rerankers understand this content or need adaptation.
- **Labelled relevance data** — query–passage pairs, if any, for evaluating or fine-tuning.

## Constraints

**Must:**
- Measure **recall@N for the candidate set N** before designing anything. Reranking's ceiling is exactly the recall of the candidate set it reorders; if recall@50 is low, reranking cannot help and the effort belongs in retrieval.
- Report the **position of the correct document** before and after reranking, not just aggregate relevance scores — the question is whether the right passage reaches the generator.
- State latency as a function of candidate count, since cross-encoder cost scales with candidates × passage length and is the dominant design constraint.
- Evaluate on the domain's own queries; general reranker quality does not transfer reliably to specialized corpora.
- Define behaviour when the reranker is unavailable or slow — fall back to first-stage order.

**Must Not:**
- Assert reranker comparison results, latency figures, or benchmark scores from memory; mark quantities `[measure on your data]`.
- Rerank a candidate set so large that latency breaks the budget, or so small that the correct document is usually outside it — both make the stage pointless.
- Evaluate reranking on the same examples used to select it.
- Assume a general-purpose reranker understands domain jargon; measure it.
- Report improvement in mean relevance score without showing that the correct document moved into the generator's window.

**Instructions:**

1. **Measure the recall ceiling.** Recall@10, @50, @100 on a labelled query set. If recall@50 is not substantially above recall@5, reranking has little to promote and the finding is that retrieval needs work — a legitimate and money-saving conclusion.

2. **Choose the candidate count N.** Large enough that the correct document is usually inside it (from step 1), small enough that N × per-candidate cost fits the latency budget. State both bounds and where N sits between them.

3. **Screen reranker options.**
   - *Cross-encoder* — scores query and passage jointly; strongest, and cost scales with N.
   - *Late-interaction* — precomputes passage representations; cheaper at query time, more storage.
   - *LLM-as-reranker* — flexible and expensive; can apply nuanced criteria a trained reranker cannot.
   - *Feature-based / learning-to-rank* — combines retrieval score with recency, authority, and metadata; very cheap and often overlooked when relevance is not purely semantic.
   Note that the last option is frequently the right answer when the real problem is that stale or low-authority documents outrank current ones.

4. **Decide on domain adaptation.** Evaluate a general reranker on domain queries first. Fine-tune only if it underperforms and labelled pairs exist; state the data requirement honestly rather than assuming it.

5. **Measure position, not just score.** Report the rank of the known-correct document before and after reranking, and the fraction that land inside the generator's window. That fraction is the metric the pipeline actually cares about.

6. **Report latency by candidate count.** A table of N against added p50 and p99, so the trade between recall ceiling and latency is explicit and someone can choose.

7. **Check for systematic bias.** Rerankers can favour longer passages, particular formats, or lexically similar text over semantically correct text. Inspect what gets promoted, particularly on the queries that got worse.

8. **Evaluate end to end, once.** Confirm the retrieval improvement produces an answer improvement. If it does not, the generator was not limited by retrieval and the reranking cost buys nothing user-visible.

9. **Define the fallback.** Reranker timeout or error → first-stage order, logged.

**Output Format:**

A markdown design:
- **Recall Ceiling** — recall@10/@50/@100 and the headroom reranking can address.
- **Candidate Count** — N, with its upper and lower bounds.
- **Reranker Screening** — table: Option | Quality on domain queries | Latency at N | Storage | Verdict.
- **Domain Adaptation** — needed or not, with evidence.
- **Position Measurement** — table: Query set | Correct-doc rank before | after | % inside generator window.
- **Latency by N** — table: N | p50 | p99.
- **Bias Inspection** — what gets promoted, especially on regressions.
- **End-to-End Check** — did answers improve.
- **Fallback** — reranker unavailable.

## Verification

- [ ] Recall at the candidate count is measured before design, and a low ceiling stops the work.
- [ ] N is justified against both the recall ceiling and the latency budget.
- [ ] Rerankers are evaluated on domain queries, not on general reputation.
- [ ] The correct document's position before and after is reported.
- [ ] The fraction landing inside the generator's window is reported.
- [ ] Latency is tabulated by candidate count.
- [ ] Promotion bias is inspected, including on queries that regressed.
- [ ] An end-to-end check confirms answers improved.
- [ ] A fallback to first-stage order exists.
- [ ] No reranker comparisons or latency figures are asserted from memory.

## False-Positive Prevention

❌ **DON'T:**
- Add reranking when recall@50 is barely above recall@5 — there is nothing to promote, and the stage adds latency for noise.
- Report mean relevance improvement without showing the correct document reached the generator; the generator sees only the top few, and the mean says nothing about them.
- Pick a reranker from general reputation and deploy it on a specialized corpus without measuring it there.
- Set N by convention; too small and the correct document is outside the candidate set, too large and latency breaks — both make the stage useless in different ways.
- Ignore that rerankers can systematically prefer longer or lexically overlapping passages over shorter correct ones.
- Skip the end-to-end check; if answers do not improve, retrieval was not the constraint and the cost is unrecovered.

✅ **DO:**
- Measure the recall ceiling first and let a low ceiling redirect the work to retrieval.
- Justify N explicitly between its two bounds.
- Consider cheap feature-based reranking when the real problem is staleness or authority rather than semantics.
- Report where the correct document lands, and how often it reaches the generator.
- Inspect what the reranker promotes on queries that got worse.
- Confirm the improvement survives to the answer before declaring success.

## Example Output

```markdown
## Reranking Strategy: Product Support RAG

### Recall Ceiling
| k | Recall |
|---|---|
| @5 (what the generator sees) | `[measure]` |
| @20 | `[measure]` |
| @50 | `[measure]` |
| @100 | `[measure]` |

The gap between recall@5 and recall@50 **is** the headroom reranking can address. If recall@50
is close to recall@5, stop: the correct documents are not being retrieved at all, and no
reordering fixes that.

### Candidate Count
- **Lower bound:** N must be large enough that the correct document is inside it — from the table
  above, the k where recall plateaus.
- **Upper bound:** N × per-candidate cross-encoder cost must fit `[remaining latency budget]`.
- **Chosen N:** `[select between the bounds]`, stated with both bounds so the trade is visible.

### Reranker Screening
| Option | Quality on **our** queries | Latency at N | Storage | Verdict |
|---|---|---|---|---|
| General cross-encoder | `[measure]` | `[measure]` | none | — |
| Late-interaction | `[measure]` | `[measure]` | **higher index storage** | — |
| LLM-as-reranker | `[measure]` | `[measure — expect highest]` | none | likely too slow |
| **Feature-based (retrieval score + doc recency + product-version match)** | `[measure]` | negligible | none | **evaluate seriously** |

The feature-based option is listed first among cheap candidates deliberately: a recurring
complaint here is that documentation for **superseded product versions** outranks current
documentation. That is a metadata problem, not a semantic one, and a cross-encoder is an
expensive way to fail at it.

### Domain Adaptation
Evaluate the general cross-encoder on domain queries before considering fine-tuning. Support
content is dense with product-specific jargon and version identifiers that general rerankers may
treat as noise. Fine-tune only if it underperforms **and** labelled query–passage pairs exist —
`[state how many are available]`, honestly, rather than assuming they can be produced.

### Position Measurement
| Query set | Correct-doc rank before | after | % inside top-5 |
|---|---|---|---|
| All labelled queries | `[measure]` | `[measure]` | `[measure]` |
| **Version-specific queries** | `[measure]` | `[measure]` | `[measure]` |
| **Regressed queries** | — | — | **inspect individually** |

"% inside top-5" is the number that matters, because the generator never sees anything else.

### Latency by N
| N | Added p50 | Added p99 |
|---|---|---|
| 20 | `[measure]` | `[measure]` |
| 50 | `[measure]` | `[measure]` |
| 100 | `[measure]` | `[measure]` |

Reranking sits between retrieval and generation, so this is additive on the critical path.

### Bias Inspection
Examine what the reranker promotes, focusing on **queries that got worse**. Watch for: promotion
of longer passages over shorter correct ones; promotion of passages with high lexical overlap
over semantically correct ones; and — the specific risk here — continued promotion of
superseded-version documents, which would mean the reranker is not attending to the version
metadata that the feature-based option handles directly.

### End-to-End Check
Confirm the retrieval improvement produces an answer improvement on a held-out set. If the
correct document now reaches the generator and answers do not improve, retrieval was not the
binding constraint and the reranking cost is buying nothing users experience — which is a
finding worth reporting rather than absorbing.

### Fallback
Reranker timeout or error → serve first-stage order, log the event, and alert if the fallback
rate exceeds a threshold. A pipeline that fails when the reranker is unavailable has made an
optimization into a dependency.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** the recall ceiling is measured before the stage is designed, so reranking is not added where it cannot help.
- **DS-02 (Metric Specification):** correct-document position and the fraction inside the generator window are the defined success metrics.
- **RT-02 (Multi-Dimensional Analysis Framework):** reranker option × domain quality × latency × storage is the screening grid.
- **CM-02 (Constraint Specification):** the N-bounds and domain-evaluation rules bound the design.
- **QA-12 (False Positives Identification):** rejects mean-relevance improvement as evidence and inspects promotion bias on regressions.

**Related Prompts:**
- `genai_rag_retrieval_quality_debug.md` — establishing whether the problem is recall or ranking.
- `genai_query_rewriting_expansion.md` — the query-side fix when retrieval misses entirely.
- `genai_vector_index_tuning.md` — raising the recall ceiling that bounds this stage.
- `../specialized-ml/recommender-systems/recsys_candidate_ranking_design.md` — the same two-stage pattern in recommendation.
