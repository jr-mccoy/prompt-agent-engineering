# `domain-science/ml-for-science/`

Machine learning used **as an instrument for scientific inference**: deciding whether ML is the right instrument for a lab or field question, designing a validation whose held-out data are independent at the level the claim generalises over, and translating interpretability output into claims no stronger than the evidence. Composes on top of [`../methods-foundations/`](../methods-foundations/) and [`../statistics/`](../statistics/), and works alongside the two ML-for-science prompts that shipped earlier in [`../computational/`](../computational/).

**Domain boundary:** [`../../domain-AI-ML/`](../../domain-AI-ML/) is for **building ML systems** — framing a product problem as ML, pipelines, deployment, monitoring, governance. This folder is for **ML as an instrument for scientific inference** — the unit of independence, batch and site structure, external validation tiers, and what a model-level statement licenses about the world. When a scientist is building a reusable ML system (a lab-wide segmentation service, a deployed clinical tool), the engineering lives in `domain-AI-ML/`; the scientific claim made with it lives here.

## Map (3 prompts)

| File | Coverage |
|---|---|
| [`science_ml_project_scoping.md`](science_ml_project_scoping.md) | Question class (inference / prediction / measurement automation / discovery) → ML vs classical stats; effective sample size from units of independence; batch/sample leakage and label-confounding map; baselines; go / redesign / stop triggers |
| [`science_ml_validation_split_design.md`](science_ml_validation_split_design.md) | Dependence diagnosis; grouped / forward-chaining / spatially blocked / similarity-clustered splits sized from measured dependence; nested tuning; external-validation tiers T0–T3 mapped to claim wording; cluster-level uncertainty; REFORMS / DOME / TRIPOD+AI map |
| [`science_ml_interpretation_for_claims.md`](science_ml_interpretation_for_claims.md) | Claim ladder (predictive → model attribution → data association → mechanistic); correlated-feature, stability, Rashomon, saliency sanity-check and shortcut-learning tests; the experiment required before a mechanistic claim |

### Related, filed in `computational/` (paths kept stable)

| File | Coverage |
|---|---|
| [`../computational/science_ml_for_science_benchmark_design.md`](../computational/science_ml_for_science_benchmark_design.md) | Baselines, pre-specified metrics, calibration, ablations, error analysis, test-set query budget |
| [`../computational/science_ml_for_science_validation_audit.md`](../computational/science_ml_for_science_validation_audit.md) | After-the-fact Kapoor–Narayanan leakage audit and claim-validity verdict |

## Typical sequence

```
science_ml_project_scoping  (is ML warranted? is n_eff enough? where will it leak?)
  → science_ml_validation_split_design  (split geometry, external tiers, unit-level uncertainty)
  + ../computational/science_ml_for_science_benchmark_design  (baselines, metrics, ablations)
  → run the locked evaluation
  → ../computational/science_ml_for_science_validation_audit  (leakage audit)
  → science_ml_interpretation_for_claims  (what the model's internals license you to say)
```

## Lives elsewhere

- Is ML right for a business or product problem → [`../../domain-AI-ML/problem-framing-scoping/`](../../domain-AI-ML/problem-framing-scoping/)
- CV and split strategy for production ML systems → [`../../domain-AI-ML/classical-ml-modeling/mlmodel_cross_validation_design.md`](../../domain-AI-ML/classical-ml-modeling/mlmodel_cross_validation_design.md), [`../../domain-AI-ML/data-for-ml/mldata_train_test_split_strategy.md`](../../domain-AI-ML/data-for-ml/mldata_train_test_split_strategy.md)
- Feature importance for model development → [`../../domain-AI-ML/feature-engineering/mlfeature_importance_analysis.md`](../../domain-AI-ML/feature-engineering/mlfeature_importance_analysis.md)
- Disclosing LLM / AI-tool use in research → [`../ethics-integrity/science_responsible_ai_use_in_research_audit.md`](../ethics-integrity/science_responsible_ai_use_in_research_audit.md)
- Causal identification for a mechanistic follow-up → [`../statistics/science_causal_inference_design.md`](../statistics/science_causal_inference_design.md)

## Floor (per [`../README.md`](../README.md))

Every prompt requires discipline + study type; forbids fabricated citations, datasets, ICCs, autocorrelation ranges, similarity thresholds, attributions, and performance figures (`[user-supplied]` or estimate it); locks the output format; names the relevant community standard (REFORMS, DOME, TRIPOD+AI where clinical, Kapoor–Narayanan leakage taxonomy); preserves the pre-specified-vs-exploratory distinction (scoping triggers, split design, and interpretation analyses locked before evaluation); defaults to the Open Science branch (split assignments, seeds, code, data or access route); and ends with a verification checklist + false-positive matrix.
