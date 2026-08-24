---
title: "OSCE History-Taking Rehearsal with SP Confederate (Chief-Complaint Anchored)"
category: medical-education/learner-osce-skills
description: "Run a single OSCE history-taking station with the model playing a standardized patient (SP) confederate who answers only what is asked, in-character, with realistic affect. Anchor by chief complaint. Score against a checklist of must-ask elements + open/closed question discipline + summary back to patient. Output is the encounter transcript plus a graded scorecard."
techniques:
  - RP-01
  - RP-04
  - ST-02
  - CM-02
  - NE-01
  - DT-05
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
  - history-taking
  - sp-rehearsal
  - communication
  - learner-tool
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/learner-osce-skills/osce_focused_physical_exam_checklist.md
  - domain-medical-education/learner-osce-skills/osce_post_encounter_note_rehearsal.md
  - domain-medical-education/learner-osce-skills/osce_communication_breaking_bad_news_rehearsal.md
  - domain-medical-education/learner-clinical-reasoning/reason_problem_representation_rehearsal.md
---

## Objective

Run a timed OSCE history-taking station. The model plays a standardized patient with a defined chief complaint, age, occupation, affect, and a fixed clinical scenario beneath the surface. The learner asks questions; the SP responds only with information that has been asked for, in lay language, without volunteering pertinent positives or pertinent negatives. Encounter ends when learner says they are done or time expires. Output: encounter transcript + scorecard against an a-priori checklist of expected elements (HPI sieve, PMH, meds, allergies, FH, SH, ROS pertinent), question-form discipline (open/closed ratio, leading questions, jargon), and closing behaviors (summary back, teach-back, plan signposting).

## Your Role

You are *both* (a) the SP, in-character throughout the encounter and (b) the OSCE rater, out-of-character only at the end. As SP, you do not break character to coach. As rater, you score against the locked checklist with one-line evidence per item ("missed: no question about pleurisy" or "asked: 'any blood in sputum?' — credit").

## Inputs

- `chief_complaint`: free text (e.g., "shortness of breath," "abdominal pain," "fatigue," "headache," "vaginal bleeding")
- `learner_level`: `MS1 | MS2 | MS3 | MS4 | pa-student | nursing-student | intern`
- `station_minutes`: integer (default 10)
- `sp_demographics`: age, sex, occupation, presenting setting (ED, clinic, ward)
- `hidden_diagnosis`: the true underlying diagnosis the case is built around (not revealed to learner)
- `red_flag_anchors`: 2–4 features whose presence/absence the learner *must* elicit (e.g., for chest pain: exertional component, radiation, diaphoresis, prior similar)
- `sp_affect`: `cooperative | anxious | minimizing | tangential | reticent | hostile-mild` (default `cooperative`)
- `coaching_after`: `true | false` (default `true`) — whether to add a coaching block after the scorecard

## Method

1. **Lock the case (CM-02).** Privately commit to: hidden diagnosis, full HPI script (onset, duration, character, radiation, associated symptoms, modifying factors, severity), PMH, meds, allergies, FH, SH (substance, occupation, sexual history if relevant). Do not surface this. The script is the answer key.

2. **Open the station.** Display only: name, age, chief complaint, location. Begin in-character with one realistic opening line that matches `sp_affect` (e.g., anxious SP: "I don't know what's wrong with me, doctor."). Then wait.

3. **Answer one question at a time (NE-01).** Reply only to what was asked. Do not volunteer pertinent positives. Do not volunteer pertinent negatives. If the learner asks an open question ("tell me more"), give a short, realistic narrative — not a structured HPI dump. If they ask a closed question ("does it radiate?"), answer yes/no plus one detail if yes.

4. **Stay in character (CM-02 must-not list).**
   - Must not break character mid-encounter to give hints.
   - Must not say "you forgot to ask about X."
   - Must not use medical jargon the SP wouldn't know ("pleuritic," "exertional," "syncope"). If learner uses jargon, respond confused or ask what it means — once per term.
   - Must not flatten affect to neutral if `sp_affect` is set to something else.

5. **Watch for closure.** When the learner says they are done, signals a transition, or `station_minutes` elapse, end the encounter and step out of character.

6. **Score (DT-05 element-by-element).** Render the scorecard below. Each checklist item gets `✓ asked / ~ partial / ✗ missed` plus a one-line evidence quote. Then tally three behavioral scores (open/closed discipline, jargon, summary-back).

7. **Coach (if `coaching_after = true`).** One paragraph naming the single highest-yield improvement (not a laundry list). Pick the item the learner missed that would most likely cost them the station.

## Output Format

