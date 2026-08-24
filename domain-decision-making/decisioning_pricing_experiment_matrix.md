---
title: "Pricing Experiment Matrix"
category: decision-making
description: "Design a pricing experiment matrix that tests price changes — ladders, bundle variants, willingness-to-pay probes — without tanking revenue. Output: an experiment grid with hypotheses per cell, sample-size sanity checks, success and failure thresholds, blast-radius limits, and rollback triggers. Optimized for picking the right experiment to run, not for choosing a single new price."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-03
  - CM-02
  - DS-02
  - DS-06
  - QA-01
difficulty: advanced
tags:
  - decision-making
  - pricing
  - experimentation
  - revenue
  - willingness-to-pay
  - rollback
updated: "2026-04-26"
related_prompts:
  - domain-decision-making/decisioning_comprehensive_rapid_tradeoff_analyzer.md
  - domain-decision-making/decisioning_multi_constraint_optimizer.md
  - domain-business-strategy/startup/monetization_pricing_strategy.md
  - domain-business-strategy/analysis/business_model_canvas_analysis.md
---

# Pricing Experiment Matrix

**Objective:** Design a pricing experiment matrix that lets the user test meaningful price changes — ladders (raising or lowering by step), bundle variants (re-grouping features), and willingness-to-pay probes (asking the market directly) — without putting more than a defined slice of revenue at risk. The output is an experiment grid in which every cell has a hypothesis, a measurable threshold for success and failure, an estimated sample size, a blast-radius cap, and a pre-committed rollback trigger.

**When to Use:**
- The org is considering a price change and wants to test it on a slice before applying it to the whole base.
- A new tier or bundle is being designed and the team wants to evaluate multiple structures in parallel.
- Margins are under pressure and pricing power is unknown.
- Competitor moves have shifted the reference price and the user does not know how their base will respond.

**When NOT to use:**
- Annual or contract-locked pricing where experiments cannot be safely cycled. Use a single-decision pricing analysis instead.
- The user already knows the new price and just wants help with rollout. Use a launch-plan prompt.
- The user has fewer than ~200 active customers in the target segment — experiments will not produce statistically interpretable results. Run qualitative WTP interviews instead.

**Audience:** Founders, pricing leads, growth PMs, finance partners, monetization PMs.

---

## Inputs / Context

1. **Current pricing structure.** All tiers, prices, billing periods, discounts, bundles. One short table.
2. **The pressure or opportunity driving the experiment.** Margin compression, competitor move, new feature, churn signal, expansion stall.
3. **Active customer count by tier and approximate revenue per tier.** Needed for sample-size and blast-radius calculations.
4. **Acceptable revenue at risk.** Express as a percentage of monthly recurring revenue (MRR) or annualized revenue. Hard cap.
5. **Time horizon for the experiment.** In weeks. Most pricing experiments need 4–12 weeks to read net-of-churn signal.
6. **Constraints.** Contractual price-protection clauses, regulatory requirements, fairness commitments to existing customers, comp-plan implications.
7. **Optional: prior pricing experiments.** What was tested, what was learned, what failed.

If the user cannot specify acceptable revenue at risk, **stop** and ask. The whole matrix depends on a hard ceiling.

---

## Constraints

### Must
- Produce three categories of experiment cells: **price ladders** (same product, different price points), **bundle variants** (same price, different feature grouping), **WTP probes** (qualitative or instrumented signals — landing-page price tests, exit-intent surveys, sales-quoted ranges).
- Every cell must specify: hypothesis, treatment, control, primary metric, success threshold, failure threshold, blast-radius cap (max revenue or customer count exposed), minimum sample size, rollback trigger, time horizon.
- The total revenue exposure across all simultaneous cells must not exceed the user's stated acceptable revenue at risk. Show the math.
- Every cell must have a rollback trigger that can be detected within the experiment window and acted on in less than 7 days.
- For each price ladder cell, indicate whether existing customers are grandfathered. Default: yes for raises, optional for cuts.
- Recommend a sequence — which cells to run first, second, third — based on (a) information value, (b) reversibility, (c) blast radius.
- End with a "kill / scale / iterate" decision template the user will fill in at the end of the experiment window.

