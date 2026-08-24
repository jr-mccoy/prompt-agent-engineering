---
title: PACU Orientation Simulation Calendar Designer
category: pacu/orientation-curriculum
task_type: CREATE
audience: PACU educator scheduling simulation and skill-drill touchpoints across an orientation
updated: "2026-05-15"
tags:
  - pacu
  - orientation
  - simulation
  - skill-drill
  - calendar
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - ED-02
difficulty: intermediate
related_prompts:
  - prompts/pacu_orientation_curriculum_designer.md
  - prompts/pacu_simulation_scenario_builder.md
  - prompts/pacu_simulation_debrief_facilitator.md
  - prompts/pacu_skill_drill_designer.md
  - prompts/pacu_emergency_drill_designer.md
  - prompts/pacu_unfolding_case_study.md
references:
  - ASPAN Standards of Perianesthesia Nursing Practice
  - INACSL Standards of Best Practice Simulation
  - Drain's PeriAnesthesia Nursing Practice (7th ed.)
---

# PACU Orientation Simulation Calendar Designer

> Safety reminder: Simulation supplements, does not replace, bedside teaching. Verify simulation content against facility resources and orientation program before scheduling.

## Objective

Produce a **multi-week simulation and skill-drill calendar** mapping scenario types to orientation weeks. Output names *what* to simulate, *when*, *why* (which competency it targets), and *how long* — so the educator can book simulation lab time and pre-build scenarios using `pacu_simulation_scenario_builder.md`.

## Inputs

- **Orientation length:** {{N weeks}}
- **Orientation pathway theme sequence:** {{from curriculum designer}}
- **Available simulation modalities:** {{full sim lab / part-task trainer / tabletop case / unfolding case discussion only}}
- **Available cadence:** {{e.g., weekly / biweekly / monthly}}
- **Orientee background:** {{drives which scenarios to emphasize}}
- **Facility constraints:** {{e.g., no peds simulator, limited mannequin availability}}

## Audience / Scope

- **Primary:** Unit educator or sim lab coordinator.
- **Secondary:** Primary preceptor (knows when scenarios land relative to bedside curriculum).
- **Scope:** Calendar only. Scenario content is produced by `pacu_simulation_scenario_builder.md`.

## Output requirements

```markdown
# Orientation Simulation Calendar — {N} weeks

> Safety reminder: Simulation calendar is a planning aid. Verify lab availability and facility constraints before booking.

**Cadence:** {weekly / biweekly / monthly / mixed}
**Available modalities:** {modalities}

## Calendar

| Week | Scenario name | Type | Competency target | Modality | Duration | Debrief lead |
|---|---|---|---|---|---|---|
| Wk 2 | Post-extubation airway compromise | emergency drill | airway management | mannequin sim | 30 min sim + 30 min debrief | educator |
| Wk 3 | Post-spinal hypotension cascade | unfolding case | hemodynamics, escalation | tabletop | 45 min | preceptor |
| Wk 4 | PONV with cascading failure | unfolding case | PONV, escalation | tabletop | 45 min | preceptor |
| Wk 5 | Emergence delirium | mannequin sim | emergence, family comms | mannequin | 30 + 30 | educator |
| Wk 6 | Two-bay awareness drill | tabletop dual-patient | judgment in ambiguity | tabletop | 60 min | educator |
| Wk 7 | Code Blue from PACU | emergency drill | crisis resource management | full sim | 45 + 45 | educator + RT |
| Wk 8 | Difficult handoff outbound (ICU receiver) | role-play | handoff communication | role-play | 30 min | preceptor |
| Wk 9 | Mock independent shift | tabletop full-day | integration | tabletop / shadow | 90 min | preceptor |

(Adapt scenario count and types to cadence.)

## Scenario sequencing rationale

3–5 sentences naming why scenarios sequence in this order:
- Single-patient scenarios precede dual-patient (judgment competency depends on individual-case judgment).
- Emergency drills (low-frequency, high-stakes) cluster mid-orientation, when foundational competency is at C — too early is unproductive; too late wastes sign-off prep weeks.
- Communication and handoff scenarios cluster late (after clinical content is consolidated).

## Background-specific adjustments

For experienced ICU RN: code blue scenario can move earlier (basic CRM transfers); emergence delirium and regional block scenarios stay default position.
For new-grad: emergency drill scheduling should not precede Wk 4 cueing-decay milestones; preceptor co-leads early.

## Pre-scenario authoring

For each scenario, the educator runs `pacu_simulation_scenario_builder.md` with the scenario name + competency target ≥ 1 week before the scheduled date.

## Post-scenario flow

Every scenario uses `pacu_simulation_debrief_facilitator.md` for the debrief, and feeds debrief themes into the rolling debrief log (`pacu_preceptor_debrief.md`).

## What this calendar is not

- Not a sign-off rubric (passing the simulation ≠ sign-off).
- Not a substitute for live patient experience.
- Not an HR document.

## Sources / reference

- ASPAN *Standards* — competency expectations.
- INACSL standards — simulation best practice (sequencing, debrief, fidelity).
- *Drain's* — clinical content for scenario authoring (handed to scenario builder).
```

