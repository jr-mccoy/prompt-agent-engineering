---
title: "Osteoporosis Care Plan"
category: domain-healthcare-clinical/care-plans
description: "Build an osteoporosis management plan: fracture-risk stratification, antiresorptive vs anabolic selection, drug holiday logic, and monitoring with named drugs and doses."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
  - DS-02
difficulty: intermediate
tags:
  - endocrine
  - osteoporosis
  - bone-health
  - care-plan
updated: "2026-06-19"
---

## Objective

Produce an osteoporosis care plan: stratify fracture risk, choose antiresorptive vs anabolic therapy by risk level, sequence agents correctly, define drug-holiday logic, and set monitoring. Output is a risk-matched pharmacologic plan plus the calcium/vitamin D and fall-prevention bundle.

## Inputs

- Diagnosis/risk: DXA T-scores (spine, hip, femoral neck), prior fragility fractures, FRAX 10-year major/hip fracture probability, glucocorticoid use
- Patient: age, sex, menopause status, renal function (eGFR), dental status (ONJ risk), GI tolerance (oral bisphosphonate), prior osteoporosis therapy
- Secondary causes: vitamin D/calcium, thyroid/parathyroid, celiac, hypogonadism, myeloma, medications
- Falls risk, calcium/vitamin D intake

## Role

Endocrinologist or primary care attending managing osteoporosis.

## Reasoning Steps

1. **Diagnose/risk-stratify:** osteoporosis if T-score ≤−2.5, or a fragility fracture (hip/vertebral) regardless of T-score, or high FRAX. Distinguish **high risk** vs **very high risk** (recent fracture, multiple fractures, T-score very low, ongoing glucocorticoids, high FRAX) — drives anabolic-first decision.

2. **Evaluate secondary causes** and correct: 25-OH vitamin D, calcium, renal/hepatic, TSH, PTH, celiac/myeloma workup if indicated. Repletion of vitamin D before starting/with therapy.

3. **Foundation for all:** calcium (diet first; supplement to ~1000–1200 mg/day total) + vitamin D (800–1000+ IU to keep 25-OH adequate), weight-bearing exercise, fall prevention, smoking/alcohol moderation.

4. **Pharmacologic selection:**
   - **High risk:** antiresorptive first-line — oral bisphosphonate (alendronate 70 mg weekly, risedronate) or IV zoledronic acid 5 mg yearly (if GI intolerance/adherence). Denosumab 60 mg SC q6 months as alternative (renal-safe).
   - **Very high risk (recent/multiple fractures, very low T-score):** **anabolic first** — teriparatide or abaloparatide (daily SC, up to 2 years) or romosozumab (monthly × 12, avoid with recent MI/stroke). Anabolic-then-antiresorptive builds more bone than the reverse.

5. **Sequencing rules (critical):**
   - **After anabolic therapy, always follow with an antiresorptive** (bisphosphonate or denosumab) — gains are lost otherwise.
   - **Denosumab cannot be stopped without transition** to a bisphosphonate — discontinuation causes rebound vertebral fractures. Do not delay/skip doses.

6. **Drug holiday (bisphosphonates only):** consider after 3–5 years (oral) or 3 years (IV) in patients no longer high-risk — bisphosphonates persist in bone. No holiday for denosumab/anabolics. Reassess risk during holiday.

7. **Glucocorticoid-induced osteoporosis:** treat earlier/at higher BMD threshold; bisphosphonate or anabolic depending on risk and steroid duration.

8. **Safety:** dental evaluation before IV bisphosphonate/denosumab (ONJ, rare); atypical femoral fracture counseling; oral bisphosphonate administration instructions (upright, empty stomach); avoid bisphosphonates if eGFR <30–35 (use denosumab); ensure normocalcemia before antiresorptive.

9. **Monitor:** DXA every 1–2 years, response/adherence, calcium/vitamin D, renal function, fracture occurrence.

## Output Format

```
DIAGNOSIS / RISK LEVEL (DXA, fractures, FRAX, glucocorticoid):
SECONDARY CAUSES EVALUATED + CORRECTED:

FOUNDATION:
- Calcium / vitamin D targets, exercise, fall prevention

PHARMACOLOGIC PLAN:
- Agent by risk level: [antiresorptive vs anabolic, drug, dose]
- Sequencing rule (anabolic → antiresorptive; denosumab no-stop)
- Drug-holiday logic if applicable

SAFETY:
- Dental/ONJ, renal limits, administration, normocalcemia

MONITORING:
- DXA interval, labs, adherence, fractures

PITFALLS:
- [stopping denosumab without bridge, no antiresorptive after anabolic, bisphosphonate in low eGFR, missing secondary causes]
```

## Worked Example

**Input:** 70 y/o postmenopausal F, recent low-trauma vertebral compression fracture, DXA femoral neck T-score −3.2, FRAX high. 25-OH vitamin D 22 ng/mL, calcium normal, eGFR 70, normal dentition. No prior osteoporosis therapy. Not on glucocorticoids.

**Output:**

```
DIAGNOSIS / RISK LEVEL: VERY HIGH risk — recent vertebral fragility fracture + femoral neck T −3.2 + high FRAX.
SECONDARY CAUSES: vitamin D insufficient (22) — replete to >30 before/with therapy; calcium normal; check TSH/PTH/celiac if any clues; renal OK.

FOUNDATION:
- Calcium to ~1200 mg/day total (diet first), vitamin D 1000–2000 IU to reach adequate 25-OH.
- Weight-bearing exercise, formal fall-prevention assessment.

PHARMACOLOGIC PLAN:
- Very high risk → ANABOLIC FIRST: romosozumab 210 mg SC monthly × 12 (no recent MI/stroke), or teriparatide/abaloparatide daily × up to 2 years.
- After the anabolic course → transition to an antiresorptive (zoledronic acid 5 mg IV yearly or alendronate) to lock in gains. This is mandatory.
- (If anabolic not feasible: zoledronic acid is a strong antiresorptive alternative, but anabolic-first is preferred at very high risk.)

SAFETY:
- Ensure vitamin D repleted and normocalcemia before antiresorptive (avoid hypocalcemia).
- Dental status fine; counsel ONJ/atypical femoral fracture (rare).
- eGFR 70 — bisphosphonate acceptable for the follow-on.

MONITORING:
- DXA in 1–2 years; vitamin D/calcium; adherence; watch for new fractures.

PITFALLS:
- Do NOT give a bisphosphonate first then anabolic — anabolic-first builds more bone.
- After the anabolic, do not leave her untreated — follow with an antiresorptive or gains reverse.
- If denosumab were ever used, never stop it without a bisphosphonate bridge (rebound fractures).
```
