---
name: deepthink-plan
description: Start a deep, multi-perspective planning session to work through how to get from here to a defined goal. Drives the model through Frame → Decompose into milestones & dependencies → Multi-perspective (BACKBONE.md mandatory roster + scope-specific additions) → Stress-test → Synthesize, using AskUserQuestion at every phase gate. Terminal artifact is a sequenced plan with risks, tripwires, and abort conditions.
version: "1.0.0"
category: deep-analysis
tags: [deep-analysis, planning, strategy, multi-perspective, dependencies, sequencing, gated-workflow]
---

# /deepthink-plan

Run the **deep-think plan / strategy system**: a five-phase, multi-perspective workflow for sequencing the path to an already-chosen goal at a depth that compensates for the absence of a human team.

## When to use

- "How do I get from where we are to where we need to be?"
- "What's the 90-day plan for shipping X?"
- "How do I migrate this codebase / roll out this tool / exit this role?"
- "Sequence the path to launch."

Use when **sequencing execution** is the goal. If the goal hasn't been chosen yet, run `/deepthink-decision` first. If the question is *what* to build (rather than *when* to build it), run `/deepthink-design`.

## How it works

This command inherits shared behavior from [`domain-deep-analysis/BACKBONE.md`](../BACKBONE.md): five gated phases/steps, mandatory perspectives, `AskUserQuestion` with plain-chat fallback, and anti-procrastination checks.

1. **Phase 1 — Frame.** Restate goal as observable end state, separate stated from revealed goal, run capacity reality check, lock scope priorities. Gate: confirm framing and capacity.
2. **Phase 2 — Decompose.** Walk backward from goal + forward from start; produce 4–8 milestones; classify dependencies (hard / soft / external); surface critical path; estimate effort; flag overcommitment. Gate: confirm milestones and capacity.
3. **Phase 3 — Multi-perspective.** Run the mandatory roster and plan-specific additions from `BACKBONE.md`. Gate: pick what to stress-test.
4. **Phase 4 — Stress-test.** Pre-mortem with milestone-level early warnings, cascade failure scan, capacity stress at 30% slippage, define observable abort conditions. Gate: confirm what shapes the plan.
5. **Phase 5 — Synthesize.** Produce sequenced plan with milestones, dependencies, risks, tripwires (course-correct), abort conditions (stop), confidence calibration, re-planning checkpoint. Final gate: what's next.

`AskUserQuestion`/plain-chat gate behavior follows [`BACKBONE.md`](../BACKBONE.md).

## Configuration

### Parameters
- `$ARGUMENTS` — Optional. The goal (one sentence) and any known constraints. If omitted, the command will ask via `AskUserQuestion`.

## Execution

1. **Load the underlying prompt:** Read [`domain-deep-analysis/deepthink_plan.md`](../deepthink_plan.md). Treat its instructions as authoritative.

2. **Collect inputs.** If not in `$ARGUMENTS`, ask via `AskUserQuestion`:
   - The goal (one sentence — must be made observable)
   - The starting state
   - Time horizon and any hard deadlines
   - Resources (people, time-per-week, budget, decision authority)
   - Known constraints
   - What's already been tried (optional)

3. **Reality-check before planning.** If Phase 1 capacity check fails (goal is implausible given resources within timeframe), name it and offer the user the GATE 1 option to cut scope or extend timeframe before proceeding.

4. **Run Phase 1 (Frame).** Output framing + capacity reality check. `AskUserQuestion` for GATE 1. **Stop. Wait.**

5. **Continue phase-by-phase.** Each phase ends with the gate mechanism defined in `BACKBONE.md`. Never run multiple phases in one output.

6. **At the FINAL GATE in Phase 5,** suggest re-running this command after the first major milestone to update the plan with what was learned.

## Success Criteria

- All five phases ran, each with a gate.
- The goal was made observable in Phase 1 (or the system refused to plan toward it).
- Critical path was named in Phase 2.
- Capacity was checked at Phase 1 (rough) and Phase 4 (with 30% slippage).
- Phase 4 produced abort conditions distinct from tripwires (stop vs. course-correct).
- Phase 5 produced concrete milestones (each observable, owned, dated) with named dependencies and contingencies for external dependencies.
- A re-planning checkpoint is named.

## Coordination Notes

- This command is one of four scope-specific deep-think commands. If Phase 1 reveals the user hasn't actually decided on the goal, point them to `/deepthink-decision` before continuing.
- For lighter-weight planning: [`domain-engineering-workflows/workflows/engineering_delivery_sprint_planner.md`](../../domain-engineering-workflows/workflows/engineering_delivery_sprint_planner.md) (sprint scope), [`domain-productivity/deep-work/deepwork_chunk_project_to_calendar.md`](../../domain-productivity/deep-work/deepwork_chunk_project_to_calendar.md) (calendar-fit), [`domain-personal-development/prompts/agency/agency_ship_sprint_design.md`](../../domain-personal-development/prompts/agency/agency_ship_sprint_design.md) (ship-sprint).
- After execution begins, the plan is a hypothesis. Re-run after the first milestone with actuals; the value of the re-plan is the actuals, not the model.
