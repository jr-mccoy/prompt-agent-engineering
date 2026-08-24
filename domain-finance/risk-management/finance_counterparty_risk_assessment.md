---
title: "Counterparty / Credit-Exposure Assessment — Concentration and Netting"
category: finance/risk-management
description: "Assess counterparty credit risk through current and potential future exposure, netting and collateral, expected loss, and portfolio concentration — quantifying how netting sets and wrong-way risk change the exposure without inventing ratings or default probabilities."
techniques:
  - RT-02
  - NE-11
  - DS-06
  - QA-04
  - QA-01
difficulty: intermediate
tags:
  - counterparty-risk
  - credit-exposure
  - netting
  - concentration
  - expected-loss
  - wrong-way-risk
updated: "2026-06-08"
related_prompts:
  - domain-finance/risk-management/finance_hedging_strategy_designer.md
  - domain-finance/risk-management/finance_enterprise_risk_register.md
  - domain-finance/credit-lending/finance_credit_risk_assessment.md
  - domain-finance/field_guide.md
---

*For informational purposes only. Not financial, credit, or risk-management advice. Ratings, PDs, and netting enforceability must be verified by qualified professionals against current data and jurisdiction.*

## Objective

Assess counterparty credit risk across a set of exposures by quantifying: (1) **current exposure** and **potential future exposure (PFE)** per counterparty, (2) the effect of **netting sets** and **collateral** on exposure, (3) **expected loss** given user-supplied default-probability and recovery inputs, and (4) **portfolio concentration** (single-name, sector, geography) and **wrong-way risk**. Netting and collateral are applied only where enforceability is confirmed. No ratings, PDs, or recoveries are invented.

## When to Use

- Reviewing counterparty exposure for a trading book, treasury, or lending portfolio
- Pre-trade or pre-onboarding counterparty risk assessment and limit-setting
- Monitoring concentration against single-name and sector limits
- Evaluating the exposure-reduction benefit of netting agreements and collateral (CSA)
- Building the counterparty-risk leg of an enterprise risk register

## Inputs / Context Required

- **Counterparties:** Names/IDs, exposure type (derivatives, repo, receivables, deposits, loans).
- **Exposure data:** Mark-to-market values, notionals, and add-on/PFE inputs or a method to estimate PFE.
- **Netting & collateral:** Master agreements (ISDA/GMRA) and enforceability by jurisdiction; CSA terms (threshold, MTA, collateral held), state confirmation status.
- **Credit inputs:** User-supplied PD (rating-implied or internal), LGD/recovery, and EAD. State sources.
- **Limits:** Single-name, sector, geography, tenor limits.
- **Correlation/wrong-way signals:** Any link between counterparty default likelihood and the exposure size (wrong-way risk).

## Constraints

### Must
- Compute exposure per counterparty as current exposure and PFE; show formulas.
- Apply netting only within enforceable netting sets and collateral only where the CSA/agreement is confirmed; state enforceability.
- Compute expected loss using the standard decomposition; show inputs and sources.
- Measure concentration by single name, sector, and geography against stated limits.
- Identify wrong-way risk where exposure rises as counterparty credit deteriorates.
- State the basis/source for every PD, LGD, and rating; mark assumed ones `[ASSUMED]`.

### Must Not
- Invent credit ratings, default probabilities, recoveries, or collateral values; gaps are `[ASSUMED]` and excluded from definitive conclusions.
- Apply netting benefit across counterparties or across unenforceable jurisdictions.
- Treat collateral as risk-free or instantly liquid; apply haircuts and consider wrong-way collateral.
- Net positive and negative exposures outside a legally enforceable netting set.
- Ignore concentration because individual exposures are within limit (aggregate may breach).

## Instructions

1. **Map exposures (DS-06).** For each counterparty, list exposures, current mark-to-market, and notional. Group into legally enforceable netting sets.
2. **Compute current exposure.**
   ```
   Gross current exposure (per trade) = max(MtM, 0)
   Netted current exposure (per set)  = max( Σ MtM_within_set , 0 )   [enforceable netting only]
   Net of collateral                   = max( Netted exposure − Collateral (post-haircut) , 0 )
   ```
