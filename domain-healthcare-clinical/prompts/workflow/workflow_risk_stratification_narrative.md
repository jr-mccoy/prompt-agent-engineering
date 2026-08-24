---
title: "Risk Stratification Narrative"
category: domain-healthcare-clinical/workflow
description: "Turn a patient's data into a defensible risk-stratification narrative using named, validated tools — readmission, deterioration, mortality, or disease-specific risk — with the drivers and the mitigations that follow."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
  - QA-01
difficulty: advanced
tags:
  - workflow
  - risk-stratification
  - population-health
  - prognosis
updated: "2026-06-19"
---

## Objective

Produce a risk-stratification narrative that quantifies a patient's risk for a specified outcome using the appropriate validated instrument, names the modifiable and non-modifiable drivers behind the score, and translates the result into a concrete management intensity (monitoring frequency, intervention, disposition). The output is the reasoning behind a risk tier — auditable, tied to a named tool, and actionable — not a bare number.

## Inputs

- The outcome of interest: 30-day readmission, in-hospital deterioration, short-term mortality, surgical risk, disease-specific event risk (ASCVD, stroke in AFib, bleeding, VTE, etc.)
- Patient data the relevant score requires (the prompt should request exactly the inputs the chosen instrument needs)
- Setting and decision the stratification will drive (admit vs. discharge, level of care, intensity of follow-up, whether to start a therapy)
- Time horizon of the risk estimate

## Role

Attending producing the risk assessment that justifies a disposition or intensity-of-care decision to a colleague.

## Reasoning Steps

1. **Select the validated instrument that matches the outcome and population** — and name it. Stroke risk in AFib → CHA2DS2-VASc; bleeding on anticoagulation → HAS-BLED; ASCVD → Pooled Cohort Equations/PREVENT; PE severity → PESI/sPESI; pneumonia → CURB-65/PSI; surgical cardiac risk → RCRI; readmission → LACE or HOSPITAL; mortality in cirrhosis → MELD-Na; ICU deterioration → NEWS2/MEWS. If no validated tool fits, say so and reason from established risk factors rather than inventing a score.

2. **Confirm you have the inputs the instrument requires;** if any are missing, state which and how it limits the estimate. Don't impute a value to complete a score silently.

3. **Compute or apply the score** and place the patient in the tool's risk tier, with the tier's associated outcome estimate as published (cite the tool's own stratification, e.g., "CHA2DS2-VASc 4 → ~4–5%/yr stroke risk").

4. **Decompose the score into drivers.** Separate non-modifiable contributors (age, prior event, sex) from modifiable ones (BP, glycemic control, smoking, anticoagulation status, volume status). The modifiable drivers are where the narrative becomes actionable.

5. **Calibrate against clinical gestalt.** Validated tools are population instruments; note where this individual's context pushes the true risk above or below the score (frailty, social determinants, non-adherence, a factor the tool doesn't capture). State the direction of adjustment and why — without overriding the tool arbitrarily.

6. **Translate the tier into management intensity.** A high readmission risk → intensive transitional care (early follow-up, med reconciliation, home health, telephonic check-in). A high deterioration score → higher level of care or increased monitoring frequency. Tie each mitigation to a driver.

7. **Verification pass on the numbers.** Re-check that the inputs map correctly to the score and that the tier and its published outcome estimate are stated accurately. Flag any input you were unsure of. For decisions hinging on a threshold (admit vs. discharge), make the threshold logic explicit.

## Output Format

```
OUTCOME ASSESSED: [outcome + time horizon]
INSTRUMENT: [named validated tool + why chosen]

INPUTS USED:
- [each input the tool requires + value]
- MISSING/ESTIMATED: [any input not available + impact]

SCORE / TIER: [score → published risk tier + associated outcome estimate]

DRIVERS:
- Non-modifiable: [list]
- Modifiable: [list — these drive the mitigations]

GESTALT CALIBRATION: [where individual context raises/lowers true risk vs. the score + direction]

MANAGEMENT INTENSITY (mitigations tied to drivers):
- [intervention] ← addresses [driver]

DECISION SUPPORTED: [the disposition/intensity this justifies]

VERIFICATION: [inputs→score check; tier/estimate accuracy; flagged uncertainties]
```

## Worked Example

**Input:** Discharge-planning question. 78 y/o M admitted for HFrEF decompensation, now euvolemic and ready for discharge. Outcome of interest: 30-day readmission risk. Data: this is his 2nd HF admission in 6 months; lives alone; eGFR 40; on Medicaid; A1c 9.0 (diabetic); discharged on a 5-drug regimen; LACE inputs — Length of stay 5 days, Acute admission via ED, Charlson comorbidity (HF, DM, CKD), ED visits 2 in prior 6 months.

**Output:**

```
OUTCOME ASSESSED: 30-day hospital readmission (post-HF discharge).
INSTRUMENT: LACE index (Length of stay, Acuity, Comorbidity, ED visits) — validated for 30-day readmission/death after medical discharge. (HOSPITAL score is a reasonable alternative.)

INPUTS USED:
- L (length of stay 5 days): 4 points.
- A (acute/emergent admission): 3 points.
- C (Charlson comorbidity — HF, diabetes, CKD): ~3–4 points.
- E (ED visits in prior 6 mo = 2): 2 points.
- Approximate LACE ≈ 12–13.
- MISSING/ESTIMATED: exact Charlson tally depends on full comorbidity coding; range stated.

SCORE / TIER: LACE ~12–13 → HIGH risk tier (LACE ≥10 indicates high readmission risk; expected 30-day readmission/death substantially above baseline).

DRIVERS:
- Non-modifiable: age 78, multimorbidity (HF + DM + CKD), prior admission pattern.
- Modifiable: HF self-management/adherence, glycemic control (A1c 9.0), volume monitoring, social support, medication complexity (5-drug regimen), access (lives alone, Medicaid).

GESTALT CALIBRATION: True risk likely ABOVE the score. LACE doesn't fully capture that this is a 2nd HF admission in 6 months, he lives alone (no in-home monitor for early decompensation), and has uncontrolled diabetes — all push real readmission risk higher.

MANAGEMENT INTENSITY (mitigations tied to drivers):
- Early follow-up within 7 days (HF clinic or PCP) ← prior admission pattern, lives alone.
- Discharge medication reconciliation + simplified regimen/pillbox + teach-back ← 5-drug complexity.
- Home health referral with daily-weight monitoring and a weight-gain action plan ← lives alone, recurrent volume overload.
- Telephonic check-in at 48–72 h ← no in-home support.
- Diabetes optimization plan and follow-up ← A1c 9.0 modifiable driver.
- Confirm medication affordability/access (Medicaid formulary) before discharge ← access barrier.

DECISION SUPPORTED: Discharge is appropriate (euvolemic) BUT mandates a high-intensity transitional-care bundle, not routine follow-up. Without it, readmission risk is unacceptably high.

VERIFICATION: LACE components mapped to provided data; score placed in the published high-risk tier (≥10). Charlson exact points flagged as range-dependent. Gestalt adjustment (upward) justified by factors LACE omits, stated explicitly rather than altering the score.
```
