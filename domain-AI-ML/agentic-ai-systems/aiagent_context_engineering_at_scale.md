---
title: "AI Agent Context Engineering at Scale"
category: AI-ML/agentic-ai-systems
description: "Design what occupies an agent's active context window over a long or multi-agent run — context budget allocation, hierarchical layers (scratch/episode/principles), incremental compaction, session-resume packets, and sub-agent context isolation — so the agent neither overflows nor rots as the task grows."
techniques:
  - ST-02
  - CM-02
  - RT-02
  - QA-12
  - QA-01
difficulty: advanced
tags:
  - context-engineering
  - context-window
  - compaction
  - context-isolation
  - context-rot
updated: "2026-06-25"
related_prompts:
  - domain-AI-ML/agentic-ai-systems/aiagent_memory_design.md
  - domain-AI-ML/agentic-ai-systems/aiagent_project_continuity_memory_design.md
  - domain-AI-ML/agentic-ai-systems/aiagent_project_memory_guard_before_action.md
  - domain-AI-ML/agentic-ai-systems/aiagent_durable_execution_state_persistence.md
  - domain-prompt-engineering/agent-workflows/agent_state_summary_for_compaction.md
---

# AI Agent Context Engineering at Scale

**Objective:** Design how an agent's *active context window* is managed across a long-running or multi-agent task — how the token budget is allocated across instructions, working state, and retrieved content; how context is layered and compacted as the run grows; how session-resume packets are assembled; and how sub-agents are kept from polluting each other's context — so the agent stays coherent instead of overflowing or degrading into context rot.

**When to Use:**
- A task runs long enough that observations, tool outputs, and history outgrow the context window.
- An agent gets less reliable as a session lengthens (forgets early instructions, contradicts itself, latency/cost climbs).
- A multi-agent system shares too much context, so one agent's noise degrades another's reasoning.
- A future session or different agent needs a bounded, high-signal resume packet rather than raw transcript history.

**When NOT to Use:**
- The task fits comfortably in one context window and never grows — context engineering is unnecessary.
- You're designing the persistent memory store (what's saved/retrieved/forgotten across tasks) — use `aiagent_memory_design.md`. This prompt is about the *active window*, not the store.
- You're designing portable repo-local project continuity memory across humans, tools, agents, and devices — use `aiagent_project_continuity_memory_design.md`, then use this prompt to decide what enters the active context window.
- You only need the prompt that writes a resume-ready state summary — use `domain-prompt-engineering/agent-workflows/agent_state_summary_for_compaction.md`.

## Inputs / Context

Provide what you can; the design degrades gracefully if some are missing:
- **Context window size** — the model's token limit and the realistic usable fraction.
- **What fills the window over time** — instructions, tool outputs, intermediate artifacts, history, retrieved docs.
- **Load-bearing content** — the facts/instructions that must never be dropped or summarized away.
- **Run length** — how many steps/turns a task typically runs before completion.
- **Session-resume needs** — what a fresh session must know immediately: next action, decisions, blockers, failed attempts, branch/commit, and verification commands.
- **Multi-agent sharing** — whether sub-agents share a window or each gets an isolated one.

## Constraints

**Must:**
- Allocate the context budget explicitly across fixed layers (system/instructions, durable working state, transient observations, retrieved content) with a reserve so the window never hard-overflows.
- Define a compaction policy: what is summarized, what is dropped, and what is pinned (never compacted) — and the trigger that fires it.
- Verify that compaction is lossless for load-bearing facts: the agent can still recover the information that drives its decisions after a compaction.
- Define a bounded session-resume packet when work may cross sessions or agents; it should point to canonical memory records rather than copying raw history.
- For multi-agent runs, isolate sub-agent contexts by default and pass only the typed handoff payload, not raw history.

**Must Not:**
- Let the window fill until the model silently truncates the oldest (often the instructions).
- Summarize away load-bearing details (IDs, constraints, prior decisions) in the name of saving tokens.
- Re-inject the entire history each turn when a compacted state summary suffices.
- Share one giant shared context across all agents so noise and token cost compound.
- Treat a resume packet as the canonical project memory; it is a generated projection of the source records.

**Instructions:**

1. **Inventory what consumes context over the run.** List the content classes (instructions, working state, observations, retrieved docs, history) and how each grows with steps.

2. **Allocate a context budget.** Assign a token share (or priority order) to each class, with a reserve headroom. Pin the always-present layer (system + load-bearing instructions) so it's never evicted.

