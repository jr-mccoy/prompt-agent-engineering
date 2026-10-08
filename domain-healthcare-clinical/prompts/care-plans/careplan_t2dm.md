---
title: "Type 2 Diabetes Longitudinal Care Plan"
category: domain-healthcare-clinical/care-plans
description: "Build a longitudinal type 2 diabetes management plan with A1c targets, organ-protective agent selection, titration, and monitoring cadence using named drugs and doses."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
  - DS-02
difficulty: advanced
tags:
  - endocrine
  - diabetes
  - care-plan
  - chronic-disease
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

Produce a longitudinal type 2 diabetes care plan: individualized A1c target, glucose-lowering regimen sequenced by comorbidity (ASCVD, HF, CKD), titration schedule, monitoring cadence, and the comorbidity/complication surveillance bundle. Output is a problem-oriented plan a colleague could enact at the next three visits.

## Inputs

- Glycemic data: A1c (current and trend), fasting/postprandial fingersticks or CGM time-in-range, hypoglycemia history
- Patient: age, weight/BMI, eGFR, UACR, duration of diabetes, ASCVD or HF status, frailty/life expectancy
- Current regimen: agents, doses, adherence, tolerability, cost/insurance
- Comorbidities: hypertension, dyslipidemia, NAFLD, neuropathy, retinopathy status, prior CV events
- Barriers: cost, injection willingness, hypoglycemia risk (driver, lives alone, CKD)

## Role

Endocrinologist or primary care attending managing T2DM longitudinally, writing the plan for the care team.

## Reasoning Steps

1. **Individualize the A1c target.** Standard <7%. Tighter (<6.5%) if achievable without hypoglycemia in young, short-duration, no CVD. Looser (<8% or even <8.5%) in frailty, limited life expectancy, hypoglycemia unawareness, advanced complications.

2. **Anchor on metformin** unless eGFR <30 or intolerance. Start 500 mg daily or BID with food, titrate weekly to 1000 mg BID. Hold if eGFR <30; do not start if eGFR <45 (continue with caution).

3. **Layer organ-protective agents by compelling indication — independent of A1c.**
   - **ASCVD or high CV risk:** GLP-1 RA with proven benefit (semaglutide, dulaglutide, liraglutide) OR SGLT2i (empagliflozin, canagliflozin).
   - **Heart failure (HFrEF or HFpEF):** SGLT2i (dapagliflozin or empagliflozin) — class benefit regardless of diabetes.
   - **CKD (UACR ≥200 or eGFR 25–60):** SGLT2i first (dapagliflozin/empagliflozin slow progression); add finerenone if persistent albuminuria on ACEi/ARB + SGLT2i.
   - **Obesity-dominant:** GLP-1 RA or dual GIP/GLP-1 (tirzepatide) for weight + glycemic effect.

4. **If A1c remains above target,** intensify: combine GLP-1 RA + SGLT2i (complementary), then consider basal insulin.

5. **Basal insulin start:** glargine or detemir 10 units (or 0.1–0.2 units/kg) at bedtime; titrate 2 units q3 days to fasting glucose 80–130. Add prandial rapid-acting only if A1c uncontrolled on adequate basal (fasting at goal but A1c high → postprandial gap).

6. **Deprescribe sulfonylureas** (glipizide) and reduce insulin when adding GLP-1 RA/SGLT2i to limit hypoglycemia.

7. **Complication surveillance bundle:** annual dilated retinal exam, annual UACR + eGFR, monofilament foot exam each visit, lipid panel, BP target <130/80, statin per ASCVD risk, ACEi/ARB if albuminuric.

8. **Lifestyle and vaccines:** MNT referral, ≥150 min/week activity, smoking cessation; pneumococcal, annual influenza, hepatitis B, COVID per schedule.

## False-Positive Prevention

❌ **DON'T:**
- Label CKD from one eGFR or one UACR — both need persistence (>3 months); report the KDIGO G and A categories together (eGFR 52 + UACR 340 mg/g = G3a/A3) rather than "CKD" alone.
- Add a GLP-1 RA or tirzepatide without checking for personal/family medullary thyroid carcinoma or MEN2, prior pancreatitis, and current retinopathy grade (rapid A1c lowering with semaglutide has been linked to retinopathy worsening).
- Add an SGLT2i without checking for prior DKA, a very-low-carbohydrate diet, or features of insulin deficiency (LADA, pancreatogenic diabetes) — the euglycaemic-DKA counselling line is not the same as screening for it.
- Present the "expected A1c drop" of a combination as a sum of single-agent effects; SGLT2i glycaemic effect shrinks as eGFR falls, so label the figure an estimate.
- Leave the metformin dose unchanged across an eGFR band change; state the band and the label action for it `[VERIFY: metformin label]`.

