---
title: "FX Exposure Analysis — Transaction, Translation, and Economic Exposure with Netting Math"
category: finance/markets-macro
description: "Map and quantify foreign-exchange exposure across transaction, translation, and economic dimensions, net exposures by currency, size sensitivity to rate moves, and frame hedge-ratio options under explicit FX scenarios."
techniques:
  - NE-11
  - RT-02
  - NE-10
  - QA-04
  - DS-02
difficulty: intermediate
tags:
  - fx
  - currency-risk
  - hedging
  - exposure-netting
  - translation-risk
updated: "2026-06-08"
related_prompts:
  - domain-finance/treasury-capital-markets/finance_treasury_hedging_program_design.md
  - domain-finance/markets-macro/finance_economic_scenario_modeler.md
  - domain-finance/markets-macro/finance_cross_asset_correlation_analysis.md
  - domain-finance/field_guide.md
---

**Informational only — not investment or hedging advice. All FX rates and exposure figures are user-supplied; outputs require review by qualified treasury/finance professionals.**

## Objective

Build a structured FX-exposure analysis that (1) separates transaction, translation, and economic exposure, (2) nets exposures by currency pair to find the true open position, (3) quantifies sensitivity to defined FX moves, and (4) frames hedge-ratio options across explicit scenarios — with every number traced to a user-supplied input and no current FX level asserted from memory.

## When to Use

- A treasury or finance team mapping its currency risk before setting a hedging policy
- Quantifying the P&L / equity impact of FX moves on a multi-currency business
- Reconciling "we hedge our invoices" with residual translation and economic exposure
- Preparing an FX section for a board, audit, or risk committee
- Upstream input to a hedging-program design or cross-asset risk view

## Inputs / Context Required

```
<fx_inputs>
Reporting (functional) currency:
As-of date:

CURRENT SPOT & FORWARD RATES — USER MUST SUPPLY (source/date each):
  - Spot rate for each relevant pair (e.g., EURUSD, USDJPY)
  - Forward points / forward rates if hedging is in scope
  - Interest rates per currency (for forward/carry math) if needed

TRANSACTION EXPOSURE (committed/forecast cash flows by currency):
  - Receivables / payables by currency and tenor
  - Forecast foreign-currency revenue / costs (with confidence)

TRANSLATION EXPOSURE (balance-sheet / income from foreign subs):
  - Net investment in foreign operations by currency
  - Foreign-currency-denominated debt
  - Subsidiary net income by currency (for income translation)

ECONOMIC / OPERATING EXPOSURE:
  - Competitor cost-base currencies; pricing power; input-cost currencies
  - Demand sensitivity to home-currency strength

EXISTING HEDGES:
  - Notional, direction, instrument, maturity per pair

RISK CONTEXT:
  - Risk tolerance / VaR limit / earnings-at-risk threshold (if any)
</fx_inputs>
```

If spot/forward rates are not supplied, request them. Do not fabricate FX levels.

## Constraints

### Must
- Use only user-supplied rates and exposures; restate each with source/date.
- Separate the three exposure types (RT-02) and never net transaction against translation without flagging the accounting/cash distinction.
- Net exposures within each currency to find the true open position (longs offset shorts).
- Show sensitivity as formula → inputs → result (NE-11).
- Provide FX scenarios (NE-10): base, home-currency-strength, home-currency-weakness, and a stress shock.
- State whether each exposure hits cash, P&L, or equity (OCI/CTA) — these are not interchangeable.
- State confidence on forecast (unhedged anticipated) exposures (QA-04).
- Apply a guardrail against double-counting and against treating accounting hedges as economic protection.

### Must Not
- Assert current spot or forward FX rates from memory.
- Net translation (equity/OCI) exposure against transaction (cash/P&L) exposure as if equivalent.
- Present a single hedge ratio as "correct" without the policy trade-off (cost of carry vs. risk reduction).
- Ignore economic exposure because it is harder to quantify — flag it qualitatively at minimum.
- Treat a forecast cash flow as a certain exposure without a probability/confidence note.

## Instructions

**Step 1 — Restate rates and raw exposures.** Tabulate spot/forward and each exposure with source/date.

**Step 2 — Classify exposure by type and impact channel.**

