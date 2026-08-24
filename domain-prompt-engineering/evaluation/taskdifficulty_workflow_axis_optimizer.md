---
title: "Optimize a Workflow Based on Which AI-Difficulty Axes Are Hardest"
category: prompt-engineering/evaluation
description: "Takes a multi-step workflow the user is running with AI and redesigns it to reduce the total difficulty along its hardest axes — moving steps, changing human-AI hand-offs, adding verification points, splitting steps, or rerouting entirely. The goal is not to 'reduce difficulty' in general but to target the specific axis that's dragging the workflow."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-06
  - CM-02
  - DS-01
  - QA-01
difficulty: advanced
tags:
  - task-difficulty
  - workflow-optimization
  - axis-based
  - hand-off-design
  - verification-points
updated: "2026-04-20"
related_prompts:
  - domain-prompt-engineering/evaluation/taskdifficulty_decompose_by_axes.md
  - domain-prompt-engineering/evaluation/taskdifficulty_calibrated_comparison.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_agent_work_loop_design.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_verification_depth_calibrator.md
  - domain-prompt-engineering/delegation/delegation_role_based_plan.md
---

# Optimize a Workflow Based on Which AI-Difficulty Axes Are Hardest

**Objective:** Given a multi-step workflow that includes AI (e.g., "draft → review → revise → send" or "triage → research → synthesize → recommend"), identify the step-axis pairs that cause the most drag on the workflow, and redesign the workflow to reduce drag on those specific axes. The output is a revised workflow — not a general admonition to "try harder."

**When to use:** An existing AI-assisted workflow is producing inconsistent results, slow iteration, or silent quality drift. The user has run `taskdifficulty_decompose_by_axes.md` on individual steps and wants to redesign the flow around the findings. Or: the user hasn't done the per-step decomposition yet but has a workflow they want to diagnose holistically.

**Audience:** Developers and prompt engineers redesigning a workflow for reliability. Also operations-minded individuals tightening a personal cadence they run weekly.

---

## Inputs Required

1. **The workflow, step by step.** Each step named. For each: who/what does it (human / AI / automation), what's the input, what's the output.
2. **A sample of 3–5 recent runs of the workflow** with outcomes — ideally including a run that failed or felt wrong.
3. **Where the workflow hurts.** User's report: "the third step is where it usually goes wrong," "the whole thing feels slow," "outputs are inconsistent."
4. **Any per-step axis decompositions** already run (from `taskdifficulty_decompose_by_axes.md`). If none, the prompt runs a quick axis pass inline.

Refuse to optimize a workflow that has only run once or twice. A workflow without reps doesn't have a pattern to optimize against; you'd be optimizing noise. Wait until there are 3+ runs.

---

## Instructions

### Step 1 — Map the workflow as a step grid

Produce a grid: rows = steps, columns = the eight axes from `taskdifficulty_decompose_by_axes.md` (specification clarity, context payload, tool availability, reversibility, stakes, verification cost, ambiguity of correctness, horizon). Score each cell 0–3.

If the user supplied per-step decompositions, use those. Otherwise run the axis scoring inline for each step.

Add one extra column: **who owns the step** (human / AI / hybrid).

### Step 2 — Identify drag cells

