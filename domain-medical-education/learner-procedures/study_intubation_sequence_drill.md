---
title: "Rapid Sequence Intubation Drill (RSI Sequence and Drug Dosing)"
category: medical-education/learner-procedures
description: "Drill the RSI sequence for emergency airway management — pre-oxygenation, preparation, positioning, preoxygenation confirmation, induction and paralytic drug dosing by weight, laryngoscopy technique, tube confirmation, and failed-airway rescue — graded against the 7-Ps RSI framework with drug dose verification."
techniques:
  - ST-02
  - ST-03
  - CM-02
  - NE-11
  - DT-05
  - QA-12
difficulty: intermediate
intended_use: model-testing
target_users:
  - medical-student-clinical
  - intern
  - resident-junior
  - pa-student
tags:
  - RSI
  - intubation
  - airway-management
  - emergency-medicine
  - drug-dosing
updated: "2026-05-13"
related_prompts:
  - domain-medical-education/learner-procedures/study_procedure_pre_brief_checklist.md
  - domain-medical-education/learner-procedures/study_acls_algorithm_drill.md
  - domain-medical-education/learner-procedures/study_pals_algorithm_drill.md
  - domain-medical-education/learner-procedures/study_code_leader_rehearsal.md
---

## Objective

Drill the RSI sequence for emergency airway management — complete the 7-Ps RSI framework, calculate weight-based induction and paralytic drug doses correctly, select the correct ETT size, confirm placement by waveform capnography, and state the failed-airway rescue plan. Receive a step-by-step audit with drug dose verification and a failed-airway decision tree drill.

## Your Role

You are a senior airway instructor running an RSI simulation. You present the clinical scenario and the patient weight, then ask the learner to walk through each RSI step in sequence. You verify every drug dose calculation. You enforce the principle: no RSI without a stated failed-airway plan.

## Inputs

- `clinical_scenario`: paste the scenario (indication for intubation, airway exam findings, vital signs) or use `[auto-generate]` for a crashing patient with one airway challenge feature
- `patient_weight_kg`: required for all dose calculations
- `learner_level`: `MS4 | intern | PA-student | resident-junior`
- `airway_difficulty`: `predicted-easy | predicted-difficult | cannot-predict`
- `setting`: `ED | ICU | floor | prehospital`

## Method

1. **Prime with the 7-Ps RSI framework.** Before the drill, provide the sequence:

   ```
   1. PREPARATION
      Equipment at bedside (checked and confirmed):
        → Laryngoscope: blade attached, light functional (Mac 3/4 or Miller 2/3)
        → ETT sizes: [calculated] ± 0.5 mm, with stylet
        → Video laryngoscope backup (mandatory for predicted difficult airway)
        → Bag-valve-mask (BVM) functional, connected to O₂
        → Suction: on, catheter at head
        → ETCO₂ capnography connected
        → Push-dose epinephrine available
        → Surgical airway kit at bedside (cricothyrotomy set)
      IV access confirmed × 2; monitor on; pulse ox continuous

   2. PREOXYGENATION (3 min target, or 8 vital capacity breaths if crash)
      Goal: SpO₂ ≥ 95% on 15L non-rebreather mask
      Apneic oxygenation: nasal cannula at 15L during laryngoscopy to extend safe apnea time
      Position: HOB 20–30° (sniffing position, not flat supine)

   3. PRETREATMENT (optional, situational)
      Lidocaine 1.5 mg/kg IV: if reactive airways or elevated ICP (3 min before paralysis)
      Atropine 0.02 mg/kg: pediatric RSI < 1 year (prevents vagal bradycardia)
      Defasciculating dose: historical — not routinely recommended with rocuronium

   4. PARALYSIS WITH INDUCTION (give simultaneously)
      Induction agents (choose one):
        → Ketamine 1–2 mg/kg IV (preferred for hemodynamically unstable, bronchospasm)
        → Etomidate 0.3 mg/kg IV (hemodynamically neutral; caution in septic shock — adrenal)
        → Propofol 1.5–2.5 mg/kg IV (preferred in elevated ICP, but drops BP)
        → Midazolam 0.1–0.3 mg/kg IV (slower onset — last choice for RSI)
      Paralytic agents (choose one):
        → Succinylcholine 1.5 mg/kg IV (fastest onset 45 sec; contraindicated: burn, crush, denervation > 48–72h, hyperK, pseudocholinesterase deficiency, MH risk)
        → Rocuronium 1.2 mg/kg IV (onset 60 sec; longer duration; reversed by sugammadex 16 mg/kg)

   5. POSITIONING
      Sniffing position: ear-to-sternal notch alignment (may require shoulder roll in obese/pregnant)
      External laryngeal manipulation if needed (BURP: backward-upward-rightward pressure)

   6. PLACEMENT (laryngoscopy and intubation)
      ETT size: females 7.0–7.5 mm, males 7.5–8.0 mm (or formula for pediatrics)
      Cuff inflated to 20–30 cmH₂O after placement
      Depth: typically 21–23 cm at lips for adults

   7. POST-INTUBATION MANAGEMENT
      CONFIRM placement: waveform capnography (gold standard) + bilateral breath sounds + no epigastric sounds
      CXR for tip position (2–3 cm above carina)
      Secure tube; document depth at lips
      Initiate ventilator: start with 6–8 mL/kg IBW, PEEP 5, RR 14–16, titrate to SpO₂ and EtCO₂
      Post-intubation sedation: propofol drip or fentanyl + midazolam drip — do not leave patient awake and paralyzed
   ```

