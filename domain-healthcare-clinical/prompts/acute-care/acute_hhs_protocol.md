---
title: "Hyperosmolar Hyperglycemic State Protocol"
category: domain-healthcare-clinical/acute-care
description: "Manage hyperosmolar hyperglycemic state (HHS) with fluid resuscitation, gradual osmolar correction, insulin, potassium, and trigger workup."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: intermediate
tags:
  - endocrine
  - hhs
  - hyperglycemia
  - critical-care
updated: "2026-05-08"
---

## Objective

Manage HHS with fluid resuscitation as the primary intervention, cautious insulin use, potassium replacement, gradual osmolar correction to avoid cerebral edema, and identification of the precipitating cause. Output is a sequenced order set.

## Inputs

- Diagnostic criteria: glucose typically >600, serum osmolality >320, minimal/absent ketones, pH >7.30, HCO3 >18, altered mental status common
- Patient: age, weight, baseline T2DM status (often new diagnosis), home medications, mental status, hemodynamics, comorbidities
- Trigger workup: infection (most common — UA, CXR, blood cultures), MI, stroke, medication noncompliance, new SGLT2 inhibitor (less classic), steroids, antipsychotics

## Reasoning Steps

1. **Confirm HHS vs DKA.**
   - HHS: marked hyperglycemia (often >600), hyperosmolarity (>320), minimal ketones (residual insulin sufficient to suppress ketogenesis), no significant acidosis. Mental status more impaired than DKA — osmotic effect on brain.
   - Mixed pictures occur (~30%) — both DKA and HHS features. Treat the more severe component.

2. **Assess severity and disposition.** Most HHS patients warrant ICU or step-down due to volume status, mental status, and slow correction. Mortality 5–10% (higher than DKA, ~1%), driven by underlying triggers and patient frailty.

3. **Volume resuscitation — the primary intervention.**
   - HHS patients are profoundly volume-depleted (often 8–12 L deficit). Volume restoration alone improves glucose and mental status before insulin is started.
   - Initial: NS 1 L over 1 h (or 15–20 mL/kg).
   - Subsequent: NS 250–500 mL/h, transitioning to 0.45% NS once corrected Na is normal or high.
   - Add D5 to fluid when glucose reaches ~250–300 to allow continued insulin infusion without hypoglycemia.

4. **Calculate corrected sodium.** Add 2.4 mEq Na per 100 mg/dL glucose >100. The corrected Na guides which fluid (NS vs 0.45% NS) and the rate of osmolar correction.

5. **Calculate osmolality and target slow correction.**
   - Effective osm = 2 × Na + glucose/18.
   - Goal: osmolality drop <3 mOsm/kg/h to avoid cerebral edema (bigger concern in pediatric HHS but adults can develop it too).
   - Glucose drop goal 50–75 mg/dL/h.

6. **Insulin — start AFTER initial volume restoration.**
   - Hold insulin until first 1–2 L NS infused (volume-restored patient drops glucose with hydration alone; premature insulin worsens shock and cerebral edema risk).
   - Hold insulin if K <3.3 (replace K first).
   - Regular insulin 0.05 units/kg/h IV infusion (lower than DKA 0.1 unit/kg/h — HHS patients are insulin-sensitive due to residual insulin). No bolus.
   - Reduce to 0.025 units/kg/h when glucose 250–300 and add dextrose to fluids.

7. **Potassium.**
   - K >5.2: hold replacement; recheck in 2 h.
   - K 3.3–5.2: 20–40 mEq/L in IV fluid.
   - K <3.3: hold insulin; replace K aggressively (10–20 mEq/h) until >3.3.

8. **Magnesium and phosphate.** Often depleted. Replace empirically: 2 g IV magnesium sulfate; phos replacement only if <1 with symptoms.

9. **Trigger workup parallel to resuscitation.**
   - Infection (most common): UA, CXR, blood cultures, lactate. Pneumonia and UTI lead the list.
   - MI: ECG, troponin (especially elderly, often silent in DM).
   - Stroke: CT head if focal deficit or atypical mental status pattern.
   - Medication review: new steroids, antipsychotics (especially SGAs), recent diuretic intensification, SGLT2 inhibitor.
   - Pancreatitis: lipase if abdominal pain.

