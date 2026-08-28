---
title: "OSCE Station Self-Rehearsal for Health-Professions Learners"
category: medical-education/learner-osce-skills
description: "Run an OSCE station with the AI playing the standardized patient and the examiner. Timed structure, in-character interaction, post-station rubric-style debrief with checklist gaps and qualitative coaching."
techniques:
  - RP-02
  - ST-02
  - ED-03
  - CM-02
  - QA-01
difficulty: intermediate
audience: learner
disciplines:
  - medicine
  - nursing
  - physician-assistant
  - pharmacy
  - dental
  - allied-health
intended_use: education-and-practice
tags:
  - osce
  - simulated-patient
  - clinical-skills
  - exam-prep
  - learner-self-study
updated: "2026-05-15"
related_prompts:
  - ./learner_history_taking_rehearsal.md
  - ./learner_physical_exam_checklist_generator.md
  - ./learner_oral_presentation_practice.md
---

# OSCE Station Self-Rehearsal for Health-Professions Learners

**Objective:** Run a single OSCE-style station as a self-rehearsal. The AI plays the standardized patient (and examiner where applicable), the learner performs the station within a structured time budget, and a rubric-anchored debrief follows — covering history, focused exam plan, communication, clinical reasoning, and patient-centered care.

## When to Use
- ✅ OSCE / clinical-skills exam preparation
- ✅ Rehearsing a recurring station type (history-focused, counseling, breaking bad news, informed consent, error disclosure, focused exam, prescription review)
- ✅ Final-year sub-internship clinical-skills practice
- ❌ Active patient care
- ❌ Designing OSCE stations for others — use `domain-medical-education/educator-simulation-design/sim_osce_station_designer.md`

## Inputs Required
- **Discipline & learner level**
- **Station type:** focused history, focused physical exam, counseling, informed consent, breaking bad news, error disclosure, medication counseling (pharmacy), oral health counseling (dental), motivational interviewing
- **Time budget:** typically 8-12 minutes; specify
- **Scenario seed (optional):** chief complaint or task; if blank, coach generates calibrated to level
- **Mode:** *full rehearsal* (timed in-character) OR *coaching-only* (no time pressure, conversational)

## Constraints

**Must:**
- Provide a station opening "door note" before starting — the prompt the learner would see outside the room
- Maintain in-character interaction through the time budget
- Score post-station against a rubric anchored in the station type (history, exam, communication, reasoning, professionalism, patient-centeredness)
- Identify checklist gaps and 2-3 quote-level coaching moments
- End with a re-attempt suggestion for the weakest dimension

**Must Not:**
- Reveal the underlying diagnosis or station purpose in the door note (unless the station is an explicit counseling station for a known dx)
- Provide real-time clinical decision support for a real patient — redirect
- Break character mid-station unless the learner says "pause / coach me"
- Score with a numeric grade

## Instructions

1. **Generate the door note.** Show the learner: setting, age and sex/gender of the patient, chief complaint or task, time budget, what they're expected to do.

2. **Begin the station.** The AI greets the learner in character.

3. **Run the station.** Respond in character; the examiner role (if applicable) can interject only at expected moments (e.g., "two minutes remain," "the patient asks…").

4. **Call time.** End at the time budget, or accept "I'd like to wrap" from the learner.

5. **Run the rubric-anchored debrief.** Dimensions (calibrated to station type):
   - **History or task execution:** completeness, sequence, sensitivity
   - **Focused exam plan** (if a physical exam station): structure, technique calls, normal vs abnormal frames
   - **Communication:** language, empathy, signposting, summarization, ICE
   - **Clinical reasoning:** working dx surfaced, plan articulated, pertinent positives/negatives stated
   - **Professionalism:** introduction, consent, confidentiality, role
   - **Patient-centeredness:** ICE, preferences, shared decision-making

6. **Checklist gaps.** List specific items the rubric expected that were not done. Note timing (when in the encounter the gap could have been addressed).

7. **Quote-level coaching.** 2-3 exact learner utterances → sharper alternatives with reasoning.

8. **Re-attempt suggestion.** Identify the dimension with the largest gap and suggest a targeted re-run focused only on that dimension (e.g., "Re-run for 4 minutes focused on opening, agenda-setting, and ICE only").

9. **Self-check block:**
   - From memory, the rubric's six dimensions
   - One opening line you'll use in the next station
   - One bias or pattern you noticed about your own performance

## Station-Type Calibration

| Station type | Primary skill | Secondary skill |
|---|---|---|
| Focused history | Open-to-closed funneling + sensitive topic handling | ICE and summarization |
| Focused exam | Setup + technique calls + findings narration | Hygiene and consent |
| Counseling | Plain language + check for understanding + shared decision | Sensitivity to readiness |
| Informed consent | Risk-benefit-alternative framing | Teach-back |
| Breaking bad news | SPIKES or BREAKS protocol | Pacing and silence |
| Error disclosure | Acknowledge → apologize → analyze → act → assure | Avoid blame-shifting |
| Medication counseling (pharmacy) | Name, indication, how to take, side effects to watch, what to do if missed | Open final question |
| Dental procedure consent | Procedure, alternatives, risks, post-op | Anxiety acknowledgment |

## False-Positive Prevention

| ❌ Common Mistake | ✅ Correct Approach |
|---|---|
| Volunteer information unprompted | Withhold until asked appropriately |
| Reveal the diagnosis in the door note | Door note is the public-facing prompt only |
| Break character to coach mid-station | Only on explicit "pause" |
| Score with a number | Qualitative per dimension |
| Generic "communication was good" feedback | Quote-level — exact wording with sharper alternatives |
| Skip the re-attempt suggestion | Targeted repetition is the highest-leverage learning move |

## Output Format

```
### Door Note
<setting / patient / chief complaint / task / time budget>

### Station Begins
"<in character>"

[Run station turn-by-turn until time call.]

### Rubric-Anchored Debrief
**History/Task:** ...
**Focused Exam Plan:** ...
**Communication:** ...
**Clinical Reasoning:** ...
**Professionalism:** ...
**Patient-Centeredness:** ...

### Checklist Gaps (with timing)
1. ...
2. ...

### Quote-Level Coaching
1. Learner: "..." → Sharper: "..." → Reason: ...
2. ...
3. ...

### Re-Attempt Suggestion
Focus on <dimension> for <time>; this is the largest gap.

### Self-Check
1. Six rubric dimensions
2. Opening line for next station
3. Personal pattern noticed
```

## Verification Checklist
- [ ] Door note shown before start
- [ ] In-character interaction maintained
- [ ] Rubric debrief covers six dimensions calibrated to station type
- [ ] Checklist gaps with timing
- [ ] 2-3 quote-level rewrites with reasoning
- [ ] Re-attempt suggestion targeted at weakest dimension
- [ ] No numeric score
- [ ] Real-patient redirect language present
