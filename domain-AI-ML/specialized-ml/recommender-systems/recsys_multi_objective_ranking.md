---
title: "Multi-Objective Ranking Design"
category: AI-ML/specialized-ml/recommender-systems
description: "Balance relevance against diversity, revenue, freshness, and fairness in a single ranker — choose between scalarization (weighted sum), constrained optimization, and Pareto methods, select and validate objective weights, and install guardrail metrics that catch silent degradation."
techniques:
  - ST-02
  - RT-02
  - CM-02
  - DS-06
  - QA-01
difficulty: advanced
tags:
  - recommender-systems
  - multi-objective
  - ranking
  - diversity
  - guardrail-metrics
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/specialized-ml/recommender-systems/recsys_objective_business_alignment.md
  - domain-AI-ML/specialized-ml/recommender-systems/recsys_candidate_ranking_design.md
  - domain-AI-ML/specialized-ml/recommender-systems/recsys_offline_evaluation.md
---

# Multi-Objective Ranking Design

**Objective:** Help the user design a ranking layer that optimizes more than one objective at once — typically relevance plus some mix of diversity, revenue, freshness, and fairness — without letting any single goal quietly cannibalize the others. The aim is to enumerate the real objectives and their business priority, choose a combination method (scalarization via weighted sum, hard/soft constrained optimization, or Pareto-frontier selection) appropriate to how the objectives trade off, decide how weights or constraints are set and *validated*, and install guardrail metrics and an online test design so that an apparent win on one metric is never accepted while a load-bearing metric silently regresses.

**When to Use:**
- A single-objective ranker (pure relevance) is producing side effects: filter bubbles, revenue leakage, stale content, or fairness complaints.
- Stakeholders disagree on what "good" means and you need to make the tradeoff explicit and tunable.
- You can measure several objectives offline and have an online experimentation channel to validate weight choices.

**When NOT to Use:**
- You have not yet established which business objective the recommender serves at all — start with `recsys_objective_business_alignment.md`.
- You are designing candidate generation and base scoring rather than re-ranking — see `recsys_candidate_ranking_design.md`.
- You only need a single-metric offline harness — see `recsys_offline_evaluation.md`.

## Inputs / Context

Provide what you can:
- **Objective list** — every goal in play (relevance, diversity, revenue, freshness, fairness, etc.) and which are primary vs. secondary.
- **Per-objective metrics** — how each objective is measured today (e.g. NDCG, intra-list diversity, GMV/CTR, content age, exposure parity).
- **Business priority / non-negotiables** — which objectives are guardrails that must not regress vs. which can be traded.
- **Current ranker** — what it optimizes now and known side effects.
- **Experimentation capability** — A/B or interleaving availability and minimum detectable effect.
- **Constraints** — latency budget, regulatory/fairness requirements, inventory or contract obligations.
- **Time horizon of interest** — whether short-term (session CTR/revenue) or long-term (retention) is the true target.

## Constraints

**Must:**
- Make every objective and its measurement explicit, and label each as primary, secondary, or guardrail.
- Choose the combination method (scalarization, constrained optimization, Pareto) based on how the objectives actually trade off, not by default.
- Define guardrail metrics with regression thresholds before tuning any weights.
- Validate weights/constraints through an online experiment, not a single offline metric.

**Must Not:**
- Tune objective weights to maximize one offline metric (e.g. revenue) without simultaneously reporting the others.
- Treat a weighted sum as obviously correct when objectives are on different scales or in genuine conflict — normalize and justify.
- Fabricate offline/online metric numbers or tradeoff curves from memory; reason from the user's data and mark unknowns.
- Optimize a short-term proxy (clicks) as if it equals the long-term goal (retention) without flagging the gap.

**Instructions:**

1. **Enumerate and rank objectives.** List each objective, how it is measured, and its priority (primary / secondary / guardrail). Surface conflicts (e.g. diversity vs. relevance, revenue vs. retention) explicitly.
2. **Pin the true target and horizon.** Identify which objective the business actually cares about long-term and which metrics are proxies; note where a proxy can move opposite the true goal.
3. **Choose a combination method.** Map the objectives to: weighted-sum scalarization (objectives roughly comparable, smooth tradeoff), constrained optimization (some objectives are hard floors/ceilings), or Pareto-frontier selection (you want to inspect the tradeoff surface before committing). Justify the pick.
4. **Normalize and scale.** If using a weighted sum, define how each objective is normalized so weights are interpretable and not dominated by scale.
5. **Set weights/constraints with a method, not a guess.** Describe how initial weights or constraint thresholds are chosen (stakeholder priority, target operating point on the Pareto frontier, or grid search) and how they will be revisited.
6. **Define guardrail metrics and thresholds.** For every objective that must not regress, set an explicit regression threshold (e.g. "revenue may rise but CTR must not drop > 0.5%, exposure parity must stay within band").
7. **Design offline analysis + online validation.** Specify the offline tradeoff analysis (frontier or weight sweep) and the online A/B/interleaving test, including which guardrails halt the rollout.
8. **Plan monitoring for silent degradation.** State which metrics are tracked post-launch so a later drift on a non-optimized objective is caught.

