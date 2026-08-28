---
title: "Progressive Disclosure Clinical Case Designer"
category: medical-education/educator-case-writing
description: "Design sequential clinical cases where information is revealed in clinical order, requiring learners to commit to intermediate diagnoses and management steps before receiving subsequent data — building probabilistic clinical reasoning and illness script richness through structured diagnostic commitment."
techniques:
  - ST-02
  - RT-03
  - ED-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - progressive-disclosure
  - clinical-reasoning
  - sequential-case
  - diagnostic-reasoning
  - commitment-to-diagnosis
  - medical-education
updated: "2026-05-15"
related_prompts:
  - ../meded_pbl_case_writer.md
  - ../meded_virtual_patient_case_builder.md
  - ../meded_debriefing_guide_designer.md
---

# Progressive Disclosure Clinical Case Designer

**Objective:** Design a sequential clinical case that reveals information in clinical discovery order, requiring explicit diagnostic commitment at each phase before subsequent data is disclosed — developing probabilistic reasoning, hypothesis revision skills, and illness script richness calibrated to the specified learner level.

## When to Use
- ✅ Teaching clinical reasoning through structured hypothesis generation and revision
- ✅ Demonstrating how diagnostic probability shifts as clinical information accumulates
- ✅ Building illness scripts by repeatedly exercising the pattern of presentation → hypothesis → examination → revision
- ✅ Running a facilitated large-group session (modified Socratic case) or small-group tutorial where the educator controls information release
- ✅ Creating an asynchronous self-study case where learners write their commitments before advancing to the next phase
- ❌ When the presenting complaint is pathognomonic — if the diagnosis is identifiable from the chief complaint alone, progressive disclosure adds no cognitive work
- ❌ When learners are true novices with no prior exposure to the clinical domain — illness script formation requires minimal prior knowledge; do not use rare or complex presentations for learners with no foundational exposure
- ❌ When the primary goal is procedural decision-making (e.g., "which surgical approach") rather than diagnostic reasoning — use simulation or virtual patient formats for procedural decisions

## Inputs Required
- **Learner level:** M1, M2, M3, M4, Resident PGY-1 to PGY-3, Fellow, or Attending (for CME)
- **Clinical domain / specialty:** e.g., Internal Medicine, Neurology, Pediatrics, Obstetrics
- **Presenting complaint:** the symptom or syndrome anchoring the case (e.g., "acute onset headache," "three-week history of progressive dyspnea")
- **Target diagnosis:** the final diagnosis the case resolves to; this is kept internal and drives case design
- **Top competing diagnoses:** 2-3 diagnoses that should be active differentials throughout the case before the final diagnosis is confirmed
- **Learning objectives:** 3-5 specific LOs; at minimum one should be diagnostic reasoning, one clinical knowledge, one management
- **Commitment format preference:** written (individual journal), verbal (cold-call), whiteboard (group), or digital (response system) — this determines facilitation instructions
- **Illness script / semantic qualifier focus:** optional — if the educator wants the case to specifically build one illness script (e.g., "typical vs. atypical MI," "central vs. peripheral vertigo"), name it here

## Constraints

**Must:**
- Reveal information in strict clinical order: History only → Physical Exam → Initial Investigations → Specialist/Advanced Data → Resolution
- Require explicit diagnostic commitment (written or verbal, individual or group) before each phase is disclosed
- Design Phase 1 around probabilistic ambiguity — the chief complaint should generate a meaningful differential, not recognition of a single diagnosis
- Include facilitation prompts for each phase transition (what the educator says to bridge phases and frame the commitment task)
- Include an illness script alignment note: which illness script pattern this case is designed to build or test
- Include reflective debrief questions in Phase 5 that operate at synthesis and metacognition levels

