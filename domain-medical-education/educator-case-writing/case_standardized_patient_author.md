---
title: "Standardized Patient Scenario Writer"
category: medical-education/educator-case-writing
description: "Write complete standardized patient encounter scenarios including patient script, doorway information card, hidden history with unlock conditions, emotional cue behavioral anchors, SP training guide, communication behaviors checklist, and post-encounter debrief questions for OSCE or formative clinical skills practice."
techniques:
  - RP-02
  - ST-02
  - CM-02
  - OC-01
  - QA-01
difficulty: intermediate
tags:
  - standardized-patient
  - clinical-skills
  - osce
  - communication
  - history-taking
  - sp-training
updated: "2026-05-15"
related_prompts:
  - ../meded_osce_station_designer.md
  - ../meded_learner_feedback_composer.md
  - ../meded_clinical_skills_checklist_designer.md
---

# Standardized Patient Scenario Writer

**Objective:** Write a complete standardized patient scenario — from doorway card through SP training guide — with behavioral anchors for emotional cues, explicit unlock conditions for hidden history, and a communication checklist that separates what the SP enacts from what the SP scores.

## When to Use
- ✅ Designing a new clinical encounter for OSCE assessment, formative clinical skills practice, or communication skills curriculum
- ✅ Training a new cohort of standardized patients who need behavioral anchors, not just a narrative script
- ✅ Creating an encounter with emotionally complex content (grief, anger, fear, domestic violence disclosure, substance use history) that requires specific portrayal coaching
- ✅ Building a history-taking encounter where hidden information is disclosed only in response to direct inquiry — testing the student's ability to ask the right questions
- ❌ When the primary clinical skill being assessed is physical examination technique rather than history-taking or communication — physical examination OSCE stations require SP training guides that specifically address "what to report when palpated," which is a specialized format outside this prompt's scope
- ❌ When a high-stakes summative OSCE is the context — scoring reliability and standard-setting for high-stakes assessment require psychometric oversight beyond prompt-generated content; use this prompt for formative or low-stakes assessment and as a drafting tool for expert review

## Inputs Required
- **Learner level:** M1, M2, M3, M4, Resident PGY-1 to PGY-3, Fellow, or Advanced Practice Learner
- **Clinical domain and presenting complaint:** e.g., "Psychiatry — depressive symptoms and suicidal ideation," "Internal Medicine — chest pain in a 55-year-old," "Pediatrics — caregiver reporting a 6-year-old's recurrent abdominal pain"
- **Primary clinical skill to assess:** specify the domain (e.g., history-taking, communication of bad news, motivational interviewing for health behavior change, informed consent discussion)
- **Hidden history topics:** specify what sensitive information the patient holds back unless directly asked (e.g., domestic violence, illicit drug use, sexual history, psychiatric history, financial barriers to medication adherence)
- **Emotional arc:** describe the patient's emotional state at encounter start and any emotional shifts that occur (e.g., "starts guarded and defensive, becomes tearful when son's hospitalization is mentioned, anger if student uses jargon without explanation")
- **Encounter length:** specify the allotted time (common formats: 8-minute, 12-minute, 15-minute, 20-minute encounters)
- **Assessment purpose:** formative (learning-focused, SP gives verbal feedback at end) or summative (scored OSCE station, SP completes checklist only)

## Constraints

**Must:**
- Write separate SP script and scoring checklist documents — these are distinct artifacts serving different purposes
- Include specific behavioral anchors for every emotional cue ("cry when the student says the word 'cancer'" not "appear sad")
- Specify exact unlock conditions for all hidden history items: the precise question type or topic the student must raise to trigger disclosure
- Write a verbatim opening statement: the first words the SP says when the student enters
- Include an SP training guide that anticipates common student errors and provides scripted SP responses
- Calibrate the encounter to the specified learner level: an M1 communication encounter differs in complexity from a PGY-2 informed consent encounter

