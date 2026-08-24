---
title: "Baseline Comparison Protocol"
category: AI-ML/model-evaluation-validation
description: "Define the baselines every model must beat — trivial, heuristic, prior-model, and human — and a protocol for comparing honestly with intervals, so 'improvement' is never measured against nothing."
techniques:
  - ST-02
  - RT-02
  - DS-02
  - DS-06
  - QA-12
difficulty: intermediate
tags:
  - baselines
  - honest-comparison
  - majority-class
  - confidence-intervals
  - benchmarking
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/model-evaluation-validation/mleval_metric_selection_guide.md
  - domain-AI-ML/model-evaluation-validation/mleval_statistical_significance_testing.md
  - domain-AI-ML/model-evaluation-validation/mleval_evaluation_harness_design.md
---

# Baseline Comparison Protocol

**Objective:** Establish the full ladder of baselines a model must clear — trivial (random/majority), simple heuristic, prior production model, and (where relevant) human performance — and a protocol for comparing against them honestly, with intervals and the same evaluation conditions, so a reported "improvement" is meaningful rather than a comparison against nothing.

**When to Use:**
- Reporting a new model's performance and you need to know if it's actually good.
- A claim of improvement is made and you must validate that the comparison was fair.
- Setting up the baseline registry for an evaluation harness or benchmark.

**When NOT to Use:**
- You're testing whether a specific gap is significant (use `mleval_statistical_significance_testing.md`).
- You only need to pick the metric (use `mleval_metric_selection_guide.md`).

## Inputs / Context

Provide what you can:
- **Task & primary metric** with its operating point.
- **The model's reported score** and the evaluation set it was measured on.
- **Existing solutions** — any current rules engine, heuristic, or prior model in production.
- **Class balance / target distribution** — to compute trivial baselines.
- **Human/expert performance**, if the task has a meaningful human reference.
- **Comparison conditions** — was the model evaluated on the same data, split, and metric as the baselines?

## Constraints

**Must:**
- Always include at least the **trivial baseline** (random or majority/mean predictor) and, if one exists, the **prior production model**.
- Compare all contenders on the **identical** evaluation set, split, metric, and operating point — note any mismatch as a comparison invalidator.
- Report each baseline's score with a confidence interval and compare deltas with intervals, not point gaps.

**Must Not:**
- Report a model's score with no baseline, or against a baseline measured under different conditions.
- Fabricate baseline scores; if a baseline can't be computed from the input, mark it as required-but-missing.
- Treat beating a trivial baseline as success when a cheap heuristic or the prior model is the real bar.

**Instructions:**

1. **Build the baseline ladder.** Define, in increasing strength: (a) trivial — random or majority/mean; (b) simple heuristic — a one-rule predictor a non-ML person would try; (c) prior model — the current production champion; (d) human/expert — where a meaningful reference exists.

2. **Compute baselines under identical conditions.** Score every baseline on the *same* golden set, split, metric, and operating point as the model. Flag any baseline that was measured differently as not comparable.

3. **Attach intervals.** Report each score with a confidence interval (bootstrap or analytic) so the comparison accounts for sampling noise.

4. **Compare deltas with intervals.** For each rung, report the model's improvement over the baseline and the CI on that delta — a gain whose CI includes zero is not established.

5. **Set the meaningful bar.** Identify which rung is the *real* bar for a launch decision (usually the prior model or the strongest cheap baseline), and judge the model against that, not just the trivial one.

6. **Sanity-check implausible margins.** If the model crushes even strong baselines by an implausible margin, treat it as a leakage/eval-bug signal and route to a skepticism audit before celebrating.

7. **State the verdict.** Conclude whether the model beats the meaningful bar, by how much (with CI), under what conditions, and what would invalidate the comparison.

**Output Format:**

A markdown protocol + result:
- **Baseline Ladder** — table: Baseline | Definition | Score ± CI.
- **Comparison Conditions** — confirmation that all were measured identically (or mismatch flags).
- **Model vs. Each Baseline** — delta ± CI per rung.
- **Meaningful Bar** — which rung is the real bar and why.
- **Verdict** — beats / ties / loses the meaningful bar, with caveats.

## Verification

- [ ] A trivial baseline and (if it exists) the prior model are both included.
- [ ] All contenders were measured on the same data/split/metric/operating point.
- [ ] Each score and each delta carries a confidence interval.
- [ ] The meaningful bar (not just the trivial one) is identified and used for the verdict.
- [ ] Implausibly large margins trigger a leakage/eval-bug check.
- [ ] No baseline score is fabricated; missing required baselines are flagged.

## False-Positive Prevention

❌ **DON'T:**
- Report "92% accuracy" with no baseline — the reader can't tell if that beats predicting the majority class.
- Compare the model on a fresh, clean set against a baseline measured on a noisier old set and call the gap real.
- Celebrate beating a random baseline when a one-line heuristic already does nearly as well.
- Trust a huge margin over a strong baseline without ruling out leakage or an evaluation bug.

✅ **DO:**
- Always compute at least the trivial and prior-model baselines on the same set.
- Hold the evaluation conditions identical across all contenders, or declare the comparison invalid.
- Identify the strongest cheap/prior baseline as the real bar and judge against it.
- Treat implausible dominance as a red flag and audit the eval before believing it.

## Example Output

```markdown
## Baseline Comparison: Email Priority Classifier

### Baseline Ladder
| Baseline | Definition | Macro-F1 ± CI |
|---|---|---|
| Trivial (majority) | always "normal" | 0.31 (0.29–0.33) |
| Heuristic | rule: VIP sender OR "urgent" in subject → high | 0.58 (0.55–0.61) |
| Prior model | current production classifier | 0.71 (0.69–0.73) |
| Human | analyst triage agreement | 0.79 (0.76–0.82) |
| **New model** | challenger | **0.74 (0.72–0.76)** |

### Comparison Conditions
All scored on golden set v4 (n=6,000), same temporal split, macro-F1 at argmax. Conditions identical — comparable.

### Model vs. Each Baseline
- vs. trivial: +0.43 (CI +0.40 to +0.46) — clears easily.
- vs. heuristic: +0.16 (CI +0.12 to +0.20) — clears.
- vs. prior model: +0.03 (CI +0.00 to +0.06) — marginal; lower bound touches 0.
- vs. human: −0.05 — below human reference.

### Meaningful Bar
The prior production model (0.71) is the real bar. The +0.03 gain's CI barely excludes 0.

### Verdict
The new model beats trivial and heuristic clearly but only marginally beats the prior model (CI lower
bound = 0.00). Recommend a significance test and a fresh-window check before promotion. The margin is
plausible (not implausibly large), so leakage is a lower concern here.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** ladder → identical conditions → intervals → deltas → bar → verdict.
- **RT-02 (Multi-Dimensional Analysis Framework):** baselines span trivial → heuristic → prior → human.
- **DS-02 (Metric Specification):** scores and deltas defined precisely with intervals.
- **DS-06 (Prioritization & Severity Guidance):** the meaningful bar prioritizes which comparison decides.
- **QA-12 (False Positives Identification):** no-baseline and mismatched-condition traps are guarded.

**Related Prompts:**
- `mleval_metric_selection_guide.md` — choose the metric the baselines are compared on.
- `mleval_statistical_significance_testing.md` — test whether a marginal delta is real.
- `mleval_evaluation_harness_design.md` — register these baselines so they run every time.
