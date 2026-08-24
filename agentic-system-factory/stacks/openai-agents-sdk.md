# Stage-7 Stack Guide — OpenAI Agents SDK

> **Version-neutral inside the stack.** This maps the agnostic bundle's primitives to OpenAI Agents SDK (`openai-agents` Python) constructs. Exact API signatures, class/decorator names, package versions, model IDs, and pricing **drift** — every such fact below is flagged **`[verify against current docs]`** and must not be asserted from memory. Output of Stage 7 is **scaffolding + specs + harness**, not a deployed service.

**When to use:** the user committed to the OpenAI Agents SDK and Gate C has passed. MCP is assumed as the interop layer for tools. Canonical reference: the open-source docs at `openai.github.io/openai-agents-python` `[verify against current docs]`.

---

## Transform map (agnostic → OpenAI Agents SDK)

| Agnostic bundle artifact | OpenAI Agents SDK construct | Notes |
|--------------------------|-----------------------------|-------|
| Agent (`agents/*.md`) | An `Agent` (system prompt/instructions + tool set + model) | Right-size the model per `ARCHITECTURE.md §4.4`; model ID `[verify against current docs]` |
| Tool (`tools/*.md`) | A function tool (Python function → tool w/ generated schema) or an MCP server tool | Keep the ACI design: workflow-shaped, errors-as-guidance, semantic identifiers |
| Topology (`ARCHITECTURE.md §3`) | `Runner` drives the loop (turns, tools, handoffs); orchestrator-workers = agents-as-tools or sub-runs | The `Runner` is the control loop; don't hand-roll turn management |
| Handoff / routing | `handoffs` (delegate control to a specialized agent) | Star topology only if the design forbids peer channels |
| Gate A deterministic policy (allowlist) | An **input/output guardrail** + a tool-call wrapper that validates each call vs the allowlist/schema and can deny | Guardrails run alongside execution and **fail fast**; the allowlist wrapper is the load-bearing deterministic enforcement, independent of model output |
| HITL approval gate | An approval guardrail / tool wrapper that pauses high-risk tools for human sign-off | Risk-adaptive, not confirm-everything |
| Loop bounds | `max_turns` (Runner) `[verify against current docs]` + cap-fallback | Define the fallback behavior, not a silent stop |
| Kill switch | A config flag checked in the tool-call wrapper before any action-taking tool | When set, deny all action tools |
| Context / memory | `Sessions` (persistent working memory) + external state for resumable runs | Persist resumable state externally; keep sub-agent context isolated |
| Eval harness (`EVAL_HARNESS.md`) | Capability + safety suites run against the agent (tracing/eval tooling) | Keep capability and safety as **separate** suites/gates |
| Disclosure manifest / runbook | Carried over as docs + an `AGENTS.md`/`CLAUDE.md` rules file for a downstream coding agent | — |

## Carry the gates into code (do not drop any)
- **Deterministic allowlist** → a tool-call wrapper (+ guardrails) that denies non-allowlisted or schema-invalid calls before they execute.
- **Sandbox code execution** → run code tools in an isolated sandbox/workspace `[verify against current docs]`; human review of destructive code.
- **Loop bounds** → `max_turns` + an explicit cap-fallback.
- **Kill switch** → config flag checked before every action-taking tool call.

## Scaffold layout (suggested)
```
<system>-openai-agents/
├── agents/            # one module per AGENT_SPEC (Agent definitions)
├── tools/             # one module per TOOL_SPEC (function tools or MCP)
├── policy/            # guardrails + tool-call allowlist wrapper + kill switch = deterministic enforcement
├── run.py             # Runner wiring for the chosen topology (handoffs / agents-as-tools)
├── eval/              # capability/ and safety/ suites (kept separate)
├── runbook.md         # from RUNBOOK.md
└── AGENTS.md          # rules file for the coding agent that completes/deploys this
```

## Anti-fabrication reminders
- Do **not** assert current model IDs, the SDK package name/version, exact decorator/function names (`@function_tool`, `Runner.run`, etc.), or pricing — flag each `[verify against current docs]`.
- Treat the open-source `openai-agents-python` docs as the canonical primitive reference; confirm guardrail/handoff/session APIs at build time rather than from this guide.