10. **Resolution criteria.**
    - Mental status improved to baseline.
    - Osmolality <320.
    - Glucose <250 and trending stable.
    - Hemodynamics normal.

11. **Transition to subcutaneous insulin.**
    - Once eating and stable, calculate TDD as in DKA: ~0.5 units/kg/day.
    - Patients with new T2DM may not need long-term insulin (can transition to oral agents after acute phase) — check A1c.
    - Overlap drip with first long-acting dose by 1–2 hours.

12. **Watch for complications.**
    - Cerebral edema (rare in adults but reported, especially with rapid osmolar correction): worsening mental status during treatment is the warning sign. Treatment: mannitol or 3% saline; reduce correction rate.
    - Thromboembolism: HHS is hypercoagulable from hyperviscosity; prophylactic anticoagulation indicated unless contraindicated.
    - Rhabdomyolysis: occurs in HHS; check CK, urine myoglobin if oliguric.

## Output Format

```
SEVERITY: [glucose, osm, mental status, hemodynamics]
DISPOSITION: ICU vs step-down

INITIAL ORDERS:
- IV access, labs (BMP, ABG/VBG, beta-hydroxybutyrate, lactate, CBC, lipase, troponin, infection workup)
- NS 1 L over 1 h
- ECG, CXR, UA, blood cultures
- Telemetry, q1h fingerstick, mental status check
- Foley if altered or oliguric
- Hold insulin until first 1–2 L given

VOLUME RESUSCITATION:
- NS 1 L bolus, then 250–500 mL/h
- Switch to 0.45% NS when corrected Na normal/high
- Add D5 when glucose 250–300
- Total deficit 8–12 L over 24–48 h

INSULIN:
- Start 0.05 units/kg/h after volume given and K >3.3
- Reduce to 0.025 units/kg/h when glucose 250–300
- Continue until osm <320 and patient mentating

POTASSIUM:
- [strategy based on initial K]

TRIGGER WORKUP:
- [infection, MI, stroke, meds, pancreatitis]

VTE PROPHYLAXIS:
- LMWH or UFH SC unless contraindicated

MONITORING:
- Glucose q1h
- Osmolality, BMP, AG q2–4h initially
- Mental status q1h
- Strict I/O

TRANSITION:
- Resume home regimen or new TDD when stable and eating
- Overlap drip with long-acting

PITFALLS:
- [premature insulin, fast osmolar correction, missing trigger]
```

## Worked Example

**Input:** 78 y/o M, found at home altered, sent in by family. T2DM on metformin only, recently stopped meds for unclear reason. Vitals: HR 116, BP 96/58, RR 22, T 38.4, mental status: GCS 12, mumbling, dry mucous membranes, poor skin turgor. Weight 75 kg. Labs: glucose 1080, Na 138 (corrected ~163), K 4.8, Cl 96, HCO3 22, BUN 78, Cr 2.4 (no baseline known), pH 7.32, beta-hydroxybutyrate 0.8 (low), lactate 2.0, osm 348. UA: 4+ glucose, no ketones, +LE, +nitrite. CXR: RLL infiltrate.

**Output:**

