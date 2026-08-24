---
title: "Critical Care Daily Progress Note"
category: domain-healthcare-clinical/workflow
description: "Generate an ICU daily note by organ system — with drips, vent settings, lines, and a systems-based assessment and plan — at intensivist documentation standard."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
  - DS-02
difficulty: advanced
tags:
  - documentation
  - critical-care
  - icu
  - systems-based-note
updated: "2026-06-19"
---

## Objective

Produce an ICU daily progress note organized by organ system: the events of the last 24 hours, the objective data including drips and device settings, and a systems-based assessment and plan. The ICU note's defining feature is the head-to-toe systems framework, which forces completeness across the multiple simultaneous problems a critically ill patient has, and supports the daily-goals/checklist function (sedation, VTE/GI prophylaxis, lines, nutrition, glycemic control).

## Inputs

- ICU day, primary diagnosis/reason for ICU admission
- Overnight events and interval change
- Vitals with ranges, hemodynamics, current vasoactive/sedation drips with rates
- Ventilator settings and respiratory parameters (or O2 device), ABG
- I/O, fluid balance, weight; renal/dialysis status
- Current labs, cultures, imaging
- Active infusions, antibiotics (day of therapy), nutrition, lines/tubes/drains
- Neurologic status/sedation, glycemic control

## Role

Intensivist rounding and documenting the daily ICU note.

## Reasoning Steps

1. **Open with a one-liner and ICU day,** the reason for ICU admission, and the overall trajectory (improving, stable, critical). Set the frame.

2. **Capture the 24-hour events** — significant changes, procedures, escalations or de-escalations, new culture data, family discussions.

3. **Document objective data with the ICU specifics:** vitals ranges, hemodynamics, every active drip with its current rate (norepinephrine 0.08 mcg/kg/min, propofol 30 mcg/kg/min), vent settings (mode, FiO2, PEEP, tidal volume, latest ABG), I/O and net balance, and current labs.

4. **Work the assessment and plan by organ system,** the core ICU discipline:
   - **Neuro:** mental status, sedation (target RASS, agent), analgesia, delirium (CAM-ICU).
   - **CV:** hemodynamics, vasopressors/inotropes, rhythm, fluid responsiveness.
   - **Resp:** vent settings and weaning status (SBT, RSBI), oxygenation, secretions.
   - **GI/Nutrition:** feeding (enteral/TPN), bowel function, GI prophylaxis, LFTs.
   - **Renal/Fluids/Lytes:** urine output, creatinine, dialysis, electrolyte repletion, net balance goal.
   - **Heme:** Hgb, platelets, coags, transfusion/VTE prophylaxis.
   - **ID:** temperature/WBC, cultures, antibiotics with day-of-therapy and planned duration/de-escalation, source control.
   - **Endo:** glucose control, steroids, thyroid/adrenal as relevant.

5. **Run the daily-goals checklist:** sedation target and daily awakening, spontaneous breathing trial candidacy, line necessity (can any line/tube come out today?), VTE and GI prophylaxis, nutrition, glycemic target, mobility, code status/goals.

6. **Each system gets an assessment and a today-action,** with named drugs/doses and explicit weaning or escalation decisions. Don't carry forward settings that the data says should change (wean FiO2, narrow antibiotics, de-escalate pressors).

7. **Keep it current** — ICU notes are high-stakes and frequently copy-forwarded; reflect today's data, not yesterday's.

## Output Format

```
ICU Progress Note — ICU Day [#]
ONE-LINER: [age, sex, reason for ICU admit, trajectory]

24-HOUR EVENTS:
[interval changes, procedures, new data]

OBJECTIVE:
- Vitals: [ranges]; hemodynamics: [MAP, etc.]
- Drips: [agent + rate, each]
- Vent: [mode, FiO2, PEEP, Vt, RR]; ABG: [values]
- I/O: [in/out/net]; weight:
- Labs: [current, salient interpreted]
- Lines/tubes/drains: [list + day]
- Antibiotics: [agent, day of therapy]

ASSESSMENT & PLAN (by system):
NEURO: [assessment] → [plan/action]
CV: ...
RESP: ...
GI/NUTRITION: ...
RENAL/FLUIDS/LYTES: ...
HEME: ...
ID: ...
ENDO: ...

DAILY GOALS CHECKLIST:
- Sedation target/awakening: 
- SBT candidacy: 
- Lines to remove: 
- VTE prophylaxis: / GI prophylaxis: 
- Nutrition: / Glycemic target: 
- Mobility: 
- Code status/goals: 
```

