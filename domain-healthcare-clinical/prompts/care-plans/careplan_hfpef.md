---
title: "HFpEF Longitudinal Care Plan"
category: domain-healthcare-clinical/care-plans
description: "Manage heart failure with preserved ejection fraction: SGLT2i foundation, comorbidity-targeted therapy, decongestion, and phenotype-specific workup with named doses."
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
  - heart-failure
  - hfpef
  - care-plan
updated: "2026-06-19"
---

## Objective

Produce a HFpEF (LVEF ≥50%) care plan: confirm the diagnosis, install SGLT2i foundation, treat the dominant comorbidities that drive symptoms, manage congestion, and screen for specific phenotypes (amyloid, ischemia, valvular). Output is a problem-oriented longitudinal plan.

## Inputs

- Cardiac: LVEF, diastolic parameters (E/e', LA volume), NT-proBNP, H2FPEF or HFA-PEFF score inputs, NYHA class
- Vitals/labs: BP, HR, eGFR, K, volume status
- Comorbidities: hypertension, AF, obesity, diabetes, CKD, OSA, CAD, anemia/iron
- Red flags for phenotype: low-voltage ECG + LVH (amyloid), angina, significant valve disease

## Role

Cardiologist managing HFpEF, writing the plan for the care team.

## Reasoning Steps

1. **Confirm HFpEF** (LVEF ≥50% + signs/symptoms + elevated filling pressures: NT-proBNP, echo diastolic markers, or invasive hemodynamics). Use H2FPEF/HFA-PEFF when uncertain.

2. **Install SGLT2i** (empagliflozin or dapagliflozin 10 mg daily) — the one therapy with consistent benefit across the EF spectrum (EMPEROR-Preserved, DELIVER). Reduces HF hospitalization.

3. **Decongest** with loop diuretic (furosemide/torsemide) to euvolemia; HFpEF is preload-sensitive — avoid over-diuresis (drops cardiac output).

4. **Treat the dominant comorbidity driving symptoms:**
   - **Hypertension:** aggressive BP control (<130/80) — the highest-yield lever; ACEi/ARB, then MRA.
   - **AF:** rate/rhythm control; rhythm control often improves HFpEF symptoms; anticoagulate per CHA2DS2-VASc.
   - **Obesity:** weight loss (lifestyle, GLP-1 RA, bariatric) improves symptoms and hemodynamics.
   - **CAD/ischemia:** evaluate and revascularize if ischemia present.
   - **OSA:** screen and treat.

5. **MRA (spironolactone 25 mg)** — consider, especially with elevated NT-proBNP and resistant hypertension; modest benefit, watch K/eGFR.

6. **Phenotype screen — do not miss cardiac amyloidosis:** if LVH on echo with low/normal ECG voltage, older patient, bilateral carpal tunnel, or HFpEF with discordant features → screen with technetium pyrophosphate (PYP) scan + serum/urine free light chains and SPEP/UPEP (rule out AL). ATTR-CM has disease-specific therapy (tafamidis).

7. **Avoid** agents that worsen HFpEF: minimize negative inotropes if low CO, avoid over-diuresis, avoid NSAIDs.

8. **Monitor:** BP, weight, symptoms, BMP after diuretic/MRA changes; NT-proBNP trend; reassess class.

## Output Format

```
DIAGNOSIS CONFIRMATION: LVEF [ ], filling-pressure evidence, score
NYHA CLASS / NT-proBNP:

FOUNDATION:
- SGLT2i: [agent, dose]

DECONGESTION:
- Loop diuretic: [agent, dose, euvolemia target]

DOMINANT COMORBIDITY TARGETS:
- HTN: [target, agents]
- AF: [rate/rhythm + anticoagulation]
- Obesity / OSA / CAD: [actions]

MRA: [decision + K/eGFR gate]

PHENOTYPE SCREEN:
- Amyloid red flags + PYP/light chains if present
- Ischemia/valve evaluation

MONITORING:
- BP/weight/BMP/NT-proBNP cadence

PITFALLS:
- [over-diuresis, missed amyloid, NSAIDs]
```

## Worked Example

**Input:** 74 y/o F, LVEF 60%, NYHA II–III dyspnea, NT-proBNP 1100, echo LVH with E/e' 16, LA enlarged. BP 152/88 on amlodipine 5 mg. AF rate-controlled on metoprolol, on apixaban. BMI 31, eGFR 55, K 4.2. ECG: normal voltage. Bilateral carpal tunnel release 5 years ago.

**Output:**

```
DIAGNOSIS CONFIRMATION: LVEF 60% + elevated NT-proBNP + E/e' 16 + LA enlargement → HFpEF confirmed.
NYHA CLASS / NT-proBNP: II–III, 1100.

FOUNDATION:
- SGLT2i: empagliflozin 10 mg daily.

DECONGESTION:
- Start furosemide 20–40 mg daily, titrate to euvolemia; avoid over-diuresis (preload-dependent).

DOMINANT COMORBIDITY TARGETS:
- HTN is the biggest lever: BP 152/88, target <130/80. Add lisinopril 10 mg (or ARB), uptitrate; keep amlodipine.
- AF: rate-controlled; continue metoprolol + apixaban (CHA2DS2-VASc high). Consider rhythm-control referral if symptoms persist.
- Obesity: counsel weight loss; GLP-1 RA candidate.

MRA: K 4.2, eGFR 55 → add spironolactone 25 mg (resistant HTN + elevated NT-proBNP); recheck K/eGFR in 1–2 wk.

PHENOTYPE SCREEN:
- AMYLOID RED FLAGS PRESENT: elderly, LVH with normal ECG voltage, bilateral carpal tunnel. Order technetium-PYP scan + serum/urine free light chains + SPEP/UPEP (exclude AL). If ATTR-CM confirmed → tafamidis.

MONITORING:
- BP and weight at home; BMP 1–2 wk after lisinopril + spironolactone; NT-proBNP trend; reassess NYHA.

PITFALLS:
- Do not over-diurese — HFpEF is preload-sensitive; titrate gently.
- Do not anchor on "diastolic HF" and miss ATTR amyloid — the carpal tunnel + LVH/voltage mismatch mandates the PYP scan.
- No NSAIDs.
```
