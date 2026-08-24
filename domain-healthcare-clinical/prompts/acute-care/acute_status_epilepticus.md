---
title: "Status Epilepticus Management"
category: domain-healthcare-clinical/acute-care
description: "Run a status epilepticus algorithm: benzodiazepine first-line, second-line antiepileptic, refractory anesthetic infusion, and concurrent workup."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - neurology
  - status-epilepticus
  - critical-care
  - antiepileptic
updated: "2026-05-08"
---

## Objective

Manage convulsive status epilepticus with timed, sequenced pharmacotherapy and concurrent workup. Output is a phase-by-phase algorithm with named drugs, doses, and time thresholds.

## Inputs

- Seizure description: tonic-clonic, focal motor, absence-like, suspected non-convulsive
- Duration of current seizure activity (or time since onset if witnessed)
- Patient: age, weight, prior seizure history, antiepileptic regimen, comorbidities (hepatic, renal, cardiac), current pregnancy
- Vital signs, glucose at bedside, IV access status

## Reasoning Steps

1. **Define status epilepticus.** Continuous seizure activity ≥5 minutes, OR ≥2 seizures without recovery to baseline between them. Treat aggressively from minute 5; do not wait for the older 30-minute definition.

2. **Concurrent measures (first 5 min).**
   - ABC: airway position, suction, supplemental O2, monitor SpO2.
   - IV access ×2 (if first attempt fails, IM or IO route for benzo).
   - Fingerstick glucose immediately. Hypoglycemia is treatable cause and easily missed.
   - Place on telemetry, NIBP, SpO2.
   - If hypoglycemic: D50 50 mL IV bolus (children: D25 2 mL/kg or D10 5 mL/kg). Add thiamine 100 mg IV before glucose in alcohol-use or malnourished patients to prevent Wernicke.

3. **Phase 1 — Benzodiazepine (5–20 min).**
   - **Lorazepam 0.1 mg/kg IV (typical 4 mg) over 2 min, may repeat once after 5 min.** First-line if IV access.
   - **Midazolam 10 mg IM** (or 0.2 mg/kg IM) if no IV access — equivalent efficacy to IV lorazepam (RAMPART trial).
   - **Diazepam 0.15 mg/kg IV (typical 10 mg) over 2 min** acceptable alternative if lorazepam not on hand. Or PR (5–10 mg in adult; 0.5 mg/kg child) if no IV/IM.
   - **Underdosing benzodiazepines is the most common error.** Give the full dose.

4. **Phase 2 — Second-line antiepileptic (20–40 min, if seizure continues).**
   - Three options with comparable efficacy in ESETT trial (~50% termination at 60 min):
     - **Levetiracetam 60 mg/kg IV (max 4500 mg) over 10 min.** First choice for many — minimal interactions, no hepatic concerns, no hemodynamic effects.
     - **Fosphenytoin 20 mg PE/kg IV (max 1500 mg PE) at 150 mg PE/min.** Watch QT and BP; monitor for hypotension. Avoid in hepatic failure.
     - **Valproate 40 mg/kg IV (max 3000 mg) over 10 min.** Avoid in hepatic disease, pregnancy (teratogenic), suspected mitochondrial disease, known carnitine deficiency.
   - Choose based on patient: pregnant → levetiracetam; hepatic disease → levetiracetam; renal failure → adjust levetiracetam dose; QT prolongation → avoid fosphenytoin; mitochondrial → avoid valproate.

