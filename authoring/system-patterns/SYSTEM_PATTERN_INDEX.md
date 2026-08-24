# Agentic System Pattern Index

**The pattern catalog for designing agentic systems.** Five pattern families, each with a stable code, a definition, when to use / when NOT to use, the primitives it needs, its failure modes, and the existing repo prompt(s) that author its parts.

> **Naming:** patterns are coded by family — **TP** (Topology), **SP** (Structural), **SAFE** (Safety/Security), **CTX** (Context/Durability), **EVAL** (Evaluation). The topology catalog (TP-01…TP-09) is the spine; everything else hangs off the chosen topology.

**Provenance:** distilled from a verified research base — framework-agnostic, with per-vendor aliases preserved so a design maps cleanly onto Anthropic / OpenAI Agents SDK / Azure / Microsoft Agent Framework / Google ADK / LangGraph / LlamaIndex.

---

## 0. The Complexity Ladder (read this first)

The catalog is a **ladder of escalating complexity, not a menu of equals.** Always choose the lowest rung that reliably meets the scope.

```
TP-01 Direct call            ┐ cheapest, most reliable, easiest to make safe
TP-02 Single agent (loop)    │
TP-03 Sequential / chaining  │  ← workflows: control flow in CODE (deterministic)
TP-04 Routing / handoff      │
TP-05 Parallel / concurrent  ┘
─────────────────────────────  the "needs a real agent" line
TP-06 Orchestrator-workers   ┐
TP-07 Evaluator-optimizer    │  ← agentic: control flow (partly) in the MODEL (dynamic)
TP-08 Group chat / debate    │
TP-09 Magentic / task-ledger ┘ most expensive (~15× tokens), hardest to make safe
```

**Cost anchors:** single agent ≈ 4× a chat turn; multi-agent ≈ 15×. Multi-agent is justified only for high-value, parallelizable, breadth-first work — and is a poor fit for most coding.

### The primitives (the nouns every topology composes)

| Primitive | What it is |
|-----------|-----------|
| **Model call** | The augmented LLM = model + retrieval + tools + memory |
| **Tool** | Function / hosted / MCP; also agents-as-tools, local runtime tools. Consolidated, namespaced, token-efficient |
| **State** | Shared, typed, externally persisted/checkpointed |
| **Memory** | In-context vs external/agentic notes |
| **Agent** | Model + tools + state + instructions + an autonomous loop |
| **Handoff** | Transfer of control between agents |
| **Guardrail** | Validation/policy gate on input, tool call, tool output, or final output (with position + tripwire semantics) |
| **Tracing/observability** | Per-agent + whole-system |
| **Human checkpoint (HITL)** | Approval gate vs feedback loop; scoped whole-agent or per-tool |

> **The agent loop** is the defining runtime abstraction. Call the LLM → typed final output, no tool calls ⇒ stop → handoff ⇒ swap active agent, re-loop → tool calls ⇒ run them, append results, re-loop. Bounded by `max_turns`. Every topology below is a way of arranging control transfer around this loop.

---

## 1. Topology Patterns (TP-01 … TP-09) — the spine

### TP-01 — Direct call
- **Definition:** one augmented LLM call, optionally + retrieval/tools. No loop, no autonomy.
- **Aliases:** baseline.
- **Use when:** most tasks. The honest default.
- **Avoid when:** the task genuinely needs dynamic multi-step tool use.
- **Primitives:** model call, (optional) tool, (optional) retrieval.
- **Failure modes:** —
- **Authors with:** any single prompt. This usually means *don't build a system* — author a prompt instead.

### TP-02 — Single agent (loop)
- **Definition:** one agent plans + acts in a loop, taking ground-truth from the environment each step, bounded by stop conditions.
- **Aliases:** Anthropic *autonomous agent*; Azure *single agent with tools*; LangGraph LLM↔ToolNode cycle.
- **Use when:** dynamic tool choice is needed within a single domain. **Often the right default** once TP-01 is insufficient.
- **Avoid when:** subtasks are independent and parallelizable (use TP-05/06), or steps are fixed (use TP-03).
- **Primitives:** agent, tools, state, guardrail, tracing, (optional) HITL.
- **Failure modes:** unbounded loops; runaway cost. **Always bound the loop + define a cap-fallback.**
- **Authors with:** `aiagent_architecture_design`, `ai_pattern_agent_work_loop_design`, `done_definition_loop_operator`.

