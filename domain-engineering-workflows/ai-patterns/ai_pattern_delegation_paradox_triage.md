---
title: "Agent Task Delegation Triage (Collaboration Paradox)"
category: ai-patterns
description: "Triage a set of tasks into delegate-to-agent, co-work, or keep-human using the collaboration-paradox heuristic, then assign each a verification signal and an oversight level so delegation is safe by construction."
techniques:
  - DS-06
  - AG-28
  - RT-02
  - AG-27
  - QA-12
difficulty: intermediate
tags:
  - delegation
  - agentic-coding
  - oversight
  - task-triage
  - collaboration-paradox
updated: "2026-06-19"
related_prompts:
  - domain-engineering-workflows/ai-patterns/ai_pattern_agent_task_first_delegation_spec.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_agent_task_code_distance_scorer.md
  - domain-engineering-workflows/ai-native-rollouts/airollout_delegate_like_parallel_coworker.md
---

# Agent Task Delegation Triage (Collaboration Paradox)

**Objective:** Sort a concrete set of tasks into delegate-to-agent, co-work, or keep-human, and for each delegated task name the verification signal that makes delegation safe and the oversight level it warrants — turning the collaboration paradox (heavy AI use, narrow safe delegation) into a per-task decision rather than a vibe.

**When to Use:**
- You have a backlog or sprint of tasks and need to decide what to hand to an agent versus what to keep.
- Delegation has been ad hoc and you want a repeatable, defensible triage.
- An agent keeps producing plausible-but-wrong output on tasks that should have stayed co-worked.

**When NOT to Use:**
- You have a single already-chosen task and need its delegation spec (use `ai_pattern_agent_task_first_delegation_spec.md`).
- You are estimating one task's distance from existing code (use `ai_pattern_agent_task_code_distance_scorer.md`).

**Source:** Figures are drawn from vendor reports — Anthropic's *2026 Agentic Coding Trends Report* and Anthropic Societal Impacts research — figures attributed inline; no source text reproduced.

## Inputs / Context

Provide what you can; triage degrades gracefully if some are missing:
- **Task list** — the candidate tasks, each with a one-line description.
- **Stakes** — blast radius / reversibility of each task's output.
- **Verifiability** — what signals exist (tests, type checker, build, lint, staging, human spot-check).
- **Context dependence** — how much organizational context, design judgment, or "taste" each task needs.
- **Your competence** — for which tasks you "know what the answer should look like."

## Constraints

**Must:**
- Apply the delegation heuristic explicitly: delegate easily-verifiable, well-defined, repetitive, or low-stakes tasks; keep or co-work conceptually hard, design-dependent, context-heavy, or high-stakes tasks.
- Tie delegation safety to feedback-signal strength — strong signals (tests, type checker, build, lint) enable more autonomy; weak signals require closer oversight.
- Give every task a verdict, an oversight level, and a named verification signal.

**Must Not:**
- Delegate a task whose output cannot be verified by any concrete signal without flagging it for closer oversight.
- Treat "the agent can probably do it" as a reason to delegate when stakes are high and signals are weak.
- Collapse co-work into delegate — co-work means a human stays in the loop on judgment, not just at the end.

**Instructions:**

1. **List the determining factors per task.** For each task, mark: verifiability, definedness, repetitiveness, stakes, context/taste dependence, and whether you know what the right answer looks like.

2. **Apply the collaboration-paradox heuristic.** Delegate when the task is easily verifiable, well-defined, repetitive, or low-stakes. Keep or co-work when it is conceptually hard, design-dependent, requires organizational context or taste, or is high-stakes. The load-bearing insight: practitioners report being most effective delegating "where I know what the answer should look like" — judgment built by doing the work the hard way.

3. **Render the verdict.** Assign delegate-to-agent, co-work, or keep-human. Co-work is the right call when the task is partly delegable but judgment must stay human throughout.

4. **Name the verification signal.** For each delegated or co-worked task, name the specific signal that makes the output checkable: tests, type checker, build, lint, schema validation, staging behavior, or a defined human spot-check. A task with no signal is not safely delegable as-is.

