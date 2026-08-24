---
title: "Offline–Online Metric Alignment"
category: AI-ML/model-evaluation-validation
description: "Diagnose and close the gap between offline evaluation metrics and online/business outcomes — finding why the model that wins on the holdout fails to move the real KPI."
techniques:
  - ST-02
  - RT-09
  - DS-02
  - CM-02
  - QA-12
difficulty: advanced
tags:
  - offline-online-gap
  - train-serve-skew
  - proxy-metrics
  - business-alignment
  - root-cause
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/model-evaluation-validation/mleval_ab_test_design_for_models.md
  - domain-AI-ML/model-evaluation-validation/mleval_metric_selection_guide.md
  - domain-AI-ML/data-for-ml/mldata_data_leakage_detector.md
---

# Offline–Online Metric Alignment

**Objective:** When an offline metric improves but the online/business outcome doesn't follow (or moves the wrong way), systematically diagnose the cause — proxy-metric mismatch, train/serve skew, distribution shift, feedback loops, or leakage — and produce a ranked set of fixes that re-couple the offline number to the outcome you actually want.

**When to Use:**
- A model that won offline shows flat or negative results in an A/B test.
- The offline metric keeps improving across launches but the north-star KPI is stagnant.
- Before trusting offline gains for a high-stakes launch, to pressure-test whether they will transfer.

**When NOT to Use:**
- You haven't yet defined the offline metric (use `mleval_metric_selection_guide.md`).
- You need to design the online experiment itself (use `mleval_ab_test_design_for_models.md`).

## Inputs / Context

Provide what you can:
- **Offline metric + value** and the evaluation setup that produced it.
- **Online/business outcome** the model is supposed to move (the north-star KPI) and observed online result.
- **Serving path** — how features are computed and the model is called in production vs. offline.
- **Time gap** — when offline data was collected vs. when the model serves; known distribution shifts.
- **Feedback loops** — does the model's output influence the data it later trains/evaluates on (recommendations, ranking)?

## Constraints

**Must:**
- Treat the offline metric as a *proxy* and explicitly test whether it is correlated with the online outcome over past launches, not assumed to be.
- Trace the feature/serving path end-to-end to surface train/serve skew (different code, timing, or data at serve time).
- Anchor each hypothesized cause to a check that would confirm or rule it out.

**Must Not:**
- Assume the offline metric is "right" and the online result is "noise" without an A/B power/duration check.
- Fabricate the offline–online correlation; if past-launch data isn't available, say the proxy validity is unestablished.
- Recommend more offline optimization before confirming the proxy actually predicts the outcome.

**Instructions:**

1. **Restate proxy vs. outcome.** Name the offline metric (the proxy) and the online outcome (the goal). State the assumed link between them in one sentence — this is the assumption under test.

2. **Validate the proxy historically.** If past launches exist, check whether offline gains historically tracked online gains. A proxy that doesn't correlate with the outcome is the root cause by itself.

3. **Check the online result's validity.** Confirm the A/B test had adequate power, duration (past novelty/primacy effects), correct unit of randomization, and no instrumentation bug — so a "no effect" is real, not under-powered.

4. **Hunt train/serve skew.** Compare offline and serving feature computation: same code path, same timing, same data freshness, same preprocessing. Skew is a top cause of offline-only wins.

5. **Check distribution shift.** Compare the offline evaluation population to the live serving population (time gap, segment mix). An offline win on stale data may not hold on current traffic.

6. **Check feedback loops and selection.** Determine whether the model's own outputs shaped the offline data (logged from a prior policy), creating offline optimism that doesn't survive deployment.

7. **Rule out leakage.** A leaked offline metric can be high and uncorrelated with reality; route to a leakage audit before concluding the proxy is merely weak.

8. **Rank causes and prescribe fixes.** Order causes by likelihood × impact; for each, give the fix (align serving code, redefine the proxy, fix randomization, off-policy correction, refresh eval data) and how to verify it.

**Output Format:**

