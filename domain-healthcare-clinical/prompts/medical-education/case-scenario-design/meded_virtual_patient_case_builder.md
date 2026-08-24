---
title: "Virtual Patient Case Builder"
category: healthcare-clinical/medical-education
description: "Build branching virtual patient cases with decision nodes, clinical consequence logic, graduated feedback text, optimal path specification, and learning objective mapping for deployment on e-learning platforms including CASUS, DxR, OpenLabyrinth, and custom LMS environments."
techniques:
  - ST-02
  - RT-03
  - CM-02
  - OC-01
  - QA-01
difficulty: advanced
tags:
  - virtual-patient
  - branching-logic
  - e-learning
  - decision-making
  - clinical-simulation
  - medical-education
updated: "2026-05-15"
related_prompts:
  - ../meded_progressive_disclosure_case_designer.md
  - ../meded_simulation_scenario_designer.md
  - ../meded_pbl_case_writer.md
---

# Virtual Patient Case Builder

**Objective:** Build a complete branching virtual patient case with decision nodes, clinically calibrated consequence logic, graduated formative feedback at every branch, learning objective mapping, and platform-agnostic scripting ready for deployment in e-learning environments.

## When to Use
- ✅ Creating self-paced clinical reasoning practice that learners complete asynchronously
- ✅ Building decision-making exercises for topics where consequence of choice is educationally important (not just "correct answer" identification)
- ✅ Scaling clinical reasoning instruction when simulation time or standardized patients are limited
- ✅ Designing remediation pathways that direct struggling learners to targeted content based on their choices
- ❌ When the primary learning goal is procedural skill acquisition — virtual patients teach decision-making, not manual technique
- ❌ When the topic is so straightforward that all reasonable learners would make identical choices — VP cases require genuine decision complexity to justify branching
- ❌ When assessment (not learning) is the primary goal and branch path data is needed for high-stakes scoring — VP cases optimized for assessment require psychometric validation outside this prompt's scope

## Inputs Required
- **Learner level:** M1, M2, M3, M4, Resident PGY-1 to PGY-3, Fellow, or Advanced Practice Learner
- **Clinical domain / specialty:** e.g., Emergency Medicine, Internal Medicine, Pediatrics, Psychiatry
- **Presenting complaint and core clinical decision:** the patient problem and the type of decision the VP case is designed to exercise (e.g., "undifferentiated chest pain — decision: initial workup prioritization")
- **Learning objectives:** 3-5 specific LOs this case will address; each node will be mapped to one or more
- **Target platform (or platform-agnostic):** CASUS, DxR Clinician, OpenLabyrinth, custom LMS, or specify "platform-agnostic scripting format"
- **Desired case complexity:** specify number of decision nodes (minimum 3, recommended 3-5 for a 20-40 minute self-paced session)
- **Optimal path designation:** indicate whether the case has one clearly optimal path, multiple valid management approaches, or deliberately constructed near-optimal vs. suboptimal branches

## Constraints

**Must:**
- Change the patient's clinical state based on learner choices — decision nodes must have clinically meaningful consequences, not just narrative flavor text
- Provide formative feedback at every decision node for every option chosen (not just at case end)
- Graduate consequences across at least three levels: optimal → suboptimal → harmful (or near-miss → missed → critical failure)
- Specify at least one critical failure state that terminates the case with strong corrective feedback
- Map every learning objective to the node(s) where it is exercised
- Include platform-agnostic scripting notes explaining how to translate the case structure into the specified or generic LMS

**Must Not:**
- Build a linear quiz with a story wrapper — patient state must change based on choices; this is the defining feature of a VP case
- Penalize all non-optimal paths equally — graduated consequences reflect clinical reality and prevent learned helplessness
- Omit feedback on any choice, including wrong ones — formative feedback at every node is non-negotiable
- Frame the case as having a single "correct" path when multiple management approaches are clinically valid — acknowledge valid variation explicitly
- Introduce new clinical information at a node that is not causally connected to the learner's prior choices — consequence logic must be traceable

## Instructions

1. **Collect inputs from the educator.**
   - Confirm: learner level, clinical domain, presenting complaint, core clinical decision, 3-5 LOs, target platform, desired number of nodes, optimal path designation.
   - Ask the educator: Should the case terminate at all critical failure states, or should the learner be allowed to recover after a suboptimal choice? (Determines whether the branching structure is "hard penalizing" or "corrective redirection.")
   - Ask: Does the platform support multimedia (audio, video, images, labs) or text-only? This affects how clinical information is delivered at each node.

2. **Design the case backbone and patient identity.**
   - Write complete patient demographics, opening scene text (what the learner sees when they enter the case), and clinical setting.
   - Decide the diagnosis and the key clinical decision points before writing the branches — work backwards from what you want learners to decide, then construct the scenario to make those decisions meaningful.
   - Write the "complete patient truth" document (internal to the case builder, not shown to learner): the full history, findings, diagnosis, and management — all facts available across all branches, from which you will selectively reveal information at each node.

