---
title: "Follow-up Question Handler — Re-retrieve or Reuse Prior Context"
category: prompt-engineering/rag-prompts
description: "Decision rule for whether a follow-up turn should reuse the prior turn's retrieved passages, re-retrieve with a rewritten query, or both."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DC-01
  - QA-01
difficulty: intermediate
tags:
  - rag
  - followup
  - conversation
  - retrieval_decision
  - context_reuse
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/rag-prompts/rag_query_rewriter.md
  - domain-prompt-engineering/rag-prompts/rag_no_answer_refusal.md
  - domain-prompt-engineering/rag-prompts/rag_freshness_aware_prompt.md
---

# Follow-up Question Handler — Re-retrieve or Reuse Prior Context

**Objective:** For each follow-up turn in a multi-turn RAG conversation, decide one of: `reuse`, `re_retrieve`, `augment` (reuse + add), or `clarify`. Output is a routing decision plus the rewritten query if retrieval is needed.

**When to use:** Any conversational RAG agent. Default behavior in most stacks is naive re-retrieval every turn, which loses prior context, or naive reuse, which misses topic shift. Both are wrong.

---

## Inputs

1. `prior_turn` — `{question, queries_used, retrieved_ids, answer}`.
2. `current_turn` — verbatim user message.
3. `corpus_volatility` — `static`, `slow`, or `live`.
4. `max_context_age_turns` — int; older context is auto-evicted.
5. `cost_profile` — `latency_sensitive` or `quality_first`.

---

## Constraints

### Must
- Output exactly one routing decision: `reuse`, `re_retrieve`, `augment`, or `clarify`.
- For `re_retrieve` or `augment`, emit a rewritten query that resolves pronouns and ellipsis using `prior_turn.question` and `prior_turn.answer`.
- For `augment`, list which prior `retrieved_ids` to keep and why.
- For `clarify`, emit a single concrete clarifying question — not "could you clarify".
- Detect topic shift via entity-set diff between turns; > 50% new entities forces `re_retrieve`.

### Must Not
- Reuse prior context if `corpus_volatility=live` and the current turn is time-sensitive.
- Re-retrieve when current turn is purely a refinement of formatting/length and no new factual claim is requested.
- Carry resolved pronouns silently into the answer; the rewritten query must show the resolution.
- Default to `re_retrieve` to be safe. The decision must be justified.

---

## Decision Rules

| Signal in current turn | Default decision |
|---|---|
| Pronoun/ellipsis only ("what about her?", "and the other one") | `re_retrieve` with resolved query |
| New entity not in prior context | `re_retrieve` |
| Same entity, new attribute | `augment` |
| Same entity, same attribute, asking for elaboration | `reuse` |
| Format / length change only ("shorter", "as a table") | `reuse` |
| Time-sensitive on `live` corpus | `re_retrieve` regardless of entity overlap |
| Ambiguous referent (≥ 2 candidates from prior turn) | `clarify` |

---

## Instructions

1. **Resolve referents.** Replace every pronoun and elided phrase using prior turn entities. Show before/after.
2. **Entity diff.** Compute new vs. carried-over entities.
3. **Volatility check.** If `corpus_volatility=live` and current turn touches a time-sensitive attribute (price, status, count), force `re_retrieve`.
4. **Apply table.** Pick the first row that matches.
5. **Cost adjustment.** If `cost_profile=latency_sensitive` and the table says `augment`, downgrade to `reuse` only when ≥ 80% of needed entities/attributes are already covered by prior `retrieved_ids` (else keep `augment`).
6. **Emit.**

---

## Output Format

```json
{
  "decision": "reuse | re_retrieve | augment | clarify",
  "justification": "<one sentence citing the matched table row and inputs>",
  "resolved_query": "<rewritten query with referents replaced, or null if reuse/clarify>",
  "carry_over_ids": ["<id>", "..."],
  "evict_ids": ["<id>", "..."],
  "clarifying_question": "<only if decision == clarify>",
  "topic_shift_score": <float between 0 and 1>
}
```

---

## Verification

- [ ] Exactly one decision emitted.
- [ ] Resolved query has zero pronouns referring to prior turn.
- [ ] Carry-over IDs are a subset of `prior_turn.retrieved_ids`.
- [ ] Eviction happens for any ID older than `max_context_age_turns`.
- [ ] If `live` + time-sensitive attribute, decision is `re_retrieve`.
- [ ] `clarifying_question`, if present, is concrete (names the ambiguity).

---

## Anti-Patterns

1. Re-retrieving every turn — loses cheap reuse, doubles cost.
2. Reusing prior passages when the user shifted entity — answer cites wrong source.
3. Resolving "it" silently and getting it wrong — shows up as confidently wrong answer.
4. Using "could you clarify what you mean?" as the clarifying question — the model must name the specific ambiguity.
