# Agentic System Authoring System

> **Comprehensive guide for AI agents (and curators) to design high-quality, production-ready agentic AI systems.**
>
> This is the fourth authoring system in `authoring/`, structurally identical to `skill-patterns/`, `agent-patterns/`, and `command-patterns/`. Where those produce a *skill*, an *agent persona*, or a *command*, this one produces a **validated, gated agentic workflow** — a design bundle (always) and, optionally, stack-specific runnable scaffolding.

---

## ⚠️ Important: This is the Authoring System, Not the Implementation Library

**This directory (`authoring/system-patterns/`) contains design guides for CREATING new agentic systems.**

| Directory | Purpose | Contains |
|-----------|---------|----------|
| **`authoring/system-patterns/`** (this) | 📐 **Authoring System** | The 6-step process, pattern catalog, quality rubric, and templates for designing agentic systems |
| **`domain-AI-ML/agentic-ai-systems/`** | 📚 **Design-advice library** | 31 framework-neutral `aiagent_*` prompts the authoring process *references* (never moves) |
| **[`agentic-system-factory/`](../../agentic-system-factory/)** (Phase 3, ✅ built) | 🏭 **Guided factory** | A self-contained toolkit that runs this process end-to-end, enforces gates 0/A/B/C as scripts, and emits the artifact bundle (+ optional stack scaffolding) |

**Use this directory when:** You want to **design a new agentic system** correctly and consistently.
**Use `domain-AI-ML/agentic-ai-systems/` when:** You want deep design advice on one decision (tool design, memory, topology, HITL, etc.).

### Quick Decision

```
"I need to DESIGN an agentic system"        → Stay here (authoring/system-patterns/)
"I need deep advice on ONE design decision" → domain-AI-ML/agentic-ai-systems/
"I need to CREATE a skill"                  → authoring/skill-patterns/README.md
"I need to CREATE an agent persona"         → authoring/agent-patterns/AGENT_QUICK_START.md
"I need to CREATE a command"                → authoring/command-patterns/COMMAND_QUICK_START.md
```

---

## Quick Navigation

