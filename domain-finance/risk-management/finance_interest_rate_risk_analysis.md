---
title: "Interest-Rate Risk Analysis — Duration/Gap, IRRBB, Rate-Shock Impact"
category: finance/risk-management
description: "Measure interest-rate risk via modified/effective duration, DV01, and repricing-gap analysis, then translate parallel and non-parallel rate shocks into changes in economic value of equity and net interest income — flagging convexity and IRRBB-style caveats without inventing rates or balances."
techniques:
  - NE-11
  - NE-10
  - QA-04
  - QA-02
  - RT-03
difficulty: advanced
tags:
  - interest-rate-risk
  - duration
  - irrbb
  - repricing-gap
  - eve
  - nii
  - convexity
updated: "2026-06-08"
related_prompts:
  - domain-finance/risk-management/finance_liquidity_risk_analysis.md
  - domain-finance/risk-management/finance_stress_test_scenario_design.md
  - domain-finance/risk-management/finance_hedging_strategy_designer.md
  - domain-finance/field_guide.md
---

*For informational purposes only. Not financial, investment, treasury, or risk-management advice. IRRBB shock specifications vary by jurisdiction; verify against current regulations as of the analysis date.*

## Objective

Quantify interest-rate risk on a portfolio or banking book using two complementary lenses: (1) **price/value sensitivity** via modified and effective duration, DV01, and convexity, and (2) **repricing-gap** analysis translating rate shocks into changes in net interest income (ΔNII) and economic value of equity (ΔEVE). Apply parallel and non-parallel (steepener/flattener/short-up/short-down) shocks in an IRRBB-style frame. All durations, balances, and shock sizes come from the user or are marked assumed.

## When to Use

- Banking-book interest-rate risk (IRRBB) measurement and limit-setting
- Bond / fixed-income portfolio sensitivity and hedging analysis
- Treasury asset-liability management (ALM) review
- Sizing the rate-shock impact on earnings and capital
- Preparing the rate-risk leg of an enterprise stress program

## Inputs / Context Required

- **Instruments / book:** Assets and liabilities with balances, coupons/rates, maturities or repricing dates, fixed vs. floating.
- **Durations / sensitivities:** Modified or effective duration per position (or cash flows to derive them); option features (caps, floors, prepayment, callability).
- **Yield curve:** Current curve or relevant rates, and the basis (par, zero, forward) — user-supplied.
- **Shock set:** Parallel ±bp and non-parallel scenarios; if a regulatory IRRBB set is intended, state the jurisdiction.
- **Behavioral assumptions:** Non-maturity deposit (NMD) repricing behavior, prepayment speeds, and their source.
- **Horizon for NII:** Earnings horizon (e.g., 12 months) for gap-based ΔNII.

## Constraints

### Must
- Show formulas before computing (modified duration, DV01, gap, ΔEVE, ΔNII).
- Distinguish price/value risk (EVE) from earnings risk (NII) — they answer different questions.
- Account for convexity on large shocks; note that duration is a first-order (linear) approximation that errs for big moves and optionality.
- Apply both parallel and non-parallel shocks; a parallel-only view misses curve-shape risk.
- State behavioral assumptions (NMD repricing, prepayment) and mark assumed ones `[ASSUMED]`.
- Flag where embedded options (caps/floors/prepayment) make effective duration diverge from modified duration.

### Must Not
- Invent durations, balances, curve levels, or shock sizes; gaps are `[ASSUMED]` and excluded from definitive conclusions.
- Use modified duration alone for option-heavy or large-shock cases without flagging convexity error.
- Present ΔEVE as if it were an earnings number, or ΔNII as if it were a value number.
- Assume floating-rate assets reprice perfectly with no basis or lag without stating it.
- Report a single parallel shock as a complete interest-rate risk picture.

## Instructions

1. **Classify the book (NE-10).** Tag each position fixed/floating, by repricing bucket, and flag embedded optionality (callable, prepayable, capped/floored).
2. **Compute price sensitivity.**
   ```
   Modified duration price impact:  ΔP ≈ −D_mod × Δy × P
   With convexity:                  ΔP ≈ −D_mod × Δy × P + ½ × C × (Δy)² × P
   DV01 (dollar value of 1bp):      DV01 ≈ D_mod × P × 0.0001
   ```
   Use **effective** duration where options are present (it captures the option-adjusted response).
