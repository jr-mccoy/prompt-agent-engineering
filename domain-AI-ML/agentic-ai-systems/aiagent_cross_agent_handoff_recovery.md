---
title: "Cross-Agent Handoff & Failure Recovery Design"
category: AI-ML/agentic-ai-systems
description: "Design handoffs and recovery for a multi-agent or cross-tool run so that when one agent's output feeds the next, or one session/tool hands to another, downstream failure is contained, attributable, and recoverable — with full-context handoff records, failure isolation, compensation, project-memory writeback, evaluator redundancy, and explicit shared stopping conditions."
techniques:
  - ST-02
  - CM-02
  - AG-29
  - QA-12
  - QA-01
difficulty: advanced
tags:
  - multi-agent
  - handoff
  - failure-recovery
  - coordination
  - reliability
updated: "2026-06-25"
related_prompts:
  - domain-AI-ML/agentic-ai-systems/aiagent_project_continuity_memory_design.md
  - domain-AI-ML/agentic-ai-systems/aiagent_project_memory_capture_protocol.md
  - domain-AI-ML/agentic-ai-systems/aiagent_inter_agent_communication_protocol.md
  - domain-AI-ML/agentic-ai-systems/aiagent_multi_agent_orchestration.md
  - domain-AI-ML/agentic-ai-systems/aiagent_failure_recovery_rescope.md
  - domain-AI-ML/agentic-ai-systems/aiagent_orchestration_topology_selection.md
  - domain-prompt-engineering/agent-workflows/agent_subagent_brief_generator.md
  - domain-agentic-resources/commands/multi-agent/multiagent_graceful_session_endings.md
---

# Cross-Agent Handoff & Failure Recovery Design

**Objective:** Design how agents, sessions, or tools hand work to each other, and how the system recovers when a downstream agent/session/tool fails — so that "Agent A's output feeds Agent B and B fails" or "Claude Code today hands to Codex tomorrow" does not silently corrupt the result or force a full restart. The design covers the handoff record, failure isolation, compensation across boundaries, failure attribution, defenses against error contagion, project-memory writeback, and shared stopping conditions. Use it only once a multi-agent or cross-tool handoff is justified; multi-agent costs roughly an order of magnitude more tokens and adds coordination failure modes, so a single coherent agent is the default.

**When to Use:**
- Work passes between agents (orchestrator→worker, pipeline A→B→C, or peer handoff) and a downstream failure must be recoverable.
- Work passes between tools or sessions, such as Claude Code → Codex, local CLI → cloud agent, Cursor → human, or one branch/worktree → another.
- You are seeing coordination failures: conflicting decisions, lost context across handoffs, duplicated work, or a stuck integration step.
- A long multi-agent or multi-session run needs to resume after one agent/session fails without redoing the others' work.

**When NOT to Use:**
- The task is coupled/write-heavy enough that a single-threaded agent with context compression is more reliable — don't add agents.
- You haven't yet decided *whether* to split into multiple agents — use `aiagent_multi_agent_orchestration.md` first.
- You need portable, repo-local project memory as the primary design — use `aiagent_project_continuity_memory_design.md`; this prompt designs handoff and recovery boundaries.
- You need the message-schema/shared-state protocol itself — use `aiagent_inter_agent_communication_protocol.md` and cross-link.

## Inputs / Context

Provide what you can:
- **Topology** — orchestrator-worker, pipeline, fan-out/fan-in, debate/council, cross-tool session chain, etc., and where handoffs occur.
- **Per-handoff data** — what each agent/session/tool needs from the previous one to act correctly.
- **Coupling** — are downstream decisions constrained by upstream ones (write-heavy) or independent (read-heavy/parallel)?
- **Irreversible actions per agent/session** — side effects any agent commits that cross the boundary.
- **Project-memory substrate** — whether `.project-memory/`, handoff records, decisions, attempts, or traps exist and should be written.
- **Observed failures** — conflicting outputs, lost context, duplicated work, stalls (if recovering an existing system).

## Constraints

