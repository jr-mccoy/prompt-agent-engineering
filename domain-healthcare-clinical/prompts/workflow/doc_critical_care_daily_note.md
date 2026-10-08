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

## False-Positive Prevention

❌ **DON'T:**
- Populate Lines/tubes/drains, code status, prophylaxis agents or "afebrile" from what an ICU patient usually has — a central line, arterial line or Foley that was not in today's input becomes a line-day and CLABSI/CAUTI audit error.
- Advance line days and antibiotic day by incrementing yesterday's note instead of counting from a dated start; an off-by-one antibiotic day mis-times the stop date.
- Write "AKI improving", "Cr improving" or "K repleted" when only one value or no value was supplied — a trajectory needs two dated values.
- Mark a DAILY GOALS item "yes" (SBT candidacy, lines to remove) when the criteria behind it — FiO2/PEEP, vasopressor dose, mental status off sedation — were not in the input.

✅ **DO:**
- Recompute every derived number from its inputs and show it: P/F = PaO2 ÷ FiO2 (as a fraction), net balance = in − out, weight-based drip rate in the stated units (mcg/kg/min vs mcg/min); with a metabolic acidosis on the ABG, check the PaCO2 against Winter's formula (1.5 × HCO3 + 8 ± 2) before writing "compensated".
- Check that every drip in OBJECTIVE carries agent, rate and units and reappears in its system's plan with a direction (wean, titrate, stop, continue).
- List every culture or result still pending in the ID (or relevant system) plan together with what will change when it returns; count pending items in the input and in the note.

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

**Input:** ICU Day 2, septic shock from pneumonia, intubated. Overnight: weaning norepinephrine, lactate cleared 4.2 → 1.6, started enteral feeds (tolerating), no other events. Vitals Tmax 37.6, MAP 70–78, HR 88–96. Norepinephrine down to 0.04 mcg/kg/min, propofol 25 mcg/kg/min. Vent: AC/VC, set RR 18, FiO2 0.4, PEEP 8, Vt 6 mL/kg, last ABG 7.36/40/92. Not yet assessed off sedation. UOP improving, net +1.2L. Cr 1.9 yesterday → 1.5 today; K 3.4 yesterday, repleted, 4.0 today. WBC 14 down from 19; Hgb and platelets unchanged from yesterday. Cultures: blood pending, sputum gram-positive cocci. On ceftriaxone+azithromycin day 2. Glucose 150s. Lines (all placed ICU day 1): right IJ central line, arterial line, ETT, Foley. Prophylaxis: enoxaparin, PPI. Code status: full code per family; family meeting planned.

**Output:**

```
ICU Progress Note — ICU Day 2
ONE-LINER: Adult with septic shock secondary to community-acquired pneumonia, intubated/ventilated, improving — vasopressor weaning, lactate cleared.

24-HOUR EVENTS:
Hemodynamically improving overnight with successful down-titration of norepinephrine. Lactate cleared from 4.2 to 1.6. Enteral nutrition initiated and tolerated. No new fevers or events.

OBJECTIVE:
- Vitals: MAP 70–78, HR 88–96, Tmax 37.6.
- Drips: norepinephrine 0.04 mcg/kg/min (weaning); propofol 25 mcg/kg/min.
- Vent: AC/VC, FiO2 0.40, PEEP 8, Vt 6 mL/kg (lung-protective), RR set 18. ABG 7.36/40/92.
- I/O: net +1.2 L over 24h; urine output improving.
- Labs: WBC 14 (down from 19), lactate 1.6 (cleared from 4.2), Cr 1.5 (from 1.9), K 4.0 after repletion (from 3.4), Hgb/platelets unchanged.
- Lines/tubes/drains: right IJ central line (day 2), arterial line (day 2), ETT, Foley.
- Antibiotics: ceftriaxone + azithromycin, day 2.

ASSESSMENT & PLAN (by system):
NEURO: Sedated on propofol, target RASS −1 to 0. → Begin daily sedation awakening trial this morning; assess for extubation readiness; CAM-ICU screen.
CV: Septic shock resolving, norepinephrine weaning. → Continue weaning to off as MAP tolerates ≥65; reassess fluid status (net positive, avoid further large positive balance).
RESP: Pneumonia/early sepsis-related; oxygenation good (P/F ~230 on FiO2 0.4). → Wean FiO2 toward 0.3; screen for spontaneous breathing trial after this morning's awakening trial (FiO2 0.4/PEEP 8 and low-dose norepinephrine recorded; mental status off sedation not yet assessed); if SBT passed and mentating off sedation, extubate.
GI/NUTRITION: Enteral feeds started and tolerated. → Advance to goal rate; continue.
RENAL/FLUIDS/LYTES: AKI improving with resuscitation (Cr 1.9 → 1.5); UOP up. → Target even-to-net-negative balance now that shock resolving; continue electrolyte repletion.
HEME: Hgb/platelets unchanged. → Continue VTE prophylaxis (enoxaparin).
ID: CAP with septic shock; sputum gram-positive cocci. → Continue ceftriaxone + azithromycin; narrow per culture/sensitivities when finalized; blood cultures pending; plan 5–7 day course; reassess azithromycin once atypicals excluded.
ENDO: Glucose 150s. → Insulin protocol, target 140–180.

DAILY GOALS CHECKLIST:
- Sedation target/awakening: RASS −1 to 0; awakening trial this AM.
- SBT candidacy: screen after awakening trial — mental status off sedation not yet assessed.
- Lines to remove: reassess arterial line and central line need as pressors wean off.
- VTE prophylaxis: enoxaparin. / GI prophylaxis: PPI while intubated.
- Nutrition: enteral, advancing to goal. / Glycemic target: 140–180.
- Mobility: out of bed/PT once extubated.
- Code status/goals: full code per family; family meeting planned.
```
