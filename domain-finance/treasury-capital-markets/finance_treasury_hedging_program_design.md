---
title: "Treasury Hedging Program Design — FX / Rates / Commodity Hedge Ratio, Layering, and Policy Limits"
category: finance/treasury-capital-markets
description: "Design a treasury hedging program: identify exposure, set hedge ratio and tenor layering, select instruments, define policy limits, and quantify residual risk across scenarios."
techniques:
  - NE-11
  - NE-10
  - QA-02
  - DS-02
  - RT-03
difficulty: advanced
tags:
  - hedging
  - fx-risk
  - interest-rate-risk
  - commodity-hedge
  - treasury-policy
updated: "2026-06-08"
related_prompts:
  - domain-finance/risk-management/finance_hedging_strategy_designer.md
  - domain-finance/risk-management/finance_interest_rate_risk_analysis.md
  - domain-finance/treasury-capital-markets/finance_investment_policy_statement_builder.md
  - domain-finance/field_guide.md
---

**Informational only — not financial, investment, or hedge-accounting advice.**

## Objective

Design a treasury hedging program for FX, interest-rate, or commodity exposure: quantify the underlying exposure, set a target hedge ratio with a tenor-layering schedule, select appropriate instruments, codify policy limits and governance, and present the residual (unhedged) risk across market scenarios so leadership can see what the program does and does not protect.

---

## When to Use

- Establishing or refreshing a corporate FX, rates, or commodity hedging policy.
- Sizing a hedge layering schedule for a forecast exposure (e.g., next-12-month revenue).
- Selecting between forwards, swaps, options, and collars for a defined exposure.
- Translating a board risk appetite into hedge ratios and limits.
- **Do not use** to determine hedge-accounting designation or effectiveness testing (ASC 815 / IFRS 9 — route to accounting) or to give a market view/directional bet.

---

## Inputs / Context Required

```
<hedging_program_inputs>
Entity:
Reporting / functional currency:    [CCY]
Jurisdiction:                       [derivatives regulation, documentation regime]
Risk type(s):                       FX | Interest rate | Commodity (specify)

EXPOSURE
- Exposure description (e.g., EUR revenue, USD COGS, floating-rate debt, fuel cost):
- Notional / volume by period (12+ months forecast):
- Exposure certainty (committed vs. forecast/anticipated):
- Natural offsets (e.g., matching-currency costs, fixed-rate assets):
- Current hedges in place (instrument, notional, tenor, rate/strike):

RISK APPETITE / POLICY
- Board/treasury risk tolerance (e.g., max earnings variance, max % unhedged):
- Permitted instruments:
- Counterparty limits / credit policy:
- Existing hedge ratio targets (if any):

MARKET CONTEXT (state source + date; do not invent)
- Current spot / forward curve / swap rates / commodity curve:
- Volatility levels (for option pricing context):

SCENARIOS to test (e.g., +/−10% FX, +/−200 bps rates, +/−30% commodity):
</hedging_program_inputs>
```

---

## Constraints

### Must
- Quantify exposure and **net of natural offsets** before sizing hedges.
- Set a **hedge ratio** and a **tenor-layering schedule** (declining ratio for further-out, less-certain periods).
  - `Hedge Ratio = Hedged Notional ÷ Underlying Exposure` (per period).
- Justify **instrument selection** against the exposure profile and risk appetite (forward vs swap vs option vs collar), naming the tradeoff (cost vs. protection vs. flexibility) — RT-03.
- Compute **residual risk** per scenario: the unhedged exposure × market move (NE-11), shown across base/up/down moves (NE-10).
- Define **policy limits**: max notional, max tenor, permitted instruments, counterparty credit limits, approval authorities.
- Apply an **adversarial stress (QA-02)**: test the program where the forecast exposure does not materialize (over-hedge risk) and where the market moves against the unhedged residual.
- State that **hedge accounting (ASC 815 / IFRS 9) exists** and route designation/effectiveness specifics to accounting — do not fabricate treatment.
- Flag currency/jurisdiction and "verify current curves/rates and applicable derivatives regulation as of [date]."

### Must Not
- Invent forward points, swap rates, volatilities, or option premia.
- Recommend hedging 100% of an uncertain forecast exposure (creates over-hedge / speculative risk).
- Treat a hedge as eliminating risk (basis risk, credit risk, and forecast risk remain).
- Express a directional market view as the rationale for the hedge ratio.
- Omit counterparty credit risk from the program design.

---

## Instructions

1. **Quantify net exposure.**
   ```
   Net Exposure_period = Gross Exposure_period − Natural Offsets_period
   ```
   Separate **committed** (high certainty) from **forecast/anticipated** (lower certainty) exposure.

2. **Set the hedge-ratio policy by certainty and tenor (layering).** Higher ratio for near, committed periods; lower for far, forecast periods.
   ```
   Target Hedge Ratio(period) declines with tenor and forecast uncertainty
   Hedged Notional(period) = Net Exposure(period) × Target Hedge Ratio(period)
   Incremental layer each cycle = (Target ratio − Current ratio) × Net Exposure
   ```

3. **Select instruments (RT-03 tradeoff).**
   - **Forwards/futures:** lock a rate; zero upfront; no upside participation; good for committed exposure.
   - **Swaps:** convert floating↔fixed for rate exposure over a tenor.
   - **Options (caps/floors):** pay premium; retain favorable-move upside; good for uncertain forecast exposure.
   - **Collars:** finance option cost by giving up some upside; bounded outcome.
   State which instrument fits each layer and why (cost vs. protection vs. flexibility).

