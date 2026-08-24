---
title: "Multiple Comparisons Strategy"
category: science/statistics
description: "Decide between FWER, FDR, hierarchical/gatekeeping, or no-correction strategies for a family of tests, keyed to the cost of false positives versus false negatives and the confirmatory/exploratory structure."
techniques:
  - ST-01
  - RT-03
  - CM-02
  - DS-02
  - NE-10
  - QA-01
difficulty: advanced
tags:
  - multiple-comparisons
  - fdr
  - fwer
  - benjamini-hochberg
  - holm-bonferroni
  - gatekeeping
  - error-control
  - pre-specification
updated: "2026-06-26"
related_prompts:
  - domain-science/statistics/science_statistical_test_selector.md
  - domain-science/statistics/science_statistical_results_interpreter.md
  - domain-science/statistics/science_effect_size_and_uncertainty_reporter.md
  - domain-science/methods-foundations/science_power_and_sample_size_calculator.md
---

# Multiple Comparisons Strategy

**Objective:** Choose a multiplicity-control strategy — FWER (Bonferroni/Holm/Hochberg), FDR (Benjamini-Hochberg/Benjamini-Yekutieli), hierarchical/gatekeeping (fixed-sequence, fallback), or no correction because there is a single pre-specified primary endpoint — by explicitly weighing the cost of a false positive against the cost of a false negative for the test family at hand. It produces a pre-specifiable error-control plan aligned with SAMPL and CONSORT/STROBE analysis-reporting items.

**When to use:** At analysis planning, before looking at the test results — whenever more than one hypothesis test, endpoint, subgroup, or contrast is in play.

**Required inputs:**
- **Discipline.** [user-supplied]
- **Study type.** [user-supplied] (observational / experimental / computational / high-throughput screen)
- **The set of tests.** Number and nature of comparisons, endpoints, or contrasts — `[user-supplied]`.
- **Confirmatory structure.** Which test(s) are pre-specified primary vs secondary vs exploratory.
- **Cost framing.** Relative cost of a false positive (e.g., chasing a spurious lead, harmful intervention) vs a false negative (e.g., missing a real signal in a screen).

**Optional inputs:**
- Dependence structure among tests (independent, positively correlated, arbitrary).
- A target error rate (e.g., FWER 0.05, FDR 0.10).
- Hierarchy/logical ordering among endpoints (for gatekeeping).
- Whether results have already been seen (if so, flag the integrity limitation).

**Constraints — Must:**
- Define the test family explicitly before choosing a procedure; state what is inside and outside it.
- Frame the FWER-vs-FDR-vs-gatekeeping choice as a false-positive/false-negative cost tradeoff using probability-weighted scenarios.
- Match the procedure to the dependence structure (Benjamini-Yekutieli for arbitrary dependence; Holm valid under any dependence; Benjamini-Hochberg for independence/positive dependence).
- Output adjusted thresholds (or the procedure's rejection rule) and label what is explicitly excluded from the corrected family as exploratory.
- Require pre-specification of the strategy before results are inspected.

**Constraints — Must Not:**
- Do not invent citations, DOIs, datasets, effect sizes, or instrument/vendor specs. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not recommend choosing or changing the correction after seeing which tests are significant.
- Do not use the words "novel," "groundbreaking," "first-ever," or "gold standard" in any drafted plan text.
- Do not apply a blanket Bonferroni to a single pre-specified primary endpoint, nor leave a large exploratory family uncorrected and report its "hits" as confirmatory.
- Do not treat FDR control as if it controlled the per-comparison or family-wise error rate.

**Instructions:**

1. **Confirm inputs.** Restate discipline, study type, the test set, the confirmatory structure, and the cost framing. Mark gaps `[user-supplied]` and ask.
2. **Define the family.** Specify the exact set of hypotheses whose error rate will be controlled; separate confirmatory primary/secondary from exploratory.
3. **Weigh the costs (NE-10).** Build probability-weighted scenarios for false-positive cost and false-negative cost; this drives FWER (false positives expensive) vs FDR (missing signals expensive, e.g., discovery screens).
4. **Consider structure.** If endpoints are logically ordered or there is a clear hierarchy, evaluate gatekeeping/fixed-sequence; if one primary endpoint exists, no correction may be the right call.
5. **Compare candidate procedures (Tree of Thoughts).** Lay out 2–3 procedures with their assumptions, dependence requirements, and what they control.
6. **Choose and parameterize.** State the procedure, the target rate, and the resulting adjusted thresholds or rejection rule.
7. **Demarcate the exploratory remainder.** Explicitly list tests outside the corrected family and label them hypothesis-generating.
8. **Lock pre-specification.** State that the strategy is fixed before results are seen; if results were already seen, flag the integrity limitation.
9. **Self-check.** Run the verification checklist and false-positive matrix.

**Output format (locked):**

```
## Inputs Confirmed
[discipline, study type, test set, confirmatory structure, cost framing]

## Family Definition
- In the family:
- Out of the family (exploratory):

## Cost-of-Error Tradeoff
| Scenario | Probability weight | FP cost | FN cost | Implication |
|---|---|---|---|---|

## Candidate Procedures
| Procedure | Controls | Dependence requirement | Best when |
|---|---|---|---|

## Chosen Strategy
- Procedure + target rate:
- Adjusted thresholds / rejection rule:
- Dependence justification:

## Exploratory Remainder
[tests excluded from correction, labeled hypothesis-generating]

## Pre-Specification Statement
[strategy fixed before results; integrity caveat if not]
```

**Reporting-standard alignment:** SAMPL guidelines; CONSORT item 18 / STROBE item 12 (subgroup/multiplicity handling). Benjamini-Hochberg (FDR) and Holm/Bonferroni (FWER) named explicitly; Benjamini-Yekutieli for dependence.

**Verification checklist (before delivering):**
- [ ] Test family defined explicitly, with in/out membership stated.
- [ ] FWER/FDR/gatekeeping/no-correction choice tied to a false-positive vs false-negative cost argument.
- [ ] Procedure matches the dependence structure.
- [ ] Adjusted thresholds or rejection rule given concretely.
- [ ] Exploratory remainder labeled hypothesis-generating.
- [ ] Strategy pre-specified before results; integrity caveat if results already seen.
- [ ] Single pre-specified primary endpoint not over-corrected.
- [ ] No invented citations/data/specs; gaps marked `[user-supplied]`.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Post-hoc correction switch | Loosening to FDR after Bonferroni "killed" the result | Lock the procedure before results; label any change exploratory |
| FDR misread as FWER | Treating BH-adjusted q-values as family-wise error guarantees | State explicitly what each procedure controls |
| Uncorrected fishing | Reporting "significant" hits from a large exploratory family as findings | Demarcate exploratory remainder; require independent confirmation |
| Over-correction | Bonferroni on a single pre-specified primary endpoint | No correction needed for one primary; reserve correction for genuine families |
| Wrong dependence assumption | BH applied under arbitrary/negative dependence | Use Benjamini-Yekutieli or Holm when dependence is unknown/arbitrary |
