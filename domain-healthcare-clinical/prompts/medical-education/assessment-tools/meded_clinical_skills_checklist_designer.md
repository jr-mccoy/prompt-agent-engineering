---
title: "Clinical Skills Checklist Designer"
category: healthcare-clinical/medical-education
description: "Design observable-behavior checklists for clinical procedures, physical exam techniques, and communication skills with binary and global rating items"
techniques:
  - ST-02
  - QA-01
  - CM-02
  - OC-01
  - ED-04
difficulty: beginner
tags:
  - checklist
  - clinical-skills
  - procedure
  - physical-exam
  - osce
  - direct-observation
updated: "2026-05-15"
related_prompts:
  - domain-healthcare-clinical/prompts/medical-education/case-scenario-design/meded_osce_station_designer.md
  - domain-healthcare-clinical/prompts/medical-education/case-scenario-design/meded_standardized_patient_scenario_writer.md
  - domain-healthcare-clinical/prompts/medical-education/assessment-tools/meded_assessment_rubric_builder.md
---

# Clinical Skills Checklist Designer

**Objective:** Produce a complete, observer-ready clinical skills checklist — with binary observable-behavior items in clinical sequence, communication and patient interaction items, safety and hygiene items, critical error flags, a global rating scale with behavioral anchors, and a scoring guide — for a specified procedure, physical exam technique, or communication skill.

## When to Use
- ✅ Clinical skills educators designing checklists for simulation lab practice and assessment
- ✅ OSCE station designers building standardized patient encounter scoring forms
- ✅ Clerkship faculty creating direct observation tools for bedside procedures
- ✅ Residency programs building competency-based procedural assessment tools
- ✅ Allied health educators designing checklist assessments for nursing, pharmacy, or respiratory therapy skills
- ✅ Standardized patient (SP) trainers building SP-scored checklist items for communication skills
- ❌ Not for multidimensional analytic rubrics where criterion-by-criterion feedback is needed (use `meded_assessment_rubric_builder.md`)
- ❌ Not for patient care decisions or clinical management recommendations

## Inputs Required
- **Learner level:** M1 / M2 / M3 / M4 / Resident PGY-X / Nursing student / Allied health learner
- **Clinical domain/specialty:** e.g., Internal Medicine — Cardiology, Nursing — Acute Care
- **Skill to be assessed:** Specific procedure or skill name (e.g., "Peripheral intravenous catheter insertion," "Cardiovascular physical examination," "Breaking bad news using the SPIKES protocol," "Nasogastric tube placement")
- **Assessment context:** Formative practice (simulation lab, skills station) / OSCE station (standardized patient encounter) / Direct observation in clinical practice (real patient) / Certification or competency examination
- **Learner type and prior exposure:** First time performing / Practiced in simulation only / Some clinical exposure / Seeking certification
- **Pass/fail requirement:** Is there a required pass/fail cutoff for this checklist? If so, what is the minimum performance threshold for the program?

## Constraints

**Must:**
- Write every checklist item as one specific observable binary behavior — either performed (✓) or not performed (✗)
- Sequence items in the order a competent clinician would perform them (clinical sequence, not alphabetical or importance order)
- Separate critical error items into a distinct section — critical errors trigger automatic failure regardless of total score
- Include a global rating scale (3-point minimum) with behavioral anchors for each level
- Specify a pass/fail threshold: how many items must be checked "performed" to pass, and how critical errors interact with total score
- Adjust checklist scope and complexity to learner level — novice checklists include setup and preparation steps that experts do automatically

**Must Not:**
- Write vague items ("performs correctly," "demonstrates appropriate technique") — every item must describe one specific observable behavior
- Exceed 25 items — observer cognitive load above 25 items degrades reliability; exceed only with strong justification and item justification table
- Combine two behaviors in one checklist item — one behavior per item, so each item has a binary pass/fail
- Omit critical error flags — some omissions (sterile field break, wrong patient, wrong site, allergy check failure) must trigger automatic failure regardless of total score
- Apply the same checklist to all learner levels without adjustment — novice and expert assessments have different foci

## Instructions

