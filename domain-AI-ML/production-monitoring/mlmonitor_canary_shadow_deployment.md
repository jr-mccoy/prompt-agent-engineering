---
title: "ML Canary & Shadow Deployment Design"
category: AI-ML/production-monitoring
description: "Design canary and shadow deployments to de-risk model releases — what to compare, against which baseline, with what promotion and abort criteria — before a new model takes full traffic."
techniques:
  - ST-02
  - RT-02
  - DS-02
  - CM-02
  - QA-12
difficulty: advanced
tags:
  - canary
  - shadow-deployment
  - rollout
  - ab-testing
  - release-safety
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/production-monitoring/mlmonitor_rollback_strategy.md
  - domain-AI-ML/production-monitoring/mlmonitor_retraining_trigger_strategy.md
  - domain-AI-ML/production-monitoring/mlmonitor_slo_design_for_ml.md
---

# ML Canary & Shadow Deployment Design

**Objective:** Design a staged rollout for a new model version using shadow deployment (mirror traffic, no user impact) and canary deployment (small live traffic slice) — specifying which signals are compared against which baseline, the sample sizes and durations needed for trustworthy comparison, and the promotion and abort criteria — so a release is de-risked by evidence rather than hope before it serves all traffic.

**When to Use:**
- Promoting a retrained or rearchitected model and you want to catch regressions before full exposure.
- A past release caused a production regression that offline evaluation missed.
- Designing the standard release path for a model that ships frequently.

**When NOT to Use:**
- To design the rollback mechanism a failed canary triggers (use `mlmonitor_rollback_strategy.md`).
- To decide whether to retrain in the first place (use `mlmonitor_retraining_trigger_strategy.md`).
- For offline model selection before any deployment (that belongs in model-evaluation prompts).

## Inputs / Context

Provide what you can:
- **Candidate vs incumbent** — what changed (data, features, architecture, hyperparameters).
- **Label latency** — immediate, delayed, or none (decides whether canary judges live quality or proxies).
- **Traffic volume** — requests/period, so canary slices reach statistical power in a tolerable time.
- **Risk profile** — blast radius of a bad model (user-facing, money, safety).
- **Comparison signals** — quality metrics, business KPIs, operational metrics, prediction-distribution stats.
- **Infra capabilities** — can you mirror traffic (shadow)? split traffic deterministically by user? roll back fast?

## Constraints

**Must:**
- Use shadow to validate correctness/operational behavior without user impact, and canary to validate live quality/business impact on a small slice — and state what each stage can and cannot prove.
- Compare the candidate against a concurrent incumbent baseline (same time window, same traffic mix), not against a historical number.
- Define promotion and abort criteria as thresholds with sample-size/duration requirements and intervals — not "looks good."

**Must Not:**
- Declare a canary "winning" from a difference that is within noise for the sample collected (require power/intervals).
- Judge live quality from a shadow stage when labels are delayed and shadow predictions are never acted on (no outcomes to score).
- Compare candidate canary metrics to a stale historical baseline instead of the concurrent control slice.

**Instructions:**

1. **Define the release goal and risk.** State what the candidate must prove (no quality regression, a target lift, lower latency) and the blast radius if it fails — this calibrates slice size and stage durations.

2. **Design the shadow stage.** Mirror production traffic to the candidate without serving its outputs. Compare candidate vs incumbent on: operational behavior (latency, errors, resource use), prediction-distribution agreement, and disagreement-rate analysis. State explicitly that shadow cannot measure outcome-based quality when actions aren't taken.

3. **Design the canary stage.** Route a small, representative live slice (deterministic by user/session to avoid contamination) to the candidate, holding a concurrent control slice on the incumbent. Specify the slice size and how it scales up across phases.

4. **Choose comparison metrics by label latency.** With fast labels: live quality + business KPI vs control. With delayed/no labels: proxy and guardrail metrics (prediction-distribution health, engagement leading indicators, operational SLIs), and defer the quality verdict to a post-promotion holdout.

5. **Size for statistical power.** For each compared metric, state the minimum sample/duration to detect the effect you care about with intervals, accounting for traffic volume and metric variance. Guard against peeking-driven false positives (use a fixed horizon or sequential testing).

6. **Set promotion criteria.** Define the bar to advance each phase and to full traffic: candidate is non-inferior (or superior) on primary metrics with intervals, no guardrail breached, no segment regressing beyond tolerance.

