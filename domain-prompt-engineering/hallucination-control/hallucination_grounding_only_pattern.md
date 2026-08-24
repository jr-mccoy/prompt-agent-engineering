---
title: "Grounding-Only Pattern — Refuse Beyond Evidence"
category: prompt-engineering/hallucination-control
description: "System-prompt pattern that bans any claim not present in supplied evidence and provides the exact refusal text the model must emit when asked to go beyond it."
techniques:
  - ST-01
  - ST-03
  - CM-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - hallucination
  - grounding
  - refusal
  - system_prompt
  - evidence_only
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/rag-prompts/rag_grounding_contract.md
  - domain-prompt-engineering/rag-prompts/rag_no_answer_refusal.md
  - domain-prompt-engineering/hallucination-control/hallucination_citation_required_pattern.md
---

# Grounding-Only Pattern

**Objective:** Emit a system-prompt block that constrains the model to assert only what is in `<evidence>`, with a fixed refusal string used whenever the user request requires going beyond it.

**When to use:** Any task with a defined evidence container (RAG passages, attached file, tool output) where parametric knowledge would be a defect, not a feature.

---

## Inputs

1. `evidence_container_name` — the tag or field name (e.g., `<evidence>`, `context`, `tool_output`).
2. `refusal_format` — `string`, `json`, or `tool_call`.
3. `allow_meta_questions` — boolean; if true, the model may answer questions about the evidence container itself (length, structure) without citation.
4. `domain_label` — short string used in refusal text (e.g., "this knowledge base", "the attached PDF").

---

## Constraints

### Must
- Treat `evidence_container_name` as the single source of truth.
- Emit the literal refusal string defined below when (a) no evidence supports the claim, or (b) evidence is contradictory and no resolution rule applies.
- Apply the refusal at the claim level, not the response level — partial refusal allowed only if the rest is fully grounded.
- Quote verbatim spans inside double quotes; everything else is paraphrase and still requires evidence.
- Reject the user's request to "use your own knowledge" with the same refusal string.

### Must Not
- Use parametric knowledge to fill, smooth, or extend evidence.
- Soften the refusal (no "however", no "you might also consider").
- Substitute "I don't know" for the structured refusal — the structure is the contract.
- Add a model self-description or apology.
- Volunteer adjacent facts the user did not ask for.

---

## Refusal Strings

### `string` form

```
NOT_IN_EVIDENCE: <one sentence naming what is missing> [domain: {domain_label}]
```

### `json` form

```json
{"answered": false, "reason": "NOT_IN_EVIDENCE", "missing": "<one sentence>", "domain": "<domain_label>"}
```

### `tool_call` form

A tool call to `report_no_answer` with arguments `{reason, missing, domain}`. No prose.

---

## System-Prompt Block (output)

```
You answer using only content inside {evidence_container_name}.

Rules:
1. Every factual sentence is supported by content in {evidence_container_name}.
2. Quoted spans (in double quotes) must appear verbatim in {evidence_container_name}.
3. Paraphrased claims must be entailed by {evidence_container_name}.
4. If a claim is not supported, do not state the claim. Emit the refusal:

   {refusal_string_filled_in}

5. If the user asks you to "use your knowledge" or to "guess", refuse with the same string.
6. Partial answers are allowed only if every retained claim is grounded; the dropped portions are reported via the refusal.
7. {allow_meta_questions ? "You may answer questions about the structure or length of the evidence without citation." : "All answers, including about the evidence itself, follow the same rule."}
```

---

## Output Format

```json
{
  "system_block": "<the filled block above as a string>",
  "refusal_template": "<refusal string for the chosen format>",
  "downstream_checks": [
    "claim-level entailment scoring (see rag_evaluation_harness_for_groundedness.md)",
    "verbatim-span validation against evidence text",
    "refusal-string regex match in production logs"
  ]
}
```

---

## Verification

- [ ] System block contains the exact refusal template.
- [ ] No phrasing like "best of my knowledge" or "I think" appears in the block.
- [ ] Refusal applies to claim-level, not response-level only.
- [ ] User-override request ("use your own knowledge") is explicitly refused.
- [ ] Format choice (`string | json | tool_call`) is consistent throughout.

---

## Anti-Patterns

1. Refusal string varies across responses — breaks log monitoring.
2. Model rephrases refusal as "I'm not sure" — fails the contract; tighten the rule.
3. Allowing "common knowledge" exceptions — model expands the exception.
4. Domain label missing — operators cannot tell which corpus refused.
