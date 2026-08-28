---
title: "Problem-Based Learning Case Writer"
category: medical-education/educator-case-writing
description: "Generate complete PBL cases with progressive trigger packets, guiding questions, facilitator guide, and learning objectives mapped to competencies for any learner level and clinical domain."
techniques:
  - ST-02
  - ED-01
  - CM-02
  - RT-03
  - QA-01
difficulty: intermediate
tags:
  - pbl
  - case-writing
  - clinical-education
  - curriculum-design
  - facilitator
  - competency-alignment
updated: "2026-05-15"
related_prompts:
  - ../meded_progressive_disclosure_case_designer.md
  - ../meded_small_group_facilitation_guide.md
  - ../meded_tbl_application_exercise_designer.md
---

# Problem-Based Learning Case Writer

**Objective:** Generate a complete, curriculum-ready PBL case with three progressive trigger packets, Bloom's-tagged guiding questions, learning objective mapping, and a facilitator guide calibrated to the specified learner level.

## When to Use
- ✅ Designing a new PBL case for a preclinical or clinical curriculum
- ✅ Retrofitting a lecture-based topic into a self-directed discovery format
- ✅ Building a facilitated small-group session where students drive inquiry
- ✅ Aligning existing case content to ACGME/CanMEDS/EPA competency frameworks
- ❌ When you need a single worked clinical vignette for exam review — use a progressive disclosure case or NBME-style MCQ writer instead
- ❌ When learner groups are larger than 8-10 students and simultaneous reporting is required — use a TBL application exercise instead

## Inputs Required
- **Learner level:** M1, M2, M3, M4, Resident PGY-1 to PGY-3, Fellow, or Advanced Practice Learner
- **Clinical domain / specialty:** e.g., Internal Medicine, Pediatrics, Family Medicine, Neurology
- **Presenting complaint:** the chief symptom or clinical problem the case centers on (e.g., "acute chest pain," "failure to thrive in a 9-month-old")
- **Intended learning objectives (optional):** if the educator has pre-specified 3-5 LOs, include them; otherwise the prompt will generate them from the case content
- **Competency framework to align to:** ACGME Milestones, CanMEDS Roles, EPA (Entrustable Professional Activities), or custom institutional framework
- **Session length:** typical PBL sessions are 90-120 minutes; specify if shorter or longer

## Constraints

**Must:**
- Produce exactly three trigger packets, sequenced in clinical discovery order
- Include at least one open-ended guiding question per packet tagged with Bloom's taxonomy level
- Map every learning objective to the trigger packet that is designed to surface the knowledge gap
- Include a complete facilitator guide with facilitation moves, misconception signals, and redirect strategies
- Suggest at least three self-directed learning (SDL) tasks for learners to complete before the next session
- Calibrate case complexity and clinical detail to the specified learner level

**Must Not:**
- Reveal the primary diagnosis in Packet 1 — Packet 1 exists to generate hypotheses, not recognition
- Embed all information needed to answer the guiding questions — strategic knowledge gaps drive SDL
- Write guiding questions with single correct factual answers — PBL questions must be generative and open
- Use jargon or diagnostic labels in Packet 1 that prematurely narrow the differential
- Present a case so rare that it fails to build transferable illness scripts for common presentations (unless explicitly requested)

## Instructions

1. **Collect inputs from the educator.**
   - Ask for: learner level, clinical domain, presenting complaint, any pre-specified learning objectives, competency framework, and session length.
   - If the educator provides a draft clinical scenario, extract the key clinical facts and restructure them into the three-packet format below.
   - Confirm whether the case should represent a common presentation (builds schema for common disease) or a variant presentation (tests schema flexibility).

2. **Draft the case backbone.**
   - Write a complete patient backstory (demographics, setting, timeline) that you will reveal progressively across packets.
   - Choose a diagnosis that is educationally productive for the stated learner level — avoid both trivially obvious and unreasonably obscure diagnoses.
   - Identify 5-7 key learning objectives the case will address. For M1-M2: emphasize basic science mechanisms and pathophysiology. For M3-M4: emphasize clinical reasoning, diagnosis, and management. For residents: emphasize evidence-based management, complications, and system-level issues.

