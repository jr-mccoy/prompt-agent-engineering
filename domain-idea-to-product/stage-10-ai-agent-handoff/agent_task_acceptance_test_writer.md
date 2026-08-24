---
title: "Agent Task Acceptance-Test Writer (Per-Task Verification Block)"
category: idea-to-product/ai-agent-handoff
description: "For a single AI-agent-delegated task, write the precise verification block the agent must satisfy before reporting 'done': test commands, expected outputs, lint/typecheck gates, behavioral assertions, and explicit 'false-success' traps that catch the common ways agents declare victory on broken work."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-01
  - QA-01
  - QA-02
  - QA-03  # False-positive prevention
difficulty: advanced
tags:
  - ai-agent-handoff
  - acceptance-tests
  - verification
  - false-positive-prevention
  - claude-code
updated: "2026-05-19"
related_prompts:
  - domain-idea-to-product/stage-10-ai-agent-handoff/prd_to_agent_brief_bridge.md
  - domain-idea-to-product/stage-10-ai-agent-handoff/ai_pattern_agent_task_first_delegation_spec.md
  - domain-idea-to-product/stage-10-ai-agent-handoff/ai_pattern_agent_work_loop_design.md
  - domain-idea-to-product/stage-10-ai-agent-handoff/viberescue_rules_file_design.md
---

# Agent Task Acceptance-Test Writer (Per-Task Verification Block)

