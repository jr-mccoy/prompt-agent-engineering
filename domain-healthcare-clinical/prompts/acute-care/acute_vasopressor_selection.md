---
title: "Vasopressor Selection in Shock"
category: domain-healthcare-clinical/acute-care
description: "Select and titrate vasopressor and inotrope therapy for a specific shock state with named agents, doses, escalation thresholds, and combination logic."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - critical-care
  - shock
  - vasopressor
  - hemodynamics
updated: "2026-05-08"
---

## Objective

Given a specific shock state with available hemodynamic data, select the first-line vasopressor or inotrope, name dose ranges and titration targets, and define when to add a second agent or escalate. Output names agents, mcg/kg/min ranges, and the order of escalation.

## Inputs

- Shock category (septic, cardiogenic, hypovolemic, distributive non-septic, obstructive, mixed) or as much as known
- Vitals: MAP, HR, SpO2, lactate, urine output
- Hemodynamic data if available: CVP, PCWP, CI, SVR, SvO2, echo findings (LV/RV function, IVC)
- Prior interventions: fluid resuscitation given, current pressors, mechanical ventilation
- Patient factors: age, comorbidities (CAD, HFrEF, RV disease), pregnancy

## Role

Senior critical care attending or emergency medicine attending titrating pressors at the bedside.

## Reasoning Steps

1. **Confirm shock physiology.** MAP <65, lactate >2, organ dysfunction (oliguria, altered mental status). Categorize: warm vs cold, pulmonary edema vs not, JVP/CVP high vs low.

2. **First-line agent by shock type:**
   - **Septic shock:** norepinephrine. Start 0.05 mcg/kg/min, titrate q3–5 min to MAP ≥65. Range to ~0.5 mcg/kg/min before adding second agent.
   - **Cardiogenic (no profound hypotension):** dobutamine 2.5–10 mcg/kg/min for inotropy. If MAP <65, add norepinephrine first to restore perfusion pressure, then add dobutamine for inotropy.
   - **Cardiogenic with profound hypotension:** norepinephrine first to restore aortic root pressure (which restores coronary perfusion to the failing ventricle), then add dobutamine or milrinone.
   - **RV failure (massive/submassive PE, pulmonary HTN crisis, RV MI):** norepinephrine first (alpha-1 raises SVR → improves RV coronary perfusion). Dobutamine for RV inotropy. Inhaled pulmonary vasodilator (NO 20–40 ppm or inhaled epoprostenol) to lower PVR. Avoid pure alpha agents that may raise PVR.
   - **Hypovolemic:** fluids first; pressor only as bridge. Norepinephrine acceptable bridge.
   - **Anaphylaxis:** epinephrine IM 0.3–0.5 mg q5–15 min; IV infusion 0.05–0.5 mcg/kg/min if refractory or peri-arrest.
   - **Tamponade / tension pneumo:** mechanical relief is the answer; pressor is only a bridge. Norepinephrine while preparing pericardiocentesis or chest tube.
   - **Neurogenic shock (high spinal injury):** norepinephrine; phenylephrine acceptable in patients with adequate cardiac function. Often need pacing for severe bradycardia.

3. **Second-agent logic:**
   - **Septic shock not responding to norepinephrine ~0.3–0.5 mcg/kg/min:** add vasopressin 0.03 units/min (fixed; do not titrate beyond this in standard sepsis protocols). Vasopressin is V1-mediated, catecholamine-independent → useful when vasoplegia is severe and beta-receptors are downregulated.
   - **Septic shock with persistent hypotension on norepi + vasopressin:** add hydrocortisone 200 mg/day (50 mg q6h or continuous infusion). Stress-dose steroids reduce vasopressor duration and probably mortality in vasopressor-dependent septic shock.
   - **Septic shock refractory to above:** consider epinephrine (added or substituted for norepi); angiotensin II (giapreza) for catecholamine-resistant vasodilatory shock; methylene blue for refractory vasoplegia.
   - **Cardiogenic shock with low CO despite dobutamine:** consider milrinone (PDE3 inhibitor, lowers PVR, useful in pulmonary HTN, but causes hypotension; pair with vasopressor); mechanical circulatory support (IABP, Impella, VA-ECMO) for severe persistent low output.

4. **Avoid these pitfalls.**
   - Pure alpha agents (phenylephrine) in cardiogenic shock — raises afterload on a failing pump.
   - Dopamine: associated with more arrhythmia and mortality vs norepi in shock; relegated to bradycardic shock or specialized scenarios.
   - High-dose epinephrine routinely as first-line: more arrhythmia, more lactate, harder to titrate than norepi.
   - Starting pressors before adequate volume resuscitation in septic shock without echo evidence of cardiac dysfunction.
   - Withholding pressors waiting for "more fluids" in clearly volume-replete patient — escalate pressor.

5. **Targets and weaning.**
   - MAP target ≥65 (higher, 75–85, in chronic HTN or to maintain renal function — RCTs are mixed).
   - Lactate trend, urine output, mental status, capillary refill — composite targets, not MAP alone.
   - Wean once underlying cause controlled (source control in sepsis, revascularization in cardiogenic, drainage in obstructive). Reduce one agent at a time, vasopressin last (rebound hypotension common when removed before norepi is at low dose).

