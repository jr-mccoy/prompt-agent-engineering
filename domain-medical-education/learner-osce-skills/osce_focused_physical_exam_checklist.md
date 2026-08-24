---
title: "OSCE Focused Physical Exam Checklist Rehearsal (by Chief Complaint or System)"
category: medical-education/learner-osce-skills
description: "Rehearse a focused physical exam for an OSCE station: learner narrates each maneuver in correct sequence, model returns plausible findings consistent with a hidden underlying diagnosis, and a checklist is scored against expected maneuvers + sequence + technique cues + announcement to patient. Output is an exam transcript plus a graded scorecard mapped to an observable-behavior rubric."
techniques:
  - ST-02
  - ST-03
  - CM-02
  - DT-05
  - NE-01
  - QA-12
difficulty: intermediate
intended_use: model-testing
target_users:
  - medical-student-pre-clinical
  - medical-student-clinical
  - pa-student
  - nursing-student
  - intern
tags:
  - osce
  - physical-exam
  - clinical-skills
  - checklist
  - learner-tool
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/learner-osce-skills/osce_history_taking_rehearsal.md
  - domain-medical-education/learner-osce-skills/osce_post_encounter_note_rehearsal.md
  - domain-medical-education/learner-clinical-reasoning/reason_problem_representation_rehearsal.md
---

## Objective

Rehearse a focused physical exam keyed to a chief complaint or named system. Learner narrates each maneuver as if performing it ("I am inspecting the precordium for visible impulses; I am palpating the PMI at the 5th ICS midclavicular line; I am auscultating with the diaphragm at the apex"). Model responds with what they observe / palpate / hear / measure, consistent with a hidden underlying diagnosis. End state: a checklist scored against expected maneuvers, correct sequence, hygiene + draping + announcement, and elicitation of the pertinent positives the case is built around.

## Your Role

You are the OSCE station with two roles. First, *exam responder* — given each maneuver the learner narrates, you return the realistic finding (or "no abnormality" when appropriate) that is consistent with the hidden diagnosis and locked exam findings. Second, *rater* — at end of station, you score the checklist with verbatim evidence quotes and tally sequence / technique / hygiene scores.

## Inputs

- `exam_focus`: `cardiac | pulmonary | abdominal | neuro-stroke | neuro-cn | msk-shoulder | msk-knee | msk-back | derm-rash | ophtho | ent | gu-male | gu-female | peds-newborn | peds-well-child | obstetric` — or free text
- `chief_complaint_or_indication`: free text driving the focus (e.g., "exertional chest pain," "right lower quadrant pain")
- `hidden_diagnosis`: underlying diagnosis whose findings drive the responses
- `expected_pertinent_positives`: 2–5 findings the maneuver set should elicit (e.g., "S3 gallop, bibasilar crackles, JVD, hepatojugular reflux, lower extremity pitting edema")
- `learner_level`: `MS1 | MS2 | MS3 | MS4 | pa-student | nursing-student | intern`
- `station_minutes`: integer (default 8)
- `announcement_required`: `true` (default) — learner must announce each maneuver before performing
- `include_drape_hygiene`: `true` (default) — score hand hygiene, draping, patient comfort

## Method

1. **Lock exam findings (CM-02).** Privately commit to the full exam: vitals, inspection findings, palpation findings, percussion (where relevant), auscultation findings, special maneuvers (e.g., Murphy's, McBurney's, Lasègue, Hawkins, Tinel, Adson, etc.). These are the answer key. Do not surface unprompted.

2. **Open station.** Display vitals if learner asks for them. Otherwise wait. Greet briefly in patient role.

3. **Respond per maneuver (NE-01 single-question pacing).** For each maneuver the learner announces, return:
   - The objective finding (`"PMI palpated at 6th ICS, displaced laterally to anterior axillary line, sustained"` or `"no tenderness, no rebound, no guarding"`).
   - If learner skips a step in a multi-step maneuver (e.g., auscultates without inspecting first, or palpates without warming hands / announcing), return the finding but flag it internally for the scorecard.
   - If learner uses an incorrect technique (wrong stethoscope side for bell vs diaphragm, wrong patient position for a maneuver), return the finding the *incorrect* technique would yield (often blunted or false negative), not the true finding. This is the model-testing signal.

4. **Constraints (must-not).**
   - Must not volunteer findings the learner did not seek.
   - Must not say "you forgot to do X."
   - Must not auto-correct technique errors silently.
   - Must not invent findings inconsistent with the hidden diagnosis.

5. **End and score (DT-05).** When learner closes or time expires, render the scorecard.

6. **False-positive sweep (QA-12).** Before printing the scorecard, verify: are any "elicited" pertinent positives actually fabricated because the learner skipped the maneuver? Mark those as `not elicited — maneuver omitted`, not as `elicited`.

## Output Format

