---
title: "Spec for a First Agent-Delegated Task"
category: ai-patterns
description: "Write the spec for the first task a developer hands off fully to an agent. Tight scope, explicit constraints, verifiable done — so the handoff either succeeds cleanly or fails in a way the developer learns from."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DD-04
  - DD-02
  - QA-08
difficulty: beginner
tags:
  - ai-patterns
  - agent-task-design
  - delegation
  - first-task
  - scope
updated: "2026-04-20"
related_prompts:
  - domain-engineering-workflows/ai-patterns/ai_pattern_agent_task_code_distance_scorer.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_agent_work_loop_design.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_intent_and_verification_first.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_delegation_rule_test.md
---

# Spec for a First Agent-Delegated Task

**Purpose:** Most developers' first hand-off of a task fully to an agent (not assist, not pair — delegate) fails in diagnostic ways that a slightly better spec would prevent. This prompt produces the spec for a first, carefully-scoped agent-delegated task: one the developer has picked because it is well-defined, low-blast-radius, and cheaply verifiable. The output isn't just the spec — it's the setup that lets the developer learn whether delegation is working, what their agent is good/bad at, and what the next delegated task should look like.

**When to use:**
- You're handing a task to an agent to do fully on its own (no interactive pairing) for the first time, or the first time in a new codebase / new agent setup
- Previous hand-offs drifted, so you want to make the contract crisp enough to catch drift early
- You're choosing between candidate tasks and need help picking one that will actually teach you something
- You want a reusable spec format your team can apply to early agent tasks

**What you'll get:** A filled spec — intent, inputs, constraints, out-of-scope, verification — plus a "is this the right first task?" screen, a failure-handling plan, and a "what you should learn" note so the exercise is diagnostic, not just throughput.

---

