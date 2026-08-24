---
title: "ARDS Management"
category: domain-healthcare-clinical/acute-care
description: "Manage acute respiratory distress syndrome with lung-protective ventilation, PEEP titration, prone positioning, paralysis, and ECMO escalation."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - critical-care
  - ards
  - mechanical-ventilation
  - ecmo
updated: "2026-05-08"
---

## Objective

Manage a patient with ARDS using lung-protective ventilation, PEEP titration, prone positioning, neuromuscular blockade, and rescue therapies. Output names ventilator targets, PEEP-FiO2 selection, prone criteria, and ECMO escalation triggers.

## Inputs

- Berlin criteria confirmation: acute onset (≤7 days), bilateral opacities not from cardiogenic edema or fluid overload, P/F ratio on PEEP ≥5
- Severity: mild (P/F 200–300), moderate (P/F 100–200), severe (P/F <100)
- Ventilator data: Vt, RR, PEEP, FiO2, Pplat, driving pressure, compliance
- Patient: PBW, hemodynamics, RV function on echo, fluid balance
- Etiology: pneumonia (bacterial, viral, fungal), aspiration, sepsis, pancreatitis, transfusion (TRALI), drug, near-drowning

## Reasoning Steps

1. **Confirm ARDS and stage severity.**
   - Berlin: bilateral opacities not explained by effusions/atelectasis/nodules; not primarily cardiogenic (echo / clinical / wedge if available); P/F ≤300 on PEEP ≥5.
   - Mild 200–300; moderate 100–200; severe <100.

2. **Lung-protective ventilation.**
   - Vt 6 mL/kg PBW (4–8 range; lower for high Pplat/DP).
   - RR 18–28 to maintain reasonable minute ventilation; permissive hypercapnia accepted (pH ≥7.20).
   - Pplat <30 cmH2O.
   - Driving pressure (Pplat − PEEP) <15 cmH2O — strongest mortality predictor.
   - FiO2 titrated to SpO2 88–95%.

3. **PEEP titration.**
   - **ARDSNet PEEP-FiO2 tables.** Lower-PEEP table for mild ARDS, higher-PEEP table for moderate-severe.
     - Higher-PEEP table examples: FiO2 0.4 → PEEP 10; FiO2 0.6 → PEEP 14; FiO2 0.8 → PEEP 16; FiO2 1.0 → PEEP 18–24.
   - **Best-PEEP titration:** find PEEP that maximizes compliance or minimizes driving pressure at the same Vt.
   - **PEEP and hemodynamics:** higher PEEP raises intrathoracic pressure → reduces preload → may drop BP. Echo for RV strain.

4. **Conservative fluid strategy.**
   - FACTT trial: conservative fluid (target CVP <4 or PCWP <8 if measured) reduces ventilator days and ICU time without increasing AKI or shock.
   - Diurese as tolerated once hemodynamically stable; avoid net positive fluid balance.

5. **Sedation, analgesia, paralysis.**
   - Adequate sedation and analgesia first (RASS −3 to −4 initially; lighter as tolerated).
   - **Neuromuscular blockade (cisatracurium 48 hours)** for severe ARDS (P/F <150) with persistent dyssynchrony despite deep sedation. ACURASYS showed mortality benefit; ROSE trial mixed results — current practice individualized to those with refractory dyssynchrony or prone-positioning facilitation.

6. **Prone positioning.**
   - **Indication: P/F <150 on FiO2 ≥0.6 and PEEP ≥5** despite optimization.
   - **Duration: ≥16 hours/day** (PROSEVA mortality benefit).
   - Continue until P/F >150 in supine for at least 4 hours.
   - Mechanism: improves V/Q matching, reduces dorsal atelectasis, redistributes pulmonary blood flow, reduces ventilator-induced lung injury.
   - Risks: pressure injury (face, chest, knees — pad and rotate), accidental extubation, line/tube dislodgement, transient desaturation during turn.