1. **Define the skill and set scope for this learner level**
   - Write a one-paragraph skill description: what the learner does, from start to finish, in what setting, on what type of patient
   - Specify the start point ("observer begins scoring when the learner enters the room/simulation bay") and end point ("observer stops scoring when the learner disposes of sharps and removes gloves")
   - Adjust scope by learner level:
     - **Novice (M1/M2 / first exposure):** Include all preparation and setup steps — these are not automatic yet and represent significant skill dimensions at this level
     - **Intermediate (M3/M4 / some clinical exposure):** Setup steps may be condensed; focus on procedural technique and clinical decision points
     - **Advanced (Resident / fellow / competency exam):** Focus on procedural fluency, adaptive responses, complication recognition, and efficiency; exclude obvious setup steps unless patient safety-critical
   - Note any patient population or setting constraints that affect the checklist (e.g., pediatric vs. adult differences, sterile vs. clean procedure)

2. **Write the preparation and setup items**
   Items in this section assess readiness before the procedure begins. Include:
   - Hand hygiene (before and after patient contact)
   - Equipment verification: all required supplies present and functioning
   - Patient identification: two-patient identifiers confirmed
   - Procedure explanation and verbal consent (or written if required)
   - Patient positioning and exposure
   - Sterile field setup (if applicable): sterile drape placed without contamination, sterile gloves donned using sterile technique
   - Universal precautions / PPE (if applicable)
   - Surgical timeout or pre-procedure safety check (if applicable)

   Write each as a binary item: "Performs hand hygiene with soap and water or alcohol-based sanitizer before patient contact" — not "Maintains hand hygiene."

3. **Write the sequential procedural steps**
   - List 10–20 procedural steps in the exact order they should be performed by a competent clinician
   - Each item: one specific observable behavior, phrased as an action statement
   - Use this sentence structure: "[Action verb] [specific object] [specific manner or condition if needed]"
     - Example: "Inserts IV catheter at 10–30 degree angle, bevel up, into the vein"
     - Not: "Correctly inserts the IV"
   - Where sequence flexibility exists for competent practitioners, note this in a parenthetical: "(Order may vary based on clinical presentation)"
   - Where technique has acceptable variations, write the item to accept all valid approaches: "Secures catheter hub with tape or transparent dressing" not "secures with Tegaderm"

4. **Write the communication and patient interaction items**
   Include 3–5 items assessing the learner's communication with the patient during the skill:
   - Introduces self by name and role before beginning
   - Explains what they are about to do in language the patient can understand
   - Checks for patient comfort or pain at specified points (e.g., before needle insertion, after positioning)
   - Responds to patient question or expression of discomfort during procedure
   - Informs patient when procedure is complete and what to expect next

   Note: For standardized patient (SP) encounters, these items may be scored by the SP using the same checklist.

5. **Write the safety and hygiene items**
   Include a discrete safety section separate from procedural steps. Items should include:
   - Hand hygiene: before patient contact and after procedure
   - Sharps disposal: disposed in sharps container immediately after use, not recapped
   - Sterile field integrity: field not contaminated at any point during procedure (if applicable)
   - Patient identification re-check (if administering a medication or blood product during the procedure)
   - Correct site, correct side confirmation (if applicable to the procedure)
   - Allergy check documented or verbalized before medication administration (if applicable)

6. **Identify and list critical errors**
   Critical errors are items where failure results in automatic checklist failure, regardless of total score. Present these as a separate list:

   **Critical Error Definition:** An error that represents a patient safety risk, infection control violation, or fundamental procedure failure that would not be acceptable in any clinical context.

   Common critical error categories:
   - Sterile field violation (for sterile procedures)
   - Sharps recapping or unsafe sharps disposal
   - Failure to confirm patient identity before the procedure
   - Administration of medication without allergy check
   - Wrong site or wrong side (for lateralized procedures)
   - Failure to obtain patient consent or explanation before beginning
   - Any action that causes patient injury in the simulation (e.g., incorrect angle causing arterial puncture in an IV access simulation)

   For each critical error: name the specific behavior, state the consequence ("automatic failure; procedure must stop and be repeated from the beginning"), and specify whether the simulation observer should stop the simulation or allow it to continue to completion.

