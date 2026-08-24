---
title: "Computer Vision Incident Patterns & Runbooks"
category: AI-ML/production-monitoring
description: "A catalog of computer-vision-specific production incident patterns with detection + response — camera/sensor config shift, domain/lighting shift, class/label distribution drift, corrupted or out-of-distribution input, adversarial perturbation, and confidence/calibration collapse — each with signals, containment, diagnosis, and durable fix."
techniques:
  - ST-02
  - RT-10
  - DS-06
  - RT-09
  - QA-12
difficulty: advanced
tags:
  - computer-vision
  - sensor-shift
  - domain-shift
  - out-of-distribution
  - calibration
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/production-monitoring/mlmonitor_incident_runbook_library.md
  - domain-AI-ML/specialized-ml/computer-vision/cv_medical_imaging_considerations.md
  - domain-AI-ML/production-monitoring/mlmonitor_drift_detection_design.md
---

# Computer Vision Incident Patterns & Runbooks

**Objective:** Produce a catalog of computer-vision-specific production incident patterns — camera/sensor configuration shift, domain/lighting shift, class/label distribution drift, corrupted or out-of-distribution input, adversarial perturbation, and confidence/calibration collapse — each with detection signals, immediate containment, CV-aware diagnosis, and a durable fix, so a vision-system responder can recognize failures that arise from the imaging pipeline and the physical world, not just the model weights.

**When to Use:**
- Operating a CV system (detection, classification, segmentation, OCR) where the input is sensor/camera imagery.
- After a CV incident where accuracy dropped but the model file never changed (the camera, lighting, or input did).
- When generic ML runbooks miss the imaging-pipeline and physical-environment causes specific to vision.

**When NOT to Use:**
- For non-vision tabular/text failure classes (use `mlmonitor_incident_runbook_library.md`).
- For clinical/regulatory imaging design considerations and safety framing (use `cv_medical_imaging_considerations.md`).
- To design the drift detectors themselves (use `mlmonitor_drift_detection_design.md`).

## Inputs / Context

- **System & sensors** — task, camera/sensor types, resolution, capture conditions, deployment sites.
- **Imaging pipeline** — preprocessing (resize, normalize, color space), codec/compression, any on-device transforms.
- **Signals available** — input-image statistics (brightness, contrast, sharpness, color histograms), prediction-distribution and confidence histograms, OOD/embedding-distance scores, quality on matured labels.
- **Containment levers** — fallback model, human review queue, confidence-gate/abstain, disable affected site/camera.
- **Escalation map** — on-call, sensor/hardware/site owner, data/labeling owner, model owner.

## Constraints

**Must:**
- Treat each pattern as distinct with its own detection signals, containment, diagnosis, and durable fix.
- Separate input-side causes (sensor config, lighting, corruption, OOD, adversarial) from label/distribution causes — because retraining fixes the latter, not the former.
- Check the imaging pipeline (preprocessing, color space, compression) before concluding the model degraded.
- Separate immediate containment from durable fix.

**Must Not:**
- Invent incident events, image statistics, OOD scores, root causes, or accuracy figures; reconstruct from logs/telemetry and mark gaps "unknown / needs investigation."
- Default to "the model degraded, retrain it" without first ruling out a camera/lighting/preprocessing change (single-root-cause oversimplification).
- Apply hindsight bias — judge responder/threshold decisions by what input statistics were visible at the time.

**Instructions:**

1. **Enumerate the CV patterns.** Camera/sensor config shift (firmware/ISP/exposure/resolution change); domain/lighting shift (season, time-of-day, new site); class/label distribution drift; corrupted or OOD input (occlusion, blur, new object types); adversarial perturbation; confidence/calibration collapse.

2. **Define detection signals per pattern.** Input-image statistic shifts (brightness/contrast/sharpness/color histograms), prediction-distribution shift, confidence-histogram changes, OOD/embedding-distance spikes, calibration error on matured labels, and per-site/per-camera breakdowns.

3. **Specify immediate containment.** Confidence-gate or abstain on low-confidence outputs; route to human review; fall back to a robust model; disable the affected camera/site; reject inputs failing a quality check.

4. **Add CV-aware diagnosis.** Is the shift in the input statistics (sensor/lighting) or in the labels? Did preprocessing/color-space/compression change? Is it one camera/site or system-wide? Is low confidence uniform (calibration) or concentrated on OOD inputs? Could perturbation be adversarial (targeted, structured noise) vs natural corruption?

