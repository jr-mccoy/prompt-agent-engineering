---
title: "DKA Protocol Reasoning"
category: domain-healthcare-clinical/acute-care
description: "Run a diabetic ketoacidosis protocol with insulin, fluid, potassium, and transition to subcutaneous insulin, with named doses and trigger thresholds."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: intermediate
tags:
  - endocrine
  - dka
  - insulin
  - critical-care
updated: "2026-05-08"
---

## Objective

Manage a patient with diabetic ketoacidosis from initial fluid and insulin orders through anion gap closure and transition to subcutaneous insulin. Output is a sequenced order set with named doses, monitoring intervals, and trigger thresholds for transition.

## Inputs

- Diagnostic confirmation: glucose >250 (or euglycemic if SGLT2 inhibitor), AGMA, ketonemia (beta-hydroxybutyrate elevated)
- Initial labs: BMP, ABG/VBG, beta-hydroxybutyrate, lactate, CBC, lipase if abdominal pain
- Patient: weight, age, T1DM vs T2DM vs new diagnosis, home insulin regimen, oral intake status, mental status, hemodynamics
- Trigger workup: infection (UA, CXR, blood cultures), MI (ECG, troponin), pancreatitis (lipase), pregnancy, missed insulin doses, drug use (cocaine), new SGLT2 inhibitor (euglycemic DKA)

## Role

Senior internist or critical care attending running DKA in the ED or ICU.

## Reasoning Steps

1. **Confirm DKA and assess severity.**
   - Mild: pH 7.25–7.30, HCO3 15–18, mental status normal.
   - Moderate: pH 7.00–7.24, HCO3 10–15.
   - Severe: pH <7.00, HCO3 <10, altered mental status. ICU.

2. **Establish IV access, draw labs, place patient on telemetry.**

3. **Fluid resuscitation.**
   - Initial: NS 1 L bolus over 1 hour (or 15–20 mL/kg). Pediatric: 10 mL/kg.
   - Ongoing: 250–500 mL/h thereafter, titrated to volume status. Switch to 0.45% NS once hemodynamics stabilized and corrected Na is normal or high; remain on NS if corrected Na is low.
   - Add D5 to fluids when glucose reaches 200–250 to allow continued insulin infusion (which keeps suppressing ketogenesis) without iatrogenic hypoglycemia. Common: D5 + 0.45% NS at 150–250 mL/h alongside continued insulin drip.

4. **Potassium replacement BEFORE insulin in many cases.**
   - K >5.2: hold K replacement for now; recheck in 2 h.
   - K 3.3–5.2: add 20–40 mEq KCl per liter of IV fluid (target K 4–5).
   - K <3.3: HOLD insulin, replace K aggressively (10–20 mEq/h IV) until K >3.3, then start insulin. Insulin will drop K rapidly into cells; pre-insulin hypokalemia + insulin = fatal arrhythmia.

5. **Insulin.**
   - **Do not bolus** in adults (recent literature shows no benefit, possible harm with hypoglycemia and rapid osm shifts). In pediatric DKA, bolus is contraindicated (cerebral edema risk).
   - Start regular insulin IV infusion at 0.1 units/kg/h. Some protocols use 0.14 units/kg/h without bolus.
   - Goal: glucose drop 50–75 mg/dL/h. Faster drop risks cerebral edema, especially in pediatrics.
   - When glucose 200–250: reduce insulin to 0.05 units/kg/h AND add dextrose to fluid (not switch insulin off — the goal is anion gap closure, not glucose normalization).

6. **Bicarbonate.**
   - Indicated only if pH <6.9 with hemodynamic instability, severe hyperkalemia, or refractory acidosis impairing inotropy. NaHCO3 100 mEq in 400 mL water with 20 mEq KCl over 2 h, recheck pH.
   - Avoid routine bicarb: paradoxical CSF acidosis, worsening hypokalemia, delayed ketone metabolism.

7. **Phosphate.**
   - Replace only if phos <1 with cardiac dysfunction, respiratory weakness, or anemia. Routine phos replacement does not improve outcomes.

8. **Magnesium.**
   - Common deficiency. Replace 2 g IV magnesium sulfate empirically; recheck.

9. **Monitoring cadence.**
   - Glucose: q1h fingerstick.
   - BMP, VBG, anion gap: q2–4h initially, q4h once trending.
   - Telemetry continuous.
   - Mental status q1h.
   - I/O strict; consider Foley if oliguric or altered.
   - Beta-hydroxybutyrate q4h if available — clears slower than glucose; use to gauge resolution.

10. **Trigger workup running in parallel.**
    - UA, CXR, blood cultures if febrile or any concern for infection.
    - ECG and troponin for any patient >40 or with cardiac risk factors.
    - Lipase if abdominal pain.
    - Pregnancy test in women of reproductive age.
    - Urine drug screen if presentation atypical.
    - Review home meds — was an SGLT2i recently started? (Euglycemic DKA can present with glucose <250.)

11. **Resolution criteria (all three required).**
    - Glucose <200.
    - HCO3 ≥18 (or anion gap closed, AG ≤12).
    - Venous pH ≥7.30.

12. **Transition to subcutaneous insulin.**
    - Patient must be eating or able to tolerate scheduled insulin.
    - Calculate total daily dose (TDD): if known regimen, resume home dose. If new diagnosis, start ~0.5–0.7 units/kg/day (lower in elderly, renal failure, lean patient; higher in obesity).
    - Split: 50% basal (glargine or detemir), 50% prandial (lispro/aspart in three meal divisions).
    - Give first dose of long-acting insulin 1–2 hours BEFORE stopping the IV drip. The drip's tail will overlap with the long-acting onset; failure to overlap → recurrent ketosis.
    - Continue carbohydrate intake; bolus rapid-acting insulin with first meal.