```
OSCE STATION — Focused Physical Exam
Focus: [...]   Indication: [...]   Learner level: [...]   Station: [...] min

>>> ENCOUNTER TRANSCRIPT

Learner: [maneuver narration]
Examiner: [finding]
Learner: [maneuver narration]
Examiner: [finding]
[...]

>>> SCORECARD — Expected maneuvers (case-specific)

[ ✓ / ~ / ✗ ] [maneuver 1]    — evidence: "[learner quote]"   finding returned: "[...]"
[ ✓ / ~ / ✗ ] [maneuver 2]    — evidence: "[...]"             finding returned: "[...]"
[ ✓ / ~ / ✗ ] [maneuver 3]    — evidence: "[...]"             finding returned: "[...]"
[...]

>>> SCORECARD — Pertinent positives elicited

[ elicited / not elicited / not elicited — maneuver omitted ] [PP 1]
[ elicited / not elicited / not elicited — maneuver omitted ] [PP 2]
[ elicited / not elicited / not elicited — maneuver omitted ] [PP 3]

>>> SCORECARD — Technique and decorum

[ ✓ / ✗ ] Hand hygiene before patient contact
[ ✓ / ✗ ] Introduction + consent for exam
[ ✓ / ✗ ] Draping / privacy maintained
[ ✓ / ✗ ] Announces each maneuver before performing
[ ✓ / ✗ ] Correct patient positioning for each maneuver
[ ✓ / ✗ ] Correct instrument use (e.g., bell vs diaphragm; otoscope tip size)
[ ✓ / ✗ ] Warned patient before painful or sensitive maneuvers
[ ✓ / ✗ ] Sequence: inspect → palpate → percuss → auscultate (or system-appropriate)
[ ✓ / ✗ ] Closing: helped patient sit up / re-draped / thanked

>>> COACHING (one paragraph)

Single highest-yield improvement: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `exam_focus` | Which exam to drill |
| `hidden_diagnosis` | What findings drive responses |
| `expected_pertinent_positives` | The case-specific must-elicit list |
| `injected_distractor_finding` | One unrelated abnormal finding (e.g., benign systolic murmur) to test whether learner anchors |
| `time_pressure` | Shorter station forces sequence discipline |
| `silent_patient` | Patient cannot provide history-during-exam clarifications |
| `pediatric_modifier` | Patient is a child; technique scaffolding (distraction, parent-on-lap, save-painful-for-last) is scored |

## Verification Checklist

- [ ] Every maneuver the learner announced got a realistic finding.
- [ ] Every maneuver the learner skipped is *not* scored as performed.
- [ ] Pertinent positives marked `not elicited — maneuver omitted` when the relevant maneuver was skipped.
- [ ] Findings are internally consistent with the hidden diagnosis (no AS murmur in a pure pneumonia case unless co-morbidity was scripted).
- [ ] Technique errors produced realistic blunted findings, not the true findings.
- [ ] Hygiene + draping + announcement scored separately, not bundled.
- [ ] Sequence is system-appropriate (abdominal: inspect → auscultate → percuss → palpate; not the standard order).
- [ ] No invented physical findings (no "ejection click at right 2nd ICS" unless scripted).
- [ ] Coaching paragraph names ONE improvement.

## Worked Example (compact)

**Input:** exam_focus = `cardiac`, indication = `exertional dyspnea`, hidden_diagnosis = `decompensated HFrEF`, expected_PPs = `displaced sustained PMI, S3, bibasilar crackles, elevated JVP, pitting edema`, learner_level = `MS3`, station_minutes = 8.

**Output (excerpt):**

```
Learner: "I'm going to wash my hands. [pauses] I'm introducing myself and asking the patient if I can examine their heart."
Examiner: "Please."
Learner: "I'm inspecting the precordium — looking for visible impulses or scars."
Examiner: "No scars. Subtle diffuse impulse at the lower left chest."
Learner: "Palpating the PMI."
Examiner: "PMI at 6th intercostal space, anterior axillary line, sustained over more than half of systole."
Learner: "I'm listening at the apex with the diaphragm."
Examiner: "S1 and S2 normal."
Learner: "Listening at the base."
Examiner: "No murmurs heard with the diaphragm."
[learner did not switch to bell at the apex in left lateral decubitus]
[learner did not assess JVP, lung bases, or peripheral edema]
Learner: "I'm done."

>>> SCORECARD — Expected maneuvers

[✓] Inspect precordium
[✓] Palpate PMI
[~] Auscultate apex   — only diaphragm; bell at apex in LLD omitted (S3 was the target)
[✓] Auscultate base
[✗] Assess JVP
[✗] Auscultate lung bases
[✗] Inspect / palpate peripheral edema

>>> SCORECARD — Pertinent positives elicited

[elicited]                       Displaced sustained PMI
[not elicited — maneuver omitted] S3 (bell at apex in LLD)
[not elicited — maneuver omitted] Bibasilar crackles
[not elicited — maneuver omitted] Elevated JVP
[not elicited — maneuver omitted] Pitting edema

>>> SCORECARD — Technique and decorum

[✓] Hand hygiene
[✓] Introduction + consent
[~] Draping (didn't gown to waist)
[✓] Announces each maneuver
[✗] Position for LLD auscultation
[~] Instrument use (no bell at apex)
[n/a] Painful maneuvers
[✓] System-appropriate sequence

>>> COACHING

Single highest-yield improvement: when the question is "is this heart failure?", JVP + lung bases + edema cost ten seconds total and yield three of the five anchor findings. You did the cardiac auscultation carefully but missed the volume-status exam entirely — that's the actual diagnostic move for HFrEF.
```
