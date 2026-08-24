---
title: "AI Agent Durable Execution & State Persistence Design"
category: AI-ML/agentic-ai-systems
description: "Design how a long-running agent persists state, checkpoints progress, and resumes after a crash or interruption — including idempotent replay and cross-session continuation — so a failure doesn't lose work or repeat irreversible actions."
techniques:
  - ST-02
  - CM-02
  - AG-29
  - QA-12
  - QA-01
difficulty: advanced
tags:
  - durable-execution
  - checkpointing
  - state-persistence
  - crash-recovery
  - idempotent-replay
updated: "2026-06-18"
related_prompts:
  - domain-AI-ML/agentic-ai-systems/aiagent_architecture_design.md
  - domain-agentic-resources/commands/multi-agent/multiagent_graceful_session_endings.md
  - domain-prompt-engineering/agent-workflows/agent_state_summary_for_compaction.md
---

# AI Agent Durable Execution & State Persistence Design

**Objective:** Design how a long-running agent survives interruption — what state is persisted, where checkpoints fall, how it resumes after a crash without losing progress or re-running irreversible actions, and how it continues across sessions — so durability is a property of the design, not a hope that nothing crashes.

**When to Use:**
- An agent runs long enough (minutes to days, or across sessions) that a crash, deploy, or timeout mid-task is likely.
- The agent takes irreversible actions and a naive retry would repeat them (double-send, double-charge).
- Work must survive a process restart or hand off cleanly between sessions/operators.

**When NOT to Use:**
- The task is short and cheap enough that re-running from scratch on failure is acceptable — durability machinery isn't worth it.
- You only need the prompt that produces a resume-ready state summary — use `domain-prompt-engineering/agent-workflows/agent_state_summary_for_compaction.md`.
- You need the multi-agent checkpoint-and-restart *protocol* for session boundaries — use `domain-agentic-resources/commands/multi-agent/multiagent_graceful_session_endings.md` and cross-link.

## Inputs / Context

Provide what you can; the design degrades gracefully if some are missing:
- **Run duration & interruption risk** — how long a task runs and what can interrupt it (crash, deploy, timeout, session end).
- **Irreversible actions** — external/state-changing actions that must not be repeated on resume.
- **State to preserve** — the minimal set the agent needs to continue (progress, intermediate artifacts, plan position).
- **Recovery objective** — acceptable lost work (RPO) and acceptable resume latency (RTO).
- **Storage** — available durable store (DB, object store, queue) and its consistency guarantees.

## Constraints

**Must:**
- Define the minimal durable state that lets the agent resume, and the checkpoint points where it is written atomically.
- Make every irreversible action idempotent (deterministic operation key + dedup record written before/with the action) so replay after a crash cannot repeat it.
- Define the recovery procedure: on restart, how the agent detects an in-flight task, loads state, and continues from the last good checkpoint.
- State the recovery objective (max acceptable lost progress) and confirm the checkpoint cadence meets it.

**Must Not:**
- Hold task-critical state only in process memory or the context window where a crash loses it.
- Implement retry/resume without idempotency keys for irreversible actions (replays cause double-effects).
- Checkpoint so coarsely that a crash loses an unacceptable amount of work, or so finely it dominates cost.
- Assume the durable store is always consistent/available — name its guarantees and the failure handling.

**Instructions:**

1. **Profile interruption risk and the recovery objective.** State what can interrupt the run and how much progress loss (RPO) and resume delay (RTO) are acceptable. This sizes the checkpoint cadence.

2. **Define the minimal durable state.** Identify the smallest state needed to resume: plan position, completed-step record, intermediate artifacts (or references), and outstanding-action ledger. Keep it small and serializable.

3. **Place checkpoints.** Specify where state is durably written — after each completed step, before each irreversible action, and at session boundaries — and that each write is atomic (no half-written checkpoint).

4. **Make irreversible actions idempotent.** For each external/state-changing action, define a deterministic operation key and a dedup record written transactionally so a replay detects "already done" and skips it.

5. **Design the recovery procedure.** On startup: detect an in-flight task, load the latest valid checkpoint, reconcile the outstanding-action ledger (what was attempted vs. confirmed), and resume from the last good step.