✅ **DO:**
- Trace each organ-protective agent to the input finding that triggers it (the dated ASCVD event, HF type and EF, eGFR and UACR values), and each eGFR-dependent line (metformin, SGLT2i initiation, sulfonylurea, finerenone) to the current eGFR with its date.
- Check the visit-by-visit schedule against each titration interval: no GLP-1 RA step sooner than the label interval, and the BMP after SGLT2i/ACEi changes actually placed in a visit row.
- When a sulfonylurea or insulin is reduced or stopped, write the expected glucose effect and the fingerstick/CGM check that will catch a rebound.

## Output Format

```
A1c TARGET: [value + rationale]
CURRENT A1c / TREND:

GLUCOSE-LOWERING PLAN:
- Foundation: [metformin dose or reason omitted]
- Organ-protective agent: [drug, dose, indication driving choice]
- Add-on(s): [drug, dose]
- Titration schedule: [agent → increment → interval → target]
- Deprescribe: [agents to stop/reduce + reason]

MONITORING:
- A1c q3 months until stable, then q6 months
- Renal function before/after SGLT2i; eGFR/UACR annually
- CGM/fingerstick plan; hypoglycemia counseling

COMORBIDITY / COMPLICATION BUNDLE:
- BP target + agent
- Statin decision
- ACEi/ARB if albuminuric
- Retina / foot / UACR schedule
- Vaccines

VISIT-BY-VISIT (next 3 visits):
- Visit 1: [actions]
- Visit 2: [actions]
- Visit 3: [actions]

SAFETY / PITFALLS:
- [SGLT2i euglycemic DKA, GU infection, volume; GLP-1 GI titration; insulin/SU hypoglycemia]
```

## Worked Example

**Input:** 58 y/o M, T2DM 6 years, A1c 8.4%, BMI 33, eGFR 52, UACR 340 mg/g, prior NSTEMI 2 years ago. Current: metformin 1000 mg BID, glipizide 10 mg daily. BP 138/84 on lisinopril 20 mg. LDL 78 on atorvastatin 40 mg. No hypoglycemia.

**Output:**

```
A1c TARGET: <7% — relatively young, established ASCVD and CKD make organ protection the priority over tight glycemia.
CURRENT A1c / TREND: 8.4%, above goal.

GLUCOSE-LOWERING PLAN:
- Foundation: continue metformin 1000 mg BID (eGFR 52, acceptable).
- Organ-protective agent #1 (CKD + albuminuria + ASCVD): empagliflozin 10 mg daily → 25 mg. Slows CKD progression, HF/CV benefit.
- Organ-protective agent #2 (ASCVD + obesity + A1c gap): semaglutide 0.25 mg SC weekly × 4 wk → 0.5 → 1.0 mg. CV benefit + weight loss.
- Deprescribe: stop glipizide — hypoglycemia risk with no organ benefit, redundant once GLP-1/SGLT2i on board.
- Expected A1c drop with empagliflozin + semaglutide ≈ 1.5–2%, should reach goal.

MONITORING:
- A1c in 3 months.
- BMP 1–2 weeks after empagliflozin start (expect small eGFR dip — do not stop for that), then eGFR/UACR q3–6 months.
- Counsel SGLT2i sick-day rules (hold if not eating/acutely ill — euglycemic DKA), GU hygiene.
- Semaglutide GI titration counseling; slow up-titration.

COMORBIDITY / COMPLICATION BUNDLE:
- BP 138/84, target <130/80: uptitrate lisinopril to 40 mg (also maximizes albuminuria benefit).
- Statin: LDL 78 on atorvastatin 40 — post-MI very-high-risk, target LDL <55. Uptitrate to atorvastatin 80 mg; add ezetimibe 10 mg if still >55.
- ACEi already on; finerenone candidate later if UACR stays elevated on empagliflozin + max ACEi.
- Annual dilated retinal exam (order), monofilament foot exam today, UACR/eGFR scheduled.
- Vaccines: influenza, pneumococcal, hepatitis B, COVID per schedule.

VISIT-BY-VISIT:
- Visit 1: stop glipizide, start empagliflozin 10 mg + semaglutide 0.25 mg, uptitrate lisinopril + atorvastatin, foot exam, order retina + labs.
- Visit 2 (1 month): semaglutide to 0.5 mg, review GI tolerance, BMP review.
- Visit 3 (3 months): A1c, eGFR/UACR; semaglutide to 1.0 mg if needed; assess LDL, add ezetimibe if >55.

SAFETY / PITFALLS:
- Do not restart a sulfonylurea — hypoglycemia with no benefit.
- Counsel empagliflozin hold during acute illness/fasting (euglycemic DKA).
- Do not stop empagliflozin for the expected early eGFR dip.
```
