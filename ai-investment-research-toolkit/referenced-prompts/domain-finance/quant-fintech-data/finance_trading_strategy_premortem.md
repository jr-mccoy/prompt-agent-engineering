---
title: "Trading Strategy Pre-Mortem — Regime Risk, Costs, Crowding, and Capacity"
category: finance/quant-fintech-data
description: "Run a structured pre-mortem on a trading strategy before it goes live: assume it has already failed and work backward through the most likely killers — regime dependence, underestimated transaction costs and slippage, crowding/alpha decay, capacity limits, leverage and tail risk, and operational/execution failure — producing a ranked failure register with tripwires and kill criteria."
techniques:
  - QA-02
  - NE-10
  - DS-06
  - RT-02
  - QA-04
difficulty: intermediate
tags:
  - pre-mortem
  - trading-strategy
  - regime-risk
  - crowding
  - capacity
  - transaction-costs
updated: "2026-06-08"
related_prompts:
  - domain-finance/quant-fintech-data/finance_backtest_design_critique.md
  - domain-finance/quant-fintech-data/finance_alt_data_thesis_evaluator.md
  - domain-finance/risk-management/finance_tail_risk_premortem.md
  - domain-finance/field_guide.md
---

**Informational only — not investment advice. A clean pre-mortem does not validate a strategy; it surfaces failure modes. All outputs must be reviewed by qualified professionals before any capital is committed.**

## Objective

Before deploying a trading strategy, assume it is twelve months later and the strategy has lost money or been shut down — then reason backward to the most probable causes and pressure-test the strategy against each. The deliverable is a ranked failure register, the early-warning tripwires that would flag each failure, and explicit kill criteria, so the strategy is deployed (if at all) with its weak points named and monitored rather than discovered in a drawdown.

## When to Use

- Final gate before allocating capital to a new (often backtested) strategy
- Re-underwriting a live strategy that is underperforming its backtest
- Investment-committee challenge of a quant or discretionary trading proposal
- Sizing and risk-limit setting for a strategy about to scale
- Pairing with a backtest critique: the backtest checks the history, the pre-mortem checks the future
- Designing the monitoring dashboard and kill switches before go-live

## Inputs / Context Required

```
<strategy_context>
Strategy summary: [signal, direction, universe, holding period, rebalance cadence]
Edge hypothesis: [why it should make money; what inefficiency it harvests]
Backtested metrics: [CAGR, Sharpe, max DD, turnover — and the deflated version if available]
Capital / target AUM: [intended size; expected % of ADV traded]
Leverage & instruments: [gross/net, derivatives, financing, borrow needs]
Liquidity of universe: [ADV of typical names; ease of exit]
Crowding context: [is this a well-known factor/anomaly? how many run it?]
Cost assumptions: [spread, commission, slippage, impact, financing]
Execution setup: [manual/algo, venues, latency sensitivity]
Regime dependence: [which market environment does the edge rely on?]
Risk limits / drawdown tolerance: [stated]
</strategy_context>
```

If the edge hypothesis or regime dependence is vague, treat that vagueness as itself a top failure mode — strategies whose authors can't say why they work tend to fail quietly.

## Constraints