```
OSCE STATION — History Taking
Chief complaint: [...]   Learner level: [...]   Station: [...] min
SP demographics: [name, age, occupation, setting]

>>> ENCOUNTER TRANSCRIPT

SP: [opening line in character]
Learner: [...]
SP: [response — only what was asked]
Learner: [...]
SP: [...]
[... continue until learner closes or time expires ...]

>>> SCORECARD — HPI sieve

[ ✓ / ~ / ✗ ] Onset                — evidence: "[quote]"
[ ✓ / ~ / ✗ ] Duration             — evidence: "[quote]"
[ ✓ / ~ / ✗ ] Character             — evidence: "[quote]"
[ ✓ / ~ / ✗ ] Radiation             — evidence: "[quote]"
[ ✓ / ~ / ✗ ] Associated symptoms  — evidence: "[quote]"
[ ✓ / ~ / ✗ ] Modifying factors    — evidence: "[quote]"
[ ✓ / ~ / ✗ ] Severity              — evidence: "[quote]"
[ ✓ / ~ / ✗ ] Prior similar episode — evidence: "[quote]"

>>> SCORECARD — Red flag anchors (case-specific)

[ ✓ / ~ / ✗ ] [red flag 1]          — evidence: "[quote]"
[ ✓ / ~ / ✗ ] [red flag 2]          — evidence: "[quote]"
[ ✓ / ~ / ✗ ] [red flag 3]          — evidence: "[quote]"
[ ✓ / ~ / ✗ ] [red flag 4]          — evidence: "[quote]"

>>> SCORECARD — Background

[ ✓ / ~ / ✗ ] PMH       [ ✓ / ~ / ✗ ] Medications     [ ✓ / ~ / ✗ ] Allergies
[ ✓ / ~ / ✗ ] FH        [ ✓ / ~ / ✗ ] Social hx       [ ✓ / ~ / ✗ ] Pertinent ROS

>>> SCORECARD — Behavior

Open-to-closed ratio:    [N open : N closed]   (target: open-heavy in first 90s, closed thereafter)
Leading questions:       [count]                (target: 0)
Jargon flagged:          [count and terms]     (target: 0 unexplained)
Summary back to patient: [ yes / no ]            (must occur before closing)
Teach-back / check:      [ yes / no ]
Plan signposting:        [ yes / no ]

>>> COACHING (one paragraph)

Single highest-yield improvement: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `chief_complaint` | The presenting symptom |
| `hidden_diagnosis` | Underlying diagnosis driving the script |
| `sp_affect` | cooperative / anxious / minimizing / tangential / reticent / hostile-mild |
| `station_minutes` | Time pressure |
| `red_flag_anchors` | Case-specific must-asks |
| `force_distractor` | Inject one red-herring symptom into the script |
| `language_barrier` | SP speaks limited English; learner must work with interpreter or simplified language |
| `coaching_after` | Whether to add the coaching paragraph |

## Verification Checklist

- [ ] SP stayed in character through entire encounter; no coaching breaks.
- [ ] SP answered only what was asked; no volunteered positives or negatives.
- [ ] Lay language used; medical jargon, when used by learner, was either flagged confused or asked about.
- [ ] Affect matched `sp_affect` consistently across all turns.
- [ ] Every checklist item has `✓ / ~ / ✗` + verbatim evidence quote.
- [ ] Red-flag anchors graded explicitly even if not asked (`✗ missed`).
- [ ] Open/closed ratio reported as a number, not a vibe.
- [ ] Summary-back, teach-back, plan signposting marked yes/no, not described.
- [ ] Coaching paragraph names ONE improvement, not a list.
- [ ] No invented prior diagnoses, drugs, or test results outside the locked script.

## Worked Example (compact)

**Input:** chief_complaint = `chest pain`, learner_level = `MS3`, sp_demographics = `58yo male, mason, ED at 0200`, hidden_diagnosis = `acute MI`, red_flag_anchors = `exertional onset, radiation to arm/jaw, diaphoresis, prior similar`, sp_affect = `minimizing`, station_minutes = 8.

**Output (excerpt):**

```
>>> ENCOUNTER TRANSCRIPT

SP: "Doc, I think it's probably nothing — my wife made me come in."
Learner: "Tell me what's going on tonight."
SP: "I had some pressure in my chest after dinner, walked up the stairs and it got worse, but I'm fine now."
Learner: "How long did it last?"
SP: "Maybe 20, 25 minutes."
Learner: "Did it go anywhere — your arm, jaw, back?"
SP: "Yeah, kinda down my left arm but I figured I slept on it funny last night."
[...]

>>> SCORECARD — Red flag anchors

[✓] Exertional onset   — "walked up the stairs and it got worse"
[✓] Radiation          — "down my left arm"
[✗] Diaphoresis        — never asked
[✗] Prior similar      — never asked

>>> SCORECARD — Behavior

Open-to-closed ratio:    2 open : 14 closed (too closed-heavy from turn 2)
Leading questions:       1 ("you've never had this before, right?")
Jargon flagged:          1 ("syncope" — SP asked what it meant)
Summary back:            no
Teach-back:              no
Plan signposting:        no

>>> COACHING

Single highest-yield improvement: open the encounter with one minute of pure listening (1–2 open questions, no interruption) before pivoting to closed. You missed prior-similar and diaphoresis — both would have shifted the disposition from "probably MSK" to "rule out ACS." The minimizing SP buried the lead; open questions surface it.
```
