---
title: "Inhaler Regimen Selection (Asthma & COPD)"
category: domain-healthcare-clinical/pharmacology
description: "Build an inhaler regimen for asthma or COPD by GINA / GOLD step, biomarker phenotype (eosinophil, FeNO), exacerbation history, comorbidities, and device technique; specify ICS / ICS-LABA / LAMA / LABA-LAMA / triple therapy / biologic with brand-name examples, doses, and patient-education priorities."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: intermediate
tags:
  - pulmonology
  - asthma
  - copd
  - inhalers
  - prescribing
updated: "2026-05-12"
---

## Objective

Design a stepwise inhaler regimen for an asthma or COPD patient: stage severity per GINA / GOLD, select the appropriate combination (SABA, ICS, ICS-formoterol as both controller and reliever per MART/SMART, LABA, LAMA, dual bronchodilation, triple therapy, biologics), match device type to patient capacity, address comorbidities, and counsel on technique. Output names specific products, doses, frequencies, and reassessment cadence.

## Inputs

- Diagnosis (asthma, COPD, ACO, eosinophilic asthma, exercise-induced bronchospasm, occupational, atopic)
- Spirometry (FEV1, FEV1/FVC, bronchodilator response, reversibility)
- Symptom burden: GINA control (well-controlled / partially / uncontrolled), CAT, mMRC dyspnea, exacerbation history (≥2 moderate or any severe in 12 months)
- Biomarkers: blood eosinophils, FeNO, IgE, sputum eosinophilia, sensitization
- Comorbidities: GERD, OSA, anxiety/panic, cardiovascular, glaucoma (anticholinergic caution), prostatic hyperplasia, age
- Smoking status
- Inhaler-technique capacity (hand strength, coordination, inspiratory flow), prior device tolerance
- Trigger / occupational exposures

## Role

Senior pulmonologist or primary care prescriber building the inhaler regimen with rationale.

## Reasoning Steps

1. **Confirm diagnosis and phenotype.**
   - **Asthma:** variable airflow obstruction, ≥12% bronchodilator reversibility, history of variable symptoms, atopy/family history, often eosinophilic or T2-high (FeNO ≥25 ppb, eos ≥150/µL).
   - **COPD:** post-bronchodilator FEV1/FVC <0.70, history of smoke / occupational exposure, less reversibility (though present).
   - **ACO (asthma-COPD overlap):** features of both; treat as asthma (start ICS, never LABA-only).
   - **Eosinophilic COPD (eos ≥300):** higher ICS responsiveness, biologic candidate (anti-IL-5, anti-IL-4Rα being explored).

2. **GINA stepwise approach for asthma (2024).**
   - **Track 1 (preferred):** as-needed low-dose ICS-formoterol (anti-inflammatory reliever).
     - **Step 1 (intermittent / mild):** as-needed low-dose budesonide-formoterol 160/4.5 µg (Symbicort) or beclomethasone-formoterol.
     - **Step 2:** same as-needed regimen, used more frequently or as MART (maintenance + reliever, low-dose daily).
     - **Step 3:** low-dose ICS-formoterol MART (one puff BID + as-needed).
     - **Step 4:** medium-dose ICS-formoterol MART.
     - **Step 5:** high-dose ICS-LABA + add-on (LAMA — tiotropium 2.5 µg Respimat; biologic per phenotype).
   - **Track 2 (alternative — daily ICS controller + as-needed SABA):**
     - Step 1: SABA as needed + low-dose ICS at same time as reliever.
     - Step 2: daily low-dose ICS + SABA prn.
     - Step 3: low-dose ICS-LABA daily + SABA prn (e.g., fluticasone-salmeterol Advair, mometasone-formoterol Dulera).
     - Step 4: medium-dose ICS-LABA + SABA prn; consider add LAMA (Trelegy = ICS-LABA-LAMA single inhaler).
     - Step 5: high-dose ICS-LABA + LAMA + biologic (omalizumab, mepolizumab, benralizumab, reslizumab, dupilumab, tezepelumab); add-on tiotropium even without biologic.
   - **Never LABA alone in asthma** — increases mortality.

