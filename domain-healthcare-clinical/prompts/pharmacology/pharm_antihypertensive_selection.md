---
title: "Antihypertensive Selection by Patient Profile"
category: domain-healthcare-clinical/pharmacology
description: "Select first-line and add-on antihypertensives based on compelling indications, comorbidities, race, age, pregnancy status, target BP, and side-effect profile; specify named drugs, doses, and titration logic per ACC/AHA 2017, ESC/ESH 2023, and KDIGO 2021."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: intermediate
tags:
  - cardiology
  - hypertension
  - pharmacology
  - prescribing
updated: "2026-05-12"
---

## Objective

Select and prescribe a tailored antihypertensive regimen for a specific patient: identify compelling indications that dictate first-line class, choose the right second / third agent for additive mechanism, account for comorbidities and contraindications, specify drug name, starting dose, titration schedule, target BP, and monitoring. Output names the drug, dose, frequency, monitoring labs, and reassessment timing.

## Inputs

- Age, sex, race / ancestry, weight, comorbidities (DM, CKD, CAD, HF, AFib, stroke, gout, asthma, pregnancy or reproductive potential)
- Current and prior antihypertensives, intolerances
- Baseline office BP and home/24h ambulatory BP if available; orthostatic BP
- Labs: SCr, eGFR, K, Na, glucose, lipids, UACR; urinalysis
- Concurrent medications (NSAIDs, OCPs, decongestants, immunosuppressants, antidepressants that raise BP)
- Lifestyle context (sodium intake, alcohol, exercise, sleep apnea risk)
- Target BP per guideline / patient circumstance (see step 1)

## Role

Senior internist / cardiologist / nephrologist writing the prescription with explicit reasoning for class selection.

## Reasoning Steps

1. **Establish target BP.**
   - **ACC/AHA 2017:** <130/80 for most adults including DM, CKD, ASCVD, ≥65; lower thresholds in some high-risk groups.
   - **ESC/ESH 2023:** office <140/90; <130/80 for most if tolerated; <140/80 in older.
   - **KDIGO 2021 (CKD):** SBP <120 on standardized office measurement.
   - **Pregnancy:** <140/90 in chronic HTN with labetalol, nifedipine, methyldopa per ACOG; lower in preeclampsia per institution.
   - **Hypertensive emergency:** reduce MAP ~25% in first hour, then 160/100 over next 2–6 h, then normal over 24–48 h (faster in aortic dissection and eclampsia).

2. **Identify compelling indications (Class I / IIa indications that drive class choice).**
   - **HFrEF (EF ≤40%):** ACEi or ARB + β-blocker (carvedilol, metoprolol succinate, bisoprolol) + MRA (spironolactone, eplerenone) + ARNI (sacubitril/valsartan) when stable + SGLT2i (dapagliflozin or empagliflozin) — these are also antihypertensive.
   - **HFpEF:** SGLT2i (empagliflozin, dapagliflozin), spironolactone, ARNI (post-PARAGON: benefit signal in lower EF subgroup), diuretics; avoid CCBs negative inotropic (verapamil, diltiazem).
   - **Post-MI / CAD:** β-blocker + ACEi (or ARB); add MRA if HFrEF post-MI.
   - **Stable angina:** β-blocker first-line for symptoms + BP; CCB (amlodipine, diltiazem) addition or alternative; nitrates.
   - **AFib (rate control + HTN):** β-blocker or non-DHP CCB (diltiazem, verapamil — avoid in HFrEF).
   - **Diabetes with albuminuria (UACR ≥30):** ACEi or ARB first-line; add SGLT2i (cardiorenal benefit; reduces BP modestly); add finerenone (non-steroidal MRA) for diabetic CKD with persistent albuminuria.
   - **CKD without DM:** ACEi/ARB if albuminuria present; SBP target <120 per KDIGO; add CCB and/or thiazide-type (chlorthalidone) for combination.
   - **Stroke (secondary prevention):** ACEi + thiazide (PROGRESS).
   - **Pregnancy / women of reproductive age not on contraception:** avoid ACEi, ARB, direct renin inhibitor, MRA (teratogenic); use labetalol, nifedipine ER, methyldopa.
   - **Pheochromocytoma:** α-blocker first (phenoxybenzamine or doxazosin), then β-blocker (never β-first — unopposed α can precipitate hypertensive crisis).
   - **Aortic dissection / aneurysm:** β-blocker first to reduce dP/dt, then add vasodilator (nicardipine, nitroprusside).

