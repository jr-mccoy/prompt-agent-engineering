---
title: "KPI Tree Decomposition — Break an Outcome Metric into Drivers That Multiply or Add Back Up"
category: data-analytics/framing-and-metrics
description: "Decompose one outcome metric (revenue, gross margin, active accounts) into a driver tree whose branches reconcile arithmetically to the parent, mark which drivers a team can move, size each driver's contribution to a recent change, and name the dominant driver — so a KPI conversation becomes a driver conversation."
techniques:
  - DT-01
  - NE-11
  - DP-06
  - QA-01
difficulty: intermediate
tags:
  - kpi-tree
  - driver-tree
  - metric-decomposition
  - business-analytics
  - variance-attribution
  - operating-metrics
  - what-drives-revenue
  - setting-team-targets
  - too-many-causes
updated: "2026-09-24"
related_prompts:
  - domain-data-analytics/framing-and-metrics/analytics_metric_definition_spec.md
  - domain-data-analytics/analysis-and-sql/analytics_metric_movement_investigation.md
  - domain-agentic-resources/skills/data-engineering/kpi-dashboard-design/SKILL.md
---

# KPI Tree Decomposition

**Objective:** Build a driver tree for one outcome metric in which every level
reconciles exactly to the level above, each leaf has an owner who can move it, and
a recent change in the outcome is attributed to named drivers with their share.

**When to Use:**
- Leadership tracks one top-line number and teams cannot see which lever is theirs.
- The outcome moved and "it's a lot of things" is the current explanation.
- You are setting team targets and need them to sum to the company target.
- Before designing a dashboard, to decide which drivers deserve a tile.

**When NOT to use:**
- You need dashboard layout, chart choice, and refresh patterns —
  `domain-agentic-resources/skills/data-engineering/kpi-dashboard-design/`.
- You are decomposing a budget-vs-actual variance for finance into price/volume/mix —
  `domain-finance/corporate-finance-fpa/finance_budget_variance_investigator.md`.
- You are decomposing ROE — `domain-finance/financial-statement-analysis/finance_dupont_decomposition.md`.
- The metric itself is not yet defined — write `analytics_metric_definition_spec.md` first.
- You are choosing the product's north-star metric —
  `domain-product-management/prompts/product_north_star_metric_definition.md`. This prompt
  decomposes an existing outcome into drivers that add up to it.

## Inputs / Context

1. **The outcome metric** and its spec (or best current definition).
2. **Two periods to compare**, with values for the outcome and any drivers you have.
3. **The org chart of ownership** — which team runs which part of the funnel or P&L.
4. **Known structural changes** between the periods (pricing, packaging, new market).

## Method

1. **Choose the decomposition identity (DT-01).** Each split must be either:
   - **multiplicative** — Revenue = Customers × Orders/Customer × Revenue/Order; or
   - **additive** — Revenue = New + Expansion − Contraction − Churn + Existing base.
   State which, per node. Do not mix both at one node.

2. **Build two to four levels deep.** Stop where the leaf is something a named team
   can act on this quarter. A leaf nobody owns is a note, not a driver.

3. **Write the formula at every node (NE-11).** Every child set must reconcile to its
   parent to within rounding, for both periods. Check it numerically.

4. **Attribute the change.**
   - Additive nodes: the change is the sum of the child changes — direct.
   - Multiplicative nodes: use log decomposition so contributions sum exactly:
     `share_i = ln(x_i,t1 / x_i,t0) / ln(Y_t1 / Y_t0)`. State the method; sequential
     substitution gives order-dependent answers and should be flagged if used.
   - Mark any driver where the change is inside its normal week-to-week noise band.

5. **Name the dominant driver (DP-06).** One sentence: "Most of the change came from
   X, which moved from a to b." If two drivers offset each other, say that too — an
   unchanged parent can hide two large opposite moves.

6. **Tag each leaf** with owner, controllability (direct / influence / none), and
   whether it is **measured** or **derived** (computed as a residual). Residual leaves
   absorb every error in the tree; flag them.

7. **Verify the tree (QA-01).** Recompute the top from the leaves; confirm the
   attributions sum to 100% of the change; check that no leaf is double-counted
   across two branches.

## Output Format