### TP-03 — Sequential / chaining
- **Definition:** fixed sequential steps with **programmatic gates** between them. Control flow in code.
- **Aliases:** Anthropic *prompt chaining*; Azure *sequential / pipeline* (≈ pipes-and-filters); ADK *Sequential agent*.
- **Use when:** the task cleanly decomposes into a known, fixed sequence (draft → review → polish).
- **Avoid when:** the number/order of steps depends on intermediate results (→ TP-06).
- **Primitives:** model calls, gates (guardrails between steps), state.
- **Failure modes:** early-step failures poison later steps. **Validate output before passing downstream.**
- **Authors with:** `done_definition_gate_sets_by_domain`, `aiagent_planning_decomposition_design`.

### TP-04 — Routing / handoff
- **Definition:** classify, then dispatch to a specialized path/agent. Two sub-variants: **deterministic routing** (code owns the route) vs **handoff** (agents decide to transfer control).
- **Aliases:** Anthropic *routing*; Azure *handoff*; OpenAI Agents SDK *handoffs* (first-class); LangGraph router / `Command`.
- **Use when:** inputs fall into distinct classes and the right specialist emerges at runtime.
- **Avoid when:** there's really only one path (→ TP-02).
- **Primitives:** classifier/router, agents, handoff, guardrail.
- **Failure modes:** infinite handoff loops; misroutes. Bound handoffs; log routes.
- **Authors with:** `aiagent_orchestration_topology_selection`, `aiagent_task_routing_load_balancing`.

### TP-05 — Parallel / concurrent
- **Definition:** run multiple calls/agents simultaneously, then aggregate. **Sectioning** (independent subtasks) vs **voting** (same task ×N for confidence/diversity).
- **Aliases:** Anthropic *parallelization*; Azure *concurrent / fan-out-fan-in / scatter-gather / map-reduce*; ADK *Parallel agent*.
- **Use when:** subtasks are independent, or you need diversity/confidence via voting.
- **Avoid when:** subtasks are interdependent (shared context cost dominates).
- **Primitives:** parallel model calls/agents, aggregator, state.
- **Failure modes:** conflict resolution at aggregation; quota spikes / shared-endpoint rate-limiting.
- **Authors with:** `aiagent_planning_decomposition_design`, `aiagent_orchestration_topology_selection`.

### TP-06 — Orchestrator-workers
- **Definition:** a central LLM **dynamically decomposes** the task (subtasks not known in advance), delegates to workers, and synthesizes their results. *This is the canonical "research sub-agent fleet" pattern.*
- **Aliases:** Anthropic *orchestrator-workers* / lead + subagents; LangGraph `Send` API.
- **Use when:** the number/shape of subtasks is input-dependent (multi-source research, multi-file code changes).
- **Avoid when:** subtasks are fixed (→ TP-03/05) or interdependent with heavy shared state (coordination cost explodes).
- **Primitives:** orchestrator agent, worker agents (sub-agent isolation), handoff/delegation, shared state, aggregator, tracing.
- **Failure modes:** coordination overhead; cost (≈15× tokens); workers duplicating work; context bloat in the orchestrator.
- **Authors with:** `aiagent_multi_agent_orchestration`, `aiagent_planning_decomposition_design`, `aiagent_context_engineering_at_scale` (sub-agent isolation), `aiagent_inter_agent_communication_protocol`.

### TP-07 — Evaluator-optimizer
- **Definition:** a generator produces output; an evaluator scores it against explicit criteria; feedback loops until pass or an iteration cap.
- **Aliases:** Anthropic *evaluator-optimizer*; Azure *maker-checker / generator-verifier / critic / reflection*; ADK *Loop agent*.
- **Use when:** there are clear eval criteria and iteration measurably improves output.
- **Avoid when:** criteria are fuzzy (the evaluator just rubber-stamps) or one pass is enough.
- **Primitives:** generator, evaluator (guardrail-as-judge), loop with cap, state.
- **Failure modes:** must have an iteration cap **and** a cap-fallback; evaluator collusion / grade inflation.
- **Authors with:** `aiagent_evaluation_design`, `ai_review_outcome_level_code_review`, `done_definition_verification_hardening`.

### TP-08 — Group chat / debate
- **Definition:** multiple agents on a **shared thread**; a chat manager controls turns + termination; agents are usually read-only.
- **Aliases:** Azure *group chat / roundtable / council / debate*.
- **Use when:** consensus, brainstorming, or structured cross-validation adds value.
- **Avoid when:** >3 agents (control degrades) or a single agent suffices.
- **Primitives:** shared thread/state, chat manager, agents, termination guardrail.
- **Failure modes:** loops; hard to control beyond 3 agents; talk without convergence.
- **Authors with:** `aiagent_orchestration_topology_selection`, `aiagent_inter_agent_communication_protocol`.

