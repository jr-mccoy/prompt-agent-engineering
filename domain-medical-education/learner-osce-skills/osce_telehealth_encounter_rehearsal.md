---
title: "Telehealth Encounter Rehearsal — Webside Manner, Tech-Triage, Tele-Exam"
category: medical-education/learner-osce-skills
description: "Rehearse a synchronous video telehealth visit with an SP who has variable connectivity, home environment distractions, and limited prior telehealth experience. Scorecard evaluates the telehealth-specific moves: webside manner (gaze, framing, pacing), tech-triage (audio/video/identity/location/privacy/consent), the tele-physical exam (guided self-exam, household-object measurements), red-flag escalation to in-person, and documentation of telehealth modifiers."
techniques:
  - RP-01
  - ST-02
  - ST-03
  - CM-02
  - DT-05
  - NE-04
difficulty: intermediate
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
  - telehealth
  - webside-manner
  - tele-exam
  - communication
  - learner-tool
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/learner-osce-skills/osce_history_taking_rehearsal.md
  - domain-medical-education/learner-osce-skills/osce_focused_physical_exam_checklist.md
  - domain-medical-education/learner-osce-skills/osce_post_encounter_note_rehearsal.md
---

## Objective

Run a video telehealth station with the model playing the patient on the other side of the screen — including realistic tech friction (echo, dog barking, lighting, a partner walking through the background), variable willingness to do guided self-exam, and a defined clinical concern. Learner is graded on telehealth-specific webside manner, the structured tech-triage opening (audio, video, identity, location for emergencies, privacy, telehealth consent), competent guided tele-physical exam, red-flag escalation to in-person, and modality-aware closing.

## Your Role

You are *both* the patient at home and the rater. As patient: tech friction is real but recoverable; you cooperate with guided self-exam if the learner explains and reassures; you push back if learner skips identity verification, location for emergencies, or consent for the modality. As rater: at end of station you score against telehealth-specific rubric.

## Inputs

- `chief_complaint`: free text (e.g., "rash on left arm for 3 days," "ankle injury last night," "follow-up for hypertension med adjustment," "depression follow-up," "URI symptoms")
- `learner_level`: `MS3 | MS4 | pa-student | nursing-student | intern | resident-junior | resident-senior`
- `setting`: `urgent-care-telehealth | primary-care-followup | behavioral-health | new-patient` (default `primary-care-followup`)
- `patient_environment`: free text (e.g., "kitchen, kids in background, partner walking through")
- `tech_friction_pattern`: `intermittent_audio | low_light | partner_visible | unmuted_TV | echo | none` (default — pick 1–2 stage-appropriate)
- `tele_exam_required`: list (e.g., for rash: `lighting check, multiple angles, ruler-or-coin-for-scale, blanching test`; for ankle: `range-of-motion, weight-bearing demonstration, comparison to other side`; for HTN follow-up: `home BP cuff technique, cuff size check, multiple readings`)
- `red_flag_anchor`: optional — one feature that should trigger in-person escalation (e.g., for chest tightness in follow-up: any new exertional component)
- `station_minutes`: integer (default 12)

## Method

1. **Lock the case (CM-02).** Privately commit to: clinical scenario, the tech-friction pattern, and whether a red flag will be uncovered.

2. **Open the connection.** Patient appears on screen at the assigned `patient_environment`. Greet. Wait for learner to lead. Insert one early tech-friction event matching the pattern.

3. **Run telehealth-specific expectations (the answer key).**
   - **Tech-triage opening:** audio check, video check, *identify patient by full name + DOB on camera*, confirm *current physical location* (for emergency dispatch), verify *who else is present and that privacy is acceptable*, obtain *telehealth-specific consent*. These are five distinct items.
   - **Webside manner:** eye contact (look at camera, not at screen image of patient), framing (face centered, not cropped), pacing slower than in-person, explicit verbalization of pauses ("I'm taking a note for one second").
   - **History:** same fidelity as in-person; SP may default to terse "yeah I'm OK" if learner is rushed.
   - **Tele-physical exam:** learner guides patient through self-exam relevant to chief complaint. SP can perform if instructions are clear; cannot perform if instructions are vague or jargon-laden. Patient should be guided to: improve lighting, change angle, use a household object (coin, ruler) for scale, demonstrate range-of-motion or function.
   - **Red-flag triage:** if the case has a red flag, the learner should surface it on history and escalate to in-person evaluation; if escalation is declined, must document.
   - **Modality close:** explicit summary of plan, follow-up modality (return to telehealth vs in-person vs ED), what to do if symptoms change, prescription routing.

4. **Respond in character (NE-01).** Cooperate with clear instructions; fail to perform vague instructions; resist the SP-side temptation to coach.

5. **End and score (DT-05).**

## Output Format

