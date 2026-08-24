---
title: "Rate Path & Yield-Curve Analysis — Slope, Term-Premium Decomposition, and Positioning Signal"
category: finance/markets-macro
description: "Analyze the policy-rate path and yield-curve shape (level, slope, curvature) by decomposing yields into expected-rate and term-premium components, reading the signal in inversions and steepenings, and translating it into positioning implications under explicit scenarios."
techniques:
  - NE-11
  - RT-06
  - NE-10
  - QA-02
  - QA-04
difficulty: advanced
tags:
  - yield-curve
  - interest-rates
  - term-premium
  - rate-path
  - duration
updated: "2026-06-08"
related_prompts:
  - domain-finance/markets-macro/finance_central_bank_reaction_function.md
  - domain-finance/markets-macro/finance_economic_scenario_modeler.md
  - domain-finance/risk-management/finance_interest_rate_risk_analysis.md
  - domain-finance/field_guide.md
---

**Informational only — not investment advice. All yield, rate, and forward inputs are user-supplied; outputs require review by qualified professionals.**

## Objective

Analyze the current yield curve and expected policy-rate path by (1) decomposing the curve into level, slope, and curvature, (2) separating yields into expected-average-short-rate and term-premium components, (3) reading the macro signal in the curve's shape, and (4) translating the analysis into duration/positioning implications across explicit rate scenarios — with every figure traced to a user-supplied input.

## When to Use

- Reading what the curve implies for growth, inflation, and policy expectations
- Deciding duration, curve (steepener/flattener), and roll-down positioning
- Interpreting an inversion or a sharp steepening/bear-flattening
- Building the rates layer of a macro scenario or treasury hedging decision
- Reconciling the market-implied path with a house view of the central bank

## Inputs / Context Required

```
<rate_inputs>
Market / currency: (e.g., US Treasuries, USD) and as-of date
Curve points (user-supplied yields, stated source/date):
  - Policy rate (current target)
  - 3M, 2Y, 5Y, 10Y, 30Y yields (or available tenors)
  - 2s10s and 3m10y spreads (or compute from above)
Market-implied path (if available): forward / OIS-implied policy rate at future dates
Real-yield / breakeven data (if available): e.g., 10Y TIPS yield, 10Y breakeven
House view (optional): user's expected policy path vs. market-implied
Source & date for every input.
SPECIFIC QUESTION (optional): __________
</rate_inputs>
```

If yields or forwards are not supplied, request them. Do not assert current yields or forward-implied rates from memory.

## Constraints

### Must
- Use only user-supplied yields/forwards; restate each with source and date.
- Decompose the curve into level, slope, and curvature with explicit formulas.
- Separate nominal yield into real yield + breakeven inflation where data permits (Fisher relation).
- State the term-premium framing: long yield ≈ average expected future short rate + term premium; note the term premium is an estimate, not observable, and cite the basis if a model value is supplied.
- Compare market-implied path vs. house view (if supplied) and quantify the gap.
- Run the analysis across explicit rate scenarios (NE-10), not a single path.
- Stress-test the positioning conclusion (QA-02) and state confidence (QA-04).
- Apply a guardrail against the "inversion = imminent recession" over-read.

### Must Not
- Assert current yields, spreads, or forward-implied rates from memory.
- Treat the term premium as directly observed; it is model-dependent.
- Read a single curve signal (e.g., inversion) as deterministic of recession timing.
- Present one duration call without scenario contingency.
- Confuse a decline in long yields driven by lower term premium with one driven by lower expected growth — distinguish the channel.

## Instructions

**Step 1 — Restate the curve.** Tabulate user-supplied yields with source/date; flag missing tenors.

**Step 2 — Decompose level / slope / curvature.**

```
Level      ≈ average of yields across tenors (or a chosen anchor, e.g., 5Y)
Slope      = Long yield − Short yield
             2s10s  = 10Y − 2Y
             3m10y  = 10Y − 3M    (negative = inverted)
Curvature  = 2 × Mid yield − Short yield − Long yield   (butterfly, e.g., 2×5Y − 2Y − 10Y)
```

**Step 3 — Real vs. nominal (Fisher) where data permits.**

```
Nominal yield(T) ≈ Real yield(T) + Breakeven inflation(T)
  10Y real yield   = 10Y nominal − 10Y breakeven   (or use TIPS yield directly)
Interpret: rising nominal driven by real yield (growth/term-premium) vs. breakeven (inflation expectations)
```

