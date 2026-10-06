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
updated: "2026-10-06"
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
> **Review status:** AI-assisted content, reviewed by AI only (2026-10-06);
> **not yet reviewed by a licensed clinician.**

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

1. **Stroke prevention first (the highest-yield decision).** Score CHA2DS2-VASc (the thresholds below are the ACC/AHA 2023 ones; the ESC 2024 AF-CARE guideline uses CHA2DS2-VA, which omits sex, with its own thresholds) [VERIFY: current ACC/AHA or ESC AF guideline, whichever is used locally].
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

## False-Positive Prevention

❌ **DON'T:**
- Back-calculate serum creatinine from eGFR to settle the apixaban "Cr ≥1.5" criterion; the label uses measured creatinine, so without it the dose line reads `[serum Cr needed]`.
- Use eGFR in place of Cockcroft-Gault CrCl for rivaroxaban, dabigatran or edoxaban dose bands; those thresholds are CrCl and need age, weight, sex and creatinine.
- Award CHA2DS2-VASc or HAS-BLED points for items the input does not document (e.g., "vascular disease" inferred from diabetes, HF from dyspnea alone).
- Choose a rate- or rhythm-control drug without checking LVEF from the input — a diltiazem or flecainide line reads routine until the EF or CAD status is looked up.

✅ **DO:**
- Re-add CHA2DS2-VASc and HAS-BLED one input-supported point at a time and show the sum (e.g., HTN 1 + age 65–74 1 + female 1 + diabetes 1 = 4).
- Compute CrCl by Cockcroft-Gault before naming any DOAC dose, and state which label criterion the chosen dose rests on, tagged `[VERIFY: current product label]`.
- Check the current-medication list for interactions with the chosen anticoagulant and antiarrhythmic (strong CYP3A4/P-gp inhibitors or inducers; amiodarone with digoxin or warfarin).

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
- Apixaban — dose pending serum creatinine. Dose-reduction criteria: age ≥80 (no), weight ≤60 (yes, 58 kg), Cr ≥1.5 ([serum Cr needed] — not derivable from eGFR 48). If Cr <1.5 → 1 of 3 criteria → 5 mg BID; if Cr ≥1.5 → 2 of 3 → 2.5 mg BID.
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
- Serum creatinine at least annually and with illness (apixaban dosing); HR/symptom burden; bleeding check.

PITFALLS:
- Do not finalize the apixaban dose without measured serum creatinine — weight already meets 1 reduction criterion, so Cr decides between 5 mg and 2.5 mg BID.
- Do not cardiovert without 3 wk anticoagulation or TEE.
- Confirm CAD status before flecainide.
```
