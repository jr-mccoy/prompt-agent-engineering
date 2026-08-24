---
title: "Monte-Carlo Withdrawal Analysis — Sequence-of-Returns Risk and Probability-of-Success Bands"
category: finance/personal-finance-planning
description: "Design a Monte-Carlo retirement-withdrawal analysis that models a withdrawal strategy across many simulated return paths, quantifies sequence-of-returns risk, and reports probability-of-success and percentile terminal-balance bands rather than a single deterministic outcome."
techniques:
  - NE-11
  - NE-10
  - QA-02
  - QA-04
  - DS-02
difficulty: advanced
tags:
  - monte-carlo
  - sequence-of-returns
  - withdrawal-rate
  - probability-of-success
  - retirement-spending
  - longevity-risk
updated: "2026-06-08"
related_prompts:
  - domain-finance/personal-finance-planning/finance_retirement_projection_model.md
  - domain-finance/personal-finance-planning/finance_tax_aware_withdrawal_sequencing.md
  - domain-finance/personal-finance-planning/finance_asset_allocation_glidepath.md
  - domain-finance/personal-finance-planning/finance_fire_planning_model.md
  - domain-finance/field_guide.md
---

**Informational only — not financial, investment, or tax advice. Personal financial decisions depend on individual circumstances; consult a qualified financial planner (CFP), CPA, or attorney as appropriate.**

## Objective

Specify and interpret a Monte-Carlo analysis of a retirement-withdrawal strategy: define the return/inflation distribution, the number of trials, the withdrawal rule, and a precise success/failure definition; then report results as a probability of success plus percentile bands (10th / 50th / 90th) of terminal balance and sustainable spending — explicitly surfacing sequence-of-returns risk, which a deterministic average-return projection hides.

## When to Use

- A user near or in retirement wants to know the probability their money lasts, not just an average.
- Comparing withdrawal strategies (fixed-real, fixed-percentage, guardrails, floor-and-ceiling).
- Stress-testing a plan against a market crash early in retirement (the dominant failure mode).
- Pressure-testing a "safe withdrawal rate" claim under a return distribution rather than a single mean.

## Inputs / Context Required

```
<monte_carlo_inputs>
Starting portfolio value:             [$]
Retirement horizon:                   [years; default test 30 AND 40]
Current age / retirement age:         [years]

WITHDRAWAL RULE (choose one; define precisely):
  Fixed real:        [$ in year 1, inflated each year by realized/assumed inflation]
  Fixed percentage:  [% of current balance each year]
  Guardrails:        [initial %, raise/cut % triggers, e.g., ±20% bands]
  Floor-and-ceiling: [floor $, ceiling $]

DISTRIBUTION ASSUMPTIONS (user-supplied; state, do not assert):
  Expected real return (mean):        [%]
  Return volatility (std dev):        [%]
  Inflation mean / std dev:           [% / %]
  Correlation/return model:           [i.i.d. normal | block bootstrap of historical | regime]
  Asset mix / glidepath:              [static or changing equity %]
  Fees (drag on return):              [%/yr]

SIMULATION SETTINGS:
  Number of trials:                   [e.g., 1,000–10,000]
  Success definition:                 [e.g., "% of paths with balance > 0 at horizon end"]
  Other income (SS/pension):          [$/yr; mark "verify"]
  Taxes treatment:                    [pre-tax portfolio | after-tax; state]
</monte_carlo_inputs>
```

## Constraints

### Must
- State the full distribution spec: mean return, volatility, inflation, correlation/return-generation model, number of trials, and fees (NE-11, QA-04).
- Define success/failure explicitly (e.g., % of paths not depleting before the horizon) — never leave "success" implicit.
- Report results as probability of success **and** percentile terminal-balance bands (10th/50th/90th), not a single number (NE-10).
- Explicitly isolate sequence-of-returns risk: show that two paths with identical average returns but different ordering produce very different outcomes (QA-02).
- Note the limitations of the chosen return model (i.i.d. normal understates fat tails and serial correlation) (QA-04).

### Must Not
- Report only an average ending balance or only a probability of success without the percentile bands.
- Assert historical return/volatility figures as authoritative; they are user-supplied assumptions.
- Treat a high success probability as certainty; an 85% success rate means ~1-in-7 paths fail.
- Ignore fees, taxes, or other income the user provided.

