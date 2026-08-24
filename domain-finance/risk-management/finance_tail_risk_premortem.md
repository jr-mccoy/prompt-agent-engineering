---
title: "Tail-Risk / Black-Swan Pre-Mortem — Position, Portfolio, or Plan"
category: finance/risk-management
description: "Run a structured pre-mortem on the tail: assume the position, portfolio, or plan has suffered a catastrophic loss, work backward to the chains that could cause it, and design early-warning tripwires and mitigations — explicitly countering tail-risk blindness and normalcy bias."
techniques:
  - QA-02
  - NE-10
  - RT-03
  - QA-01
  - CM-01
difficulty: intermediate
tags:
  - tail-risk
  - black-swan
  - pre-mortem
  - fat-tails
  - tripwires
  - stress-testing
updated: "2026-06-08"
related_prompts:
  - domain-finance/risk-management/finance_stress_test_scenario_design.md
  - domain-finance/risk-management/finance_market_risk_var_stress.md
  - domain-finance/risk-management/finance_enterprise_risk_register.md
  - domain-finance/field_guide.md
---

*For informational purposes only. Not financial, investment, or risk-management advice. Tail scenarios are illustrative, not predictive; review with qualified professionals.*

## Objective

Run a pre-mortem focused on the tail: assume the position, portfolio, or plan has already produced a catastrophic loss, then reason backward to the causal chains that could produce it — including the low-probability, high-impact and "unknown-unknown-adjacent" paths that standard VaR and base-case analysis miss. Output the dominant loss chains, early-warning tripwires, and mitigations, with explicit naming and countering of tail-risk blindness, normalcy/recency bias, and over-reliance on thin-tailed models.

## When to Use

- Before sizing or committing to a concentrated position or leveraged strategy
- Pressure-testing a portfolio whose risk metrics look benign
- Stress-testing a business plan or capital deployment against ruin
- Complementing VaR (which understates the tail) with scenario reasoning
- Designing early-warning tripwires and contingency plans for rare, severe events

## Inputs / Context Required

- **Subject:** The position, portfolio, or plan, its size, leverage, and time horizon.
- **Exposures & dependencies:** Concentrations, leverage, funding/liquidity reliance, key counterparties, correlated holdings, and operational single points of failure.
- **Assumptions:** The load-bearing assumptions the subject relies on (liquidity available, correlations stable, counterparty solvent, market open).
- **Loss threshold:** What level of loss counts as "catastrophic" / ruinous (e.g., breaches capital, covenant, or survival).
- **History/analogues:** Relevant past tail events, if any. State if none.
- **Existing safeguards:** Stops, hedges, diversification, liquidity buffers already in place.

## Constraints

### Must
- Begin from the assumed catastrophe (the pre-mortem frame), not from the base case.
- Enumerate multiple distinct loss chains, including ones that depend on correlations migrating to 1 and liquidity vanishing.
- Name the bias pitfalls explicitly: tail-risk blindness, normalcy/recency bias, survivorship (only surviving strategies are studied), and precision-illusion from thin-tailed models.
- Distinguish what is knowable-but-ignored from genuine unknown-unknowns, and address each differently (tripwires vs. resilience/optionality).
- Attach an early-warning tripwire to each major loss chain with a defined threshold and pre-committed action.
- Frame severity qualitatively where probabilities are unknowable; do not assign false-precision odds.

### Must Not
- Invent probabilities for tail events; treat them as plausible-and-severe, not as calibrated odds.
- Dismiss a chain because it "hasn't happened" — absence of precedent is not evidence of impossibility.
- Rely on the same distributional assumptions (normality) that hide the tail.
- Present mitigations that only work if the benign assumptions hold.
- Reduce the analysis to a single worst case; tails are a family of chains.

## Instructions

