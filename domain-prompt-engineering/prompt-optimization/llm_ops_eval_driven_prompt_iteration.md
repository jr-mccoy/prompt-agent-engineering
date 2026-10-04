---
title: "Eval-Driven Prompt Iteration Loop — Fixed Dev Set, Sealed Test Set, One Hypothesis per Round, and a Stop Rule"
category: prompt-engineering/prompt-optimization
description: "Run a multi-round prompt optimisation loop that cannot fool itself: frozen model and scorer configuration, a measured noise band from repeated baseline runs, one written hypothesis per round tested on the whole dev set, acceptance only above the noise band with no protected-case regressions and within the token budget, a round log counting cases fixed and broken, overfitting guards against case-specific rules, a single look at a sealed test set, and a plateau rule that hands off to non-prompt levers."
techniques:
  - MP-02
  - DD-06
  - QA-07
  - QA-11
difficulty: advanced
tags:
  - prompt-optimization
  - eval-driven-development
  - hill-climbing
  - dev-test-split
  - overfitting
  - noise-band
  - prompt-keeps-getting-tweaked
  - is-my-prompt-change-actually-better
  - when-to-stop-tuning
updated: "2026-10-03"
related_prompts:
  - domain-prompt-engineering/evaluation/regression/regression_ab_test_runner_prompt.md
  - domain-prompt-engineering/evaluation/eval-datasets/dataset_holdout_split_designer.md
  - domain-prompt-engineering/prompt-optimization/llm_ops_failure_cluster_prioritizer.md
---

# Eval-Driven Prompt Iteration Loop

**Objective:** Improve a prompt over many rounds of edits while keeping every
accepted change real — above run-to-run noise, not paid for by breaking other cases,
and not tuned to the particular cases you happen to be looking at.

**When to Use:**
- You have an eval set and are about to spend days editing a prompt against it.
- Scores move up and down between edits and you cannot tell which changes helped.
- A prompt has accumulated rules that each fixed one case and nobody knows which matter.
- **Not this prompt if** you are comparing exactly two finished variants for a ship
  decision — use `domain-prompt-engineering/evaluation/regression/regression_ab_test_runner_prompt.md`.
  If you are fixing one failure with the smallest edit, use
  `domain-prompt-engineering/prompt-improvement/improve_minimal_change_pass.md`; cutting
  tokens within a tolerance is
  `domain-prompt-engineering/compression-and-cost/compression_lossy_with_test_set.md`;
  finding which past edit broke something is
  `domain-prompt-engineering/debugging/debug_bisect_prompt_changes.md`. The broad
  checklist of optimisation dimensions is `llm_ops_prompt_optimization.md` in this folder.

## Inputs / Context

1. **Current prompt** and its version.
2. **Eval set split** into a *dev* set you iterate on and a *sealed test* set you do
   not look at during iteration (see `dataset_holdout_split_designer.md`).
3. **Scorer**: deterministic checks where possible; an LLM judge with its prompt version
   and known agreement with humans where not.
4. **Protected cases**: safety, refusal, and must-pass cases that may never regress.
5. **Frozen configuration**: model and version, temperature, max tokens, tools.
6. **Budgets**: token ceiling for the prompt, cost per run, rounds or time available.
7. **Failure clusters** from the latest run, if available
   (`llm_ops_failure_cluster_prioritizer.md`).

## Method

1. **Freeze the configuration.** Model version, decoding settings, judge prompt and
   scorer code are fixed for the loop. A change to any of them starts a new baseline.
2. **Measure the noise band (QA-07).** Run the baseline on the full dev set k times
   (k ≥ 3; more at temperature > 0). The spread across runs is the noise. Set the
   acceptance threshold above it — e.g. 2 × the observed range, never less than 2 cases.
3. **Choose one target per round.** Take the largest addressable failure cluster.
   Write the hypothesis *before* editing: the change, the cases it should fix, the cases
   it might break.
4. **Run on the whole dev set (QA-11).** Never only on the failing cases. Record pass
   rate, cases fixed, cases broken (flips in both directions), protected-case results,
   prompt tokens, and cost.
5. **Accept or revert by rule.** Accept only if: net gain ≥ threshold; zero protected
   regressions; tokens and cost within budget. Otherwise revert — even if it "looks
   better". Log the round either way (MP-02).
6. **Overfitting guards.** Reject on sight: rules naming specific entities or phrasings
   from dev cases; examples copied from dev cases; rules that fix one case each. Count
   rounds — every look at the dev set adds selection pressure. Refresh the dev set with
   new cases when it has been iterated on for many rounds.
7. **Stop rule (DD-06).** Stop when the target is reached on dev, or after N consecutive
   rejected rounds (plateau), or when the budget is spent. A plateau means the remaining
   failures are probably not prompt-shaped: route them to context, tools, model, or
   task decomposition.
8. **One look at the sealed test.** Score the final candidate (and the baseline, if not
   already scored) on the test set once. A dev–test gap larger than the noise band means
   the gains partly overfit the dev set; report it rather than re-tuning on test.
9. **Hand off.** Final version, round log, test result, and new regression cases go to
   the release gate (`regression_release_gate_scorecard.md`).

## Output Format

