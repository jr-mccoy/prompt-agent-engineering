---
title: "Decompose a Task Across Orthogonal AI-Difficulty Axes"
category: prompt-engineering/evaluation
description: "Given a candidate task for AI, score it across orthogonal axes that actually predict AI difficulty — specification clarity, context payload, tool availability, reversibility, stakes, verification cost, ambiguity of correctness, and horizon — so the user can decide whether the task is AI-shaped, and if so, which axis is the bottleneck."
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
  - decomposition
  - ai-fit
  - orthogonal-axes
  - task-assessment
updated: "2026-04-20"
related_prompts:
  - domain-prompt-engineering/evaluation/taskdifficulty_workflow_axis_optimizer.md
  - domain-prompt-engineering/evaluation/taskdifficulty_calibrated_comparison.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_agent_task_first_delegation_spec.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_agent_task_code_distance_scorer.md
  - domain-prompt-engineering/delegation/delegation_tool_vs_colleague_decision.md
---

# Decompose a Task Across Orthogonal AI-Difficulty Axes

**Objective:** Given a candidate task — one the user is considering delegating to AI — produce a multi-axis difficulty profile that names which specific dimensions make the task hard for AI, not a single "difficulty score." The output tells the user (a) whether the task is AI-shaped at all, and (b) if yes, which axis is the bottleneck that will determine success or failure. A task with a 9/10 difficulty on one axis and 2/10 on all others has a completely different intervention from a task with 5/10 across eight axes.

**When to use:** Before delegating a non-trivial task to AI. Especially useful when the user can feel a task is "hard for AI" but can't say why, or when two candidate tasks that feel similar behave wildly differently when delegated.

**Audience:** Developers and prompt engineers evaluating whether a task is right-shaped for AI delegation. Also useful for individuals deciding which tasks to push to AI first.

---

## The Eight Axes

The axes below are the ones that empirically produce AI failure when any one of them is weak, independent of the others. Tasks fail on whichever axis is weakest.

| Axis | What "hard" looks like on this axis | What "easy" looks like |
|---|---|---|
| **Specification clarity** | Done is fuzzy; criteria are subjective; no pass/fail test | Done is observable and testable by a stranger |
| **Context payload** | Task needs large, scattered, or non-textual context to be done right | Task fits in a small prompt or a single attached file |
| **Tool availability** | Task requires tools the agent doesn't have, or integrations the user hasn't wired | Task can be done with tools already available |
| **Reversibility** | Outcome is hard to undo (prod deployment, sent email, committed contract) | Outcome is a draft the user reviews before any effect |
| **Stakes** | Wrong output costs money, trust, safety, or legal exposure | Wrong output costs a few minutes of redo |
| **Verification cost** | Checking whether the output is correct is expensive — requires expert review, running expensive operations, waiting | Correctness is cheap to check — glance-pass |
| **Ambiguity of correctness** | "Correct" depends on context, taste, or things the user hasn't decided yet | Correctness is single-valued and determined by the output alone |
| **Horizon** | Task requires maintaining state over many steps, long time, or across sessions | Task is one-shot, short, and stateless |

The axes are not fully independent — high stakes often correlate with high verification cost — but they are distinct enough that a task can be high on one and low on all others. That profile predicts what will break.

---

## Inputs Required

1. **The candidate task.** Named specifically — not "a research task" but "a 2-page competitive brief on vendor X for the board meeting on Friday."
2. **Who acts on the output** (user themselves, teammate, automated downstream system, customer).
3. **Whether the task has been done before** by a human. If yes, how long did it take; if not, how does the user know what good looks like.
4. **The user's rough prior on which axes worry them.** Not required, but informative — compare the decomposition to the prior.

Refuse to decompose on a task the user can't name at the outcome level. Generic task types ("research," "draft," "analyze") don't have stable axis profiles; they inherit them from the specific task. Also refuse on hypothetical tasks — the decomposition's value is grounded in a real upcoming job, not an exercise.

---

## Instructions

### Step 1 — Score each axis 0–3

For each of the eight axes, give a score:
- **0:** Not a concern for this task.
- **1:** Mild concern; probably manageable.
- **2:** Real concern; will shape the approach.
- **3:** Likely bottleneck; will determine success or failure.

Require one-line evidence for any 2 or 3. "Specification clarity: 3 — the user hasn't decided what done looks like, and the downstream audience expects something specific."

### Step 2 — Identify the dominant axis

The axis with the highest score is the bottleneck. If multiple axes tie at 3, the task is AI-unshaped as stated — too many things are simultaneously hard. Route the user to split the task before delegating.

If no axis is 3 and the max is 2, the task is probably AI-shaped but needs care on the 2s.

If all axes are 0 or 1, the task is probably AI-shaped and the user is overthinking. Proceed.

### Step 3 — Generate interventions by dominant axis

For each axis, there's a canonical intervention when it's the bottleneck:

- **Specification clarity = 3:** Before delegating, run `domain-prompt-engineering/skill-development/promptcraft_specification_defines_done.md`. Don't delegate without a spec.
- **Context payload = 3:** Attach, don't describe. If the context is too large to attach, the task needs decomposition. Consider `promptcraft_personal_context_document.md`.
- **Tool availability = 3:** Either wire the tool first or stop. Don't delegate to an agent missing the tools it needs — it will confidently improvise.
- **Reversibility = 3:** Require a review gate before any output takes effect. Default output to "draft for review," not "apply."
- **Stakes = 3:** Escalation triggers are mandatory. Pair with `goalorientation_constraint_architecture_workshop.md`. Route any output touching regulated surfaces through a human.
- **Verification cost = 3:** Build an eval harness (`promptcraft_eval_harness.md`) or accept that quality will drift silently.
- **Ambiguity of correctness = 3:** The task isn't yet AI-shaped. Resolve the ambiguity first — run `goalorientation_right_problem_diagnostic.md` or talk to the stakeholder whose definition matters.
- **Horizon = 3:** Multi-step horizon tasks need agent-work-loop design (`ai_pattern_agent_work_loop_design.md`) and checkpoint design. Don't run them as one prompt.

