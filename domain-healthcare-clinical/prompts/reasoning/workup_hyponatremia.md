---
title: "Hyponatremia Diagnostic Workup"
category: domain-healthcare-clinical/reasoning
description: "Workup hyponatremia by tonicity, volume status, and urine indices; treat per acute vs chronic, with named correction limits to prevent osmotic demyelination."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - nephrology
  - electrolytes
  - critical-care
  - diagnostic-workup
updated: "2026-05-08"
---

## Objective

Work up hyponatremia: rule out pseudo- and translocational hyponatremia, classify by volume status and urine osmolality/sodium, identify cause (SIADH, hypovolemia, hypervolemia, hypothyroidism, adrenal insufficiency, polydipsia, beer potomania), treat acutely vs chronically with named correction caps.

## Inputs

- Serum sodium, repeat to confirm
- Symptom severity: asymptomatic, mild (headache, nausea, fatigue), moderate (confusion, lethargy), severe (seizure, coma, cardiopulmonary arrest, herniation)
- Tempo: acute (<48 h) vs chronic (≥48 h or unknown)
- Volume status: hypovolemic (orthostasis, dry mucous membranes, decreased skin turgor, oliguria), euvolemic (no clinical fluid excess or deficit), hypervolemic (edema, ascites, JVD, pulmonary congestion)
- Comorbidities: HF, cirrhosis, CKD, malignancy, recent CNS event, hypothyroidism, adrenal insufficiency, psychiatric (polydipsia), recent surgery, postoperative state
- Medications: thiazides (especially HCTZ in elderly), SSRIs, carbamazepine, oxcarbazepine, vincristine, cyclophosphamide, NSAIDs, MDMA/ecstasy, opioids, antipsychotics, ACE/ARB
- Diet: tea-and-toast, low-protein, beer potomania
- Labs: serum osmolality, urine osmolality, urine sodium, BUN, creatinine, glucose, lipids, total protein, uric acid, TSH, AM cortisol, BNP, urinalysis
- Vitals (orthostatics), exam
- Imaging if indicated: CXR, CT chest (occult lung malignancy in SIADH), brain imaging if symptomatic or trauma

## Reasoning Steps

1. **Confirm true hyponatremia.**
   - Measure **serum osmolality**:
     - **Hypotonic** (Sosm <275 mOsm/kg) → true hyponatremia.
     - **Isotonic** (275–295) → pseudohyponatremia from severe hyperlipidemia or hyperproteinemia (laboratory artifact); use direct ISE.
     - **Hypertonic** (>295) → translocational from hyperglycemia (correct Na: add 1.6–2.4 mEq/L per 100 mg/dL glucose >100), mannitol, IVIG.

2. **Severity check first.**
   - **Severe symptoms (seizure, coma, severe AMS, respiratory distress):** treat as emergency regardless of cause:
     - **3% saline 100–150 mL IV bolus over 10 min, repeat up to 3 times** until symptoms improve or Na rises 4–6 mEq/L.
     - Goal: raise Na 4–6 mEq/L in first 1–6 hours, then stop urgent therapy.
     - Continue work-up while stabilizing.
     - Cap total correction at 8–10 mEq/L in 24 h, ≤18 mEq/L in 48 h to prevent osmotic demyelination (ODS, formerly central pontine myelinolysis).
     - High-risk for ODS: chronic hyponatremia, alcoholism, malnutrition, hypokalemia, liver disease — cap at 6–8 mEq/L in 24 h, even more conservative if all risk factors.

3. **Acute vs chronic.**
   - Acute (<48 h, often perioperative, polydipsia, MDMA, marathon runner) tolerates faster correction; cerebral edema risk dominates.
   - Chronic (≥48 h or unknown) — slow correction critical (ODS risk dominates).

