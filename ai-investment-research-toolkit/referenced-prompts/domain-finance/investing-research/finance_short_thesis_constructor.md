---
title: "Short Thesis Constructor — Catalyst, Borrow/Squeeze Risk, Asymmetry"
category: finance/investing-research
description: "Construct a disciplined short thesis: the specific flaw and dated catalyst, an honest borrow-cost and squeeze-risk assessment, the bounded-upside/unbounded-loss asymmetry, and the cover criteria that limit damage when wrong."
techniques:
  - RT-05
  - NE-10
  - QA-02
  - AG-02
  - AG-08
difficulty: advanced
tags:
  - short-selling
  - short-thesis
  - borrow-cost
  - short-squeeze
  - asymmetry
  - catalyst
updated: "2026-06-08"
related_prompts:
  - domain-finance/investing-research/finance_bull_bear_debate_memo.md
  - domain-finance/investing-research/finance_competitive_moat_analyzer.md
  - domain-finance/investing-research/finance_position_sizing_framework.md
  - domain-finance/field_guide.md
---

*For informational purposes only. Not financial, investment, or tax advice. Short selling carries theoretically unbounded loss and unique mechanical risks; this prompt does not recommend any short position.*

## Objective

Construct a rigorous short thesis that survives the structural disadvantages of shorting. It requires: (1) a specific, evidenced flaw (fraud, structural decline, broken model, untenable valuation, looming dilution/refinancing), (2) a dated or windowed catalyst that forces recognition, (3) an honest borrow-cost and short-squeeze assessment, (4) an explicit asymmetry analysis acknowledging bounded gains and unbounded losses, and (5) pre-committed cover/stop criteria. The default stance is skeptical of the short itself: most shorts fail because timing, borrow, and squeeze risk are underestimated.

## When to Use

- Building a standalone short or the short leg of a pair/hedge
- Pressure-testing a "this is overvalued" instinct against the mechanics of shorting
- Assessing whether a known short candidate is actionable now or a value trap on the short side
- Preparing a short pitch with the risk factors a committee will demand

## Inputs / Context Required

**Security & mechanics**
- Company, ticker, current price, market cap, average daily volume
- Short interest (% of float), days-to-cover, current borrow rate/availability — or "not supplied"
- Float characteristics: insider/strategic ownership, index inclusion, recent issuance

**The flaw**
- The specific thesis: fraud / structural decline / broken unit economics / untenable valuation / dilution or refinancing wall
- Evidence for the flaw with named sources (filings, accounting analysis, channel data)
- Consensus view and current expectations being bet against

**Catalyst & risk**
- The dated/windowed catalyst that forces recognition (covenant breach, refinancing, earnings, guidance cut, regulatory action)
- Known squeeze risks (high short interest, low float, retail attention, potential buyout)
- The user's horizon and risk tolerance / max loss limit

## Constraints

### Must
- Adopt a skeptical default toward the short itself; state the strongest reason NOT to be short (AG-02).
- Require a specific, evidenced flaw and a dated/windowed catalyst — "overvalued" alone is not a short thesis (RT-05).
- Assess borrow cost and squeeze risk explicitly and quantify the carry drag (NE-11 logic embedded).
- Analyze asymmetry honestly: bounded gain (to zero) vs. unbounded loss, and the effect of the position growing as it moves against you (NE-10, QA-02).
- Define cover/stop criteria up front (AG-08).
- Trace evidence to named sources; flag estimates `[ASSUMED]`.

### Must Not
- Present a valuation-only short without a catalyst (the market can stay irrational longer than you stay solvent).
- Ignore or understate borrow cost, recall risk, or squeeze dynamics.
- Treat the maximum gain (stock to zero) as the expected outcome.
- Invent short interest, borrow rates, or float data. Mark `[ASSUMED]`/"not supplied."
- Assert fraud without specific, sourced evidence.

## Instructions

1. **State the flaw and grade the evidence (RT-05).** Name the thesis type (fraud / structural decline / broken model / valuation / dilution-refinancing). For each pillar, give evidence and source, graded Hard fact / Inference / `[ASSUMED]`.

2. **Steel-man the long (AG-02).** Before building the short, state the strongest bull case and the single best reason not to be short. A short that cannot survive the bull case is not ready.

3. **Identify the catalyst (timing).**
```
A short needs a clock. List the catalyst, its date/window, and what it forces the market to recognize.
No catalyst → flag as "value trap risk on the short side"; require a borrow-cost carry test before proceeding.
```

