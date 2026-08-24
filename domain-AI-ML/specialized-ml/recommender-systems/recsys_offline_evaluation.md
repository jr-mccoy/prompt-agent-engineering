---
title: "Recommender Offline Evaluation & the Offline→Online Gap"
category: AI-ML/specialized-ml/recommender-systems
description: "Evaluate a recommender offline with appropriate ranking metrics and beyond-accuracy measures, and reason rigorously about why offline gains may not translate to online lift due to logged-data bias."
techniques:
  - ST-02
  - DS-02
  - QA-17
  - QA-12
  - RT-05
difficulty: advanced
tags:
  - recommender-systems
  - offline-evaluation
  - ranking-metrics
  - offline-online-gap
  - selection-bias
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/specialized-ml/recommender-systems/recsys_candidate_ranking_design.md
  - domain-AI-ML/specialized-ml/recommender-systems/recsys_feedback_loop_bias_audit.md
  - domain-AI-ML/specialized-ml/recommender-systems/recsys_objective_business_alignment.md
---

# Recommender Offline Evaluation & the Offline→Online Gap

**Objective:** Design and interpret an offline evaluation for a recommender — selecting ranking and beyond-accuracy metrics, building a time-honest evaluation set, choosing the right baselines — and, critically, reason about the offline→online gap: why metrics computed on logged data biased by the incumbent recommender often fail to predict online A/B lift.

**When to Use:**
- Comparing recommender candidates before an A/B test, to decide what's worth shipping to traffic.
- Offline metrics improved but the online A/B showed no lift (or a regression) — diagnosing why.
- Establishing an offline evaluation protocol the team can trust as a gate.

**When NOT to Use:**
- Designing the retrieval/ranking stages themselves (use `recsys_candidate_ranking_design.md`).
- Auditing systemic popularity/position/feedback bias as a phenomenon (use `recsys_feedback_loop_bias_audit.md`).
- Choosing the online objective (use `recsys_objective_business_alignment.md`).

## Inputs / Context