**Must Not:**
- Write a fully cooperative patient script where the SP volunteers all information without prompting — real patients require inquiry; over-volunteering invalidates the assessment of history-taking skill
- Conflate the SP script (what to say and do) with the scoring checklist (what to observe and score) — they are separate documents
- Omit portrayal coaching — SPs need behavioral anchors, not just narrative understanding of the character
- Write a single static emotional state for the patient — patient affect changes in response to student behavior; specify the triggers
- Include medical jargon in patient dialogue — the patient speaks as a lay person; technical terms belong in the SP training guide, not the patient script

## Instructions

1. **Collect inputs from the educator.**
   - Confirm: learner level, clinical domain and presenting complaint, primary clinical skill, hidden history topics, emotional arc description, encounter length, and assessment purpose.
   - Ask whether the SP will also complete a post-encounter checklist without the student present, or whether a separate examiner will score in real time.
   - Ask whether the scenario should include a physical examination component (SP reports scripted findings when examined) or is history-taking and communication only.
   - Ask whether the SP should give immediate verbal feedback to the student after the encounter (formative model) and if so, what key feedback messages the educator wants the SP to deliver.

2. **Write the Doorway Information Card.**
   - This is the written card the student reads outside the room before entering. It must include:
     a. Patient name, age, sex
     b. Reason for visit (1-2 sentences, as brief as a triage note)
     c. Vital signs if relevant (typically provided for urgent/acute scenarios)
     d. Task instruction: what the student is asked to do in this encounter (e.g., "Take a focused history and address the patient's concerns. You will have 15 minutes.")
   - The doorway card must not reveal the diagnosis, hidden history, or the emotional arc.

3. **Write the Patient Background Document (SP Reference — Not Learner-Facing).**
   - This is the SP's complete backstory and characterization guide. Include:
     a. Full name, age, occupation, living situation, family context
     b. Medical history (by system), surgical history, current medications, allergies
     c. Social history: substance use, housing, finances, relationships, cultural background
     d. Family history relevant to the presenting complaint
     e. Review of systems (by system — what the patient would report if asked about each system)
   - Specify which information is volunteered and which is hidden (see Step 4 for hidden history).

4. **Write the Hidden History and Unlock Conditions.**
   - For each piece of hidden history, specify:
     a. The information itself (what the SP will disclose when unlocked)
     b. The exact unlock condition: the type of question or topic the student must raise (e.g., "Disclose domestic violence history only if the student asks directly about safety at home using language like 'Do you feel safe?' or 'Is anyone hurting you?' — indirect questions or questions about 'stress at home' do not unlock this disclosure")
     c. The SP's disclosure response: verbatim or near-verbatim language the SP uses when disclosing (e.g., "Well… there is something I haven't told anyone. My husband has been hitting me.")
     d. Post-disclosure behavior: how the SP behaves immediately after disclosing (e.g., "look down, speak quietly, do not make eye contact for 10-15 seconds — wait to see how the student responds before continuing")
   - Include at least 2 hidden history items for intermediate/advanced learner levels; 1 is sufficient for M1/M2 encounters focused on basic history-taking.

5. **Write the Verbatim Opening Statement.**
   - Write exactly what the SP says when the student enters the room — the first words spoken.
   - The opening statement should: (a) be naturalistically appropriate to the clinical setting, (b) reflect the patient's emotional state at encounter start, and (c) not volunteer the chief complaint immediately (leave room for the student to elicit it).
   - Example format: a greeting, a brief expression of emotional state, or a question the patient asks before the student can begin.

