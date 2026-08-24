# Agentic AI Systems — Build-Focused Prompt Library

Design-time prompts for **engineering autonomous AI agents and larger multi-agent systems**. This subdirectory owns the *AI/ML-engineering design framing* — architecture decisions, tradeoff scorecards, reproducibility, and agentic False-Positive Prevention. It deliberately **cross-links, rather than re-implements**, the prompt-level control-flow templates and multi-agent contract templates that live elsewhere (see *What lives elsewhere* below).

Every prompt is `difficulty: advanced`, follows the domain [field guide](../field_guide.md) section order, and pairs task success with cost / latency / safety / trajectory evidence.

## How to use this directory

Read it as a build pipeline: **design one agent well → coordinate a fleet → run it durably → secure it → improve it.** Most projects start at *Design the agent* and pull in the later stages only when scale, autonomy, or production exposure demands them.

### Gate 0 — Justify the agent (before any design)
The prior question every credible source leads with: does this need an agent at all?

| Prompt | Use it to |
|---|---|
| [`aiagent_complexity_ladder_gate.md`](aiagent_complexity_ladder_gate.md) | Walk the use case down the complexity ladder (function → direct call → workflow → agent → multi-agent) and stop at the lowest rung that works; produce the written agent-justification or recommend a workflow and STOP. |

### Stage 0 — Design the agent (foundations)
Start here for any single agent. Establish the architecture before adding coordination or scale.

| Prompt | Use it to |
|---|---|
| [`aiagent_architecture_design.md`](aiagent_architecture_design.md) | Choose planning approach, tool set, memory, control loop, and stopping conditions from task + risk. |
| [`aiagent_tool_design.md`](aiagent_tool_design.md) | Design tool/function interfaces — schemas, error contracts, idempotency, least privilege. |
| [`aiagent_memory_design.md`](aiagent_memory_design.md) | Design short/long-term memory — store, retrieve, summarize, forget — and its failure modes. |
| [`aiagent_cost_token_budget_design.md`](aiagent_cost_token_budget_design.md) | Set per-task token/cost/latency budgets with circuit breakers. |
| [`aiagent_evaluation_design.md`](aiagent_evaluation_design.md) | Design a reproducible eval scoring success + cost + latency + safety + trajectory. |
| [`aiagent_agentic_safety_eval_layer.md`](aiagent_agentic_safety_eval_layer.md) | Add the agentic layer on top of a general eval: ABC task/outcome-validity checks + the OpenAgentSafety 8-category real-tool safety eval as a **separate** gate from capability. |
| [`aiagent_failure_mode_analysis.md`](aiagent_failure_mode_analysis.md) | Enumerate and mitigate failure modes (loops, hallucinated calls, runaway cost, stalls). |
| [`aiagent_human_in_the_loop_design.md`](aiagent_human_in_the_loop_design.md) | Place approval gates and escalation thresholds calibrated to risk. |
| [`aiagent_safety_sandboxing.md`](aiagent_safety_sandboxing.md) | Bound blast radius by construction — permissions, isolation, oversight. |

### Stage A — Coordinate a fleet (multi-agent depth)
When one agent demonstrably can't do the job. Decide *whether* to split first, then *how* to coordinate.

| Prompt | Use it to |
|---|---|
| [`aiagent_multi_agent_orchestration.md`](aiagent_multi_agent_orchestration.md) | Decide **whether** a task warrants multiple agents (single-agent baseline first). |
| [`aiagent_planning_decomposition_design.md`](aiagent_planning_decomposition_design.md) | Design the **planner** — decomposition strategy, plan representation, replanning triggers. |
| [`aiagent_orchestration_topology_selection.md`](aiagent_orchestration_topology_selection.md) | Select the **topology** (manager-worker, pipeline, fan-out, debate, blackboard, market) on a scorecard. |
| [`aiagent_inter_agent_communication_protocol.md`](aiagent_inter_agent_communication_protocol.md) | Design the **protocol** — message schemas, shared state, handoff contracts, conflict reconciliation. |
| [`aiagent_task_routing_load_balancing.md`](aiagent_task_routing_load_balancing.md) | Allocate work across a **pool** — routing, sizing, backpressure, retry-vs-escalate. |
| [`aiagent_cross_agent_handoff_recovery.md`](aiagent_cross_agent_handoff_recovery.md) | Design **handoffs + recovery** so a downstream agent failure (A→B, B fails) is contained, attributable, and recoverable — full-context handoffs, isolation, cross-boundary compensation, evaluator redundancy. |
| [`aiagent_orchestrator_generator.md`](aiagent_orchestrator_generator.md) | Emit the **master orchestrator** for a multi-stage system/toolkit — entry-stage classifier, recommend-next, per-stage critique, gate enforcement, in guided/manual/surgical modes. |