```
# Iteration log — [prompt] v[x] → v[y]   Model: [..] (frozen)   Judge: [..] v[..]

## Setup
Dev n=[..]  Test n=[..] (sealed)  Protected n=[..]
Baseline dev: runs [..], [..], [..] → noise band [..] → accept threshold +[..] cases
Budgets: prompt ≤ [..] tokens · cost ≤ [..]/run · rounds ≤ [..]

## Rounds
| # | Hypothesis (written first) | Change | Dev pass | Fixed | Broken | Protected | Tokens | Decision |

## Overfitting review
[rules or examples rejected as case-specific] · rounds on this dev set: [..]

## Stop reason: [target | plateau after n | budget]
## Sealed test (one look)
Baseline [..] → final [..]   Dev–test gap [..] vs noise [..] → [OK | partial overfit]
## Hand-off: [non-prompt levers for remaining clusters] · regression cases added: [..]
```

## Verification

- [ ] Model, decoding, and scorer were frozen; any change restarted the baseline.
- [ ] The noise band was measured from repeated baseline runs before any edit.
- [ ] Each hypothesis was written before its run.
- [ ] Every round ran on the full dev set and recorded fixed and broken cases.
- [ ] Accept decisions follow the stated rule, including protected cases and budgets.
- [ ] Case-specific rules and copied examples were rejected.
- [ ] The test set was scored once, at the end, and the dev–test gap is reported.
- [ ] The stop reason is stated and remaining clusters are routed.

## False-Positive Prevention

1. **Noise as progress.** A two-case gain on a set whose baseline wobbles by three cases
   is nothing. Measure the band first.
2. **Net score hiding churn.** +5 can be +12 fixed and −7 broken. Report both flips;
   heavy churn means the change is unstable.
3. **Testing only the failures.** The edit that fixes the failing cases often breaks
   passing ones; always run the whole dev set.
4. **Overfitting by a thousand rules.** Each case-specific rule raises dev and lowers
   generality. The sealed test is where this shows.
5. **Peeking at test.** Iterating against the test set turns it into a second dev set.
   One look, at the end.
6. **Moving the goalposts.** Changing the judge prompt mid-loop changes the score
   without changing the prompt. Freeze it.
7. **Prompting past a plateau.** When several rounds fail, the failures are usually
   missing context, a missing tool, or a capability limit — not wording.

## Example Output

```
# Iteration log — support-ticket triage v3.0 → v3.3   Model: frozen snapshot, T=0   Judge: exact match (category) + rubric v2 (priority)

## Setup
Dev n=160  Test n=80 (sealed)  Protected n=12 (abuse/escalation)
Baseline dev: 115, 114, 116 → band ±1 → accept threshold +3 cases
Budgets: prompt ≤ 2,500 tokens · rounds ≤ 10

## Rounds
| 1 | Billing/Refund confusion (14 fails) fixed by definitions | category definitions | 124 | 11 | 2 | 12/12 | 2,010 | accept |
| 2 | priority escalation examples fix 4 | +2 examples | 126 | 4 | 2 | 12/12 | 2,190 | reject (+2 < 3) |
| 3 | schema before examples fixes format slips | reorder | 123 | 1 | 2 | 12/12 | 2,010 | reject |
| 4 | multi-issue tickets: classify first actionable request | rule | 131 | 9 | 2 | 12/12 | 2,060 | accept |
| 5 | "Stripe" mentions → Billing | rule | 134 | 3 | 0 | 12/12 | 2,075 | reject: case-specific |
| 6 | priority rubric with SLA thresholds | rubric | 136 | 7 | 2 | 12/12 | 2,310 | accept |
| 7 | tone-neutral wording for angry tickets | rewrite | 135 | 2 | 3 | 12/12 | 2,330 | reject |
| 8 | Account vs Access definitions | definitions | 137 | 3 | 2 | 12/12 | 2,350 | reject (+1) |

## Overfitting review
Round 5 rejected (vendor name from 3 dev cases). Rounds on this dev set: 8.

## Stop reason: plateau after 2 rejected rounds (7, 8)
## Sealed test (one look)
Baseline 56/80 (70.0%) → final 65/80 (81.3%)   Dev 136/160 (85.0%)
Dev–test gap 3.7 pts vs noise ≈ 1.3 pts (2-case dev range) → mild overfit; add 20 fresh log cases to dev next cycle
## Hand-off: 9 remaining fails need order-system lookup (tool lever) · 6 regression cases added
```

## Techniques Used

- **MP-02 Recursive Optimization** — versioned rounds, each logged with its hypothesis and decision.
- **DD-06 Iteration Control** — acceptance threshold, budgets, and a plateau stop rule.
- **QA-07 Statistical A/B Testing for Prompts** — repeated baseline runs set the noise band each round must beat.
- **QA-11 Pass/Fail Test Harness** — whole-dev-set runs with protected cases as hard gates.

## Related Prompts

- `domain-prompt-engineering/evaluation/regression/regression_ab_test_runner_prompt.md` — the formal two-variant experiment for the final ship decision.
- `domain-prompt-engineering/evaluation/eval-datasets/dataset_holdout_split_designer.md` — building the dev and sealed test split this loop depends on.
- `domain-prompt-engineering/prompt-optimization/llm_ops_failure_cluster_prioritizer.md` — choosing each round's target from clustered failures.
