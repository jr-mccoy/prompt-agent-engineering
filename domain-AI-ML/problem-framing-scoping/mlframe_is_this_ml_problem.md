---
title: "Is This an ML Problem?"
category: AI-ML/problem-framing-scoping
description: "Decide whether a problem genuinely warrants machine learning versus rules, heuristics, or analytics — with an honest cost/benefit and the conditions under which ML is the wrong tool."
techniques:
  - ST-01
  - RT-02
  - CM-02
  - DS-06
  - QA-12
difficulty: intermediate
tags:
  - problem-framing
  - ml-vs-rules
  - cost-benefit
  - scoping
  - decision-support
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/problem-framing-scoping/mlframe_ml_use_case_canvas.md
  - domain-AI-ML/problem-framing-scoping/mlframe_baseline_first_design.md
  - domain-AI-ML/problem-framing-scoping/mlframe_feasibility_risk_assessment.md
---

# Is This an ML Problem?

**Objective:** Given a proposed initiative, determine whether machine learning is the right approach at all — versus deterministic rules, a heuristic, classical analytics/BI, or simply not building anything — and produce a defensible recommendation that names the conditions ML must satisfy to be worth its lifetime cost.

**When to Use:**
- A stakeholder has asked for "an AI/ML model" before the problem is even framed.
- You suspect a handful of rules would solve 90% of the case at a fraction of the cost.
- Before allocating data-science headcount or compute to a new initiative.
- When the same outcome could plausibly be reached by analytics or process change.

**When NOT to Use:**
- The decision to use ML is already made and validated; you now need to scope it (use `mlframe_ml_use_case_canvas.md`).
- You are choosing between specific ML task types (use `mlframe_problem_to_ml_task_translator.md`).

## Inputs / Context

Provide what you can; the analysis still runs if some are missing:
- **The problem in plain language** — what outcome someone wants to change, for whom.
- **The decision or action** the output will drive (and who/what acts on it).
- **Current approach** — manual process, existing rules, nothing.
- **Available signal** — what data exists, its volume, labeling, and history.
- **Volume & latency** — how many decisions per day; how fast each must be.
- **Tolerance for error** and the cost of being wrong.

## Constraints

**Must:**
- Compare ML against at least three alternatives: rules/heuristics, classical analytics, and do-nothing/process-change.
- State the conditions under which ML *becomes* the right tool, and the conditions under which it is the wrong one.
- Account for ML's full lifetime cost (data, labeling, training, serving, monitoring, retraining, on-call), not just build cost.

**Must Not:**
- Recommend ML by default or because it is fashionable.
- Fabricate accuracy, ROI, or volume figures — if a number is unknown, mark it as an assumption to validate, not a fact.
- Assume data exists, is labeled, or is usable without confirming it from the inputs.

**Instructions:**

1. **Restate the actual problem and the decision it serves.** Strip the solution language ("we need a model") and name the outcome someone wants and the action the output triggers. If there is no downstream decision, flag it — a prediction nobody acts on is not worth building.

2. **Test the four ML-fit signals.** ML earns its keep when: (a) the pattern is real but too complex to enumerate as rules; (b) sufficient representative labeled/observable data exists; (c) the input distribution is reasonably stable or monitorable; (d) approximate, probabilistic answers are acceptable. Score each signal present / partial / absent with the evidence.

3. **Stress the rules/heuristic alternative.** Could a small set of expert rules or a threshold capture most of the value? Estimate the coverage of a rules baseline. If rules plausibly clear the bar, ML must justify the *marginal* lift over them.

4. **Stress the analytics/do-nothing alternatives.** Would a dashboard, segmentation, or a process change reach the same outcome? Would doing nothing be acceptable? Name what ML buys beyond these.

5. **Tally ML's lifetime cost.** Enumerate data acquisition/labeling, training, serving infra, monitoring, retraining cadence, and the human cost of errors and on-call. Contrast with the cost of the rules/analytics path.

6. **Surface the disqualifiers.** Flag any condition that makes ML the wrong tool here: too few examples, non-stationary process that can't be monitored, need for exact/auditable determinism, unacceptable error cost, or absence of a real decision.

7. **Render the recommendation with conditions.** Give a clear verdict — ML / rules / analytics / don't build / start with a baseline — and the specific conditions that would flip it.

**Output Format:**

