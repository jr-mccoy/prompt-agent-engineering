---
title: "Earnings Preview Builder — Expectations, Key Metrics, Scenarios, Stock Reaction"
category: finance/investing-research
description: "Build a pre-earnings setup: consensus and buy-side whisper expectations, the metrics that matter most, line-item scenarios, the implied move, and a map of what would move the stock up or down — with every number traced to a source."
techniques:
  - NE-11
  - DS-02
  - NE-10
  - QA-01
  - DT-02
difficulty: intermediate
tags:
  - earnings-preview
  - expectations
  - key-metrics
  - implied-move
  - scenario-analysis
  - setup
updated: "2026-06-08"
related_prompts:
  - domain-finance/investing-research/finance_earnings_review_analyzer.md
  - domain-finance/investing-research/finance_catalyst_map_builder.md
  - domain-finance/investing-research/finance_investment_thesis_builder.md
  - domain-finance/field_guide.md
---

*For informational purposes only. Not financial, investment, or tax advice.*

## Objective

Build a disciplined pre-earnings setup that answers four questions: (1) what is the market expecting (consensus, and where the buy-side bar is set above/below it), (2) which metrics will actually drive the reaction, (3) what the realistic beat/in-line/miss scenarios look like line by line, and (4) what specific outcomes would move the stock and by roughly how much. The goal is to separate the *expectations game* from the *fundamentals*, so a beat that disappoints and a miss that rallies are both anticipated.

## When to Use

- Setting up a position into a print (hold/add/trim/hedge decision)
- Deciding whether the risk/reward into earnings is favorable given the implied move
- Building an investment-committee pre-earnings note
- Calibrating a model's forecast against the published consensus before the event
- Defining in advance which data points will confirm or break the thesis

## Inputs / Context Required

**Event context**
- Company, ticker, report date/time (before/after market), current price
- Fiscal period being reported and reporting currency

**Expectations**
- Consensus estimates (revenue, EPS, key segment/KPI lines) with source — or "consensus not supplied"
- Any sense of the buy-side "whisper" or where the bar sits vs. consensus
- The options-implied move for the event, if available (or ATM straddle pricing)

**Fundamental inputs**
- The 3–5 KPIs that matter most for this company and why (e.g., net adds, same-store sales, bookings, gross margin)
- The user's own model estimates for the key lines, if any
- Guidance previously given for this quarter and full year
- Recent data points (channel checks, high-frequency data, peer prints) bearing on the quarter

## Constraints

### Must
- Distinguish consensus from the buy-side bar (whisper) explicitly; a beat vs. consensus that misses the whisper is a miss to the stock (DT-02).
- Specify each key metric precisely: definition, period, and source (DS-02).
- Provide beat / in-line / miss scenarios at the line-item level with internally consistent assumptions (NE-10).
- State the options-implied move and compare it to the scenario-implied dispersion (NE-11).
- Pre-commit which data points would confirm or break the thesis (QA-01).
- Trace every estimate to a source; flag user/model estimates as `[ASSUMED]` where not from consensus.

### Must Not
- Invent consensus numbers, whisper figures, or implied-move data. Mark gaps `[ASSUMED]` or "not supplied."
- Predict the actual result or the direction of the stock move as a certainty.
- Treat a headline beat/miss as the driver without addressing guidance and the expectations bar.
- Ignore the role of guidance and forward commentary, which often dominate the reaction.

## Instructions

1. **Set the expectations frame.** Tabulate consensus for the key lines and, where supplied, the buy-side bar. State where the whisper sits relative to consensus and the implied "real" hurdle.

2. **Identify the metrics that move the stock (DT-02).** Rank the 3–5 KPIs by their expected influence on the reaction. For each, give the precise definition, the consensus/expected level, and why it matters this quarter.

