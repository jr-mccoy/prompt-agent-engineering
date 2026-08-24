---
title: "Pre-Specified Outlier Handling Decision"
category: science/statistics
description: "Set pre-specified, rationale-backed outlier rules, prefer robust methods over deletion, and document a with/without-exclusion robustness check."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-01
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - outliers
  - robust-statistics
  - pre-specification
  - sensitivity-analysis
  - influence-diagnostics
  - mad
  - winsorization
  - data-integrity
updated: "2026-06-26"
related_prompts:
  - domain-science/statistics/science_pre_specified_analysis_plan.md
  - domain-science/statistics/science_bayesian_analysis_plan.md
  - domain-science/statistics/science_p_hacking_self_check.md
  - domain-science/methods-foundations/science_preregistration_drafter.md
  - domain-science/methods-foundations/science_replicability_premortem.md
---

# Pre-Specified Outlier Handling Decision

**Objective:** Help the researcher decide, *before seeing outcome-dependent results*, how outliers and influential observations will be handled — distinguishing genuine errors/contaminants from real extreme values, preferring robust methods to deletion, and committing to a with-and-without-exclusion robustness check. The aim is to remove the single most common silent path to a false positive: outcome-dependent outlier removal.

**When to use:** You are designing or finalizing an analysis plan and need a defensible, documented outlier policy; or you are mid-analysis and need to lock the policy before letting any exclusion touch the headline result.

**Required inputs:**
- **Discipline.** [user-supplied]
- **Study type.** [user-supplied] (observational / experimental / computational / etc.)
- **Variables subject to outlier rules and their measurement scale/units.** [user-supplied]
- **Known error sources / contaminants.** [user-supplied] (e.g., sensor faults, transcription errors, assay failures, ineligible units)
- **Primary analysis model the rules feed into.** [user-supplied]

**Optional inputs:**
- Expected/plausible physical range per variable (hard bounds for impossible values).
- Sample size and group structure.
- Pre-registration identifier (OSF / AsPredicted).