## Must / Must not

**Must:**
- Sequence single-patient scenarios before dual-patient.
- Place emergency drills mid-orientation (not Wk 1, not Wk N).
- Match cadence and modality to user-declared availability.
- Reference `pacu_simulation_scenario_builder.md`, `pacu_simulation_debrief_facilitator.md`, and `pacu_preceptor_debrief.md` for downstream artifacts.
- Adapt scenario emphasis to orientee background.

**Must not:**
- Schedule a code blue or emergency drill in Wk 1.
- Schedule a peds scenario if facility lacks peds simulator (per constraints).
- Project scenario passing as competency sign-off.
- Invent simulation lab availability beyond declared.
- Use protected-characteristic content in scenarios.
- Use license-pathway-based scheduling.

## Quality signals

- An educator can copy the calendar into the unit's resource-booking system as-is.
- Scenario sequencing rationale is concrete enough that a covering educator can defend the schedule.
- A scenario landing in a given week ties cleanly to that week's bedside theme.

## Verification

- [ ] Cadence and modality match input.
- [ ] Emergency drills mid-orientation, not Wk 1 or Wk N.
- [ ] Single-patient before dual-patient.
- [ ] Each scenario has competency target, modality, duration.
- [ ] Sequencing rationale present.
- [ ] Background adjustments named.
- [ ] Safety + FPP sections present.

## False-Positive Prevention

- **No invented sim lab availability** beyond declared.
- **No invented mannequin or part-task trainer brand specifics.**
- **No invented INACSL section numbers.** Cite by theme.
- **No invented facility-specific scenario libraries** ("our unit's standard MH drill").
- **No invented passing thresholds** ("must complete 4/5 scenarios to advance").
- **No protected-characteristic or license-pathway sequencing.**
- **No invented debriefing scripts** beyond the structure in the debrief facilitator prompt.

## Worked Example

<details>
<summary>Example: 10-week orientation, biweekly cadence, full sim lab + tabletop available (click to expand)</summary>

```markdown
| Week | Scenario | Type | Competency | Modality | Duration | Debrief |
|---|---|---|---|---|---|---|
| Wk 2 | Inbound handoff — disorganized CRNA report | role-play | handoff inbound | role-play | 30 min | preceptor |
| Wk 4 | Post-spinal hypotension cascade | unfolding case | hemodynamics, escalation | tabletop | 45 min | preceptor |
| Wk 6 | Emergence delirium (with family in room) | mannequin sim | emergence, family comms | mannequin sim | 30 + 30 | educator |
| Wk 8 | Code Blue from PACU | emergency drill | CRM | full sim | 45 + 45 | educator + RT |
| Wk 10 | Mock independent shift — two bays, mixed | tabletop dual-patient | judgment, integration | tabletop | 90 min | preceptor |

## Sequencing rationale

Single-patient scenarios (Wk 2, 4, 6) precede dual-patient (Wk 10). Emergency drill placed at Wk 8 (mid-late) so foundational competency is at C before crisis content. Communication scenario at Wk 2 sets handoff baseline early; family-communication scenario at Wk 6 follows emergence content. Wk 10 mock shift integrates rather than tests.

## Background-specific adjustments

For experienced ICU RN: Wk 8 code blue could move to Wk 6 (CRM transfers); flagged.
For new-grad: keep Wk 8 placement; do not advance.
```

Notes: cadence honored, drill mid-orientation, dual-patient last, downstream prompts referenced.
</details>

## Self-check

- [ ] Cadence matches input.
- [ ] Drill placement mid-orientation.
- [ ] Single-patient before dual-patient.
- [ ] Downstream prompts referenced.
- [ ] Background adjustments named.
- [ ] FPP section passed.
