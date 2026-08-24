---
title: "Cost-of-Being-Wrong Analysis"
category: AI-ML/problem-framing-scoping
description: "Quantify the asymmetric costs of false negatives versus false positives and let that asymmetry drive metric choice, decision threshold, and human-in-the-loop design."
techniques:
  - ST-02
  - RT-02
  - DS-02
  - CM-02
  - QA-12
difficulty: advanced
tags:
  - error-costs
  - asymmetric-costs
  - threshold
  - cost-sensitive
  - problem-framing
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/problem-framing-scoping/mlframe_success_metric_selection.md
  - domain-AI-ML/problem-framing-scoping/mlframe_feasibility_risk_assessment.md
  - domain-AI-ML/problem-framing-scoping/mlframe_problem_to_ml_task_translator.md
---

# Cost-of-Being-Wrong Analysis

**Objective:** Make the asymmetry between false-negative and false-positive consequences explicit, express it as a cost ratio (or cost matrix), and use it to drive the choice of metric, the decision threshold, and where humans must stay in the loop — so the model is optimized for real-world consequences, not symmetric accuracy.

**When to Use:**
- The two error types have clearly different consequences (medical, fraud, safety, lending).
- A team is about to optimize a symmetric metric (accuracy, F1) on an asymmetric problem.
- You need to justify a non-default threshold or a human-review tier.

**When NOT to Use:**
- Errors are genuinely symmetric and low-stakes (a balanced metric is fine).
- You only need to pick a metric without the cost analysis (use `mlframe_success_metric_selection.md`).

## Inputs / Context

Provide what you can:
- **The decision and the two error types** in plain terms (what a FP and a FN each mean).
- **Consequences** of each error — financial, safety, reputational, regulatory, human.
- **Recovery** — is an error reversible/recoverable, and at what cost?
- **Base rate** of the positive class, if known.
- **Operational capacity** for human review of borderline cases.

## Constraints

**Must:**
- Define a false positive and a false negative in this domain's concrete terms before discussing cost.
- Express the asymmetry as a cost ratio or cost matrix, even if approximate, and state the assumptions behind it.
- Connect the asymmetry to a concrete recommendation: metric (e.g., recall-weighted), threshold direction, and human-in-the-loop design.

**Must Not:**
- Invent dollar values, base rates, or probabilities as facts — label them assumptions to validate and run a sensitivity range.
- Assume symmetric costs by defaulting to accuracy or F1.
- Recommend a single point threshold without showing how it shifts as the cost ratio changes.

**Instructions:**

1. **Define both errors concretely.** Write what a false positive and a false negative each mean for this decision and who bears the consequence. Ambiguity here corrupts the whole analysis.

2. **Enumerate consequences and recoverability.** For each error, list financial, safety, reputational, regulatory, and human consequences, and whether/how it can be recovered. Irreversible harm dominates.

3. **Express the cost asymmetry.** Build an approximate cost ratio (cost of FN ÷ cost of FP) or a 2×2 cost matrix. State every assumption and give a range, not a false-precise point.

4. **Derive the metric implication.** Translate the asymmetry into a metric stance — e.g., FN much costlier ⇒ optimize recall at a precision floor or use a cost-weighted metric / F-beta with β>1.

5. **Derive the threshold implication.** Show the direction and rough position the operating threshold should move given the cost ratio and base rate, and how it shifts across the ratio's plausible range.

6. **Design the human-in-the-loop tier.** Decide where uncertainty should route to human review given costs and review capacity (e.g., auto-act on confident cases, escalate the costly-error band).

7. **Run a sensitivity check.** Show how the recommendation changes across the plausible cost-ratio and base-rate ranges, and name what to measure to tighten it.

**Output Format:**

A markdown analysis:
- **Error Definitions** — what FP and FN mean here, and who bears each.
- **Consequence & Recoverability Table** — per error type.
- **Cost Asymmetry** — ratio or 2×2 matrix + assumptions (with a range).
- **Implications** — metric stance, threshold direction, human-in-the-loop design.
- **Sensitivity** — how the call changes across the cost-ratio/base-rate range.
- **To Validate** — the numbers most worth pinning down.

## Verification

- [ ] FP and FN are defined in concrete domain terms before any cost reasoning.
- [ ] Recoverability/irreversibility is considered, not just monetary cost.
- [ ] The asymmetry is expressed as a ratio/matrix with stated assumptions and a range.
- [ ] Metric, threshold, and human-in-the-loop implications all follow from the asymmetry.
- [ ] A sensitivity check shows how robust the recommendation is.
- [ ] No cost/base-rate figure is asserted as fact; assumptions are flagged.

## False-Positive Prevention

❌ **DON'T:**
- Optimize accuracy or F1 when a false negative costs far more than a false positive — symmetric metrics hide the asymmetry.
- Quote a single dollar cost ratio as if precise; small input changes can flip the threshold.
- Ignore irreversibility — a recoverable expensive error can be cheaper than a cheap irreversible one.
- Set a threshold from the cost ratio while ignoring the base rate, which co-determines the optimal operating point.

✅ **DO:**
- Define both error types in domain terms before costing them.
- Carry a cost-ratio *range* and show how the threshold and metric move across it.
- Weight irreversible harm heavily even when its monetary tag is fuzzy.
- Use the asymmetry to justify a human-review band for the costliest error type.

## Example Output

```markdown
## Cost-of-Being-Wrong: Tumor Triage Flag (assistive, not autonomous)

### Error Definitions
- FN: a true malignancy not flagged for radiologist priority → delayed diagnosis (patient harm).
- FP: a benign case flagged for priority review → extra radiologist time (operational cost).

### Consequence & Recoverability
| Error | Financial | Human/Safety | Recoverable? |
|---|---|---|---|
| FN | Litigation, late treatment | Severe, potentially irreversible | Often not |
| FP | Reviewer minutes | Mild anxiety / extra read | Yes |

### Cost Asymmetry
Cost(FN) ≫ Cost(FP). Approximate ratio range 20:1 to 100:1 (assumption — clinical input needed),
weighted further by irreversibility of FN.

### Implications
- Metric: optimize recall at a fixed false-positive/review-capacity ceiling (not F1, not accuracy).
- Threshold: set low (high sensitivity); accept more FPs to minimize FNs.
- Human-in-the-loop: model only *prioritizes* the worklist; radiologist makes every call. No autonomy.

### Sensitivity
Across 20:1–100:1, the recommendation (high recall, low threshold, human-final) is stable; only
the acceptable FP volume shifts with review capacity.

### To Validate
Radiologist review capacity per day; clinically-grounded FN:FP cost ratio; base malignancy rate.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** define errors → cost → metric → threshold → HITL.
- **RT-02 (Multi-Dimensional Analysis Framework):** weighs financial, safety, and reversibility dimensions.
- **DS-02 (Metric Specification):** the asymmetry selects the metric and operating point.
- **CM-02 (Constraint Specification):** review capacity and irreversibility constrain the threshold.
- **QA-12 (False Positives Identification):** the analysis is literally about FP/FN tradeoffs done right.

**Related Prompts:**
- `mlframe_success_metric_selection.md` — consumes this asymmetry to fix the metric.
- `mlframe_feasibility_risk_assessment.md` — costly errors feed the harm-risk dimension.
- `mlframe_problem_to_ml_task_translator.md` — the task formulation defines what FP/FN even mean.