**Must:**
- Define the handoff record so each agent/session receives **full relevant context / relevant traces, not just a summarized message** — lost conversation history and information withholding are leading multi-agent failure modes.
- For cross-tool/cross-session handoffs, include project-memory pointers: current state, handoff file, active decisions, failed attempts, open questions, branch/commit, and verification commands.
- Isolate failures so one agent/session failing does not collapse the whole run (orchestrator-worker isolation; bounded blast radius).
- Define cross-boundary compensation: if a downstream agent/session fails after an upstream agent committed irreversible effects, name the compensating actions and order.
- Provide attribution support: structured, per-agent/session handoff records with trace/run IDs, because automated "which agent caused the failure / at which step" localization is unreliable today.
- Define explicit, **shared stopping conditions** and a "done" definition all agents/sessions agree on (to prevent premature termination, step repetition, and runaway loops).
- Add a verification gate at handoff boundaries (the receiving agent/session or an evaluator checks the handoff is valid before acting) — missing/incorrect verification is a top failure category.

**Must Not:**
- Pass only summaries between agents when downstream decisions depend on upstream reasoning.
- Let a downstream failure trigger a full restart when upstream work is valid and resumable.
- Assume you can auto-localize blame — design for it with explicit records rather than relying on a model to find the culprit.
- Use a homogeneous evaluator with no redundancy where an evaluator's error can propagate agent-to-agent (contagion).
- Spawn agents or hand sessions forward without a shared stopping condition.
- Treat a handoff as durable project memory unless it is captured in the project's canonical continuity-memory format.

**Instructions:**

1. **Map handoffs and coupling.** For each boundary, state what crosses, whether downstream decisions are constrained by upstream ones, and which agent/session commits irreversible effects. If coupling is high, reconsider whether multi-agent is the right choice at all.

2. **Design the handoff record.** Specify the payload that crosses each boundary: the result *plus* the relevant context/trace and the implicit decisions the receiving agent/session must respect, with a trace/run ID and a content hash. Cross-link `agent_subagent_brief_generator.md` for the per-agent brief.

3. **Add cross-tool/session fields where needed.** For Claude Code → Codex, Cursor → terminal, cloud → local, or human → agent handoffs, include {tool/session, branch, commit, dirty_files, active_decisions, failed_attempts_to_avoid, open_questions, next_action, verification_commands, stale_after}.

4. **Add a handoff verification gate.** The receiving agent/session (or an evaluator) validates the incoming handoff against expected schema/criteria before acting; on invalid handoff, reject back to the sender or escalate — don't proceed on a bad input.

5. **Isolate failures.** Ensure a worker/downstream failure is caught by the orchestrator (or pipeline coordinator) and contained — checkpoint completed agents' outputs so a failure doesn't discard them.

6. **Define cross-boundary recovery.** For a downstream failure: can the run resume by re-running only the failed agent/session from the last valid handoff? If the failed agent/session (or an upstream one) committed irreversible effects that are now invalid, define the compensating actions and reverse order. Route the actual decision through `aiagent_failure_recovery_rescope.md`.

7. **Support attribution.** Ensure every handoff and agent action carries IDs so a failure can be traced to an agent/session and step; record the decisive handoff state. Don't rely on automated culprit-finding alone.

8. **Defend against contagion.** Where an evaluator/critic judges agents' work, use redundancy (a small committee / multiple independent checks) rather than a single evaluator whose error spreads; flag homogeneous-model cascades.

9. **Set shared stopping conditions.** Define the run-level "done," per-agent/session termination, max handoffs/iterations, and the cap-fallback (escalate vs best-effort). Cross-link `multiagent_graceful_session_endings.md` for session boundaries.

10. **Write durable handoff memory.** If a project continuity memory system exists, write or update the handoff/session records and promote durable decisions, failed attempts, traps, or open questions to their canonical files. Cross-link `aiagent_project_memory_capture_protocol.md`.

**Output Format:**

A markdown handoff-and-recovery design:
- **Handoff Map** — boundary | data crossed | coupling | irreversible effects
- **Handoff Record** — payload schema (result + context/trace + implicit decisions + IDs/hash)
- **Cross-Tool / Cross-Session Fields** — branch, commit, dirty files, active decisions, attempts to avoid, next action, verification
- **Handoff Verification** — gate criteria + reject/escalate behavior
- **Failure Isolation** — how a downstream failure is contained; what is checkpointed
- **Cross-Boundary Recovery** — resume the failed agent/session vs compensate; compensations + order
- **Attribution** — IDs/records that localize a failure
- **Contagion Defense** — evaluator redundancy where applicable
- **Shared Stopping Conditions** — run-level done + per-agent termination + caps + fallback
- **Project-Memory Writeback** — what gets captured into decisions/attempts/handoff/open questions

