---
title: "Central-Bank Reaction Function Modeler — Taylor-Rule Framing and Policy-Path Scenarios"
category: finance/markets-macro
description: "Model a central bank's reaction function using a Taylor-rule framework, infer the implied policy rate from user-supplied inflation/output/employment inputs, compare against the market-implied path, and build policy-path scenarios — without asserting any current data or central-bank statement from memory."
techniques:
  - NE-11
  - NE-10
  - RT-06
  - QA-02
  - QA-04
difficulty: advanced
tags:
  - central-bank
  - monetary-policy
  - taylor-rule
  - reaction-function
  - policy-path
updated: "2026-06-08"
related_prompts:
  - domain-finance/markets-macro/finance_rate_path_yield_curve_analysis.md
  - domain-finance/markets-macro/finance_inflation_regime_analysis.md
  - domain-finance/markets-macro/finance_economic_scenario_modeler.md
  - domain-finance/field_guide.md
---

**Informational only — not investment advice. A reaction function is a stylized model, not a prediction of policy; all data and any central-bank guidance are user-supplied. Outputs require professional review.**

## Objective

Model a central bank's reaction function with an explicit Taylor-rule-style framework: compute a rule-implied policy rate from user-supplied inflation, output-gap, and employment inputs; compare it against the current rate, the bank's stated guidance (if supplied), and the market-implied path; then build policy-path scenarios reflecting different mandate weights and shocks — flagging that the rule is a stylized approximation, not a forecast.

## When to Use

- Estimating where policy "should" be vs. where it is, given the data
- Reconciling the market-implied path with a fundamentals-based read
- Stress-testing a higher-for-longer / pivot narrative against a rule
- Building the policy layer of a macro scenario or rate-path analysis
- Briefing on how sensitive policy is to inflation vs. growth surprises

## Inputs / Context Required

```
<reaction_inputs>
Central bank / economy: (e.g., Fed/US, ECB/Eurozone, BoE/UK) | Currency | As-of date

USER-SUPPLIED DATA (value, source, date — do not assume):
  - Current policy rate (target)
  - Inflation (core PCE/CPI, YoY) and the bank's inflation target
  - Output gap or a proxy (GDP vs. potential), if available
  - Unemployment rate and estimated natural rate (u*), if dual-mandate
  - Neutral real rate estimate (r*) if available (else state assumption)
  - Stated central-bank guidance / dot plot / market-implied path (if available)

RULE PARAMETERS (use defaults if user does not specify; state them):
  - Inflation response coefficient (a, default ~0.5)
  - Output/employment gap coefficient (b, default ~0.5)
  - Neutral nominal rate basis (r* + target)
SHOCKS OF INTEREST: (e.g., inflation surprise, growth shock, financial-stability event)
</reaction_inputs>
```

If current rate, inflation, or targets are not supplied, request them. Do not assert current policy settings or central-bank statements from memory.

## Constraints

### Must
- Use only user-supplied data and guidance; restate each with source/date.
- State the Taylor-rule form and all coefficients explicitly; compute the implied rate as formula → inputs → result (NE-11).
- Treat r* (neutral rate) as an estimate with a stated source/assumption.
- Compare rule-implied vs. current vs. guidance vs. market-implied path; quantify gaps in bps.
- Build policy-path scenarios (NE-10) varying mandate weights and incoming data.
- Distinguish a rules-based read from the bank's actual stated reaction (RT-06) — the bank may deviate (smoothing, financial stability, judgment).
- State confidence and the key sensitivities (QA-04); stress-test the path (QA-02).
- Apply guardrails against treating the rule as a forecast and against over-reading a single data surprise.

### Must Not
- Assert the current policy rate, inflation, targets, or any central-bank statement from memory.
- Present the Taylor-rule output as a prediction of what the bank will do.
- Hide the coefficients or the r* assumption — they drive the result.
- Ignore policy inertia/smoothing and non-rule factors (financial stability, forward guidance commitments).
- Confuse the bank's stated stance with the rule-implied rate.

## Instructions

**Step 1 — Restate inputs and parameters.** Tabulate user data, targets, and rule coefficients with source/date and assumption flags.

**Step 2 — Compute the rule-implied rate.**