4. **Compute residual risk per scenario (NE-11, NE-10).**
   ```
   Unhedged Notional(period) = Net Exposure × (1 − Hedge Ratio)
   Residual P&L impact = Unhedged Notional × Market Move (scenario)
   Aggregate residual = Σ across periods
   ```
   Show base / adverse-up / adverse-down moves.

5. **Define policy limits and governance.** Specify: max aggregate notional, max tenor, permitted instruments, per-counterparty credit limits, mark-to-market reporting cadence, and approval authority tiers (who can transact what size).

6. **Adversarial stress (QA-02).**
   - **Over-hedge case:** forecast exposure under-delivers (e.g., revenue 20% below forecast) — the hedge becomes a speculative position; quantify the resulting MTM exposure.
   - **Adverse-market case:** market moves against the residual; quantify earnings/cash impact.
   - **Counterparty case:** note concentration if one bank holds most of the book.

7. **Basis & residual-risk disclosure.** Name what remains unhedged: forecast (volume) risk, basis risk (hedge index ≠ exposure index), credit/counterparty risk, and timing/rollover risk.

8. **Bias check + verification (QA-01).** Named pitfall: tail-risk blindness (assuming the forecast exposure is certain) and recency bias on current low vol/rates. Disconfirming check: re-run residual at the trailing-high adverse move. Confirm hedge-ratio and residual arithmetic; confirm no fabricated market data.

---

## Output Format

```
## Treasury Hedging Program — [Entity] — [FX / Rates / Commodity]
Functional currency: [CCY] | Prepared: [date] | Data + market context: user-supplied
(All figures illustrative unless traced to an input; market data must be sourced & dated)
Hedge-accounting note: ASC 815 / IFRS 9 designation & effectiveness routed to accounting.

### Net Exposure (illustrative)
| Period | Gross exposure | Natural offset | Net exposure | Certainty |
|--------|----------------|----------------|--------------|-----------|
| M1–3   | 120            | (20)           | 100          | Committed |
| M4–6   | 110            | (15)           | 95           | High      |
| M7–12  | 200            | (30)           | 170          | Forecast  |

### Hedge-Ratio Layering Policy
| Tenor band | Certainty | Target hedge ratio | Hedged notional |
|------------|-----------|--------------------|-----------------|
| 0–3 mo     | Committed | 90%                | 90 |
| 4–6 mo     | High      | 70%                | 66.5 |
| 7–12 mo    | Forecast  | 40%                | 68 |
| 13–24 mo   | Forecast  | 0–25%              | layered in over time |

### Instrument Selection
| Layer   | Instrument | Rationale (cost / protection / flexibility) |
|---------|------------|---------------------------------------------|
| 0–3 mo  | Forwards   | Committed; lock rate; zero premium |
| 7–12 mo | Options/collar | Forecast uncertainty; retain upside; bounded cost |

### Residual Risk Across Scenarios (illustrative)
| Scenario       | Aggregate unhedged notional | Market move | Residual P&L impact |
|----------------|-----------------------------|-------------|---------------------|
| Base           | 110                         | 0%          | 0 |
| Adverse −10%   | 110                         | −10%        | (11.0) |
| Adverse −10%, forecast under-delivers 20% | over-hedge 24 | −10% | (2.4) MTM + delivery gap |

### Policy Limits & Governance
| Limit                | Setting (illustrative) |
|----------------------|------------------------|
| Max aggregate notional | 400 |
| Max tenor            | 24 months |
| Permitted instruments| Forwards, swaps, vanilla options, collars |
| Counterparty limit   | ≤ 40% of book per bank; min rating [grade] |
| MTM reporting        | Monthly to treasury committee |
| Approval authority   | <50: treasurer; ≥50: CFO; ≥150: board |

### Residual Risks Disclosed
- Forecast/volume risk on the unhedged forecast portion.
- Basis risk: hedge index vs. exposure index mismatch.
- Counterparty credit risk; rollover/timing risk.

**Disconfirming check:** Re-run residual at trailing-high adverse move and with forecast exposure 20% short; confirm the program still fits risk appetite.
```

---

## Verification

- [ ] Exposure quantified net of natural offsets; committed vs forecast separated.
- [ ] Hedge ratio set with a tenor-layering schedule (declining ratio further out).
- [ ] Instrument selection justified per layer with cost/protection/flexibility tradeoff.
- [ ] Residual risk computed per scenario (base + adverse moves) using stated formulas.
- [ ] Policy limits and approval authorities defined.
- [ ] Over-hedge and adverse-market stress cases run; counterparty concentration noted.
- [ ] Hedge-accounting (ASC 815 / IFRS 9) flagged and routed to accounting.
- [ ] Market data sourced and dated; nothing fabricated.

---

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Hedging 100% of forecast exposure | Layer by certainty; near-committed high, far-forecast low; over-hedge stress required |
| Claiming a hedge eliminates risk | Disclose basis, forecast, counterparty, rollover risk explicitly |
| Inventing forward points / swap rates / vols | Use only sourced, dated market data |
| Hedge ratio justified by a market view | Policy must be appetite-driven, not directional |
| Fabricating hedge-accounting treatment | Route ASC 815 / IFRS 9 to accounting; do not state effectiveness conclusions |
| Ignoring counterparty concentration | Per-bank limit in policy; flag if one bank dominates the book |
