---
title: "Sum-of-the-Parts Valuation — Per-Segment Method Selection and Holding-Company Discount"
category: finance/valuation
description: "Build a sum-of-the-parts valuation by assigning the most defensible valuation method to each business segment, aggregating to an enterprise value, and applying a holding-company discount with explicit rationale and range."
techniques:
  - NE-11
  - RT-02
  - NE-10
  - QA-01
  - DS-02
difficulty: advanced
tags:
  - sotp
  - sum-of-the-parts
  - valuation
  - conglomerate
  - segment-valuation
  - holding-company-discount
updated: "2026-06-08"
related_prompts:
  - domain-finance/valuation/finance_trading_comps_builder.md
  - domain-finance/valuation/finance_dcf_model_builder.md
  - domain-finance/valuation/finance_football_field_synthesizer.md
  - domain-finance/financial-statement-analysis/finance_ratio_analysis_engine.md
  - domain-finance/field_guide.md
---

**Informational only — not investment advice. All outputs must be reviewed by qualified finance professionals before use in any transaction or decision.**

## Objective

Construct a sum-of-the-parts (SOTP) valuation for a diversified or multi-segment company by selecting the most appropriate valuation method for each business segment, combining segment values to a consolidated enterprise value, applying a defensible holding-company (conglomerate) discount or premium, and translating the result into a per-share equity value range across base / bull / bear scenarios.

## When to Use

- Valuing a conglomerate, holding company, or diversified industrial/financial company where a single-multiple approach distorts value
- Identifying a "sum-of-the-parts discount" relative to the consolidated trading price (potential activism or M&A catalyst analysis)
- Assisting a corporation considering spinning off or divesting a business segment
- Fairness-opinion work requiring segment-by-segment method selection
- Anchoring an investment thesis around the idea that one or more segments are mispriced within a consolidated structure

## Inputs / Context Required

**Parent company**
- Name, ticker, industry classification
- Consolidated financials (LTM): Revenue, EBITDA, EBIT, Net Income, Net Debt, Total Shares Outstanding
- Accounting framework (US GAAP / IFRS)
- Any publicly disclosed segment-level financials (from 10-K segment note or management reporting)

**Segment information — for each segment**
- Segment name and brief business description
- Revenue and EBITDA (LTM, and forward if available)
- Key operating metrics (e.g., ARR for SaaS, beds for healthcare, MWh capacity for utilities)
- Capex and working-capital profile (if different from consolidated)
- Any intra-company revenue eliminations that must be stripped out
- Whether segment financials are disclosed or must be estimated from management commentary

**Corporate overhead**
- Unallocated corporate-center costs that are not attributed to any segment
- Net debt at the consolidated level (any segment-specific debt if known)
- Non-operating assets (minority stakes, surplus real estate, pension surplus/deficit)

**Valuation preferences**
- Preferred method per segment (if the analyst has a view); otherwise, the model selects
- Comparable companies / transactions per segment (if available)

## Constraints

### Must
- Select and defend the valuation method for each segment based on the segment's financial profile and comparables (see Step 2).
- Treat unallocated corporate overhead as a negative-value component (capitalize it or apply a multiple); do not ignore it.
- Apply a holding-company discount within a stated, defensible range; do not apply zero discount or a round-number discount without rationale.
- Present segment values as ranges (bear / base / bull), not single-point estimates.
- Reconcile the SOTP to the consolidated financials: the sum of segment EBITDA ± corporate costs should equal consolidated EBITDA (after eliminations).
- Explicitly bridge from SOTP enterprise value to equity value per share.

### Must Not
- Apply the same multiple to every segment regardless of different business profiles.
- Include a segment at its book value without noting the limitation if a market-based method cannot be applied.
- Apply a conglomerate discount without a range and rationale (common academic shorthand of "20% discount" is not acceptable without support).
- Invent segment financials; use disclosed data and flag estimates.
- Double-count inter-segment revenues that appear in multiple segment line items.

