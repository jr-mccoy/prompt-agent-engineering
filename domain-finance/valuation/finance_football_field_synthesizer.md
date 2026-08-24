---
title: "Football Field Synthesizer — Multi-Method Valuation Range with Weighting Rationale"
category: finance/valuation
description: "Synthesize DCF, trading comps, precedent transactions, LBO, and other valuation methods into a structured football-field chart with explicit method weighting, cross-method anchoring, and a calibrated implied-value range."
techniques:
  - RT-02
  - DS-02
  - QA-01
  - NE-10
  - RP-03
difficulty: intermediate
tags:
  - football-field
  - valuation-synthesis
  - multi-method
  - fairness-opinion
  - investment-analysis
updated: "2026-06-08"
related_prompts:
  - domain-finance/valuation/finance_dcf_model_builder.md
  - domain-finance/valuation/finance_trading_comps_builder.md
  - domain-finance/valuation/finance_precedent_transactions_analysis.md
  - domain-finance/valuation/finance_lbo_model_builder.md
  - domain-finance/field_guide.md
---

**Informational only — not investment advice. All outputs must be reviewed by qualified finance professionals before use in any transaction or decision.**

## Objective

Synthesize two or more distinct valuation methods into a structured "football field" comparison — presenting each method's range on a common implied-value axis, applying explicit, defended weighting to arrive at a composite range, and using cross-method analysis to identify convergence zones and outlier methods that warrant scrutiny.

## When to Use

- Investment banking or fairness-opinion work requiring a multi-method valuation summary
- Investment committee presentations that must show the range of valuation outcomes
- Buy-side or sell-side research backing up a price target with more than one method
- M&A board presentations requiring "adequate consideration" support
- Synthesizing valuation work already done separately using prompts in this domain

## Inputs / Context Required

**Method outputs (supply any combination)**
- DCF: bear / base / bull equity value per share (or EV)
- Trading comps: 25th–75th percentile implied equity value per share
- Precedent transactions: 25th–75th percentile implied equity value per share
- LBO / financial-buyer floor: bear / base IRR-threshold-clearing equity value per share
- DDM: bear / base / bull intrinsic value per share
- Sum-of-the-parts: bear / base / bull equity value per share
- Any other method (e.g., 52-week high/low range, analyst price-target range — label as reference, not a fundamental method)

**Company context**
- Current share price (for comparison)
- 52-week trading range (optional, for reference bar)
- Analyst consensus price target range (optional, for reference bar)
- Nature of the valuation: standalone vs. transaction (acquisition, divestiture, fairness)

**Weighting preferences**
- If the analyst has method weighting preferences, state them; otherwise, the model will apply a default framework and ask for confirmation

## Constraints

### Must
- Present every method on the same implied-equity-value axis so ranges are visually comparable.
- State explicit, written rationale for why each method is given its assigned weight.
- Identify any method that produces an outlier range (>20% above or below the other methods) and investigate the cause.
- Cross-reference methods: the DCF and trading comps should be broadly consistent for a mature company; large divergences require explanation.
- Label reference bars (52-week range, price target) separately from fundamental valuation methods.
- Present the composite as a range, not a point estimate; state the derivation of the composite range boundaries.

### Must Not
- Average all methods with equal weight without justification; method weighting should reflect reliability for the specific company and purpose.
- Include the current trading price as a valuation method (it is the benchmark, not a method).
- Present a football field without noting that it reflects a point-in-time market snapshot; conditions can change.
- Use the composite to paper over a significant outlier without explaining why the outlier is discounted.

## Instructions

**Step 1 — Compile method outputs on a common axis**

List every available method with its output range (bear low → bull high for fundamental methods; 25th–75th percentile for comps-based methods):

| Method | Category | Low (Bear / 25th pct) | Midpoint (Base / Median) | High (Bull / 75th pct) | Notes |
|---|---|---|---|---|---|
| DCF (intrinsic) | Fundamental | [$] | [$] | [$] | [key assumptions] |
| Trading comps | Market-based | [$] | [$] | [$] | [peer set, multiple] |
| Precedent transactions | M&A-based | [$] | [$] | [$] | [deal set, multiple] |
| LBO (fin. buyer floor) | Transaction-based | [$] | [$] | [$] | [IRR threshold, leverage] |
| Sum-of-the-parts | Fundamental | [$] | [$] | [$] | [segment methods] |
| 52-week range | Reference only | [$] | — | [$] | [not a fundamental method] |
| Analyst targets | Reference only | [$] | [$] | [$] | [consensus range] |

**Step 2 — Identify cross-method consistency or divergence**

For each pair of fundamental methods, compute:
```
Midpoint Divergence = |Method A Midpoint − Method B Midpoint| / Method B Midpoint × 100%

Threshold:
  < 15% divergence: Broadly consistent — methods cross-confirm the range
  15–30% divergence: Material difference — investigate driver (market sentiment vs. intrinsic value gap?)
  > 30% divergence: Significant outlier — identify and address before synthesis
```

Common explanations for divergence:
- **DCF > Trading Comps**: market is pricing the stock at a discount to intrinsic value (potential upside) OR DCF assumptions are too optimistic
- **Precedent Transactions > Trading Comps**: control premium is embedded in deal prices; the gap reflects the expected acquisition premium
- **LBO floor < DCF**: financial buyer's return requirement is more demanding than the intrinsic discount rate; the LBO floor is the minimum a sponsor would pay, not the fundamental value

