---
title: "Known/Unknown Separator — Split Confident Facts From Guesses"
category: prompt-engineering/hallucination-control
description: "Force the model to physically segregate verified claims from inferred or guessed claims into two output blocks, so downstream consumers can act on them differently."
techniques:
  - ST-01
  - ST-03
  - CM-02
  - QA-01
  - DC-01
difficulty: intermediate
tags:
  - hallucination
  - known_unknown
  - segregation
  - output_format
  - structured
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/hallucination-control/hallucination_calibrated_uncertainty_prompt.md
  - domain-prompt-engineering/hallucination-control/hallucination_grounding_only_pattern.md
  - domain-prompt-engineering/hallucination-control/hallucination_invented_entity_audit.md
---

# Known/Unknown Separator

**Objective:** Output is split into two blocks: `known` (claims with named, verifiable evidence) and `inferred_or_guessed` (claims that extend, fill, or extrapolate). The split is physical, not stylistic. A consumer can drop the second block to get a no-guess answer.

**When to use:** Decision-support tasks where the human will accept some inference but must know which is which (clinical reasoning, investment analysis, security triage, root-cause analysis).

---

## Inputs

1. `evidence` — text, passages, or structured facts available.
2. `inference_allowed` — boolean; if false, the second block is empty by contract.
3. `inference_distance_cap` — `1` (one logical step from evidence), `2`, or `unbounded`.
4. `min_evidence_for_known` — int; minimum citations a claim needs to qualify as `known`.

---

## Constraints

### Must
- Place each claim in exactly one block.
- Every `known` claim cites ≥ `min_evidence_for_known` evidence IDs.
- Every `inferred_or_guessed` claim names the evidence it extends and the inference step ("derived from X by ...").
- Sort each block by topic, not by confidence.
- If `inference_allowed=false`, the second block is `[]`; do not migrate inferences into block 1.
- If a claim cannot be classified, refuse it — do not put it in either block.

### Must Not
- Use phrases like "it is known that" inside the inferred block, or "presumably" inside the known block.
- Mix the two blocks under one heading.
- Demote a known claim to inferred to make a stronger argument.
- Include parametric facts in the known block. Parametric → inferred at best.
- Drop the second block to make the answer look stronger.

---

## Block Definitions

### `known`
- Backed by ≥ `min_evidence_for_known` cited evidence IDs.
- No logical extension beyond the cited spans.
- Verbatim quotes optional but allowed.

### `inferred_or_guessed`
- Allowed only if `inference_allowed=true`.
- Each item names: source evidence IDs, inference type (`deduction`, `induction`, `analogy`, `default_assumption`), and inference distance (1–N).
- Items beyond `inference_distance_cap` are dropped, not buried.

---

## Instructions

1. Extract atomic claims from the planned response.
2. For each claim, attempt to find direct evidence support meeting `min_evidence_for_known`. If found, classify `known`.
3. If not, check whether it derives from evidence within `inference_distance_cap`. If yes, classify `inferred_or_guessed`.
4. If neither, refuse the claim entirely.
5. Build both blocks; sort within each by topic.
6. Emit.

---

## Output Format

```markdown
## Known
- [<claim>] (sources: <id>, <id>)
- [<claim>] (sources: <id>)

## Inferred or guessed
- [<claim>] (from: <id>; inference: deduction; distance: 1)
- [<claim>] (from: <id>, <id>; inference: analogy; distance: 2)

## Refused
- [<claim>] (reason: no evidence and inference exceeds cap)
```

Plus a JSON sidecar:

```json
{
  "known_count": <int>,
  "inferred_count": <int>,
  "refused_count": <int>,
  "min_evidence_for_known": <int>,
  "inference_distance_cap": <int>,
  "inference_allowed": <bool>
}
```

---

## Verification

- [ ] Exactly two visible blocks (plus optional `Refused`).
- [ ] No claim appears in both blocks.
- [ ] Every `known` claim has ≥ `min_evidence_for_known` citations.
- [ ] Every `inferred_or_guessed` item names source IDs, inference type, and distance.
- [ ] If `inference_allowed=false`, second block is empty.
- [ ] Counts in JSON match the markdown.

---

## Anti-Patterns

1. Single narrative paragraph with hedge words — loses the physical split.
2. Blending high-confidence inference into the known block.
3. Listing every parametric fact under inferred without citing the trigger evidence.
4. Migrating refused claims into inferred to fill the block.
