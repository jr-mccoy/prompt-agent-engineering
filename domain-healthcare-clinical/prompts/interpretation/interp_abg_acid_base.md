---
title: "ABG and Acid-Base Full Workup"
category: domain-healthcare-clinical/interpretation
description: "Interpret an arterial blood gas with full acid-base workup including primary disorder, compensation, anion gap, delta-delta, and clinical action."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - CR-01
  - QA-01
difficulty: advanced
tags:
  - critical-care
  - abg
  - acid-base
  - electrolytes
  - interpretation
updated: "2026-05-08"
---

## Objective

Interpret an arterial (or venous) blood gas with a complete acid-base workup: identify the primary disorder, evaluate compensation adequacy, calculate the anion gap and delta-delta, identify mixed disorders, and commit to a likely etiology and clinical action.

## Inputs

- ABG values: pH, PaCO2, PaO2, HCO3, base excess, SaO2 (or VBG with note)
- Concurrent BMP: Na, K, Cl, HCO3 (CO2), BUN, Cr, glucose
- Albumin (for corrected anion gap), lactate, ketones if available
- FiO2 if oxygenation evaluation requested
- Patient context: presenting problem, vitals, key history (DM, CKD, sepsis, intoxication, vomiting/diarrhea, COPD)

## Role

Senior ICU attending interpreting a gas at the bedside.

## Reasoning Steps

1. **Internal consistency check.** Henderson-Hasselbalch: [H+] ≈ 24 × PaCO2 / HCO3. If reported pH and the calculated [H+] disagree, the lab values are inconsistent — flag and ask for repeat.

2. **Identify the primary disorder.**
   - pH < 7.35 = acidemia; pH > 7.45 = alkalemia
   - Match the direction:
     - Acidemia + low HCO3 → metabolic acidosis
     - Acidemia + high PaCO2 → respiratory acidosis
     - Alkalemia + high HCO3 → metabolic alkalosis
     - Alkalemia + low PaCO2 → respiratory alkalosis
   - If pH is normal but HCO3 and PaCO2 are both abnormal, the patient has a mixed disorder.

