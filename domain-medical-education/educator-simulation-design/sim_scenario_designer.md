---
title: "Simulation Scenario Designer"
category: medical-education/educator-simulation-design
description: "Design complete high-fidelity simulation scenarios with pre-briefing script, manikin state progressions with action-based triggers, confederate role scripts, embedded clinical cues, learning objective-linked debriefing objectives, and team composition guidance for emergency and acute care training."
techniques:
  - ST-02
  - CM-02
  - RT-03
  - ED-01
  - QA-01
difficulty: advanced
tags:
  - simulation
  - high-fidelity
  - debriefing
  - team-training
  - clinical-emergency
  - medical-education
updated: "2026-05-15"
related_prompts:
  - ../meded_debriefing_guide_designer.md
  - ../meded_standardized_patient_scenario_writer.md
  - ../meded_progressive_disclosure_case_designer.md
---

# Simulation Scenario Designer

**Objective:** Design a complete high-fidelity simulation scenario — from pre-briefing script through state-by-state manikin progressions, confederate role scripts, embedded cue library, and debriefing objectives — with action-based state triggers that make learner decisions drive clinical consequence.

## When to Use
- ✅ Designing a team-training scenario for emergency, acute care, or high-acuity clinical situations
- ✅ Building a scenario where learner actions (not just time) drive clinical deterioration or improvement
- ✅ Creating a scenario intended to surface interprofessional communication failures, team dynamics, or system-level issues
- ✅ Designing a scenario with a deliberate debriefing objective — a specific mental model or assumption the debrief is intended to surface and examine
- ❌ When the primary learning goal is individual procedural skill (e.g., endotracheal intubation technique) — procedural skill is better developed with task trainers and deliberate practice; full scenario design is appropriate for integration and decision-making
- ❌ When learner groups are individuals rather than teams — single-learner scenarios with confederate support can work, but the team dynamics objectives in this prompt require at least 2 learners
- ❌ When the simulation center does not have staff available to run confederate roles — embedded cues and confederate scripts require trained personnel; without them, use a lower-fidelity or tabletop format

## Inputs Required
- **Learner level and team composition:** e.g., "2 PGY-2 Internal Medicine residents + 1 RN + 1 respiratory therapist" or "4 M4 students in their acting internship"
- **Clinical domain and acute care situation:** the type of clinical emergency or acute deterioration (e.g., "adult septic shock," "pediatric respiratory failure," "post-operative hemorrhage")
- **Learning objectives:** 3-5 observable behavioral objectives; at minimum one should be clinical decision-making, one team communication, and one system-level behavior (closed-loop communication, role clarity, escalation)
- **Debriefing objectives:** separate from learning objectives — 2-3 mental models or assumptions to surface and examine in debrief (e.g., "the belief that a normal blood pressure rules out sepsis," "the assumption that someone else has called for help")
- **Simulation center capabilities:** manikin model if known (SimMan 3G, METIman, CAE HPS, etc.), available monitoring equipment, medication availability, and number of confederates available
- **Scenario duration:** total simulation time not including pre-brief or debrief; typical high-fidelity scenarios run 15-25 minutes
- **Endpoint type preference:** stabilization, deterioration requiring escalation, or patient death — specify which is educationally appropriate for this learner level and objective set

## Constraints

**Must:**
- Use action-based state triggers for the majority of state transitions — learner actions (or inaction) must drive most changes in patient state, not the clock alone
- Write separate learning objectives (what the team should do) and debriefing objectives (what mental models to surface in debrief) — these are distinct constructs prepared and used differently
- Include a complete pre-briefing script with psychological safety language, fiction contract, and learning focus framing
- Write confederate roles with scripted behaviors, embedded cue timing, and instructions for what to do when learners ask for help versus when to actively escalate
- Specify at least 3 distinct manikin states (Initial, Deterioration/Evolution, Resolution or Crisis) with full vital signs for each
- Include a facilitator control guide: specific adjustments for each state transition

**Must Not:**
- Use time-only triggers for most state transitions — if the scenario progresses regardless of learner action, it removes the consequence of clinical decision-making that is the core educational mechanism
- Conflate simulation learning objectives (behavioral goals for the team during the scenario) with debriefing objectives (frames of reference to examine after) — they serve different functions
- Omit the pre-briefing — without psychological safety establishment, performance anxiety and evaluation threat contaminate learning and distort behavior
- Write a single-state scenario — at least 2-3 states are needed to reveal team dynamics, escalation behavior, and adaptation to evolving clinical information
- Design the scenario so that the "correct" clinical management is obvious from scene entry — the scenario should require clinical reasoning, not scripted execution of a known algorithm

## Instructions

