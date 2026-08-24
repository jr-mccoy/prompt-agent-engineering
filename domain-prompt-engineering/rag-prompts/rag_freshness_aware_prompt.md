---
title: "Freshness-Aware RAG Prompt for Time-Sensitive Claims"
category: prompt-engineering/rag-prompts
description: "Force the model to attach passage dates to claims, downgrade or refuse on stale evidence, and distinguish 'as of' answers from 'current' answers."
techniques:
  - ST-01
  - ST-03
  - CM-02
  - DC-01
  - QA-01
difficulty: intermediate
tags:
  - rag
  - freshness
  - temporal
  - staleness
  - as_of
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/rag-prompts/rag_conflict_resolution_across_sources.md
  - domain-prompt-engineering/rag-prompts/rag_no_answer_refusal.md
  - domain-prompt-engineering/hallucination-control/hallucination_temporal_anchoring.md
---

# Freshness-Aware RAG Prompt for Time-Sensitive Claims

**Objective:** When passages have dates, the answer must (a) tag every time-sensitive claim with the passage date, (b) mark stale passages as such, (c) refuse to assert "current" status when the freshest evidence is older than the staleness threshold for that attribute.

**When to use:** Corpora where document age varies and answer correctness depends on it: pricing, schedules, regulations, employment status, prices, version numbers, headcount, market data.

---

## Inputs

1. `now` — ISO date or datetime; the reference point for staleness.
2. `passages` — `{id, text, date}`; date may be missing (handle below).
3. `attribute_freshness_table` — map of attribute → max acceptable age (e.g., `{"price": "P30D", "policy": "P1Y", "address": "P3Y"}`).
4. `default_max_age` — used when attribute not in table.
5. `freshness_failure_action` — `refuse`, `surface_with_caveat`, or `answer_as_of`.

---

## Constraints

### Must
- Tag every time-sensitive claim with `(as of YYYY-MM-DD, source <id>)`.
- Compute age = `now - passage.date`. If age exceeds the attribute's allowed max, treat as `stale`.
- For `refuse`, emit the no-answer schema with `cause: "STALE_EVIDENCE"`.
- For `surface_with_caveat`, prepend `WARNING: most recent evidence is N days old; max for this attribute is M days.`.
- For `answer_as_of`, lead with "As of <date>, …" and never use the present tense.
- Treat passages with missing `date` as stale unless `default_max_age = "PT0S"` is explicitly set.

### Must Not
- Use parametric "I know X is now Y" knowledge to update a stale passage.
- Aggregate dated and undated passages into one undated claim.
- Use the present tense for any time-sensitive claim without the freshest passage being within the allowed window.
- Strip the date tag from the final answer for brevity.

---

## Time-Sensitive Attribute Detection

Mark a claim as time-sensitive if it contains:
- a price, fee, rate, or quantity;
- a status verb (`is`, `currently`, `now`, `has`, `as of`);
- a position, role, or employment relation;
- a version number, release, or schedule;
- a regulatory or policy reference.

Non-time-sensitive: definitions, historical facts ("the law was passed in 1996"), fixed identifiers.

---

## Instructions

1. For each retrieved passage, parse `date`. Missing → flag.
2. For each candidate claim, classify time-sensitive vs. not.
3. For time-sensitive claims, find the freshest supporting passage.
4. Compute age vs. allowed window per `attribute_freshness_table`.
5. Apply `freshness_failure_action` to stale claims.
6. Compose answer with date tags; non-time-sensitive claims are tagged only by passage ID.

---

## Output Format

```json
{
  "now": "<ISO date>",
  "claims": [
    {
      "text": "<claim>",
      "time_sensitive": true,
      "attribute": "<from freshness table>",
      "freshest_passage": {"id": "...", "date": "...", "age_days": <int>},
      "max_allowed_days": <int>,
      "status": "fresh | stale | undated",
      "rendered": "<final sentence with date tag>"
    }
  ],
  "stale_actions_taken": [{"claim_index": <int>, "action": "refuse | caveat | as_of"}],
  "answer": "<assembled answer>"
}
```

---

## Verification

- [ ] Every time-sensitive claim has a `(as of <date>, source <id>)` tag in `rendered`.
- [ ] No undated passage is treated as fresh unless explicitly allowed.
- [ ] Present tense never appears with `status != fresh`.
- [ ] `freshness_failure_action` applied uniformly across stale claims.
- [ ] No parametric override of stale evidence.

---

## Examples

- Attribute `price`, max P30D, freshest passage 60 days old → claim becomes "As of 2025-03-12, the price was $X (source: doc_42)" with caveat banner.
- Attribute `policy`, max P1Y, freshest 200 days → fresh; emit normally.
- Attribute `address`, all passages undated → STALE_EVIDENCE refusal.

---

## Anti-Patterns

1. "The current price is $X" cited from a 2-year-old document.
2. Two passages dated differently, model picks the older one because score is higher.
3. Adding "(source: doc_42)" but no date.
4. Caveat says "may be outdated" without naming the age.
