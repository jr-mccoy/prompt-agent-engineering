---
title: "Atrial Fibrillation Longitudinal Care Plan"
category: domain-healthcare-clinical/care-plans
description: "Manage atrial fibrillation across the AF-CARE framework: anticoagulation by CHA2DS2-VASc, rate vs rhythm control, and risk-factor modification with named drugs and doses."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
  - DS-02
difficulty: advanced
tags:
  - cardiology
  - atrial-fibrillation
  - anticoagulation
  - care-plan
updated: "2026-06-19"
---

## Objective

Produce an atrial fibrillation management plan: stroke-prevention decision (anticoagulant choice/dose), rate-vs-rhythm control strategy, and comorbidity/risk-factor modification. Output is a longitudinal plan organized around stroke prevention, symptom control, and substrate modification.

## Inputs

- AF characterization: paroxysmal/persistent/permanent, first detected vs known, symptom burden (EHRA class), ventricular rate, valvular (mechanical valve / mod-severe MS) vs non-valvular
- Stroke/bleed risk: CHA2DS2-VASc components, HAS-BLED/modifiable bleed factors, prior stroke/TIA, falls
- Labs/vitals: eGFR/creatinine, weight, BP, Hgb, LFTs, TSH
- Comorbidities: HF/LVEF, CAD, hypertension, OSA, obesity, alcohol, diabetes
- Current meds: rate/rhythm agents, anticoagulant, interacting drugs

## Role

Cardiologist or internist managing AF longitudinally.

## Reasoning Steps

1. **Stroke prevention first (the highest-yield decision).** Score CHA2DS2-VASc.
   - Men ≥2 / women ≥3: anticoagulate.
   - Men 1 / women 2: consider (shared decision).
   - Men 0 / women 1: no anticoagulation.
   - **Mechanical valve or moderate–severe mitral stenosis → warfarin (INR target by valve), NOT a DOAC.**

2. **Choose anticoagulant.** DOAC preferred for non-valvular AF: apixaban 5 mg BID (2.5 if ≥2 of: age ≥80, weight ≤60 kg, Cr ≥1.5), rivaroxaban 20 mg with dinner (15 if CrCl 15–50), dabigatran 150 BID (110/75 by renal/age), edoxaban (avoid if CrCl >95). Dose by renal function and label criteria. Antiplatelets are NOT adequate stroke prophylaxis. Consider LAA occlusion (Watchman) if anticoagulation contraindicated.

3. **Rate control.** Beta-blocker (metoprolol, carvedilol) or non-dihydropyridine CCB (diltiazem, verapamil — avoid in HFrEF) for resting HR <110 (lenient) or stricter if symptomatic. Digoxin as add-on (especially HF/hypotension). Avoid CCB in reduced EF.

4. **Rhythm control — favor earlier, especially within ~1 year of diagnosis (EAST-AFNET 4), symptomatic, HF, or younger patients.**
   - Antiarrhythmic by substrate: no structural disease → flecainide/propafenone (with AV-nodal agent) or dronedarone/sotalol; CAD → sotalol/dronedarone; HF → amiodarone or dofetilide.
   - **Catheter ablation:** first-line or after AAD failure, especially paroxysmal AF and AF + HFrEF (mortality/HF benefit).

5. **Cardioversion:** if AF >48 h or unknown duration, either 3 weeks therapeutic anticoagulation pre-cardioversion or TEE to exclude LAA thrombus; anticoagulate ≥4 weeks after regardless.

6. **Risk-factor / substrate modification (AF-CARE "C"):** weight loss (≥10%), BP control <130/80, OSA treatment, alcohol reduction, glycemic control, exercise — reduces AF burden and recurrence.

7. **Monitor:** renal function (DOAC dosing) at least annually and with illness; rate/rhythm; symptom burden; bleeding; TSH if on amiodarone (plus LFTs, pulmonary).

## Output Format

```
AF TYPE / BURDEN / VALVULAR STATUS:
CHA2DS2-VASc: [score] → HAS-BLED: [score, modifiable factors]

STROKE PREVENTION:
- Anticoagulant: [drug, dose with renal/criteria rationale] (or warfarin if valvular)
- LAA occlusion if applicable

RATE CONTROL:
- [agent, dose, HR target]

RHYTHM CONTROL:
- Strategy (rate vs rhythm) + rationale
- AAD by substrate / ablation referral
- Cardioversion anticoagulation rule if applicable

RISK-FACTOR MODIFICATION:
- Weight, BP, OSA, alcohol, glycemia

MONITORING:
- Renal function, TSH/LFT if amiodarone, bleeding, symptom burden

PITFALLS:
- [DOAC dosing errors, CCB in HFrEF, cardioversion without anticoagulation, antiplatelet as substitute]
```

## Worked Example

**Input:** 70 y/o F, newly diagnosed persistent AF, symptomatic palpitations + mild dyspnea for 3 months. HTN, T2DM, LVEF 55%. BP 144/86, resting HR 104. eGFR 48, weight 58 kg, age 70. No prior stroke. Not anticoagulated.

**Output:**

```
AF TYPE / BURDEN / VALVULAR STATUS: persistent, symptomatic (EHRA II–III), non-valvular.
CHA2DS2-VASc: HTN(1) + age 65–74(1) + female(1) + diabetes(1) = 4 → anticoagulate.
HAS-BLED: HTN, age — modifiable: BP control. No high-bleed contraindication.

STROKE PREVENTION:
- Apixaban 5 mg BID. Dose-reduction criteria: age ≥80 (no), weight ≤60 (yes, 58 kg), Cr ≥1.5 (eGFR 48 ≈ Cr ~1.1, no) → only 1 of 3 criteria → full dose 5 mg BID.
- Antiplatelet not a substitute.

RATE CONTROL:
- Metoprolol succinate 50 mg daily, titrate to resting HR <110 (stricter given symptoms). LVEF 55 — diltiazem also acceptable but beta-blocker preferred here.

RHYTHM CONTROL:
- Symptomatic + within 1 year of diagnosis → pursue rhythm control (EAST-AFNET 4).
- Plan elective cardioversion: AF >48 h → anticoagulate apixaban ≥3 weeks first OR TEE; continue ≥4 weeks after.
- AAD if recurs: no significant structural disease/CAD → flecainide (need to exclude CAD first given diabetes; if CAD, use sotalol/dronedarone). Refer for catheter ablation discussion.

RISK-FACTOR MODIFICATION:
- BP <130/80 (add/uptitrate ACEi/ARB — also CV/renal benefit in diabetes).
- Screen for OSA; weight loss; glycemic optimization; alcohol counseling.

MONITORING:
- eGFR at least annually and with illness (apixaban dosing); HR/symptom burden; bleeding check.

PITFALLS:
- Do not under-dose apixaban — only 1 reduction criterion met, so full dose.
- Do not cardiovert without 3 wk anticoagulation or TEE.
- Confirm CAD status before flecainide.
```