3. **Build the repricing gap.** Bucket assets and liabilities by repricing date; compute gap per bucket and cumulative gap.
   ```
   Repricing gap_bucket = rate-sensitive assets − rate-sensitive liabilities
   ΔNII ≈ cumulative gap (to horizon) × Δrate
   ```
4. **Compute ΔEVE.** Revalue assets and liabilities under each shock (duration + convexity, or full revaluation for optionality); ΔEVE = Δ(PV assets) − Δ(PV liabilities).
5. **Apply the shock set (RT-03).** Parallel ±100/±200bp and non-parallel (steepener, flattener, short-rate up, short-rate down). For each, report ΔEVE and ΔNII.
6. **Behavioral overlay (QA-04).** Apply NMD repricing betas and prepayment assumptions; show how results shift vs. contractual treatment. State the source of each behavioral assumption.
7. **Stress and disconfirming check (QA-02).** Add a severe-but-plausible shock (e.g., a large flattener with deposit repricing acceleration). Name the bias pitfalls: anchoring on a parallel-only view, and assuming historical NMD stability persists. Test whether assets and liabilities reprice as independently as the gap assumes.

## Output Format

### Position Classification
| Instrument | Balance | Fixed/Float | Repricing bucket | Duration (mod/eff) | Optionality |
|---|---|---|---|---|---|

### Price Sensitivity
```
ΔP ≈ −D_mod × Δy × P    DV01 ≈ D_mod × P × 0.0001
  Portfolio D_mod = [ ]   P = [$ ]   DV01 = [$ ]/bp
  With convexity C = [ ]: ΔP(±200bp) = [$ ]
```

### Repricing Gap Ladder
| Bucket | RS Assets | RS Liabilities | Gap | Cumulative Gap |
|---|---|---|---|---|
| ≤3m | | | | |
| 3–12m | | | | |
| 1–5y | | | | |
| >5y | | | | |

### Rate-Shock Impact (base / adverse / severe)
| Scenario | ΔEVE | ΔEVE / Equity | ΔNII (12m) | ΔNII / Base NII |
|---|---|---|---|---|
| Base | — | — | — | — |
| Parallel +200bp (adverse) | [$] | [%] | [$] | [%] |
| Flattener / NMD accel. (severe) | [$] | [%] | [$] | [%] |
| Parallel −200bp | [$] | [%] | [$] | [%] |
| Steepener | [$] | [%] | [$] | [%] |

### Behavioral Sensitivity
| Assumption | Contractual | Behavioral | Source |
|---|---|---|---|
| NMD repricing beta | | | |
| Prepayment speed | | | |

### Findings
[EVE vs. NII tension, curve-shape exposure, optionality/convexity caveats, disconfirming-check result.]

## Verification

- [ ] Duration, DV01, gap, ΔEVE, and ΔNII formulas are shown before the numbers.
- [ ] EVE (value) and NII (earnings) risk are presented as distinct measures.
- [ ] Convexity is included for large shocks; duration-as-linear-approximation caveat stated.
- [ ] Effective duration is used where embedded options exist; divergence from modified duration flagged.
- [ ] Both parallel and non-parallel shocks are applied.
- [ ] Behavioral (NMD/prepayment) assumptions are stated with sources; assumed values `[ASSUMED]`.
- [ ] No durations, balances, curve levels, or shocks are invented.
- [ ] A severe-but-plausible shock and the disconfirming check are included.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Duration as exact price change | Duration is first-order; convexity term required for large shocks and optionality |
| Parallel shock as complete picture | Non-parallel (steepener/flattener/short-up/down) shocks mandatory |
| Conflating EVE and NII | Value and earnings risk reported separately with distinct formulas |
| Modified duration on option-heavy book | Effective (option-adjusted) duration required; divergence flagged |
| Assuming perfect floating-rate repricing | Basis/lag and NMD betas stated; behavioral overlay shown vs. contractual |
| Stable-deposit assumption from calm periods | Recency/anchoring bias named; severe deposit-repricing scenario included |
| Inventing curve levels to produce a result | Curve and shocks must be user-supplied or `[ASSUMED]` and excluded from conclusions |
