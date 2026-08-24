---
title: "Token Valuation Framework — Tokenomics, Value Accrual, and Scenario-Ranged Worth"
category: finance/crypto
description: "Value a crypto token by modeling its supply schedule and emissions, mapping how (and whether) value accrues to the token versus the protocol, applying the appropriate valuation lens (network value, fee/cash-flow, or relative), and expressing worth as a probability-weighted scenario range — with every input sourced or explicitly queued, never assumed."
techniques:
  - NE-11
  - NE-10
  - DS-02
  - QA-02
  - QA-04
difficulty: advanced
tags:
  - tokenomics
  - token-valuation
  - value-accrual
  - emissions
  - network-value
  - crypto
updated: "2026-06-18"
related_prompts:
  - domain-finance/crypto/finance_onchain_metrics_analysis.md
  - domain-finance/crypto/finance_smart_contract_risk_review.md
  - domain-finance/valuation/finance_reverse_dcf_expectations.md
  - domain-finance/field_guide.md
---

**Informational only — not investment advice. Crypto assets are highly volatile, may be illiquid or worthless, and token-valuation models rest on fragile assumptions. All outputs must be independently verified before any capital is committed.**

## Objective

Produce a defensible, scenario-ranged valuation of a token by first answering the question most
token "valuations" skip: **does value actually accrue to this token, and how?** The deliverable
is a fully-supply-aware model (circulating vs. fully-diluted, emission schedule, unlocks), an
explicit value-accrual mechanism (fees, burn, staking, governance, or none), the valuation lens
that mechanism justifies, and a bear/base/bull range with probabilities — not a single price
target. Every figure traces to a source or is marked queued; nothing is assumed.

## When to Use

- Valuing a token for a Stage 2 research dossier (equity-style rigor for crypto)
- Distinguishing tokens with real value accrual from those priced on narrative alone
- Stress-testing fully-diluted valuation against emission/unlock overhang
- Comparing a token's implied network value to on-chain usage

## Inputs / Context Required

**Supply & tokenomics**
- Circulating supply, total supply, fully-diluted supply; emission/inflation schedule; vesting
  and unlock calendar (team/investor/treasury allocations)
- Current price and market cap (circulating and fully-diluted)

**Value accrual & usage**
- The mechanism (if any) routing value to the token: protocol fees, buyback/burn, staking
  yield, real-yield distribution, governance rights, collateral/utility demand
- Protocol revenue/fees and their split (to token holders vs. treasury vs. LPs)
- On-chain usage signals (link to `finance_onchain_metrics_analysis.md`)

**Comparables & context**
- Peer tokens with comparable mechanisms (for relative lenses); market regime
- Any input not available → mark `UNAVAILABLE` and queue it (DS-02)

## Constraints

### Must
- Distinguish circulating from fully-diluted supply and model the emission/unlock schedule
  explicitly with embedded formulas (NE-11).
- State the value-accrual mechanism plainly; if value does **not** accrue to the token, say so —
  that is the most important finding (QA-02).
- Choose the valuation lens that the mechanism justifies (fee/cash-flow only where fees reach the
  token; network-value/relative otherwise) and show the math (NE-11).
- Express output as a probability-weighted bear/base/bull range, never a point target (NE-10).
- Source or queue every input; mark conclusions resting on `UNAVAILABLE` data as provisional
  (DS-02, QA-04).

### Must Not
- Value on fully-diluted optimism while ignoring emission/unlock dilution overhang.
- Apply a discounted-cash-flow or P/E-style lens to a token that captures no fees/cash flow.
- Treat protocol revenue as token-holder revenue without confirming the fee split.
- Invent supply figures, fee splits, or peer multiples — queue unknowns instead (DS-02).
- Collapse the range to a single number or imply precision the inputs cannot support.

## Instructions

1. **Map supply and emissions (NE-11).** Tabulate circulating / total / fully-diluted supply and
   the emission + unlock schedule by date. Compute forward dilution: `dilution_pct =
   (future_circulating − current_circulating) / current_circulating`. Flag near-term unlock cliffs.

2. **Determine value accrual (QA-02).** Identify exactly how value reaches the token: fees routed
   to holders, buyback/burn, staking real-yield, or none. If the answer is "none / governance
   only," record that as the headline finding and value accordingly (often network-value/relative).

3. **Select the lens and model it (NE-11).**
   - *Fee/cash-flow* (only if fees accrue to the token): annualized protocol fees to holders ÷
     required yield → holder-value; cross-check vs. market cap.
   - *Network value*: relate market cap to on-chain usage (e.g. value-to-usage ratios), using the
     on-chain read; avoid spurious precision.
   - *Relative*: compare to peer tokens on the same mechanism via consistent multiples.

4. **Build the scenario range (NE-10).** Construct bear/base/bull on the key drivers (usage growth,
   fee capture, dilution absorbed, multiple) with probabilities; show each scenario's implied
   value and the assumptions behind it.

5. **Stress and flag gaps (QA-04).** Note which conclusions depend on `UNAVAILABLE` inputs; mark
   them provisional and list the queued retrieval items.

## Output Format

```
## TOKEN VALUATION: <TOKEN> | as_of [date] | Value accrual: [fees/burn/staking/none]
```

### Supply & dilution
| Measure | Value | Note |
|---|---|---|
| Circulating supply | … | |
| Fully-diluted supply | … | |
| Forward dilution (next 12m) | …% | unlock cliffs: … |

### Value accrual
- Mechanism: [fees-to-holders / buyback-burn / staking real-yield / governance-only / NONE]
- Fee split (holders / treasury / LPs): … · Headline finding: …

### Valuation (lens: [fee / network-value / relative])
| Scenario | Probability | Implied value | Key assumptions |
|---|---|---|---|
| Bear | … | … | … |
| Base | … | … | … |
| Bull | … | … | … |

### Open items (queued, not guessed)
- `UNAVAILABLE` inputs + provisional conclusions that depend on them

## Verification

- [ ] Circulating vs. fully-diluted supply distinguished; emission/unlock schedule modeled.
- [ ] Value-accrual mechanism stated explicitly (including "none" where true).
- [ ] Valuation lens matches the mechanism; math is shown and auditable.
- [ ] Output is a probability-weighted range, not a point target.
- [ ] Forward dilution / unlock overhang is quantified.
- [ ] Every input is sourced or marked `UNAVAILABLE` and queued; no invented figures.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| "Cheap" on circulating mcap while huge unlocks loom | Model fully-diluted supply + unlock calendar; quantify forward dilution |
| Cash-flow lens applied to a token that captures no fees | Confirm value accrual first; mismatched lens is rejected (QA-02) |
| Protocol revenue counted as holder revenue | Require the fee split before crediting fees to the token |
| Point price target implies false precision | Mandatory bear/base/bull range with probabilities (NE-10) |
| Missing tokenomics filled with assumptions | `UNAVAILABLE` + queue; dependent conclusions marked provisional (DS-02) |
| Network-value ratios treated as exact | Present as ranges/orders of magnitude; cross-check with on-chain usage |
