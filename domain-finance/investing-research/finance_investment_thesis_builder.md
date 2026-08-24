---
title: "Investment Thesis Builder — Variant View, Catalysts, Valuation, Risk, Exit Criteria"
category: finance/investing-research
description: "Construct a falsifiable long (or long-bias) investment thesis with an explicit variant view vs. consensus, dated catalysts, a valuation range, ranked risks, exit criteria, and a pre-committed disconfirming-evidence test."
techniques:
  - RT-05
  - NE-10
  - QA-02
  - AG-08
  - DS-02
difficulty: advanced
tags:
  - investment-thesis
  - variant-view
  - catalysts
  - valuation
  - risk-management
  - exit-criteria
updated: "2026-06-08"
related_prompts:
  - domain-finance/investing-research/finance_bull_bear_debate_memo.md
  - domain-finance/investing-research/finance_catalyst_map_builder.md
  - domain-finance/investing-research/finance_position_sizing_framework.md
  - domain-finance/field_guide.md
---

*For informational purposes only. Not financial, investment, or tax advice. All outputs require independent verification before any capital is committed.*

## Objective

Build a complete, falsifiable investment thesis that states what you believe, why it differs from the market's view (the variant view), what specific dated events will close the gap (catalysts), what the security is worth across scenarios (valuation range), what could break it (ranked risks), and the pre-committed conditions under which you would exit or admit error. The thesis must be testable: a neutral reader should be able to identify exactly which future observations would confirm or disconfirm it.

## When to Use

- Initiating a new long position and needing a written, accountable rationale
- Converting a screen hit or qualitative interest into a structured, defensible case
- Memorializing the entry logic so future review can separate thesis-being-wrong from variance
- Preparing a pitch for an investment committee or partner review
- Re-underwriting an existing position after a material event

## Inputs / Context Required

**Security & coverage context**
- Company name, ticker, exchange; sector and primary business lines
- Current price, shares outstanding (diluted), market cap, enterprise value
- Time horizon for the thesis (e.g., 12–36 months) and base currency

**The claim**
- One-sentence thesis statement (what you believe and the expected return path)
- The consensus / market-implied view you are betting against (sell-side estimates, implied growth, current multiple)

**Evidence base**
- Financial history (≥3 years preferred) and any forward estimates with their source
- Industry/competitive context, unit economics, and the key operating drivers
- Named primary sources: filings, transcripts, channel data, expert calls (cite each)

**Catalyst & risk inputs**
- Known dated events (earnings, product launches, regulatory decisions, capital allocation)
- Known risk factors, prior failure modes, and any short interest / sentiment data

## Constraints

### Must
- State the variant view explicitly: name the consensus number/multiple and your differing number/multiple, with the magnitude of the gap (RT-05).
- Present valuation as a base/bull/bear range with internally consistent assumptions, never a single point (NE-10).
- Attach a probability and an estimated price/value impact to each catalyst.
- Define exit criteria *before* entry: price targets, time stops, and thesis-violation triggers.
- Specify the single disconfirming observation that would most cheaply prove the thesis wrong, and commit to tracking it (QA-02, AG-08).
- Trace every quantitative claim to a stated input or named source; flag estimates as `[ASSUMED]`.

### Must Not
- Invent financials, consensus estimates, short interest, or third-party data. If missing, mark `[ASSUMED]` and state the basis.
- Present a thesis that no realistic observation could falsify (unfalsifiable narrative).
- Let the bull case set both the upside and the downside (anchoring/confirmation bias) — the bear case must be argued in good faith.
- Conflate "the stock went up" with "the thesis was right," or "it went down" with "the thesis was wrong."

## Instructions

1. **State the thesis in one sentence**, then expand to a 3–5 sentence summary: the mispricing, the mechanism that corrects it, and the expected return path.

2. **Articulate the variant view.** Identify what the market currently prices in (cite the consensus estimate, implied growth, or current multiple) and state precisely where and why your view differs.
   ```
   Variant gap = Your estimate − Consensus estimate
   Implied upside if you are right = (Your fair value − Current price) / Current price
   ```
   If you cannot name a specific number you disagree with, you do not yet have a variant view — say so.

3. **Lay out the evidence chain (RT-05).** For each pillar of the thesis, give the claim, the supporting evidence, and the source. Distinguish facts (filed/observed) from inferences (your interpretation) from assumptions (`[ASSUMED]`).

4. **Build the valuation range (NE-10).** Estimate fair value under bear/base/bull, holding assumptions internally consistent across each column.
   ```
   Expected value (EV) = Σ (Probability_i × Fair value_i)
   Upside/Downside skew = (Bull − Current) / (Current − Bear)
   ```
   Defer detailed mechanics to a dedicated DCF/comps prompt; here, state the method, the 2–3 swing assumptions, and the resulting range.