## Instructions

**Step 1 — Confirm the segment structure and reconcile to consolidated financials**

Build a segment reconciliation:

| Segment | Revenue | EBITDA | EBIT | Notes |
|---|---|---|---|---|
| Segment A | | | | [disclosed / estimated] |
| Segment B | | | | |
| Segment C | | | | |
| Corporate / Unallocated | | | | [costs only, negative] |
| Inter-segment eliminations | | | | [negative adjustment] |
| **Consolidated Total** | | | | [must tie to reported financials] |

If segment EBITDA does not reconcile to consolidated EBITDA within a small rounding difference, flag and investigate before proceeding.

**Step 2 — Select the valuation method for each segment**

Use the decision framework below. For each segment, select the most defensible method and document the rationale.

| Segment Characteristic | Recommended Method | Backup Method |
|---|---|---|
| Stable, recurring cash flows; public comps available | EV/EBITDA trading comps | DCF |
| High growth, limited current earnings | EV/Revenue comps; forward EV/EBITDA | DCF on revenue-to-margin ramp |
| Asset-intensive (utilities, real estate, mining) | EV/EBITDA + asset/replacement value | DCF |
| Financial services (bank, insurance, asset manager) | P/E or P/Book comps | DDM / Embedded Value |
| R&D pipeline / optionality | Sum of risk-adjusted NPV of programs | Real-options framework |
| Non-operating minority stake (publicly traded) | Market value of stake × ownership % | Quoted market price |
| Non-operating minority stake (private) | Book value or last-round valuation | DCF if cash-flow data available |

**Step 3 — Value each segment (base case)**

For each segment, apply the selected method:

```
For a trading-comps segment:
  Segment EV = Peer Median Multiple × Segment Normalized EBITDA (or Revenue)
  State the peer set and multiple applied

For a DCF segment:
  Segment EV = Σ PV(FCF) + PV(Terminal Value)
  State all key assumptions (see finance_dcf_model_builder.md)

For a minority-stake (public):
  Segment Value = Shares Owned × Current Market Price × Ownership %
  Note any discount for lack of control / lock-up if applicable
```

**Step 4 — Value corporate overhead**

Unallocated corporate-center costs are a drag on value. Capitalize them at a representative multiple:

```
Corporate Overhead Value = − [Annual Unallocated Corporate Costs] × Capitalization Multiple

Capitalization Multiple options:
  Conservative: use the lowest EBITDA multiple of any segment (most pessimistic)
  Mid-point: use a blended average of segment multiples
  Most common practice: apply a perpetuity-style capitalization: − Corporate Costs / WACC
```

State the method chosen and the impact on total SOTP value.

**Step 5 — Aggregate to SOTP enterprise value**

| Component | Method | Bear EV | Base EV | Bull EV |
|---|---|---|---|---|
| Segment A | [method] | | | |
| Segment B | [method] | | | |
| Segment C | [method] | | | |
| Corporate overhead | [method] | | | |
| Non-operating minority stakes | Market / stated | | | |
| Other non-operating assets | [method] | | | |
| **SOTP Enterprise Value (pre-discount)** | | | | |

**Step 6 — Apply the holding-company discount (or premium)**

The holding-company / conglomerate discount reflects:
- Management overhead and complexity premium demanded by investors
- Lack of pure-play visibility and benchmarking
- Potential capital misallocation risk
- Limited exit options for individual segments

Common observable discount range: **10–25% for diversified conglomerates**; tighter (5–15%) for focused or highly correlated segments; wider (25–35%) for truly unrelated segments with complex cross-holdings.

```
SOTP EV (discounted) = SOTP EV (pre-discount) × (1 − Conglomerate Discount %)

Conglomerate Discount range — state the basis:
  Low end (5–10%): segments are strategically related; management overhead is modest; parent has a history of value-creating capital allocation
  Mid-point (15–20%): diversified but with some strategic rationale; typical for most conglomerates
  High end (25–35%): unrelated businesses; complex cross-holdings; limited transparency
```

