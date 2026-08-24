---
title: "Baseline-First Design"
category: AI-ML/problem-framing-scoping
description: "Design the simplest viable baseline before any model is built, and define precisely what 'beating it' must mean — so model effort is justified, not assumed."
techniques:
  - ST-01
  - ST-02
  - DS-02
  - RT-05
  - QA-12
difficulty: intermediate
tags:
  - baseline
  - problem-framing
  - evaluation
  - heuristics
  - decision-support
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/problem-framing-scoping/mlframe_success_metric_selection.md
  - domain-AI-ML/problem-framing-scoping/mlframe_is_this_an_ml_problem.md
  - domain-AI-ML/feature-engineering/mlfeature_ideation_workshop.md
---

# Baseline-First Design

**Objective:** Specify the simplest defensible baseline for a problem — majority class, simple heuristic, a single strong feature, or the current production process — measure it on the real evaluation setup, and define the explicit, pre-committed margin by which a learned model must beat it to justify its cost.

**When to Use:**
- Before training the first model on a new problem.
- When someone reports a model's metric with nothing to compare it against.
- When a complex model is proposed and you want to know whether a trivial one would suffice.

**When NOT to Use:**
- You still aren't sure ML is warranted (use `mlframe_is_this_an_ml_problem.md`).
- You need the full metric contract first (use `mlframe_success_metric_selection.md`), then return to set the bar.

## Inputs / Context

Provide what you can:
- **Task type and target** — classification/regression/ranking and what's predicted.
- **The chosen primary metric** (or note it's TBD).
- **Class balance / target distribution** if known.
- **Candidate cheap signals** — any single feature or rule that obviously correlates.
- **Current process** — what humans or rules do today, and its known performance.
- **Cost of the modeling effort** — rough sense of what a full model costs to build and run.

## Constraints

**Must:**
- Define at least two baselines: a trivial floor (majority/random/mean) and a "smart simple" one (best single rule/feature or current process).
- Measure each baseline on the *same* split and metric the model will use.
- State the explicit margin (absolute or relative, with a confidence interval expectation) by which the model must beat the strongest baseline.

**Must Not:**
- Report a baseline number without naming the split and metric it was computed on.
- Invent baseline performance figures — if unmeasured, mark them as "to measure," not as facts.
- Set the bar against the trivial floor when a smart-simple baseline is achievable — that inflates apparent model value.

**Instructions:**

1. **Define the trivial floor.** Specify the majority-class predictor (classification), the mean/median predictor (regression), or random ranking — whatever encodes "no skill." This is the absolute floor any model must clear.

2. **Design the smart-simple baseline.** Identify the strongest single rule, single feature threshold, or the current production process. This is the real competitor; models often fail to beat it.

3. **Lock the evaluation to match the model's.** Compute baselines on the identical split, metric, and slices the model will be judged on, so the comparison is apples-to-apples.

4. **Measure (or schedule measurement).** Produce baseline numbers from data; where data isn't yet available, mark each as "to measure" and specify how.

5. **Set the bar with a margin and uncertainty.** State the minimum improvement over the strongest baseline that justifies the model, and require it to hold beyond noise (CI / repeated splits), not on a single lucky run.

6. **Define the kill condition.** State what happens if the model fails to clear the bar after a fair attempt — ship the baseline, simplify the problem, or stop.

7. **Record the baseline as the standing reference.** Note that all future model claims are reported relative to this baseline, not in isolation.

**Output Format:**

A markdown baseline spec:
- **Baselines** — table: Baseline | Definition | Metric value (or "to measure") | Notes.
- **Evaluation Setup** — split, metric, slices (must match the model's).
- **Bar to Beat** — the margin over the strongest baseline + uncertainty requirement.
- **Kill Condition** — what to do if the bar isn't cleared.
- **Open Measurements** — baselines still to compute and how.

## Verification

- [ ] Both a trivial floor and a smart-simple baseline are defined.
- [ ] Baselines are measured on the same split/metric/slices as the model.
- [ ] The bar is an explicit margin over the *strongest* baseline, with an uncertainty requirement.
- [ ] A kill condition exists.
- [ ] No baseline figure is asserted without a source; unmeasured ones are marked "to measure."

## False-Positive Prevention

❌ **DON'T:**
- Compare the model only to a majority-class floor when a one-rule baseline would have been far stronger — that overstates model value.
- Compute the baseline on a different split or metric than the model and call it a comparison.
- Declare the model "wins" from a single split without a confidence interval — the gap may be noise.
- Skip the baseline entirely and report the model number in isolation.

✅ **DO:**
- Make the current production process or best single rule the bar, since beating noise is trivial but beating the status quo is the real test.
- Require the improvement to exceed run-to-run variance (repeat splits / CI).
- Keep the baseline as a permanent reference so every later claim is relative.
- Pre-commit the kill condition before training, to avoid moving the goalposts after seeing results.

## Example Output

```markdown
## Baseline Spec: 30-Day Churn Prediction (primary metric: PR-AUC)

### Baselines
| Baseline | Definition | Metric value | Notes |
|---|---|---|---|
| Trivial floor | Predict majority (no churn) | PR-AUC = base rate ≈ 0.08 | "no skill" floor |
| Smart-simple | Rule: churn if logins_last_14d == 0 | PR-AUC ≈ 0.31 (to measure) | strongest cheap signal |
| Current process | Manual CS watchlist | recall ~0.4 at unknown precision (to measure) | status quo |

### Evaluation Setup
Temporal split (train ≤ Mar, test = Apr); PR-AUC primary; slices: tenure bucket, plan tier.
Matches the planned model evaluation exactly.

### Bar to Beat
Model must beat the smart-simple rule's PR-AUC by ≥ 0.05 absolute, and the gap's 95% CI
(over 5 temporal folds) must exclude zero.

### Kill Condition
If after a fair feature/model pass the model can't clear the bar, ship the single-rule baseline
and revisit only if richer behavioral data becomes available.

### Open Measurements
- Smart-simple rule PR-AUC on the temporal test set.
- Current manual-watchlist precision (pull from CS logs).
```

**Techniques Used:**
- **ST-01 (Clear Objective Statement):** the output is a committed bar-to-beat, not a vibe.
- **ST-02 (Structured Sequential Instructions):** trivial floor → smart-simple → measure → set bar.
- **DS-02 (Metric Specification):** baselines are pinned to the model's exact metric and split.
- **RT-05 (Evidence-Based Reasoning):** baseline claims must come from measurement, not assertion.
- **QA-12 (False Positives Identification):** guards against comparing only to a weak floor.

**Related Prompts:**
- `mlframe_success_metric_selection.md` — fixes the metric the baseline is measured in.
- `mlframe_is_this_an_ml_problem.md` — if a baseline already suffices, ML may be unnecessary.
- `mlfeature_ideation_workshop.md` — features to push a model past the bar.
