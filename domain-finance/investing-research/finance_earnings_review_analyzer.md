---
title: "Earnings Review Analyzer — Beat/Miss Attribution, Guidance Read-Through, Thesis Impact"
category: finance/investing-research
description: "Post-print analysis: attribute the beat or miss to its real drivers, read through the guidance and forward commentary, separate quality from optics, and update the standing thesis with explicit confirm/break verdicts."
techniques:
  - NE-11
  - DS-02
  - QA-01
  - DS-04
  - AG-08
difficulty: intermediate
tags:
  - earnings-review
  - beat-miss-attribution
  - guidance
  - thesis-update
  - earnings-quality
  - post-print
updated: "2026-06-08"
related_prompts:
  - domain-finance/investing-research/finance_earnings_preview_builder.md
  - domain-finance/investing-research/finance_10k_10q_teardown.md
  - domain-finance/investing-research/finance_investment_thesis_builder.md
  - domain-finance/field_guide.md
---

*For informational purposes only. Not financial, investment, or tax advice.*

## Objective

Analyze a reported quarter to determine: (1) what actually drove the beat or miss versus consensus and versus the pre-print setup, (2) what the guidance and management commentary imply for forward estimates, (3) whether the result was high- or low-quality (operating vs. one-time, accrual vs. cash), and (4) how the standing investment thesis should change — confirmed, broken, or modified. The output ties the print back to the pre-earnings preview's confirm/break data points so the verdict is disciplined rather than reactive.

## When to Use

- Immediately after a print to decide hold/add/trim/exit
- Updating the model and thesis with the new data
- Reconciling a counterintuitive stock reaction (beat that fell, miss that rallied)
- Writing a post-earnings note for an investment committee
- Comparing the actual result to the pre-print preview to grade the setup

## Inputs / Context Required

**The result**
- Press release / earnings tables: revenue, EPS (GAAP and adjusted), key KPIs, segment detail
- Consensus that was in place and, if available, the pre-print preview / setup
- Guidance issued (next quarter and/or full year) and prior guidance for comparison
- Reporting currency and period

**Context**
- The earnings-call transcript or key management commentary, if available
- The standing thesis and its pre-defined confirm/break data points
- The stock's reaction (price move) if known
- Recent peer prints for read-across

## Constraints

### Must
- Attribute the beat/miss to specific drivers (volume, price/mix, FX, margin, tax, buyback, one-time items), each quantified or marked `[NOT DISCLOSED]` (NE-11, DS-02).
- Separate operating beats from optical beats (lower tax rate, share count, reserve release) (DS-04).
- Read guidance through to forward estimates: state the direction and rough magnitude of revisions implied (QA-01).
- Render an explicit thesis verdict: confirmed / broken / modified, tied to the pre-defined data points (AG-08).
- Reconcile a counterintuitive reaction (beat-down / miss-up) when it occurs.
- Trace every number to the release/transcript; flag estimates `[ASSUMED]`.

### Must Not
- Invent figures, guidance, or transcript quotes not provided. Mark gaps `[NOT DISCLOSED]`.
- Treat a headline beat as thesis confirmation without attribution and quality assessment.
- Confuse the stock's reaction with the fundamental verdict; analyze both but keep them distinct.
- Anchor the new estimate to the old one without incorporating the guidance read-through.

## Instructions

1. **Tabulate actual vs. expected.** For each key line, show actual, consensus, the pre-print setup (if supplied), and the surprise.
```
Surprise vs. consensus = (Actual − Consensus) / |Consensus|
EPS surprise decomposition: revenue Δ → operating margin Δ → below-the-line Δ (tax, interest, share count)
```

2. **Attribute the beat/miss (NE-11, DS-02).** Decompose the surprise into operating drivers (volume, price/mix, FX, margin) and non-operating/optical drivers (tax rate, buyback, one-time gains, reserve release). Quantify each to the extent disclosed.

3. **Grade earnings quality (DS-04).** Assess whether the beat is durable:
```
Quality flags: adjusted-EPS add-backs that recur; tax-rate benefit; below-consensus capex sustaining margins;
   CFO lagging net income; revenue pulled forward; reserve releases.
```
   Compare net income to operating cash flow if disclosed.

