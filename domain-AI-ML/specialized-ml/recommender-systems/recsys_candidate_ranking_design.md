---
title: "Two-Stage Candidate Generation & Ranking Design"
category: AI-ML/specialized-ml/recommender-systems
description: "Design the two-stage retrieval (candidate generation) + ranking pipeline for a recommender — the recall mechanisms, the ranking features and objective, and the handoff between stages — sized to catalog scale and latency."
techniques:
  - ST-02
  - RT-02
  - DS-02
  - CM-02
  - DS-06
difficulty: advanced
tags:
  - recommender-systems
  - candidate-generation
  - ranking
  - retrieval
  - features
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/specialized-ml/recommender-systems/recsys_architecture_design.md
  - domain-AI-ML/specialized-ml/recommender-systems/recsys_offline_evaluation.md
  - domain-AI-ML/specialized-ml/recommender-systems/recsys_objective_business_alignment.md
---

# Two-Stage Candidate Generation & Ranking Design

**Objective:** Design the internals of a two-stage recommender — the candidate-generation (retrieval) layer that recalls a manageable set from the full catalog, and the ranking layer that scores them precisely — specifying each stage's mechanism, inputs, training labels, objective, and the handoff between them, all sized to catalog scale and the per-request latency budget.

**When to Use:**
- The overall architecture is settled as two-stage and you need to design the retrieval and ranking layers.
- Recall is poor (good items never reach the ranker) or precision is poor (the ranker reorders bad candidates well).
- Adding or replacing a retriever, or upgrading the ranking model and its features/objective.

**When NOT to Use:**
- Choosing whether a two-stage system is even warranted (use `recsys_architecture_design.md`).
- Measuring whether the design works offline and whether it will transfer online (use `recsys_offline_evaluation.md`).
- Defining what the ranker should optimize for the business (use `recsys_objective_business_alignment.md`).

## Inputs / Context

Provide what you can:
- **Catalog & latency** — item count, per-request latency budget, QPS, target candidate-set size after retrieval.
- **Available retrieval signals** — co-occurrence/co-engagement, embeddings (collaborative or content), recency, business rules, multiple complementary sources.
- **Ranking features** — user features, item features, context (time, device, query), and cross/interaction features; what's available online at serving time.
- **Labels & objective** — what the ranker trains on (click, purchase, dwell, multi-objective) and how labels are logged.
- **Constraints** — diversity/freshness needs, train/serve parity concerns, cold-item coverage requirements.

## Constraints

**Must:**
- Specify both stages: retrieval (recall, cheap, many) and ranking (precision, expensive, few), and the candidate-set size handed off.
- Tie the retriever choice to recall coverage (including cold/long-tail items) and the ranker to the labeled objective.
- State the train/serve parity requirement — features must be computed identically offline and online.

**Must Not:**
- Optimize ranking metrics while ignoring retrieval recall — the ranker can only reorder what retrieval surfaces.
- Use a feature in training that is unavailable (or computed differently) at serving time.
- Fabricate metric numbers; reason from the user's data and mark unknowns.

**Instructions:**

1. **Set the stage budget.** From catalog size and latency, fix the retrieval output size (how many candidates the ranker can afford to score) and the per-stage latency split. This bounds every downstream choice.

2. **Design candidate generation for recall.** Choose complementary retrievers (e.g., collaborative co-engagement + content/embedding ANN + recency/popularity backfill) so that good items — including cold and long-tail — reach the ranker. State the recall target and how it's measured.

3. **Design the ranking model.** Specify the model class (right-sized to data volume), its feature groups (user / item / context / cross), and how it consumes the candidate set. Avoid a heavyweight ranker where a gradient-boosted model on engineered features suffices.

4. **Define the ranking label and objective.** Choose the training label(s) and whether ranking is pointwise/pairwise/listwise. Flag where the proxy label diverges from the business goal (hand off depth to `recsys_objective_business_alignment.md`).

5. **Enforce train/serve parity.** Specify the shared feature transform path and identify any feature whose offline value could differ from its online value (a classic source of train/serve skew).

6. **Add the re-rank/policy handoff.** Specify diversity, freshness, dedup, and exploration applied after scoring, so the ranker isn't asked to encode product rules implicitly.

7. **Define stage-wise evaluation.** Measure retrieval (Recall@K, coverage) and ranking (NDCG/MAP@K) separately so a failure is attributable to the right stage, and note the offline→online gap.