1. **Collect inputs from the educator.**
   - Confirm: learner level and team composition, clinical situation, 3-5 learning objectives, 2-3 debriefing objectives, simulation center capabilities, scenario duration, and endpoint type.
   - Ask: Is this scenario new, or a revision of an existing one? If revision, what specifically did not work in the prior version?
   - Ask: Will the scenario be debriefed using a structured framework (Debriefing with Good Judgment, PEARLS, TeamGAINS, advocacy-inquiry)? This affects how debriefing objectives are framed.
   - Ask: Is interprofessional team training a goal? If so, specify which professional roles will be present and whether there are role-specific learning objectives for any group.

2. **Write the Scenario Overview and Educational Rationale.**
   - Case name, clinical situation, target team composition, learner levels, scenario duration, endpoint type.
   - Educational rationale: one paragraph explaining why this scenario was designed, what gap in team training or clinical management it addresses, and what evidence from practice (error data, mortality data, root cause analysis) informed the design.
   - Learning objectives (3-5): each must describe an observable team behavior (e.g., "Team will recognize early sepsis and initiate fluid resuscitation within 10 minutes of scenario start" — not "understand sepsis").
   - Debriefing objectives (2-3): each must describe a mental model or assumption to surface (e.g., "Examine the belief that a mean arterial pressure of 65 mmHg confirms adequate resuscitation").

3. **Write the Pre-Briefing Script.**
   - Write a verbatim pre-briefing script the faculty delivers before the simulation begins. It must include:
     a. **Psychological safety statement:** explicit language establishing that the simulation environment is for learning, not evaluation of personal worth ("What you do in this room stays in this room. The point of simulation is to practice — including practicing failure — so we can learn from it together.")
     b. **Fiction contract:** agreement that learners will treat the manikin as a real patient ("We ask you to speak to the manikin as you would speak to a real patient — use the patient's name, respond to the monitoring as you would in the hospital.")
     c. **Learning focus framing:** brief statement of what the scenario is designed to practice — without revealing the diagnosis or the specific failures the scenario is designed to expose ("This session is designed to practice managing an acutely ill patient as a team. We'll debrief together afterward.")
     d. **Confidentiality agreement:** learners agree not to discuss the scenario content with peers who have not yet run it.
     e. **Environment orientation:** what equipment is present, what is functional, what is simulated (e.g., "The IV line is real. Medications will be drawn and administered normally. Auscultation is functional. Pupils are controlled from the control room.").

4. **Write State 1 — Initial Presentation.**
   - Write the patient handoff: a verbatim SBAR that a confederate nurse delivers to the arriving team at scenario start — the primary mechanism for delivering State 1 information.
   - State 1 manikin settings: vital signs (HR, BP, RR, SpO2, temperature, GCS if applicable), general appearance, monitoring display.
   - Physical findings available on examination: what auscultation reveals, what palpation reveals, what visual inspection shows.
   - State 1 action-based transition triggers: list 2-3 team actions that, when performed, move the scenario to State 2 (e.g., "If team administers IV fluid bolus AND obtains blood cultures AND orders lactate → transition to State 2A [partial improvement]"; "If 15 minutes elapse without fluid resuscitation → transition to State 2B [decompensation]").
   - Time-only trigger as safety net: after X minutes without appropriate action, advance to the deterioration state — but frame this as a backstop, not the primary transition mechanism.

5. **Write State 2 — Deterioration or Evolution.**
   - Specify whether State 2 is a deterioration state, an improvement state, or a branching state (multiple State 2 variants depending on which State 1 trigger was met).
   - State 2 manikin settings: updated vital signs, new physical findings, new monitoring changes.
   - New clinical information introduced at State 2: lab results delivered by control room as a phone call, imaging reports delivered by confederate radiologist, additional data requiring management revision.
   - State 2 action-based transition triggers: what team actions advance to State 3.
   - Critical action watch: if the team has not performed a specified critical action by the time State 2 is established, have the confederate nurse deliver the first embedded escalation cue.

6. **Write State 3 — Resolution, Crisis, or Escalation Required.**
   - If stabilization endpoint: write the patient improvement trajectory in response to correct management — vital sign normalization, clinical improvement signs, patient appearing more alert.
   - If deterioration endpoint: write the crisis state requiring urgent intervention — cardiac arrest, severe respiratory failure, hemodynamic collapse — including manikin settings for the crisis state.
   - If escalation required: write the clinical state signaling the team must call for external help (code team, attending escalation, ICU transfer) and the confederate behaviors that prompt or reward appropriate escalation.
   - Terminal scenario state: specify what triggers scenario end (stabilization achieved, code called and worked, faculty decision to terminate). Write verbatim faculty termination language: "Thank you — I'm going to stop the simulation there."

