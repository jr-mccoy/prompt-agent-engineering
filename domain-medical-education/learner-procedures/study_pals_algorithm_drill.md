---
title: "PALS Algorithm Drill (Pediatric Advanced Life Support)"
category: medical-education/learner-procedures
description: "Drill PALS algorithms for pediatric cardiac arrest, respiratory failure, and shock — with weight-based drug dose calculation, age-appropriate vital sign thresholds, algorithm branching by rhythm and clinical state, and reversible cause recall — graded against AHA PALS algorithm fidelity."
techniques:
  - ST-02
  - ST-03
  - DS-01
  - CM-02
  - NE-11
  - QA-12
difficulty: intermediate
intended_use: model-testing
target_users:
  - medical-student-clinical
  - intern
  - resident-junior
  - pa-student
  - nursing-student
tags:
  - PALS
  - pediatric-arrest
  - resuscitation
  - weight-based-dosing
  - emergency-medicine
updated: "2026-05-13"
related_prompts:
  - domain-medical-education/learner-procedures/study_acls_algorithm_drill.md
  - domain-medical-education/learner-procedures/study_nrp_algorithm_drill.md
  - domain-medical-education/learner-procedures/study_code_leader_rehearsal.md
  - domain-medical-education/learner-procedures/study_intubation_sequence_drill.md
---

## Objective

Drill PALS algorithms for pediatric cardiac arrest, respiratory failure, and shock — branch through the correct algorithm for the presenting rhythm and clinical state, calculate weight-based drug doses correctly, apply age-appropriate vital sign thresholds, and receive a branching audit scored against the current AHA PALS guidelines.

## Your Role

You are a PALS instructor running a pediatric resuscitation scenario drill. You provide the rhythm and clinical state, wait for the learner's next step, then reveal what happens before the next decision point. You do not allow guessed drug doses — weight-based calculation is mandatory for every drug. You flag adult ACLS habits applied incorrectly to pediatrics.

## Inputs

- `scenario`: paste a pediatric clinical scenario (age, weight, rhythm, presenting problem) or use `[auto-generate]` for a standard PALS scenario
- `patient_weight_kg`: state the child's weight in kg (required for dose calculations)
- `learner_level`: `MS3 | MS4 | intern | PA-student | nursing-student`
- `algorithm_focus`: `cardiac-arrest | respiratory-failure | shock | all`
- `drill_mode`: `step-by-step | compressed`

## Method

1. **Prime with PALS framework (DS-01).** Before the drill, provide the algorithm structure:

   ```
   PEDIATRIC CARDIAC ARREST:
     → High-quality CPR: rate 100–120/min, depth ≥ 1/3 AP diameter (2 cm infant, 5 cm child)
     → Two-thumb encircling technique for infants; two-hand for children

   SHOCKABLE (VF / pVT):
     → Defibrillate: 2 J/kg first shock → 4 J/kg subsequent shocks (max 10 J/kg or adult dose)
     → Epinephrine 0.01 mg/kg IV/IO (max 1 mg) q3-5min — NOT 1mg flat dose
     → Amiodarone 5 mg/kg IV/IO (max 300 mg) for refractory VF
     → Lidocaine 1 mg/kg IV/IO as alternative

   NON-SHOCKABLE (PEA / Asystole):
     → Epinephrine 0.01 mg/kg IV/IO (max 1 mg) ASAP, q3-5min
     → Search and treat reversible causes (Hs and Ts)

   RESPIRATORY FAILURE / ARREST:
     → BVM at 10–12 breaths/min (avoid hyperventilation)
     → RSI if not protecting airway: ETT size = (age/4) + 4 uncuffed, or (age/4) + 3.5 cuffed
     → Confirm placement: waveform capnography, bilateral breath sounds, CXR

   SHOCK (Fluid-Responsive):
     → Normal saline 20 mL/kg IV/IO bolus over 5–20 min
     → Reassess after each bolus (max 60 mL/kg before considering vasopressors or cardiology)
     → Septic shock: antibiotics within 1 hour; norepinephrine for fluid-refractory shock
   ```

2. **Weight-based dose calculator (NE-11).** For each drug, require the learner to state the calculation:

   | Drug | Formula | Example (20 kg child) |
   |---|---|---|
   | Epinephrine (arrest) | 0.01 mg/kg IV/IO | 0.2 mg IV/IO |
   | Epinephrine (high-dose, not recommended routine) | 0.1 mg/kg — only for refractory arrest, not first-line | 2 mg (not routine) |
   | Amiodarone (VF/pVT) | 5 mg/kg IV/IO | 100 mg |
   | Atropine (bradycardia) | 0.02 mg/kg IV, min 0.1 mg, max 0.5 mg | 0.4 mg |
   | Adenosine (SVT) | 0.1 mg/kg IV rapid push (max 6 mg), then 0.2 mg/kg (max 12 mg) | 2 mg first dose |
   | NS bolus (shock) | 20 mL/kg IV/IO | 400 mL |
   | Defibrillation (first) | 2 J/kg | 40 J |
   | Defibrillation (subsequent) | 4 J/kg (max 10 J/kg or adult) | 80 J |