3. **Estimate potential future exposure (PFE, NE-11).** Add a PFE add-on for future market moves over the horizon (user method or supplied add-on factors):
   ```
   EAD ≈ Net current exposure + PFE add-on
   ```
   State that PFE depends on volatility/horizon assumptions supplied by the user.
4. **Compute expected loss (QA-04).**
   ```
   Expected Loss (EL) = PD × LGD × EAD
     LGD = 1 − Recovery rate
   ```
   Show PD, LGD, EAD and their sources per counterparty.
5. **Quantify the netting/collateral benefit.** Show gross vs. netted vs. collateralized exposure to evidence the risk reduction — and flag where enforceability is unconfirmed (benefit not counted).
6. **Measure concentration (RT-02).**
   ```
   Single-name concentration = EAD_counterparty / total EAD
   Sector / geography concentration = Σ EAD_group / total EAD
   ```
   Compare to limits; flag aggregate breaches even when individual lines comply.
7. **Identify wrong-way risk (QA-01).** Flag counterparties where exposure increases as their credit worsens (e.g., FX hedge with a counterparty exposed to that same currency), or collateral correlated with the counterparty's default.
8. **Disconfirming check.** Name the bias pitfalls — anchoring on current ratings (stale before a default), and concentration blind spots (counterparties that default together via a common driver). Test whether "diversified" counterparties share a hidden common exposure.

## Output Format

### Exposure & Netting Summary
| Counterparty | Netting set | Gross current exp | Netted current exp | Collateral (haircut) | Net exp | PFE add-on | EAD | Enforceability |
|---|---|---|---|---|---|---|---|---|

### Expected Loss
| Counterparty | PD (source) | LGD (source) | EAD | Expected Loss | Basis |
|---|---|---|---|---|---|
| | | | | EL = PD×LGD×EAD | |

### Netting / Collateral Benefit
| Counterparty | Gross exp | Netted exp | Net of collateral | Reduction | Counted? (enforceable) |
|---|---|---|---|---|---|

### Concentration (base / adverse / severe)
| Dimension | Largest | Top-3 | Limit | Breach? | Severe-scenario shift |
|---|---|---|---|---|---|
| Single name | | | | | |
| Sector | | | — | | |
| Geography | | | — | | |

### Wrong-Way Risk
| Counterparty | Linkage (exposure ↑ as credit ↓) | Collateral correlation | Flag |
|---|---|---|---|

### Findings
[Top exposures, concentration breaches, wrong-way risks, unconfirmed-netting gaps, disconfirming-check result.]

## Verification

- [ ] Current exposure and PFE are computed per counterparty with formulas shown.
- [ ] Netting is applied only within confirmed enforceable netting sets; collateral haircuts applied.
- [ ] Expected loss uses `PD × LGD × EAD` with sources stated per input.
- [ ] Netting/collateral benefit is shown gross vs. net; unconfirmed enforceability is not credited.
- [ ] Concentration is measured by name, sector, and geography against limits, including aggregate breaches.
- [ ] Wrong-way risk is identified where exposure rises with counterparty deterioration.
- [ ] No ratings, PDs, recoveries, or collateral values are invented; gaps `[ASSUMED]` and excluded from conclusions.
- [ ] The disconfirming pass tests for common-driver counterparty co-default.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Crediting netting where unenforceable | Netting benefit counted only within confirmed enforceable sets/jurisdictions |
| Collateral treated as risk-free | Haircuts applied; wrong-way collateral correlation flagged |
| Inventing PDs/ratings | All credit inputs user-sourced or `[ASSUMED]` and barred from definitive EL conclusions |
| Individual limits passing while aggregate breaches | Concentration measured at portfolio/sector/geography level, not just per name |
| Current rating anchoring | Ratings can be stale pre-default; disconfirming pass and stress shift required |
| Ignoring wrong-way risk | Exposure-credit correlation explicitly screened per counterparty |
| "Diversified" counterparties assumed independent | Common-driver co-default check required before claiming diversification |
