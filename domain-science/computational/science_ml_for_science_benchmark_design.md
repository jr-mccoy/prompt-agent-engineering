---
title: "ML-for-Science Benchmark & Evaluation Design"
category: science/computational
description: "Design a scientifically valid benchmark for an ML-based claim: choose a held-out split that matches the inference target, calibrate proper baselines, pre-specify metrics and uncertainty, and plan ablations and error analysis before the test set is touched."
techniques:
  - ST-01
  - ST-03
  - RT-03
  - QA-01
  - DS-02
  - NE-10
difficulty: advanced
tags:
  - ml-for-science
  - benchmark-design
  - held-out-evaluation
  - baselines
  - ablations
  - calibration
  - error-analysis
  - reproducibility
updated: "2026-06-26"
related_prompts:
  - domain-science/computational/science_ml_for_science_validation_audit.md
  - domain-science/statistics/science_pre_specified_analysis_plan.md
  - domain-science/statistics/science_multiple_comparisons_strategy.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
---

# ML-for-Science Benchmark & Evaluation Design

**Objective:** Design an evaluation that lets a machine-learning model serve as a credible scientific instrument: a held-out benchmark whose split matches the inference target, baselines calibrated so that "the model works" means "the model beats a fair reference," pre-specified metrics with calibration and uncertainty, and a planned set of ablations and error analyses. The deliverable is a benchmark-design table plus a pre-registration-style evaluation protocol that is fixed before the test set is queried.

**When to use:** Before running the confirmatory evaluation behind an ML-based scientific claim — i.e., after the model and analysis are exploratory-complete but before any reportable test-set number exists. Pair with the validation/leakage audit, which checks a pipeline after the fact.

**Required inputs:**
- **Discipline.** The scientific field (e.g., genomics, climate modeling, materials discovery, clinical prediction, ecology).
- **Scientific claim / study type.** The exact claim the benchmark must support (e.g., "the model predicts property Y for unseen compound scaffolds," "performance generalizes to a future season," "feature set X is sufficient to predict Y out-of-distribution"). Name the inference target population/distribution.
- **Task definition.** Task type (classification/regression/ranking/segmentation/etc.), prediction target, and the unit of analysis (sample, subject, site, time window, molecule scaffold).
- **Data provenance.** Source(s), sampling frame, grouping structure, and temporal structure of the data.

**Optional inputs:**
- Candidate baselines already in mind `[user-supplied]`.
- Existing reported numbers or a public benchmark to position against `[user-supplied]`.
- Compute/sample-size constraints and number of model configurations to be compared.
- Deployment/claim-population description for choosing an OOD split.

**Constraints — Must:**
- Restate discipline and the scientific claim first; select the split type *from* the claim (random vs grouped vs temporal vs out-of-distribution).
- Lock the full evaluation protocol — split, metrics, calibration assessment, uncertainty, baselines, ablations, error-analysis subgroups, and number-of-configs budget — *before* the test set is touched; mark anything decided later as exploratory.
- Specify at least two baselines: a simple non-ML reference (e.g., majority class, mean, last-value, linear model, domain heuristic) and a strong-but-fair ML baseline. Report the effect over baseline, not the absolute number alone.
- Pre-specify metrics appropriate to the task and the claim, plus a calibration assessment (e.g., ECE / reliability diagram for probabilistic outputs) and uncertainty quantification (confidence/credible intervals via an appropriate resampling or analytic method).
- Plan ablations that isolate which component actually carries performance, and an error analysis with subgroup/condition breakdowns (where and for whom the model fails).
- Control multiple comparisons across model configurations evaluated on the held-out data.
- Default to an Open Science release: data splits (with seeds), code, environment, model card, and a reproducible evaluation script.

**Constraints — Must Not:**
- Do not invent citations, DOIs, dataset names, benchmark numbers, or model performance figures. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not tune, threshold-select, or feature-select on the test set; the test set is queried once under the locked protocol.
- Do not use the words "novel," "groundbreaking," "first-ever," or "gold standard" in drafted text; any "state of the art" positioning must be calibrated or `[user-supplied]`.
- Do not report an absolute metric as evidence of scientific success without its baseline comparison and uncertainty interval.

**Instructions:**

