# Prompt Skill Development

**Purpose:** Prompts that help individuals build their prompt-engineering skill over time. Not one-off utilities — these produce assets (context documents, specs, eval harnesses, constraint architectures) the user reuses and refines for months.

These prompts assume the user already works with AI regularly and wants to level up. Beginners should start with `NON_CODING_QUICK_START.md` and `AI_AGENT_QUICK_START.md` at the repo root, not here.

---

## The Four Disciplines

The skill-development track is organized around four orthogonal disciplines:

| Discipline | What it is | Signal of weakness |
|---|---|---|
| **Prompt craft** | Writing the prompt — structure, format, explicit output contract | Prompts get vague answers; user relitigates output for an hour |
| **Context management** | What the model can see — files, memory, vocabulary | Model is confidently wrong about things it couldn't have known |
| **Intent clarity** | Knowing what the user actually wants | User accepts plausible answers that miss the real need |
| **Specification** | Turning intent into observable, testable criteria | User can't tell whether output is good; iteration loops forever |

Weaknesses in one don't imply weaknesses in another. Fix by leverage, not by how each one feels.

---

## The 8 Prompts

| File | What it does |
|------|--------------|
| `promptcraft_pre_ai_thinking_exercise.md` | Off-screen thinking pass before opening a chat — produces a one-page artifact naming outcome, knowns, unknowns, done, and mode |
| `promptcraft_rapid_four_discipline_diagnostic.md` | ~10-minute self-assessment across the four disciplines, returning the single weakest one + one next action |
| `promptcraft_deep_four_discipline_roadmap.md` | Evidence-based diagnostic using 10+ real artifacts; produces a 3–6 month sequenced development roadmap with artifacts, checkpoints, and exit criteria |
| `promptcraft_rewrite_vague_ask.md` | Transforms a real, casual chat opener into a self-contained problem statement naming outcome, inputs, constraints, done, and mode |
| `promptcraft_personal_context_document.md` | Builds a reusable 1–2 page context document (identity, projects, stack, vocabulary, anti-context) from evidence of what the user keeps re-typing into new chats |
| `promptcraft_specification_defines_done.md` | Produces a pass/fail spec for a recurring task — observable criteria, must-pass/should-pass ranking, stop rule, escalation triggers, counterfactual |
| `promptcraft_eval_harness.md` | Builds a personal-scale eval harness (5–10 cases + rubric + baseline) for a recurring task so prompt changes become measurable instead of felt |
| `promptcraft_constraint_architecture_design.md` | Designs a reusable, layered constraint architecture (format, content, style, scope, authority, safety) for a whole class of tasks — distinct from a per-task workshop |

---

## How the Prompts Fit Together

A typical skill-development arc over 3–6 months:

1. **Start with diagnosis.** Run `promptcraft_rapid_four_discipline_diagnostic.md` first to locate the weakest discipline.
2. **If the rapid diagnostic stops moving,** escalate to `promptcraft_deep_four_discipline_roadmap.md` and work the roadmap.
3. **Build intent muscles first.** `promptcraft_pre_ai_thinking_exercise.md` for two weeks on every non-trivial task, paired with `promptcraft_rewrite_vague_ask.md` when a chat opener feels thin.
4. **Then context.** Build `promptcraft_personal_context_document.md`. Layer with `cos_memory_scaffold_claude_md.md` (role) and `escapemedian_bootstrap_instruction_file.md` (preferences) — three separate files, not one merged file.
5. **Then specification.** `promptcraft_specification_defines_done.md` on the 2–3 task types you run most.
6. **Then measurement.** `promptcraft_eval_harness.md` on top of the specs.
7. **Finally, architecture.** `promptcraft_constraint_architecture_design.md` produces a reusable library across a task class.

Prompt craft improves as a byproduct of fixing the other three. Most users who go "my prompts are bad" are actually diagnosing intent or specification weakness.

---

## Distinctions From Adjacent Folders

- `goal-orientation/` — pre-flight diagnostics for a single task ("am I solving the right problem?" workshop). This folder is for building durable skill; goal-orientation is for per-task use.
- `escape-median/` — moving the model off its default output. Overlaps with prompt craft; use escape-median when the issue is "the model keeps defaulting to median," not "I don't know what I want."
- `evaluation/` — measuring correctness of AI outputs at production scale. `promptcraft_eval_harness.md` in this folder is the personal-scale entry point; `correctness_eval_design_prompt.md` in evaluation/ is the scale-up.
- `prompt-improvement/` — rewrites existing prompts. Use when the issue is the prompt itself, not the underlying skill pattern the user needs to build.
- `domain-engineering-workflows/done-definition/` — production tools for translating fuzzy tasks into done gates. `promptcraft_specification_defines_done.md` is the skill-development complement that teaches the user how to build their own; `done_definition_translator.md` is for running the translation on-the-fly.

---

## When to Use This Folder

- You already use AI regularly and want to level up.
- You have real artifacts (chats, outputs, corrections) to ground the work.
- You're willing to spend 2+ hours/week on deliberate practice.

## When Not to Use This Folder

- You're new to AI. Read the quick-start guides at the repo root first.
- You want a single prompt to run right now. Use the per-task tools in adjacent folders.
- You're looking for team-level AI adoption guidance. Try `goal-orientation/goalorientation_team_ai_misalignment_map.md` or the browser-automation and AI-strategy folders in `domain-business-strategy/`.
