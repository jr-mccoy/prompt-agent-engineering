---
title: "Bull/Bear Debate Memo — Opposing-Analyst Structure with Decision Synthesis"
category: finance/investing-research
description: "Produce a balanced bull/bear investment memo by running two opposing analyst personas in good faith, scoring each side's strongest arguments, and synthesizing a probability-weighted decision with the key swing factors."
techniques:
  - RP-03
  - RT-05
  - NE-10
  - QA-02
  - AG-08
difficulty: intermediate
tags:
  - bull-bear
  - debate
  - investment-memo
  - decision-synthesis
  - devil's-advocate
  - balanced-analysis
updated: "2026-06-08"
related_prompts:
  - domain-finance/investing-research/finance_investment_thesis_builder.md
  - domain-finance/investing-research/finance_short_thesis_constructor.md
  - domain-finance/investing-research/finance_catalyst_map_builder.md
  - domain-finance/field_guide.md
---

*For informational purposes only. Not financial, investment, or tax advice.*

## Objective

Generate a structured bull/bear memo by instantiating two opposing analyst personas — a Bull and a Bear — each making the strongest honest case for its side, then a neutral Chair who scores the exchange, identifies the genuine swing factors, and renders a probability-weighted decision. The goal is to surface the best argument on both sides and isolate what actually decides the call, not to manufacture false balance.

## When to Use

- Pressure-testing a draft thesis before committing capital or pitching it
- Resolving internal disagreement on a name by formalizing both sides
- Surfacing hidden assumptions that the primary analyst is too close to see
- Preparing a two-sided investment-committee memo
- Re-examining a consensus name where you suspect groupthink

## Inputs / Context Required

**Security context**
- Company, ticker, current price, market cap / EV, sector
- Time horizon and base currency

**Starting material**
- Any existing thesis, model output, or analyst notes (optional but preferred)
- Consensus estimates and current valuation multiple, if available
- Known catalysts, risks, and recent news flow

**Calibration**
- The 3–5 questions the user most wants the debate to resolve (optional)
- Any constraints (e.g., long-only mandate, no leverage, ESG screens)

## Constraints

### Must
- Run the Bull and Bear as distinct personas, each arguing in good faith and presenting its strongest case (RP-03).
- Require each side to anchor claims to evidence and named sources, not assertion (RT-05).
- Have each side directly rebut the other's two strongest points (cross-examination).
- Express the conclusion as a probability range, not a binary, with the swing factors that would shift it (NE-10).
- Identify the single point on which the two sides most disagree and what evidence would resolve it (QA-02).
- Render a decision gate at the end justified by the scored exchange (AG-08).

### Must Not
- Build a strawman bear (or bull) so the preferred side wins by default.
- Invent financials, estimates, short interest, or sources; flag missing data as `[ASSUMED]`.
- Declare a winner without naming the swing factor that drove the call.
- Collapse genuine uncertainty into false confidence.

## Instructions

1. **Frame the question.** Restate the security, horizon, and the specific decision at stake (initiate / add / hold / trim / avoid). List the 3–5 questions the debate must resolve.

2. **Bull persona — opening case.** As a conviction-long analyst, present the strongest bull argument: the thesis, the variant view, 3–5 supporting pillars each with evidence and source, the upside scenario, and the catalysts that realize it.

3. **Bear persona — opening case.** As a skeptical short/avoid analyst, present the strongest bear argument: the broken assumption, the downside drivers, 3–5 pillars with evidence and source, and the catalysts or risks that realize the downside.

4. **Cross-examination.** Each side rebuts the other's two strongest points directly. Force concessions where a point is well-made; do not let either side ignore a strong rebuttal.

5. **Chair scoring.** As a neutral Chair, score each pillar on (a) evidence quality and (b) materiality to the outcome.
   ```
   Pillar weight = Evidence quality (1–5) × Materiality (1–5)
   Side score   = Σ pillar weights, net of conceded points
   ```

6. **Isolate the swing factor (QA-02).** Identify the single question on which the sides most disagree and that most moves the outcome. State what observable evidence would resolve it.

7. **Probability-weighted synthesis (NE-10).** Assign probabilities to bull/base/bear outcomes and compute the expected return.
   ```
   E[return] = Σ (P_outcome × Return_outcome)
   Skew = (Bull return) / |Bear return|
   ```

8. **Decision (AG-08).** Conclude with initiate / add / hold / trim / avoid, justified by the score, the swing factor, and the skew. State the conditions that would flip the call.

## Output Format

```
## BULL/BEAR MEMO: [Company] ([Ticker]) | Horizon: [X mo] | As of [date]
## Decision at stake: [initiate / add / hold / trim / avoid]
```

### Questions to Resolve
1. ... 2. ... 3. ...

### Bull Case (opening)
| Pillar | Claim | Evidence | Source | Type (Fact/Inference/`[ASSUMED]`) |
|---|---|---|---|---|
| 1 | ... | ... | ... | ... |
- **Upside scenario:** [target & path]

### Bear Case (opening)
| Pillar | Claim | Evidence | Source | Type |
|---|---|---|---|---|
| 1 | ... | ... | ... | ... |
- **Downside scenario:** [target & path]

### Cross-Examination
- **Bull rebuts Bear:** [responses to Bear's two strongest points; concessions noted]
- **Bear rebuts Bull:** [responses to Bull's two strongest points; concessions noted]

### Chair Scorecard
| Side | Pillar | Evidence (1–5) | Materiality (1–5) | Weight | Conceded? |
|---|---|---|---|---|---|
| Bull | 1 | | | | |
| Bear | 1 | | | | |
- **Bull total:** [score] | **Bear total:** [score]

### Swing Factor
- **The decisive disagreement:** [the one question]
- **Resolving evidence:** [what observation settles it, and where to find it]

### Probability-Weighted Synthesis
| Outcome | Probability | Return | Contribution |
|---|---|---|---|
| Bull | [%] | [%] | [%] |
| Base | [%] | [%] | [%] |
| Bear | [%] | [%] | [%] |
- **E[return]:** [%] | **Skew:** [x : 1]

### Decision
**[INITIATE / ADD / HOLD / TRIM / AVOID]** — [justification tied to score, swing factor, and skew]
- **Would flip if:** [conditions]

## Verification

- [ ] Both Bull and Bear present their strongest honest case; neither is a strawman.
- [ ] Every pillar is anchored to evidence with a named source or `[ASSUMED]` flag.
- [ ] Each side directly rebuts the other's two strongest points, with concessions noted.
- [ ] The Chair scorecard applies evidence × materiality weighting transparently.
- [ ] The single decisive swing factor is named with resolving evidence.
- [ ] The synthesis is probability-weighted with an explicit skew, not a binary verdict.
- [ ] The decision states the conditions that would flip it.
- [ ] No financials, estimates, or sources are invented.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Strawman on the disfavored side producing false balance | Both personas must present strongest case; Chair penalizes weak/uncharitable arguments |
| Declaring a winner without naming why | Decision must cite the swing factor and the scorecard |
| Manufactured certainty from a close debate | Output is probability-weighted; near-even scores must be reported as such |
| Confirmation bias toward the pre-existing view | Personas argue independently; Chair scores evidence, not the house view |
| Invented short interest or estimates to strengthen a side | Missing data flagged `[ASSUMED]`; unsourced claims down-weighted |
| Treating debate eloquence as evidence | Materiality and evidence-quality scored separately from rhetorical strength |