7. **Write the global rating scale**
   Provide a 3-point global rating with behavioral anchors:

   | Rating | Label | Behavioral Description |
   |---|---|---|
   | 3 | Satisfactory | [Observable behaviors that define a safe, competent performance of this skill at this learner level] |
   | 2 | Borderline | [Observable behaviors at minimum competency — what is present and what is missing from a satisfactory performance] |
   | 1 | Unsatisfactory | [Observable behaviors that define an unsafe or incompetent performance — specific critical gaps] |

   The global rating is independent of the checklist item score — it reflects the rater's overall judgment of performance quality and may diverge from the sum score in cases where many minor steps were missed but overall technique was fluent, or vice versa.

8. **Write the scoring guide**
   Specify the pass/fail rules:
   - **Item score:** Total items marked "performed" out of total scored items (exclude "Not observed" items from denominator)
   - **Pass threshold:** State the minimum percentage or absolute number of items required to pass (typical range: 75–80% for formative; 85–90% for summative competency examination)
   - **Critical error rule:** State how critical errors interact with total score (recommended: any critical error = automatic failure, regardless of item score)
   - **Global rating rule:** State whether global rating is independent of item score or integrated (recommended: global rating of "Unsatisfactory" overrides passing item score; "Satisfactory" global rating cannot compensate for item score below pass threshold)
   - **Incomplete attempt rule:** If the learner does not complete the procedure within the time limit, specify which items are scored "not performed" and which are scored "not observed"

9. **Write the observer instructions**
   Brief instructions for the faculty observer or standardized patient completing this checklist:
   - Mark each item ✓ (performed) or ✗ (not performed) at the moment it occurs — do not score from memory at the end
   - Mark "N/O" (not observed) only if the item was genuinely not observable (e.g., patient positioning not visible); not observed items do not count for or against the score
   - If a critical error is observed, [specify response: stop simulation / allow completion / flag immediately]
   - Do not coach the learner during the scored portion of the assessment
   - Complete the narrative feedback field and global rating before leaving the observation area

## False-Positive Prevention

| ❌ Common Mistake | ✅ Correct Approach |
|---|---|
| Vague checklist items ("performs correctly," "demonstrates proper technique") | Every item must describe one specific observable behavior: "Applies sterile drape to field without touching the non-sterile outer packaging with gloved hands" — if you cannot observe it happening or not happening in real time, it is not a valid checklist item |
| Omitting critical error flags | Some omissions must trigger automatic failure regardless of total score; if these are buried in the regular checklist, they will be treated like any other item — list critical errors separately and state the consequence explicitly |
| More than 25 items | Observer cognitive load above 25 items reliably degrades reliability across observation studies; if a skill genuinely requires more, split into two sequential checklists (Preparation and Setup; Procedure and Completion) |
| One checklist for all learner levels | A novice checklist for M1 students should include hand hygiene and equipment check (not automatic at that level); an attending competency checklist should focus on efficiency, adaptive response, and complication recognition — the same checklist serves neither population well |
| Combining two behaviors in one item | "Explains procedure and confirms consent" is two behaviors — a learner who explains but forgets to confirm consent cannot be scored; write two separate items so each can be marked independently |
| Sequencing items by importance rather than clinical order | Observers score in real time; if the checklist is not in procedural order, observers must search the list while watching the learner — use clinical sequence, not priority order |

## Output Format

Deliver the complete checklist in this structure:

---

**CHECKLIST OVERVIEW**
- Skill: [specific name]
- Learner level: [level]
- Assessment context: [Formative / OSCE / Direct observation / Certification exam]
- Total scored items: [X]
- Critical error items: [X listed separately]
- Pass threshold: [X% or X of Y items — and critical error rule]
- Time allotment: [X minutes for procedure + Y minutes for debrief]

---

**OBSERVER INSTRUCTIONS**

[One paragraph for the observer completing this checklist]

---

**SECTION 1: PREPARATION AND SETUP**

