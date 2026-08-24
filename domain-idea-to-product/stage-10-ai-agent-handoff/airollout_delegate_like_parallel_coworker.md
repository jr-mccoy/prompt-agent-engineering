---
title: "Delegate to AI the Way You'd Delegate to a Parallel Coworker"
category: engineering-workflows/ai-native-rollouts
description: "Design an AI delegation practice that borrows from how competent managers delegate to a parallel coworker: written brief, clear acceptance criteria, checkpoints, and a handback point. Produces a per-task delegation template the engineer can reuse, tuned to their actual task shape."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-01
  - RT-11
  - QA-01
difficulty: intermediate
tags:
  - ai-native-rollouts
  - delegation
  - brief
  - acceptance-criteria
  - handback
updated: "2026-04-21"
related_prompts:
  - domain-engineering-workflows/ai-native-rollouts/airollout_ship_without_writing_code.md
  - domain-engineering-workflows/ai-native-rollouts/airollout_long_running_project_memory.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_agent_task_first_delegation_spec.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_intent_and_verification_first.md
  - domain-business-strategy/chief-of-staff/cos_specify_subagent_task.md
---

# Delegate to AI the Way You'd Delegate to a Parallel Coworker

**Purpose:** Most AI delegation fails not because the AI is bad but because the delegation is worse than what the user would hand a human coworker. This prompt produces a reusable delegation brief template calibrated to the user's actual task shape — with the elements a competent manager would include when handing a task to a parallel human peer: brief, acceptance criteria, checkpoints, handback signal, and escalation.

**When to use:**
- The user is delegating knowledge work to AI (code, analysis, research, writing, planning) and keeps getting "80% right but 20% wrong in surprising ways" output.
- A team is standardizing AI delegation practice and needs a template the whole team uses.
- An engineer is moving toward higher-leverage AI use (from IDE autocomplete to task delegation) and needs the brief format.

**Don't use when:** The task is a single-turn autocomplete or a one-line question. Delegation overhead isn't worth it.

**Audience:** Individual IC or manager delegating to AI. Output is a reusable template they customize per task class.

---

## Inputs Required

1. **The class of tasks being delegated.** Examples: "bug fix PRs," "weekly competitive briefs," "data-extraction from customer transcripts," "legal contract redlines at a certain clause level." One class per run; different classes get different templates.
2. **A concrete recent example.** One actual task in this class the user recently did (or tried to delegate).
3. **What "done" looked like for that task.** The artifact, the state, or the decision produced.
4. **Where AI delegation has failed for this class before.** 1–3 specific failures: wrong scope, hallucinated detail, unclear output, subtle error, etc.
5. **Acceptance authority.** Who accepts the AI's output — the user directly, a reviewer, a downstream consumer? This changes the handback format.
6. **Escalation path.** When the AI is stuck, what the user wants to happen: paused / asked a specific clarifying question / handed back with state / routed to a different model.

---

## Instructions

### Step 1 — Mirror the coworker test

Write one paragraph: if you handed this task to a competent, unfamiliar peer engineer/analyst/writer, what would your written brief to them include? If the answer is "I wouldn't write a brief — I'd just talk to them," that's fine — force it into writing now, because AI requires the written form a peer gets away without.

### Step 2 — Build the delegation brief template

The template has 7 sections. Each section is required; omit nothing.

#### 2.1 Context (2–5 sentences)
What the task is part of, why it matters now, what has already been done, what the downstream consumer will do with the output. A peer would need this; the AI needs it more.

#### 2.2 Task, stated as an outcome
Not "write the function that does X" — "the system should behave such that Y, verifiable by Z." If the class of tasks has a typical outcome form, state it as the template default.

#### 2.3 Acceptance criteria (3–6 bullets)
Observable, testable, or reviewable. Each bullet is specific enough that the AI cannot return "done" without the criterion being met.

#### 2.4 Out-of-scope (explicit)
What NOT to do. A peer would infer this; the AI will often do it if not told not to. Common items: don't touch neighboring files, don't change tests unless asked, don't restructure, don't add dependencies.

#### 2.5 Checkpoints (1–3)
When the AI should pause and report back before continuing. For a multi-step task, checkpoints prevent long wrong-direction runs. For a short task, 1 checkpoint after the plan is enough.

#### 2.6 Handback format
What the AI returns when done: diff only, diff + explanation, written summary, filled-in table, etc. Tied to acceptance authority (input 5) — if a reviewer will gate, the handback must make review efficient.

#### 2.7 Escalation
What the AI does when it hits ambiguity, missing input, or a failure it can't resolve. Tied to input 6. Common patterns: ask a specific clarifying question and wait; emit a structured "I'm stuck because X, need Y" block; stop and hand back current state.

### Step 3 — Pre-fill the template using the concrete example (input 2)

Do NOT leave the template abstract. Fill in the Context, Task, Acceptance, Out-of-scope, Checkpoints, Handback, and Escalation using the user's actual recent task. The user then sees a working example that proves the template is usable.

### Step 4 — Address the prior failure modes (input 4)

For each of the 1–3 failures the user described, name which section of the brief would have prevented it:

- Scope creep → Out-of-scope + Checkpoints.
- Hallucinated detail → Acceptance criteria that require evidence.
- Unclear output → Handback format.
- Subtle error → Acceptance criteria + Checkpoints + escalation.

