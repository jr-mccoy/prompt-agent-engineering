---
title: "Workshop for Building Constraints, Escalation Triggers, and a Value Hierarchy for Any AI Task"
category: prompt-engineering/goal-orientation
description: "Structured session that produces three artifacts for an AI task before the model runs: the constraints the output must respect, the triggers that escalate the task out of AI back to a human, and the value hierarchy that tells the model which goal wins when goals conflict — so the user doesn't discover missing constraints in review."
techniques:
  - ST-01
  - ST-02
  - DS-01
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - goal-orientation
  - constraint-design
  - escalation
  - value-hierarchy
  - task-design
updated: "2026-04-20"
related_prompts:
  - domain-prompt-engineering/goal-orientation/goalorientation_right_problem_diagnostic.md
  - domain-prompt-engineering/goal-orientation/goalorientation_team_ai_misalignment_map.md
  - domain-prompt-engineering/delegation/delegation_intent_specification.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_intent_and_verification_first.md
---

# Workshop for Building Constraints, Escalation Triggers, and a Value Hierarchy for Any AI Task

**Objective:** Produce three artifacts the user will hand to the model together with the task itself: (1) a constraint set — what the output must respect no matter what; (2) an escalation trigger set — conditions under which the model should stop and hand back to a human; and (3) a value hierarchy — the ranked order the model uses to decide when goals conflict. These three make the difference between an AI workflow that mostly works and one that produces safe, useful output at scale.

**When to use:** You're designing an AI task that will run more than once, or will produce output that others act on, or involves real downside risk if the output is wrong. Applies to coding agents, content generation at scale, decision-support tools, customer-facing generation, and any workflow where a quiet failure is costly.

**Audience:** Individuals and small teams building AI workflows (internal agents, Claude Code setups, custom GPTs, automation pipelines, content generation). For team-wide misalignment risk, pair with `goalorientation_team_ai_misalignment_map.md`.

---

## Inputs Required

1. **Task definition.** The job in one paragraph — what the model is being asked to do.
2. **Outcome.** What changes in the user's world when the task is run successfully.
3. **Who acts on the output.** The user, a teammate, an automated downstream system, a customer — each changes the constraint set.
4. **Known failure modes.** Ways the task has gone wrong before, ways the user worries it could go wrong, or the nearest analogous tasks' failure modes.
5. **Stakes.** Roughly: what does a bad output cost? (Time to fix / trust erosion / revenue / safety / regulatory — name any that apply.)

Refuse to run the workshop on a task that doesn't have at least one identified failure mode. A task with no imaginable failure is either trivial (doesn't need this workshop) or hasn't been thought through enough to know what to constrain. Route the user to `goalorientation_right_problem_diagnostic.md` in the latter case.

---

## Instructions

### Step 1 — Build the constraint set

Constraints are what must be true of the output, independent of the task's goals. Work through these categories; name the specific constraint for any that apply, leave blank for any that don't.

- **Legal / compliance.** Regulatory, jurisdictional, licensing. Verbatim where relevant.
- **Factual.** Accuracy bars — claims that must be sourced, numbers that must match, names that must not be invented.
- **Safety.** What the output must never do or recommend.
- **Format.** Downstream-system requirements: JSON schema, markdown structure, length caps, file type.
- **Stylistic.** Voice, reading level, house-style rules that are non-negotiable (versus the preferences that go in CLAUDE.md).
- **Scope.** What the output must not include — topics, recommendations, data that are out of bounds.
- **Privacy.** PII, credentials, confidential material.

For each constraint, state it as a sentence the model could check its draft against. "Don't include PII" is weaker than "Don't include any string matching a name, email, phone number, or address pattern."

### Step 2 — Build the escalation trigger set

Escalation triggers are the conditions under which the model should stop and hand off to a human rather than proceed. The goal is to catch the edges of the task where continued automation makes the outcome worse.

Work through the following trigger categories:

- **Ambiguity triggers.** The model doesn't have enough information to proceed without guessing. ("If a required field is missing and cannot be inferred from context, stop.")
- **Confidence triggers.** The model's own confidence in the answer is below a threshold. ("If you would attach 'I'm not sure' to the output, stop and ask.")
- **Consequence triggers.** The output would have effects the user wants a human to vet. ("If the recommendation involves firing, terminating, or communicating with a customer in crisis, stop.")
- **Domain-boundary triggers.** The task has drifted outside the domain the model should operate in. ("If the user asks for medical advice beyond information already in public guidelines, stop.")
- **Constraint-conflict triggers.** Two constraints conflict and resolving requires a human judgment call.
- **Novelty triggers.** The situation differs materially from the cases the workflow was designed for.

Each trigger should state: **condition → action**. The action is usually "stop and route to [specific human / team]" plus "emit a message in format X so the human knows what's blocking."

Escalation triggers without explicit handoff routes degrade into the model continuing anyway.

### Step 3 — Build the value hierarchy

When two legitimate goals conflict, the model needs to know which one wins. Without an explicit hierarchy, the model averages or silently picks — and silent picks are where trust breaks.

Structure:
1. List the goals that can plausibly conflict. Typical pairs: speed vs. accuracy, comprehensiveness vs. brevity, being helpful vs. being safe, preserving the user's phrasing vs. fixing it, breadth vs. depth.
2. Rank them for this task. Not in general — for *this* task. The ranking may differ across tasks with the same model.
3. Name the tie-breaker for same-rank goals. Usually either "flag and let the user decide" or "prefer the more conservative choice."

