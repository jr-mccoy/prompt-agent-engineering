---
title: "Vector Index Tuning"
category: AI-ML/genai-llm-engineering
description: "Tune an approximate-nearest-neighbour index for the recall the application actually needs — measuring recall against exact search rather than assuming it, navigating the recall/latency/memory/build-time trade explicitly, and re-tuning when the corpus changes."
techniques:
  - DS-02
  - RT-02
  - ST-02
  - CM-02
  - QA-12
difficulty: advanced
tags:
  - vector-index
  - ann
  - recall-tuning
  - retrieval-latency
  - index-parameters
updated: "2026-08-22"
related_prompts:
  - domain-AI-ML/genai-llm-engineering/genai_rag_retrieval_quality_debug.md
  - domain-AI-ML/genai-llm-engineering/genai_reranking_strategy.md
  - domain-AI-ML/genai-llm-engineering/genai_embedding_model_selection.md
  - domain-AI-ML/genai-llm-engineering/genai_pgvector_vector_db_playbook.md
---

# Vector Index Tuning

**Objective:** Configure an approximate-nearest-neighbour index to deliver the recall the application needs at acceptable latency and memory — measuring approximation loss against exact search instead of assuming it away, and treating the tuning as something that expires when the corpus changes.

**When to Use:**
- Retrieval quality is below expectation and the embedding model is not the suspect.
- Query latency or index memory is unacceptable and you need to know what recall it would cost to fix.
- Corpus size has grown materially since the index was configured.

**When NOT to Use:**
- The embeddings themselves are the problem — use `genai_embedding_model_selection.md`; no index tuning fixes a representation that does not separate your content.
- The corpus is small enough for exact search — use it; ANN parameters are pure risk at that scale.
- You need vendor-specific setup rather than the tuning method — use the relevant playbook, e.g. `genai_pgvector_vector_db_playbook.md`.

## Inputs / Context

- **Corpus size and growth rate** — current vectors and expected growth, since the right structure changes with scale.
- **Embedding dimensionality and distance metric** — and confirmation the index is configured for the *same* metric the embeddings were trained for.
- **Recall requirement** — derived from the application: what the downstream stage needs to work.
- **Latency budget** for retrieval specifically.
- **Memory available** for the index.
- **Update pattern** — static, append-only, or frequently updated with deletions, which strongly constrains index choice.
- **Filtering requirements** — metadata filters applied with the vector search, which interact badly with some index types.

## Constraints

**Must:**
- Measure recall **against exact search on the same corpus and query set**. ANN recall is the fraction of true nearest neighbours returned, and it cannot be assumed from parameter values or vendor defaults.
- Derive the recall target from the downstream stage — if a reranker consumes the top 100, what matters is recall@100, not recall@10.
- Report the four-way trade together: recall, query latency, memory, and build time. Optimizing one silently spends the others.
- Confirm the index distance metric matches the embedding model's training objective; a mismatch degrades retrieval in a way that looks like a bad index.
- State how filtered search behaves, since pre- and post-filtering have very different recall consequences and this is where production filtering quietly breaks.

**Must Not:**
- Assert parameter values, recall figures, or latency numbers from memory; every one is `[measure on your corpus]`.
- Accept vendor defaults as tuned; defaults target a generic workload, not yours.
- Tune on the training or example queries; use held-out queries representative of production.
- Report recall@k for a k the application does not use.
- Assume tuning holds after significant corpus growth or a distribution change — it expires.

**Instructions:**

1. **Establish the exact-search ground truth.** Compute exact nearest neighbours for a held-out query set. This is the yardstick; without it every recall number is a guess. For large corpora, a sample suffices but must be representative.

2. **Verify the metric match.** Confirm the index distance metric is the one the embedding model was trained for, and that vectors are normalized if the metric expects it. A mismatch here produces poor retrieval that no amount of parameter tuning repairs, and it is a common silent misconfiguration.

3. **Derive the recall target from downstream need.** If a reranker takes 100 candidates, the target is recall@100. If passages go straight to the generator, it is recall at that small k, which is a much harder requirement. State which and why.

