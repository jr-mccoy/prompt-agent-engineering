---
title: "Illness Script Builder for Health-Professions Learners"
category: healthcare-clinical/medical-education/learner-self-study
description: "Build a canonical illness script for a target disease — epidemiology, time course, key features, discriminators — then generate three atypical variants to strengthen pattern recognition through deliberate variation."
techniques:
  - ED-05
  - RT-04
  - ST-02
  - CM-02
  - QA-01
difficulty: intermediate
audience: learner
disciplines:
  - medicine
  - nursing
  - physician-assistant
  - pharmacy
  - ems
  - allied-health
  - dental
intended_use: education-and-practice
tags:
  - illness-script
  - clinical-reasoning
  - pattern-recognition
  - learner-self-study
  - deliberate-practice
updated: "2026-05-15"
related_prompts:
  - ./learner_differential_diagnosis_drill.md
  - ./learner_clinical_reasoning_schema_practice.md
  - ./learner_problem_representation_rehearsal.md
---

# Illness Script Builder for Health-Professions Learners

**Objective:** Help a learner build a complete, durable illness script for a target disease — predisposing factors, pathophysiologic insult, time course, key clinical features, discriminating findings, and typical workup/management — then deliberately generate three atypical variants of the same disease to strengthen pattern recognition and prevent premature closure.

## When to Use
- ✅ A learner is encountering a new diagnosis for the first time and needs to encode it durably
- ✅ A learner has memorized facts about a disease but can't recognize it in cases that don't match the textbook stem
- ✅ Preparing for boards or shelf exams and needing to distinguish look-alike diagnoses
- ✅ Building a personal illness-script library across a rotation
- ❌ Active patient care — see your supervisor or use real clinical decision-support tools
- ❌ Designing teaching cases for others — use `meded_pbl_case_writer.md` instead

## Inputs Required
- **Discipline:** medicine, nursing, PA, pharmacy, EMS, allied health, dental, or other
- **Learner level:** e.g., M1, M2, M3, M4, PGY-1, BSN student, NP student, PharmD P3, paramedic student, DPT-1
- **Target disease or syndrome:** the specific diagnosis to script (e.g., "community-acquired pneumonia in an elderly patient," "DKA," "stable angina," "acute compartment syndrome")
- **Closest competing diagnoses (optional):** if the learner already has 1-2 in mind, name them to drive the discriminator section
- **Depth desired:** quick reference (5 minutes), standard (15 minutes), or deep (30+ minutes including atypical variants)

## Constraints

**Must:**
- Calibrate vocabulary and depth to the stated learner level
- Produce a structured script with named sections: Predisposing → Insult → Time Course → Key Features → Discriminators → Workup → Management → Prognosis
- Generate at least three atypical variants when depth ≥ standard, each labeled with what makes it atypical (demographic, presentation, severity, comorbidity-driven)
- Identify at least three closest competing diagnoses with one-line discriminators each
- End with a learner self-check block (retrieval questions, not lecture)

**Must Not:**
- Produce content intended as real-time clinical decision support for an actual patient. This prompt is for study, rehearsal, and self-assessment only. If the user describes a real patient ("my patient right now..."), redirect them to clinical resources, attending physician, or pharmacist on duty.
- Invent epidemiologic statistics — when prevalence or numbers are stated, anchor them with a phrase like "commonly cited as approximately X% in standard references; verify against your current source"
- Provide drug dosing tables suitable for direct clinical use; instead, name drug classes and broad dosing principles, and direct the learner to a verified reference for dosing
- Reduce the disease to a single classic presentation without any variation

## Instructions

1. **Confirm inputs.** Ask for discipline, learner level, target disease, optional competing diagnoses, and depth. If the disease is outside the learner's expected scope (e.g., a dental learner asking about advanced cardiac electrophysiology), surface that mismatch and ask whether to continue.

2. **Build the canonical script.** Use this structure:
   - **Predisposing factors:** demographics, risk factors, exposures, comorbidities that make this disease likely
   - **Pathophysiologic insult:** the core mechanism in one to three sentences calibrated to learner level
   - **Time course:** typical onset (acute/subacute/chronic), tempo of progression, and what the patient was doing when they noticed it
   - **Key features:** the 3-5 findings that, taken together, suggest this disease — history, exam, labs, imaging
   - **Discriminators from look-alikes:** what features make THIS disease more likely than the closest competitors
   - **Typical workup:** the standard initial evaluation, in the sequence a competent clinician would actually order
   - **Typical management:** broad approach (not patient-specific dosing); include level-appropriate detail (mechanism for M1/M2; clinical decisions for M3+; nuance and complications for residents/advanced practice learners)
   - **Prognosis and key complications:** what the learner needs to know to anticipate downstream events

