---
title: "Mechanical Ventilation Initial Settings and Adjustment"
category: domain-healthcare-clinical/acute-care
description: "Set initial mechanical ventilator parameters for a specific patient and adjust based on plateau pressure, oxygenation, and ventilation."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - critical-care
  - ventilation
  - ards
  - copd
  - asthma
updated: "2026-05-08"
---

## Objective

Set initial ventilator parameters for an intubated patient and adjust based on observed plateau pressure, driving pressure, oxygenation (P/F), ventilation (PaCO2), and patient-ventilator synchrony. Output is mode + tidal volume + RR + PEEP + FiO2 + I:E with explicit reasoning.

## Inputs

- Indication for intubation (ARDS, hypercapnic respiratory failure, asthma, COPD exacerbation, neuromuscular weakness, airway protection, post-cardiac arrest)
- Patient: height (used for predicted body weight, PBW), sex, weight
- Pre-intubation gas if available (PaO2, PaCO2, pH, FiO2/SpO2)
- Comorbidities: ARDS, obstructive disease, chronic CO2 retention, intracranial pathology, pregnancy
- Hemodynamics (PEEP increases intrathoracic pressure → reduces preload → can drop BP in volume-depleted patients)

## Role

Senior critical care attending or anesthesiologist setting the vent at the bedside post-intubation.

## Reasoning Steps

1. **Calculate predicted body weight (PBW).** Use sex and height — actual weight is irrelevant for tidal volume.
   - Male: PBW (kg) = 50 + 0.91 × (height_cm − 152.4)
   - Female: PBW (kg) = 45.5 + 0.91 × (height_cm − 152.4)

2. **Choose mode.**
   - **Volume control (VC) / assist-control (AC) volume:** delivers set Vt with each breath. Easiest to enforce lung-protective ventilation. Default for ARDS.
   - **Pressure control (PC):** sets inspiratory pressure; Vt varies with compliance. Useful when peak pressures are problematic or compliance very abnormal.
   - **Pressure support (PS):** patient-triggered; for spontaneously breathing patients during weaning.
   - **SIMV:** rarely chosen first-line; weaning use only.

3. **Set tidal volume (Vt).**
   - **ARDS or any acute lung injury:** 6 mL/kg PBW (range 4–8 mL/kg, lower if high plateau).
   - **Healthy lungs (e.g., post-anesthesia, neurologic indication):** 6–8 mL/kg PBW. Avoid >8 mL/kg routinely; large Vt drives volutrauma even in normal lungs.

4. **Set respiratory rate (RR).**
   - Start at 16–20 for ARDS to compensate for low Vt and maintain minute ventilation.
   - 12–14 for routine indications.
   - Lower (8–12) for severe obstructive disease (asthma, COPD) to allow time for exhalation and prevent breath-stacking / auto-PEEP.

5. **Set PEEP.**
   - **Routine:** start at 5 cmH2O.
   - **ARDS:** higher PEEP per ARDSNet table or lung-protective strategies. Mild ARDS (P/F 200–300): PEEP 8–12. Moderate (P/F 100–200): PEEP 12–16. Severe (P/F <100): PEEP 14–20 with lung recruitment.
   - **Obstructive disease (asthma/COPD):** low PEEP (0–5) to avoid worsening dynamic hyperinflation.
   - **Cardiogenic pulmonary edema:** PEEP 8–12 helps reduce LV transmural pressure (afterload reduction effect).

6. **Set FiO2.**
   - Start 100% post-intubation, titrate down.
   - Target SpO2 92–96% (88–92% in chronic CO2 retainers; lower targets in ARDS to avoid hyperoxic injury, with permissive hypoxemia 88–92% acceptable in severe cases).
   - Avoid prolonged FiO2 >0.6 — oxygen toxicity. Increase PEEP first to allow FiO2 reduction.

7. **Set inspiratory time / I:E ratio.**
   - Default I:E 1:2 for normal lungs.
   - 1:1 or inverse ratio (1:1.5) in ARDS to improve oxygenation (longer inspiratory time for alveolar recruitment).
   - Prolonged expiration (1:3 to 1:5) in obstructive disease to prevent air trapping.

8. **Check plateau pressure (Pplat).** Inspiratory hold on the vent.
   - **Goal Pplat <30 cmH2O** in ARDS. Reflects alveolar pressure.
   - **Driving pressure (DP) = Pplat − PEEP.** Goal <15 cmH2O. Driving pressure has emerged as a stronger mortality predictor than Pplat alone (ARMA reanalysis, Amato et al.).
   - If Pplat >30 or DP >15: reduce Vt to 4–5 mL/kg PBW (permissive hypercapnia acceptable to pH 7.20–7.25).

9. **Check auto-PEEP.** Expiratory hold.
   - Common in obstructive disease with rapid RR or short expiratory time.
   - Manage: reduce RR, increase expiratory time, treat bronchospasm aggressively, suction secretions, accept permissive hypercapnia.