**Output Format:**

A markdown ranking-design brief:
- **Objective Inventory** — each objective, metric, priority label, known conflicts.
- **True Target & Horizon** — long-term goal vs. proxies, mismatch warnings.
- **Combination Method** — chosen approach and rationale.
- **Normalization Plan** — scaling/normalization for comparability.
- **Weight / Constraint Strategy** — how values are set and revisited.
- **Guardrail Metrics** — metric list with explicit regression thresholds.
- **Offline + Online Validation** — tradeoff analysis and experiment design.
- **Monitoring Plan** — post-launch drift detection.
- **Open Questions / Unknowns** — values to measure on the user's data.

## Verification

- [ ] Every objective is listed with its metric and a primary/secondary/guardrail label.
- [ ] The combination method is justified by how the objectives trade off.
- [ ] Guardrail metrics with explicit regression thresholds are defined before weight tuning.
- [ ] Weights/constraints are validated online, not on a single offline metric.
- [ ] Short-term proxies are distinguished from the long-term target.
- [ ] No offline/online metric numbers or tradeoff curves are invented — all are to be measured on the user's data.

## False-Positive Prevention

❌ **DON'T:**
- Tune the weighted sum to maximize revenue and declare success while long-term retention or CTR silently degrades (optimizing one metric while quietly hurting others).
- Pick objective weights by eyeballing a single offline metric without guardrails or a Pareto view.
- Sum objectives on raw, differently-scaled values so one objective dominates by accident.
- Accept a short-term click lift as proof the long-term goal improved.

✅ **DO:**
- Report every objective's movement together for any weight setting, and require guardrails to hold.
- Set regression thresholds for load-bearing metrics before tuning, and treat a breach as a rollout stop.
- Normalize objectives so weights express real priority, and inspect the Pareto frontier when tradeoffs are sharp.
- Validate the chosen operating point with an online test and monitor for delayed degradation on non-optimized objectives.

## Example Output

```markdown
## Multi-Objective Ranking — Home Feed

**Objective Inventory:**
- Relevance (NDCG@10) — primary.
- Intra-list diversity (category entropy) — secondary.
- Revenue (sponsored GMV) — secondary.
- Freshness (median content age) — guardrail (must not exceed +20%).
- Creator exposure parity — guardrail (Gini within band).
Conflicts: relevance vs. diversity; revenue vs. long-term retention.

**True Target & Horizon:** Long-term = 28-day retention. Proxy = session CTR (can move
opposite retention; flagged).

**Combination Method:** Constrained scalarization — weighted sum of relevance + diversity
+ revenue, with freshness and parity as hard constraints. Justified: two objectives are
floors, not tradeable.

**Normalization Plan:** Min-max each objective on a rolling window before weighting.

**Weight / Constraint Strategy:** Initial weights from stakeholder priority; sweep on a
held-out window; revisit quarterly.

**Guardrail Metrics:** CTR drop ≤ 0.5%; freshness +≤20%; parity Gini ≤ 0.35; 28-day
retention non-inferior.

**Offline + Online Validation:** Offline weight sweep → Pareto view; online A/B, guardrail
breach halts rollout.

**Monitoring Plan:** Daily dashboard on all six objectives + retention cohort tracking.

**Open Questions:** Measure actual relevance–diversity tradeoff curve; confirm CTR↔retention
sign on the user's data.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** Drives the flow from objective enumeration through monitoring.
- **RT-02 (Multi-Dimensional Analysis Framework):** Forces the tradeoff between combination methods and competing objectives to be made explicit.
- **CM-02 (Constraint Specification):** Encodes guardrails, no-fabrication, and the weighted-sum cautions.
- **DS-06 (Prioritization & Severity Guidance):** Brings the Pareto/weight-sweep reasoning to the surface for decision-making.
- **QA-01 (Self-Verification):** Installs guardrail metrics and thresholds that catch silent degradation.

**Related Prompts:**
- `recsys_objective_business_alignment.md` — establishing which business objective the recommender serves.
- `recsys_candidate_ranking_design.md` — candidate generation and base scoring upstream of re-ranking.
- `recsys_offline_evaluation.md` — the offline metric harness the tradeoff analysis depends on.
