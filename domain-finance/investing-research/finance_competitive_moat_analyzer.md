---
title: "Competitive Moat Analyzer — Source, Durability, and Erosion Tests"
category: finance/investing-research
description: "Diagnose the source and durability of a competitive moat (network effects, scale, switching costs, IP, brand, cost advantage), test it against quantitative evidence, and stress it with erosion scenarios that could narrow or break it."
techniques:
  - RT-02
  - RT-05
  - DT-02
  - QA-02
  - DS-06
difficulty: intermediate
tags:
  - competitive-advantage
  - moat
  - durability
  - network-effects
  - switching-costs
  - pricing-power
updated: "2026-06-08"
related_prompts:
  - domain-finance/investing-research/finance_investment_thesis_builder.md
  - domain-finance/investing-research/finance_management_quality_assessment.md
  - domain-finance/investing-research/finance_short_thesis_constructor.md
  - domain-finance/field_guide.md
---

*For informational purposes only. Not financial, investment, or tax advice.*

## Objective

Determine whether a business has a durable competitive advantage, what its source is, and how long it is likely to persist. The analyzer (1) classifies the moat source(s), (2) tests each claimed moat against quantitative evidence (returns on capital, pricing power, market-share stability, retention), and (3) stress-tests durability with concrete erosion scenarios. The output distinguishes a genuine, evidenced moat from a narrative moat that the numbers do not support.

## When to Use

- Underwriting a "quality compounder" thesis where durability is the crux
- Assessing whether high returns on capital are defensible or will mean-revert
- Comparing the moat strength of two competitors
- Building the durability leg of a long thesis or the erosion leg of a short thesis
- Re-checking a long-held quality name for moat erosion

## Inputs / Context Required

**Business context**
- Company, ticker, sector; what the business sells and to whom
- Market structure (fragmented / oligopoly / monopoly) and main competitors

**Quantitative evidence**
- Returns on capital history (ROIC / ROCE) over a full cycle, with WACC if available
- Gross/operating margins vs. peers; pricing history (ability to raise price without volume loss)
- Market-share trend; customer retention / churn / net revenue retention if disclosed
- R&D, capex, and customer-acquisition intensity

**Moat-specific inputs**
- Evidence for each claimed moat source (network data, switching-cost friction, patent estate, brand surveys, cost-curve position)
- Any disruptive entrants, technology shifts, or regulatory changes in the space

## Constraints

### Must
- Classify the moat into one or more recognized sources and require evidence for each (RT-02, DT-02): network effects, economies of scale / cost advantage, switching costs, intangible assets (IP/brand/licenses), and efficient-scale niche.
- Test each claimed moat against quantitative evidence — a moat claim with stable-or-rising ROIC above WACC and pricing power is supported; one without is narrative (RT-05).
- Stress durability with at least three concrete erosion scenarios (QA-02).
- Rank moat sources by strength and durability (DS-06).
- Distinguish a wide-but-shrinking moat from a narrow-but-widening one — direction matters as much as level.

### Must Not
- Accept a moat claim on narrative alone; require it to show up in returns, pricing, share, or retention.
- Invent ROIC, market-share, retention, or survey data. Mark gaps `[ASSUMED]`/`[NOT DISCLOSED]`.
- Assume past high returns guarantee future durability (survivorship/extrapolation bias).
- Conflate a strong brand with pricing power, or scale with a cost advantage, without the supporting evidence.

## Instructions

1. **Classify the moat source(s) (RT-02).** Identify which of the recognized sources apply and state the specific mechanism for each. A company may have more than one; some claimed moats may not survive scrutiny.

2. **Test against the returns evidence (RT-05).** A real moat manifests as persistent excess returns on capital:
```
Economic spread = ROIC − WACC
   Persistently positive and stable/rising → moat supported
   Positive but compressing → moat narrowing
   Near or below zero → moat absent or already eroded
```
   Examine the full-cycle ROIC path, not a single peak year.