A markdown decision brief:
- **Reframed Problem & Decision** — outcome, actor, action.
- **ML-Fit Signal Scorecard** — table: Signal | Present/Partial/Absent | Evidence.
- **Alternatives Comparison** — table: Approach | Est. Value Captured | Est. Lifetime Cost | Time-to-Value | Notes.
- **Disqualifiers Check** — any conditions that rule ML out, or "none found."
- **Recommendation** — verdict + the conditions that would change it.

## Verification

- [ ] The downstream decision/action is named (or its absence is flagged).
- [ ] All four ML-fit signals are scored with evidence, not assertion.
- [ ] At least three non-ML alternatives are compared.
- [ ] Lifetime (not just build) cost of ML is itemized.
- [ ] The recommendation states the conditions under which it would flip.
- [ ] Every quantitative claim is labeled fact vs assumption-to-validate.

## False-Positive Prevention

❌ **DON'T:**
- Recommend ML because the data is "big" — volume alone is not an ML-fit signal if a rule already separates the classes.
- Treat the absence of current rules as evidence that rules can't work; nobody may have tried.
- Assume labels exist because the data exists — most real problems are unlabeled.
- Compare ML's accuracy to nothing; an improvement claimed against no baseline is meaningless.
- Ignore the recurring cost of monitoring/retraining and present ML as a one-time build.

✅ **DO:**
- Demand a concrete baseline (majority class, simple rule, current process) as the bar ML must beat.
- Separate "a pattern exists" from "the pattern is too complex for rules" — only the latter favors ML.
- Require that the input distribution is stable or at least monitorable before recommending ML.
- Confirm a real decision consumes the output; kill prediction-for-prediction's-sake.
- Mark every accuracy/ROI/volume number as a fact (from input) or an assumption to validate.

## Example Output

```markdown
## ML-Fit Assessment: "Flag fraudulent refund requests"

### Reframed Problem & Decision
Outcome: reduce fraudulent refund payouts. Actor: refund-ops reviewer. Action: auto-approve, auto-deny, or route to manual review.

### ML-Fit Signal Scorecard
| Signal | Present/Partial/Absent | Evidence |
|---|---|---|
| Pattern too complex for rules | Partial | ~70% of fraud caught by 5 known rules today; remainder is adaptive |
| Sufficient representative labeled data | Partial | ~18 mo of labeled chargebacks; positives ~1.2% (assumption: label quality TBD) |
| Stable / monitorable distribution | Present | Fraud tactics shift but volume is monitorable weekly |
| Approximate answers acceptable | Present | Borderline cases route to humans; no need for exactness |

### Alternatives Comparison
| Approach | Est. Value Captured | Est. Lifetime Cost | Time-to-Value | Notes |
|---|---|---|---|---|
| Expert rules (current) | ~70% (assumption) | Low | Now | Misses adaptive fraud |
| Analytics / segmentation | ~70–75% | Low | Weeks | Surfaces patterns, doesn't auto-decide |
| ML on residual cases | rules + marginal lift | High (label, serve, monitor, retrain) | Months | Justified only if it beats rules on the hard 30% |
| Do nothing | 0 | 0 | — | Unacceptable given loss trend (assumption) |

### Disqualifiers Check
None disqualifying. Caveat: label quality and class imbalance must be validated before committing.

### Recommendation
Keep the rules as the baseline; pilot ML *only on cases the rules don't catch*, and require it to beat a rules-plus-threshold baseline on the hard residual by a pre-agreed margin. Flip to "rules only" if label quality proves too noisy to train on. (See `mlframe_baseline_first_design.md`.)
```

**Techniques Used:**
- **ST-01 (Clear Objective Statement):** forces the brief to a single verdict — ML or not.
- **RT-02 (Multi-Dimensional Analysis Framework):** compares ML across value/cost/time against alternatives.
- **CM-02 (Constraint Specification):** the real-decision and lifetime-cost constraints govern the verdict.
- **DS-06 (Prioritization & Severity Guidance):** ranks alternatives and disqualifiers by impact.
- **QA-12 (False Positives Identification):** guards against the reflex of choosing ML by default.

**Related Prompts:**
- `mlframe_ml_use_case_canvas.md` — once ML is justified, scope it on one page.
- `mlframe_baseline_first_design.md` — define the rules/heuristic bar ML must beat.
- `mlframe_feasibility_risk_assessment.md` — pressure-test feasibility before committing resources.
