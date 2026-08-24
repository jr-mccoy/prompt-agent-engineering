---
title: "Inflation Regime Analysis — Diagnosis, Decomposition, and Asset/Sector Implications"
category: finance/markets-macro
description: "Diagnose the prevailing inflation regime by decomposing inflation into demand-pull, cost-push, and expectations components, classify the regime (disinflation/reflation/stagflation/deflation), and trace asset-class and sector implications under explicit scenarios — with all data user-supplied."
techniques:
  - RT-06
  - NE-10
  - NE-11
  - QA-02
  - QA-04
difficulty: advanced
tags:
  - inflation
  - regime
  - stagflation
  - real-assets
  - macro
updated: "2026-06-08"
related_prompts:
  - domain-finance/markets-macro/finance_central_bank_reaction_function.md
  - domain-finance/markets-macro/finance_economic_scenario_modeler.md
  - domain-finance/markets-macro/finance_commodity_exposure_analysis.md
  - domain-finance/field_guide.md
---

**Informational only — not investment advice. All inflation, wage, and price data are user-supplied; outputs require review by qualified professionals.**

## Objective

Diagnose the prevailing inflation regime by (1) decomposing reported inflation into demand-pull, cost-push/supply, and expectations-driven components, (2) classifying the regime and its likely persistence, (3) tracing real-vs-nominal and asset/sector implications, and (4) framing scenarios for how the regime evolves — with every figure traced to a user-supplied input and no current inflation reading asserted from memory.

## When to Use

- Determining whether current inflation is demand-driven, supply-driven, or entrenched
- Distinguishing transitory disinflation from a regime change
- Positioning real assets, duration, and equity sectors for an inflation regime
- Building the inflation layer of a macro scenario or central-bank reaction analysis
- Pressure-testing a "inflation is beaten / inflation is back" narrative against the data

## Inputs / Context Required

```
<inflation_inputs>
Economy / region:  | Currency | As-of date

USER-SUPPLIED INFLATION DATA (value, prior, trend, source, date — do not assume):
  - Headline CPI/PCE (YoY, MoM, annualized recent run-rate)
  - Core CPI/PCE (YoY, MoM)
  - Core goods vs. core services split (esp. supercore/services-ex-housing if available)
  - Shelter/housing inflation
  - Wage growth (ECI, AHE) and unit labor costs
  - Inflation expectations: breakevens (5y, 5y5y), survey measures
  - Supply/cost proxies: commodity/energy prices, supplier delivery times, freight
  - Output gap / capacity utilization (if available)

CONTEXT:
  - Central-bank target and stated stance
  - Structural factors flagged by user (fiscal stance, deglobalization, demographics, energy transition)
QUESTION (optional): __________
</inflation_inputs>
```

If inflation data is not supplied, request it. Do not fabricate inflation readings.

## Constraints

### Must
- Use only user-supplied data; restate each series with source/date.
- Decompose inflation into demand-pull, cost-push/supply, and expectations components (RT-06), citing the indicator basis for each.
- Distinguish goods vs. services and sticky vs. flexible components.
- Show computed metrics as formula → inputs → result (NE-11) — e.g., real wage growth, run-rate annualization, real policy rate.
- Classify the regime (disinflation / reflation / stagflation / deflation / entrenched-high) with persistence reasoning.
- Provide scenarios (NE-10) for regime evolution with implications.
- Distinguish real vs. nominal effects across assets (Fisher).
- Apply guardrails for recency bias (one print ≠ a trend), base-effect distortion, and narrative fallacy; state confidence (QA-04).

### Must Not
- Assert current inflation, wage, or expectations data from memory.
- Call a regime change from a single month's print without trend and base-effect context.
- Treat all inflation as one thing — demand-pull and cost-push have opposite policy/asset implications.
- Conflate disinflation (slowing rate of increase) with deflation (falling prices).
- Present an asset implication without distinguishing the real vs. nominal channel.

## Instructions

**Step 1 — Restate the data.** Tabulate user-supplied series with source/date; compute recent run-rate.

```
Annualized run-rate from MoM:  (1 + MoM)^12 − 1   [state which months]
Base-effect flag: note if YoY is distorted by the comparison-period level a year ago.
```

