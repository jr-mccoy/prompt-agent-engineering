---
title: "Stress-Test Scenario Design — Severe-but-Plausible, Internally Consistent"
category: finance/risk-management
description: "Design coherent stress scenarios across macro and idiosyncratic drivers — calibrated to severe-but-plausible severity, internally consistent across correlated variables, and narrated with a triggering storyline — for use in market, credit, liquidity, and capital stress programs."
techniques:
  - NE-10
  - RT-03
  - QA-02
  - CM-01
  - QA-04
difficulty: advanced
tags:
  - stress-testing
  - scenario-design
  - severe-but-plausible
  - reverse-stress
  - macro-shocks
  - capital
updated: "2026-06-08"
related_prompts:
  - domain-finance/risk-management/finance_market_risk_var_stress.md
  - domain-finance/risk-management/finance_liquidity_risk_analysis.md
  - domain-finance/risk-management/finance_tail_risk_premortem.md
  - domain-finance/field_guide.md
---

*For informational purposes only. Not financial, investment, or risk-management advice. Scenario severity and calibration must be reviewed by qualified risk professionals.*

## Objective

Design a set of stress scenarios that are (1) **severe-but-plausible** — beyond base case but anchored to historical or coherent forward analogues, (2) **internally consistent** — correlated drivers move together in economically sensible directions and magnitudes, and (3) **narrated** — each scenario has a triggering storyline and a transmission path to the portfolio. Produce base / adverse / severe scenario specifications plus an optional reverse-stress scenario that solves for what breaks the entity.

## When to Use

- Building scenarios for market, credit, liquidity, capital, or enterprise stress tests
- Designing the shock set that feeds VaR-complement, IRRBB, or ALM analyses
- Board / regulatory stress narratives requiring defensible severity calibration
- Reverse stress testing: finding the scenario that renders the business unviable
- Challenging an existing scenario library for coherence and severity gaps

## Inputs / Context Required

- **Exposure profile:** What the entity/portfolio is sensitive to (rates, equities, FX, credit spreads, commodities, real estate, funding, key counterparties, key customers).
- **Risk drivers:** The macro and idiosyncratic variables that matter; their current levels.
- **Historical analogues:** Reference episodes the user considers relevant (e.g., a named crisis window) — for severity anchoring. State if none.
- **Severity intent:** How severe (e.g., 1-in-X years, regulatory-prescribed, or "worse than base by N").
- **Correlation/transmission views:** Known linkages between drivers (or accept reasoned defaults, flagged).
- **Output use:** Which downstream model consumes the scenario (so shocks are expressed in the needed units).

## Constraints

### Must
- Calibrate each scenario to a stated severity basis (historical analogue, statistical quantile, or prescribed) — never an unanchored guess.
- Enforce internal consistency: co-moving drivers move in coherent directions and proportionate magnitudes (CM-01).
- Provide a narrative trigger and transmission path for each scenario, not just a shock vector.
- Produce a graded set: base / adverse / severe-but-plausible (NE-10), each more severe than the last on the key dimensions.
- Express shocks in units the downstream model needs (bp, %, $, multiples).
- Distinguish systematic (market-wide) from idiosyncratic (entity-specific) shocks and show how they combine.

### Must Not
- Invent historical figures, correlations, or "1-in-X" probabilities; mark assumed calibration `[ASSUMED]` and state its basis.
- Produce internally inconsistent scenarios (e.g., equities crash while credit spreads tighten and unemployment falls — without explicit justification).
- Set severity so mild it cannot break anything, or so extreme it is dismissed as implausible.
- Treat correlations as fixed; severe scenarios should allow correlations to migrate (often toward 1) and say so.
- Omit the transmission story — a shock vector with no mechanism is not a scenario.

## Instructions

1. **Map drivers to exposures (NE-10).** List the risk drivers the portfolio is sensitive to and the direction of harmful moves for each.
2. **Set the severity anchor (QA-04).** For each scenario tier, state the calibration basis:
   ```
   Severity anchors (choose & state):
     · Historical replay: magnitude of a named past episode
     · Statistical: a stated quantile move of the driver (e.g., −Xσ)
     · Prescribed: regulator/board-mandated shock
   Mark any number not sourced as [ASSUMED] with its rationale.
   ```
