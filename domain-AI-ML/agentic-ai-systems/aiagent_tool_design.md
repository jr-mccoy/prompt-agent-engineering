---
title: "AI Agent Tool / Function Interface Design"
category: AI-ML/agentic-ai-systems
description: "Design tool and function interfaces an agent can call reliably — schemas, error contracts, idempotency, and least privilege — so the agent fails safely instead of hallucinating or causing irreversible damage."
techniques:
  - ST-02
  - CM-02
  - AG-28
  - QA-04
  - DS-06
difficulty: advanced
tags:
  - tool-design
  - function-calling
  - error-contracts
  - idempotency
  - least-privilege
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/agentic-ai-systems/aiagent_architecture_design.md
  - domain-AI-ML/agentic-ai-systems/aiagent_safety_sandboxing.md
  - domain-AI-ML/agentic-ai-systems/aiagent_failure_mode_analysis.md
---

# AI Agent Tool / Function Interface Design

**Objective:** Design the tools (functions/APIs) an agent calls so they are easy for a model to invoke correctly, hard to misuse, and safe when invoked wrongly — covering schema clarity, error contracts, idempotency, and least-privilege scoping — so tool failures degrade gracefully rather than turning into hallucinated calls or irreversible actions.

**When to Use:**
- Building or revising the tool set an agent uses, and you want the interfaces to drive correct behavior.
- The agent frequently calls tools with malformed arguments, retries unsafely, or "pretends" a tool succeeded.
- A tool can change real-world state (write, send, pay, deploy) and you need its blast radius bounded.

**When NOT to Use:**
- You haven't yet decided the agent's control loop or which tools it needs (start with `aiagent_architecture_design.md`).
- You only need sandboxing/permission enforcement at runtime (use `aiagent_safety_sandboxing.md`).

## Inputs / Context

Provide what you can:
- **Tool list & purpose** — each candidate tool, what it does, and whether it reads or changes state.
- **Underlying API/contract** — parameters, types, required vs. optional, and known error modes of the real system behind the tool.
- **Risk per tool** — reversible vs. irreversible; external side effects; cost per call.
- **Calling model context** — roughly how the agent decides to call (free-form vs. constrained), and any history of misuse.
- **Throughput / rate limits** — call ceilings, latency, and quotas the tool must respect.

## Constraints

**Must:**
- Give each tool a single clear purpose, a typed/validated schema, and a description written for the *model*, not for human docs.
- Define an explicit error contract: every failure returns a structured, distinguishable result the agent can act on — never a silent success.
- Scope each tool to least privilege and mark whether it is idempotent; for non-idempotent state-changers, specify safe-retry handling (e.g., idempotency key).

**Must Not:**
- Design a single "do-everything" tool with mode flags that the model must orchestrate.
- Return ambiguous errors (e.g., raw stack traces or `null`) that the agent will paper over with a hallucinated outcome.
- Grant a tool broader scope, write access, or rate headroom than the task requires.

**Instructions:**

1. **One purpose per tool.** Split overloaded tools so each does one verifiable thing. Name and describe it from the agent's decision perspective ("when should I call this?"), and state read-only vs. state-changing explicitly in the description.

2. **Specify the input schema with guardrails in the types.** Use enums over free text, required vs. optional, ranges/formats, and validation that rejects bad input *before* any side effect. Make impossible-to-misuse the default.

3. **Define the error contract.** Enumerate failure modes (invalid args, not-found, rate-limited, upstream-down, permission-denied, partial-success) and give each a distinct structured response the agent can branch on. Errors must be actionable, not just descriptive.

4. **Handle idempotency and retries.** Mark each tool idempotent or not. For non-idempotent state-changers, require an idempotency key or a pre-check-then-act pattern so a retried call cannot double-charge, double-send, or double-write.

5. **Apply least privilege and bound the blast radius.** Scope credentials, allowed targets, and rate limits to the minimum the task needs. For irreversible actions, require a confirmation/approval token or route through a human gate (cross-link `aiagent_human_in_the_loop_design.md`).

6. **Attach cost, latency, and safety metadata.** Record per-call cost and latency and the worst-case effect of a wrong call, so the agent loop and budget breakers can reason about tool use (cross-link `aiagent_cost_token_budget_design.md`).