3. **Write the Opening Scenario.**
   - Patient demographics, chief complaint, clinical setting, and opening vital signs.
   - Opening question or task prompt: what the learner must do first (e.g., "You walk into Room 4. What will you do first?" followed by branching options).
   - 3-4 opening choices, representing: one optimal first step, one defensible near-optimal step, one suboptimal step that is common in practice, and one clearly harmful or inappropriate step.

4. **Write Decision Node 1.**
   For each choice at Node 1, specify:
   - **Consequence text:** what happens to the patient in clinical terms (vital sign changes, symptom evolution, new findings) as a result of this choice. Consequences must be clinically plausible given the case facts.
   - **Feedback text:** formative feedback explaining why this choice led to this consequence. For optimal choices: affirm and explain the reasoning. For suboptimal choices: explain what was missed and why the consequence followed. For harmful choices: explain the mechanism of harm clearly.
   - **Next node:** which node the learner proceeds to from this choice (optimal and near-optimal paths typically advance to Node 2; suboptimal paths may regress or branch to a remediation node; harmful paths may terminate or require critical recovery).
   - Write the options at Node 2 (the next clinical situation the learner faces from the optimal path).

5. **Write Decision Node 2.**
   - Present the next clinical situation based on patient state after Node 1 (which should reflect what happened as a result of the learner's Node 1 choice on the optimal path).
   - Write 3-4 choices at Node 2, with consequence text, feedback text, and next node specification for each.
   - At Node 2, introduce at least one piece of new clinical information (lab result, imaging finding, specialist input) that was not available at Node 1 — this tests whether learners integrate new data or anchor on initial impression.

6. **Write Decision Node 3 (and additional nodes as specified).**
   - Node 3 typically represents the management or disposition decision.
   - Specify whether Node 3 is the terminal node or whether additional nodes follow.
   - If this is the terminal node, write the Case Resolution: what happens to the patient over the next 24-72 hours as a result of all the learner's choices (optimal path: recovery; near-optimal: recovery with complication; suboptimal: preventable harm or prolonged course; harmful: serious adverse outcome).

7. **Write Critical Failure States.**
   - Write at least 2 critical failure state termination points: specific choice combinations or individual choices that result in severe patient harm, missed diagnosis, or death.
   - For each critical failure state, write:
     a. A clinical consequence description (what happens to the patient)
     b. A strong corrective feedback statement (not a lecture — a direct, specific explanation of what the error was and what should have been done)
     c. A redirect prompt: invite the learner to restart the case from the most recent safe decision point, or restart from the beginning
   - Critical failure states must be clinically defensible — do not create artificial failure states that penalize reasonable practice variation

8. **Write the Learning Objective Trigger Map.**
   - Create a table: Learning Objective | Decision Node Where Exercised | Choice That Demonstrates Mastery | Choice That Reveals Gap
   - Every LO must appear in the table. The "Choice That Reveals Gap" column identifies which distractor choice a learner who has not mastered the LO is most likely to select.

9. **Write the Optimal Path Specification.**
   - Write the complete optimal path as a narrative: what the learner chooses at each node, what consequence follows, and what feedback they receive.
   - If multiple management paths are clinically valid, write a "valid variation note" specifying which alternate paths are acceptable and what distinguishes them from suboptimal choices.
   - The optimal path narrative is intended for the educator's reference and for QA before platform upload — it is not shown to learners.

10. **Write the Platform-Agnostic Scripting Format and Adaptation Notes.**
    - Describe the case structure in a table with columns: Node ID | Node Prompt | Option | Consequence | Feedback | Next Node ID
    - Write a brief note for each of the following platforms explaining how to map this structure: CASUS (scenario tree with node types), DxR Clinician (patient encounter with branching orders), OpenLabyrinth (map node structure), custom LMS (SCORM package branching logic).
    - If the educator specified a single platform, provide detailed adaptation notes for that platform only.

## False-Positive Prevention

| ❌ Common Mistake | ✅ Correct Approach |
|---|---|
| Linear quiz with story wrapper ("Read the case, answer Question 1, read more case, answer Question 2") | True VP cases change the patient's clinical state based on learner choices; a patient who receives the wrong workup presents differently at Node 2 than one who received the right workup |
| Penalizing all non-optimal paths equally with the same "incorrect — try again" message | Graduated consequences: near-miss paths lead to delay or complication; suboptimal paths lead to preventable harm; harmful paths lead to severe outcome — each with calibrated feedback |
| Omitting feedback on "wrong" choices and providing feedback only at case end | Formative feedback at every node, for every choice — the feedback is the instruction; withholding it until the end removes the learning mechanism |
| Framing all paths except one as "wrong" when multiple management approaches are clinically valid | Acknowledge clinical validity of alternative approaches explicitly; distinguish "clinically valid variation" from "suboptimal" from "harmful" in the consequence logic |
| Decision nodes that are purely factual recall (e.g., "What is the normal range of serum sodium?") | Every decision node should require clinical judgment, not factual retrieval; use progressive disclosure cases or MCQ writers for factual recall |
| Introducing information at a node that is not causally connected to prior choices | Consequence logic must be traceable: the learner's Node 1 choice must plausibly cause the Node 2 state; arbitrary information injection breaks clinical realism |

## Output Format

The output should be organized in the following sections, each clearly headed:

### Case Overview
- Case name, clinical domain, learner level, presenting complaint, core clinical decision, number of nodes, estimated completion time, educational rationale

### Patient Identity and Opening Scene
- Demographics, chief complaint, clinical setting, vital signs, opening scene narrative text, opening task prompt

### Complete Patient Truth Document (Educator Reference — Not Shown to Learner)
- Full history, all physical findings, diagnosis, and ideal management — the facts pool from which nodes draw selectively

### Decision Node 1
- Node prompt (what the learner reads/sees)
- Options (3-4), each with: option text | consequence text | feedback text | next node ID
- Node LO trigger note: which learning objective this node exercises

### Decision Node 2
- Same structure as Node 1
- New information introduced at this node (with justification for why it appears here)

### Decision Node 3 (and additional nodes)
- Same structure; terminal nodes include Case Resolution narrative

### Critical Failure States
- Failure state trigger (which choice combination or single choice)
- Clinical consequence description
- Corrective feedback statement
- Restart or redirect prompt

### Learning Objective Trigger Map
- Table: LO | Node Where Exercised | Mastery Choice | Gap-Revealing Choice

### Optimal Path Specification
- Narrative walkthrough of optimal choices, consequences, and feedback at each node
- Valid variation note (if applicable)

### Platform-Agnostic Scripting Table
- Node ID | Node Prompt | Option | Consequence | Feedback | Next Node ID
- Platform adaptation notes

---

## Example Output Snippet

The following is an example of **Decision Node 1** for an M3 Emergency Medicine virtual patient case on undifferentiated chest pain:

---

**Decision Node 1: The First Five Minutes**

> You enter Room 7. Mr. D.W. is a 52-year-old male who arrived via EMS reporting chest pain that started 45 minutes ago while mowing his lawn. He is diaphoretic and pale. BP 138/88, HR 102, RR 20, SpO2 94% on room air. He is clutching his chest and says, "It feels like something is sitting on me."
>
> **What do you do first?**

| Option | Consequence | Feedback | Next Node |
|---|---|---|---|
| **A. Obtain a 12-lead ECG immediately while placing IV access and supplemental oxygen** | ECG completed in 4 minutes. STEMI pattern: ST elevation in leads II, III, aVF, with reciprocal changes in I and aVL. Cath lab team is available. | Optimal first step. In suspected ACS, the 12-lead ECG is the highest-yield, time-sensitive action that determines the entire management trajectory. Simultaneous IV access and O2 are appropriate supportive measures. | Node 2A (STEMI pathway) |
| **B. Administer aspirin 325 mg and obtain IV access, then order ECG** | Aspirin administered. ECG obtained 8 minutes after arrival. STEMI identified. Door-to-balloon time is already compressed. | Aspirin is appropriate but not the first action — the ECG should precede antiplatelet therapy because the diagnosis must be confirmed before initiating irreversible therapy. You cost 4 minutes of door-to-balloon time. | Node 2B (STEMI with delay) |
| **C. Order a chest X-ray, troponin, BMP, and ECG simultaneously** | ECG returned in 6 minutes showing STEMI. However, waiting for the X-ray result before calling cath lab adds 12 minutes to door-to-balloon time. | In an undifferentiated chest pain patient with high pretest probability for ACS, the ECG alone drives the STEMI diagnosis and cath lab activation. Waiting for other results before ECG review delays reperfusion. | Node 2B (STEMI with delay) |
| **D. Administer sublingual nitroglycerin for pain relief and reassess in 5 minutes** | Nitroglycerin given. BP drops to 82/54. Patient becomes diaphoretic and confused. ECG obtained emergently shows inferior STEMI with suspected right ventricular involvement. | Nitroglycerin is contraindicated in RV infarction (common in inferior STEMI) because it causes preload reduction that precipitates hemodynamic collapse. This choice caused a critical complication before the diagnosis was established. | Critical Failure State 1 |

---

## Verification Checklist
- [ ] Learner level explicitly specified and case complexity calibrated to that level
- [ ] Every decision node changes patient clinical state based on learner choice — not just narrative flavor text
- [ ] Formative feedback provided at every node for every option, including optimal choices
- [ ] Consequences are graduated: optimal → suboptimal → harmful — not binary correct/incorrect
- [ ] At least 2 critical failure states specified with corrective feedback and restart prompts
- [ ] Learning Objective Trigger Map is complete — every LO mapped to a node
- [ ] Optimal path narrative written for educator QA reference
- [ ] Platform-agnostic scripting table includes all node IDs, options, consequences, feedback, and next-node pointers