1. **Anchor the task to the claim.** Write the scientific claim and the inference target in one sentence each. The split and metrics are chosen to make the benchmark a test of *that* claim, not of in-sample fit.
2. **Choose the held-out split by inference target.** Map claim → split: random hold-out only for i.i.d. claims; grouped split when the unit of analysis (subject/site/scaffold) must be unseen; temporal split when prediction is forward in time; out-of-distribution split when the claim is generalization to a different population/regime. Use nested cross-validation when tuning and evaluation would otherwise share data.
3. **Specify baselines and the comparison contract.** Define a simple non-ML baseline and a strong-but-fair ML baseline, both evaluated under the identical protocol. State that the headline result is the model's *improvement over baseline* with an uncertainty interval, not the raw metric.
4. **Pre-specify metrics, calibration, and uncertainty.** Select primary and secondary metrics tied to the claim; specify the calibration check (ECE, reliability diagram) for probabilistic predictions; specify how uncertainty intervals are computed and how "better than baseline" will be judged.
5. **Plan ablations.** Enumerate the components whose contribution is in question (features, architecture pieces, pretraining, augmentation) and the leave-one-out / add-one-in ablations that attribute performance to them.
6. **Plan error analysis.** Define the subgroups, conditions, or covariate slices over which performance will be broken down, so the benchmark reveals where and for whom the model fails — not just an aggregate score.
7. **Control multiple comparisons.** State how many configurations will be scored against the held-out set and the correction/selection rule (e.g., single locked config, or a correction across configs) to prevent adaptive overfitting.
8. **Write the pre-registration-style protocol.** Freeze everything above into a dated protocol; record the test-set query budget; declare any post-hoc change as exploratory and reported separately.
9. **Assemble the reproducibility package.** List the artifacts (splits + seeds, code, environment, model card, dataset documentation, eval script) required for an independent re-run.

**Output format (locked):**

```
## Claim & Task
- Discipline:
- Scientific claim (one sentence):
- Inference target population/distribution:
- Task type / prediction target / unit of analysis:

## Benchmark Design Table
| Design element | Choice | Justification (tied to the claim) |
|---|---|---|
| Held-out split type (random/grouped/temporal/OOD) |  |  |
| Cross-validation scheme (incl. nested if tuning) |  |  |
| Simple non-ML baseline |  |  |
| Strong-but-fair ML baseline |  |  |
| Primary metric |  |  |
| Secondary metric(s) |  |  |
| Calibration assessment (ECE / reliability) |  |  |
| Uncertainty quantification method |  |  |
| "Better than baseline" decision rule |  |  |

## Ablation Plan
| Component | Ablation (remove/add) | Question it answers |
|---|---|---|

## Error-Analysis Plan
| Subgroup / condition / slice | Why it matters to the claim | Metric reported per slice |
|---|---|---|

## Multiple-Comparisons Control
- Number of configurations to be scored on held-out data:
- Selection / correction rule:
- Test-set query budget:

## Pre-Registration-Style Evaluation Protocol (locked)
- Protocol date / "test set not yet touched" attestation:
- Frozen split + seeds:
- Confirmatory analyses (pre-specified):
- Exploratory analyses (reported separately):

## Open Science Reproducibility Package
- [splits + seeds / code / environment / model card / dataset documentation / eval script]
```

**Reporting-standard alignment:** REFORMS reporting checklist / model info sheets for ML-based science; train/validation/test and nested cross-validation discipline; calibration reporting (ECE, reliability diagrams); datasheets for datasets; model cards; Gundersen reproducibility framework.

**Verification checklist (before delivering):**
- [ ] Discipline and the exact scientific claim are restated, with the inference target named.
- [ ] The split type is justified *from* the claim (not defaulted to random) and uses nested CV where tuning shares data.
- [ ] Both a simple non-ML baseline and a strong-but-fair ML baseline are specified under the identical protocol.
- [ ] Headline result is defined as improvement-over-baseline with an uncertainty interval, not an absolute number.
- [ ] Calibration and uncertainty methods are pre-specified for probabilistic outputs.
- [ ] Ablation and error-analysis (subgroup) plans are present and tied to the claim.
- [ ] Multiple-comparisons control and a test-set query budget are stated; protocol is dated and frozen before test-set use.
- [ ] No fabricated metrics, datasets, baseline numbers, or citations; unknowns marked `[user-supplied]`; banned hype words absent and any SOTA positioning calibrated.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Impressive metric without a reference | A high absolute accuracy that a majority-class or mean baseline would nearly match | Always report improvement over a simple non-ML baseline with an interval. |
| Wrong split flatters the claim | Random hold-out used for a claim that requires unseen subjects/time/distribution | Pick the split from the inference target; demote a mismatched split to in-sample. |
| Aggregate score hides failure | Strong overall metric masks a subgroup or condition where the model is useless or harmful | Require pre-specified subgroup error analysis, not just a pooled number. |
| Best-of-many config reported as the result | Many configurations scored on the test set; the max is reported as if pre-specified | Lock the config or correct across configs; record the query budget. |
| Confident but miscalibrated probabilities | High discrimination metric (AUC) with badly calibrated probabilities used for a scientific claim about likelihoods | Pre-specify ECE / reliability-diagram assessment alongside discrimination metrics. |
| Ablation "confirming" the favored component | An ablation run only on the configuration that already wins, with no fair re-tuning | Hold the protocol fixed across ablations; avoid re-tuning that advantages the favored variant on test data. |