3. **Define the context layers.** Separate short-term scratch (current step), medium-term episode state (this task's durable summary), and long-term principles (stable rules). Decide what lives in each and how they're refreshed.

4. **Specify the compaction policy and trigger.** Define when compaction fires (budget threshold, step count) and the operation: summarize transient history into the episode state, drop superseded observations, keep pinned content verbatim.

5. **Protect load-bearing facts.** Identify the facts that must survive compaction (IDs, constraints, decisions) and route them to a pinned or structured store rather than free-text history that can be summarized away.

6. **Design retrieval-into-context.** Where the agent pulls external/large content, specify just-in-time retrieval with relevance + recency limits so the window holds only what the current step needs (cross-link RAG resources for the retrieval pipeline itself).

7. **Design the session-resume packet.** If work crosses sessions or tools, define the bounded packet loaded at start: project/task purpose, current focus, next action, live blockers, active decisions, relevant failed attempts, known traps, open questions, branch/commit, likely files, and verification commands. Cross-link `aiagent_project_continuity_memory_design.md` for the canonical record system.

8. **Isolate sub-agent contexts.** For multi-agent runs, default each sub-agent to its own window and pass only the typed handoff (cross-link `aiagent_inter_agent_communication_protocol.md`), preventing cross-task context pollution.

9. **Measure context health.** Name the signals (window utilization, post-compaction recall of pinned facts, late-session error rate, resume-packet accuracy) that show whether the policy is working — cross-link `aiagent_observability_telemetry_design.md`.

**Output Format:**

A markdown design doc:
- **Context Consumers** — content classes + growth
- **Budget Allocation** — class | token share/priority | pinned?
- **Layers** — scratch / episode / principles + refresh
- **Compaction Policy** — trigger + summarize/drop/pin rules
- **Load-Bearing Protection** — facts routed to pinned/structured store
- **Retrieval-into-Context** — JIT relevance/recency limits
- **Session-Resume Packet** — contents, size cap, source records, stale/branch checks
- **Sub-Agent Isolation** — per-agent window + handoff payload
- **Context-Health Signals**

## Verification

- [ ] The context budget is allocated per class with reserve headroom and a pinned always-present layer.
- [ ] A compaction trigger and summarize/drop/pin policy are defined.
- [ ] Load-bearing facts are protected from being summarized away (pinned/structured).
- [ ] Retrieval into context is just-in-time and bounded, not dumped wholesale.
- [ ] Session-resume packet is bounded, source-linked, and not treated as canonical memory.
- [ ] Sub-agents are isolated by default; only typed handoffs cross.
- [ ] Context-health signals are named and cross-linked to telemetry.

## False-Positive Prevention

❌ **DON'T:**
- Let the window grow until the model silently truncates (usually evicting the instructions).
- Compress history into a summary that drops the IDs/constraints/decisions the agent needs next.
- Re-send the full transcript every turn when a compacted episode summary would do.
- Pool all agents into one shared context so noise and cost compound across the fleet.
- Use a stale resume packet without checking source records and branch/commit context.

✅ **DO:**
- Budget the window by content class with reserve headroom and a pinned core.
- Route load-bearing facts to a pinned or structured store that compaction can't erase.
- Compact transient history into a durable episode summary on a defined trigger.
- Build session-resume packets from canonical project memory records when cross-session continuity matters.
- Give each sub-agent its own window and pass only typed handoffs.

## Example Output

```markdown
## Context Design: Long-Running Migration Agent (~80 steps, 200k-token window)

### Context Consumers
Instructions (fixed), plan + completed-step ledger (grows slowly), tool outputs (grows fast), file snippets (transient).

### Budget Allocation
| Class | Share | Pinned? |
|---|---|---|
| System + rules | 8k | yes |
| Episode state (plan, ledger) | 20k | yes |
| Recent tool outputs | 60k | no (compacted) |
| JIT file snippets | 40k | no |
| Reserve | rest | — |

### Layers
Scratch = current step's tool output. Episode = plan + completed-step summary (refreshed each step). Principles = migration rules (static).

### Compaction Policy
Trigger at 70% utilization: summarize tool outputs older than 5 steps into the episode ledger; drop superseded file snippets; keep system + episode state verbatim.

### Load-Bearing Protection
File paths, chosen versions, and failed-step reasons written to the structured episode ledger (pinned), not left in free-text history.

### Retrieval-into-Context
File contents fetched JIT for the current step only, top-relevance, evicted after the step.

### Session-Resume Packet
At session boundary, generate a <=3k-token packet from canonical state: task, next action, completed steps, active decisions, failed attempts to avoid, open questions, branch/commit, and verification command. Do not include raw transcript.

### Sub-Agent Isolation
Sub-agent per package gets its own window; receives only {package, target_version, constraints} handoff. See `aiagent_inter_agent_communication_protocol.md`.

### Context-Health Signals
window_utilization, pinned-fact recall after compaction, resume-packet accuracy, late-session error rate. See `aiagent_observability_telemetry_design.md`.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** consumers → budget → layers → compaction → resume packet → isolation.
- **CM-02 (Constraint Specification):** the token budget, pinned layer, and resume-packet source rules are hard constraints.
- **RT-02 (Multi-Dimensional Analysis Framework):** trades token cost, recall, and coherence against each other.
- **QA-12 (False Positives Identification):** the load-bearing-recall and resume-packet checks catch summaries that silently drop needed facts.
- **QA-01 (Self-Verification):** the checklist enforces no-silent-truncation and protected facts.

**Related Prompts:**
- `aiagent_memory_design.md` — the persistent store behind the active window.
- `aiagent_project_continuity_memory_design.md` — portable project memory records used to build bounded resume packets.
- `aiagent_durable_execution_state_persistence.md` — persisting the episode state for resume.
- `domain-prompt-engineering/agent-workflows/agent_state_summary_for_compaction.md` — the prompt that writes the compacted summary.