6. **Handle ambiguous in-flight actions.** Define what happens to an action that was issued but whose outcome is unknown after a crash (query for completion, treat the op-key as the source of truth) — never blindly retry.

7. **Define cross-session continuation.** Specify how a session boundary persists state and how a new session (or operator) resumes — cross-link `multiagent_graceful_session_endings.md` for the multi-agent case.

8. **Account for the cost of durability.** Estimate the storage and latency overhead of checkpointing and confirm it's justified by the run length and irreversibility risk.

**Output Format:**

A markdown design doc:
- **Interruption Risk & Recovery Objective** — RPO/RTO
- **Durable State** — minimal serializable state to resume
- **Checkpoint Points** — where + atomicity guarantee
- **Idempotency** — action | operation-key | dedup mechanism
- **Recovery Procedure** — detect → load → reconcile → resume
- **Ambiguous-Action Handling**
- **Cross-Session Continuation** — cross-link
- **Durability Cost** — overhead vs. benefit

## Verification

- [ ] The minimal durable state is sufficient to resume any in-flight task.
- [ ] Checkpoint cadence meets the stated RPO; writes are atomic.
- [ ] Every irreversible action has a deterministic op-key and dedup record — replay can't double-fire.
- [ ] The recovery procedure detects in-flight work, reconciles the action ledger, and resumes correctly.
- [ ] Actions with unknown post-crash outcome are reconciled, not blindly retried.
- [ ] Durability overhead is justified against run length and irreversibility risk.

## False-Positive Prevention

❌ **DON'T:**
- Call an agent "resumable" when its working state lives only in memory or the context window.
- Add retries/resume without idempotency keys and assume actions won't be replayed.
- Treat a crashed-mid-action task as "failed, retry from scratch" when the action may have succeeded.
- Checkpoint after the whole task only, losing hours of work on a late crash.

✅ **DO:**
- Persist a minimal, serializable resume state at well-placed atomic checkpoints.
- Give every irreversible action a deterministic op-key with a transactional dedup record.
- Reconcile the outstanding-action ledger on recovery before resuming.
- Size checkpoint cadence to the stated RPO and the cost of lost work.

## Example Output

```markdown
## Durable-Execution Design: Bulk Invoice-Reconciliation Agent (runs ~2h, sends emails)

### Interruption Risk & Recovery Objective
Risks: deploy, timeout, crash mid-run. RPO: ≤1 processed invoice of lost progress. RTO: resume <60s.

### Durable State
{run_id, cursor (last invoice id done), results[], outstanding_actions[]}. Stored in a DB row per run; artifacts by reference.

### Checkpoint Points
After each invoice processed (cursor advance, atomic). Before each email send (record intent). At session end.

### Idempotency
| Action | Op-key | Dedup |
|---|---|---|
| Send dispute email | hash(invoice_id, run_id) | unique row in sent_actions before send |

### Recovery Procedure
On start: find runs with status=in_flight → load row → for each outstanding action, check sent_actions by op-key → resume from cursor+1.

### Ambiguous-Action Handling
Email issued but unconfirmed: op-key present in sent_actions → treat as sent (don't resend); absent → safe to send.

### Cross-Session Continuation
Run row persists across sessions; any worker can pick up by run_id. See `multiagent_graceful_session_endings.md`.

### Durability Cost
1 small DB write/invoice (~ms). Justified: 2h runtime + irreversible sends make from-scratch retry unacceptable.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** risk → state → checkpoints → idempotency → recovery.
- **CM-02 (Constraint Specification):** RPO/RTO and atomicity are the governing constraints.
- **AG-29 (Agent Loop Architecture):** checkpoints and resume are designed into the control loop, not bolted on.
- **QA-12 (False Positives Identification):** idempotency dedup prevents replays from re-firing irreversible actions.
- **QA-01 (Self-Verification):** the checklist enforces resumability and no-double-effect.

**Related Prompts:**
- `aiagent_architecture_design.md` — the control loop these checkpoints live in.
- `domain-agentic-resources/commands/multi-agent/multiagent_graceful_session_endings.md` — multi-agent checkpoint/restart at session boundaries.
- `domain-prompt-engineering/agent-workflows/agent_state_summary_for_compaction.md` — produce a resume-ready state summary.