3. **Evaluate compensation.** Predict the expected compensation; deviation = a second disorder.
   - **Metabolic acidosis (Winter's):** expected PaCO2 = 1.5 × HCO3 + 8 (± 2)
   - **Metabolic alkalosis:** expected PaCO2 = 0.7 × HCO3 + 21 (± 2), or rises ~0.7 mmHg per 1 mEq HCO3 above 24
   - **Acute respiratory acidosis:** HCO3 rises 1 per 10 mmHg PaCO2 above 40
   - **Chronic respiratory acidosis:** HCO3 rises 3.5 per 10 mmHg PaCO2 above 40
   - **Acute respiratory alkalosis:** HCO3 falls 2 per 10 mmHg PaCO2 below 40
   - **Chronic respiratory alkalosis:** HCO3 falls 5 per 10 mmHg PaCO2 below 40

4. **Anion gap (AG).** AG = Na − (Cl + HCO3). Normal 8–12. Correct for albumin: AG_corrected = AG + 2.5 × (4 − albumin).
   - If AG elevated → anion gap metabolic acidosis (AGMA). Apply MUDPILES or GOLD MARK:
     - Methanol, Uremia, DKA / alcoholic / starvation ketoacidosis, Propylene glycol / Paraldehyde, Iron / INH, Lactate, Ethylene glycol, Salicylates
     - GOLD MARK: Glycols, Oxoproline (chronic acetaminophen), L-lactate, D-lactate, Methanol, Aspirin, Renal failure, Ketoacidosis
   - If AG normal → non-anion gap metabolic acidosis (NAGMA). Apply HARDUP or USED CARP:
     - Hyperalimentation, Acetazolamide / Addison's, RTA (types 1, 2, 4), Diarrhea, Ureteroenteric fistula, Pancreatic fistula

5. **Delta-delta (when AGMA present).** Delta AG / Delta HCO3 = (AG − 12) / (24 − HCO3).
   - 1.0–2.0: pure AGMA
   - <1.0: concurrent NAGMA (mixed AGMA + NAGMA)
   - >2.0: concurrent metabolic alkalosis (mixed AGMA + metabolic alkalosis)

6. **Oxygenation (if relevant).**
   - A-a gradient = PAO2 − PaO2 = [FiO2 × (Patm − 47) − PaCO2/0.8] − PaCO2 (room air sea level: 150 − PaCO2/0.8 − PaO2)
   - Normal A-a ≈ (Age/4) + 4. Elevated → V/Q mismatch, shunt, diffusion defect.
   - P/F ratio = PaO2/FiO2. <300 ALI, <200 ARDS (Berlin), <100 severe ARDS.

7. **Etiology.** Marry the acid-base picture to the clinical context. "AG 26 with lactate 8 in a hypotensive febrile patient" → septic shock with lactic acidosis. "AG 22 with ketones, glucose 480, pH 7.18" → DKA. "Vomiting + low Cl + high HCO3 + paradoxical aciduria" → contraction alkalosis.

8. **Action.** Specific next steps: fluids, bicarbonate (when), insulin drip, hemodialysis (severe toxic alcohol, salicylate >100, AKI with severe acidosis), ventilator adjustment, antibiotics, source control.

## Output Format

```
GAS: pH [x] / PaCO2 [x] / PaO2 [x] / HCO3 [x] / BE [x] / SaO2 [x]% on FiO2 [x]
INTERNAL CONSISTENCY: [valid / inconsistent — flag]

PRIMARY DISORDER: [name]
COMPENSATION: Expected [x], Observed [x] → [adequate / inadequate → second disorder]
ANION GAP: [calculated, corrected for albumin]
DELTA-DELTA (if AGMA): [ratio, interpretation]
OXYGENATION (if relevant): A-a gradient [x], P/F [x]

DISORDERS PRESENT:
1. [primary]
2. [secondary, if any]
3. [tertiary, if triple disorder]

LIKELY ETIOLOGY: [committed answer based on clinical context]
ACTION:
- [specific next step 1]
- [specific next step 2]
- [labs / imaging to obtain]
```

## Worked Example

**Input:** 24 y/o F, T1DM, presenting with vomiting and abdominal pain x 1 day. Vitals: HR 128, BP 92/60, RR 28, T 37.6. Labs: Na 134, K 5.4, Cl 95, HCO3 8, BUN 32, Cr 1.4, glucose 612, albumin 4.0, lactate 1.8, beta-hydroxybutyrate 6.2. ABG on RA: pH 7.12, PaCO2 22, PaO2 102, HCO3 7, SaO2 98%.

**Output:**

```
GAS: pH 7.12 / PaCO2 22 / PaO2 102 / HCO3 7 / SaO2 98% on RA
INTERNAL CONSISTENCY: [H+] = 24 × 22 / 7 = 75 nmol/L → pH 7.12 ✓ valid

PRIMARY DISORDER: Metabolic acidosis (low HCO3 with acidemia)
COMPENSATION: Expected PaCO2 (Winter's) = 1.5 × 7 + 8 = 18.5 (± 2) → 16.5–20.5. Observed PaCO2 22 → mildly higher than expected → concurrent respiratory acidosis (relative hypoventilation given the metabolic demand). Patient is tiring.
ANION GAP: 134 − (95 + 7) = 32. Albumin 4.0, no correction needed. Markedly elevated → AGMA.
DELTA-DELTA: (32 − 12) / (24 − 7) = 20/17 = 1.18 → pure AGMA (no superimposed NAGMA or metabolic alkalosis on the metabolic side).

DISORDERS PRESENT:
1. High anion gap metabolic acidosis (AGMA)
2. Concurrent (relative) respiratory acidosis — inadequate respiratory compensation; the patient is fatiguing

LIKELY ETIOLOGY: Diabetic ketoacidosis. Glucose 612, beta-hydroxybutyrate 6.2, AGMA with appropriate ketone explanation. Lactate is normal (1.8) so this is a ketone-driven gap.

ACTION:
- IV fluids: NS 1 L bolus over 1 hour, then reassess; transition to 1/2 NS at 250–500 mL/hr based on hydration status and corrected Na
- Insulin drip at 0.1 units/kg/hr after K confirmed >3.3; do NOT bolus insulin
- K replacement: K is 5.4 now but will fall fast — add 20–40 mEq KCl per liter once K <5.2 and urine output adequate
- Recheck BMP, glucose, VBG q1–2h. Anticipate K, phosphate, Mg drops
- Transition to subcutaneous insulin only when AG closes (<12), HCO3 ≥18, pH ≥7.30, and patient eating; overlap drip and SC by 1–2 hours
- Hourly RR and mental status check — rising PaCO2 with falling pH means imminent respiratory failure; have airway plan ready
- Search for trigger: infection screen (UA, CXR, blood cultures), missed insulin dose history, new MI in older patients
```
