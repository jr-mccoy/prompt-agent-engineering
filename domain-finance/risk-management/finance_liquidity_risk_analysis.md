---
title: "Liquidity-Risk Analysis — Runway, Funding Concentration, LCR-Style Buffers"
category: finance/risk-management
description: "Analyze liquidity risk through cash runway, funding-source concentration, contractual maturity ladders, and an LCR-style buffer of high-quality liquid assets against stressed 30-day outflows — without inventing balances, run-off rates, or regulatory thresholds."
techniques:
  - NE-11
  - NE-10
  - QA-04
  - QA-02
  - DS-06
difficulty: advanced
tags:
  - liquidity-risk
  - cash-runway
  - lcr
  - funding-concentration
  - maturity-ladder
  - stress-testing
updated: "2026-06-08"
related_prompts:
  - domain-finance/risk-management/finance_stress_test_scenario_design.md
  - domain-finance/risk-management/finance_interest_rate_risk_analysis.md
  - domain-finance/credit-lending/finance_credit_risk_assessment.md
  - domain-finance/field_guide.md
---

*For informational purposes only. Not financial, investment, treasury, or risk-management advice. LCR and run-off conventions vary by jurisdiction; verify against current regulations as of the analysis date.*

## Objective

Assess an entity's liquidity risk across three lenses: (1) **cash runway** under base and stressed burn, (2) **funding concentration** by source, counterparty, tenor, and currency, and (3) an **LCR-style buffer** comparing high-quality liquid assets (HQLA) to net stressed 30-day cash outflows. Build a contractual maturity ladder to locate refinancing cliffs. Every figure traces to user-supplied balances and run-off assumptions; nothing is invented.

## When to Use

- Treasury liquidity review for a corporate, fund, fintech, or bank
- Pre-financing or covenant-monitoring liquidity check
- Diagnosing concentration in deposits, credit lines, or wholesale funding
- Building the liquidity leg of an enterprise stress program
- Startup / scale-up runway and bridge-planning under a downside case

## Inputs / Context Required

- **Liquidity sources:** Cash, equivalents, marketable securities (by quality tier), undrawn committed facilities, expected operating inflows.
- **Outflows:** Operating burn, debt service, contractual maturities, contingent draws (margin calls, guarantees), and their timing.
- **Funding profile:** Each funding source, amount, counterparty, tenor, currency, secured/unsecured, committed/uncommitted.
- **Run-off / haircut assumptions:** Stressed run-off rates on deposits/funding and haircuts on assets (user-supplied or regulatory; state source).
- **Horizon:** Runway in months; LCR uses a 30-day stress window.
- **Framework flag:** If a Basel III LCR-style calculation is intended, state the jurisdiction and that thresholds must be verified.

## Constraints

### Must
- Show formulas before computing (runway, LCR, concentration).
- Distinguish committed vs. uncommitted and secured vs. unsecured funding — uncommitted lines are not reliable stressed liquidity.
- Apply stressed run-off and haircut assumptions explicitly and state their source; mark assumed ones `[ASSUMED]`.
- Build a contractual maturity ladder and identify refinancing cliffs.
- Present base / adverse / severe-but-plausible runway and buffer outcomes.
- State that an LCR-style figure is a methodology illustration, not a regulatory determination, unless the user supplies official run-off categories.

### Must Not
- Invent balances, run-off rates, haircuts, or regulatory minimums; gaps are `[ASSUMED]` and excluded from definitive conclusions.
- Count uncommitted or revocable facilities as guaranteed liquidity under stress.
- Net inflows against outflows beyond conservative caps (LCR caps inflows at 75% of outflows; state if applying).
- Treat illiquid or encumbered assets as HQLA.
- Present a single runway number without a stressed downside.

## Instructions

1. **Inventory liquidity sources and tier them (NE-10).** Classify assets into HQLA tiers (Level 1: cash, high-grade sovereigns; Level 2: lower-quality, haircut) per user/regulatory definition; flag encumbered or illiquid holdings as non-HQLA.
2. **Compute cash runway.**
   ```
   Runway (months) = Available liquidity / Net monthly cash burn
     Available liquidity = unrestricted cash + reliably-available committed facilities
     Net monthly burn    = operating outflows − operating inflows (stressed)
   ```
   Compute base, adverse, and severe burn.