### TP-09 — Magentic / task-ledger
- **Definition:** a manager builds and **continuously refines a task ledger** by consulting tool-equipped specialists; backtracks/replans; keeps an auditable plan.
- **Aliases:** Azure *magentic* (newest; no clean Anthropic equivalent).
- **Use when:** open-ended work (SRE remediation, deep research) that needs an audit trail + HITL gates.
- **Avoid when:** the task is bounded enough for TP-06; you can't afford unpredictable cost.
- **Primitives:** manager agent, task ledger (external state), specialist agents/tools, HITL gates, tracing.
- **Failure modes:** slow convergence; hardest cost to predict. Gate it heavily.
- **Authors with:** `aiagent_planning_decomposition_design`, `aiagent_durable_execution_state_persistence`, `aiagent_human_in_the_loop_design`.

### Topology selection scorecard

| Variable | Pushes toward |
|----------|---------------|
| Control of next step is **code** | TP-03 / TP-04(deterministic) / TP-05 |
| Control of next step is **the model** | TP-02 / TP-06 / TP-07 / TP-09 |
| Subtasks **independent** | TP-05 / TP-06 |
| Subtasks **in sequence** | TP-03 |
| Subtasks **conversational** | TP-08 |
| Plan **known in advance** | TP-03 / TP-05 |
| Plan **built at runtime** | TP-06 / TP-09 |
| Need **iteration to quality** | TP-07 |

Use `aiagent_orchestration_topology_selection` for the full scored selector.

---

## 2. Structural Patterns (SP-01 … SP-05) — how to package a system

Distilled from the repo's three working toolkit exemplars (`ai-investment-research-toolkit/`, `domain-idea-to-product/`, `financial-records-toolkit/`).

| Code | Pattern | What it does |
|------|---------|--------------|
| **SP-01** | **Three-layer documentation** | `README.md` (purpose/modes/scope) + `ARCHITECTURE.md` (load-bearing decisions, seams, gates) + `PIPELINE_OVERVIEW.md` (visual flow, stages, branching, terminal artifacts). |
| **SP-02** | **Hard gates as code, not trust** | Gate A (prerequisite/input validation) → Gate B (mid-execution limits/risk) → Gate C (terminal unlock) + an explicit kill switch. Enforced in code/config, not prose. |
| **SP-03** | **Local-first / privacy by design** | Config in YAML (not prompts); `data/` git-ignored; secrets in env; no fabricated data (unknowns queued as `UNAVAILABLE`, never guessed). |
| **SP-04** | **Multi-usage modes** | Guided (orchestrator interviews + gates) · Manual (walk the pipeline) · Surgical (jump to one stage). |
| **SP-05** | **Self-contained with cross-links** | Gather needed prompts into one directory (copies, not moves); explicitly cross-link parent domains; document composition. |

---

## 3. Safety / Security Patterns (SAFE-01 … SAFE-10) — the load-bearing family

Each maps to an OWASP ASI risk and to an existing `aiagent_*` prompt. **These are not optional; they are what makes output "production-ready" rather than a prototype.** (Full checklist: research base §9a.)

| Code | Pattern | OWASP ASI | Core mitigation | Authors with |
|------|---------|-----------|-----------------|--------------|
| **SAFE-01** | **Data/control separation (CaMeL)** | ASI01 | Untrusted data never drives control flow / tool selection; privileged planner on trusted query, quarantined handler for untrusted data; capability-based taint tracking | `aiagent_prompt_injection_untrusted_content_defense` |
| **SAFE-02** | **Deterministic policy enforcement** | ASI02/05/08 | Tool allowlists, rate limits, schema/arg validation, HITL confirmation — blocks prohibited actions *regardless of LLM output*. The most mature defense layer | `aiagent_runtime_guardrails_policy` |
| **SAFE-03** | **Least-agency scoping** | (cross-cutting) | Avoid unnecessary autonomy; deploy agentic behavior only where it adds value | `aiagent_least_agency_scoping` |
| **SAFE-04** | **Least-privilege tools** | ASI02/03 | Minimal tool set per agent; high-privilege ops re-verify intent | `aiagent_tool_design`, `aiagent_trust_boundary_design` |
| **SAFE-05** | **Indirect-injection defense** | ASI01 | Validate/sanitize all external content; monitor objective drift; defense-in-depth (input + instruction hierarchy + policy enforcement) | `aiagent_prompt_injection_untrusted_content_defense` |
| **SAFE-06** | **Memory-poisoning defense** | ASI06 | Access control + integrity validation on memory/RAG; monitor writes | `aiagent_memory_poisoning_defense` |
| **SAFE-07** | **Cascading-failure circuit breakers** | ASI08 | Circuit breakers; blast-radius caps (quotas/progress caps); separate planning from execution; isolation | `aiagent_failure_mode_analysis`, `aiagent_secops_autonomous_defense` |
| **SAFE-08** | **Governed identity** | ASI03; NIST | Unique governed identity per agent; attributable actions; no credential caching; off static secrets | `aiagent_privacy_data_governance`, `aiagent_zero_trust_maturity_assessment` |
| **SAFE-09** | **Risk-adaptive authorization** | ASI09 | RBAC + aggregated-risk thresholds (not confirmation fatigue); human approval + confidence scoring for high-risk actions | `aiagent_human_in_the_loop_design` |
| **SAFE-10** | **Inter-agent trust model** | ASI07/10 | Encrypt + authenticate peers; verified discovery; documented trust model before any multi-agent rollout; measurable aligned objectives + spawn limits | `aiagent_inter_agent_communication_protocol`, `aiagent_agentic_threat_model` |