3. **GOLD stepwise for COPD (2024).**
   - Initial therapy by group (A, B, E):
     - **Group A** (≤1 moderate exacerbation, mMRC 0–1, CAT <10): bronchodilator (SABA or SAMA prn; or LAMA/LABA daily).
     - **Group B** (≤1 moderate, mMRC ≥2, CAT ≥10): **LABA + LAMA** combination preferred over single (Trelegy without ICS — but Trelegy includes ICS; for LABA + LAMA see Anoro [umeclidinium-vilanterol], Stiolto [olodaterol-tiotropium], Bevespi [glycopyrrolate-formoterol], Duaklir [aclidinium-formoterol]).
     - **Group E** (≥2 moderate or ≥1 severe with hospitalization): **LABA + LAMA**; add ICS (triple therapy) if blood eosinophils ≥300, or ≥100 with history of exacerbations, or ACO features.
   - Follow-up strategy:
     - Persistent dyspnea on LAMA or LABA monotherapy → escalate to dual.
     - Persistent exacerbations on LABA-LAMA + eos ≥100 + exacerbation history → escalate to triple (LABA-LAMA-ICS, e.g., Trelegy [fluticasone-umeclidinium-vilanterol], Breztri [budesonide-glycopyrrolate-formoterol]).
     - Persistent exacerbations despite triple → consider roflumilast (PDE4 inhibitor — chronic bronchitis + FEV1 <50% phenotype), azithromycin 250 mg daily or 500 mg 3×/week (anti-inflammatory; QTc monitor; tinnitus / hearing checks).
     - Eosinophilic COPD with ongoing exacerbations on triple therapy: dupilumab (FDA approved late 2024 for COPD with eosinophilic phenotype).
   - **Pneumonia risk** with ICS in COPD — weigh exacerbation benefit vs pneumonia risk; consider stopping ICS in low-eos, no-exacerbation patients.

4. **Inhaler device selection.**
   - **Pressurized metered-dose inhaler (pMDI):** requires hand-breath coordination; spacer (valved holding chamber) recommended for most patients to overcome coordination issues and reduce oral deposition.
   - **Dry powder inhaler (DPI):** requires adequate inspiratory flow (≥60 L/min for some); not appropriate in severe airflow obstruction with very low PIF, very young children, or very elderly with weak inspiratory effort.
   - **Soft mist inhaler (Respimat — tiotropium, olodaterol, ipratropium-albuterol):** slower aerosol cloud, easier coordination than pMDI without spacer.
   - **Nebulizer:** when neither pMDI nor DPI feasible (severe exacerbation, very young, frail, neuro-impaired); slower delivery but no coordination.
   - **Mask vs mouthpiece:** mask for young children and very impaired; mouthpiece preferred when possible (reduces facial deposition).
   - Test inspiratory flow with In-Check DIAL or similar in clinic when concerned.

5. **Biologic selection for severe asthma.**
   - **Omalizumab (anti-IgE):** atopic, total IgE 30–700 (varies by weight); reduces exacerbations, allergic asthma.
   - **Mepolizumab, reslizumab, benralizumab (anti-IL-5 / anti-IL-5Rα):** eosinophilic asthma (eos ≥150, often ≥300); reduce exacerbations, OCS-sparing.
   - **Dupilumab (anti-IL-4Rα):** Th2-high (eos ≥150 or FeNO ≥25); covers both atopic and eosinophilic; effective in nasal polyps, AD comorbidity.
   - **Tezepelumab (anti-TSLP):** broad — not phenotype-restricted; reduces exacerbations across phenotypes; useful when low Th2 markers.

6. **Comorbidity adjustments.**
   - **Cardiovascular disease:** LABA/SABA bronchodilator caution if symptomatic arrhythmia; tiotropium has favorable cardiac safety profile vs early concerns.
   - **Glaucoma (narrow-angle):** LAMA caution; use spacer/closed-eye technique.
   - **BPH / urinary retention:** LAMA can worsen; counsel.
   - **Osteoporosis:** high-dose ICS chronic use — bone density monitoring, calcium/vitamin D.
   - **OSA:** treat both; OSA worsens asthma control.
   - **GERD:** treat reflux; can mimic and worsen asthma.

7. **Counseling — technique critical.**
   - Demonstrate device technique at every visit.
   - Spacer use for pMDI; rinse mouth after ICS (thrush prevention, dysphonia).
   - Slow steady inhalation for pMDI; deep forceful inhalation for DPI.
   - Hold breath 5–10 seconds after inhalation.
   - Wait 30–60 seconds between puffs of same med.
   - Track use; teach when to use reliever vs controller.

8. **Action plan and follow-up.**
   - Written asthma action plan (green/yellow/red zones).
   - COPD exacerbation plan: when to start prednisone (40 mg PO daily ×5 days) and antibiotic (amoxicillin-clav, azithromycin, or doxycycline for 5 days for increased sputum purulence).
   - Reassess control / exacerbations every 1–3 months when titrating; every 3–6 months when stable.

## Output Format

```
PATIENT SNAPSHOT:
- Diagnosis (asthma / COPD / overlap, severity, phenotype, eos, FeNO)
- Symptom burden, exacerbation history
- Comorbidities, device-capacity factors

REGIMEN:
- Maintenance: [drug + device + dose + frequency]
- Reliever: [drug + device + dose]
- Add-on (if applicable): [biologic + dose + frequency]

RATIONALE:
- Step / group alignment with guideline
- Phenotype match (eos, FeNO, IgE)
- Device match to patient capacity
- Avoidance of LABA monotherapy in asthma

DEVICE & TECHNIQUE NOTES:
- pMDI + spacer / DPI / Respimat
- Rinse mouth after ICS
- Inhalation technique

COMORBIDITY ADJUSTMENTS:
- [Glaucoma, BPH, CV, OSA, GERD, osteoporosis]

ACTION PLAN:
- Green zone: maintenance only
- Yellow zone: add reliever, ICS bump, consider prednisone
- Red zone: ED / urgent care
- Steroid rescue: prednisone 40 mg PO ×5 days
- Antibiotic for COPD exacerbation: [criteria]

MONITORING:
- Symptom control (ACT, CAT, mMRC)
- Exacerbations
- Spirometry (annual or post-titration)
- Eos / FeNO (asthma; periodic)
- Bone density if chronic high-dose ICS

WHEN TO ESCALATE:
- Persistent symptoms / exacerbations despite triple → biologic
- Adverse effect (thrush, hoarseness, palpitations, urinary retention): switch device or class
- Pneumonia in COPD on ICS: consider de-escalation

FOLLOW-UP:
- 1 month after change
- Every 3 months thereafter
- Action-plan review at each visit
```

