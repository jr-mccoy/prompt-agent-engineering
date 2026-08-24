---
title: "ML Interpretability-First Modeling"
category: AI-ML/classical-ml-modeling
description: "Decide when to prefer an inherently interpretable model over a black box, and how to build a glass-box model (linear, rule-based, GAM/EBM, shallow tree) that meets the explainability mandate without surrendering too much performance."
techniques:
  - ST-02
  - RT-02
  - CM-02
  - QA-12
  - DS-06
difficulty: intermediate
tags:
  - interpretability
  - glass-box-models
  - gam-ebm
  - explainability
  - model-selection
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/classical-ml-modeling/mlmodel_algorithm_selection_matrix.md
  - domain-AI-ML/classical-ml-modeling/mlmodel_baseline_modeling_plan.md
  - domain-AI-ML/classical-ml-modeling/mlmodel_regularization_strategy.md
---

# ML Interpretability-First Modeling

**Objective:** Determine whether a problem calls for an inherently interpretable model (rather than a black box explained after the fact), and if so, design a glass-box model — regularized linear/logistic, rule sets, generalized additive models / explainable boosting, or shallow trees — that satisfies the explainability requirement while quantifying and minimizing any performance cost relative to a black-box reference.

**When to Use:**
- Decisions are high-stakes, regulated, or contested (credit, hiring, clinical, legal) where per-decision reasons must be auditable.
- A human must trust, override, or act on individual predictions.
- Stakeholders demand transparency and you need to weigh it against a black-box's headroom.

**When NOT to Use:**
- No interpretability requirement and pure predictive performance is the only goal.
- The need is post-hoc explanation of an already-fixed black box (SHAP/LIME), not choosing the model class.
- You're choosing a family across all criteria, not specifically optimizing for transparency (use `mlmodel_algorithm_selection_matrix.md`).

## Inputs / Context

Provide what you can:
- **Why interpretability is needed** — regulatory mandate, human override, debugging, fairness audit, stakeholder trust — and at what level (global model behavior vs per-prediction reasons).
- **Stakes & audience** — who reads the explanations and what they do with them.
- **Black-box reference** — performance of a black-box model if known (to size the tradeoff).
- **Data shape** — linearity, interactions, feature count, categorical mix.
- **Framework** — ask the user (sklearn, interpret/EBM, rule-fit, GAM libraries).

## Constraints

**Must:**
- Distinguish *inherently interpretable* (glass-box) from *post-hoc explained* black box, and justify which the requirement actually demands.
- Quantify the performance gap between the glass-box and a black-box reference on the same honest evaluation, so the tradeoff is explicit.
- Preserve genuine interpretability — avoid so many features/interactions that the "interpretable" model is no longer human-readable.

**Must Not:**
- Assume interpretability requires a large accuracy sacrifice without measuring it on this data.
- Pass off post-hoc SHAP on a black box as "interpretable" when the requirement demands an inherently transparent model.
- Quote the size of the accuracy/interpretability tradeoff as fact; measure it.

**Instructions:**

1. **Pin the interpretability requirement.** State precisely what must be explainable (global behavior, per-prediction reason codes, monotonic guarantees) and whether post-hoc explanation legally/operationally suffices or an inherently transparent model is required.

2. **Choose the glass-box class.** Map the requirement and data to a class: regularized linear/logistic (additive, coefficient reasons), GAM / explainable boosting (additive + per-feature shape, captures nonlinearity transparently), short rule sets / decision lists, or shallow trees. Note each class's interpretability granularity.

3. **Encode constraints into the model.** Where the domain demands it, impose monotonicity constraints, sparsity (L1) for fewer terms, and bounded interactions so the model stays readable and aligned with domain logic.

4. **Build the black-box reference.** Train a strong black-box model under identical evaluation as a performance ceiling, so the cost of transparency is measured, not assumed.

5. **Measure the tradeoff.** Compare glass-box vs black-box on the primary metric with uncertainty; report the gap honestly. Often the gap is small on tabular data — but that is an empirical finding here, not a guarantee.

6. **Validate the explanations.** Sanity-check that the glass-box's reasons are stable, plausible to domain experts, and don't encode proxies for protected or leaky variables.