6. **Write the Emotional Cue Behavioral Anchors.**
   - List every emotional shift the patient may display, with:
     a. The trigger: what the student says or does that causes the emotional shift
     b. The behavioral display: specific, observable, reproducible behaviors (not "appear anxious" but "shift in chair, avoid eye contact, speak more quietly, cross arms")
     c. The recovery: if the patient's emotional state should return to baseline, specify what student behavior triggers recovery
   - Write behavioral anchors for at least 3 emotional states: the starting state and at least 2 emotional shifts.
   - Specify any emotional state that is NOT triggered by student behavior — emotions that are present throughout regardless of what the student does (e.g., "patient is chronically fatigued; this appears as slow speech and delayed responses throughout, regardless of student behavior").

7. **Write the SP Training Guide.**
   - This is the coaching document the SP uses to prepare for the role. Include:
     a. Character overview: 2-3 sentences on who this patient is and what they want from this encounter
     b. Behavioral anchors summary: all triggers and displays from Step 6 in a compact table
     c. Response to common student errors: for each of 3-4 likely student errors (e.g., asking leading questions, using medical jargon, interrupting, failing to acknowledge emotion), write the SP's scripted response
     d. What unlocks hidden information: a simplified table of unlock conditions from Step 4 for quick reference during role preparation
     e. What the patient will NOT say unless asked: a brief checklist of withheld information to prevent over-volunteering
     f. Physical portrayal notes: posture, clothing, affect presentation on entry, any props (tissues, medications in a bag, a phone the patient checks anxiously)

8. **Write the Communication Behaviors Checklist.**
   - This is the scoring document — separate from the SP script.
   - Write 12-20 binary items (did/did not observe) describing specific, directly observable student behaviors.
   - Each item must be directly observable without inference: "Student introduced themselves by name" (observable) not "Student was professional" (requires inference).
   - Categories to include: introduction and consent, agenda-setting, active listening behaviors, empathy and acknowledgment, information-gathering technique, response to emotional cues, disclosure of sensitive topics, closure and next steps.
   - Flag 2-3 items as "critical behaviors" — items that if not performed represent a significant communication failure the educator should debrief regardless of overall score.
   - Write one global rating item at the end: "Overall, this student communicated effectively with this patient" (1 = strongly disagree to 5 = strongly agree).

9. **Write the Post-Encounter Debrief Questions.**
   - Write 4-5 questions the SP asks the student immediately after the encounter (formative model) or that an educator uses in group debrief.
   - At least one question should ask the student about their subjective experience: "Was there a moment in the encounter when you felt unsure of how to proceed?"
   - At least one question should ask the student to reflect on the patient's perspective: "From where you were sitting, what do you think the patient most needed from you in that encounter?"
   - At least one question should be specific to the hidden history: "Did you get a sense that there was something the patient hadn't told you? What cues led you to that impression?"

10. **Deliver the complete scenario as separate documents.**
    - Produce: (1) Doorway Information Card, (2) SP Background and Script, (3) SP Training Guide, (4) Communication Checklist, (5) Post-Encounter Debrief Questions — as clearly labeled separate sections.
    - If the assessment purpose is formative, add an SP feedback guide: a 3-sentence template the SP uses to give verbal feedback to the student ("One thing you did well was… One thing to consider next time is… One question I have for you as the patient is…").

## False-Positive Prevention

| ❌ Common Mistake | ✅ Correct Approach |
|---|---|
| Fully cooperative SP script where the patient volunteers all history without being asked | Real patients require inquiry; SPs must wait to be asked and resist over-volunteering — hidden history is disclosed only when specific unlock conditions are met |
| Conflating the SP script with the scoring checklist | The SP script tells the SP what to say and do; the checklist tells the SP what to observe and score — combining them creates confusion about the SP's two distinct roles |
| Emotional cue instructions written as internal states ("feel sad") rather than behavioral anchors ("lower voice, look down, pause 3-5 seconds before responding") | SPs need reproducible behavioral anchors to portray emotions consistently across multiple encounters with different students |
| Single emotional state throughout the encounter regardless of student behavior | Patient affect changes in response to student behavior; specify triggers for at least 2 emotional shifts so that the SP's portrayal can respond to the learner's actions |
| Checklist items requiring inference ("student was empathic," "student was professional") | Every checklist item must describe a directly observable behavior: "Student asked the patient if they had any questions before the encounter ended" |
| Medical jargon in patient dialogue | The patient speaks as a lay person; SP training guides can use medical terminology for clarity, but the patient script must reflect authentic lay speech |