## Worked Example

**Input:** 32-year-old woman with moderate-persistent asthma (GINA step 3–4), 3 exacerbations in past 12 months requiring oral steroids, FeNO 55, blood eos 320, currently on fluticasone propionate 220 µg pMDI BID + albuterol prn. Daily symptoms despite adherence. Pollen-allergic.

**Output:**

```
PATIENT SNAPSHOT:
- 32 y F, moderate-persistent asthma, GINA step 4 (uncontrolled despite ICS), eosinophilic + T2-high phenotype (FeNO 55, eos 320), atopic, 3 exacerbations/yr requiring OCS.
- Current: fluticasone 220 µg BID (medium-dose ICS) + albuterol prn — insufficient.

REGIMEN (transition to GINA Step 4 Track 1 MART preferred):
- **Maintenance + reliever: budesonide-formoterol 160/4.5 µg (Symbicort DPI Turbuhaler or pMDI)** — **2 puffs BID** + **as-needed for symptoms (max 12 puffs/day)** — MART approach.
- **Consider biologic add-on**: given eosinophilic phenotype + ≥3 exacerbations/year + ongoing OCS need, the patient qualifies for **dupilumab 200 mg SC q2 weeks** (loading dose 400 mg) — covers both T2-high features (eos + FeNO + atopic) and rhinitis comorbidity.
  - Alternatives: mepolizumab 100 mg SC q4 weeks (eosinophilic), benralizumab 30 mg SC q4 weeks ×3 then q8 weeks, tezepelumab 210 mg SC q4 weeks (broad).
- **Discontinue albuterol as routine reliever** under MART; albuterol available for severe acute episodes only.

RATIONALE:
- MART preferred per GINA: addresses inflammation at the time of symptom escalation, reduces severe exacerbations vs SABA-only reliever.
- Step 4 upgrade given current uncontrolled status on medium-dose ICS.
- Biologic indication: severe eosinophilic and atopic asthma not controlled on step 4–5; reduces exacerbations and OCS use; dupilumab particularly favorable given comorbid allergic rhinitis.
- Spacer for pMDI if patient prefers pMDI; DPI Turbuhaler reasonable given normal inspiratory flow.

DEVICE & TECHNIQUE NOTES:
- Symbicort Turbuhaler: load, deep forceful inhalation, hold 5–10s. Rinse mouth after each use.
- If poor inspiratory flow: switch to Symbicort pMDI with spacer.
- Reinforce technique at every visit; demonstrate.

COMORBIDITY ADJUSTMENTS:
- Pollen allergy: nasal corticosteroid (fluticasone furoate 1 spray each nostril daily); H1 antihistamine.
- GERD if present: treat.
- Vaccination: annual influenza, COVID, pneumococcal (PCV20).

ACTION PLAN:
- **Green (well-controlled, no/few symptoms):** Symbicort 2 puffs BID + as-needed for any symptom.
- **Yellow (escalating symptoms, peak flow 50–80%):** continue maintenance + use as-needed (up to 12/day); if symptoms persist >24–48 h, contact clinician.
- **Red (severe symptoms, peak flow <50%, can't speak full sentences, blue lips):** call 911 / emergency department; start prednisone 40 mg PO daily ×5 days if pre-prescribed.

MONITORING:
- ACT score monthly initially.
- Exacerbation count and OCS use tracked.
- FeNO and eos at 3, 6, 12 months on biologic (eos may drop dramatically on mepolizumab/benralizumab; less so on dupilumab).
- Spirometry at 6 months.
- DEXA every 2 years if chronic OCS use prior or high-dose ICS long-term.
- Adherence and technique check at every visit.

WHEN TO ESCALATE:
- Inadequate response to dupilumab at 4–6 months → switch biologic (mepolizumab, benralizumab, tezepelumab) based on phenotype.
- Bronchial thermoplasty if severe, very specific phenotype, refractory.
- Pulmonology referral if not already.

FOLLOW-UP:
- 1 month: tolerability of Symbicort, MART use pattern, biologic injection technique (in-clinic first dose).
- 3 months: ACT, FeNO, eos, exacerbation count.
- 6 months: spirometry, control reassessment, OCS use.
- Every 3 months thereafter for biologic continuation review.
```
