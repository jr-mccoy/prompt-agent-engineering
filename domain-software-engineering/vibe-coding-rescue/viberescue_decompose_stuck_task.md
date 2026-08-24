---
title: "Decompose a Stuck Task Into Agent-Sized Subtasks"
category: software-engineering/vibe-coding-rescue
description: "When an AI keeps failing at the same coding task across multiple attempts, decompose it into subtasks that fit an agent's per-turn capacity — each with its own spec, acceptance, and verification — rather than retrying the whole task with more prompt engineering."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-01
  - RT-07
  - RT-11
  - QA-01
difficulty: intermediate
tags:
  - vibe-coding
  - task-decomposition
  - agent-sizing
  - spec
  - verification
updated: "2026-04-21"
related_prompts:
  - domain-software-engineering/vibe-coding-rescue/viberescue_wall_diagnosis.md
  - domain-software-engineering/vibe-coding-rescue/viberescue_rules_file_design.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_agent_task_first_delegation_spec.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_agent_task_code_distance_scorer.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_agent_work_loop_design.md
  - domain-engineering-workflows/ai-native-rollouts/airollout_delegate_like_parallel_coworker.md
---

# Decompose a Stuck Task Into Agent-Sized Subtasks

**Purpose:** When an AI has tried the same coding task 3+ times and failed — output compiles but is wrong, passes tests the AI wrote but fails the ones you ask for, or gets partially done then thrashes — the usual fix isn't a better prompt. The task is too big for one turn or one session. This prompt decomposes the stuck task into subtasks sized for the agent's actual capacity, each with its own spec, acceptance, and verification. The output is a dependency-ordered subtask list, not a new attempt at the original prompt.

**When to use:**
- AI has failed at a specific task 3+ times; each retry looks similar.
- Diagnosis (`viberescue_wall_diagnosis.md`) returned Mode 9 (task too big for the loop).
- A task mixes multiple concerns (data model change + API change + migration + tests) and the AI keeps doing 2 of 4.
- A user is about to hand a task to an agent and wants to size it properly before kickoff.

**Don't use when:** The task is small and the AI just produced a small bug. Debug, don't decompose.

**Audience:** The engineer delegating to AI. Output is a subtask list they can execute sequentially.

---

## Inputs Required

1. **The original task description.** As currently written; paste the prompt or instruction the user has been giving.
2. **The 2–3 recent failed attempts.** For each: what the AI produced, what specifically was wrong, how the user ended the attempt.
3. **The repo context.** Language, framework, which files the task touches (or is expected to touch), test runner.
4. **The user's current rules file.** If one exists, cite it; if not, note.
5. **The AI tool being used.** Determines per-turn context window and tool access.
6. **The single observable "done" criterion for the whole original task.** If the user can't state it in one sentence, that's itself a clue — lack of a "done" criterion is often why decomposition is needed.

---

## Instructions

### Step 1 — Restate the original task as a concrete outcome

One sentence. What state does the codebase need to be in when done? If the user's original prompt was action-shaped ("do X and Y and then Z"), convert to outcome-shaped ("the system's behavior is [Y] verifiable by [specific test or command]").

If no outcome can be written, STOP decomposition. The task needs a spec first (see `ai_pattern_agent_task_first_delegation_spec.md`).

### Step 2 — Identify the concerns the task actually mixes

List every concern the task touches. Use this checklist as a prompt:

- Data model / schema changes
- Migration / backfill
- API / interface change (breaking?)
- Business-logic change
- UI change
- Config / environment change
- Test changes (separate from production code changes)
- Documentation
- Dependency additions
- Security-sensitive code (auth, crypto, permissions)
- External side effects (emails, webhooks, payments)

A task that touches > 3 concerns is a strong decomposition candidate. One that touches ≥ 5 is definitely too big for an agent-turn without structure.

### Step 3 — Determine the right subtask size

Subtasks should be:

