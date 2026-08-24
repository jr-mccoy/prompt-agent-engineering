---
title: "Out-of-Distribution Detection Design"
category: AI-ML/model-evaluation-validation
description: "Design detection for inputs the model should not be trusted on — defining what counts as out-of-distribution for this deployment, evaluating against near-OOD rather than only obvious cases, and setting the threshold from the cost of an undetected input rather than from an AUROC."
techniques:
  - RT-02
  - DS-02
  - QA-12
  - CM-02
  - RT-10
difficulty: advanced
tags:
  - ood-detection
  - distribution-shift
  - novelty-detection
  - near-ood
  - operational-threshold
updated: "2026-08-22"
related_prompts:
  - domain-AI-ML/model-evaluation-validation/mleval_uncertainty_quantification_design.md
  - domain-AI-ML/model-evaluation-validation/mleval_selective_prediction_abstention.md
  - domain-AI-ML/production-monitoring/mlmonitor_drift_detection_design.md
  - domain-AI-ML/specialized-ml/other-modalities/mlmodal_anomaly_outlier_detection.md
---

# Out-of-Distribution Detection Design

**Objective:** Build detection for inputs this model should not be trusted on — defining out-of-distribution operationally rather than abstractly, evaluating against the near-OOD cases that actually arrive, and setting the operating threshold from the cost of missing one rather than from a summary score.

**When to Use:**
- The model will meet inputs unlike its training data, and a confident wrong answer on those is costly.
- A new segment, product line, geography, or sensor is being onboarded and you need to know whether the model covers it.
- Uncertainty estimates are already in place but confident errors on novel inputs persist.

**When NOT to Use:**
- The task *is* anomaly detection as the product — use `../specialized-ml/other-modalities/mlmodal_anomaly_outlier_detection.md`.
- The question is population-level drift over time rather than per-input novelty — use `../production-monitoring/mlmonitor_drift_detection_design.md`.
- No action follows detection; building a detector nothing consumes is instrumentation, not a control.

## Inputs / Context

- **What action follows detection** — reject, escalate, fall back, or log. This determines the acceptable false-positive rate more than anything else.
- **Realistic OOD examples** — actual inputs the deployment will meet that are unlike training data, ideally sampled from history rather than imagined.
- **Training distribution characterization** — what the model was trained on, including the slices it saw thinly.
- **Cost of an undetected OOD input** — a confident wrong answer on a novel input, and what it triggers downstream.
- **Cost of a false alarm** — an in-distribution input wrongly rejected or escalated.
- **Model access** — whether the detector can use internal features, logits, or only outputs.

## Constraints

**Must:**
- Define out-of-distribution **operationally for this deployment** — a specific list of what should be flagged and what should not — rather than as an abstract notion. Without this the detector has no target and cannot be evaluated.
- Evaluate against **near-OOD** cases: inputs similar to training data but from a different population, product, or period. Far-OOD is easy and evaluating on it alone overstates readiness.
- Set the operating threshold from the cost ratio between a missed detection and a false alarm, and report the resulting rates at that threshold rather than a summary score.
- Report per-source performance, since a detector can be strong on one kind of novelty and blind to another.
- Define the fallback behaviour for detected inputs, since a detection with no action is a log entry.

**Must Not:**
- Report AUROC as the design's conclusion — it summarizes across thresholds you will never use, and the operating point is what determines behaviour.
- Assert detector-comparison results, benchmark figures, or method rankings from memory; mark quantities `[measure on your data]`.
- Evaluate only against obviously different inputs and conclude the detector works; the failures that matter are near-OOD.
- Treat low model confidence as OOD detection — confidence is often *high* on novel inputs, which is the failure mode motivating the work.
- Deploy a detector whose false-alarm rate exceeds what the fallback path can absorb.

**Instructions:**

1. **Write the operational definition.** Two lists: inputs that must be flagged (with examples), and inputs that must not be (with examples). This is the specification, and constructing it usually surfaces disagreement worth resolving before any modelling.

2. **Assemble evaluation sets by distance.** *Far-OOD*: obviously different. *Near-OOD*: same task, adjacent population — a new region, a new product line, a new device, a later period. *In-distribution hard cases*: genuinely difficult but covered inputs that must **not** be flagged. The third set is what prevents a detector that simply flags everything difficult.