| # | Item | ✓ Performed | ✗ Not Performed | N/O |
|---|---|---|---|---|
| 1 | [Observable behavior] | ☐ | ☐ | ☐ |
| 2 | [Observable behavior] | ☐ | ☐ | ☐ |

---

**SECTION 2: PROCEDURAL STEPS** *(in clinical order)*

| # | Item | ✓ Performed | ✗ Not Performed | N/O |
|---|---|---|---|---|
| 3 | [Observable behavior] | ☐ | ☐ | ☐ |

---

**SECTION 3: COMMUNICATION AND PATIENT INTERACTION**

| # | Item | ✓ Performed | ✗ Not Performed | N/O |
|---|---|---|---|---|

---

**SECTION 4: SAFETY AND HYGIENE**

| # | Item | ✓ Performed | ✗ Not Performed | N/O |
|---|---|---|---|---|

---

**CRITICAL ERRORS** *(automatic failure if any item checked)*

| Critical Error | Observed? | Action |
|---|---|---|
| [Specific behavior] | ☐ Yes ☐ No | [Stop simulation / Flag for review] |

---

**GLOBAL RATING**

☐ 3 — Satisfactory: [behavioral anchor]
☐ 2 — Borderline: [behavioral anchor]
☐ 1 — Unsatisfactory: [behavioral anchor]

---

**SCORING SUMMARY**

- Items performed: \_\_ / \_\_ = \_\_ %
- Critical errors: ☐ None ☐ Yes — specify: \_\_\_\_\_\_\_\_\_
- Pass/Fail: ☐ Pass ☐ Fail
- Global rating: \_\_
- Overall result: ☐ Pass ☐ Fail

---

**OBSERVER NARRATIVE FEEDBACK** *(complete before leaving observation area)*

What went well (one specific behavior):
[Text field]

What to change (one specific behavior, stated as the desired action):
[Text field]

---

## Example Output Snippet

> **SECTION 2: PROCEDURAL STEPS — Peripheral IV Insertion (Partial)**
>
> | # | Item | ✓ Performed | ✗ Not Performed | N/O |
> |---|---|---|---|---|
> | 6 | Applies tourniquet 3–4 inches above intended insertion site | ☐ | ☐ | ☐ |
> | 7 | Identifies vein by visual inspection and palpation before reaching for catheter | ☐ | ☐ | ☐ |
> | 8 | Cleanses insertion site with alcohol wipe using circular motion outward from center; allows to air dry | ☐ | ☐ | ☐ |
> | 9 | Removes needle cap and inserts catheter at 10–30 degree angle, bevel up | ☐ | ☐ | ☐ |
> | 10 | Observes for blood flashback in catheter hub before advancing | ☐ | ☐ | ☐ |
> | 11 | Advances catheter into vein while simultaneously withdrawing needle | ☐ | ☐ | ☐ |
> | 12 | Releases tourniquet before connecting IV tubing or flushing | ☐ | ☐ | ☐ |
>
> **CRITICAL ERRORS**
>
> | Critical Error | Observed? | Action |
> |---|---|---|
> | Recaps needle after use | ☐ Yes ☐ No | Automatic failure; stop simulation; debrief sharps safety |
> | Fails to dispose of needle in sharps container immediately after withdrawal | ☐ Yes ☐ No | Automatic failure; flag for immediate debrief |
> | Contaminates sterile field after setup | ☐ Yes ☐ No | Automatic failure; stop and restart |

## Verification Checklist
- [ ] Learner level explicitly specified and checklist scope calibrated accordingly
- [ ] Every item states one specific observable binary behavior — no vague items
- [ ] Items sequenced in clinical order, not by importance
- [ ] Total items do not exceed 25 without explicit justification
- [ ] Critical errors listed separately with automatic failure consequence stated
- [ ] Communication and patient interaction items included (minimum 3)
- [ ] Safety and hygiene items included (hand hygiene, sharps, sterile field if applicable)
- [ ] Global rating scale has behavioral anchors for all 3 levels
- [ ] Scoring guide specifies pass threshold, critical error interaction, and global rating rule
- [ ] Observer instructions included on the form