5. **Phase 3 — Refractory status epilepticus (40+ min).**
   - Intubate (if not already) with rapid-sequence induction. Use etomidate or propofol (propofol has antiepileptic activity).
   - Continuous EEG (cEEG) monitoring — must start. Without cEEG, you cannot detect ongoing electrographic seizures masked by paralysis.
   - Anesthetic infusion. Goal: burst suppression on EEG for 24–48 hours, then taper.
     - **Midazolam infusion 0.05–2 mg/kg/h** (load 0.2 mg/kg). Tachyphylaxis develops; doses escalate.
     - **Propofol infusion 30–200 mcg/kg/min** (load 1–2 mg/kg). Watch for propofol infusion syndrome (lactic acidosis, rhabdo, cardiac failure, hypertriglyceridemia) at sustained high doses; check CK and lipids daily.
     - **Pentobarbital infusion 1–10 mg/kg/h** (load 5–15 mg/kg) — last-line. Long t½, profound hypotension.
     - **Ketamine infusion 1–10 mg/kg/h** (load 1.5 mg/kg) — increasingly used; preserves hemodynamics, NMDA antagonism.

6. **Phase 4 — Super-refractory status epilepticus (>24 h despite anesthetic).**
   - Continue anesthetic, optimize maintenance AED, address triggers.
   - Add additional AEDs: lacosamide 200–400 mg IV, phenobarbital 20 mg/kg IV (monitor for hypotension, sedation, respiratory depression).
   - Consider: ketogenic diet (effective in some pediatric and adult cases), immunotherapy if autoimmune encephalitis suspected (high-dose steroids, IVIG, plasmapheresis), hypothermia, surgical intervention.

7. **Concurrent workup (run in parallel from the start).**
   - **Reversible causes first:** glucose (already done), Na (hyponatremic seizures need 3% saline 100 mL bolus, can repeat ×3), Ca/Mg (hypocalcemia, hypomagnesemia precipitate seizures — replace empirically if status refractory and electrolytes not yet back), uremia.
   - **Toxicology / withdrawal:** alcohol withdrawal (give thiamine + benzo), benzodiazepine withdrawal, isoniazid (give pyridoxine 5 g IV), tricyclic overdose (sodium bicarbonate), bupropion, tramadol, theophylline.
   - **Infection:** fever, meningismus → LP after stabilization, CT head first if focal deficit. Empiric antibiotics + acyclovir for suspected bacterial meningitis or HSV encephalitis.
   - **Structural:** stroke, hemorrhage, tumor, abscess → CT head non-contrast urgently. Consider MRI when stable.
   - **AED level:** if known epilepsy on AED, draw level — subtherapeutic from missed doses is common.
   - **Eclampsia:** in pregnant or postpartum patient → magnesium sulfate 4–6 g IV load over 15–20 min, then 1–2 g/h infusion. Magnesium is first-line, not benzo, in eclamptic seizures.
   - **Autoimmune encephalitis:** suspect when cryptogenic, young patient, recent neuropsychiatric symptoms, MRI mesiotemporal abnormalities. Send autoimmune encephalitis panel (NMDA-R, LGI1, GABA-B, etc.); start empiric immunotherapy if high suspicion.

8. **Documentation and signout.** Time stamps for each medication and observed effect. cEEG at the bedside. Plan for tapering anesthetic with cEEG monitoring.

## Output Format

```
TIME ZERO ACTIONS (first 5 min):
- ABC, O2, suction, IV ×2 (or IM/IO if no IV)
- Fingerstick glucose, telemetry, NIBP, SpO2
- Thiamine 100 mg IV if at risk + D50 if hypoglycemic

PHASE 1 (5–20 min) — Benzodiazepine:
- [drug, dose, route, repeat]

PHASE 2 (20–40 min) — Second-line AED:
- [drug, dose, rate]

PHASE 3 (40+ min) — Refractory:
- Intubate, cEEG
- [anesthetic, load, infusion]

PHASE 4 — Super-refractory:
- [escalation options]

CONCURRENT WORKUP:
- Labs: [list]
- Imaging: [list]
- Specific scenarios: [eclampsia, INH, alcohol withdrawal, autoimmune]

DISPOSITION: ICU with cEEG.

PITFALLS TO AVOID:
- [underdosing benzo, missing reversible cause, paralyzing without cEEG, etc.]
```

## Worked Example