3. **Characterize the training distribution.** Including the slices seen thinly — inputs from a slice with few training examples are partially OOD already, and the detector should be assessed on whether it reflects that.

4. **Screen detector families against model access and cost.**
   - *Output-based* (max probability, entropy) — cheapest, weakest, and often high-confidence exactly on novel inputs.
   - *Feature-space distance* (distance to training features) — strong for near-OOD, needs internal access.
   - *Reconstruction-based* — useful where a generative model of the input exists.
   - *Trained OOD classifier* — strong on the novelty types represented in training, and blind to the rest, which is the trap.
   - *Ensemble disagreement* — strong signal, multiplies inference cost.

5. **Evaluate per source, not pooled.** Report detection rate for each near-OOD source separately. A detector strong on new-geography inputs and blind to new-device inputs has a good pooled number and a specific operational hole.

6. **Set the threshold from cost.** Convert the miss cost and false-alarm cost into an operating point. Report detection rate and false-alarm rate *at that point*, and check the false-alarm volume against the fallback path's capacity.

7. **Define fallback behaviour.** What the system does with a flagged input: refuse, route to a human, use a simpler robust model, or serve with a warning. Different sources may warrant different responses.

8. **Plan for the known blind spot.** Every detector misses some novelty type. Name the type this design is expected to miss and state the compensating control — usually monitoring realized accuracy on new segments after onboarding.

9. **Define maintenance.** When yesterday's OOD becomes today's in-distribution, the detector must be updated, or it will keep flagging a segment the model now handles.

**Output Format:**

A markdown design:
- **Operational Definition** — must-flag and must-not-flag lists with examples.
- **Evaluation Sets** — far-OOD, near-OOD sources, in-distribution hard cases.
- **Detector Screening** — table: Family | Model access needed | Cost | Near-OOD strength | Verdict.
- **Per-Source Results** — table: Source | Detection rate at threshold | Notes.
- **Threshold Derivation** — cost ratio, operating point, false-alarm volume vs capacity.
- **Fallback Behaviour** — per source where they differ.
- **Known Blind Spot** — what this misses and the compensating control.
- **Maintenance** — when the detector is updated.

## Verification

- [ ] An operational must-flag / must-not-flag definition exists with examples.
- [ ] Near-OOD sets are used, not only far-OOD.
- [ ] In-distribution hard cases are included to catch a difficulty detector masquerading as an OOD detector.
- [ ] Results are reported per source, not pooled.
- [ ] The threshold is derived from the cost ratio, and rates are reported at that operating point.
- [ ] False-alarm volume is checked against fallback capacity.
- [ ] Fallback behaviour is defined for every flagged source.
- [ ] A known blind spot is named with a compensating control.
- [ ] No AUROC is presented as the conclusion; no benchmark figures are asserted from memory.

## False-Positive Prevention

❌ **DON'T:**
- Report AUROC and stop — it averages over thresholds you will never operate at, and says nothing about the point you will.
- Validate on obviously different inputs and declare readiness; the inputs that cause harm resemble training data closely enough to be scored confidently.
- Use low model confidence as the detector when the motivating problem is *high* confidence on novel inputs.
- Omit in-distribution hard cases and ship a detector that flags every difficult input — it will look excellent on OOD sets and drown the fallback path.
- Pool near-OOD sources into one number and hide that the detector is blind to an entire novelty type.
- Set the threshold where the ROC curve looks best rather than where the cost ratio puts it.

✅ **DO:**
- Write the must-flag and must-not-flag lists first, and resolve disagreement about them before modelling.
- Build near-OOD sets from real adjacent populations — a new region, device, or period.
- Include hard in-distribution cases so a difficulty detector cannot pass as a novelty detector.
- Report detection per source and treat a blind source as an operational hole.
- Derive the operating point from miss cost versus false-alarm cost, then check the volume against capacity.
- Name the novelty type you expect to miss, and put a monitoring control behind it.

## Example Output

