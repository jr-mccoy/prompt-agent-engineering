---
title: "Pre-Specified Statistical Analysis Plan (SAP)"
category: science/statistics
description: "Lock the estimand, primary, secondary, and clearly-labeled exploratory analyses in a version-stamped SAP before data lock."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-01
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - pre-specification
  - statistical-analysis-plan
  - estimand
  - confirmatory-vs-exploratory
  - missing-data
  - subgroup-analysis
  - ich-e9
  - preregistration
updated: "2026-06-26"
related_prompts:
  - domain-science/statistics/science_bayesian_analysis_plan.md
  - domain-science/statistics/science_outlier_handling_decision.md
  - domain-science/statistics/science_p_hacking_self_check.md
  - domain-science/methods-foundations/science_preregistration_drafter.md
  - domain-science/methods-foundations/science_replicability_premortem.md
---

# Pre-Specified Statistical Analysis Plan (SAP)

**Objective:** Help the researcher author a Statistical Analysis Plan that locks every analytic decision *before* data lock (or before unblinding). The plan must define the estimand, the single primary analysis, pre-specified secondary analyses, and a clearly fenced-off set of exploratory analyses — so that the confirmatory/exploratory boundary is fixed in advance and cannot drift after the data are seen.

**When to use:** You have a finalized study design and protocol, you have not yet locked/unblinded the data, and you want a version-stamped analysis plan that constrains researcher degrees of freedom and supports honest reporting.

**Required inputs:**
- **Discipline.** [user-supplied] (e.g., clinical trial, ecology, psychology, materials science)
- **Study type.** [user-supplied] (observational / experimental / RCT / computational / etc.)
- **Primary research question and hypothesis.** [user-supplied]
- **Primary endpoint / outcome variable(s) and how measured.** [user-supplied]
- **Planned sample size and the design (arms, units, randomization, blinding).** [user-supplied]

**Optional inputs:**
- Pre-registration / protocol identifier (OSF, AsPredicted, ClinicalTrials.gov, SPIRIT protocol).
- Known intercurrent events (treatment switching, rescue medication, dropout) and how design handles them.
- Pre-specified subgroups and the scientific rationale for each.
- Planned interim analyses / stopping rules and the alpha-spending function.
- Software and version intended for the analysis.

**Constraints — Must:**
- Define the estimand using all five ICH E9(R1) attributes: target population, treatment/exposure, endpoint/variable, intercurrent-event handling strategy, and population-level summary measure.
- Name exactly **one** primary analysis (model + estimand + test/estimator) and bind the study's headline conclusion to it.
- Label every analysis as **confirmatory (pre-specified)** or **exploratory**; exploratory analyses are hypothesis-generating only and must say so.
- Specify the missing-data strategy mechanistically (e.g., multiple imputation under a stated MAR/MNAR assumption with a sensitivity analysis); do not default to LOCF or complete-case without justification.
- Specify multiplicity control (family definition + method, e.g., hierarchical testing, Holm, Bonferroni, gatekeeping) for the confirmatory family.
- Pre-specify subgroups as interaction tests, not separate within-subgroup significance hunts.
- Version-stamp the SAP and state the data-lock / unblinding date it precedes.
- Align with a named reporting standard (SPIRIT for protocols, ICH E9/E9(R1) for trials, CONSORT for reporting).

**Constraints — Must Not:**
- Do not invent citations, DOIs, datasets, effect sizes, or instrument/vendor specs. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not present an exploratory finding as confirmatory, or move an analysis between categories after data lock.
- Do not select the primary endpoint or analysis model based on which gives the best result.
- Do not use the words "novel," "groundbreaking," "first-ever," or "gold standard" in drafted plan text.
- Do not leave the missing-data, multiplicity, or stopping-rule sections as "to be decided."

**Instructions:**