## Worked Example

**Input:** ICU Day 2, septic shock from pneumonia, intubated. Overnight: weaning norepinephrine, lactate cleared 4.2 → 1.6, started enteral feeds. Vitals MAP 70–78, HR 88–96. Norepinephrine down to 0.04 mcg/kg/min, propofol 25 mcg/kg/min. Vent: AC/VC, FiO2 0.4, PEEP 8, Vt 6 mL/kg, last ABG 7.36/40/92. UOP improving, net +1.2L. WBC 14 down from 19. Cultures: blood pending, sputum gram-positive cocci. On ceftriaxone+azithromycin day 2. Glucose 150s.

**Output:**

```
ICU Progress Note — ICU Day 2
ONE-LINER: Adult with septic shock secondary to community-acquired pneumonia, intubated/ventilated, improving — vasopressor weaning, lactate cleared.

24-HOUR EVENTS:
Hemodynamically improving overnight with successful down-titration of norepinephrine. Lactate cleared from 4.2 to 1.6. Enteral nutrition initiated and tolerated. No new fevers or events.

OBJECTIVE:
- Vitals: MAP 70–78, HR 88–96, afebrile. 
- Drips: norepinephrine 0.04 mcg/kg/min (weaning); propofol 25 mcg/kg/min.
- Vent: AC/VC, FiO2 0.40, PEEP 8, Vt 6 mL/kg (lung-protective), RR set 18. ABG 7.36/40/92.
- I/O: net +1.2 L over 24h; urine output improving.
- Labs: WBC 14 (down from 19), lactate 1.6 (cleared), Cr improving, K repleted.
- Lines/tubes/drains: right IJ central line (day 2), arterial line (day 2), ETT, Foley.
- Antibiotics: ceftriaxone + azithromycin, day 2.

ASSESSMENT & PLAN (by system):
NEURO: Sedated on propofol, target RASS −1 to 0. → Begin daily sedation awakening trial this morning; assess for extubation readiness; CAM-ICU screen.
CV: Septic shock resolving, norepinephrine weaning. → Continue weaning to off as MAP tolerates ≥65; reassess fluid status (net positive, avoid further large positive balance).
RESP: Pneumonia/early sepsis-related; oxygenation good (P/F ~230 on FiO2 0.4). → Wean FiO2 toward 0.3; perform spontaneous breathing trial today given improving picture and low pressor requirement; if passes and mentating off sedation, extubate.
GI/NUTRITION: Enteral feeds started and tolerated. → Advance to goal rate; continue.
RENAL/FLUIDS/LYTES: AKI improving with resuscitation; UOP up. → Target even-to-net-negative balance now that shock resolving; continue electrolyte repletion.
HEME: Stable. → Continue VTE prophylaxis (enoxaparin/SCDs).
ID: CAP with septic shock; sputum gram-positive cocci. → Continue ceftriaxone + azithromycin; narrow per culture/sensitivities when finalized; blood cultures pending; plan 5–7 day course; reassess azithromycin once atypicals excluded.
ENDO: Glucose 150s. → Insulin protocol, target 140–180.

DAILY GOALS CHECKLIST:
- Sedation target/awakening: RASS −1 to 0; awakening trial this AM.
- SBT candidacy: yes — perform today.
- Lines to remove: reassess arterial line and central line need as pressors wean off.
- VTE prophylaxis: enoxaparin. / GI prophylaxis: PPI while intubated.
- Nutrition: enteral, advancing to goal. / Glycemic target: 140–180.
- Mobility: out of bed/PT once extubated.
- Code status/goals: full code; confirm with family.
```
