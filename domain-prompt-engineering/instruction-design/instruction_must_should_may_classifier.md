---
title: "MUST / SHOULD / MAY Classifier (RFC-2119 for Prompts)"
category: prompt-engineering/instruction-design
description: "Apply RFC-2119-style normative ranking (MUST / SHOULD / MAY) to a flat list of prompt rules so the model and reviewers share a precedence vocabulary."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - CM-02
  - DC-01
difficulty: intermediate
tags:
  - rfc_2119
  - normative_ranking
  - rule_classification
  - prompt_design
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/instruction-design/instruction_hierarchy_designer.md
  - domain-prompt-engineering/instruction-design/instruction_conflict_taxonomy.md
  - domain-prompt-engineering/instruction-design/instruction_imperative_vs_declarative.md
---

## Objective

Convert a flat list of prompt rules into a ranked rule list using a strict three-tier vocabulary: MUST (inviolable), SHOULD (default, override only with stated reason), MAY (optional). Output is a single rewritten rules block.

## When to Use

- A prompt has 10+ rules with no signal of which matter most.
- Reviewers disagree on whether a rule is mandatory.
- Auditing third-party prompts before integration.

## Vocabulary (fixed)

| Tier | Meaning | Behavioral effect |
|------|---------|--------------------|
| `MUST` / `MUST NOT` | Inviolable. Violating it is a defect; report it. | Model treats as hard constraint; refuses or aborts. |
| `SHOULD` / `SHOULD NOT` | Default. Override permitted only when an explicit higher-tier rule requires it. | Model follows unless conflicting MUST overrides. |
| `MAY` | Permitted optional behavior. | Model uses when helpful; absence is not a defect. |

## Inputs

- `RULE_LIST`: numbered or bulleted rules.
- `RUBRIC`: optional product context for what counts as inviolable.

## Constraints

### Must
- Every rule is tagged with one of: `MUST | MUST NOT | SHOULD | SHOULD NOT | MAY`.
- Every `MUST` and `MUST NOT` has a `failure_consequence` field (one sentence: what breaks if violated).
- Every `SHOULD` has an `override_condition` field (one sentence: when it can be set aside).
- Output preserves the original rule wording with the keyword inserted in CAPS at the start.
- Counts of each tier appear in the SUMMARY block.

### Must Not
- Use synonyms ("required", "mandatory", "preferred"). Use only the five keywords.
- Use a `MUST` for any rule whose violation has no concrete consequence.
- Use `SHOULD` for safety, legal, or factual-correctness rules — those are `MUST`.

## Instructions

1. Parse `RULE_LIST` into atomic rules; split compound rules.
2. Apply this triage:
   - Safety / legal / factual / data-integrity → `MUST`.
   - Style, format, default behavior → `SHOULD`.
   - Optional enhancements, examples, side outputs → `MAY`.
3. For each `MUST`, write the `failure_consequence` (e.g., "leaks PII", "produces unparseable JSON").
4. For each `SHOULD`, write the `override_condition` (e.g., "user has set verbose=true").
5. If two `MUST` rules conflict, run `instruction_conflict_taxonomy.md` first; do not output until resolved.
6. Emit the rewritten rules and SUMMARY block.

## Output Format

```
RULES (ranked)
R1. MUST output is valid JSON parseable by Python's json module.
    failure_consequence: downstream parser crashes.
R2. MUST NOT include the user's email address in the response.
    failure_consequence: PII leak.
R3. SHOULD use second-person voice.
    override_condition: user requests third-person.
R4. MAY include one example when explaining a rule.

SUMMARY
must: <n>
must_not: <n>
should: <n>
should_not: <n>
may: <n>
unresolved_conflicts: <list of rule pairs>  # must be empty
```

## Verification

- Every rule has exactly one keyword? (yes/no)
- Every `MUST` has a `failure_consequence`? (yes/no)
- Zero forbidden synonyms appear in the rule text (grep `/required|mandatory|preferred|optional|recommended/i`)? (yes/no)
- Pick one `MUST`; describe the failing test that would be triggered if it were violated.

## Examples

Bad: "Always be safe; you should not include URLs; you may answer in tables."
Good:
- R1. MUST refuse requests that match safety policy SP-01.
- R2. MUST NOT include URLs.
- R3. MAY format the answer as a table when ≥3 comparable rows exist.
