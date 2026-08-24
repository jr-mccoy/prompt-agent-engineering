---
title: "Resolve Conflicts Across Retrieved Sources"
category: prompt-engineering/rag-prompts
description: "Decision rules for the model when retrieved passages disagree — apply authority, recency, specificity, or surface the conflict explicitly rather than silently picking one side."
techniques:
  - ST-01
  - ST-03
  - CM-02
  - DC-01
  - QA-01
difficulty: advanced
tags:
  - rag
  - conflict_resolution
  - authority
  - recency
  - source_priority
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/rag-prompts/rag_grounding_contract.md
  - domain-prompt-engineering/rag-prompts/rag_freshness_aware_prompt.md
  - domain-prompt-engineering/hallucination-control/hallucination_known_unknown_separator.md
---

# Resolve Conflicts Across Retrieved Sources

**Objective:** Specify the model's behavior when ≥ 2 retrieved passages give incompatible answers. Output is either (a) a resolved answer with the resolution rule named, or (b) a structured conflict surface for the user.

**When to use:** Multi-source RAG over heterogeneous corpora (web + KB, multiple vendors, multiple time slices, internal + external policy).

---

## Inputs

1. `question` — verbatim.
2. `passages` — `{id, text, source_type, authority_tier, date}`.
3. `policy` — ranked list of resolution criteria; subset of `[authority, recency, specificity, plurality, manual]`.
4. `surface_threshold` — if disagreement spans > N% of passages on the same fact, surface instead of resolve. Default N=30.
5. `tie_breaker` — `surface` or one of the policy criteria.

---

## Constraints

### Must
- Detect disagreement at the claim level, not the document level. Two passages can agree on most things and conflict on one.
- For every resolved claim, name the criterion used and the losing passage IDs.
- Apply criteria in the exact `policy` order; do not reorder per question.
- If the policy is exhausted with no winner, apply `tie_breaker`.
- When surfacing, present each conflicting position with at least one verbatim quote and its ID.

### Must Not
- Average numerical claims that conflict (e.g., revenue figures); pick or surface.
- Use plurality alone as the resolver in domains where authority is ranked (legal, clinical guidelines).
- Hide conflict by quietly preferring the first-listed passage.
- Assume newer = correct outside policy permission.
- Resolve a conflict by falling back to parametric knowledge.

---

## Resolution Criteria

| Criterion | Definition | Best for |
|---|---|---|
| `authority` | `authority_tier` rank wins | Legal, regulatory, official documentation |
| `recency` | latest `date` wins | Pricing, schedules, current events |
| `specificity` | passage matching more entities/attributes wins | Multi-hop questions |
| `plurality` | most-supported claim wins | Crowd corpora, FAQs |
| `manual` | use a custom rule provided in `policy.rule` | Domain-specific edge cases |

---

## Instructions

1. **Claim extraction.** For each passage, extract atomic claims relevant to `question`.
2. **Cluster.** Group claims that talk about the same entity+attribute pair.
3. **Disagreement check.** Within a cluster, mark claims as agreeing, ambiguous, or conflicting. Numerics within ±2% may be marked agreeing only if `policy` allows (else conflict).
4. **Apply policy.** For each conflict cluster, walk `policy` in order; first criterion that produces a strict winner resolves it.
5. **Surface decision.** If unresolved or > `surface_threshold` of passages disagree, switch to surfacing for that cluster.
6. **Emit.**

---

## Output Format

```json
{
  "claims": [
    {
      "entity_attribute": "<e.g., 'AcmeCo.q3_2025_revenue'>",
      "status": "agreed | resolved | surfaced",
      "winning_value": "<value or null>",
      "winner_ids": ["..."],
      "loser_ids": ["..."],
      "criterion_applied": "authority | recency | specificity | plurality | manual | tie_breaker",
      "surfaced_positions": [
        {"value": "...", "ids": ["..."], "quote": "<verbatim>"}
      ]
    }
  ],
  "answer": "<assembled from agreed + resolved claims, with citations>",
  "conflicts_surfaced": <int>
}
```

---

## Verification

- [ ] Every conflict cluster has a named criterion or is `surfaced`.
- [ ] No numeric averaging across conflicting numerics.
- [ ] Loser IDs listed; not silently dropped.
- [ ] Policy order honored top-to-bottom (verifiable from criterion sequence across clusters).
- [ ] `surface_threshold` triggers surfacing, not resolution.
- [ ] Each surfaced position has a verbatim quote and ID.

---

## Anti-Patterns

1. Synthesizing a "balanced" sentence that combines both numbers ("revenue was around $10–12M") when sources said $10M and $12M.
2. Picking the longer passage as the winner — length is not authority.
3. Treating "doesn't mention X" as agreement with a passage that does mention X.
4. Resolving via parametric knowledge when policy fails — emit `surface` instead.
