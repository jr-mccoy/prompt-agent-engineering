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
├── prompts/      # 8 product-management prompts
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
| [`product_planning_coding_roadmap.md`](prompts/product_planning_coding_roadmap.md) | You need a sequenced build roadmap |

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