**Objective:** Given a single agent-delegated task (one task ID from the bridge prompt's task list), produce the exact acceptance-test block the agent must paste into its work-loop and satisfy before declaring "done." The block includes commands to run, expected outputs, behavioral assertions, lint/type/test gates, and "false-success traps" that prevent the agent from claiming victory on technically-passing-but-broken code.

## When to Use

- After `prd_to_agent_brief_bridge.md` has produced the first N tasks.
- Once per task before the task is delegated.
- Whenever a task fails and you're re-issuing it with a sharper acceptance spec.

## Inputs

The user must provide:
1. **Task ID and title** (e.g., "T-003: User can sign up with email and verify via magic link").
2. **Feature(s) this task implements** (from the epic/feature tree).
3. **Stack canon excerpt** relevant to this task (e.g., "Next.js app router, Drizzle ORM, Clerk auth").
4. **Existing test commands** in the repo (e.g., `npm run test`, `npm run test:e2e`, `npm run typecheck`, `npm run lint`).
5. **Definition of "done" in the user's words** — what does the user need to be able to do/see for this task to be considered complete?

If any input is missing, ask. Do not infer the definition of done.

## Constraints

**Must:**
- Produce acceptance criteria as a checklist of binary (pass/fail), executable assertions — not vibe descriptions.
- Include at least one **behavioral assertion** (end-to-end: simulate a user action and observe the outcome) for any task that touches user-visible behavior.
- Include at least one **false-success trap** (a specific way the agent might think it succeeded but didn't).
- Include the literal commands to run, with expected output snippets (not just "tests should pass").
- Include lint, typecheck, and test gates as separate items (not lumped).
- Specify the **artifacts the agent must produce** (files created/modified, with paths).
- Specify the **artifacts the agent must NOT produce** (e.g., "no new dependencies without ADR," "no migrations outside `db/migrations/`").
- Specify **observable-from-outside verification** — at least one check the user can run without reading code.

**Must Not:**
- Use vague criteria like "code is clean" or "well-tested." Be specific.
- Allow "skip if not applicable" without an explicit justification clause.
- Trust passing tests alone as success — include behavioral assertions and false-success traps.
- Write so many criteria that the agent can't reasonably satisfy them. Aim for 8-15 items.
- Author tests in this prompt's output. This prompt describes WHAT the agent must verify; the agent writes the test code itself.

## Instructions

### Step 1: Restate the task in user-observable terms
"After this task is done, [user persona] can [observable action], producing [observable outcome]."
If you can't write that sentence, stop and ask the user.

### Step 2: Enumerate the acceptance criteria
Group into these categories:

**Functional (behavioral, end-to-end):**
- What can the user now do that they couldn't before?
- What happens at each branch (happy path, common error, edge case)?
- What's the verification command/UI step (curl, browser, CLI) to observe each?

**Structural:**
- Which files must exist, and what must they contain (specific exports, schema, route)?
- Which files must NOT have been touched (out-of-scope safety)?

**Quality gates (commands, with expected outputs):**
- `npm run lint` → exit 0
- `npm run typecheck` → exit 0
- `npm run test` → all named tests in [pattern] pass; coverage on changed files ≥ X%
- `npm run test:e2e -- [specific test file]` → pass

**Non-regression:**
- Specific existing functionality that this task is most likely to accidentally break — list 1-3 explicit checks.

**Documentation & memory:**
- `.project-memory/00-state.md` updated with task completion entry.
- `decisions-log.md` appended if any architectural choice was made.
- Any new public API surface documented in `docs/`.

### Step 3: False-success traps (the critical section)
List the specific ways the agent might wrongly claim success on this task. Common patterns:
- **Test exists but tests nothing.** ("test('sign up works', () => { expect(true).toBe(true) })" pattern — explicitly forbidden.)
- **Mock satisfies the test but production code is broken.** (e.g., a mocked auth client that doesn't match the real one's interface.)
- **Tests pass because the code is never executed.** (Route exists but isn't registered; component exists but isn't imported anywhere.)
- **TypeScript passes because of `any` escape hatches.** (Forbid `any` and `@ts-ignore` in changed files.)
- **The feature works in isolation but breaks the existing flow it integrates with.**
- **Database migration runs forward but not in reverse / not on a fresh database.**

For each trap, write the specific check that would catch it.

### Step 4: Observable-from-outside verification
At least one verification step that the user (not the agent) can run from a fresh terminal/browser to confirm the task is done. Example:
- `curl -X POST http://localhost:3000/api/signup -d '{"email":"test@example.com"}'` returns 200 with a verification-email-sent confirmation.

### Step 5: Status reporting format
The agent's "done" report must include:
- Every acceptance criterion with PASS / FAIL / N-A (with justification for N-A)
- The exact commands run, with outputs (truncated to relevant lines)
- Files changed (paths + brief description)
- New dependencies added (or "none")
- Open questions or assumptions made
- Updated `.project-memory/00-state.md` entry (pasted)

## Output Format

```
## Acceptance Spec: [Task ID] — [Task title]

### User-observable restatement
After this task, [persona] can [action] producing [outcome].

### Functional acceptance
- [ ] [Specific behavior 1] — verify by: [command/step]
- [ ] [Behavior 2] — verify by: [command/step]
- [ ] [Error path] — verify by: [command/step]
- [ ] [Edge case] — verify by: [command/step]

### Structural acceptance
- [ ] Files created: [list with paths and required contents]
- [ ] Files modified: [list with paths and nature of change]
- [ ] Files NOT touched: [out-of-scope safety list]

### Quality gates (commands + expected)
- [ ] `npm run lint` → exit 0
- [ ] `npm run typecheck` → exit 0
- [ ] `npm run test [-- pattern]` → all listed tests pass
- [ ] `npm run test:e2e [-- pattern]` → pass

### Non-regression
- [ ] [Existing behavior X] still works — verify by: [command]
- [ ] [Existing behavior Y] still works — verify by: [command]

### False-success traps (explicit checks)
- [ ] No test of form `expect(true).toBe(true)` or empty `it()` blocks added
- [ ] No `any`, `@ts-ignore`, `eslint-disable` in changed files
- [ ] Code is actually wired up: [check that route/component/handler is reachable from the user-observable starting point]
- [ ] Mocks match real interface: [check by running [specific integration test]]
- [ ] Migration is reversible AND runs on a fresh DB: [check by `npm run db:migrate:reset && npm run db:migrate`]
- [ ] [Task-specific trap based on the task's content]

### Observable-from-outside verification
[1-3 commands or UI steps the user runs to independently confirm]

### Status report format the agent must submit
[Template restating all of the above as PASS/FAIL/N-A with evidence]
```

## Verification

- [ ] User-observable restatement present
- [ ] At least 1 behavioral assertion (not just unit tests)
- [ ] Quality gates list lint, typecheck, test as separate items
- [ ] At least 3 false-success traps, including one task-specific
- [ ] At least 1 observable-from-outside verification step
- [ ] Status-report format included
- [ ] Total acceptance items: 8-15 (not too few, not too many)

## False-Positive Prevention

- **Agents will pad their done-reports.** Insist on the structured PASS/FAIL/N-A format with command outputs, not narrative.
- **"Tests pass" is not done.** Without behavioral assertions and false-success traps, an agent can satisfy a test suite while shipping broken code.
- **Acceptance specs that lump categories** (e.g., one bullet for "code quality") let the agent declare success without evidence. Decompose.
- **N-A as an escape hatch.** Require explicit justification for any N-A; spot-check the first 3 tasks for unjustified N-As.
- **The user not running the observable-from-outside check.** Don't trust the agent's report alone for the first 5 tasks. The check exists precisely so the user can verify.
- **Migration / database tasks.** These have the highest false-success rate because tests often run on the same DB the agent built. Always require the fresh-DB reset check.
