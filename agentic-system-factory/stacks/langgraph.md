# Stage-7 Stack Guide — LangGraph

> **Version-neutral inside the stack.** This maps the agnostic bundle's primitives to LangGraph constructs. Exact API signatures, class/function names, package versions, and model/pricing facts **drift** — every such fact is flagged **`[verify against current docs]`** and must not be asserted from memory. Output of Stage 7 is **scaffolding + specs + harness**, not a deployed service.

**When to use:** the user committed to LangGraph and Gate C has passed. LangGraph's explicit graph model makes it a good neutral target for the topology wiring. MCP may be used for tools.

---

## Transform map (agnostic → LangGraph)

| Agnostic bundle artifact | LangGraph construct | Notes |
|--------------------------|---------------------|-------|
| Topology (`ARCHITECTURE.md §3`) | A `StateGraph` with nodes + edges `[verify against current docs]` | Control flow lives in the graph (deterministic edges) vs. agent nodes (model-decided) — match the topology |
| Agent (`agents/*.md`) | A node (agent or tool-calling node) | Right-size the model per `§4.4`; model ID `[verify against current docs]` |
| Orchestrator-workers | Fan-out via the dynamic-dispatch construct (e.g., `Send`) `[verify against current docs]` | Workers run with isolated state; return condensed summaries |
| Sequential / routing | Plain edges / conditional edges | Conditional edge = the router |
| Tool (`tools/*.md`) | A tool bound to the relevant node (or an MCP tool) with the designed schema | Keep the ACI design |
| State | The graph's typed state object (shared channels) | Persist via a checkpointer for resumable runs |
| Gate A deterministic policy (allowlist) | A **pre-tool-call hook / guard node** that validates calls vs the allowlist/schema and routes to a deny path | Load-bearing deterministic enforcement — independent of model output |
| HITL approval gate | An interrupt / human-in-the-loop pause before high-risk nodes `[verify against current docs]` | Risk-adaptive |
| Loop bounds | Recursion/step limit `[verify against current docs]` + cap-fallback node | Define the fallback, not a silent stop |
| Kill switch | A `halt` flag in graph state checked by a guard node before action nodes | Routes to a safe-stop node when set |
| Context strategy | Compaction / external notes / sub-graph isolation per `§4.3` | Checkpointer enables resume-not-restart |
| Eval harness (`EVAL_HARNESS.md`) | Capability + safety suites run against the compiled graph | Keep the two gates separate |
| Disclosure manifest / runbook | Carried over as docs + an `AGENTS.md`/`CLAUDE.md` rules file | — |

## Carry the gates into code (do not drop any)
- **Deterministic allowlist** → a guard node / pre-tool hook that denies non-allowlisted or schema-invalid calls before they execute.
- **Loop bounds** → graph recursion/step limit + an explicit cap-fallback node.
- **Kill switch** → a `halt` channel in state, checked by a guard node ahead of every action node.
- **Checkpointing** → use a checkpointer so long runs resume rather than restart.

## Scaffold layout (suggested)
```
<system>-langgraph/
├── graph.py           # StateGraph: nodes + edges = the topology wiring
├── nodes/             # one module per agent node (from AGENT_SPEC)
├── tools/             # one module per TOOL_SPEC (or MCP)
├── guards/            # allowlist guard node + kill-switch check = deterministic enforcement
├── eval/              # capability/ and safety/ suites (kept separate)
├── runbook.md         # from RUNBOOK.md
└── AGENTS.md          # rules file for the coding agent that completes/deploys this
```

## Anti-fabrication reminders
- Do **not** assert current LangGraph class/function names, the exact `Send`/interrupt/recursion-limit API, package versions, or model IDs/pricing — flag each `[verify against current docs]`.
- Verify the graph/checkpointer/interrupt APIs against the official LangGraph docs at build time rather than trusting this guide.
