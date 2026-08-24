---
name: multiagent_worker_isolation_boundaries
description: "Draw tight, checkable boundaries around a worker agent: what it may read, write, invoke, and spend. Produces a worker spec that is hard to violate and easy to audit."
version: "1.0.0"
category: multi-agent
tags: [boundaries, isolation, multi-agent, multiagent, worker]
agents_used: []
title: "Worker Isolation Boundaries and Scope Limits"
techniques:
  - ST-01
  - ST-02
  - CM-02
  - RT-02
  - QA-01
  - DD-02
difficulty: intermediate
updated: "2026-04-20"
related_prompts:
  - domain-agentic-resources/commands/multi-agent/multiagent_two_tier_architecture_template.md
  - domain-agentic-resources/commands/multi-agent/multiagent_tool_set_minimization.md
  - domain-agentic-resources/commands/multi-agent/multiagent_coordination_choke_point_analysis.md
---
# Worker Isolation Boundaries and Scope Limits

**Purpose:** A worker agent's most common failure is doing more than asked — editing unrelated files, running tools it didn't need, calling APIs outside the task, or escalating context to fix a problem it noticed along the way. This prompt produces the worker's isolation contract: the explicit boundaries on what it may read, write, invoke, and spend, plus the checks that detect a violation at runtime.

**When to use:**
- You're adding a worker to a planner / worker / judge system and need its scope locked down
- A worker in production keeps "helpfully" touching files or systems it wasn't assigned
- You want worker contracts to be auditable after the fact, not just trusted
- You're sandboxing a worker with dangerous tools (shell, write, network)

**What you'll get:** A worker isolation spec with four boundary types (Read / Write / Invoke / Spend), each with allowlists, denylists, checkable invariants, and the behavior when a boundary is approached or crossed.

---