For bear / base / bull, vary the discount:
- Bear: discount at the high end of the range (more value destroyed at parent)
- Base: discount at the midpoint
- Bull: discount at the low end (or no discount if a specific unlock catalyst is identified)

**Step 7 — Bridge to equity value per share**

```
SOTP Equity Value = SOTP EV (discounted) − Net Debt − Pension Deficit + Pension Surplus
                  − Minority Interest (at consolidated level, if any subsidiary is not wholly owned)
                  + Non-operating assets (already captured above; do not double-count)

SOTP Value / Share = SOTP Equity Value / Diluted Shares Outstanding
```

| | Bear | Base | Bull |
|---|---|---|---|
| SOTP EV (pre-discount) | | | |
| Conglomerate discount % | | | |
| SOTP EV (post-discount) | | | |
| − Net Debt | | | |
| − Pension deficit / + surplus | | | |
| − Minority interest | | | |
| SOTP Equity Value | | | |
| Diluted Shares | | | |
| **SOTP Value / Share** | | | |
| Current Share Price | | | |
| Premium / (Discount) to Price | | | |

**Step 8 — Catalyst analysis and sum-of-parts spread**

Calculate the SOTP discount to current price if the stock is trading below SOTP:

```
SOTP Spread = SOTP Value / Share − Current Price
SOTP Spread % = SOTP Spread / Current Price × 100

Identify potential catalysts for closing the discount:
  - Spin-off or IPO of a high-multiple segment
  - Divestiture of a drag segment
  - Activist investor pressure for structural change
  - Improved segment-level disclosure
```

## Output Format

### Segment Reconciliation to Consolidated Financials
[Step 1 table — must tie to reported numbers]

### Method Selection Rationale
[Step 2 table — one row per segment]

### SOTP Build

[Step 5 table — all components, bear/base/bull EV]

### Holding-Company Discount Rationale

> [One paragraph: state the discount rate and range, the basis for the selected point, and the factors that would move it toward the bull or bear end of the range.]

### Equity Bridge and Per-Share Value

[Step 7 table]

### SOTP Spread and Catalyst Map

| Catalyst | Estimated Value Unlock | Probability | Timeline |
|---|---|---|---|
| [Spin-off Segment A] | [+$X / share] | [%] | [12–18 months] |

## Verification

- [ ] Segment EBITDA reconciles to consolidated EBITDA after eliminations and corporate costs.
- [ ] Each segment has an explicitly stated and defended valuation method; no segment defaults to book value without disclosure.
- [ ] Corporate overhead is capitalized and included as a negative value.
- [ ] Conglomerate discount is applied as a range with written rationale; not a round number applied without basis.
- [ ] Non-operating assets included and not double-counted.
- [ ] Equity bridge complete: net debt, pension, minority interest all addressed.
- [ ] Diluted share count used.
- [ ] SOTP value expressed as a range (bear / base / bull); current price compared.
- [ ] No segment financial figures invented; estimated inputs are labeled `[ESTIMATED]`.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Applying the same multiple to all segments ("blended" comps shortcut) | Each segment gets a method selection from Step 2; different segment profiles require different methods |
| Setting the conglomerate discount to zero without rationale | Discount is required unless a specific reason for no discount is stated (e.g., ongoing separation process already announced) |
| Forgetting to include corporate overhead as a negative value | Corporate overhead is a required SOTP line item; omitting it overstates value |
| Double-counting inter-segment revenues | Reconciliation table in Step 1 explicitly removes inter-segment eliminations |
| Treating the SOTP result as a fundamental floor price | SOTP reflects a theoretical break-up value; market may sustain a conglomerate discount indefinitely if no catalyst exists |
| Precision illusion from segment-level modeling | Segment values are inherently less precise than pure-play comps; express as ranges and acknowledge estimation uncertainty for private/unreported segments |
