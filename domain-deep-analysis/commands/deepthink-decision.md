---
name: deepthink-decision
description: Start a deep, multi-perspective analysis of a hard decision. Drives the model through Frame → Decompose options & criteria → Multi-perspective (BACKBONE.md mandatory roster + scope-specific additions) → Stress-test → Synthesize, using AskUserQuestion at every phase gate. Terminal artifact is a recommendation with rationale, calibrated confidence, reversibility, and observable tripwires.
version: "1.0.0"
category: deep-analysis
tags: [deep-analysis, decision-making, multi-perspective, tradeoff-analysis, reversibility, gated-workflow]
---

# /deepthink-decision

Run the **deep-think decision system**: a five-phase, multi-perspective workflow for working through a hard choice at a depth that compensates for the absence of a human team.

## When to use

- "Should I do A or B?"
- "Build vs. buy?"
- "Take the job / leave the job / wait?"
- "Migrate to X now or later?"
- "Confront this issue or let it ride?"

Use when **choosing** is the goal. If the situation is unclear and you need to understand it first, run `/deepthink-problem`. If you've already decided and need to plan execution, run `/deepthink-plan`.

## How it works

This command inherits shared behavior from [`domain-deep-analysis/BACKBONE.md`](../BACKBONE.md): five gated phases/steps, mandatory perspectives, `AskUserQuestion` with plain-chat fallback, and anti-procrastination checks.

1. **Phase 1 — Frame.** Restate the decision, classify reversibility (Type 1 / Type 2), confirm option set, surface forcing function. Gate: confirm framing.
2. **Phase 2 — Decompose.** Surface 4–7 criteria, identify load-bearing ones, score options qualitatively, name the tradeoff sharply. Gate: confirm criteria and tradeoff.
3. **Phase 3 — Multi-perspective.** Run the mandatory roster and decision-specific additions from `BACKBONE.md`. Gate: pick threads to stress-test.
4. **Phase 4 — Stress-test.** Pre-mortem per option, adversarial check, reversibility re-check, define observable tripwires. Gate: pick what shapes the recommendation.
5. **Phase 5 — Synthesize.** Produce recommendation + rationale + reversibility + tripwires + confidence + steel-manned objection. Final gate: what's next.

`AskUserQuestion`/plain-chat gate behavior follows [`BACKBONE.md`](../BACKBONE.md).

## Configuration

### Parameters
- `$ARGUMENTS` — Optional. The decision in one sentence (with options if known). If omitted, the command will ask via `AskUserQuestion`.

## Execution

1. **Load the underlying prompt:** Read [`domain-deep-analysis/deepthink_decision.md`](../deepthink_decision.md). Treat its instructions as authoritative.

2. **Collect inputs.** If not in `$ARGUMENTS`, ask via `AskUserQuestion`:
   - The decision (with at least 2 options; if only 1 option, what does "not doing it" look like)
   - Why now / forcing function
   - Stakes & reversibility (rough)
   - Decision deadline (real or self-imposed)
   - Any current lean (optional)

3. **Right-sizing check.** If Phase 1 reveals a Type 2 (easily reversible) decision with bounded stakes, recommend the smaller reversible test rather than running the full five-phase analysis. Don't run decision theater on a decision that should be acted on.

4. **Run Phase 1 (Frame).** Output framing + reversibility classification. `AskUserQuestion` for GATE 1. **Stop. Wait.**

5. **Continue phase-by-phase.** Each phase ends with the gate mechanism defined in `BACKBONE.md`. Never run multiple phases in one output.

6. **At the FINAL GATE in Phase 5,** offer `/deepthink-plan` if the user accepts the recommendation and wants to schedule execution.

## Success Criteria

- All five phases ran, each with a gate.
- Reversibility was classified in Phase 1 and re-checked in Phase 4.
- Tradeoff was named in one sentence per option (not vague "balanced consideration").
- Tripwires are observable within a defined timeframe — not aspirational.
- Phase 5 takes a position. The user knows what they're being recommended *and* what they're giving up.
- Confidence is calibrated; the user knows what evidence would move it.

## Coordination Notes

- This command is one of four scope-specific deep-think commands. If Phase 1 reveals the user doesn't yet understand the situation well enough to choose, suggest `/deepthink-problem` first.
- For lighter-weight decision support: [`domain-decision-making/decisioning_comprehensive_rapid_tradeoff_analyzer.md`](../../domain-decision-making/decisioning_comprehensive_rapid_tradeoff_analyzer.md) (rapid tradeoff), [`domain-decision-making/decisioning_blind_spot_mirror_see_what_im_missing.md`](../../domain-decision-making/decisioning_blind_spot_mirror_see_what_im_missing.md) (blind-spot only), [`domain-productivity/validation/validation_am_i_being_nuts.md`](../../domain-productivity/validation/validation_am_i_being_nuts.md) (gut check).
- The system can be used to procrastinate. If the user has run the same decision through twice, recommend acting on the smallest reversible test rather than running it a third time.
