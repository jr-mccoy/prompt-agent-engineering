---
title: "Statistical Test Selector"
category: science/statistics
description: "Route a research hypothesis to the correct statistical test given outcome data type, design, and assumptions, then surface the assumption checks and fallbacks for each candidate."
techniques:
  - ST-01
  - RT-01
  - RT-03
  - CM-02
  - QA-01
  - DS-02
difficulty: advanced
tags:
  - statistical-testing
  - assumption-checks
  - study-design
  - nonparametric-fallback
  - glm
  - test-selection
  - residual-diagnostics
  - pre-specification
updated: "2026-06-26"
related_prompts:
  - domain-science/statistics/science_effect_size_and_uncertainty_reporter.md
  - domain-science/statistics/science_multiple_comparisons_strategy.md
  - domain-science/statistics/science_statistical_results_interpreter.md
  - domain-science/methods-foundations/science_power_and_sample_size_calculator.md
---

# Statistical Test Selector

**Objective:** Given a design, outcome data type, and hypothesis, recommend the appropriate statistical test(s), enumerate each candidate's assumptions and the specific diagnostic that checks each assumption, and pair every candidate with its robust/nonparametric/GLM fallback when an assumption fails. It produces a defensible, pre-specifiable analysis plan aligned with SAMPL guidelines and CONSORT/STROBE statistical-reporting items.

**When to use:** At the analysis-planning stage — ideally before data collection (preregistration) or before any model is fit — so the test is chosen by the question and design, not by which result yields p < 0.05.

**Required inputs:**
- **Discipline.** [user-supplied] (e.g., ecology, neuroscience, materials, clinical)
- **Study type.** [user-supplied] (observational / experimental / computational / quasi-experimental)
- **Outcome (dependent) variable type.** Continuous / binary / count / ordinal / time-to-event / proportion.
- **Hypothesis class.** Difference / association / equivalence / non-inferiority / trend.
- **Design structure.** Independent groups / paired / repeated-measures / clustered/nested / factorial / crossover.
- **Number of groups / levels** and **predictor types** (categorical, continuous, mixed).

**Optional inputs:**
- Sample size per group and any imbalance.
- Known distributional features (skew, zero-inflation, censoring).
- Whether the analysis is pre-specified (confirmatory) or exploratory.
- Smallest effect size of interest (SESOI) for equivalence/non-inferiority.
- Software/package constraints.

**Constraints — Must:**
- Route on outcome data type first, then design, then hypothesis class.
- For every candidate test, state each assumption AND the concrete diagnostic that checks it (e.g., normality of *residuals* via QQ-plot/Shapiro on residuals — not of the raw outcome; homoscedasticity via Levene/residual-vs-fitted; independence via design logic/ICC; linearity via component-plus-residual; proportional odds via Brant test; overdispersion via dispersion ratio/score test).
- Pair each candidate with its fallback when an assumption fails (robust SE, nonparametric analog, GLM with appropriate link/family, mixed model for clustering, GEE).
- Preserve the pre-specified vs exploratory distinction in the output.
- Name SAMPL and the relevant CONSORT/STROBE statistical items as the reporting target.

**Constraints — Must Not:**
- Do not invent citations, DOIs, datasets, effect sizes, or instrument/vendor specs. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not recommend selecting the test after inspecting which test gives a significant p-value (this is a form of p-hacking) — flag this explicitly.
- Do not test normality of the raw outcome as a gate for a parametric model when the assumption is about residuals.
- Do not use the words "novel," "groundbreaking," "first-ever," or "gold standard" in any drafted recommendation text.
- Do not collapse ordinal outcomes to means without justifying it, or dichotomize continuous outcomes to gain a simpler test.

**Instructions:**

1. **Confirm inputs.** Restate discipline, study type, outcome type, design, and hypothesis class. If any required input is missing, mark `[user-supplied]` and ask before proceeding.
2. **Classify the outcome.** Fix the data type, since it determines the family of tests (continuous → t/ANOVA/linear models; binary → logistic/chi-square/Fisher; count → Poisson/negative binomial; ordinal → ordinal logistic/Mann-Whitney; time-to-event → log-rank/Cox).
3. **Encode the design.** Map independence vs pairing/repetition/clustering, number of groups, and factorial structure. Clustering or repeated measures forces a mixed model / GEE / paired analog.
4. **Match to hypothesis class.** Difference vs association vs equivalence/non-inferiority changes the test (e.g., equivalence → TOST, not a standard two-sided test; trend → Jonckheere-Terpstra or linear contrast).
5. **Generate 2–3 viable candidates (Tree of Thoughts).** For each, reason through fit to the design, list assumptions + the diagnostic for each, and state the fallback if it fails.
6. **Recommend one test** with an explicit assumption-check plan (which diagnostic, on what, decision rule for switching to fallback).
7. **Flag pre-specification.** State whether this is confirmatory (lock it) or exploratory (label results as hypothesis-generating).
8. **Surface power/sample-size linkage.** Note if the chosen test implies a different power calculation than already done; route to the power-and-sample-size prompt.
9. **Self-check.** Run the verification checklist and false-positive matrix before delivering.

**Output format (locked):**

```
## Inputs Confirmed
[discipline, study type, outcome type, design, hypothesis class, pre-specified? ]

## Candidate Decision Table
| Candidate test | Fits because | Key assumptions | Assumption check (diagnostic) | Fallback if violated |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## Recommended Test
- Test:
- Why this over the alternatives:
- Assumption-check plan (what / how / switch rule):
- Pre-specified (confirmatory) or exploratory:

## Power / Sample-Size Note
[implication for power; route if recalculation needed]

## Pre-Specification Caveat
[lock for confirmatory; "hypothesis-generating" label for exploratory; warning against post-hoc test shopping]
```

**Reporting-standard alignment:** SAMPL guidelines (statistical analysis and methods reporting); CONSORT item 12a / STROBE item 12 (statistical methods, handling of missing data and confounding). Estimation-over-NHST framing per Cumming's "new statistics."

**Verification checklist (before delivering):**
- [ ] Outcome data type explicitly classified and drives the test family.
- [ ] Design structure (independence/pairing/clustering/factorial) encoded correctly.
- [ ] Hypothesis class (difference/association/equivalence/non-inferiority/trend) matched to test.
- [ ] Every candidate lists assumptions AND the concrete diagnostic for each.
- [ ] Normality check targets residuals, not raw outcome, where applicable.
- [ ] Each candidate has a robust/nonparametric/GLM/mixed fallback.
- [ ] Pre-specified vs exploratory status stated.
- [ ] No invented citations/data/specs; missing inputs marked `[user-supplied]`.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Test shopping | Picking the test that yields p<0.05 after running several | Lock the test from design + hypothesis before seeing results; label any switch as exploratory |
| Wrong normality target | Shapiro test on the raw outcome used to justify/reject a parametric model | Check normality of residuals; for large n note that the test itself is high-powered for trivial deviations |
| Ignored clustering | t-test/ANOVA on nested/repeated data inflating significance | Use mixed model/GEE/paired analog when independence is violated; report ICC |
| Count outcome as continuous | OLS on overdispersed/zero-inflated counts | Poisson with dispersion check → negative binomial / zero-inflated fallback |
| Ordinal as interval | Means/SDs on Likert-type outcomes without justification | Ordinal logistic (check proportional odds via Brant) or rank-based test |
