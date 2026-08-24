---
title: "Reliable Structured Output & Function Calling"
category: AI-ML/genai-llm-engineering
description: "Make LLM structured output and function/tool calling reliable: schema design, output validation, constrained decoding, retry/repair on failure, and graceful handling of invalid or hallucinated calls."
techniques:
  - ST-02
  - CM-02
  - QA-12
  - RT-10
  - DS-02
difficulty: intermediate
tags:
  - structured-output
  - function-calling
  - tool-use
  - json-schema
  - validation
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/genai-llm-engineering/genai_llm_evaluation_design.md
  - domain-AI-ML/genai-llm-engineering/genai_guardrails_design.md
  - domain-AI-ML/genai-llm-engineering/genai_llm_observability_tracing.md
---

# Reliable Structured Output & Function Calling

**Objective:** Design an LLM integration that emits structured output (JSON/schema) or invokes functions/tools reliably — covering schema design, output validation, constrained/structured decoding where available, retry-and-repair on malformed output, and explicit handling of invalid arguments, hallucinated tools, and partial failures — so downstream code never silently consumes malformed or wrong calls.

**When to Use:**
- The LLM must return parseable data or call tools/functions that your code executes.
- Structured outputs sometimes fail to parse, miss fields, or call the wrong tool.
- You're wiring an agent/tool-use loop and need the tool interface to be robust.

**When NOT to Use:**
- The output is free-form prose with no schema (this is about structure).
- You're designing the full agent loop's planning/control (this covers the tool interface, not the policy).

## Inputs / Context

State the model + provider + version (structured-output and function-calling support varies by model/version). Provide what you can:
- **Target schema / tools** — the JSON schema or function signatures the model must produce/call.
- **Downstream consumer** — what happens with the output (DB write, API call, UI render) and its tolerance for error.
- **Failure cost** — what a malformed or wrong call would do (idempotent vs destructive).
- **Volume/latency** — how often, how fast, retry budget.
- **Current failures** — what's breaking today (parse errors, missing fields, wrong tool, hallucinated args).

## Constraints

**Must:**
- Validate every model output against the schema before any downstream use; never trust raw model output as valid.
- Use the provider's structured-output / function-calling / constrained-decoding feature if available, and verify support for the model version.
- Define the behavior on each failure mode: parse failure, schema-invalid, missing required field, hallucinated tool/argument, low-confidence call.

**Must Not:**
- Pass unvalidated model output to a destructive or non-idempotent action.
- Assume a successful parse means the *values* are correct — validate types, enums, ranges, and referential integrity.
- Fabricate which structured-output features a model supports; require verification against current provider docs.

**Instructions:**

1. **Design the schema for the model, not just the consumer.** Use clear field names, descriptions, enums over free strings, required vs optional, and avoid deeply nested/ambiguous structures that models fill inconsistently. Document each field's meaning in the schema.

2. **Use native structured output / function calling.** If the model/version supports JSON-schema-constrained output or tool calling, use it — it removes most parse failures. Verify the feature and its limits against current docs; fall back to prompt-instructed JSON + parsing only where unsupported.

3. **Validate against the schema.** After generation, validate syntax (parses) and semantics (types, required fields, enums, value ranges, cross-field/referential constraints). Treat validation failure as a control-flow event, not an exception to swallow.

4. **Design retry-and-repair.** On validation failure, re-prompt with the specific error (e.g., "field X must be one of [...]; you returned Y") and a bounded retry count. Distinguish transient (re-ask) from structural (schema/prompt fix) failures.

5. **Handle tool-call failure modes.** For function calling: reject hallucinated tool names, validate arguments against the tool's signature, and define behavior on missing/ambiguous arguments (ask, default, or abstain). Never execute a destructive tool on unvalidated args.

6. **Guard execution.** For tools with side effects, require validated args, idempotency keys where possible, and confirmation/dry-run for destructive actions. Log every call and result (cross-link `genai_llm_observability_tracing.md`).