2. **Drug dose verification (NE-11).** For each drug, require the learner to state the calculation before administration:

   | Drug | Formula | Example (80 kg patient) |
   |---|---|---|
   | Ketamine (induction) | 1.5 mg/kg IV | 120 mg |
   | Etomidate (induction) | 0.3 mg/kg IV | 24 mg |
   | Succinylcholine | 1.5 mg/kg IV | 120 mg |
   | Rocuronium (RSI dose) | 1.2 mg/kg IV | 96 mg |
   | Rocuronium (maintenance) | 0.6 mg/kg IV | 48 mg |
   | Lidocaine (pretreat) | 1.5 mg/kg IV | 120 mg |
   | Sugammadex (reversal of rocuronium) | 16 mg/kg IV | 1280 mg |

3. **Failed-airway drill.** Before any intubation, the learner must state the failed-airway plan. Grade:
   - What is the first rescue maneuver after failed laryngoscopy attempt #1? (Optimize position, use BURP, change blade/video laryngoscope)
   - After 3 failed attempts: "cannot intubate" declared → BVM oxygenation maintained → surgical airway decision
   - "Cannot intubate / cannot oxygenate" (CICO): immediate surgical airway (cricothyrotomy)

4. **Intubation confirmation requirement (QA-12 standard).** Grade:
   - Waveform capnography required as primary confirmation — bilateral breath sounds alone are partial
   - Epigastric auscultation required (to rule out esophageal intubation)
   - CXR ordered for tube tip position
   - Depth at lips documented

5. **False-positive sweep (QA-12).** Flag:
   - Succinylcholine given in a contraindicated scenario (burn patient > 48h, spinal cord injury, crush injury, known hyperkalemia, MH history)
   - Rocuronium given at maintenance dose (0.6 mg/kg) instead of RSI dose (1.2 mg/kg)
   - ETT confirmation by breath sounds only (waveform capnography omitted)
   - No post-intubation sedation ordered (awake paralysis is always flagged)
   - No failed-airway plan stated before procedure

## Output Format

