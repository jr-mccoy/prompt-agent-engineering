---
title: "Hypertension Longitudinal Care Plan"
category: domain-healthcare-clinical/care-plans
description: "Build a hypertension management plan: confirm and stage, set comorbidity-adjusted targets, select and titrate agents, and work up resistant or secondary hypertension with named doses."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
  - DS-02
difficulty: intermediate
tags:
  - cardiology
  - hypertension
  - care-plan
  - chronic-disease
updated: "2026-06-19"
---

## Objective

Produce a hypertension care plan: confirm the diagnosis with appropriate measurement, set an individualized BP target, select first- and second-line agents by compelling indication, define the titration cadence, and trigger resistant/secondary workup when indicated. Output is a stepwise plan to target.

## Inputs

- BP data: office, home/ambulatory readings, technique, pattern (sustained vs white-coat vs masked)
- Patient: age, race, comorbidities (diabetes, CKD/UACR, CAD, HF, prior stroke, gout, pregnancy plans), weight
- Labs: BMP (K, Cr/eGFR), UACR, lipids, glucose/A1c
- Current regimen: agents, doses, adherence; OTC/contributors (NSAIDs, decongestants, alcohol, stimulants)
- Resistant features: ≥3 agents at max dose including a diuretic and still above goal

## Role

Internist or cardiologist managing hypertension longitudinally.

## Reasoning Steps

1. **Confirm and stage** with proper technique and out-of-office readings (home/ABPM) to exclude white-coat. Stage 1: 130–139/80–89; Stage 2: ≥140/90.

2. **Set target.** General <130/80 for most (especially diabetes, CKD, ASCVD, ≥10% 10-yr risk). Individualize in frailty/orthostasis. SBP <120 reasonable in selected high-risk patients tolerating it (SPRINT).

3. **First-line agents (any of three classes; combine early for Stage 2 or >20/10 above goal):**
   - Thiazide-type (chlorthalidone 12.5–25 mg preferred over HCTZ for potency/duration; indapamide)
   - ACEi (lisinopril) or ARB (losartan/valsartan) — preferred with diabetes, CKD/albuminuria, HF, post-MI
   - Dihydropyridine CCB (amlodipine 5–10 mg)
   - **Do not combine ACEi + ARB.**

4. **Compelling indications:**
   - Diabetes/CKD with albuminuria → ACEi or ARB.
   - HFrEF → ARNI/ACEi + beta-blocker + MRA + diuretic.
   - Post-MI/CAD → beta-blocker + ACEi/ARB.
   - Black patients without HF/CKD → thiazide or CCB first.
   - Pregnancy → labetalol, nifedipine ER, methyldopa; avoid ACEi/ARB.

5. **Titrate every 2–4 weeks**; prefer single-pill combinations (e.g., amlodipine/valsartan, lisinopril/HCTZ) for adherence. Most need ≥2 agents.

6. **Add-on order:** start ACEi/ARB + CCB + thiazide as the standard triple; if uncontrolled on all three at max dose → resistant hypertension.

7. **Resistant HTN:** confirm adherence and out-of-office BP, remove contributors (NSAIDs, salt, alcohol, sleep apnea), then add **spironolactone 25 mg** (4th-line, most effective) if K/eGFR allow; alternatives eplerenone, beta-blocker, hydralazine.

8. **Secondary workup** when resistant, young (<30), abrupt onset, or features: aldosterone/renin ratio (primary aldosteronism — common, underdiagnosed), renal artery imaging (renovascular), metanephrines (pheo), TSH, OSA screen, Cushing features, coarctation.

9. **Monitor:** BMP within 1–2 weeks of ACEi/ARB/MRA start or change; home BP log; UACR/eGFR; address lifestyle (DASH, sodium <1.5–2.3 g, weight, alcohol, activity).

## Output Format

```
DIAGNOSIS / STAGE / CONFIRMATION (home/ABPM):
BP TARGET: [value + rationale]

REGIMEN PLAN:
- First-line by indication: [agent, dose]
- Second/third agent: [agent, dose]
- Single-pill combination if applicable
- Titration cadence

RESISTANT PATHWAY (if applicable):
- Adherence/contributor check
- Spironolactone 25 mg add-on (K/eGFR gate)

SECONDARY WORKUP (if indicated):
- [ARR, renal imaging, metanephrines, OSA, TSH]

MONITORING:
- BMP after RAAS agents, home BP, UACR

LIFESTYLE:
- DASH, sodium, weight, alcohol, activity

PITFALLS:
- [ACEi+ARB combo, missing primary aldosteronism, NSAID contribution, orthostasis in elderly]
```

## Worked Example

**Input:** 52 y/o Black man, office BP 158/96 confirmed on home readings ~150/92. T2DM, UACR 80 mg/g, eGFR 72, K 4.3. BMI 31. Current: amlodipine 10 mg only. Takes ibuprofen for knee pain.

**Output:**

```
DIAGNOSIS / STAGE: Stage 2 (≥140/90), confirmed on home readings.
BP TARGET: <130/80 (diabetes + albuminuria).

REGIMEN PLAN:
- Diabetes + albuminuria = compelling indication for ACEi/ARB: add losartan 50 mg daily (organ protection beyond BP), uptitrate to 100.
- Continue amlodipine 10 mg.
- Likely needs a third agent: add chlorthalidone 12.5 mg if not at goal in 2–4 wk.
- Consider single-pill combination to consolidate (e.g., amlodipine/olmesartan/HCTZ).
- Titrate q2–4 wk.

CONTRIBUTOR:
- Stop ibuprofen (raises BP, blunts ACEi/ARB, nephrotoxic with albuminuria) — switch to topical NSAID or acetaminophen.

RESISTANT PATHWAY:
- Not yet resistant (only 1 agent). Reassess after triple therapy.

SECONDARY WORKUP:
- Not indicated yet; screen OSA given BMI 31 + HTN. If uncontrolled on triple therapy → aldosterone/renin ratio.

MONITORING:
- BMP 1–2 wk after losartan (K, Cr); home BP log; UACR/eGFR q3–6 months.

LIFESTYLE:
- DASH diet, sodium <2.3 g, weight loss, alcohol limit, activity ≥150 min/wk.

PITFALLS:
- Add ARB, not a second RAAS — never ACEi + ARB.
- NSAID is a major reversible contributor here.
- Recheck K after losartan + future chlorthalidone.
```