7. **Rescue therapies for refractory hypoxemia.**
   - **Inhaled pulmonary vasodilator** (iNO 20–40 ppm or inhaled epoprostenol): improves oxygenation acutely; no mortality benefit. Bridge to other therapy.
   - **Recruitment maneuvers:** sustained inflation (e.g., 40 cmH2O for 40 sec) or stepwise PEEP increase. Mixed evidence; ART trial showed harm with aggressive recruitment + decremental PEEP. Use selectively.
   - **VV-ECMO:** EOLIA trial. Indications:
     - P/F <80 for >6 h despite optimization.
     - Refractory hypercapnia with pH <7.25 despite RR 35 and Pplat ≤32.
     - Failure of prone positioning, paralysis, optimal PEEP.
   - Refer/transport to ECMO center early — outcomes worse with delayed referral.

8. **Identify and treat the underlying cause.**
   - Bacterial pneumonia: appropriate antibiotics; bronchoscopy if not improving.
   - Viral (influenza, COVID, RSV): antiviral if applicable; supportive.
   - Sepsis: source control, antibiotics, hemodynamic support.
   - Aspiration: airway clearance, reasonable empiric antibiotics if witnessed massive aspiration with infiltrate (anaerobic coverage debated).
   - TRALI: stop transfusion; supportive only.
   - Pancreatitis: source treatment, fluid management.
   - Steroids:
     - **COVID ARDS:** dexamethasone 6 mg daily × 10 days (RECOVERY).
     - **General ARDS:** dexamethasone 20 mg daily × 5 days then 10 mg × 5 days (DEXA-ARDS) showed benefit. Methylprednisolone protocols also studied.
     - **Avoid late steroids** beyond day 14 (LaSRS).

9. **Daily reassessment and weaning.**
   - Daily SAT (sedation hold) and SBT (spontaneous breathing trial) when safe.
   - Wean FiO2 first as oxygenation improves, then PEEP cautiously.
   - Liberation criteria: P/F >200 on PEEP ≤8 and FiO2 ≤0.5 with stable Pplat.

10. **Long-term considerations.**
    - PICS (post-ICU syndrome): physical, cognitive, mental health.
    - ICU-acquired weakness: minimize paralytic duration, early mobility when feasible.
    - Pulmonary follow-up post-discharge for residual fibrosis, exercise capacity.

## Output Format

```
ARDS SEVERITY: [Berlin classification, P/F]
ETIOLOGY: [identified cause]

VENT SETTINGS:
- Mode: VC-AC
- Vt: 6 mL/kg PBW = [number] mL
- RR: [number]
- PEEP: [from PEEP-FiO2 table or titrated]
- FiO2: [%, with target SpO2]
- Pplat target: <30
- Driving pressure target: <15

FLUID STRATEGY:
- Conservative; net negative balance once stable

SEDATION / PARALYSIS:
- [RASS target, agents]
- Cisatracurium [criteria]

PRONE POSITIONING:
- [Yes/no, duration, criteria for return to supine]

ETIOLOGIC TREATMENT:
- [antibiotics / antivirals / steroids per cause]

RESCUE / ESCALATION:
- iNO or inhaled epoprostenol [criteria]
- VV-ECMO [criteria, transfer]

WEANING:
- Daily SAT/SBT
- FiO2 then PEEP wean once P/F >200

MONITORING:
- ABG q4–8h
- Daily POCUS for RV
- Driving pressure every setting change
```

## Worked Example

**Input:** Day 2 in the ICU. 45 y/o M, 178 cm, intubated for severe COVID-19 ARDS. Currently: VC-AC, Vt 410 mL (6 mL/kg PBW 68 kg), RR 22, PEEP 12, FiO2 80%. Pplat 28, driving pressure 16. ABG: pH 7.27, PaCO2 56, PaO2 58, HCO3 25. P/F 73. Hemodynamics stable on no pressors. Echo: normal LV, mildly dilated RV with preserved function.

**Output:**

