---
title: "Geriatric Encounter Rehearsal — Patient-First with Caregiver Present"
category: medical-education/learner-osce-skills
description: "Rehearse a geriatric encounter where the patient is present with a caregiver (spouse, adult child, paid aide). Learner is graded on patient-first orientation (address patient, not caregiver), sensory accommodation, cognitive screening when indicated (Mini-Cog, MoCA prompt, AD8), functional assessment (ADL/IADL), polypharmacy/Beers-class red flags, fall risk, advance care planning entry, and clarification of decision-making roles."
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
  - fellow
tags:
  - osce
  - geriatrics
  - caregiver
  - cognitive-assessment
  - polypharmacy
  - learner-tool
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/learner-osce-skills/osce_history_taking_rehearsal.md
  - domain-medical-education/learner-osce-skills/osce_pediatric_caregiver_interview_rehearsal.md
  - domain-medical-education/learner-osce-skills/osce_communication_breaking_bad_news_rehearsal.md
---

## Objective

Run a geriatric OSCE encounter with a caregiver in the room. Learner must address the patient first and primarily, accommodate sensory limitations, screen cognition with a validated short tool when indicated by the chief complaint, do a brief functional assessment (ADL + IADL), surface polypharmacy and Beers-class concerns, screen fall risk, open advance-care-planning where appropriate, and clarify who holds decision-making authority. Output: encounter transcript + scorecard.

## Your Role

You are the *patient* (older adult with named sensory and cognitive features), the *caregiver* (with their own anxieties and agenda), and the *rater*. As patient: stay in role per `cognitive_status` and `sensory_status`. As caregiver: realistic — sometimes helpfully filling gaps, sometimes inappropriately answering for the patient, sometimes carrying agenda the patient doesn't share. As rater: score the rubric.

## Inputs

- `patient_age`: integer (e.g., `82`)
- `chief_complaint_or_visit_reason`: free text (e.g., "increasing forgetfulness, daughter concerned," "fall last week," "depression follow-up," "med review after hospitalization," "annual wellness visit")
- `caregiver_role`: `spouse | adult-child | paid-aide | sibling | both-spouse-and-child`
- `cognitive_status`: `intact | mild-impairment | moderate-dementia | delirium-overlay`
- `sensory_status`: list — e.g., `hearing-aided | hearing-not-aided | low-vision | both`
- `decision_maker`: `patient | shared-with-named-surrogate | activated-DPOA`
- `med_list`: free text — count and at least one high-risk Beers-class medication if applicable (benzodiazepine, anticholinergic, sliding-scale insulin, NSAID, etc.)
- `learner_level`: `MS3 | MS4 | pa-student | nursing-student | intern | resident-junior | resident-senior | fellow`
- `station_minutes`: integer (default 12)

## Method

1. **Lock the case (CM-02).** Privately commit to: full med list with one Beers-class drug; one functional impairment (e.g., IADL: finances, medications, transportation); cognitive baseline; sensory baseline; advance-care-planning status (none / chat-only / completed POLST); caregiver agenda points.

2. **Open the station.** Greet *the patient* by surname first, then the caregiver. If sensory: speak at normal pace and volume, low-pitched, facing patient (lip-reading), in good light. Sit at eye level.

3. **Run patient-first expectations (the answer key).**
   - Address questions to the patient *first*, even if cognition is impaired.
   - Use the caregiver to verify or supplement — not replace — patient.
   - If patient defers ("ask my daughter"), still verify with patient: "and is that OK with you — for your daughter to tell me?"
   - Explicitly ask the patient what *they* want from the visit before turning to caregiver agenda.

4. **Run sensory accommodation expectations.**
   - Ask about hearing aids / glasses; ask if they are in / on.
   - Position face visible; do not block mouth.
   - Loop / amplification offered if no hearing aid present.
   - Written summary or large-font handout if low-vision.