1. **Set the catastrophe frame (QA-02).** State: "It is [future date]. This [position/portfolio/plan] has suffered a loss of [≥ catastrophic threshold]. What happened?" Reason backward from the failure.
2. **Decompose into loss chains (NE-10).** Enumerate distinct paths to the catastrophe. Cover at minimum:
   - **Market tail:** an outsized move in the primary driver beyond modeled bounds.
   - **Correlation breakdown:** diversifiers move together; the hedge fails when needed (CM-01).
   - **Liquidity evaporation:** cannot exit at modeled prices; forced selling at gaps.
   - **Leverage/funding:** margin calls, facility withdrawal, refinancing failure.
   - **Counterparty/operational:** a key counterparty defaults or a single point of failure breaks.
   - **Reflexive/second-order:** the act of de-risking worsens the move (crowded exit).
3. **Identify load-bearing assumptions (QA-01).** For each chain, name the assumption whose violation enables it, and how plausible the violation is.
4. **Separate knowable from unknown-unknown.** For knowable-but-ignored risks, design tripwires. For genuine unknown-unknowns, prescribe resilience: lower leverage, liquidity buffers, position-size caps, optionality.
5. **Design tripwires (RT-03).** For each major chain, define a leading indicator and a threshold that pre-commits an action before the loss compounds.
   ```
   Tripwire example: if [driver] moves > X% in Y days OR funding spread > Zbp
                     → reduce position by N% / activate hedge / raise liquidity
   ```
6. **Mitigation design.** Map mitigations to chains: hedges (with their own basis/counterparty residual), diversification (that survives correlation migration), liquidity buffers, leverage limits, and contingency playbooks.
7. **Disconfirming / survivorship check.** Ask what comparable strategies blew up historically and why their risk looked fine beforehand. Confirm the analysis would have flagged those, not just the survivors.
8. **Synthesize.** Rank loss chains by severity and by how cheaply they can be defended; state the residual ruin risk that cannot be economically hedged.

## Output Format

### Catastrophe Frame
> It is [date]. [Subject] has lost [threshold]. Working backward…

### Loss Chains
| # | Loss chain (backward narrative) | Enabling assumption violated | Plausibility (qual.) | Severity (qual.) | Defendable cheaply? |
|---|---|---|---|---|---|
| 1 | Market tail … | modeled bounds hold | | | |
| 2 | Correlation breakdown … | diversification holds | | | |
| 3 | Liquidity evaporation … | exit at modeled price | | | |
| 4 | Funding/leverage … | facility available | | | |
| 5 | Counterparty/operational … | counterparty solvent | | | |
| 6 | Reflexive/crowded exit … | independent actors | | | |

### Knowable vs. Unknown-Unknown
| Risk | Type | Treatment (tripwire vs. resilience) |
|---|---|---|

### Tripwires
| Chain | Leading indicator | Threshold | Pre-committed action | Owner |
|---|---|---|---|---|

### Mitigation Map
| Chain | Mitigation | Residual after mitigation |
|---|---|---|

### Survivorship Check & Residual Ruin
[Comparable blow-ups and why they looked safe; the residual ruin risk that cannot be economically hedged.]

## Verification

- [ ] The analysis starts from an assumed catastrophe, not the base case.
- [ ] Multiple distinct loss chains are enumerated, including correlation breakdown and liquidity evaporation.
- [ ] Tail-risk blindness, normalcy/recency, and survivorship biases are named and countered.
- [ ] Knowable risks get tripwires; genuine unknown-unknowns get resilience/optionality.
- [ ] Each major chain has a tripwire with a threshold and pre-committed action.
- [ ] No false-precision probabilities are assigned to tail events; severity framed qualitatively.
- [ ] Thin-tailed (normality) assumptions are not relied upon to dismiss chains.
- [ ] The survivorship check tests whether comparable historical blow-ups would have been flagged.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| "It hasn't happened, so it won't" | Absence of precedent explicitly rejected as evidence of safety |
| Assigning precise odds to black swans | Severity framed qualitatively; no false-precision probabilities |
| VaR/normality hiding the tail | Analysis reasons from scenarios, not the modeled distribution; correlation→1 and liquidity gaps modeled |
| Single worst case mistaken for the tail | Tails treated as a family of distinct chains, each with its own tripwire |
| Mitigations that need benign assumptions | Mitigations stress-tested against the very assumptions whose failure causes the loss |
| Studying only survivors | Survivorship check requires examining comparable blow-ups and their pre-event risk picture |
| Tripwire with no committed action | Each tripwire pre-commits a specific action and owner before compounding |
