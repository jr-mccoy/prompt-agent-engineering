---
name: deepthink-plan-plain
description: A plain-English version of /deepthink-plan, written for non-technical users. Same five-step rigor as the original, with simpler language and friendlier check-ins. Drives the model through Frame → Break Down milestones & dependencies → Multiple Viewpoints → Stress-Test → Sum Up, using AskUserQuestion at every check-in. Result is a sequenced plan with named risks, warning signs, and clear stop-the-whole-thing conditions.
version: "1.0.0"
category: deep-analysis
tags: [deep-analysis, planning, strategy, multi-perspective, plain-english, non-technical, accessible, gated-workflow]
---

# /deepthink-plan-plain

Run the **plain-English deep-think planning system**: a five-step, multi-viewpoint workflow for mapping out how to get from where you are to where you want to go, one-on-one with an AI, written so anyone — no technical background needed — can follow along.

## When to use

- "How do I leave this job over six months?"
- "What's my plan to launch this side business?"
- "How do we get this renovation / move / rollout done by [date]?"
- "How do I get back on track with my health / habits / studies?"

Use when **sequencing the path** is the goal. If the goal hasn't been chosen yet, run `/deepthink-decision-plain` first. If the question is "what should we build or set up?", run `/deepthink-design-plain`.

## How it works

This command inherits shared behavior from [`domain-deep-analysis/BACKBONE.md`](../BACKBONE.md): five gated phases/steps, mandatory perspectives, `AskUserQuestion` with plain-chat fallback, and anti-procrastination checks.

1. **Step 1 — Frame.** Restate the goal as something observable, separate stated from revealed goal, reality-check capacity, and lock down required vs. nice-to-have. Check-in: confirm framing and realistic capacity.
2. **Step 2 — Break it down.** Map milestones (working both forwards and backwards), label dependencies (hard / soft / outside-your-control), name the must-finish-first chain, flag everything-rests-on-this assumptions, and check capacity. Check-in: confirm milestones and dependencies.
3. **Step 3 — Multiple viewpoints.** Run the mandatory roster and scope-specific additions from `BACKBONE.md`. Check-in: pick what to stress-test.
4. **Step 4 — Stress-test.** Pre-mortem failure modes, what slips if anything slips, the strongest challenge, capacity re-check at 30%-slower-than-expected, stop-the-whole-thing conditions, honest confidence ratings. Check-in: pick what makes it into the plan.
5. **Step 5 — Sum up.** Produce a sequenced plan with milestones, owners, dates, dependencies, risks, warning signs, stop-the-whole-thing conditions, capacity + confidence, and a re-planning checkpoint. Final check-in: what's next.

`AskUserQuestion`/plain-chat gate behavior follows [`BACKBONE.md`](../BACKBONE.md).

## Configuration

### Parameters
- `$ARGUMENTS` — Optional. The goal in one paragraph. If omitted, the command will ask for it via `AskUserQuestion`.

## Execution

1. **Load the underlying prompt:** Read [`domain-deep-analysis/deepthink_plan_plain.md`](../deepthink_plan_plain.md). Treat its instructions as authoritative for this session.

2. **Collect inputs.** If not provided in `$ARGUMENTS`, ask the user via `AskUserQuestion` for:
   - The goal (one sentence — observable end state)
   - Where things are now
   - Time horizon and any hard deadlines
   - Resources (people, time-per-week, budget, decision authority — roughly)
   - Non-negotiable constraints
   - What's already been tried (optional)

3. **Run Step 1 (Frame).** Output framing, run the rough capacity check, then call `AskUserQuestion` for the first check-in. **Stop. Wait.**

4. **Continue step-by-step.** Each step ends with the gate mechanism defined in `BACKBONE.md`. Never run multiple steps in a single output.

5. **At the final check-in in Step 5,** offer follow-ons (convert to a task tracker; re-run after the first milestone) as relevant.

## Success Criteria

- All five steps ran, each with a check-in.
- The user steered the analysis at every check-in.
- The goal was made observable in Step 1.
- The must-finish-first chain was named explicitly.
- Capacity was reality-checked twice: rough in Step 1, harder (30%-slower) in Step 4.
- Course-correct warning signs and stop-the-whole-thing conditions are both present and clearly distinguished.
- A re-planning checkpoint is named.
- Outside-your-control dependencies have backup plans.
- The output used plain language throughout — no unexplained jargon.

## Coordination Notes

- This command is the **plain-English version** of `/deepthink-plan`. Same rigor, different vocabulary. Recommend the rigorous original (`/deepthink-plan`) only when the user is already fluent in business / engineering / analytical vocabulary and prefers the original phrasing.
- This is one of four plain-English deep-think commands. The others: `/deepthink-problem-plain`, `/deepthink-decision-plain`, `/deepthink-design-plain`. If during Step 1 it becomes clear the user hasn't actually chosen the goal, recommend switching to `/deepthink-decision-plain` first — planning toward an undecided goal is wasted output.
- The system is interactive by design. Do not produce a "complete plan" in one shot.
