---
title: "Workplace-Based Assessment Tool Designer"
category: healthcare-clinical/medical-education
description: "Design mini-CEX, DOPS, CBD, and EPA observation forms with rating scales, narrative prompt fields, and feedback facilitation guides"
techniques:
  - ST-02
  - QA-01
  - ED-04
  - CM-02
  - OC-01
difficulty: intermediate
tags:
  - mini-cex
  - dops
  - cbd
  - epa
  - workplace-assessment
  - wba
  - direct-observation
updated: "2026-05-15"
related_prompts:
  - domain-healthcare-clinical/prompts/medical-education/assessment-tools/meded_assessment_rubric_builder.md
  - domain-healthcare-clinical/prompts/medical-education/feedback-remediation/meded_milestone_narrative_writer.md
  - domain-healthcare-clinical/prompts/medical-education/feedback-remediation/meded_learner_feedback_composer.md
---

# Workplace-Based Assessment Tool Designer

**Objective:** Produce a complete, ready-to-use workplace-based assessment (WBA) form — mini-CEX, DOPS, CBD, EPA, or multi-source — with domain-specific rating scales, behavioral anchors, narrative prompt fields, a feedback conversation guide, and data aggregation guidance for summative entrustment decisions.

## When to Use
- ✅ Residency and fellowship programs building or refining direct observation instruments
- ✅ Clerkship directors designing structured observation tools for student clinical encounters
- ✅ Program directors creating EPA-linked entrustment observation forms
- ✅ Simulation educators designing structured debrief forms that mirror WBA format
- ✅ QI-oriented programs that want to standardize assessment data collection across supervisors
- ❌ Not for summative written examinations or MCQ assessment design
- ❌ Not for patient care decisions or clinical management recommendations

## Inputs Required
- **Learner level:** M3 / M4 / Resident PGY-X / Fellow
- **Clinical domain/specialty:** e.g., Emergency Medicine, Obstetrics and Gynecology
- **WBA type:** mini-CEX / DOPS / CBD / EPA / 360 Multi-source — or request recommendation
- **Clinical task or encounter type:** Specific description (e.g., "Chest pain history and physical," "Central venous catheter insertion," "Goals-of-care conversation," "Lumbar puncture")
- **Linked EPA (if applicable):** Specify which EPA this tool contributes evidence toward (e.g., EPA 1: Gather a history and perform a physical examination)
- **Assessment context:** Formative (coaching-focused) or Summative (contributing to entrustment decision)
- **Program structure:** How many WBA observations are collected per learner per rotation/period?

## Constraints

**Must:**
- Write domain-specific rating scales for the WBA type selected — not generic categories
- Provide behavioral anchors for each rating level (not just numeric labels)
- Include a structured narrative feedback field with distinct prompt subfields (not an open text box)
- Include a feedback conversation guide with specific facilitator language for the post-encounter debrief
- Specify data aggregation guidance: how many observations of each type are needed before an entrustment decision is defensible
- Distinguish clearly between the formative role (coaching conversation) and the summative role (data point for entrustment) of the same WBA instrument

**Must Not:**
- Deliver a form with numeric ratings but no narrative — numbers alone do not support learning or defensible summative decisions
- Design a single WBA observation as sufficient for an EPA entrustment decision — entrustment requires triangulated evidence across multiple encounters and rater types
- Use the same rating language for both formative and summative contexts without flagging the distinction
- Omit the feedback conversation guide — the WBA form is a conversation scaffold, not a completed document to hand to the learner without discussion
- Write global rating anchors that could apply to any task (e.g., "excellent performance") — anchors must reference specific behaviors for the assessed task

## Instructions

