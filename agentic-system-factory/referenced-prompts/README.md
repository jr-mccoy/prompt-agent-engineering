# Referenced Prompts — Pointers, Not Copies

> **Decision D5 (reference, never move):** the factory **orchestrates** the repo's existing agent-design, acceptance-gate, observability, and governance prompts — it does not copy or relocate them. This file is the index of those pointers. Each factory stage's `References` section names the same prompts.
>
> The only files the factory *copies* (for self-containment, so an external dev can lift the directory out) are the **fill-in templates** in [`../templates/`](../templates/). Design *advice* stays in `domain-AI-ML/` etc. and is linked here.

If you copied `agentic-system-factory/` out of this repository, these paths are relative to the repo root and tell you which upstream prompt authors each part of the design. Treat them as the canonical, maintained source; the factory stays current by linking rather than duplicating.

---

## Stage 0 — Justify (complexity ladder / Gate 0)
- ⭐ `domain-AI-ML/agentic-ai-systems/aiagent_complexity_ladder_gate.md` — agent vs. deterministic workflow, lowest-rung-first.
- `domain-AI-ML/agentic-ai-systems/aiagent_multi_agent_orchestration.md` — when (and when not) to split to multi-agent.
- `domain-engineering-workflows/ai-patterns/ai_pattern_agent_task_code_distance_scorer.md` — Delegate / Decompose / DIY scorer.

## Stage 1 — Scope
- ⭐ `domain-engineering-workflows/done-definition/done_definition_translator.md` — fuzzy goal → observable, checkable gates.
- `domain-engineering-workflows/ai-patterns/ai_pattern_intent_and_verification_first.md` — intent + verification + out-of-scope.
- `domain-engineering-workflows/ai-patterns/ai_pattern_outcome_language_translator.md` — implementation → outcome language.

## Stage 2 — Topology
- ⭐ `domain-AI-ML/agentic-ai-systems/aiagent_orchestration_topology_selection.md` — scorecard topology selector.
- `domain-AI-ML/agentic-ai-systems/aiagent_planning_decomposition_design.md` — plan/decomposition design.
- `domain-engineering-workflows/ai-patterns/ai_pattern_agent_work_loop_design.md` — run-time agent loop.

## Stage 3 — Architecture
- ⭐ `domain-AI-ML/agentic-ai-systems/aiagent_architecture_design.md` — agent architecture (loop, state, control).
- `domain-AI-ML/agentic-ai-systems/aiagent_tool_design.md` — ACI tool design.
- `domain-AI-ML/agentic-ai-systems/aiagent_memory_design.md` — memory design.
- `domain-AI-ML/agentic-ai-systems/aiagent_project_continuity_memory_design.md` — portable, repo-local project continuity memory across humans, sessions, agents, tools, and devices.
- `domain-AI-ML/agentic-ai-systems/aiagent_project_memory_capture_protocol.md` — low-friction write protocol for sessions, decisions, attempts, traps, questions, and handoffs.
- `domain-AI-ML/agentic-ai-systems/aiagent_project_memory_guard_before_action.md` — pre-action guard that checks proposed work against prior project memory.
- `domain-AI-ML/agentic-ai-systems/aiagent_project_memory_interop_adapter_design.md` — plain-file, CLI, MCP, hook, and agent-signpost adapter design.
- `domain-AI-ML/agentic-ai-systems/aiagent_cost_token_budget_design.md` — per-task cost/budget.
- `domain-AI-ML/agentic-ai-systems/aiagent_context_engineering_at_scale.md` — compaction / notes / sub-agent isolation.
- `domain-AI-ML/agentic-ai-systems/aiagent_failure_mode_analysis.md` — failure-mode seeding.
- `domain-AI-ML/genai-llm-engineering/` — RAG / retrieval when memory is retrieval-backed.

