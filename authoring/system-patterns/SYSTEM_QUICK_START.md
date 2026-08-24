# Agentic System Authoring — Quick Start (The 6-Step Process)

**Design a production-ready agentic system in 6 steps. Step 0 is a gate, not a formality.**

> This adapts the repo's proven 5-step authoring process (skills/agents/commands) and inserts a **mandatory complexity-ladder gate (Step 0)** at the front, because the #1 research imperative is to *talk users down the ladder*. The output is a **framework-agnostic design bundle** (always) plus, optionally, stack-specific scaffolding.

**Time estimate:** 45–120 minutes for a single-agent system; longer for a fleet.
**Target quality score:** 75/100 against [SYSTEM_QUALITY_RUBRIC.md](SYSTEM_QUALITY_RUBRIC.md).
**Companion docs:** [SYSTEM_PATTERN_INDEX.md](SYSTEM_PATTERN_INDEX.md), [SYSTEM_USE_CASE_LOOKUP.md](SYSTEM_USE_CASE_LOOKUP.md), [templates/](templates/).

```
Step 0: Justify the agent (complexity ladder)  → STOP with a workflow recommendation if it doesn't earn it
Step 1: Scope the system
Step 2: Select the topology
Step 3: Design the architecture
Step 4: Design the gates (code-not-trust)
Step 5: Design the eval harness (capability AND a separate safety gate)
Step 6: Assemble, validate (≥75), document
```

---

## Step 0: Justify the Agent (Complexity-Ladder Gate)

**This step can end the whole exercise. That is a success, not a failure.**

Force the question, in order, before anything else:

```
Can a deterministic function or hardcoded rule do this?
├─ YES → write the function. STOP. (No agent. No LLM, even.)
└─ NO ↓
Can a single model call (maybe + retrieval/one tool) do this reliably?
├─ YES → that's a "direct call". STOP. Author it as a prompt, not a system.
└─ NO ↓
Can a fixed, code-controlled workflow (prompt chain / router / parallel) do this?
├─ YES → build the WORKFLOW. Control flow stays in code. STOP here unless dynamism is required.
└─ NO ↓
Does the task genuinely require the MODEL to decide the next step at runtime
(unknown number of steps, input-dependent decomposition, dynamic tool choice)?
└─ YES → an agent is justified. Proceed to Step 1. Write the one-line reason below.
```

**Required output of Step 0** — one written sentence, recorded in the architecture doc:

> *"An agent is required because ____ (the number/order of steps is not knowable in advance / tool choice depends on intermediate results / the task needs runtime replanning), and a deterministic workflow cannot because ____."*

If you cannot complete that sentence honestly, **you do not have an agent use case.** Recommend the workflow and stop.

**Cost reality (use it to push back):** agents use ~**4×** the tokens of a chat turn; multi-agent systems ~**15×**. Multi-agent is only justified for high-value, parallelizable, breadth-first work and is a **poor fit for most coding** (interdependency + shared context). Never escalate to multi-agent to "be safe."

**References:** `aiagent_complexity_ladder_gate` ⭐ (Gate 0: agent vs. workflow, lowest-rung-first); `aiagent_multi_agent_orchestration` (when-to-split); `ai_pattern_agent_task_code_distance_scorer` (Delegate / Decompose / DIY).
**Rubric tie-in:** *Agent justification & complexity-appropriateness (15 pts).*

---

## Step 1: Scope the System

Define the bounded problem before choosing any pattern.

Capture:
- **Use case** in one sentence + the **job-to-be-done**.
- **Success criteria** as *observable, checkable gates* (not vibes). "Returns a sourced answer where every claim cites a retrieved document" — not "good research."
- **Inputs / outputs** — types, formats, volume, trust level (which inputs are untrusted external content?).
- **Autonomy level** — does it act, or only recommend?
- **Blast radius** — what is the worst thing it can do? (sends money? deletes files? emails customers?) This sizes every later gate.
- **Reuse vs net-new** — which existing repo prompts/agents/tools cover parts of this?

**References:** `done_definition_translator` ⭐ (fuzzy → observable gates with evidence); `ai_pattern_intent_and_verification_first` (intent + verification + out-of-scope); `ai_pattern_outcome_language_translator`.
**Template:** start filling [`ARCHITECTURE_TEMPLATE.md`](templates/ARCHITECTURE_TEMPLATE.md) §1–§2.