**Step 4 — Expected-path vs. term-premium framing.**

```
Long yield(T) ≈ (1/T) × Σ expected future short rates over [0,T]  +  Term premium(T)
- If market-implied forwards are supplied, the expected-path component is derived from them.
- Term premium = Long yield − model/estimated expected-average-short-rate.
  State the source of any term-premium estimate (e.g., ACM, KW model) — do not invent a value.
```

**Step 5 — Market vs. house path.** If the user supplied a house view, tabulate implied policy rate by date (market) vs. house, and compute the gap in bps and the number of implied hikes/cuts difference.

**Step 6 — Read the macro signal.** Map shape to interpretation, with caveats:

```
Bull steepening   (front-end falls fastest)  → easing expectations / growth concern
Bear steepening   (long-end rises fastest)   → growth/inflation/term-premium up, fiscal supply
Bull flattening   (long-end falls fastest)   → duration demand / growth-down / safe-haven
Bear flattening   (front-end rises fastest)  → hiking cycle / tightening
Inversion (3m10y/2s10s < 0)                  → historically a recession lead indicator, BUT
                                               variable/long lead, false positives exist, term-premium
                                               distortions can muddy the signal — do not date a recession
```

**Step 7 — Positioning implications across scenarios (NE-10).** For base / higher-for-longer / cutting cases: duration stance, curve trade (steepener/flattener), and roll-down/carry note.

```
Approx. price impact of a yield move:  ΔPrice% ≈ −Duration × Δy + ½ × Convexity × (Δy)^2
Carry + roll (simplified):             ≈ Yield + (roll-down: yield differential to shorter tenor over horizon)
State duration and convexity inputs; do not assume them.
```

**Step 8 — Stress-test & bias check.** Attack the positioning call: what rate move breaks it? Apply the inversion-over-read and recency-bias guardrails; state confidence.

## Output Format

### Curve Snapshot (user-supplied)

| Tenor | Yield | Prior | Source / date |
|---|---|---|---|
| 3M | | | |
| 2Y | | | |
| 5Y | | | |
| 10Y | | | |
| 30Y | | | |

### Decomposition

| Measure | Formula | Inputs | Result |
|---|---|---|---|
| Level | | | |
| 2s10s slope | | | |
| 3m10y slope | | | |
| Curvature (butterfly) | | | |
| 10Y real / breakeven | | | |

### Path: Market-Implied vs. House View

| Date | Market-implied policy rate | House view | Gap (bps) |
|---|---|---|---|

### Term-Premium Framing
[Step 4 — expected-path vs. term-premium split; source of any TP estimate]

### Macro Signal Read
[Step 6 — shape interpretation with caveats]

### Positioning Across Scenarios

| Scenario | Duration stance | Curve trade | Carry/roll note | Key risk |
|---|---|---|---|---|
| Base | | | | |
| Higher-for-longer | | | | |
| Cutting cycle | | | | |

### Stress-Test & Confidence
[Step 8 — break point of the call, confidence level, bias notes]

## Verification

- [ ] All yields and forwards are user-supplied with source/date; none from memory.
- [ ] Slope, level, and curvature shown with explicit formulas.
- [ ] Real/nominal split applied where breakeven data is available.
- [ ] Term premium framed as an estimate with a stated source; not treated as observed.
- [ ] Market-implied vs. house path gap quantified (if house view supplied).
- [ ] Positioning given across ≥3 scenarios, not a single call.
- [ ] Price-impact formula shows duration/convexity inputs explicitly.
- [ ] Inversion-over-read and recency-bias guardrails applied; confidence stated.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Reading inversion as a dated recession call | State the lead is variable/long with false positives and term-premium distortions; do not assign a recession date |
| Treating the term premium as observed | Frame as a model estimate; cite the source of any value; never invent one |
| One-path duration call | Require positioning across ≥3 rate scenarios with a stated break point |
| Asserting current yields/forwards from memory | All are user inputs with source/date; stop if missing |
| Confusing real-yield vs. inflation-driven yield moves | Decompose nominal into real + breakeven; attribute the move to a channel |
| Ignoring convexity on large moves | Price-impact formula includes the convexity term for large Δy |