5. **Run geriatric-specific scaffold (case-appropriate).**
   - Cognitive screen indicated by chief complaint (memory concern, fall, med error, change in function) → use a validated short tool (Mini-Cog, AD8, MoCA prompt with delayed recall).
   - Functional: at least 2 ADL + 2 IADL probed.
   - Falls: gait/balance question + one Timed Up-and-Go consideration + home environment + orthostatic check.
   - Polypharmacy: review of all meds + one Beers-class flag named if present.
   - Advance care planning: appropriate entry depending on stakes ("we don't have to decide today but I want to make sure I know what's important to you if something serious came up").

6. **Run failure-mode audit (NE-04).**
   - Speaking through the caregiver throughout.
   - Speaking loudly and slowly *without* checking sensory need ("elderspeak").
   - Asking caregiver "is mom OK with that?" before checking with mom.
   - Skipping cognitive screen when indicated.
   - Missing the Beers-class red flag.
   - Forcing ACP in a poorly-timed acute visit.

7. **End and score (DT-05).**

## Output Format

```
OSCE STATION — Geriatric Encounter
Patient age: [...]   Cognitive: [...]   Sensory: [...]   Decision-maker: [...]
Caregiver: [...]   Chief concern: [...]   Learner level: [...]   Station: [...] min

>>> ENCOUNTER TRANSCRIPT

Patient: [...]
Caregiver: [...]
Learner: [...]
[turn-by-turn]

>>> SCORECARD — Patient-first orientation

[ ✓ / ~ / ✗ ] Greeted patient by surname before caregiver
[ ✓ / ~ / ✗ ] Asked patient what they want from the visit
[ ✓ / ~ / ✗ ] Addressed questions to patient first
[ ✓ / ~ / ✗ ] Verified caregiver-supplied info with patient
[ ✓ / ~ / ✗ ] Did not use elderspeak
[ ✓ / ~ / ✗ ] Clarified decision-making role (patient/shared/surrogate)

>>> SCORECARD — Sensory accommodation

[ ✓ / ✗ ] Asked about hearing aids / glasses + their use today
[ ✓ / ✗ ] Faced patient with mouth visible
[ ✓ / ✗ ] Spoke at appropriate pace + pitch (not shouting)
[ ✓ / ✗ ] Offered amplification / large-font when relevant

>>> SCORECARD — Geriatric scaffold

[ n/a / ✓ / ~ / ✗ ] Cognitive screen used (Mini-Cog / AD8 / MoCA prompt)
[ ✓ / ~ / ✗ ] Function — ADL (≥ 2 probed)
[ ✓ / ~ / ✗ ] Function — IADL (≥ 2 probed)
[ ✓ / ~ / ✗ ] Fall risk (gait, environment, orthostatics)
[ ✓ / ~ / ✗ ] Med review + Beers-class flag named if applicable
[ ✓ / ~ / ✗ ] Advance care planning entry (where appropriate)

>>> SCORECARD — Failure-mode audit

[ count ] Speaking through caregiver throughout
[ count ] Elderspeak (loud, slow, "honey/sweetie")
[ count ] Asked caregiver before patient
[ count ] Skipped cognitive screen when indicated
[ count ] Missed Beers-class red flag
[ count ] Forced ACP in inappropriate setting

>>> COACHING (one paragraph)

Single highest-yield improvement: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `patient_age` | Anchor only — does not drive rubric |
| `cognitive_status` | intact / MCI / moderate dementia / delirium — drives screen + decision-making |
| `sensory_status` | hearing / vision combinations |
| `caregiver_role` | spouse / adult-child / paid-aide / both |
| `med_list` | Set Beers-class flag |
| `acute_event_overlay` | Recent fall / hospitalization / new med — changes priorities |
| `decision_maker` | patient / shared / activated-DPOA |
| `goals_of_care_window` | If `open`, expect ACP entry; if `acute_inappropriate`, learner should NOT push |

## Verification Checklist

- [ ] Patient and caregiver lines clearly separated.
- [ ] Patient-first scored on first-question target, not impression.
- [ ] Cognitive screen graded `n/a` if not indicated by case.
- [ ] Beers-class flag only marked if a Beers-class med was actually in the list — no fabrication.
- [ ] Elderspeak scored on verbatim phrases.
- [ ] Decision-making role explicitly verified, not inferred.
- [ ] ACP entry scored on whether the *timing* was right, not just whether it happened.
- [ ] No invented diagnoses or surrogate documents.
- [ ] Coaching names ONE improvement.

## Worked Example (compact)

**Input:** patient_age = `82`, chief_complaint = `daughter concerned about memory + missed pills`, caregiver = `adult-daughter`, cognitive = `mild-impairment`, sensory = `hearing-aided`, decision_maker = `patient`, med_list = `lisinopril, metformin, atorvastatin, ASA 81, lorazepam 0.5mg qhs prn for "bad nights"`, learner_level = `intern`, station_minutes = 12.

**Output (excerpt):**

```
Learner: "Mrs. Adesina, hello — I'm Dr. Park. (turns) And you must be Funke, her daughter. Mrs. Adesina, before anything else — what did you hope to talk about today?"
Mrs. Adesina: "Funke says I'm forgetting things. I think I'm fine."
Daughter: "Mom, you missed your pills three days last week and you couldn't remember the neighbor's name yesterday."
Learner: "Funke — thank you, I'll come back to you for examples. Mrs. Adesina, what's your sense — has anything felt different to you?"
Mrs. Adesina: "(thinks) ... maybe a little slower. But I'm 82 — that's normal, isn't it?"
Learner: "It can be — I want to do a quick test that takes a few minutes and gives us better information than guessing. Is that OK?"
[Mini-Cog: registers 3 words, draws clock 4/5 errors with hands, recalls 1 of 3 at delay]
Learner: "Thank you. Let me also ask about your day-to-day. Who handles the pills at home?"
Mrs. Adesina: "I do — but it's confusing now."
Learner: "And shopping, cooking, paying bills?"
Mrs. Adesina: "Funke helps with the bills."
[learner reviews med list with patient, names lorazepam, asks about sleep]
Learner: "Mrs. Adesina — when did you start the lorazepam, and how often are you taking it lately?"
Mrs. Adesina: "Every night now. It started after my husband passed."
Learner: "I understand. And I want to share — that medicine is one that, in our 80s, can affect memory and balance. I'd like us to plan a slow taper and find something safer for sleep. Funke, this is something you and I will check in on every few weeks. Mrs. Adesina, what do you think?"
[...]

