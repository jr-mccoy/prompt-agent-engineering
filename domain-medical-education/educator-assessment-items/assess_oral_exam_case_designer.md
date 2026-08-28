---
title: "Oral Exam Case Designer"
category: medical-education/educator-assessment-items
description: "Design oral examination cases with clinical stem, structured probing questions at graduated difficulty, evaluator scoring guide, and standard-setting anchors"
techniques:
  - ST-02
  - RT-03
  - CM-02
  - QA-01
  - ED-04
difficulty: advanced
tags:
  - oral-exam
  - clinical-examination
  - evaluator-guide
  - probing-questions
  - competency-assessment
  - medical-education
updated: "2026-05-15"
related_prompts:
  - domain-medical-education/educator-assessment-items/assess_nbme_style_mcq_writer.md
  - domain-medical-education/educator-rubrics-wba/assess_rubric_builder.md
  - domain-medical-education/feedback-remediation/meded_milestone_narrative_writer.md
---

# Oral Exam Case Designer

**Objective:** Produce a complete oral examination case — including clinical stem, graduated probing question sequence, pivot questions, evaluator scoring guide with behavioral anchors, sample exemplar responses, and examiner training notes — ready for standardized use across examiners.

## When to Use
- ✅ Clerkship directors designing end-of-rotation oral examinations
- ✅ Residency programs building objective structured clinical examinations (OSCEs) with oral components
- ✅ Fellowship programs assessing advanced clinical reasoning and judgment
- ✅ Boards and certifying bodies developing oral board examination cases
- ✅ Simulation educators creating facilitated debriefs structured as oral assessments
- ❌ Not for written MCQ or short answer assessments (use `assess_nbme_style_mcq_writer.md`)
- ❌ Not for patient care decisions or clinical management recommendations

## Inputs Required
- **Learner level:** M3 / M4 / Resident PGY-X / Fellow / Candidate for board certification
- **Clinical domain/specialty:** e.g., Internal Medicine — Pulmonology, Surgery — Acute Abdomen
- **Competency focus:** Primary ACGME competency domain or CanMEDS role being assessed (e.g., Patient Care — Clinical Reasoning; Medical Knowledge; Interpersonal Communication)
- **Case complexity target:** Standard (PGY-1/2), Complex (PGY-3/Fellow), Judgment-heavy (Board-level)
- **Time allotted:** Typical oral exam station is 15–30 minutes; specify target duration
- **Minimum passing standard:** Describe the intended borderline candidate for this exam cohort

## Constraints

**Must:**
- Write a case stem that allows multiple valid entry points — the opening question must not have one correct answer path
- Sequence probing questions from lower to higher cognitive demand (Recall → Application → Analysis → Synthesis → Evaluation)
- Include pivot questions for each major domain so examiners can assess minimum competency even when a candidate struggles
- Provide behavioral anchors (not impressionistic adjectives) for each scoring level
- Include at least one exemplar Excellent response and one exemplar Borderline response per major probing question
- Provide examiner training notes covering: how to probe without leading, when to pivot, how to handle silence, how to score interrupted answers

**Must Not:**
- Write a case with a single correct answer path that punishes alternative valid clinical approaches
- Omit pivot/fallback questions — without them, one cognitive block can derail an otherwise competent candidate
- Use vague scoring anchors ("demonstrates understanding," "shows good judgment") — every anchor must describe observable behavior
- Design all questions at the same cognitive level — graduated difficulty is required to discriminate pass from distinction
- Include examiner scripts so rigid they prevent adaptive follow-up

## Instructions

1. **Clarify case parameters before generating**
   - Confirm learner level and set case complexity accordingly (M4 ≠ PGY-3 ≠ board candidate)
   - Identify the 3–5 clinical reasoning domains the case will test (e.g., differential generation, diagnostic prioritization, management planning, complication recognition, patient communication)
   - Specify whether the case is designed for formative practice (feedback-forward) or summative examination (pass/fail decision)
   - Confirm time allotment and calculate question count: approximately 2–3 minutes per major question

2. **Write the case stem**
   - Paragraph 1: Opening scenario (setting, chief complaint, immediate clinical context — e.g., "You are called to the emergency department to see...")
   - Paragraph 2: Initial data provided to candidate at stem read (vital signs, chief complaint, one to two historical elements, one physical exam finding)
   - Paragraph 3: The opening clinical question the candidate is asked to answer aloud (broad, open-ended — e.g., "Tell me how you would approach this patient," not "What is the diagnosis?")
   - Design the stem so that the correct clinical response is a process (differential, systematic approach), not a single answer
   - Total stem length: 150–250 words, read aloud by examiner or candidate in under 90 seconds

