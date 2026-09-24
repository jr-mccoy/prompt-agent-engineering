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
  - breathing-test-results
  - short-of-breath
  - ex-smoker
updated: "2026-09-24"
related_prompts:
  - domain-healthcare-clinical/prompts/interpretation/interp_abg_acid_base.md
  - domain-healthcare-clinical/prompts/pharmacology/pharm_inhaler_regimen_asthma_copd.md
  - domain-healthcare-clinical/prompts/specialty/specialty_ild_workup.md
---

> **Medical disclaimer — read before use.** This prompt is a decision-support and
> teaching aid for **licensed clinicians**. It is **not medical advice** and is not for
> patients to diagnose or treat themselves. Drug doses, thresholds and guideline
> references in it and in its worked example may be incomplete, outdated or wrong:
> verify each one against the current guideline, the product label and your local
> formulary, and follow your institution's protocols. It does not replace examination
> or clinical judgment. **Medical emergency: call your local emergency number (911 in
> the US).**
>
> **Review status:** clinical content and doses reviewed by AI only (2026-09-24);
> **not yet reviewed by a licensed clinician.**

## Objective

Read a full or partial PFT report and produce a structured interpretation: test quality, ventilatory pattern, severity, bronchodilator responsiveness, lung volumes, gas transfer, and flow-volume loop shape — then name the most likely diagnosis in context and the concrete next step (therapy, further testing, referral).

Decision support for a licensed clinician: confirm inhaler doses, reference equations, and severity thresholds against the current guideline (ATS/ERS, GOLD) and local formulary. A hypoxemic or rapidly deteriorating patient is escalated now, not after this output.

## When to Use

- A spirometry, lung-volume, DLCO, or flow-volume report needs a committed pattern, severity, and next step.
- Deciding whether a low FVC is true restriction, air trapping, or effort-related.
- Comparing serial PFTs for progression (COPD, ILD, neuromuscular disease).

**Not this prompt if:**
- The pattern is already established and the question is which inhaler step to use — use `domain-healthcare-clinical/prompts/pharmacology/pharm_inhaler_regimen_asthma_copd.md`.
- The result in hand is an arterial blood gas — use `domain-healthcare-clinical/prompts/interpretation/interp_abg_acid_base.md`.
- A restrictive/low-DLCO pattern needs a full interstitial lung disease workup — use `domain-healthcare-clinical/prompts/specialty/specialty_ild_workup.md`.

## Inputs

- Spirometry pre- and post-bronchodilator: FEV1, FVC, FEV1/FVC — measured, % predicted, LLN, z-score
- Quality grade (acceptability/repeatability) and technician comments
- Reference equation used (GLI race-neutral vs legacy)
- Lung volumes: TLC, RV, RV/TLC, FRC (plethysmography vs gas dilution)
- DLCO (Hb-corrected), VA, KCO
- Flow-volume loop description; MIP/MEP and supine FVC if neuromuscular question
- Clinical context: age, sex, height, weight/BMI, smoking pack-years, symptoms, exposures, imaging, eosinophil count, exacerbation history

## Role

Senior pulmonology attending supporting the treating clinician; signs out the PFT lab read as a committed interpretation they can verify.

## Reasoning Steps

1. **Quality first.** Acceptable maneuvers with FVC and FEV1 repeatable (best two within 150 mL). Poor effort or early termination falsely lowers FVC and can mimic restriction. If quality is inadequate, say the numbers are uninterpretable for that parameter.

   **Stop and escalate now if:** resting hypoxemia (or desaturation during testing), rapidly progressive dyspnea, or a flow-volume loop suggesting upper-airway obstruction (flattened inspiratory and/or expiratory limbs) — urgent clinical evaluation (airway/ENT or pulmonology) before the routine interpretation. A falling FVC or MIP in neuromuscular disease with symptoms of hypoventilation is also urgent.

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

## Verification

- [ ] Red flags (resting hypoxemia, rapidly progressive dyspnea, upper-airway pattern on the loop) addressed before routine interpretation.
- [ ] Test quality stated first, and any parameter from an unacceptable maneuver marked uninterpretable.
- [ ] Obstruction and restriction called by LLN/z-score, with fixed-ratio disagreement reported; restriction claimed only with TLC.
- [ ] Every severity grade and bronchodilator criterion attributed to a named standard and year (ATS/ERS 2021, ATS/ERS 2005 for DLCO, GOLD).
- [ ] Inhaler doses checked against the current guideline and formulary.
- [ ] States what would change the interpretation (lung volumes, Hb correction, prior PFTs, repeat after therapy).

## False-Positive Prevention

- **Restriction called from a low FVC alone:** air trapping, obesity, and poor effort all lower FVC with a normal TLC.
- **Obstruction over-called by the fixed 0.70 ratio** in older adults whose FEV1/FVC is above LLN.
- **Low DLCO read without Hb correction** or without checking VA/KCO, so anemia or a low alveolar volume is mistaken for parenchymal or vascular disease.
- **A negative bronchodilator response taken to exclude asthma,** or a positive one to exclude COPD.

## Worked Example

**Input:** 62 y/o F, former smoker (30 pack-years, quit 3 years ago), 1 year of exertional dyspnea, one prednisone-treated exacerbation last winter, mMRC 2. Blood eosinophils 150/µL. PFTs (GLI race-neutral, quality A): pre-BD FEV1 1.42 L (58% pred, z −2.9), FVC 2.60 L (80% pred, z −1.5), FEV1/FVC 0.55 (LLN 0.67); post-BD FEV1 1.52 L. TLC 118% pred, RV 165% pred, RV/TLC elevated. DLCO (Hb-corrected) 45% pred, KCO reduced. Flow-volume loop: coved expiratory limb.

**Output:**

```
QUALITY: Grade A, GLI race-neutral — interpretable.
SPIROMETRY: FEV1/FVC 0.55 < LLN 0.67 → obstruction. FVC reduced mildly (z −1.5, above LLN).
SEVERITY: FEV1 z −2.9 → moderate (ATS/ERS). GOLD 2 (FEV1 58% predicted).
BRONCHODILATOR: +100 mL; relative to predicted FEV1 (~2.45 L) ≈ 4% → not significant (criterion: >10% of predicted).
LUNG VOLUMES: TLC 118% (hyperinflation), RV 165% (air trapping). No restriction.
DLCO: 45% predicted, KCO reduced → moderate gas-transfer impairment (ATS/ERS 2005 grading: 40–60% moderate, <40% severe).
FLOW-VOLUME LOOP: Coved expiratory limb — small-airways obstruction.

INTERPRETATION: Moderate obstruction without significant bronchodilator response, with hyperinflation, air trapping, and moderately reduced DLCO.
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