13. **Disposition and counseling.**
    - Diabetes educator if new T1DM or recurrent DKA — sick-day rules, insulin pump troubleshooting if applicable, ketone home monitoring.
    - Address trigger: treat infection completely, MI workup, missed insulin counseling, SGLT2i hold if implicated.

## Output Format

```
SEVERITY: [mild / moderate / severe]
DISPOSITION: [floor / step-down / ICU]

INITIAL ORDERS (first hour):
- IV access, labs (BMP, VBG, beta-hydroxybutyrate, lactate, CBC, [trigger workup])
- NS [volume] over 1 h
- Telemetry, q1h fingerstick, strict I/O
- ECG, CXR if indicated
- HOLD insulin if K <3.3

INSULIN:
- Regular insulin IV at 0.1 units/kg/h = [calculated dose]
- Reduce to 0.05 units/kg/h when glucose 200–250 AND add dextrose

POTASSIUM:
- [strategy based on initial K]

FLUIDS ONGOING:
- [type, rate]
- [transition trigger to add D5]

MONITORING:
- Glucose q1h
- BMP / VBG / AG q[2–4]h
- Telemetry continuous
- Mental status q1h

TRIGGER WORKUP:
- [list relevant tests]

RESOLUTION CRITERIA:
- Glucose <200, AG closed, pH ≥7.30

TRANSITION TO SUBCUTANEOUS:
- TDD: [calculated]
- Basal: [drug, dose, timing]
- Prandial: [drug, dose, timing]
- Overlap drip with long-acting by 1–2 h

PITFALLS TO AVOID:
- [bicarb, K timing, pediatric-specific, cerebral edema, etc.]
```

## Worked Example

**Input:** 22 y/o F with T1DM, missed insulin x 2 days while traveling. Weight 60 kg. Vitals: HR 124, BP 102/68, RR 26, T 37.1, mental status alert but tired. Labs: glucose 580, Na 132 (corrected ~143), K 5.4, Cl 96, HCO3 7, BUN 28, Cr 1.1, beta-hydroxybutyrate 6.8, pH 7.10, lactate 1.4, lipase 80 (normal), UA 4+ ketones 4+ glucose, no nitrites/LE, pregnancy test negative.

**Output:**

```
SEVERITY: Severe DKA (pH 7.10, HCO3 7).
DISPOSITION: ICU or step-down with telemetry and q1h checks.

INITIAL ORDERS (first hour):
- 2 large-bore PIVs.
- Already drawn: BMP, VBG, beta-hydroxybutyrate, lactate, CBC. Add: troponin, lipase (done), urine pregnancy (done), urine tox if any concern.
- NS 1 L bolus over 1 h.
- Telemetry continuous, q1h fingerstick, strict I/O (Foley if mental status declines or output unclear).
- ECG to rule out MI as trigger and assess for hyperK changes (K 5.4 borderline).
- HOLD insulin? — K is 5.4, well above 3.3 threshold; insulin can start. But do not bolus.

INSULIN:
- Regular insulin IV at 0.1 units/kg/h = 6 units/h. No bolus.
- When glucose reaches 200–250, reduce to 0.05 units/kg/h = 3 units/h and add D5 to fluids.
- Continue insulin drip until anion gap closes (AG ≤12) and pH ≥7.30, regardless of glucose.

POTASSIUM:
- K 5.4 → no replacement now. Recheck K with first BMP at 2 hours. Anticipate K dropping fast once insulin starts (insulin drives K into cells; total body K is depleted from osmotic diuresis).
- When K <5.2: add 40 mEq KCl per liter of IV fluid.
- When K <3.3: hold insulin, replace K aggressively.

FLUIDS ONGOING:
- After 1 L NS bolus: NS 250 mL/h × 2 hours (until volume restored).
- Then 0.45% NS 250 mL/h (corrected Na ~143, normal/high → can switch to half-normal).
- When glucose hits 200–250: switch to D5 + 0.45% NS at 150–250 mL/h.
- Total fluid replacement over 24 h often 5–10 L; use clinical assessment, not formula alone.

MONITORING:
- Glucose q1h fingerstick.
- BMP and VBG q2h until AG trending closed; then q4h.
- Beta-hydroxybutyrate q4h (lags glucose; tracks ketone resolution).
- Continuous telemetry; mental status check q1h.
- Strict I/O.

TRIGGER WORKUP:
- Already: lipase normal, UA shows ketones/glucose without infection, pregnancy negative.
- Confirmed trigger: insulin omission (history). No further infection workup needed unless fever or new findings.
- Repeat exam in 2 h to verify no missed source (abdominal exam, mental status).

RESOLUTION CRITERIA:
- Glucose <200, AG ≤12, pH ≥7.30, eating.

TRANSITION TO SUBCUTANEOUS (anticipated 12–24 h):
- TDD: home regimen on chart? If not, start 0.5 units/kg/day = 30 units total.
  - Basal: glargine 15 units SC q evening.
  - Prandial: lispro 5 units SC with each meal (3 meals).
- Give first glargine dose 1–2 hours BEFORE stopping insulin drip. Failure to overlap → recurrent ketosis.
- Diabetes educator before discharge: sick-day rules, ketone monitoring at home, insulin storage during travel.

PITFALLS TO AVOID:
- Do not bolus insulin (no benefit, possible harm with rapid glucose drop).
- Do not give bicarbonate at this pH (7.10 > 6.9 threshold).
- Do not stop insulin drip when glucose normalizes — continue with dextrose-containing fluids until AG closes.
- Do not forget K replacement; K can fall from 5.4 to <3 within 4 hours of starting insulin.
- Do not delay trigger workup; missed infection or pancreatitis prolongs DKA.
- Do not transition to subcutaneous without overlapping with the drip.
```