### Must
- Open with the **pre-mortem framing**: "It is 12 months from now and this strategy failed. What happened?" Then enumerate causes (QA-02).
- Cover the **standard killers** across dimensions (RT-02): **regime dependence**, **transaction costs/slippage**, **crowding & alpha decay**, **capacity/liquidity**, **leverage & tail risk**, **execution/operational failure**, and **edge-was-never-real** (overfit backtest).
- For each failure mode, estimate **likelihood and impact** and rank them (DS-06) — do not treat all risks as equal.
- Stress the **cost realism**: re-state the cost stack and show how the edge survives (or doesn't) at realistic frictions and at target turnover.
- Address **capacity and crowding** quantitatively in framing: how does expected return degrade as AUM rises and as more capital chases the same signal?
- Define **tripwires** (leading indicators) and **kill criteria** (hard stops) for the top failure modes — observable, pre-committed, not discretionary.
- Acknowledge uncertainty (QA-04): the pre-mortem reduces surprise; it does not guarantee the list is complete.

### Must Not
- Invent return, Sharpe, slippage, or capacity figures — reason from supplied inputs or label `[ESTIMATE]`.
- Treat a strong backtest as a reason to skip the pre-mortem — overfit backtests are a named failure mode here.
- Produce an undifferentiated risk list; ranking by likelihood × impact is required.
- Leave failure modes without a corresponding tripwire or kill criterion.

## Instructions

**Step 1 — Pre-mortem framing.**
"Twelve months out, the strategy is down materially or has been pulled. Write the post-mortem in advance." Generate the candidate causes before evaluating them, to avoid anchoring on the most comfortable one.

**Step 2 — Failure-mode enumeration (RT-02).** For each dimension, state the specific way this strategy could die:

| Dimension | This strategy's specific failure path |
|---|---|
| Regime dependence | [edge relies on X regime; what if it flips?] |
| Transaction costs / slippage | [cost stack vs edge at target turnover] |
| Crowding / alpha decay | [how known is this; what happens as others pile in] |
| Capacity / liquidity | [% of ADV; can it exit in stress?] |
| Leverage / tail risk | [gross exposure; gap/blow-up scenarios] |
| Execution / operational | [venue, latency, data outage, model bug] |
| Edge never real | [overfit/leaked backtest; deflated Sharpe ≈ 0] |

**Step 3 — Likelihood × impact ranking (DS-06).**
```
Score each failure mode:
  Likelihood: High / Medium / Low
  Impact:     Severe / Moderate / Minor
Rank top 3–5 by combined severity. These get tripwires and kill criteria.
```

**Step 4 — Cost-survival check.**
```
Restate cost stack: half-spread + commission + slippage + market impact + financing/borrow.
Annual cost drag ≈ 2 × turnover × per-trade cost + financing.
Edge survives if: net expected return = gross edge − cost drag > 0 with margin.
Show whether the edge is robust or marginal to a realistic cost increase (e.g., +50% slippage).
```

**Step 5 — Capacity & crowding framing.**
```
- As AUM rises, trades become a larger % of ADV → impact rises → realized edge falls.
- As more managers run the signal, the anomaly compresses → IC decays.
State the AUM band where the strategy still clears costs, and the crowding signals to watch
  (e.g., correlated drawdowns with peer factor returns).
```

**Step 6 — Tripwires and kill criteria.**

| Failure mode | Tripwire (leading, observable) | Kill criterion (hard stop) |
|---|---|---|
| Regime flip | [e.g., factor return sign change over N weeks] | [e.g., trailing 3-mo Sharpe < threshold] |
| Cost blowout | [realized slippage vs modeled] | [net edge < 0 over rolling window] |
| Crowding | [rising correlation to known factor] | [IC below floor for N periods] |
| Capacity | [fill rates / impact rising] | [% ADV breach] |

**Step 7 — Verdict.**
Deploy / deploy-smaller / redesign / pass — with the top failure modes, their tripwires, and the pre-committed kill criteria stated. Note residual unknowns (QA-04).

## Output Format

```
## Trading Strategy Pre-Mortem — [Strategy Name]
Target AUM: [ ] | Horizon: [ ] | Prepared: [date] | Data: user-supplied

### 1. Pre-Mortem Framing
[The assumed-failure narrative]

### 2. Failure-Mode Enumeration
[Step 2 table across all dimensions]

### 3. Likelihood × Impact Ranking
[Top 3–5 ranked]

### 4. Cost-Survival Check
[Cost stack vs edge at target turnover; sensitivity]

### 5. Capacity & Crowding
[AUM band; crowding signals]

### 6. Tripwires & Kill Criteria
[Step 6 table for top failure modes]

### 7. Verdict
[Deploy / smaller / redesign / pass + residual unknowns]
```

## Verification

- [ ] Pre-mortem opens by assuming failure and enumerating causes before judging them.
- [ ] All seven dimensions covered, including "edge was never real" (overfit backtest).
- [ ] Failure modes ranked by likelihood × impact, not listed flat.
- [ ] Cost stack restated; edge tested for survival at realistic frictions and at +stress.
- [ ] Capacity/crowding framed with an AUM band and watch signals.
- [ ] Each top failure mode has both a tripwire and a hard kill criterion.
- [ ] Verdict states residual unknowns; pre-mortem not treated as validation.
- [ ] No return, cost, or capacity figures invented; estimates labeled.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Strong backtest used to skip the pre-mortem | Overfit/leaked backtest is itself a top failure mode; always include it |
| Treating all risks as equal | Rank by likelihood × impact; tripwires go on the top few, not everything |
| Assuming backtested costs hold live | Restate the full cost stack and stress slippage; marginal edges die on friction |
| Ignoring crowding for a "known" anomaly | Well-known signals decay as capital crowds in; state the crowding watch signals |
| Discretionary "we'll know when to stop" | Kill criteria must be pre-committed and observable, not judged in the moment |
| Treating a clean pre-mortem as a green light | The pre-mortem reduces surprise; it does not prove the edge — state residual unknowns |