6. **Access and monitoring.**
   - Central venous access for infusions >0.1 mcg/kg/min norepi, all epinephrine and vasopressin infusions, and most cardiogenic shock pressors. Peripheral lines for short-term lower-dose norepi (recent literature shows safe up to 0.1 mcg/kg/min for ≤4–6 hours in well-functioning antecubital IVs).
   - Arterial line for accurate MAP and serial blood gases.
   - Echo (POCUS) repeatedly to reassess preload, RV function, LV function, pericardial effusion.
   - Daily reassessment: shock state may evolve (cardiogenic shock from sepsis-induced cardiomyopathy can develop in patient who was distributive on admission).

## Output Format

```
SHOCK CATEGORY: [committed answer]
HEMODYNAMIC PICTURE: [restate the data and what it implies]

FIRST-LINE AGENT:
- [drug] starting [dose], titrate to [target]
- Mechanism: [why this drug for this shock]

SECOND AGENT (if needed):
- Threshold: [when to add]
- Drug: [name, dose]
- Mechanism: [why]

THIRD AGENT (if needed):
- Threshold: [...]
- Drug: [...]

ADJUNCTS:
- [steroids / inhaled vasodilator / mechanical support if applicable]

AVOID:
- [agent and why in this scenario]

TARGETS:
- MAP [number]
- Lactate trend, urine output, mental status

ACCESS:
- [central line, art line, echo]

WEANING:
- [order of taper]
```

## Worked Example

**Input:** 64 y/o M, septic shock from urosepsis. Received 30 mL/kg LR over 2 hours (2.4 L). Now: MAP 56, HR 122, lactate 4.8, UOP 15 mL/h, mottled extremities. POCUS: hyperdynamic LV, IVC small and collapsing >50%. CVP 6.

**Output:**

```
SHOCK CATEGORY: Septic shock (distributive). Persistent hypotension after adequate initial fluid resuscitation = vasopressor-dependent septic shock by definition.
HEMODYNAMIC PICTURE: Hyperdynamic LV and small collapsing IVC with low CVP suggest he is not yet fully volume-replete — but the lactate is high and MAP critically low; pressors must start now while continuing volume.

FIRST-LINE AGENT:
- Norepinephrine starting 0.05 mcg/kg/min via central or well-functioning peripheral line, titrate q3–5 min by 0.05 mcg/kg/min increments to MAP ≥65.
- Mechanism: alpha-1 vasoconstriction restores SVR (the broken determinant in sepsis); modest beta-1 inotropy supports the hyperdynamic but stressed LV without major arrhythmia risk.
- Continue concurrent fluid resuscitation: another 500–1000 mL crystalloid bolus while assessing fluid responsiveness (passive leg raise, IVC dynamics, stroke volume variation if monitored). Do not chase fluids indefinitely — fluid overload is harmful in sepsis.

SECOND AGENT (if needed):
- Threshold: norepinephrine reaches ~0.3–0.5 mcg/kg/min and MAP still <65, OR norepi escalation rapid.
- Drug: vasopressin 0.03 units/min, fixed dose (do not titrate beyond).
- Mechanism: V1-receptor vasoconstriction independent of adrenergic pathway; catecholamines are downregulated in sepsis. Spares norepi dose, reduces arrhythmia risk.

THIRD AGENT (if needed):
- Threshold: persistent hypotension despite norepi + vasopressin.
- Drug: epinephrine 0.05 mcg/kg/min titrated up, OR angiotensin II 5–20 ng/kg/min for catecholamine-refractory vasoplegia. Methylene blue 1–2 mg/kg IV bolus once for refractory vasoplegia is reasonable in selected patients.

ADJUNCTS:
- Hydrocortisone 50 mg IV q6h (or 200 mg/day continuous) once on second pressor — reduces vasopressor duration in septic shock.
- Source control: imaging now (CT abdomen/pelvis if not already done), urology consult if obstructed kidney, drainage of any abscess.
- Antibiotics: ensure broad-spectrum gram-negative coverage now if not yet given. Time-to-antibiotics matters in sepsis mortality.

AVOID:
- Phenylephrine: pure alpha; loses the modest beta-1 support of norepi without benefit; reflex bradycardia can drop CO.
- Dopamine: more arrhythmia and mortality vs norepi.
- Routine bicarbonate for lactate/acidosis: pH >7.20 does not benefit.

TARGETS:
- MAP ≥65 (consider 75 if chronic HTN with high baseline).
- Lactate clearance ≥10% in first 2 hours, trending toward normal.
- UOP >0.5 mL/kg/h.
- Capillary refill <3 seconds.

ACCESS:
- Place central venous catheter (IJ or subclavian) for sustained pressor infusion and CVP monitoring.
- Arterial line for accurate MAP.
- POCUS reassess q2–4h: LV function, RV function, IVC, B-lines on lung exam.

WEANING:
- Source control + antibiotics + ongoing volume titration.
- Wean norepinephrine first as it is dose-titratable. Once norepi <0.05 mcg/kg/min, discontinue vasopressin (if used).
- Hydrocortisone taper over 5–7 days once off pressors.
```
