---
name: multiagent_coordination_via_tests_and_policy
description: "Use a shared test suite as the coordination surface between parallel agents, and pair it with a conflict-resolution policy for when agents produce conflicting changes. Replaces chatty inter-agent negotiation with executable contracts."
version: "1.0.0"
category: multi-agent
tags: [coordination, multi-agent, multiagent, policy, tests]
agents_used: []
title: "Coordinate Multiple Agents Through Tests and Conflict-Resolution Policy"
techniques:
  - ST-01
  - ST-02
  - CM-02
  - RT-02
  - RT-11
  - QA-08
difficulty: advanced
updated: "2026-04-20"
related_prompts:
  - domain-agentic-resources/commands/multi-agent/multiagent_worker_isolation_boundaries.md
  - domain-agentic-resources/commands/multi-agent/multiagent_good_enough_gate_design.md
  - domain-agentic-resources/commands/multi-agent/multiagent_coordination_choke_point_analysis.md
---
# Coordinate Multiple Agents Through Tests and Conflict-Resolution Policy

**Purpose:** When multiple agents work on the same codebase or artifact, the worst coordination mechanism is chat between agents. The best is a shared executable contract — usually tests — plus a deterministic policy for resolving the conflicts that still happen at the merge point. This prompt designs both: the coordination test surface (what each agent must satisfy) and the conflict-resolution policy (who wins when changes collide).

**When to use:**
- Two or more agents work in parallel on the same repo / codebase / document
- Agents sometimes "negotiate" in inline messages that waste tokens and drift
- You've had conflicting edits at merge time and resolved them by hand or by ad hoc rules
- You're standing up a new multi-agent system and want coordination by contract, not by conversation
- An orchestrator keeps re-broadcasting partial state between agents

**What you'll get:** A coordination-test spec (what shared tests each agent must pass, who owns what), a conflict-resolution policy (priority order, merge strategy, escalation path), and the observability a human needs to debug conflicts after the fact.

---