### Stage B — Run it durably (runtime & reliability)
Moving from demo to production traffic and long-running tasks.

| Prompt | Use it to |
|---|---|
| [`aiagent_observability_telemetry_design.md`](aiagent_observability_telemetry_design.md) | Design the **telemetry** — event/span schema, trajectory traces, dashboards, alerts. |
| [`aiagent_durable_execution_state_persistence.md`](aiagent_durable_execution_state_persistence.md) | Make long runs **survive interruption** — checkpoint/resume, crash recovery, idempotent replay. |
| [`aiagent_deployment_serving_architecture.md`](aiagent_deployment_serving_architecture.md) | Design the **serving substrate** — sync/async, concurrency, config versioning, shadow/canary rollout. |
| [`aiagent_context_engineering_at_scale.md`](aiagent_context_engineering_at_scale.md) | Manage the **active context window** — budget, layers, compaction, sub-agent isolation. |
| [`aiagent_project_continuity_memory_design.md`](aiagent_project_continuity_memory_design.md) | Design portable, repo-local **project continuity memory** across humans, sessions, agents, tools, and devices. |
| [`aiagent_project_memory_capture_protocol.md`](aiagent_project_memory_capture_protocol.md) | Design the low-friction write protocol for sessions, decisions, failed attempts, traps, ideas, questions, recovery records, and handoffs. |
| [`aiagent_project_memory_guard_before_action.md`](aiagent_project_memory_guard_before_action.md) | Design the pre-action guard that checks proposed work against prior decisions, failed attempts, known traps, open questions, stale memory, and branch context. |
| [`aiagent_project_memory_interop_adapter_design.md`](aiagent_project_memory_interop_adapter_design.md) | Design interop adapters for plain files, CLI, MCP resources/prompts/tools, hooks, and agent-specific signpost files. |
| [`aiagent_long_running_task_setup.md`](aiagent_long_running_task_setup.md) | Assemble one coherent **long-running setup** — durability, idempotent/compensated side effects, context strategy, durable human waits, observability, consistency eval. |
| [`aiagent_failure_recovery_rescope.md`](aiagent_failure_recovery_rescope.md) | Decide what to do **after a run fails/stalls** — triage (transient/systemic/spec), then resume vs compensate-and-rerun vs safely re-scope. |

### Stage C — Secure it (safety & security at scale)
Agent-specific security beyond sandbox isolation.

| Prompt | Use it to |
|---|---|
| [`aiagent_runtime_guardrails_policy.md`](aiagent_runtime_guardrails_policy.md) | Build the **enforcement layer** — input/output/action guardrails, policy-as-code, fail-closed gating. |
| [`aiagent_hard_gates_designer.md`](aiagent_hard_gates_designer.md) | Compose the security/eval/governance checks into enforced **Gate A/B/C + a kill switch**, sized to blast radius and tied to code/config locations (code-not-trust). |
| [`aiagent_agentic_threat_model.md`](aiagent_agentic_threat_model.md) | Threat-model instruction handling, tool/resource misuse, identity/privilege abuse, memory/context integrity, and supply-chain risks for a specific agentic system. |
| [`aiagent_memory_poisoning_defense.md`](aiagent_memory_poisoning_defense.md) | Defend persisted memory and retrieved context against integrity drift, shared-context contamination, rollback failure, and cross-session corruption. |
| [`aiagent_project_memory_security_decay_audit.md`](aiagent_project_memory_security_decay_audit.md) | Audit project continuity memory for stale, disputed, unsafe, private, or overgrown records before future agents rely on it. |
| [`aiagent_prompt_injection_untrusted_content_defense.md`](aiagent_prompt_injection_untrusted_content_defense.md) | Defend against hostile instructions embedded in read content — data/instruction separation and confused-deputy controls. |
| [`aiagent_privacy_data_governance.md`](aiagent_privacy_data_governance.md) | Keep sensitive data safe across **prompts, logs, traces, state** — minimization, redaction, audit, retention. |

