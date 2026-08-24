---
title: "Statistical Significance Testing for Model Comparison"
category: AI-ML/model-evaluation-validation
description: "Choose and apply the right significance test (McNemar, paired t, bootstrap CIs) to decide whether one model truly beats another, with proper care for paired data and multiple comparisons."
techniques:
  - ST-02
  - RT-02
  - DS-02
  - CM-02
  - QA-12
difficulty: advanced
tags:
  - significance-testing
  - confidence-intervals
  - mcnemar
  - bootstrap
  - multiple-comparisons
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/model-evaluation-validation/mleval_baseline_comparison_protocol.md
  - domain-AI-ML/model-evaluation-validation/mleval_ab_test_design_for_models.md
  - domain-AI-ML/model-evaluation-validation/mleval_eval_result_skepticism_audit.md
---

# Statistical Significance Testing for Model Comparison

**Objective:** Given two (or more) models evaluated on data, select the appropriate statistical test and report a defensible verdict on whether the difference is real — accounting for paired vs. unpaired data, the metric type, sample size, and the number of comparisons being made — instead of declaring victory on a raw point gap.

**When to Use:**
- Deciding whether a challenger model genuinely beats the champion before promoting it.
- A leaderboard shows a small gap and you must judge if it's signal or noise.
- Comparing many model variants and needing to avoid false discoveries from repeated testing.

**When NOT to Use:**
- Designing an online experiment with traffic allocation (use `mleval_ab_test_design_for_models.md`).
- You only need to pick which metric to test (use `mleval_metric_selection_guide.md`).

## Inputs / Context

Provide what you can:
- **Per-example predictions** from each model on the *same* evaluation set (enables paired tests) — or aggregate scores only.
- **Metric type** — accuracy/error rate (proportion), continuous metric (RMSE, latency), or ranking metric.
- **Sample size** and whether examples are independent (watch grouped data: users, sessions).
- **Number of comparisons** — how many models/variants/metrics are being compared at once.
- **Decision stakes** — what acting on a false positive (shipping a non-better model) would cost.

## Constraints

**Must:**
- Prefer **paired** tests when both models were run on the same examples — pairing removes example-difficulty variance and is far more powerful.
- Report an **effect size with a confidence interval**, not just a p-value; a significant-but-tiny difference is a real possibility to surface.
- Apply a **multiple-comparison correction** (or report the family-wise context) when more than one comparison is made.

**Must Not:**
- Apply an independent-samples test to paired predictions (it throws away the pairing and loses power).
- Fabricate p-values, CIs, or sample statistics; if per-example data is absent, state what test *would* apply and what data is needed.
- Treat statistical significance as practical significance, or vice versa.

**Instructions:**

1. **Determine pairing.** Establish whether both models scored the *same* examples. If yes, use paired methods; if not, note the power loss and use the appropriate unpaired test.

2. **Match the test to the metric.** For two classifiers on the same set with discrete correct/incorrect → **McNemar's test** on the discordant pairs. For a continuous per-example metric → **paired t-test** (or Wilcoxon signed-rank if non-normal). For complex metrics (AUC, F1, NDCG) where no closed-form paired test fits → **paired bootstrap** of the metric difference.

3. **Check assumptions and independence.** Verify normality for t-tests (or fall back to a non-parametric / bootstrap option) and confirm examples are independent — if data is grouped (same user/session), use a cluster/block bootstrap, not a naive one.

4. **Compute effect size + CI.** Report the metric difference and its confidence interval (e.g., bootstrap percentile CI for the delta). The CI's relation to zero is the headline, alongside the p-value.

5. **Correct for multiple comparisons.** If comparing K models or M metrics, apply Bonferroni (strict) or Benjamini–Hochberg (FDR, less conservative) and state which and why; report adjusted thresholds.

6. **Separate statistical from practical significance.** State the minimum difference that matters to the business and judge the result against it — a tiny significant gain may not justify a launch.

7. **State the verdict and its caveats.** Conclude "better / not distinguishable / worse," with the test used, the CI, the correction applied, and the residual risks (small n, grouped data, single eval set).

**Output Format:**

A markdown report:
- **Setup** — paired vs. unpaired, metric type, n, grouping, number of comparisons.
- **Test Choice** — the test and why it fits.
- **Result** — effect size, CI, p-value (corrected if applicable).
- **Practical Significance** — vs. the minimum meaningful difference.
- **Verdict & Caveats** — the conclusion and what could still make it wrong.

## Verification

- [ ] Pairing status is determined and the test choice respects it.
- [ ] The test matches the metric type (McNemar / paired t / Wilcoxon / bootstrap).
- [ ] Independence/grouping is checked; clustered data uses a clustered resampling method.
- [ ] An effect size with a confidence interval is reported, not a p-value alone.
- [ ] Multiple-comparison correction is applied or its absence justified.
- [ ] Statistical vs. practical significance is explicitly distinguished.

## False-Positive Prevention

❌ **DON'T:**
- Run an unpaired two-sample t-test when both models scored the identical examples — it discards the pairing and inflates the CI.
- Compare 20 model variants on the same holdout and trust the single "winner" at p<0.05 without correction — ~1 will look significant by chance.
- Bootstrap independently across rows when examples are grouped (multiple per user) — it understates the true CI.
- Equate a statistically significant 0.1% gain with a launch-worthy improvement.

✅ **DO:**
- Use McNemar / paired t / paired bootstrap to exploit the pairing and gain power.
- Apply Bonferroni or Benjamini–Hochberg across the family of comparisons and report the adjusted threshold.
- Use cluster/block bootstrap when the unit of independence is the user/session, not the row.
- Report the effect size and CI, and check it against the minimum difference that matters.

## Example Output

```markdown
## Significance Test: Challenger vs. Champion Classifier

### Setup
Both models scored the same 12,000-example golden set (paired). Metric: error rate (discrete correct/incorrect).
Examples independent (one per transaction). Comparisons in this family: 3 challengers vs. champion.

### Test Choice
McNemar's test on discordant pairs — correct framing for two classifiers on identical examples with binary correctness.

### Result
Discordant counts: champion-right/challenger-wrong = 210; champion-wrong/challenger-right = 268.
McNemar χ² = 6.8, raw p = 0.009. With Bonferroni across 3 comparisons, threshold = 0.0167 → still significant.
Accuracy delta = +0.48pp; paired bootstrap 95% CI on the delta = [+0.12pp, +0.84pp] (excludes 0).

### Practical Significance
Minimum meaningful gain for launch was set at +0.30pp accuracy. The CI lower bound (+0.12pp) dips below it,
so the gain is statistically real but its practical size is uncertain.

### Verdict & Caveats
Challenger is statistically better, but the practical magnitude is borderline. Caveats: single eval set
(temporal robustness unverified); recommend confirming on a fresh time window before promotion. If the
delta looked implausibly large, audit the eval for leakage first.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** pairing → test → assumptions → effect size → correction → verdict.
- **RT-02 (Multi-Dimensional Analysis Framework):** balances metric type, pairing, and comparison count.
- **DS-02 (Metric Specification):** defines effect size and CI precisely, not just p-values.
- **CM-02 (Constraint Specification):** the minimum-meaningful-difference is the governing decision constraint.
- **QA-12 (False Positives Identification):** multiple-comparison and pairing errors are the core false-positive traps.

**Related Prompts:**
- `mleval_baseline_comparison_protocol.md` — establish what "better than baseline" must clear first.
- `mleval_ab_test_design_for_models.md` — when the comparison should happen online instead.
- `mleval_eval_result_skepticism_audit.md` — when a difference looks too large to be real.
