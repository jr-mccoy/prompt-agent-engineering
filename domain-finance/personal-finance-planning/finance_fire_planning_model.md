---
title: "FIRE Planning Model — Target Number, Savings Rate, and Withdrawal-Rate Sensitivity"
category: finance/personal-finance-planning
description: "Build a Financial Independence / Retire Early (FIRE) model that derives the target number from spending and a withdrawal rate, projects time-to-FI from the savings rate, and stress-tests the safe-withdrawal-rate assumption for long horizons with sequence-of-returns framing."
techniques:
  - NE-11
  - NE-10
  - QA-02
  - DS-02
  - QA-04
difficulty: intermediate
tags:
  - fire
  - financial-independence
  - savings-rate
  - withdrawal-rate
  - early-retirement
  - sequence-risk
updated: "2026-06-08"
related_prompts:
  - domain-finance/personal-finance-planning/finance_monte_carlo_withdrawal_analysis.md
  - domain-finance/personal-finance-planning/finance_retirement_projection_model.md
  - domain-finance/personal-finance-planning/finance_asset_allocation_glidepath.md
  - domain-finance/field_guide.md
---

**Informational only — not financial, investment, or tax advice. Personal financial decisions depend on individual circumstances; consult a qualified financial planner (CFP), CPA, or attorney as appropriate.**

## Objective

Build an auditable FIRE (Financial Independence / Retire Early) model that: (1) derives the FI target number from annual spending and a withdrawal rate, (2) projects years-to-FI from the savings rate and return assumptions, (3) stress-tests the withdrawal-rate assumption for the long (often 40–50 year) horizons FIRE implies, and (4) reports results as scenario bands with explicit sequence-of-returns framing — never a single deterministic timeline.

## When to Use

- A user pursuing financial independence wants a target number and a time-to-FI estimate.
- Comparing FIRE variants (lean / regular / fat / coast / barista FIRE).
- Stress-testing whether the 4% rule is safe over a 40–50 year horizon.
- Understanding how the savings rate (not income) drives time-to-FI.

## Inputs / Context Required

```
<fire_inputs>
Current annual spending (FI lifestyle):  [$ — the number that defines the target]
Current portfolio / net investable:      [$]
Annual savings (or savings rate %):       [$ or % of take-home]
Take-home income:                         [$]
Current age:                              [years]

FIRE variant:                             [lean | regular | fat | coast | barista]
Expected post-FI income (barista/coast):  [$/yr, if any]

ASSUMPTIONS (user-supplied; state ranges, do not assert):
  Real return (accumulation):             [%, base/optimistic/pessimistic]
  Real return (post-FI):                  [%]
  Withdrawal rate:                        [%, test 3.0 / 3.25 / 3.5 / 4.0]
  Inflation:                              [%]
  Return volatility:                      [%, for sequence-risk note]
  Horizon in retirement:                  [years; FIRE often 40–50]
</fire_inputs>
```

## Constraints

### Must
- Derive the target number from spending and withdrawal rate (NE-11, DS-02).
- Show that time-to-FI is primarily a function of the SAVINGS RATE, not income level.
- Test withdrawal rates at multiple levels (3.0–4.0%) given long FIRE horizons (QA-02, QA-04).
- Present years-to-FI as scenario bands (return + savings rate) (NE-10).
- Explicitly note that the 4% rule was derived for ~30-year horizons; longer horizons argue for lower rates.
- Pair the deterministic time-to-FI with a sequence-of-returns caveat and route to the Monte-Carlo prompt.

### Must Not
- Present a single "you'll reach FI in X years" without bands.
- Assert the 4% rule is safe for 40–50 year horizons.
- Assert historical returns or withdrawal-rate safety as fact.
- Ignore taxes, healthcare (pre-Medicare), and fees in early retirement (note them even if not modeled).

## Instructions

**Step 1 — FI target number (NE-11)**

