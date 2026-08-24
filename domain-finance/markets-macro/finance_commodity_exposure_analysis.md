---
title: "Commodity Exposure Analysis — Direct/Indirect Exposure and Pass-Through to Financials"
category: finance/markets-macro
description: "Map a company's or portfolio's commodity-price exposure (direct input, indirect, revenue-linked), estimate pass-through to margins and cash flow, and quantify sensitivity to price moves under explicit scenarios — with all prices and elasticities user-supplied."
techniques:
  - NE-11
  - RT-02
  - NE-10
  - QA-02
  - DS-02
difficulty: intermediate
tags:
  - commodities
  - input-costs
  - pass-through
  - margin-sensitivity
  - hedging
updated: "2026-06-08"
related_prompts:
  - domain-finance/markets-macro/finance_inflation_regime_analysis.md
  - domain-finance/treasury-capital-markets/finance_treasury_hedging_program_design.md
  - domain-finance/markets-macro/finance_economic_scenario_modeler.md
  - domain-finance/field_guide.md
---

**Informational only — not investment or hedging advice. All commodity prices, volumes, and elasticities are user-supplied; outputs require review by qualified professionals.**

## Objective

Build a commodity-exposure analysis that (1) maps direct, indirect, and revenue-linked commodity exposure, (2) estimates pass-through from commodity price to COGS, margin, and free cash flow, (3) quantifies sensitivity to defined price moves across scenarios, and (4) frames mitigation/hedging options — with every figure traced to a user-supplied input and no current commodity price asserted from memory.

## When to Use

- A manufacturer, energy buyer, agribusiness, or transport firm sizing its input-cost risk
- Estimating how a move in oil/gas/metals/grains flows through to margins and cash
- Reconciling "we have a fuel surcharge" with residual net exposure
- Building the input-cost layer of an earnings model, scenario, or hedging decision
- An investor assessing a company's commodity beta

## Inputs / Context Required

```
<commodity_inputs>
Company / portfolio:  | Reporting currency:  | As-of date:

CURRENT PRICES — USER MUST SUPPLY (source/date each):
  - Spot/forward price for each relevant commodity (e.g., Brent $/bbl, HH gas $/MMBtu, copper $/t)
  - FX if commodity is priced in a non-functional currency

EXPOSURE DATA:
  - Direct consumption: volume per commodity per period (e.g., bbl/yr, tonnes/yr)
  - Indirect exposure: commodity content embedded in purchased inputs (e.g., resin from oil)
  - Revenue linkage: products priced off a commodity index (output exposure)
  - Inventory position (long physical exposed to price falls)

FINANCIALS:
  - Revenue, COGS, EBITDA, and the commodity-cost share of COGS
  - Contractual pass-through terms (surcharges, indexed pricing, lag)
  - Existing hedges (notional, instrument, tenor, strike)

CONTEXT:
  - Pricing power / demand elasticity (qualitative or estimate)
  - Competitor exposure (do they share the same input?)
</commodity_inputs>
```

If prices are not supplied, request them. Do not fabricate commodity prices.

## Constraints

### Must
- Use only user-supplied prices, volumes, and elasticities; restate each with source/date.
- Separate direct, indirect, and revenue-linked (output) exposure (RT-02); note net long/short.
- Estimate pass-through explicitly: state the assumed pass-through ratio and lag, and show its source/basis.
- Show margin and cash sensitivity as formula → inputs → result (NE-11).
- Provide price scenarios (NE-10): base, up-shock, down-shock, and a stress move.
- Distinguish gross exposure from net exposure after pass-through and hedges.
- Stress-test the pass-through assumption (QA-02) — pass-through is rarely 100% or instant.
- Apply a guardrail against assuming full, immediate pass-through and against ignoring volume/demand response.

### Must Not
- Assert current commodity prices from memory.
- Assume 100% instantaneous pass-through unless contractually guaranteed and stated.
- Net output (revenue-linked) exposure against input exposure without flagging timing and basis differences.
- Present sensitivity without stating the commodity-cost share of COGS it depends on.
- Ignore second-order effects (demand destruction at high prices, competitor response).

## Instructions

**Step 1 — Restate prices and exposures.** Tabulate user-supplied prices and volumes with source/date.

