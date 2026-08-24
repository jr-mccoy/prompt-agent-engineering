---
title: "Uncertainty Quantification Design"
category: AI-ML/model-evaluation-validation
description: "Design uncertainty estimates a downstream decision can actually use — separating aleatoric from epistemic uncertainty, choosing a method against the decision rather than the literature, and validating that the estimates are honest before anyone acts on them."
techniques:
  - RT-02
  - DS-02
  - CM-02
  - QA-12
  - RT-05
difficulty: advanced
tags:
  - uncertainty-quantification
  - epistemic-uncertainty
  - aleatoric-uncertainty
  - calibration
  - decision-support
updated: "2026-08-22"
related_prompts:
  - domain-AI-ML/model-evaluation-validation/mleval_conformal_prediction_design.md
  - domain-AI-ML/model-evaluation-validation/mleval_calibration_assessment.md
  - domain-AI-ML/model-evaluation-validation/mleval_selective_prediction_abstention.md
  - domain-AI-ML/model-evaluation-validation/mleval_ood_detection_design.md
---

# Uncertainty Quantification Design

**Objective:** Produce uncertainty estimates that change a downstream decision — starting from what the decision needs, separating irreducible noise from model ignorance, choosing a method on that basis, and validating that the estimates are honest before anything is allowed to depend on them.

**When to Use:**
- A downstream decision would differ if the model could say how sure it is — routing to a human, sizing an action, or abstaining.
- A model already emits confidence values and you need to know whether they mean anything.
- Deploying into a domain where the input distribution will drift and silent overconfidence is the failure mode.

**When NOT to Use:**
- Nothing downstream would act differently given an uncertainty estimate — build the plumbing only when a decision consumes it.
- You need a guaranteed coverage interval rather than an uncertainty score — use `mleval_conformal_prediction_design.md`.
- The question is whether existing probabilities are calibrated — use `mleval_calibration_assessment.md`.

## Inputs / Context

- **The decision consuming uncertainty** — exactly what changes at what threshold. Without this the design has no target.
- **Task type** — classification, regression, ranking, or generation; each has different available methods and failure modes.
- **Sources of irreducible noise** — label noise, measurement error, genuine ambiguity in the input.
- **Expected distribution shift** — whether inputs will move away from training data, which is what epistemic uncertainty is for.
- **Compute budget at inference** — several methods multiply inference cost, and this rules some out immediately.
- **Cost asymmetry** — the relative cost of a confident error versus an unnecessary abstention or escalation.

## Constraints

**Must:**
- Separate **aleatoric** (irreducible noise in the data) from **epistemic** (model ignorance, reducible with more data) uncertainty, and state which one the decision needs — they call for different methods and different responses.
- Start from the decision and the threshold it uses; an uncertainty number nobody acts on is instrumentation, not design.
- Validate estimates against outcomes before deployment: calibration on in-distribution data **and** behaviour on shifted data, since the whole point is behaviour when inputs move.
- State inference-cost multiplication for any ensemble or sampling method, against the stated budget.
- Report uncertainty quality per slice, because average calibration coexists with severe miscalibration in the subgroups that matter.

**Must Not:**
- Treat a softmax maximum as an uncertainty estimate; it is a normalized score that is frequently high on inputs the model has never seen.
- Assert calibration-error figures, method-comparison results, or ensemble-size recommendations from memory; mark quantities `[measure on your data]`.
- Report only in-distribution calibration — that is the regime where uncertainty matters least and every method looks acceptable.
- Present epistemic uncertainty as detecting all out-of-distribution inputs; it detects some, and confidently fails on others.
- Recommend a method whose inference cost exceeds the stated budget without saying so.

**Instructions:**

1. **Write the decision and its threshold.** What changes, at what uncertainty level, with what consequence. This is the specification; everything else is chosen to serve it.

2. **Decide which uncertainty the decision needs.** If the decision is "escalate ambiguous cases to a human", that is largely aleatoric. If it is "refuse to predict on inputs unlike anything we trained on", that is epistemic. Many designs fail because they measure one and act as though they had the other.