**Input:** 28 y/o pregnant woman (32 weeks gestation) brought to ED after witnessed tonic-clonic seizure at home that lasted "a few minutes," currently still seizing in ED. BP 168/108, HR 110, T 36.9. Weight ~75 kg. No prior seizure history.

**Output:**

```
TIME ZERO ACTIONS (first 5 min):
- ABC, O2 by mask, lateral position, suction, IV ×2.
- Fingerstick glucose (likely normal but always check).
- Telemetry, frequent BP, SpO2, fetal monitoring.
- Notify obstetrics and neurology immediately.
- This is eclampsia until proven otherwise: pregnant, third trimester, hypertensive (168/108), seizing. Magnesium is first-line, not benzodiazepines.

PHASE 1 — Eclampsia-specific (immediate):
- Magnesium sulfate 4 g IV bolus over 15–20 min, then 2 g/h continuous infusion. Goal: serum Mg 4–7 mEq/L.
- If seizure continues despite mag bolus: lorazepam 4 mg IV may be added. But the priority intervention is magnesium.
- BP control: labetalol 20 mg IV, may repeat 40 mg q10 min (max 300 mg total). Goal SBP <160, DBP <110, MAP not dropped abruptly to avoid placental hypoperfusion.

PHASE 2 (20–40 min) — Second-line AED if magnesium fails:
- Levetiracetam 60 mg/kg IV = 4500 mg (max) over 10 min. Preferred AED in pregnancy.
- Avoid valproate (teratogenic; this patient is already pregnant but third trimester organogenesis less of an issue — still, levetiracetam is safer).
- Avoid phenytoin/fosphenytoin if possible due to fetal hydantoin syndrome risk and maternal hemodynamic effects; acceptable if needed.

PHASE 3 (40+ min) — Refractory:
- Intubate (RSI with etomidate or propofol).
- Continuous EEG.
- Propofol infusion 30–100 mcg/kg/min initially. In pregnancy, propofol crosses placenta — fetal monitoring continuous; obstetrics making delivery decisions in parallel.
- The definitive treatment for eclampsia is delivery. Continued seizures after stabilization → urgent obstetric delivery decision.

CONCURRENT WORKUP (eclampsia-specific):
- Labs: CBC (HELLP — hemolysis, low platelets), peripheral smear (schistocytes), LDH, haptoglobin, AST/ALT, BMP (Cr), uric acid, urine protein:Cr ratio, coags (DIC complication possible).
- Magnesium level after loading (target 4–7 mEq/L); monitor reflexes, RR, urine output (Mg is renally cleared; Cr rise → reduce dose).
- Fetal monitoring continuous; obstetrics for delivery planning.
- Imaging: CT head non-contrast if seizure was focal, persistent neurologic deficit, or atypical features (concern for ICH which complicates ~2% of severe pre-eclampsia/eclampsia). MRI later if available; PRES (posterior reversible encephalopathy) is in the differential.
- ECG.

DISPOSITION: Labor and delivery / OB-ICU. Continuous cEEG if seizures persist post-magnesium. Plan for delivery — eclampsia is treated by delivery; magnesium is bridge.

PITFALLS TO AVOID:
- Defaulting to lorazepam first in a pregnant seizing patient — magnesium is first-line for eclampsia and should not be delayed for benzodiazepine.
- Aggressive BP reduction below MAP 100–105 → placental hypoperfusion and fetal compromise.
- Missing HELLP syndrome — must check platelets, LDH, haptoglobin, smear; HELLP changes management and delivery urgency.
- Failing to deliver: persistent eclampsia despite magnesium and BP control = delivery indicated, gestational age permitting and after maternal stabilization.
- Not continuing magnesium for 24 hours postpartum (eclamptic seizures can occur up to 6 weeks postpartum but most within 48 h after delivery).
- Confusing eclampsia with new-onset epilepsy or non-eclamptic seizure in pregnancy: eclampsia diagnosis requires HTN and/or proteinuria with seizure in pregnancy or postpartum.
```
