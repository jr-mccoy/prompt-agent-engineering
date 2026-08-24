---
title: "RAI Fairness Mitigation Strategy"
category: AI-ML/responsible-ai-governance
description: "Choose a pre-, in-, or post-processing bias mitigation under a stated fairness definition, and measure its accuracy-fairness tradeoff with slice-level evidence rather than asserting it worked."
techniques:
  - RT-02
  - ST-02
  - DS-02
  - QA-12
  - DS-06
difficulty: advanced
tags:
  - fairness
  - bias-mitigation
  - accuracy-fairness-tradeoff
  - pre-in-post-processing
  - responsible-ai
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/responsible-ai-governance/rai_bias_detection_audit.md
  - domain-AI-ML/responsible-ai-governance/rai_fairness_metric_selection.md
  - domain-AI-ML/responsible-ai-governance/rai_model_card_authoring.md
---

# RAI Fairness Mitigation Strategy

**Objective:** Given a confirmed disparity under a stated fairness definition, select an appropriate mitigation — pre-processing (data), in-processing (training objective), or post-processing (thresholds/scores) — and measure its effect on both the fairness gap and predictive performance per slice, so the team accepts a documented tradeoff rather than a claimed fix.

**When to Use:**
- After `rai_bias_detection_audit.md` has confirmed a material, evidenced disparity.
- When choosing between mitigation families and needing to justify the choice.
- When a prior mitigation needs its tradeoff re-measured after retraining or drift.

**When NOT to Use:**
- Before a disparity is confirmed with slice evidence — don't mitigate noise.
- To pick the fairness definition itself — use `rai_fairness_metric_selection.md`.

## Inputs / Context

- **Confirmed disparity** — the metric gap, the groups/intersections affected, sample sizes, and the stated fairness definition it violates.
- **Constraints** — whether the protected attribute may be used at training/inference time (legal/ethical), latency, retraining cost.
- **Pipeline access** — can you change the data, the training objective, or only the post-hoc decision layer?
- **Baseline performance** — current per-slice accuracy/utility metrics to compare against.
- **Regulation/framework in scope** — if any (ask the user; some jurisdictions restrict using the protected attribute in mitigation).

## Constraints

**Must:**
- Restate the fairness definition being optimized and the slices in scope before recommending any technique.
- Report the mitigation's effect on BOTH the fairness gap AND per-slice performance, with intervals, on a held-out set not used to tune the mitigation.
- Present the result as a tradeoff (what improved, what regressed, for whom).

**Must Not:**
- Claim a mitigation "fixed bias" from the training/validation set it was tuned on, or from aggregate metrics.
- Recommend a post-processing threshold adjustment that uses the protected attribute at inference without flagging the legal/ethical question (ask the user about the jurisdiction; do not assume it is allowed).
- Fabricate the expected magnitude of improvement; estimate from the user's data or mark it unknown.

**Instructions:**

1. **Restate the target.** Name the fairness definition, the affected slices, and the current gap with its interval. Confirm it is a real disparity, not noise.

2. **Determine the feasible lever.** Establish which family is available: pre-processing (reweighing, resampling, relabeling), in-processing (constrained/adversarial training), or post-processing (group-aware thresholds, score calibration). Rule out levers the constraints forbid.

3. **Map candidate techniques to the lever and definition.** For each feasible technique, state what it changes and which fairness definition it naturally serves.

4. **Flag the protected-attribute question.** State clearly whether the candidate needs the protected attribute at inference, and that this may be legally/ethically restricted — defer to the user's confirmed jurisdiction.

5. **Define the measurement protocol.** Specify a held-out set, the per-slice metrics, and the intervals you will compute to judge the tradeoff. The set tuning the mitigation must differ from the set judging it.

6. **Estimate / measure the tradeoff.** Report the change in the fairness gap and the change in per-slice utility. State who gains and who absorbs any regression.

7. **Recommend and bound the choice.** Recommend the technique whose tradeoff is acceptable under the stated harm priorities, and define monitoring tripwires for drift back toward disparity.