3. **Test pricing power (DT-02).** Look for the ability to raise prices ahead of cost inflation without losing volume/share. Note gross-margin stability through input-cost cycles. Flag if "pricing power" is actually just inflation pass-through.

4. **Test share and retention stability.** Stable or rising market share and high customer retention / net revenue retention corroborate switching-cost or network moats. Falling share with high margins is a warning that the moat is being harvested, not defended.

5. **Map the reinvestment runway.** Assess whether the company can redeploy capital at high returns (a moat that also reinvests compounds; a moat with no runway is a cash cow that fades).

6. **Stress durability — erosion scenarios (QA-02).** Construct at least three concrete threats and assess each:
   - Technology / business-model disruption
   - New entrant with scale capital (or a platform bundling the product)
   - Regulatory or standardization change reducing switching costs
   - Customer/supplier concentration shifting bargaining power
   For each, estimate the time-to-impact and the moat dimension it attacks.

7. **Rank and synthesize (DS-06).** Score each moat source on strength (1–5) and durability (1–5), give the net assessment (wide/narrow × widening/stable/narrowing), and state the single biggest erosion risk and its leading indicator.

## Output Format

```
## MOAT ANALYSIS: [Company] ([Ticker]) | [Sector] | Market structure: [ ]
```

### Moat Source Classification
| Source | Claimed? | Mechanism | Evidence | Verdict (Real / Partial / Narrative) |
|---|---|---|---|---|
| Network effects | | | | |
| Economies of scale / cost advantage | | | | |
| Switching costs | | | | |
| Intangibles (IP / brand / license) | | | | |
| Efficient-scale niche | | | | |

### Quantitative Tests
```
Economic spread = ROIC − WACC = [%]   (full-cycle path: [trend])
Pricing power: gross margin through cost cycle = [stable / compressing]
Market share trend = [rising / stable / falling]
Retention / NRR = [%]   → [supports / contradicts moat claim]
```

### Reinvestment Runway
[Can capital be redeployed at high incremental returns? Evidence and assessment]

### Erosion Stress Tests
| Threat | Moat dimension attacked | Likelihood | Time-to-impact | Leading indicator |
|---|---|---|---|---|
| Tech / model disruption | | | | |
| Scaled new entrant | | | | |
| Regulatory / standardization | | | | |
| Concentration / bargaining shift | | | | |

### Moat Scorecard
| Source | Strength (1–5) | Durability (1–5) | Net |
|---|---|---|---|

- **Overall:** [Wide / Narrow] and [Widening / Stable / Narrowing]
- **Biggest erosion risk:** [threat] — **watch:** [leading indicator]

## Verification

- [ ] Each claimed moat source has a stated mechanism and supporting evidence.
- [ ] The moat is tested against full-cycle ROIC − WACC, not a single peak year.
- [ ] Pricing power is distinguished from mere inflation pass-through.
- [ ] Market-share and retention trends are checked for corroboration or contradiction.
- [ ] At least three concrete erosion scenarios are stress-tested with time-to-impact.
- [ ] Moat direction (widening/narrowing) is assessed, not just the level.
- [ ] Missing data is `[ASSUMED]`/`[NOT DISCLOSED]`; no invented ROIC/share/retention figures.
- [ ] The single biggest erosion risk and its leading indicator are named.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Accepting a moat on narrative alone | Require the moat to appear in ROIC, pricing, share, or retention evidence |
| Extrapolating past high returns indefinitely | Full-cycle ROIC path + mandatory erosion scenarios; survivorship bias named |
| Confusing brand with pricing power | Pricing-power test isolates price increases ahead of cost without volume loss |
| Confusing scale with cost advantage | Require cost-curve evidence, not size alone |
| Inventing share/retention/survey data | Mark `[NOT DISCLOSED]`; never fabricate corroborating metrics |
| Missing a narrowing moat behind high margins | Direction assessed explicitly; falling share + high margin flagged as harvesting |
| Treating a cash cow as a compounder | Reinvestment-runway test separates durable compounding from fade |
