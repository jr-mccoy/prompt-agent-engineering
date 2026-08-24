---
title: "Clean Refusal When Retrieved Context Is Insufficient"
category: prompt-engineering/rag-prompts
description: "Force the model to emit a structured 'no answer' response — naming what's missing and what was searched — instead of confabulating when retrieved passages do not support the question."
techniques:
  - ST-01
  - ST-03
  - CM-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - rag
  - refusal
  - no_answer
  - hallucination_control
  - structured_output
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/rag-prompts/rag_grounding_contract.md
  - domain-prompt-engineering/hallucination-control/hallucination_grounding_only_pattern.md
  - domain-prompt-engineering/rag-prompts/rag_followup_question_handler.md
---

# Clean Refusal When Retrieved Context Is Insufficient

**Objective:** Specify a refusal contract the model must use whenever the retrieved passages do not contain enough evidence to answer. The refusal must (a) classify the cause, (b) name the missing fact, (c) list what was retrieved, and (d) propose a next action.

**When to use:** Any RAG path where users currently get fluent but unsupported answers when the right passage is not in context. This is the most common cause of RAG hallucination.

---

## Inputs

1. `passage_manifest` — list of `{id, title, snippet}` for every passage retrieved this turn.
2. `question` — verbatim user question.
3. `min_support` — minimum passages required to answer (integer, default 1).
4. `next_action_options` — subset of `{retry_with_expansion, ask_clarifying_question, escalate_to_human, abandon}`.

---

## Constraints

### Must
- Distinguish four refusal causes: `NO_RELEVANT_PASSAGE`, `PARTIAL_EVIDENCE`, `CONFLICTING_EVIDENCE`, `OUT_OF_SCOPE`.
- Name the specific missing fact in one sentence (e.g., "the Q3 2025 figure is not in the retrieved passages"), not a generic apology.
- List the retrieved passage IDs and one-line reason each was insufficient.
- Propose exactly one next action from `next_action_options`.
- Use the JSON schema below verbatim — no prose-only refusals.

### Must Not
- Apologize, hedge, or use phrases like "I'm sorry but" or "as an AI".
- Provide a "best guess" alongside the refusal.
- Mention training cutoff or model limitations as the cause if the real cause is missing context.
- Refuse on a question that is answerable from the passages but uses different vocabulary — that is a retrieval bug, not a refusal case.
- Suggest a next action not in `next_action_options`.

---

## Refusal Schema

```json
{
  "answered": false,
  "cause": "NO_RELEVANT_PASSAGE | PARTIAL_EVIDENCE | CONFLICTING_EVIDENCE | OUT_OF_SCOPE",
  "missing_fact": "<one sentence naming the specific gap>",
  "retrieved_summary": [
    {"id": "<passage_id>", "why_insufficient": "<one phrase: off_topic | wrong_entity | wrong_time | partial_match | low_specificity>"}
  ],
  "next_action": "retry_with_expansion | ask_clarifying_question | escalate_to_human | abandon",
  "clarifying_question": "<only if next_action == ask_clarifying_question; else null>"
}
```

---

## Cause Decision Rules

| Cause | Trigger |
|---|---|
| `NO_RELEVANT_PASSAGE` | Zero passages mention the question's primary entity or topic. |
| `PARTIAL_EVIDENCE` | Some entities present but not all attributes the question requests. |
| `CONFLICTING_EVIDENCE` | ≥ 2 passages give incompatible answers and no authority/recency rule resolves them. |
| `OUT_OF_SCOPE` | Question is outside the corpus domain (e.g., asks for personal opinion from a fact corpus). |

---

## Instructions

1. Classify each retrieved passage by relevance to the question's primary entity AND requested attribute.
2. If `relevant_count < min_support`, do not answer; emit refusal.
3. Apply cause table; pick the first matching cause top-to-bottom.
4. Choose `next_action`:
   - `NO_RELEVANT_PASSAGE` + retrieval was narrow → `retry_with_expansion`.
   - `PARTIAL_EVIDENCE` with a missing parameter → `ask_clarifying_question`.
   - `CONFLICTING_EVIDENCE` on a high-stakes domain → `escalate_to_human`.
   - `OUT_OF_SCOPE` → `abandon`.
5. Emit the JSON.

---

## Verification

- [ ] Output is the schema, no extra prose.
- [ ] `cause` matches the decision table.
- [ ] `missing_fact` names a specific entity/attribute, not a category.
- [ ] `retrieved_summary` has one row per retrieved passage.
- [ ] `next_action` ∈ `next_action_options`.
- [ ] No apology or self-reference about being an AI.

---

## Anti-Patterns

1. "I don't have enough information to answer." — too generic; no cause, no missing fact, no next action.
2. Refusal that lists 0 retrieved passages — means refusal was emitted before retrieval ran; bug.
3. Refusal followed by "but generally…" — defeats the purpose.
4. Refusal on a clearly answerable question — points to upstream retrieval/embedding fault.