1. **Select WBA type and justify the choice**
   Review these definitions and select the appropriate instrument type:

   - **Mini-CEX (Mini Clinical Evaluation Exercise):** Direct observation of an entire or partial clinical encounter — includes history-taking, physical examination, clinical assessment and plan formulation, and communication with patient. Best for assessing integrated clinical performance in a real patient encounter. Typical duration: 15–20 minutes of observation + 5-minute debrief.
   - **DOPS (Direct Observation of Procedural Skills):** Direct observation of a specific procedural or technical skill. Best for procedures where technique, safety, and patient communication can be observed discretely. Typical duration: duration of the procedure + 5-minute debrief.
   - **CBD (Case-Based Discussion):** Structured discussion of a clinical case the learner has already managed — based on the learner's medical record documentation. Best for assessing clinical reasoning, decision-making, and documentation without requiring real-time observation. Typical duration: 20–30 minutes.
   - **EPA (Entrustable Professional Activity):** A global entrustment decision aggregated across multiple WBA observations; not a single observation form but a summary instrument. Best for making formal statements about unsupervised competence.
   - **360 Multi-source Feedback:** Structured feedback from multiple rater types (supervisor, peer, nurse, patient) for the same learner. Best for assessing interprofessional and communication competencies that supervisors alone cannot observe.

   State the recommended WBA type and the rationale. If the educator's task would be better served by a different WBA type than requested, flag this before proceeding.

2. **Define the encounter or clinical task**
   - Write a precise task description: what the learner does, in what setting, with what patient complexity, and what a complete performance includes
   - Specify the observation window: what portion of the encounter is observed (full encounter vs. focused component)
   - Note task complexity level: straightforward (appropriate for early learners), moderate complexity (mid-training), or high complexity / multiple competing considerations (advanced learners)
   - Specify which EPA(s) this observation contributes toward and what level of entrustment the program is seeking at this training stage

3. **Design the domain rating scale**
   For each WBA type, use these domain sets:

   **Mini-CEX domains:**
   1. History-taking: systematic, focused, patient-centered elicitation
   2. Physical examination: appropriate, systematic, technique-competent
   3. Clinical judgment: differential generation, diagnostic reasoning, assessment quality
   4. Communication with patient: explanation, comprehension check, responsiveness to patient concerns
   5. Professionalism: introduction, consent, patient dignity, time management
   6. Overall clinical competence: global entrustment-level impression

   **DOPS domains:**
   1. Demonstrates knowledge of indications, contraindications, and anatomy
   2. Preparation and patient positioning, equipment check, and timeout (if applicable)
   3. Procedural technique: sequence, precision, adaptation to patient response
   4. Sterile technique and infection prevention (where applicable)
   5. Communication with patient during procedure: explanation, distress monitoring
   6. Efficiency and fluency of technique
   7. Overall procedural competence

   **CBD domains:**
   1. Medical record quality: SOAP/H&P documentation, problem formulation
   2. Clinical assessment: differential, diagnostic reasoning documented
   3. Investigation selection: appropriate ordering, interpretation
   4. Management plan: appropriate, evidence-based, prioritized
   5. Follow-up and safety netting: recognition of red flags, escalation plan
   6. Professionalism in documentation: timeliness, completeness, attribution
   7. Overall case management

   For each domain, write a 1–6 global rating scale with behavioral anchors:

   | Rating | Label | Behavioral Anchor for This Task |
   |---|---|---|
   | 6 | Expert / Unsupervised | [Task-specific behaviors at unsupervised level] |
   | 5 | Advanced | [Task-specific behaviors requiring only distant oversight] |
   | 4 | Competent | [Task-specific behaviors at expected level for training stage] |
   | 3 | Developing | [Task-specific behaviors present but with notable gaps] |
   | 2 | Early | [Task-specific behaviors rudimentary; requires close supervision] |
   | 1 | Not yet demonstrated | Insufficient observation to rate; or critical safety concern observed |

4. **Design the narrative feedback fields**
   Replace a generic open text box with structured narrative prompt fields:

   **Field 1 — What I Observed:**
   *"Describe 2–3 specific behaviors you observed during this encounter. Use behavioral language: what the learner said or did."*
   [Text field]

   **Field 2 — What Went Well:**
   *"Identify one specific behavior or decision that represented a strength. Be specific enough that the learner can repeat it."*
   [Text field]

   **Field 3 — What to Change:**
   *"Identify one specific behavior or decision that should be different next time. Describe the desired behavior, not just the gap."*
   [Text field]

   **Field 4 — One Specific Improvement Action:**
   *"Name the single most important thing for this learner to practice or change before the next similar encounter."*
   [Text field]

   **Field 5 — Complexity of This Encounter:**
   *Select: Low / Moderate / High* — This contextualizes the rating for program directors reviewing aggregated data.

