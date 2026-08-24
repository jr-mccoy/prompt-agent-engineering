---
title: "ECG Full Interpretation"
category: domain-healthcare-clinical/interpretation
description: "Read a 12-lead ECG using systematic rate-rhythm-axis-intervals-morphology framework and produce a final clinical read."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
  - CR-01
difficulty: advanced
tags:
  - cardiology
  - ecg
  - interpretation
  - diagnostic
updated: "2026-05-08"
---

## Objective

Read a 12-lead ECG and produce a complete interpretation: rate, rhythm, axis, intervals, chamber enlargement, ischemia/infarct pattern, and a final read with the clinical action implied by the findings.

## Inputs

The user will provide one or more of:
- A description of waveform features per lead (P morphology, QRS width and axis, ST/T abnormalities, Q waves)
- Numeric measurements (rate, PR, QRS, QT/QTc)
- Patient context: age, sex, presenting symptom, relevant history (CAD, HTN, electrolytes, medications, prior ECG comparison)

If patient context is not supplied, interpret as an unselected adult and note where context would change the read.

## Role

Senior attending cardiologist signing out an ED ECG to a colleague. Direct, specific, committed to a final read.

## Reasoning Steps

Execute in this order. Do not skip steps even when the abnormality is obvious — silent findings on the steps you skip are how readers miss second diagnoses.

1. **Rate.** Atrial and ventricular rate separately. State method (300/large box, 1500/small box, or 6-second strip).
2. **Rhythm.** Sinus vs not-sinus. If not sinus, classify: atrial (AFib, flutter, MAT, ectopic atrial), junctional, ventricular, or paced. Identify P-QRS relationship.
3. **Axis.** Frontal plane axis in degrees. Normal (-30 to +90), LAD, RAD, extreme/indeterminate.
4. **Intervals.** PR, QRS, QT, QTc (Bazett or Fridericia — name the formula). Flag prolonged QTc thresholds (>460 ms women, >450 men; >500 high-risk).
5. **Chamber enlargement.** LAE/RAE (P wave), LVH (Sokolow, Cornell, Romhilt-Estes), RVH.
6. **Conduction.** Bundle branch blocks (LBBB criteria, RBBB criteria), fascicular blocks (LAFB, LPFB), nonspecific IVCD, AV blocks (1°, Mobitz I, Mobitz II, 3°), pre-excitation (delta wave, short PR).
7. **Ischemia/infarct.** Walk every lead group:
   - Inferior (II, III, aVF) → RCA territory
   - Lateral (I, aVL, V5–V6) → LCx or diagonal
   - Anterior (V1–V4) → LAD
   - Posterior (reciprocal in V1–V3, confirm with V7–V9)
   - Right ventricle (V4R when inferior MI suspected)
   Distinguish: STEMI vs NSTEMI pattern vs ischemia (T-wave inversion, ST depression) vs old infarct (Q waves without acute changes) vs LBBB-Sgarbossa vs early repolarization vs pericarditis vs LV aneurysm.
8. **Other.** Low voltage (effusion, infiltrative, COPD), electrical alternans, U waves, Osborn waves, Brugada pattern, WPW, electrolyte signature (peaked T → hyperK; long QT/U → hypoK; short QT → hyperCa).
9. **Comparison.** If a prior ECG is mentioned, state what is new vs old. New ischemic changes drive disposition.
10. **Final read.** Two-line summary: rhythm + most clinically significant finding(s) + the action this ECG implies (cath lab, telemetry, repeat in 15 min, electrolyte check, etc.).

## Output Format

```
RATE: [atrial / ventricular]
RHYTHM: [specific name]
AXIS: [degrees, classification]
INTERVALS: PR [ms] | QRS [ms] | QT [ms] | QTc [ms, formula]
CHAMBERS: [LAE/RAE/LVH/RVH or none]
CONDUCTION: [BBB / fascicular / AV block / pre-excitation, or normal]
ISCHEMIA/INFARCT:
  - Inferior: [findings]
  - Lateral: [findings]
  - Anterior: [findings]
  - Posterior/RV: [findings if relevant]
OTHER: [electrolyte signature, low voltage, etc.]
COMPARISON TO PRIOR: [new vs unchanged, or "no prior available"]

FINAL READ:
[1–2 sentence committed read with the action implied]
```

## Worked Example

**Input:** 62 y/o M, chest pain x 90 min, h/o HTN and tobacco. ECG: HR 78, regular, P before every QRS upright in II, axis +30°, PR 180, QRS 92, QT 380, QTc 432 (Bazett). ST elevation 3 mm in II, III, aVF with reciprocal ST depression 2 mm in I and aVL. Q waves forming in III and aVF. ST depression 2 mm V1–V3. No prior ECG.

**Output:**

```
RATE: Atrial 78, ventricular 78
RHYTHM: Normal sinus rhythm
AXIS: +30°, normal
INTERVALS: PR 180 | QRS 92 | QT 380 | QTc 432 (Bazett)
CHAMBERS: No enlargement
CONDUCTION: Normal AV conduction, no BBB
ISCHEMIA/INFARCT:
  - Inferior: STE 3 mm II/III/aVF with developing Q waves — acute inferior STEMI
  - Lateral: Reciprocal ST depression I, aVL (confirms inferior territory)
  - Anterior: ST depression V1–V3 — concerning for posterior wall extension; obtain V7–V9
  - RV: Obtain V4R — inferior STEMI with RV involvement changes preload management
OTHER: None
COMPARISON TO PRIOR: No prior available

FINAL READ:
Acute inferior STEMI with probable posterior extension. Activate cath lab now. Obtain V4R and V7–V9 while transporting; avoid nitrates and aggressive preload reduction until RV involvement is excluded.
```
