# `domain-science/statistics/`

The statistical-analysis-and-interpretation layer for the working scientist: choosing the test, sizing and reporting effects, controlling multiplicity, locking the analysis before data lock, and the model families and integrity audits that keep a result defensible. Composes on top of [`../methods-foundations/`](../methods-foundations/) (design, power, preregistration) and feeds the discipline modules in [`../disciplines/`](../disciplines/).

**Stance (per the ASA p-value statement):** estimation over isolated p-values, pre-specification over post-hoc flexibility, and calibrated claims over spin.

## Map (Phase 2D — 12 prompts)

### Test selection & reporting

| File | Coverage |
|---|---|
| [`science_statistical_test_selector.md`](science_statistical_test_selector.md) | Route test to outcome type / design / hypothesis; assumptions + the assumption-check and fallback for each |
| [`science_effect_size_and_uncertainty_reporter.md`](science_effect_size_and_uncertainty_reporter.md) | Right effect-size metric + confidence/credible interval + practical-significance call; journal-aware reporting |
| [`science_multiple_comparisons_strategy.md`](science_multiple_comparisons_strategy.md) | FWER vs FDR vs hierarchical/gatekeeping, framed by cost-of-error and family structure |
| [`science_statistical_results_interpreter.md`](science_statistical_results_interpreter.md) | Calibrated interpretation of supplied results; absence-of-evidence guard; inferential ceiling |

### Pre-specification & analysis integrity

| File | Coverage |
|---|---|
| [`science_pre_specified_analysis_plan.md`](science_pre_specified_analysis_plan.md) | Statistical Analysis Plan with ICH E9(R1) estimands; primary/secondary/exploratory locked before data lock |
| [`science_outlier_handling_decision.md`](science_outlier_handling_decision.md) | Pre-specified, rationale-backed outlier rules; robust methods; with/without sensitivity check |
| [`science_p_hacking_self_check.md`](science_p_hacking_self_check.md) | Garden-of-forking-paths register: researcher degrees of freedom → false-positive exposure → fix |

### Model families

| File | Coverage |
|---|---|
| [`science_bayesian_analysis_plan.md`](science_bayesian_analysis_plan.md) | Priors + prior predictive check, MCMC diagnostics, posterior summaries, decision rule, prior sensitivity |
| [`science_mixed_models_design.md`](science_mixed_models_design.md) | Fixed vs random, nested vs crossed, maximal-vs-parsimonious RE, REML/ML, singularity diagnosis |
| [`science_survival_analysis_design.md`](science_survival_analysis_design.md) | Censoring, KM/Cox/AFT, proportional-hazards assessment, competing risks (cause-specific vs Fine-Gray) |
| [`science_causal_inference_design.md`](science_causal_inference_design.md) | DAG → identification strategy (adjustment / IV / RDD / DiD), assumptions each buys, sensitivity (E-value) |
| [`science_meta_analysis_protocol.md`](science_meta_analysis_protocol.md) | PRISMA 2020 / PRISMA-P protocol: search, screen, extract, RoB, synthesize, heterogeneity, GRADE |

## Floor (per [`../README.md`](../README.md))

Every prompt requires discipline + study type; forbids fabricated citations, datasets, and effect sizes (`[user-supplied]` gaps); locks the output format; names the relevant reporting standard (ASA, SAMPL, CONSORT/STROBE, PRISMA, GRADE, ICH E9(R1)); preserves the pre-specified-vs-exploratory distinction; defaults to the Open Science branch (shared data/code/analysis script, preregistered analysis); and ends with a verification checklist + false-positive matrix.

See [`../EXPANSION_ROADMAP.md`](../EXPANSION_ROADMAP.md) for the remaining phases and build order.
