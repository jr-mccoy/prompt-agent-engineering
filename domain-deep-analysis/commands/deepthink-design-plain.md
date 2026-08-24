---
name: deepthink-design-plain
description: A plain-English version of /deepthink-design, written for non-technical users. Same five-step rigor as the original, with simpler language and friendlier check-ins. Drives the model through Frame → Break Down design choices → Multiple Viewpoints → Stress-Test → Sum Up, using AskUserQuestion at every check-in. Result is a design document with the choices made, the tradeoffs accepted honestly, and the open questions named out loud.
version: "1.0.0"
category: deep-analysis
tags: [deep-analysis, design, architecture, multi-perspective, tradeoff-analysis, plain-english, non-technical, accessible, gated-workflow]
---

# /deepthink-design-plain

Run the **plain-English deep-think design system**: a five-step, multi-viewpoint workflow for designing what to build or set up, one-on-one with an AI, written so anyone — no technical background needed — can follow along.

## When to use

- "Design my morning routine for a busy season."
- "Design our school's parent-teacher communication system."
- "Design the structure of our weekly team meeting."
- "Design a hiring process for our first three roles."
- "Design a personal review cadence — weekly / monthly / quarterly."

Use when **what to build or set up** is the question. If the question is whether to build it at all, run `/deepthink-decision-plain`. If you've already designed it and need to schedule the actual build, run `/deepthink-plan-plain`.

## How it works

This command inherits shared behavior from [`domain-deep-analysis/BACKBONE.md`](../BACKBONE.md): five gated phases/steps, mandatory perspectives, `AskUserQuestion` with plain-chat fallback, and anti-procrastination checks.

1. **Step 1 — Frame.** Restate what's being designed, separate stated from revealed need, surface unspoken constraints, flag what's hard to change later vs. easy. Check-in: confirm framing and constraints.
2. **Step 2 — Break it down.** Identify the design choices to make, surface 2–4 candidate answers per choice, state real tradeoffs in one sentence each, flag the heavy-hitter (hard-to-change) choices, and mark where choices constrain each other. Check-in: confirm choices and tradeoffs.
3. **Step 3 — Multiple viewpoints.** Run the mandatory roster and scope-specific additions from `BACKBONE.md`. Check-in: pick what to stress-test.
4. **Step 4 — Stress-test.** Pre-mortem aging modes, what spreads when something breaks, the strongest challenge, the what-changes-easily-vs-not table, what the design depends on, honest confidence ratings. Check-in: pick what makes it into the design document.
5. **Step 5 — Sum up.** Produce a design document: choices made on each dimension, reasoning, tradeoffs accepted, constraints, assumptions, what changes easily vs. doesn't, risks, and open questions. Final check-in: what's next.

`AskUserQuestion`/plain-chat gate behavior follows [`BACKBONE.md`](../BACKBONE.md).

## Configuration

### Parameters
- `$ARGUMENTS` — Optional. What you're designing, in one paragraph. If omitted, the command will ask for it via `AskUserQuestion`.

## Execution

1. **Load the underlying prompt:** Read [`domain-deep-analysis/deepthink_design_plain.md`](../deepthink_design_plain.md). Treat its instructions as authoritative for this session.

2. **Collect inputs.** If not provided in `$ARGUMENTS`, ask the user via `AskUserQuestion` for:
   - What they're designing (one sentence)
   - Who or what it's for
   - Hard (non-negotiable) requirements
   - Soft (could-trade-off) requirements
   - Constraints they can't change
   - Anything they're already leaning toward (optional)

3. **Run Step 1 (Frame).** Output framing, surface unspoken constraints, flag hard-to-change vs. easy-to-change, then call `AskUserQuestion` for the first check-in. **Stop. Wait.**

4. **Continue step-by-step.** Each step ends with the gate mechanism defined in `BACKBONE.md`. Never run multiple steps in a single output.

5. **At the final check-in in Step 5,** offer the follow-on (`/deepthink-plan-plain`) when relevant.

## Success Criteria

- All five steps ran, each with a check-in.
- The user steered the analysis at every check-in.
- Unspoken constraints were surfaced in Step 1, not just stated ones.
- A real tradeoff was named (one sentence) for every design choice in Step 2.
- Hard-to-change vs. easy-to-change was classified explicitly.
- The Maintainer-in-Two-Years viewpoint was run.
- Step 5 takes a position on every hard-to-change choice and names open questions out loud.
- The design document does not pretend to be a plan or a decision.
- The output used plain language throughout — no unexplained jargon.

## Coordination Notes

- This command is the **plain-English version** of `/deepthink-design`. Same rigor, different vocabulary. Recommend the rigorous original (`/deepthink-design`) only when the user is already fluent in business / engineering / analytical vocabulary and prefers the original phrasing.
- This is one of four plain-English deep-think commands. The others: `/deepthink-problem-plain`, `/deepthink-decision-plain`, `/deepthink-plan-plain`. If during Step 1 it becomes clear the user is asking *whether* to build, not *what* to build, recommend switching to `/deepthink-decision-plain`.
- **Anti-procrastination check:** if the user has run two or more design passes without a small build / trial / prototype attempt, the design phase has become the avoidance. Recommend a small build experiment — some designs only reveal flaws when partly built.
- The system is interactive by design. Do not produce a "complete design" in one shot.