```
Transaction exposure  → committed/forecast FX cash flows → hits CASH and P&L on settlement
Translation exposure  → foreign subs/net investment/FX debt → hits EQUITY (OCI/CTA) or income on consolidation
Economic exposure     → competitive/operating cash-flow sensitivity → long-run P&L, not on the balance sheet
```

**Step 3 — Net by currency.**

```
Net open position (currency c) = Σ long exposures(c) − Σ short exposures(c) − existing hedges(c)
  Long  = you receive / own assets in c
  Short = you pay / owe liabilities in c
Report net position per currency in both foreign and reporting-currency terms:
  Reporting-currency value = Net position(c) × Spot(c → reporting)
```

**Step 4 — Quantify sensitivity.**

```
ΔReporting-currency value ≈ Net open position(c, foreign units) × ΔSpot(c)
%-move sensitivity:  for a ±X% move in the pair,
  Impact = Net position (reporting ccy) × (±X%)
Earnings-at-risk (simplified, single pair):
  EaR ≈ Net P&L-relevant position × σ(FX) × z   (z for chosen confidence; state σ source)
```

**Step 5 — Hedge-ratio framing across scenarios (NE-10).** For 0% / partial / full hedge, show residual open position and the cost of carry:

```
Forward rate ≈ Spot × (1 + i_quote)/(1 + i_base)   [covered interest parity, state rate inputs]
Hedge carry  = Forward − Spot   (points; positive = pickup, negative = cost)
Residual exposure at hedge ratio h = Net open position × (1 − h)
```

**Step 6 — Scenario impact table.** Base / home-strength / home-weakness / stress: show P&L, equity (CTA), and cash impact separately.

**Step 7 — Bias & double-count guardrails.** Confirm no exposure is counted twice (e.g., FX debt counted in both translation and transaction); flag economic exposure even if unquantified; state confidence on forecast exposures.

## Output Format

### Rates & Raw Exposures (user-supplied)

| Item | Currency | Amount (foreign) | Spot | Reporting-ccy value | Type | Source/date |
|---|---|---|---|---|---|---|

### Exposure by Type and Channel

| Exposure type | Currency | Net amount | Hits cash? | Hits P&L? | Hits equity (OCI/CTA)? |
|---|---|---|---|---|---|

### Net Open Position by Currency

| Currency | Long | Short | Existing hedge | Net open (foreign) | Net open (reporting) |
|---|---|---|---|---|---|

### Sensitivity

| Pair | Net position | ±1% move impact | ±10% move impact | EaR (state σ, z) |
|---|---|---|---|---|

### Hedge-Ratio Options

| Hedge ratio | Residual open position | Carry cost/pickup | Notes |
|---|---|---|---|
| 0% | | | |
| Partial (state %) | | | |
| Full (100%) | | | |

### Scenario Impact

| Scenario | FX move | Cash impact | P&L impact | Equity (CTA) impact |
|---|---|---|---|---|
| Base | | | | |
| Home-currency strength | | | | |
| Home-currency weakness | | | | |
| Stress shock | | | | |

### Economic Exposure & Bias Notes
[Qualitative economic-exposure flag; double-count check; forecast-exposure confidence]

## Verification

- [ ] All spot/forward rates and exposures are user-supplied with source/date.
- [ ] Transaction, translation, and economic exposures separated; not netted across channels.
- [ ] Net open position computed per currency (longs − shorts − hedges).
- [ ] Sensitivity shown as formula → inputs → result.
- [ ] Hedge carry computed via covered interest parity with stated rate inputs.
- [ ] Scenario table separates cash, P&L, and equity (CTA) impacts.
- [ ] Economic exposure flagged even where not quantified.
- [ ] Double-count check performed; forecast-exposure confidence stated.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Asserting current FX rates from memory | Spot/forward are user inputs with source/date; stop if missing |
| Netting translation against transaction exposure | Keep channels separate; equity (OCI/CTA) is not cash or P&L |
| Presenting one hedge ratio as optimal | Show 0/partial/full with residual exposure and carry trade-off; no single "right" answer |
| Ignoring economic exposure | Always flag it qualitatively even if unquantified |
| Double-counting FX debt | Explicit double-count check; an item appears in one exposure channel |
| Treating forecast flows as certain | Attach probability/confidence to anticipated (unhedged forecast) exposures |