5. **Write the EPA description (if EPA-linked)**
   If this WBA contributes to an EPA entrustment decision, include:
   - Full EPA title and number
   - Behavioral description of what unsupervised performance looks like for this EPA at the end of training
   - Minimum evidence threshold: "This EPA typically requires [6–12] observations across [X] rater types before an entrustment decision is made at the program level"
   - Entrustment scale for the EPA (distinct from per-encounter rating):
     | EPA Level | Description |
     |---|---|
     | 1 | Requires co-management (supervisor does, learner observes) |
     | 2 | Requires direct supervision (supervisor in room) |
     | 3 | Requires indirect supervision (supervisor immediately available) |
     | 4 | Practice-ready (supervisor available by phone; reviews plan) |
     | 5 | Can supervise others performing this EPA |

6. **Write the feedback conversation guide**
   Provide a structured script for the 5-minute post-encounter debrief:

   **Step 1 — Learner self-assessment (90 seconds):**
   Supervisor prompt: "Before I share what I observed, tell me: what went well in that encounter, and what would you do differently?"
   Rationale: Learner self-assessment activates reflective practice and reveals self-insight level.

   **Step 2 — Supervisor observation sharing (90 seconds):**
   Supervisor prompt: "Here's what I observed: [specific behavior from Field 1]. Specifically, I noticed [Field 2 strength] and I also noticed [Field 3 gap]."
   Rule: Describe behavior, not character. "You interrupted the patient twice" not "you were impatient."

   **Step 3 — One improvement focus (60 seconds):**
   Supervisor prompt: "The one thing I'd focus on before the next encounter like this: [Field 4 action]."
   Rule: One specific, actionable behavior. Not a list.

   **Step 4 — Forward commitment (30 seconds):**
   Supervisor prompt: "What will you do differently in the next encounter?"
   Rationale: Learner articulating the change increases retention and accountability.

7. **Write data aggregation guidance**
   Provide program-level guidance on how to use WBA data:

   - **Minimum observations per rotation:** mini-CEX: 2–4 per rotation; DOPS: 3–6 per skill per year; CBD: 2–4 per rotation
   - **Rater diversity requirement:** Summative entrustment decisions should include observations from at least 2–3 different supervisors to reduce individual rater bias
   - **Triangulation principle:** An EPA entrustment decision at the program level typically requires 8–12 WBA observations across multiple encounter types, raters, and clinical contexts
   - **Red flag threshold:** If ≥2 raters independently score any domain at Level 1 or 2 on a 6-point scale, flag for CCC review regardless of overall average
   - **Aggregation method:** For milestone reporting, use median score across observations (more robust to outliers than mean)

8. **Write the assessor training note**
   Brief guidance for faculty completing this tool:
   - Complete the form within 24 hours of observation while behavioral memory is fresh
   - Narrative fields are required — a form with numeric ratings only will not be accepted for program records
   - Rate the observed performance, not your expectation of performance at this training level — use the behavioral anchors, not your prior impression of this learner
   - If you did not observe a domain (e.g., you observed only the procedural technique and not the consent discussion), mark it "Not observed" rather than estimating

## False-Positive Prevention

| ❌ Common Mistake | ✅ Correct Approach |
|---|---|
| Numeric ratings without narrative | Rating numbers alone do not support learning (no coaching signal) or defensible summative decisions (no behavioral evidence); narrative fields are required components, not optional add-ons |
| Single WBA observation used for EPA entrustment decision | EPA-level trust requires triangulated evidence across multiple encounters, multiple rater types, and varied clinical contexts — a single observation is a data point, not a decision |
| Same rating scale for formative and summative | Formative WBA focuses on coaching conversation and next-step improvement; summative WBA generates data for CCC and entrustment decisions — the stakes and interpretation differ |
| Omitting feedback conversation guide | The WBA form is a conversation scaffold for a structured debrief; handing the completed form to a learner without a debrief conversation wastes the educational opportunity and does not constitute feedback |
| Generic rating anchors ("excellent," "satisfactory") | Anchors must describe specific observable behaviors for the assessed task; "excellent procedural technique" is not an anchor — "performs all steps in correct sequence without hesitation, anticipates instrument needs, maintains sterile field throughout" is |
| Raters rating the learner, not the performance | WBA rates this specific observed performance, not the learner's general ability or training-stage expectation; a PGY-1 can earn a 5/6 on a straightforward encounter; a PGY-3 can earn a 2/6 on a complex one |

