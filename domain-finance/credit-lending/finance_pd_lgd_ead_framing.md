---
title: "PD / LGD / EAD Framing — Expected-Loss Methodology and Input Sourcing"
category: finance/credit-lending
description: "Frame the inputs and logic for expected-loss estimation — Probability of Default, Loss Given Default, Exposure at Default — emphasizing methodology, data sourcing, and assumption transparency; never inventing probabilities or recovery rates."
techniques:
  - NE-11
  - QA-04
  - DS-02
  - RT-05
  - AG-02
difficulty: advanced
tags:
  - expected-loss
  - pd
  - lgd
  - ead
  - credit-risk
  - ifrs9-cecl
updated: "2026-06-08"
related_prompts:
  - domain-finance/credit-lending/finance_five_cs_credit_analysis.md
  - domain-finance/credit-lending/finance_watchlist_early_warning.md
  - domain-finance/credit-lending/finance_workout_restructuring_options.md
  - domain-finance/field_guide.md
---

*For informational purposes only. Not financial, credit, or regulatory advice. Expected-loss estimates and model parameters must be developed and validated by qualified risk-modeling professionals under the applicable accounting and regulatory framework.*

## Objective

Frame the inputs and reasoning for expected-loss (EL) estimation across its three components — Probability of Default (PD), Loss Given Default (LGD), and Exposure at Default (EAD) — by structuring the methodology, the data each parameter requires, the assumptions and their sources, and the EL arithmetic. This prompt produces a methodology and input scaffold; it does not invent PD, LGD, recovery rates, or regulatory thresholds. The user supplies or sources the parameters; the model enforces transparency and consistency.

## When to Use

- Setting up an expected-loss estimate for a single exposure or a small portfolio
- Documenting the methodology and assumptions behind a credit reserve or pricing input
- Reviewing a counterparty's EL logic for internal consistency
- Preparing IFRS 9 / CECL ECL methodology framing (point-in-time vs. through-the-cycle, staging)
- Educating on how PD/LGD/EAD combine, without asserting specific values

## Inputs / Context Required

Provide as much as available; missing parameters are flagged, not invented.

**PD inputs**
- Internal rating / scorecard output, or external rating mapping the user supplies
- PD source: internal model, agency master scale, market-implied (CDS/spread), or scorecard — state which
- Horizon (1-year vs. lifetime), point-in-time vs. through-the-cycle basis

**LGD inputs**
- Collateral type and value, advance/recovery rates, lien position, seniority
- Recovery data source (internal history, external study, or assumption) — state which
- Cost-of-recovery and time-to-recovery / discount rate

**EAD inputs**
- Current drawn balance, undrawn commitment, credit conversion factor (CCF) assumption
- Amortization, expected utilization at default

**Framework**
- Accounting / regulatory framework (IFRS 9 ECL, CECL, Basel IRB) and its specific requirements — verify against current regulations as of [date]
- Reporting currency

## Constraints

