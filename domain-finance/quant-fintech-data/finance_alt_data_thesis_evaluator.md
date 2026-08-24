---
title: "Alternative-Data Signal Evaluator — Edge, Decay, and Capacity"
category: finance/quant-fintech-data
description: "Evaluate an alternative-data signal (credit-card panels, web traffic, satellite, app downloads, sentiment) for genuine predictive edge, signal decay/half-life, capacity before it crowds out, coverage/bias limitations, and the look-ahead/point-in-time traps specific to alt-data — producing a go/no-go with a deflated, decay-aware expectation."
techniques:
  - RT-05
  - QA-02
  - NE-10
  - DS-02
  - QA-04
difficulty: advanced
tags:
  - alternative-data
  - signal-decay
  - capacity
  - edge-evaluation
  - point-in-time
  - quantitative-research
updated: "2026-06-08"
related_prompts:
  - domain-finance/quant-fintech-data/finance_backtest_design_critique.md
  - domain-finance/quant-fintech-data/finance_trading_strategy_premortem.md
  - domain-finance/investing-research/finance_investment_thesis_builder.md
  - domain-finance/field_guide.md
---

**Informational only — not investment advice. Alternative-data signals carry data-rights, privacy, and material-nonpublic-information considerations; clear legal/compliance review before use. All outputs must be reviewed by qualified professionals.**

## Objective

Determine whether an alternative-data signal is worth paying for and trading: does it carry incremental predictive edge beyond what price and fundamentals already contain; how fast does that edge decay as the data becomes widely available; how much capital can it absorb before crowding erodes the return; and what coverage, sampling, and point-in-time limitations could make the backtested edge an illusion. The deliverable is a structured evaluation and a go / pilot / pass recommendation with a deflated, decay-aware expectation — not invented signal statistics.

## When to Use

- A data vendor is pitching a panel/feed and you must decide whether to license it
- Prioritizing among several candidate alt-data sources competing for a research budget
- Diagnosing why an alt-data signal that backtested well is fading in production
- Sizing how much capital a signal can carry before slippage/crowding kills it
- Compliance/edge review of an alt-data idea before a pilot
- Building the evaluation rubric a quant team applies to every new data source

## Inputs / Context Required

```
<alt_data_context>
Signal description: [what the data measures and the economic hypothesis for why it predicts returns]
Source type: [card/transaction panel, web/app traffic, satellite, sentiment, supply-chain, geolocation]
Target: [which securities/sector; what it is supposed to predict — revenue surprise, traffic, demand]
Coverage: [% of the relevant universe/population the panel observes; known gaps]
History length & point-in-time: [how long; is the data as-it-was-known or backfilled/restated?]
Latency: [lag from real-world event to data availability; how fresh vs the market]
Update frequency & granularity: [daily/weekly; entity-level vs aggregate]
Reported backtest (if any): [IC, hit rate, return — as provided]
Cost: [license fee; engineering cost to operationalize]
Exclusivity: [exclusive, limited, or widely sold? how many likely subscribers]
Legal/compliance status: [data rights, PII, MNPI review status]
</alt_data_context>
```

If coverage, point-in-time status, or subscriber breadth is unknown, treat each as a material risk and weight the recommendation toward "pilot" or "pass."

## Constraints

### Must
- Require an **economic hypothesis** for why the signal should predict the target (RT-05) — a correlation without a mechanism is presumed spurious until shown otherwise.
- Evaluate **incremental edge**: does the signal add information *beyond* price, consensus estimates, and standard factors? Test orthogonality, not standalone correlation.
- Estimate **signal decay / half-life**: how the information coefficient (IC) erodes over time and as the data disseminates; an alpha that decays in weeks is a different asset than one durable for quarters.
- Assess **capacity**: the AUM the signal can support before market impact and crowding compress the return; tie capacity to liquidity of the target names and turnover.
- Audit **coverage & sampling bias**: is the panel representative? Geographic/demographic/merchant skew can make the signal track a biased slice, not the true population (DS-02).
- Apply the **point-in-time / look-ahead** discipline from backtesting: backfilled or restated alt-data is a classic leakage source; consumption timing must match real availability latency.
- Present a **deflated, decay-aware expectation** as a scenario band (NE-10 / QA-04), not a single IC.
- Adversarially stress (QA-02): "If this signal had no edge, what benign explanation would produce the observed backtest?"

### Must Not
- Invent IC, hit rates, capacity figures, or coverage percentages — compute from supplied data or label `[REQUIRES DATA]`.
- Treat standalone correlation with returns as edge; it must be incremental to existing information.
- Assume the historical IC persists; decay and crowding are the base case for disseminated data.
- Ignore data-rights / privacy / MNPI flags — route them to compliance explicitly.

## Instructions

