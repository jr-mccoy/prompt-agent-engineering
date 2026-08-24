---
title: "Effect Size and Uncertainty Reporter"
category: science/statistics
description: "Select the correct effect-size metric for the design and report it with an appropriate confidence or credible interval and a practical-significance interpretation, in the target journal's style."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - CM-02
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - effect-size
  - confidence-intervals
  - estimation-statistics
  - practical-significance
  - reporting-standards
  - cohens-d
  - sesoi
  - new-statistics
updated: "2026-06-26"
related_prompts:
  - domain-science/statistics/science_statistical_test_selector.md
  - domain-science/statistics/science_statistical_results_interpreter.md
  - domain-science/statistics/science_multiple_comparisons_strategy.md
  - domain-science/methods-foundations/science_power_and_sample_size_calculator.md
---

# Effect Size and Uncertainty Reporter

**Objective:** Choose the design-appropriate effect-size metric, pair it with a confidence (or credible) interval, and interpret it against a smallest-effect-size-of-interest so the reader sees magnitude and precision — not just a p-value. It produces estimation-first reporting text aligned with SAMPL, APA effect-size norms, and CONSORT/STROBE numeric-reporting items.

**When to use:** When writing up results — after the test is run and the analysis plan is fixed — to report magnitude and uncertainty rather than only statistical significance.

**Required inputs:**
- **Discipline.** [user-supplied]
- **Study type.** [user-supplied] (observational / experimental / computational)
- **Design.** Independent / paired / repeated / factorial / regression / survival.
- **Outcome type.** Continuous / binary / count / ordinal / time-to-event / correlation.
- **The estimate(s) and their components.** Group means/SDs, cell counts, model coefficients, n per group — `[user-supplied]`.
- **Target journal or style.** (e.g., APA, a specific journal's instructions-to-authors) — `[user-supplied]`.

**Optional inputs:**
- Smallest effect size of interest (SESOI) / minimal clinically important difference.
- Preference for standardized vs unstandardized reporting.
- Frequentist vs Bayesian interval preference and prior (if Bayesian).
- Whether the estimand is pre-specified (primary) or exploratory.

**Constraints — Must:**
- Match the effect-size metric to the design and outcome (Cohen's d / Hedges' g for mean differences; Cliff's delta for ordinal/nonparametric; odds ratio, risk ratio, and risk difference for binary; Pearson/Spearman r for association; eta²/omega² for ANOVA variance explained; rate ratio for counts; hazard ratio for time-to-event).
- Report every effect size WITH an interval (CI or credible interval) and the practical-significance interpretation relative to a SESOI.
- State whether the effect size is standardized or unstandardized and justify the choice.
- Provide a journal-aware reporting sentence template.
- Preserve the pre-specified (primary) vs exploratory distinction.

**Constraints — Must Not:**
- Do not invent citations, DOIs, datasets, effect sizes, or instrument/vendor specs. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not report a p-value without an accompanying effect size and interval.
- Do not use the words "novel," "groundbreaking," "first-ever," or "gold standard" in any drafted results/reporting text.
- Do not interpret a statistically significant result as automatically practically important, or a wide interval as a precise estimate.
- Do not convert between metrics (e.g., d↔r, OR↔RR) without stating the conversion assumption and base rate.

**Instructions:**

1. **Confirm inputs.** Restate discipline, study type, design, outcome type, and the supplied estimate components. Mark any missing piece `[user-supplied]` and ask.
2. **Select the metric.** Map design + outcome to the correct effect-size family; if more than one is defensible, state the tradeoff (e.g., OR vs RR interpretability; d vs g for small n).
3. **Compute or template the estimate.** Use only supplied numbers; if numbers are absent, give the formula and the labeled placeholders rather than fabricating values.
4. **Attach uncertainty.** Provide the matching interval (CI default; credible interval if Bayesian, with prior stated). Note the interval's width as the precision signal.
5. **Set the practical-significance anchor.** Compare the estimate and interval to the SESOI; if no SESOI was supplied, request one and explain why magnitude can't be judged without it.
6. **Decide standardized vs unstandardized.** Recommend based on whether the outcome's raw units are interpretable to the audience; report both when feasible.
7. **Draft journal-aware reporting text.** Produce an APA-style sentence and a CONSORT/STROBE-aligned numeric line; keep language calibrated.
8. **Label estimand status.** Mark primary (confirmatory) vs exploratory effect sizes distinctly.
9. **Self-check.** Run the verification checklist and false-positive matrix.

**Output format (locked):**

```
## Inputs Confirmed
[discipline, study type, design, outcome type, supplied estimates, target style, SESOI?]

## Effect-Size Selection
| Metric considered | Appropriate when | Chosen? | Reason |
|---|---|---|---|

## Estimate + Uncertainty
- Effect size (point estimate):
- Interval (type, level, bounds):
- Standardized / unstandardized (and why):
- Precision read (interval width):

## Practical Significance
- SESOI / MCID used:
- Interpretation vs SESOI:

## Reporting Text (journal-aware)
- APA-style sentence:
- CONSORT/STROBE numeric line:

## Estimand Status
[primary/confirmatory vs exploratory]
```

**Reporting-standard alignment:** SAMPL guidelines; APA effect-size and interval reporting norms; CONSORT item 17b / STROBE item 16 (report estimates with precision, e.g., 95% CI). Estimation-over-NHST per Cumming's "new statistics."

**Verification checklist (before delivering):**
- [ ] Effect-size metric matches both design and outcome type.
- [ ] Every effect size is paired with a CI or credible interval.
- [ ] Practical significance judged against a stated SESOI/MCID.
- [ ] Standardized vs unstandardized choice stated and justified.
- [ ] No p-value reported without effect size + interval.
- [ ] Interval width interpreted as precision, not ignored.
- [ ] Primary vs exploratory estimands distinguished.
- [ ] No invented numbers/citations/specs; gaps marked `[user-supplied]`.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Significance = importance | Calling a tiny d "important" because p<0.05 | Compare estimate + interval to SESOI; state magnitude separately from significance |
| Wrong metric | Cohen's d on binary outcomes; OR reported as if RR | Route metric by outcome type; for binary report RR/RD when base rate is interpretable |
| Naked p-value | Reporting p without effect size or interval | Block delivery until effect size + interval present |
| False precision | Treating a wide CI as a settled estimate | Surface interval width explicitly; recommend "estimate is imprecise" language |
| Silent conversion | d↔r or OR↔RR conversion without base rate stated | Show the conversion assumption and base rate, or decline to convert |