```
## ROLE
You design the coordination surface between multiple agents working in parallel on shared state. You do NOT design the agents' individual logic. You produce two artifacts: (1) the test / contract surface each agent codes against, and (2) the conflict-resolution policy that applies when their outputs collide.

## CONTEXT
Two agents working on the same repo can fail in three ways:

- **Semantic conflict:** both agents edit different lines of the same file; git merges cleanly but the combined behavior is wrong (e.g., both remove the same safety check from different angles)
- **Physical conflict:** both agents edit the same lines; the second merge fails, forcing rework
- **Spec drift:** an agent's contract changes mid-task and the other agent's work is now wrong against the new spec

Coordination solutions come in two layers:

1. **Tests as contracts (forcing).** A shared test suite defines the observable behavior every agent's changes must preserve or produce. Agents don't negotiate what's correct; they run the tests. This moves coordination from chat to CI.

2. **Policy for residuals.** Even with good tests, collisions happen. Policy tells the orchestrator (or a human) how to resolve them deterministically: which agent's change takes precedence, whether to merge + rerun, or whether to escalate.

The two layers are complementary: tests prevent most conflicts; policy handles the rest.

## INPUTS
Ask the user:

1. **Agents in scope** — list each agent, its role, and its write surface (which files, rows, or resources it edits).
2. **Shared state** — what each agent reads / writes that others also touch.
3. **Observed conflicts** — real examples of semantic / physical / spec-drift conflicts from recent runs.
4. **Existing tests** — what test suite exists, how it runs, how fast, coverage gaps.
5. **Merge / apply mechanism** — is each agent producing a branch / a patch / a PR / direct commits? Who merges?
6. **Constraints** — latency budget (can we afford to rerun tests after each agent?), human-in-the-loop availability, CI access.

## INSTRUCTIONS

1. **Partition write surfaces first.** Coordination is easier when write surfaces don't overlap. For each pair of agents:
   - Can their write surfaces be disjoint? (different directories, different config keys, different DB tables)
   - If yes, recommend the partition and reduce conflict handling to the narrow shared seam
   - If no (they must edit the same files), move to the test + policy design below

2. **Design the coordination test surface.** For each shared piece of state:
   - **Invariant tests:** behaviors that must hold regardless of what any agent does (e.g., "auth middleware is present on every route," "schema migration is reversible")
   - **Contract tests:** the interface between agents' work (e.g., frontend agent's component API consumed by backend agent's handlers)
   - **Regression tests:** behaviors that existed before and must still work after parallel edits
   
   Each test is:
   - Owned by someone (a team, a skill, the coordinator — not "all agents")
   - Fast enough to run on every agent's handoff (if slow, a subset runs per-agent and full suite runs pre-merge)
   - Has a clear failure message that tells the agent what to fix

3. **Define which tests each agent must pass before its output is accepted.** Not every agent runs every test. An agent editing docs does not need to pass the backend contract tests, but its output should not break the docs-build test. Map agent → required tests.

4. **Design the conflict-resolution policy** for the residual collisions:
   - **Physical conflicts (merge conflicts):** deterministic priority order (by agent role, by timestamp, by patch size) OR semantic merge via a mediator agent OR always-escalate-to-human for these files
   - **Semantic conflicts:** detected when all agents' tests pass individually but the merged state fails the suite. Policy: who reruns? The last committer? A mediator? How is blame assigned?
   - **Spec drift:** when one agent changes the shared spec mid-task, detected by spec-file test failure on other agents' outputs. Policy: halt dependent agents, re-broadcast spec, resume.

5. **Define the orchestrator's role.** The orchestrator is not an agent — it is a process that applies the policy. It:
   - Runs required tests per agent output
   - Applies the priority rule on physical conflicts
   - Runs the full suite after merges
   - Escalates when the policy fails (e.g., two priority-equal agents collide)

6. **Define the observability.** After the fact, a human must be able to reconstruct:
   - Which agent wrote which change
   - Which tests ran at which stage
   - Where a conflict occurred and how it was resolved
   - How long each resolution took
   
   Require a conflict log in structured form (agent, file, type of conflict, resolution applied, outcome).

7. **Define the fallback: when the policy loops.** If the conflict-resolution policy itself produces oscillation (agent A's fix breaks agent B's tests; agent B's re-fix breaks agent A's; repeat) — detect at cycle 2, escalate at cycle 3. Do not let the system auto-fix indefinitely.

## FALSE-POSITIVE PREVENTION (MUST follow)
- Do NOT rely on inter-agent chat for coordination. Chat does not scale and is not replayable.
- Do NOT assume "the tests cover it." Ask for coverage numbers and identify which shared state has no test coverage — those are future conflict sources.
- Do NOT pick "timestamp order" as a priority rule by default. Timestamp-wins reward race conditions. Prefer role-based priority (owner agent wins) or explicit patch-size heuristics.
- Do NOT let any agent edit the shared test suite as part of its task unless it is a designated tests-owner agent. Otherwise, tests decay into whatever the busiest agent needed.
- Do NOT omit the spec-drift case. It is the most destructive and the least noticed.
- Do NOT skip observability. An unreplayable conflict resolution is worse than no coordination — it prevents learning.
- Do NOT recommend a mediator agent unless semantic conflicts are frequent and cheap test reruns won't resolve them. Mediators add their own failure surface.
- DO prefer partitioning write surfaces. Disjoint writes dissolve most conflict problems.
- DO require tests to be owned. Ownerless tests rot.

## OUTPUT FORMAT

### Partition Check
| Agent A | Agent B | Can writes be disjoint? | Proposed partition |
|---------|---------|-------------------------|--------------------|
| | | Y/N | |

### Coordination Test Surface
| Test ID | Type (Invariant / Contract / Regression) | Owner | Triggers (per-agent / per-merge) | Failure message template |
|---------|------------------------------------------|-------|----------------------------------|--------------------------|
| | | | | |

### Per-Agent Required Tests
| Agent | Must pass tests |
|-------|-----------------|
| | |

### Conflict-Resolution Policy
**Physical conflicts:**
- Priority rule: 
- Merge mechanism: 
- Escalation: 

**Semantic conflicts:**
- Detection: 
- Who fixes first: 
- Blame assignment: 
- Escalation: 

**Spec drift:**
- Detection: 
- Halt / re-broadcast procedure: 
- Resume condition: 

### Orchestrator Role
- Runs: [tests, at which stage]
- Applies: [which policies]
- Escalates when: [conditions]

### Observability
Conflict log schema:
```
{
  "conflict_id": "...",
  "agents_involved": [...],
  "type": "physical|semantic|spec_drift",
  "files": [...],
  "resolution_applied": "...",
  "resolution_time_ms": ...,
  "outcome": "merged|reverted|escalated"
}
```

### Oscillation Fallback
- Cycle detection: 
- Escalation at cycle: 
- Escalation target: 

### Sanity Checklist
- [ ] Write surfaces partitioned where possible
- [ ] Every shared state has at least one coordination test
- [ ] Every test has a named owner
- [ ] No agent edits the test suite except the tests-owner
- [ ] Priority rules are deterministic and replayable
- [ ] Spec-drift handling is explicit
- [ ] Conflict log structure is defined
- [ ] Oscillation cap exists

## IMPORTANT
- Tests convert coordination from negotiation to execution. Invest here before investing in mediator agents.
- When two agents can edit the same file, one of them is mis-scoped. Revisit the split.
- The observability is not optional. Without it, every conflict is a fresh mystery.
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) — output is test surface + conflict policy, not a general coordination essay
- ST-02 (Structured Sequential Instructions) — 7 ordered steps force partitioning before escalation
- CM-02 (Constraint Specification) — Must / Must Not rules block timestamp-wins and chat-based coordination
- RT-02 (Multi-Dimensional Analysis) — three conflict types (physical / semantic / spec drift) handled separately
- RT-11 (Error Recovery) — oscillation fallback defines the end condition of the resolution loop
- QA-08 (Gate-Based Verification) — coordination tests act as the pre-merge gate each agent's output must pass
