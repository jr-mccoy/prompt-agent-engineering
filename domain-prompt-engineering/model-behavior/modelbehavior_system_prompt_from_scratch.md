---
title: "Build a System Prompt from Scratch Aligned with Constitutional Principles"
category: prompt-engineering/model-behavior
description: "Structured design session for authoring a new system prompt that cooperates with the target model's base training — starting from the task, deriving the principles that should govern it, translating them into operational rules the model can check itself against, and locking them in an ordered format the model won't average over."
techniques:
  - ST-01
  - ST-02
  - DS-01
  - CM-02
  - ST-03
  - QA-01
difficulty: advanced
tags:
  - model-behavior
  - system-prompt
  - constitutional-alignment
  - design
  - from-scratch
updated: "2026-04-20"
related_prompts:
  - domain-prompt-engineering/model-behavior/modelbehavior_refactor_system_prompt.md
  - domain-business-strategy/chief-of-staff/cos_memory_scaffold_claude_md.md
  - domain-prompt-engineering/goal-orientation/goalorientation_constraint_architecture_workshop.md
---

# Build a System Prompt from Scratch Aligned with Constitutional Principles

**Objective:** Produce a new system prompt for a specific task on a specific model by (1) extracting the principles that should govern the task, (2) translating each principle into an operational rule the model can apply and self-check, (3) ordering the rules so the highest-priority ones come first and tie-break the rest, and (4) stating what the model should do when rules conflict. The result is a prompt the model's base training supports rather than fights.

**When to use:** You're writing a system prompt for a new workflow — a new agent, a new internal tool, a new repeat-use Claude Code / Custom GPT — and you want to start from principles rather than patching your way up from a rough draft. Or: your previous prompt has drifted past the point of refactor and you want to restart with structure.

**Audience:** Prompt engineers, developers, product teams, and power users who ship system prompts into production and need the prompt to behave consistently across sessions and across minor task variations.

---

## Inputs Required

1. **Task definition.** What the model is supposed to do, in one paragraph. Not the artifact format — the job.
2. **Target model and version.** Constitutional tendencies differ across model families.
3. **Audience of the output.** Who reads or uses what the model produces.
4. **Known failure modes** in this task — either observed from prior prompts or anticipated. Failure modes are the raw material for the rules.
5. **Non-negotiables** — anything that must be true of every output (legal, safety, format for downstream systems).
6. **Whether the prompt is for a one-off or a recurring workflow.** Recurring workflows need a revision trigger; one-offs don't.

Refuse to produce a system prompt for an undefined task. "A general assistant system prompt" is not a task — it's a label. Redirect to the CLAUDE.md scaffold prompt for that case.

---

## Instructions

### Step 1 — Extract 3–7 governing principles

Principles are the "why." Each principle must:
- Answer a decision the model will face. Not "be helpful" (too vague). "When the request is ambiguous, prefer the narrower interpretation and flag the assumption" (answers a real decision).
- Be defensible. If the user had to justify it to a colleague, they could.
- Be distinguishable from the other principles. If two principles could be merged, merge them.

Aim for 3–7. Fewer than 3 and the prompt will underspecify; more than 7 and the model will average across them.

### Step 2 — For each principle, write the operational rule

A principle is abstract; a rule is checkable. For each principle produce one rule that:
- States what the model *does* (positive action), not only what it doesn't do.
- Is testable against a single output. A reviewer should be able to look at an output and decide yes/no.
- Names the behavior it overrides, if it's overriding a base-model default. (E.g., "Default to decision, not options" overrides the common default of offering alternatives.)

### Step 3 — Rank the rules

Number the rules 1..N by priority. The ranking matters for conflict resolution (Step 5). Ranking criteria:
- Non-negotiables first.
- Rules that govern the output's *purpose* before rules that govern *form*.
- Rules that govern *correctness* before rules that govern *style*.

If the user can't rank two rules, flag it — they're either redundant or the user hasn't decided which matters more.

### Step 4 — Define the output contract

Separately from the behavioral rules, specify:
- Format (prose, table, JSON, markdown sections — name it).
- Length bounds, if any.
- What must appear in every output.
- What must never appear.
- What the model should do when it doesn't have enough information (ask, flag, proceed with assumption — pick one).

The output contract is thin on purpose. Most of the prompt's weight is in the rules, not the format.

### Step 5 — State the conflict-resolution policy

Rules will eventually conflict. State how the model breaks ties:
- Higher-ranked rule wins.
- If two rules at the same rank conflict, the model should [surface the conflict and ask | pick the more conservative | pick the one closer to the stated task].

