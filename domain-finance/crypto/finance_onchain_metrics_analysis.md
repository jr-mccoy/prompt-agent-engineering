---
title: "On-Chain Metrics Analysis — Usage, Flows, and Holder Concentration vs. Base Rates"
category: finance/crypto
description: "Interpret on-chain metrics (active addresses, transactions, TVL, exchange flows, holder concentration, supply dynamics) for an investment read — anchoring every claim to a base rate, separating signal from noise, and guarding against the wash-trading, address-inflation, and Sybil artifacts that make raw on-chain numbers misleading."
techniques:
  - DS-02
  - NE-11
  - QA-02
  - RT-06
  - QA-04
difficulty: advanced
tags:
  - on-chain
  - blockchain-metrics
  - tvl
  - exchange-flows
  - holder-concentration
  - crypto
updated: "2026-06-18"
related_prompts:
  - domain-finance/crypto/finance_token_valuation_framework.md
  - domain-finance/crypto/finance_smart_contract_risk_review.md
  - domain-reasoning-craft/forecasting/forecasting_signal_vs_noise_filter.md
  - domain-finance/field_guide.md
---

**Informational only — not investment advice. On-chain data is noisy, gameable (wash trading, Sybil addresses), and easily misread. All outputs must be independently verified before any capital is committed.**

## Objective

Turn raw on-chain data into a disciplined investment read: what the metrics actually say about
usage, demand, distribution, and flows — and, just as important, what they do **not** say because
of measurement artifacts. The deliverable anchors each metric to a base rate (its own history and
peer comparables), separates genuine signal from noise, flags gameable metrics, and states a
confidence-qualified interpretation rather than a narrative dressed up as data.

## When to Use

- Building the on-chain section of a Stage 2 crypto dossier
- Checking whether usage supports (or contradicts) a token's valuation/narrative
- Detecting distribution risk (whale concentration) or flow-driven supply pressure
- Sanity-checking a bullish "metrics are exploding" claim against artifacts

## Inputs / Context Required

**Core metrics (point-in-time, with history)**
- Activity: active addresses, transaction count/volume, fees paid
- Capital: TVL (for DeFi), realized cap / market cap, stablecoin supply on chain
- Flows: exchange inflows/outflows, bridge flows
- Distribution: holder concentration (top-N wallet share), supply held by contracts vs. EOAs
- Supply dynamics: issuance, burns, staked/locked share

**Context for base rates (RT-06)**
- The metric's own trailing history (to judge "high/low" relative to itself)
- Peer protocols/tokens for cross-comparison
- Any metric unavailable → mark `UNAVAILABLE` and queue (DS-02)

## Constraints

### Must
- Anchor every "high/low/rising" claim to a base rate — the metric's own history and/or peers —
  with the comparison shown (NE-11, RT-06).
- Apply a signal-vs-noise filter before interpreting; distinguish a trend from a single spike
  (reuse `forecasting_signal_vs_noise_filter.md`) (QA-04).
- Explicitly flag gameable metrics (address counts → Sybil; volume → wash trading; TVL →
  double-counting/incentive farming) and discount them (QA-02).
- Cross-read metrics together (e.g. rising addresses + flat fees may mean Sybil farming), not in
  isolation (RT-06).
- State a confidence level on each conclusion; queue missing inputs (DS-02, QA-04).

### Must Not
- Present a raw metric as bullish/bearish without a base-rate comparison.
- Treat active-address or volume spikes as organic demand without an artifact check.
- Count incentive-inflated TVL as durable capital without saying so.
- Infer causation from a single co-moving pair (correlation ≠ cause).
- Invent metric values or peer baselines — queue unknowns instead (DS-02).

## Instructions

1. **Establish base rates (NE-11, RT-06).** For each metric, state its trailing range/percentile
   and a peer comparison. Compute relative position, e.g. `z_or_pctile = where today sits vs.
   trailing distribution`. Without this, a number is not yet a signal.

2. **Filter signal from noise (QA-04).** Apply `forecasting_signal_vs_noise_filter.md`: is the
   move persistent and corroborated, or a one-off/seasonal/artifact? Down-weight noise.

3. **Run the artifact checks (QA-02).** For each gameable metric, test the artifact hypothesis:
   address inflation/Sybil, wash-traded volume, incentive-farmed or double-counted TVL,
   exchange-internal transfers masquerading as flows. Discount accordingly.

4. **Cross-read metrics (RT-06).** Combine metrics for a coherent read (e.g. fees vs. addresses
   for genuine usage; exchange outflows vs. price for accumulation; concentration vs. liquidity
   for dump risk). Note contradictions rather than cherry-picking.

5. **Write the confidence-qualified read (QA-04).** State the interpretation per theme (usage,
   demand, distribution, flows) with a confidence level and the queued unknowns.

## Output Format

```
## ON-CHAIN READ: <TOKEN/PROTOCOL> | as_of [date]
```

### Metric vs. base rate
| Metric | Value | Base rate (history / peers) | Relative position | Signal/noise |
|---|---|---|---|---|
| Active addresses | … | … | … | … |
| Fees | … | … | … | … |
| TVL | … | … | … | … |
| Exchange net flow | … | … | … | … |
| Top-N holder share | … | … | … | … |

### Artifact checks
| Metric | Artifact risk | Verdict (organic / discounted) |
|---|---|---|
| Addresses | Sybil inflation | … |
| Volume | Wash trading | … |
| TVL | Incentive/double-count | … |

### Cross-read & interpretation
- Usage · Demand/flows · Distribution risk — each with a confidence level

### Open items (queued, not guessed)
- `UNAVAILABLE` metrics / baselines

## Verification

- [ ] Every claim is anchored to a base rate (own history and/or peers), shown explicitly.
- [ ] Signal/noise filter applied; single spikes not treated as trends.
- [ ] Gameable metrics flagged and discounted (Sybil / wash / incentive TVL).
- [ ] Metrics cross-read for coherence; contradictions surfaced, not hidden.
- [ ] Conclusions carry confidence levels; missing inputs queued, not invented.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| "Addresses are exploding" = organic demand | Base-rate + Sybil artifact check; cross-read with fees (RT-06) |
| Wash-traded volume read as liquidity/interest | Volume artifact check; discount gameable volume (QA-02) |
| Incentive-farmed TVL counted as durable capital | Flag incentive dependence; mark non-durable |
| One co-moving pair implies causation | Cross-read multiple metrics; correlation ≠ cause |
| Raw number called high/low with no reference | Mandatory base-rate comparison (NE-11) |
| Missing metric filled with a plausible value | `UNAVAILABLE` + queue (DS-02) |