### Must
- Treat PD, LGD, and EAD as user-sourced parameters; the model frames methodology and checks consistency, not values (AG-02 skeptical of supplied values' provenance).
- For every parameter, require and record its source and basis (NE-11): internal model / external study / market-implied / `[ASSUMED]`.
- Show the EL arithmetic explicitly and the units (PD as probability, LGD and EAD as defined).
- Cross-validate (QA-04) that PD basis, LGD basis, and EAD basis are mutually consistent (e.g., lifetime PD pairs with lifetime EAD profile).
- Present EL under base / downside / severe parameter scenarios (RT-05) using stated stress logic, not invented numbers.
- State the framework and flag "verify against current regulations as of [date]."

### Must Not
- Invent or estimate a specific PD, LGD, recovery rate, or CCF when the user has not supplied or sourced it — flag `[REQUIRED INPUT — not supplied]`.
- Assert a regulatory threshold, staging trigger, or capital weight as fact.
- Map an internal rating to an agency PD without a user-supplied mapping.
- Mix point-in-time and through-the-cycle PDs without flagging the inconsistency.
- Present EL as a precise figure that implies the parameters are observed rather than estimated.

## Instructions

1. **State the framework and horizon.** Confirm IFRS 9 ECL / CECL / Basel IRB context, the PD horizon (1-year vs. lifetime), and the PIT/TTC basis. Note "verify against current regulations as of [date]."

2. **Source the PD.** Record the PD value, its source, and basis. If not supplied, flag as required input. Methodology notes:
```
PD = probability the obligor defaults over the stated horizon (0 <= PD <= 1)
Sources: internal rating model | scorecard | agency master scale (user mapping) | market-implied
Market-implied (approx, illustrative methodology only):
   PD_approx ≈ CDS spread / (1 - LGD)    [state assumptions; do not plug invented spreads]
```

3. **Source the LGD.** Build LGD from recovery logic, all user-supplied:
```
LGD = 1 - Recovery Rate
Recovery Rate = (Recoveries - Recovery Costs) / EAD, discounted to default date
   discounted recovery = Σ Recovery_t / (1 + d)^t
Sources: internal recovery history | external recovery study | collateral-based estimate
```
For secured exposures, tie LGD to collateral value, advance rate, and liquidation discount the user provides.

4. **Source the EAD.** Combine drawn and undrawn exposure:
```
EAD = Drawn Balance + CCF x Undrawn Commitment
CCF = credit conversion factor (user-supplied or framework-prescribed; flag if assumed)
```

5. **Compute expected loss.**
```
EL = PD x LGD x EAD
```
Show the arithmetic with each parameter's source annotated.

6. **Consistency cross-check.** Confirm horizons and bases align (lifetime PD with lifetime EAD/LGD; PIT vs TTC consistent). Flag any mismatch.

7. **Scenario framing.** Present EL under base / downside / severe by stressing the parameters per a stated rule (e.g., downside applies a stated PD multiple and an LGD haircut to recoveries). The stress logic is stated; the stressed values remain user-driven or clearly `[ASSUMED]`.

## Output Format

### Parameter Register
| Parameter | Value | Source / Basis | Horizon / Basis | Flag |
|---|---|---|---|---|
| PD | [value or REQUIRED] | internal/agency/market/[ASSUMED] | 1-yr / lifetime, PIT/TTC | |
| Recovery Rate | [value or REQUIRED] | history/study/collateral | discounted? | |
| LGD = 1 - RR | [value] | derived | | |
| Drawn Balance | $ | reported | | |
| Undrawn Commitment | $ | reported | | |
| CCF | [value or REQUIRED] | framework/[ASSUMED] | | |
| EAD = Drawn + CCF x Undrawn | $ | derived | | |

### Expected Loss Arithmetic
```
EAD = Drawn + CCF x Undrawn = $X
LGD = 1 - Recovery Rate     = X%
PD  = [value, source]       = X%
EL  = PD x LGD x EAD        = $X
```

### Consistency Cross-Check
- [ ] PD horizon matches EAD/LGD horizon
- [ ] PIT/TTC basis consistent across parameters
- [ ] LGD discounting and recovery costs applied
- [ ] CCF basis stated (framework or assumed)

### EL Scenario Framing (base / downside / severe)
| Parameter | Base | Downside | Severe | Stress Rule |
|---|---|---|---|---|
| PD | X% | X% | X% | [stated multiple] |
| LGD | X% | X% | X% | [recovery haircut] |
| EAD | $X | $X | $X | [utilization shift] |
| **EL** | **$X** | **$X** | **$X** | |

### Methodology & Framework Notes
[Framework: IFRS 9 / CECL / Basel IRB. Staging logic, PIT/TTC, "verify against current regulations as of [date]". Sources of every parameter.]

## Verification

- [ ] Every parameter has a recorded source/basis or is flagged `[REQUIRED INPUT]` / `[ASSUMED]`.
- [ ] No PD, LGD, recovery rate, or CCF was invented.
- [ ] EL arithmetic (PD x LGD x EAD) is shown with units and parameter sources.
- [ ] PD horizon and PIT/TTC basis are consistent with LGD and EAD.
- [ ] LGD reflects discounted, cost-adjusted recoveries.
- [ ] EAD combines drawn and CCF-weighted undrawn exposure.
- [ ] Scenario stress rules are stated; stressed values are user-driven or `[ASSUMED]`.
- [ ] Framework named with "verify against current regulations as of [date]."

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Inventing a PD or recovery rate to complete the math | Unsupplied parameters flagged `[REQUIRED INPUT]`; not estimated |
| Presenting EL as an observed, precise figure | EL labeled an estimate; parameters' sources and uncertainty disclosed |
| Mapping internal rating to agency PD without a mapping | Mapping must be user-supplied; otherwise flagged |
| Mixing PIT and TTC PDs | Consistency cross-check flags basis mismatch |
| Ignoring recovery costs / time value in LGD | LGD requires discounted, cost-adjusted recoveries |
| Asserting a regulatory capital weight or staging trigger | Framework requirements flagged "verify against current regulations as of [date]" |
| Treating undrawn as zero exposure | EAD includes CCF-weighted undrawn commitment |