7. **Define the give-up path.** After max retries, specify the fallback: human handoff, safe default, or surfaced error — never a silent malformed write.

8. **Evaluate reliability.** Measure parse-success rate, schema-validity rate, correct-tool/correct-arg rate, and retry distribution on a representative set (cross-link `genai_llm_evaluation_design.md`).

**Output Format:**

A markdown integration spec:
- **Schema / Tool Definitions** — fields/signatures with descriptions, enums, required flags
- **Generation Mode** — native structured output / function calling vs prompt+parse (with support verified)
- **Validation Rules** — syntactic + semantic checks (types, enums, ranges, referential)
- **Failure Handling** — table: Failure mode | Detection | Action (retry/repair/abstain)
- **Execution Guards** — idempotency, dry-run/confirmation for destructive tools
- **Give-Up Path** — fallback after max retries
- **Reliability Metrics** — what to measure + targets

## Verification

- [ ] Every output is validated (syntax + semantics) before downstream use.
- [ ] Native structured-output/function-calling support is verified against the model version, not assumed.
- [ ] Each failure mode (parse, schema, missing field, hallucinated tool/arg) has a defined action.
- [ ] Destructive tools require validated args + idempotency/confirmation.
- [ ] A bounded give-up path exists; no silent malformed writes.
- [ ] Reliability metrics (parse/validity/correct-call rates) are defined.

## False-Positive Prevention

❌ **DON'T:**
- Treat a successful JSON parse as "valid" — wrong enum values, out-of-range numbers, and broken references still pass parsing.
- Execute a tool call without validating the tool name and arguments against the signature.
- Retry indefinitely on a structural failure that re-prompting can't fix (schema is wrong).
- Assume a model version supports constrained decoding because a sibling model does.

✅ **DO:**
- Validate types, enums, ranges, and referential integrity, not just parseability.
- Reject hallucinated tools and invalid args; re-prompt with the specific error for repair.
- Bound retries and define a safe give-up path (human handoff / default / surfaced error).
- Verify structured-output/function-calling support for the exact model version in use.

## Example Output

```markdown
## Structured Output: Expense-Categorization Tool (model: <provider/model vX>)

### Schema
{ category: enum[travel,meals,software,other], amount: number>0, currency: enum[USD,EUR],
  needs_receipt: bool } — all required; descriptions per field.

### Generation Mode
Native JSON-schema-constrained output (verified supported on model vX). Fallback parse path
retained for the streaming variant which (verify) doesn't support constraints.

### Validation Rules
Parse -> category in enum -> amount > 0 -> currency in enum -> needs_receipt is bool.
Cross-field: amount > 75 implies needs_receipt = true (else flag).

### Failure Handling
| Mode | Detection | Action |
|---|---|---|
| Parse fail | json.parse error | re-prompt w/ raw error, max 2 |
| Bad enum | schema check | re-prompt: "category must be one of [...]" |
| Cross-field violation | rule check | flag for human review (don't auto-correct) |

### Execution Guards
Write to ledger is idempotent (keyed by expense_id). No destructive action; no confirmation needed.

### Give-Up Path
After 2 retries -> route expense to manual categorization queue; log trace.

### Reliability Metrics
Target: schema-validity ≥ 0.99, correct-category vs human ≥ 0.95 on 300-expense eval set.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** schema → generation → validate → repair → execute → give-up.
- **CM-02 (Constraint Specification):** the schema and execution guards are the governing constraints.
- **QA-12 (False Positives Identification):** parses-but-invalid and hallucinated-tool cases are caught.
- **RT-10 (Troubleshooting Decision Tree):** the failure-mode table routes each failure to an action.
- **DS-02 (Metric Specification):** reliability metrics make robustness measurable.

**Related Prompts:**
- `genai_llm_evaluation_design.md` — evaluate structured-output reliability as a quality dimension.
- `genai_guardrails_design.md` — output validation is a guardrail layer.
- `genai_llm_observability_tracing.md` — log tool calls and validation results.
