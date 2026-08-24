---
title: "First-Failure Cause Isolator"
category: prompt-engineering/debugging
description: "Given a bad output, name the single primary cause from a fixed taxonomy and emit one corrective edit."
techniques:
  - ST-02
  - ST-03
  - QA-01
  - DC-01
difficulty: intermediate
tags:
  - root_cause
  - first_failure
  - triage
  - debugging
  - fixed_taxonomy
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/debugging/debug_failure_mode_taxonomy.md
  - domain-prompt-engineering/debugging/debug_minimal_repro_isolator.md
  - domain-prompt-engineering/debugging/debug_multi_turn_drift_diagnosis.md
---

## Objective

Given a single (prompt, input, bad output, predicate) tuple, name exactly one primary cause from a fixed cause taxonomy and emit one corrective edit. Distinct from `debug_failure_mode_taxonomy.md` — that names the *symptom class*, this names the *cause root*.

## When to Use

- After classifying with `debug_failure_mode_taxonomy.md`.
- When a fix needs to ship and the team needs to agree on what to change.
- For populating a defect database with structured root-cause entries.

## Cause Taxonomy (fixed; pick exactly one)

| Code | Cause | Fix shape |
|------|-------|-----------|
| C1 | Missing rule | Required behavior never stated. → ADD rule. |
| C2 | Vague rule | Rule present but unfalsifiable. → REWRITE rule with measurable predicate. |
| C3 | Conflicting rules | Two rules disagree, no precedence. → ADD precedence OR DELETE one. |
| C4 | Negation priming | "Do not X" rule increases X. → REWRITE as positive form. |
| C5 | Missing example | Behavior is correctly specified but un-anchored. → ADD one canonical example. |
| C6 | Schema gap | Output structure not declared. → ADD schema with required fields. |
| C7 | Input ambiguity | The input itself permits multiple valid interpretations. → ADD input pre-processing or clarify in prompt. |
| C8 | Model capability | Task exceeds model's known capability at that size/family. → SWAP model OR add tool support. |
| C9 | Sampling noise | Failure not reproducible at T=0. → No prompt change; pin T or accept rate. |
| C10 | Context overflow | Required information lost from context window. → ADD rolling summary or move to system. |
| C11 | Tool result pollution | Tool output reshaped behavior. → ADD sanitization or schema-strict tool wrapping. |
| C12 | Self-conditioning | Model's earlier output set the wrong precedent. → ADD periodic self-audit OR clear history. |

## Inputs

- `PROMPT_TEXT`, `INPUT`, `BAD_OUTPUT`, `FAILURE_PREDICATE`.
- `RECENT_CONTEXT` (turns / tool results) if conversational.
- `MODEL_ID`, `TEMPERATURE`.

## Constraints

### Must
- Output exactly one cause code.
- Cite at least one piece of evidence for the chosen cause (rule ID, input span, prior turn index, or T value).
- Output exactly one corrective edit in the form `ACTION: <ADD|DELETE|REWRITE|SWAP>` with the literal text to add or replace.
- Set `confidence: high|medium|low` based on whether the chosen rule alone falsifies the failure.
- If `confidence = low`, list the top 2 alternative causes with brief reasons.

### Must Not
- Pick more than one cause.
- Recommend "review the whole prompt."
- Skip the corrective edit field.

## Decision Procedure

Apply in order; first match wins:

1. Failure rate at T=0 is < 0.5 (per `debug_temperature_sensitivity_probe.md`) → **C9**.
2. Required information was outside model's effective context → **C10**.
3. Conversational; recent tool result contradicts rule → **C11**.
4. Conversational; model's own prior output already drifted → **C12**.
5. Two rules in prompt jointly justify both correct and bad output → **C3**.
6. The relevant rule is missing → **C1**.
7. The relevant rule exists but is unfalsifiable → **C2**.
8. The relevant rule contains a negation priming the failure → **C4**.
9. Output structure undeclared → **C6**.
10. Behavior is specified but no example anchors it → **C5**.
11. Input is genuinely ambiguous → **C7**.
12. None of the above apply and the failure persists across rephrasings → **C8**.

## Output Format

```
CAUSE
code: C<n>
evidence: "<verbatim quote or location reference>"
confidence: high|medium|low

CORRECTIVE_EDIT
action: ADD|DELETE|REWRITE|SWAP
target: <rule ID, schema field, model_id, OR "new rule R<n>">
new_text: |
  <the exact text to insert or replace with>

ALTERNATIVES (only if confidence = low)
- <Code>: <one-line reason>
- <Code>: <one-line reason>

VERIFICATION_TEST
input: <the input that failed>
expected_property: <predicate that should now pass>
```

## Verification

- Code is exactly one of C1–C12? (yes/no)
- `evidence` cites a concrete artifact (rule ID, span, index, value)? (yes/no)
- Apply the corrective edit; rerun the failing input N=10 at the original temperature; failure rate must drop by ≥ 0.5.
- If failure rate does not drop, escalate confidence down a level and revisit alternatives.

## Examples

BAD_OUTPUT: "Sure, here is the JSON: { ... }" with prompt rule "Do not include preamble."
- code: C4 (negation priming)
- action: REWRITE
- target: rule D3
- new_text: "Begin your reply with `{`."
- expected_property: output[0] == '{'