## Stage 4 — Gates (security / HITL / kill switch — Gate A)
- ⭐ `domain-AI-ML/agentic-ai-systems/aiagent_hard_gates_designer.md` — composes OWASP-ASI/eval/governance into enforced Gate A/B/C + kill switch.
- `domain-AI-ML/agentic-ai-systems/aiagent_human_in_the_loop_design.md` — where to place HITL gates.
- `domain-AI-ML/agentic-ai-systems/aiagent_runtime_guardrails_policy.md` — how to enforce guardrails.
- `domain-AI-ML/agentic-ai-systems/aiagent_prompt_injection_untrusted_content_defense.md` — indirect-injection defense.
- `domain-AI-ML/agentic-ai-systems/aiagent_agentic_threat_model.md` — threat model.
- `domain-AI-ML/agentic-ai-systems/aiagent_memory_poisoning_defense.md` — memory and retrieved-context integrity defense.
- `domain-AI-ML/agentic-ai-systems/aiagent_project_memory_security_decay_audit.md` — stale/private/unsafe project-memory audit.
- `domain-AI-ML/agentic-ai-systems/aiagent_least_agency_scoping.md` — least-agency scoping.
- `domain-AI-ML/agentic-ai-systems/aiagent_zero_trust_maturity_assessment.md` — zero-trust maturity.

## Stage 5 — Eval (capability + safety — Gate B)
- ⭐ `domain-AI-ML/agentic-ai-systems/aiagent_agentic_safety_eval_layer.md` — ABC validity + OpenAgentSafety real-tool safety as a separate gate.
- `domain-AI-ML/agentic-ai-systems/aiagent_evaluation_design.md` — general agent eval.
- ⭐ `domain-engineering-workflows/done-definition/done_definition_verification_hardening.md` — close false-PASS loopholes.
- `domain-AI-ML/model-evaluation-validation/` — general eval substrate (error slicing, baselines, A/B).

## Stage 6 — Assemble / run / observe (Gate C)
- ⭐ `domain-engineering-workflows/done-definition/done_definition_loop_operator.md` — the work→check→retry→ship run loop.
- `domain-engineering-workflows/done-definition/done_definition_stop_policy.md` — stop policy.
- `domain-AI-ML/agentic-ai-systems/aiagent_observability_telemetry_design.md` — design-time observability.
- `domain-AI-ML/agentic-ai-systems/aiagent_durable_execution_state_persistence.md` — checkpoint/resume.
- `domain-AI-ML/agentic-ai-systems/aiagent_deployment_serving_architecture.md` — deploy/serve.
- `domain-AI-ML/production-monitoring/` — operational runbooks (drift, SLOs, dashboards, canary/shadow, rollback, incident postmortems).
- ⭐ `domain-AI-ML/responsible-ai-governance/rai_documentation_suite_orchestrator.md` — disclosure-bundle orchestration (adapt for the agent manifest).
- `domain-AI-ML/responsible-ai-governance/rai_model_risk_register.md` — living risk register (parameterize for agent risks).

## Stage 7 — Code-gen (optional, gated on a committed stack)
- `domain-AI-ML/learning-ai-ml/notebook-to-production/mllearn_n2p_01..04` — package → reproducible pipeline → serve → deploy/monitor/CI-CD scaffold.
- Per-stack playbooks (one per supported framework) for the deployment slice.
- Factory-local stack guides (all six Stage-7 targets): [`../stacks/claude-agent-sdk.md`](../stacks/claude-agent-sdk.md), [`../stacks/langgraph.md`](../stacks/langgraph.md), [`../stacks/openai-agents-sdk.md`](../stacks/openai-agents-sdk.md), [`../stacks/google-adk.md`](../stacks/google-adk.md), [`../stacks/microsoft-agent-framework.md`](../stacks/microsoft-agent-framework.md), [`../stacks/llamaindex.md`](../stacks/llamaindex.md).

## Improve (optional, post-deploy)
- `domain-AI-ML/agentic-ai-systems/aiagent_self_improvement_online_adaptation.md`
- `domain-AI-ML/agentic-ai-systems/aiagent_fleet_cost_attribution_optimization.md`
- `domain-AI-ML/production-monitoring/` drift / retraining-trigger / feedback-loop prompts.

---

## The authoring system this factory operationalizes
- `authoring/system-patterns/SYSTEM_QUICK_START.md` — the 6-step process the stages implement.
- `authoring/system-patterns/SYSTEM_PATTERN_INDEX.md` — the 9-topology catalog + safety/context/eval patterns.
- `authoring/system-patterns/SYSTEM_QUALITY_RUBRIC.md` — the 100-pt rubric `scripts/score_rubric.py` mirrors.
- `authoring/system-patterns/SYSTEM_USE_CASE_LOOKUP.md` — "I need X" → topology + gates.
