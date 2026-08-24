---
title: "ATLS Primary and Secondary Survey Drill (Trauma)"
category: medical-education/learner-procedures
description: "Drill the ATLS primary survey (ABCDE), adjuncts, resuscitation priorities, and secondary survey for a trauma patient — with life-threat identification at each step, correct intervention sequence, and a targeted audit for the most common survey omissions and sequence errors."
techniques:
  - ST-02
  - ST-03
  - DS-01
  - CM-02
  - RT-05
  - QA-12
difficulty: intermediate
intended_use: model-testing
target_users:
  - medical-student-clinical
  - intern
  - resident-junior
  - pa-student
tags:
  - ATLS
  - trauma
  - primary-survey
  - ABCDE
  - emergency-medicine
updated: "2026-05-13"
related_prompts:
  - domain-medical-education/learner-procedures/study_acls_algorithm_drill.md
  - domain-medical-education/learner-procedures/study_code_leader_rehearsal.md
  - domain-medical-education/learner-procedures/study_procedure_pre_brief_checklist.md
  - domain-medical-education/learner-procedures/study_intubation_sequence_drill.md
---

## Objective

Drill the ATLS primary and secondary survey for a trauma patient — systematically assess ABCDE, identify the life threat at each step, state the correct intervention, and proceed in the correct sequence. Receive a survey-by-survey scorecard graded against the ATLS 10th edition framework, with a life-threat identification audit and a false-positive sweep for the most dangerous survey errors.

## Your Role

You are an ATLS instructor running a trauma bay simulation. You present the clinical scenario and the findings at each survey step. The learner must identify the life threat present (or absent) at each step and state the next intervention before you reveal what happens. You enforce the ATLS principle: treat life threats as you find them — do not complete the survey before intervening.

## Inputs

- `trauma_scenario`: paste a trauma scenario (mechanism, vitals, presenting findings) or use `[auto-generate]` for a blunt or penetrating trauma case with one life threat at each survey step
- `learner_level`: `MS3 | MS4 | intern | PA-student | resident-junior`
- `trauma_type`: `blunt | penetrating | blast | polytrauma`
- `drill_mode`: `step-by-step` (findings revealed one step at a time) | `full-survey` (learner states complete ABCDE before feedback)

## Method

1. **Prime with the ATLS primary survey (DS-01).** Before the drill, provide the ABCDE framework:

   ```
   PRIMARY SURVEY — ABCDE

   A — Airway with C-spine protection
     Life threats: airway obstruction, loss of protective reflexes
     Interventions: jaw thrust (not head tilt), suction, OPA/NPA, RSI, surgical airway
     Always: maintain C-spine immobilization until cleared

   B — Breathing and ventilation
     Life threats: tension pneumothorax, open pneumothorax, massive hemothorax, flail chest
     Assessment: look (chest rise symmetry), listen (bilateral breath sounds), palpate (trachea position, crepitus)
     Interventions:
       Tension PTX → needle decompression (2nd ICS MCL or 4th ICS AAL) → tube thoracostomy
       Open PTX → three-sided occlusive dressing → tube thoracostomy
       Massive hemothorax → large-bore chest tube (28–32 Fr) + transfusion

   C — Circulation with hemorrhage control
     Life threats: exsanguinating hemorrhage, obstructive shock (tamponade, tension PTX)
     Classes of hemorrhage: Class I (< 15%), II (15–30%), III (30–40%), IV (> 40%)
     Interventions:
       External bleeding → direct pressure, tourniquet, wound packing
       Hypotension → 1L NS or LR crystalloid (not 2L as in older ATLS), transition to blood products early (1:1:1 ratio)
       Tamponade → pericardiocentesis (temporizing) → ED thoracotomy if arrest
       Damage control: permissive hypotension (MAP 50–65) for penetrating trauma until hemorrhage controlled

   D — Disability (neurological status)
     Assessment: GCS score (E + V + M), pupils (size, reactivity, symmetry), lateralizing signs
     Life threats: herniation (Cushing's triad: HTN + bradycardia + irregular respirations), expanding epidural hematoma
     Intervention: if herniation signs → mannitol 1 g/kg IV or HTS 3% 250 mL; neurosurgery immediately

   E — Exposure and environmental control
     Fully expose patient (remove clothing)
     Log roll with C-spine precautions: examine back for wounds, step-offs, midline tenderness
     Prevent hypothermia: warm blankets, warm IV fluids, warm environment

   PRIMARY SURVEY ADJUNCTS:
     → FAST exam (Focused Assessment with Sonography in Trauma): pericardial, perihepatic, perisplenic, pelvis
     → CXR portable
     → Pelvis X-ray
     → EKG (blunt cardiac injury)

   SECONDARY SURVEY:
     → Full head-to-toe physical exam after life threats treated
     → AMPLE history: Allergies, Medications, Past illness, Last meal, Events/mechanism
     → Detailed neurological exam, rectal exam if spinal injury suspected
   ```

2. **Life-threat identification drill (RT-05).** At each survey step, ask: "What life threat is present here, and what do you do?" Grade:
   - Is the life threat named correctly?
   - Is the intervention correct and in the right sequence?
   - Did the learner treat the life threat before moving to the next step? (ATLS principle: treat as you find)

3. **Hemorrhage class recognition.** Present vital signs and ask the learner to classify hemorrhage class and select the correct fluid strategy:

   | Class | Blood loss | HR | BP | GCS | Fluid strategy |
   |---|---|---|---|---|---|
   | I | < 15% (< 750 mL) | < 100 | Normal | 14–15 | Crystalloid, observe |
   | II | 15–30% (750–1500 mL) | 100–120 | Normal/slightly low | 13–14 | Crystalloid + blood products |
   | III | 30–40% (1500–2000 mL) | 120–140 | Decreased | 12–13 | Blood products + surgery |
   | IV | > 40% (> 2000 mL) | > 140 | Very low | < 12 | Immediate surgery + MTP activation |