```
Taylor rule (standard form):
  i* = r*neutral + π + a(π − π_target) + b(output gap)
  where:
    i*          = rule-implied nominal policy rate
    r*neutral   = neutral real rate (estimate — state source)
    π           = current inflation
    π_target    = inflation target
    a           = inflation-gap coefficient (state value)
    b           = output/employment-gap coefficient (state value)
    output gap  = (actual − potential) output, or −Okun-mapped unemployment gap

Dual-mandate variant (employment gap form):
  output gap term ≈ −c × (unemployment − u*)   [state c]

Show: r*neutral + π = neutral nominal anchor; then add the two gap responses.
Result: i* and the gap vs. current policy rate (bps).
```

**Step 3 — Inertia/smoothing adjustment.**

```
Smoothed rate:  i_t = ρ × i_(t−1) + (1 − ρ) × i*   [ρ = smoothing parameter, state it]
Note: banks rarely jump to i* in one step; smoothing explains gradualism.
```

**Step 4 — Compare paths (RT-06).** Tabulate rule-implied vs. current vs. stated guidance vs. market-implied (if supplied); explain divergences (e.g., bank weighting financial stability, lagged data, credibility).

**Step 5 — Sensitivity.** Show how i* moves for ±0.5pp inflation, ±1pp output gap, and ±0.5pp r* — formula-driven.

**Step 6 — Policy-path scenarios (NE-10).** Hawkish (higher a / inflation surprise), dovish (growth/employment weighting / financial stress), and base: implied rate path and triggers.

**Step 7 — Stress-test & bias (QA-02 / QA-04).** What single data surprise most changes the path? Apply the "rule ≠ forecast" and recency guardrails; state confidence and the dominant sensitivity.

## Output Format

### Inputs & Rule Parameters (user-supplied)

| Item | Value | Source / date | Assumption flag |
|---|---|---|---|
| Policy rate | | | |
| Inflation / target | | | |
| Output gap / unemployment & u* | | | |
| r* neutral | | | (estimate) |
| Coefficients a, b, ρ | | | (stated) |

### Rule-Implied Rate

| Component | Formula | Inputs | Value |
|---|---|---|---|
| Neutral nominal anchor (r* + π) | | | |
| Inflation-gap response a(π−π*) | | | |
| Output-gap response b·gap | | | |
| **Rule-implied i\*** | | | |
| Gap vs. current rate (bps) | | | |
| Smoothed one-step rate | | | |

### Path Comparison

| Path | Implied rate / direction | Gap vs. rule (bps) | Divergence explanation |
|---|---|---|---|
| Current | | | |
| Stated guidance / dots | | | |
| Market-implied | | | |

### Sensitivity

| Shock | Δi* | 
|---|---|
| Inflation +0.5pp | |
| Output gap +1pp | |
| r* +0.5pp | |

### Policy-Path Scenarios

| Scenario | Mandate weighting / shock | Implied path | Trigger |
|---|---|---|---|
| Base | | | |
| Hawkish | | | |
| Dovish | | | |

### Stress-Test & Confidence
[Step 7 — most path-changing surprise; rule ≠ forecast note; confidence; dominant sensitivity]

## Verification

- [ ] Current rate, inflation, targets, and any guidance are user-supplied with source/date; none from memory.
- [ ] Taylor-rule form and all coefficients (a, b, ρ) stated explicitly.
- [ ] r* treated as an estimate with a stated source/assumption.
- [ ] Rule-implied rate shown as formula → inputs → result.
- [ ] Smoothing/inertia adjustment applied and explained.
- [ ] Rule-implied vs. current vs. guidance vs. market-implied compared with bps gaps.
- [ ] Sensitivity to inflation, output gap, and r* shown.
- [ ] Scenarios vary mandate weights; "rule ≠ forecast" guardrail applied; confidence stated.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Asserting current policy rate / inflation / CB statements from memory | All are user inputs with source/date; stop if missing |
| Presenting the Taylor-rule output as a forecast | Label explicitly as a stylized rule, not a prediction; banks deviate (smoothing, judgment, stability) |
| Hiding r* and coefficient choices | r*, a, b, ρ stated and flagged as assumptions; sensitivity shown |
| Ignoring policy inertia | Smoothing step mandatory; explains gradualism vs. jumping to i* |
| Confusing stance with rule-implied rate | Path-comparison table separates rule, guidance, market, and current |
| Over-reading one data surprise | Recency guardrail; stress-test isolates the most path-changing single surprise |
