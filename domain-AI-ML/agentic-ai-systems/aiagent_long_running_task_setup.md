---
title: "Long-Running Agentic Task Setup"
category: AI-ML/agentic-ai-systems
description: "Configure a single coherent setup for an agent task that runs for minutes-to-days or across sessions — durable workflow, idempotent side effects, compensation for irreversible actions, durable human-approval waits, long-horizon context/memory strategy, observability, and a consistency eval — so the run survives crashes, deploys, and context overflow without losing work or repeating irreversible actions."
techniques:
  - ST-02
  - CM-02
  - AG-29
  - QA-01
  - QA-12
difficulty: advanced
tags:
  - long-running-agents
  - durable-execution
  - context-engineering
  - human-in-the-loop
  - reliability
updated: "2026-06-21"
related_prompts:
  - domain-AI-ML/agentic-ai-systems/aiagent_durable_execution_state_persistence.md
  - domain-AI-ML/agentic-ai-systems/aiagent_context_engineering_at_scale.md
  - domain-AI-ML/agentic-ai-systems/aiagent_human_in_the_loop_design.md
  - domain-AI-ML/agentic-ai-systems/aiagent_observability_telemetry_design.md
  - domain-AI-ML/agentic-ai-systems/aiagent_cost_token_budget_design.md
  - domain-prompt-engineering/agent-workflows/agent_loop_termination_designer.md
  - domain-engineering-workflows/done-definition/done_definition_stop_policy.md
---

# Long-Running Agentic Task Setup

**Objective:** Produce one coherent, framework-neutral setup for a task an agent must run over a long horizon (minutes to days, or across sessions) so the run is reliable by construction — it survives crashes/deploys/timeouts, stays coherent as context overflows the window, waits durably for humans, never repeats irreversible actions on resume, and is measured for *repeatable* success. This prompt stitches the individual long-running primitives (each covered by its own prompt) into a single recommended configuration; it does not replace them.

**When to Use:**
- A task runs long enough that a crash, deploy, timeout, rate-limit stall, or context-window overflow is *likely* before completion.
- Work spans more than one context window or more than one session.
- Restarting from scratch on failure is unacceptable (lost work, repeated side effects, blown token budget).

**When NOT to Use:**
- The task is short and cheap enough that re-running from scratch on failure is fine — skip the machinery.
- You only need one slice (just durability, just context strategy, just the eval) — use the specific prompt instead (see Related Prompts) and cross-link.
- You are deciding *whether the task needs an agent at all* — settle that first (deterministic workflow beats an agent by default).

## Inputs / Context

Provide what you can; the setup degrades gracefully if some are missing:
- **Task & horizon** — what the agent does, expected wall-clock duration, and whether it crosses sessions.
- **Irreversible actions** — external/state-changing actions that must not repeat on resume (send, charge, deploy, delete).
- **Interruption risks** — crash, deploy, timeout, rate-limit, human wait, context overflow.
- **Human-decision points** — where approval/judgment is required, and acceptable wait length.
- **Stack & substrate** — framework/runtime if chosen (durable-execution engine, checkpoint store), or "undecided."
- **Budget & SLOs** — token/cost ceiling, acceptable lost work (RPO), acceptable resume latency (RTO), and the reliability bar (target success rate at what task length).

## Constraints

**Must:**
- Choose a durability mechanism (durable workflow + journaled steps, or checkpoint-to-store) and state how the run resumes from the last completed step rather than restarting.
- Make every side-effecting action idempotent (stable operation key + dedup record) — journaled/retried steps run at-least-once.
- For each irreversible action, define either an idempotency guard or a compensating action (saga), and name the pivot (point of no return).
- Define the long-horizon context strategy (how the run stays coherent past one window: compaction, external notes/memory, sub-agent isolation, just-in-time retrieval) and bound the loop (max iterations + cap-fallback).
- Model human approval as a durable wait with a timeout, not a blocking process.
- Specify observability (trace/span schema) and a consistency-oriented acceptance check (repeatable success, not a single pass).

**Must Not:**
- Hold task-critical state only in process memory or the context window.
- Add retry/resume without idempotency keys for irreversible actions.
- Let memory or context accumulate unbounded (relevance-filter and compact — accumulation degrades recall).
- Treat "ran once for hours in a demo" as evidence of reliability — design for the reliability bar, not a single run.
- Re-author the underlying primitives here — reference the dedicated prompts and assemble.

**Instructions:**

1. **Size the horizon and reliability bar.** State expected duration, interruption risks, RPO/RTO, and the target success rate at the task's length. Note that demanding higher reliability sharply shortens usable task length, so plan to decompose long tasks into short, verifiable sub-tasks.
2. **Choose the durability mechanism.** Pick durable-workflow-with-journaled-steps or checkpoint-to-store; state where checkpoints fall (after each completed step, before each irreversible action, at session boundaries) and that writes are atomic. Cross-link `aiagent_durable_execution_state_persistence.md` for the detailed design.
3. **Make side effects safe.** List every side-effecting action; assign each a stable idempotency key + dedup record. For irreversible actions, mark the pivot and define a compensating action for everything before it (saga), and idempotent retry for everything after.
4. **Set the long-horizon context strategy.** Choose how coherence is maintained past one window — compaction near the limit, structured notes/external memory retrieved just-in-time, and/or sub-agents with clean windows returning condensed summaries. Add memory hygiene (relevance-filter on retrieval, dedup/conflict-resolve on write, treat the write path as untrusted). Cross-link `aiagent_context_engineering_at_scale.md` and `aiagent_memory_poisoning_defense.md`.
5. **Bound the loop and define stopping conditions.** Max iterations/tool-calls, falsifiable termination, and the cap-fallback (escalate vs return best-effort). Cross-link `agent_loop_termination_designer.md` and `done_definition_stop_policy.md`.
6. **Design durable human waits.** For each decision point, define the approval gate as a durable wait (the run persists and suspends, then resumes from the exact state) with a timeout/heartbeat and an escalation path. Cross-link `aiagent_human_in_the_loop_design.md`.
7. **Wire observability and self-healing.** Emit a trace/span per decision and tool call; on tool failure, surface the error to the agent and let it adapt within deterministic safeguards (bounded retries + checkpoints). Cross-link `aiagent_observability_telemetry_design.md`.
8. **Define the acceptance check.** Specify a consistency-oriented eval (repeat the task and require success across runs, not a single pass) plus cost/latency budget, before this setup is called production-ready.