4. **Choose the index structure against corpus size, update pattern, and filtering.**
   - *Flat / exact* — perfect recall, linear scan. Correct for small corpora, and frequently dismissed too early.
   - *Graph-based* — strong recall–latency trade; higher memory; deletions can be awkward.
   - *Cluster / partition-based* — lower memory; recall depends on how many partitions are probed.
   - *Quantized variants* — much lower memory, some recall loss; often combined with the above.
   Note the update pattern explicitly: a frequently-updated corpus rules out structures that are expensive to modify.

5. **Sweep the parameters that trade recall for latency.** Every structure has one or two: how many partitions to probe, how wide the graph search is, quantization coarseness. Sweep and record recall against latency at each point. This sweep is the actual deliverable.

6. **Report the four-way trade.** A table of configuration against recall, p50 and p99 latency, index memory, and build time. Build time matters more than it appears — a configuration that takes many hours to build constrains how often the corpus can be refreshed.

7. **Test filtered search separately.** Metadata filtering combined with vector search is where recall silently collapses: post-filtering can return far fewer results than requested, and pre-filtering may not use the index at all. Measure recall **with the filters production actually applies**, not on unfiltered queries.

8. **Choose the operating point.** The lowest-cost configuration meeting the recall target with headroom, not the highest-recall configuration available.

9. **Set the re-tuning trigger.** Corpus growth beyond a threshold, embedding model change, or observed recall drift. Record the measured recall so drift is detectable rather than inferred from complaints.

**Output Format:**

A markdown tuning report:
- **Ground Truth** — exact-search query set, size, representativeness.
- **Metric Verification** — index metric vs embedding objective; normalization.
- **Recall Target** — derived from the downstream consumer.
- **Index Structure Choice** — against size, update pattern, filtering.
- **Parameter Sweep** — table: Config | Recall@target-k | p50 | p99 | Memory | Build time.
- **Filtered-Search Results** — recall with production filters applied.
- **Operating Point** — chosen configuration and why.
- **Re-tuning Triggers** — conditions and the recorded baseline.

## Verification

- [ ] Recall is measured against exact search on a held-out, representative query set.
- [ ] The index distance metric is verified against the embedding model's objective.
- [ ] The recall target is derived from what the downstream stage consumes.
- [ ] Index structure choice accounts for update pattern and filtering.
- [ ] The parameter sweep reports recall, latency, memory, and build time together.
- [ ] Filtered search is measured separately with production filters.
- [ ] The operating point is the lowest-cost configuration meeting the target with headroom.
- [ ] Re-tuning triggers are defined and the baseline recall is recorded.
- [ ] No parameter values or recall figures are asserted from memory.

## False-Positive Prevention

❌ **DON'T:**
- Assume ANN recall from parameter values or vendor documentation — measure it against exact search on your corpus, because it depends on your data's geometry.
- Accept vendor defaults as tuned; they target a generic workload and are frequently far from your recall requirement in either direction.
- Report recall@10 when a reranker consumes 100 candidates — you are measuring a quantity the pipeline does not use.
- Test only unfiltered queries when production applies metadata filters; filtered ANN search is where recall collapses silently and the unfiltered number hides it entirely.
- Optimize latency without reporting the recall it cost — the retrieval got faster and worse, and only one of those is visible.
- Treat a tuning as permanent; corpus growth changes the geometry the parameters were tuned against.

✅ **DO:**
- Build an exact-search ground truth first and keep it for future re-tuning.
- Verify the metric and normalization before touching any parameter — this misconfiguration masquerades as a tuning problem.
- Derive the recall target from the actual downstream consumer.
- Sweep the recall–latency parameter and publish the whole curve, not one point.
- Measure filtered recall with production's real filters.
- Record the baseline and define what triggers re-tuning.

## Example Output