3. **Write the narrative trigger (CM-01).** For each scenario, draft a plausible storyline: what initiates it, how it propagates, over what horizon. The narrative disciplines the shock magnitudes.
4. **Specify co-moving shocks consistently.** Build the full driver vector so variables move together coherently (e.g., a recession scenario: equities ↓, credit spreads ↑, unemployment ↑, rates path per central-bank reaction, defaults ↑). Document each linkage.
5. **Grade the set.** Produce base, adverse, and severe-but-plausible versions where severity escalates monotonically on the key dimensions. Avoid a severe scenario that is merely "adverse ×2" with no mechanism change.
6. **Allow correlation migration.** In the severe tier, shift correlations toward co-movement (diversification fails in crises) and state the new assumed correlations.
7. **Transmit to the portfolio (RT-03).** For each scenario, trace the path to the portfolio's P&L / EVE / liquidity / capital and express the expected directional impact (quantification happens in the consuming model).
8. **Reverse-stress option (QA-02).** Solve the inverse: what combination of moves drives the entity below a survival threshold (capital, liquidity, covenant)? Identify the minimal scenario that breaks it.
9. **Disconfirming / plausibility check.** Name the bias pitfalls — disaster myopia / recency (only modeling recent crises), and survivorship (excluding scenarios that wiped out comparable firms). Confirm each scenario is severe enough to matter and plausible enough to be taken seriously.

## Output Format

### Driver–Exposure Map
| Driver | Current level | Harmful direction | Exposure / sensitivity |
|---|---|---|---|

### Scenario Specifications (base / adverse / severe)
| Driver | Base | Adverse | Severe-but-plausible | Unit | Calibration basis |
|---|---|---|---|---|---|
| Equity index | | | | % | [historical/quantile/prescribed] |
| Credit spreads | | | | bp | |
| Policy rate | | | | bp | |
| Unemployment | | | | pp | |
| FX (key pair) | | | | % | |
| Key counterparty default | | | | — | |

### Scenario Narratives
- **Adverse:** [trigger → transmission → horizon]
- **Severe-but-plausible:** [trigger → transmission → correlation migration → horizon]

### Correlation Treatment
| Pair | Base correlation | Severe-scenario correlation | Rationale |
|---|---|---|---|

### Reverse-Stress Scenario
| Survival threshold | Breaking combination of moves | Plausibility note |
|---|---|---|

### Transmission to Portfolio
| Scenario | Market impact | Credit impact | Liquidity impact | Capital impact (direction) |
|---|---|---|---|---|

## Verification

- [ ] Each scenario tier states an explicit severity calibration basis.
- [ ] Co-moving drivers are internally consistent in direction and magnitude; linkages documented.
- [ ] Every scenario has a narrative trigger and transmission path.
- [ ] The set is graded base → adverse → severe with monotonic escalation on key dimensions.
- [ ] Severe tier allows correlations to migrate toward co-movement, with stated values.
- [ ] Systematic vs. idiosyncratic shocks are distinguished and combined.
- [ ] No historical figures, correlations, or probabilities are invented; assumed ones `[ASSUMED]` with rationale.
- [ ] A reverse-stress scenario identifies what breaks the entity.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Unanchored severity guesses | Each tier cites a calibration basis (historical/statistical/prescribed); assumed values flagged |
| Internally inconsistent shocks | Co-moving drivers must move coherently; contradictory moves require explicit justification |
| Shock vector with no mechanism | Narrative trigger and transmission path mandatory per scenario |
| Correlations held fixed in a crisis | Severe tier migrates correlations toward 1 and states them |
| Disaster myopia (only recent crises) | Bias named; require analogues beyond the most recent episode |
| Scenario too mild to break anything | Reverse stress identifies the breaking point; severe tier must approach it |
| Implausibly extreme scenario dismissed | Plausibility check anchors severity to coherent, narratable storylines |