5. **Set the oversight level by signal strength.** Map to: let-it-run (strong automated signals, low stakes), check-milestones (decent signals, moderate stakes), watch-closely (weak signals or rising stakes), or review-every-change (high stakes or no automated signal). Per Anthropic Societal Impacts research, developers use AI across roughly 60% of work yet can fully delegate only 0–20% of tasks — most tasks land in co-work with real oversight, not let-it-run.

6. **Flag signal-deficient tasks for hardening.** Where a worthwhile task lacks a verification signal, recommend adding one (write the test first, add a type, stand up a staging check) so it can move toward delegation later.

**Output Format:**

A markdown triage:
- **Task Triage Table** — Task | Determining factors | Verdict (delegate/co-work/keep) | Verification signal | Oversight level
- **Signal-Hardening Recommendations** — tasks worth promoting once a signal is added
- **Summary** — rough split across the three verdicts and what it implies about realistic delegation depth

## Verification

- [ ] Every task has a verdict, a verification signal (or a flag that none exists), and an oversight level.
- [ ] Oversight level is justified by signal strength and stakes, not by guesswork.
- [ ] High-stakes or weak-signal tasks are not marked let-it-run.
- [ ] Co-work tasks keep a human in the loop on judgment, not only at the end.
- [ ] Signal-deficient but valuable tasks have a hardening recommendation.

## False-Positive Prevention

❌ **DON'T:**
- Delegate a task just because the agent produced something plausible — plausible output with no signal is the paradox's trap.
- Assume high AI usage means most tasks are fully delegable; the 0–20% reality says otherwise.
- Mark a design-heavy or taste-dependent task delegate-to-agent because it is technically small.
- Set oversight loosely to "save time" when the verification signal is weak.

✅ **DO:**
- Anchor each verdict in concrete determining factors, including whether you know the right answer.
- Let signal strength set autonomy — strong tests earn let-it-run; absent signals force watch-closely or keep.
- Use co-work as a first-class verdict for partly-delegable, judgment-heavy work.
- Recommend adding the missing signal so a task can graduate to delegation safely.

## Example Output

```markdown
## Delegation Triage: Sprint 14 Backlog

### Task Triage Table
| Task | Determining factors | Verdict | Verification signal | Oversight level |
|---|---|---|---|---|
| Add pagination to list endpoint | Well-defined, repetitive, low-stakes | Delegate | Existing API tests + type checker | Let-it-run |
| Migrate config to new schema | Defined, reversible, medium-stakes | Co-work | Schema validation + staging smoke | Check-milestones |
| Redesign permissions model | Conceptually hard, design-dependent, high-stakes | Keep | None automated; needs judgment | Review-every-change |
| Bulk-rename internal symbols | Repetitive, easily verifiable | Delegate | Build + full test suite | Let-it-run |
| Choose caching strategy | Context-heavy, taste-dependent | Co-work | Benchmark harness (partial) | Watch-closely |

### Signal-Hardening Recommendations
- "Choose caching strategy": add a benchmark + correctness test before raising autonomy.
- "Redesign permissions model": once design is fixed, write an authorization test matrix to make implementation delegable.

### Summary
2 delegate / 2 co-work / 1 keep. Consistent with the 0–20% fully-delegable band: most real value sits in co-work with genuine oversight, not hands-off automation.
```

**Techniques Used:**
- **DS-06 (Prioritization & Severity Guidance):** stakes and signal strength order the triage and set oversight.
- **AG-28 (Agent Oversight Calibration):** maps each task to a justified oversight level.
- **RT-02 (Role-Based Expertise):** reasons as an engineer calibrating safe delegation.
- **AG-27 (Agent Task Decomposition):** separates delegable parts from judgment that must stay human (co-work).
- **QA-12 (False Positives Identification):** guards against delegating plausible-but-unverifiable output.

**Related Prompts:**
- `ai_pattern_agent_task_first_delegation_spec.md` — write the full spec for a task this triage marks delegate.
- `ai_pattern_agent_task_code_distance_scorer.md` — score how far a task sits from existing code.
- `airollout_delegate_like_parallel_coworker.md` — operate delegated tasks like parallel coworkers.