Drag cells are cells scoring 2 or 3 where the owner is not the right owner for the axis:
- Specification clarity weak + AI owner → drag (AI shouldn't own fuzzy-spec steps).
- Verification cost high + human owner → drag (cheap to verify tasks wasting human time).
- Ambiguity of correctness high + AI owner → drag (AI confidently wrong).
- Reversibility low + AI owner with no gate → drag (irreversible AI actions without review).

These are the intervention targets.

### Step 3 — Identify axis clusters across steps

Some axes are hard in a pattern:
- **Context payload stays high across multiple steps** → context isn't moving forward between steps; likely missing a context document or handoff artifact.
- **Verification cost increases late in the workflow** → errors compound; catch them earlier.
- **Specification clarity drops at a handoff** → handoff is losing intent. Add an explicit intent-and-verification-first artifact (see `ai_pattern_intent_and_verification_first.md`).

Name the cluster patterns; they drive redesign more than any single cell.

### Step 4 — Apply redesign moves, targeted by axis

There are six canonical redesign moves; pick by which axis is dragging.

1. **Move the step to the other owner.** For specification-clarity-weak or ambiguity-high AI steps, move to human. For verification-low and expertise-low human steps, move to AI.
2. **Split the step.** If a step has multiple 3s, split into two steps where each handles one bottleneck axis. (E.g., "research and synthesize" splits into "gather raw material (AI)" and "synthesize and frame (human or AI with tight spec)".)
3. **Add a verification gate.** For reversibility-low + stakes-high combinations without a gate, insert a human-review step before the output takes effect. The gate's job is to catch silent failures.
4. **Push context forward explicitly.** If context payload is high across multiple steps, produce a per-run context artifact at step 1 that gets passed into subsequent steps, rather than reassembled each time.
5. **Change the mode.** A step being run as "draft" with ambiguity-of-correctness at 3 is a mode mismatch; run as "options" (AI produces 2–3 alternates, human picks) or as "critique" (human produces, AI pokes holes).
6. **Cut the step.** If a step's drag outweighs its value, question whether it belongs at all.

### Step 5 — Name the intervention per drag cell

For each drag cell, name which redesign move applies and what the step looks like after.

### Step 6 — Rebuild the workflow

Produce the revised step grid. Show:
- The new sequence of steps.
- Who owns each.
- New axis scores (with evidence that the drag axis has moved from ≥2 to ≤1).
- Any new hand-off artifacts that persist context across steps.

If the redesign doesn't move the drag axis, the redesign failed. Try a different move.

### Step 7 — Budget the redesign

Not every redesign is worth doing. For each proposed change, estimate:
- Setup cost (one-time): how long to wire up the new step / artifact / gate.
- Per-run cost (recurring): does the redesign add human time?
- Expected benefit: which drag axis does it move, by how much.

Reject changes where setup cost is high and per-run benefit is tiny. Prioritize changes that move a 3 to a 1 at low per-run cost.

### Step 8 — Define the measure

Before the user adopts the redesign, define how they'll know it worked. Usually one of:
- Failure rate drops (track failed runs before vs. after).
- Iteration count per run drops.
- Human time per run drops without quality dropping.
- Eval harness score rises (see `promptcraft_eval_harness.md`).

Without a measure, the redesign can't be evaluated and the workflow will silently drift back.

---

## Constraints

### Must
- Score every step on every axis, not just the steps the user complained about.
- Identify drag cells (owner-axis mismatches) explicitly.
- Name cluster patterns across steps, not just per-cell issues.
- Apply a canonical redesign move for each drag; don't improvise generic "make it better" suggestions.
- Budget the redesign (setup + per-run + benefit).
- Define the success measure before adoption.

### Must Not
- Optimize a workflow with <3 real runs.
- Propose a redesign that doesn't move a specific axis from ≥2 to ≤1.
- Collapse steps because collapsing feels tidier; collapse only if the collapse actually reduces drag.
- Add human gates everywhere — that defeats the point of delegation.
- Recommend a redesign whose setup cost outweighs multi-month benefit.
- Treat the workflow as a black box. Step-by-step owner + axis scoring is the point.

---

## False-Positive Prevention

1. **Optimizing the loud step, not the bottleneck step.** The step the user complains about may not be the drag step. Scoring the whole grid often reveals the real drag is an earlier step (bad context hand-off) that the complained-about step is just symptomatic of.
2. **Moving steps to humans whenever AI struggles.** If every struggling step goes to a human, the workflow isn't an AI workflow anymore. The question is which owner handles each axis well, not which owner handles *this task* well.
3. **Splitting steps that shouldn't split.** Some steps fail because they're split (context gets lost at the seam). If verification cost is dominated by re-establishing context between steps, merge, don't split.
4. **Gates that the user will skip.** A human-review gate that slows the workflow by 10× will get skipped within two weeks. Make the gate proportional to the reversibility and stakes; don't require human review of every draft.
5. **Context documents that don't actually travel.** A step-1 artifact that later steps don't read isn't a context hand-off; it's a file. Make sure the later steps actually receive the artifact.
6. **Single-axis tunnel vision.** Reducing specification clarity drag while raising verification cost is a wash. Check that moves don't push drag to a different axis.
7. **Premature redesign.** Running this prompt on a workflow that has run twice and "felt wrong" is premature. Gather more reps first.
8. **Post-redesign drift.** Workflows decay without a measure. Step 8 isn't optional.

---

## Output Format

```markdown
## Workflow today
| Step | Owner | Input | Output |
|---|---|---|---|
| 1 | ... | ... | ... |
| ... | | | |

## Axis grid (0–3)
| Step | Spec | Context | Tools | Reversibility | Stakes | Verification | Ambiguity | Horizon | Owner |
|---|---|---|---|---|---|---|---|---|---|
| 1 | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| ... | | | | | | | | | |

## Drag cells (owner-axis mismatches ≥ 2)
- Step [N], [axis]: [score] owned by [owner]. Why it's drag: [...]

## Cluster patterns across steps
- [Pattern]: [...]

## Redesign
### Change [N]
- Drag cell targeted: [...]
- Move: [which of the six canonical moves]
- After: [new step or owner or artifact]
- Projected new score: [old] → [new]
- Setup cost: [...]
- Per-run cost: [...]
- Expected benefit: [...]

## Revised workflow
| Step | Owner | Input | Output | Notes |
|---|---|---|---|---|
| 1 | ... | ... | ... | ... |
| ... | | | | |

## Success measure
- Metric: [failure rate / iteration count / human time / eval score]
- Baseline (before adoption): [value]
- Target after adoption: [value]
- Review date: [...]

## Adoption plan
- [Order of changes, dependencies, rollback criteria]
```

---

## Verification

- [ ] All steps scored on all eight axes.
- [ ] Drag cells identified via owner-axis mismatch, not vague concern.
- [ ] Cluster patterns across steps named.
- [ ] Each redesign change cites one of the six canonical moves.
- [ ] Each redesign move demonstrates moving the drag axis from ≥2 to ≤1.
- [ ] Budget (setup + per-run + benefit) named per change.
- [ ] Success measure and review date set before adoption.