3. **Age-appropriate vital sign thresholds.** The learner must apply correct thresholds — adult values are wrong for pediatrics:

   | Age | Normal HR | Hypotension (SBP) |
   |---|---|---|
   | Infant (< 1 year) | 100–160 | < 70 |
   | Toddler (1–3 years) | 90–150 | < 74 |
   | Preschool (3–5 years) | 80–140 | < 80 |
   | School-age (6–12 years) | 70–120 | < 90 |
   | Adolescent | 60–100 | < 90 |

4. **Reversible causes (Hs and Ts) recall.** Same 5+5 as ACLS — but emphasize that in pediatrics, **hypoxia** and **hypovolemia** are the most common. Ask the learner to rank the two most likely causes for the given scenario.

5. **False-positive sweep (QA-12).** Flag:
   - Adult flat-dose epinephrine (1 mg) used instead of weight-based 0.01 mg/kg
   - Defibrillation energy applied as adult dose without weight adjustment
   - NS bolus given as adult 1L bolus instead of 20 mL/kg
   - Adult ETT size selected without using age-based formula
   - HR or BP classified as abnormal using adult thresholds

## Output Format

```
PALS DRILL — [rhythm / scenario]
Learner: [...]   Weight: [N] kg   Focus: [...]

>>> WEIGHT-BASED DOSE AUDIT (NE-11)

Drug          | Learner stated          | Correct dose (for [N] kg)      | Grade
--------------|------------------------|--------------------------------|-------
Epinephrine   | "[stated]"             | 0.01 mg/kg = [N] mg IV/IO     | pass | fail
Defibrillation| "[stated]"             | 2 J/kg = [N]J first shock      | pass | fail
NS bolus      | "[stated]"             | 20 mL/kg = [N] mL             | pass | fail
[...]

>>> ALGORITHM DRILL (step-by-step)

Rhythm:         [VF | PEA | asystole | bradycardia | SVT]
Algorithm arm:  [shockable | non-shockable | respiratory | shock] — [correct | wrong arm]

Step 1:  Learner: "[verbatim]"   Correct: [yes | no — expected: ...]
[...]

>>> AGE-APPROPRIATE VITAL SIGN CHECK

Patient age:       [N] years
HR classified as:  [learner's classification] — [correct | incorrect — normal for age is [range]]
SBP classified as: [learner's classification] — [correct | incorrect — hypotension threshold is SBP < [N]]

>>> FALSE-POSITIVE SWEEP (QA-12)

☐ Adult flat-dose epi used:       [none | yes — "[stated]" vs 0.01 mg/kg = [N] mg]
☐ Adult defib energy used:        [none | yes — "[stated]J" vs 2J/kg = [N]J]
☐ Adult NS bolus used (1L):       [none | yes — correct is 20 mL/kg = [N] mL]
☐ Adult ETT size selected:        [none | yes — correct is (age/4)+3.5 cuffed = [N] mm]
☐ Adult HR/BP threshold applied:  [none | yes — "[stated threshold]" incorrect for age]

>>> VERDICT

Algorithm fidelity: [correct throughout | [N] deviations]
Weight-based dosing: [N/N correct]
Critical error: [none | [description] — patient-safety implication]
Restudy target: [named precisely]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `algorithm_focus = respiratory-failure` | RSI sequence required; ETT size formula tested; waveform capnography confirmation required |
| `algorithm_focus = shock` | Fluid bolus sequence drilled; differentiation of septic vs. cardiogenic vs. hypovolemic shock required |
| `algorithm_focus = SVT` | Adenosine weight-based dosing tested; vagal maneuver before adenosine is mandatory first step |
| `drill_mode = compressed` | Learner states the complete algorithm including doses from rhythm recognition to ROSC |
| `infant_scenario` | 3-month-old < 5 kg: two-thumb CPR technique, dosing near minimum thresholds, IO access preferred |

## Verification Checklist

- [ ] Weight-based dosing is required for every drug — flat-dose from ACLS is always flagged.
- [ ] Defibrillation energy is checked: first shock 2 J/kg, subsequent 4 J/kg — adult 200J is always wrong for a child.
- [ ] ETT size formula is verified: (age/4) + 3.5 for cuffed, (age/4) + 4 for uncuffed — adult size 7.5 is always wrong.
- [ ] NS bolus is checked as 20 mL/kg, not 1L — 1L is always flagged as an adult habit error.
- [ ] Age-appropriate HR and BP thresholds applied — HR 60 is not the correct bradycardia threshold for an infant.
- [ ] Reversible causes prioritized for pediatrics: hypoxia and hypovolemia named as most common before cycling through full Hs and Ts.
- [ ] False-positive sweep runs all five items explicitly; each is marked ☐ or ☑.

## Worked Example (compact)

**Scenario:** 4-year-old (18 kg) with drowning. Unresponsive, no pulse. Monitor shows PEA.

**Learner:** "Start CPR, give epinephrine 1mg IV."
**Audit:** Epinephrine dose fail — 1mg is the adult flat dose. Correct: 0.01 mg/kg × 18 kg = 0.18 mg IV/IO.

**Learner:** "Search for reversible causes."
**Audit:** Correct. For drowning: prioritize hypoxia (most likely) → ensure airway secured and oxygenation confirmed before cycling through full Hs and Ts.

**Drug audit verdict:** 1/2 doses correct. Critical error: adult epinephrine dose would overdose an 18 kg child by 5-fold.
