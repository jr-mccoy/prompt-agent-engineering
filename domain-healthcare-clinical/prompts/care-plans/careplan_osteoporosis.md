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

## False-Positive Prevention

❌ **DON'T:**
- Apply the T-score ≤−2.5 cutoff to premenopausal women or men under 50 — that population is read on Z-scores, and a "DXA-diagnosed osteoporosis" label there is a misclassification.
- Accept a lumbar-spine T-score measured across a compressed or degenerated vertebra as the lowest site — fracture and osteophytes falsely raise spine BMD; use the valid vertebrae or the hip.
- Produce or "recalculate" a FRAX probability the input did not give — FRAX is country-specific and takes femoral-neck BMD; write `[FRAX not supplied]`.
- Label the patient "very high risk" without naming the criterion that met it (fracture in the past 12 months, multiple fractures, fracture on therapy, T-score ≤−3.0 …) `[VERIFY: AACE/Endocrine Society definition]` — the anabolic-first choice inherits that label.
- Write "no recent MI/stroke" for romosozumab, or clear teriparatide/abaloparatide, because the history is silent — romosozumab needs the date of any MI/stroke (label: not within the past year), and the PTH-analogue line needs prior skeletal radiation and unexplained alkaline-phosphatase elevation checked.

✅ **DO:**
- Before any antiresorptive line, quote calcium (albumin-corrected when albumin is given — recompute Ca + 0.8 × (4.0 − albumin g/dL)), 25-OH vitamin D, eGFR and dental status with their dates; a "normocalcemia ✓" with no value is not done.
- For bisphosphonate drug-holiday logic, compute years on therapy from the start date and route (oral vs IV) in the input, and state why the patient is or is not still high risk (a fracture on therapy rules the holiday out).
- Whenever denosumab appears — current, planned or as a fallback — write its exit plan in the same line: follow-on agent and timing relative to the last injection `[VERIFY: current guidance]`.
- In eGFR <30, pair any denosumab choice with a hypocalcaemia monitoring plan instead of calling it simply "renal-safe".

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
