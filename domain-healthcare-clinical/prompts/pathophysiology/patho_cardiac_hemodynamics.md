---
title: "Cardiac Hemodynamics Reasoning"
category: domain-healthcare-clinical/pathophysiology
description: "Reason through cardiac hemodynamics from preload, afterload, contractility, and heart rate to chamber pressures, output, and clinical findings in a specific cardiac state."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - CR-01
difficulty: advanced
tags:
  - cardiology
  - hemodynamics
  - preload
  - afterload
  - mechanism
updated: "2026-05-08"
---

## Objective

Given a specific cardiac pathology or hemodynamic scenario, reason through the loading conditions and contractility to predict chamber pressures, cardiac output, mixed venous saturation, and clinical findings. Output explains why the hemodynamics look the way they do and what each intervention will do mechanically.

## Inputs

- Cardiac state (e.g., "cardiogenic shock from acute MI," "septic shock," "tamponade," "RV failure from massive PE," "HFpEF decompensation," "aortic stenosis with hypotension")
- Available hemodynamic data: BP, HR, CVP, PCWP, PA pressures, cardiac index (CI), SVR, mixed venous saturation (SvO2), echo findings (EF, RV function, valvular disease)
- Optional: planned intervention to evaluate ("what will starting norepinephrine do here?", "why does giving fluid worsen this patient?")

## Role

Senior cardiology or critical care attending teaching hemodynamics at the bedside.

## Reasoning Steps

1. **Restate the hemodynamic state.** Name the syndrome (cardiogenic, hypovolemic, distributive, obstructive shock; HFrEF/HFpEF decompensation; valvular crisis).

2. **Frame each determinant of cardiac output.**
   - **Preload:** end-diastolic volume of each ventricle. Driven by venous return. Estimated by CVP (RV preload), PCWP (LV preload). Frank-Starling: increased preload → increased SV up to a plateau, then decline (acute decompensation).
   - **Afterload:** wall stress during ejection. SVR estimates LV afterload; PVR estimates RV afterload. LaPlace: wall stress = (pressure × radius) / (2 × wall thickness). Concentric hypertrophy reduces wall stress for a given pressure.
   - **Contractility (inotropy):** intrinsic myocardial force at given preload and afterload. Reflected in EF, dP/dt, end-systolic pressure-volume relationship.
   - **Heart rate:** rate × stroke volume = cardiac output. Excessive rate impairs diastolic filling (especially in HFpEF, MS, HCM).

3. **Pressure-volume relationships.**
   - Preload reserve: how much SV will rise with more preload. Falls in advanced systolic failure.
   - Afterload sensitivity: how much SV falls with more afterload. Highest in failing LV; lowest in normal heart.
   - Diastolic function: stiffer ventricle (HFpEF, ischemic, infiltrative, hypertrophic) means high LVEDP at relatively normal LVEDV → pulmonary congestion at "normal" volumes.

4. **Map pathology to determinants.**
   - **Cardiogenic shock from MI:** contractility falls (large infarct, ≥40% LV mass or critical territory), preload rises (failing LV cannot eject → backs up), afterload rises (compensatory sympathetic and RAAS activation increases SVR). End result: low CI + high PCWP + high SVR + low SvO2.
   - **Hypovolemic shock:** preload falls, contractility intact, afterload compensatorily rises (sympathetic). Low CVP, low PCWP, high SVR, low CI, low SvO2.
   - **Distributive (septic) shock:** SVR falls (vasodilation, NO synthesis from inducible NOS in vascular smooth muscle), preload variable but often relatively low (capillary leak, third-spacing, vasodilation), contractility paradoxically may be impaired in 30–50% (sepsis-induced cardiomyopathy) but often hyperdynamic early. Low SVR + normal or high CI early; low SVR + low CI in sepsis-induced cardiomyopathy. High SvO2 if mitochondrial dysfunction prevents O2 utilization.
   - **Obstructive (tamponade):** diastolic filling impaired by external compression; equalization of diastolic pressures (CVP ≈ PCWP ≈ PA diastolic ≈ pericardial pressure). Stroke volume falls; tachycardia compensates partly. Pulsus paradoxus from interventricular dependence.
   - **RV failure from PE:** PVR rises acutely from clot burden + hypoxic vasoconstriction; RV cannot generate enough pressure → RV dilates → septum bows leftward → impairs LV filling → systemic hypotension. CVP high, PCWP normal or low, RV pressure-overloaded on echo.

