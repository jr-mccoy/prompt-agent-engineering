---
title: "Fermi Estimation — Order-of-Magnitude Estimate with Visible Assumption Ladder"
category: reasoning-craft/reasoning-moves
description: "Produce an order-of-magnitude estimate of a numeric quantity by decomposing it into 3–6 multiplicative factors, estimating each with an explicit confidence band, and combining them into a final range. The point is auditable assumptions, not precision — every factor is named, justified, and can be challenged independently."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - DS-02
  - QA-01
difficulty: intermediate
tags:
  - reasoning
  - estimation
  - decomposition
  - order-of-magnitude
  - market-sizing
updated: "2026-05-10"
reasoning:
  styles: [decomposition, multiplicative, calibration]
  stakes: variable
  horizon: variable
  uncertainty: ambiguity
  evidence_quality: sparse
  domain_complexity: variable
  collaboration: solo
  output_format: factor_chain
  user_role: [analyst, founder, pm, consultant, student]
  mode: [forecast, audit]
related_prompts:
  - domain-reasoning-craft/reasoning-moves/reasoning_reference_class_forecast.md
  - domain-product-management/prompts/product_market_size_calculator.md
  - domain-reasoning-craft/forecasting/forecasting_super_forecaster_decomposition.md
---

# Fermi Estimation

**Objective:** Produce a defensible order-of-magnitude estimate of a numeric quantity using a multiplicative decomposition of 3–6 factors. Each factor gets a low / mid / high estimate with a one-line justification. The combined estimate is a range, not a number. The deliverable is the *assumption ladder*, not the final number — anyone reading the output should be able to challenge or replace any single factor independently.

**When to use:**
- The user needs a quick estimate of a quantity (market size, addressable users, energy required, time-to-completion, cost) and no clean dataset exists.
- An expert claim or business case rests on a number that has not been decomposed; you want to test it.
- A decision hinges on whether a quantity is closer to 10K or 10M, and current intuitions span that range.

**When NOT to use:**
- The quantity is small enough to count directly. Just count.
- A clean primary source already exists and is trusted. Use it.
- The user wants two-decimal precision. Fermi is for orders of magnitude; if precision matters, this isn't the tool.

**Audience:** Founders sizing markets, PMs scoping launches, analysts pressure-testing claims, students practicing structured reasoning, anyone trapped in a "could be anywhere from X to Y" debate.

---

## Inputs / Context

1. **The quantity to estimate.** Stated with units (people, dollars, kWh, hours, transactions per month, etc.).
2. **Geographic / temporal scope.** Global, US, a specific city, a specific year.
3. **Definitional boundaries.** What counts and what doesn't (e.g., "active users" — minimum frequency? engagement threshold?).
4. **Any anchor data already in hand.** A known total population, a known per-capita rate, a comparable benchmark.
5. **Acceptable uncertainty band.** Order of magnitude (factor of 10) is normal; if narrower is needed, say so up front — the decomposition will need to be deeper.

---

## Constraints

### Must
- Produce a multiplicative chain of 3–6 factors. Fewer than 3 hides assumptions; more than 6 fakes precision.
- Give each factor a low / mid / high estimate, not a single number.
- Combine: mid estimate from products of mids; low estimate from products of lows; high from products of highs.
- Justify each factor in one sentence with the source of the estimate (data, analogy, common knowledge, pure guess) explicitly labeled.
- Report the final estimate as `[low, mid, high]` with the spread described in factors of 10 (e.g., "spans ~1.5 orders of magnitude").
- Sanity-check against any anchor data the user provided; if the estimate disagrees by >10x, find the load-bearing factor and inspect it.

### Must Not
- Multiply chains so long that the cumulative uncertainty exceeds 3 orders of magnitude. If it does, the estimate is uninformative.
- Hide a guess inside an authoritative-sounding factor name. If a factor is a guess, say "guess".
- Anchor every factor to the same base (e.g., US population) without checking that the bases compose. Population × population = nonsense.
- Convert the result into a confidence percentage without doing a sensitivity step.
- Smuggle in the user's hoped-for answer by reverse-engineering factor estimates.

---

## Instructions

### Step 1 — Define the quantity sharply
Write the quantity with full units, scope, and definitional boundaries. Test: could two analysts agree on what counts? If not, refine.

### Step 2 — Pick the decomposition path
Sketch 2–3 different decomposition paths (e.g., "people × adoption × frequency × spend" vs. "businesses × seats × price"). Pick the one whose factors are most independently estimable. Write the chosen chain.