## Output Format

Deliver the complete WBA tool in this structure:

---

**WBA OVERVIEW**
- Tool type: [mini-CEX / DOPS / CBD / EPA / 360]
- Task assessed: [specific clinical task]
- Learner level: [level]
- Linked EPA: [EPA number and title, or "Not applicable"]
- Assessment context: [Formative / Summative / Both]
- Observation duration: [X minutes of observation + Y minutes debrief]

---

**ASSESSOR COMPLETION GUIDE** *(one paragraph for top of form)*

[Instructions for the faculty rater]

---

**DOMAIN RATING SCALE**

| Domain | 1 — Not Yet | 2 — Early | 3 — Developing | 4 — Competent | 5 — Advanced | 6 — Expert | Not Observed |
|---|---|---|---|---|---|---|---|
| [Domain 1] | [anchor] | [anchor] | [anchor] | [anchor] | [anchor] | [anchor] | ☐ |
| [Domain 2] | | | | | | | ☐ |
| [etc.] | | | | | | | |

**Global Entrustment Rating for This Encounter:**
☐ 1 — Direct supervision required (in room)
☐ 2 — Indirect supervision required (immediately available)
☐ 3 — Supervised practice (available by phone)
☐ 4 — Unsupervised practice appropriate for this task

---

**NARRATIVE FEEDBACK FIELDS**

What I observed (specific behaviors):
[Text field]

What went well (one specific behavior):
[Text field]

What to change (one specific behavior, stated as desired behavior):
[Text field]

One improvement action for next encounter:
[Text field]

Encounter complexity: ☐ Low ☐ Moderate ☐ High

---

**EPA DESCRIPTION** *(if applicable)*

[EPA title, behavioral description of unsupervised performance, entrustment scale]

---

**FEEDBACK CONVERSATION GUIDE** *(for assessor use only — not shown to learner)*

[Structured 5-step debrief script]

---

**DATA AGGREGATION GUIDANCE** *(for program directors)*

[Minimum observations, rater diversity, triangulation, red flag threshold, aggregation method]

---

## Example Output Snippet

> **Mini-CEX — Domain 3: Clinical Judgment**
>
> *This domain assesses the learner's ability to synthesize history and physical examination findings into a differential diagnosis and initial management plan.*
>
> | Rating | Behavioral Anchor |
> |---|---|
> | 6 — Expert | Generates a complete, prioritized differential that explicitly accounts for all key findings; identifies the most life-threatening diagnosis and explains the distinguishing features; formulates a management plan with clear rationale; articulates uncertainty appropriately and names the decision point that will guide next steps |
> | 4 — Competent | Generates a differential with 3 or more plausible diagnoses in reasonable priority order; identifies the most likely diagnosis with supporting evidence from the encounter; management plan addresses the leading diagnosis with appropriate first steps |
> | 2 — Early | Names a diagnosis without generating a differential; management plan is not connected to the clinical reasoning; requires supervisor prompting to identify alternatives or to explain the reasoning behind management choices |
>
> **Feedback Conversation Guide — Step 3 (One improvement focus):**
>
> Supervisor prompt: "The one thing I'd focus on before the next encounter like this: When you name your diagnosis, say out loud what makes you confident enough to lead with that one — what feature most distinguishes it from the next most likely diagnosis? That explicit reasoning step is what separates a confident assessment from a guess."

## Verification Checklist
- [ ] WBA type selected with explicit rationale for this task and learner level
- [ ] Domain rating scale uses task-specific behavioral anchors — not generic descriptors
- [ ] Narrative feedback fields are structured with distinct prompt subfields (not one open text box)
- [ ] Feedback conversation guide included with specific facilitator language
- [ ] EPA linkage specified if applicable — with entrustment scale and evidence threshold
- [ ] Data aggregation guidance specifies minimum observations, rater diversity, and red flag threshold
- [ ] Distinction between formative and summative use explicitly addressed
- [ ] Assessor training note included on form
