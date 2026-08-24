# TOOL SPEC (ACI) — `<tool name>`

> One per tool. Fill during Step 3. Tools are the Agent-Computer Interface — the most underrated reliability + security lever. Build tools around **high-impact workflows, not API endpoints.** A tool that modifies the world is an authority boundary.

**Tool:** `<namespaced_name, e.g., research_sources_search>` · **Owner agent(s):** `<…>`

---

## Purpose & altitude
- **What workflow it serves (not which endpoint it wraps):** `<…>`
- **Why this is one tool, not three:** `<consolidation rationale>`
- **Namespace / related tools:** `<group, e.g., research_*>`

## Signature
```
<tool_name>(
  <arg>: <type>   # description that encodes expert implicit knowledge
  …
) -> <return type>
```
- **`response_format` enum (token control):** `<concise | detailed>` (concise ≈ ⅓ tokens)
- **Returns semantic identifiers** (name/url), not technical (uuid)? `<yes/no>`

## Schema & validation (SAFE-02)
- **Pre-execution validation:** `<schema + allowlist checks before the call runs>`
- **Permission scope (least privilege):** `<read-only | write:scope | …>`

## Errors as guidance
| Error condition | Message returned to the agent (actionable, not a code) |
|-----------------|--------------------------------------------------------|
| `<bad arg>` | `<"X must be a date in YYYY-MM-DD; you passed …">` |
| `<not found>` | `<"No match; try broadening …">` |

## Safety for state-modifying tools
- **Idempotency key:** `<how repeat calls are deduped>`
- **Dry-run / preview:** `<for destructive calls>`
- **Rollback path:** `<…>`
- **HITL required?** `<yes/no — which action classes>`

## Untrusted output handling
- **Does this tool return external/untrusted content?** `<yes/no>` → if yes, **data/control separation (SAFE-01)**: output is treated as data, never as instructions; cannot select the next tool.

## Eval
- **Iterate with evals:** `<agent-judged realistic tasks that exercise this tool>`
