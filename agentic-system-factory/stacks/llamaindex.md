# Stage-7 Stack Guide — LlamaIndex

> **Version-neutral inside the stack.** This maps the agnostic bundle's primitives to LlamaIndex agent constructs. Exact API signatures, class names, package versions, model IDs, and pricing **drift** — every such fact below is flagged **`[verify against current docs]`** and must not be asserted from memory. Output of Stage 7 is **scaffolding + specs + harness**, not a deployed service.

**When to use:** the user committed to LlamaIndex and Gate C has passed. LlamaIndex is a strong fit when the system is retrieval-heavy (RAG over the user's data) and uses `AgentWorkflow` to coordinate agents. MCP may be used for tools. Canonical reference: `developers.llamaindex.ai` `[verify against current docs]`.

---

## Transform map (agnostic → LlamaIndex)

| Agnostic bundle artifact | LlamaIndex construct | Notes |
|--------------------------|----------------------|-------|
| Agent (`agents/*.md`) | A `FunctionAgent` (name + description + system prompt + tools + LLM) | Right-size the model per `ARCHITECTURE.md §4.4`; model ID `[verify against current docs]` |
| Topology (`ARCHITECTURE.md §3`) | An `AgentWorkflow` (one **root agent**; agents hand off to coordinate) or an explicit event-driven `Workflow` for custom control flow | Root-agent routing for handoff topologies; a custom `Workflow` (steps + events) for deterministic pipelines/loops |
| Orchestrator-workers | Root agent delegating to specialist agents; sub-results merged | Keep sub-agent context isolated; return condensed results |
| Tool (`tools/*.md`) | A function tool (type-annotated, sync/async); context-aware tools; query-engine tools for RAG; MCP tools | Keep the ACI design: workflow-shaped, errors-as-guidance, semantic identifiers |
| Gate A deterministic policy (allowlist) | A **tool wrapper / validation step** that checks each call vs the allowlist/schema and can deny (a guard step in the `Workflow`) | The wrapper/guard is the load-bearing deterministic enforcement, independent of model output |
| HITL approval gate | A **human-in-the-loop tool** (a tool that pauses for human confirm/feedback before a high-risk action) `[verify against current docs]` | Risk-adaptive |
| Loop bounds | Workflow step/iteration cap + cap-fallback `[verify against current docs]` | Define the fallback, not a silent stop |
| Kill switch | A `halt` flag in the workflow `Context` checked by a guard step before action tools | When set, deny action tools |
| State / memory | The workflow `Context` (set/get variables shared across steps and tools); external store for resumable runs | Persist resumable state externally |
| Eval harness (`EVAL_HARNESS.md`) | Capability + safety suites; LlamaIndex eval modules for RAG faithfulness where relevant `[verify against current docs]` | Keep capability and safety as **separate** gates; add groundedness checks if RAG |
| Disclosure manifest / runbook | Carried over as docs + an `AGENTS.md`/`CLAUDE.md` rules file | — |

## Carry the gates into code (do not drop any)
- **Deterministic allowlist** → a tool wrapper / guard step that denies non-allowlisted or schema-invalid calls before execution.
- **Sandbox code execution** → run any code/exec tools in an isolated sandbox `[verify against current docs]`; human review of destructive code.
- **Loop bounds** → workflow step/iteration cap + an explicit cap-fallback.
- **Kill switch** → `halt` flag in `Context`, checked by a guard step ahead of every action tool.
- **Groundedness (if RAG)** → a citation/faithfulness check so retrieved data is cited, not fabricated.

## Scaffold layout (suggested)
```
<system>-llamaindex/
├── agents/            # FunctionAgent definitions (one per AGENT_SPEC)
├── workflow.py        # AgentWorkflow (root + handoffs) or custom Workflow = the topology
├── tools/             # function / query-engine / MCP tool modules
├── guards/            # allowlist wrapper + kill-switch guard step = deterministic enforcement
├── eval/              # capability/ and safety/ suites (kept separate; + RAG faithfulness if applicable)
├── runbook.md         # from RUNBOOK.md
└── AGENTS.md          # rules file for the coding agent that completes/deploys this
```

## Anti-fabrication reminders
- Do **not** assert current model IDs, the LlamaIndex package name/version, exact class/function names (`FunctionAgent`, `AgentWorkflow`, `Workflow`, `Context`, etc.), or pricing — flag each `[verify against current docs]`.
- Confirm the `AgentWorkflow`/`Workflow`, HITL-tool, and `Context` APIs against the current LlamaIndex docs at build time rather than from this guide.