Provide what you can:
- **Logged interaction data** — exposures and outcomes (clicks/purchases/dwell), and crucially *what was shown* (the incumbent's recommendations), with timestamps.
- **Candidate models** — what's being compared, and against which baseline (popularity, prior model, random).
- **Online metric** — the business metric the A/B will move (so offline metrics can be chosen to correlate).
- **Position/exposure logging** — is the rank position of each impression recorded? (needed to reason about position bias).
- **Constraints** — class imbalance, slate size, cold-item share, time span of logs.

## Constraints

**Must:**
- Use a time-respecting (temporal) evaluation split, not a random one, for any sequential/temporal recommender.
- Report ranking metrics with a named baseline and acknowledge confidence (variance across folds/time windows).
- Explicitly reason about the offline→online gap: the logged data only contains outcomes for items the incumbent chose to show.

**Must Not:**
- Treat an offline NDCG/Recall improvement as a prediction of online lift — state the gap and its causes.
- Compute metrics only on impressed items as if they represented the full action space (survivorship/exposure bias).
- Fabricate metric values or claim a lift magnitude; reason from the user's logs and mark unknowns.

**Instructions:**

1. **Pin the evaluation question.** State exactly what the offline eval is meant to decide (ship to A/B? pick between two rankers?) and the online metric it must predict.

2. **Build a time-honest eval set.** Split by time (train on past, evaluate on future), respecting any session/temporal order. Verify no leakage of future interactions into features.

3. **Select metrics deliberately.** Choose ranking metrics (Recall@K, Precision@K, NDCG@K, MAP, MRR) appropriate to the surface, plus beyond-accuracy metrics (coverage, diversity, novelty) and, if probabilities are consumed, calibration. Justify each against the surface and objective.

4. **Set baselines.** Always compare to a meaningful baseline — popularity, most-recent, prior production model — never to nothing. Report relative, not just absolute, numbers.

5. **Quantify uncertainty.** Report variance across time windows or folds; a single-number improvement without a sense of noise is not decision-grade.

6. **Diagnose the offline→online gap.** Identify the biases in the logged data: selection/exposure bias (only shown items have labels), position bias (higher slots get more clicks regardless of relevance), and distribution shift. State how each could make offline metrics mislead.

7. **Recommend gap-mitigations and the A/B plan.** Where feasible, propose counterfactual/IPS-style estimators or unbiased evaluation slices, and specify that the offline result is a *gate to* an A/B, not a substitute for it.

**Output Format:**

A markdown evaluation report:
- **Evaluation Question** — what this decides and the target online metric.
- **Eval Set Construction** — time split + leakage check.
- **Metric Scorecard** — table: Metric | Model | Baseline | Δ | Variance.
- **Beyond-Accuracy** — coverage / diversity / novelty / calibration as relevant.
- **Offline→Online Gap Analysis** — selection bias, position bias, shift, each with its mislead-risk.
- **Recommendation** — ship-to-A/B or not, the A/B metric and guardrails.

## Verification

- [ ] The eval split respects time order (for any temporal/sequential recommender).
- [ ] Every ranking metric is reported against a named baseline, not in isolation.
- [ ] Uncertainty/variance is reported, not just point estimates.
- [ ] Selection bias, position bias, and distribution shift are each addressed in the gap analysis.
- [ ] The report states that offline is a gate to A/B, not a replacement.
- [ ] No fabricated metric values or claimed lift magnitudes.

## False-Positive Prevention

❌ **DON'T:**
- Read a higher offline NDCG as "this model will win the A/B" — logged labels favor whatever the incumbent already showed.
- Use a random train/test split on session/time-ordered data (it leaks future behavior into evaluation).
- Compute precision only over impressed items and call it the model's true precision (you never observed the un-shown items).
- Report a single improvement number with no variance and gate a launch on it.

✅ **DO:**
- Attribute the offline→online gap to concrete mechanisms: exposure bias, position bias, distribution shift — and say which dominates here.
- Pair accuracy metrics with coverage/diversity so a model that just re-serves the popular head isn't mistaken for "better."
- Report variance across time windows so noise isn't mistaken for signal.
- Treat the strongest offline result as a hypothesis to confirm in an A/B, with guardrail metrics attached.

## Example Output

```markdown
## Offline Evaluation: Ranker v4 vs Production v3 — Music Home

### Evaluation Question
Should v4 graduate to an A/B? Target online metric: 30-day listening minutes per user.

### Eval Set Construction
Temporal split: train through Apr 30, evaluate May 1–14 sessions. Leakage check: rolling features use only pre-impression windows; no future plays in features. Clean.

### Metric Scorecard
| Metric | v4 | v3 (baseline) | Δ | Variance (across 14 days) |
|---|---|---|---|---|
| Recall@50 | 0.41 | 0.38 | +0.03 | ±0.015 |
| NDCG@10 | 0.052 | 0.049 | +0.003 | ±0.004 (overlaps zero) |
| MAP@20 | 0.071 | 0.068 | +0.003 | ±0.003 |

### Beyond-Accuracy
Catalog coverage: v4 0.22 vs v3 0.19 (v4 surfaces more of the catalog — good). Intra-list diversity: roughly equal. Novelty: v4 slightly higher.

### Offline→Online Gap Analysis
- Selection bias (HIGH): labels exist only for tracks v3 chose to show; v4 recommends some never-shown tracks scored as "no engagement" → understates v4. Suggests offline UNDERstates v4.
- Position bias (MED): top-slot clicks inflate any model that agrees with v3's ordering.
- Distribution shift (LOW): two-week window, stable catalog.
Net: NDCG Δ overlaps its variance → not decision-grade alone; coverage gain + selection-bias direction argue for an A/B.

### Recommendation
Graduate v4 to a 5% A/B. Primary: 30-day listening minutes. Guardrails: catalog coverage (must not drop), skip rate, new-artist exposure. Do not ship on the offline NDCG delta alone.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** question → eval set → metrics → baselines → uncertainty → gap → recommendation.
- **DS-02 (Metric Specification):** deliberate selection of ranking and beyond-accuracy metrics.
- **QA-17 (Named Scores for Multi-Dimensional Metrics):** the metric scorecard with named, baselined scores.
- **QA-12 (False Positives Identification):** separates genuine offline gains from logged-data artifacts.
- **RT-05 (Evidence-Based Reasoning):** the offline→online gap is reasoned from the data-generating process, not asserted.

**Related Prompts:**
- `recsys_candidate_ranking_design.md` — the system whose stages this evaluation scores.
- `recsys_feedback_loop_bias_audit.md` — the biases that drive the offline→online gap, examined systemically.
- `recsys_objective_business_alignment.md` — choosing the online metric this offline eval must predict.