**Must Not:**
- Reveal pathognomonic findings in Phase 1 — the cognitive work is in probabilistic reasoning through ambiguous data, not pattern recognition from a single symptom cluster
- Skip commitment steps between phases — diagnostic commitment before revelation creates the cognitive dissonance that drives learning; without it, progressive disclosure is just sequential narration
- Use a zebra (rare disease) case as the primary content for novice learners — novices need schema-building with common presentations before schema-testing with rare ones
- Make Phase 5 (Resolution) a simple factual summary — the debrief must surface metacognition ("What were you thinking when you saw the potassium level?"), not just correct answers
- Conflate the facilitator guide with the learner materials — they are separate outputs; learners never see the facilitator guide

## Instructions

1. **Collect inputs from the educator.**
   - Confirm: learner level, clinical domain, presenting complaint, target diagnosis, top 2-3 competing diagnoses, 3-5 LOs, commitment format, and any illness script focus.
   - Ask whether the case will be used in: (a) facilitated group setting with real-time educator control, (b) small group with student-led disclosure (student facilitator model), or (c) asynchronous self-study. Each use modality changes the facilitation guide format.
   - Ask whether the educator wants a clinical "red herring" — a finding in Phase 2 or 3 that is present but not causally related to the diagnosis, designed to test anchoring and premature closure.

2. **Design the case backbone.**
   - Write the complete patient truth document: all clinical facts, the final diagnosis, the relevant pathophysiology, and the key management decisions — this is the pool from which you will selectively reveal information across phases.
   - Sequence the information release so that each phase reveals the next most clinically logical type of data — mirroring how a clinician actually encounters a patient.
   - Plan which competing diagnoses should be plausible after each phase, and what finding in the subsequent phase most significantly updates their probability.

3. **Write Phase 1 — History Only.**
   - Include: chief complaint, HPI (onset, duration, quality, location, radiation, severity, modifying factors, associated symptoms), pertinent negatives from the history, relevant past medical history, medications, allergies, social history, family history.
   - Do NOT include: any physical examination findings, vital signs beyond what was obtained at triage, or laboratory data.
   - Write the Phase 1 commitment task: "Based on the history alone, write your top 3 differential diagnoses in order of probability. For each, state one piece of history that supports it and one piece that argues against it."
   - Write the Phase 1 facilitation prompt: the educator's bridge statement before handing out Phase 2 (e.g., "Hold your differentials in mind. What would you most want to examine on this patient to move these probabilities?").
   - Write the illness script / semantic qualifier note: which semantic qualifiers in the history should be activating a particular illness script pattern (e.g., "sudden onset" activates vascular; "progressive over weeks" activates neoplastic/inflammatory).

4. **Write Phase 2 — Physical Examination.**
   - Include: general appearance, vital signs, and all relevant physical exam findings by system.
   - Design the examination findings to: (a) narrow the differential by increasing probability of 1-2 diagnoses and decreasing probability of others, and (b) introduce at least one unexpected or surprising finding that requires hypothesis revision.
   - If a red herring was requested, introduce it here as a physical finding that is present but does not drive the diagnosis (e.g., a benign heart murmur in a patient presenting with dyspnea caused by pulmonary embolism).
   - Write the Phase 2 commitment task: "Revise your differential. State your probability estimates (high/moderate/low) for each diagnosis and explain which exam findings most changed your thinking."
   - Write the Phase 2 facilitation prompt: bridge to Phase 3.

5. **Write Phase 3 — Initial Investigations.**
   - Include: laboratory results, basic imaging (X-ray, ECG, point-of-care ultrasound), and initial diagnostic tests relevant to the clinical context.
   - Design the investigation results to: (a) confirm or exclude 1-2 remaining competing diagnoses, and (b) narrow to 1-2 remaining working diagnoses without yet fully confirming the final diagnosis.
   - Write the Phase 3 commitment task: "State your working diagnosis and initial management plan. What additional testing or consultation would you order, and why?"
   - Write the Phase 3 facilitation prompt: bridge to Phase 4.
   - Write an anchoring check note for the facilitator: at this point, learners who are anchoring on an early hypothesis may be resistant to revising despite new data — specify the anchoring pattern to watch for and a Socratic redirect question.

