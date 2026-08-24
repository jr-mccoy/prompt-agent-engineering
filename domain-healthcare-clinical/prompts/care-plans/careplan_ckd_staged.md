---
title: "Chronic Kidney Disease Staged Care Plan"
category: domain-healthcare-clinical/care-plans
description: "Build a CKD management plan by KDIGO stage: slow progression with RAAS/SGLT2i/finerenone, manage complications, and time nephrology and transplant referral with named drugs and targets."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
  - DS-02
difficulty: advanced
tags:
  - nephrology
  - ckd
  - care-plan
  - chronic-disease
updated: "2026-06-19"
---

## Objective

Produce a CKD care plan staged by KDIGO (eGFR G + albuminuria A): slow progression (BP, RAAS, SGLT2i, finerenone), manage metabolic complications (anemia, mineral-bone, acidosis, hyperkalemia), adjust drugs for renal function, and time nephrology/transplant/dialysis-access referral. Output is a stage-specific plan.

## Inputs

- Renal: eGFR (and trend), UACR, cause of CKD (diabetic, hypertensive, glomerular, polycystic), urinalysis/sediment
- Labs: K, bicarbonate, hemoglobin, iron studies, calcium, phosphate, PTH, 25-OH vitamin D, albumin
- Comorbidities: diabetes, hypertension, HF, CVD, gout
- Current meds (nephrotoxins, RAAS, dose-adjustment needs), BP, volume status

## Role

Nephrologist or internist managing CKD longitudinally.

## Reasoning Steps

1. **Stage by KDIGO** (G1–G5 by eGFR; A1–A3 by UACR) and identify cause. Quantify progression risk (lower eGFR + higher albuminuria = higher risk).

2. **Slow progression (the core levers):**
   - **BP <120–130 systolic** (target individualized); ACEi or ARB first-line if albuminuria (UACR ≥300, or ≥30 with diabetes) — titrate to max tolerated; tolerate ≤30% creatinine rise.
   - **SGLT2i** (dapagliflozin/empagliflozin) for CKD with eGFR ≥20 and albuminuria (and most diabetic CKD) — slows progression, CV benefit (DAPA-CKD, EMPA-KIDNEY).
   - **Finerenone** (nonsteroidal MRA) for diabetic CKD with persistent albuminuria on max ACEi/ARB + SGLT2i, K <5.0 (FIDELIO/FIGARO).
   - **Glycemic control** (A1c individualized ~7%), **GLP-1 RA** for diabetic CKD.

3. **Manage complications by stage:**
   - **Metabolic acidosis** (HCO3 <22): sodium bicarbonate to keep HCO3 ≥22 — slows progression.
   - **Anemia:** evaluate when Hgb low; iron repletion (ferritin/TSAT targets), ESA if Hgb <10 after iron (target 10–11, not normal); newer HIF-PH inhibitors where available.
   - **CKD-MBD:** monitor Ca/Phos/PTH/vitamin D; phosphate binders and dietary phosphate restriction as phosphate rises; treat secondary hyperparathyroidism.
   - **Hyperkalemia:** dietary K, loop diuretic, optimize bicarbonate; K binders (patiromer, sodium zirconium) to preserve RAAS/SGLT2i therapy rather than stopping them.
   - **Volume:** loop diuretics for overload.

4. **Drug safety:** dose-adjust or avoid renally-cleared/nephrotoxic agents (metformin per eGFR, gabapentin, certain antibiotics, contrast caution, NSAIDs off).

5. **Referral timing:**
   - **Nephrology:** eGFR <30, rapidly declining eGFR, A3 albuminuria, refractory complications, uncertain etiology.
   - **Transplant/access:** discuss kidney transplant evaluation and dialysis-access (AV fistula) planning as eGFR approaches 15–20; preemptive transplant referral when eGFR <20.

6. **Cardiovascular risk:** statin (most CKD patients are high-risk), BP, smoking, aspirin per indication.