**Step 2 — Decompose the drivers (RT-06).**

```
Demand-pull signals   : output gap > 0, tight labor, strong core-services-ex-shelter, wage-price feedback
Cost-push/supply signals: energy/commodity spikes, supplier delays, freight, core-goods led
Expectations signals  : breakevens & surveys rising/anchored; wage-setting behavior
Attribute the bulk of current inflation across these three buckets with the evidence for each.
```

**Step 3 — Goods/services & sticky/flexible split.** Identify where inflation is concentrated and how persistent each component tends to be (services/shelter sticky; goods/energy flexible).

**Step 4 — Compute supporting metrics.**

```
Real wage growth   = Nominal wage growth − Headline inflation
Real policy rate   = Policy rate − inflation (state measure)
Misery proxy / output-gap context as available
```

**Step 5 — Classify the regime and persistence.**

```
Disinflation   : inflation positive but decelerating
Reflation      : inflation rising from low base alongside growth
Stagflation    : high/sticky inflation + weak/negative growth (worst for 60/40)
Deflation      : falling price level (negative inflation)
Entrenched-high: inflation elevated and expectations un-anchoring
Persistence read: weight sticky-component share, expectations anchoring, wage dynamics.
```

**Step 6 — Trace implications (real vs. nominal).**

```
Rates/duration   : higher/sticky inflation → higher nominal yields, negative for long duration (real channel)
Real assets      : commodities, TIPS, infrastructure, some real estate tend to hedge (regime-dependent)
Equities         : pricing-power/short-duration/value tend to fare better in high inflation;
                   long-duration growth more sensitive; stagflation broadly negative
Cash             : real return = nominal − inflation (can be negative)
State each as a tendency with the channel, not a guarantee.
```

**Step 7 — Scenarios (NE-10).** Re-acceleration / sticky-plateau / clean disinflation / stagflation: implications and probability bands.

**Step 8 — Stress-test & bias check (QA-02 / QA-04).** Attack the regime call: what would falsify it? Apply recency, base-effect, and narrative-fallacy guardrails; state confidence and a disconfirming monitor.

## Output Format

### Inflation Data (user-supplied)

| Series | Latest | Prior | Run-rate | Source / date |
|---|---|---|---|---|

### Driver Decomposition

| Driver | Evidence | Estimated contribution | Persistence |
|---|---|---|---|
| Demand-pull | | | |
| Cost-push / supply | | | |
| Expectations | | | |

### Goods/Services & Sticky/Flexible Split
[Step 3]

### Computed Metrics
[Step 4 — formula → inputs → result]

### Regime Classification

- **Regime:** [chosen] | **Persistence:** [high/med/low] | **Confidence:** [H/M/L]

### Asset & Sector Implications

| Asset / sector | Direction | Channel (real/nominal) | Caveat |
|---|---|---|---|

### Scenarios

| Scenario | Inflation path | Likelihood band | Key implication | Falsifying indicator |
|---|---|---|---|---|

### Stress-Test & Bias Notes
[Step 8]

## Verification

- [ ] All inflation/wage/expectations data are user-supplied with source/date.
- [ ] Inflation decomposed into demand-pull, cost-push, and expectations with evidence.
- [ ] Goods/services and sticky/flexible split identified.
- [ ] Computed metrics show formula → inputs → result; base-effect flagged.
- [ ] Regime classified with persistence reasoning and confidence.
- [ ] Asset/sector implications distinguish real vs. nominal channel.
- [ ] Scenarios include likelihood bands and falsifying indicators.
- [ ] Recency, base-effect, and narrative-fallacy guardrails applied.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Asserting current inflation data from memory | All series are user inputs with source/date; stop if missing |
| Calling a regime change off one print | Require trend, run-rate, and base-effect context; recency guardrail |
| Treating all inflation as one driver | Mandatory demand/cost/expectations decomposition with evidence |
| Confusing disinflation with deflation | Define both explicitly; disinflation = slowing increase, not falling prices |
| Asset implication without channel | State real vs. nominal channel for every implication |
| Clean stagflation/reflation narrative | Narrative-fallacy guardrail; require a falsifying indicator per scenario |