>>> SCORECARD — Patient-first orientation

[✓] Greeted patient by surname first
[✓] Asked patient what she wanted
[✓] Addressed questions to patient first
[✓] Verified caregiver info with patient
[✓] No elderspeak
[✓] Decision-making role clarified (patient is decider)

>>> SCORECARD — Sensory accommodation

[✓] Asked re: hearing aids (in)
[✓] Face visible
[✓] Normal pace + pitch
[n/a] Vision

>>> SCORECARD — Geriatric scaffold

[✓] Cognitive screen — Mini-Cog performed and scored
[✓] ADL — bathing, dressing not directly asked (~)
[✓] IADL — meds, finances, shopping probed
[~] Fall risk — gait/orthostatics not probed
[✓] Med review + Beers-class flag (lorazepam)
[~] ACP — entry deferred; reasonable for first visit

>>> SCORECARD — Failure-mode audit

[0] Spoke through daughter throughout
[0] Elderspeak
[0] Asked daughter before mother
[0] Skipped cognitive screen
[0] Missed Beers flag
[0] Forced ACP

>>> COACHING

Single highest-yield improvement: fall risk. Lorazepam + 82yo + memory concern is a fall-and-fracture pathway. Sixty seconds for gait observation, orthostatics, and "have you fallen or come close to falling in the last year?" would have given you the data to weight the taper urgency.
```