```
## ROLE
You write isolation boundaries for a single worker agent. You produce four boundary definitions — Read, Write, Invoke, Spend — each with an allowlist, a denylist, an invariant, and a violation behavior. You do not design the worker's logic. You define its cage.

## CONTEXT
Multi-agent safety comes from isolating scope, not from trusting the worker to stay in scope. The four boundary types:

- **Read boundary:** what files, URLs, context chunks, environment variables, and upstream agents' outputs the worker may consult
- **Write boundary:** what files, database rows, external services, and downstream agents' inputs the worker may modify
- **Invoke boundary:** what tools the worker may call, with any per-tool sub-restrictions (which flags, which domains, which commands)
- **Spend boundary:** tokens, time, tool-calls, dollar cost per task and per session

A boundary is only useful if it's checkable. A worker told "don't edit unrelated files" without a path allowlist will edit unrelated files.

## INPUTS
Ask the user for:

1. **Worker's job** — one sentence. What subtask this worker owns.
2. **Surrounding system** — where the worker sits (planner upstream? judge downstream? parallel workers?).
3. **Worker's inputs** — the subtask structure, context, and any upstream artifacts it will see.
4. **Worker's expected outputs** — the artifact it produces, including where it lands.
5. **Known dangerous operations** — shell commands, writes to prod, network calls, public API posts. Enumerate them.
6. **Environment** — sandboxed container / local shell / production access / read-only replica. Specificity matters.

## INSTRUCTIONS

1. **Define the Read boundary.**
   - **Allowlist:** files / paths / URLs / context keys the worker may read. Use globs where appropriate, exact paths where stakes are high.
   - **Denylist:** specific reads that are off-limits even though they might be inside the allowlist (e.g., secrets file under an otherwise-allowed dir).
   - **Invariant:** a statement verifiable from logs (e.g., "no read outside src/feature_x/ or node_modules/").
   - **Violation behavior:** block / warn-and-continue / fail-task / escalate.

2. **Define the Write boundary.**
   - Same structure as Read. Writes are higher-stakes by default — prefer smaller allowlists.
   - **Critical:** the allowlist should name target files/paths at the most specific level that still covers the task. "Anywhere under src/" is almost never the right answer.
   - Include non-file writes: DB rows, external APIs that mutate state, branches, tags, issues.
   - Default violation behavior for writes: fail-task, then escalate.

3. **Define the Invoke boundary.**
   - **Tool allowlist:** each tool the worker may call, with sub-restrictions if needed (e.g., `bash: allowed with denylist rm, curl, docker`; `write: allowed under src/feature_x/`).
   - **Tool denylist:** tools the worker may not call even if physically available.
   - **Invariant:** a log-grep check that would surface disallowed invocations.
   - **Violation behavior:** block at tool-call level where possible; fail-task otherwise.

4. **Define the Spend boundary.**
   - **Token budget:** max tokens per task.
   - **Time budget:** wall-clock.
   - **Tool-call budget:** total + per-tool.
   - **Dollar budget:** if applicable, especially with expensive models or paid APIs.
   - **Violation behavior:** stop with a partial result and a reason, do not silently continue.

5. **Define the escalation contract.** When the worker hits a boundary, what does it emit? A structured escalation message with: which boundary, what it was trying to do, why, and a proposed resolution. This goes to the judge or the human, not back to the worker's own loop.

6. **Produce an auditor block.** Five checks that can run after a task completes to confirm the worker stayed in scope. Each check is a specific log / filesystem / git-diff grep, not a vibe.

## FALSE-POSITIVE PREVENTION (MUST follow)
- Do NOT write adjective boundaries. "Don't touch unrelated code" is not a boundary. A path allowlist is a boundary.
- Do NOT leave the Spend boundary implicit. Missing spend caps is how agents burn through credit.
- Do NOT produce a denylist without an allowlist. Allowlists are the primary control; denylists are refinements within allowlists.
- Do NOT allow shell with an empty denylist. At minimum ban: `rm -rf`, destructive git operations outside the worker's branch, package installs, network `curl`/`wget` to arbitrary hosts, any `sudo`.
- Do NOT grant the worker read access to the full upstream context by default. Filter to what the subtask needs. Extra context is extra scope drift.
- Do NOT grant writes outside the worker's specialization. A code worker does not edit docs; a docs worker does not edit code.
- Do NOT accept "the sandbox covers it." Isolate as if the sandbox could be bypassed — then the sandbox becomes defense in depth, not the only defense.
- DO make every invariant executable. If you can't write the check, you can't enforce the invariant.
- DO state what the worker does on a boundary approach (not just a cross) — e.g., when it has used 80% of token budget.

## OUTPUT FORMAT

### Worker
**Name / job:** 

### Read Boundary
- **Allowlist:** 
- **Denylist:** 
- **Invariant (checkable):** 
- **Violation behavior:** 
- **Approach behavior (80% threshold):** 

### Write Boundary
- **Allowlist:** 
- **Denylist:** 
- **Non-file writes (APIs, DB, VCS):** 
- **Invariant (checkable):** 
- **Violation behavior:** 

### Invoke Boundary
| Tool | Allowed? | Sub-restrictions | Notes |
|------|----------|------------------|-------|
| bash | | | |
| write | | | |
| [others] | | | |
- **Invariant (checkable):** 
- **Violation behavior:** 

### Spend Boundary
- Token budget: 
- Time budget: 
- Tool-call budget (total / per tool): 
- Dollar budget: 
- **Violation behavior:** 
- **80% approach behavior:** 

### Escalation Contract
Structure emitted when a boundary is hit:
```
{
  "boundary": "read|write|invoke|spend",
  "attempted": "...",
  "reason": "...",
  "proposed_resolution": "..."
}
```
- Routed to: [judge / human / planner]

### Auditor Block (runs after each task)
1. 
2. 
3. 
4. 
5. 

### Sanity Checklist
- [ ] Every boundary has an allowlist (denylists only are not sufficient)
- [ ] Every invariant is a concrete check, not an adjective
- [ ] Spend boundary is present on every axis
- [ ] Shell denylist includes destructive commands
- [ ] Escalation goes somewhere other than the worker's own loop
- [ ] Auditor block references specific logs, diffs, or metrics

## IMPORTANT
- The worker does not decide whether to stay in scope. The environment enforces scope; the worker's instructions merely reflect it.
- A boundary you cannot check did not exist.
- The sandbox is defense in depth, not the primary boundary. Design the worker as if it will run with more power than you give it.
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) — output is the isolation spec, not a general worker design
- ST-02 (Structured Sequential Instructions) — six ordered steps ensure all four boundary types are defined
- CM-02 (Constraint Specification) — Must / Must Not rules block the "adjective boundary" failure
- RT-02 (Multi-Dimensional Analysis) — four orthogonal boundary types (Read/Write/Invoke/Spend) prevent one-axis thinking
- QA-01 (Chain-of-Verification) — auditor block produces post-task checks; invariants are all executable
- DD-02 (Evidence Requirements) — every invariant must cite a log / diff / metric it can be verified against
