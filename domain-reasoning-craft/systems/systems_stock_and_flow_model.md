---
title: "Stock-and-Flow Model — Map What Accumulates and What Changes It"
category: reasoning-craft/systems
description: "Sketch the stocks (accumulations), flows (rates that fill or drain them), and delays in a dynamic problem, then read the behavior-over-time the structure produces. More quantitative than a causal loop diagram: it isolates why interventions on flows take time to move stocks, and why stocks keep moving after flows are cut. Counters the failure mode of treating a slow-moving accumulation as if it responds instantly to a rate change."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - DS-02
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - systems-thinking
  - stock-and-flow
  - dynamics
  - delays
  - accumulation
updated: "2026-05-21"
reasoning:
  styles: [systems, causal, quantitative, structural]
  stakes: variable
  horizon: months_to_years
  uncertainty: deep
  evidence_quality: moderate
  domain_complexity: cross_domain
  collaboration: solo_or_pair
  output_format: stock_flow_table_plus_behavior_sketch
  user_role: [analyst, founder, executive, operator, policy]
  mode: [audit, synthesize, diagnose, forecast]
related_prompts:
  - domain-reasoning-craft/systems/systems_causal_loop_diagram.md
  - domain-reasoning-craft/systems/systems_feedback_loop_identifier.md
  - domain-reasoning-craft/systems/systems_leverage_point_analysis.md
---

# Stock-and-Flow Model

**Objective:** Translate a dynamic problem into a stock-and-flow structure: the **stocks** (quantities that accumulate — people, capital, trust, debt, inventory, attention, technical debt), the **flows** that fill or drain each stock (rates: hires per month, capital deployed per quarter, trust earned/lost per interaction), and the **delays** between an action and its effect on a stock. Then read off the behavior-over-time the structure produces (S-curve, oscillation, exponential, decay, overshoot-and-collapse). Output a structured stocks/flows/delays table plus a behavior sketch. Designed for asynchronous use without simulation software.

**When to use:**
- An intervention targets a *rate* (hiring faster, paying down debt) but the *level* (team size, debt balance) responds slowly or not at all, and you need to see why.
- A quantity keeps moving after you stopped pushing it (pipelines, momentum, reputational damage), suggesting an accumulation with inertia.
- You want a more quantitative frame than a causal loop diagram — one that distinguishes levels from rates.
- Diagnosing oscillation, overshoot, or "we fixed the inflow but the stock is still wrong."

**When NOT to use:**
- The feedback structure (which loops dominate when) is the real question — start with `systems_causal_loop_diagram.md`, then add stocks/flows if needed.
- The problem is genuinely static or a one-shot event with no accumulation over time.
- You need a calibrated numeric forecast and have time-series data — build a real simulation model; this prompt is a structured qualitative sketch, not a solver.

**Audience:** Analysts, founders, operators, policy people, and executives diagnosing why a system's *levels* don't track their *interventions*.

---

## Inputs / Context

1. **The dynamic problem.** The behavior that needs explaining, framed in terms of a quantity that is too high, too low, or moving wrong over time ("headcount keeps overshooting plan", "cash burns faster than revenue accumulates", "trust collapsed and isn't recovering").
2. **Time horizon.** Over what period does the behavior unfold (and at what cadence — daily, monthly, quarterly)?
3. **Known rates and levels.** Any numbers you have: current stock levels, inflow/outflow rates, observed delays.
4. **Interventions tried or proposed.** What rate or level someone tried to change, and what happened to the stock.
5. **Boundary.** Which stocks are inside the model vs treated as exogenous inputs.

---

## Constraints

### Must
- Identify 2–6 **stocks**. A stock is something that would still have a value if all flows stopped (a level, a balance, a count). Use noun phrases for accumulations.
- For each stock, name its **inflows** and **outflows** as rates (per unit time). Every stock has at least one flow; most have both an inflow and an outflow.
- Mark **delays** on flows or on the perception of stock levels, with a magnitude estimate (short / medium / long, plus units if known).
- State each stock's **initial level** (or "unknown — estimate range") and the **net rate** (inflow − outflow) at the current moment.
- Produce a **behavior-over-time sketch**: describe the curve each key stock follows (linear rise, exponential, S-curve, oscillation, overshoot-and-collapse, decay-to-floor) and why the structure produces it.
- Explicitly answer the **stock-vs-flow lag question**: how long after a flow change does the stock meaningfully respond, and why.

### Must Not
- Confuse a stock with a flow. "Hiring" is a flow (per month); "team size" is a stock (a level). If a quantity has no time unit, it's probably a stock; if it's inherently per-period, it's a flow.
- Omit outflows. The most common error is modeling only inflows ("we hired 40 people") and ignoring the drain (attrition), which is why the stock didn't grow as expected.
- Hand-wave delays. Either estimate the magnitude or state "delay assumed negligible" with a reason.
- Claim a precise numeric trajectory without data. The deliverable is structural behavior (the *shape* and *why*), not a forecast to two decimal places.
- Skip the behavior sketch. The table is the input; the behavior explanation is the output.

---

## Instructions

### Step 1 — State the problem as a quantity over time
Name the stock that is behaving wrong and describe its observed trajectory. If the problem is framed as an action ("we keep over-hiring"), restate it as a level ("headcount overshoots target by ~15% then corrects").