The hierarchy must fit in 3–5 lines at the top of the system prompt. A hierarchy longer than that won't be followed.

### Step 4 — Stress-test the three artifacts

Run each artifact against the known failure modes supplied in inputs:

- **For each failure mode, which constraint would have caught it?** If none, add a constraint or acknowledge the failure mode is not constraint-preventable (a different mitigation is needed).
- **For each failure mode, which escalation trigger would have fired?** If none, add a trigger or accept the gap.
- **For each failure mode, would the value hierarchy have made the right call?** If not, the hierarchy needs adjustment.

This is the stress test that distinguishes a real constraint set from a reasonable-looking one.

### Step 5 — Write the composite header

Produce the block the user appends to the task prompt (or lifts into the system prompt). Structure:

```
Constraints (must respect every output):
- [...]

Escalation triggers (stop and hand off if):
- If [condition] → [action].

Value hierarchy (when goals conflict):
1. [Highest-priority goal]
2. [...]
Tie-breaker: [rule].
```

Keep the block compact. Length is the enemy of adherence.

### Step 6 — Predict the test

State what failure modes the workshop should now prevent and what failure modes it won't. The user should go into the task knowing which risks the artifacts cover and which risks remain on the human.

---

## Constraints

### Must
- Run every category in Step 1 (leave blank if truly none), not just the ones that feel obvious.
- State each constraint as a testable sentence the model can check its draft against.
- Pair every escalation trigger with an explicit handoff route.
- Rank the value hierarchy; do not leave goals unordered.
- Stress-test the artifacts against every supplied failure mode.
- Predict which failure modes remain uncovered.

### Must Not
- Copy a generic constraint list. Constraints must be specific to this task.
- Produce an escalation trigger without a handoff route. "Stop and ask" without specifying who dies in silence.
- Produce a value hierarchy longer than ~5 lines.
- Invent failure modes the user didn't name in order to pad the stress test.
- Treat the workshop output as final for a recurring task without a revision trigger.

---

## False-Positive Prevention

1. **Constraint proliferation erodes constraints.** Past ~10 constraints, the model averages. Cut to the load-bearing ones; move style and preference to CLAUDE.md (see `escapemedian_bootstrap_instruction_file.md`).
2. **Escalation triggers that never fire are dead code.** If a trigger has never fired and the task has run 50 times, consider whether the trigger is real or a reassurance.
3. **Escalation triggers that fire on every run have become task-definition bugs.** The task is scoped wrong, not the triggers.
4. **Value hierarchies are often aspirational.** The user says "accuracy over speed" and then overrides every time the model slows down. Check against actual behavior over the past 3–5 runs. If the hierarchy doesn't match behavior, fix the hierarchy or fix the behavior — don't leave them in conflict.
5. **Generic constraints ("be accurate," "be helpful") aren't constraints.** They're goals. Replace with specific checkable rules.
6. **Over-escalating kills the workflow's leverage.** If every ambiguous moment routes to a human, the workflow is human-in-the-loop with extra steps. Scope triggers so routine-ambiguous cases proceed; only non-routine ones escalate.
7. **Don't assume constraints transfer across tasks.** A constraint set tuned for a content-generation task will be wrong for a decision-support task. Run the workshop per task.
8. **The block at the top of the prompt is not the same as the broader CLAUDE.md.** Constraints here are task-level and load-bearing. General preferences go to the instruction file, not here.

---

## Output Format

```markdown
## Task + outcome
- Task: [...]
- Outcome: [...]
- Who acts on output: [...]
- Stakes: [...]

## Known failure modes (from input)
1. [...]
2. [...]

## Constraints

| Category | Constraint (testable sentence) |
|----------|--------------------------------|
| Legal / compliance | [...] |
| Factual | [...] |
| Safety | [...] |
| Format | [...] |
| Stylistic | [...] |
| Scope | [...] |
| Privacy | [...] |

## Escalation triggers

| Category | Condition | Action (route + message format) |
|----------|-----------|----------------------------------|
| Ambiguity | [...] | stop → [human / team] with message "[...]" |
| Confidence | [...] | [...] |
| Consequence | [...] | [...] |
| Domain-boundary | [...] | [...] |
| Constraint-conflict | [...] | [...] |
| Novelty | [...] | [...] |

## Value hierarchy (for this task)
1. [Highest-priority goal]
2. [...]
3. [...]
Tie-breaker: [rule].

## Stress test against failure modes
| Failure mode | Covered by constraint? | Covered by trigger? | Hierarchy would resolve correctly? |
|--------------|-----------------------|---------------------|------------------------------------|
| [...] | [which] | [which] | [yes / no] |

## Composite header (paste into prompt)

```
Constraints (every output must respect these):
- [...]

Escalation triggers (stop and hand off if):
- If [condition] → [action].

Value hierarchy (when goals conflict):
1. [...]
2. [...]
Tie-breaker: [...].
```

## Uncovered risks
- [Failure mode not addressed by any artifact; on the human to watch.]

## Revision trigger (recurring tasks only)
Revise this workshop output when: [specific signal, e.g., "any new failure mode appears that no constraint or trigger covered"].
```

---

## Verification

- [ ] Task has at least one named failure mode.
- [ ] Every constraint category was considered; applicable ones have testable sentences.
- [ ] Every escalation trigger has an explicit handoff route and message format.
- [ ] Value hierarchy is ranked and ≤5 lines.
- [ ] Stress test run against every supplied failure mode.
- [ ] Uncovered risks are stated explicitly.
- [ ] Composite header fits at the top of a prompt without dominating it.
