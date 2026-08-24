---
title: "AI Agent Master-Orchestrator Generator (Guided / Manual / Surgical)"
category: AI-ML/agentic-ai-systems
description: "Emit a master orchestrator for a multi-stage agentic system or toolkit — a top-level conductor that interviews the user, classifies their entry stage, routes to the right stage prompts, critiques each output against that stage's verification, and enforces the hard gates between stages — exposed in three usage modes (guided, manual, surgical) so it adapts to how much hand-holding the user wants."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-06
difficulty: advanced
tags:
  - orchestrator
  - multi-stage-pipeline
  - usage-modes
  - gate-enforcement
  - toolkit-assembly
updated: "2026-06-20"
related_prompts:
  - domain-AI-ML/agentic-ai-systems/aiagent_hard_gates_designer.md
  - domain-AI-ML/agentic-ai-systems/aiagent_planning_decomposition_design.md
  - domain-agentic-resources/commands/multi-agent/multiagent_two_tier_architecture_template.md
---

# AI Agent Master-Orchestrator Generator (Guided / Manual / Surgical)

**Objective:** Generate the **master orchestrator** for a multi-stage agentic system or self-contained toolkit — the top-level prompt/agent that sequences the stages, decides what to run next, and holds the gates. The generated orchestrator interviews the user, classifies which stage they are actually starting from, recommends the next ≤3 stage prompts, critiques each stage's output against that stage's verification checklist, and **enforces the hard gates** before gated stages may proceed. It exposes three usage modes — **guided** (the orchestrator drives, interview + critique + gates), **manual** (the user walks the pipeline themselves with the orchestrator as a map), and **surgical** (jump straight to one stage) — so one artifact serves a novice and an expert. This produces the conductor; it does not re-author the stage prompts it conducts.

**When to Use:**
- You have (or are designing) a multi-stage pipeline/toolkit and need the top-level orchestrator that ties the stages together.
- Each stage prompt exists or is planned, but nothing sequences them, classifies the entry point, or enforces the between-stage gates.
- You want one entry point that adapts to user expertise instead of hand-rolling a bespoke orchestrator per toolkit.

**When NOT to Use:**
- The system is a single agent or a single stage — there is nothing to orchestrate; author the agent/prompt directly.
- You need the *gate logic itself* designed — produce it with `aiagent_hard_gates_designer.md` first, then have this orchestrator enforce it.

## Inputs / Context

Provide what you can; the generator degrades gracefully if some are missing:
- **Pipeline definition** — the ordered stages, each with its purpose and terminal artifact.
- **Stage prompts** — the prompt/agent that authors each stage's output (paths if they exist; placeholders if not).
- **Verification per stage** — the checklist each stage's output must pass to be "done."
- **Hard gates** — the gate(s) that block progression (which stage they sit before, the pass condition), ideally from `aiagent_hard_gates_designer.md`.
- **Entry-point signals** — how to tell which stage a given user is actually starting from.
- **Terminal artifact** — the final bundle the whole pipeline produces.

## Constraints

**Must:**
- Generate an orchestrator that **classifies the user's entry stage** before recommending work, and recommends a small next set (≤3), not the whole pipeline at once.
- **Enforce the hard gates in code/logic**, not as a suggestion — a gated stage cannot proceed until its prerequisite gate passes; the orchestrator refuses, it does not merely warn.
- Expose all three modes (guided / manual / surgical) and make the default mode explicit.

**Must Not:**
- Re-author or duplicate the stage prompts — the orchestrator **routes to and critiques** them by reference.
- Let the user skip a hard gate by choosing surgical mode (surgical jumps *between* gates, never *through* one).
- Recommend the next stage without first critiquing the current stage's output against its verification checklist.

**Instructions:**

1. **Lay out the pipeline spine.** List the stages in order with each one's purpose, the stage prompt that authors it, its terminal artifact, and its verification checklist. This table is the orchestrator's routing map.

2. **Mark the hard gates on the spine.** For each gate, record which stage it precedes, its pass condition, and the refusal behavior when unmet. These are the points where surgical and manual modes are still blocked from advancing.

