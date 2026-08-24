---
title: "ACT Group Protocol (Hexaflex-Sequenced)"
category: psychology/modalities/act
description: "Design a multi-session group-delivered ACT protocol sequenced across the hexaflex (acceptance, defusion, present-moment contact, self-as-context, values, committed action) plus creative hopelessness/workability, with experiential exercises and metaphors per process, group facilitation, homework, and a psychological-flexibility measurement plan."
techniques:
  - ST-04
  - RT-02
  - DT-02
  - ED-04
  - QA-04
  - CM-02
difficulty: intermediate
tags:
  - ACT
  - hexaflex
  - psychological-flexibility
  - group-therapy
  - defusion
  - values
  - committed-action
  - Hayes
  - AAQ-II
intended_use: model-testing
updated: "2026-06-08"
related_prompts:
  - domain-psychology/modalities/act/psychology_act_matrix_session_facilitator.md
  - domain-psychology/modalities/act/psychology_act_values_card_sort.md
  - domain-psychology/modalities/group/psychology_group_therapy_curriculum_builder.md
  - domain-psychology/populations/cross-population/psychology_group_therapy_member_screening.md
---

# ACT Group Protocol (Hexaflex-Sequenced)

## Objective

Design a multi-session, **group-delivered Acceptance and Commitment Therapy (ACT; Hayes, Strosahl, Wilson)** protocol sequenced across the **six core processes of the hexaflex** — acceptance, cognitive defusion, present-moment contact, self-as-context, values, and committed action — with **creative hopelessness / workability** as the early entry point. Each session targets a process (or pairing) with experiential exercises and metaphors, group-specific facilitation, between-session homework, and a psychological-flexibility measurement plan. This **adds a group format** to the existing individual ACT resources in this directory. Output is a session-by-session hexaflex map, a group willingness/values bridge, and a measurement plan.

## When to Use

- Standing up a closed (or cohort-based) ACT group for depression, anxiety, chronic pain, stress, substance use, or transdiagnostic distress.
- Translating individual ACT into a multi-session group arc where experiential exercises run in dyads and full-group sharing.
- When psychological inflexibility (experiential avoidance, fusion, values-disconnection) is the shared mechanism across members.
- Programs (IOP/PHP, community mental health, primary-care behavioral health) wanting a structured, replicable ACT curriculum.
- Not for acute crisis stabilization as the primary intervention, and not a substitute for pre-group screening (use the member-screening prompt) or clinician judgment about member fit and risk. Not a substitute for individualized case formulation where a member needs it.

## Inputs / Context

- Group purpose, target population, severity/acuity, and setting.
- Number of sessions, session length, open vs closed, and co-facilitation availability.
- Members' shared presenting concerns and any process most central (e.g., heavy fusion, strong avoidance).
- Prior ACT exposure of members and facilitators; cultural/language and developmental considerations.
- Screening status and exclusion/risk flags from the member-screening prompt.
- `[clinician input required: pre-group screening outcomes, risk/exclusion flags, and any program-mandated session count]`

## Constraints

### Must

