---
title: "Pharmacokinetics Reasoning"
category: domain-healthcare-clinical/pathophysiology
description: "Reason through ADME parameters (absorption, distribution, metabolism, elimination), Vd, clearance, half-life, steady state, and dosing implications for a specific drug in a specific patient."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - CR-01
  - QA-01
difficulty: advanced
tags:
  - pharmacology
  - pharmacokinetics
  - dosing
  - mechanism
updated: "2026-05-08"
---

## Objective

Given a drug and a patient (with relevant pathophysiology), reason through the pharmacokinetic parameters and explain how dosing should be adjusted, why steady state will or will not be reached at the standard regimen, and what plasma concentration trajectory to predict. Output is a numerical and mechanistic walk, not a lookup.

## Inputs

- Drug name (with route, dose, frequency)
- Patient parameters: age, weight, height, sex, eGFR, ALT/AST/bilirubin/albumin (hepatic function), volume status, pregnancy/lactation if relevant, drug-drug interactions, dialysis status
- Optional: target plasma concentration, therapeutic drug monitoring (TDM) result, observed clinical effect or toxicity

## Role

Senior clinical pharmacologist or critical care attending teaching dosing logic. Comfortable with PK math and mechanism.

## Reasoning Steps

1. **Restate the clinical question.** "Should this dose be adjusted?" or "Why isn't this drug working?" or "Why is this level supratherapeutic?" — frame the answer around the actual question.

2. **Walk ADME for this drug.**
   - **Absorption:** route, oral bioavailability (F), food effect, transporters at gut wall (P-gp, BCRP), first-pass metabolism in gut wall and liver. If IV, F = 1.
   - **Distribution:**
     - Volume of distribution (Vd): low (~0.1–0.3 L/kg, plasma-bound) for highly protein-bound drugs (warfarin, valproate); intermediate (~0.5–1 L/kg, total body water) for hydrophilic drugs (aminoglycosides, vancomycin partly); high (>2 L/kg, lipophilic, tissue-distributed) for amiodarone (~60 L/kg), digoxin (~7 L/kg), tricyclics
     - Protein binding: % bound, albumin vs alpha-1-acid glycoprotein, displaceable in hypoalbuminemia
     - Tissue penetration: CSF (lipophilicity, P-gp), prostate, lung, biofilm
     - Loading dose: LD = Vd × Cp_target / F. Required when steady state is far away and rapid effect needed.
   - **Metabolism:**
     - Phase I: CYP enzymes (3A4, 2D6, 2C9, 2C19, 1A2, 2B6, 2E1) — substrate, inducer, inhibitor profile. Genetic polymorphisms (CYP2D6 ultrarapid, poor metabolizer; CYP2C19 in clopidogrel; CYP2C9 + VKORC1 in warfarin)
     - Phase II: glucuronidation (UGTs), sulfation, acetylation (NAT2 fast/slow acetylators for INH)
     - Prodrug activation: codeine → morphine via CYP2D6; clopidogrel → active metabolite via CYP2C19; tamoxifen → endoxifen via CYP2D6
   - **Elimination:**
     - Routes: renal (filtration vs tubular secretion vs reabsorption), hepatic (biliary excretion, enterohepatic recycling), pulmonary (volatile anesthetics), fecal
     - Clearance (CL): volume of plasma cleared per unit time
     - First-order (linear) vs zero-order (saturable) kinetics — examples of zero-order: ethanol, phenytoin (at therapeutic levels), salicylate at toxic levels

3. **Calculate or estimate.**
   - **Half-life (t½) = 0.693 × Vd / CL.** Longer t½ when Vd large or CL small.
   - **Steady state** reached at ~4–5 half-lives.
   - **Cp at steady state** = Dose × F / (CL × tau) for IV/oral with frequency tau.
   - **Loading dose** = Vd × Cp_target / F.
   - **AUC** = Dose × F / CL (linear PK).