7. **Monitor:** eGFR/UACR/K/HCO3 cadence by stage; CBC, Ca/Phos/PTH; vaccinate (influenza, pneumococcal, hepatitis B — important pre-dialysis).

## Output Format

```
STAGE (G + A) / CAUSE / TREND:
PROGRESSION RISK:

SLOW-PROGRESSION PLAN:
- BP target + RAAS agent/dose
- SGLT2i: [agent, dose, eGFR gate]
- Finerenone: [if criteria + K gate]
- Glycemic / GLP-1

COMPLICATION MANAGEMENT:
- Acidosis (bicarbonate)
- Anemia (iron/ESA targets)
- CKD-MBD (Ca/Phos/PTH/binders)
- Hyperkalemia (binders to preserve RAAS/SGLT2i)
- Volume

DRUG SAFETY:
- [dose-adjust / avoid list]

REFERRAL:
- Nephrology / transplant / access timing

CV RISK:
- Statin, BP, smoking

MONITORING:
- Lab cadence by stage; vaccines

PITFALLS:
- [stopping RAAS/SGLT2i for tolerable changes, missing acidosis, over-correcting anemia, contrast/NSAID/metformin]
```

## Worked Example

**Input:** 60 y/o M, diabetic CKD. eGFR 38 (stable decline), UACR 620 mg/g, K 4.6, HCO3 20, Hgb 10.8, ferritin 90, TSAT 16%, Ca/Phos normal, PTH mildly elevated. BP 142/86 on lisinopril 20 mg. A1c 7.8% on metformin + empagliflozin not yet started.

**Output:**

```
STAGE: G3b (eGFR 38), A3 (UACR 620), diabetic CKD. High progression risk (low eGFR + heavy albuminuria).

SLOW-PROGRESSION PLAN:
- BP 142/86, target <130/80 (or lower): uptitrate lisinopril to 40 mg (max RAAS for albuminuria).
- SGLT2i: start empagliflozin 10 mg (eGFR 38 ≥20, albuminuric, diabetic) — key progression-slowing step. Expect early eGFR dip; do not stop.
- Finerenone: diabetic CKD with persistent albuminuria; K 4.6 acceptable. Add after lisinopril maxed + SGLT2i established; recheck K. (Sequence/space additions; watch K with three RAAS-axis effects.)
- Glycemic: A1c 7.8 — metformin OK at eGFR 38 (continue, monitor; stop <30). GLP-1 RA candidate for added renal/CV benefit.

COMPLICATION MANAGEMENT:
- Acidosis: HCO3 20 (<22) → sodium bicarbonate 650 mg BID, target HCO3 ≥22.
- Anemia: Hgb 10.8 with TSAT 16%, ferritin 90 → iron deficiency; repletion (IV iron preferred in CKD) to TSAT >20%/ferritin >100, recheck Hgb before considering ESA.
- CKD-MBD: monitor PTH/Ca/Phos; check 25-OH vitamin D; dietary phosphate counseling.
- Hyperkalemia: K 4.6 now; if it rises with RAAS/finerenone, use patiromer to KEEP the therapy rather than stop it.

DRUG SAFETY:
- Metformin continue at eGFR 38, reassess; NSAIDs off; contrast caution.

REFERRAL:
- Nephrology referral (A3, eGFR <45 with heavy albuminuria, diabetic).
- Begin transplant/access education; formal eval when eGFR <20.

CV RISK:
- High-intensity statin; BP; smoking.

MONITORING:
- eGFR/UACR/K/HCO3 q3 months (more often after RAAS/finerenone/SGLT2i changes); CBC, iron, Ca/Phos/PTH; hepatitis B + pneumococcal + influenza vaccines.

PITFALLS:
- Do not withhold SGLT2i for the expected initial eGFR dip.
- Treat acidosis and iron deficiency — both modifiable.
- Preserve RAAS/SGLT2i with K binders rather than discontinuing.
```