### Step 4 — Look at the pattern across all axes, not just the max

Two common patterns to flag:

- **Stakes + Reversibility both ≥ 2.** High-consequence, hard-to-undo output. Requires a human review gate regardless of other scores. This pattern causes more real-world AI damage than any other.
- **Verification cost + Ambiguity of correctness both ≥ 2.** Hard to check and hard to define what's right. The user will accept outputs that look plausible and not know they're wrong. This is the silent-failure profile. Recommend escalating to an eval harness or a different human-review workflow before delegating.

### Step 5 — Compare decomposition to user's prior

If the user supplied a prior, show where the decomposition agrees and where it diverges. Divergences are findings: the user thought specification was fine but decomposition scored it at 3 — that's a calibration signal as much as a task assessment.

### Step 6 — Produce the decision

One of three outputs:
- **Proceed.** Max score ≤ 2, no worrying pattern across axes. Name the 2s as things to handle in the prompt.
- **Proceed with changes.** Max is 3 on a single axis. Apply the canonical intervention for that axis; rescore after the intervention.
- **Not yet AI-shaped.** Multiple 3s or a silent-failure pattern. Decompose the task, resolve ambiguities, or don't delegate this one.

### Step 7 — Record the decomposition

Save the axis profile. When the task runs (or doesn't) and the outcome is known, come back and compare predicted bottleneck to actual failure mode. This is the feedback loop that calibrates the user's task-assessment instinct over time.

---

## Constraints

### Must
- Score all eight axes, even if some are obviously 0.
- Require one-line evidence for any score of 2 or 3.
- Identify a dominant axis (or declare the task AI-unshaped if tied at 3).
- Name the canonical intervention for any 3.
- Flag the silent-failure pattern (verification cost + ambiguity both ≥ 2) explicitly.
- Return one of the three outcomes (proceed / proceed with changes / not yet AI-shaped).

### Must Not
- Produce a single aggregate "difficulty score." The axes are the point.
- Decompose on hypothetical or generic tasks.
- Skip the pattern check — max-axis view misses the silent-failure profile.
- Recommend "just try it" when reversibility or stakes are ≥ 2.
- Score aspirationally ("the spec will be clearer once I start"). Score against current reality.

---

## False-Positive Prevention

1. **Confidence as evidence.** "I'm sure the spec is clear" without observable criteria is a spec clarity of 2, not 0. Require evidence, not confidence.
2. **Undersized context payload.** Users systematically underestimate context. If the task references "the codebase," "the project," "the last meeting" — that's context, and the payload is not small unless the model can actually see all of it in one shot.
3. **Ignoring horizon.** Multi-session tasks get scored as one-shot because the user mentally collapses them. "First AI drafts; I review; AI revises; I ship" is 4 steps with 2 human interventions — not 1.
4. **Collapsing stakes and reversibility.** They correlate but aren't the same. A task can be low stakes but irreversible (a sent casual email) or high stakes but reversible (a draft proposal before review). Score separately.
5. **Verification cost ignored when the output is short.** Short outputs can still be expensive to verify (short legal advice, short medical claim). Length is not a proxy for verification cost.
6. **Ambiguity of correctness masked by taste.** "I'll know it when I see it" is ambiguity of correctness = 3. Taste is not a correctness criterion.
7. **One bad axis treated as a minor issue.** If any single axis is 3, the task has an open bottleneck that will dominate. Don't average axes; they're not comparable.
8. **Running this as a habit on trivial tasks.** This prompt is for non-trivial tasks. On simple lookups, skip it. Using it everywhere dilutes its signal.

---

## Output Format

```markdown
## Task
[Named specifically.]

## Who acts on the output
[User / teammate / automated system / customer]

## Precedent
- Done before by a human? [Y/N — if Y, how long]
- Definition of good comes from? [user / stakeholder / spec / taste]

## Axis scores (0–3)
| Axis | Score | Evidence (required if ≥2) |
|---|---|---|
| Specification clarity | [0–3] | [...] |
| Context payload | [0–3] | [...] |
| Tool availability | [0–3] | [...] |
| Reversibility | [0–3] | [...] |
| Stakes | [0–3] | [...] |
| Verification cost | [0–3] | [...] |
| Ambiguity of correctness | [0–3] | [...] |
| Horizon | [0–3] | [...] |

## Dominant axis
[Name + score.]

## Pattern flags
- Stakes + Reversibility both ≥ 2: [yes / no + note]
- Verification cost + Ambiguity both ≥ 2 (silent-failure profile): [yes / no + note]

## Prior comparison (if supplied)
- User's prior: [...]
- Decomposition: [...]
- Divergence / agreement: [...]

## Canonical interventions for any 3
- [Axis]: [specific intervention, with prompt path]

## Decision
[ Proceed / Proceed with changes / Not yet AI-shaped ]
Reason: [one sentence]

## Next step
[Specific action with path / deadline]

## Follow-up
After the task runs (or doesn't), compare predicted bottleneck to
actual failure mode. Record in a task-assessment log to calibrate
future scoring.
```

---

## Verification

- [ ] All eight axes scored.
- [ ] Every 2 or 3 has evidence.
- [ ] Dominant axis named (or task declared AI-unshaped if tied at 3).
- [ ] Pattern flags checked (stakes+reversibility, verification+ambiguity).
- [ ] Canonical intervention named for any 3.
- [ ] One of three decisions returned, with reason.
- [ ] A follow-up step is named.
