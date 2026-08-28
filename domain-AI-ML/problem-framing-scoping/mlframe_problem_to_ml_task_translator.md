---
title: "Problem-to-ML-Task Translator"
category: AI-ML/problem-framing-scoping
description: "Map a fuzzy business ask to a concrete ML task type (classification, regression, ranking, clustering, detection, forecasting, etc.) with a precise target definition and unit of analysis."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-02
  - QA-12
difficulty: intermediate
tags:
  - task-formulation
  - target-definition
  - problem-framing
  - ml-task-types
  - scoping
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/problem-framing-scoping/mlframe_is_this_ml_problem.md
  - domain-AI-ML/problem-framing-scoping/mlframe_success_metric_selection.md
  - domain-AI-ML/problem-framing-scoping/mlframe_ml_use_case_canvas.md
---

# Problem-to-ML-Task Translator

**Objective:** Take a vague request ("predict churn," "find anomalies," "recommend products") and translate it into a precisely-specified ML task: the task type, the exact target/label definition, the unit of analysis, the prediction-time boundary, and the label horizon — so the rest of the project is built on an unambiguous formulation.

**When to Use:**
- A use case is approved but the ML task is still described in business language.
- Two people on the team mean different things by the same prediction.
- Before designing labels, splits, or metrics — all of which depend on the task formulation.

**When NOT to Use:**
- The decision to use ML is unsettled (use `mlframe_is_this_ml_problem.md`).
- The task is already precisely formulated and you need a metric (use `mlframe_success_metric_selection.md`).

## Inputs / Context

Provide what you can:
- **The ask in business language** and the decision it serves.
- **What "the answer" looks like** to the consumer (a yes/no, a number, a ranked list, a group).
- **The entity** the prediction is about (user, transaction, session, asset, time window).
- **Timing** — when the prediction is made and when the outcome becomes known.
- **Available signal/labels** — what could serve as the target.

## Constraints

**Must:**
- Recommend a specific task type and justify it from how the output is consumed.
- Define the target precisely: positive/negative definition (classification), the quantity and units (regression), the comparison set (ranking), etc.
- State the unit of analysis, the prediction-time boundary, and (where relevant) the label horizon.

**Must Not:**
- Leave the target ambiguous (e.g., "churn" without a definition of churned and a horizon).
- Invent label availability — if no clean target exists, say so and propose how to construct one.
- Force a single task type where the ask is genuinely two tasks (flag that instead).

**Instructions:**

1. **Extract the consumed output.** Determine what the consumer actually does with the answer — a binary action, a numeric estimate, a prioritized list, a grouping. The action dictates the task type.

2. **Select the task type.** Map to classification (incl. multi-label), regression, ranking/recommendation, clustering/segmentation, anomaly/detection, forecasting, or sequence/structured — and justify the choice against the consumed output.

3. **Define the target precisely.** For classification, write the exact positive-class definition and edge cases; for regression, the quantity and units; for ranking, the relevance signal; for clustering, what "similar" means and how clusters are used.

4. **Set the unit of analysis.** Name the entity each prediction is about and its grain (per user, per user-day, per transaction). This drives splitting and leakage control.

5. **Fix the prediction-time boundary and label horizon.** State the instant of inference and the window over which the outcome is measured (e.g., "predicted at signup, label = churned within 30 days").

6. **Check for hidden multi-task structure.** If the ask bundles two decisions (detect AND prioritize), split into distinct tasks rather than forcing one.

7. **Summarize the formulation and risks.** Produce the task spec and note formulation risks (proxy targets, horizon choices, leakage traps the framing creates).

**Output Format:**

A markdown task spec:
- **Consumed Output** — what the user does with the answer.
- **Task Type** — chosen type + justification.
- **Target Definition** — exact positive/negative, quantity/units, or relevance signal.
- **Unit of Analysis & Grain**
- **Prediction-Time Boundary & Label Horizon**
- **Alternatives Considered** — task types rejected and why.
- **Formulation Risks** — proxy/horizon/leakage cautions.

## Verification

- [ ] The task type is justified by how the output is consumed.
- [ ] The target is defined precisely, including edge cases and (for classification) the positive class.
- [ ] Unit of analysis and grain are stated.
- [ ] Prediction-time boundary and label horizon are explicit.
- [ ] Hidden multi-task structure is checked.
- [ ] No label availability is assumed; construction is proposed where needed.

## False-Positive Prevention

❌ **DON'T:**
- Formulate "predict churn" without defining churned (cancellation? inactivity?) and a horizon — the label is undefined otherwise.
- Choose regression when the consumer only acts on a threshold (then it's effectively classification at an operating point).
- Pick "anomaly detection" for a problem with labeled positives — that's supervised classification, usually stronger.
- Collapse two decisions into one model when they need different targets and metrics.

✅ **DO:**
- Let the consumed action choose the task type (threshold action ⇒ classification; ranked review ⇒ ranking).
- Write the positive-class definition and its edge cases explicitly.
- Fix the prediction-time boundary now, because the whole leakage and splitting strategy depends on it.
- Flag proxy targets (the available label isn't the true outcome) as a formulation risk.

## Example Output

```markdown
## ML Task Spec: "Help us reduce customer churn"

### Consumed Output
CS team gets a daily ranked list of accounts to proactively contact (top ~50/day capacity).

### Task Type
**Ranking / probability of churn used to prioritize** (not pure classification): the action is
"who do we call first," so a calibrated risk score ranked by likelihood fits better than a
hard label.

### Target Definition
Positive = account with zero paid activity for 30 consecutive days AND no renewal within the
window. Edge cases: paused/seasonal accounts excluded; downgrades counted as non-churn.

### Unit of Analysis & Grain
Per account, evaluated daily (account-day grain). Splitting must group by account_id.

### Prediction-Time Boundary & Label Horizon
Predicted using data available at end of day D; label measured over D+1..D+30.

### Alternatives Considered
- Binary classification at a threshold: rejected — capacity-limited outreach needs ranking.
- Survival/time-to-churn: viable upgrade later if "when" matters, not just "who."

### Formulation Risks
- 30-day horizon is a choice; a longer horizon changes positives materially.
- "Activity" is a proxy for engagement; validate it tracks real retention.
- Account-day grain risks leakage if features use post-D windows — enforce the boundary.
```

**Techniques Used:**
- **ST-01 (Clear Objective Statement):** output is one unambiguous task formulation.
- **ST-02 (Structured Sequential Instructions):** output → task type → target → grain → timing.
- **RT-02 (Multi-Dimensional Analysis Framework):** weighs candidate task types against the action.
- **CM-02 (Constraint Specification):** prediction-time boundary and horizon are governing constraints.
- **QA-12 (False Positives Identification):** guards against undefined targets and wrong task types.

**Related Prompts:**
- `mlframe_is_this_ml_problem.md` — confirm ML before formulating the task.
- `mlframe_success_metric_selection.md` — the formulation sets which metrics are valid.
- `mlframe_ml_use_case_canvas.md` — the prediction cell that this prompt makes precise.
