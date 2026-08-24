---
title: "Sector Rotation Framework — Cycle-Based Positioning with Regime Indicators"
category: finance/markets-macro
description: "Build a business-cycle-based sector-rotation framework that ties named regime indicators to cycle phases, maps historical sector leadership tendencies (with caveats), and produces an evidence-based tilt — without asserting current data or treating historical patterns as guarantees."
techniques:
  - RT-06
  - NE-10
  - DS-04
  - QA-02
  - QA-04
difficulty: intermediate
tags:
  - sector-rotation
  - business-cycle
  - regime
  - factor
  - positioning
updated: "2026-06-08"
related_prompts:
  - domain-finance/markets-macro/finance_macro_indicator_dashboard_interpreter.md
  - domain-finance/markets-macro/finance_economic_scenario_modeler.md
  - domain-finance/investing-research/finance_portfolio_construction_review.md
  - domain-finance/field_guide.md
---

**Informational only — not investment advice. Sector leadership patterns are historical tendencies, not guarantees; all current data is user-supplied and outputs require professional review.**

## Objective

Construct a disciplined sector-rotation framework that (1) defines the cycle phase from named, user-supplied regime indicators, (2) maps the historical sector/factor leadership tendency for that phase with explicit caveats, (3) reconciles the historical playbook with current divergences, and (4) produces an evidence-based, scenario-aware sector tilt — guarding against the assumption that past rotation patterns will repeat.

## When to Use

- Setting or reviewing sector tilts in a portfolio against the macro backdrop
- Translating a cycle-phase read into actionable over/underweights
- Building a repeatable, indicator-driven rotation discipline (vs. narrative-driven)
- Stress-testing a sector bet against the possibility the historical pattern breaks
- Briefing an allocation committee with an evidence trail

## Inputs / Context Required

```
<rotation_inputs>
Market / universe: (e.g., US large-cap GICS sectors) | Currency | As-of date
Benchmark: (e.g., S&P 500 sector weights)

REGIME INDICATORS — USER MUST SUPPLY current readings (value, trend, source, date):
  - Growth: PMI / LEI / GDP nowcast
  - Inflation: CPI/PCE trend, breakevens
  - Policy: policy rate direction, curve slope (2s10s/3m10y)
  - Credit/conditions: HY spreads, financial conditions index
  - Profit cycle: earnings revisions breadth (if available)
  - Risk appetite: volatility regime, cyclical-vs-defensive relative performance (if available)

CONSTRAINTS:
  - Tracking-error / active-weight limits per sector (if any)
  - Sectors that are off-limits or capped
  - Existing sector weights vs. benchmark
QUESTION (optional): __________
</rotation_inputs>
```

If regime indicators are not supplied, request them. Do not assert current macro readings or recent sector returns from memory.

## Constraints

### Must
- Use only user-supplied current indicator readings; restate with source/date.
- Define the cycle phase from the indicators (RT-06), not from a market narrative.
- Present sector/factor leadership tendencies as historical, regime-conditional patterns (DS-04) — with explicit "tendency, not guarantee" caveats.
- Reconcile the historical playbook against current divergences before recommending a tilt.
- Provide tilts across scenarios (NE-10): base phase + the adjacent phase if the cycle turns.
- Respect any user active-weight/tracking-error constraints.
- Apply guardrails for recency bias, regime-blindness, and pattern-overfitting; require a disconfirming check (QA-04).
- Stress-test the tilt (QA-02): what regime shift breaks it?

### Must Not
- Assert current sector returns, indicator values, or "what's working" from memory.
- Present historical rotation patterns as deterministic ("late cycle ⇒ energy outperforms").
- Recommend a tilt without an evidence trail from indicator → phase → tendency → reconciliation.
- Ignore current divergences that contradict the textbook phase playbook.
- Exceed stated active-weight limits.

## Instructions

**Step 1 — Restate regime indicators.** Tabulate user inputs with direction and source/date.

**Step 2 — Determine the cycle phase (RT-06).** Combine indicators into a phase read with confidence:

```
Phase signals (illustrative composite logic — weigh leading indicators):
  Early expansion : growth turning up, easy policy, steep curve, spreads tightening, low rates
  Mid expansion   : growth solid, policy neutralizing, spreads stable, earnings breadth positive
  Late expansion  : growth strong but slowing-at-margin, tight policy, flat/inverting curve, inflation elevated
  Slowdown        : growth decelerating, policy peaking/easing-soon, spreads widening
  Contraction     : growth negative, policy easing, spreads wide, risk-off
  Early recovery  : growth troughing, policy very easy, spreads peaking then tightening
```

**Step 3 — Map the historical leadership tendency (DS-04, with caveats).**

```
Stylized cycle-rotation tendencies (HISTORICAL, NOT GUARANTEES — confounded by regime, valuation, idiosyncratics):
  Early expansion : cyclicals, financials, consumer discretionary, small caps, value
  Mid expansion   : technology, industrials, broad participation
  Late expansion  : energy, materials, inflation beneficiaries; quality begins to lead
  Slowdown        : defensives (staples, healthcare, utilities), quality, low-vol
  Contraction     : defensives, long-duration safe assets, cash
  Early recovery  : cyclicals, financials, small caps, value re-rate
State that valuation, rates, and structural shifts can override these tendencies.
```

**Step 4 — Reconcile with current divergences.** Where current sector behavior or valuations contradict the playbook, name the divergence and decide whether to follow the pattern, fade it, or stay neutral — with reasoning.

**Step 5 — Build scenario-aware tilts (NE-10).** For the base phase and the likely next phase, set sector over/underweights within active-weight limits.

**Step 6 — Stress-test & bias guardrails (QA-02 / QA-04).** What cycle turn or rate move breaks the tilt? Apply recency-bias, regime-blindness, and overfitting checks; state one disconfirming indicator to monitor.

## Output Format

### Regime Indicators (user-supplied)

| Indicator | Reading | Direction | Source / date |
|---|---|---|---|

### Cycle-Phase Read

- **Phase:** [chosen] | **Confidence:** [H/M/L] | **Biggest uncertainty:** [one line]

### Historical Leadership Tendency (caveated)

| Phase | Tendency over/underweight | Caveat |
|---|---|---|

### Current-Divergence Reconciliation

| Playbook expectation | Current observation | Decision (follow/fade/neutral) | Reasoning |
|---|---|---|---|

### Recommended Tilts (scenario-aware)

| Sector | Benchmark wt | Base-phase tilt | Next-phase tilt | Active wt vs. limit | Rationale |
|---|---|---|---|---|---|

### Stress-Test & Monitoring
[Regime turn that breaks the tilt; recency/regime/overfitting checks; disconfirming indicator]

## Verification

- [ ] All current indicator readings are user-supplied with source/date.
- [ ] Cycle phase derived from indicators, not narrative; confidence stated.
- [ ] Leadership tendencies labeled historical and regime-conditional with caveats.
- [ ] Current divergences explicitly reconciled before tilts are set.
- [ ] Tilts respect stated active-weight/tracking-error limits.
- [ ] Tilts given for base phase and the likely next phase.
- [ ] Recency-bias, regime-blindness, and overfitting guardrails applied with a disconfirming monitor.
- [ ] Evidence trail runs indicator → phase → tendency → reconciliation → tilt.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Treating rotation patterns as deterministic rules | Label as historical tendencies; require reconciliation against current data; valuation/rates can override |
| Asserting "what's working now" from memory | Current returns/indicators are user inputs with source/date |
| Overfitting to the last cycle | Apply overfitting and regime-blindness checks; note structural shifts (e.g., sector composition changes) |
| Recommending tilts without an evidence trail | Output must show indicator → phase → tendency → reconciliation → tilt |
| Ignoring contradicting current data | Divergence reconciliation table is mandatory; cannot follow the playbook silently |
| Breaching mandate limits | Active weights checked against stated tracking-error/limit inputs |