5. **Define the durable fix.** Recalibrate or pin sensor/ISP config; add input-quality gates; augment/retrain for the new domain (only after confirming a real label/domain shift, not a sensor bug); add OOD rejection; recalibrate confidence; harden against adversarial inputs.

6. **Set escalation and severity.** Sensor/site owner for hardware/config; data owner for distribution/label; model owner for calibration/retrain; severity by downstream harm (safety-critical vision raises severity).

7. **Index the patterns.** Symptom → pattern routing with disambiguation (an accuracy drop could be sensor shift OR domain shift OR corruption).

**Output Format:**

A markdown catalog:
- **Routing Index** — Symptom → candidate pattern(s) → disambiguation
- **Per-Pattern entries**, each: Pattern | Detection signals | Immediate containment | Diagnosis decision points | Durable fix | Escalation/severity
- **Cross-links** — to drift-detector design and (where relevant) imaging-domain considerations

## Verification

- [ ] Each CV pattern is a distinct runbook with all four parts.
- [ ] Diagnosis checks the imaging pipeline and input statistics before blaming the model.
- [ ] Input-side causes are separated from label/distribution causes (so retrain isn't the reflex).
- [ ] Per-camera/per-site breakdowns are used to localize the shift.
- [ ] Immediate containment is separated from durable fix.
- [ ] No invented image statistics or accuracy figures; gaps marked "unknown / needs investigation."

## False-Positive Prevention

❌ **DON'T:**
- Retrain the model when a camera firmware update changed the ISP color space — retraining won't fix a sensor config bug.
- Call uniform low-confidence "the model got worse" when it's a calibration shift after a preprocessing change.
- Treat structured adversarial perturbation as ordinary noise and just lower the confidence threshold.
- Declare system-wide domain shift from one bad camera/site without a per-camera breakdown.

✅ **DO:**
- Compare input-image statistics (brightness/contrast/color) before vs during the incident first.
- Localize with per-camera/per-site metrics to tell sensor config from true domain shift.
- Distinguish OOD/corruption (input fails quality gate) from adversarial (targeted, structured) inputs.
- Retrain only after confirming a real domain/label shift, not a fixable imaging-pipeline change.

## Example Output

```markdown
## CV Incident Patterns — Retail Shelf Detector

### Routing Index
| Symptom | Candidate pattern(s) | Disambiguation |
|---|---|---|
| mAP drop, one store | Sensor config shift, domain/lighting shift | Per-camera image stats: brightness/color changed? firmware update? |
| Low confidence everywhere | Calibration collapse | Did preprocessing/normalization change? matured-label calibration error? |
| Random misses on odd items | OOD / corrupted input | New product packaging? occlusion/blur spike? |

### P1 — Camera/Sensor Config Shift
- **Detection:** per-camera brightness/contrast/color histogram shift coincident with a firmware/ISP change; mAP drop localized to affected cameras.
- **Containment:** route affected cameras to human review; pin/rollback the camera config if possible.
- **Diagnosis:** confirm shift is in input statistics (not labels); correlate with config-change log; one camera vs fleet.
- **Durable fix:** restore/standardize ISP config; add input-statistic monitor per camera; re-validate.
- **Escalation/severity:** SEV-3 localized; site/hardware owner.

### P2 — Confidence / Calibration Collapse
- **Detection:** confidence histogram compresses toward mid-range; calibration error (ECE) rises on matured labels; accuracy may be stable while confidence is unreliable.
- **Containment:** widen abstain band; route uncertain predictions to review.
- **Diagnosis:** preprocessing/normalization change? distribution shift? vs genuine miscalibration.
- **Durable fix:** recalibrate (temperature scaling); pin preprocessing; monitor ECE per `mlmonitor_drift_detection_design.md`.
- **Escalation/severity:** model owner.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** every pattern follows detect → contain → diagnose → fix.
- **RT-10 (Troubleshooting Decision Tree):** routing index and per-pattern decision points.
- **DS-06 (Prioritization & Severity Guidance):** severity by downstream harm drives escalation.
- **RT-09 (Root Cause Explanation):** diagnosis resolves to imaging-pipeline vs label vs model cause.
- **QA-12 (False Positives Identification):** blocks reflexive retrain and sensor-vs-model confusion.

**Related Prompts:**
- `mlmonitor_incident_runbook_library.md` — the general failure-class library this CV catalog extends.
- `cv_medical_imaging_considerations.md` — imaging-domain considerations for safety-critical vision.
- `mlmonitor_drift_detection_design.md` — the detectors behind input-statistic and calibration monitoring.
