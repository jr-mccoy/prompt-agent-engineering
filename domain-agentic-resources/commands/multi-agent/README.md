# Multi-Agent Architecture Prompts

**Scope:** Design and diagnosis prompts for engineers building or running multi-agent AI systems — whether with the Claude Agent SDK, LangGraph, CrewAI, or hand-rolled orchestration. These are not orchestration workflows themselves; they are design-time and audit-time prompts for the architectural decisions that make the difference between a multi-agent system that earns its coordination cost and one that burns it.

**When to use this subfolder:**
- You're deciding whether to split a single-agent task into multiple agents at all
- You're designing a planner / worker / judge pattern for the first time
- A running multi-agent system is slow, brittle, or producing conflicts and you need to find the root cause
- You're tightening a worker's scope, minimizing its tool set, or designing its session boundaries
- You're defining the acceptance contract that judge agents (or human reviewers) will apply

**When NOT to use this subfolder:**
- You need a one-shot code analysis — use `domain-software-engineering/analysis/`
- You want a specific orchestration workflow to run — see `commands/orchestration/`
- You're improving how a single agent handles a single task — see `domain-engineering-workflows/ai-patterns/`
- You're building the agent persona itself — see `../../authoring/agent-patterns/`

---

## Prompts

### Design-time (choose architecture; set boundaries)
| File | What it does |
|------|--------------|
| [`multiagent_scaling_vs_single_agent_diagnosis.md`](multiagent_scaling_vs_single_agent_diagnosis.md) | Diagnoses whether the single-agent setup actually needs multi-agent or just needs fixing — biased toward not splitting |
| [`multiagent_two_tier_architecture_template.md`](multiagent_two_tier_architecture_template.md) | Produces a filled-in planner / worker / judge architecture with named contracts, handback protocol, and fallbacks |
| [`multiagent_worker_isolation_boundaries.md`](multiagent_worker_isolation_boundaries.md) | Defines Read / Write / Invoke / Spend boundaries for a worker with allowlists, invariants, and violation behavior |
| [`multiagent_tool_set_minimization.md`](multiagent_tool_set_minimization.md) | Classifies each of an agent's tools as Always-On / On-Demand / Remove and produces the minimized always-on set |
| [`multiagent_graceful_session_endings.md`](multiagent_graceful_session_endings.md) | Designs checkpoint + restart protocol for sessions that end on convergence, hard limits, soft pauses, or failure |
| [`multiagent_good_enough_gate_design.md`](multiagent_good_enough_gate_design.md) | Separates pass/fail gates from graded criteria, produces the judge's enumerated acceptance contract |

### Audit-time (find the real problem in a running system)
| File | What it does |
|------|--------------|
| [`multiagent_coordination_choke_point_analysis.md`](multiagent_coordination_choke_point_analysis.md) | Surfaces contention — serial dependencies, shared writable state, rate limits, coordinator bottlenecks — with Impact × Likelihood ranking |
| [`multiagent_coordination_via_tests_and_policy.md`](multiagent_coordination_via_tests_and_policy.md) | Replaces inter-agent chat with a shared test surface and a deterministic conflict-resolution policy |

---

## Typical flow

1. **Decide whether to split at all** — `multiagent_scaling_vs_single_agent_diagnosis.md`. The default answer is no; you'll often find a single-agent fix first.
2. **If splitting, design the architecture** — `multiagent_two_tier_architecture_template.md` for planner / worker / judge, then `multiagent_worker_isolation_boundaries.md` for each worker, then `multiagent_tool_set_minimization.md` to trim each agent's always-on tools.
3. **Design for survival** — `multiagent_graceful_session_endings.md` (how sessions end), `multiagent_good_enough_gate_design.md` (how the judge decides).
4. **Design for coordination** — if multiple agents share state, `multiagent_coordination_via_tests_and_policy.md` defines how they coordinate through executable contracts rather than chat.
5. **Audit running systems** — `multiagent_coordination_choke_point_analysis.md` when a live system is slow, brittle, or expensive.

---

## Core techniques used across this subfolder

| Technique | What it contributes |
|-----------|---------------------|
| ST-01 Clear Objective Statement | Every prompt produces a narrow, specific artifact (template, classification, policy) rather than general guidance |
| ST-02 Structured Sequential Instructions | Ordered pipelines force diagnosis before prescription |
| RT-02 Multi-Dimensional Analysis | Failures, conflicts, and tool choices scored across orthogonal axes |
| CM-02 Constraint Specification | Must / Must Not rules block the common "add a critic agent" / "make everything a gate" reflexes |
| DD-04 MVP Gates | Judge-contract and sanity checklists gate the design on load-bearing decisions |
| QA-08 Gate-Based Verification | Acceptance criteria and coordination tests become the downstream pass/fail contract |

---

## Related subfolders

- [`../orchestration/`](../orchestration/) — specific orchestration workflows that use multi-agent architectures (not design prompts)
- [`../../../domain-engineering-workflows/ai-patterns/`](../../../domain-engineering-workflows/ai-patterns/) — single-agent patterns for AI-augmented development, including agent task design
- [`../../../domain-engineering-workflows/done-definition/`](../../../domain-engineering-workflows/done-definition/) — gate-based convergence for agentic loops
- [`../../../authoring/agent-patterns/`](../../../authoring/agent-patterns/) — build an individual agent's persona and capabilities