---

## Step 2: Select the Topology

Pick the **lowest-complexity topology** that reliably meets the scope. Use the three selection variables:

1. **Who controls the next step** — code (deterministic) or the model (dynamic)?
2. **Do components work in sequence, in parallel, or in conversation?**
3. **Is the plan known in advance, or built at runtime?**

The 9-topology catalog (full detail + per-vendor aliases + failure modes in [SYSTEM_PATTERN_INDEX.md](SYSTEM_PATTERN_INDEX.md)):

| # | Topology | One-line "use when" |
|---|----------|---------------------|
| 1 | **Direct call** | Most tasks; the honest default |
| 2 | **Single agent (loop)** | Dynamic tool choice, one domain |
| 3 | **Sequential / chaining** | Cleanly decomposable fixed subtasks (draft→review→polish) |
| 4 | **Routing / handoff** | Distinct input classes; right specialist at runtime |
| 5 | **Parallel / concurrent** | Independent subtasks, or voting for confidence |
| 6 | **Orchestrator-workers** | Input-dependent # of subtasks (multi-source research, multi-file code) |
| 7 | **Evaluator-optimizer** | Clear eval criteria + iteration improves output |
| 8 | **Group chat / debate** | Consensus, brainstorming, structured validation |
| 9 | **Magentic / task-ledger** | Open-ended, needs an auditable replanning trail + HITL gates |

Then **name the primitives** you'll need: model call, tool, state, memory, agent, handoff, guardrail, tracing, human checkpoint. (Definitions in the pattern index.)

> Everything compiles down to the **agent loop**: call the LLM → if it returns a typed final output with no tool calls, stop → if it hands off, swap active agent and re-loop → if it calls tools, run them, append results, re-loop. Bound by `max_turns`. A topology is just *how control transfers* inside/around that loop.

**References:** `aiagent_orchestration_topology_selection` ⭐ (scorecard selector); `aiagent_planning_decomposition_design`; `ai_pattern_agent_work_loop_design`.
**Rubric tie-in:** *Topology fit & primitive correctness (15 pts).*

---

## Step 3: Design the Architecture

Turn the chosen topology into a concrete design. Fill [`ARCHITECTURE_TEMPLATE.md`](templates/ARCHITECTURE_TEMPLATE.md).

Decide and document:
- **Stages / agents and seams** — for each agent, fill an [`AGENT_SPEC_TEMPLATE.md`](templates/AGENT_SPEC_TEMPLATE.md) (identity, role, authority boundary Can-Do / Ask-First / Never, minimized tool set, guardrails, memory scope).
- **Tools (the Agent-Computer Interface)** — fill a [`TOOL_SPEC_TEMPLATE.md`](templates/TOOL_SPEC_TEMPLATE.md) per tool. Build tools around **high-impact workflows, not API endpoints**; consolidate multi-call flows; namespace related tools; return semantic identifiers; make error messages *guidance*; add idempotency keys + a dry-run for destructive calls. **More tools ≠ better.**
- **Context / durability strategy** — per hop choose full-raw vs summary vs fresh-instruction-only. Apply the three long-horizon techniques where relevant:
  1. **Compaction** — summarize near the window limit, reinitialize with the summary.
  2. **Structured note-taking / agentic memory** — write notes outside context, retrieve later.
  3. **Sub-agent isolation** — separate context windows; subagents return *condensed summaries* (separate explore from synthesize).
  Persist state **externally** for any long-running or resumable work; design for checkpoint/resume, not restart.
- **Cost / model right-sizing** — cheap models for classify/extract/format; reserve the strong model for reasoning/synthesis. Note expected tokens per-agent and per-run.
- **"Right altitude" system prompts** — specific enough to guide, flexible enough to leave heuristics. Avoid both brittle hardcoded logic and vague generalities.

**References:** `aiagent_architecture_design` ⭐; `aiagent_tool_design`; `aiagent_memory_design`; `aiagent_cost_token_budget_design`; `aiagent_context_engineering_at_scale`; `aiagent_failure_mode_analysis`; `genai-llm-engineering/` (RAG/retrieval) when memory is retrieval-backed.
**Rubric tie-in:** *Durability / observability / cost design (10 pts).*

---

## Step 4: Design the Gates (Code-Not-Trust)

