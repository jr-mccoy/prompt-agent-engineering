---
title: "Feature Importance Analysis"
category: AI-ML/feature-engineering
description: "Interpret feature importance correctly — permutation, SHAP, and model-native scores — without sliding from correlation into causal claims or being fooled by collinearity and leakage."
techniques:
  - ST-02
  - RT-05
  - RT-09
  - DS-02
  - QA-12
difficulty: advanced
tags:
  - feature-importance
  - shap
  - permutation-importance
  - interpretability
  - correlation-causation
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/feature-engineering/mlfeature_selection_strategy.md
  - domain-AI-ML/data-for-ml/mldata_data_leakage_detector.md
  - domain-AI-ML/feature-engineering/mlfeature_drift_audit.md
---

# Feature Importance Analysis

**Objective:** Produce a correct interpretation of feature importance for a trained model — choosing the right method (permutation, SHAP, model-native), reading it within its assumptions, and explicitly separating "predictive in this model" from "a causal lever" — so stakeholders don't act on importance scores as if they were intervention effects.

**When to Use:**
- Explaining which features drive a model's predictions.
- Validating that the model relies on sensible signals (and not on a leak).
- Informing feature selection or stakeholder communication about drivers.

**When NOT to Use:**
- You need a causal effect estimate (importance is not causal — use a causal inference approach).
- You're auditing for leakage specifically (use `mldata_data_leakage_detector.md`, then return).

## Inputs / Context

Provide what you can (ask for framework + version if code is expected):
- **Model family** and the trained model context.
- **Importance method(s)** available or used (native gain, permutation, SHAP).
- **Feature correlations / collinearity** if known.
- **The decision** the interpretation will inform (selection, communication, debugging).
- **Validation setup** — importance should be computed on held-out data, not train.

## Constraints

**Must:**
- Choose the importance method appropriate to the model and question, and state its assumptions and failure modes.
- Compute/report importance on held-out data (permutation on validation), not on training data.
- Explicitly label every importance claim as predictive association, never as a causal lever, unless a causal design backs it.

**Must Not:**
- Present feature importance as the effect of changing the feature (correlation→causation slippage).
- Invent importance values or rankings — if not computed, describe how to compute, don't fabricate.
- Read collinear features' split importances naively (credit is shared/unstable across correlated features).

**Instructions:**

1. **Match method to question.** Native split importance answers "what did the trees use"; permutation importance answers "what does the model rely on for generalization"; SHAP gives per-prediction attributions. Pick per the goal and note biases (native gain favors high-cardinality; permutation is fooled by correlation).

2. **Compute on the right data.** Use held-out data for permutation/SHAP so importance reflects generalization, not memorization. State this explicitly.

3. **Handle collinearity.** For correlated features, use grouped permutation or cluster features before attributing, since correlated pairs split or trade credit unpredictably.

4. **Sanity-check for leakage signatures.** A single dominant feature that "explains everything" is a leakage red flag as much as an insight — cross-check against the prediction-time boundary.

5. **Read SHAP correctly.** Treat SHAP values as attributions under the model's learned function (associations), including interactions; do not read direction as a guaranteed real-world effect.

6. **Separate predictive from causal.** For any "X drives Y" temptation, state that importance shows association within the model and what a causal claim would additionally require (intervention/experiment).

7. **Communicate with caveats.** Present the ranking with stability (across folds/seeds), the method's assumptions, and an explicit predictive-not-causal disclaimer tailored to the decision.

**Output Format:**

A markdown interpretation:
- **Method & Why** — chosen method(s), assumptions, biases.
- **Importance Ranking** — table: Feature | Importance | Stability | Notes (incl. collinearity).
- **Leakage Sanity Check** — any dominant-feature red flags vs the boundary.
- **Predictive vs Causal** — explicit statement per high-importance feature.
- **Caveats & Communication Notes** — how to present to the decision owner.
- **Open Computations** — what still needs computing (no fabricated values).

## Verification

- [ ] The method matches the question and its biases are stated.
- [ ] Importance is computed on held-out data (for permutation/SHAP).
- [ ] Collinearity handling is addressed.
- [ ] A leakage sanity check on dominant features is performed.
- [ ] Every importance claim is labeled predictive, not causal.
- [ ] No importance values or rankings are fabricated.

## False-Positive Prevention

❌ **DON'T:**
- Tell a stakeholder "increasing feature X will raise outcome Y by Z" from importance — that's a causal claim importance cannot support.
- Trust native tree gain as "the truth"; it is biased toward high-cardinality and continuous features.
- Read permutation importance literally when features are correlated — permuting one while its correlate stays leaks information and understates importance.
- Celebrate one feature dominating importance without checking it isn't a target/temporal leak.

✅ **DO:**
- State that importance reflects association within this model, and name what a causal claim would require.
- Use permutation on held-out data and grouped attribution for collinear features.
- Cross-check a suspiciously dominant feature against the prediction-time boundary for leakage.
- Report stability across folds/seeds, since single-run rankings of correlated features are noisy.

## Example Output

```markdown
## Feature Importance: 30-Day Churn Model (GBT)

### Method & Why
Permutation importance on the held-out temporal fold (reflects generalization) + SHAP for
per-segment explanation. Native gain reported only as a cross-check (biased toward high-card).

### Importance Ranking
| Feature | Permutation imp. | Stability (5 folds) | Notes |
|---|---|---|---|
| days_since_last_login | high | stable | plausible engagement signal |
| logins_last_14d | high | stable | correlated w/ above (grouped) |
| support_tickets_last_30d | medium | stable | friction signal |
| plan_tier | low | stable | weak alone |

(days_since_last_login & logins_last_14d are correlated; reported as a group to avoid split credit.)

### Leakage Sanity Check
No single feature collapses performance when removed; top features are all observable ≤ day D.
No leakage signature found.

### Predictive vs Causal
"days_since_last_login is highly predictive of churn" — association within the model. It does NOT
imply that forcing logins reduces churn; that requires an experiment.

### Caveats & Communication Notes
Present to CS as "signals the model watches," not "levers to pull." Re-pull importance if drift
is detected (see drift audit).

### Open Computations
SHAP interaction values for the engagement cluster (not yet computed).
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** method → data → collinearity → leakage → causal framing.
- **RT-05 (Evidence-Based Reasoning):** rankings are tied to held-out computation, not assertion.
- **RT-09 (Root Cause Explanation):** distinguishes why a feature is predictive from whether it's causal.
- **DS-02 (Metric Specification):** importance is grounded in a generalization metric (permutation drop).
- **QA-12 (False Positives Identification):** centers on correlation→causation and leakage-as-importance traps.

**Related Prompts:**
- `mlfeature_selection_strategy.md` — importance informs which features to keep.
- `mldata_data_leakage_detector.md` — a dominant feature may be a leak, not a driver.
- `mlfeature_drift_audit.md` — re-check importance when feature distributions move.