10. **Permissive hypercapnia.** In ARDS or severe obstruction, accept PaCO2 60–80 (or higher) and pH 7.20–7.25 to maintain lung-protective settings. Avoid in raised ICP, severe pulmonary HTN, severe right heart failure, pregnancy.

11. **Adjuncts for severe ARDS.**
   - Prone positioning: 16+ hours/day for P/F <150 (PROSEVA mortality benefit).
   - Neuromuscular blockade (cisatracurium 48 hours): for severe ARDS with patient-vent dyssynchrony despite deep sedation.
   - Recruitment maneuvers: case by case; not routine.
   - Inhaled pulmonary vasodilator (iNO or epoprostenol): rescue for refractory hypoxemia.
   - VV-ECMO: severe ARDS with P/F <80, refractory hypercapnia, or failure of all of the above.

12. **Sedation and analgesia targets.**
   - RASS −2 to 0 ideal; deeper only when needed (paralysis, severe ARDS, raised ICP).
   - Daily SAT (sedation interruption) and SBT (spontaneous breathing trial) when conditions allow.

## Output Format

```
INDICATION: [reason for intubation]
PBW: [calculated kg]

MODE: [VC-AC / PC-AC / PRVC etc.]
Vt: [mL/kg PBW × PBW = mL]
RR: [breaths/min]
PEEP: [cmH2O]
FiO2: [%]
I:E: [ratio]

TARGETS:
- SpO2: [range]
- pH: [range, with permissive hypercapnia if applicable]
- Pplat: <30 cmH2O
- Driving pressure: <15 cmH2O

FIRST 30 MIN ACTIONS:
- ABG at 30 minutes
- Inspiratory hold for Pplat
- Expiratory hold for auto-PEEP if obstructive
- POCUS for pneumothorax / placement check
- CXR for tube position

ESCALATION TRIGGERS:
- [P/F threshold for prone]
- [Vt reduction if Pplat >30]
- [Adjuncts considered]

SEDATION:
- [agent, target RASS]
```

## Worked Example

**Input:** 32 y/o F, 165 cm, 70 kg, just intubated for severe COVID-19 ARDS. Pre-intubation P/F 78 on HFNC 60 L 100%. BP 110/68 on no pressors.

**Output:**

```
INDICATION: Severe ARDS (P/F <100) from COVID-19 pneumonitis.
PBW: 45.5 + 0.91 × (165 − 152.4) = 45.5 + 11.5 = 57 kg.

MODE: Volume control / AC. Lung-protective Vt enforcement is the priority.
Vt: 6 mL/kg PBW × 57 = 342 mL → set 340 mL.
RR: 22 (compensate for low Vt; minute ventilation goal preserves CO2 clearance).
PEEP: 14 cmH2O initially (severe ARDS, ARDSNet higher-PEEP table).
FiO2: 100% start; titrate down to SpO2 88–94% as tolerated.
I:E: 1:1.5 (slightly prolonged inspiratory time for recruitment).

TARGETS:
- SpO2: 88–94% (permissive hypoxemia accepted in severe ARDS).
- pH: 7.25–7.45 (permissive hypercapnia to PaCO2 ~55–65 acceptable for lung protection).
- Pplat: <30 cmH2O.
- Driving pressure: <15 cmH2O (Pplat − PEEP <15 → with PEEP 14, target Pplat <29).

FIRST 30 MIN ACTIONS:
- ABG at 30 minutes; recalculate P/F.
- Inspiratory hold for Pplat. If >30, reduce Vt to 5 then 4 mL/kg PBW; accept rising PaCO2.
- CXR to confirm ETT 3–5 cm above carina; rule out post-intubation pneumothorax.
- Bedside echo: assess RV — severe ARDS frequently produces acute cor pulmonale; high PEEP + permissive hypercapnia raise PVR.
- Calculate driving pressure with each setting change.

ESCALATION TRIGGERS:
- P/F <150 after 12–24 h on optimal settings → prone positioning 16 h/day (PROSEVA).
- Patient-vent dyssynchrony despite RASS −4 → cisatracurium infusion 48 h.
- Refractory hypoxemia despite prone + paralysis → inhaled pulmonary vasodilator (iNO 20 ppm or inhaled epoprostenol).
- Refractory hypoxemia (P/F <80 sustained) or refractory hypercapnia (pH <7.15) → consider VV-ECMO; transfer to ECMO center if not on-site.
- If RV strain develops: lower PEEP cautiously, consider iNO, prone helps RV by reducing PVR.

SEDATION:
- Propofol 20–50 mcg/kg/min initially + fentanyl 50–100 mcg/h. Target RASS −3 to −4 for first 24 h to ensure ventilator synchrony.
- Once stable and synchronous, attempt lighter sedation (RASS −2) and daily SAT.
- If paralysis used, deep sedation (RASS −5) is mandatory.
```
