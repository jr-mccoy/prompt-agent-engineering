# Agentic System Use-Case Lookup

**"I need X" → the lowest-complexity topology, the patterns to apply, and the gates that are mandatory.**

> Read top to bottom. The table is ordered by complexity — **stop at the first row that fits.** If an earlier row works, don't reach for a later one. Many rows resolve to "this isn't an agentic system — author a prompt or a workflow instead," which is the correct answer more often than not.

**Legend:** topology codes = TP-01…TP-09; pattern families = SP / SAFE / CTX / EVAL (see [SYSTEM_PATTERN_INDEX.md](SYSTEM_PATTERN_INDEX.md)).

---

## Step 0 first, always

Before using this table, pass the **complexity-ladder gate** (Step 0 in [SYSTEM_QUICK_START.md](SYSTEM_QUICK_START.md)). If a deterministic function or a single prompt does the job, **stop there** — none of the rows below apply.

---

## Lookup table

| I need to… | Lowest-fit topology | Apply patterns | Mandatory gates | Notes / "actually, don't build an agent if…" |
|------------|---------------------|----------------|-----------------|----------------------------------------------|
| Answer/classify/extract/format one thing | **TP-01 Direct call** | — | input validation | This is a **prompt**, not a system. Go to `AI_AGENT_QUICK_START.md` / `NON_CODING_QUICK_START.md`. |
| Run a fixed pipeline (draft → review → polish) | **TP-03 Sequential** | SP-02 (gates between steps) | gate-between-steps; validate before passing downstream | Control flow stays in **code**. Not a "real" agent. |
| Send each input to the right specialist | **TP-04 Routing/handoff** | SP-02 | bound handoffs; log routes; SAFE-05 if inputs are untrusted | Prefer **deterministic routing** (code owns the route) over agent-decided handoff unless the route truly depends on reasoning. |
| Do N independent subtasks fast, or vote for confidence | **TP-05 Parallel** | SP-02 | aggregation conflict policy; watch shared-endpoint rate limits | Only if subtasks are **independent**. |
| Use tools dynamically within one domain | **TP-02 Single agent (loop)** | CTX-01/02; SAFE-02/04 | **bound the loop + cap-fallback**; least-privilege tools; deterministic policy enforcement | The **right default** once a prompt/workflow is insufficient. |
| Research a question across many sources and synthesize | **TP-06 Orchestrator-workers** | SP-01/02/03; CTX-03/04; SAFE-01/05 | injection defense on web content; sub-agent isolation; trust model; circuit breakers | The **gold-standard example**. Multi-agent ⇒ ~15× tokens — justify breadth/parallelism. |
| Change code across many files / decompose at runtime | **TP-06 Orchestrator-workers** | CTX-03/04; SAFE-02/05 | sandbox code exec; human review of destructive changes; loop bounds | Caution: most coding is a **poor multi-agent fit** (interdependency). Prefer TP-02 unless the work is genuinely breadth-first. |
| Iterate output to a quality bar | **TP-07 Evaluator-optimizer** | EVAL-02 | **iteration cap + cap-fallback**; guard against evaluator rubber-stamping | Needs *clear* eval criteria, else the evaluator just inflates grades. |
| Reach consensus / stress-test via multiple viewpoints | **TP-08 Group chat / debate** | SP-02; SAFE-10 | turn + termination control; ≤3 agents | If one agent + a checklist works, do that instead. |
| Handle open-ended work needing an auditable replanning trail (SRE remediation, deep research with backtracking) | **TP-09 Magentic / task-ledger** | SP-01/02/03; CTX-04; SAFE-02/07/09 | heavy HITL gates; external task ledger; kill switch | Highest cost + hardest to predict. Gate aggressively; require HITL on consequential actions. |

---

## By blast radius (sizes the gates, independent of topology)

| If the system can… | Then you MUST add |
|--------------------|-------------------|
| Read untrusted external content (web, email, user files) | SAFE-01 (data/control separation) + SAFE-05 (injection defense) — non-negotiable |
| Modify state (files, DB, records) | SAFE-02 (deterministic policy + schema/allowlist validation) + idempotency + dry-run + rollback path |
| Execute code | SAFE-02 + sandboxing (ASI05) + human review of destructive/unreviewed code |
| Spend money / move funds / contact customers | SAFE-09 (HITL approval + confidence scoring) + kill switch + Gate C disclosure |
| Spawn sub-agents / run as a fleet | SAFE-07 (circuit breakers) + SAFE-10 (inter-agent trust model) + population-level monitoring |
| Persist memory across runs | SAFE-06 (memory-poisoning defense: access control + integrity validation) |

---

## By topology → which existing repo prompts to pull

| Topology | Strongest existing prompts to assemble |
|----------|----------------------------------------|
| TP-02 Single agent | `aiagent_architecture_design`, `ai_pattern_agent_work_loop_design`, `done_definition_loop_operator` |
| TP-04 Routing | `aiagent_orchestration_topology_selection`, `aiagent_task_routing_load_balancing` |
| TP-06 Orchestrator-workers | `aiagent_multi_agent_orchestration`, `aiagent_planning_decomposition_design`, `aiagent_inter_agent_communication_protocol`, `aiagent_context_engineering_at_scale` |
| TP-07 Evaluator-optimizer | `aiagent_evaluation_design`, `done_definition_verification_hardening`, `ai_review_outcome_level_code_review` |
| TP-09 Magentic | `aiagent_planning_decomposition_design`, `aiagent_durable_execution_state_persistence`, `aiagent_human_in_the_loop_design` |
| (any, for gates) | `aiagent_hard_gates_designer` (composes A/B/C + kill switch), `aiagent_runtime_guardrails_policy`, `aiagent_human_in_the_loop_design`, `aiagent_agentic_threat_model`, `aiagent_prompt_injection_untrusted_content_defense` |
| (any, for eval) | `aiagent_evaluation_design`, `model-evaluation-validation/*`, `aiagent_agentic_safety_eval_layer` |
| (Gate 0 / justify) | `aiagent_complexity_ladder_gate` (agent vs workflow, lowest-rung-first) |
| (multi-stage orchestration) | `aiagent_orchestrator_generator` (guided/manual/surgical master orchestrator) |
| (any, for observability/runbooks) | `aiagent_observability_telemetry_design`, `mlmonitor_*` |
| (any, for disclosure/Gate C) | `rai_documentation_suite_orchestrator`, `rai_model_risk_register`, `rai_*_assessment` (jurisdiction selector) |

---

## Sanity checks before you commit to a topology

- **Did you try to talk yourself down a rung?** If not, do it now.
- **Is multi-agent buying you parallelism/breadth, or just complexity?** If you can't name the breadth, drop to TP-02.
- **Is any input untrusted?** If yes, SAFE-01 + SAFE-05 are mandatory regardless of topology.
- **What's the worst action the system can take, and is there a gate + kill switch in front of it?**

---

**Next:** run the full process in [SYSTEM_QUICK_START.md](SYSTEM_QUICK_START.md) and score with [SYSTEM_QUALITY_RUBRIC.md](SYSTEM_QUALITY_RUBRIC.md).