```markdown
## OOD Detection Design: Equipment Failure Prediction (industrial sensors)

### Operational Definition
**Must flag:** readings from a sensor model not in training; readings from a machine type never
seen; readings after a firmware change that alters the sampling rate; readings during a plant
configuration the model was not trained on.
**Must NOT flag:** genuinely unusual but covered conditions — startup transients, seasonal
temperature extremes, and known fault signatures. These are hard, not novel, and flagging them
would suppress exactly the predictions the system exists to make.

Building these two lists surfaced a disagreement between the reliability and data teams about
whether startup transients were "novel" — resolving it before modelling was worth more than the
detector itself.

### Evaluation Sets
| Set | Construction |
|---|---|
| Far-OOD | readings from a different plant's process entirely |
| Near-OOD A | **new sensor model**, same machine type |
| Near-OOD B | **same sensor, post-firmware** sampling-rate change |
| Near-OOD C | machine type added after training cutoff |
| In-dist hard | startup transients + known fault signatures |

### Detector Screening
| Family | Access needed | Cost | Near-OOD strength | Verdict |
|---|---|---|---|---|
| Max probability | outputs only | 1× | weak — high confidence on novel inputs | **Reject** |
| Feature-space distance | penultimate layer | ~1× | strong | **Adopt** |
| Reconstruction error | requires generative model | 2× | moderate | Hold — no generative model today |
| Trained OOD classifier | training data + OOD examples | 1× | strong on represented types only | **Reject** — blind to unrepresented novelty, which is the whole point |
| Ensemble disagreement | 4× inference | 4× | strong | Reject — cost on edge hardware |

### Per-Source Results
| Source | Detection at threshold | Notes |
|---|---|---|
| Far-OOD | `[measure]` | expected near-total; not informative |
| Near-OOD A (new sensor) | `[measure]` | primary target |
| **Near-OOD B (firmware)** | `[measure — expected weakest]` | same physical sensor; feature distance may be small |
| Near-OOD C (new machine type) | `[measure]` | primary target |
| In-dist hard | **false-alarm rate `[measure]`** | must stay low or the detector suppresses real predictions |

Source B is called out in advance as the likely weak point: a firmware change alters sampling
without changing the sensor, so the input can look familiar in feature space while the model's
assumptions no longer hold.

### Threshold Derivation
Missed OOD → a confident wrong failure prediction → either an unnecessary line stop or a missed
failure. False alarm → a maintenance engineer inspects manually, ~25 minutes. The miss cost
dominates, so the threshold is set toward higher sensitivity. **Check:** the resulting flag
volume must fit the maintenance team's inspection capacity — if it does not, the answer is a
staged rollout by machine type, not a looser threshold.

### Fallback Behaviour
| Source | Response |
|---|---|
| New sensor / machine type | suppress prediction; notify onboarding; collect labelled data |
| Post-firmware | suppress prediction; **trigger recalibration review** — the model may need retraining, not just flagging |
| Unclassified flag | serve with a warning banner and log for weekly review |

### Known Blind Spot
Feature-space distance detects inputs far from training features. It is expected to miss
**gradual degradation** — a sensor drifting slowly out of calibration produces inputs that stay
close in feature space while becoming progressively less trustworthy. That is population drift,
not per-input novelty. Compensating control: `mlmonitor_drift_detection_design.md` running in
parallel, plus monitoring realized accuracy per sensor cohort after onboarding.

### Maintenance
When a new sensor model is onboarded and training data is collected for it, it must be added to
the reference distribution — otherwise the detector keeps flagging a cohort the model now handles
correctly, and the maintenance team learns to ignore it. Reviewed at each retrain.
```

**Techniques Used:**
- **RT-02 (Multi-Dimensional Analysis Framework):** OOD source × detector family × cost is the evaluation grid.
- **DS-02 (Metric Specification):** detection and false-alarm rates are specified at a derived operating point rather than as a summary score.
- **QA-12 (False Positives Identification):** the in-distribution-hard set exists to reject a difficulty detector posing as a novelty detector.
- **CM-02 (Constraint Specification):** the operational-definition and near-OOD requirements bound the evaluation.
- **RT-10 (Troubleshooting Decision Tree):** flagged source determines the fallback branch.

**Related Prompts:**
- `mleval_uncertainty_quantification_design.md` — epistemic uncertainty as a complementary signal.
- `mleval_selective_prediction_abstention.md` — the abstention machinery this feeds.
- `../production-monitoring/mlmonitor_drift_detection_design.md` — the population-level counterpart covering this design's blind spot.
- `../specialized-ml/other-modalities/mlmodal_anomaly_outlier_detection.md` — when anomaly detection is the product rather than a guard.
