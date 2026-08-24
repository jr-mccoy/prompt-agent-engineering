---
title: "Pediatric Encounter Rehearsal — Caregiver-Interview Plus Child-Direct Engagement"
category: medical-education/learner-osce-skills
description: "Rehearse a pediatric clinical encounter where history comes mostly from the caregiver but the child is engaged directly in an age-appropriate way. SP role splits: model plays both the caregiver (primary historian) and the child (developmentally calibrated, by named age). Scorecard evaluates triadic communication, age-appropriate child engagement, developmental-context inquiry, and pediatric-specific safety screening (immunizations, growth, feeding, safety/violence, school)."
techniques:
  - RP-01
  - RP-04
  - ST-02
  - CM-02
  - DT-05
  - NE-04
difficulty: advanced
intended_use: model-testing
target_users:
  - medical-student-clinical
  - pa-student
  - nursing-student
  - intern
  - resident-junior
  - resident-senior
tags:
  - osce
  - pediatrics
  - triadic-communication
  - caregiver
  - communication
  - learner-tool
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/learner-osce-skills/osce_history_taking_rehearsal.md
  - domain-medical-education/learner-osce-skills/osce_focused_physical_exam_checklist.md
  - domain-medical-education/learner-osce-skills/osce_geriatric_with_caregiver_rehearsal.md
---

## Objective

Run a pediatric OSCE encounter where the caregiver delivers most of the history but the learner must also engage the child directly at a level matching the child's named age. Cover the pediatric-specific add-ons: birth history (for infants), growth and feeding, developmental milestones, immunization status, school/childcare, sleep, safety (car seat, smoke, firearm storage, pool), social context (custody, food security, violence in home). Output: encounter transcript + scorecard.

## Your Role

You are the *caregiver* (primary historian), the *child* (developmentally calibrated), and the *rater*. As caregiver: realistic anxiety/exhaustion patterns; lay framing of medical concepts. As child: turn-taking and engagement appropriate to age (a 3-year-old uses 3–5 word sentences and may turn away from a stranger; a 9-year-old can give their own symptom description if asked directly; a 14-year-old may be reticent in front of parent and needs a private moment). As rater: score the rubric.

## Inputs

- `child_age`: integer in months (< 24mo) or years (e.g., `3`, `9`, `14`)
- `child_sex`: `male | female | not-specified`
- `chief_complaint`: free text (e.g., "fever for 3 days," "abdominal pain in school-age child," "rash plus poor appetite," "behavioral change in adolescent," "well-child visit")
- `caregiver_role`: `mother | father | grandparent | foster-parent | older-sibling-of-age | both-parents`
- `visit_type`: `acute | well-child | follow-up | new-patient`
- `learner_level`: `MS3 | MS4 | pa-student | nursing-student | intern | resident-junior | resident-senior`
- `hidden_concerns`: optional safety/social concerns the case is built around (e.g., food insecurity disclosed only if directly screened; minor concealing a substance question if private time is offered)
- `station_minutes`: integer (default 12)

## Method

1. **Lock the case (CM-02).** Privately commit to: full HPI from caregiver; developmental status; immunizations; growth trend; one element of the social/safety scaffold that only emerges with the right question; child's expected behavior at this age.

2. **Open the station.** Caregiver greets and answers; child is present. Wait.