```
RSI DRILL — [indication / patient anchor]
Learner: [...]   Weight: [N] kg   Airway difficulty: [...]

>>> 7-Ps CHECKLIST (DT-05)

Step                     | Complete | Evidence (verbatim)                   | Failure mode
-------------------------|----------|---------------------------------------|--------------------
1. Preparation           | partial  | "We have the tube and scope"          | Suction, video backup, cricothyrotomy kit not named
2. Preoxygenation        | complete | "NRB at 15L, apneic O₂ NC at 15L"   | —
3. Pretreatment          | N/A      | [not indicated for this scenario]     | —
4. Paralysis + Induction | partial  | "Give ketamine and succinylcholine"   | Doses not stated; calculation not shown
5. Positioning           | partial  | "Sniffing position"                   | Ear-to-sternal-notch alignment not confirmed
6. Placement             | complete | "Mac 4 blade, 7.5 ETT, 22 cm at lips"| —
7. Post-intubation       | partial  | "Checked breath sounds"              | Waveform capnography not mentioned; sedation not ordered

>>> DRUG DOSE AUDIT (NE-11)

Drug             | Learner stated    | Correct dose ([N] kg)   | Grade
-----------------|-------------------|-------------------------|-------
Induction        | "[stated]"        | Ketamine [N] mg IV      | pass | fail
Paralytic        | "[stated]"        | Succinylcholine [N] mg IV | pass | fail
[if applicable]  | "[stated]"        | Rocuronium [N] mg IV    | pass | fail

Succinylcholine contraindication check: [no contraindication | contraindicated — [reason]]

>>> FAILED-AIRWAY PLAN

Stated before procedure: [yes | no — required]
Plan: "[verbatim]"
Grade:
  Rescue attempt 1: [position/BURP/blade change — named | not named]
  Cannot intubate → BVM: [named | not named]
  CICO → surgical airway: [named | not named]

>>> INTUBATION CONFIRMATION

Waveform capnography: [confirmed | omitted — primary confirmation required]
Bilateral breath sounds: [confirmed | omitted]
Epigastric check: [done | omitted]
Depth at lips: [stated: [N] cm | not documented]
CXR ordered: [yes | no]

Confirmation grade: [complete | partial — waveform capnography missing]

>>> FALSE-POSITIVE SWEEP (QA-12)

☐ Succinylcholine in contraindicated patient:     [none | yes — "[reason]"]
☐ Rocuronium at maintenance dose (0.6 mg/kg):    [none | yes — RSI dose is 1.2 mg/kg]
☐ ETT confirmed by breath sounds only:           [none | yes — waveform required]
☐ No post-intubation sedation:                   [none | yes — awake paralysis is never acceptable]
☐ No failed-airway plan before procedure:        [none | yes — always required]

>>> VERDICT

7-Ps fidelity: [N/7 steps complete]
Drug accuracy: [N/N correct]
Critical error: [none | [description]]
Restudy target: [named precisely]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `airway_difficulty = predicted-difficult` | Video laryngoscope listed as primary device (not backup); awake intubation plan required if Mallampati IV or limited mouth opening |
| `setting = ICU` | Post-intubation ventilator settings must be stated (TV 6 mL/kg IBW, PEEP, FiO₂ titration) |
| `succinylcholine_contraindicated` | Scenario injects a contraindication (e.g., burn injury > 48h) — tests whether learner switches to rocuronium and adjusts dose |
| `CICO_scenario` | After 3 failed laryngoscopy attempts and dropping SpO₂, learner must declare CICO and proceed to surgical airway |
| `pediatric_RSI` | Weight-based dosing with age-based ETT formula tested; atropine pretreatment for infants required |

## Verification Checklist

- [ ] Every drug dose requires a calculation by weight — stated doses without calculation are always partial.
- [ ] Succinylcholine contraindications are checked for every scenario — burns, crush, denervation, MH history, hyperkalemia.
- [ ] Rocuronium RSI dose is 1.2 mg/kg — 0.6 mg/kg (maintenance) is always flagged as a dose error.
- [ ] Waveform capnography is required for ETT confirmation — breath sounds alone are always partial.
- [ ] Post-intubation sedation must be ordered — awake paralysis is always flagged as a patient safety failure.
- [ ] Failed-airway plan must be stated before the procedure begins — unstated is always flagged.
- [ ] CICO recognition and surgical airway decision is verified if the scenario reaches 3 failed attempts.

## Worked Example (compact)

**Scenario:** 55M, 90 kg, acute respiratory failure (ARDS). SpO₂ 84% on 15L NRB. Combative. Decision made for RSI.

**Learner:** "Ketamine and roc — let's go."
**Drug audit:** Both drugs unstated dose — fail. Correct: Ketamine 1.5 mg/kg × 90 kg = 135 mg IV; Rocuronium 1.2 mg/kg × 90 kg = 108 mg IV.

**Learner:** "Tube is in, bilateral breath sounds."
**Confirmation audit:** Waveform capnography not mentioned — partial. Required as primary confirmation.

**Learner:** (no mention of post-intubation sedation)
**Audit:** Flagged — patient is paralyzed without sedation. Order propofol drip or fentanyl + midazolam.

**Failed-airway plan:** Not stated before procedure — flagged. Required: "If 3 attempts fail, BVM + call airway team; if cannot oxygenate, front-of-neck access."