7. **Write Confederate Role Scripts.**
   - For each confederate role (typically: nurse, family member, consultant on phone, respiratory therapist), write:
     a. **Role characterization:** who this person is, their clinical competence level, and what they want from the encounter
     b. **Opening behaviors:** the first 2-3 things the confederate says or does at scenario start
     c. **Embedded cue schedule:** when and how to deliver escalation cues if the team is not performing expected actions — with timing triggers (e.g., "If team has not obtained IV access by minute 5, nurse says: 'Should I get another IV line? The patient's veins look difficult.'")
     d. **Response to direct requests for help:** scripted response maintaining confederate's role without leading the team (e.g., "As the nurse, I can get that for you — but you'll need to give me an order")
     e. **Response to information requests:** scripted answers to common team questions (e.g., "What is the urine output?" → "Doctor, urine output has been 10 mL over the last hour")
     f. **Escalation script:** if the team misses a critical action and active escalation is required — what the confederate says to prompt without solving (e.g., "Doctor, I'm concerned — the patient looks a lot worse. Should we be calling someone?")

8. **Write the Embedded Cue Library.**
   - An embedded cue is any verbal or environmental signal that delivers clinical information without faculty interruption.
   - Organize the cue library by type and timing:
     a. **Nurse cues:** verbal prompts the confederate nurse delivers on a schedule or in response to team behavior, with timing (e.g., "Minute 8: if no antibiotic order has been placed, nurse says: 'The pharmacy called — they're waiting for an antibiotic order.'")
     b. **Lab call script:** verbatim phone call from the "laboratory" (control room or confederate) delivering critical lab results — including the caller's opening, the results, and how they respond if asked to repeat
     c. **Radiology call script:** verbatim call from "radiology" or "imaging," if applicable
     d. **Family member statements:** if a confederate family member is present, scripted lines that add clinical context or emotional complexity
     e. **Environmental cues:** monitoring alarm settings, visible changes in patient appearance that the team should notice and respond to

9. **Write the Facilitator Control Guide.**
   - For each state and each transition trigger, write the specific manikin controller adjustments the control room operator makes: which vital sign parameters to change, which physical finding programs to activate (breath sounds, pupil response, skin color), and which monitoring alarms to enable or silence.
   - Write a contingency guide: if the team performs unexpectedly well or poorly and the scenario needs to be extended or truncated, specify what adjustments the faculty can make without breaking scenario fidelity (e.g., "If team resolves State 2 rapidly, delay State 3 improvement by having the confederate nurse note: 'BP is still borderline — 96/60. Should we give more fluid?'").

10. **Write the Debriefing Objectives and Framework.**
    - For each of the 2-3 debriefing objectives (mental models to surface), write:
      a. The mental model or assumption being examined
      b. The scenario moment designed to reveal it (which state, which action or inaction by the team)
      c. A debriefing trigger question: the specific question the facilitator uses to surface the mental model without leading (e.g., "When you saw the blood pressure at 90 systolic, what were you thinking?" — not "Did you notice the blood pressure was low?")
      d. The educational destination: the correct mental model or clinical insight the debrief helps the team arrive at through discussion — this is the intended landing point, not a script to recite
    - Recommend a debriefing framework (Debriefing with Good Judgment, PEARLS, TeamGAINS, or advocacy-inquiry) with one sentence explaining why it is appropriate for this scenario's objectives.

## False-Positive Prevention

| ❌ Common Mistake | ✅ Correct Approach |
|---|---|
| Automatic state progression driven by time alone | Most state transitions must require learner action; pure time-based progression removes the consequence of clinical decision-making, which is the core educational mechanism of simulation |
| Conflating simulation learning objectives ("team will perform X") with debriefing objectives ("examine the belief that Y") | Sim objectives state intended behaviors during the scenario; debrief objectives surface the mental models behind those behaviors — they are different outputs used at different times |
| Omitting the pre-briefing or delivering it informally | Without explicit psychological safety establishment, fiction contract, and learning focus framing, performance anxiety distorts behavior in ways that contaminate both scenario performance and debrief authenticity |
| Single-state scenario design | At minimum 2-3 states are required to surface team dynamics, adaptation to evolving information, and escalation behavior; single-state scenarios test speed of recall, not team clinical reasoning |
| Confederate nurses who solve problems the team is failing to address | Confederates provide cues and support; they do not lead clinical decision-making — a confederate who spontaneously initiates the critical intervention removes the learning experience from the team |
| Designing the scenario to "test" whether learners know the answer | High-fidelity simulation is most powerful as a formative experience; the scenario surfaces behaviors for debrief, not to catch or fail learners |

## Output Format

The output should be organized in the following sections, each clearly headed:

### Scenario Overview and Educational Rationale
- Case name, clinical situation, team composition, learner levels, duration, endpoint type, educational rationale

### Learning Objectives
- 3-5 observable team behavioral objectives (numbered)

### Debriefing Objectives
- 2-3 mental models to surface (numbered), explicitly distinct from learning objectives

### Pre-Briefing Script
- Psychological safety statement | Fiction contract | Learning focus framing | Confidentiality agreement | Environment orientation (verbatim, ready for faculty to read aloud)

### State 1 — Initial Presentation
- SBAR handoff script | Manikin settings | Physical findings available | Action-based transition triggers | Time-only safety-net trigger

### State 2 — Deterioration / Evolution
- Manikin settings | New clinical information | Action-based transition triggers | Critical action watch | Embedded cue schedule for State 2

### State 3 — Resolution / Crisis / Escalation
- Endpoint-specific state description | Manikin settings | Terminal scenario state and termination language

### Confederate Role Scripts
- For each confederate: role characterization | opening behaviors | embedded cue schedule | response to help requests | response to information requests | escalation script

### Embedded Cue Library
- Organized by cue type: nurse cues | lab call script | radiology call script | family member lines | environmental cues

### Facilitator Control Guide
- State-by-state manikin controller adjustments | Contingency protocol for early resolution or prolonged difficulty

### Debriefing Objectives and Framework
- For each objective: mental model | scenario moment | trigger question | educational destination
- Recommended debriefing framework with rationale

---

## Example Output Snippet

The following is an example of **State 1 — Initial Presentation** for a PGY-2 Internal Medicine simulation scenario on sepsis recognition and initial management:

---

**State 1 — Initial Presentation**

**SBAR Handoff (Confederate Nurse delivers at scenario start):**

> "Hi — I'm glad you're here. I've got Mr. K.T. in Bed 4. He's a 68-year-old man admitted last night for a urinary tract infection. He was doing okay earlier but in the last hour he's gotten a lot worse. His temperature this morning was 38.9. Current vitals: HR 118, BP 94/58, RR 24, SpO2 93% on room air, temperature 38.7. He's been on IV ceftriaxone since admission — first dose just two hours ago. He looks really pale and he's more confused than when he came in. I tried to call his attending but I haven't gotten a call back. I don't know what to do."

**State 1 Manikin Settings:**
- HR: 118 bpm (sinus tachycardia)
- BP: 94/58 mmHg
- RR: 24 breaths/min
- SpO2: 93% on room air
- Temperature: 38.7°C
- GCS: 13 (confused — E4, V3, M6)
- Skin: mottled, warm peripherally, dry mucous membranes on inspection
- Lung sounds: clear bilaterally

**Action-Based Transition Triggers — State 1 to State 2:**

| Team Action | Consequence | Next State |
|---|---|---|
| IV fluid bolus ≥ 30 mL/kg ordered AND blood cultures ordered AND lactate ordered | BP stabilizes to 100/62, HR decreases to 102, SpO2 improves to 96% — patient appears less confused | State 2A (Partial Improvement — further management needed) |
| 12 minutes elapse without fluid resuscitation initiated | BP drops to 82/48, HR increases to 132, patient becomes minimally responsive (GCS 9) | State 2B (Decompensation) |
| Antibiotics changed without clinical rationale while resuscitation is delayed | Nurse delivers embedded cue: "The blood pressure is still in the 80s — should we be doing something about that?" — remain in State 1; restart trigger clock | State 1 (continue) |

**Debriefing Objective Linked to State 1:**

> Mental model to surface: "The team assumed the antibiotic choice was the primary problem because it was the most recent clinical action — they did not recognize that hemodynamic resuscitation takes precedence over antibiotic optimization in acute sepsis."
>
> Trigger question: "When you first saw Mr. K.T.'s vital signs, what was your initial read on what was most urgent — and what drew your attention there first?"

---

## Verification Checklist
- [ ] Learner level and team composition explicitly specified and scenario complexity calibrated accordingly
- [ ] Learning objectives and debriefing objectives are separate, numbered outputs — not combined or conflated
- [ ] Pre-briefing script includes psychological safety statement, fiction contract, and learning focus framing verbatim
- [ ] At least 3 manikin states specified with full vital signs for each state
- [ ] Most state transitions are action-based; time-only triggers used only as safety-net backstops
- [ ] Confederate role scripts include opening behaviors, cue schedule, and scripted responses to both help requests and information requests
- [ ] Embedded cue library is organized by type and timed — with minute-markers or trigger conditions for each cue
- [ ] Facilitator control guide includes manikin adjustments for every state transition and a contingency protocol
- [ ] Each debriefing objective includes a trigger question that surfaces the mental model without leading