```
# KPI tree — [outcome]   Periods: [t0] vs [t1]

## Tree
[outcome] = [identity]
├── [driver] = ...
│   ├── [leaf]  (owner, controllability, measured|derived)

## Values and reconciliation
| Node | t0 | t1 | Δ | Identity check (t0/t1) |
|---|---|---|---|---|

## Attribution of Δ[outcome]
| Driver | Contribution | Share | Inside noise band? |
|---|---|---|---|
Method: [log decomposition | additive | sequential — order stated]

## Dominant driver
## Offsetting moves
## Leaves without owners / derived leaves
## Confidence: [High | Medium | Low] — because [...]
```

## Verification

- [ ] Every node states whether it is additive or multiplicative.
- [ ] Children reconcile to parent for both periods.
- [ ] Attributions sum to 100% of the parent change.
- [ ] The attribution method is named.
- [ ] Every leaf has owner, controllability, and measured/derived tags.
- [ ] Noise bands are stated for the drivers used in the conclusion.

## False-Positive Prevention

1. **A tree that does not add up is an org chart.** If the leaves do not reconcile to
   the root, attribution is meaningless. Check the arithmetic before the story.
2. **Order-dependent attribution.** Sequential substitution assigns the interaction
   term to whichever driver you change first. Use log or Shapley-style methods, or
   report the order.
3. **Mix shift masquerading as a rate change.** If revenue per order rose because the
   customer mix shifted toward a high-price segment, the per-segment rate may not have
   moved at all. Split by segment before crediting a pricing team.
4. **Residual leaves soaking up errors.** "Other" computed as parent minus children
   will look like a real driver. Label it derived.
5. **Unowned leaves presented as levers.** "Market growth" is context, not a driver
   a team can be held to.
6. **Treating noise as signal.** A driver that moved 1.2% when it normally moves ±2%
   week to week did not "contribute" in any meaningful sense.

## Example Output

```
# KPI tree — Monthly subscription revenue   Periods: Jul 2026 vs Aug 2026

## Tree
Revenue = Paying accounts × Avg seats per account × Revenue per seat
├── Paying accounts = Prior accounts + New − Churned        (additive)
│   ├── New accounts          (Growth, direct, measured)
│   └── Churned accounts      (CS, influence, measured)
├── Avg seats per account     (CS/Sales, influence, measured)
└── Revenue per seat          (Pricing, direct, derived = revenue ÷ seats)

## Values and reconciliation
| Node | Jul | Aug | Δ | Identity check |
|---|---|---|---|---|
| Revenue | $1,200,000 | $1,164,000 | −$36,000 | 1,000×12×100 ✓ / 1,010×11.8×97.66 ✓ |
| Paying accounts | 1,000 | 1,010 | +10 | 1,000+60−50 ✓ |
| Seats per account | 12.0 | 11.8 | −0.2 | measured |
| Revenue per seat | $100.00 | $97.66 | −$2.34 | derived |

## Attribution of Δrevenue (ln(1,164/1,200) = −0.0305)
| Driver | ln ratio | Share | Inside noise band? |
|---|---|---|---|
| Paying accounts | +0.0100 | −33% (offsets) | No |
| Seats per account | −0.0168 | +55% | No (normal ±0.08 seats) |
| Revenue per seat | −0.0237 | +78% | No |
Method: log decomposition; shares sum to 100%.

## Dominant driver
Revenue per seat fell from $100.00 to $97.66 and explains ~78% of the decline.

## Offsetting moves
Account growth (+10 net) offset about a third of the decline.

## Leaves without owners / derived leaves
Revenue per seat is derived. Before crediting Pricing, split by plan: the August
annual-plan promo moved new seats onto a 20% discount [verify with billing export].

## Confidence: Medium — tree reconciles exactly; per-seat driver not yet split by plan mix.
```

## Techniques Used

- **DT-01 Hierarchical Task Breakdown** — outcome split level by level into ownable leaves.
- **NE-11 Embedded Calculation Formulas** — identity at every node and a log-decomposition formula for attribution.
- **DP-06 Dominant Driver Identification** — one named driver carries the explanation.
- **QA-01 Self-Verification** — recompute the root from leaves and confirm attribution sums to 100%.

## Related Prompts

- `domain-data-analytics/framing-and-metrics/analytics_metric_definition_spec.md` — specify each node before trusting it.
- `domain-data-analytics/analysis-and-sql/analytics_metric_movement_investigation.md` — when a driver moved and you need the cause.
- `domain-agentic-resources/skills/data-engineering/kpi-dashboard-design/SKILL.md` — turning the tree into a dashboard.
