---
title: "Design a Reusable Constraint Architecture That Channels AI Output"
category: prompt-engineering/skill-development
description: "Build a durable, reusable constraint architecture — a layered set of constraints (format, content, style, scope, authority, safety) the user applies across a class of tasks to reliably channel AI output into the shape the user wants. Distinct from a per-task constraint workshop; this is the library-building version, producing an asset reused for months."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-01
  - RT-02
  - QA-01
difficulty: advanced
tags:
  - skill-development
  - constraint-architecture
  - reusable
  - output-channeling
  - layered-constraints
updated: "2026-04-20"
related_prompts:
  - domain-prompt-engineering/goal-orientation/goalorientation_constraint_architecture_workshop.md
  - domain-prompt-engineering/skill-development/promptcraft_specification_defines_done.md
  - domain-prompt-engineering/skill-development/promptcraft_eval_harness.md
  - domain-prompt-engineering/skill-development/promptcraft_personal_context_document.md
---

# Design a Reusable Constraint Architecture That Channels AI Output

**Objective:** Produce a durable, reusable constraint architecture — a layered set of constraints the user applies across a class of tasks (not a single task) to reliably channel AI output into the shape the user needs. The architecture is a personal asset: reused across months, refined over time, and layered into prompts, system prompts, or instruction files depending on where each layer lives best.

**When to use:** The user runs a class of recurring tasks (a weekly stand-up summary, a code review comment, a customer email, a research brief, a bug report) and has noticed they keep typing similar constraints into every prompt. Or: the user has already produced a spec (via `promptcraft_specification_defines_done.md`) for one task and realizes the same constraints apply across the whole task class.

**Audience:** Users building AI practice infrastructure — who expect to run these tasks for months and are willing to invest in reusable assets.

**Distinction from `goalorientation_constraint_architecture_workshop.md`:** The goal-orientation workshop produces a per-task artifact before one run — constraints, escalation triggers, value hierarchy for *this* task. This prompt is the library-building version: it produces a cross-task architecture applicable to a whole class of tasks, designed to be reused. The workshop is a disposable; this is an asset.

---

## The Six Layers of a Constraint Architecture

Constraints come from different levels and belong in different places. Mixing them is what makes AI output feel random.

| Layer | What it constrains | Where it typically lives |
|---|---|---|
| **Format** | Length, structure, section ordering, markdown/plaintext, required fields | In the prompt |
| **Content** | What must be included, what must be excluded, required references, forbidden topics | In the prompt + sometimes the spec |
| **Style** | Tone, voice, person, reading level, vocabulary use | In the instruction file or persistent memory |
| **Scope** | What the task covers, what's out of scope, what belongs in a different task | In the prompt, reinforced by the spec |
| **Authority** | What the model can decide vs. must ask, what it can do vs. must flag | In the instruction file, reinforced by the prompt |
| **Safety** | Regulatory, legal, ethical, reputational floors; things the model must refuse | In the instruction file, never only the prompt |

An architecture names which layers apply, what each layer says, and where each layer is loaded. The user stops re-typing; the model stops freelancing.

---

## Inputs Required

1. **The task class.** Not one task — a family ("weekly exec summaries," "code review comments on PRs," "customer issue triage responses"). If the user can't name a class, they should build specs for 2–3 tasks first and look for the pattern.
2. **3–6 past examples of the class** where the user was satisfied with the output.
3. **2–4 past examples where the user was dissatisfied** — with a one-line note on what went wrong.
4. **The user's current prompt(s)** for this class. Might be one reused prompt or several adjacent ones.
5. **Where the user's persistent memory lives.** CLAUDE.md? ChatGPT custom instructions? A project context file? Nothing yet?

Refuse to run on a single-task sample. A single task can produce a spec, not an architecture. Architectures require cross-task generalization, which requires at least 3 tasks. If the user only has one, send them to `promptcraft_specification_defines_done.md` and come back after they've run a few more.