3. **Build the maturity ladder.** Bucket inflows and outflows by tenor (≤1m, 1–3m, 3–6m, 6–12m, >12m). Compute cumulative net position per bucket; flag negative cumulative buckets as refinancing cliffs.
4. **Measure funding concentration.**
   ```
   Concentration_source = funding from source / total funding
   Top-3 concentration  = Σ three largest sources / total funding
   ```
   Report by counterparty, tenor, currency; flag single-source dependence and short-dated reliance.
5. **Compute LCR-style buffer (QA-04).**
   ```
   LCR = HQLA (post-haircut) / Net stressed 30-day cash outflows
   Net outflows = Σ(outflow_i × stressed run-off_i) − min(Σ inflows × inflow_rate, 0.75 × gross outflows)
   ```
   State the haircut and run-off assumptions and their source. A ratio ≥ 1.0 means buffers cover one stressed month under the stated assumptions.
6. **Stress the buffer and runway (QA-02).** Re-run under adverse (partial deposit flight, facility pull) and severe (compounded run-off + asset haircut widening + facility withdrawal) cases.
7. **Bias & disconfirming check.** Name recency bias (calm-period funding stability assumed permanent) and concentration blind spots (correlated funders who run together). Test whether "diversified" funding actually behaves as one bloc under stress.

## Output Format

### Liquidity Sources (HQLA tiering)
| Source | Amount | Tier / HQLA? | Haircut | Post-haircut value | Encumbered? |
|---|---|---|---|---|---|

### Cash Runway
```
Runway = Available liquidity / Net monthly burn
  Base:   [$ ] / [$ ]/mo = [ ] months
  Adverse:[$ ] / [$ ]/mo = [ ] months
  Severe: [$ ] / [$ ]/mo = [ ] months
```

### Maturity Ladder
| Bucket | Inflows | Outflows | Net | Cumulative net | Cliff? |
|---|---|---|---|---|---|
| ≤1m | | | | | |
| 1–3m | | | | | |
| 3–6m | | | | | |
| 6–12m | | | | | |
| >12m | | | | | |

### Funding Concentration
| Dimension | Largest exposure | Top-3 share | Flag |
|---|---|---|---|
| Counterparty | [%] | [%] | |
| Tenor (short-dated) | [%] | — | |
| Currency | [%] | — | |

### LCR-Style Buffer (base / adverse / severe)
| | Base | Adverse | Severe-but-plausible |
|---|---|---|---|
| HQLA (post-haircut) | [$] | [$] | [$] |
| Net 30-day outflows | [$] | [$] | [$] |
| **LCR-style ratio** | [x] | [x] | [x] |

### Findings
[Refinancing cliffs, concentration breaches, buffer shortfalls, disconfirming-check result.]

## Verification

- [ ] Runway, LCR, and concentration formulas are shown before the numbers.
- [ ] Committed vs. uncommitted and secured vs. unsecured funding are distinguished.
- [ ] Run-off rates and haircuts are stated with their source; assumed values are `[ASSUMED]`.
- [ ] A maturity ladder is built and refinancing cliffs are flagged.
- [ ] Inflow netting respects the conservative cap (state if 75% LCR cap applied).
- [ ] Encumbered/illiquid assets are excluded from HQLA.
- [ ] Base, adverse, and severe cases are all presented for runway and buffer.
- [ ] Jurisdiction/framework caveat is present for any LCR-style determination.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Counting uncommitted lines as stressed liquidity | Only committed/irrevocable facilities count under stress; uncommitted excluded |
| Presenting an LCR figure as regulatory compliance | Labeled methodology illustration unless official run-off categories supplied; jurisdiction verification required |
| Single runway number implying safety | Mandatory adverse and severe burn cases alongside base |
| Treating illiquid assets as buffer | HQLA tiering with haircuts; encumbered assets flagged and excluded |
| "Diversified" funding assumed independent | Concentration check tests correlated-funder run-together risk |
| Calm-period stability assumed permanent | Recency bias named; stressed run-off applied to all funding |
| Inventing run-off rates to make the ratio pass | Run-off/haircuts must be user- or regulation-sourced; assumed values barred from definitive conclusions |