**Step 3 — Apply method weighting framework**

Default weighting logic by context:

| Context | Primary weight | Secondary weight | Reference only |
|---|---|---|---|
| Standalone investment analysis (no deal) | DCF 50–60% | Trading comps 30–40% | Precedents (no deal expected), LBO |
| Sell-side M&A advisory (strategic buyer) | Trading comps 40%, Precedents 40% | DCF 20% | LBO (shows floor) |
| Buy-side M&A advisory | DCF 40–50%, Trading comps 30% | Precedents 20% | — |
| Fairness opinion | All fundamental methods weighted; reference bars shown | — | — |
| Distressed / restructuring | LBO / recovery analysis 50%+ | DCF (going-concern) | Trading comps (less relevant) |

For the subject analysis, assign weights and state the rationale:

| Method | Weight | Rationale |
|---|---|---|
| DCF | [%] | [e.g., "Long-horizon intrinsic value; most reflective of standalone value; primary method for this analysis"] |
| Trading comps | [%] | [e.g., "Current market pricing; reliable peer set of 7 companies; secondary check"] |
| Precedent transactions | [%] | [e.g., "Relevant if acquisition is the expected outcome; 30% weight given no confirmed deal process"] |
| LBO | [%] | [e.g., "Financial-buyer floor; 0% in composite — used as a reference floor, not a fundamental value"] |
| **Total** | **100%** | |

**Step 4 — Compute the composite valuation range**

```
Composite Low = Σ (Method Low × Weight)
Composite Midpoint = Σ (Method Midpoint × Weight)
Composite High = Σ (Method High × Weight)
```

Present as: **Composite Range: $X.XX – $X.XX per share; Midpoint: $X.XX**

**Step 5 — Bull / bear debate on the composite (RP-03)**

Apply an opposing-analyst frame to stress-test the composite:

**Bull case for the composite range:**
- Which method produces the highest value, and why might it be the most relevant for this situation?
- What catalyst or rerating event would push the stock toward the high end?

**Bear case for the composite range:**
- Which method produces the lowest value, and what would make it the most predictive outcome?
- What deterioration in business fundamentals or market conditions would drive toward the low end?

**Synthesis:**
- At what price does the bull or bear case represent compelling risk/reward?
- What is the most important single assumption driving the difference between bull and bear composite?

**Step 6 — Sensitivity of the composite to method weighting**

Test whether the composite range changes materially if weighting shifts:

| Weighting Scenario | DCF Wt | Comps Wt | Precedent Wt | Composite Midpoint | Change vs. Base |
|---|---|---|---|---|---|
| DCF-heavy | 70% | 20% | 10% | [$] | [%] |
| Base weights | [%] | [%] | [%] | [$] | — |
| Comps-heavy | 20% | 60% | 20% | [$] | [%] |

If the composite midpoint moves materially with weighting changes, note that the conclusion is sensitive to method selection — a key risk to disclose.

## Output Format

### Football Field Table

[Step 1 — all methods with low/midpoint/high and notes]

### Cross-Method Consistency Check

| Method Pair | Midpoint A | Midpoint B | Divergence % | Assessment |
|---|---|---|---|---|
| DCF vs. Trading Comps | [$] | [$] | [%] | Consistent / Investigate |
| Trading Comps vs. Precedents | | | | |
| DCF vs. LBO | | | | |

### Method Weighting

[Step 3 table — weights and rationale]

### Composite Valuation Range

| | Low | Midpoint | High |
|---|---|---|---|
| Composite (weighted) | [$] | [$] | [$] |
| Current share price | — | [$] | — |
| Premium / (discount) to price | [%] | [%] | [%] |

### Bull / Bear Debate Summary

[Step 5 — 3–5 sentences per side, synthesis]

### Weighting Sensitivity

[Step 6 — sensitivity table]

## Verification

- [ ] All methods presented on a common equity-value axis.
- [ ] Each method's range is sourced from a completed analysis (not invented for the football field).
- [ ] Reference bars (52-week range, analyst targets) clearly labeled as non-fundamental.
- [ ] Method weighting is explicit with written rationale; does not default to equal weighting without justification.
- [ ] Cross-method divergence assessed; any >20% divergence investigated and explained.
- [ ] Composite range computed as a weighted sum of method midpoints / lows / highs.
- [ ] Bull / bear debate applied to the composite; synthesis identifies the most important driver.
- [ ] Weighting sensitivity table shows how the composite changes under alternative weight allocations.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Including the current trading price as a valuation "method" to anchor the football field | Trading price is a benchmark, not a fundamental method; label it as "Current Price" in a separate reference row |
| Equal-weighting all methods regardless of reliability for the context | Method weighting is explicit and context-driven; equal weighting requires a stated reason |
| Presenting the composite midpoint as "the" fair value | Composite is a range with stated uncertainty; the midpoint is a reference, not a conclusion |
| Ignoring an outlier method because it inconveniently widens the range | Outlier investigation is mandatory; if a method is excluded from the composite, the reason must be stated |
| Treating precedent-transaction multiples as a standalone-value method for a no-deal analysis | Precedent multiples embed control premia; they should be weighted lower in standalone analyses |