7. **Recommend with the tradeoff stated.** Recommend the glass-box if it meets the requirement at an acceptable performance cost, or surface the explicit gap if the organization must choose between transparency and headroom.

**Output Format:**

A markdown report:
- **Interpretability Requirement** — what must be explained, at what level, and whether post-hoc suffices.
- **Glass-Box Class Choice** — class + granularity + why it fits.
- **Built-in Constraints** — monotonicity/sparsity/interaction bounds applied.
- **Black-Box Reference** — the ceiling model and evaluation.
- **Tradeoff Measurement** — glass-box vs black-box on the metric, with uncertainty.
- **Explanation Validation** — stability, plausibility, proxy/leakage check.
- **Recommendation** — chosen model + the stated tradeoff.

## Verification

- [ ] The requirement specifies the explanation level and whether post-hoc suffices.
- [ ] A glass-box class is chosen with its interpretability granularity stated.
- [ ] A black-box reference is built under identical evaluation to size the tradeoff.
- [ ] The performance gap is measured with uncertainty, not assumed.
- [ ] Explanations are validated for stability, plausibility, and proxy/leakage risk.
- [ ] No tradeoff magnitude is quoted as fact.

## False-Positive Prevention

❌ **DON'T:**
- Assume "interpretable means worse" and skip building the black-box reference that would reveal the real (often small) gap.
- Present SHAP on a gradient-boosted model as satisfying a requirement for an inherently transparent model.
- Pile dozens of features and interactions into a "linear" model until no human can read it, then call it interpretable.
- Trust glass-box coefficients/shapes without checking they aren't encoding a protected-attribute proxy or leaked feature.

✅ **DO:**
- Measure the transparency cost against a black-box ceiling on this data before deciding.
- Confirm whether the mandate accepts post-hoc explanation or requires an inherently interpretable model.
- Keep the glass-box genuinely readable via sparsity, monotonicity, and bounded interactions.
- Validate that explanations are stable and free of proxy/leakage artifacts with domain experts.

## Example Output

```markdown
## Interpretability-First: Credit Decisioning Model

### Interpretability Requirement
- Regulation requires per-applicant adverse-action reason codes and no proxy discrimination → inherently interpretable model required; post-hoc SHAP alone judged insufficient by compliance.

### Glass-Box Class Choice
- Explainable Boosting Machine (GAM-style) — additive per-feature shape functions give exact per-prediction contributions while capturing nonlinearity. Granularity: global shapes + per-prediction term contributions.

### Built-in Constraints
- Monotonic constraint on income (higher income never increases predicted risk); bounded pairwise interactions to keep terms readable; protected attributes and their close proxies excluded.

### Black-Box Reference
- LightGBM trained under identical grouped CV as the performance ceiling.

### Tradeoff Measurement
- Compare EBM vs LightGBM AUC across folds with fold-spread; report the gap honestly (often modest on tabular credit data, but measured here, not assumed).

### Explanation Validation
- Shape functions reviewed by credit risk experts for plausibility and monotonic sanity; checked that no remaining feature proxies a protected attribute.

### Recommendation
- Ship EBM if its AUC is within the compliance-acceptable margin of LightGBM; otherwise escalate the explicit transparency-vs-headroom gap to the risk committee.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** requirement → class → constraints → reference → tradeoff.
- **RT-02 (Multi-Dimensional Analysis Framework):** weighs interpretability granularity vs performance.
- **CM-02 (Constraint Specification):** monotonicity/sparsity and the explainability mandate as constraints.
- **QA-12 (False Positives Identification):** guards against "post-hoc passes as inherent" and proxy explanations.
- **DS-06 (Prioritization & Severity Guidance):** frames the transparency-vs-headroom decision for escalation.

**Related Prompts:**
- `mlmodel_algorithm_selection_matrix.md` — when interpretability is one of several selection criteria.
- `mlmodel_baseline_modeling_plan.md` — build the honest baseline the glass-box must clear.
- `mlmodel_regularization_strategy.md` — L1 sparsity keeps a glass-box model readable.