4. **Read the guidance through (QA-01).** Compare new guidance to prior guidance and to consensus. State whether forward estimates likely move up, down, or hold, and roughly how much. Note any change in segment mix, margin trajectory, or capital-allocation plan.

5. **Reconcile the reaction (if known).** If the stock moved against the headline, explain why (guidance, quality, positioning, whisper vs. consensus).

6. **Update the thesis (AG-08).** Compare the result against the pre-defined confirm/break data points and render: **Confirmed / Broken / Modified**. State which specific data points were hit and what changed in the variant view.

7. **Recommend action.** Conclude with hold / add / trim / exit and the rationale, plus what to watch next quarter.

## Output Format

```
## EARNINGS REVIEW: [Company] ([Ticker]) | [Fiscal Period] | Reported [date]
## Reaction: [±%, if known]
```

### Actual vs. Expected
| Line | Actual | Consensus | Pre-print setup | Surprise |
|---|---|---|---|---|
| Revenue | | | | [%] |
| Adj. EPS | | | | [%] |
| GAAP EPS | | | | |
| [Key KPI] | | | | |
| Guidance (next Q / FY) | | (prior) | | |

### Beat/Miss Attribution
| Driver | Operating? | Contribution | Disclosed? |
|---|---|---|---|
| Volume | Yes | | |
| Price / mix | Yes | | |
| FX | — | | |
| Margin | Yes | | |
| Tax rate | No (optical) | | |
| Buyback / share count | No (optical) | | |
| One-time / reserve | No | | |

```
Surprise vs. consensus = (Actual − Consensus)/|Consensus| = [%]
Operating share of surprise = [%]   Optical share = [%]
```

### Earnings Quality
| Quality flag | Present? | Notes |
|---|---|---|
| Recurring adj. add-backs | | |
| Tax-rate benefit | | |
| CFO lagging net income | | |
| Pulled-forward revenue | | |
| Reserve release | | |

### Guidance Read-Through
| Metric | Prior guide | New guide | Consensus | Implied revision |
|---|---|---|---|---|

### Reaction Reconciliation (if applicable)
[Why the stock moved as it did relative to the headline]

### Thesis Verdict
**[CONFIRMED / BROKEN / MODIFIED]**
| Pre-defined data point | Result | Hit? |
|---|---|---|
| [confirm point] | | |
| [break point] | | |
- **What changed in the variant view:** …

### Action
**[HOLD / ADD / TRIM / EXIT]** — [rationale] | **Watch next quarter:** …

## Verification

- [ ] Actuals are shown against consensus and the pre-print setup with computed surprises.
- [ ] The beat/miss is decomposed into operating vs. optical drivers, each quantified or `[NOT DISCLOSED]`.
- [ ] Earnings quality is assessed (add-backs, tax, CFO vs. NI, pull-forwards, reserves).
- [ ] Guidance is compared to prior guidance and consensus, with implied revisions stated.
- [ ] A counterintuitive reaction is reconciled when present.
- [ ] The thesis verdict maps to the pre-defined confirm/break data points.
- [ ] All figures trace to the release/transcript; estimates flagged `[ASSUMED]`.
- [ ] Stock reaction and fundamental verdict are analyzed separately.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Calling a headline beat a thesis win | Require attribution and quality grading before any verdict |
| Treating an optical beat as operating strength | Separate tax/buyback/reserve drivers from operating drivers explicitly |
| Anchoring new estimates to old ones | Guidance read-through must drive the forward revision |
| Inventing guidance or transcript quotes | Mark `[NOT DISCLOSED]`; never fabricate management language |
| Confusing the stock move with the fundamentals | Reaction and fundamental verdict reported in separate sections |
| Recency bias from one strong/weak quarter | Quality flags and multi-driver attribution prevent single-quarter overreaction |
| Confirmation bias updating the thesis | Verdict tied to pre-committed confirm/break points, not post-hoc rationalization |