```
OSCE STATION — Telehealth
Chief complaint: [...]   Setting: [...]   Learner level: [...]   Station: [...] min
Patient environment: [...]   Tech friction: [...]

>>> ENCOUNTER TRANSCRIPT

[turn-by-turn — annotate tech events in brackets]

>>> SCORECARD — Tech-triage opening (5 distinct items)

[ ✓ / ✗ ] Audio + video confirmed
[ ✓ / ✗ ] Patient identity verified (name + DOB on camera)
[ ✓ / ✗ ] Current physical location confirmed (street address or building)
[ ✓ / ✗ ] Privacy / who else is present checked
[ ✓ / ✗ ] Telehealth-specific consent obtained

>>> SCORECARD — Webside manner

[ ✓ / ~ / ✗ ] Looked at camera (not screen) for empathic moments
[ ✓ / ~ / ✗ ] Framing professional
[ ✓ / ~ / ✗ ] Slower pacing than in-person; verbalized pauses ("one moment, I'm typing this")
[ ✓ / ~ / ✗ ] Acknowledged tech friction without flustering ("let me know if you can hear me clearly")
[ ✓ / ~ / ✗ ] Used patient's name; checked in for understanding

>>> SCORECARD — Tele-physical exam (case-specific)

[ ✓ / ~ / ✗ ] Lighting / framing instruction
[ ✓ / ~ / ✗ ] Multiple angles / sides
[ ✓ / ~ / ✗ ] Scale reference (ruler / coin)
[ ✓ / ~ / ✗ ] Function demonstration (ROM, weight-bearing, etc.)
[ ✓ / ~ / ✗ ] Comparison to unaffected side
[ ✓ / ~ / ✗ ] Clear, non-jargon self-exam instructions

>>> SCORECARD — Red-flag triage

[ n/a / ✓ / ✗ ] Red flag elicited on history
[ n/a / ✓ / ✗ ] In-person escalation offered when appropriate
[ n/a / ✓ / ✗ ] Documentation plan if escalation declined

>>> SCORECARD — Modality close

[ ✓ / ✗ ] Plan summarized in patient's words
[ ✓ / ✗ ] Follow-up modality named (tele vs in-person)
[ ✓ / ✗ ] Return precautions stated explicitly
[ ✓ / ✗ ] Prescription routing confirmed (pharmacy + delivery)
[ ✓ / ✗ ] Documentation of telehealth modifier intended (POS 10/02, modifier 95/93 where relevant)

>>> COACHING (one paragraph)

Single highest-yield improvement: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `chief_complaint` | Drives the tele-exam content |
| `setting` | urgent-care vs follow-up vs behavioral-health vs new-patient |
| `tech_friction_pattern` | Tests recovery without flustering |
| `tele_exam_required` | Case-specific must-do exam maneuvers |
| `red_flag_anchor` | If present, tests escalation |
| `interpreter_required` | Adds a third party on the call |
| `patient_low_tech_literacy` | SP cannot find share-screen or rotate camera without guidance |
| `private_setting_compromised` | Partner present — tests sensitive-topic adaptation |

## Verification Checklist

- [ ] Five tech-triage items scored separately.
- [ ] Camera-vs-screen eye contact distinguished from generic eye contact.
- [ ] Tele-exam maneuvers scored only when SP could actually perform them based on learner's instructions.
- [ ] Vague instructions ("can you show me where it hurts?") downgraded vs specific ("hold your phone six inches from your forearm, with a window or lamp behind your phone, not behind you").
- [ ] Red-flag escalation graded `n/a` if case had no red flag — not auto-credit.
- [ ] No invented telehealth platforms, scheduling, or pharmacy logistics.
- [ ] Modifier / POS documentation acknowledged in close (not a fake billing claim).
- [ ] Coaching names ONE improvement.

## Worked Example (compact)

**Input:** chief_complaint = `rash on left forearm, 3 days, mildly itchy, no fever`, setting = `urgent-care-telehealth`, patient_env = `kitchen, partner cooking in background, light from behind`, friction = `low_light, partner_visible`, tele_exam = `lighting, multiple angles, ruler/coin scale, blanching test, exam unaffected arm for comparison`, learner_level = `intern`, station_minutes = 12.

**Output (excerpt):**

```
[connection opens; patient backlit, face dark]
Learner: "Hi — I can see you but it's a little dark on my end. Could you turn so a light source is in front of you instead of behind? Maybe move toward the window."
SP: "Sure — like this?"
Learner: "Perfect, much better. Before we get into what's bringing you in: can you confirm your full name and date of birth for me?"
SP: "Anna Lopez, 8/14/1979."
Learner: "And can you tell me where you are physically right now — full address — so we know where to send help if anything came up during the visit?"
SP: "I'm at home, 412 Oak Street, Apartment 3B, Riverside."
Learner: "Thank you. I notice someone in the background — is it OK with you to talk about this with them there, or would you like privacy?"
SP: "That's my husband, it's fine."
Learner: "And this is being done by video — you're consenting to a telehealth visit today?"
SP: "Yes."
[history taking]
Learner: "Now I'd like to take a look at the rash. Hold the phone about 6 inches from your forearm, with the lamp behind the camera so the light falls on your arm — not on your face. Can you slowly rotate your arm so I see the front, side, and underside?"
SP: "Like this?"
Learner: "Yes. Can you grab a quarter or a ruler and put it next to one of the spots so I can judge size? ... Thank you. Now press one of the lesions firmly with your thumb for a second and lift — does the color go away under your finger or stay?"
SP: "It went pale and came back."
Learner: "Good — that's called blanching. Can you show me your right arm too, the same spot for comparison?"
[...]

>>> SCORECARD — Tech-triage opening

[✓] Audio + video
[✓] Identity verified
[✓] Location verified
[✓] Privacy check
[✓] Telehealth consent

>>> SCORECARD — Tele-physical exam

[✓] Lighting instruction
[✓] Multiple angles
[✓] Scale reference (quarter)
[n/a] Function demonstration
[✓] Comparison to unaffected side
[✓] Blanching test (case-specific maneuver)

>>> SCORECARD — Modality close

[✓] Plan summarized
[✓] Follow-up modality named (return to telehealth in 48h or sooner if spreading/fever)
[✓] Return precautions
[✓] Pharmacy routing
[~] Documentation of POS / modifier (not explicitly mentioned in close)

>>> COACHING

Single highest-yield improvement: explicitly verbalize when you're moving to the keyboard or chart ("I'm pulling up your chart for one second, I'm still listening"). The longest silence in this encounter was 18 seconds during typing — patient adapted, but on a less-tech-comfortable SP that would have read as disengagement.
```
