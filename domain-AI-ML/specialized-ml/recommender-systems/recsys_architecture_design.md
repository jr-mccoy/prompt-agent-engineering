---
title: "Recommender System Architecture Design"
category: AI-ML/specialized-ml/recommender-systems
description: "Design an end-to-end recommender (retrieval + ranking, content/collaborative/hybrid) matched to the use case, data, scale, and latency budget."
techniques:
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - DS-06
difficulty: advanced
tags:
  - recommender-systems
  - architecture
  - retrieval-ranking
  - collaborative-filtering
  - hybrid
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/specialized-ml/recommender-systems/recsys_candidate_ranking_design.md
  - domain-AI-ML/specialized-ml/recommender-systems/recsys_cold_start_strategy.md
  - domain-AI-ML/specialized-ml/recommender-systems/recsys_objective_business_alignment.md
---

# Recommender System Architecture Design

**Objective:** Produce a concrete, justified architecture for a recommender system — choosing the algorithmic family (content-based, collaborative, hybrid), the stage structure (single-stage vs retrieval + ranking), the data/feature sources, and the serving path — fitted to the use case, catalog/user scale, latency budget, and the realities of the available interaction data.

**When to Use:**
- Standing up a recommender from scratch and choosing an approach.
- Re-architecting an existing recommender that doesn't scale or doesn't serve well.
- Deciding between buying/managed vs building, or between collaborative and content-based given sparse data.

**When NOT to Use:**
- When the architecture is fixed and you only need the two-stage internals (use `recsys_candidate_ranking_design.md`).
- For a pure offline metric comparison of trained models (use `recsys_offline_evaluation.md`).
- For aligning the training target to the business metric (use `recsys_objective_business_alignment.md`).

## Inputs / Context

Provide what you can; the design degrades gracefully if some are missing:
- **Use case & surface** — homepage feed, "more like this", search re-rank, email digest, notifications; one item or a slate.
- **Scale** — number of users, number of items (catalog size), interactions/day, item churn rate (how fast new items appear).
- **Interaction data** — explicit (ratings) vs implicit (clicks, plays, purchases, dwell); density/sparsity; presence of strong popularity skew.
- **Item/user metadata** — content features available (text, image, category, attributes) and side information.
- **Constraints** — latency budget (p99 for the surface), QPS, freshness requirement, infra/team maturity, privacy/compliance limits.
- **Business objective** — what success means (engagement, conversion, retention, diversity/discovery).

## Constraints

**Must:**
- Tie every architectural choice to a specific input (scale, sparsity, latency, freshness) — no default-pattern recommendations without justification.
- State which algorithmic family fits and why, including when a simple popularity/content baseline is the right first version.
- Specify the serving path explicitly: how candidates are produced under the latency budget (e.g., ANN index, precompute, online scoring).

**Must Not:**
- Recommend deep collaborative models when interaction data is too sparse to support them — say so and route to content/hybrid.
- Fabricate metric or latency numbers; reason from the user's stated scale and mark unknowns as open questions.
- Ignore the offline→online gap or cold start — both must be named as design forces even if detailed elsewhere.

**Instructions:**

1. **Frame the recommendation problem.** State what is being recommended to whom, on which surface, the slate size, and the dominant business objective. Distinguish "predict rating" from "rank a slate" from "retrieve candidates" — these drive different architectures.

2. **Characterize the data regime.** Classify interaction data as explicit/implicit, dense/sparse, and popularity-skewed or not. Establish whether collaborative signal is strong enough to carry the system, or whether content features must do the heavy lifting (sparse data, high item churn).

3. **Select the algorithmic family.** Map the regime to candidates: content-based (rich metadata, cold-heavy catalog), collaborative (dense interactions, stable catalog), or hybrid (the common production answer). Justify against the inputs; name the simplest viable baseline first.

4. **Decide the stage structure.** For large catalogs, separate retrieval (cheap recall over millions of items) from ranking (expensive precision over hundreds). For small catalogs, a single ranking pass may suffice. Tie the decision to catalog size and latency.

5. **Design the serving path.** Specify how candidates are produced within the latency budget — precomputed lists, ANN/embedding index, online feature lookup, real-time scoring — and where freshness enters (new items, new interactions).

6. **Name the cross-cutting forces.** Explicitly account for cold start, the offline→online gap, and feedback-loop/popularity bias as design constraints, with a pointer to where each is handled in depth.

7. **Stage the build.** Sequence v0 (baseline that ships), v1 (the chosen family), v2 (refinements), with the metric/gate that justifies advancing.

**Output Format:**

A markdown design document:
- **Problem Frame** — surface, slate, objective, data regime in one paragraph.
- **Architecture Decision** — table: Decision | Choice | Driving Input | Rationale.
- **Recommended Architecture** — staged diagram-in-prose: retrieval → ranking → serving, with data sources.
- **Cross-Cutting Risks** — cold start, offline→online gap, feedback loop, with where each is addressed.
- **Phased Rollout** — v0 / v1 / v2 with advancement gates.
- **Open Questions** — unknowns that change the design if answered.

