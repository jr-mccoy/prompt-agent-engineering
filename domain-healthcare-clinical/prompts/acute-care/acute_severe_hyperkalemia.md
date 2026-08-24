---
title: "Severe Hyperkalemia Management"
category: domain-healthcare-clinical/acute-care
description: "Manage severe hyperkalemia with cardiac membrane stabilization, intracellular shift, and removal, with named drugs, doses, and dialysis criteria."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: intermediate
tags:
  - electrolytes
  - hyperkalemia
  - critical-care
  - dialysis
updated: "2026-05-08"
---

## Objective

Treat severe or symptomatic hyperkalemia with the three-step paradigm: stabilize cardiac membrane, shift K intracellularly, remove K from body. Output is a sequenced order set with named doses, ECG triggers, and dialysis criteria.

## Inputs

- Serum K value (and whether sample was hemolyzed)
- ECG findings (peaked T waves, PR prolongation, QRS widening, sine wave, bradycardia, arrhythmia)
- Symptoms (weakness, palpitations, none)
- Renal function (eGFR, baseline Cr)
- Cause: AKI/CKD, ACE/ARB/spironolactone/trimethoprim, RTA type 4, tissue breakdown (rhabdo, tumor lysis, hemolysis), acidosis, missed dialysis, K-rich diet (banana, salt substitute) plus impaired excretion
- Medications, baseline cardiac history, dialysis status

## Reasoning Steps

1. **Verify the K value.**
   - Hemolysis on draw causes pseudohyperkalemia (lab will note); redraw with care if patient is asymptomatic and ECG is normal.
   - Pseudohyperkalemia also from severe leukocytosis or thrombocytosis at lab handling.
   - Do not delay treatment if symptoms or ECG changes are present.

2. **Risk stratify by ECG and K.**
   - **Severe (K ≥6.5 or any ECG change):** treat immediately, three-step paradigm.
   - **Moderate (K 6.0–6.4 without ECG change):** reduce K and address cause; less urgent but treat now.
   - **Mild (K 5.5–5.9):** address cause; consider dietary restriction, hold offending drugs, recheck.
   - ECG progression: peaked T → PR prolongation, P-wave flattening → QRS widening → sine wave → asystole/VF.

3. **Step 1 — Cardiac membrane stabilization (within minutes).**
   - **Indication:** any ECG change attributable to hyperK, or K ≥6.5 in dialysis patient.
   - **Calcium gluconate 1 g IV (10 mL of 10% solution) over 2–3 min,** repeat in 5 min if ECG unchanged. Calcium chloride 1 g equivalent (more elemental Ca) if central line — caution with peripheral line (vesicant).
   - Onset 1–3 min, duration 30–60 min — bridges to definitive K-lowering.
   - **Caution in digoxin toxicity:** historically taught to avoid; current evidence suggests slow IV calcium is acceptable — risk of "stone heart" appears overstated. If digoxin toxicity suspected, give digoxin-specific antibody (DigiFab) too.

4. **Step 2 — Shift K intracellularly (within 15–30 min).**
   - **Insulin + glucose:** regular insulin 10 units IV + dextrose 25 g IV (50 mL D50). Onset 15 min, duration 4–6 h. Lowers K by ~0.6–1.0 mEq/L. Watch for hypoglycemia at 1–4 h, especially in renal failure (delayed insulin clearance) — give 10 units IV with 50 g D50 (D50W 100 mL) in moderate-to-severe AKI/ESRD if glucose <250.
   - **Albuterol nebulized 10–20 mg** (4–8 standard nebs back to back). Beta-2 agonist drives K into cells via Na/K-ATPase. Onset 30 min, lowers K by 0.5–1.0 mEq/L. Effects additive with insulin. Caution: tachycardia, tremor.
   - **Sodium bicarbonate IV:** only useful if metabolic acidosis is contributing. Slow onset, modest K-lowering. 50–100 mEq IV over 10–20 min in patients with significant metabolic acidosis. Not first-line in chronic dialysis hyperK without acidosis.

5. **Step 3 — Remove K from body (over hours).**
   - **Loop diuretic (furosemide 40–80 mg IV)** if patient is making urine and not severely volume-depleted. Promotes kaliuresis.
   - **Patiromer (8.4 g PO) or sodium zirconium cyclosilicate (SZC, 10 g PO)** for non-dialysis patients with chronic hyperK. Onset hours; useful for ongoing management not acute removal.
   - **Sodium polystyrene sulfonate (Kayexalate, 30 g PO/PR with sorbitol)** — older agent; concerns about colonic necrosis (especially with sorbitol or in postoperative ileus). Mostly replaced by patiromer/SZC.
   - **Hemodialysis** is the definitive therapy for severe hyperK in renal failure. Onset minutes once initiated.

6. **Hemodialysis indications.**
   - Refractory hyperK despite medical therapy.
   - Anuric/oliguric AKI with K ≥6.5.
   - ESRD with K ≥6.5 or ECG changes.
   - Hyperkalemia from cellular release in ongoing process (tumor lysis, rhabdo) where medical therapy cannot keep up.
   - Prepare access (consider central line if no functional dialysis access), notify nephrology, do not wait if K rising despite optimal medical management.

