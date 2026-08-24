# Stage-7 Stack Guide — Microsoft Agent Framework (MAF)

> **Version-neutral inside the stack.** This maps the agnostic bundle's primitives to Microsoft Agent Framework constructs. Exact API signatures, class/builder names, package versions, model IDs, and pricing **drift** — every such fact below is flagged **`[verify against current docs]`** and must not be asserted from memory. Output of Stage 7 is **scaffolding + specs + harness**, not a deployed service.

**When to use:** the user committed to Microsoft Agent Framework (Python or .NET) and Gate C has passed. MAF models orchestration as **graph-based workflows** with named patterns; MCP may be used for tools. Canonical reference: `learn.microsoft.com/agent-framework` `[verify against current docs]`.

---

## Transform map (agnostic → Microsoft Agent Framework)

| Agnostic bundle artifact | Microsoft Agent Framework construct | Notes |
|--------------------------|-------------------------------------|-------|
| Agent (`agents/*.md`) | An agent (instructions + tools + model) | Right-size the model per `ARCHITECTURE.md §4.4`; model ID `[verify against current docs]` |
| Topology (`ARCHITECTURE.md §3`) | A graph-based **workflow** with the matching orchestration pattern: sequential, concurrent, handoff, group-chat, or Magentic | Map the chosen rung to the pattern: pipeline→sequential, fan-out→concurrent, routing→handoff, orchestrator-workers→Magentic (manager + subagents) |
| Handoff / routing | Handoff orchestration (`HandoffBuilder` registers handoff tools) `[verify against current docs]` | Star/handoff topology per the design; no peer channel unless allowed |
| Tool (`tools/*.md`) | A registered tool / function; MCP server tools | Keep the ACI design; MAF can RAG over tool descriptions to present only relevant tools — still enforce the allowlist |
| Gate A deterministic policy (allowlist) | A **tool-invocation filter / middleware** that validates each call vs the allowlist/schema and can deny | The filter is the load-bearing deterministic enforcement, independent of model output `[verify against current docs]` |
| HITL approval gate | Built-in human-in-the-loop approval / pause on high-risk steps | Risk-adaptive; MAF supports pause/resume |
| Loop bounds | Workflow step/iteration limit + cap-fallback `[verify against current docs]` | Define the fallback, not a silent stop |
| Kill switch | A `halt` flag checked by the tool filter / a guard step before action steps | When set, deny action steps |
| State / durability | Checkpointing + streaming; external store for resumable runs | MAF supports checkpointing and time-travel `[verify against current docs]` — use it for resume-not-restart |
| Eval harness (`EVAL_HARNESS.md`) | Capability + safety suites run against the compiled workflow | Keep capability and safety as **separate** gates |
| Disclosure manifest / runbook | Carried over as docs + an `AGENTS.md`/`CLAUDE.md` rules file | — |

## Carry the gates into code (do not drop any)
- **Deterministic allowlist** → a tool-invocation filter/middleware that denies non-allowlisted or schema-invalid calls before execution.
- **Sandbox code execution** → run code/exec tools in an isolated sandbox `[verify against current docs]`; human review of destructive code.
- **Loop bounds** → workflow step/iteration limit + an explicit cap-fallback.
- **Kill switch** → `halt` flag checked by the tool filter / a guard step ahead of every action step.
- **Checkpointing** → enable checkpointing so long workflows resume rather than restart.

## Scaffold layout (suggested)
```
<system>-maf/
├── agents/            # one module per AGENT_SPEC
├── workflow/          # graph workflow + orchestration pattern = the topology wiring
├── tools/             # tool/function modules (or MCP)
├── policy/            # tool-invocation filter = allowlist + kill switch = deterministic enforcement
├── eval/              # capability/ and safety/ suites (kept separate)
├── runbook.md         # from RUNBOOK.md
└── AGENTS.md          # rules file for the coding agent that completes/deploys this
```

## Anti-fabrication reminders
- Do **not** assert current model IDs, the MAF package name/version (Python or .NET), exact builder/class names (`HandoffBuilder`, workflow APIs, etc.), or pricing — flag each `[verify against current docs]`.
- Confirm the orchestration-pattern, HITL, and checkpointing APIs against the current MAF docs at build time rather than from this guide.