### Step 3 — Estimate each factor (low / mid / high)
For each factor in the chain:
- **Low estimate:** plausible floor
- **Mid estimate:** central guess
- **High estimate:** plausible ceiling
- **Justification:** one line, with source label `[data | analogy | common knowledge | guess]`

The low/high band should be wide enough to feel uncomfortable. If you're confident your mid is within 10%, the band is too narrow.

### Step 4 — Combine
- `mid_total = product of mids`
- `low_total = product of lows`
- `high_total = product of highs`
- Round each to 1 significant figure.

### Step 5 — Spread report
- Spread: `log10(high_total / low_total)` orders of magnitude.
- If spread > 3, find the noisiest factor (largest log10(high/low)) and refine or split it.

### Step 6 — Anchor check
If any anchor data was provided, compare. Disagreement >10x triggers a factor audit:
- Which single factor change would make them agree?
- Is that factor change defensible?

### Step 7 — Sensitivity (which factor matters most)
For each factor, compute how much the mid_total changes if that single factor moves to its low / high. The factor with the largest impact is the load-bearing assumption — the one to research further if precision matters.

### Step 8 — Final statement
State: "[Quantity] is approximately [mid_total] with a plausible range of [low_total] to [high_total], spanning ~[N] orders of magnitude. The estimate is most sensitive to [factor], where uncertainty in that factor alone moves the result by ~[X]×."

---

## False-Positive Prevention

1. **Spurious precision.** A Fermi estimate is rounded to 1 significant figure. If you write "3,247,891 users", you have lied with arithmetic.
2. **Independence violation.** Multiplied factors must be approximately independent. "Number of users × revenue per user" assumes revenue doesn't depend on user count — usually false at scale; flag.
3. **Authority laundering.** A factor sourced as "industry estimates" without a citation is a guess wearing a suit. Label it as a guess.
4. **Single-decomposition lock-in.** The first decomposition path you write is rarely the cleanest. Sketching 2–3 and picking forces honesty about what you actually know.
5. **Mid-only optimism.** Reasoners are systematically over-confident in their mid estimates. The low and high should each feel surprising, not "well, maybe a little less / more."
6. **Anchor data ignored.** If the user gave anchor data and the result disagrees by >10x, do not just report the result. Investigate.
7. **Cumulative confidence inflation.** Per-factor bands set too narrow (overconfident factor ranges) produce a falsely narrow product — even though combining products-of-lows and products-of-highs is itself conservative. The fix is at the factor level: widen any band that feels comfortable.

---

## Output Format

```
# Fermi estimate — [quantity, with units and scope]

## Definitional boundaries
- [What counts]
- [What does not count]

## Decomposition path
[factor1] × [factor2] × [factor3] × … = [quantity]

(Considered alternative paths: [briefly])

## Factor table
| # | Factor                          | Low       | Mid       | High      | Source         | Justification |
|---|---------------------------------|-----------|-----------|-----------|----------------|---------------|
| 1 | [name]                          | [val]     | [val]     | [val]     | data/guess/etc | [one line]    |
| 2 | …                               |           |           |           |                |               |
| 3 | …                               |           |           |           |                |               |

## Combination
- low_total  = [computed]  (product of lows)
- mid_total  = [computed]  (product of mids)
- high_total = [computed]  (product of highs)

## Spread
- log10(high/low) = [value] orders of magnitude
- Noisiest factor: [name], contributing [factor] of total spread

## Anchor check
- Anchor provided: [yes/no, what]
- Comparison: [agree within 2x / disagree by Nx]
- If disagreement: [load-bearing factor + recommendation]

## Sensitivity (per-factor leverage on mid_total)
| Factor | Mid_total at low | Mid_total at high | Range × |
|--------|------------------|-------------------|---------|
| [f1]   | [val]            | [val]             | [×]     |
| …      |                  |                   |         |

## Final
> [Quantity] is approximately **[mid_total]** with a plausible range of **[low_total] to [high_total]**, spanning ~[N] orders of magnitude. Most sensitive to **[factor]**.
```

---

## Verification

- [ ] Quantity has explicit units, scope, and definitional boundaries.
- [ ] Decomposition has 3–6 factors and was chosen from at least 2 candidate paths.
- [ ] Every factor has low / mid / high estimates with one-line justifications.
- [ ] Each factor's source is labeled `[data | analogy | common knowledge | guess]`.
- [ ] Combination shows three products (low / mid / high), rounded to 1 sig fig.
- [ ] Spread is reported in orders of magnitude.
- [ ] Anchor data, if provided, was compared and disagreement investigated.
- [ ] Sensitivity table identifies the load-bearing factor.
- [ ] No spurious precision in the final number.
- [ ] No factor unjustified or hidden.