5. **Predict associated findings.**
   - Mixed venous oxygen saturation (SvO2): falls when CO is low (more O2 extracted per mL blood); high in distributive shock (microvascular shunting); high in severe MR (oxygenated blood passes through).
   - Lactate: rises when O2 delivery < O2 demand at tissue level.
   - JVP: rises with elevated CVP (RV failure, tamponade, tricuspid disease, volume overload).
   - Crackles: pulmonary edema from elevated PCWP.
   - Cool extremities: high SVR (vasoconstriction).
   - Warm extremities: low SVR (sepsis early).
   - Pulse pressure: narrow in low CO with high SVR; wide in AR, severe AS post-AVR, or high-output states.

6. **Predict effect of each intervention.**
   - Volume: increases preload. Helps hypovolemic and right heart-limited states; worsens cardiogenic and HFpEF if PCWP already high.
   - Norepinephrine: increases SVR (alpha-1) and modestly contractility (beta-1). Raises BP, raises afterload (caution in cardiogenic), raises preload via venoconstriction.
   - Epinephrine: beta-1 inotropy + beta-2 vasodilation at lower dose, alpha-1 vasoconstriction at higher dose. Raises CO; arrhythmogenic.
   - Dobutamine: beta-1 inotropy + beta-2 vasodilation. Raises CO, lowers SVR. First-line in cardiogenic shock without severe hypotension.
   - Milrinone: PDE3 inhibitor → cAMP rises in myocyte (inotropy) and vascular smooth muscle (vasodilation). Lowers PVR and SVR; useful in RV failure and pulmonary hypertension. Not first-line in shock because of hypotension; long t½ (~2.5 h, longer in renal failure).
   - Vasopressin: V1 vasoconstriction (independent of catecholamine pathway). Useful adjunct in vasodilatory shock.
   - Diuresis: reduces preload. Helps congestion; can drop CO if patient is preload-dependent.
   - Inhaled NO or epoprostenol: pulmonary vasodilation; lowers PVR; helps RV failure and pulmonary hypertension.

## Output Format

```
HEMODYNAMIC STATE: [name the syndrome]
DATA: [available BP, HR, CVP, PCWP, CI, SVR, SvO2]

DETERMINANT WALK:
- Preload: [direction, mechanism]
- Afterload: [direction, mechanism]
- Contractility: [direction, mechanism]
- Heart rate: [direction, mechanism]

PRESSURE-VOLUME LOGIC:
- [chamber-specific volume and pressure analysis]

PREDICTED ASSOCIATED FINDINGS:
- SvO2: [...]
- Lactate: [...]
- JVP / crackles / extremities / pulse pressure: [...]

INTERVENTION EFFECTS:
- [intervention 1] → [hemodynamic change predicted]
- [intervention 2] → [...]

COMMITTED MANAGEMENT REASONING:
- [what to do, why, and what would worsen this state]
```

## Worked Example

**Input:** A 65 y/o M with massive submassive PE (saddle thrombus on CTA). BP 92/64, HR 118, satting 88% on 4 L NC. Echo: severely dilated and hypokinetic RV with septal bowing into LV in diastole, McConnell's sign (apical RV sparing with mid free-wall hypokinesis), small underfilled LV. CVP 18, lactate 3.4. Should we give fluids? Start norepinephrine? Inotrope?

**Output:**