## Verification

- [ ] Each handoff carries full relevant context/trace and the implicit decisions, not just a summary.
- [ ] Cross-tool/session handoffs include branch/commit, next action, active decisions, attempts to avoid, open questions, and verification commands.
- [ ] A verification gate validates handoffs before the receiving agent/session acts.
- [ ] A downstream failure is isolated; completed agents' valid work is checkpointed, not discarded.
- [ ] Cross-boundary recovery is defined: resume the failed agent/session or compensate committed irreversible effects (in order).
- [ ] Handoffs/actions carry IDs so failures can be attributed without relying on auto-localization.
- [ ] Evaluator redundancy guards against error contagion where a critic judges agents.
- [ ] Shared stopping conditions and a common "done" prevent premature termination and runaway loops.
- [ ] Durable handoff facts are captured into project continuity memory where applicable.

## False-Positive Prevention

❌ **DON'T:**
- Pass only summarized messages between agents when downstream decisions depend on upstream reasoning.
- Restart the whole run because one downstream agent/session failed.
- Assume a model can reliably tell you which agent broke a long trace.
- Rely on a single evaluator whose mistake then propagates to other agents.
- Spawn parallel agents without a shared "done" and handoff caps.
- Trust a cross-tool handoff that lacks branch, commit, and verification context.

✅ **DO:**
- Hand off full context/traces + the implicit decisions, with trace IDs and a content hash.
- Verify each handoff before acting; isolate and checkpoint so a failure is contained.
- Resume only the failed agent/session from the last valid handoff; compensate committed effects in reverse order.
- Build explicit attribution records; use evaluator redundancy to damp contagion.
- Define shared stopping conditions and a common acceptance gate up front.
- Promote durable handoff facts into `.project-memory/` when cross-session continuity matters.

## Example Output

```markdown
## Handoff & Recovery: Claude Code → Codex auth refactor

### Handoff Map
| Boundary | Data crossed | Coupling | Irreversible? |
|---|---|---|---|
| Claude Code → Codex | patch summary + failing test + decisions + branch state | high | none yet |

### Cross-Tool / Cross-Session Fields
{from_tool: claude-code, to_tool: codex, branch: feature/auth, commit: abc123, dirty_files: [auth.ts, auth.test.ts], active_decisions: [dec_auth_tenant_boundary], failed_attempts_to_avoid: [att_full_rewrite], next_action: "make tenant resolver test pass", verification_commands: ["npm test -- auth.test.ts"], stale_after: "2026-06-28"}

### Handoff Verification
Codex must confirm branch/commit match and read `dec_auth_tenant_boundary` before editing. If branch differs, pause and ask human.

### Failure Isolation
Claude Code's completed failing test and decision notes remain valid. Codex failure does not discard them.

### Project-Memory Writeback
Update `.project-memory/handoff.md`; create session record; promote the failed full rewrite to `attempts/` if not already present.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** map → record → verify → isolate → recover → attribute → writeback → stop.
- **CM-02 (Constraint Specification):** full-context handoffs, failure isolation, and shared stopping conditions are governing constraints.
- **AG-29 (Agent Loop Architecture):** recovery is expressed in terms of handoff boundaries, pivots, checkpoints, and the orchestrator's control of the fleet.
- **QA-12 (False Positives Identification):** handoff verification + evaluator redundancy prevent bad handoffs and contagion from passing as success.
- **QA-01 (Self-Verification):** the checklist enforces contained failures and attributable, recoverable handoffs.

**Related Prompts:**
- `aiagent_project_continuity_memory_design.md` — portable repo-local project memory that stores durable handoff facts.
- `aiagent_project_memory_capture_protocol.md` — write protocol for sessions, decisions, attempts, and handoffs.
- `aiagent_inter_agent_communication_protocol.md` — the message-schema/shared-state protocol the handoff record builds on.
- `aiagent_multi_agent_orchestration.md` — decide whether to split into multiple agents before designing handoffs.
- `aiagent_failure_recovery_rescope.md` — the per-failure resume/compensate/re-scope decision this design invokes.
- `multiagent_graceful_session_endings.md` — checkpoint/restart at session boundaries.