7. **Write a misuse test set.** For each tool, list the wrong calls a model is likely to make (missing arg, wrong enum, retry after success) and confirm the schema/error contract handles each safely.

**Output Format:**

A markdown tool spec per tool, plus a summary:
- **Tool Catalog** — table: Tool | Read/Write | Idempotent? | Risk | Least-privilege scope
- **Per-Tool Spec** — purpose, model-facing description, input schema, error contract (table of failure → structured response), retry/idempotency rule
- **Misuse Test Set** — likely wrong calls + expected safe handling
- **Cost/Latency/Safety Metadata** — per-tool table

## Verification

- [ ] Each tool has one purpose and a model-facing description stating read vs. write.
- [ ] Every tool has an enumerated error contract with distinct, actionable structured responses.
- [ ] Every non-idempotent state-changer specifies a safe-retry mechanism.
- [ ] Each tool's scope, credentials, and rate limits are least-privilege for the task.
- [ ] A misuse test set exists and each likely wrong call has a defined safe outcome.

## False-Positive Prevention

❌ **DON'T:**
- Call a tool "well-designed" because the happy-path schema validates — without testing the wrong-argument and retry-after-success paths.
- Return errors as free-text or raw exceptions and assume the agent will interpret them correctly.
- Mark a tool idempotent because it "usually" is; un-keyed state-changers are not idempotent under retry.
- Grant write or broad scope "to be safe for future use" — that enlarges the blast radius now.

✅ **DO:**
- Validate tool quality against a misuse set (malformed args, repeated calls, partial success), not just the happy path.
- Make every failure a structured, branchable result so the agent acts on it instead of hallucinating success.
- Require idempotency keys (or pre-check-then-act) for any call that creates, charges, sends, or deploys.
- Scope to least privilege today and widen only when a concrete task requires it.

## Example Output

```markdown
## Tool Spec: refund_payment

### Tool Catalog (excerpt)
| Tool | R/W | Idempotent? | Risk | Scope |
|---|---|---|---|---|
| lookup_order | Read | Yes | None | read:orders |
| refund_payment | Write | Yes (via key) | Irreversible/external | write:refunds, ≤ order total |

### Per-Tool Spec: refund_payment
- Purpose: issue a refund for one order, up to its captured amount.
- Model-facing description: "Use ONLY after lookup_order confirms a refundable charge. State-changing and irreversible."
- Input schema: `order_id: str (required)`, `amount_cents: int (1..order_total)`, `reason: enum[duplicate, defective, goodwill]`, `idempotency_key: str (required)`.
- Error contract:
  | Failure | Structured response | Agent action |
  |---|---|---|
  | order not found | `{error:"not_found"}` | stop, do not retry |
  | amount > total | `{error:"amount_exceeds_total", max}` | clamp or escalate |
  | duplicate key seen | `{status:"already_refunded", refund_id}` | treat as success |
  | upstream down | `{error:"upstream_unavailable", retryable:true}` | retry w/ same key, max 3 |
- Retry/idempotency: same `idempotency_key` returns the original result; safe to retry.

### Misuse Test Set
- Calls refund without prior lookup → blocked by description + not_found.
- Retries after success without key → would double-refund; key makes it a no-op.
- Passes `amount` over total → rejected with max returned.

### Cost/Latency/Safety Metadata
| Tool | Cost/call | Latency p95 | Worst-case if wrong |
|---|---|---|---|
| refund_payment | $0 (internal) | 400ms | Over-refund → bounded by ≤ total + idempotency |
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** purpose → schema → error contract → idempotency → privilege.
- **CM-02 (Constraint Specification):** least privilege, rate limits, and amount caps are governing constraints.
- **AG-28 (Tool Use / Function Calling Design):** schemas and contracts are written for reliable model invocation.
- **QA-04 (Edge Case Handling):** the misuse test set drives the error and retry design.
- **DS-06 (Prioritization & Severity Guidance):** tools are ranked by risk to focus hardening effort.

**Related Prompts:**
- `aiagent_architecture_design.md` — decide which tools the loop needs before specifying them.
- `aiagent_safety_sandboxing.md` — enforce the least-privilege scopes at runtime.
- `aiagent_failure_mode_analysis.md` — many failures originate at the tool boundary.