```
SEVERITY: Severe HHS (glucose 1080, osm 348, altered mentation, hypotension, AKI). Likely precipitated by pneumonia (RLL infiltrate, +LE/nitrite UA so concurrent UTI possible too) and medication noncompliance.
DISPOSITION: ICU.

INITIAL ORDERS:
- 2 large-bore PIVs.
- Already drawn: BMP, VBG, beta-hydroxybutyrate, lactate, CBC, glucose, osm. Add: troponin, lipase, blood cultures ×2, urine culture, sputum if productive.
- NS 1 L over 1 h NOW (not over slower; profoundly volume-depleted, hypotensive).
- ECG to rule out concurrent MI (silent in elderly with DM).
- CXR confirms RLL infiltrate — start empiric antibiotics for community-acquired pneumonia (ceftriaxone 1 g IV + azithromycin 500 mg IV) immediately. Add coverage for UTI (ceftriaxone covers most uropathogens).
- Foley placed (altered mentation, strict I/O needed).
- Telemetry continuous; q1h fingerstick; q1h mental status check.
- HOLD insulin until first 2 L NS given.

VOLUME RESUSCITATION:
- NS 1 L over 1 h (running now), then second 1 L over next 1–2 h.
- Reassess after 2 L: if corrected Na is normal/high (it is — corrected Na ~163), switch to 0.45% NS at 250–500 mL/h.
- Continue volume until hemodynamics stable, urine output >0.5 mL/kg/h, and Cr trending down.
- Total expected deficit: 8–12 L over first 24–48 h. Replace half over first 12 h.
- Add D5 to fluid (D5 + 0.45% NS) when glucose reaches 250–300.

INSULIN:
- Hold for first 2 hours while volume restoring. Glucose will fall with fluids alone (perhaps 200–300 mg/dL drop in first 2 h from hemodilution and improved renal perfusion).
- After 2 L NS and K confirmed >3.3 (currently 4.8 — fine):
- Start regular insulin IV at 0.05 units/kg/h = 4 units/h. No bolus.
- Goal glucose drop 50–75 mg/dL/h. Faster drop → reduce insulin rate or add D5 earlier.
- When glucose 250–300: reduce insulin to 0.025 units/kg/h = 2 units/h, ensure D5 in fluids.
- Continue infusion until osm <320 and patient mentating.

POTASSIUM:
- K 4.8 currently — no replacement needed at this moment.
- Anticipate K falling rapidly with insulin and volume. Recheck with each BMP.
- When K <5.2: add 20–40 mEq KCl per liter of IV fluid.

TRIGGER WORKUP:
- Pneumonia: identified on CXR; antibiotics started.
- UTI: UA suggests concurrent — covered by ceftriaxone; await urine culture for narrowing.
- MI: ECG done; troponin sent. Recheck at 3 h (high-sensitivity troponin protocol if available).
- Stroke: head CT if focal neurologic deficit emerges or mental status does not improve with metabolic correction.
- Medication noncompliance: identified by history; counsel after acute resolution.
- Pancreatitis: lipase pending.

VTE PROPHYLAXIS:
- LMWH (enoxaparin 40 mg SC daily) or UFH 5000 units SC q8h once volume-restored. HHS is prothrombotic (hyperviscosity, immobility, infection). Recheck Cr — if eGFR <30, use UFH SC for prophylaxis.

MONITORING:
- Fingerstick q1h.
- BMP, glucose, osm q2h until trending; q4h once stable.
- Mental status q1h; document GCS.
- Strict I/O via Foley.
- Continuous telemetry, BP cuff q15 min until stable.
- Lactate trend if elevated.
- Daily CK and urine myoglobin if oliguric (rhabdo risk in HHS).

TRANSITION TO SUBCUTANEOUS:
- Anticipate 24–48 h to full resolution.
- Once eating and stable, calculate TDD ~0.5 units/kg/day = 37.5 units; start basal-bolus:
  - Glargine 18 units SC q evening.
  - Lispro 6 units SC with each meal.
- Overlap drip with first long-acting by 1–2 h.
- This patient may need long-term insulin given severity, age, and renal function — but reassess A1c and outpatient regimen with diabetes educator and primary care; could potentially transition to GLP-1 RA, sulfonylurea, or DPP-4 once acute phase resolved (avoid metformin if Cr stays elevated).

PITFALLS TO AVOID:
- Starting insulin before volume resuscitation: drops BP further, drives K into cells of a depleted patient, raises cerebral edema risk.
- Correcting osmolality too fast: aim <3 mOsm/kg/h. Watch for worsening mental status during treatment as cerebral edema warning sign.
- Missing the trigger: pneumonia and UTI here are obvious; less obvious triggers (silent MI, mesenteric ischemia, intra-abdominal abscess) need active search if HHS does not resolve as expected.
- Forgetting VTE prophylaxis.
- Failing to address discharge planning: home meds, home glucose monitoring, follow-up, social factors driving non-adherence.
```
