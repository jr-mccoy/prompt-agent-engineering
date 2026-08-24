---
title: "Input Perturbation Battery"
category: prompt-engineering/debugging
description: "Apply a fixed battery of small input perturbations (case, whitespace, length, delimiters) to surface brittleness."
techniques:
  - ST-02
  - QA-01
  - PR-01
  - PR-02
  - DC-01
difficulty: intermediate
tags:
  - input_perturbation
  - robustness
  - brittleness
  - test_battery
  - debugging
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/debugging/debug_temperature_sensitivity_probe.md
  - domain-prompt-engineering/debugging/debug_silent_failure_detector.md
  - domain-prompt-engineering/debugging/debug_failure_mode_taxonomy.md
---

## Objective

Apply a fixed catalogue of small input perturbations to a passing prompt and report which perturbations break it, ranked by sensitivity.

## When to Use

- Suspect the prompt only works on idealized inputs.
- Validating robustness before shipping.
- Diagnosing complaints from users whose inputs differ stylistically from internal test cases.

## Perturbation Catalogue (fixed)

| ID | Perturbation | Example transform |
|----|--------------|-------------------|
| P1 | Lowercase all | `"What is X?"` → `"what is x?"` |
| P2 | Uppercase all | → `"WHAT IS X?"` |
| P3 | Strip punctuation | → `"what is x"` |
| P4 | Add trailing whitespace and newlines | → `"what is X?\n\n   "` |
| P5 | Collapse all internal whitespace | multiple spaces → one |
| P6 | Pad with leading instruction-like phrase | `"Note: "` prefix |
| P7 | Append benign trailing text | `"Thanks!"` |
| P8 | Halve input length | drop second half |
| P9 | Double input length | repeat input verbatim |
| P10 | Swap quote style (smart ↔ straight) | `"X"` ↔ `“X”` |
| P11 | Insert a single typo (1 char) | random one-character edit |
| P12 | Translate to lowercase ASCII (strip diacritics) | `"café"` → `"cafe"` |
| P13 | Wrap in code fence | ```` ```input``` ```` |
| P14 | Add a numbered list prefix | `"1. "` |
| P15 | Replace newlines with literal `\n` | escape-style |

## Inputs

- `PROMPT_TEXT`, `BASE_INPUT` (a known-passing input), `PASS_PREDICATE`.
- `MODEL_ID`, `TEMPERATURE` (recommended 0.0).
- `N`: trials per perturbation (default 5).

## Constraints

### Must
- Apply every perturbation in the catalogue.
- Run baseline `BASE_INPUT` first; if it does not pass at ≥ 4/5, abort and re-baseline.
- For each perturbation, record `pass_rate`, `delta_vs_baseline`, sample failing output (truncated to 200 chars).
- Mark a perturbation `BRITTLE` if `delta ≥ 0.3` (drop in pass rate).
- Emit `BRITTLENESS_INDEX = count(BRITTLE) / 15`.

### Must Not
- Apply two perturbations in a single test (one variable at a time).
- Skip perturbations that "obviously won't matter".
- Modify the prompt during the run.

## Instructions

1. Run baseline `BASE_INPUT × N`; record pass rate.
2. For each `P1..P15`, generate the perturbed input, run `× N`, record outcome.
3. Compute deltas; flag BRITTLE rows.
4. Sort output by delta descending.
5. Emit recommendations per BRITTLE row.

## Output Format

```
BASELINE
input: "<original>"
pass_rate: K/N

| id | perturbation              | perturbed_input (truncated)   | pass_rate | delta | brittle | sample_failure                |
|----|---------------------------|-------------------------------|-----------|-------|---------|-------------------------------|
| P9 | double length             | "...repeat..."                 | 0/5       | 1.00  | yes     | "..."                         |
| P6 | leading 'Note: '          | "Note: ..."                   | 1/5       | 0.80  | yes     | "..."                         |
| P1 | lowercase                 | "..."                         | 4/5       | 0.20  | no      | (none)                         |

BRITTLENESS_INDEX: 0.40   # 6/15
TOP_BRITTLE: [P9, P6, P11]

RECOMMENDATIONS
- P9 (length doubling): add input length cap with truncation rule in prompt.
- P6 (leading 'Note:'): add anti-prefix-injection rule to instruction layer.
- P11 (typo): add a normalization preprocessing step or fuzzy match.
```

## Verification

- All 15 perturbations exercised? (yes/no)
- Baseline pass rate ≥ 4/5? (yes/no)
- For top-1 BRITTLE perturbation, re-run with N=20 to confirm.
- After applying recommendation, re-run; brittle row should fall below 0.3 delta.

## Examples

Many "case sensitivity" bugs surface as P1 BRITTLE; many context-injection bugs surface as P6 or P14 BRITTLE.