---

## Instructions

### Step 1 — Extract constraints from the satisfied examples

For each of the 3–6 satisfied examples, list the constraints that actually held. Not wishful constraints ("I'd like concise outputs") — real ones the output actually respected. Look for:
- Format: length bounds, structure patterns, section headers.
- Content: what showed up every time (a specific section, a specific caveat).
- Style: tone consistency.
- Scope: what each satisfied output did *not* try to cover.

Pool across examples. Constraints that appear in 2+ examples are architecture candidates. Constraints unique to a single example are task-specific, not class-wide.

### Step 2 — Diagnose the dissatisfied examples

For each of the 2–4 dissatisfied examples, trace the issue back to a missing or weak constraint. "The model added speculation I didn't want" → missing scope constraint or weak content constraint. "Output was twice as long as I'd accept" → missing format constraint. "Tone was wrong for the audience" → missing style constraint.

This produces the list of constraints the architecture needs to add.

### Step 3 — Assign each constraint to a layer

Every extracted or diagnosed constraint goes into exactly one of the six layers. If you can't decide which layer it belongs to, the constraint is probably either too vague (sharpen it) or actually two constraints (split them).

### Step 4 — Assign each layer to a home

Each layer goes where it reliably loads:
- **Format + Content:** prompt. (Per-task specific; change frequently.)
- **Scope:** prompt; reinforce in spec.
- **Style:** instruction file or persistent memory. (Changes rarely.)
- **Authority:** instruction file. (Changes on trust changes.)
- **Safety:** instruction file, *never only the prompt*. Anything in only the prompt vanishes when the user forgets to paste it.

Mismatched homes are the #1 source of inconsistent output. A style constraint that lives only in one prompt won't be applied to the next prompt.

### Step 5 — Write each layer's content

For each layer, produce the text that goes into its home:
- Testable: "Use second person throughout" beats "friendly tone."
- Specific: "Under 250 words" beats "concise."
- Complete: if constraints interact, state the precedence ("if conciseness conflicts with specificity, choose specificity").

Layer text is brittle when it's vague. Rewrite until a reader who has never met the user could apply the constraint and get the user's preferred output.

### Step 6 — Add the value hierarchy

Constraints conflict. Format says short; content says include the caveat; style says plain. Name the order constraints win in:
1. Safety.
2. Authority.
3. Content (what must be in).
4. Scope (what must stay out).
5. Format (length, structure).
6. Style (tone).

Name this explicitly in the architecture doc. Without a value hierarchy, the model picks — which is the model freelancing, which is the problem the architecture was built to solve.

### Step 7 — Write the loading protocol

One short section: how the architecture is loaded on any given task:
- What's already loaded persistently (from the instruction file / memory)?
- What the user adds per-task (from the prompt)?
- What's optional / situational?

A loading protocol prevents "I thought I told the model X" confusion — if X lives in persistent memory, it's there; if it lives in the prompt, the user has to paste it.

### Step 8 — Measure against the dissatisfied examples

For each dissatisfied example, ask: *if this architecture had been loaded, would the dissatisfaction have been prevented?* If not, the architecture is missing a constraint. Add it.