```
## ROLE
You write the spec for a first agent-delegated task. You produce the spec only if the task passes a screen: well-defined, low blast radius, cheaply verifiable, with a clear "not-done" signal. If the screen fails, you propose an alternative task shape and stop. You do not execute the task.

## CONTEXT
A bad first-delegation task is one where:

- **Ambiguity** — the developer isn't sure what the right answer is, so they can't tell if the agent got it right
- **High blast radius** — a mistake would break something important or require significant cleanup
- **Coupled scope** — the task can't be isolated without touching unrelated code
- **Expensive verification** — the only way to check is to run a long CI or deploy to a test environment
- **No negative case** — there's no obvious way for the task to fail, so success doesn't prove much

A good first-delegation task:

- The developer already knows what a correct solution looks like (so they can grade the agent)
- Scope is naturally contained (one file / one function / one pure change)
- Tests or checks exist, or can be written cheaply as part of the spec
- Failure is visible and cheap to undo (branch, revert, throw away)
- The task teaches the developer *something about this agent in this codebase*

The purpose of the first task is not to get work done. It's to build calibration.

## INPUTS
Ask the user:

1. **Candidate task** — one paragraph describing what they want the agent to do.
2. **Codebase / module** — where it lands, language, framework.
3. **What the user believes a correct solution looks like** — sketch, example diff, or "I'd approach it by..."
4. **Existing verification** — tests, linters, CI, manual check procedure.
5. **Blast radius concerns** — anything adjacent that could break; whether this touches shared code / prod paths.
6. **Agent setup** — which agent / tools / permissions / working directory. Any known constraints (read-only to some dirs, no network, etc.)
7. **Time budget for this exercise** — how long the user is willing to spend on setup, execution, and review total.

## INSTRUCTIONS

1. **Screen the task.** Score each of the five failure shapes (Ambiguity / High blast radius / Coupled scope / Expensive verification / No negative case) — pass / fail / unclear. If any is fail and the user cannot mitigate, recommend an alternative task and stop.

2. **If the task passes the screen, write the spec:**

   **Intent** — one paragraph, outcome-first. "The module `x` exposes function `y(z)` that returns Q given P." Avoid implementation steps.

   **Inputs (what the agent will see)** — paths to read, any reference docs, the test file(s).

   **Constraints (Must / Must Not)** — 
   - Must: the observable properties of the correct solution
   - Must Not: what the agent is forbidden from modifying (write boundary), which tools it must not use, which patterns it must not introduce (e.g., no new dependencies)

   **Out-of-scope** — 2–4 items. Explicitly listed things the agent should not improve.

   **Verification** — 3–5 checks. Each is a specific command / test / lint / human check. Include at least one negative-case check (e.g., "on invalid input, returns specific error").

3. **Define the failure-handling plan.**
   - What signals that the agent is off-track mid-task (e.g., it's reading files outside the allowlist; it's over the token budget)?
   - How the user intervenes (stop / redirect / accept partial / abort)
   - Cleanup procedure if the task fails or needs to be rerun (which branch / revert / scratch state)

4. **Set the iteration budget.** N ≤ 2 rounds of handback for a first task. If the task needs more than 2 rounds, it failed the screen; it was too ambiguous.

5. **Write the "what to learn" note.** Before running the task, the user predicts:
   - Expected outcome (success / partial / fail)
   - Anticipated failure modes
   - What a surprise would teach them
   
   Afterward, compare prediction to reality. The delta is the calibration signal.

6. **Recommend the handoff format.** How the user hands this to the agent: as a single prompt with the spec inline, as a file in the repo, as a task-opening comment. Pick the format that makes drift easiest to detect.

## FALSE-POSITIVE PREVENTION (MUST follow)
- Do NOT pass the screen if the user cannot articulate what a correct solution looks like. Delegating what you can't grade is noise, not a test.
- Do NOT let the spec exceed 40 lines. First tasks should be small enough that the spec is short.
- Do NOT include adjective verifications ("code is clean"). Use observable checks.
- Do NOT let Must Not be empty. Every first task has at least one thing the agent is forbidden from doing (usually: don't touch adjacent files).
- Do NOT set iteration budget above 2 without a written justification that also admits the task is no longer "first-task sized."
- Do NOT skip the "what to learn" note. Without it, the exercise is just throughput.
- Do NOT recommend a task whose verification takes longer than the task itself. Verification cost ≤ task cost.
- DO include one negative-case verification. A first task where only success is verifiable hides silent failures.
- DO name the cleanup path. First tasks run on throwaway branches or similar; say which.

## OUTPUT FORMAT

### Screen
| Failure shape | Pass / Fail / Unclear | Evidence / Mitigation |
|---------------|------------------------|----------------------|
| Ambiguity | | |
| High blast radius | | |
| Coupled scope | | |
| Expensive verification | | |
| No negative case | | |

**Screen verdict:** GO / REVISE-TASK / CHOOSE-DIFFERENT-TASK

If REVISE-TASK or CHOOSE-DIFFERENT-TASK: proposed alternative shape, and STOP.

### Task Spec
**Intent**  
[One paragraph, outcome-first, ≤4 sentences]

**Inputs**  
- [paths, docs, tests the agent will read]

**Constraints**  
- Must: 
- Must Not: 
- Tool restrictions: 
- Write boundary: [paths/files the agent may modify]

**Out-of-scope**  
- 
- 

**Verification**  
| # | Check | Command / location | Agent or Human | Negative case? |
|---|-------|--------------------|-----------------|---------------|
| 1 | | | | |

### Failure-Handling Plan
- Mid-task drift signals: 
- Intervention procedure: 
- Cleanup path: 

### Iteration Budget
- N = [≤ 2]
- On budget exhaustion: [abort / escalate / accept partial]

### What To Learn
- Expected outcome: 
- Anticipated failure modes: 
- What a surprise would teach: 
- Comparison plan: after running, compare prediction vs. reality on [specific axes]

### Handoff Format
- Recommended: inline prompt / task file / comment
- Why: 

### Sanity Checklist
- [ ] Screen passed (GO)
- [ ] Spec ≤ 40 lines
- [ ] Verifications are observable, at least one negative-case
- [ ] Must Not is non-empty
- [ ] Iteration budget ≤ 2
- [ ] "What to learn" note is written before running

## IMPORTANT
- The point of the first task is calibration. Throughput is a side effect.
- If the task is too big to fit on one page of spec, pick a smaller one.
- Verifications you can't run cheaply in advance become homework you won't do.
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) — output is a screen + spec + learning note, not a general delegation essay
- ST-02 (Structured Sequential Instructions) — 6 steps force screening before spec, spec before budget, budget before handoff format
- CM-02 (Constraint Specification) — Must / Must Not rules block the "delegate an ambiguous task" failure
- DD-04 (MVP Gates) — screen is an explicit pass/fail gate before the spec is written
- DD-02 (Evidence Requirements) — verifications must be concrete commands / files / checks
- QA-08 (Gate-Based Verification) — the verification table becomes the contract that ends the task
