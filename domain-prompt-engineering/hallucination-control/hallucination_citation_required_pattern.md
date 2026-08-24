---
title: "Citation-Required Pattern — Every Claim Needs a Source Token"
category: prompt-engineering/hallucination-control
description: "Enforce a strict per-claim citation rule with a source-token format, post-hoc validator, and rejection action for unattributed claims."
techniques:
  - ST-01
  - ST-03
  - CM-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - hallucination
  - citations
  - per_claim
  - validator
  - source_token
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/rag-prompts/rag_citation_format_designer.md
  - domain-prompt-engineering/rag-prompts/rag_grounding_contract.md
  - domain-prompt-engineering/hallucination-control/hallucination_grounding_only_pattern.md
---

# Citation-Required Pattern

**Objective:** Define a per-claim citation contract (token format, what counts as a claim, what to do when a claim has no source) and a deterministic validator that rejects responses violating the contract.

**When to use:** Any production path where unattributed factual sentences are bugs. The validator is the enforcement; the prompt alone is not enough.

---

## Inputs

1. `source_id_format` — regex describing valid source tokens (e.g., `\[doc=\d+\]`, `\[\d+\]`, `\(<UUID>\)`).
2. `claim_definition` — `every_sentence`, `every_factual_sentence`, or `every_assertion_with_named_entity_or_number`.
3. `validator_action_on_violation` — `reject_full_response`, `strip_unattributed_sentences`, or `flag_and_pass`.
4. `source_manifest` — list of valid source IDs the model may cite.
5. `min_sources_per_claim` — int, default 1.

---

## Constraints

### Must
- Match `source_id_format` exactly. Validator rejects malformed tokens.
- Every unit identified by `claim_definition` ends with ≥ `min_sources_per_claim` source tokens.
- Each token's ID must appear in `source_manifest`. Invented IDs cause validator failure.
- The validator runs every time; no skip path.
- The model is told both the rule AND the validator's action so it cannot pretend the rule is soft.

### Must Not
- Allow citations that point to a global "References" footer instead of inline.
- Accept summary citations like `(see sources)` — must resolve to specific IDs.
- Permit citation-free transition sentences as a workaround.
- Strip citations before display unless explicitly post-processed; the audit trail must persist server-side.

---

## What Counts as a Claim (by mode)

| Mode | Counts as a claim |
|---|---|
| `every_sentence` | Every period-terminated unit, including transitions. |
| `every_factual_sentence` | Sentences that assert a fact about the world (not commentary, not formatting). |
| `every_assertion_with_named_entity_or_number` | Sentences containing a named entity, date, number, or quoted span. |

The mode is a tradeoff: stricter modes catch more hallucination but produce more refusals on legitimate transitional prose. Pick deliberately.

---

## Validator Specification

```python
def validate(response, source_manifest, source_id_format, claim_def, min_sources):
    claims = extract_claims(response, claim_def)
    violations = []
    for c in claims:
        tokens = re.findall(source_id_format, c)
        if len(tokens) < min_sources:
            violations.append(("missing_citation", c))
            continue
        for t in tokens:
            if extract_id(t) not in source_manifest:
                violations.append(("invented_source", c, t))
    return violations
```

The validator is deterministic; LLM-as-judge is not an acceptable substitute for ID-presence checks.

---

## Instructions for the Model

Insert into system prompt:

```
Every {claim_definition} ends with ≥ {min_sources_per_claim} source tokens
matching pattern: {source_id_format}.

Allowed source IDs are exactly the IDs in the supplied manifest.

A post-response validator will run. Violations cause: {validator_action_on_violation}.

If you cannot cite a claim, do not write the claim. Use the refusal block from
the grounding contract instead.
```

---

## Output Format

The pattern produces:

```json
{
  "system_prompt_block": "<filled rule above>",
  "validator_pseudocode": "<the function above>",
  "claim_extraction_rule": "<exact regex or sentence-splitter spec>",
  "expected_metrics": {
    "violation_rate_target_pct": <float>,
    "false_positive_rate_target_pct": <float>
  }
}
```

---

## Verification

- [ ] `source_id_format` is a concrete regex.
- [ ] `claim_definition` is one of the three named modes.
- [ ] Validator action is one of the three named values.
- [ ] Validator runs on every response (no skip path documented).
- [ ] Pattern requires inline tokens; footers are forbidden.
- [ ] Invented IDs are rejected against `source_manifest`.

---

## Anti-Patterns

1. Citation regex permissive enough that any bracketed text passes. Tighten.
2. Mode `every_sentence` on conversational paths — transitional prose blocks legitimate output.
3. Trusting model to self-validate citations.
4. Logging citations only in the rendered HTML; lost when the format changes.