3. **For uncomplicated HTN, choose by demographic/PK rationale.**
   - **Black adults without compelling indication for ACEi/ARB:** thiazide or CCB first-line (lower renin, less ACEi response on monotherapy; combination with ACEi/ARB is still effective and indicated when DM/CKD/HF present).
   - **Older adults:** CCB or thiazide first-line (HYVET supported BP lowering in ≥80); watch orthostasis with α-blockers and high-dose diuretics.
   - **Younger adults with high renin:** ACEi/ARB or β-blocker reasonable.

4. **Combine drugs by complementary mechanism.**
   - **RAAS blockade (ACEi or ARB) + diuretic** — synergistic; diuretic activates RAAS, ACEi/ARB blocks it.
   - **RAAS blockade + CCB** — orthogonal mechanisms; ACCOMPLISH trial favored ACEi + CCB over ACEi + thiazide in higher-risk patients.
   - **Triple: RAAS + CCB + diuretic** — common third agent regimen.
   - **Add 4th agent: spironolactone 25–50 mg/d** — most effective add-on for resistant HTN per PATHWAY-2; monitor K and SCr.
   - **Avoid combining:** ACEi + ARB (no benefit, ↑ AKI / hyperkalemia); two non-DHP CCB; β-blocker + non-DHP CCB (bradycardia, conduction block — verapamil or diltiazem with β-blocker is hazardous).

5. **Choose specific agents with starting doses and titration.**
   - **ACEi:** lisinopril 10 mg PO daily (titrate 20–40 mg); ramipril 2.5 mg PO daily → 10 mg; benazepril 10–40 mg/d; enalapril 5–20 mg PO BID. Cough (kinin accumulation), angioedema (rare; higher in Black patients) → switch to ARB.
   - **ARB:** losartan 50 mg PO daily → 100 mg; valsartan 80–320 mg/d; olmesartan 20–40 mg/d; telmisartan 40–80 mg/d (longest t½). Generally cough/angioedema lower than ACEi.
   - **CCB (dihydropyridine):** amlodipine 5 mg PO daily → 10 mg; nifedipine ER 30–90 mg PO daily; felodipine 5–10 mg/d. Pedal edema (dose-dependent); flushing, headache early.
   - **CCB (non-DHP):** diltiazem ER 180 mg PO daily → 360 mg; verapamil ER 180–480 mg/d. Bradycardia, AV block, constipation (verapamil > diltiazem). Avoid in HFrEF.
   - **Thiazide / thiazide-like:** chlorthalidone 12.5–25 mg PO daily (preferred — longer t½, better outcomes); hydrochlorothiazide 12.5–50 mg/d; indapamide 1.25–2.5 mg/d. Hypokalemia, hyponatremia, hyperuricemia, ↑ lipids, glucose. Loop diuretic (furosemide) used when GFR <30 (thiazides lose effect).
   - **β-blocker:** carvedilol 6.25 mg PO BID → 25 mg BID (50 mg BID for >85 kg); metoprolol succinate 25–200 mg PO daily; bisoprolol 2.5–10 mg/d; atenolol 25–100 mg/d (less preferred for primary HTN per LIFE; cardio-selectivity decreases at high doses). Asthma — prefer cardioselective at low dose if needed.
   - **MRA:** spironolactone 25–50 mg PO daily; eplerenone 25–50 mg BID. K and SCr monitoring; gynecomastia with spironolactone; eplerenone more selective.
   - **α-blocker:** doxazosin 1 mg qHS → 4–8 mg; useful for BPH symptoms; orthostatic hypotension; not first-line for HTN per ALLHAT (worse HF outcomes).
   - **Central α2-agonist:** clonidine 0.1 mg PO BID → 0.3 mg BID; dry mouth, sedation, rebound HTN on abrupt cessation; useful in resistant HTN as add-on.
   - **Direct vasodilators:** hydralazine 25–100 mg PO TID-QID (reflex tachycardia, lupus-like syndrome); minoxidil 2.5–10 mg PO BID (refractory; hirsutism, fluid retention — pair with loop + β-blocker).
   - **Newer:** sacubitril/valsartan 24/26 → 97/103 mg PO BID for HF; aliskiren (direct renin inhibitor) — avoid with ACEi/ARB.