A markdown diagnosis:
- **Proxy vs. Outcome** — the metric, the goal, the assumed link.
- **Proxy Validity** — historical correlation evidence (or "unestablished").
- **Online Validity Check** — power/duration/unit/instrumentation status.
- **Cause Hypotheses** — table: Cause | Evidence | Confirming check | Likelihood.
- **Ranked Fixes** — fix, expected effect, verification.

## Verification

- [ ] The offline metric is explicitly framed as a proxy whose link to the outcome is tested, not assumed.
- [ ] The online result's statistical validity (power/duration/unit) is checked before it's trusted.
- [ ] The serving path is compared to the offline path for train/serve skew.
- [ ] Distribution shift and feedback loops are each considered (or noted N/A with reason).
- [ ] A leakage check is invoked when the offline metric is suspiciously strong.
- [ ] Each cause carries a confirming check; none is asserted as fact prematurely.

## False-Positive Prevention

❌ **DON'T:**
- Conclude "online is just noisy" when the A/B test was under-powered or ran for two days against a weekly cycle.
- Assume the offline metric is a valid proxy without ever checking it predicted past online wins.
- Blame distribution shift while ignoring that features are computed differently in the serving code.
- Keep optimizing the offline metric when it has no demonstrated link to the business outcome.

✅ **DO:**
- Power and duration-check the online test before treating a null result as real.
- Backtest the proxy: does offline improvement historically coincide with online improvement?
- Diff the offline vs. serving feature pipelines for skew before reaching for exotic causes.
- Rule out leakage when the offline number is implausibly good — a leaked proxy explains the gap directly.

## Example Output

```markdown
## Offline–Online Diagnosis: Recommendation Ranker v9

### Proxy vs. Outcome
Proxy: offline NDCG@10 on logged clicks (+4% vs. champion). Outcome: 14-day user retention.
Assumed link: better ranking → more engagement → higher retention.

### Proxy Validity
Across last 6 launches, offline NDCG gains correlated only weakly with retention (r≈0.2).
Proxy validity is WEAK — a primary suspect on its own.

### Online Validity Check
A/B ran 21 days, user-level randomization, adequately powered for a 0.5pp retention change. Result: −0.3pp (CI crosses 0).
The null/negative result appears valid (not under-powered).

### Cause Hypotheses
| Cause | Evidence | Confirming check | Likelihood |
|---|---|---|---|
| Proxy mismatch (NDCG ≠ retention) | weak historical correlation | re-define proxy toward downstream engagement | HIGH |
| Feedback loop in logged data | NDCG computed on champion-logged clicks | off-policy / counterfactual eval | MEDIUM |
| Train/serve skew | offline uses batch features; serving uses real-time | diff feature values for 100 live requests | MEDIUM |
| Leakage in offline NDCG | +4% is large for this task | run leakage audit | LOW–MEDIUM |

### Ranked Fixes
1. Redefine the offline proxy toward a metric that historically tracks retention (e.g., session-depth proxy); re-validate correlation.
2. Add counterfactual/off-policy evaluation to remove logging bias from offline NDCG.
3. Diff offline vs. serving features; align computation if skew is found.
4. Run `mldata_data_leakage_detector` on the offline eval as a precaution.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** proxy → validity → online check → skew → shift → loops → leakage → fixes.
- **RT-09 (Root Cause Explanation):** the deliverable is causal, not descriptive.
- **DS-02 (Metric Specification):** rigor about proxy vs. outcome metric definitions.
- **CM-02 (Constraint Specification):** the proxy-must-track-outcome rule is the governing constraint.
- **QA-12 (False Positives Identification):** guards against treating under-powered nulls and leaked proxies as truth.

**Related Prompts:**
- `mleval_ab_test_design_for_models.md` — design the online test whose result you're interpreting.
- `mleval_metric_selection_guide.md` — choose a proxy more likely to track the outcome.
- `mldata_data_leakage_detector.md` — rule out leakage as the source of an offline-only win.