7. **Address the cause.**
   - Hold ACE/ARB, spironolactone, eplerenone, K-sparing diuretics, trimethoprim, NSAIDs, beta-blockers (modestly contributory).
   - Treat acidosis (bicarbonate, ventilation if respiratory acidosis component).
   - Tumor lysis: rasburicase, fluids, dialysis.
   - Rhabdomyolysis: aggressive IV fluids (NS at 200–300 mL/h targeting UOP 200–300 mL/h), watch for compartment syndrome.
   - Adrenal insufficiency (hyporeninemic-hypoaldo / type 4 RTA in DM): fludrocortisone if applicable.
   - Missed dialysis: dialyze.
   - Dietary review: K-rich foods, salt substitutes (KCl), supplements.

8. **Monitoring.**
   - Continuous telemetry until K <5.5 and stable.
   - Repeat K at 1, 2, 4, 6 h after treatment.
   - Glucose q1h × 4 after insulin (rebound hypoglycemia).
   - Anticipate K rebound after insulin/albuterol effects wear off if no removal step taken.

## Output Format

```
SEVERITY: [K value, ECG findings, symptoms]
DIALYSIS PATIENT? [yes/no]
SUSPECTED CAUSE: [list]

STEP 1 — STABILIZE:
- [Calcium dose if indicated]

STEP 2 — SHIFT:
- Insulin 10 U IV + dextrose
- Albuterol [dose]
- Bicarbonate [if acidosis]

STEP 3 — REMOVE:
- [Furosemide / patiromer / SZC / dialysis]

DIALYSIS:
- [Indicated yes/no, why]

ADDRESS CAUSE:
- [Hold offending drugs, treat acidosis, treat trigger]

MONITORING:
- Continuous telemetry
- K at 1, 2, 4, 6 h
- Glucose q1h × 4 after insulin

PITFALLS:
- [hypoglycemia, rebound, mistaking pseudohyperK, etc.]
```

## Worked Example

**Input:** 68 y/o M with ESRD on HD M/W/F, missed dialysis on Friday, presents Sunday morning with weakness. K 7.4, ECG: peaked T waves and widened QRS to 140 ms, HR 52 sinus brady. BP 158/92. Last dialysis 5 days ago.

**Output:**

```
SEVERITY: K 7.4 with ECG changes (peaked T, wide QRS) and symptoms (weakness). Severe.
DIALYSIS PATIENT: Yes (ESRD, missed two HD sessions).
SUSPECTED CAUSE: Missed dialysis, dietary intake over the interdialytic period; possible diet/medication contributors should be reviewed.

STEP 1 — STABILIZE (NOW):
- Calcium gluconate 1 g IV (10 mL of 10%) over 2–3 min. Repeat ECG in 3–5 min; if QRS still widened, repeat calcium gluconate 1 g.
- Effect lasts 30–60 min — must follow with shift and removal steps.

STEP 2 — SHIFT (within 15 min):
- Regular insulin 10 units IV + D50 25 g IV (50 mL).
  - In ESRD, insulin clearance is delayed and hypoglycemia risk extends 2–6 hours; consider continuous D5 or D10 infusion after the bolus, glucose checks q1h.
- Albuterol 10–20 mg nebulized (4–8 standard nebs back-to-back) over 15–30 min.
- Sodium bicarbonate is unlikely to help here unless ABG shows significant acidosis — check VBG; if HCO3 <18, give 50–100 mEq IV over 15 min.

STEP 3 — REMOVE:
- Hemodialysis is definitive. Notify nephrology immediately; arrange emergent HD.
- Furosemide is not useful in anuric ESRD.
- Patiromer / SZC could be added for ongoing reduction but does not substitute for HD in this case.

DIALYSIS: Yes — emergent HD now. Use the patient's existing access (AVF or AVG); if access unusable, place temporary dialysis catheter.

ADDRESS CAUSE:
- Review medications: any new K-sparing agent, ACE/ARB started?
- Review diet: K-rich foods (banana, orange juice, salt substitute, potatoes, tomatoes), missed binders.
- Reinforce dialysis adherence; arrange for next session.
- Check for occult bleeding (GI), hemolysis (LDH, smear) — released intracellular K from any source contributes.

MONITORING:
- Continuous telemetry until K <5.5 and ECG normal.
- Recheck K immediately post-HD and at 2 h, 6 h.
- Glucose q1h × 6 after insulin given prolonged insulin t½ in ESRD.
- BP monitoring during HD (intradialytic hypotension common).

PITFALLS TO AVOID:
- Stopping after Step 2 — insulin and albuterol shift K into cells; without HD, the K rebounds within 4–6 hours.
- Forgetting prolonged hypoglycemia risk after insulin in ESRD.
- Delaying calcium because of digoxin concern when patient is not on digoxin.
- Failing to identify the underlying cause (missed dialysis is obvious here, but multiple causes can compound — review all).
- Repeating K too early (immediately post-bolus K may show pseudo-improvement before equilibration); recheck at appropriate intervals.
```
