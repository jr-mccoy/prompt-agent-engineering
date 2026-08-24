---
title: "Minimal Reproducer Isolator for Prompt Failures"
category: prompt-engineering/debugging
description: "Reduce a failing prompt + input pair to the smallest reproducer that still triggers the failure."
techniques:
  - ST-02
  - QA-01
  - PR-01
  - PR-02
  - DC-01
difficulty: intermediate
tags:
  - minimal_repro
  - bug_isolation
  - delta_debugging
  - prompt_debugging
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/debugging/debug_bisect_prompt_changes.md
  - domain-prompt-engineering/debugging/debug_failure_mode_taxonomy.md
  - domain-prompt-engineering/debugging/debug_first_failure_cause_isolator.md
---

## Objective

Given a failing prompt and a failing input, output the smallest prompt + smallest input that still triggers the failure ≥ K times out of N runs.

## When to Use

- A model is misbehaving on a complex prompt and the cause is unknown.
- Before opening a bug report against a model or before asking for review.
- Prior to running `debug_first_failure_cause_isolator.md`.

## Inputs

- `PROMPT_TEXT`: full failing prompt.
- `INPUT`: failing user input.
- `FAILURE_PREDICATE`: machine-checkable boolean over model output (regex, schema check, or contains-string).
- `MODEL_ID`, `TEMPERATURE`.
- `N`: trials per candidate (default 5).
- `K`: failures-out-of-N required to call it "still failing" (default 3).
- `BUDGET`: max candidate reductions (default 50).

## Constraints

### Must
- Treat the original as the baseline; record baseline failure rate `K0/N`.
- Reduce by deleting prompt sections in order: examples, schema, narrative, rules tagged MAY, optional context, then SHOULD rules.
- Never delete a MUST rule.
- A candidate is accepted only if it still satisfies `FAILURE_PREDICATE` at rate `≥ K/N`.
- Use 1-minimality: the final reproducer has the property that deleting any further single chunk drops the failure rate below `K/N`.

### Must Not
- Reword rules during reduction (delete-only).
- Reduce the user `INPUT` and the `PROMPT_TEXT` in the same pass; reduce prompt fully first, then input.
- Change `TEMPERATURE` or `MODEL_ID` mid-reduction.

## Instructions

1. Tokenize prompt into chunks at natural boundaries (sections, list items, schema blocks).
2. Greedy delete each chunk; re-run N trials; keep deletion if `K/N` met.
3. After greedy pass, run binary-section reduction: bisect remaining; keep failing half.
4. When prompt is 1-minimal, switch to `INPUT`: delete words/sentences with same accept rule.
5. Output the minimal pair, the deleted-set log, and final stats.

## Output Format

```
MINIMAL_REPRO
prompt:
<minimal prompt>

input:
<minimal input>

STATS
baseline_failure_rate: K0/N
final_failure_rate: K_final/N
prompt_tokens: before=<a>, after=<b>
input_tokens: before=<a>, after=<b>
reductions: <count>

DELETION_LOG
| step | what_deleted | failure_rate_after | accepted |
|------|--------------|---------------------|----------|
|  1   | examples block | 5/5               | yes      |
|  2   | schema preamble | 1/5              | no       |
```

## Verification

- Is `final_failure_rate ≥ K/N`? (yes/no)
- 1-minimality check: re-delete each remaining chunk one at a time; each must drop rate below K/N. List confirmations.
- Re-run minimal repro 20 times on a fresh sample; report rate.
- If the failure depends on temperature, set `TEMPERATURE=0` and re-verify; note `temperature_sensitive: true|false`.

## Examples

A long prompt with 12 rules + 4 examples reduces to 3 rules + 0 examples + a 6-word user input, while still failing at 4/5. That minimal repro is the artifact to submit upstream.