```markdown
## Vector Index Tuning: Legal Document Retrieval
~2.4M passage embeddings; monthly corpus additions; every query filters by jurisdiction and
date range.

### Ground Truth
500 held-out production queries with exact nearest neighbours computed over the full corpus.
Sampled to match the production distribution of jurisdiction and query length. Retained for
future re-tuning, so later comparisons are like-for-like.

### Metric Verification
Embedding model trained with a cosine objective; index **must** be configured for cosine with
normalized vectors. `[verify — an index configured for Euclidean on unnormalized vectors
degrades retrieval in a way that looks exactly like poor tuning and will absorb days.]`

### Recall Target
A reranker consumes the **top 100**. Target is therefore **recall@100**, not recall@10 — a much
easier target, and tuning against recall@10 here would spend latency and memory on precision the
pipeline discards anyway.

### Index Structure Choice
| Factor | Implication |
|---|---|
| 2.4M vectors | too large for exact search at the latency budget |
| **Monthly additions, occasional deletions** | rules out structures that are expensive to modify; favours incrementally updatable |
| **Every query filtered** | filtering behaviour is a primary selection criterion, not an afterthought |

Filtering being universal here promotes it from a detail to a deciding factor.

### Parameter Sweep
| Config | Recall@100 | p50 | p99 | Memory | Build time |
|---|---|---|---|---|---|
| A (low search width) | `[measure]` | `[measure]` | `[measure]` | `[measure]` | `[measure]` |
| B (medium) | `[measure]` | `[measure]` | `[measure]` | `[measure]` | `[measure]` |
| C (high) | `[measure]` | `[measure]` | `[measure]` | `[measure]` | `[measure]` |
| D (medium + quantization) | `[measure]` | `[measure]` | `[measure]` | **lower** | `[measure]` |

Build time is in the table because the corpus refreshes monthly — a configuration taking many
hours to build constrains the refresh cadence, which is an operational cost that a
recall-and-latency-only comparison would hide entirely.

### Filtered-Search Results — measured separately
| Filter selectivity | Recall@100 unfiltered | Recall@100 **with filter** |
|---|---|---|
| Broad (common jurisdiction) | `[measure]` | `[measure]` |
| **Narrow (rare jurisdiction + tight date range)** | `[measure]` | `[measure — expect collapse]` |

This is the measurement most likely to change the design. With post-filtering, a narrow filter
can leave far fewer than 100 results after filtering because the ANN search returned candidates
that the filter then removed. The unfiltered recall number looks healthy while production
retrieval for a rare jurisdiction is returning almost nothing — and every query here is filtered.

### Operating Point
Choose the **lowest-cost** configuration meeting recall@100 **with the production filters
applied**, plus headroom for corpus growth. Not the highest-recall configuration: the reranker
consumes 100 candidates and cannot use precision beyond what it reorders.

### Re-tuning Triggers
- Corpus growth beyond a set fraction of the tuned size.
- Any embedding model change — the geometry changes and every parameter is invalidated.
- Observed recall drift on a periodic re-measurement against the retained ground truth.
- **Baseline recorded:** recall@100 filtered and unfiltered at the chosen configuration, so drift
  is measured rather than inferred from user complaints.
```

**Techniques Used:**
- **DS-02 (Metric Specification):** recall is defined against exact search at the k the downstream stage consumes.
- **RT-02 (Multi-Dimensional Analysis Framework):** recall × latency × memory × build time is the four-way trade reported together.
- **ST-02 (Structured Sequential Instructions):** ground truth and metric verification precede parameter tuning, so a misconfiguration is not tuned around.
- **CM-02 (Constraint Specification):** the measure-against-exact and filtered-search rules bound what may be claimed.
- **QA-12 (False Positives Identification):** rejects unfiltered recall as representative when production always filters.

**Related Prompts:**
- `genai_embedding_model_selection.md` — when the representation, not the index, is the limit.
- `genai_reranking_strategy.md` — the consumer whose candidate count sets the recall target.
- `genai_rag_retrieval_quality_debug.md` — locating the failure before tuning anything.
- `genai_pgvector_vector_db_playbook.md` — and its Pinecone, Weaviate, and Milvus siblings for vendor-specific setup.