Without a tie-breaker, the model will silently pick, and silent picks accumulate into drift.

### Step 6 — Add the self-check

End the prompt with 2–4 lines the model runs against its own draft before emitting:
- "Does this respect rule 1?"
- "Does this violate any non-negotiable?"
- "If I cut this output to half the length, what would I cut — and should it be cut?"

Self-check lines are cheap and catch a meaningful fraction of drift. Keep them short or the model will average over them.

### Step 7 — Write the revision trigger (recurring prompts only)

One line at the end: what signal tells the author this prompt needs updating. Examples:
- "When a rule is being violated on 1 in 5 runs."
- "When a new failure mode appears that no existing rule covers."
- "After any model version change."

Without a revision trigger, system prompts rot and the author doesn't notice until the drift is systemic.

### Step 8 — Predict the behavior

Write two short examples of what you'd expect the model to produce under this prompt for two representative inputs — one easy, one hard. These aren't part of the prompt; they're the user's yardstick for whether the prompt is doing its job after deployment.

---

## Constraints

### Must
- Start from task and principles, not from a template.
- Produce exactly one operational rule per principle.
- Rank the rules.
- Specify the conflict-resolution policy.
- Include a self-check.
- Include a revision trigger for recurring prompts.

### Must Not
- Produce more than 7 rules. More rules = less adherence.
- Rely on adjectives ("thoughtful," "rigorous," "balanced") in the rules. The model cannot check these.
- State only negative rules ("don't hedge," "don't add preambles"). Each negative rule needs a positive replacement.
- Invent non-negotiables the user didn't supply.
- Embed examples so long they dominate the prompt. Keep examples one sentence to one short paragraph.

---

## False-Positive Prevention

1. **A beautiful prompt is not a working prompt.** Judge by outputs on the two representative inputs, not by how it reads.
2. **Don't let principles drift into platitudes.** "Be truthful" fails the "answers a decision" test. "When confidence is below X, flag it inline rather than deferring" passes.
3. **The ranking is not a formality.** If the author shrugs when asked to rank, the prompt will produce drift at the rank boundary. Push for a real ranking or flag the unranked pair.
4. **Self-check lines that are too long stop being checked.** If the model's self-check is itself four paragraphs, it will average over it. Keep each check to one short line.
5. **Recurring prompts without a revision trigger will rot.** Non-negotiable for recurring; skip for one-offs.
6. **Don't copy rules across model families.** A rule that works on Claude may need rephrasing on GPT. Flag model-specific phrasing.
7. **If the task is underdefined**, the prompt will be too. Push back on task definitions like "assistant that helps with customer emails" — get to "draft a response to a customer email where [X] such that [Y]."
8. **Non-negotiables can themselves be wrong.** Name any non-negotiable that seems to conflict with the task — don't silently route around it.

---

## Output Format

```markdown
## Task
[One paragraph, from input.]

## Audience of the output
[One line.]

## Governing principles (3–7)
1. [Principle — answers what decision.]
2. [...]

## Rules (ranked)
1. **[Rule — positive action].** Overrides default: [default the model would otherwise execute, if any]. Test: [how to check compliance on a single output].
2. [...]

## Non-negotiables
- [Item] (from user input — preserved verbatim).

## Output contract
- Format: [...]
- Length bounds: [...]
- Must appear: [...]
- Must never appear: [...]
- If insufficient information: [ask | flag | proceed with assumption] — [which and why].

## Conflict-resolution policy
When rules conflict: higher-ranked wins. When same-rank rules conflict: [surface | conservative | closer-to-task].

## Self-check (appended to the prompt)
Before emitting:
- [Check line 1]
- [Check line 2]

## Revision trigger (recurring prompts only)
Revise when: [specific signal].

---

## System prompt (ready to paste)

```
[The full composed prompt, ordered: role/task → rules in rank order → output contract → conflict policy → self-check → revision trigger.]
```

## Predicted behavior on representative inputs
- **Easy input:** [brief description]. Expected output: [one-line sketch].
- **Hard input:** [brief description]. Expected output: [one-line sketch].

If actual outputs drift from these, a rule is probably at the wrong rank or missing an override.
```

---

## Verification

- [ ] Task is defined as a job, not a label.
- [ ] 3–7 principles, each answering a real decision.
- [ ] One operational rule per principle, each testable.
- [ ] Rules are ranked.
- [ ] Non-negotiables are user-supplied and preserved verbatim.
- [ ] Output contract is specified.
- [ ] Conflict-resolution policy is explicit.
- [ ] Self-check lines are short.
- [ ] Revision trigger present if recurring.
- [ ] Two representative-input predictions are stated.