1. **Restate the question and fix the estimand.** Write the primary question in one sentence, then decompose it into the five ICH E9(R1) estimand attributes. Flag any intercurrent events the design must address and pick a handling strategy (treatment-policy, hypothetical, composite, while-on-treatment, principal-stratum) per event.
2. **Lock the primary analysis.** Specify the single estimator/model (e.g., mixed model for repeated measures, Cox PH, logistic GLM), the test statistic, the alpha, the directionality (one- vs two-sided + justification), and the exact effect measure reported. State the pre-specified covariates and why each is adjusted for.
3. **Specify secondary analyses.** List each pre-specified secondary endpoint/analysis, its model, and its place in the multiplicity hierarchy. Make clear these support but do not replace the primary conclusion.
4. **Fence off exploratory analyses.** List exploratory analyses separately and label them hypothesis-generating; state that their p-values/intervals are descriptive and uncorrected, and will be reported as such.
5. **Plan missing data.** State the expected missingness mechanism, the primary handling method (e.g., multiple imputation with stated imputation model and number of imputations), and at least one sensitivity analysis under an alternative assumption (e.g., MNAR delta-adjustment).
6. **Plan subgroups and interactions.** For each pre-specified subgroup, state the interaction test, the model, and that the analysis is powered/interpreted as exploratory unless explicitly powered.
7. **Plan interim looks and stopping rules (if any).** Specify the number/timing of looks, the alpha-spending or boundary (e.g., O'Brien-Fleming), and the decision at each look; if no interim analysis, state "none — single analysis at data lock."
8. **State the decision rule.** Write the explicit success criterion the primary analysis must meet, and what each plausible result implies (use probability-weighted scenarios where helpful). Version-stamp and freeze.

**Output format (locked):**

```
## Statistical Analysis Plan — v[X.Y], frozen [DATE], precedes data lock [DATE]
Discipline: [...]    Study type: [...]    Pre-registration: [user-supplied or none]

## 1. Estimand (ICH E9(R1))
| Attribute | Specification |
|---|---|
| Population | ... |
| Treatment/exposure | ... |
| Endpoint/variable | ... |
| Intercurrent-event handling | ... |
| Population-level summary | ... |

## 2. Primary analysis (CONFIRMATORY)
Model/estimator: ...   Test + alpha + sidedness: ...   Covariates: ...   Effect measure: ...
Success criterion: ...

## 3. Secondary analyses (CONFIRMATORY, in hierarchy)
| # | Endpoint | Model | Multiplicity position |
|---|---|---|---|

## 4. Exploratory analyses (HYPOTHESIS-GENERATING ONLY)
| # | Analysis | Reported as |
|---|---|---|

## 5. Missing data
Mechanism assumed: ...   Primary method: ...   Sensitivity analysis: ...

## 6. Subgroups (interaction-tested)
| Subgroup | Interaction test | Pre-specified? | Confirmatory/Exploratory |
|---|---|---|---|

## 7. Multiplicity control
Family: ...   Method: ...

## 8. Interim looks / stopping rules
...

## 9. Decision rule + scenario interpretation
| Result scenario | Interpretation |
|---|---|
```

**Reporting-standard alignment:** ICH E9 and E9(R1) (estimands), SPIRIT (protocol items), CONSORT (downstream reporting); OSF / AsPredicted / ClinicalTrials.gov as the pre-registration home.

**Verification checklist (before delivering):**
- [ ] All five ICH E9(R1) estimand attributes are explicitly stated.
- [ ] Exactly one primary analysis is named and bound to the headline conclusion.
- [ ] Every analysis is labeled confirmatory or exploratory; none is ambiguous.
- [ ] Missing-data method is mechanistic and has a sensitivity analysis (no unjustified LOCF/complete-case).
- [ ] Multiplicity control is specified for the confirmatory family.
- [ ] Subgroups are framed as interaction tests with rationale.
- [ ] Interim looks / stopping rules are specified or explicitly absent.
- [ ] SAP is version-stamped and dated before the data-lock/unblinding date.
- [ ] No fabricated citations, effect sizes, or specs; unknowns marked `[user-supplied]`.
- [ ] No banned hype language in drafted text.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Estimand drift | A clean primary model with no intercurrent-event strategy | Require all five E9(R1) attributes filled, including intercurrent events |
| Confirmatory inflation | Many "secondary confirmatory" tests, no hierarchy | Force a multiplicity hierarchy; cap the confirmatory family |
| Exploratory laundering | Exploratory result reported with a bare significant p-value | Label exploratory analyses as descriptive/uncorrected in the plan itself |
| Missing-data hand-wave | "LOCF" or "complete cases" with no mechanism stated | Require stated mechanism + imputation model + sensitivity analysis |
| Post-hoc subgroup | Subgroup "significant" via within-group test | Require interaction tests and pre-specification flag |
| Late editing | SAP undated, edited after a peek at data | Version-stamp and assert freeze date precedes data lock |
