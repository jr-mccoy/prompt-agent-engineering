---
title: "Pulmonary Function Test Interpretation"
category: domain-healthcare-clinical/interpretation
description: "Interpret spirometry, bronchodilator response, lung volumes, DLCO, and flow-volume loops using LLN/z-scores to classify obstruction, restriction, mixed, or isolated gas-transfer defects and commit to diagnosis and therapy."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: intermediate
tags:
  - pulmonology
  - pft
  - spirometry
  - copd
  - interpretation
updated: "2026-09-24"
---

## Objective

Read a full or partial PFT report and produce a structured interpretation: test quality, ventilatory pattern, severity, bronchodilator responsiveness, lung volumes, gas transfer, and flow-volume loop shape — then name the most likely diagnosis in context and the concrete next step (therapy, further testing, referral).

## Inputs

- Spirometry pre- and post-bronchodilator: FEV1, FVC, FEV1/FVC — measured, % predicted, LLN, z-score
- Quality grade (acceptability/repeatability) and technician comments
- Reference equation used (GLI race-neutral vs legacy)
- Lung volumes: TLC, RV, RV/TLC, FRC (plethysmography vs gas dilution)
- DLCO (Hb-corrected), VA, KCO
- Flow-volume loop description; MIP/MEP and supine FVC if neuromuscular question
- Clinical context: age, sex, height, weight/BMI, smoking pack-years, symptoms, exposures, imaging, eosinophil count, exacerbation history

## Role

Senior pulmonology attending signing out the PFT lab read.

## Reasoning Steps

1. **Quality first.** Acceptable maneuvers with FVC and FEV1 repeatable (best two within 150 mL). Poor effort or early termination falsely lowers FVC and can mimic restriction. If quality is inadequate, say the numbers are uninterpretable for that parameter.

2. **Obstruction.** FEV1/FVC below LLN (z-score < −1.645). The fixed 0.70 ratio (GOLD) over-diagnoses obstruction in older adults and under-diagnoses it in the young — report both when they disagree and interpret by LLN.

3. **Severity.** By FEV1 z-score (ATS/ERS 2021: > −2.5 mild, −2.5 to −4 moderate, < −4 severe) and, for COPD, GOLD grade by FEV1 % predicted (≥80 GOLD 1, 50–79 GOLD 2, 30–49 GOLD 3, <30 GOLD 4).

4. **Bronchodilator response.** Current ATS/ERS criterion: >10% change in FEV1 or FVC relative to the predicted value. Older criterion (≥12% and ≥200 mL from baseline) still appears in reports — state which is used. A negative response does not exclude asthma (methacholine challenge if suspicion persists); a positive response does not exclude COPD.

5. **Low FVC → confirm restriction with lung volumes.** Restriction = TLC < LLN. Low FVC with normal TLC and high RV → air trapping (pseudo-restriction). Mixed defect = low FEV1/FVC + low TLC. Low FEV1 and FVC with normal ratio and normal TLC = non-specific pattern (obesity, early small-airways disease, poor effort, asthma).

6. **DLCO (Hb-corrected).**
   - Low with obstruction → emphysema (vs asthma, where DLCO is normal or high).
   - Low with restriction → interstitial lung disease.
   - Restriction with normal DLCO/KCO → extraparenchymal (obesity, chest wall, neuromuscular, pleural).
   - Isolated low DLCO with normal spirometry and volumes → pulmonary vascular disease (CTEPH, PAH), early ILD, combined emphysema–fibrosis, anemia (if uncorrected).
   - High DLCO → alveolar hemorrhage, polycythemia, asthma, obesity, left-to-right shunt.

7. **Flow-volume loop.** Fixed upper-airway obstruction → flattening of both limbs; variable extrathoracic → inspiratory limb flattening; variable intrathoracic → expiratory limb flattening. Coved expiratory limb → small-airways obstruction.

8. **Neuromuscular.** Low MIP/MEP; supine FVC drop >20–25% from upright → diaphragm weakness. In ALS and other progressive neuromuscular disease, falling FVC (e.g., <50% predicted) or low MIP triggers NIV discussion.

9. **Integrate and commit.** Pattern + clinical picture → diagnosis and treatment. Compare to prior PFTs: FEV1 decline rate and FVC decline in ILD (≥10% relative FVC drop is clinically significant progression).

## Output Format

```
QUALITY: [grade, reference equation]
SPIROMETRY: [FEV1, FVC, ratio with LLN/z; pattern]
SEVERITY: [z-score category; GOLD grade if COPD]
BRONCHODILATOR: [change, criterion used, significant Y/N]
LUNG VOLUMES: [TLC, RV, RV/TLC — restriction / hyperinflation / air trapping]
DLCO: [corrected value, KCO — interpretation]
FLOW-VOLUME LOOP: [shape]

INTERPRETATION: [pattern in one line]
MOST LIKELY DIAGNOSIS: [in context]

ACTION:
- [therapy with drug/dose]
- [further testing]
- [referral / monitoring interval]
```

## Worked Example

**Input:** 62 y/o F, former smoker (30 pack-years, quit 3 years ago), 1 year of exertional dyspnea, one prednisone-treated exacerbation last winter, mMRC 2. Blood eosinophils 150/µL. PFTs (GLI race-neutral, quality A): pre-BD FEV1 1.42 L (58% pred, z −2.9), FVC 2.60 L (80% pred, z −1.5), FEV1/FVC 0.55 (LLN 0.67); post-BD FEV1 1.52 L. TLC 118% pred, RV 165% pred, RV/TLC elevated. DLCO (Hb-corrected) 45% pred, KCO reduced. Flow-volume loop: coved expiratory limb.

**Output:**

```
QUALITY: Grade A, GLI race-neutral — interpretable.
SPIROMETRY: FEV1/FVC 0.55 < LLN 0.67 → obstruction. FVC reduced mildly (z −1.5, above LLN).
SEVERITY: FEV1 z −2.9 → moderate (ATS/ERS). GOLD 2 (FEV1 58% predicted).
BRONCHODILATOR: +100 mL; relative to predicted FEV1 (~2.45 L) ≈ 4% → not significant (criterion: >10% of predicted).
LUNG VOLUMES: TLC 118% (hyperinflation), RV 165% (air trapping). No restriction.
DLCO: 45% predicted, KCO reduced → significant gas-transfer impairment.
FLOW-VOLUME LOOP: Coved expiratory limb — small-airways obstruction.

INTERPRETATION: Moderate obstruction without significant bronchodilator response, with hyperinflation, air trapping, and severely reduced DLCO.
MOST LIKELY DIAGNOSIS: COPD, emphysema-predominant. GOLD 2, group B (mMRC ≥2; one moderate exacerbation in the past year does not meet group E, which requires ≥2 moderate or ≥1 hospitalized exacerbation).

ACTION:
- LAMA/LABA: tiotropium/olodaterol 2.5/2.5 mcg, 2 inhalations once daily via soft-mist inhaler; teach technique. No ICS (eosinophils 150, one moderate exacerbation).
- Albuterol 90 mcg, 2 puffs q4–6h PRN.
- Alpha-1 antitrypsin level and phenotype (every COPD patient once).
- Low-dose CT chest: meets lung cancer screening criteria (age 50–80, ≥20 pack-years, quit <15 years) — also characterizes emphysema distribution.
- Resting and ambulatory oximetry (DLCO 45% → exertional desaturation likely).
- Pulmonary rehabilitation referral; influenza, COVID-19, pneumococcal, RSV, Tdap vaccines up to date.
- Repeat spirometry in 12 months or with clinical change; escalate if a second moderate or any severe exacerbation occurs.
```