**Constraints — Must:**
- Require each outlier rule to be **defined before** the outcome is examined, with a stated rationale.
- Separate **error/contaminant exclusions** (documented mechanism, e.g., impossible value, instrument fault, ineligibility) from **genuine extreme values** (real but distant data).
- Prefer **robust methods over deletion** for genuine extremes: MAD-based scaling, trimmed/Winsorized estimators, robust regression (M-estimators, Huber/Tukey loss), or models with heavy-tailed likelihoods.
- Use named detection criteria with stated thresholds (e.g., Tukey IQR fences at 1.5×/3× IQR; MAD-based z with cutoff ~3; studentized residuals; Cook's distance / leverage for influence) and state them in advance.
- Run the primary analysis **with and without** exclusions and report both as a robustness check; report N excluded and the reason for each.
- Align with a named reporting standard for transparency of data handling (e.g., CONSORT/STROBE flow accounting; the ASA p-value statement on transparency).

**Constraints — Must Not:**
- Do not invent citations, DOIs, datasets, effect sizes, or instrument/vendor specs. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not remove an observation because it moves a p-value across 0.05 (or any threshold); outcome-dependent exclusion is prohibited.
- Do not delete genuine extreme values when a robust method preserves them.
- Do not apply different exclusion rules across groups/arms unless pre-specified and justified.
- Do not use "novel," "groundbreaking," "first-ever," or "gold standard" in drafted text.

**Instructions:**

1. **Classify the candidates.** For each variable, list the error/contaminant mechanisms (handled by documented exclusion) versus the possibility of genuine extreme values (handled by robust methods). Set any hard physical bounds for impossible values.
2. **Choose detection criteria.** Pick the rule(s) and thresholds per variable: Tukey IQR fences, MAD-based z, studentized residuals; for influence, Cook's distance / leverage / DFBETAS. State them before seeing the outcome.
3. **Default to robustness, not deletion.** For genuine extremes, specify the robust estimator or model (trimmed mean, Winsorization fraction, Huber/Tukey M-estimator, robust regression, or heavy-tailed likelihood) as the *primary* handling; reserve deletion for documented errors only.
4. **Pre-specify the decision rule per case.** Build a decision table: condition met → action (document-and-exclude error / retain-and-model-robustly / flag-for-blinded-review). Apply identically across groups unless a justified exception is stated.
5. **Lock blinded review (if used).** If any human adjudication of candidates occurs, require it to be blinded to the outcome/grouping and recorded.
6. **Run the robustness comparison.** Specify the with-exclusion and without-exclusion analyses (and, where relevant, robust-method vs naive) and require both in the report, with the effect estimate from each.
7. **Account for every excluded point.** Specify a count + reason ledger and a flow statement (how many candidates, how many excluded, by which rule, why).
8. **Interpret divergence honestly.** State in advance how to interpret cases where conclusions change with/without exclusions: a conclusion that depends on removing genuine extremes is reported as fragile, not as the headline.

**Output format (locked):**

```
## Outlier Handling Decision — v[X.Y], frozen [DATE], precedes outcome inspection [DATE]
Discipline: [...]   Study type: [...]   Pre-registration: [user-supplied or none]

## 1. Candidate classification
| Variable | Units | Error/contaminant sources | Genuine-extreme possible? | Hard bounds |
|---|---|---|---|---|

## 2. Detection criteria (pre-specified)
| Variable | Rule | Threshold | For value or influence? |
|---|---|---|---|

## 3. Handling decision table
| Condition met | Classification | Action | Applied per-group identically? |
|---|---|---|---|
(Actions: document-and-exclude error / retain-and-model-robustly / blinded-review)

## 4. Robust method (primary handling of genuine extremes)
Estimator/model: ...   Parameters (trim/Winsor fraction, loss): ...

## 5. Robustness comparison template
| Analysis | N retained | N excluded | Effect estimate | Interval |
|---|---|---|---|---|
| With exclusions (primary) | | | | |
| Without exclusions | | | | |
| Robust method (no deletion) | | | | |

## 6. Exclusion ledger
| Obs ID | Variable | Rule triggered | Reason class | Blinded? |
|---|---|---|---|---|

## 7. Fragility interpretation
If conclusion changes across rows of §5: report as fragile, state which.
```

**Reporting-standard alignment:** CONSORT / STROBE participant-and-data flow accounting; ASA statement on p-values (transparency of data handling); robust-statistics literature (MAD, trimmed/Winsorized estimators, M-estimators, Cook's distance for influence).

**Verification checklist (before delivering):**
- [ ] Every rule is defined before outcome inspection, with a date stamp.
- [ ] Error/contaminant exclusions are separated from genuine extreme values.
- [ ] A robust method is the primary handling for genuine extremes (deletion reserved for documented errors).
- [ ] Detection thresholds are named and stated in advance.
- [ ] The with/without-exclusion (and robust) robustness comparison is required and templated.
- [ ] An exclusion ledger with count + reason exists; flow accounting is specified.
- [ ] No rule removes points based on movement across a significance threshold.
- [ ] Any human adjudication is blinded to outcome/group.
- [ ] No fabricated citations, effect sizes, or specs; unknowns marked `[user-supplied]`.
- [ ] No banned hype language in drafted text.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Outcome-dependent deletion | "Removed 3 outliers" that flip the result | Ban threshold-crossing removal; require pre-specification + ledger |
| Deleting real signal | Genuine extremes dropped as "outliers" | Default to robust methods; deletion only for documented errors |
| Asymmetric rules | Different cutoffs in treatment vs control | Require identical rules across groups unless pre-justified |
| Influence ≠ outlier confusion | A high-leverage point removed as an "outlier" | Separate value-rules (IQR/MAD) from influence-rules (Cook's D) |
| Unblinded adjudication | Human "judgment calls" made knowing the outcome | Require blinded review, logged |
| Hidden fragility | Reporting only the cleaned analysis | Require with/without comparison and fragility statement |