- **Single-concern** where possible (one concern per subtask from step 2).
- **Small enough to fit in one agent turn + one review** (typical: touches 1–3 files, changes ≤ ~100 LOC including tests).
- **Independently verifiable** — the subtask passes or fails its own acceptance on its own, without needing downstream subtasks done.
- **Non-breaking when merged on its own** — if the user stops after subtask N, the code is in a valid state.

If any subtask violates the "non-breaking alone" rule, reorder or refactor until each landed subtask leaves the code working.

### Step 4 — Generate the subtask list

Produce 3–8 subtasks. More than 8 and the user loses coordination; fewer than 3 and the original wasn't actually too big. Each subtask has:

- **Name.** Short, descriptive.
- **Outcome.** What state the code reaches when this subtask is done.
- **Spec.** What the AI is told in one paragraph.
- **Acceptance criteria.** 2–4 bullets; observable.
- **Tests to add or update.** Named.
- **Files expected to be touched.** With an "out of scope" note for anything the AI should NOT touch in this subtask.
- **Estimated agent turns.** 1 ideal; 2–3 max.

### Step 5 — Order the subtasks by dependency

Draw the dependency graph in prose. Rules:

- Every subtask's inputs (files, interfaces, schema) are produced or unchanged by an earlier subtask or were present before.
- Migrations land before code that depends on the new schema state.
- Tests for new behavior can land as part of the subtask that introduces the behavior, NOT separately (it's one of the most common decomposition errors).
- A subtask that enables feature-flagged code can land before the user-visible change.

Output the final ordering. Cycles mean the decomposition is wrong — redo.

### Step 6 — For each subtask, flag handoff points

Between subtasks, the user (or another reviewer) must:

- Review the subtask's change.
- Run the subtask's tests.
- Confirm the "done" state before starting the next.

Name the reviewer for each (often the user themselves). This prevents serial agent failures where subtask 3 builds on a flawed subtask 2.

### Step 7 — Run failure-mode coverage

For each failure from input 2, identify which subtask would have caught or constrained it:

- If the AI was producing too much at once → size of subtask addresses.
- If the AI was hallucinating file locations → subtask's named file list constrains.
- If tests the AI wrote were self-confirming → subtask's acceptance specifies tests the USER defines.
- If the AI kept changing unrelated files → out-of-scope note in each subtask.

If a failure isn't addressed, revise the decomposition.

### Step 8 — Produce the integration check

After all subtasks land, the original outcome from step 1 must hold. Name the specific test or behavioral check that confirms the whole task is done (not just the last subtask). This is often a test that couldn't meaningfully exist until after subtask N but that ties the work together.

### Step 9 — Handle "this task shouldn't be done by the AI" honestly

Sometimes the failure mode is: the task requires a decision or piece of context the AI doesn't have, and no decomposition fixes that. Call it out:

- If the task needs a design decision the user hasn't made → decompose the decision-making separately; the AI can only execute after.
- If the task needs external input (API docs, customer data, prior code history) the AI can't see → the first subtask is "surface and capture that input," possibly a human task.
- If the task is security-sensitive beyond what delegated work should do → remove from agent scope entirely.

Don't decompose a task into subtasks that still have the same blocker.

### Step 10 — Verify and output

Run the verification checklist.

---

## Constraints

### Must
- Restate the original task as an outcome before decomposing.
- Identify mixed concerns explicitly.
- Produce 3–8 subtasks, each single-concern where possible.
- Every subtask has outcome, spec, acceptance, tests, files, out-of-scope, turn estimate.
- Order subtasks by dependency; each landable standalone.
- Include an integration check after all subtasks.

### Must Not
- Produce a subtask that can't be merged alone without breaking the code.
- Separate tests into their own subtask from the behavior they cover.
- Exceed 8 subtasks (if the task genuinely needs more, it's an architectural change — flag for human).
- Decompose past the point where each subtask is single-turn-feasible.
- Hide required human decisions inside a subtask.
- Use vague acceptance criteria. Each subtask's acceptance is pass/fail by inspection.

---

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Decompose by file ("one subtask per file touched"). File-based decomposition breaks the "single concern" rule; one file can carry multiple concerns and often does.
- Create a "setup subtask" that's just scaffolding. If there's real setup work, name it; if it's just "make the AI think about it," drop it.
- Let subtask 1 be "understand the codebase." That's not a subtask; it's a prerequisite handled by rules-file / memory.
- Treat test-writing as a trailing subtask. Tests land with the behavior they cover.
- Claim single-turn feasibility for a subtask whose file list spans > 3 files without strong structural coupling.

✅ **DO:**
- For each subtask, imagine handing it to a mid-level engineer who has the rules file. Would they know what to do? If yes, the agent probably can too.
- Add a "canary" check to each subtask's acceptance: one behavior observable BEFORE and AFTER the change to confirm the change is active.
- If the same concern keeps wanting to span multiple subtasks, consolidate — over-decomposition is as bad as under-decomposition.
- Name which subtasks are feature-flag gated vs user-visible; this affects rollout.
- Acknowledge when the original task genuinely doesn't decompose — that's evidence the project needs an architecture change or a human in the loop, not more prompting.

---

## Dual-Failure Prevention (QA-20)

❌ **HARMFUL failure:** Decomposition produces subtasks that land individually but compose to a broken state because a dependency was missed. User merges each, then at subtask 5 finds the whole flow is wrong.

❌ **UNHELPFUL failure:** Decomposition produces 12 micro-subtasks that each require more ceremony than the change itself. User abandons the framework.

✅ **Quality check:** A senior engineer would agree each subtask is single-turn-feasible, the ordering makes sense, and the integration check ties it together.

---

## Output Format

```markdown
# Stuck-Task Decomposition — [Original Task]

## Original Task Restated as Outcome
[One-sentence desired state + verification.]

## Mixed Concerns
- [List from step 2; note total concern count.]

## Subtasks (in dependency order)
### Subtask 1: [Name]
- **Outcome:** 
- **Spec:** 
- **Acceptance:**
  - [ ] 
  - [ ] 
- **Tests to add/update:** 
- **Files touched:** 
- **Out of scope:** 
- **Estimated turns:** 
- **Reviewer:** 

### Subtask 2: …

## Dependency Graph
[Prose description of ordering + why.]

## Failure-Mode Coverage
| Prior failure (input 2) | Subtask that prevents it | How |
|-------------------------|--------------------------|-----|
| | | |

## Integration Check
[Test or behavioral verification that confirms the whole original outcome.]

## Honest-Out
- [Subtasks that cannot be AI-delegated and why, if any.]
- [Human decisions required upstream, if any.]
```

---

## Verification

- [ ] Original task restated as outcome, not action list.
- [ ] Concerns enumerated; decomposition tied to concerns.
- [ ] 3–8 subtasks, each single-concern where possible.
- [ ] Each subtask lands independently without breaking code.
- [ ] Tests co-land with the behavior they cover (not separated).
- [ ] Dependency graph acyclic.
- [ ] Every prior failure (input 2) is covered by a specific subtask mechanism.
- [ ] Integration check defined.
- [ ] Human-only subtasks or decisions named honestly.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Output is a dependency-ordered subtask plan, not a better prompt.
- **ST-02 (Structured Sequential Instructions):** Ten steps restate → concerns → size → list → order → handoffs → failure coverage → integration → honest-out → verify.
- **CM-02 (Constraint Specification):** Must Not block forbids test/code separation, file-based decomposition, and sub-tasks that require their downstream to land first.
- **DS-01 (Framework Application):** Mixed-concerns checklist + subtask-size rules are the framework.
- **RT-07 (Cascade Effect Analysis):** Failure-mode coverage table catches the cascade where each subtask passes locally but they compose to broken state.
- **RT-11 (Error Recovery):** Honest-out step (step 9) handles the case where decomposition doesn't work and escalates properly rather than silently retrying.
- **QA-01 (Self-Verification):** Verification checklist + integration check validate the decomposition before the user starts executing it.