**Gates are enforced in code, never "the agent will remember to."** Fill [`GATE_DESIGN_TEMPLATE.md`](templates/GATE_DESIGN_TEMPLATE.md). The OWASP-ASI security gate here is to this system what **False-Positive Prevention** is to a Tier-1 prompt: the load-bearing differentiator.

Design four gate layers sized to the **blast radius** from Step 1:

- **Gate 0 (justification)** — already passed in Step 0; record the written reason.
- **Gate A (security, OWASP ASI)** — minimum set, every box deliberate:
  - Governed **unique identity per agent**; actions attributable; no credential caching (ASI03).
  - **Least privilege per tool**; high-privilege ops re-verify intent (ASI02/03).
  - **Data/control separation** — untrusted data never drives control flow or tool selection (CaMeL pattern) (ASI01).
  - **Indirect-prompt-injection defense** on all external content (ASI01).
  - **Defense-in-depth, three layers** — input detection + model instruction hierarchy + **deterministic policy enforcement** (the only layer that blocks prohibited actions *regardless of LLM output*).
  - **Validate every tool call vs schema/allowlist pre-execution** (ASI02/05); **sandbox all code execution** + human review of destructive code (ASI05).
  - **Circuit breakers + blast-radius caps** vs cascading failure (ASI08); **measurable aligned objectives + spawn/resource limits** vs rogue agents (ASI10).
  - **Encrypt + authenticate inter-agent messages** if multi-agent (ASI07); access-control + integrity-validate memory/RAG (ASI06).