3. **Enumerate irreducible noise.** Label noise rate, measurement error, and genuinely ambiguous inputs. This sets the floor: no method reduces aleatoric uncertainty, and a design that promises to is mis-specified.

4. **Screen methods against task, budget, and the uncertainty type needed.**
   - *Calibrated probabilities* — cheap, aleatoric, classification. The baseline; try it before anything else.
   - *Deep ensembles* — both types, strong, cost multiplies with ensemble size.
   - *Monte Carlo dropout* — approximate epistemic, moderate cost, quality varies by architecture.
   - *Quantile or distributional regression* — aleatoric for regression, cheap, gives intervals directly.
   - *Bayesian last layer / Laplace approximation* — epistemic at modest cost.
   - *Distance-to-training-data measures* — epistemic proxy, very cheap, degrades in high dimensions.

5. **Validate in distribution.** Calibration curves and a scalar calibration measure, overall and per slice. Note that good calibration on the training distribution is necessary and nowhere near sufficient.

6. **Validate under shift — the decisive test.** Construct or collect shifted data and check that uncertainty *rises*. A method whose confidence stays high as inputs move away from training data is worse than no uncertainty estimate, because it will be trusted.

7. **Set the threshold from cost asymmetry.** Convert the cost of a confident error and of an unnecessary escalation into a threshold, and report the resulting escalation rate at that threshold. Check the rate against the capacity of whoever receives escalations.

8. **Define the monitoring.** Uncertainty distribution drift, escalation-rate drift, and realized accuracy within confidence bands — the last is the one that tells you the estimates have stopped being honest.

**Output Format:**

A markdown design:
- **Decision & Threshold** — what changes, at what level, with what consequence.
- **Uncertainty Type Needed** — aleatoric, epistemic, or both, with the reason.
- **Irreducible Noise** — sources and the resulting floor.
- **Method Screening** — table: Method | Type | Task fit | Inference cost | Verdict.
- **In-Distribution Validation** — calibration overall and per slice.
- **Shift Validation** — shifted sets used, and whether uncertainty rose.
- **Threshold & Escalation Rate** — derived from cost asymmetry, checked against capacity.
- **Monitoring** — signals and what degradation looks like.

## Verification

- [ ] The consuming decision and its threshold are stated before any method is chosen.
- [ ] Aleatoric and epistemic are separated, and the design targets the one the decision needs.
- [ ] Irreducible noise sources are enumerated and set an explicit floor.
- [ ] Inference-cost multiplication is stated per method and checked against budget.
- [ ] Calibration is reported per slice, not only in aggregate.
- [ ] Behaviour under shift is validated and reported, not assumed.
- [ ] The threshold is derived from cost asymmetry and its escalation rate checked against capacity.
- [ ] Monitoring includes realized accuracy within confidence bands.
- [ ] No calibration or method-comparison figures are asserted from memory.

## False-Positive Prevention

❌ **DON'T:**
- Use the softmax maximum as confidence — it is routinely high on inputs the model has never seen, which is precisely the case the design exists to catch.
- Validate only in distribution and ship; every method looks acceptable there, and the regime that matters is the one you skipped.
- Report a single aggregate calibration number when a subgroup is badly miscalibrated — the average is dominated by the majority slice.
- Promise that uncertainty estimates will reduce ambiguity that is aleatoric; irreducible noise is irreducible, and the model can only report it.
- Choose an ensemble because it performs best in comparisons without pricing the inference-cost multiple against the budget.
- Set the escalation threshold to a round number and discover the escalation volume in production.

✅ **DO:**
- Start from the decision, and build only the uncertainty it will consume.
- Name which uncertainty type the decision needs and choose the method for that type.
- Quantify the noise floor first, so the design does not promise to reduce it.
- Test under shift and treat rising uncertainty as the acceptance criterion.
- Report calibration per slice and lead with the worst.
- Derive the threshold from cost asymmetry and confirm the escalation rate fits the receiving team's capacity.

## Example Output