If a failure isn't prevented by any section, revise the template — add or expand a section until it is.

### Step 5 — Write the reuse rules

The template is meant to be reused. Specify:

- **What changes per task:** Context, Task, Acceptance (always; these are task-specific).
- **What stays constant across tasks in the class:** Out-of-scope, Handback format, Escalation (template-level defaults).
- **Where the template lives.** Committed to a repo, saved as a snippet, pinned in a doc. Be concrete.
- **How it gets updated.** When a new failure mode appears, the template gets a new line; assign who owns updates.

### Step 6 — Stop pattern if delegation is wrong-shaped

If during step 3 you realize the task can't be briefed tightly (the problem is ill-defined; the user doesn't know what "done" looks like yet), call that out. Don't force the template. The task needs scoping work first — point at `domain-prompt-engineering/evaluation/correctness_discovery_prompt.md` or similar.

### Step 7 — Verify and output

Run the verification checklist.

---

## Constraints

### Must
- Produce a brief that mirrors what a manager would write for a human peer.
- Fill in the template with the user's concrete example — no abstract templates.
- Address every prior failure mode in input 4 via a specific section.
- Separate per-task fields from template-constant fields.
- Define where the template lives and who updates it.

### Must Not
- Produce a template without an escalation path. Ambiguous tasks with no escalation cause silent wrong answers.
- Skip acceptance criteria. "Use your judgment" is not delegation.
- Collapse Context and Task. Context is why; Task is what. The AI uses both.
- Let handback be "just give me the answer" for non-trivial tasks — the handback format should enable efficient review.
- Let the template grow past ~1 page. Longer templates go unused.

---

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Let the brief substitute for thinking. Writing a good brief is part of the work.
- Make acceptance criteria vague ("quality is high," "the code is clean"). Every criterion should fail or pass by inspection.
- Tell the AI to "do what you think is best." That's abdication, not delegation.
- Copy a template from another task class verbatim. Per-class tuning matters.
- Treat a first-time template as final. The second task reveals gaps.

✅ **DO:**
- Write out-of-scope in negative form; the AI pattern-matches on negatives weakly, so be specific ("do not modify tests/" not "only modify the production code").
- Tie each acceptance criterion to something observable: a test name, a file state, a specific output field, a specific sentence.
- Treat escalation as a feature, not a bug — a brief that invites escalation gets better output.
- Version the template. When you update it, note why.
- Pair the brief with the project memory scaffold (`cos_memory_scaffold_claude_md.md`) so shared context isn't re-briefed each time.

---

## Dual-Failure Prevention (QA-20)

❌ **HARMFUL failure:** Brief is so tight it forces AI to produce a wrong answer rather than escalate — AI complies, user ships broken work.

❌ **UNHELPFUL failure:** Brief is so loose the AI produces generic output; user concludes delegation doesn't work for this class.

✅ **Quality check:** A colleague reading the brief for a task they've never seen could either (a) produce an acceptable answer or (b) articulate, specifically, what they still need to know.

---

## Output Format

```markdown
# AI Delegation Template — [Task Class]

## Template (per-task filled example)

### Context
[2–5 sentences. Filled for the user's concrete example.]

### Task (as outcome)
[Outcome-form statement with verifiable Y and Z.]

### Acceptance Criteria
- [ ] [Specific, observable]
- [ ] [Specific, observable]
- [ ] […]

### Out of Scope
- [Specific don't-do item]
- [Specific don't-do item]

### Checkpoints
1. [When / what to report back]
2. [If applicable]

### Handback Format
[Diff only / diff + explanation / structured summary / filled table]

### Escalation
- On ambiguity: [specific action]
- On stuck: [specific action]
- On failure: [specific artifact to emit]

---

## Failure Mode → Template Section Coverage
| Prior failure (input 4) | Prevented by section |
|--------------------------|----------------------|
| [failure 1] | [section + how] |
| [failure 2] | [section + how] |

## Reuse Rules
- Per-task fields: Context, Task, Acceptance
- Template-constant fields: Out-of-scope, Handback, Escalation
- Template lives at: [path / tool]
- Owner + update cadence: [who, when]

## Stop Pattern
- If a future task can't be briefed tightly, re-scope via [named prompt] before delegating.
```

---

## Verification

- [ ] Template has all 7 sections.
- [ ] Example is fully filled in; no abstract placeholders remain.
- [ ] Every prior failure mode is addressed by a named section.
- [ ] Per-task vs template-constant fields separated.
- [ ] Escalation path defined.
- [ ] Template is ≤ ~1 page; redundant sections trimmed.
- [ ] Storage location and owner specified.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Output is a reusable delegation template, not a delegation philosophy.
- **ST-02 (Structured Sequential Instructions):** Seven steps force coworker-test → template build → concrete fill → failure-mode coverage → reuse rules → stop pattern → verify.
- **CM-02 (Constraint Specification):** Must Not block forbids abdication phrases and loose acceptance.
- **DS-01 (Framework Application):** Seven-section brief template is the framework; per-task vs constant separation keeps it tractable.
- **RT-11 (Error Recovery):** Explicit escalation section as a first-class template field handles ambiguity and stuck states.
- **QA-01 (Self-Verification):** Failure-mode coverage table is the verification that the template actually addresses prior problems.