5. **Map dated catalysts.** List each catalyst with its date/window, probability of occurring, and estimated value impact.
   ```
   Probability-weighted catalyst impact = Σ (P(catalyst_i) × Δvalue_i)
   ```

6. **Rank the risks (DS-06 logic).** Order risks by (probability × severity). For each, note the leading indicator that would signal it materializing.

7. **Define exit criteria up front.** Specify: (a) price/value target to trim or exit on success, (b) time stop if the thesis hasn't progressed, (c) thesis-violation trigger that forces a re-underwrite regardless of price.

8. **Pre-commit the disconfirming test (QA-02).** Name the single cheapest observation that would most damage the thesis, and where/when you will look for it. State what you would do if you see it.

9. **Decision gate (AG-08).** Conclude with a go / watch / pass recommendation justified by the evidence gathered, the skew, and whether the variant view is genuinely differentiated.

## Output Format

```
## INVESTMENT THESIS: [Company] ([Ticker]) | Horizon: [X months] | As of [date]
```

### Thesis Summary
- **One-liner:** [single sentence]
- **Mechanism:** [how the mispricing corrects]
- **Expected return path:** [base-case % over horizon]

### Variant View
| Dimension | Consensus / Market-Implied | Our View | Gap | Source |
|---|---|---|---|---|
| [e.g., FY+1 revenue growth] | [%] | [%] | [±pp] | [source] |
| [e.g., terminal margin] | [%] | [%] | [±pp] | [source] |
| [e.g., exit multiple] | [x] | [x] | [±x] | [source] |

### Evidence Chain
| Pillar | Claim | Evidence | Type (Fact / Inference / `[ASSUMED]`) | Source |
|---|---|---|---|---|
| 1 | ... | ... | ... | ... |
| 2 | ... | ... | ... | ... |

### Valuation Range
| | Bear | Base | Bull |
|---|---|---|---|
| Probability | [%] | [%] | [%] |
| Swing assumption 1 | | | |
| Swing assumption 2 | | | |
| Fair value / share | | | |
| Implied return vs. current | | | |

- **Probability-weighted fair value:** [$]
- **Upside/Downside skew:** [x : 1]

### Catalyst Map
| Catalyst | Date / Window | P(occur) | Est. value impact | Notes |
|---|---|---|---|---|
| ... | ... | [%] | [±%] | ... |
- **Probability-weighted catalyst impact:** [±%]

### Ranked Risks
| Rank | Risk | P × Severity | Leading indicator | Mitigant |
|---|---|---|---|---|
| 1 | ... | High/Med/Low | ... | ... |

### Exit Criteria (pre-committed)
- **Success target:** [price/value action]
- **Time stop:** [date/condition]
- **Thesis-violation trigger:** [specific observation forcing re-underwrite]

### Disconfirming Test
- **Cheapest falsifier:** [the one observation]
- **Where/when tracked:** [data source, cadence]
- **Action if observed:** [response]

### Decision
**[GO / WATCH / PASS]** — [2–3 sentence justification grounded in skew, variant differentiation, and evidence quality]

## Verification

- [ ] The thesis is stated as a falsifiable claim with a named consensus view it disagrees with.
- [ ] The variant gap is quantified (a specific number vs. a specific number).
- [ ] Valuation is a bear/base/bull range with internally consistent assumptions, not a point estimate.
- [ ] Every catalyst has a date/window, probability, and impact estimate.
- [ ] Risks are ranked by probability × severity, each with a leading indicator.
- [ ] Exit criteria (success, time, thesis-violation) are defined before entry.
- [ ] A single cheapest disconfirming observation is named and assigned a tracking source.
- [ ] All numbers trace to a stated input or named source; estimates are `[ASSUMED]`-flagged.
- [ ] The bear case is argued in good faith, not as a strawman.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Presenting a narrative with no variant view as a "thesis" | Require a named consensus number and a quantified gap; if absent, downgrade to "watch" |
| Unfalsifiable thesis that no evidence could disprove | Mandatory single cheapest disconfirming observation with a tracking source |
| Confirmation bias (only supporting evidence collected) | Evidence chain must label inferences and assumptions; bear case argued in good faith |
| Anchoring on current price as fair value | Valuation derived independently; skew computed vs. range, not vs. price alone |
| Treating a stock move as thesis validation | Exit criteria separate price action from thesis-violation triggers |
| Precision illusion from a single fair-value number | Output is a probability-weighted range with explicit skew |
| Recency bias from latest quarter | Evidence base requires multi-year/full-cycle context, not just the last print |
