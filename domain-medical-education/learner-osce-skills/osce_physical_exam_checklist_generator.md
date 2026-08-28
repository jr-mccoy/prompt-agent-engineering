---
title: "Physical Exam Checklist Generator for Health-Professions Learners"
category: medical-education/learner-osce-skills
description: "Generate a region-specific physical exam checklist for a learner: setup, hygiene, sequence, technique calls, normal vs abnormal findings, special tests, and self-check cues for video review."
techniques:
  - ST-02
  - ED-01
  - CM-02
  - QA-01
difficulty: beginner
audience: learner
disciplines:
  - medicine
  - nursing
  - physician-assistant
  - allied-health
  - dental
intended_use: education-and-practice
tags:
  - physical-exam
  - clinical-skills
  - osce-prep
  - learner-self-study
  - checklist
updated: "2026-05-15"
related_prompts:
  - ./learner_osce_self_rehearsal.md
  - ./learner_history_taking_rehearsal.md
---

# Physical Exam Checklist Generator for Health-Professions Learners

**Objective:** Produce a learner-facing, region-specific physical exam checklist with explicit setup, hygiene, sequence, technique calls, normal-versus-abnormal framing, special tests, and post-exam summarization cues — usable for OSCE practice and for self-review when watching a recording of one's own attempt.

## When to Use
- ✅ OSCE / clinical-skills exam prep
- ✅ First exposure to a region's physical exam (e.g., first time learning the knee exam)
- ✅ Refreshing an exam between rotations
- ❌ Active patient care
- ❌ Designing exam teaching content — use educator-facing skills checklist designer

## Inputs Required
- **Discipline & learner level**
- **Exam region or system:** e.g., cardiac, pulmonary, abdominal, neuro screen, neuro detailed, MSK shoulder, MSK knee, MSK lumbar spine, thyroid, breast, GU male, GU female pelvic, prostate, pediatric well-child, oral exam (dental), cranial nerves
- **Focus level:** screening (rapid) vs focused (problem-driven) vs comprehensive
- **Special tests required (optional):** if learner needs specific provocative maneuvers (Lachman, Spurling, McMurray, Tinel, Hawkins, etc.)

## Constraints

**Must:**
- Open with setup and hygiene (introduction, role, consent, draping, hand hygiene, light/position)
- Organize sequence: inspection → palpation → percussion → auscultation, or the standard sequence for the region (e.g., MSK: inspection → palpation → ROM → special tests → neurovascular)
- Pair each technique call with what is being looked for, normal finding, and abnormal finding(s) that matter
- List special tests with the indication and what a positive means
- Include a closing: re-cover patient, summarize findings, thank the patient
- Add self-review cues a learner can use when watching their own recording

**Must Not:**
- Produce real-patient guidance for live clinical decision-making
- Imply that an examination substitutes for imaging or labs when the latter is indicated
- Use sexualized or non-consensual phrasing for sensitive exams; default to standard professional language and chaperone reminders

## Instructions

1. **Confirm exam region and focus level.** Calibrate detail accordingly: a screening cardiac exam is 60-90 seconds, a comprehensive cardiac exam is 4-6 minutes.

2. **Open with setup and hygiene block.** A short list: introduction, identity check, consent, hand hygiene, room setup, patient position, draping/exposure, chaperone reminder where appropriate.

3. **Produce the sequenced checklist.** For each maneuver:
   - **Technique call** (one phrase, what the learner would say aloud)
   - **What you're examining for**
   - **Normal finding**
   - **Abnormal findings that matter** (1-3 items)
   - **Common technique errors**

4. **Special tests section.** Each test:
   - Indication
   - Setup and maneuver
   - What positive looks like (clearly, not vaguely)
   - Sensitivity/specificity *only if* the learner brings a verified source; otherwise qualitative ("moderately specific")

5. **Closing block.** Re-cover patient, summarize findings concisely, ask if any questions, thank, and wash hands on exit.

6. **Self-review cues** for watching one's own recording:
   - Did you state the technique call out loud?
   - Did you pause for the patient's response or comfort?
   - Were maneuvers in the standard sequence?
   - Did you skip steps because you "already knew" the answer?
   - Did you re-cover and summarize?

7. **Calibration note.** A brief paragraph: when is the screening sequence sufficient, when do you need the focused or comprehensive version, and what triggers a transition mid-exam?

8. **Self-check block:**
   - State the standard sequence (inspection → palpation → … ) from memory
   - Name two abnormal findings for this region you'd most want to catch
   - Name one common technique error you'll guard against next time

## Discipline-Specific Anchors

| Discipline | Notes |
|---|---|
| Medicine / PA | Full sequence; problem-driven focus on abnormality |
| Nursing | Functional and safety-focused (e.g., gait + falls in older adult assessment; skin assessment in pressure-injury screen) |
| Allied health (PT) | Joint-specific MSK exam + neurovascular + functional movement |
| Allied health (OT) | Functional motor + sensory + cognitive screen relevant to ADLs |
| Dental | Extra/intra-oral exam, periodontal probing, occlusion, lymph nodes |

## False-Positive Prevention

| ❌ Common Mistake | ✅ Correct Approach |
|---|---|
| List maneuvers without what you're looking for | Always pair technique call with what's being examined |
| Skip the setup block | Setup is often where OSCE points are won or lost |
| Vague "positive" definition for special tests | Make positive concrete (e.g., Lachman: anterior tibial translation without firm endpoint compared to other side) |
| Invent sensitivity/specificity numbers | Qualitative unless learner brings a verified source |
| One-size-fits-all sequence | Calibrate to screening / focused / comprehensive |
| No chaperone reminder for sensitive exams | Always include for breast, GU, pelvic, rectal exams |

## Output Format

```
### Exam Region / Focus Level / Discipline
<inputs>

### Setup & Hygiene
- Introduction / consent / hand hygiene / position / draping / chaperone reminder

### Sequenced Checklist
1. Technique call → looking for → normal → abnormal(s) → common error
2. ...

### Special Tests
- Test name → indication → maneuver → positive looks like → qualitative usefulness

### Closing
- Re-cover, summarize, ask if questions, thank, wash hands

### Self-Review Cues for Recording Review
- 5 cues

### Calibration Note
- When to use screening vs focused vs comprehensive

### Self-Check
1. Standard sequence (from memory)
2. Two abnormals you'd most want to catch
3. One technique error to guard against
```

## Verification Checklist
- [ ] Setup and hygiene block present
- [ ] Each maneuver paired with what / normal / abnormal / common error
- [ ] Special tests have concrete "positive looks like" descriptions
- [ ] No invented sensitivity/specificity numbers
- [ ] Closing block present
- [ ] Self-review cues for recording review
- [ ] Chaperone reminder where appropriate
- [ ] Real-patient redirect language present
