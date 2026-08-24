---
title: "ML Success Metric Selection"
category: AI-ML/problem-framing-scoping
description: "Translate a business objective into a single primary model metric, a set of guardrail metrics, and a concrete decision threshold — so 'success' is unambiguous before training begins."
techniques:
  - ST-01
  - DS-02
  - RT-02
  - CM-02
  - QA-12
difficulty: intermediate
tags:
  - metrics
  - success-criteria
  - guardrails
  - threshold
  - problem-framing
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/problem-framing-scoping/mlframe_ml_use_case_canvas.md
  - domain-AI-ML/problem-framing-scoping/mlframe_cost_of_being_wrong_analysis.md
  - domain-AI-ML/problem-framing-scoping/mlframe_baseline_first_design.md
---

# ML Success Metric Selection

**Objective:** Convert a stated business objective into one primary model metric that the project optimizes, a small set of guardrail metrics that must not regress, and a decision threshold tied to how the prediction is acted upon — producing a metric contract everyone agrees to before a single model is trained.

**When to Use:**
- A use case is framed but "what does good look like?" is still answered with accuracy-by-default.
- Multiple metrics are in play and the team needs one to optimize and others to protect.
- You need to set the operating threshold that turns a score into an action.

**When NOT to Use:**
- The asymmetric cost of errors is the central question — start with `mlframe_cost_of_being_wrong_analysis.md`, then return here.
- You are designing the evaluation protocol itself (use a model-evaluation prompt).

## Inputs / Context

Provide what you can:
- **Business objective** — the outcome to move and its direction (increase/decrease).
- **The decision the model drives** and the action taken at each output.
- **Class balance / target distribution** if known.
- **Error costs** — relative cost of false positives vs false negatives, if known.
- **Operational constraints** — review capacity, budget per action, latency.
- **Fairness / regulatory** requirements that must be protected.

## Constraints

**Must:**
- Choose exactly one *primary* metric and justify it against the business objective and class balance.
- Define guardrail metrics (e.g., calibration, a fairness slice, latency, cost) that must not regress past stated limits.
- Tie the decision threshold to the action and the operating point, not to a default 0.5.

**Must Not:**
- Default to accuracy on an imbalanced problem.
- Invent class balance, error costs, or capacity numbers — mark unknowns and state how they'd change the metric.
- Optimize a metric the business cannot act on (e.g., AUC when a single threshold drives the action and calibration matters).

**Instructions:**

1. **Anchor to the business objective.** Name the outcome and its direction, and the smallest change that would matter to the owner. The metric must be a faithful proxy for this.

2. **Map the decision to a metric family.** Ranking action → ranking metrics (AUC, NDCG, precision@k); fixed-threshold classification → precision/recall/F-beta at the operating point; probabilities consumed downstream → calibration alongside discrimination; regression → error metric matched to cost shape (MAE vs RMSE vs quantile loss).

3. **Account for class balance.** On imbalanced targets, reject accuracy and prefer PR-AUC, recall at fixed precision, or cost-weighted metrics. State the majority-class baseline as the floor.

4. **Select the single primary metric.** Pick the one metric the team optimizes, and write one sentence on why it beats the alternatives for *this* decision and distribution.

5. **Define guardrail metrics with limits.** List the metrics that must not regress (calibration/ECE if probabilities are used, a fairness-slice metric, latency, cost-per-action) and the limit for each.

6. **Set the decision threshold.** Derive the operating threshold from the action's economics or capacity (e.g., review top-k per day, or the precision the business requires) — never assume 0.5.

7. **Write the metric contract.** Summarize primary + guardrails + threshold + baseline as a one-paragraph contract the team commits to, and list the assumptions that, if wrong, would change it.

**Output Format:**

A markdown metric contract:
- **Business Objective → Metric Rationale** — short paragraph.
- **Primary Metric** — name, definition, why this one.
- **Guardrail Metrics** — table: Metric | Why it matters | Must-not-cross limit.
- **Decision Threshold** — value/rule + how it was derived.
- **Baseline / Floor** — the number to beat.
- **Assumptions That Would Change This** — bulleted.

## Verification

- [ ] Exactly one primary metric is chosen and justified against objective + class balance.
- [ ] Accuracy is not the primary metric on an imbalanced problem (or imbalance is shown to be benign).
- [ ] Guardrails include any required fairness/calibration/latency/cost limits.
- [ ] The threshold is derived from the action's economics or capacity, not defaulted.
- [ ] A baseline floor is stated.
- [ ] No class-balance or cost figure is invented; unknowns are flagged.

## False-Positive Prevention

❌ **DON'T:**
- Optimize AUC when the action is a single hard threshold and the business needs calibrated probabilities — AUC is threshold-free and ignores calibration.
- Report accuracy on a 1%-positive problem; 99% accuracy is the do-nothing baseline.
- Pick F1 reflexively when false negatives and false positives have very different costs (use F-beta or cost-weighting).
- Treat a metric the team can't move operationally as the target.

✅ **DO:**
- Match the metric to how the output is consumed (ranking vs threshold vs probability).
- Always state the majority-class / random baseline as the floor the primary metric must clear.
- Make guardrails explicit limits, so optimizing the primary can't silently wreck fairness, calibration, or latency.
- Derive the threshold from capacity or cost, and revisit it if those change.

## Example Output

```markdown
## Metric Contract: Refund-Fraud Flagging

### Business Objective → Metric Rationale
Cut fraudulent payouts without overwhelming the 2-reviewer ops team. Reviewers can examine
~120 flagged refunds/day, so precision at a fixed review budget matters more than raw AUC.

### Primary Metric
**Precision@120/day (recall reported alongside).** With fixed review capacity, the question is
"of the cases we surface, how many are truly fraud?" — precision at the operating volume.

### Guardrail Metrics
| Metric | Why it matters | Must-not-cross limit |
|---|---|---|
| Recall on confirmed fraud | Don't silently miss big losses | ≥ current rules' recall |
| Calibration (ECE) | Score feeds an auto-deny tier later | ECE ≤ 0.05 (illustrative) |
| Decision latency | Inline at checkout | p95 < 2s |
| Slice precision (new vs tenured accounts) | Avoid over-flagging new users | within 10% of overall |

### Decision Threshold
Threshold set so daily flags ≈ 120 (reviewer capacity), recomputed weekly from score distribution.
Not 0.5.

### Baseline / Floor
Current rules: ~70% precision on flagged set (user-stated, to validate). ML must beat this at equal volume.

### Assumptions That Would Change This
- If reviewer capacity grows, raise volume and re-tune the threshold.
- If an auto-deny tier is added, calibration becomes a co-primary, not a guardrail.
```

**Techniques Used:**
- **ST-01 (Clear Objective Statement):** the deliverable is a single, committed metric contract.
- **DS-02 (Metric Specification):** core to selecting and defining primary and guardrail metrics.
- **RT-02 (Multi-Dimensional Analysis Framework):** weighs discrimination, calibration, fairness, and cost together.
- **CM-02 (Constraint Specification):** capacity and latency act as binding constraints on the threshold.
- **QA-12 (False Positives Identification):** guards against accuracy-on-imbalance and AUC-when-calibration-matters errors.

**Related Prompts:**
- `mlframe_ml_use_case_canvas.md` — the value cell feeds the metric choice.
- `mlframe_cost_of_being_wrong_analysis.md` — asymmetric costs shape which metric and threshold.
- `mlframe_baseline_first_design.md` — defines the floor the primary metric must beat.