3. **Design the entry-stage classifier.** Specify the short interview/questions the orchestrator asks to determine which stage the user is actually starting from (what they already have vs. what's missing), so it doesn't restart finished work.

4. **Design the recommend-next logic.** From the classified stage, the orchestrator proposes the next ≤3 stage prompts with a one-line why each, and the artifact each will produce. Keep the horizon short to avoid overwhelming the user.

5. **Design the critique loop.** After each stage runs, the orchestrator scores the output against that stage's verification checklist, names gaps, and either passes it forward or sends it back — closing the loop so quality is checked at every hop, not just at the end.

6. **Wire gate enforcement.** Before any gated stage, the orchestrator checks the gate's pass condition and **refuses to proceed** if unmet, telling the user exactly what is missing. Confirm surgical/manual modes cannot route around a gate.

7. **Specify the three modes.** Define precisely how the same orchestrator behaves in: **guided** (interview → recommend → run → critique → gate, the orchestrator drives); **manual** (the orchestrator prints the map and gates but the user picks stages); **surgical** (jump to one named stage, run it, return — gates between still apply). State the default and how the user switches.

8. **Emit the orchestrator artifact.** Produce the actual orchestrator prompt/spec — its identity, the interview script, the routing table, the critique rubric reference per stage, the gate checks, the mode switch, and the terminal-artifact assembly — ready to drop in as the toolkit's entry point.

**Output Format:**

A markdown orchestrator spec (the deliverable is the orchestrator itself):
- **Pipeline Spine** — table: Stage | Purpose | Stage prompt (path) | Terminal artifact | Verification ref
- **Gate Map** — table: Gate | Sits before stage | Pass condition | Refusal behavior
- **Entry-Stage Classifier** — the interview questions + how answers map to a starting stage
- **Recommend-Next Logic** — how the next ≤3 stages are chosen and presented
- **Critique Loop** — how each stage's output is scored and passed/returned
- **Three Modes** — guided / manual / surgical behavior + default + switch mechanism
- **Generated Orchestrator** — the assembled orchestrator prompt/spec, ready to use

## Verification

- [ ] The orchestrator classifies the entry stage before recommending work, and recommends ≤3 next stages.
- [ ] Hard gates are enforced as refusals; no mode (including surgical) can route through a gate.
- [ ] Each stage's output is critiqued against its verification checklist before advancing.
- [ ] Stage prompts are referenced/routed-to, never duplicated in the orchestrator.
- [ ] All three modes are specified with an explicit default and switch mechanism.
- [ ] The generated orchestrator artifact is concrete enough to use as the toolkit's entry point.

## False-Positive Prevention

❌ **DON'T:**
- Emit an orchestrator that dumps the entire pipeline at the user at once — that is a table of contents, not a conductor.
- Let surgical mode become a way to skip a gate ("just run stage 7") — surgical jumps between gates, never through one.
- Copy the stage prompts' content into the orchestrator; it should route to them and critique their output.
- Advance to the next stage without checking the current output against its verification checklist.

✅ **DO:**
- Classify where the user really is and recommend a short, ordered next step.
- Make gates refusals with a clear "here's what's missing," not warnings.
- Keep the orchestrator thin: sequencing, classification, critique, gates, assembly — the stages do the work.
- Make the three modes genuinely different in how much the orchestrator drives, sharing one gate set.

## Example Output

```markdown
## Generated Orchestrator: "Idea → Shippable-Software" Toolkit (excerpt)

### Pipeline Spine (excerpt)
| Stage | Purpose | Stage prompt | Terminal artifact | Verification |
|---|---|---|---|---|
| 2 Problem validation | Confirm the pain is real | stage-2/validation_*.md | ≥5 scored interviews | rubric in stage 2 |
| 6 Decision validation | Pre-mortem the bet | stage-6/premortem_*.md | pre-mortem doc | stage 6 checklist |
| 7 PRD authoring | Spec the build | stage-7/prd_*.md | PRD + cut lines | stage 7 checklist |

### Gate Map
| Gate | Sits before | Pass condition | Refusal behavior |
|---|---|---|---|
| Validation gate | Stage 4 | ≥5 rubric-scored interviews exist | refuse; list missing interviews |
| Pre-mortem gate | Stage 7 | pre-mortem doc present | refuse; route to stage 6 |

### Entry-Stage Classifier
Asks: "Do you have customer interviews? A PRD? An architecture?" → maps presence/absence to the
earliest incomplete stage; never restarts a stage whose artifact already passes verification.

### Recommend-Next Logic
From classified stage, proposes ≤3: e.g., "Stage 2 (you have no interviews) → Stage 3 → Stage 4."

### Critique Loop
After Stage 2: scores interviews against the rubric; if <5 scored, returns with the gap, does not advance.

### Three Modes
- **Guided (default):** interview → recommend → run → critique → gate, orchestrator drives.
- **Manual:** prints spine + gate map; user picks stages; gates still enforced.
- **Surgical:** "run stage 7" → checks pre-mortem gate first; if unmet, refuses and routes to stage 6.
Switch via: "switch to manual/surgical."

### Generated Orchestrator
[Assembled identity + interview script + routing table + per-stage critique refs + gate checks +
mode switch + terminal-bundle assembly — ready to drop in as orchestrator_*.md.]
```

**Techniques Used:**
- **ST-01 (Clear Objective Statement):** the orchestrator's job — sequence, classify, critique, gate, assemble — is stated up front.
- **ST-02 (Structured Sequential Instructions):** spine → gates → classifier → recommend → critique → modes → emit.
- **ST-03 (Output Format Specification):** the deliverable is a concrete, ready-to-use orchestrator artifact with a fixed shape.
- **CM-02 (Constraint Specification):** route-don't-duplicate and gates-as-refusals are governing constraints.
- **DS-06 (Prioritization and Severity Guidance):** recommend-next surfaces the few highest-priority stages, not the whole pipeline.

**Related Prompts:**
- `aiagent_hard_gates_designer.md` — produces the gate logic this orchestrator enforces between stages.
- `aiagent_planning_decomposition_design.md` — design the stage decomposition the orchestrator sequences.
- `domain-agentic-resources/commands/multi-agent/multiagent_two_tier_architecture_template.md` — the planner/worker pattern an orchestrator-led system implements.
