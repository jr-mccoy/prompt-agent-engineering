---
title: "PACU Shift Structure Card — The Orientee's Default Flow"
category: pacu-learning/stage-1-orientation
journey_stage: 1
benner_stage: "advanced-beginner"
competency_domains:
  - professional-role-leadership
  - safety-escalation
  - assessment-scoring
  - handoff-communication
task_type: "reference-bridge"
audience: "learner"
intended_use: "practice-and-study"
target_users:
  - new-graduate-nurse
  - experienced-nurse-new-to-pacu
techniques: [ST-01, ST-02, DS-06, RT-02, QA-01]
difficulty: beginner
updated: "2026-07-16"
related_prompts:
  - pacu_orient_prioritization_rule_drill.md
  - pacu_orient_inbound_handoff_receiving_rehearsal.md
  - pacu_orient_recovery_one_liner_drill.md
  - pacu_orient_daily_debrief_selfprep.md
see_also_seed:
  - domain-healthcare-clinical/prompts/nursing/nursing_pacu_shift_structure.md
see_also_toolkit:
  - domain-image-generation/healthcare/pacu_orientee_shift_flow_map_meta.md
references:
  - "ASPAN Standards of Perianesthesia Nursing Practice (current edition)"
  - "Drain's PeriAnesthesia Nursing (current edition)"
---

# PACU Shift Structure Card — The Orientee's Default Flow

> **Boundary:** A study-and-rehearsal aid, not live clinical decision support. Your real shift flow follows your preceptor, charge nurse, and facility protocol.

## Objective

Turn the repo's PACU shift-structure card into a flow the learner can **run from memory on day 1** — a default sequence for receiving, recovering, and discharging a patient — so that when the bay gets busy the learner has a scaffold instead of a blank. The learner leaves with a personalized, one-page flow card they keep and refine each shift.

## Your Role

You are adapting an existing anchor artifact (the seed shift-structure card) into *this learner's* words and unit. You do not invent new clinical steps or numbers; you sequence the moves the learner will actually make and mark where each connects to a deeper Stage-1 drill. You keep the flow scope-safe: the nurse receives, assesses, recovers, prepares, assists, and escalates.

## Inputs

- `unit_context` (optional): bay layout, typical surgical mix, staffing pattern.
- `prior_background` (optional): where the learner is coming from (ICU/ED/OR/med-surg/new grad).
- `focus` (default `full-shift`): or a segment (`receiving`, `active-recovery`, `discharge-handoff`).

## Method

1. **Anchor on the seed card.** Restate the standard PACU flow phases in the learner's words: pre-arrival bay prep → receive inbound handoff → initial assessment & first vitals → active recovery loop (assess–act–reassess) → discharge-readiness scoring → outbound report.
2. **For each phase, name the nurse's core move and the cue that ends it.** (e.g., "Initial assessment ends when I have a baseline I can trend against.")
3. **Mark the reassess rhythm.** Active recovery is a loop, not a line — name "reassess at the interval per facility" as the heartbeat of the middle phase.
4. **Wire each phase to its Stage-1 drill** so the card is a table of contents for the learner's practice (handoff-receiving, one-liner, recognition drills, scoring practice, SBAR report).
5. **Flag the two escalation-always moments** in the flow (a deviation on assessment; a stalled discharge score) and route them to role, never to a number or name.
6. **Close with the single highest-yield habit** for a beginner running this flow.

## Output Format

```
PACU SHIFT FLOW — MY DEFAULT CARD
Background: [...]   Focus: [...]

>>> PHASE-BY-PHASE
### [Phase]
My core move: [...]
This phase ends when: [cue]
Reassess rhythm: [per facility, where applicable]
Deepens into (drill): [library filename]
Escalate-always trigger here: [ / — ]  → escalate to [role]

>>> THE MIDDLE-LOOP HEARTBEAT
Assess → act within scope → reassess in the interval per facility → repeat.

>>> HIGHEST-YIELD HABIT
[one sentence]

Phase I'm least sure of right now: [ ]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `focus` | Zoom to one phase for deep rehearsal |
| `prior_background` | Add a "what transfers / what to re-tune" note per phase |
| `depth` | `orientation` (default) vs. `enriched` (adds pre-arrival prep detail) |

## Verification Checklist

- [ ] Flow mirrors the seed shift-structure card; **no new clinical steps or numbers invented**.
- [ ] Every phase names a core move **and** an end-cue.
- [ ] "Reassess in the interval per facility" appears in the active-recovery loop.
- [ ] Each phase links to a Stage-1 drill filename (table-of-contents function).
- [ ] Both escalation-always moments route to a **role**, not a name/number.
- [ ] Scope-safe verbs only (receive/assess/prepare/assist/escalate).

## Worked Example (compact)

**Input:** `focus = receiving`, `prior_background = new grad`.

**Output (excerpt):**
```
### Receive inbound handoff
My core move: listen for the story + confirm the baseline (airway, breathing, circulation, lines, what was given, what to watch).
This phase ends when: I can restate the plan and name the one thing I'm watching most.
Deepens into (drill): pacu_orient_inbound_handoff_receiving_rehearsal.md
Escalate-always trigger here: a handoff gap I can't reconcile → escalate to the anesthesia provider before they leave.
```

> Safety reminder: A rehearsal scaffold only — run your real shift with your preceptor and facility protocol; escalate any real concern by role.
