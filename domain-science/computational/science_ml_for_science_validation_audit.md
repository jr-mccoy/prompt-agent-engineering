---
title: "ML-for-Science Validation & Leakage Audit"
category: science/computational
description: "Adversarially audit an ML-based scientific pipeline for data, label, temporal, and group leakage; distribution shift; and test-set contamination, then issue a calibrated verdict on what the model's results can legitimately support."
techniques:
  - ST-01
  - RT-01
  - RT-03
  - QA-02
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - ml-for-science
  - data-leakage
  - reproducibility
  - distribution-shift
  - test-set-contamination
  - validity-audit
  - temporal-leakage
  - group-leakage
updated: "2026-06-26"
related_prompts:
  - domain-science/computational/science_ml_for_science_benchmark_design.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
  - domain-science/methods-foundations/science_confound_and_bias_audit.md
  - domain-science/statistics/science_pre_specified_analysis_plan.md
---

# ML-for-Science Validation & Leakage Audit

**Objective:** Adversarially stress-test a machine-learning pipeline that is being used as a scientific instrument — i.e., to support a scientific claim — for the leakage and validity failures catalogued in the ML-for-science reproducibility literature. The audit walks the Kapoor & Narayanan leakage taxonomy against *this specific* pipeline, traces how each failure inflates the reported metric, and ends with a calibrated verdict separating what the model results can and cannot support. The goal is not to "fix the model" but to protect the scientific conclusion.

**When to use:** Before a finding obtained from an ML model is reported, published, or acted on; when reviewing someone else's ML-based scientific result; or when an in-house model's headline metric looks "too good." Use it after the eval protocol has (ideally) been fixed and before any further test-set use.

**Required inputs:**
- **Discipline.** The scientific field (e.g., genomics, ecology, materials science, clinical prediction, social science).
- **Scientific claim / study type.** The exact claim the model is being used to support (e.g., "feature X predicts outcome Y out-of-sample," "this model generalizes to held-out patients," "model accuracy of Z% demonstrates Y is learnable from these data"). State the inference target population the claim is meant to cover.
- **Pipeline description.** Task type (classification/regression/etc.), data provenance and units (rows, subjects, sites, time), and the full preprocessing → feature → split → tune → evaluate sequence, in the order it was actually run.
- **Split procedure.** How train/validation/test were created, when in the workflow they were separated, and whether any step (preprocessing, imputation, scaling, feature selection, hyperparameter tuning, augmentation) touched data outside its own split.

**Optional inputs:**
- Reported metric(s) and headline number(s) `[user-supplied]`.
- Whether a public benchmark was used and how many times the test set was queried.
- Deployment / claim-population description for distribution-shift assessment.
- Whether the eval protocol was pre-specified before touching the test set (yes/no/unsure).

**Constraints — Must:**
- Begin by restating the discipline and the scientific claim; anchor every leakage finding to how it would mislead *that* claim.
- Walk the full Kapoor & Narayanan leakage taxonomy explicitly: (1) no/improper train–test separation, (2) illegitimate features, (3) test-set reuse / distribution mismatch — expanded into the subtypes below.
- Establish whether the evaluation protocol was fixed *before* the test set was touched; treat any post-hoc protocol change as exploratory, not confirmatory.
- For every leakage type, produce: detection question → likely presence (present/absent/unknown) → mechanism by which it inflates the metric → concrete fix / re-evaluation needed.
- Distinguish pre-specified (confirmatory) from exploratory results in the verdict; never let an exploratory metric stand in for a confirmatory claim.
- Reference REFORMS / model-info-sheet reporting items and datasheets-for-datasets / model-card gaps as audit evidence.
- Default to an Open Science remediation branch: code, data, exact splits (with seeds), and a model card released so the eval is reproducible.

**Constraints — Must Not:**
- Do not invent citations, DOIs, dataset names, benchmark numbers, or model performance figures. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not pronounce a result "valid" — only that no leakage was detected *given the inputs provided*; absence of evidence is not validation.
- Do not use the words "novel," "groundbreaking," "first-ever," or "gold standard" in drafted text; any "state of the art" comparison must be calibrated or `[user-supplied]`.
- Do not recommend re-tuning, threshold-picking, or feature-selecting on the test set as a remedy.

**Instructions:**

