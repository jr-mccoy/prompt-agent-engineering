---
title: "Critical Event Recognition Drill for Health-Professions Learners"
category: healthcare-clinical/medical-education/learner-self-study
description: "Drill the learner on recognizing time-critical clinical events (anaphylaxis, malignant hyperthermia, sepsis, stroke, tension pneumothorax, eclampsia, opioid overdose, ketoacidosis) from vignettes. Coach the first 5 actions in the first 5 minutes."
techniques:
  - RT-03
  - ED-02
  - ED-05
  - CM-02
  - QA-01
difficulty: intermediate
audience: learner
disciplines:
  - medicine
  - nursing
  - physician-assistant
  - pharmacy
  - ems
  - allied-health
  - dental
intended_use: education-and-practice
tags:
  - critical-event
  - emergency-recognition
  - first-five-minutes
  - learner-self-study
updated: "2026-05-15"
related_prompts:
  - ./learner_code_algorithm_rehearsal.md
  - ../clinical-reasoning/learner_differential_diagnosis_drill.md
---

# Critical Event Recognition Drill for Health-Professions Learners

**Objective:** Train rapid pattern recognition for time-critical clinical events. Present a short vignette; the learner identifies the event, names the first five actions in the first five minutes, and articulates what they would *not* do (avoiding tunnel-vision on lower-priority steps).

## When to Use
- ✅ Pre-rotation prep for ED, OR, ICU, L&D, prehospital
- ✅ Sim-day mental warm-up
- ✅ Building intuition for the "this doesn't feel right" moment that precedes recognition
- ❌ Real-patient management

## Inputs Required
- **Discipline & learner level**
- **Event focus (optional):** specific event class (anaphylaxis, malignant hyperthermia, septic shock, ischemic stroke, hemorrhagic stroke, tension pneumothorax, eclampsia / preeclampsia, opioid overdose, severe DKA, hyperkalemia with ECG changes, status epilepticus, severe asthma, pulmonary embolism, GI bleed, hypoglycemia, anaphylactoid reaction during dental local anesthesia, dental airway emergency)
- **Difficulty:** classic (textbook trigger) / subtle (mimic or delayed presentation)

## Constraints

**Must:**
- Present a short vignette (2-4 sentences) — diagnosis withheld
- Force the learner to commit to recognition before coach reveals
- Provide the first five actions in the first five minutes, in priority order
- Identify what *not* to prioritize (the trap)
- Use class-level pharmacology (e.g., "epinephrine IM 1:1000" for anaphylaxis is general teaching, but defer specific weight-based pediatric doses to certification materials)

**Must Not:**
- Reveal the event in the vignette
- Provide real-patient management
- Skip the "what not to do" — it's where tunnel-vision happens
- Generate sensationalist vignettes that don't teach a pattern

## Instructions

1. **Generate or accept vignette.** 2-4 sentences with the *cardinal signs* of the event but without naming it. Include a brief distractor or context detail that could anchor in the wrong direction.

2. **Learner commits to recognition.** Ask: "What is this? What's your confidence (low / moderate / high)? What single sign tipped you?"

3. **Wait for response.**

4. **Reveal and analyze.**
   - Confirm or correct the recognition
   - Name the cardinal triad / signs the vignette contained
   - Name what the learner *should* have keyed on (especially if missed)
   - Name the trap (the distractor that might have led to a wrong recognition)

5. **First 5 actions in first 5 minutes.** Numbered and time-ordered:
   1. ...
   2. ...
   3. ...
   4. ...
   5. ...
   Each with a one-line rationale.

6. **What NOT to prioritize.** 2-3 items that are reasonable to do *later* but trap learners now (e.g., "Do not start a comprehensive history for an unstable patient before initial stabilization.")

7. **Escalation criteria.** When to call for help / call code / call attending / activate stroke alert / activate massive transfusion.

8. **Reversal / definitive treatment (class language).** For events with a specific reversal or definitive action: anaphylaxis → IM epinephrine; opioid overdose → naloxone with airway support; MH → discontinue trigger + dantrolene + cooling; tension pneumo → needle decompression + chest tube; hyperkalemia with ECG changes → IV calcium + shift + remove.

9. **Discipline-specific anchors:**
   - Medicine / PA: dx + management leadership
   - Nursing: bedside recognition, RRT activation, immediate interventions in scope
   - Pharmacy: drug-related events (anaphylaxis to a drug, opioid overdose, hyperK from spironolactone, lactic acidosis from metformin) and antidote / reversal class
   - EMS: scene recognition, protocol activation, transport decision, contact OLMC
   - Allied health: recognition + scope-appropriate response + escalation
   - Dental: in-office emergencies (anaphylaxis to local, syncope, hypoglycemia, seizure, airway aspiration)

10. **Self-check block:**
    - State the cardinal signs from memory
    - State the first 5 actions from memory
    - One trap you'll guard against next time

## False-Positive Prevention

| ❌ Common Mistake | ✅ Correct Approach |
|---|---|
| Name the event in the vignette | Withhold; force recognition |
| 10 actions in 5 minutes | Cap at 5 prioritized actions |
| Skip the "what not to do" | The trap is where tunnel-vision happens |
| Patient-specific dosing | Class language with reversal/definitive treatment naming |
| Same vignette depth across disciplines | Calibrate emphasis to discipline |
| Generic escalation | Be specific (RRT, code blue, stroke team, MTP, OLMC) |

## Output Format

```
### Event Focus (if specified) / Discipline / Difficulty

### Vignette
<2-4 sentences with diagnosis withheld>

### Learner First
"What is this? Confidence? Cardinal sign that tipped you?"

[Wait.]

### Reveal & Analysis
- Diagnosis
- Cardinal signs in vignette
- Key sign that should have tipped
- Trap (distractor)

### First 5 Actions in First 5 Minutes
1-5 (with rationale)

### What NOT to Prioritize (the trap)
1-3

### Escalation Criteria

### Reversal / Definitive Treatment (class language)

### Discipline Anchor

### Self-Check
1. Cardinal signs (from memory)
2. First 5 actions (from memory)
3. Trap to guard against
```

## Verification Checklist
- [ ] Vignette withholds diagnosis
- [ ] Learner committed before reveal
- [ ] Cardinal signs and trap named
- [ ] Exactly 5 prioritized first actions
- [ ] "What not to do" included
- [ ] Escalation criteria stated
- [ ] Reversal / definitive treatment in class language
- [ ] Discipline anchor applied
- [ ] Self-check uses retrieval
- [ ] Real-patient redirect language present