**Output Format:**

A markdown setup doc:
- **Horizon & Reliability Bar** — duration, risks, RPO/RTO, target success@length
- **Durability** — mechanism, checkpoint points, atomicity
- **Side-Effect Safety** — action | op-key/dedup | reversible? | pivot/compensation
- **Context & Memory Strategy** — compaction / notes / sub-agents / retrieval + hygiene
- **Loop Bounds & Stopping** — caps + cap-fallback
- **Durable Human Waits** — decision point | wait mechanism | timeout | escalation
- **Observability & Self-Healing** — trace schema + failure-adaptation policy
- **Acceptance Check** — consistency eval + budget
- **Cross-links** — which dedicated prompts own each slice

## Verification

- [ ] The run resumes from the last completed step, not from scratch; checkpoint cadence meets RPO.
- [ ] Every side-effecting action has an idempotency key; every irreversible action has a guard or compensation and a named pivot.
- [ ] The context strategy keeps the run coherent past one window and bounds memory growth.
- [ ] The loop is bounded with a defined cap-fallback and falsifiable stopping conditions.
- [ ] Human approvals are durable waits with timeouts, not blocking calls.
- [ ] Observability covers every decision/tool call; failures are surfaced for adaptation, not hidden.
- [ ] Acceptance is measured as repeatable success (consistency), within the cost/latency budget.

## False-Positive Prevention

❌ **DON'T:**
- Call a setup "durable" when working state lives only in memory or the window.
- Add resume/retry without idempotency keys and assume actions won't replay.
- Compact or summarize so aggressively that load-bearing context is silently lost.
- Let long-lived memory grow unbounded and assume more context is better.
- Cite a single multi-hour demo run as proof of reliability.

✅ **DO:**
- Persist minimal serializable state at atomic checkpoints; resume from the last good step.
- Give every irreversible action an op-key or a compensating action, and name the pivot.
- Keep the smallest high-signal context; relevance-filter retrieval and validate the write path.
- Bound loops and memory; decompose long tasks into short, verifiable sub-tasks.
- Prove reliability with a consistency eval (repeat the task), not one lucky run.

## Example Output

```markdown
## Long-Running Setup: Nightly Multi-Repo Dependency-Upgrade Agent (~3–6h, opens PRs)

### Horizon & Reliability Bar
Duration 3–6h across ~40 repos; risks: CI rate-limits, deploys, timeout. RPO ≤1 repo; RTO <2 min. Bar: ≥95% of repos processed correctly across 5 nightly runs.

### Durability
Durable workflow; one journaled step per repo. Checkpoint after each repo (cursor advance, atomic) and before each PR open.

### Side-Effect Safety
| Action | Op-key / dedup | Reversible? | Pivot/compensation |
|---|---|---|---|
| Open PR | hash(repo, run_date) → unique row | yes (close PR) | compensable |
| Post review comment | hash(repo, run_date, body) | yes | compensable |
PR open is the pivot per repo; everything before (branch, edits) is local/compensable.

### Context & Memory Strategy
Per-repo sub-agent with a clean window; returns a 1–2k-token summary. Lead keeps only the cursor + per-repo verdicts. Just-in-time file reads (grep/glob), no full-tree preload.

### Loop Bounds & Stopping
Max 2 fix attempts/repo; on cap → mark repo "needs human," continue. Global stop: end-of-window or all repos done.

### Durable Human Waits
Decision: PR that touches a lockfile policy → durable wait for approval (24h timeout → skip + flag). Run persists; resumes on approval.

### Observability & Self-Healing
Span per repo + per tool call. On CI rate-limit (tool failure) → surface to agent → bounded backoff retry; after 3 → escalate.

### Acceptance Check
Replay across 5 nights; require ≥95% repos correct each night; token budget ≤ $X/run.

### Cross-links
Durability → aiagent_durable_execution_state_persistence.md · Context → aiagent_context_engineering_at_scale.md · Waits → aiagent_human_in_the_loop_design.md · Bounds → done_definition_stop_policy.md
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** horizon → durability → side-effects → context → bounds → waits → observability → acceptance.
- **CM-02 (Constraint Specification):** RPO/RTO, idempotency, and the reliability bar are the governing constraints.
- **AG-29 (Agent Loop Architecture):** durability, bounds, and self-healing are designed into the control loop.
- **QA-01 (Self-Verification):** the checklist enforces resumability, bounded memory, and consistency-based acceptance.
- **QA-12 (False Positives Identification):** idempotency/compensation prevent replays from re-firing irreversible actions; consistency eval prevents "one good run = reliable."

**Related Prompts:**
- `aiagent_durable_execution_state_persistence.md` — the checkpoint/resume/idempotency detail this setup references.
- `aiagent_context_engineering_at_scale.md` — the compaction/notes/sub-agent context strategy.
- `aiagent_human_in_the_loop_design.md` — where approval gates fall and how they escalate.
- `aiagent_failure_recovery_rescope.md` — what to do when this setup's run fails or stalls.