### Stage D — Improve it (quality & evolution)
Operating and improving a live system.

| Prompt | Use it to |
|---|---|
| [`aiagent_simulation_staging_testing.md`](aiagent_simulation_staging_testing.md) | Test pre-deployment — failure-injection simulation, trace replay, regression suite, chaos/load. |
| [`aiagent_self_improvement_online_adaptation.md`](aiagent_self_improvement_online_adaptation.md) | Improve from production runs — trace mining, gated rule updates, drift detection, anti-gaming. |
| [`aiagent_fleet_cost_attribution_optimization.md`](aiagent_fleet_cost_attribution_optimization.md) | Cut spend at scale — attribution, model tiering, caching, batching, runtime budget enforcement. |

## What lives elsewhere (cross-link, don't duplicate)

This directory makes **design decisions**. The concrete prompt blocks and contract templates live in:

| If you need… | Go to |
|---|---|
| A **guided factory** that orchestrates these design prompts end-to-end into a gated, production-ready design bundle (the meta-layer that *uses* this directory) | [`agentic-system-factory/`](../../agentic-system-factory/) (built on `authoring/system-patterns/`) |
| Prompt-level control flow (loop termination, idempotency prompt, state-summary, subagent brief, observability event emission, self-correction) | `domain-prompt-engineering/agent-workflows/` |
| Multi-agent contract templates (planner/worker/judge, worker isolation, tool-set minimization, good-enough gates, graceful session endings, coordination via tests) | `domain-agentic-resources/commands/multi-agent/` |
| Tool-use patterns (description writing, routing, multi-tool DAG orchestration, failure recovery, dry-run) | `domain-prompt-engineering/tool-use/` |
| RAG pipeline patterns (query rewrite, grounding, citation, groundedness eval) | `domain-prompt-engineering/rag-prompts/` |
| Evaluation harnesses (correctness, regression, adversarial, rubrics) | `domain-prompt-engineering/evaluation/` |
| Single-agent lifecycle & auto-improving patterns (triplet diagnostic, metric-gaming pre-mortem, trace-infra audit, reflection) | `domain-engineering-workflows/ai-patterns/` |
| Generic OpenTelemetry / serving / cost infra | `domain-software-engineering/devops/`, `domain-AI-ML/mlops-infrastructure/` |
| LLM application security review | `domain-software-engineering/analysis/security/security_llm_application_review.md` |

## Conventions

- **File naming:** `aiagent_{function}.md`.
- **Frontmatter:** `title`, `category: AI-ML/agentic-ai-systems`, `description`, `techniques` (valid IDs from [`../../techniques/MASTER_TECHNIQUE_INDEX.md`](../../techniques/MASTER_TECHNIQUE_INDEX.md)), `difficulty`, `tags`, `updated`, `related_prompts`.
- **No-fabrication:** no invented cost, latency, throughput, or benchmark numbers — reason from the user's inputs and mark unknowns.
- **Framework-neutral:** the user names their runtime/stack; prompts avoid hardcoding drifting APIs.

## External references / further reading

The most directly actionable vendor-engineering write-ups behind this directory's design framing. These describe durable *patterns*, not drifting APIs; verify any version-specific detail against the current docs.

- Anthropic — [*Writing effective tools for AI agents*](https://www.anthropic.com/engineering/writing-tools-for-agents): the agent-computer-interface (ACI) / tool-design guide — schemas, errors-as-guidance, evaluating and optimizing tools. Pairs with `aiagent_tool_design.md`.
- Anthropic — [*How we built our multi-agent research system*](https://www.anthropic.com/engineering/multi-agent-research-system): the lead/subagent (orchestrator-workers) pattern, token-cost economics, and multi-agent coordination failure modes. Pairs with `aiagent_multi_agent_orchestration.md` and `aiagent_orchestration_topology_selection.md`.
- Anthropic — [*Effective context engineering for AI agents*](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents): compaction, agentic note-taking, and sub-agent context isolation for long / multi-agent runs. Pairs with `aiagent_context_engineering_at_scale.md`.