```
Target = Annual FI spending / Withdrawal rate
   e.g., $40,000 / 0.04 = $1,000,000  (the "25× spending" rule = 4% WR)
   at 3.5%: $40,000 / 0.035 = ~$1,143,000  (≈28.6×)
   at 3.0%: $40,000 / 0.030 = ~$1,333,000  (≈33×)
Show the target at 3.0 / 3.5 / 4.0% so the sensitivity is visible.
```

**Step 2 — Savings rate drives time-to-FI**

```
Years to FI ≈ solve for n in:
   Target = Current portfolio × (1+r)^n + Annual savings × [((1+r)^n − 1)/r]
Illustrate the savings-rate relationship (real return assumed):
   ~10% savings rate → very long (40+ yrs)
   ~25% → ~30s of years
   ~50% → ~15–17 yrs
   ~65%+ → ~10 yrs
(exact years depend on the return assumption — show the formula and the band)
```

**Step 3 — FIRE variant adjustments**

```
Lean FIRE: lower spending → lower target.
Fat FIRE:  higher spending → higher target.
Coast FIRE: portfolio already large enough to grow to target by traditional retirement
  without further contributions — solve: Current × (1+r)^(years to 65) ≥ traditional target.
Barista FIRE: partial income covers part of spending → reduced withdrawal need → lower target.
```

**Step 4 — Withdrawal-rate stress for long horizons (QA-02, QA-04)**

- State that the 4% "safe" rate was studied over ~30-year horizons; FIRE horizons of 40–50 years have higher depletion risk.
- Recommend testing 3.0–3.5% for early retirement and modeling flexibility (variable spending).
- Note early-retirement-specific costs: pre-Medicare healthcare, taxes on withdrawals, and that Social Security is decades away.

**Step 5 — Scenario bands (NE-10)**

| Scenario | Real return | Savings rate | Withdrawal rate | Target | Years to FI |
|---|---|---|---|---|---|
| Optimistic | high | high | 4.0% | | |
| Base | mid | mid | 3.5% | | |
| Pessimistic | low | low | 3.0% | | |

**Step 6 — Sequence-of-returns caveat**

A poor market in the first 5–10 years of a 40+ year retirement is the dominant failure mode; deterministic time-to-FI assumes smooth returns. Route to the Monte-Carlo withdrawal analysis for probability-of-success bands.

**Step 7 — Verification (QA-01)**

Confirm target = spending/WR at each WR; confirm years-to-FI formula reproduces the target when n is plugged back; confirm variant logic.

## Output Format

### FI Target Number
[Step 1 — at 3.0/3.5/4.0% WR]

### Years to FI (Savings-Rate Driven)
[Step 2 — formula + band]

### FIRE Variant Adjustments
[Step 3]

### Withdrawal-Rate Stress (Long Horizon)
[Step 4]

### Scenario Bands
[Step 5 table]

### Sequence-Risk Caveat
[Step 6 — route to Monte-Carlo]

### Verification Notes
[Step 7]

## Verification

- [ ] Target = spending / withdrawal rate, shown at 3.0/3.5/4.0%.
- [ ] Time-to-FI tied to savings rate with the formula shown.
- [ ] FIRE variant (lean/fat/coast/barista) adjustments included if relevant.
- [ ] Long-horizon withdrawal-rate stress (4% not assumed safe for 40–50 yrs).
- [ ] Scenario bands on return and savings rate.
- [ ] Sequence-of-returns caveat with Monte-Carlo routing.
- [ ] Early-retirement costs (healthcare, taxes, no SS yet) noted.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| "25× spending and you're safe" | Show 3.0–3.5% targets; 4% is not validated for 40–50 year horizons |
| Single time-to-FI number | Require scenario bands on return and savings rate |
| Recency bias on returns | Pessimistic band below long-run averages; returns are user inputs |
| Ignoring early-retirement costs | Note pre-Medicare healthcare, taxes, fees, decades until SS |
| Sequence-risk blindness | Mandatory caveat + route to Monte-Carlo probability analysis |
| Income-focused framing | Emphasize savings RATE drives time-to-FI, not income level |
