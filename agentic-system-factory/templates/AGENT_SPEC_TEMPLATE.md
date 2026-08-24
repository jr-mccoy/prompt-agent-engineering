# AGENT SPEC — `<agent name>`

> One per agent in the system. Fill during Step 3. An agent is a security principal — its authority boundary and tool set are load-bearing, not documentation.

**Agent:** `<name>` · **System:** `<system>` · **Role in topology:** `<orchestrator | worker | router | evaluator | …>`

---

## Identity & authority
- **Governed identity:** `<unique id; how actions are attributed>`
- **Model (right-sized):** `<model + why this tier>`
- **Authority boundary:**
  | Can do (no approval) | Ask first (HITL) | Never |
  |----------------------|------------------|-------|
  | `<read X>` | `<send/spend/delete>` | `<out-of-scope actions>` |

## Role & instructions
- **Purpose (one sentence):** `<…>`
- **System-prompt altitude:** `<heuristic where, prescriptive where>`
- **Inputs it trusts vs treats as untrusted:** `<…>`

## Tools (minimized — more tools ≠ better)
| Tool | Scope/permission | Spec |
|------|------------------|------|
| `<namespaced_tool>` | least-privilege | → [TOOL_SPEC_TEMPLATE.md](TOOL_SPEC_TEMPLATE.md) |

## Memory & state
- **Context strategy:** `<full-raw | summary | fresh-instruction-only>`
- **Memory:** `<none | in-context | external notes | RAG>` + integrity controls (SAFE-06)
- **What it persists / returns:** `<condensed summary? raw? to whom>`

## Guardrails (positions)
- **Input guardrail:** `<…>` (fires on first agent)
- **Tool-call guardrail:** `<schema/allowlist validation>`
- **Output/final guardrail:** `<…>` (fires on last agent) · **tripwire ⇒ halt**

## Loop & bounds
- **Stop condition:** `<typed final output / explicit done>`
- **`max_turns`:** `<N>` · **cap-fallback:** `<…>`

## Handoffs (if any)
- **Hands off to:** `<agents>` · **type:** `<delegate ownership | agent-as-tool>`
- **On downstream failure:** `<recovery/escalation>`

## Eval hooks
- **Capability tasks that exercise this agent:** `<ids from EVAL_HARNESS>`
- **Safety scenarios targeting its tools:** `<ids>`

## Failure modes
| Failure | Mitigation | Detected by |
|---------|-----------|-------------|
| | | |
