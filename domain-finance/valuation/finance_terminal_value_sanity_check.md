---
title: "Terminal Value Sanity Check — Implied Multiple, Perpetuity-Growth Bounds, and Reasonableness Tests"
category: finance/valuation
description: "Stress-test the terminal value in a DCF model for reasonableness using implied-multiple cross-checks, perpetuity-growth bound tests, and TV-as-%-of-EV analysis — producing a pass/flag/fail verdict with corrective guidance."
techniques:
  - QA-01
  - QA-02
  - NE-11
  - DS-02
  - AG-02
difficulty: intermediate
tags:
  - terminal-value
  - dcf
  - sanity-check
  - valuation
  - perpetuity-growth
  - exit-multiple
updated: "2026-06-08"
related_prompts:
  - domain-finance/valuation/finance_dcf_model_builder.md
  - domain-finance/valuation/finance_dcf_model_auditor.md
  - domain-finance/valuation/finance_wacc_builder.md
  - domain-finance/valuation/finance_valuation_sensitivity_scenario.md
  - domain-finance/field_guide.md
---

**Informational only — not investment advice. All outputs must be reviewed by qualified finance professionals before use in any transaction or decision.**

## Objective

Perform a structured reasonableness test on the terminal value (TV) embedded in a discounted cash flow model, using four complementary checks: (1) the WACC > g mathematical requirement, (2) the implied EV/EBITDA multiple embedded in the perpetuity-growth method, (3) the implied perpetuity growth rate embedded in the exit-multiple method, and (4) the TV-as-%-of-total-EV concentration test — then produce a ranked verdict with corrective actions for any failures.

## When to Use

- Before finalizing a DCF model for investment committee, board, or fairness-opinion use
- Auditing a counterparty's DCF where the TV is the most uncertain component
- Quickly sense-checking a TV without rebuilding the full model
- As the dedicated "terminal value" step in the `finance_dcf_model_builder.md` workflow (Step 5 → cross-reference here)
- Training analysts to understand what makes a terminal value defensible vs. arbitrary

## Inputs / Context Required

**From the DCF model**
- WACC (stated in the model)
- Terminal FCF or terminal EBITDA (the base for the perpetuity or exit-multiple calculation)
- Perpetuity growth rate (g) used in the model
- Exit EV/EBITDA multiple used in the model
- TV calculated via both methods (or at least one)
- Total enterprise value (TV + PV of projection-period FCF)
- Terminal EBITDA or EBIT (needed for the implied-multiple cross-check)

**For the cross-check**
- Trading-comp peer median EV/EBITDA multiple (current, as of model date)
- Long-run nominal GDP growth rate for the company's primary market (used as the g ceiling)
- Industry-specific context: is the industry expected to grow faster or slower than GDP in the long run?

**Scenario**
- Bear / base / bull WACC and g values (if available from the full model)

## Constraints

### Must
- Test the WACC > g condition mathematically; a model where g ≥ WACC is mathematically invalid and must be flagged Critical.
- Compute the implied EV/EBITDA multiple embedded in the PGM terminal value and compare it to peer trading multiples.
- Compute the implied perpetuity growth rate embedded in the exit-multiple TV and compare it to the stated g.
- Calculate TV as % of total EV; flag if >75%; require additional sensitivity if >90%.
- Provide a verdict for each test: Pass, Flag (material concern), or Fail (Critical error).
- For any Flag or Fail, provide a corrective action with a specific, defensible alternative.

### Must Not
- Pass a terminal value that implies perpetuity growth above long-run nominal GDP without an explicit, written justification.
- Accept an implied EV/EBITDA multiple that is materially above the current peer trading range without an explicit premium rationale.
- Treat the two TV methods as independent if they diverge materially — the divergence is a signal requiring investigation.
- Flag as a problem a TV that comprises a large share of EV simply because it is large; high TV% is expected for long-horizon growth companies and must be evaluated in context.

## Instructions

**Step 1 — The WACC > g mathematical validity test**