3. **Write Trigger Packet 1: Minimal Information.**
   - Include: patient age, sex, clinical setting (ED, clinic, floor), chief complaint, vital signs (if relevant), and one sentence of context.
   - Do NOT include: any history beyond chief complaint, physical exam findings, or laboratory data.
   - Write 2-3 guiding questions that generate hypothesis formation. Each question must:
     a. Be open-ended and generative (not factual recall)
     b. Be tagged with Bloom's level (e.g., [Bloom's: Analysis])
     c. Map to one or more of the stated learning objectives
   - Write one "Packet 1 Learning Objective Trigger" note for the facilitator: what knowledge gap this packet is designed to expose.

4. **Write Trigger Packet 2: History, Examination, and Initial Data.**
   - Include: HPI, relevant past medical history, medications, allergies, social/family history, review of systems, physical examination findings, and initial laboratory or imaging results.
   - Design the data set to narrow the differential but not resolve it — one or two findings should genuinely surprise learners and require hypothesis revision.
   - Write 3-4 guiding questions at higher Bloom's levels (Application, Analysis, Evaluation).
   - Flag 2-3 SDL tasks for learners to pursue independently: specific mechanisms, pathophysiology, diagnostic criteria, or evidence-based guidelines they will need for Packet 3.

5. **Write Trigger Packet 3: Evolution, Resolution, and Debrief.**
   - Include: disease evolution (treatment response, complications, or clinical course), final diagnosis confirmation if appropriate, and outcome.
   - Write 3-5 reflective debrief questions that operate at Synthesis and Evaluation levels:
     a. At least one question that surfaces underlying mechanism ("Why did this patient present this way?")
     b. At least one question that links to management decisions ("What would you have done differently if X finding was absent?")
     c. At least one question that generalizes to the illness script ("What clinical features distinguish this from [closest competing diagnosis]?")
   - Write 2 synthesis SDL tasks: literature to read, guidelines to review, or clinical pearls to formulate.

6. **Write the Learning Objective Map.**
   - Create a table with columns: Learning Objective | Packet Where Surfaced | Bloom's Level | Competency Domain
   - Every LO must appear in the table. Competency domain should reference the specified framework (e.g., ACGME: Patient Care, Medical Knowledge; CanMEDS: Medical Expert, Scholar; EPA number).

7. **Write the Facilitator Guide.**
   For each trigger packet, write:
   - **Facilitation moves:** 2-3 specific phrases or questions the facilitator uses to open discussion, prompt hypothesis generation, and deepen analysis (not just "what do you think?").
   - **Tangent redirects:** 2 common tangents this case invites (e.g., students focusing on management before diagnosis is established) and scripted language to redirect.
   - **Misconception signals:** 2 specific misconceptions this case commonly surfaces, and the facilitator's response move (redirect question, not correction lecture).
   - **Pacing notes:** how to read the room and decide when to advance to the next packet.

8. **Write Self-Directed Learning (SDL) Task List.**
   - Compile all SDL tasks from Packets 1-3 into a clean learner-facing list.
   - Each task should specify: topic, suggested resource type (textbook, guideline, UpToDate, primary literature), and estimated time.
   - Do not name specific URLs — name resource types and guideline organizations (e.g., "ACC/AHA guidelines," "WHO clinical manual").

9. **Apply calibration check before finalizing.**
   - M1/M2 cases: confirm basic science concepts (physiology, pathology, pharmacology mechanisms) are surfaceable from the guiding questions.
   - M3/M4 cases: confirm clinical reasoning steps (history → differential → exam hypothesis testing → data interpretation → management) are exercised.
   - Resident cases: confirm management nuance, complications, and evidence-base are exercised.
   - If calibration reveals a mismatch, revise packet content before output.

10. **Format and deliver the complete case.**
    - Use the output format below.
    - Add a brief educator note at the top summarizing the case's educational purpose and estimated facilitation time per packet.

## False-Positive Prevention

