---
title: "COPD Care Plan (GOLD Framework)"
category: domain-healthcare-clinical/care-plans
description: "Build a COPD management plan using GOLD grouping: inhaler escalation, exacerbation prevention, eosinophil-guided ICS, and non-pharmacologic bundle with named devices and doses."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
  - DS-02
difficulty: advanced
tags:
  - pulmonology
  - copd
  - inhalers
  - care-plan
updated: "2026-06-19"
---

## Objective

Produce a COPD care plan using the GOLD framework: assign the ABE group, select and escalate inhaled therapy (including eosinophil-guided ICS), prevent exacerbations, and install the non-pharmacologic bundle. Output is an inhaler regimen plus prevention plan.

## Inputs

- Spirometry: post-bronchodilator FEV1/FVC <0.70, FEV1 % predicted (GOLD 1–4)
- Symptoms: mMRC dyspnea score, CAT score
- Exacerbation history: number in past year, hospitalizations
- Blood eosinophil count, smoking status, alpha-1 antitrypsin status (if young/non-smoker)
- Comorbidities: cardiovascular disease, anxiety/depression, OSA, osteoporosis
- Current inhalers (and technique/adherence), home O2 status, prior pneumonia

## Role

Pulmonologist or primary care attending managing COPD.

## Reasoning Steps

1. **Confirm diagnosis** with post-bronchodilator spirometry (FEV1/FVC <0.70). Grade airflow (GOLD 1–4 by FEV1%).

2. **Assign GOLD group (ABE):**
   - **A:** low symptoms (mMRC 0–1, CAT <10), 0–1 exacerbations (no hospitalization).
   - **B:** higher symptoms (mMRC ≥2, CAT ≥10), 0–1 exacerbations.
   - **E:** ≥2 moderate exacerbations or ≥1 hospitalization (regardless of symptoms).

3. **Initial inhaler:**
   - **Group A:** a bronchodilator (LABA or LAMA).
   - **Group B:** LABA + LAMA combination.
   - **Group E:** LABA + LAMA; add ICS (triple therapy) if blood eosinophils ≥300.

4. **Escalation on follow-up (dyspnea vs exacerbation track):**
   - Persistent dyspnea on monotherapy → LABA + LAMA.
   - Persistent exacerbations on LABA + LAMA → add ICS if eos ≥100 (especially ≥300) = triple therapy (LABA/LAMA/ICS, e.g., a single-inhaler triple).
   - Exacerbations despite triple therapy → add roflumilast (FEV1 <50%, chronic bronchitis) or azithromycin 250 mg daily/3×weekly (former smokers).

5. **Eosinophil-guided ICS:** benefit greatest eos ≥300; minimal/none <100; ICS raises pneumonia risk — withdraw if no exacerbation benefit and low eos.

6. **Exacerbation prevention bundle:** smoking cessation (the only intervention that changes the FEV1 decline trajectory), influenza + pneumococcal + COVID + RSV vaccines, pulmonary rehabilitation (especially after exacerbation), self-management action plan with rescue prednisone/antibiotics for select patients.

7. **Oxygen / advanced:** long-term O2 if resting SpO2 ≤88% or PaO2 ≤55 (or ≤59 with cor pulmonale/polycythemia). Evaluate for lung volume reduction or transplant in advanced disease. Screen for alpha-1 antitrypsin deficiency once.

8. **Rescue inhaler:** SABA (albuterol) or SABA/SAMA PRN for all.

9. **Monitor:** symptom scores, exacerbation frequency, inhaler technique each visit, eosinophils, bone health on ICS, comorbid CVD.

## Output Format

```
SPIROMETRY / GOLD GRADE:
GOLD GROUP (ABE): [+ mMRC/CAT, exacerbations]
EOSINOPHILS:

INHALER PLAN:
- Maintenance: [LABA/LAMA/ICS device + rationale]
- Rescue: [SABA]
- Escalation/de-escalation logic

EXACERBATION PREVENTION:
- Smoking cessation, vaccines, pulmonary rehab, action plan
- Roflumilast/azithromycin if applicable

OXYGEN / ADVANCED:
- O2 criteria, A1AT screen, LVRS/transplant

MONITORING:
- Symptom scores, technique, eosinophils, bone, CVD

PITFALLS:
- [ICS overuse/pneumonia, missing smoking cessation, poor inhaler technique, eos-guided decisions]
```

## Worked Example

**Input:** 67 y/o F, ex-smoker, post-BD FEV1/FVC 0.58, FEV1 47% predicted. mMRC 2, CAT 18. Two exacerbations last year, one hospitalization. Blood eos 360. Current: albuterol PRN + tiotropium only.

**Output:**

```
SPIROMETRY / GOLD GRADE: FEV1 47% → GOLD 3 (severe airflow limitation).
GOLD GROUP: E (≥2 exacerbations + 1 hospitalization); also symptomatic (CAT 18).
EOSINOPHILS: 360 (≥300 — favors ICS).

INHALER PLAN:
- Currently on LAMA monotherapy — inadequate for Group E with high eos.
- Escalate to single-inhaler TRIPLE therapy LABA/LAMA/ICS (e.g., fluticasone furoate/umeclidinium/vilanterol once daily) — eos 360 supports ICS, exacerbation history mandates dual bronchodilation + ICS.
- Rescue: continue albuterol PRN.

EXACERBATION PREVENTION:
- Confirm sustained smoking cessation; relapse support if needed.
- Vaccines: influenza, pneumococcal, COVID, RSV.
- Pulmonary rehabilitation referral (recent exacerbation/hospitalization — high benefit).
- Written COPD action plan.
- If still exacerbating on triple: add azithromycin 250 mg 3×/week (ex-smoker) or roflumilast (FEV1 <50%, chronic bronchitis phenotype).

OXYGEN / ADVANCED:
- Check resting SpO2/ABG — qualify for LTOT if SpO2 ≤88%.
- One-time alpha-1 antitrypsin level.

MONITORING:
- CAT/mMRC and exacerbations each visit, inhaler technique check, eosinophils, bone density (ICS), screen CVD and anxiety/depression.

PITFALLS:
- Verify inhaler technique — a major cause of "treatment failure."
- ICS justified here (eos 360 + exacerbations); would reconsider if eos <100 and no exacerbation benefit (pneumonia risk).
- Smoking cessation remains the only FEV1-trajectory-modifying step.
```