**Step 1 — Economic hypothesis and mechanism.**
State why the data should predict the target, and the causal pathway (e.g., "card-panel spend at retailer X leads reported revenue because the panel samples ~Y% of transactions ahead of the print"). No mechanism → treat as spurious-risk-high.

**Step 2 — Incremental edge test.**
```
Edge is incremental, not standalone:
  1. Correlation of signal with target (raw).
  2. Correlation AFTER controlling for: price/momentum, consensus estimate revisions,
     standard factors. Residual predictive power = the real candidate edge.
  3. Information Coefficient (IC) of the orthogonalized signal vs forward returns.
Report raw vs incremental — the gap is how much is already in the price.
```

**Step 3 — Decay / half-life.**
```
Estimate how IC erodes:
  - Across the holding horizon (does the edge live for days, weeks, quarters?).
  - Across calendar time as subscribers grow (dissemination decay).
Half-life framing: time for IC to fall to half its initial value.
Implication: shorter half-life → higher turnover, more cost sensitivity, faster obsolescence.
```

**Step 4 — Capacity.**
```
Capacity ≈ f(target-name liquidity, required turnover, acceptable market impact).
  Higher turnover + less-liquid names → lower capacity before slippage eats the edge.
State the AUM band the signal plausibly supports and what shrinks it (crowding, ADV limits).
```

**Step 5 — Coverage & sampling-bias audit.**
| Dimension | Question | Risk if skewed |
|---|---|---|
| Population coverage | What % of true activity does the panel see? | Signal tracks a slice, not the whole |
| Composition | Geographic/demographic/merchant skew? | Biased estimate of the target |
| Stability | Does panel composition change over time? | Apparent trend is panel drift, not reality |
| Survivorship | Are dropped entities removed retroactively? | Backfill leakage |

**Step 6 — Point-in-time / leakage check.**
Confirm the backtest consumed the data at its real availability latency, not backfilled/restated values. Backfilled alt-data is one of the most common sources of fake alt-data alpha — flag if unverified.

**Step 7 — Deflated expectation and recommendation (NE-10).**

| Scenario | Net IC / edge | Capacity | Durability | Assumptions |
|---|---|---|---|---|
| Optimistic | [ ] | [ ] | [ ] | Mechanism holds, exclusive, PIT clean |
| Base | [ ] | [ ] | [ ] | Decay + partial dissemination + costs |
| Pessimistic | [ ] | [ ] | [ ] | Crowded, biased panel, or leakage suspected |

Recommendation: **Go** (durable incremental edge, adequate capacity, clean PIT), **Pilot** (promising but unverified — run a small forward test), or **Pass** (no incremental edge, fast decay, biased coverage, or leakage).

## Output Format

```
## Alt-Data Signal Evaluation — [Signal Name]
Source: [ ] | Target: [ ] | Prepared: [date] | Data: user-supplied

### 1. Economic Hypothesis & Mechanism
[Why it should work; causal pathway]

### 2. Incremental Edge
[Raw vs orthogonalized IC; what's already in the price]

### 3. Decay / Half-Life
[Horizon decay + dissemination decay]

### 4. Capacity
[AUM band + what compresses it]

### 5. Coverage & Sampling Bias
[Step 5 table]

### 6. Point-in-Time / Leakage Check
[Backfill audit; latency match]

### 7. Deflated Expectation & Recommendation
[Scenario band + Go / Pilot / Pass]

### Compliance Flags
[Data rights / PII / MNPI — routed for review]

### Known Limitations
[Unverified coverage, unknown subscriber breadth, short history]
```

## Verification

- [ ] An economic mechanism is stated; mechanism-free signals flagged as spurious-risk-high.
- [ ] Edge measured incrementally (after controlling for price/consensus/factors), not standalone.
- [ ] Signal decay / half-life estimated across both horizon and dissemination.
- [ ] Capacity tied to target liquidity, turnover, and impact — with an AUM band.
- [ ] Coverage and sampling-bias audited across population, composition, stability, survivorship.
- [ ] Point-in-time / backfill leakage explicitly checked.
- [ ] Expectation presented as a deflated scenario band; recommendation is Go/Pilot/Pass.
- [ ] No IC, capacity, or coverage figures invented; compliance flags routed.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Standalone correlation called "edge" | Edge must be incremental to price, consensus, and factors; report the orthogonalized IC |
| Assuming historical IC persists | Decay and crowding are the base case for sold data; model the half-life explicitly |
| Backtest on backfilled alt-data | Verify point-in-time consumption at real latency; backfill is a leading cause of fake alt-data alpha |
| Ignoring panel bias | A non-representative panel tracks a slice; audit coverage/composition before trusting the signal |
| Capacity assumed unlimited | Tie capacity to liquidity and turnover; crowding compresses returns as subscribers grow |
| Skipping data-rights/MNPI review | Route legal/privacy/MNPI flags to compliance; edge is irrelevant if the data can't be used |