**Step 2 — Map exposure type and direction.**

```
Direct input exposure   → consume commodity → SHORT the commodity (price ↑ hurts)
Indirect exposure       → commodity embedded in purchased inputs → partial SHORT (apply content %)
Revenue-linked (output) → product priced off index → LONG the commodity (price ↑ helps)
Inventory (physical)    → LONG existing stock (price ↓ hurts via write-down)
Net commodity position  = Σ long exposures − Σ short exposures (per commodity, in consistent units)
```

**Step 3 — Estimate pass-through.**

```
Pass-through ratio (PT) = % of an input-cost change recovered via price/surcharge
Effective net cost change = Gross input-cost change × (1 − PT)   [account for lag separately]
  Gross input-cost change = ΔPrice × Volume consumed
State PT source: contractual surcharge formula, historical regression, or assumption (flag which).
```

**Step 4 — Flow to margin and cash.**

```
ΔCOGS              = ΔPrice × Volume × (1 − indirect content adj. if applicable)
ΔEBITDA (pre-PT)   = −ΔCOGS (for input exposure) [+ revenue effect for output exposure]
ΔEBITDA (post-PT)  = −ΔCOGS × (1 − PT) + revenue pass-through effect
Margin impact (bps)= ΔEBITDA / Revenue
ΔFCF               ≈ ΔEBITDA × (1 − tax) ± working-capital effect (inventory revaluation)
Commodity-cost share of COGS = Commodity cost / Total COGS  [drives all of the above; state it]
```

**Step 5 — Scenario sensitivity (NE-10).** Base / up-shock / down-shock / stress: show gross and post-pass-through EBITDA and margin impact.

**Step 6 — Mitigation/hedge framing.** Hedge ratio options, instrument (futures/swaps/options/collars), basis risk note, and residual exposure.

**Step 7 — Stress-test & bias check (QA-02).** Attack the pass-through assumption (what if PT is half of assumed?); add the demand-response and competitor-response checks; state confidence.

## Output Format

### Prices & Exposures (user-supplied)

| Commodity | Price | Unit | Volume/period | Exposure type | Long/Short | Source/date |
|---|---|---|---|---|---|---|

### Net Commodity Position

| Commodity | Gross long | Gross short | Net position | Net direction |
|---|---|---|---|---|

### Pass-Through Assumptions

| Commodity | PT ratio | Lag | Basis (contract/regression/assumption) | Source |
|---|---|---|---|---|

### Margin & Cash Sensitivity

| Commodity | Cost share of COGS | ΔPrice | ΔCOGS | ΔEBITDA (gross) | ΔEBITDA (post-PT) | Margin bps | ΔFCF |
|---|---|---|---|---|---|---|---|

### Scenario Impact

| Scenario | Price move | EBITDA impact (gross) | EBITDA impact (post-PT) | Margin (bps) |
|---|---|---|---|---|
| Base | | | | |
| Up-shock | | | | |
| Down-shock | | | | |
| Stress | | | | |

### Mitigation & Stress-Test
[Hedge options + residual exposure; pass-through stress; demand/competitor checks; confidence]

## Verification

- [ ] All prices, volumes, and elasticities are user-supplied with source/date.
- [ ] Direct, indirect, and revenue-linked exposures separated with net position.
- [ ] Pass-through ratio and lag stated with their basis/source.
- [ ] Margin/cash sensitivity shown as formula → inputs → result.
- [ ] Commodity-cost share of COGS stated and used.
- [ ] Scenario table shows both gross and post-pass-through impacts.
- [ ] Pass-through assumption stress-tested; demand/competitor second-order effects noted.
- [ ] Confidence stated on pass-through and forecast volumes.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Asserting current commodity prices from memory | All prices are user inputs with source/date; stop if missing |
| Assuming full, instant pass-through | State PT ratio and lag with basis; stress-test at half the assumed PT |
| Netting output against input exposure naively | Flag timing and basis differences; keep gross and net separate |
| Sensitivity without cost-share context | Commodity-cost share of COGS must be stated and drive the math |
| Ignoring demand destruction at extreme prices | Add demand-response and competitor-response checks in the stress step |
| Treating hedges as basis-risk-free | Note basis risk between hedge instrument and actual physical exposure |