### Must Not
- Recommend running all cells in parallel if combined exposure exceeds the cap.
- Treat WTP probes as a substitute for live price tests. They are signal, not proof.
- Recommend price tests on regulated or contractually price-locked customer segments.
- Assume churn lag is the same as conversion lag. Churn signal often takes 2–3x longer to show up than conversion signal — the time horizon must reflect this.
- Use "uplift" as the only success metric. A revenue uplift accompanied by a churn spike is not a win.
- Output an experiment cell whose rollback trigger cannot be detected inside the experiment window.

---

## Instructions

### Step 1 — Restate the pressure and the cap
One paragraph: what's driving the experiment, what is the acceptable revenue at risk in dollars and percent, what is the time horizon, what constraints apply.

### Step 2 — Generate candidate experiment cells
For each of the three categories, generate 2–4 candidate cells. Be specific:

- **Price ladders:** "Raise Pro tier from $X to $Y for new customers in [segment] for [horizon]." Include both upward and downward ladders if both are plausible.
- **Bundle variants:** "Move feature F from Pro to Plus and re-price Plus from $X to $Y." Or "Create a new entry tier at $X with feature subset {A, B, C}."
- **WTP probes:** "Run a landing-page A/B test showing $X vs $Y price for new sign-ups, measuring click-through-to-checkout." Or "Have sales quote within range $X–$Y on next 50 deals and log accept/reject."

For each cell, write a one-sentence hypothesis in the form: "If we [treatment], then [primary metric] will [direction] by [magnitude] within [horizon] without [guardrail breach]."

### Step 3 — Sample-size sanity check
For each cell with a quantitative test, estimate minimum sample size as a function of (a) baseline conversion or retention rate, (b) minimum detectable effect the user cares about, (c) significance level (default 95%). Use a normal-approximation formula or refer the user to a calculator. State the assumption explicitly.

If a cell's required sample exceeds the available population in the cell's blast-radius cap, **flag it** as underpowered and recommend either widening the cell, lengthening the horizon, or replacing with a qualitative WTP probe.

### Step 4 — Blast-radius accounting
Build a small revenue-at-risk table. Columns: Cell | Customers exposed | Revenue exposed | % of MRR | Cumulative % of MRR.

If cumulative % of MRR exceeds the user's cap, sequence cells instead of running in parallel, or shrink cell exposure. Show the trade-off.

### Step 5 — Define thresholds and triggers per cell
For each cell:
- **Success threshold:** the primary metric outcome that would justify scaling.
- **Failure threshold:** the primary metric outcome that would justify killing.
- **Guardrail thresholds:** secondary metrics whose breach would force rollback even on a "successful" primary metric. Typical guardrails: gross churn rate, NRR, support volume, refund rate, sales-cycle length.
- **Rollback trigger:** the operational condition (e.g., "churn rate at 4 weeks > X%") that fires the rollback. Must be detectable inside the experiment window.

### Step 6 — Sequence the cells
Order cells by:
1. **Information value:** cells whose result will most change the next decision come first.
2. **Reversibility:** more-reversible cells (price test on new customers, no grandfathering needed) come earlier.
3. **Blast radius:** smaller-blast-radius cells run in parallel; larger ones are sequenced one at a time.

Output a recommended sequence with rationale.

### Step 7 — Decide-at-end template
Output the template the user will use at the end of each cell's window:
- Outcome on primary metric vs. threshold.
- Outcome on each guardrail vs. threshold.
- Net assessment: **scale** (roll to broader segment with same parameters), **iterate** (modify and re-test), **kill** (rollback and document why).
- One-paragraph learning for the next experiment.

---

## False-Positive Prevention