> **Fleet caveat (DeepMind):** once you author *fleets*, add population-level / emergent-behavior monitoring — collective harm isn't visible per-agent.

---

## 4. Context / Durability Patterns (CTX-01 … CTX-04)

Context/state is the central scaling problem. (Research base §5.)

| Code | Pattern | What it does | Authors with |
|------|---------|--------------|--------------|
| **CTX-01** | **Compaction** | Summarize near the window limit; reinitialize with the summary | `aiagent_context_engineering_at_scale` |
| **CTX-02** | **Agentic note-taking** | Write structured notes outside context; retrieve later | `aiagent_memory_design` |
| **CTX-03** | **Sub-agent isolation** | Separate context windows; subagents return *condensed summaries*; separate explore from synthesize | `aiagent_context_engineering_at_scale`, `aiagent_multi_agent_orchestration` |
| **CTX-04** | **Checkpoint / resume** | Persist state externally; resume from checkpoints, not restart; non-disruptive deploys for in-flight agents | `aiagent_durable_execution_state_persistence` |

---

## 5. Evaluation Patterns (EVAL-01 … EVAL-04)

Capability and safety are **separate** gates. (Research base §7, §9b.)

| Code | Pattern | What it does | Authors with |
|------|---------|--------------|--------------|
| **EVAL-01** | **ABC task-validity** | Task solvable iff capability present; tool/package versions pinned; agent isolated from ground truth; oracle solver; pilot-outlier inspection | `aiagent_agentic_safety_eval_layer`, `model-evaluation-validation/` |
| **EVAL-02** | **ABC outcome-validity** | Graders robust to equivalents/negation; no success-by-guessing; code → unit+fuzz+E2E+determinism; validate LLM-judge with pilots | `done_definition_verification_hardening`, `aiagent_evaluation_design` |
| **EVAL-03** | **Real-tool safety eval (OpenAgentSafety)** | 8 risk categories in real-tool environments (shell/fs/code/browser/multi-user); rule-based + LLM-judge; benign + adversarial; **separate gate from capability** | `aiagent_agentic_safety_eval_layer` |
| **EVAL-04** | **Dual process + outcome metrics** | Measure both the trajectory and the result; report cost; include a trivial-agent baseline; confidence intervals | `aiagent_evaluation_design`, `ai_pattern_auto_improving_triplet_diagnostic` |

---

## How patterns combine (worked mini-example)

A **research sub-agent fleet** (the gold-standard example) is:
**TP-06** (orchestrator-workers) + **SP-01/02/03** (three-layer docs, hard gates, local-first) + **SAFE-01/02/04/05/07/10** (untrusted web content ⇒ injection + data/control separation are mandatory; multi-agent ⇒ trust model + circuit breakers) + **CTX-03/04** (sub-agent isolation, checkpoint/resume) + **EVAL-01/02/03/04** (ABC-valid acceptance + real-tool safety, both gates).

See the fully worked design in [templates/GOLD_STANDARD_AGENTIC_SYSTEM.md](templates/GOLD_STANDARD_AGENTIC_SYSTEM.md).

---

**Next:** match your use case in [SYSTEM_USE_CASE_LOOKUP.md](SYSTEM_USE_CASE_LOOKUP.md), or run the process in [SYSTEM_QUICK_START.md](SYSTEM_QUICK_START.md).