3. **Write the probing question sequence (6–10 questions)**
   Organize questions across three cognitive tiers:

   **Tier 1 — Recall/Application (Questions 1–2):** Basic clinical knowledge applied to this patient
   - Example: "What are the three most likely diagnoses in your differential, and what feature of this presentation supports each?"
   - Every candidate at this level should be able to answer Tier 1

   **Tier 2 — Analysis/Synthesis (Questions 3–6):** Reasoning through complexity, integrating new data, prioritizing competing considerations
   - Example: "The chest X-ray shows [finding]. How does this change your management?"
   - Distinguishes passing from passing-with-confidence candidates

   **Tier 3 — Evaluation/Judgment (Questions 7–10):** Navigating ambiguity, ethical complexity, system-level thinking, teaching others
   - Example: "Your attending disagrees with your management plan and wants to proceed differently. How do you handle this?"
   - Distinguishes high performers from the passing range

4. **Write pivot questions for each major domain**
   For each of the 3–5 clinical domains, write 2 pivot/fallback questions:
   - Pivot questions are simpler, more directive versions of the main question used when a candidate is blocked
   - Example: If a candidate cannot generate a differential for acute dyspnea, pivot to "Can you tell me what you would be most worried about missing in a patient with sudden onset shortness of breath?"
   - Pivot questions allow assessment of minimum competency; scores at the pivot level should be noted in scoring guide

5. **Write the evaluator scoring guide**
   For each major probing question, provide a 4-level scoring rubric:

   | Level | Label | Behavioral Description |
   |---|---|---|
   | 4 | Excellent | [Specific behaviors: what the candidate says and does] |
   | 3 | Satisfactory | [Specific behaviors that meet standard without exceeding] |
   | 2 | Borderline | [Specific minimum competency behaviors — what is missing compared to Satisfactory] |
   | 1 | Unsatisfactory | [Specific critical omissions or errors that constitute failure] |

   - Every level description must use observable language, not evaluative adjectives
   - Provide a global rating anchor for the overall case performance (same 4-level scale)

6. **Write sample exemplar responses**
   For each major probing question:
   - **Exemplar Excellent response:** A verbatim or near-verbatim example of what a 4/Excellent candidate says (2–4 sentences)
   - **Exemplar Borderline response:** A verbatim or near-verbatim example of what a 2/Borderline candidate says — includes what is present and what is absent
   - Examiner calibration: use these exemplars in examiner training sessions so that multiple examiners share a mental model of the standard