7. **Set abort/rollback criteria.** Define the thresholds that immediately halt the rollout and revert traffic (operational SLO breach, guardrail metric breach, quality regression beyond tolerance), linking to the rollback strategy.

8. **Plan post-promotion validation.** For delayed-label cases, specify the holdout/back-evaluation that confirms the quality verdict once labels mature, and how a late-discovered regression is handled.

**Output Format:**

A markdown rollout design:
- **Release Goal & Risk** — what must be proven, blast radius
- **Shadow Stage Plan** — comparisons, what it proves / can't prove
- **Canary Phase Plan** — table: Phase | Traffic % | Duration | Min Sample | Primary Metrics | Guardrails
- **Metric Selection by Label Latency** — what is judged when
- **Promotion Criteria** — thresholds + intervals per phase
- **Abort / Rollback Criteria** — breach conditions → action
- **Post-Promotion Validation** — delayed-label confirmation plan

## Verification

- [ ] Shadow and canary roles are distinguished, with what each can and cannot prove stated.
- [ ] Candidate is compared to a concurrent control slice, not a historical baseline.
- [ ] Each comparison metric has a sample-size/duration requirement and uses intervals.
- [ ] Metric choice is adapted to label latency (proxies vs live quality).
- [ ] Promotion and abort criteria are explicit thresholds, not judgment calls.
- [ ] Delayed-label cases have a post-promotion validation plan.

## False-Positive Prevention

❌ **DON'T:**
- Promote because the canary's metric is higher when the difference is inside the confidence interval.
- Claim a shadow run validated quality when its predictions were never acted on and labels are delayed.
- Compare the canary slice to last month's incumbent numbers instead of the concurrent control.
- Peek repeatedly and stop the canary the first hour it looks good (multiple-comparisons inflation).

✅ **DO:**
- Require non-inferiority/superiority with intervals on a powered sample before promoting.
- Use shadow for operational + prediction-agreement checks; reserve outcome-quality for canary/holdout.
- Hold a concurrent control slice for apples-to-apples comparison.
- Fix the evaluation horizon (or use sequential tests) to control false-positive promotions.

## Example Output

```markdown
## Rollout Design: Recommendation Ranker v8 (new architecture)

### Release Goal & Risk
- Prove: non-inferior CTR, ≤ incumbent latency, no segment CTR regression >1%. Blast radius: user-facing, no money — SEV-2 if it fails.

### Shadow Stage Plan
- Mirror 100% traffic to v8 for 48h. Compare: p95 latency, error rate, prediction-rank agreement vs v7, top-k disagreement rate. Proves operational safety + behavioral sanity. Cannot prove CTR (no served outputs).

### Canary Phase Plan
| Phase | Traffic | Duration | Min Sample | Primary | Guardrails |
|---|---|---|---|---|---|
| 1 | 5% | 48h | 400k sessions | CTR vs control | p95 latency, error rate |
| 2 | 25% | 72h | 2M sessions | CTR + dwell vs control | latency, per-segment CTR |
| Full | 100% | — | — | — | continuous monitoring |

### Metric Selection by Label Latency
- Clicks are near-real-time → CTR judged live in canary vs concurrent 5%/25% control. Dwell-time matures ~1d → confirmed at phase end.

### Promotion Criteria
- Advance: CTR non-inferior (95% CI lower bound > -0.5%), no guardrail breach, no segment CTR -1% (CI). Phase 2 → full also requires CTR CI excludes 0 on the downside.

### Abort / Rollback Criteria
- Immediate revert if: p95 latency >300ms (5 min), error rate >1%, or CTR -3% (CI) at any phase. → invoke rollback strategy.

### Post-Promotion Validation
- 7-day back-evaluation on dwell-time and downstream conversion once matured; rollback path stays warm for 7 days.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** shadow → canary phases → promotion/abort sequence.
- **RT-02 (Multi-Dimensional Analysis Framework):** balances quality, business, operational, and segment signals.
- **DS-02 (Metric Specification):** every comparison names metric, baseline, sample size, and interval.
- **CM-02 (Constraint Specification):** concurrent-control and power requirements constrain promotion claims.
- **QA-12 (False Positives Identification):** guards against noise-driven and peeking-driven false promotions.

**Related Prompts:**
- `mlmonitor_rollback_strategy.md` — the revert path a failed canary triggers.
- `mlmonitor_retraining_trigger_strategy.md` — produces the candidate this rollout de-risks.
- `mlmonitor_slo_design_for_ml.md` — the operational SLOs the guardrails enforce.
```