## Verification

- [ ] Every architectural choice cites a specific input (scale, sparsity, latency, freshness).
- [ ] The algorithmic family selection explicitly considers data sparsity and item churn.
- [ ] A simple baseline (popularity/content) is named as the first shippable version.
- [ ] The serving path is concrete enough to estimate feasibility under the stated latency budget.
- [ ] Cold start, offline→online gap, and feedback-loop bias are each named as design forces.
- [ ] No latency/metric numbers are asserted as fact without being grounded in the user's inputs.

## False-Positive Prevention

❌ **DON'T:**
- Default to a two-tower / deep collaborative model because it is fashionable, when the catalog is small or interactions are sparse.
- Assume a complex architecture beats a popularity baseline — for many surfaces it does not, especially early.
- Treat offline ranking quality as a promise of online lift; they routinely diverge.
- Pick retrieval + ranking for a 5,000-item catalog where a single scoring pass is simpler and sufficient.

✅ **DO:**
- Match the algorithmic family to the data regime: sparse/high-churn → content or hybrid; dense/stable → collaborative.
- Recommend the simplest architecture that meets the latency budget, and earn complexity with measured lift.
- Flag cold start and feedback loops as first-class design forces, not afterthoughts.
- Tie stage structure (single vs two-stage) to catalog size and the p99 latency budget, not to convention.

## Example Output

```markdown
## Recommender Architecture: Marketplace Homepage Feed

### Problem Frame
Rank a personalized slate of ~30 listings on the homepage for 4M monthly users over a 1.2M-item catalog with ~15% weekly item churn. Implicit signals only (clicks, saves, purchases), heavy popularity skew. Objective: purchase conversion, with a guardrail on discovery. p99 budget: 120 ms.

### Architecture Decision
| Decision | Choice | Driving Input | Rationale |
|---|---|---|---|
| Stage structure | Two-stage (retrieval + ranking) | 1.2M catalog, 120 ms p99 | Cannot score 1.2M items online; recall cheaply, rank precisely |
| Algorithmic family | Hybrid (collaborative retrieval + content-aware ranker) | Sparse-ish implicit + 15% churn | Collaborative for known items; content features carry new items |
| Retrieval | ANN over item embeddings + popularity backfill | Latency + cold items | Embedding recall fast; popularity covers cold/sparse users |
| Ranking | Gradient-boosted ranker on user/item/context features | Need precision on ~500 candidates | Strong tabular baseline, cheap to serve |
| Freshness | Hourly embedding refresh; content features at ingest | 15% weekly churn | New items rankable immediately via content path |

### Recommended Architecture
v0 served popularity-by-segment (shipped, set the baseline). v1: retrieval = ANN over collaborative item embeddings unioned with content-similarity for cold items and a popularity backfill to fill the slate; ranking = GBDT scoring ~500 candidates on user history, item content, and context (time, device). Serving: precompute user embedding nightly + on-session update; ANN index in memory; ranker scores online within budget.

### Cross-Cutting Risks
- **Cold start** — new items enter via the content-similarity retrieval path; see `recsys_cold_start_strategy.md`.
- **Offline→online gap** — GBDT NDCG gains must be confirmed by A/B; see `recsys_offline_evaluation.md`.
- **Feedback loop / popularity bias** — popularity backfill risks rich-get-richer; add an exploration slot; see `recsys_feedback_loop_bias_audit.md`.

### Phased Rollout
- v0: popularity-by-segment (done) — sets conversion baseline.
- v1: hybrid retrieval + GBDT ranker — gate: +X% conversion in A/B with no discovery regression.
- v2: sequence-aware ranker + learned exploration — gate: incremental A/B lift over v1.

### Open Questions
- Actual interaction density per user (changes whether collaborative retrieval is viable for the long tail).
- Is dwell/save reliably logged? (enables a richer ranking objective).
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** frame → data regime → family → stages → serving proceeds in a fixed order.
- **RT-02 (Multi-Dimensional Analysis Framework):** choices are weighed across scale, sparsity, latency, and freshness.
- **DS-01 (Framework Application):** applies the retrieval-and-ranking recsys reference pattern.
- **CM-02 (Constraint Specification):** the latency budget and catalog scale are governing constraints.
- **DS-06 (Prioritization & Severity Guidance):** phased rollout sequences complexity by earned lift.

**Related Prompts:**
- `recsys_candidate_ranking_design.md` — design the internals of the two-stage system chosen here.
- `recsys_cold_start_strategy.md` — handle new users/items the architecture must support.
- `recsys_objective_business_alignment.md` — make sure the ranker optimizes the right thing.
