---
title: "Bisect Prompt Changes (Git-Bisect for Prompts)"
category: prompt-engineering/debugging
description: "Run a git-bisect-style binary search over a sequence of prompt revisions to find the single change that introduced a regression."
techniques:
  - ST-02
  - QA-01
  - PR-01
  - PR-02
  - DC-01
difficulty: intermediate
tags:
  - bisect
  - regression
  - prompt_diff
  - debugging
  - version_control
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/debugging/debug_minimal_repro_isolator.md
  - domain-prompt-engineering/debugging/debug_first_failure_cause_isolator.md
  - domain-prompt-engineering/prompt-improvement/
---

## Objective

Given a known-good prompt revision (`GOOD_REV`) and a known-bad one (`BAD_REV`), run a binary bisection over revisions in between to identify the single revision that introduced the regression.

## When to Use

- A prompt worked yesterday and fails today.
- A team prompt library was edited by multiple people; the breaker is unknown.
- After committing many small prompt edits, output behavior degraded.

## Inputs

- `REVISIONS`: ordered list of prompt versions `[v_0, v_1, …, v_n]` from oldest to newest.
- `GOOD_REV`, `BAD_REV`: indices into REVISIONS with `GOOD_REV < BAD_REV`.
- `INPUT_SET`: list of test inputs (≥10 recommended).
- `PASS_PREDICATE`: machine-checkable boolean over (input, output) pair.
- `N_TRIALS`: trials per revision per input (default 3).
- `PASS_THRESHOLD`: fraction of trials that must pass (default 0.8).

## Constraints

### Must
- Use binary search, not linear scan, over the revision interval.
- Per revision tested, run all `INPUT_SET` × `N_TRIALS` calls; record pass rate per input.
- A revision is `BAD` if any input's pass rate drops below `PASS_THRESHOLD`.
- Stop when the interval has length 1; that revision is the breaker.
- Fixed temperature and model across the entire bisection.
- Log every tested revision with its pass-rate vector.

### Must Not
- Skip revisions because they "look harmless."
- Change `INPUT_SET` mid-bisection.
- Use sampling temperature > 0 unless `N_TRIALS ≥ 10`.

## Instructions

1. Verify `GOOD_REV` passes and `BAD_REV` fails on `INPUT_SET`. If not, abort and re-classify.
2. Set `lo = GOOD_REV`, `hi = BAD_REV`.
3. While `hi - lo > 1`:
   - `mid = (lo + hi) // 2`
   - Run `INPUT_SET × N_TRIALS` against revision `mid`.
   - If revision passes → `lo = mid`; else `hi = mid`.
4. Output revision `hi` as the breaker.
5. Diff `REVISIONS[lo]` vs `REVISIONS[hi]`; isolate the smallest change set.

## Output Format

```
BISECT_RESULT
breaker_revision: v<i>
predecessor: v<i-1>
diff:
<minimal diff between v<i-1> and v<i>>

PASS_RATE_LOG
| revision | pass_rate (per input)                      | overall |
|----------|--------------------------------------------|---------|
| v3       | [1.0, 1.0, 1.0, 0.9, 1.0]                  | 0.98    |
| v5       | [1.0, 0.0, 1.0, 0.3, 1.0]                  | 0.66    |
| v4       | [1.0, 0.0, 1.0, 0.4, 1.0]                  | 0.68    |  # breaker

REGRESSION_INPUTS
- input_id_2: pass_rate dropped 1.0 → 0.0 at v4
- input_id_4: pass_rate dropped 0.9 → 0.4 at v4

NEXT_STEP
Run debug_first_failure_cause_isolator.md on (v4, regression_inputs).
```

## Verification

- `breaker_revision` exists in `REVISIONS`? (yes/no)
- Pass rate at `breaker - 1` ≥ threshold AND at `breaker` < threshold? (yes/no)
- The diff includes only the breaker's change set? (yes/no)
- Re-run the bisection with a new random seed; the breaker should be the same revision (or one adjacent); otherwise raise N_TRIALS.

## Examples

If REVISIONS = [v0..v9], GOOD=v0, BAD=v9, the search visits log2(9) ≈ 4 revisions instead of all 9. The diff between v3 (good) and v4 (bad) is the artifact to debug.