6. **Write Phase 4 — Advanced Investigations and Clinical Evolution.**
   - Include: specialist consultation results, advanced imaging (CT, MRI, echocardiogram), pathology, or microbiology results that confirm the final diagnosis.
   - Include 1-2 sentences of clinical evolution: how the patient's condition has changed since Phase 3 (stable, improving, deteriorating) and any new symptoms that have emerged.
   - Write the Phase 4 commitment task: "Revise your management plan based on the confirmed diagnosis. What treatment do you initiate, and what complications should you monitor for?"
   - Write the Phase 4 facilitation prompt: bridge to Phase 5.

7. **Write Phase 5 — Resolution and Debrief.**
   - Include: patient outcome (24-72 hour course), final disposition (discharge, continued hospitalization, specialist handoff), and one sentence of epidemiological context (how common is this presentation? what is the prognosis?).
   - Write 4-6 reflective debrief questions. The questions must operate at Synthesis and Evaluation levels and include:
     a. A metacognition question: "At which point were you most confident in your diagnosis — and were you right to be?" [Bloom's: Evaluation]
     b. A mechanism question: "What pathophysiologic mechanism explains [the surprising finding in Phase 2]?" [Bloom's: Analysis]
     c. A management decision question: "If [one finding] had been absent, how would your management have differed?" [Bloom's: Synthesis]
     d. An illness script generalization question: "What are the three features that distinguish [final diagnosis] from [closest competing diagnosis] at the bedside?" [Bloom's: Synthesis]
     e. A self-regulated learning question: "What gap in your knowledge did this case expose, and what will you do about it in the next 24 hours?" [Bloom's: Evaluation]

8. **Write the Facilitation Guide (Educator Only — Not Shared with Learners).**
   - For each phase, write:
     a. Opening move: the educator's framing statement before revealing the phase
     b. Commitment facilitation: how to collect commitments (cold-call, pair-share, whiteboard, response system) and what to do if learners are reluctant to commit
     c. Bridge to next phase: the educator's statement after collecting commitments and before revealing the next phase
     d. Anticipated tangents: 2 likely tangents at this phase and scripted redirect language
     e. Anchoring watch: the specific hypothesis learners are most likely to anchor on at this phase and a question to disrupt it

9. **Write the Illness Script and Semantic Qualifier Alignment Notes.**
   - Write a brief educator note explaining which illness script this case is designed to build, strengthen, or test.
   - List 3-5 semantic qualifiers that appear in the case and explain what diagnostic category each activates (e.g., "sudden onset" → vascular; "young woman with relapsing-remitting symptoms" → demyelinating; "immunocompromised host" → opportunistic).
   - Write a "schema transfer" note: what other presentations would exercise the same illness script and could be assigned as self-study after the case.

10. **Format and deliver the complete case.**
    - Produce separate learner-facing documents and facilitator documents — never combine them.
    - If the use modality is asynchronous self-study, add instructions to the learner document explaining how to use the commitment steps without a live facilitator.

## False-Positive Prevention

| ❌ Common Mistake | ✅ Correct Approach |
|---|---|
| Revealing pathognomonic findings in Phase 1 (e.g., "malar rash and joint pain" for lupus) | Phase 1 should generate a meaningful differential of 5-8 competing hypotheses; diagnostic recognition from Phase 1 eliminates the cognitive work the case is designed to exercise |
| Skipping commitment steps between phases ("here's more information") | Diagnostic commitment before data revelation creates the productive cognitive dissonance that drives learning; without it, learners passively receive information rather than actively reasoning |
| Using a zebra presentation for novice learners | Schema-building requires repeated exposure to common presentations; save rare variants for learners who have established the common illness script |
| Making Phase 5 a factual summary ("the diagnosis was X and the treatment is Y") | The debrief questions surface metacognition and generalization — "correct answer" transmission alone wastes the experiential learning context |
| Designing Phase 2 to confirm the diagnosis rather than refine probabilities | Each phase should increase or decrease probability of competing diagnoses without resolution; final confirmation belongs in Phase 4 |
| Combining the facilitator guide with the learner materials | Learners who see facilitation moves, anticipated tangents, and debrief frameworks lose the productive uncertainty that drives inquiry |

## Output Format

The output should be organized into two clearly labeled documents:

### LEARNER DOCUMENT

#### Case Overview (Learner)
- Domain, learner level, clinical context (no diagnosis revealed)

#### Phase 1 — History Only
- HPI, PMH, medications, allergies, social history, family history, ROS
- Commitment Task 1 (written prompt)

#### Phase 2 — Physical Examination
- Vital signs, general appearance, full examination by system
- Commitment Task 2 (written prompt)

#### Phase 3 — Initial Investigations
- Laboratory results, ECG, basic imaging, point-of-care tests
- Commitment Task 3 (written prompt)

#### Phase 4 — Advanced Investigations and Clinical Evolution
- Advanced imaging, specialist results, clinical course update
- Commitment Task 4 (written prompt)

#### Phase 5 — Resolution and Debrief
- Outcome, disposition, epidemiological context
- Reflective Debrief Questions (numbered)

---

### FACILITATOR GUIDE (Educator Only)

#### Educator Overview
- Target diagnosis, competing diagnoses, key learning objectives, anticipated session time per phase

#### Complete Patient Truth Document
- All clinical facts, diagnosis, pathophysiology, ideal management

#### Phase-by-Phase Facilitation Moves
- Opening move | Commitment facilitation method | Bridge to next phase | Anticipated tangents | Anchoring watch (per phase)

#### Illness Script and Semantic Qualifier Notes
- Target illness script, semantic qualifiers present, schema transfer suggestions

---

## Example Output Snippet

The following is an example of **Phase 1** and **Commitment Task 1** for an M3 Neurology progressive disclosure case:

---

**Phase 1 — History Only**

> Ms. A.O. is a 34-year-old woman who presents to the neurology clinic reporting an episode of visual disturbance that began three days ago and has not fully resolved. She describes it as "a gray patch in the middle of my left eye" that makes reading difficult. The patch appeared over 24 hours and is now stable but still present. She denies headache. She recalls a similar but milder episode two years ago involving her right eye that resolved completely over six weeks — she did not seek care at that time.
>
> Past medical history: unremarkable. No prior neurological diagnoses. No medications. No known drug allergies.
>
> Social history: works as a nurse, non-smoker, drinks alcohol socially, no illicit drug use. Originally from Nigeria, has lived in Canada for seven years.
>
> Family history: mother has rheumatoid arthritis; no known neurological conditions in the family.
>
> Review of systems: reports mild fatigue over the past month, which she attributes to a busy work schedule. Denies weakness, numbness, bowel or bladder changes, dysphagia, or diplopia.

**Commitment Task 1**

> Before proceeding to the physical examination:
>
> 1. List your top 4 differential diagnoses in order of probability. For each, write one sentence explaining what in the history supports it and one sentence explaining what argues against it.
> 2. What is the single most important question you wish you had asked that is not in the history above?
> 3. What does the relapsing-remitting temporal pattern tell you about the category of disease you are dealing with?

---

## Verification Checklist
- [ ] Learner level explicitly specified and case complexity calibrated to that level throughout all phases
- [ ] Competency framework alignment named and learning objectives mapped to specific phases
- [ ] Commitment tasks written for all five phases — not just Phase 1
- [ ] Phase 1 generates a meaningful differential (5+ hypotheses) without revealing the diagnosis
- [ ] Facilitator guide is a separate document from learner materials — never combined
- [ ] Illness script and semantic qualifier alignment notes are included
- [ ] Phase 5 debrief includes a metacognition question and an illness script generalization question
- [ ] Anchoring watch is specified for at least two phases
