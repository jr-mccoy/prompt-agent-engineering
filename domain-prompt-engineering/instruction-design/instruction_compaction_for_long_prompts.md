---
title: "Compaction Techniques for Long Prompts"
category: prompt-engineering/instruction-design
description: "Cut a long prompt's length by ~50% while preserving every constraint, using a fixed catalogue of compaction techniques."
techniques:
  - ST-02
  - CM-02
  - QA-01
  - PR-01
  - DC-01
difficulty: advanced
tags:
  - compaction
  - prompt_compression
  - token_cost
  - rewriting
  - long_prompts
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/compression-and-cost/
  - domain-prompt-engineering/instruction-design/instruction_must_should_may_classifier.md
  - domain-prompt-engineering/instruction-design/instruction_negation_audit.md
---

## Objective

Take a long prompt and emit a shorter version that (a) is ≤50% of the original token count, (b) preserves every operational constraint, and (c) names which compaction technique was applied at each cut.

## When to Use

- Prompt exceeds context cost budget or a cache prefix length.
- Prompt has accreted comments, examples, and redundant rules.
- Migrating to a smaller-context model.

## Compaction Technique Catalogue

| ID | Technique | When to apply |
|----|-----------|---------------|
| C1 | Bullet-ize prose | Paragraph of more than 2 sentences stating list-like rules. |
| C2 | Deduplicate restatements | Same rule appears in 2+ places. |
| C3 | Move examples to suffix or external | Example block is illustrative, not load-bearing. |
| C4 | Extract schema | Repeated field descriptions → one JSON Schema or table. |
| C5 | Replace narrative with imperative | "We would like you to consider whether…" → "Decide whether…". |
| C6 | Remove unfalsifiable sentences | Sentences with no observable effect on output. |
| C7 | Collapse synonyms | "Be clear, concise, plain, direct" → "Be concise." |
| C8 | Externalize reference data | Long lists → cite by ID, store list out-of-prompt. |
| C9 | Eliminate negation pairs | If a positive rule subsumes a negation, drop the negation. |
| C10 | Compress preamble | Greeting/role boilerplate → single role line. |

## Inputs

- `PROMPT_TEXT`: original prompt.
- `TARGET_RATIO`: float in (0, 1], default 0.5.
- `TOKENIZER`: which tokenizer to count with (default: `cl100k`).

## Constraints

### Must
- Final token count ≤ `TARGET_RATIO × original_token_count`.
- Every constraint in the original maps to one or more constraints in the compacted version (no loss).
- Each cut is labeled with a technique ID from the catalogue.
- Output includes a `loss_report` block; if non-empty, the compaction is rejected.
- Preserve all rule IDs from the original; do not renumber.

### Must Not
- Apply C3 to examples that are referenced by ID elsewhere in the prompt.
- Apply C6 to sentences containing a measurable directive.
- Introduce new constraints not in the original.

## Instructions

1. Tokenize and record `original_tokens`.
2. Tag each original sentence with the cheapest applicable technique ID (multiple allowed).
3. Apply techniques in order C2, C4, C8, C7, C5, C6, C9, C1, C10, C3.
4. After each pass, count tokens; stop once `TARGET_RATIO` met.
5. Build a `constraint_map`: for each original constraint, list the new line(s) covering it.
6. Build `loss_report`: any original constraint not present in `constraint_map`.

## Output Format

```
COMPACTED_PROMPT
<the rewritten prompt>

CUT_LOG
| span_id | technique | before (chars) | after (chars) | original_snippet                | new_snippet                |
|---------|-----------|----------------|---------------|---------------------------------|----------------------------|
| s001    | C2        | 188            | 0             | "Always cite sources. Always …" | (merged into R4)           |
| s002    | C5        | 142            | 31            | "We would like …"               | "Decide whether…"          |

CONSTRAINT_MAP
| original_id | preserved_in (new ids) |
|-------------|------------------------|
| R1          | R1                     |
| R4          | R4                     |

LOSS_REPORT
<empty | list of dropped constraints — reject compaction if non-empty>

TOKEN_COUNT
original: <n>
new: <n>
ratio: <float>
```

## Verification

- `ratio ≤ TARGET_RATIO`? (yes/no)
- `LOSS_REPORT` is empty? (yes/no)
- Every original rule ID appears in `CONSTRAINT_MAP`? (yes/no)
- Run an A/B eval: 20 inputs, compare outputs. ≥95% behavior parity required, or revert.

## Examples

`C7 collapse synonyms`:
- Before: "Write clearly and concisely; be plain; do not be verbose."
- After: "Be concise."
- Loss: zero (verbosity is the negation of concise; "plain" and "clear" are subsumed).
