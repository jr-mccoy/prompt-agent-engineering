# Domain: Product Management

**Purpose:** The product manager's working documents — deciding what to build,
writing it down so a team can build it, and checking whether the write-up is
good enough to act on.

**Audience scope:** the **product**. One of the repository's five work-domain
tracks (see [Which domain does this belong in?](../CLAUDE.md)):

| Track | Domain |
|---|---|
| Self | `domain-personal-development/` |
| Individual execution | `domain-productivity/` |
| Team delivery | `domain-engineering-workflows/` |
| **Product** | **this domain** |
| Org / company | `domain-business-strategy/` |

> **The craft guide that lived here moved.** The dissolved domain's README was a
> 1,100-line field guide — document anti-patterns, a certainty framework for
> business projections, and skeleton templates for five recurring document types.
> It now sits beside the business-writing prompts it supports:
> [`domain-professional-writing/field_guide.md`](../domain-professional-writing/field_guide.md).

> **Renamed from `domain-professional-communication`.** That name described
> nothing the directory contained: every prompt was prefixed `product_` or
> `design_`, and six of ten duplicated prompts in two other domains. The
> duplicates were removed, the design and hiring prompts were routed to
> `domain-frontend-development/` and `domain-hr-management/`, the proposal
> artifacts to `domain-professional-writing/business-writing/`, and what
> remained is product management.

---

## Contents

```
domain-product-management/
├── prompts/      # 14 product-management prompts
├── templates/    # PRD template
└── README.md
```

| Prompt | Use when |
|---|---|
| [`product_create_prd.md`](prompts/product_create_prd.md) | You need a PRD and want to be interrogated into it, MVP-first |
| [`product_rigorous_prd_evaluation_and_scoring.md`](prompts/product_rigorous_prd_evaluation_and_scoring.md) | A PRD exists and you want it scored against a rubric before it ships |
| [`product_feature_requirements_extraction.md`](prompts/product_feature_requirements_extraction.md) | You have raw stakeholder conversation notes and need structured requirements out of them |
| [`product_market_size_calculator.md`](prompts/product_market_size_calculator.md) | You need TAM/SAM/SOM, rapid or comprehensive |
| [`product_competitor_feature_teardown.md`](prompts/product_competitor_feature_teardown.md) | You need a feature-by-feature matrix across 3+ named competitors and a defensible position |
| [`product_product_idea_vetting_will_it_fly_or_flop.md`](prompts/product_product_idea_vetting_will_it_fly_or_flop.md) | An idea needs a go/no-go before you invest in it |
| [`product_delivery_sprint_planner.md`](prompts/product_delivery_sprint_planner.md) | You are planning a cross-functional delivery sprint from the product side |
| [`product_planning_coding_roadmap.md`](prompts/product_planning_coding_roadmap.md) | You need a sequenced build roadmap, with an optional scoring pass where the order is not dependency-forced |
| [`product_opportunity_solution_tree.md`](prompts/product_opportunity_solution_tree.md) | You have an outcome and a pile of feature requests and no way to relate them |
| [`product_north_star_metric_definition.md`](prompts/product_north_star_metric_definition.md) | Teams are optimising different numbers, or your headline metric is signups |
| [`product_user_story_splitting.md`](prompts/product_user_story_splitting.md) | A story will not fit an iteration, or refinement keeps producing "backend work" |
| [`product_launch_readiness_gate.md`](prompts/product_launch_readiness_gate.md) | A launch date is near and you need a cross-functional go/no-go with a real no available |
| [`product_feature_sunset_decision.md`](prompts/product_feature_sunset_decision.md) | Something should probably be removed and you need to know who depends on it first |
| [`product_pricing_experiment_matrix.md`](prompts/product_pricing_experiment_matrix.md) | You need to design pricing experiments: variables, test matrix, guardrails (moved from `domain-decision-making/` in coverage Wave 4) |

---

## Two sprint planners, on purpose

[`product_delivery_sprint_planner.md`](prompts/product_delivery_sprint_planner.md)
and
[`engineering_delivery_sprint_planner.md`](../domain-engineering-workflows/workflows/engineering_delivery_sprint_planner.md)
cover the same ceremony from different seats. Use the product one when you are
planning across functions and negotiating scope against a launch commitment; use
the engineering one when you are planning an engineering team's capacity and
work breakdown. If you only want one, start with the seat you actually occupy.

---

## Route elsewhere for

- **The full idea → shippable software pipeline** → [`domain-idea-to-product/`](../domain-idea-to-product/), which vendors copies of several prompts here into its stage directories
- **Company strategy, positioning, go-to-market** → [`domain-business-strategy/`](../domain-business-strategy/)
- **Executive briefs, proposals, status reports, business prose** → [`domain-professional-writing/business-writing/`](../domain-professional-writing/business-writing/)
- **Board decks and presentations** → [`domain-presentations/`](../domain-presentations/)
- **Stakeholder navigation and org politics** → [`domain-personal-development/prompts/stakeholder/`](../domain-personal-development/prompts/stakeholder/)
- **Team delivery process, incidents, definition-of-done** → [`domain-engineering-workflows/`](../domain-engineering-workflows/)
- **Visual and design direction** → [`domain-frontend-development/design-direction/`](../domain-frontend-development/design-direction/)
