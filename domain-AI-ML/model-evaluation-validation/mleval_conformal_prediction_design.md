---
title: "Conformal Prediction Design"
category: AI-ML/model-evaluation-validation
description: "Design conformal prediction sets or intervals with a coverage guarantee that survives deployment — checking the exchangeability assumption the guarantee rests on, choosing a score function that produces useful set sizes, and reporting conditional coverage rather than marginal alone."
techniques:
  - ST-02
  - DS-02
  - CM-02
  - QA-12
  - RT-05
difficulty: advanced
tags:
  - conformal-prediction
  - coverage-guarantee
  - prediction-sets
  - exchangeability
  - distribution-free
updated: "2026-08-22"
related_prompts:
  - domain-AI-ML/model-evaluation-validation/mleval_uncertainty_quantification_design.md
  - domain-AI-ML/model-evaluation-validation/mleval_selective_prediction_abstention.md
  - domain-AI-ML/model-evaluation-validation/mleval_calibration_assessment.md
  - domain-AI-ML/specialized-ml/time-series/ts_probabilistic_forecasting.md
---

# Conformal Prediction Design

**Objective:** Design conformal prediction sets or intervals whose coverage guarantee still holds where it is used — verifying the exchangeability assumption the guarantee depends on, choosing a score function that yields sets a decision-maker can act on, and reporting conditional coverage rather than the marginal number that hides the failures.

**When to Use:**
- A downstream process needs a set or interval with a stated coverage level, rather than a confidence score.
- A regulator, clinician, or operator asks "how often is the true answer inside what you gave me?" and that must be answerable.
- Existing probability estimates are unreliable and you want a guarantee that does not depend on them being well calibrated.

**When NOT to Use:**
- The decision consumes a single point prediction plus a confidence score — use `mleval_uncertainty_quantification_design.md`.
- Exchangeability is clearly violated and no adaptive variant is available — say so; a guarantee that does not hold is worse than an honest score.
- You need to abstain rather than to emit a set — use `mleval_selective_prediction_abstention.md`, which may consume this.

## Inputs / Context

- **Consumer and required coverage** — who receives the set, and the coverage level the use demands.
- **Task type** — classification (sets), regression (intervals), or something with structured output.
- **Calibration data** — a held-out set not used for training or model selection, with its size.
- **Deployment distribution vs calibration distribution** — how similar, and whether shift is expected over time.
- **Usable set size** — the size beyond which the output stops helping the consumer; a 40-class set is technically valid and operationally useless.
- **Whether coverage must hold per subgroup**, which is a much stronger requirement than overall coverage.

## Constraints

**Must:**
- State the **exchangeability assumption** explicitly and assess whether it holds between calibration and deployment data — the guarantee rests entirely on it, and this is the step most often skipped.
- Use calibration data untouched by training, hyperparameter selection, or threshold tuning; reusing any of it voids the guarantee silently.
- Report **conditional coverage** — per class, per subgroup, per difficulty band — alongside marginal coverage, since marginal coverage is routinely met while some subgroup is badly under-covered.
- Report set-size distribution, not only mean, and state what fraction exceed the usable-size limit.
- State what invalidates the guarantee in deployment: distribution shift, temporal dependence, or model retraining without recalibration.

**Must Not:**
- Present marginal coverage as though it were per-subgroup coverage; a system can hit 90% overall while covering one group at 60%.
- Assert coverage results, calibration-set-size rules, or method comparisons from memory; mark quantities `[measure on your data]`.
- Apply standard conformal prediction to time series or any dependent data without addressing the exchangeability violation and naming the adaptive variant used.
- Report a guarantee as holding after the model is retrained unless recalibration happened on fresh held-out data.
- Describe large, uninformative sets as a success because coverage was achieved; coverage with unusable sets is a failed design.

**Instructions:**

1. **Fix the consumer, the coverage level, and the usable set size.** All three together — coverage alone is trivially satisfiable by returning everything, and the usable-size limit is what makes the design non-trivial.

