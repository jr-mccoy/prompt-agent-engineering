---
name: deepthink-problem-plain
description: A plain-English version of /deepthink-problem, written for non-technical users. Same five-step rigor as the original, with simpler language and friendlier check-ins. Drives the model through Frame → Break Down → Multiple Viewpoints → Stress-Test → Sum Up, using AskUserQuestion at every check-in. Result is an honest diagnosis with places you could push to learn more or change the situation, and how confident the answer is.
version: "1.0.0"
category: deep-analysis
tags: [deep-analysis, problem-framing, multi-perspective, diagnosis, plain-english, non-technical, accessible, gated-workflow]
---

# /deepthink-problem-plain

Run the **plain-English deep-think problem-and-question analysis system**: a five-step, multi-viewpoint workflow for thinking through a hard or fuzzy question one-on-one with an AI, written so anyone — no technical background needed — can follow along.

## When to use

- "Why is this happening?"
- "What's actually going on with this?"
- "Is this real or am I imagining it?"
- "Why does this same thing keep recurring?"

Use when **understanding** is the goal. If the goal is to *choose* between options, run `/deepthink-decision-plain`. If the goal is a *step-by-step plan*, run `/deepthink-plan-plain`. If the goal is to *figure out what to build or set up*, run `/deepthink-design-plain`.

## How it works

This command inherits shared behavior from [`domain-deep-analysis/BACKBONE.md`](../BACKBONE.md): five gated phases/steps, mandatory perspectives, `AskUserQuestion` with plain-chat fallback, and anti-procrastination checks.

1. **Step 1 — Frame.** Restate the question, separate what the user said from what their situation suggests they also want, and run a right-problem check. Check-in: confirm the framing.
2. **Step 2 — Break it down.** Split the question into 3–6 independent pieces; label what's known / unknown / assumed; flag the "everything-rests-on-this" assumptions. Check-in: confirm the breakdown.
3. **Step 3 — Multiple viewpoints.** Run the mandatory roster and scope-specific additions from `BACKBONE.md`. Check-in: pick what to stress-test.
4. **Step 4 — Stress-test.** Pre-mortem failure modes, ripple effects, the strongest challenge, honest confidence ratings. Check-in: pick caveats for the summary.
5. **Step 5 — Sum up.** Produce diagnosis + places to push + foundation assumptions + confidence summary. Final check-in: what's next.

`AskUserQuestion`/plain-chat gate behavior follows [`BACKBONE.md`](../BACKBONE.md).

## Configuration

### Parameters
- `$ARGUMENTS` — Optional. The question or problem in one paragraph. If omitted, the command will ask for it via `AskUserQuestion`.

## Execution

1. **Load the underlying prompt:** Read [`domain-deep-analysis/deepthink_problem_analysis_plain.md`](../deepthink_problem_analysis_plain.md). Treat its instructions as authoritative for this session.

2. **Collect inputs.** If not provided in `$ARGUMENTS`, ask the user via `AskUserQuestion` for:
   - The question or problem (a paragraph in their own words)
   - Why now (one sentence)
   - How much does this matter (low / medium / high)
   - How much time they want to spend (15 min / 1 hour / multi-session)
   - Anything they already think or suspect (optional)

3. **Run Step 1 (Frame).** Output the framing, then call `AskUserQuestion` for the first check-in. **Stop. Wait.**

4. **Continue step-by-step.** Each step ends with the gate mechanism defined in `BACKBONE.md`. Never run multiple steps in a single output.

5. **At the final check-in in Step 5,** offer follow-on commands (`/deepthink-decision-plain`, `/deepthink-plan-plain`, `/deepthink-design-plain`) when relevant.

## Success Criteria

- All five steps ran, each with a check-in.
- The user steered the analysis at every check-in (not just rubber-stamped).
- Each viewpoint produced something specific to the user's question, not generic content.
- The summary is a diagnosis (with places to push + honest confidence ratings), not a recommendation or a plan.
- The final check-in offered the right follow-on if the user wants to turn understanding into action.
- The output used plain language throughout — no unexplained jargon.

## Coordination Notes

- This command is the **plain-English version** of `/deepthink-problem`. Same rigor, different vocabulary. Recommend the rigorous original (`/deepthink-problem`) only when the user is already fluent in business / engineering / analytical vocabulary and prefers the original phrasing.
- This is one of four plain-English deep-think commands. The others: `/deepthink-decision-plain`, `/deepthink-plan-plain`, `/deepthink-design-plain`. If during Step 1 it becomes clear the user wants a decision / plan / design instead, suggest switching commands rather than forcing a problem-analysis frame.
- The system is interactive by design. Do not produce a "complete analysis" in one shot — it defeats the purpose.
