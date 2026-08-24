---
title: PACU Simulation Debrief Facilitator (PEARLS / 3D Model)
category: pacu/simulation
task_type: LEARN
audience: PACU educator, simulation facilitator, or lead preceptor debriefing a PACU sim
updated: "2026-04-16"
tags:
  - pacu
  - simulation
  - debrief
  - pearls
  - psychological-safety
techniques:
  - ST-01
  - ST-02
  - RT-02
  - ED-02
  - DS-06
difficulty: advanced
related_prompts:
  - prompts/pacu_simulation_scenario_builder.md
  - prompts/pacu_unfolding_case_study.md
  - prompts/pacu_emergency_drill_designer.md
  - prompts/pacu_preceptor_debrief.md
  - prompts/pacu_preceptor_approach_guide.md
references:
  - ASPAN Standards of Perianesthesia Nursing Practice
  - INACSL Healthcare Simulation Standards of Best Practice (Debriefing)
  - PEARLS (Promoting Excellence and Reflective Learning in Simulation) debriefing framework
  - Advocacy-Inquiry (Rudolph et al., Harvard Center for Medical Simulation)
---

# PACU Simulation Debrief Facilitator

> Safety reminder: Debrief structure only. The debrief is a learning conversation, not a competency sign-off. Formal competency decisions happen through facility orientation documentation, not in a debrief.

## Objective

Produce a **structured PACU simulation debrief plan** using PEARLS (or 3D: Defusing → Discovering → Deepening) with explicit psychological-safety guardrails, advocacy-inquiry stems, learning-objective alignment, and closing commitments. Output is the facilitator's running script for the 20–30 minute debrief that follows a sim run (scenario, drill, or unfolding case).

## When to use

- After any PACU simulation (mannequin, SP, in situ, drill).
- After an unfolding case study used in a group teaching block.
- After a real-shift event where the team has agreed to debrief as a learning exercise (not as root-cause analysis — use a separate facility process for that).

## When not to use

- For end-of-shift bedside debriefs — use `pacu_preceptor_debrief.md`.
- For a formal evaluation conversation — use `pacu_preceptor_writing_orientee_evaluation.md` preceded by `pacu_preceptor_approach_guide.md`.
- For a root-cause analysis on a real patient-safety event — those run through the facility's formal process.

## Inputs