4. **Classify by volume status (true hypotonic).**

   - **Hypovolemic hyponatremia:**
     - **UNa <20 mEq/L:** extrarenal loss (vomiting, diarrhea, third-spacing, burns, sweating).
     - **UNa >20 mEq/L:** renal loss (diuretics — especially thiazides, salt-wasting nephropathy, mineralocorticoid deficiency, cerebral salt wasting).
     - Treatment: **isotonic saline (NS or LR)**. Recheck Na q2–4 h initially (rapid auto-correction once volume restored is common; dDAVP rescue if Na rising too fast).

   - **Euvolemic hyponatremia:**
     - **SIADH:** Uosm >100 (often >300), UNa >20–30, low BUN, low uric acid (<4), normal thyroid and adrenal axes, no diuretics. Causes: malignancy (small cell lung, head/neck), pulmonary disease (pneumonia, TB, abscess), CNS pathology (stroke, hemorrhage, tumor, infection), drugs (SSRIs, carbamazepine, oxcarbazepine, MDMA, vincristine), postoperative pain, nausea.
     - **Hypothyroidism:** TSH; treat with levothyroxine.
     - **Glucocorticoid deficiency:** AM cortisol, ACTH stim; treat with hydrocortisone 100 mg IV (do not delay if adrenal crisis suspected).
     - **Primary polydipsia / beer potomania / tea-and-toast:** Uosm <100 (dilute) — kidney appropriately suppressing ADH; total solute intake low (beer potomania) or water intake exceeds renal capacity.
     - **Reset osmostat:** chronic mild hyponatremia, otherwise normal labs and no symptoms; no treatment needed.
     - Treatment of SIADH: fluid restriction <800–1000 mL/day; salt and protein in diet; furosemide + salt tablets if refractory; tolvaptan or conivaptan (vasopressin antagonists) for severe; treat underlying cause.

   - **Hypervolemic hyponatremia:**
     - HF, cirrhosis, nephrotic syndrome, advanced CKD.
     - UNa <20 (avid sodium retention) except CKD where UNa variable.
     - Treatment: **fluid AND sodium restriction**, treat underlying disease, loop diuretic to remove free water (relatively more), tolvaptan in selected patients.

5. **Calculate correction rates and use formulas appropriately.**
   - **Adrogue-Madias formula:** change in serum Na from 1 L of infusate = (infusate Na − serum Na) / (TBW + 1).
     - 3% saline = 513 mEq/L Na.
     - NS = 154 mEq/L.
     - TBW: 0.6 × kg (men), 0.5 × kg (women, elderly).
   - Estimates only; recheck Na q2–4 h.
   - **Free water deficit / excess** is conceptually useful but real-time labs trump formulas.

6. **Avoid overcorrection rescue.**
   - If Na rises >8–10 mEq/L in 24 h:
     - **Re-lower with D5W** 10 mL/kg over 1 h.
     - **Desmopressin (dDAVP) 2–4 mcg IV/SC q6–8 h** to halt water losses (hypovolemic and adrenal-replenished patients often have brisk water diuresis once volume restored).
   - Proactive dDAVP-clamp strategy: in high-risk patients (severe chronic hyponatremia, alcoholism, malnutrition), give dDAVP 2 mcg IV q6h and titrate hypertonic saline to controlled Na rise — prevents over-correction.

7. **Special cases.**
   - **Cerebral salt wasting (CSW):** post-SAH, post-neurosurgery; hypovolemia + high UNa, distinguished from SIADH by volume status. Treat with sodium and volume; avoid fluid restriction.
   - **MDMA / marathon runner:** acute polydipsia + ADH stimulation → severe acute hyponatremia. Treat with 3% saline if symptomatic.
   - **Postoperative hyponatremia:** common from hypotonic IVF + nausea-driven ADH; use isotonic IVF in postop period.
   - **Hyperglycemia:** correct sodium for glucose, treat hyperglycemia, sodium normalizes.

## Output Format