4. **Adjust for patient pathophysiology.**
   - **Renal impairment:** for renally cleared drugs, dose ∝ eGFR. Cockcroft-Gault traditionally for drug dosing (predates eGFR; still printed on package inserts for vanc, aminoglycosides, DOACs). Use measured CrCl when muscle mass is unusual (cachexia, amputee, body builder).
   - **Hepatic impairment:** Child-Pugh. CYP activity falls more with severe disease; phase II glucuronidation more preserved than phase I. Reduced first-pass increases F for some drugs (propranolol, morphine, tramadol).
   - **Hypoalbuminemia:** raises free fraction of highly protein-bound drugs (warfarin, phenytoin, valproate). Total level falsely low; free level may be normal or high. Use free phenytoin or correct: corrected = measured / (0.2 × albumin + 0.1) when albumin <3.5; use 0.1 instead of 0.2 for ESRD.
   - **Volume status:** affects Vd of hydrophilic drugs. In sepsis, third-spacing expands Vd of vancomycin and aminoglycosides; underdosing common in early sepsis.
   - **Obesity:** dosing weight depends on drug. Lipophilic drugs use total body weight (TBW); hydrophilic drugs often use ideal body weight (IBW) or adjusted body weight (AdjBW).
   - **Dialysis:** drugs with low Vd, low protein binding, low molecular weight, and high water solubility are dialyzable (vanc partly, aminoglycosides yes, lithium yes, salicylate yes, methotrexate partly). Highly protein-bound or large Vd drugs are not (digoxin no, amiodarone no, phenytoin minimal).
   - **Drug-drug interactions:** CYP inducers (rifampin, phenytoin, carbamazepine, phenobarb, St John's wort) ramp up over days–weeks and reduce levels of CYP substrates. CYP inhibitors (fluconazole 2C9, fluoxetine/paroxetine 2D6, clarithromycin/erythromycin 3A4, ritonavir 3A4, grapefruit 3A4) take effect quickly and raise levels.

5. **Predict the trajectory.** What will the plasma level look like at 12, 24, 48 hours? Will it accumulate? Will it reach steady state?

6. **Recommend specific adjustment.** Loading dose (yes/no with number), maintenance dose change (with number), interval change, monitoring frequency.

## Output Format

```
DRUG: [name, route, dose, frequency]
PATIENT: [relevant parameters]
QUESTION: [restate]

ADME WALK:
- Absorption / F: [...]
- Distribution / Vd / protein binding: [...]
- Metabolism / CYP: [...]
- Elimination / CL / t½: [...]

CALCULATIONS:
- Vd estimate: [...]
- CL estimate: [...]
- t½: [...]
- Time to steady state: [...]
- Cp_ss expected: [...]

PATIENT-SPECIFIC ADJUSTMENT:
- [factor 1] → [effect on PK] → [dosing implication]
- [factor 2] → [...]

TRAJECTORY PREDICTION:
- [Cp at first dose, 24h, 48h, steady state]
- [accumulation risk, toxicity threshold]

DOSING RECOMMENDATION:
- Loading dose: [yes/no, mg/kg or absolute mg]
- Maintenance dose: [mg, frequency]
- Monitoring: [trough, peak, AUC, level timing, frequency]
```

## Worked Example

**Input:** Vancomycin for MRSA bacteremia in a 78 y/o F, 60 kg, height 160 cm. SCr 1.4 (baseline 0.9), eGFR ~36 (CKD-EPI). Hospital protocol: 25 mg/kg loading dose then 15 mg/kg q12h. Should this dosing be adjusted? Predict trough.

**Output:**

```
DRUG: Vancomycin IV, planned 25 mg/kg load, 15 mg/kg q12h
PATIENT: 78 y/o F, 60 kg, 160 cm, eGFR 36 (CKD-EPI). MRSA bacteremia.
QUESTION: Is this regimen appropriate? What trough to expect?

ADME WALK:
- Absorption / F: IV, F = 1.
- Distribution / Vd / protein binding: Vd ~0.7 L/kg → 60 × 0.7 = 42 L. Protein binding ~50% (variable, falls in hypoalbuminemia and renal failure).
- Metabolism: not significantly metabolized.
- Elimination / CL / t½: ~90% renal (glomerular filtration). CL roughly tracks CrCl. Cockcroft-Gault for this patient: CrCl = (140 − 78) × 60 × 0.85 / (72 × 1.4) = 31 mL/min. t½ in patients with normal renal function ~6–8 h; rises to 24–40+ h in CKD; can be much longer in oliguric AKI. Half-life here estimated ~18–24 h.

CALCULATIONS:
- Vd: 0.7 L/kg × 60 kg = 42 L
- CL ~ CrCl ≈ 31 mL/min × 0.06 = 1.86 L/h (rough mapping vanc CL ≈ CrCl)
- t½ = 0.693 × 42 / 1.86 ≈ 15.6 h
- Time to steady state: 4–5 × t½ = ~62–78 h (2.5–3 days)
- Loading dose target Cp ~30 mg/L: Vd × Cp = 42 × 30 = 1260 mg → 25 mg/kg × 60 kg = 1500 mg gives ~36 mg/L immediate post-distribution. Reasonable.

PATIENT-SPECIFIC ADJUSTMENT:
- Reduced renal clearance (CrCl 31) → CL roughly halved relative to a young adult with CrCl 100 → standard 15 mg/kg q12h will accumulate. Trough at 12 h after second dose will rise above target.
- Age 78 with mild AKI superimposed on baseline CKD raises concern that CrCl will fall further; vanc accumulates as renal function declines.
- Hypoalbuminemia (if present, common in elderly with infection) increases free fraction; for vanc, this is less clinically managed than for highly protein-bound drugs but worth noting.
- Vanc is a known nephrotoxin; AUC-based dosing minimizes nephrotoxicity vs trough-based dosing.

TRAJECTORY PREDICTION:
- After 25 mg/kg load: peak (post-distribution, ~2 h post-infusion) ~30–35 mg/L.
- After 15 mg/kg q12h: trough at 12 h after first maintenance dose ~16–20 mg/L if function stable.
- By 48 h: at this CL, drug accumulates. Trough likely 20–25 mg/L if maintained at q12h dosing.
- AUC at steady state: AUC24 ≈ Daily dose / CL. Daily dose 30 mg/kg = 1800 mg. CL ≈ 31 × 0.06 × 24 = 44.6 L/24h. AUC24 ≈ 40 mg·h/L. Target for serious MRSA infection is AUC24/MIC 400–600 (assuming MIC 1) → AUC 400–600. Underdosed if MIC 1; overdosed if MIC 0.5.
- The single-trough approach is inferior to AUC-based monitoring here. Recommend AUC.

DOSING RECOMMENDATION:
- Loading dose: 25 mg/kg = 1500 mg IV over 90 min (slow infusion to avoid red man syndrome). Yes — load is appropriate; do not skip just because of CKD. The load fills Vd and is independent of CL.
- Maintenance dose: 15 mg/kg q24h initially (1000 mg q24h rounded, or 750 q12h with two-level AUC monitoring). Standard q12h is too frequent for this CL.
- Monitoring:
  - Bayesian AUC dosing using one or two levels — preferred. Get level around 4–6 h post-loading-dose end and trough before second dose; calculate AUC24, target 400–600 for MRSA bacteremia.
  - If trough-only: target trough 15–20 mg/L for serious MRSA infection. Draw before 4th dose if dosing q12h, or before 2nd dose if dosing q24h (sooner because t½ is long).
  - Daily SCr to track renal function. Hold or extend interval if Cr rises ≥50% from baseline.
  - Source control + repeat blood cultures q48h until clear; total 2–6 weeks of therapy depending on complications.
```