**Output Format:**

A markdown design:
- **Stage Budget** — candidate-set size, latency split, QPS.
- **Retrieval Design** — table: Retriever | Signal | Coverage Role | Recall Target.
- **Ranking Design** — model class, feature groups, label, objective form.
- **Train/Serve Parity** — shared transform path + at-risk features.
- **Re-Rank / Policy** — diversity, freshness, exploration rules.
- **Stage-Wise Evaluation** — retrieval and ranking metrics, plus offline→online note.

## Verification

- [ ] Both stages are specified, with an explicit candidate-set size handed from retrieval to ranking.
- [ ] Retrieval recall (including cold/long-tail coverage) is a stated target, not just ranking precision.
- [ ] The ranking label/objective is named and its proxy risk acknowledged.
- [ ] Train/serve parity is addressed with specific at-risk features called out.
- [ ] Retrieval and ranking are evaluated with distinct metrics.
- [ ] No fabricated metric numbers; unknowns are marked.

## False-Positive Prevention

❌ **DON'T:**
- Tune NDCG@10 while retrieval recall is 40% — the ranker physically cannot surface items retrieval missed.
- Add a feature that's trivial to compute in a batch job but isn't available within the online latency budget.
- Assume a single embedding retriever covers the catalog — it typically misses cold items and exact-match intent.
- Let the ranker learn diversity implicitly when a deterministic re-rank rule is clearer and controllable.

✅ **DO:**
- Diagnose recall vs precision first — a low Recall@K caps achievable ranking quality regardless of the model.
- Use complementary retrievers so cold, long-tail, and intent-specific items all reach the ranker.
- Verify every ranking feature is computed by the *same code path* offline and online (train/serve parity).
- Evaluate retrieval and ranking separately so you fix the stage that's actually broken.

## Example Output

```markdown
## Two-Stage Design: Video "Up Next" Recommendations

### Stage Budget
Catalog ~50M videos, p99 budget 100ms. Retrieval → 800 candidates; ranker scores 800 in ~30ms. Latency split: retrieval 25ms, ranking 35ms, policy 10ms.

### Retrieval Design
| Retriever | Signal | Coverage Role | Recall Target |
|---|---|---|---|
| Co-watch ANN | session co-engagement embeddings | head/known intent | Recall@800 >= 0.65 |
| Content ANN | title/transcript/topic embeddings | cold + long-tail | covers <7-day items |
| Recency/trending | time-decayed popularity | freshness, fallback | fills slate |

### Ranking Design
Model: gradient-boosted ranker (50M/day events supports it; no deep ranker yet).
Feature groups: user (watch history embedding, topic affinities), item (length, age, quality), context (time, device, prior video), cross (user-topic × item-topic match).
Label: weighted watch-time + completion (pairwise objective). Proxy risk: optimizing watch-time alone may favor clickbait — see objective alignment prompt.

### Train/Serve Parity
Shared feature transform library used by both the training job and the online scorer. At-risk: "trending score" — must be snapshotted at request time offline to match online; otherwise leaks future popularity.

### Re-Rank / Policy
Diversity cap (max 2 per creator), dedup already-watched, 1 exploration slot for under-exposed fresh items.

### Stage-Wise Evaluation
Retrieval: Recall@800, cold-item coverage. Ranking: NDCG@10, watch-time-weighted MAP. Offline→online gap: labels biased by current "Up Next" — confirm via A/B; offline NDCG overstates a new ranker.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** budget → retrieval → ranking → label → parity → policy → eval.
- **RT-02 (Multi-Dimensional Analysis Framework):** balances recall, precision, latency, and coverage.
- **DS-02 (Metric Specification):** distinct retrieval (Recall@K) and ranking (NDCG/MAP) metrics.
- **CM-02 (Constraint Specification):** the latency budget fixes the stage budget and feature choices.
- **DS-06 (Prioritization & Severity Guidance):** diagnose the limiting stage (recall vs precision) before optimizing.

**Related Prompts:**
- `recsys_architecture_design.md` — the architecture this two-stage pipeline implements.
- `recsys_offline_evaluation.md` — how to evaluate this pipeline and reason about the online gap.
- `recsys_objective_business_alignment.md` — resolving the ranking-label proxy risk flagged here.