6. **Address resistant hypertension (BP above goal despite 3 agents including diuretic at optimal doses).**
   - Confirm with home BP / 24h ABPM (white coat in 30% of "resistant").
   - Confirm adherence (urinary drug screen for antihypertensives in some clinics; pill count).
   - Optimize doses to maximum tolerated.
   - Switch HCTZ to chlorthalidone if not already.
   - Add spironolactone 25–50 mg (PATHWAY-2: most effective 4th drug).
   - Evaluate secondary causes: aldosterone-to-renin ratio (primary aldosteronism in 5–15% of resistant HTN), renal artery stenosis (asymmetric kidney size, abdominal bruit, FMD in younger women, atherosclerotic in older), OSA, Cushing's, pheochromocytoma, drug-induced (NSAIDs, OCP, decongestants, stimulants, calcineurin inhibitors).
   - Consider renal denervation (catheter-based) — newer device approvals (2023) for resistant HTN.

7. **Tie monitoring to drug class.**
   - ACEi/ARB: SCr and K within 1–2 weeks; 30% SCr rise is acceptable (reflects efferent arteriolar relaxation); >30% → reassess for RAS.
   - MRA: K and SCr at 1 week and 4 weeks.
   - Diuretic: BMP at 2–4 weeks (Na, K, Mg, uric acid).
   - β-blocker: HR, asthma, fatigue, sexual function.
   - CCB: edema check at 2–4 weeks; dose reduction or addition of RAAS blocker often resolves edema.

## Output Format

```
PATIENT SNAPSHOT:
[Demographics, comorbidities, current regimen, baseline BP, target BP, labs]

TARGET BP:
[Numeric target with guideline source and patient-specific rationale]

COMPELLING INDICATIONS:
- [Indication 1] → [class required]
- [Indication 2] → [...]

CONTRAINDICATIONS / CAUTIONS:
- [E.g., pregnancy → avoid ACEi/ARB; HFrEF → avoid non-DHP CCB; gout → caution thiazide]

CHOSEN REGIMEN (start or add):
- Drug 1: [name] [starting dose] PO [frequency] — titrate to [target dose] over [interval]
- Drug 2 (if combination needed at start): [...]
- (Up to 3 agents at this stage)

WHY THIS CLASS COMBINATION:
[Mechanism rationale: complementary action, additive effect, evidence-based outcome benefit]

TITRATION SCHEDULE:
- [Week 2: check BP, labs as relevant; adjust if SBP > target]
- [Week 4–6: next step]
- Up-titrate vs add agent: trigger threshold

MONITORING:
- BP: home BP log, office check at [intervals]
- Labs: [SCr / K / Na / glucose / uric acid timing per drug class]
- Adverse effect surveillance: [class-specific watches]

WHEN TO ESCALATE:
- BP not at goal despite [N] agents at max tolerated → review adherence, switch HCTZ→chlorthalidone, add spironolactone, consider secondary HTN workup
- New AKI, hyperkalemia, severe orthostasis, syncope → hold and reassess

FOLLOW-UP:
[Visit cadence, what to bring, what to reassess]
```

## Worked Example

**Input:** 58-year-old Black man with stage 2 HTN (office 168/102, home average 162/98), T2DM (A1c 7.6%), UACR 78 mg/g, eGFR 71, SCr 1.05, K 4.1. On amlodipine 5 mg daily ×3 months. No prior ACEi/ARB. Initiate appropriate next step.

**Output:**

