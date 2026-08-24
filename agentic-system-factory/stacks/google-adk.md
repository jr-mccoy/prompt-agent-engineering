# Stage-7 Stack Guide — Google Agent Development Kit (ADK)

> **Version-neutral inside the stack.** This maps the agnostic bundle's primitives to Google ADK constructs. Exact API signatures, class names, package versions, model IDs, and pricing **drift** — every such fact below is flagged **`[verify against current docs]`** and must not be asserted from memory. Output of Stage 7 is **scaffolding + specs + harness**, not a deployed service.

**When to use:** the user committed to Google ADK and Gate C has passed. ADK is code-first; its explicit **workflow agents** make deterministic orchestration a first-class construct. MCP may be used for tools. Canonical reference: `google.github.io/adk-docs` `[verify against current docs]`.

---

## Transform map (agnostic → Google ADK)

| Agnostic bundle artifact | Google ADK construct | Notes |
|--------------------------|----------------------|-------|
| Agent (`agents/*.md`) | An `LlmAgent` (model-reasoning agent) | Right-size the model per `ARCHITECTURE.md §4.4`; model ID `[verify against current docs]` |
| Topology (`ARCHITECTURE.md §3`) | **Workflow agents** for deterministic flow: `SequentialAgent` (pipeline), `ParallelAgent` (fan-out), `LoopAgent` (evaluator-optimizer); `LlmAgent`-coordinated routing for dynamic flow | Pick the workflow agent that matches the chosen topology rung; deterministic order = workflow agent, content-dependent = LLM-coordinated |
| Orchestrator-workers | A coordinator `LlmAgent` over sub-agents, or `ParallelAgent` for fixed fan-out | Workers return condensed results; keep sub-agent state isolated |
| Tool (`tools/*.md`) | `FunctionTool` (custom function) or `AgentTool` (agent-as-tool); built-in tools / MCP | Keep the ACI design: workflow-shaped, errors-as-guidance, semantic identifiers |
| Gate A deterministic policy (allowlist) | A **`before_tool_callback`** that validates each call vs the allowlist/schema and can block | `[verify against current docs]` — this callback is the load-bearing deterministic enforcement, independent of model output |
| HITL approval gate | A callback / approval step that pauses high-risk tools for human sign-off | Risk-adaptive |
| Loop bounds | `LoopAgent` max-iterations + cap-fallback `[verify against current docs]` | Define the fallback, not a silent stop |
| Kill switch | A `halt` flag in session state checked by `before_tool_callback` before action tools | When set, block all action tools |
| State / memory | Session + state (shared via context); external store for resumable runs | Workers/sub-agents read/write scoped state, not raw blobs |
| Eval harness (`EVAL_HARNESS.md`) | ADK eval tooling for capability + a separate safety suite `[verify against current docs]` | Keep capability and safety as **separate** gates |
| Disclosure manifest / runbook | Carried over as docs + an `AGENTS.md`/`CLAUDE.md` rules file | — |

## Carry the gates into code (do not drop any)
- **Deterministic allowlist** → a `before_tool_callback` that denies non-allowlisted or schema-invalid calls before execution.
- **Sandbox code execution** → run code/exec tools in an isolated sandbox `[verify against current docs]`; human review of destructive code.
- **Loop bounds** → `LoopAgent` iteration cap + an explicit cap-fallback.
- **Kill switch** → `halt` flag in state, checked by the tool callback ahead of every action tool.

## Scaffold layout (suggested)
```
<system>-adk/
├── agents/            # LlmAgent definitions (one per AGENT_SPEC)
├── workflow.py        # SequentialAgent / ParallelAgent / LoopAgent wiring = the topology
├── tools/             # FunctionTool / AgentTool modules (or MCP)
├── callbacks/         # before_tool_callback = allowlist + kill-switch = deterministic enforcement
├── eval/              # capability/ and safety/ suites (kept separate)
├── runbook.md         # from RUNBOOK.md
└── AGENTS.md          # rules file for the coding agent that completes/deploys this
```

## Anti-fabrication reminders
- Do **not** assert current model IDs, the ADK package name/version, exact class/callback signatures (`LlmAgent`, `SequentialAgent`, `before_tool_callback`, etc.), or pricing — flag each `[verify against current docs]`.
- Confirm the workflow-agent and callback APIs against the current ADK docs at build time rather than from this guide.