```
ARDS SEVERITY: Severe (P/F 73, Berlin severe).
ETIOLOGY: COVID-19 viral pneumonitis with ARDS.

VENT SETTINGS (current → adjusted):
- Mode: VC-AC (continue).
- Vt: 410 mL = 6 mL/kg PBW. Driving pressure 16 (above target). Reduce Vt to 5 mL/kg PBW = 340 mL; recheck Pplat and DP.
- RR: increase to 26 to maintain minute ventilation as Vt drops; permissive hypercapnia acceptable to pH 7.20.
- PEEP: increase to 14–16 per ARDSNet higher-PEEP table at FiO2 0.8. Reassess driving pressure at higher PEEP — if DP improves with higher PEEP, that PEEP is recruitable; if DP worsens, that PEEP is overdistention.
- FiO2: target SpO2 88–94%, accept lower-end target to limit oxygen toxicity.
- Pplat target: <30 (currently 28; closer to limit at higher PEEP — drives Vt reduction).
- Driving pressure target: <15.

FLUID STRATEGY:
- Conservative. Net negative balance ~500–1000 mL/day if hemodynamically stable; furosemide 20–40 mg IV q6–8h or infusion.
- Avoid further crystalloid; trend BUN/Cr.

SEDATION / PARALYSIS:
- Currently RASS −3 to −4; assess for ventilator dyssynchrony.
- Cisatracurium 48-hour infusion (load 0.15 mg/kg, infusion 1–10 mcg/kg/min titrated to TOF 0–2/4) IF persistent dyssynchrony despite optimal sedation, OR to facilitate prone positioning.
- Train-of-four monitoring; daily holiday from paralysis when possible to reassess.

PRONE POSITIONING:
- Indicated. P/F 73 <150 on FiO2 0.8 ≥0.6 and PEEP ≥5.
- Initiate prone positioning for ≥16 hours/day (PROSEVA protocol).
- Pre-prone: secure ETT, all lines, eye protection, foley, padding (face, chest, iliac crests, knees, dorsum of feet). Anticipate transient desaturation during turn.
- Continue until P/F >150 in supine for at least 4 hours.

ETIOLOGIC TREATMENT:
- Dexamethasone 6 mg daily × 10 days (RECOVERY trial benefit in oxygen-requiring COVID-19; continues in mechanical ventilation).
- Tocilizumab 8 mg/kg IV once if elevated CRP and other inflammatory markers (consider per institutional protocol; usually given earlier in course).
- Antiviral (remdesivir) if within 10 days of symptoms and not yet given; less benefit in late mechanically ventilated phase.
- Empiric antibiotics if superimposed bacterial pneumonia suspected (procalcitonin, sputum culture, leukocytosis pattern). Avoid routine antibiotic exposure.
- Anticoagulation: therapeutic for known VTE; prophylactic dose for ARDS without VTE in current evidence. Higher dose has been studied with mixed results in critical COVID.

RESCUE / ESCALATION:
- iNO 20–40 ppm or inhaled epoprostenol if persistent hypoxemia despite prone + paralysis + optimal PEEP. No mortality benefit but useful bridge.
- VV-ECMO criteria triggered if:
  - P/F <80 sustained despite all measures.
  - Refractory hypercapnia pH <7.25 with RR 35 and Pplat ≤32.
  - Cannot achieve lung-protective ventilation.
  Refer to ECMO center now if local center cannot escalate; do not wait for refractory deterioration.

WEANING (anticipate days 7–14):
- Daily SAT and SBT once oxygenation improves.
- Wean FiO2 first; then PEEP slowly.
- Liberation when P/F >200 on PEEP ≤8 and FiO2 ≤0.5, stable Pplat <25, stable hemodynamics, intact mental status.

MONITORING:
- ABG at 30 min after each significant setting change, then q4–6h.
- POCUS q24h: RV function (dilated RV, septal flattening, McConnell's), LV function, pleural effusions, B-lines.
- Driving pressure recorded with every Vt or PEEP change.
- Daily CXR to track infiltrate evolution; CT chest if not improving by day 5–7 to identify barotrauma, abscess, or other process.
- Watch for ARDS-related complications: VAP (microbiologic surveillance), barotrauma (pneumothorax, pneumomediastinum), DVT, ICU-acquired weakness, delirium.

PITFALLS TO AVOID:
- Failing to reduce Vt when driving pressure is high.
- Holding off on prone positioning — high-yield intervention with a learning curve worth investing in.
- Over-recruiting PEEP without checking driving pressure or hemodynamics.
- Liberal fluids — common in early sepsis resuscitation and dragging into the ARDS phase.
- Late or missed escalation to ECMO; refer early.
```