## Output Format

The output should be organized as the following five labeled documents:

### DOCUMENT 1: Doorway Information Card (Student-Facing)
- Patient name, age, sex, reason for visit, vital signs (if applicable), task instruction, time limit

### DOCUMENT 2: SP Background and Full Script (SP Reference)
- Character overview
- Complete patient history by category (medical, surgical, medications, allergies, social, family, ROS)
- Volunteered information vs. withheld information (labeled clearly)
- Verbatim opening statement
- Hidden history items with unlock conditions and disclosure language
- Emotional cue triggers and behavioral displays
- Post-disclosure behavioral notes

### DOCUMENT 3: SP Training Guide
- Character overview (2-3 sentences)
- Behavioral anchors summary table (trigger | display | recovery)
- Response to 3-4 common student errors (scripted SP responses)
- Quick-reference unlock conditions table
- What the patient will NOT say unless asked (checklist)
- Physical portrayal notes (posture, props, clothing, affect on entry)
- SP feedback template (if formative)

### DOCUMENT 4: Communication Behaviors Checklist (Scoring)
- 12-20 binary items by category
- 2-3 critical items flagged
- Global rating scale item (1-5 with anchors)

### DOCUMENT 5: Post-Encounter Debrief Questions
- 4-5 debrief questions (numbered, with Bloom's level tag)

---

## Example Output Snippet

The following is an example of **Document 2: Opening Statement and Emotional Cues** for an M3 Psychiatry SP scenario on a patient presenting with depressive symptoms:

---

**Verbatim Opening Statement:**

> *(SP is sitting with hands folded in lap, looking at the floor when student enters. Looks up slowly.)*
> "Oh — hi. Sorry, I didn't hear you come in. I've been… I don't know. Not sleeping well." *(pause 2 seconds)* "The front desk said someone was going to talk to me."

**Emotional Cue Behavioral Anchors:**

| Trigger | Display | Recovery |
|---|---|---|
| Student uses the word "depressed" or "depression" without first acknowledging the patient's experience | Stiffen posture, cross arms, say "I'm not crazy, I just can't sleep" — become guarded for the next 2-3 exchanges | If student acknowledges ("That wasn't what I meant — I just want to understand what you're going through"), visibly soften posture and resume moderate eye contact |
| Student asks about whether patient has thought about hurting herself | Pause 4-5 seconds, look away, say quietly "I've… had thoughts. But I'd never actually do anything" — hold emotional state for remainder of disclosure | Do not recover to prior baseline; remain quiet and watchful for student's response |
| Student rushes through questions or interrupts | Speak more slowly, answer in shorter sentences, begin looking at the door | If student slows down and asks "How are you feeling about our conversation so far?", re-engage with slightly more detail |
| Student directly acknowledges something the patient said with empathy ("That sounds really hard") | Brief eye contact, slight relaxation of crossed arms, 1-2 word acknowledgment ("Yeah.") — then waits | N/A — this is a positive emotional shift; maintain slightly more open posture |

---

## Verification Checklist
- [ ] Learner level explicitly specified and encounter complexity calibrated to that level
- [ ] SP script and scoring checklist are separate documents — not combined
- [ ] Every emotional cue has a specific behavioral anchor (not an internal state description)
- [ ] Every hidden history item has an exact unlock condition specifying the question type that triggers disclosure
- [ ] Verbatim opening statement written and included
- [ ] Communication checklist items describe directly observable behaviors only — no inference required
- [ ] SP training guide includes response to at least 3 common student errors with scripted SP language
- [ ] Post-encounter debrief includes a question about the patient's perspective and a question about hidden history