1. **Restate claim and inference target.** Write the scientific claim in one sentence and name the population/distribution it must generalize to. Every downstream check is judged against this target, not against in-sample fit.
2. **Reconstruct the pipeline order.** List the actual sequence of operations and mark, for each, which data partition it consumed. Any operation that consumed data from outside its own split (preprocessing-on-full-data, scaling, imputation, feature selection, hyperparameter tuning, augmentation) is flagged immediately.
3. **Audit train–test separation (taxonomy group 1).** Walk the subtypes: preprocessing/feature-selection/imputation/normalization/tuning fit on full data; duplicate or near-duplicate records across splits; group/subject leakage (rows from the same entity — patient, site, molecule scaffold, household — span splits); temporal leakage (training on records that postdate the prediction time, or random splits where time ordering matters).
4. **Audit illegitimate features (taxonomy group 2).** Look for target leakage (a feature that is a proxy for, derived from, or only available after the label), features computed using the future, and identifiers that fingerprint outcomes. Ask whether each top feature would be available at the moment of prediction in the claim setting.
5. **Audit distribution shift.** Compare the evaluation set to the deployment/claim population on covariate, label, and subpopulation distributions. A random hold-out that matches the *sampling* but not the *inference target* (e.g., same hospital, future time, new species) does not support a generalization claim.
6. **Audit test-set reuse and contamination.** Count how many times the test/benchmark was queried; detect public-benchmark overfitting, test-set leakage into pretraining/foundation-model corpora, and adaptive overfitting from many model configs scored on the same test set. Tie this to a multiple-comparisons concern across configurations.
7. **Build the leakage register.** One row per leakage type with status, mechanism of metric inflation, severity, and the specific re-evaluation that would settle it.
8. **Issue the claim-validity verdict.** State, in calibrated language, what the results *can* support, what they *cannot*, and what re-analysis (clean split, grouped/temporal/OOD split, baseline comparison) is required before the claim stands.
9. **Specify the Open Science remediation package.** Enumerate the artifacts (code, raw + processed data or access plan, exact splits + seeds, model card, REFORMS-style info sheet) needed for an independent party to reproduce a leakage-free evaluation.

**Output format (locked):**

```
## Claim Under Audit
- Discipline:
- Scientific claim (one sentence):
- Inference target population/distribution:
- Eval protocol fixed before test-set use? [yes / no / unsure → treat as exploratory]

## Pipeline Order & Partition Map
| Step | Operation | Data partition consumed | Outside-split contamination? |
|---|---|---|---|

## Leakage Register (Kapoor–Narayanan taxonomy)
| # | Leakage type | Detection question | Status (present/absent/unknown) | Metric-inflation mechanism | Severity | Fix / re-evaluation |
|---|---|---|---|---|---|---|
| 1 | No/improper train–test separation |  |  |  |  |  |
| 2 | Duplicate / near-duplicate across splits |  |  |  |  |  |
| 3 | Group / subject leakage |  |  |  |  |  |
| 4 | Temporal leakage / use of the future |  |  |  |  |  |
| 5 | Preprocessing/tuning on full data |  |  |  |  |  |
| 6 | Illegitimate features / target proxy |  |  |  |  |  |
| 7 | Distribution shift vs claim population |  |  |  |  |  |
| 8 | Test-set reuse / benchmark contamination |  |  |  |  |  |

## Reporting & Documentation Gaps
- REFORMS / model-info-sheet items missing: [...]
- Datasheet-for-dataset / model-card gaps: [...]

## Claim-Validity Verdict (calibrated)
- The results CAN support: [...]
- The results CANNOT support: [...]
- Required re-analysis before the claim stands: [...]
- Reported metric reliability: [confirmatory / exploratory only / uninterpretable until re-run]

## Open Science Remediation Package
- [code / data / exact splits + seeds / model card / info sheet / reproducible eval script]
```

**Reporting-standard alignment:** Kapoor & Narayanan leakage taxonomy for ML-based science; REFORMS reporting checklist / model info sheets; datasheets for datasets; model cards; Gundersen reproducibility framework.

**Verification checklist (before delivering):**
- [ ] Discipline and the exact scientific claim are restated up front, with the inference target named.
- [ ] All eight leakage rows are filled with status + inflation mechanism + fix (no blanks left as "N/A" without justification).
- [ ] Group/subject and temporal leakage were checked against the data's actual unit of analysis, not assumed absent.
- [ ] Distribution shift is judged against the claim population, not merely against a random hold-out.
- [ ] Test-set query count and any benchmark/pretraining contamination were assessed.
- [ ] Pre-specified vs exploratory status of the eval protocol is recorded and carried into the verdict.
- [ ] No fabricated metrics, datasets, or citations; unknowns marked `[user-supplied]`.
- [ ] Verdict uses calibrated language and names required re-analyses; banned hype words absent.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Random split mistaken for valid generalization | High test accuracy from an i.i.d. random split that splits the same subjects/time across train and test | Require the split to match the inference target (grouped/temporal/OOD); demote random-split metrics to in-sample. |
| "No leakage found" read as validation | Auditor reports absent leakage on the subtypes checked and the team treats the claim as confirmed | State explicitly that absence of detected leakage is not validation; list unchecked/unknown rows. |
| Clean code review accepted as clean data flow | Tidy notebook where scaling/feature-selection was fit before the split is buried in a preprocessing function | Trace the partition map operation-by-operation, including library defaults and pipeline objects. |
| Strong feature accepted as legitimate signal | A target proxy (e.g., a post-outcome field, an ID correlated with label) drives the metric | For each top feature ask whether it is available at prediction time in the claim setting; flag future/derived features. |
| Public-benchmark SOTA taken at face value | Headline beats a leaderboard whose test set leaked into the model's pretraining corpus | Check for benchmark/pretraining contamination and adaptive overfitting; require a fresh held-out evaluation. |