If the architecture would have prevented 3 of 4 dissatisfied cases but not the fourth, decide: is the fourth a one-off (accept; don't add noise to the architecture for a one-off) or an emerging pattern (add)?

### Step 9 — Set the revision rhythm

Architectures decay. Projects change; task classes evolve; the model itself changes.
- **Per-task:** when a new constraint is added in-prompt, log it. If it shows up in 3+ tasks, promote to the architecture.
- **Quarterly:** audit the architecture against a fresh sample of tasks.
- **On model version change:** retest, because some layers (style, authority) behave differently on different model versions.

---

## Constraints

### Must
- Be built from a class of 3+ tasks, not a single task.
- Place every constraint into exactly one of the six layers.
- Route each layer to the right home (prompt / instruction file / spec).
- Include a value hierarchy.
- Include a loading protocol.
- Be rerun against dissatisfied examples.

### Must Not
- Be built from one task.
- Load all constraints into the prompt — that's not an architecture, it's a megaprompt.
- Place safety constraints only in the prompt.
- Include constraints that appeared in only one example (unless the user explicitly promotes them).
- Exceed the length the instruction file + prompt can actually hold; architectures that overflow the instruction file get silently truncated.

---

## False-Positive Prevention

1. **Aspirational constraints.** "I'd like the model to be thoughtful" is aspirational, not testable. The architecture only includes constraints the user can verify against output.
2. **Layer collisions.** The same constraint showing up in both the prompt and the instruction file in conflicting forms is worse than either alone. Deduplicate.
3. **Overreach from one bad output.** A single bad output shouldn't add a permanent constraint. Watch for 2+ occurrences before promoting.
4. **Missing value hierarchy.** If the architecture has 10 constraints and no precedence, the model resolves conflicts by what the user never specified. Always produce Step 6.
5. **Safety in the prompt.** Anything that must hold regardless of what the user types can't live only in the prompt. If the user forgets to paste it, it doesn't hold. Escalate safety to the instruction file.
6. **Task-specific constraints promoted too early.** Architecture constraints are class-wide. If a constraint only applies to one task in the class, it's a spec item, not an architecture item.
7. **"Include everything."** An architecture that tries to cover every edge case becomes unusable. Cut. The class's 80% is worth more than 100% coverage of the 20%.
8. **Ignoring where the instruction file actually loads.** An instruction file that the user's tool doesn't read is a file with no effect. Verify the loading behavior for each tool the user uses.
9. **Running this when a spec would suffice.** If the user has only one task, produce a spec; don't manufacture a class.

---

## Output Format

```markdown
## Task class
[Named.]

## Evidence
- Satisfied examples: [N] (floor: 3)
- Dissatisfied examples: [N] (floor: 2)
- Persistent-memory target: [CLAUDE.md | custom instructions | project context | none]

## Extracted constraints (class-wide)
| Constraint | Layer | Evidence (satisfied examples) | Diagnosed from dissatisfied example? |
|---|---|---|---|
| [...] | Format | [...] | [...] |
| ... | ... | ... | ... |

## Architecture

### Layer 1 — Format
**Home:** Prompt.
**Content:** [testable, specific]

### Layer 2 — Content
**Home:** Prompt (+ reinforced in spec).
**Content:** [...]

### Layer 3 — Style
**Home:** Instruction file.
**Content:** [...]

### Layer 4 — Scope
**Home:** Prompt.
**Content:** [...]

### Layer 5 — Authority
**Home:** Instruction file.
**Content:** [...]

### Layer 6 — Safety
**Home:** Instruction file. Never only in prompt.
**Content:** [...]

## Value hierarchy
1. Safety
2. Authority
3. Content
4. Scope
5. Format
6. Style

## Loading protocol
- Persistent (always loaded): [...]
- Per-task (paste): [...]
- Optional / situational: [...]

## Dissatisfied-example retest
For each dissatisfied example: would this architecture have prevented the issue?
- Example 1: [Yes / No — if no, what's missing]
- Example 2: [...]
- ...

## Revision rhythm
- Per-task: log new prompt-only constraints. Promote if used 3+ times.
- Quarterly: audit against fresh sample.
- On model version change: retest style + authority layers.
```

---

## Verification

- [ ] Architecture was built from a class of ≥3 tasks.
- [ ] Each constraint is in exactly one layer.
- [ ] Each layer is assigned to the right home; safety is not only in prompt.
- [ ] Value hierarchy is named.
- [ ] Loading protocol is explicit.
- [ ] Dissatisfied-example retest was run; gaps addressed.
- [ ] Revision rhythm is set.
- [ ] Total content fits within the instruction file's effective load capacity.
