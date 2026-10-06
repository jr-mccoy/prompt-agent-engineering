---
name: deepthink-evaluation-plain
description: Start a plain-English, deep, multi-perspective evaluation of an existing artifact, proposal, plan, design, document, or output. Drives the model through Frame → Decompose criteria & evidence → Multi-perspective (BACKBONE.md mandatory roster + scope-specific additions) → Stress-test → Synthesize, using AskUserQuestion at every phase gate. Terminal artifact is an evaluation report with criteria, weighted findings, evidence gaps, pass/revise/reject recommendation, confidence, and reviewer caveats.
techniques: [RT-02, CM-02, QA-01, QA-02, QA-04]
version: "1.0.0"
category: deep-analysis
tags: [deep-analysis, evaluation, review, critique, evidence-assessment, weighted-criteria, gated-workflow]
---

# /deepthink-evaluation-plain

Run the **plain-English deep-think evaluation system**: a five-step, multi-perspective workflow for reviewing an existing artifact at a depth that compensates for the absence of a review panel.

## When to use

- "Evaluate this proposal / plan / design / document."
- "Review this output against our requirements."
- "Is this good enough to ship, submit, approve, or rely on?"
- "What are the strengths, defects, risks, and evidence gaps?"

Use when **judging an existing object** is the goal. If the object does not exist yet, run `/deepthink-design` or `/deepthink-plan`. If the evaluation will feed a choice among alternatives, run `/deepthink-decision` after the evaluation report.

## How it works

This command inherits shared behavior from [`domain-deep-analysis/BACKBONE.md`](../BACKBONE.md): five gated phases/steps, mandatory perspectives, `AskUserQuestion` with plain-chat fallback, and anti-procrastination checks.

1. **Step 1 — Frame.** Restate the object, intended use, review boundary, standard, stakes, and pass/revise/reject gate. Gate: confirm scope and standard.
2. **Step 2 — Decompose.** Define criteria, weights totaling 100%, gating criteria, evidence map, and load-bearing unknowns. Gate: confirm criteria and evidence needs.
3. **Step 3 — Multi-perspective.** Run the mandatory roster and evaluation-specific additions from `BACKBONE.md`. Gate: pick what to stress-test.
4. **Step 4 — Stress-test.** False-pass pre-mortem, false-reject check, criterion sensitivity, evidence sufficiency check, adversarial stakeholder check, confidence calibration. Gate: decide what shapes the report.
5. **Step 5 — Synthesize.** Produce the evaluation report: object under review, criteria and weights, strengths, defects/risks, missing evidence, pass/revise/reject recommendation, confidence and reviewer caveats. Final gate: what's next.

`AskUserQuestion`/plain-chat gate behavior follows [`BACKBONE.md`](../BACKBONE.md).

## Configuration

### Parameters
- `$ARGUMENTS` — Optional. The object to evaluate, intended use, and any known rubric. If omitted, the command will ask via `AskUserQuestion`.

## Execution

1. **Load the underlying prompt:** Read [`domain-deep-analysis/deepthink_evaluation_plain.md`](../deepthink_evaluation_plain.md). Treat its instructions as authoritative.

2. **Collect inputs.** If not in `$ARGUMENTS`, ask via `AskUserQuestion`:
   - Object under review (paste, link, or description)
   - Purpose / intended use and audience
   - Evaluation context, standards, requirements, constraints, or rubric
   - Decision stakes if the object is incorrectly passed, revised, or rejected
   - Desired recommendation gate if not pass / revise / reject

3. **Check access and evidence.** If the object or requirements are unavailable, stop and request them. Do not invent evidence.

4. **Run Step 1 (Frame).** Output object, boundary, strictness, and recommendation gate. `AskUserQuestion` for GATE 1. **Stop. Wait.**

5. **Continue phase-by-phase.** Each phase ends with the gate mechanism defined in `BACKBONE.md`. Never run multiple phases in one output.

6. **At the FINAL GATE in Step 5,** offer `/deepthink-plan` if the user wants to turn required revisions into an execution plan, or offer to re-run evaluation when new evidence is supplied.

## False-Positive Prevention

1. **Reviewing something that isn't made yet, or using a review to pick a winner.** If what you have is still an idea or a rough outline, there's nothing to judge yet — `/deepthink-design-plain` or `/deepthink-plan-plain` fits better. If you're choosing between two finished things, review each one here and then use `/deepthink-decision-plain` to pick; a pass/revise/reject on one thing doesn't tell you which is better.
2. **Moving on before you've seen how much each criterion counts.** The weights and must-pass lines decide the verdict. If the second check-in only listed the criteria, your "yes" didn't cover the weights — I'll show the full table and ask again.
3. **A report with a part left out.** Before the final check-in I make sure all seven parts are there: what was reviewed and where the review stops, the criteria table with weights and must-pass lines, strengths backed by evidence, problems with how serious each one is, missing evidence kept apart from problems, a clear pass/revise/reject with what needs fixing, and confidence with caveats.

## Success Criteria

- All five phases ran, each with a gate.
- Criteria and weights are explicit and weights sum to 100%.
- Gating criteria are marked.
- Strengths and defects are evidence-backed or labeled as inference.
- Missing evidence is separated from defects.
- Step 5 clearly recommends pass, revise, or reject.
- Confidence is calibrated to evidence sufficiency and stakes.

## Coordination Notes

- This command is one of the scope-specific deep-think commands. If the review reveals that the object needs a redesign, suggest `/deepthink-design`; if it needs execution steps, suggest `/deepthink-plan`; if it needs a go/no-go choice, suggest `/deepthink-decision`.
- The system can be used to delay judgment. If the same object has been evaluated repeatedly without new evidence, recommend acting on the current recommendation or explicitly gathering the named missing evidence.