```
HEMODYNAMIC STATE: Acute submassive PE with RV failure and obstructive shock physiology. Pulmonary vascular obstruction has acutely raised PVR beyond what the RV can generate; the RV is failing forward (low CO into LV) and backward (rising RAP, JVP, hepatic congestion).
DATA: BP 92/64, HR 118, SpO2 88% on 4 L. CVP 18 (high). Echo: severely dilated hypokinetic RV with septal bowing leftward in diastole; underfilled LV. McConnell's sign (specific for acute RV strain, often PE). Lactate 3.4.

DETERMINANT WALK:
- Preload (RV): elevated (CVP 18). RV is dilated and failing; further preload pushes RV up the descending limb of Frank-Starling and worsens septal bowing into LV.
- Preload (LV): reduced. Septal bowing from a pressure-overloaded RV reduces LV diastolic volume (interventricular dependence) → low LV preload → low LV stroke volume → systemic hypotension.
- Afterload (RV): markedly elevated PVR from mechanical clot obstruction + hypoxic pulmonary vasoconstriction + endogenous vasoconstrictors released from clot.
- Afterload (LV): SVR likely elevated from compensatory sympathetic activation, but LV is underfilled so hypotension persists.
- Contractility (RV): compromised by the acute strain and ischemia (RV mismatch — high wall stress with normal-to-low coronary perfusion gradient).
- Heart rate: tachycardic compensation; further benefit limited because diastolic filling time of underfilled LV is already short.

PRESSURE-VOLUME LOGIC:
- The RV is on the descending limb of its function curve. More preload = worse RV function = more septal bowing = even less LV filling = more shock. This is the classic "fluid worsens RV failure" trap.
- The LV is volume-depleted relative to its capacity but you cannot fill it via systemic venous loading because the RV cannot pass that volume forward through high PVR.
- LV coronary perfusion depends on (aortic diastolic pressure − LVEDP); systemic hypotension reduces RV coronary perfusion (RV is perfused throughout the cardiac cycle in normal states, but during pressure overload becomes systolic-only like the LV) → RV ischemia → worse contractility → spiral.

PREDICTED ASSOCIATED FINDINGS:
- SvO2: low (high O2 extraction from low forward CO).
- Lactate: elevated (here 3.4) from inadequate tissue O2 delivery.
- JVP: markedly elevated; Kussmaul sign possible.
- Crackles: usually absent — left heart is underfilled, not overloaded.
- Extremities: cool from low CO and SVR-mediated compensation.
- ECG: sinus tachycardia, S1Q3T3 (specific but insensitive), RBBB, T-wave inversions in V1–V4 (RV strain).
- Troponin: often elevated from RV strain — independent prognostic marker.
- BNP: elevated from RV stretch — also prognostic.

INTERVENTION EFFECTS:
- Fluid bolus 500–1000 mL: WILL WORSEN this patient. Adds preload to a RV that is already failing on the descending limb. Worsens septal bowing, further decreases LV filling, drops BP further. Fluids are appropriate only when CVP is low and RV is preload-dependent — not here with CVP 18 and dilated RV on echo.
- Norepinephrine (low dose, e.g., 0.05–0.1 mcg/kg/min): raises systemic BP via alpha-1 SVR increase, restores aortic root pressure → improves RV coronary perfusion → improves RV contractility. This is the appropriate first-line vasopressor in RV failure. Avoid pushing too hard — extreme alpha may further raise PVR via pulmonary alpha receptors.
- Dobutamine (2.5–10 mcg/kg/min): adds RV inotropy and modestly lowers PVR via beta-2; risk of hypotension if SVR is fragile. Often combined with norepinephrine.
- Milrinone: lowers PVR and SVR, increases inotropy. Useful but causes hypotension; pair with vasopressor. Long t½ a problem if patient deteriorates.
- Inhaled pulmonary vasodilator (NO 20–40 ppm or inhaled epoprostenol): selectively lowers PVR without dropping SVR. Bridge to definitive therapy.
- Definitive: systemic thrombolysis (alteplase 100 mg over 2 h or low-dose 50 mg) for hemodynamic instability; catheter-directed thrombolysis or surgical embolectomy in selected cases. ECMO (VA) as bridge if circulatory collapse.
- Avoid intubation and positive-pressure ventilation if possible — induction agents drop preload and SVR; positive intrathoracic pressure further reduces venous return; high PEEP raises PVR. Patients can arrest at intubation. If unavoidable: pre-load with norepinephrine, etomidate for induction (preserves hemodynamics), avoid succinylcholine in known PE if hyperK is a concern, use lung-protective settings with low PEEP (5).

COMMITTED MANAGEMENT REASONING:
1. Do not give fluid. CVP 18 and a dilated RV define the upper limit of preload tolerance.
2. Start norepinephrine immediately to restore aortic root pressure and rescue RV coronary perfusion. Target MAP ≥65; many would target 70–75 to compensate for elevated RAP.
3. Add dobutamine 2.5–5 mcg/kg/min for RV inotropic support if MAP rescued but CO/perfusion still inadequate.
4. Activate PERT / pulmonary embolism response team. Decision between systemic thrombolysis vs catheter-directed vs surgical embolectomy depends on bleeding risk, center capability, and clinical trajectory. Hemodynamic instability with submassive features and progression toward massive supports thrombolysis.
5. Give therapeutic anticoagulation (heparin infusion) immediately unless thrombolysis is imminent — the heparin bridge runs concurrently in many centers; coordinate with thrombolysis plan.
6. Avoid intubation if at all possible. Use HFNC or non-rebreather. Reserve intubation for failure of oxygenation despite all measures, with ICU/PERT team prepared for arrest.
```