```
Test: WACC − g > 0

If WACC > g: PASS
If WACC = g: FAIL — the denominator is zero; TV is undefined (infinite)
If WACC < g: FAIL — the denominator is negative; TV is negative (nonsensical)

WACC − g spread:
  > 2%: comfortable; terminal value is not unusually sensitive to small changes in g
  1–2%: acceptable; sensitivity analysis on g is important
  < 1%: FLAG — small changes in g produce very large changes in TV; sensitivity table is mandatory

Current model values:
  WACC = [%], g = [%], spread = [%]
  Result: [PASS / FLAG / FAIL]
```

**Step 2 — Implied-multiple check (PGM method)**

The perpetuity-growth terminal value implies an exit EV/EBITDA multiple:

```
TV_PGM = FCFF_terminal × (1 + g) / (WACC − g)

Implied EV/EBITDA = TV_PGM / EBITDA_terminal

Compare to:
  Current peer median EV/EBITDA: [x]
  Historical sector average EV/EBITDA (5-year or cycle average): [x]
  Precedent transaction median: [x]

Reasonableness test:
  If implied multiple ≈ peer median (±15%): PASS
  If implied multiple is 15–30% above peer median: FLAG — requires premium rationale
  If implied multiple is >30% above peer median OR below 5x for a profitable company: FLAG/FAIL — investigate
```

Note: The implied multiple embeds the assumption that at the end of the explicit projection period, the company is a stable perpetuity. If the company is still in a high-growth phase at the terminal year, a premium multiple is defensible — but must be stated.

**Step 3 — Implied-growth check (exit-multiple method)**

The exit-multiple terminal value implies a perpetuity growth rate:

```
TV_Exit = EBITDA_terminal × Exit Multiple

Implied g from Exit:
  g_implied = WACC − FCFF_terminal / TV_Exit
            = WACC − (FCFF_terminal / (EBITDA_terminal × Exit Multiple))

Simplification: g_implied = WACC − FCF Conversion Ratio / Exit Multiple
  where FCF Conversion Ratio = FCFF_terminal / EBITDA_terminal

Compare g_implied to:
  Stated g in PGM method: [%]
  Long-run nominal GDP growth (primary market): [%]

Reasonableness tests:
  If g_implied ≈ stated g (±50bps): PASS — methods are broadly consistent
  If g_implied > stated g: Exit multiple embeds higher growth than PGM; investigate
  If g_implied > long-run nominal GDP: FLAG — exit multiple implies above-economy perpetuity growth
  If g_implied < 0: Exit multiple implies terminal decline — flag if the company narrative contradicts this
```

**Step 4 — Method divergence test**

```
TV Divergence = (TV_PGM − TV_Exit) / TV_Exit × 100%

If |Divergence| < 10%: PASS — methods broadly agree; use average or disclose both
If |Divergence| 10–20%: FLAG — material divergence; investigate the driver
  (Common causes: FCF conversion ratio ≠ what the exit multiple implies; growth profile inconsistency)
If |Divergence| > 20%: FAIL — one method is likely using an inconsistent assumption; correct before finalizing

Steps to investigate divergence:
  1. Compute the FCF-to-EBITDA conversion ratio at the terminal year
  2. Check whether the exit multiple reflects a business with that conversion ratio
  3. Check whether g is internally consistent with the company's projected reinvestment rate
```

**Step 5 — TV-as-%-of-EV concentration test**

```
TV% = PV(Terminal Value) / Total Enterprise Value × 100%

Interpretation:
  TV% < 60%: PASS for a mature, capital-intensive business; the projection period carries significant weight
  TV% 60–75%: PASS for most growth companies; acceptable range; sensitivity analysis still recommended
  TV% 75–90%: FLAG — TV dominates the value; sensitivity on g and exit multiple is mandatory
  TV% > 90%: FAIL-level concern — the projection period adds almost no value; either the projection
              period is too short OR the projection-period cash flows are negative/minimal,
              both of which require investigation

Context adjustment: For early-stage or high-growth companies, TV% >85% may be expected and acceptable
if the explicit period shows a recognized investment phase. In that case, state the context and proceed
with heightened sensitivity disclosure.
```

**Step 6 — G ceiling test (perpetuity-growth bound)**