- **Simulation artifact:** the `pacu_simulation_scenario_builder.md` output, `pacu_unfolding_case_study.md` output, OR the `pacu_emergency_drill_designer.md` drill that just ran.
- **Learning objectives of the sim:** 2–3, carried from the scenario.
- **Runtime available for debrief:** {{15 / 20 / 30 minutes}}
- **Participants and roles:** primary learner(s), observer(s), SPs, secondary preceptors.
- **What actually happened** (facilitator's observations): 3–5 specific moments worth naming.
- **Debrief framework preference:** {{PEARLS (default) | 3D Model | GAS (Gather-Analyze-Summarize)}}

## Audience / Scope

- **Primary user:** Debrief facilitator.
- **Participants:** Sim learners (primarily Phase 1 PACU orientees), observer-preceptors.
- **Scope:** PACU Phase 1 simulation debriefs. Not for patient-safety event analysis.

## Output requirements

```markdown
# PACU Simulation Debrief Plan — {Scenario title} — {Date}

> Safety reminder: Learning conversation, not competency sign-off. Psychological safety governs. Facility orientation documentation is separate.

## Pre-Debrief Setup (facilitator, 2 min)
- Confirm private space; water available; seating in a rough circle (not a classroom row).
- State the basic assumption aloud: "We assume everyone in this room was doing their best with the information they had, working toward improvement."
- Affirm confidentiality: "What's said here stays here. We debrief behavior, not people."
- Name the learning objectives (2–3) carried from the sim.

## Phase 1 — Reactions / Defusing (3–5 min)
Opening stem options:
- "How are you feeling right now, after the sim?"
- "Before we talk about what happened — one word to describe where you are right now."
- "Anything you need to get off your chest before we get into it?"

Facilitator notes:
- Listen; do not interpret or redirect yet.
- If a learner names distress — pause, validate, offer a short break if needed.
- The goal is to clear emotional noise so learners can think, not to suppress it.

## Phase 2 — Description / Gathering (3–5 min)
Opening stem options:
- "Walk me through what happened from your point of view, from the moment the patient arrived."
- "In your own words, what was the scenario about?"
- {Observer prompt, if present:} "What did you see from the observer role?"

Facilitator notes:
- Let learners narrate. Correct factual misstatements briefly; save analysis for next phase.
- Listen for the cue points where reasoning branched.

## Phase 3 — Analysis / Discovering + Deepening (10–15 min)
Core technique: **Advocacy-Inquiry** (Rudolph). Structure:
> "I observed {specific behavior}. I'm wondering what was going on for you at that moment? [advocacy + inquiry]"

Three to five advocacy-inquiry probes, tied to the learning objectives. Use the seeded debrief questions from `pacu_simulation_scenario_builder.md`.

Example stems:
- "At T+2, I noticed you completed the checklist before naming the BP trend. Help me understand what was going through your head at that moment."
- "When the spouse interrupted at T+6, I saw you pause for about 20 seconds before coming back to the patient. What were you weighing?"
- "At T+8, the escalation to CRNA included three of the four SBAR pieces. Walk me through the R — what was the ask?"

Facilitator notes:
- Inquire first, teach second. Do not start with the correct answer.
- Name the cognitive frame the learner was operating in, then test it.
- Anchor to the sign-off scale tokens (Independent / With Cues / With Direction / Not Yet) only if the learner asks — debrief is for learning, not rating.

## Phase 4 — Application / Summarizing (5 min)
Closing stems:
- "What's one thing you'll try differently on your next PACU admission with a trend?"
- "What's one thing from this sim you want to keep doing?"
- "What's one question you're leaving with that you want your preceptor to help you with?"

Facilitator notes:
- Each learner commits to one concrete next action.
- Capture commitments in writing (hand to primary preceptor for rolling evidence log if appropriate).
- Close by restating the learning objectives and how the sim mapped to them.

## Psychological-Safety Guardrails (facilitator reminders throughout)
- Behavior, not people.
- Basic assumption ("doing their best") stays active — re-invoke if tone drifts.
- No ranking learners against each other ("you did this better than X").
- No ambush feedback from observers — observer input is invited, not unleashed.
- If a learner becomes distressed, pause; offer break; do not resume until they're ready.
- Facilitator owns the tone — if the room goes punitive, the facilitator resets.
- If a learner's error was rooted in a systems issue (equipment, protocol gap, pre-brief miss), name the systems issue.

## Red-Flag Interventions (when to pivot)
| Pattern | What to say |
|---|---|
| Learner is spiraling into self-blame | "Let's pause. I want to hear the frame you were working in at that moment, not the judgment you have now." |
| Observer delivers pile-on feedback | "I want to redirect — your observation is helpful. Let's anchor it to a behavior at a specific time point." |
| Debrief becomes a quiz ("what should you have done?") | "We're not quizzing. I'm asking what was going on for you. Teaching comes after inquiry." |
| A learner demands to know their "grade" | "This is a learning debrief, not a sign-off. Your preceptor will review competency separately. What do you want to try next time?" |
| Silence past 30 seconds after a prompt | "Take your time. I'll wait." |
| Debrief surfaces a real patient-safety concern from a recent shift | "I want to note that. Let's finish the sim debrief, and then I'll connect you to the facility's event-reporting process separately." |

## Sources / reference
- INACSL Healthcare Simulation Standards of Best Practice — Debriefing.
- PEARLS debriefing framework (Eppich & Cheng, 2015).
- Advocacy-Inquiry (Rudolph et al., Harvard Center for Medical Simulation).
- ASPAN *Standards of Perianesthesia Nursing Practice* — education and competency.
```

## Must / Must not

**Must:**
- Open with explicit psychological-safety framing and the basic assumption.
- Use a recognized debrief framework (PEARLS / 3D / GAS) — do not freelance.
- Anchor analysis phase to advocacy-inquiry: observe, then inquire before teaching.
- Let learners narrate first (description phase) before the facilitator analyzes.
- Close with a concrete commitment per learner.
- Intervene on psychological-safety violations in real time (pile-on, ranking, ambush).

**Must not:**
- Use the debrief as a covert competency evaluation — rating decisions live in separate preceptor prompts, not here.
- Allow ranking of learners against one another.
- Allow observers to deliver pile-on feedback; redirect to behavior + time-anchor.
- Identify patients by MRN, full name, full DOB, or room number in debrief discussion.
- Reference age, race, sex, disability, religion, national origin, pregnancy, license pathway, or prior unit as analysis variables unless the sim was specifically about population-specific practice (in which case frame clinically, not as a performance signal).
- Surface a real patient-safety concern and quietly let it pass — redirect to facility event-reporting.
- Invent facility-specific policies, event-reporting channels, or EAP pathways. Use "per facility protocol" / "by role."
- Substitute for root-cause analysis on a real event.

## Quality signals

- Learners leave able to name one behavior they'll try next shift.
- Every advocacy-inquiry probe connected to a time-stamped moment in the sim.
- Psychological-safety guardrails held throughout (no ranking, no pile-on, no ambush).
- Systems issues (when present) were named, not hidden.
- The facilitator taught less than half the time; inquiry led teaching.

## Verification

Before leading the debrief, verify the plan includes:

- [ ] Pre-debrief setup with basic assumption, confidentiality, and learning objectives.
- [ ] All four PEARLS phases (Reactions → Description → Analysis → Application), each time-boxed.
- [ ] ≥ 3 advocacy-inquiry probes tied to specific time points from the scenario.
- [ ] Psychological-safety guardrail reminders interspersed.
- [ ] Red-flag interventions cheat sheet with verbatim stems.
- [ ] Closing commitment per learner.

After the debrief:

- [ ] Every learner named one concrete next action.
- [ ] No ranking, pile-on, or ambush occurred.
- [ ] Any real patient-safety concern that surfaced was routed to facility event-reporting separately.

## False-Positive Prevention

Do **not** fabricate:

- **No invented rater-level judgments.** The debrief is not for competency sign-off.
- **No invented learner observations.** If a behavior wasn't witnessed, do not construct one to probe.
- **No invented INACSL / PEARLS section numbers.** Mark `{{confirm}}` when unknown.
- **No invented facility psychological-safety policies or event-reporting channels.**
- **No personality labels** ("you were too quiet," "you panicked"). Translate to behavior + time anchor.
- **No speculation about medical, mental-health, or family circumstances** that may have affected performance. EAP by role only; do not document.
- **No references to age, race, sex, disability, religion, national origin, pregnancy, license pathway, or prior unit as causal analysis.**
- **No patient-identifying information** when the debrief references a sim scenario based on a real case.

## Worked Example

<details>
<summary>Example: Advocacy-inquiry probe + redirect for a post-spinal-hypotension sim (click to expand)</summary>

```markdown
## Phase 3 — Analysis / Discovering + Deepening (excerpt)

**Advocacy-Inquiry probe 1:**
> "I observed that at T+2, you completed the lines + Foley check before verbalizing the BP trend. I'm wondering what was going on for you at that moment — were you working through the checklist, or weighing something else?"

Learner response: "I think I was on autopilot. I wanted to make sure I didn't miss anything on the checklist, so I just kept going."

**Facilitator follow-up (deepen the frame):**
> "That's helpful. So the frame was 'don't miss a checklist item,' which is a good instinct early in orientation. I want to name the tension: when a vital trends, the frame has to switch from 'complete the checklist' to 'what is the trend telling me?' What cue do you think would have triggered that switch for you?"

**Redirect (observer delivers pile-on):**
Observer: "She should have called the CRNA at T+2, not T+5. That was late."
Facilitator: "I want to redirect. Your observation about the timing is helpful. Let's anchor it: at T+2, what was the cue strength — subtle trend or overt drop? And for the learner — what would have made you call at T+2?"

Notes: advocacy-inquiry opens the frame before teaching; redirect moves pile-on toward time-anchored behavior; facilitator names the tension ("complete the checklist" vs. "trend-recognition") without labeling the learner.
```
</details>

## Self-check

- [ ] Pre-debrief setup, four PEARLS phases, psychological-safety guardrails, and red-flag interventions are all present.
- [ ] ≥ 3 advocacy-inquiry probes with time anchors.
- [ ] Closing commitment per learner.
- [ ] No ranking, no pile-on, no personality labels.
- [ ] No patient-identifying information.
- [ ] No protected-characteristic references used as causal analysis.
- [ ] Safety reminder at top.
- [ ] Verification section passed.
- [ ] False-Positive Prevention section passed.