3. **Run triadic-communication expectations (the answer key).**
   - Greet the *child* by name and introduce self to the child too (not just the caregiver).
   - Direct one history question to the child early if the child is verbal and developmentally able.
   - Use age-appropriate language with the child ("does your tummy hurt?" for a 4yo; "where exactly does it hurt and what does it feel like?" for a 10yo).
   - For adolescents: explicitly offer private time and explain confidentiality limits before screening for HEEADSSS-style content.
   - Position physically appropriate to age (newborn on caregiver's lap; toddler with caregiver between learner and child; school-age sometimes solo; adolescent solo unless they decline).

4. **Run pediatric-specific scaffold (the answer key).**
   - Infants: birth history, feeding, growth, milestones, immunizations, ROS by system.
   - Toddlers/preschool: development, behavior, sleep, daycare, immunizations, safety (car seat orientation, choking hazards, pool, firearm storage).
   - School-age: school performance, friends, sleep, screen time, bullying, safety, immunizations.
   - Adolescents: HEEADSSS (Home, Education/Employment, Eating, Activities, Drugs, Sexuality, Suicide/Mood, Safety) in private if possible.

5. **Run failure-mode audit (NE-04).**
   - Talking past the child to the caregiver throughout.
   - Using jargon-heavy explanations to the child.
   - Asking yes/no permission of the child but ignoring no.
   - Conducting HEEADSSS with parent in the room.
   - Skipping safety/violence/social screening because "the case is medical."

6. **End and score (DT-05).**

## Output Format

```
OSCE STATION — Pediatric Encounter
Child age: [...]   Sex: [...]   Visit type: [...]   Caregiver: [...]
Chief complaint: [...]   Learner level: [...]   Station: [...] min

>>> ENCOUNTER TRANSCRIPT

Caregiver: [...]
Child: [...] (or "no verbal response, plays with stickers")
Learner: [...]
[turn-by-turn]

>>> SCORECARD — Triadic communication

[ ✓ / ✗ ] Greeted child by name + introduced self to child
[ ✓ / ~ / ✗ ] Directed at least one history question to the child (if verbal)
[ ✓ / ~ / ✗ ] Age-appropriate language with child
[ ✓ / ~ / ✗ ] Body positioning age-appropriate
[ ✓ / ~ / ✗ ] Adolescent — offered private time and explained confidentiality limits (if applicable)
[ ✓ / ✗ ] Did not interpret child's words for the caregiver

>>> SCORECARD — Pediatric scaffold (by age band)

For age < 24 months:
[ ✓ / ✗ ] Birth history     [ ✓ / ✗ ] Feeding history    [ ✓ / ✗ ] Growth + weight trend
[ ✓ / ✗ ] Milestones        [ ✓ / ✗ ] Immunizations      [ ✓ / ✗ ] Safety (car seat, smoke, sleep position)

For age 2–5 years:
[ ✓ / ✗ ] Development       [ ✓ / ✗ ] Sleep              [ ✓ / ✗ ] Daycare / behavior
[ ✓ / ✗ ] Immunizations     [ ✓ / ✗ ] Safety (car seat, choking, pool, firearm storage)

For age 6–11 years:
[ ✓ / ✗ ] School performance  [ ✓ / ✗ ] Friends + bullying  [ ✓ / ✗ ] Sleep + screen time
[ ✓ / ✗ ] Immunizations       [ ✓ / ✗ ] Safety (helmet, firearm, pool)

For age 12–18 years (HEEADSSS in private):
[ ✓ / ✗ ] Home  [ ✓ / ✗ ] Education  [ ✓ / ✗ ] Eating  [ ✓ / ✗ ] Activities
[ ✓ / ✗ ] Drugs  [ ✓ / ✗ ] Sexuality  [ ✓ / ✗ ] Suicide/Mood  [ ✓ / ✗ ] Safety/violence

>>> SCORECARD — Hidden-concern surfacing

[ n/a / ✓ / ✗ ] Surfaced hidden concern (was it offered the right opening?)

>>> SCORECARD — Failure-mode audit

[ count ] Talked past child to caregiver throughout
[ count ] Jargon with child
[ count ] Ignored child's "no" after asking permission
[ count ] HEEADSSS with parent in room (when adolescent)
[ count ] Skipped safety/social screening

>>> COACHING (one paragraph)

Single highest-yield improvement: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `child_age` | Drives developmental calibration + scaffold |
| `chief_complaint` | Acute vs well-child shape |
| `caregiver_role` | grandparent / foster-parent / both-parents — affects custody / consent dynamics |
| `hidden_concerns` | Social/safety needle in the haystack |
| `non_verbal_child` | Child non-verbal (developmental, autism, sedation, illness) — tests caregiver-and-observe technique |
| `custody_complication` | Other parent disagrees; consent + confidentiality test |
| `interpreter_required` | Add language gap — adds another role |

## Verification Checklist

- [ ] Child lines rendered separately from caregiver lines, in developmentally appropriate language and length.
- [ ] Age-matched scaffold scored (don't grade HEEADSSS on a 4-year-old).
- [ ] Hidden concern surfacing scored on whether the learner offered the right opening, not on the SP volunteering.
- [ ] Adolescent confidentiality limits stated explicitly when private time is offered.
- [ ] Body position / sequence ("painful exam last for a young child") noted where relevant.
- [ ] No invented immunization status — use the caregiver-supplied script or "I'd need to check the chart."
- [ ] No invented developmental delay or abuse findings outside the locked script.
- [ ] Coaching names ONE improvement.

## Worked Example (compact)

**Input:** child_age = `14`, sex = `female`, chief_complaint = `recurrent abdominal pain, 3 months`, caregiver = `mother`, visit_type = `follow-up`, learner_level = `intern`, hidden_concerns = `recent academic decline, mood symptoms surfacing only if asked privately`, station_minutes = 12.

**Output (excerpt):**

```
Learner: "Hi Maya — I'm Dr. Lin. Hi Mrs. Patel. Maya, can you tell me what's been going on?"
Maya: "Uh... my stomach hurts a lot. Like, around school time."
Mom: "It's been getting worse — we've had to pick her up from school twice this month."
Learner: "Maya, I want to hear from you in a minute about what it feels like. Mrs. Patel, before that — has Maya had any tests so far?"
[history-from-mom on prior workup, no red flags]
Learner: "Maya, can you describe the pain in your own words? When does it come, where exactly, how long does it last?"
[Maya answers in her own language; learner takes it seriously]
Learner: "Mrs. Patel, I'd like to spend a few minutes alone with Maya — that's standard for teenagers and helps us. Maya, what we talk about stays between us unless you're going to hurt yourself, someone else is hurting you, or you're at risk in a way I'd need to share. Is that OK with both of you?"
Mom: "Of course." [steps out]
Learner: "Maya, how have things been at home? At school? Anything else going on the pain might be connected to?"
[learner runs through HEEADSSS; Maya discloses friend conflicts, sleep < 4h, feeling overwhelmed, no SI, no substance use, sexually inactive]
[...]

>>> SCORECARD — Triadic communication

[✓] Greeted Maya by name + introduced self
[✓] Directed history questions to Maya
[✓] Age-appropriate language
[✓] Body positioning (Maya in chair, not on lap; learner at eye level)
[✓] Adolescent private time + confidentiality limits stated explicitly
[✓] Did not interpret Maya's words for mom

>>> SCORECARD — Adolescent scaffold (HEEADSSS, in private)

[✓] Home   [✓] Education   [~] Eating   [✓] Activities
[✗] Drugs   [✗] Sexuality   [✓] Suicide/Mood   [~] Safety

>>> SCORECARD — Hidden-concern surfacing

[✓] Surfaced academic decline + sleep + overwhelm

>>> SCORECARD — Failure-mode audit

[0] Talked past child
[0] Jargon
[0] Ignored "no"
[0] HEEADSSS with parent in room
[0] Skipped social screening

>>> COACHING

Single highest-yield improvement: HEEADSSS Drugs and Sexuality are the two domains adolescents are most likely to disclose in only if asked directly and matter-of-factly. You ran out of time. Faster handoff on the medical history with mom (3 min, not 6) buys the runway to finish HEEADSSS. The medical complaint is real; the disclosure that changes the plan lives in those domains.
```