```
CONFIRMATION:
- Repeat Na, serum osmolality
- Pseudo / translocational excluded

ACUITY:
- Symptoms (mild / moderate / severe)
- Acute vs chronic

VOLUME STATUS:
- Hypovolemic / euvolemic / hypervolemic

URINE INDICES:
- Uosm, UNa interpretation

CAUSE (ranked):
1. [most likely]
2. [second]
3. [third]

ETIOLOGIC LABS:
- TSH, AM cortisol, BNP, drug review

CORRECTION PLAN:
- If severe symptoms: 3% saline bolus protocol with target rise 4–6 mEq/L
- 24-h cap: [value, with risk factors considered]
- 48-h cap
- Recheck cadence
- DDAVP / D5W rescue plan if overcorrecting

DEFINITIVE TREATMENT:
- Volume / fluid restriction / vaptan / underlying disease
- Free water and sodium plan

DISPOSITION:
- ICU vs floor
- Q-frequency monitoring of Na
```

## Worked Example

**Input:** 76 y/o F, on HCTZ 25 mg daily for HTN, presents with 3 days of nausea, lethargy, and one episode of confusion at home. No seizure. T 36.6, BP 102/62, HR 96, dry mucous membranes. Exam: thin, no edema, mild orthostatic drop. Labs: Na 116, K 3.4, Cl 82, HCO3 26, BUN 18, Cr 0.9, glucose 96, serum osmolality 244 mOsm/kg, urine osmolality 412, urine Na 18, TSH 1.8, AM cortisol 14. Hgb 13. CK 78.

**Output:**

```
CONFIRMATION:
- Sosm 244 (hypotonic) → true hypotonic hyponatremia.
- Glucose 96 normal — no translocational. Lipids/protein normal — no pseudo.

ACUITY:
- Moderate symptoms (lethargy, transient confusion, nausea). Likely chronic given gradual onset and thiazide use.

VOLUME STATUS:
- Hypovolemic — orthostasis, dry mucous membranes, mildly elevated BUN/Cr ratio, no edema.

URINE INDICES:
- UNa 18 (low) — appropriate sodium retention by kidney.
- Uosm 412 — concentrated urine, ADH active.

CAUSE (ranked):
1. Thiazide-induced hyponatremia with volume contraction — classic presentation in elderly woman; HCTZ is the dominant contributor. Mechanism: distal diluting impairment + ADH stimulation by volume contraction.
2. Underlying poor PO intake / dietary contribution.
3. Less likely: SIADH (UNa low, hypovolemia present) — but reassess if Na fails to correct after volume.
4. Adrenal insufficiency — cortisol 14 borderline, normally adequate but ACTH stim test if not improving.
5. Hypothyroidism — TSH 1.8 normal.

ETIOLOGIC LABS:
- AM cortisol 14, TSH normal.
- Consider ACTH stim test if response inadequate.
- Check uric acid (low in SIADH).

CORRECTION PLAN:
- Symptoms moderate, not severe — no emergency 3% saline bolus required, but proceed with care.
- High-risk for ODS: elderly, chronic hyponatremia, K low (3.4), nutritional risk.
- TARGET: raise Na by **4–6 mEq/L in 24 h, NOT to exceed 8 mEq/L**, given ODS risk factors.
- Hold HCTZ. Do not restart.
- IV isotonic NS at modest rate (e.g., 50–100 mL/h) to restore volume; total likely 1–2 L over 12–24 h.
- Replace K to >4 (will help correct Na too).
- Recheck Na q2 h initially. Anticipate brisk water diuresis once volume restored — over-correction risk. Have **dDAVP 2 mcg IV q6h ready** and 5% dextrose for rescue if Na rising too fast.
- If Na rises above target rate: stop NS, give D5W 10 mL/kg over 1 h, give dDAVP 2 mcg IV.
- Continue restriction of free water intake during correction (do not give D5W or hypotonic IVF unless rescuing overcorrection).

DEFINITIVE TREATMENT:
- Discontinue HCTZ permanently; substitute alternative antihypertensive (amlodipine, ACE/ARB if K and Cr allow).
- Patient education on thiazide risk and avoidance of recurrence.
- Repeat sodium check in 1 week post-discharge.

DISPOSITION:
- Admit to telemetry/floor with close Na monitoring (q2–4 h) over first 24 h, then q6–12 h.
- ICU not required currently but escalate if seizure, severe AMS, or hemodynamic instability.
- Discharge once Na ≥125 and stable, symptoms resolved, alternative BP regimen tolerated.
```
