---
name: deepthink-decision-plain
description: A plain-English version of /deepthink-decision, written for non-technical users. Same five-step rigor as the original, with simpler language and friendlier check-ins. Drives the model through Frame → Break Down options & criteria → Multiple Viewpoints → Stress-Test → Sum Up, using AskUserQuestion at every check-in. Result is an honest recommendation with reasoning, confidence, how-hard-to-undo, and warning signs.
version: "1.0.0"
category: deep-analysis
tags: [deep-analysis, decision-making, multi-perspective, tradeoff-analysis, plain-english, non-technical, accessible, gated-workflow]
---

# /deepthink-decision-plain

Run the **plain-English deep-think decision system**: a five-step, multi-viewpoint workflow for making a hard choice one-on-one with an AI, written so anyone — no technical background needed — can follow along.

## When to use

- "Should I take this job?"
- "Should we move? Should we hire? Should we buy?"
- "Should I confront this issue now or wait?"
- "Build it ourselves or pay someone?"

Use when **choosing** is the goal. If you don't yet understand the situation well enough to pick, run `/deepthink-problem-plain` first. If you've already chosen and need a plan, run `/deepthink-plan-plain`.

## How it works

This command inherits shared behavior from [`domain-deep-analysis/BACKBONE.md`](../BACKBONE.md): five gated phases/steps, mandatory perspectives, `AskUserQuestion` with plain-chat fallback, and anti-procrastination checks.

1. **Step 1 — Frame.** Restate the decision, separate stated from revealed framing, classify how hard it is to undo, and confirm the option set. Check-in: confirm framing and options.
2. **Step 2 — Break it down.** Surface criteria, identify the make-or-break ones, score each option, mark the everything-rests-on-this assumptions, and state the honest tradeoff in one sentence per option. Check-in: confirm criteria and tradeoff.
3. **Step 3 — Multiple viewpoints.** Run the mandatory roster and scope-specific additions from `BACKBONE.md`. Check-in: pick what to stress-test.
4. **Step 4 — Stress-test.** Pre-mortem failure modes, the strongest challenge, how hard to undo re-checked, specific observable warning signs, honest confidence rating. Check-in: pick caveats for the recommendation.
5. **Step 5 — Sum up.** Produce a real recommendation + reasoning + what you're giving up + how hard to undo + warning signs + confidence. Take a position. Final check-in: what's next.

`AskUserQuestion`/plain-chat gate behavior follows [`BACKBONE.md`](../BACKBONE.md).

## Configuration

### Parameters
- `$ARGUMENTS` — Optional. The decision in one paragraph. If omitted, the command will ask for it via `AskUserQuestion`.

## Execution

1. **Load the underlying prompt:** Read [`domain-deep-analysis/deepthink_decision_plain.md`](../deepthink_decision_plain.md). Treat its instructions as authoritative for this session.

2. **Collect inputs.** If not provided in `$ARGUMENTS`, ask the user via `AskUserQuestion` for:
   - The decision (with at least two options — if only one, ask what "not doing it" looks like)
   - Why now (one sentence)
   - How big a deal it is and roughly how hard to undo (one sentence)
   - When the decision needs to be made by
   - Anything they're already leaning toward (optional)

3. **Run Step 1 (Frame).** Output framing, classify reversibility, then call `AskUserQuestion` for the first check-in. **Stop. Wait.**

4. **Continue step-by-step.** Each step ends with the gate mechanism defined in `BACKBONE.md`. Never run multiple steps in a single output.

5. **At the final check-in in Step 5,** offer the follow-on (`/deepthink-plan-plain`) when relevant.

## Success Criteria

- All five steps ran, each with a check-in.
- The user steered the analysis at every check-in.
- The tradeoff was stated in one sentence per option in Step 2.
- How-hard-to-undo was classified in Step 1 and re-checked in Step 4.
- Warning signs are specific and observable (not vague).
- Step 5 takes a real position — no "well, it depends" hedge unless explicitly justified.
- The output used plain language throughout — no unexplained jargon.

## Coordination Notes

- This command is the **plain-English version** of `/deepthink-decision`. Same rigor, different vocabulary. Recommend the rigorous original (`/deepthink-decision`) only when the user is already fluent in business / engineering / analytical vocabulary and prefers the original phrasing.
- This is one of four plain-English deep-think commands. The others: `/deepthink-problem-plain`, `/deepthink-plan-plain`, `/deepthink-design-plain`. If during Step 1 it becomes clear the user wants problem analysis / a plan / a design instead, suggest switching commands.
- **Special case: easy-to-undo decisions.** If Step 1 reveals the decision is easy to undo and stakes are bounded, don't run the full five steps — recommend the smallest reversible test instead. Running deep analysis on a try-it-and-revise decision is theater.
- The system is interactive by design. Do not produce a "complete analysis" in one shot.
