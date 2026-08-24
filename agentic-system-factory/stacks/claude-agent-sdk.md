# Stage-7 Stack Guide — Claude Agent SDK

> **Version-neutral inside the stack.** This maps the agnostic bundle's primitives to Claude Agent SDK constructs. Exact API signatures, model IDs, package names, and pricing **drift** — every such fact below is flagged **`[verify against current docs]`** and must not be asserted from memory. Output of Stage 7 is **scaffolding + specs + harness**, not a deployed service.

**When to use:** the user committed to the Claude Agent SDK and Gate C has passed. MCP is assumed as the interop layer for tools.

---

## Transform map (agnostic → Claude Agent SDK)

| Agnostic bundle artifact | Claude Agent SDK construct | Notes |
|--------------------------|----------------------------|-------|
| Agent (`agents/*.md`) | An agent definition with a system prompt + tool set + model | Right-size the model per `ARCHITECTURE.md §4.4`; model ID `[verify against current docs]` |
| Tool (`tools/*.md`) | A tool/function definition (or an MCP server tool) with the designed JSON schema | Keep the ACI design: workflow-shaped, errors-as-guidance, semantic identifiers |
| Topology (`ARCHITECTURE.md §3`) | Loop / orchestration wiring (single loop; subagents for orchestrator-workers) | Subagents return condensed summaries (sub-agent isolation) |
| Handoff | Agent-as-tool or explicit delegation | Star topology only if the design forbids peer channels |
| Gate A deterministic policy (allowlist) | A **pre-tool-use hook** that validates every tool call vs the allowlist/schema and can deny | This is the load-bearing "deterministic policy enforcement" layer — it blocks prohibited actions regardless of model output |
| HITL approval gate | A permission/approval callback on high-risk tools | Risk-adaptive, not confirm-everything |
| Loop bounds | `max_turns` / iteration cap `[verify against current docs]` | Define the cap-fallback, not a silent stop |
| Kill switch | A config flag checked in the pre-tool-use hook before any action | When set, deny all action-taking tools |
| Context strategy | Compaction / external notes / subagent isolation per `§4.3` | Persist resumable state externally |
| Eval harness (`EVAL_HARNESS.md`) | Capability + safety test scaffolds run against the agent | Keep capability and safety as separate suites/gates |
| Disclosure manifest / runbook | Carried over as-is (docs) + a `CLAUDE.md` rules file for a downstream coding agent | — |

## Carry the gates into code (do not drop any)
- **Deterministic allowlist** → pre-tool-use hook (deny by default; allow only schema-valid, allowlisted calls).
- **Sandbox code execution** → run any code tools in an isolated sandbox `[verify against current docs]` with human review of destructive code.
- **Loop bounds** → `max_turns` + explicit cap-fallback behavior.
- **Kill switch** → config flag checked before every action-taking tool call.

## Scaffold layout (suggested)
```
<system>-claude-sdk/
├── agents/            # one module per AGENT_SPEC
├── tools/             # one module per TOOL_SPEC (or MCP server)
├── policy/            # the pre-tool-use hook = deterministic enforcement + kill switch
├── eval/              # capability/ and safety/ suites (kept separate)
├── runbook.md         # from RUNBOOK.md
└── CLAUDE.md          # rules file for the coding agent that completes/deploys this
```

## Anti-fabrication reminders
- Do **not** assert the current model IDs, SDK package name/version, exact decorator/function names, or pricing — flag each `[verify against current docs]`.
- For authoritative, current Claude API / SDK facts (model IDs, pricing, tool-use, MCP), consult the repo's `claude-api` skill or the official docs at build time rather than this guide.