3. **Quantify the implied move (NE-11).**
```
Options-implied move ≈ (ATM straddle premium) / (Current price)
Historical avg absolute move = mean(|move| over last N prints)
```
   Compare the implied move to the scenario dispersion built in Step 4. If scenario dispersion > implied move, the event may be underpriced; if smaller, overpriced — state the caveat that implied move reflects positioning and risk premium, not just fundamentals.

4. **Build line-item scenarios (NE-10).** For revenue, EPS, the key KPI, and guidance, build beat / in-line / miss columns with internally consistent assumptions (don't pair a revenue beat with an unexplained margin collapse).

5. **Map the reaction function.** For each scenario, state the plausible stock-reaction direction and rough magnitude band, explicitly noting the guidance/commentary that could override the headline (e.g., "headline beat + cut guide → likely down").

6. **Define confirm/break data points (QA-01).** List the specific observations in the print that would confirm or disconfirm the standing thesis, so the post-print review is fast and unbiased.

7. **State the setup conclusion.** Given the implied move, the asymmetry of scenarios, and the thesis, give a pre-earnings stance (hold into / trim into / hedge into / add into / no position) with the rationale.

## Output Format

```
## EARNINGS PREVIEW: [Company] ([Ticker]) | [Fiscal Period] | Reports [date, BMO/AMC]
## Price: [$] | Implied move: [±%]
```

### Expectations Frame
| Line | Consensus | Buy-side bar / whisper | Our estimate | Source |
|---|---|---|---|---|
| Revenue | | | | |
| EPS | | | | |
| [Key KPI] | | | | |
| Guidance (next Q / FY) | | | | |

### Metrics That Move the Stock
| Rank | Metric | Definition | Expected level | Why it matters this quarter |
|---|---|---|---|---|

### Implied Move
```
Options-implied move ≈ Straddle / Price = [±%]
Historical avg |move| (last N prints) = [±%]
Scenario dispersion (bull−bear) = [±%]   → [under/over-priced caveat]
```

### Line-Item Scenarios
| Line | Miss | In-line | Beat |
|---|---|---|---|
| Revenue | | | |
| EPS | | | |
| [Key KPI] | | | |
| Guidance | | | |

### Reaction Map
| Scenario | Headline | Guidance / commentary | Plausible reaction |
|---|---|---|---|
| Beat + raise | | | likely [+x%] |
| Beat + cut | | | could be [−x%] |
| In-line | | | |
| Miss + reassure | | | |
| Miss + cut | | | |

### Confirm / Break Data Points
- **Would confirm thesis:** …
- **Would break thesis:** …

### Setup Conclusion
**[HOLD / TRIM / HEDGE / ADD / NO POSITION] into the print** — [rationale tied to implied move, asymmetry, and thesis]

## Verification

- [ ] Consensus is distinguished from the buy-side bar/whisper where supplied.
- [ ] Each key metric has a precise definition, period, and source.
- [ ] The options-implied move is stated and compared to scenario dispersion.
- [ ] Scenarios are internally consistent across revenue, margin, EPS, and guidance.
- [ ] The reaction map accounts for guidance overriding the headline.
- [ ] Confirm/break data points are defined before the print.
- [ ] All estimates trace to a source; model estimates are `[ASSUMED]`-flagged.
- [ ] No actual result or stock direction is asserted as certain.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Treating a consensus beat as a guaranteed up-move | Distinguish the whisper/bar; map beat-and-cut scenarios |
| Inventing consensus or whisper numbers | Mark unsupplied figures `[ASSUMED]`/"not supplied"; never fabricate |
| Ignoring guidance in favor of the headline | Reaction map requires a guidance/commentary column |
| Predicting the result or move with false confidence | Output is scenarios with reaction bands, not a forecast |
| Confusing implied move with fundamental expectation | State that implied move embeds positioning and risk premium, not just fundamentals |
| Imprecise KPI definitions causing post-print confusion | Each metric specified with definition, period, and source upfront |
| Recency bias from the last data point | Require multiple inputs (peer prints, guidance, channel data) before scenario weights |