```
PATIENT SNAPSHOT:
- 58 y Black man with stage 2 HTN, T2DM, microalbuminuria (UACR 78), preserved eGFR 71.
- Current amlodipine 5 mg daily; BP not at goal (162/98 home).
- K 4.1, SCr 1.05 — safe for RAAS initiation.

TARGET BP:
- ACC/AHA 2017 / KDIGO 2021 for DM + CKD with albuminuria: SBP <130/80 (KDIGO actually suggests <120 on standardized measurement; <130/80 reasonable target in routine practice).

COMPELLING INDICATIONS:
- T2DM + albuminuria → **ACEi or ARB** is class I (slows progression of diabetic kidney disease independent of BP effect; reduces UACR).
- Add **SGLT2i** for cardiorenal benefit (empagliflozin or dapagliflozin) — additional BP lowering 3–5 mmHg, slows GFR decline.
- Diabetic CKD with persistent albuminuria despite ACEi/ARB → **finerenone** (non-steroidal MRA) — consider at next titration step.

CONTRAINDICATIONS / CAUTIONS:
- No pregnancy (male). No prior angioedema. No bilateral RAS clinically suspected. K 4.1 (safe). SCr 1.05.

CHOSEN REGIMEN:
- **Lisinopril 10 mg PO daily** — start ACEi.
- **Continue amlodipine 5 mg PO daily** — synergistic with ACEi (ACCOMPLISH-style combination).
- **Add empagliflozin 10 mg PO daily** — cardiorenal indication independent of HbA1c (also lowers BP modestly, reduces albuminuria).
- (No diuretic at this step; reassess.)

WHY THIS COMBINATION:
- ACEi addresses the diabetic CKD with albuminuria indication (slows progression; reduces albuminuria 25–30%).
- ACEi + DHP CCB (amlodipine) is the ACCOMPLISH-preferred dual combination in higher-risk patients (better CV outcomes than ACEi + thiazide).
- SGLT2i adds cardiorenal benefit, additional BP lowering, weight loss, modest diuresis.
- Race is not a contraindication to ACEi when there's a compelling indication (DM + albuminuria). In monotherapy for HTN alone, Black patients often respond less to ACEi monotherapy, but in combination with CCB and with compelling indication, ACEi is appropriate.

TITRATION SCHEDULE:
- Week 2 visit (in-person or virtual): check home BP log, repeat BMP (SCr, K, Na), UACR baseline if not yet done.
- Up-titrate lisinopril to 20 mg if home BP still >130/80 and K/SCr acceptable.
- Up-titrate amlodipine to 10 mg if needed.
- Add chlorthalidone 12.5–25 mg PO daily if still above goal after lisinopril 20 mg + amlodipine 10 mg.
- 4th-line: spironolactone 25 mg daily (resistant HTN strategy).

MONITORING:
- BP: home BP twice daily for 2 weeks initially, then weekly average; office visit at 2 weeks, 6 weeks, 3 months.
- Labs at 2 weeks: SCr, K, Na. Expect SCr rise up to 30% on ACEi (acceptable, reflects efferent dilation); if >30% → reassess for RAS.
- UACR at 3 months — should decline 20–40% on ACEi + SGLT2i.
- HbA1c at 3 months.
- Watch for: ACEi cough (5–10%); switch to ARB (losartan 50 mg) if intolerable. Angioedema (rare; emergency).

WHEN TO ESCALATE:
- BP >130/80 after lisinopril 40 mg + amlodipine 10 mg + chlorthalidone 25 mg + adherence verified → add spironolactone; consider 24h ABPM and secondary HTN workup (aldosterone:renin ratio, sleep study if OSA features, renal duplex if asymmetric kidneys, plasma metanephrines if episodic symptoms).
- Acute SCr rise >30% on ACEi initiation: hold ACEi, evaluate for RAS / volume depletion.
- K >5.5: hold ACEi, address (diet, hold K supplementation, consider patiromer if K elevation due to MRA).

FOLLOW-UP:
- Visit at 2 weeks, 6 weeks, 3 months.
- Bring: home BP log, glucose log, current medication list.
- Reassess: BP, labs, UACR, A1c, adherence, side effects.
- Discuss: lifestyle (sodium <2 g/day, alcohol ≤2/d, exercise 150 min/wk moderate intensity, weight loss if applicable, OSA screening if features present).
```