| ❌ Common Mistake | ✅ Correct Approach |
|---|---|
| Revealing the diagnosis in Packet 1 via specific symptoms or terminology (e.g., "crushing substernal chest pain radiating to the jaw" in a cardiac case) | Packet 1 should generate 5-8 competing hypotheses, not recognition of a single diagnosis |
| Embedding all the information needed to answer guiding questions inside the packet text | Knowledge gaps are intentional — guiding questions should require SDL to answer well |
| Writing guiding questions with single correct factual answers (e.g., "What is the most common cause of chest pain?") | PBL questions should be open and generative ("What physiologic mechanisms could explain this patient's symptoms?") |
| Writing an M1 case at clinical reasoning depth appropriate for M3 learners | M1 cases must anchor to basic science; clinical details should map to organ system physiology, not diagnostic algorithms |
| Making Packet 3 just a reveal of the diagnosis without debrief questions | The debrief drives metacognition and schema consolidation — it is not optional |
| Using a rare disease as the primary case content for novice learners | Illness script richness requires prior exposure to common variants; novices need schema-building, not schema-testing |

## Output Format

The output should be organized in the following sections, each clearly headed:

### Educator Overview
- Case name, clinical domain, learner level, estimated session time, primary educational purpose

### Learning Objectives
- Numbered list of 5-7 learning objectives, each tagged with Bloom's level and competency domain

### Trigger Packet 1: [Descriptive Title]
- Patient presentation (demographic, setting, chief complaint, vitals)
- Guiding Questions (numbered, each tagged with Bloom's level)
- Facilitator Note: Packet 1 Knowledge Gap Target

### Trigger Packet 2: [Descriptive Title]
- Full history, physical exam, initial investigations
- Guiding Questions (numbered, each tagged with Bloom's level)
- SDL Tasks for Packet 2 Gap

### Trigger Packet 3: [Descriptive Title]
- Clinical evolution, diagnosis confirmation, outcome
- Reflective Debrief Questions (numbered, tagged)
- Synthesis SDL Tasks

### Learning Objective Map
- Table: LO | Packet | Bloom's Level | Competency Domain

### Facilitator Guide
- Per-packet subsections: Facilitation Moves | Tangent Redirects | Misconception Signals | Pacing Notes

### SDL Task List (Learner-Facing)
- Compiled task list with topic, resource type, estimated time

---

## Example Output Snippet

The following is an example of **Trigger Packet 1** for an M2 Internal Medicine PBL case on a patient presenting with dyspnea:

---

**Trigger Packet 1: A Breathless Arrival**

> Mr. T.K. is a 58-year-old man who arrives to the emergency department by ambulance. He reports that he has been short of breath for the past three days, and that tonight "it got much worse." His oxygen saturation on room air is 88%. His respiratory rate is 26 breaths per minute. He is sitting upright on the stretcher and appears visibly uncomfortable.

**Guiding Questions:**

1. What organ systems could account for this patient's acute dyspnea and hypoxia? Generate at least four mechanistically distinct hypotheses. [Bloom's: Analysis]

2. What additional information would most efficiently differentiate among your hypotheses — and why does the sequence of inquiry matter? [Bloom's: Evaluation]

3. What physiologic mechanism explains why this patient's oxygen saturation is 88% on room air rather than the expected 95-100%? [Bloom's: Application]

**Facilitator Note — Packet 1 Knowledge Gap Target:** This packet is designed to expose gaps in learners' understanding of the four mechanisms of hypoxia (V/Q mismatch, diffusion impairment, shunt, hypoventilation). SDL before Packet 2 should address these mechanisms and their discriminating clinical features.

---

## Verification Checklist
- [ ] Learner level explicitly specified and calibrated throughout all three packets
- [ ] Competency framework alignment named and reflected in the LO map (ACGME/CanMEDS/EPA)
- [ ] Facilitator guide included with facilitation moves, misconception signals, and redirect language for each packet
- [ ] Diagnosis not revealed in Packet 1 — differential generation is required
- [ ] All guiding questions are open-ended and tagged with Bloom's taxonomy level
- [ ] SDL tasks are specific, feasible, and tied to knowledge gaps exposed by each packet
- [ ] Packet 3 includes reflective debrief questions, not just a diagnosis reveal
- [ ] Learning Objective Map is complete with every LO mapped to a packet and competency domain