7. **Write the examiner training notes**
   Address each of the following:
   - **How to probe without leading:** Approved neutral follow-up phrases (e.g., "Tell me more about that," "What else?" "What would concern you next?") vs. leading phrases to avoid ("Wouldn't you also consider...?")
   - **When to pivot:** Decision rule for moving to a pivot question (e.g., >20 seconds of unproductive silence, or candidate states explicitly they don't know)
   - **How to handle silence:** Guidance on wait time (allow 10–15 seconds before offering pivot), documentation of silence in scoring notes
   - **How to handle wrong answers:** Distinguish a wrong answer that reveals a reasoning process (scorable) from a wrong answer that indicates a dangerous knowledge gap (flag for examiner judgment)
   - **Interrupted responses:** If candidate begins a partially correct answer, guidance on whether to score the partial response or prompt for completion

8. **Write global rating anchor behaviors**
   Provide behavioral descriptions for the overall case:
   - **Excellent:** Candidate demonstrates [specific behaviors: e.g., systematic differential generation, appropriate diagnostic prioritization, explicit articulation of uncertainty, clear management reasoning]
   - **Satisfactory:** Candidate demonstrates [behaviors present] with [specific gaps acceptable at this level]
   - **Borderline:** Candidate requires examiner pivot to reach [minimum competency threshold]; demonstrates [specific minimum behaviors present] but lacks [specific behaviors]
   - **Unsatisfactory:** Candidate fails to demonstrate [specific critical behaviors] even with pivot questions; demonstrates [specific patient safety concerns or critical knowledge gaps]

9. **Write the standard-setting reference**
   - State the intended borderline candidate profile for this exam (training level, expected preparation, representative peer cohort)
   - Note which questions are "must pass" items — questions where a Borderline or Unsatisfactory answer, regardless of other scores, signals examination failure
   - Provide a scoring aggregation guide: how to combine question-level scores into an overall pass/fail recommendation

## False-Positive Prevention

| ❌ Common Mistake | ✅ Correct Approach |
|---|---|
| Rigid examiner script that prevents adaptive follow-up | Oral exams require responsive probing; scripts are navigational guides, not transcripts — examiners must be trained to deviate from the sequence when clinical reasoning warrants |
| Omitting examiner calibration materials | Inter-rater reliability requires shared mental models of what passing looks like; exemplar responses are not optional — they are the primary calibration tool |
| All probing questions at the same cognitive level | Graduated difficulty is the mechanism that discriminates borderline from strong candidates; a flat question sequence compresses score variance and reduces validity |
| No pivot questions | Without recovery questions, one cognitive block can cause a competent candidate to fail; pivot questions allow minimum competency assessment independent of the primary question |
| Impressionistic scoring anchors ("shows good clinical judgment") | Every anchor must describe what the candidate actually says or does; vague anchors produce rater drift and unreliable scores |
| Case with only one correct diagnostic or management path | Real clinical cases allow multiple defensible approaches; a case that penalizes an alternative valid approach measures algorithm adherence, not clinical reasoning |
| Examiner-generated data on the fly | All data revealed during the case (lab results, imaging findings, consultant opinions) must be pre-specified in the case materials to ensure standardization across candidates |

## Output Format

Deliver the complete oral exam case in this structure:

---

**CASE OVERVIEW**
- Learner level: [level]
- Clinical domain: [specialty]
- Competency focus: [ACGME domain or CanMEDS role]
- Case complexity: [Standard / Complex / Judgment-heavy]
- Time allotment: [X minutes]
- Clinical domains tested: [list of 3–5 domains]

---

**CASE STEM** *(read to candidate)*

[150–250 word clinical scenario]

**Opening question to candidate:**

[Broad, open-ended opening question]

---

**EXAMINER MATERIALS** *(not shared with candidate)*

**Sequential Data Reveals** *(information examiner provides when asked or at specified points)*

| Trigger | Data Provided |
|---|---|
| Candidate asks for vital signs | [specific values] |
| Candidate asks to examine the patient | [specific findings] |
| [additional triggers] | [data] |

---

**PROBING QUESTION SEQUENCE**

**Tier 1 — Application**

Q1: [Question text]
- Pivot if blocked: [Pivot question]
- Scoring anchors: [4/3/2/1 behavioral descriptions]
- Exemplar Excellent: [response]
- Exemplar Borderline: [response]

**Tier 2 — Analysis/Synthesis**

Q3: [Question text]
- Pivot if blocked: [Pivot question]
- Scoring anchors: [4/3/2/1 behavioral descriptions]
- Exemplar Excellent: [response]
- Exemplar Borderline: [response]

**Tier 3 — Evaluation/Judgment**

Q7: [Question text]
- Pivot if blocked: [Pivot question]
- Scoring anchors: [4/3/2/1 behavioral descriptions]
- Exemplar Excellent: [response]
- Exemplar Borderline: [response]

---

**GLOBAL RATING ANCHORS**

| Level | Global Behavioral Description |
|---|---|
| Excellent (4) | [behaviors] |
| Satisfactory (3) | [behaviors] |
| Borderline (2) | [behaviors] |
| Unsatisfactory (1) | [behaviors] |

---

**EXAMINER TRAINING NOTES**

[Guidance on probing, pivoting, silence, wrong answers, interrupted responses]

---

**STANDARD-SETTING REFERENCE**

- Intended borderline candidate: [description]
- Must-pass questions: [list]
- Scoring aggregation guide: [method]

---

## Example Output Snippet

> **CASE STEM** *(read to candidate)*
>
> You are the internal medicine resident on call when the night nurse pages you about a 68-year-old man with a history of type 2 diabetes and hypertension who was admitted this afternoon for community-acquired pneumonia. He was started on ceftriaxone and azithromycin. At 2:00 AM, the nurse reports his blood pressure has dropped to 88/54 mmHg, heart rate is 118/min, respiratory rate is 26/min, temperature is 39.2°C, and oxygen saturation is 89% on 2L nasal cannula. He was in his usual state of health at 8 PM when you assessed him. He is awake but appears anxious and mildly confused.
>
> Opening question: "Tell me how you think about this patient right now and what you want to do in the next 10 minutes."
>
> **Q2 (Tier 1 — Application):** "You've identified septic shock as your leading concern. Walk me through the initial resuscitation steps you'd order right now."
>
> Exemplar Excellent: "I'd place two large-bore IVs if not already done, draw blood cultures times two before starting antibiotics, check a lactate, and start a 30 mL/kg crystalloid bolus. I'd reassess after the bolus — if MAP is still below 65, I'd start norepinephrine. I'd also broaden his antibiotics given he's decompensating on the current regimen."
>
> Exemplar Borderline: "I'd give him fluids and check his blood pressure again. I'd probably call my attending." *(Present: fluid resuscitation intent. Missing: specific volume, culture timing relative to antibiotics, vasopressor threshold, antibiotic reassessment.)*

## Verification Checklist
- [ ] Learner level explicitly specified and case complexity calibrated accordingly
- [ ] Probing questions span all three cognitive tiers (Application → Analysis → Evaluation)
- [ ] Pivot questions written for each major domain (minimum 2 per domain)
- [ ] Scoring anchors use observable behavioral language — no evaluative adjectives
- [ ] Exemplar Excellent and Borderline responses provided for each major question
- [ ] All data reveals pre-specified in examiner materials (no improvised data)
- [ ] Examiner training notes address: probing without leading, pivot timing, silence, wrong answers
- [ ] Standard-setting reference identifies borderline candidate profile and must-pass questions