```
Ceiling: g ≤ long-run nominal GDP growth of the company's primary market
  For US-based companies: current consensus long-run nominal GDP ~2–3%
  For emerging-market companies: higher nominal growth may be appropriate (state the basis)
  For companies with declining industries: g may reasonably be negative

If g > GDP ceiling without justification: FLAG — requires explicit written rationale
  Defensible rationale examples:
    - Company addresses a global market and captures share from non-US growth
    - Inflation is expected to structurally exceed historical norms (state the basis)
    - Industry-specific drivers (healthcare cost inflation, energy transition)

If g ≥ WACC: FAIL (already captured in Step 1)
```

**Step 7 — Compile the verdict table and corrective actions**

| Test | Threshold | Model Input | Result | Severity | Corrective Action |
|---|---|---|---|---|---|
| WACC > g | g < WACC | g=[%], WACC=[%] | Pass/Flag/Fail | Critical if Fail | |
| WACC−g spread | >1% recommended | [%] | Pass/Flag | Material if <1% | Widen spread; add sensitivity |
| Implied multiple vs. peers | Within ±15% of peer median | [x] vs. [x] | Pass/Flag/Fail | Material | Adjust g or exit multiple |
| g_implied from exit multiple | ≈ stated g (±50bps) | [%] vs. [%] | Pass/Flag | Material | Investigate FCF conversion |
| TV method divergence | <10% | [%] | Pass/Flag/Fail | Material | Resolve structural inconsistency |
| TV% of EV | <75% recommended | [%] | Pass/Flag | Material if >90% | Extend explicit period; sensitivity mandatory |
| g vs. GDP ceiling | g ≤ long-run GDP | [%] vs. [%] | Pass/Flag | Material | Reduce g or document rationale |

## Output Format

### Input Summary

| Model Parameter | Value |
|---|---|
| WACC | [%] |
| Perpetuity growth rate (g) | [%] |
| WACC − g spread | [%] |
| Terminal EBITDA | [$] |
| Terminal FCFF | [$] |
| TV (PGM) | [$] |
| TV (Exit Multiple) | [$] |
| Exit multiple applied | [x] |
| Total EV | [$] |
| TV% of EV | [%] |

### Test Results

[Step 7 verdict table — all 7 tests]

### Summary Verdict

> **Overall: [PASS / CONDITIONAL PASS (address Flags) / FAIL (address Failures before use)]**
>
> [2–3 sentence narrative: identify the most important finding and the corrective action.]

### Sensitivity at Terminal Value Level (for any test that Flagged)

| g / Exit Multiple ↓ | WACC − 1% | Base WACC | WACC + 1% |
|---|---|---|---|
| g − 1% | TV = [$] | | |
| Base g | | TV = [$] | |
| g + 1% | | | TV = [$] |

## Verification

- [ ] WACC > g verified mathematically; any failure is flagged Critical.
- [ ] WACC − g spread computed; <1% spread triggers mandatory sensitivity disclosure.
- [ ] Implied EV/EBITDA from PGM method computed and compared to peer trading multiples.
- [ ] Implied g from exit-multiple method computed and compared to stated g and GDP ceiling.
- [ ] TV method divergence computed; >20% divergence requires investigation.
- [ ] TV% of EV computed; >75% triggers sensitivity requirement; >90% is a critical concern.
- [ ] g compared to long-run nominal GDP ceiling; exceedance requires written justification.
- [ ] All seven tests summarized in the verdict table with severity and corrective action.
- [ ] No benchmark figures (peer multiples, GDP growth) invented; any figure used is labeled with source.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Flagging a high TV% as inherently invalid for growth companies | High TV% is normal for growth companies in the investment phase; context assessment required before flagging |
| Flagging g > GDP ceiling for companies with multi-decade global growth runways | GDP ceiling is a guideline, not an absolute rule; flag requires investigation, not automatic rejection |
| Calling PGM and exit-multiple "consistent" when they have different embedded assumptions | Implied-g and implied-multiple cross-checks are required; close dollar values can still embed inconsistent assumptions |
| Treating a narrow WACC − g spread as a model error vs. a sensitivity concern | A spread <1% is a FLAG requiring sensitivity disclosure, not necessarily a Fail |
| Passing a terminal value simply because the arithmetic is correct | Mathematical validity (Step 1) is necessary but not sufficient; economic reasonableness tests (Steps 2–6) are equally required |
