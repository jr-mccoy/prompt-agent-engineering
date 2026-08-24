---
name: deepthink-problem
description: Start a deep, multi-perspective analysis of a problem or open-ended question. Drives the model through Frame → Decompose → Multi-perspective (BACKBONE.md mandatory roster + scope-specific additions) → Stress-test → Synthesize, using AskUserQuestion at every phase gate. Terminal artifact is a diagnosis with leverage points and calibrated confidence — not a recommendation, not a plan.
version: "1.0.0"
category: deep-analysis
tags: [deep-analysis, problem-framing, multi-perspective, diagnosis, critical-thinking, gated-workflow]
---

# /deepthink-problem

Run the **deep-think problem & question analysis system**: a five-phase, multi-perspective workflow designed to think through a hard or fuzzy question at a depth that compensates for the absence of a human team.

## When to use

- "Why is X happening?"
- "What's actually going on with Y?"
- "Is this real or am I imagining it?"
- "Why is this so hard?" / "Why does this keep recurring?"

Use when **understanding** is the goal. If the goal is to *choose*, run `/deepthink-decision`. If the goal is a *plan*, run `/deepthink-plan`. If the goal is a *spec*, run `/deepthink-design`.

## How it works

This command inherits shared behavior from [`domain-deep-analysis/BACKBONE.md`](../BACKBONE.md): five gated phases/steps, mandatory perspectives, `AskUserQuestion` with plain-chat fallback, and anti-procrastination checks.

1. **Phase 1 — Frame.** Restate the question, separate stated from revealed framing, run a right-problem check. Gate: confirm framing.
2. **Phase 2 — Decompose.** Break into 3–6 orthogonal axes; label what's known/unknown/assumed; flag load-bearing assumptions. Gate: confirm decomposition.
3. **Phase 3 — Multi-perspective.** Run the mandatory roster and scope-specific additions from `BACKBONE.md`. Gate: pick threads to stress-test.
4. **Phase 4 — Stress-test.** Pre-mortem failure modes, cascade effects, adversarial check, confidence calibration. Gate: pick caveats for synthesis.
5. **Phase 5 — Synthesize.** Produce diagnosis + leverage points + load-bearing assumptions + confidence summary. Final gate: what's next.

`AskUserQuestion`/plain-chat gate behavior follows [`BACKBONE.md`](../BACKBONE.md).

## Configuration

### Parameters
- `$ARGUMENTS` — Optional. The question or problem in one paragraph. If omitted, the command will ask for it via `AskUserQuestion`.

## Execution

1. **Load the underlying prompt:** Read [`domain-deep-analysis/deepthink_problem_analysis.md`](../deepthink_problem_analysis.md). Treat its instructions as authoritative for this session.

2. **Collect inputs.** If not provided in `$ARGUMENTS`, ask the user via `AskUserQuestion` for:
   - The question / problem (paragraph)
   - Why now (one sentence)
   - Stakes (low / medium / high)
   - Time available for analysis (15 min / 1 hour / multi-session)
   - Anything they're already concluding or suspecting (optional)

3. **Run Phase 1 (Frame).** Output framing, then call `AskUserQuestion` for GATE 1. **Stop. Wait.**

4. **Continue phase-by-phase.** Each phase ends with the gate mechanism defined in `BACKBONE.md`. Never run multiple phases in a single output.

5. **At the FINAL GATE in Phase 5,** offer follow-on commands (`/deepthink-decision`, `/deepthink-plan`, `/deepthink-design`) when relevant.

## Success Criteria

- All five phases ran, each with a gate.
- The user steered the analysis at every gate (not just rubber-stamped).
- Each perspective produced a take specific to the user's question, not generic content.
- The synthesis is a diagnosis (with leverage points + confidence calibration), not a recommendation or a plan.
- The final gate offered the right follow-on if the user wants to convert understanding into action.

## Coordination Notes

- This command is one of four scope-specific deep-think commands. The others: `/deepthink-decision`, `/deepthink-plan`, `/deepthink-design`. If during Phase 1 it becomes clear the user wants a decision / plan / spec, suggest switching commands rather than forcing a problem-analysis frame.
- The system is interactive by design. Do not produce a "complete analysis" in one shot — it defeats the purpose.
- For shorter / faster diagnostic work that doesn't warrant the full five-phase pass, point users to standalone prompts: [`domain-prompt-engineering/goal-orientation/goalorientation_right_problem_diagnostic.md`](../../domain-prompt-engineering/goal-orientation/goalorientation_right_problem_diagnostic.md), [`domain-decision-making/decisioning_blind_spot_mirror_see_what_im_missing.md`](../../domain-decision-making/decisioning_blind_spot_mirror_see_what_im_missing.md), [`domain-productivity/validation/validation_adversarial_mini_check.md`](../../domain-productivity/validation/validation_adversarial_mini_check.md).