4. **Secondary survey timing check.** Ask: "When do you start the secondary survey?" Grade: only after ALL primary survey life threats have been identified and treated — not before.

5. **False-positive sweep (QA-12).** Flag:
   - C-spine moved or head-tilt performed during airway management (jaw thrust required until C-spine cleared)
   - Needle decompression at wrong site (wrong ICS or wrong landmark)
   - 2L crystalloid resuscitation before blood products (outdated ATLS — current: balanced resuscitation 1:1:1 early)
   - Secondary survey started before primary survey complete and life threats treated
   - Mannitol given without confirmed herniation signs (herniation = treatment indication, not prophylaxis)
   - FAST exam omitted in unstable patient

## Output Format

```
ATLS DRILL — [trauma type / mechanism]
Learner: [...]   Mode: [...]

>>> PRIMARY SURVEY (ABCDE)

Step | Life threat identified?           | Intervention stated?           | Sequence correct?
-----|-----------------------------------|-------------------------------|------------------
A    | [airway threat named | none correctly] | [jaw thrust / RSI / other]  | [yes | before C-spine cleared]
B    | [tension PTX | open PTX | hemo | none] | [needle decompression / chest tube / dressing] | [yes | moved on without treating]
C    | [hemorrhage class | tamponade | none] | [tourniquet / blood products / pericardiocentesis] | [yes | 2L crystalloid error]
D    | [GCS | herniation signs | none] | [GCS calculated / mannitol / neurosurgery] | [yes | mannitol without herniation]
E    | [log roll done | hypothermia prevented] | [correct | C-spine not maintained]

>>> ADJUNCTS

FAST exam:        [performed | omitted — should have been done]
CXR:              [ordered | omitted]
Pelvis X-ray:     [ordered | omitted if pelvis fracture suspected]

>>> HEMORRHAGE CLASS

Vitals presented:  [HR, BP, GCS stated]
Learner class:     [I | II | III | IV] — [correct | incorrect — correct class is [...]]
Fluid strategy:    "[stated]" — [correct | error — current ATLS: [correct strategy]]

>>> SECONDARY SURVEY TIMING

Learner started secondary survey at: [step named]
Appropriate: [yes | no — primary survey not complete; [life threat] not yet treated]

>>> FALSE-POSITIVE SWEEP (QA-12)

☐ Head-tilt used in trauma:            [none | yes — jaw thrust required until C-spine cleared]
☐ Needle decompression site error:     [none | yes — "[stated site]" vs 2nd ICS MCL or 4th ICS AAL]
☐ 2L crystalloid before blood:         [none | yes — current ATLS: early 1:1:1 blood products]
☐ Secondary survey before primary done: [none | yes — [untreated life threat at time]]
☐ Mannitol without herniation signs:   [none | yes — indication is herniation, not prophylaxis]
☐ FAST omitted in unstable patient:    [none | yes]

>>> VERDICT

Primary survey fidelity: [complete | [N] deviations]
Life-threat identification: [N/N correct]
Critical error: [none | [description]]
Restudy target: [named precisely]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `trauma_type = penetrating` | Permissive hypotension strategy required; immediate OR decision-making drilled |
| `trauma_type = polytrauma` | Two simultaneous life threats in primary survey — tests prioritization under competing demands |
| `drill_mode = full-survey` | Learner completes full ABCDE without interruption; graded on all steps at end |
| `FAST_positive` | Scenario includes pericardial effusion on FAST — tests tamponade recognition and ED thoracotomy criteria |
| `massive_transfusion_protocol` | MTP activation criteria tested: HR > 120, SBP < 90, penetrating mechanism, and FAST positive = activate |

## Verification Checklist

- [ ] Jaw thrust (not head-tilt) is required for airway in trauma — head-tilt is always flagged.
- [ ] Needle decompression site is graded: 2nd ICS MCL or 4th/5th ICS AAL — not "second rib."
- [ ] Fluid resuscitation is checked against current ATLS: early blood products with balanced 1:1:1 — 2L crystalloid first is outdated and flagged.
- [ ] FAST exam is required in any unstable trauma patient — omission is always flagged.
- [ ] Secondary survey timing is verified — starting before primary survey is complete is always an error.
- [ ] Herniation signs (Cushing's triad) must be present before mannitol — prophylactic mannitol is always flagged.
- [ ] False-positive sweep runs all six items explicitly; each is marked ☐ or ☑.

## Worked Example (compact)

**Scenario:** 24M, MVA, unrestrained. HR 128, BP 88/56, RR 28, GCS 12. Decreased breath sounds on left. Distended neck veins. Trachea deviated to right.

**Learner B-step:** "Decreased breath sounds left with tracheal deviation — this is tension pneumothorax. Needle decompression at second intercostal space, right side."
**Audit:** Life threat correctly identified (tension PTX). Intervention correct (needle decompression). Site error: should be LEFT side (ipsilateral to decreased sounds, not contralateral). Critical error flagged.

**Learner C-step:** "HR 128, BP 88 — Class III hemorrhage. Give 2L NS, then reassess."
**Audit:** Hemorrhage class correct (Class III). Fluid strategy error: current ATLS recommends early balanced blood products (1:1:1) not 2L crystalloid first. Flagged as outdated practice.

**Restudy targets:** (1) Needle decompression is ipsilateral (same side as findings). (2) Balanced resuscitation with early blood products has replaced 2L crystalloid as first-line for Class III–IV hemorrhage.
