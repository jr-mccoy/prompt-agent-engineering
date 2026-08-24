---
name: deepthink-design
description: Start a deep, multi-perspective design session to work through what to build (a system, feature, structure, or process). Drives the model through Frame → Decompose into design dimensions → Multi-perspective (BACKBONE.md mandatory roster + scope-specific additions) → Stress-test → Synthesize, using AskUserQuestion at every phase gate. Terminal artifact is a design spec with documented tradeoffs, named load-bearing assumptions, and explicit open questions.
version: "1.0.0"
category: deep-analysis
tags: [deep-analysis, design, architecture, multi-perspective, tradeoff-analysis, specification, gated-workflow]
---

# /deepthink-design

Run the **deep-think design / architecture system**: a five-phase, multi-perspective workflow for designing what to build at a depth that compensates for the absence of a human team.

## When to use

- "Design a system / feature / API / pipeline / structure / process for X."
- "What should the architecture look like?"
- "How should this be shaped?"
- "What's the right way to structure this?"

Use when **what to build** is the question. If the question is whether to build it at all, run `/deepthink-decision`. If you've already designed it and need to schedule the build, run `/deepthink-plan`.

## How it works

This command inherits shared behavior from [`domain-deep-analysis/BACKBONE.md`](../BACKBONE.md): five gated phases/steps, mandatory perspectives, `AskUserQuestion` with plain-chat fallback, and anti-procrastination checks.

1. **Phase 1 — Frame.** Restate what's being designed, separate stated from revealed problem, surface implicit constraints, classify reversibility (Type 1 dimensions get more attention). Gate: confirm framing.
2. **Phase 2 — Decompose.** Surface design dimensions (structural, data, control flow, failure handling, evolution, operational, human). For each, name 2–4 candidates and the tradeoff sharply. Identify load-bearing dimensions. Gate: confirm dimensions and tradeoffs.
3. **Phase 3 — Multi-perspective.** Run the mandatory roster and design-specific additions from `BACKBONE.md`. Gate: pick what to stress-test.
4. **Phase 4 — Stress-test.** Pre-mortem aging modes, cascade analysis, what-changes-easily matrix, dependency stress, confidence calibration on load-bearing dimensions. Gate: confirm what shapes the spec.
5. **Phase 5 — Synthesize.** Produce design spec with positions on each dimension, named tradeoffs accepted, load-bearing assumptions, what-changes-easily matrix, risk register, open questions. Final gate: what's next.

`AskUserQuestion`/plain-chat gate behavior follows [`BACKBONE.md`](../BACKBONE.md).

## Configuration

### Parameters
- `$ARGUMENTS` — Optional. What you're designing (one sentence) and the audience. If omitted, the command will ask via `AskUserQuestion`.

## Execution

1. **Load the underlying prompt:** Read [`domain-deep-analysis/deepthink_design.md`](../deepthink_design.md). Treat its instructions as authoritative.

2. **Collect inputs.** If not in `$ARGUMENTS`, ask via `AskUserQuestion`:
   - What's being designed (one sentence)
   - Who or what it's for
   - Hard requirements (non-negotiable)
   - Soft requirements (negotiable)
   - Known constraints (existing systems, team capabilities, budget)
   - Anything you're already leaning toward (optional)

3. **Surface implicit constraints early.** Phase 1 should specifically ask the user about implicit constraints (scale, latency, team skills, deployment environment, organizational context) — these are the constraints that wreck designs when unnamed.

4. **Run Phase 1 (Frame).** Output framing + reversibility classification. `AskUserQuestion` for GATE 1. **Stop. Wait.**

5. **Continue phase-by-phase.** Each phase ends with the gate mechanism defined in `BACKBONE.md`. Never run multiple phases in one output.

6. **At the FINAL GATE in Phase 5,** suggest `/deepthink-plan` to schedule the build, or recommend a small build experiment if the design has open questions that prototyping would resolve faster than further analysis.

## Success Criteria

- All five phases ran, each with a gate.
- Implicit constraints were surfaced in Phase 1.
- Tradeoffs were named in one sentence per design dimension in Phase 2 — not hidden behind "balanced design" framing.
- Load-bearing vs. revisable dimensions were classified.
- The maintainer-two-years-from-now perspective was run in Phase 3 (always — designs are read more than written).
- Phase 5 takes a position on every load-bearing dimension; open questions are explicit, not buried.
- The what-changes-easily matrix surfaces where the design is brittle.

## Coordination Notes

- This command is one of four scope-specific deep-think commands. If Phase 1 reveals the user hasn't decided whether to build the thing, suggest `/deepthink-decision` first.
- For lighter-weight design support: [`domain-software-engineering/analysis/architecture/architecture_layer_identification.md`](../../domain-software-engineering/analysis/architecture/architecture_layer_identification.md) (existing-architecture analysis), [`domain-prompt-engineering/evaluation/correctness_tradeoff_forcer.md`](../../domain-prompt-engineering/evaluation/correctness_tradeoff_forcer.md) (forcing tradeoff clarity), [`domain-prompt-engineering/goal-orientation/goalorientation_constraint_architecture_workshop.md`](../../domain-prompt-engineering/goal-orientation/goalorientation_constraint_architecture_workshop.md) (workshop constraints).
- The system can be used to procrastinate on building. If the user has run two or more design passes without a prototype, recommend a small build experiment — some flaws only surface in code.