**Output Format:**

A markdown strategy memo:
- **Target Restated** — definition, slices, current gap.
- **Feasible Levers** — which families are usable, which are ruled out and why.
- **Candidate Techniques** — table: Technique | Lever | Definition served | Needs protected attr at inference? | Notes.
- **Measurement Protocol** — held-out set, metrics, intervals.
- **Tradeoff Result** — gap change + per-slice utility change + who gains/regresses.
- **Recommendation & Tripwires** — chosen technique, residual risk, monitoring triggers.

## Verification

- [ ] The fairness definition and affected slices are restated before any technique.
- [ ] Each candidate is mapped to a lever and to the definition it serves.
- [ ] The protected-attribute-at-inference question is explicitly flagged.
- [ ] Effect is measured on a held-out set, per slice, with intervals — not the tuning set.
- [ ] The result is framed as a tradeoff (gains AND regressions), not a "fix."
- [ ] Any legal restriction on using the protected attribute is user-confirmed, not assumed.

## False-Positive Prevention

❌ **DON'T:**
- Declare bias "removed" from the same data used to tune the mitigation.
- Report only the closed fairness gap while hiding the accuracy or utility cost.
- Apply group-aware thresholds without raising the legal/ethical question of using the protected attribute.
- Assume a pre-processing reweighing will hold after distribution shift.

✅ **DO:**
- Measure the tradeoff on a fresh held-out set, per slice, with intervals.
- Report what regressed and for whom alongside what improved.
- Surface the protected-attribute-at-inference constraint and defer to confirmed jurisdiction.
- Set tripwires so re-emergence of the gap is caught.

## Example Output

```markdown
## Fairness Mitigation Strategy: Resume Screening Model v2

### Target Restated
Definition: equal opportunity (TPR). Affected slice: Group B (TPR gap −0.11, CI [−0.14,−0.08]). Confirmed material.

### Feasible Levers
- Pre-processing: available (we own the training data).
- In-processing: available (custom training loop).
- Post-processing group-aware thresholds: technically available BUT using the protected attribute at inference may be legally restricted — user to confirm jurisdiction.

### Candidate Techniques
| Technique | Lever | Definition served | Needs protected attr at inference? | Notes |
|---|---|---|---|---|
| Reweighing | Pre | Equal opportunity-ish | No | Simple, may not fully close gap |
| Adversarial debiasing | In | Equalized odds | No (at inference) | Heavier to train/tune |
| Group thresholds | Post | Equal opportunity (exact) | Yes | Legal flag |

### Measurement Protocol
Held-out fairness set (untouched by tuning). Metrics: per-slice TPR, FPR, precision; 95% CIs.

### Tradeoff Result (adversarial debiasing)
- TPR gap: −0.11 → −0.03 (CI [−0.05,−0.01]).
- Overall accuracy: 0.86 → 0.845 (CI overlap). Group A precision −0.01; Group B recall +0.07.
- Who gains: qualified Group B candidates. Who regresses: small precision cost across groups.

### Recommendation & Tripwires
Adopt adversarial debiasing (avoids protected attr at inference, closes most of the gap). Tripwire: re-audit if TPR gap CI upper bound exceeds −0.05 in monthly monitoring.
```

**Techniques Used:**
- **RT-02 (Multi-Dimensional Analysis Framework):** compares mitigation families across feasibility and definition served.
- **ST-02 (Structured Sequential Instructions):** target → lever → candidate → measure → choose.
- **DS-02 (Metric Specification):** defines the per-slice held-out measurement.
- **QA-12 (False Positives Identification):** blocks "fixed it" claims from tuning-set or aggregate metrics.
- **DS-06 (Prioritization & Severity Guidance):** weighs tradeoffs against harm priorities.

**Related Prompts:**
- `rai_bias_detection_audit.md` — confirm the disparity before mitigating.
- `rai_fairness_metric_selection.md` — the definition this strategy optimizes.
- `rai_model_card_authoring.md` — record the mitigation and its tradeoff.