- Sequence the curriculum across the **six hexaflex processes** and name each session's target process: **acceptance, defusion, present-moment contact (mindfulness), self-as-context (the observer self), values, committed action**.
- Begin with **creative hopelessness / workability**: surface the unworkability of the control-and-avoidance agenda before introducing acceptance/defusion (don't lead with technique).
- Pair each process with at least one **experiential exercise** and/or **metaphor**, drawn from the established ACT repertoire and named accurately, e.g.:
  - Defusion → **Leaves on a Stream**, **Passengers on the Bus**, "I'm having the thought that…", milk-milk-milk repetition.
  - Acceptance/willingness → **Tug-of-War with the Monster**, the **Quicksand** metaphor, physicalizing the feeling.
  - Present-moment → mindful breathing / grounding / noticing.
  - Self-as-context → the **Observer exercise**, **Chessboard** metaphor, "noticing self."
  - Values → values clarification, sweet-spot / values card work, the funeral/80th-birthday exercise.
  - Committed action → SMART values-linked goals, willingness-and-action.
- Build in **group-specific facilitation**: experiential exercises run **in dyads**, then **full-group sharing**; in-vivo willingness practice; and a **willingness/values bridge** that links each member's avoided experience to a valued direction and a committed action.
- Assign **between-session homework** tied to each session's process (practice logs, defusion practice, values-based action).
- Include a **psychological-flexibility measurement plan** — name the **AAQ-II** (Acceptance and Action Questionnaire-II) and optionally CompACT/process measures **by name only**, with cadence (pre/mid/post) and what is tracked.
- Provide **facilitation guidance** for the monopolizer, the silent member, and over-intellectualizing (a common ACT-group pull) and specify **co-facilitation roles**.
- Reference the individual ACT matrix and values resources for cross-format consistency.

### Must Not

- Do not lead with defusion/acceptance technique before establishing workability/creative hopelessness.
- Do not present ACT as thought-elimination or feeling-control; the aim is willingness and values-consistent action, not symptom reduction per se.
- Do not impose the facilitator's values into members' values work.
- Do not misattribute or invent metaphors/exercises; use named ACT exercises accurately or mark `[clinician input required: ...]`.
- Do not fabricate measure cutoffs, normed AAQ-II thresholds, or program session counts; mark program-specific figures as `[clinician input required: ...]`.
- Do not skip screening/risk linkage or admit acutely unstable members as a substitute for stabilization.

## Instructions

1. Clarify group purpose, population, session count/length, open vs closed, and co-facilitation; confirm screening status.
2. Lay out the hexaflex sequence as a session arc, opening with creative hopelessness/workability.
3. For each session, assign the target process, an experiential exercise/metaphor (named), the in-session group activity (dyad → share), and homework.
4. Build the willingness/values bridge: connect each process to members' avoided experiences and valued directions, culminating in committed action.
5. Add the standard session structure (mindfulness opener → process content → experiential exercise in dyads → full-group sharing → home practice).
6. Specify facilitation responses for the monopolizer, silent member, and over-intellectualizing; define co-facilitation roles.
7. Define the measurement plan (AAQ-II by name, cadence, targets).
8. Note adaptations (telehealth, culture/language, developmental level) and cross-reference the individual ACT matrix/values prompts.
9. Run verification.

## Output Format

```
=== ACT GROUP PROTOCOL (HEXAFLEX-SEQUENCED) — DESIGN RECORD ===
Group name: [...]   Date: [YYYY-MM-DD]   Designer: [...]
Population: [...]   Sessions: [N x length]   Format: [Open / Closed]   Setting: [...]
Co-facilitation roles: [Lead / Co / observer]
Screening status: [clinician input required]

─────────────────────────────────────────
SESSION-BY-SESSION HEXAFLEX MAP
─────────────────────────────────────────
Session # | Target process                 | Exercise / Metaphor (named)        | Group activity (dyad → share) | Home practice
----------+--------------------------------+------------------------------------+-------------------------------+--------------
1         | Creative hopelessness/workability | [e.g., Tug-of-War / control agenda] | [...]                         | [workability log]
2         | Acceptance / willingness        | [e.g., Quicksand; physicalize]     | [...]                         | [willingness practice]
3         | Defusion                        | [Leaves on a Stream / Passengers]  | [...]                         | [defusion log]
4         | Present-moment contact          | [mindful grounding/noticing]       | [...]                         | [daily noticing]
5         | Self-as-context                 | [Observer exercise / Chessboard]   | [...]                         | [observer practice]
6         | Values                          | [values card / funeral exercise]   | [...]                         | [values write-up]
7         | Committed action                | [values-linked SMART action]       | [...]                         | [committed action + tracking]
8 (+)     | Integration / maintenance       | [review + relapse-/lapse-plan]     | [...]                         | [ongoing willingness plan]

STANDARD SESSION STRUCTURE
Mindfulness opener [N min] → Process content [N min] → Experiential exercise in DYADS [N min] → Full-group sharing [N min] → Home practice assignment

─────────────────────────────────────────
GROUP WILLINGNESS / VALUES BRIDGE
─────────────────────────────────────────
For each member (or composite):
  Avoided/feared experience: [...]
  Control/avoidance move (unworkable): [...]
  Valued direction: [...]
  Willingness practiced in group (in vivo): [...]
  Committed action: [specific, values-linked]

─────────────────────────────────────────
FACILITATION PLAYBOOK
─────────────────────────────────────────
- Monopolizer: [...]
- Silent member: [...]
- Over-intellectualizing / "figuring it out": [redirect to experiential/present moment]
- Co-facilitation roles: [...]

─────────────────────────────────────────
MEASUREMENT PLAN (psychological flexibility)
─────────────────────────────────────────
Primary measure (by name): AAQ-II (Acceptance and Action Questionnaire-II)
Optional process measures (by name): [CompACT / VLQ / others]
Cadence: [Pre / Mid / Post / per-session brief]
What is tracked: [experiential avoidance, valued-living, committed action]
Thresholds/cutoffs: [clinician input required]

─────────────────────────────────────────
NOTES / ADAPTATIONS
─────────────────────────────────────────
- Telehealth / culture-language / developmental: [...]
- Cross-format consistency: see psychology_act_matrix_session_facilitator.md, psychology_act_values_card_sort.md
- Open question for clinician: [clinician input required]
```

## Verification

- [ ] Curriculum sequenced across all six hexaflex processes, each session's target process named.
- [ ] Creative hopelessness / workability opens the arc before defusion/acceptance technique.
- [ ] Each process paired with a named, accurately attributed ACT exercise/metaphor.
- [ ] Experiential exercises structured as dyads → full-group sharing with in-vivo willingness.
- [ ] Willingness/values bridge links avoided experience → valued direction → committed action.
- [ ] Homework assigned per session and tied to its process.
- [ ] ACT framed as willingness + values-consistent action, not thought/feeling elimination.
- [ ] Facilitation playbook covers monopolizer, silent member, over-intellectualizing; co-facilitation roles defined.
- [ ] Measurement plan names AAQ-II with cadence and tracked targets.
- [ ] Screening/risk linkage preserved; program-specific counts/cutoffs marked `[clinician input required: ...]`.
- [ ] No misattributed/invented metaphors and no fabricated measure thresholds or session counts.
```
