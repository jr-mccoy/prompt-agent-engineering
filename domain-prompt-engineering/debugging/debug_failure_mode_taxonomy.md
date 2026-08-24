---
title: "Prompt Failure Mode Taxonomy Classifier"
category: prompt-engineering/debugging
description: "Classify a failed model output into one of seven failure modes from a fixed taxonomy and emit the recommended next debug step."
techniques:
  - ST-02
  - ST-03
  - QA-01
  - DC-01
difficulty: intermediate
tags:
  - failure_modes
  - taxonomy
  - debugging
  - triage
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/debugging/debug_minimal_repro_isolator.md
  - domain-prompt-engineering/debugging/debug_first_failure_cause_isolator.md
  - domain-prompt-engineering/instruction-design/instruction_conflict_taxonomy.md
---

## Objective

Given a failed model output and the prompt that produced it, name the single primary failure mode from a fixed seven-class taxonomy and emit the next debug action.

## When to Use

- A bug is reported but no one has classified it.
- Triage stage before assigning a debug technique.
- Building a failure dashboard across many incidents.

## Taxonomy (fixed; choose exactly one)

| Code | Name | Definition |
|------|------|------------|
| F1 | Omission | Required output element absent. |
| F2 | Extra | Forbidden element present (e.g., preamble, trailing text). |
| F3 | Ambiguity | Output is one of several valid interpretations of an under-specified rule. |
| F4 | Conflict | Two prompt rules can both apply; model picked the wrong one. |
| F5 | Model deviation | Prompt is unambiguous; model still violated it (instruction-following failure). |
| F6 | Hallucination | Output asserts a fact not derivable from prompt or grounding. |
| F7 | Format break | Output structure does not parse against declared schema. |

If multiple apply, choose the deepest cause (F4 over F2, F3 over F5).

## Inputs

- `PROMPT_TEXT`.
- `INPUT`.
- `OUTPUT` (the failing model output).
- `EXPECTED_PROPERTIES`: list of properties the output should satisfy.

## Constraints

### Must
- Choose exactly one code from F1–F7.
- Cite the smallest evidence span (≤ 200 chars) supporting the classification.
- Emit a `next_step` from the fixed action map below.
- If `OUTPUT` is empty or the call errored, classify as F7 (`format_break: empty_output`).

### Must Not
- Assign two codes.
- Speculate about model internals.
- Recommend "rewrite the whole prompt" as `next_step`.

## Decision Procedure

Apply in order; first match wins:
1. Output unparseable against declared schema → **F7**.
2. Output is missing a property listed in `EXPECTED_PROPERTIES` and the prompt clearly required it → **F1**.
3. Output contains a forbidden element clearly banned by the prompt → **F2**.
4. Two rules in the prompt could each justify the output → **F4**.
5. The relevant rule is vague (no measurable criterion) → **F3**.
6. Output asserts a specific fact (name, number, date) absent from input → **F6**.
7. Otherwise → **F5**.

## Action Map (`next_step`)

| Code | next_step |
|------|-----------|
| F1 | Run `instruction_imperative_vs_declarative.md` — likely declarative miss. |
| F2 | Run `instruction_negation_audit.md` on the rule banning the element. |
| F3 | Run `correctness_vague_requirements_translator.md` on the under-specified rule. |
| F4 | Run `instruction_conflict_taxonomy.md`. |
| F5 | Run `modelbehavior_instruction_deviation_diagnostic.md`. |
| F6 | Run a hallucination-control prompt; check if grounding was provided. |
| F7 | Run `debug_minimal_repro_isolator.md`, then add a JSON validator second-pass. |

## Output Format

```
CLASSIFICATION
code: F<n>
evidence_span: "<≤200 char quote from OUTPUT>"
violated_rule_id: <id or null>
explanation: <one sentence ≤30 words>
next_step: <from action map>
confidence: high|medium|low
```

## Verification

- Code is one of F1–F7? (yes/no)
- `evidence_span` is a literal substring of `OUTPUT`? (yes/no)
- For F1/F2/F4, `violated_rule_id` is set? (yes/no)
- Run two reviewers; require agreement on code or escalate to F4 (default to deepest cause).

## Examples

OUTPUT: "Sure! Here is the JSON:\n{...}"
PROMPT had: "MUST output JSON only, no preamble."
→ code: F2, evidence_span: "Sure! Here is the JSON:", next_step: instruction_negation_audit.