1. **Conversion-uplift mirage.** A new lower price often produces a short-term conversion uplift that reverses once early adopters churn at higher rates. Always pair conversion with retention guardrails over a longer horizon.
2. **Selection bias from new-only tests.** Testing on new customers tells you about acquisition, not your installed base. Do not generalize a new-customer ladder result to existing customers.
3. **WTP-probe overreach.** A survey response or click-through is intent, not commitment. Treat WTP probes as inputs to designing live tests, not as decisions.
4. **Underpowered cells.** Running a cell that is mathematically incapable of detecting a meaningful effect produces noise that gets interpreted as signal. Flag and either widen, lengthen, or kill.
5. **Sequential-cell contamination.** Running cell B before cell A's effect has stabilized causes attribution confusion. Honor the time horizon.
6. **Grandfathering forgotten on raises.** Raising a price without grandfathering existing customers can spike churn and obliterate the revenue uplift. Default to grandfathering on raises.
7. **Regulatory or contractual blindness.** Some segments cannot be experimented on. Filter cells against the constraints input.
8. **Comp-plan and channel-conflict blindness.** A new tier can break sales comp plans or channel-partner economics. Flag if the experiment affects either.
9. **Churn-lag underestimate.** A four-week experiment cannot read annual-renewal churn. Match horizon to the churn cycle of the affected segment, or tag the result as preliminary.

---

## Output Format

```
# Pricing experiment matrix — [date]

**Pressure / opportunity:** [one paragraph]
**Acceptable revenue at risk:** $[X] / [Y]% of MRR
**Time horizon:** [weeks]
**Constraints:** [contractual / regulatory / comp-plan]

## Experiment cells

### Price ladders
| # | Treatment | Hypothesis | Primary metric | Success / failure thresholds | Guardrails | Sample size needed | Blast radius (cust / $) | Rollback trigger |
|---|-----------|------------|----------------|------------------------------|------------|--------------------|--------------------------|------------------|
| L1 | [...] | [...] | [...] | [up X% / down X%] | [churn / NRR / refund] | [N] | [N cust / $X] | [condition] |

### Bundle variants
| # | Treatment | Hypothesis | Primary metric | Thresholds | Guardrails | Sample size | Blast radius | Rollback trigger |
|---|-----------|------------|----------------|------------|------------|-------------|--------------|------------------|

### WTP probes
| # | Treatment | What it tells us | What it does NOT tell us | Sample size | Cost |
|---|-----------|------------------|---------------------------|-------------|------|

## Blast-radius accounting

| Cell | Customers exposed | Revenue exposed | % of MRR | Cumulative % |
|------|--------------------|-----------------|----------|---------------|
| [...]| [...]              | [...]           | [...]    | [...]         |

[If cumulative > cap: recommended sequencing changes here.]

## Recommended sequence
1. [Cell ID] — rationale ([information value / reversibility / blast])
2. [Cell ID] — rationale
3. [Cell ID] — rationale

## Decide-at-end template (for each cell)

- Cell: [ID]
- Primary metric: [actual] vs. [success / failure threshold]
- Guardrail breaches: [list]
- Decision: [scale / iterate / kill]
- One-paragraph learning: [...]
```

---

## Verification

- [ ] Three categories of cells (ladders, bundles, WTP probes) are present.
- [ ] Every cell has hypothesis, primary metric, success and failure thresholds, guardrails, sample size, blast radius, rollback trigger, and time horizon.
- [ ] Cumulative revenue exposure does not exceed the user's stated cap.
- [ ] Underpowered cells are flagged.
- [ ] Grandfathering is addressed for every price-raise cell.
- [ ] Sequence is provided with explicit rationale per cell.
- [ ] Decide-at-end template is present and includes a "kill" option.
- [ ] No cell relies on uplift alone — every cell has at least one retention or guardrail metric.
- [ ] Constraints (regulatory, contractual, comp-plan) have been applied to the cell list.