2. **Test the exchangeability assumption.** Are calibration and deployment data plausibly exchangeable? Named violations to check: temporal ordering, per-user grouping, site or batch effects, and any shift between when calibration data was collected and when the model runs. If violated, either use an adaptive variant designed for the violation or state plainly that the guarantee is not available.

3. **Isolate the calibration set.** Confirm it was not used for training, model selection, early stopping, or threshold tuning. Record its size and state the resolution that size permits — a small calibration set makes fine coverage levels unattainable.

4. **Choose the score function against set size.** The score determines how informative the sets are at a given coverage. For classification, compare a simple softmax-based score with an adaptive one; for regression, compare a fixed-width residual score with a normalized one that adapts to local difficulty. Choose on measured set size at the required coverage, not on convention.

5. **Calibrate and measure marginal coverage.** Confirm empirical coverage on a fresh test set matches the target.

6. **Measure conditional coverage — the decisive step.** Break coverage out by class, subgroup, and difficulty band. Under-covered groups are the finding, and they are invisible in the marginal number.

7. **Measure set-size distribution.** Report the distribution, the fraction exceeding the usable limit, and which inputs produce the largest sets — usually the ones the model finds hardest, which are often the ones the consumer most needs help with.

8. **Decide the response to large sets.** Emit them, cap and flag them, or route to abstention. This connects the design to the operational path.

9. **Define recalibration triggers.** Model retraining, elapsed time, detected shift, or observed coverage drift. State who owns the recalibration and what happens between detection and recalibration.

**Output Format:**

A markdown design:
- **Consumer, Coverage Target, Usable Set Size** — all three.
- **Exchangeability Assessment** — violations checked, verdict, adaptive variant if needed.
- **Calibration Set** — provenance, size, resolution permitted.
- **Score Function Comparison** — table: Score | Coverage achieved | Mean set size | % over usable limit.
- **Marginal Coverage** — measured against target.
- **Conditional Coverage** — table: Group | Coverage | Verdict.
- **Set-Size Distribution** — distribution and the inputs producing the largest sets.
- **Large-Set Handling** — the operational response.
- **Recalibration Triggers** — conditions, owner, interim behaviour.

## Verification

- [ ] Coverage target and usable set size are both stated; neither alone is a specification.
- [ ] Exchangeability is assessed against named violation types, with a verdict.
- [ ] The calibration set is confirmed untouched by training or tuning, and its size is stated.
- [ ] Score functions are compared on set size at the required coverage.
- [ ] Conditional coverage is reported per class and per subgroup.
- [ ] Set-size distribution is reported, not only the mean.
- [ ] The handling of large sets is defined operationally.
- [ ] Recalibration triggers name an owner and the interim behaviour.
- [ ] No coverage or calibration-size figures are asserted from memory.

## False-Positive Prevention

❌ **DON'T:**
- Report 90% marginal coverage as "90% coverage for every user" — marginal and conditional coverage are different claims and only one of them is guaranteed.
- Reuse validation data for calibration because it is conveniently available; the guarantee is void and nothing in the output will show it.
- Apply standard conformal prediction to time-ordered data — exchangeability fails, and the resulting guarantee is a statement about a world you are not operating in.
- Celebrate a design whose sets contain half the label space; it is valid, and it tells the consumer nothing.
- Keep serving conformal sets after a model retrain without recalibrating; the score distribution moved and the guarantee went with it.
- Choose the score function by convention when a different one gives materially smaller sets at the same coverage.

✅ **DO:**
- Specify coverage and usable set size together, so the design has a real constraint.
- Name the exchangeability violations you checked and the verdict for each.
- Keep the calibration set clean and state the resolution its size allows.
- Report conditional coverage per subgroup and treat under-coverage as the headline finding.
- Report the set-size distribution and identify what produces the largest sets.
- Trigger recalibration on retraining and on drift, with a named owner and defined interim behaviour.

## Example Output