### Step 2 — Identify the stocks
List 2–6 accumulations. For each: is it inside the model boundary or an external input? Apply the "if all flows stopped, would this still have a value?" test — if yes, it's a stock.

### Step 3 — Identify the flows
For each stock, name:
- **Inflow(s):** what rate adds to it.
- **Outflow(s):** what rate drains it.
Flows are always per-unit-time. Note which flows are controllable (a decision sets them) vs driven by other stocks.

### Step 4 — Locate the delays
Delays live in three places: (a) between deciding to change a flow and the flow actually changing, (b) between a flow changing and the stock responding, (c) between the stock changing and anyone perceiving it. Mark each significant delay with magnitude.

### Step 5 — Compute net rate and direction
For each stock at the current moment: net rate = inflow − outflow. Positive → stock rising; negative → falling; near zero → in dynamic equilibrium (which may still be at the wrong level).

### Step 6 — Sketch behavior over time
Determine the shape each key stock will follow given its flow structure:
- Constant net inflow → linear rise.
- Inflow proportional to the stock → exponential.
- Inflow that saturates as stock grows → S-curve.
- Flows controlled by delayed perception of the stock → oscillation / overshoot.
- Outflow only → decay toward a floor.
Describe the curve and the structural reason for it.

### Step 7 — Answer the lag question
State explicitly: if someone changes flow X today, how long until stock Y meaningfully moves, and what happens in the interim. This is usually the insight the model exists to produce.

### Step 8 — Intervention read (optional)
For a proposed intervention, identify whether it acts on a flow or a stock, where delays will defer its effect, and whether the stock's inertia will make it overshoot or undershoot. Hand off feedback-loop questions to `systems_feedback_loop_identifier.md` and leverage questions to `systems_leverage_point_analysis.md`.

---

## False-Positive Prevention

1. **Stock/flow confusion.** The single most common error. Re-test every variable: does it carry a per-time unit (flow) or is it a level that persists (stock)? "Revenue" is a flow; "cash in bank" is a stock.
2. **Inflow-only modeling.** Modeling what fills a stock and ignoring what drains it. Always ask "what's the outflow?" — attrition, decay, depreciation, forgetting, churn.
3. **Instant-response assumption.** Treating a stock as if it jumps when a flow changes. Stocks integrate flows over time; that's the whole point. If your model has no lag between flow and stock, re-check.
4. **Missing perception delay.** Decisions are made on *perceived* stock levels, which lag *actual* levels. Overshoot and oscillation usually come from this delay. If you see oscillation in reality but none in your model, you're missing a perception delay.
5. **False precision.** Stating "the stock will reach 4,200 in month 7" without a calibrated model. State the shape and the structural cause; give numeric ranges only where data supports them.
6. **Boundary leakage.** Treating something as an external input when it's actually driven by an internal stock on a longer timescale. Surface it and decide whether to internalize it.
7. **Stock with no flows.** If you can't name a flow for a stock, either it's not actually changing (drop it) or you haven't found the mechanism (keep looking).
8. **Table theater.** A stocks/flows table with no behavior-over-time explanation is decoration. The behavior sketch and lag answer are the deliverable.

---

## Output Format

```
# Stock-and-flow model — [system / problem]

## Quantity behaving wrong
[The key stock and its observed trajectory over time]

## Boundary
- Internal stocks (modeled): [list]
- External inputs (exogenous): [list with one-line justification]

## Stocks
| # | Stock (level)      | Initial level / range | Net rate now | Direction      |
|---|--------------------|-----------------------|--------------|----------------|
| 1 | [noun phrase]      | [value or "unknown"]  | +/− [rate]   | rising/falling |
| … |                    |                       |              |                |

## Flows
| Stock | Inflow(s) (rate)        | Outflow(s) (rate)       | Controllable? |
|-------|-------------------------|-------------------------|---------------|
| [1]   | [rate, per time]        | [rate, per time]        | inflow: yes   |
| …     |                         |                         |               |

## Delays
| # | Where the delay sits                        | Magnitude        |
|---|---------------------------------------------|------------------|
| 1 | flow change → stock response                | medium (~3 mo)   |
| 2 | actual stock → perceived stock              | long (~2 quarters)|
| … |                                             |                  |

## Behavior over time
| Stock | Curve shape          | Structural reason                          |
|-------|----------------------|--------------------------------------------|
| [1]   | overshoot-and-correct| flows set on delayed perception of level   |
| …     |                      |                                            |

## The lag answer
[If flow X changes today, stock Y meaningfully moves after ~D, because… In the interim…]

## Intervention read (optional)
[Does the proposed intervention act on a flow or a stock? Where do delays defer its effect? Will inertia cause overshoot/undershoot?]
```

---

## Verification

- [ ] 2–6 stocks, each passing the "persists if flows stop" test.
- [ ] Every stock has at least one named inflow and the outflow is considered (not silently dropped).
- [ ] Flows are expressed as rates (per unit time); stocks are levels.
- [ ] Delays are marked with magnitude or explicitly noted negligible.
- [ ] Net rate and direction stated for each stock.
- [ ] Behavior-over-time curve named for each key stock with its structural cause.
- [ ] The flow-to-stock lag question is answered explicitly.
- [ ] No stock/flow confusion; no inflow-only models.
- [ ] No false numeric precision beyond what data supports.
