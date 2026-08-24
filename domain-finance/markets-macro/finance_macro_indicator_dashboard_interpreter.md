---
title: "Macro Indicator Dashboard Interpreter — From Growth / Inflation / Labor / Credit Prints to a Coherent Read"
category: finance/markets-macro
description: "Interpret a user-supplied macro dashboard (growth, inflation, labor, credit, financial conditions) into a coherent read: where we are in the cycle, what is confirming vs. diverging, what is leading vs. lagging, and what would change the read — without asserting any data from memory."
techniques:
  - DS-04
  - RT-06
  - NE-11
  - QA-04
  - DS-02
difficulty: intermediate
tags:
  - macro
  - indicators
  - dashboard
  - business-cycle
  - leading-indicators
updated: "2026-06-08"
related_prompts:
  - domain-finance/markets-macro/finance_economic_scenario_modeler.md
  - domain-finance/markets-macro/finance_rate_path_yield_curve_analysis.md
  - domain-finance/markets-macro/finance_sector_rotation_framework.md
  - domain-finance/field_guide.md
---

**Informational only — not investment advice. Interpretation depends entirely on user-supplied data and is point-in-time.**

## Objective

Turn a set of user-supplied macroeconomic indicators into a structured, defensible read: classify each indicator (improving/deteriorating, leading/coincident/lagging, signal strength), reconcile confirming vs. diverging signals, place the economy in a cycle phase with explicit caveats, and state what fresh data would flip the read. No indicator values are asserted from memory — they are all supplied by the user.

## When to Use

- Monthly/quarterly macro review where you have the prints and need a synthesis
- Reconciling a "soft data says X, hard data says Y" tension
- Briefing a committee on the current macro backdrop with evidence, not narrative
- Upstream input to scenario modeling, rate-path analysis, or sector rotation
- Sanity-checking a market narrative against the actual indicator set

## Inputs / Context Required

```
<dashboard>
Region / economy:
Currency & base date:

USER-SUPPLIED INDICATOR PRINTS (provide value, prior, trend, source, date — do not expect the model to know them):

GROWTH:
- Real GDP (latest, prior):
- PMI manufacturing / services:
- Industrial production:
- Retail sales:
- Leading economic index (if available):

INFLATION:
- Headline CPI / PCE (YoY, MoM):
- Core CPI / PCE:
- Wage growth (e.g., avg hourly earnings, ECI):
- Inflation expectations (breakevens, surveys):

LABOR:
- Unemployment rate:
- Nonfarm payrolls / employment change:
- Job openings / quits (if available):
- Initial jobless claims (trend):

CREDIT & FINANCIAL CONDITIONS:
- IG / HY credit spreads:
- Bank lending standards (e.g., SLOOS):
- Yield curve slope (2s10s, 3m10y):
- Financial conditions index (if available):

Source & date for each block:
SPECIFIC QUESTION (optional): __________
</dashboard>
```

If indicators are missing, request them. Do not fabricate prints.

## Constraints

### Must
- Use only user-supplied values; restate each with its source and date.
- Classify each indicator on three axes: direction (improving/deteriorating/flat), timing (leading/coincident/lagging), and signal strength (strong/moderate/weak).
- Explicitly reconcile divergences (DS-04 / RT-06): when indicators disagree, name the disagreement and weigh leading over lagging where appropriate.
- Show any computed metric as formula → inputs → result (NE-11) — e.g., real wage growth, diffusion, curve slope.
- Give a cycle-phase read with a confidence level (QA-04) and the key uncertainty.
- State the "what would change my mind" data triggers (DS-02 thresholds).
- Apply a confirmation-bias guardrail: actively seek the strongest indicator that contradicts the headline read.

### Must Not
- Assert any indicator value, level, or recent print from memory.
- Resolve a divergence by ignoring the inconvenient indicator.
- Over-weight the most recent single print (recency bias) without trend context.
- Present a cycle call as certainty; macro phase boundaries are fuzzy.
- Confuse correlation with causation when linking indicators.

## Instructions

**Step 1 — Restate the dashboard.** Build the indicator table from user inputs with source/date. Flag stale or missing items.

**Step 2 — Classify each indicator.** Direction × timing × strength. Note the standard timing role:

```
Leading (turn before the cycle):   yield-curve slope, building permits, new orders/PMI new-orders,
                                    initial claims, equity/credit-spread moves, money/credit growth
Coincident (turn with the cycle):  industrial production, employment level, real income, retail sales
Lagging (turn after the cycle):    unemployment rate, core inflation, unit labor costs, avg duration of unemployment
```

**Step 3 — Compute supporting metrics where useful.**

```
Real wage growth      = Nominal wage growth − Headline inflation
Real policy rate      = Policy rate − inflation (state which inflation measure)
Curve slope           = Long yield − Short yield   (negative = inverted)
Diffusion / breadth   = % of components improving   (if component data supplied)
```

**Step 4 — Reconcile signals (the core step).** Group indicators by what they imply (expansion / late-cycle / slowdown / contraction / recovery). Where blocks disagree, state the divergence explicitly and explain how you weight it (e.g., "leading indicators soft, lagging strong → late-cycle, not mid-cycle").

**Step 5 — Place the cycle phase.** Choose: early expansion / mid expansion / late expansion / slowdown / contraction / early recovery. Give confidence and the single biggest uncertainty.

**Step 6 — Define change-the-read triggers.** Specific thresholds on named indicators that would move the phase call up or down.

**Step 7 — Bias guardrail.** Name the indicator that most contradicts your read and explain why you are not over-weighting the latest print.

## Output Format

### Indicator Dashboard (user-supplied)

| Indicator | Value | Prior | Direction | Timing | Strength | Source / date |
|---|---|---|---|---|---|---|
| (Growth block) | | | | | | |
| (Inflation block) | | | | | | |
| (Labor block) | | | | | | |
| (Credit / conditions) | | | | | | |

### Computed Metrics
[Step 3 — formula → inputs → result for each]

### Signal Reconciliation

| Implication group | Indicators pointing here | Weight in read | Notes |
|---|---|---|---|
| Expansion / strength | | | |
| Late-cycle / overheating | | | |
| Slowdown / contraction | | | |
| Recovery | | | |

**Divergences:** [explicit list of who disagrees with whom and how you resolve it]

### Cycle-Phase Read

- **Phase:** [chosen]
- **Confidence:** [high / medium / low] — [why]
- **Biggest uncertainty:** [one line]

### Change-the-Read Triggers

| Indicator | Threshold | Implied phase shift |
|---|---|---|

### Bias Check
[Strongest contradicting indicator; recency-bias note]

## Verification

- [ ] Every indicator value is user-supplied with source + date.
- [ ] Each indicator classified on direction, timing, and strength.
- [ ] Divergences named and explicitly reconciled, not ignored.
- [ ] Computed metrics show formula → inputs → result.
- [ ] Cycle phase carries a confidence level and a stated uncertainty.
- [ ] Change-the-read triggers are specific and threshold-based.
- [ ] Confirmation-bias guardrail applied with a named contradicting indicator.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Stating indicator values from memory | All prints are user inputs with source/date; stop if missing |
| Ignoring indicators that contradict the narrative | Signal reconciliation table must place every indicator; divergences named explicitly |
| Over-reading a single latest print | Require trend/prior context; recency-bias note mandatory |
| Treating a cycle phase as certain | Confidence level + biggest uncertainty required |
| Leading/lagging confusion | Timing axis classification required for each indicator |
| Correlation read as causation | When linking indicators, state mechanism or flag as association only |