| Resource | Purpose | When to Use |
|----------|---------|-------------|
| [**SYSTEM_QUICK_START.md**](SYSTEM_QUICK_START.md) | The 6-step authoring process (Gate 0 first) | Starting any new agentic system |
| [**SYSTEM_PATTERN_INDEX.md**](SYSTEM_PATTERN_INDEX.md) | The pattern catalog: 9 topologies + structural + safety + context + eval patterns | Choosing topology and patterns |
| [**SYSTEM_USE_CASE_LOOKUP.md**](SYSTEM_USE_CASE_LOOKUP.md) | "I need X" → recommended topology + patterns + gates | Finding the right starting point quickly |
| [**SYSTEM_QUALITY_RUBRIC.md**](SYSTEM_QUALITY_RUBRIC.md) | 100-point scoring; the 3 research gates embedded | Validating a design before "production-ready" |
| [**templates/**](templates/) | Architecture, gate, eval, agent-spec, tool-spec, disclosure-manifest templates + a worked example | Filling in the design |
| [**templates/GOLD_STANDARD_AGENTIC_SYSTEM.md**](templates/GOLD_STANDARD_AGENTIC_SYSTEM.md) | A fully worked research-sub-agent-fleet example | Learning by example |

---

## What is an Agentic System?

An **agentic system** is one or more LLM-driven components that take actions in the world (call tools, modify state, send messages, spawn sub-agents) to accomplish a use case. It sits on a **complexity ladder** (see [SYSTEM_PATTERN_INDEX.md](SYSTEM_PATTERN_INDEX.md)):

```
direct model call  →  single agent with tools  →  multi-agent orchestration
        (cheapest, most reliable)   ......   (most expensive, hardest to make safe)
```

> **The single load-bearing thesis of this system:** *start simple; earn complexity.* The first job of the authoring process is to talk the user **down** the ladder, not up it. Most use cases that feel like they need "an agent" are better served by a deterministic workflow. (Source: Anthropic, Azure, Microsoft Agent Framework — all lead with this.)

### Workflow vs Agent (the root variable)

- **Workflow** = LLMs/tools orchestrated through **predefined code paths** (control flow decided by code; deterministic).
- **Agent** = the LLM **dynamically directs its own process and tool usage** (control flow decided by the model).

Every topology in the catalog is a point on this spectrum. The selection question is always: *who controls the next step — code or the model?*

---

## How to Use This System

### Decision Tree

```
User Request
│
├─→ "Design an agentic system for..."  /  "Build me an agent that..."
│   │
│   └─→ USE THIS SYSTEM
│       0. Justify the agent (complexity-ladder Gate 0) — can a function/workflow do this?
│       1. Scope the system
│       2. Select the topology (lowest-complexity fit)
│       3. Design the architecture
│       4. Design the gates (security/HITL/loop bounds/kill switch)
│       5. Design the eval harness (capability + separate safety gate)
│       6. Assemble, validate (≥75), document
│
├─→ "Help me decide ONE thing (tools / memory / topology)"
│   │
│   └─→ REFERENCE domain-AI-ML/agentic-ai-systems/ for that decision
│
└─→ "How do agentic systems work?"
    │
    └─→ Read this README, then SYSTEM_PATTERN_INDEX.md, then the GOLD_STANDARD example
```

---

## The Four Design Imperatives (non-negotiable)

These come straight from the verified research base and shape every step, pattern, and rubric dimension:

1. **Talk users down the complexity ladder.** The first gate is "does this need an agent at all?" Default to deterministic workflows.
2. **Tools are authority boundaries.** The moment an agent can send email / modify files / call APIs, it is a security principal — least privilege, deterministic policy enforcement, and data/control separation are mandatory, not optional.
3. **Capability ≠ safety ≠ valid evaluation.** Three independent gates. Frontier models are unsafe by default in real-tool settings, and most benchmarks are invalid.
4. **Design to the converging standards now** — OWASP ASI (threats), NIST (identity), MCP (interop/audit). They are the safest durable bet.

---

## The 6-Step Process (overview)

```
Step 0: Justify the agent (complexity ladder)  →  STOP with a workflow if it doesn't earn it
Step 1: Scope the system
Step 2: Select the topology
Step 3: Design the architecture
Step 4: Design the gates (code-not-trust)
Step 5: Design the eval harness
Step 6: Assemble, validate (≥75), document
```

Full detail: [SYSTEM_QUICK_START.md](SYSTEM_QUICK_START.md). Target rubric score: **75/100**.

---

## Reuse, Don't Reinvent (the operating principle)

This authoring system is **~70% assembly** of prompts the repo already has. Each step of the process cross-links the strongest existing prompt(s) that author that part:

| Step | Strongest existing prompts (referenced, not duplicated) |
|------|---------------------------------------------------------|
| 0 — Justify | `aiagent_complexity_ladder_gate` ⭐; `aiagent_multi_agent_orchestration`; `ai_pattern_agent_task_code_distance_scorer` |
| 1 — Scope | `done_definition_translator` ⭐; `ai_pattern_intent_and_verification_first` |
| 2 — Topology | `aiagent_orchestration_topology_selection` ⭐; `aiagent_planning_decomposition_design` |
| 3 — Architecture | `aiagent_architecture_design` ⭐; `aiagent_tool_design`; `aiagent_memory_design`; `aiagent_context_engineering_at_scale` |
| 4 — Gates | `aiagent_hard_gates_designer` ⭐ (composes A/B/C + kill switch); `aiagent_human_in_the_loop_design`; `aiagent_runtime_guardrails_policy`; `aiagent_prompt_injection_untrusted_content_defense`; `aiagent_agentic_threat_model` |
| 5 — Eval | `done_definition_verification_hardening` ⭐; `aiagent_evaluation_design`; `aiagent_agentic_safety_eval_layer` |
| 6 — Assemble/run | `done_definition_loop_operator` ⭐; `aiagent_orchestrator_generator` (master orchestrator for multi-stage systems); `aiagent_observability_telemetry_design`; `mlmonitor_*` runbooks; `rai_documentation_suite_orchestrator` (disclosure) |

⭐ = best-in-repo, no real substitute.

---

## Files in This Directory

```
authoring/system-patterns/
├── README.md                       # This file: overview and navigation
├── SYSTEM_QUICK_START.md           # Main guide: the 6-step process (Gate 0 first)
├── SYSTEM_PATTERN_INDEX.md         # Pattern catalog: 9 topologies + structural + safety + context + eval
├── SYSTEM_USE_CASE_LOOKUP.md       # Pattern selection by user need
├── SYSTEM_QUALITY_RUBRIC.md        # 100-point quality scoring (3 research gates embedded)
└── templates/
    ├── ARCHITECTURE_TEMPLATE.md          # Load-bearing decisions, seams, gates, failure modes
    ├── GATE_DESIGN_TEMPLATE.md           # Gate 0/A/B/C + kill switch, as code-not-trust
    ├── EVAL_HARNESS_TEMPLATE.md          # ABC-valid acceptance + OpenAgentSafety real-tool safety
    ├── AGENT_SPEC_TEMPLATE.md            # Per-agent: identity, tools, authority, guardrails, eval
    ├── TOOL_SPEC_TEMPLATE.md             # ACI tool spec (schema, errors-as-guidance, idempotency)
    ├── DISCLOSURE_MANIFEST_TEMPLATE.md   # AI Agent Index 6 dimensions
    └── GOLD_STANDARD_AGENTIC_SYSTEM.md   # Annotated worked example: research sub-agent fleet
```

---

## Related Resources

| Resource | Location | Purpose |
|----------|----------|---------|
| Agent-design prompt library | `domain-AI-ML/agentic-ai-systems/` | The 31 `aiagent_*` prompts this process references |
| Execution-loop + acceptance gates | `domain-engineering-workflows/done-definition/` | The loop spine (stages 1/5/6) |
| Observability + incident runbooks | `domain-AI-ML/production-monitoring/` | Stage 6 + Improve layer |
| Governance / disclosure | `domain-AI-ML/responsible-ai-governance/` | Gate C assembly |
| Skill / Agent / Command authoring | `authoring/{skill,agent,command}-patterns/` | The three sibling authoring systems this clones |

---

## Version History

- **v1.1.0** (2026-06-20): Phase 2 — net-new gap-filling prompts shipped under `domain-AI-ML/agentic-ai-systems/`, now referenced (not deferred) by the process:
  - **G1** `aiagent_complexity_ladder_gate` — Gate 0: agent vs. deterministic workflow, lowest-rung-first.
  - **G2** `aiagent_hard_gates_designer` — composes security/eval/governance into enforced Gate A/B/C + kill switch (code-not-trust).
  - **G3** `aiagent_orchestrator_generator` — emits a guided/manual/surgical master orchestrator for multi-stage systems.
  - **G4** `aiagent_agentic_safety_eval_layer` — ABC task/outcome-validity + the OpenAgentSafety 8-category real-tool safety eval as a separate gate.
- **v1.2.0** (2026-06-20): Phase 3 — the guided factory shipped at [`agentic-system-factory/`](../../agentic-system-factory/): master orchestrator (guided/manual/surgical), stages 0–7, 5 commands, 3 agents, 7 copied templates, 2 stack code-gen guides (Claude Agent SDK + LangGraph), and stdlib-only gate scripts that enforce gates 0/A/B/C as code-not-trust (proven on tracked sample bundles). Phase 4 (CLAUDE.md / PROMPT_INDEX routing) is the remaining milestone.
- **v1.0.0** (2026-06-20): Initial Phase 1 release.
  - 6-step authoring process (Gate 0 = complexity ladder)
  - 9-topology catalog + structural / safety / context / eval patterns
  - 100-point quality rubric with the 3 research gates as load-bearing dimensions
  - Core templates + one fully worked gold-standard example (research sub-agent fleet)
  - Net-new gap-filling prompts (G1–G4) and the guided factory were deferred to Phases 2–3.

---

**Start designing:** [SYSTEM_QUICK_START.md](SYSTEM_QUICK_START.md)