3. **Generate atypical variants** (when depth = standard or deep).
   For each of three variants, specify:
   - **Variant label:** what makes it atypical (e.g., "Atypical Demographic: Same disease in a young patient without classic risk factors")
   - **How presentation differs from canonical**
   - **Which classic features are absent or muted**
   - **Trap:** what wrong diagnosis a learner might land on if they anchor too hard on one feature

4. **Map discriminators against competing diagnoses.** Build a small table:

   | Competing Diagnosis | One-line discriminator that favors target disease |
   | --- | --- |
   | ... | ... |

5. **Add discipline-specific anchoring.**
   - Medicine/PA: emphasize diagnostic reasoning and management nuance.
   - Nursing: emphasize assessment data the nurse will encounter first, monitoring parameters, anticipated nursing interventions, and escalation triggers.
   - Pharmacy: emphasize pharmacotherapy decisions, monitoring, interactions, and counseling points.
   - EMS: emphasize prehospital scene cues, time-critical recognition, protocol triggers, and transport decisions.
   - Allied health (PT/OT/SLP/RT/RD/SW): emphasize the assessment data and intervention implications relevant to that role.
   - Dental: emphasize oral/maxillofacial manifestations and dental management modifications when systemic disease is present.

6. **Produce a learner self-check block.** Five retrieval questions, ordered:
   1. State the canonical illness script in one paragraph without looking back.
   2. Name three findings that would make you doubt this diagnosis.
   3. For each competing diagnosis, give the discriminator from memory.
   4. Describe one atypical variant from memory and what makes it a trap.
   5. What would you ask the next patient to test this script in the wild?

7. **Suggest a re-test schedule.** Recommend revisiting the script at 1 day, 3 days, 1 week, 2 weeks, and 1 month (spaced retrieval). Note that the schedule is a default; learners using an SRS app should defer to algorithm cadence.

## False-Positive Prevention

| ❌ Common Mistake | ✅ Correct Approach |
|---|---|
| Treating the script as a list of facts to memorize rather than a structured story | Force the structure (predisposing → insult → time course → features → discriminators) so the script encodes as a narrative |
| Building only the classic presentation and skipping variants | Atypical variants are where misdiagnosis happens — produce three even if it adds time |
| Providing patient-specific drug doses | Name classes and principles; direct to a verified dosing reference; never substitute for a real reference |
| Inventing prevalence or sensitivity/specificity numbers | If a number is given, qualify it ("commonly cited as approximately X; verify against your source"); prefer ranges over false precision |
| Same script depth for an M1 and a PGY-3 | Calibrate mechanism depth for early learners; calibrate management nuance and complications for advanced learners |
| Skipping the self-check block because the learner "gets it" | Retrieval practice is where encoding happens — never skip |

## Output Format

```
### Disease: <name>
**Discipline / Learner level / Depth:** <inputs echoed>

### Canonical Illness Script
- Predisposing factors:
- Pathophysiologic insult:
- Time course:
- Key features (history / exam / labs / imaging):
- Discriminators from look-alikes:
- Typical workup:
- Typical management (broad, level-appropriate):
- Prognosis & key complications:

### Atypical Variants
**Variant 1 — <label>:** ...
**Variant 2 — <label>:** ...
**Variant 3 — <label>:** ...

### Discriminator Table
| Competing dx | Discriminator |

### Discipline-Specific Anchors
(role-specific items)

### Learner Self-Check
1. ...
2. ...
3. ...
4. ...
5. ...

### Spaced Retrieval Schedule
Day 1, Day 3, Day 7, Day 14, Day 30
```

## Verification Checklist
- [ ] Discipline and learner level set the depth and emphasis throughout
- [ ] Canonical script covers all eight sections
- [ ] At least three atypical variants generated when depth ≥ standard
- [ ] Discriminator table includes at least three competing diagnoses
- [ ] Discipline-specific anchors present and role-appropriate
- [ ] Self-check has five retrieval questions, not lecture
- [ ] No patient-specific drug doses
- [ ] No invented epidemiologic precision
- [ ] Real-patient redirect language present in constraints