4. **Assess borrow and squeeze risk.**
```
Annual carry drag = Borrow rate (annualized) + dividend obligation (if any)
Squeeze risk indicators: short interest % of float, days-to-cover (SI / ADV),
   low/locked-up float, index/buyout candidacy, retail/social attention.
```
   State whether borrow is general-collateral or hard-to-borrow, and the recall risk.

5. **Analyze asymmetry honestly (NE-10, QA-02).**
```
Max gain = (Entry − 0) / Entry = up to 100% (rarely realized)
Loss is unbounded; position SIZE grows as price rises (anti-Kelly mechanics).
Scenario payoff: bear (thesis works) / base (partial) / squeeze (thesis right, wrong time).
Expected value must net out borrow carry and squeeze tail.
```

6. **Define cover/stop criteria (AG-08).** Pre-commit: price/valuation level to cover on success; hard stop or loss limit; time stop if the catalyst slips; and a thesis-violation trigger (the flaw turns out wrong).

7. **Decide (AG-08).** Conclude short / pass / watch, with the rationale tied to evidence quality, catalyst proximity, carry, squeeze risk, and asymmetry.

## Output Format

```
## SHORT THESIS: [Company] ([Ticker]) | Price [$] | SI [%] | Borrow [%] | DTC [x]
```

### The Flaw
- **Thesis type:** [fraud / structural decline / broken model / valuation / dilution-refinancing]
| Pillar | Evidence | Type (Hard / Inference / `[ASSUMED]`) | Source |
|---|---|---|---|

### Steel-Man the Long
- **Strongest bull case:** …
- **Best reason NOT to be short:** …

### Catalyst
| Catalyst | Date / window | Forces recognition of | Confidence |
|---|---|---|---|
- **If no catalyst:** [value-trap-on-short flag + carry test]

### Borrow & Squeeze Risk
```
Annual carry drag = Borrow rate + dividend = [%]
Days-to-cover = Short interest / ADV = [x]
Short interest = [% of float]   Float quality = [ ]
Squeeze indicators: [list]
```

### Asymmetry
| Scenario | Probability | Stock outcome | Position P&L | Notes |
|---|---|---|---|---|
| Thesis works (bear) | | | | |
| Partial (base) | | | | |
| Squeeze / wrong-time | | | | |
```
Max gain ≈ 100% (rarely realized); loss unbounded; size grows against you
E[return] (net of carry) = Σ (P_i × P&L_i) − carry = [ ]
```

### Cover / Stop Criteria (pre-committed)
- **Cover on success:** [level]
- **Hard stop / loss limit:** [level]
- **Time stop:** [date/condition]
- **Thesis-violation trigger:** …

### Decision
**[SHORT / PASS / WATCH]** — [rationale tied to evidence, catalyst, carry, squeeze, asymmetry]

## Verification

- [ ] A specific, evidenced flaw is named and graded; "overvalued" alone is not accepted.
- [ ] The strongest bull case and the best reason not to be short are stated.
- [ ] A dated/windowed catalyst is identified, or the value-trap risk is flagged with a carry test.
- [ ] Borrow cost (carry drag) and days-to-cover are quantified.
- [ ] Squeeze risk indicators are listed and assessed.
- [ ] Asymmetry analysis acknowledges bounded gain, unbounded loss, and position growth against you.
- [ ] Cover/stop/time/thesis-violation criteria are pre-committed.
- [ ] No invented short interest, borrow, or float data; estimates `[ASSUMED]`-flagged.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Valuation-only short with no catalyst | Catalyst is required; absence triggers a value-trap flag and carry test |
| Understating borrow cost and recall risk | Carry drag quantified; hard-to-borrow and recall risk stated explicitly |
| Ignoring squeeze dynamics | Days-to-cover, SI %, float quality, and squeeze indicators are mandatory |
| Treating stock-to-zero as the expected outcome | Asymmetry table assigns probabilities; max gain shown as rarely realized |
| Forgetting that losers grow into the portfolio | Anti-Kelly mechanics named; loss limit and stop required |
| Asserting fraud without sourced evidence | Fraud pillars require Hard-fact-grade sourcing; inference labeled as such |
| Optimism/confirmation bias on the short | Skeptical default (AG-02): steel-man the long before building the short |