- **HITL approval gates** — human approval + confidence scoring for high-risk actions (ASI09). Use **risk-adaptive authorization** (RBAC + risk thresholds), not confirmation fatigue.
- **Loop bounds + cap-fallbacks** — bound *every* loop; define what happens at the cap (don't just stop silently).
- **Kill switch** — an explicit, code-level halt (e.g., a `halt` flag in config) that stops the system's ability to act.

**References:** `aiagent_human_in_the_loop_design` ⭐; `aiagent_runtime_guardrails_policy`; `aiagent_prompt_injection_untrusted_content_defense`; `aiagent_agentic_threat_model`; `aiagent_least_agency_scoping`; `aiagent_zero_trust_maturity_assessment`; `aiagent_hard_gates_designer` ⭐ (composes A/B/C + kill switch).
**Rubric tie-in:** *Security gate coverage vs OWASP ASI (20 pts — load-bearing).*

---

## Step 5: Design the Eval Harness (Two Independent Gates)

**Capability and safety are separate gates. A system can be capable and unsafe — frontier models are unsafe by default in real-tool settings (51–73% unsafe-action rate in OpenAgentSafety).** Fill [`EVAL_HARNESS_TEMPLATE.md`](templates/EVAL_HARNESS_TEMPLATE.md).

- **Gate B-capability (ABC-valid acceptance suite):**
  - **Task validity** — each task solvable *iff* the agent has the target capability; specify exact tool/package **versions**; isolate the agent from ground truth; verify ground-truth setup; provide an oracle solver; inspect pilot outliers.
  - **Outcome validity** (by task category) — graders robust to semantic equivalents/negation; no success-by-listing/guessing; for code, manually-verified unit tests + coverage + **fuzzing** + E2E + determinism; validate any LLM-judge with pilots.
  - **Reporting** — open harness; confidence intervals; **trivial-agent baseline** (e.g., an empty-response agent must score ~0); dual **process + outcome** metrics; report cost.
  - Start small: ~**20 realistic queries**, rubric/LLM-as-judge (not exact-match), held-out set, human spot-check.
- **Gate B-safety (OpenAgentSafety real-tool eval) — SEPARATE:**
  - Evaluate in **real-tool environments** (shell + filesystem, code execution, browser, multi-user messaging), not stubs.
  - Cover the **8 risk categories**: computer-security compromise, data loss/corruption, privacy breach, unsafe code execution, financial loss, spreading malicious content, legal violations, harmful decision-making.
  - Detection = rule-based final-state checks **+ LLM-as-judge** (catches unsafe *intent* and near-misses). Run benign + adversarial, multi-turn.

> An "invalid benchmark" is worse than no benchmark — it manufactures false confidence (the exact failure the research warns about). Watch for: empty responses scoring as success; tests too weak to fail a wrong answer; the agent seeing ground truth.

**References:** `aiagent_agentic_safety_eval_layer` ⭐ (the ABC + OpenAgentSafety layer); `aiagent_evaluation_design`; `done_definition_verification_hardening` ⭐ (close false-PASS loopholes); `model-evaluation-validation/` (general eval substrate).
**Rubric tie-in:** *Evaluation validity (ABC) + real-tool safety eval present (20 pts).*

---

## Step 6: Assemble, Validate, Document

Emit the **framework-agnostic design bundle** (the terminal artifact), score it, and write the docs.

The bundle (parallels `domain-idea-to-product/`'s day-1 software bundle):

1. **System design doc** — topology (+ why this rung of the ladder), primitives, architecture diagram, seams, context/durability strategy, cost/model plan.
2. **Per-agent specs** — from the `AGENT_SPEC_TEMPLATE` instances.
3. **Tool specs (ACI)** — from the `TOOL_SPEC_TEMPLATE` instances.
4. **Gate/policy spec** — from `GATE_DESIGN_TEMPLATE` (deterministic policy rules, HITL thresholds, loop bounds + fallbacks, kill switch).
5. **Eval harness** — from `EVAL_HARNESS_TEMPLATE` (capability + safety suites + rubrics).
6. **Observability plan** — event/span schema, trajectory traces, dashboards, alerts. (`aiagent_observability_telemetry_design` + `mlmonitor_*` runbooks.)
7. **Disclosure manifest** — the AI Agent Index 6 dimensions ([`DISCLOSURE_MANIFEST_TEMPLATE.md`](templates/DISCLOSURE_MANIFEST_TEMPLATE.md)); adapt `rai_documentation_suite_orchestrator`.
8. **Runbook** — deployment/rollout (shadow/canary), rollback path, failure-mode catalog. (`mlmonitor_*`.)
9. **Rules file (`CLAUDE.md` / `AGENTS.md`)** — if a coding agent will build the system.

Then:
- **Score against [SYSTEM_QUALITY_RUBRIC.md](SYSTEM_QUALITY_RUBRIC.md). Below 75 → revise; the security and eval gates are load-bearing — a design that skips either is not Tier 1, regardless of total.**
- **Write the three-layer docs** if shipping as a self-contained system: `README.md` (purpose/modes/scope) + `ARCHITECTURE.md` (decisions/seams/gates) + `PIPELINE_OVERVIEW.md` (flow/stages/branching/terminal artifacts).

**Optional Step 7 — stack-specific code-gen (gated):** only if the user has named/committed to a stack (Claude Agent SDK, LangGraph, OpenAI Agents SDK, Google ADK, Microsoft Agent Framework, LlamaIndex; MCP as the interop layer). The agnostic bundle is always the source of truth; code-gen is a *transform* of it. Stack code stays **version-neutral inside the named stack** — drifting facts (API signatures, model IDs, pricing) are flagged **"verify against current docs,"** never asserted. Output is scaffolding + specs + harness, not a deployed service.

**References:** `done_definition_loop_operator` ⭐ (the run loop); `done_definition_stop_policy`; `aiagent_durable_execution_state_persistence`; `aiagent_deployment_serving_architecture`; `rai_documentation_suite_orchestrator` (disclosure); `learning-ai-ml/notebook-to-production/` (code-gen scaffold).

---

## Quick Quality Checklist (pre-flight before scoring)

- [ ] **Step 0 written justification exists** (or the answer was "use a workflow" and we stopped).
- [ ] Topology is the **lowest-complexity** fit, not the most impressive.
- [ ] Every tool has a spec: schema, least-privilege scope, errors-as-guidance, idempotency/dry-run for destructive calls.
- [ ] **Every loop is bounded** with a defined cap-fallback.
- [ ] OWASP-ASI security gate satisfied for the actual blast radius (data/control separation + deterministic policy enforcement present).
- [ ] A **kill switch** exists in code.
- [ ] Capability eval (ABC-valid) **and** a separate real-tool safety eval both present.
- [ ] Disclosure manifest covers all 6 AI Agent Index dimensions, including safety evals actually run.
- [ ] Rollback path + observability/traces designed.
- [ ] No fabricated data; cross-links to existing prompts instead of duplicating them.

---

**Next:** pick your topology in [SYSTEM_PATTERN_INDEX.md](SYSTEM_PATTERN_INDEX.md), or study the worked example in [templates/GOLD_STANDARD_AGENTIC_SYSTEM.md](templates/GOLD_STANDARD_AGENTIC_SYSTEM.md).