## Instructions

**Step 1 — Lock the simulation spec.** Restate every distribution assumption and setting. If volatility or inflation std dev is missing, request it or state a default range and flag it.

**Step 2 — Describe the engine (auditable, even if hand-run).**
```
For each trial (1..N):
  balance_0 = starting portfolio
  for year t in 1..horizon:
     r_t      = draw from return distribution (mean, vol)  − fees
     infl_t   = draw from inflation distribution
     w_t      = withdrawal per the rule (inflate fixed-real by infl_t)
     balance_t = (balance_{t-1} − w_t) × (1 + r_t) + other_income_t
     if balance_t <= 0: mark trial FAILED at year t
Collect: success flag, terminal balance, year-of-depletion (if failed)
```

**Step 3 — Compute headline outputs.**
```
Probability of success = (# trials not depleted) / N
Terminal balance percentiles: P10, P25, P50 (median), P75, P90
Median year-of-depletion among failed paths
Worst decile (P10) terminal balance — the "bad but plausible" case
```

**Step 4 — Sequence-of-returns demonstration (QA-02).**
- Construct two illustrative paths with the SAME arithmetic mean return: one with poor returns in years 1–5 (crash-early), one with strong returns early. Hold withdrawals identical.
- Show that the crash-early path depletes years earlier — this is sequence risk, invisible to average-return math.
- Report the "magic number" intuition: a large drawdown in the first 5 retirement years is the dominant determinant of failure.

**Step 5 — Compare strategies (optional, RT-style).** Run the spec across 2–3 withdrawal rules; tabulate success probability and P10/P50/P90 spending and terminal balances. Guardrail/dynamic rules typically raise success at the cost of spending variability — state the tradeoff.

**Step 6 — Stress overlays.** Add: (a) a −30% to −40% market shock in year 1; (b) +1 standard deviation inflation for a decade; (c) horizon extended to 40 years (longevity). Report success probability under each.

**Step 7 — Verification & uncertainty (QA-01, QA-04).** Sanity-check that a 4% fixed-real withdrawal over 30 years roughly aligns with widely-cited success ranges given the stated assumptions; if it does not, re-examine inputs. State model limitations.

## Output Format

```
## Monte-Carlo Withdrawal Analysis
Spec: [mean return / vol / inflation / model / N trials / fees / success definition]

### Headline Results
Probability of success (30 yr): __%    (40 yr): __%
Terminal balance bands:  P10 $___ | P50 $___ | P90 $___
Median depletion year (failed paths): year __

### Sequence-of-Returns Demonstration
[Crash-early vs. strong-early paths, same mean — depletion year contrast]

### Strategy Comparison (if run)
| Rule | Success % | P10 spend | P50 spend | P10 terminal | P90 terminal |

### Stress Overlays
| Stress | Success % | Notes |
| Year-1 crash −35% | | |
| +1σ inflation 10 yr | | |
| 40-year horizon | | |

### Limitations & Disconfirming Check
[Return-model caveats; what would make the plan unsafe]
```

## Verification

- [ ] Full distribution spec stated (mean, vol, inflation, model, N, fees).
- [ ] Success/failure defined explicitly and quantitatively.
- [ ] Results reported as probability + P10/P50/P90 bands, not a single number.
- [ ] Sequence-of-returns demonstration present (same-mean, different-order paths).
- [ ] Year-1 crash stress overlay included.
- [ ] Longevity (40-year horizon) tested.
- [ ] Model limitations (fat tails, serial correlation) acknowledged.
- [ ] Return/inflation figures labeled user-supplied assumptions, not facts.
- [ ] Disclaimer present near top.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Reporting only the average/median outcome | P10/P50/P90 bands required; the median is not the plan's safety margin |
| Treating 85–90% success as "safe" | State the failure share explicitly (1-in-7 to 1-in-10); pair with depletion-year detail |
| Sequence-risk blindness | Mandatory same-mean different-order demonstration + year-1 crash overlay |
| i.i.d.-normal hides tail risk | State that normal draws understate crashes; recommend bootstrap/fat-tail sensitivity |
| Longevity underestimation | Test both 30- and 40-year horizons; report both success probabilities |
| Precision illusion from "87.3% success" | Round; present as a band of assumptions; restate that it is conditional on inputs |