```markdown
## Uncertainty Design: Insurance Claim Auto-Approval

### Decision & Threshold
Claims below a confidence threshold route to a human adjuster instead of auto-approving.
Consequence of a confident error: an incorrect payout, occasionally large. Consequence of an
unnecessary escalation: ~9 minutes of adjuster time.

### Uncertainty Type Needed
**Both, for different reasons.** Aleatoric: genuinely ambiguous claims (incomplete
documentation, contested facts) should escalate. Epistemic: novel claim types not in the
training window should escalate even when they look confidently classifiable — this is the case
a calibrated-probability-only design would miss entirely.

### Irreducible Noise
Adjuster label agreement on a re-labelled sample: 0.87 — so roughly 13% of claims are genuinely
ambiguous to experts. **No method reduces this**; the design's job is to surface it rather than
to promise it away. Any escalation-rate target below ~13% is unachievable without confident errors.

### Method Screening
| Method | Type | Task fit | Inference cost | Verdict |
|---|---|---|---|---|
| Calibrated probabilities (isotonic) | aleatoric | good | 1× | **Adopt as baseline** |
| Deep ensemble (5×) | both | good | **5×** | Reject — exceeds the per-claim latency budget |
| MC dropout (20 samples) | epistemic (approx) | moderate | 20× | Reject — cost |
| Bayesian last layer | epistemic | good | ~1.1× | **Adopt** — the epistemic signal at affordable cost |
| Distance to training data | epistemic proxy | good on tabular | ~1× | **Adopt** — cheap second signal, cross-checks the above |

### In-Distribution Validation
| Slice | ECE | Notes |
|---|---|---|
| Overall | `[measure]` | — |
| Auto claims | `[measure]` | majority slice, dominates the aggregate |
| Property claims | `[measure]` | — |
| Commercial claims (n small) | `[measure]` | **watch** — aggregate hides this |

The commercial slice is reported separately because it is small, high-value, and would be
invisible in the overall number.

### Shift Validation — the decisive test
Shifted sets: claims from a product line launched after the training cutoff; claims from a
region added post-training; and a synthetic set with a documentation format the model never saw.
**Acceptance criterion: mean epistemic uncertainty must rise materially on all three.** If
confidence stays high on the post-cutoff product line, the epistemic signal is not working and
auto-approval must be disabled for that line regardless of measured accuracy.

### Threshold & Escalation Rate
Cost asymmetry: a confident error costs roughly two orders of magnitude more than 9 minutes of
adjuster time `[verify against your own loss data]`, so the threshold is set conservatively.
Resulting escalation rate must be checked against adjuster capacity — if the threshold implies
more escalations than the team can absorb, the answer is a staged rollout by claim type, not a
looser threshold.

### Monitoring
- Uncertainty distribution drift, weekly, per claim type.
- Escalation rate vs adjuster capacity — a rising rate is an early shift signal, not just a
  staffing problem.
- **Realized accuracy within each confidence band** — the signal that tells you the estimates
  have stopped being honest. If the top band's accuracy falls, everything downstream is
  mis-trusting the model, and auto-approval should halt before the next retrain.
```

**Techniques Used:**
- **RT-02 (Multi-Dimensional Analysis Framework):** uncertainty type × method × cost × validation regime is the design grid.
- **DS-02 (Metric Specification):** calibration, escalation rate, and the noise floor are specified as measured quantities.
- **CM-02 (Constraint Specification):** the decision-first rule and the shift-validation requirement bound the design.
- **QA-12 (False Positives Identification):** rejects softmax-as-confidence and in-distribution-only validation.
- **RT-05 (Evidence-Based Reasoning):** the threshold follows from measured cost asymmetry rather than convention.

**Related Prompts:**
- `mleval_conformal_prediction_design.md` — when a coverage guarantee is required rather than a score.
- `mleval_calibration_assessment.md` — the calibration measurement this design depends on.
- `mleval_selective_prediction_abstention.md` — designing the abstention behaviour this feeds.
- `mleval_ood_detection_design.md` — a dedicated treatment of the shift case.