```markdown
## Conformal Design: Dermatology Triage Support (38 conditions)

### Consumer, Coverage Target, Usable Set Size
Consumer: a general practitioner deciding whether to refer. Required coverage: **90%** — the
true condition must be in the returned set 9 times in 10. **Usable set size: ≤4.** Beyond four
conditions the GP reports the set stops narrowing the decision, so a valid-but-large set is a
failed output, not a conservative one.

### Exchangeability Assessment
| Violation type | Present? | Handling |
|---|---|---|
| Temporal ordering | Mild — imaging hardware upgraded mid-collection | calibrate on post-upgrade data only |
| Per-patient grouping | **Yes** — some patients contribute multiple images | group-aware split; one image per patient in calibration |
| Site effects | **Yes** — 6 clinics, different lighting | assessed per site; see conditional coverage |
| Calibration-to-deployment shift | Expected seasonally | recalibration trigger below |

Verdict: exchangeability holds **within site and post-upgrade**, after the per-patient grouping
fix. Without that fix the calibration set would contain near-duplicates of test images and the
guarantee would have been optimistic in a way nothing in the output would reveal.

### Calibration Set
Post-upgrade images, one per patient, no overlap with training or model selection. Size
`[record yours]`. Note that the required resolution at 90% coverage sets a minimum size —
`[compute the minimum for your target before relying on the guarantee]`.

### Score Function Comparison
| Score | Coverage achieved | Mean set size | % over 4 |
|---|---|---|---|
| Softmax-threshold | `[measure]` | `[measure]` | `[measure]` |
| Adaptive (cumulative) | `[measure]` | `[measure]` | `[measure]` |

Choose on the last two columns at equal coverage — both will hit the coverage target by
construction, so set size is the only discriminator that matters.

### Conditional Coverage
| Group | Coverage | Verdict |
|---|---|---|
| Overall (marginal) | 0.90 | meets target |
| Clinic A–D | ~0.90 | fine |
| **Clinic E** (newest, different lighting) | **0.78** | **under-covered — the finding** |
| Common conditions | 0.93 | fine |
| **Rare conditions (<50 train)** | **0.71** | **under-covered** |

Marginal coverage is exactly on target while two groups sit well below it. Reporting only the
marginal number here would have concealed both — including the rare-condition group, which is
the group a triage aid most needs to get right.

### Set-Size Distribution
Report the full distribution rather than the mean. Largest sets concentrate on rare conditions
and on Clinic E images — the same groups that are under-covered, so those inputs are both less
reliable and less informative at once.

### Large-Set Handling
Sets exceeding 4 are **not** returned as a list. They return "insufficient confidence — refer
for specialist assessment", which is the honest rendering of a set the GP cannot use. This
converts an unusable output into an actionable one.

### Recalibration Triggers
- Any model retrain — mandatory, on fresh held-out data.
- New clinic onboarded — Clinic E is the reason this trigger exists.
- Observed coverage drift below 0.87 on the rolling monitor.
- Scheduled every 6 months regardless.
Owner: the clinical ML lead. Between detection and recalibration, the affected site falls back
to the "refer" path rather than continuing to serve sets whose guarantee is unverified.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** exchangeability is tested before calibration, which precedes any coverage claim.
- **DS-02 (Metric Specification):** coverage, set size, and the usable limit are specified together as the joint acceptance criterion.
- **CM-02 (Constraint Specification):** clean-calibration-data and conditional-coverage rules bound what may be claimed.
- **QA-12 (False Positives Identification):** rejects marginal coverage presented as conditional and valid-but-unusable sets presented as success.
- **RT-05 (Evidence-Based Reasoning):** the guarantee is stated with the assumptions it depends on attached.

**Related Prompts:**
- `mleval_uncertainty_quantification_design.md` — when a score suffices and no guarantee is needed.
- `mleval_selective_prediction_abstention.md` — the abstention path large sets route into.
- `mleval_calibration_assessment.md` — complementary check on the underlying probabilities.
- `../specialized-ml/time-series/ts_probabilistic_forecasting.md` — the time-series case, where exchangeability needs an adaptive variant.
