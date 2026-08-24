---
title: "Invented-Entity Audit — Find Made-Up Names, IDs, and References"
category: prompt-engineering/hallucination-control
description: "Scan a model output for entities, identifiers, and references that do not exist in supplied evidence and tag each as invented, paraphrased, or grounded."
techniques:
  - ST-01
  - ST-03
  - CM-02
  - QA-01
  - PR-02
difficulty: advanced
tags:
  - hallucination
  - audit
  - entity_resolution
  - fabrication
  - post_hoc
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/hallucination-control/hallucination_citation_required_pattern.md
  - domain-prompt-engineering/hallucination-control/hallucination_known_unknown_separator.md
  - domain-prompt-engineering/rag-prompts/rag_evaluation_harness_for_groundedness.md
---

# Invented-Entity Audit

**Objective:** Given a generated response and the evidence corpus that should have grounded it, return a per-entity verdict: `grounded`, `paraphrased_match`, `invented`, or `unverifiable`. Use deterministic matching first, model judgment only as a fallback.

**When to use:** Post-hoc audit on RAG outputs; pre-publication audit on long-form generations; routine eval of any path that produces names, IDs, citations, URLs, dates, or quantities.

---

## Inputs

1. `response` — the model output to audit.
2. `evidence` — the corpus that the response should have been grounded in (passages, documents, or structured records).
3. `entity_classes` — subset of `[person, organization, place, product, doc_id, url, doi, isbn, date, monetary_amount, statistic, code_identifier, function_name, file_path, citation]`.
4. `paraphrase_distance_max` — token-level edit distance allowed for `paraphrased_match` (default 3) or semantic threshold for fuzzy matchers.
5. `unverifiable_policy` — `treat_as_invented` or `flag_only`.

---

## Constraints

### Must
- Run deterministic exact-match first; only escalate to fuzzy or LLM judgment when exact fails.
- Classify each extracted entity into one verdict and one only.
- Produce evidence span(s) for `grounded` and `paraphrased_match` verdicts.
- Treat fabricated URLs, DOIs, ISBNs, file paths as `invented` regardless of plausibility.
- Apply `unverifiable_policy` when the entity could be real but is not in evidence.

### Must Not
- Use model judgment to overturn an exact-match result.
- Mark a number as `paraphrased_match` if it differs from evidence (numbers do not paraphrase).
- Ignore entities embedded in code blocks or markdown links.
- Skip entities just because they appear in transitional sentences.
- Average verdicts into a single score; report counts.

---

## Audit Pipeline

1. **Extract.** Run an entity recognizer over `response` for each class in `entity_classes`. Capture span and type.
2. **Exact-match.** For each entity, search `evidence` for a literal occurrence (case-insensitive for names, exact for IDs/URLs/numbers).
3. **Fuzzy-match.** If no exact match, run a class-specific fuzzy match:
   - Names: token-set ratio ≥ 0.9.
   - URLs/IDs: no fuzzy match permitted.
   - Numbers / dates: no fuzzy match permitted.
4. **Verdict.**
   - Exact hit → `grounded`.
   - Fuzzy hit within `paraphrase_distance_max` → `paraphrased_match`.
   - Class permits external lookup AND `unverifiable_policy=flag_only` AND no match → `unverifiable`.
   - Otherwise → `invented`.

---

## Output Format

```json
{
  "entities": [
    {
      "text": "<extracted span>",
      "class": "person | organization | ... | citation",
      "char_start": <int>,
      "char_end": <int>,
      "verdict": "grounded | paraphrased_match | invented | unverifiable",
      "match": {"evidence_id": "...", "match_type": "exact | fuzzy", "evidence_span": "..."} ,
      "notes": "<one phrase if invented or unverifiable>"
    }
  ],
  "counts": {
    "grounded": <int>,
    "paraphrased_match": <int>,
    "invented": <int>,
    "unverifiable": <int>
  },
  "invented_rate": <float>,
  "audit_blocking": <bool>
}
```

`audit_blocking` is true if `invented_rate > 0` for classes `[doc_id, url, doi, isbn, code_identifier, file_path, citation]`.

---

## Verification

- [ ] Every extracted entity has one verdict.
- [ ] No fuzzy match used on numbers, dates, or IDs.
- [ ] Invented URLs / DOIs / ISBNs surface even when domain looks plausible.
- [ ] `invented_rate` excludes the `unverifiable` count.
- [ ] `audit_blocking` triggered for any invented hard-identifier.

---

## Anti-Patterns

1. Letting a model "explain" away an invented citation. The verdict is mechanical.
2. Allowing fuzzy match on monetary amounts ($10M vs $10.5M is not a paraphrase).
3. Ignoring entities inside code blocks — fabricated function names are common.
4. Reporting only invented count without `invented_rate` denominator.
