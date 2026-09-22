# Domain: Advertising (Image Prompt Set)

**Purpose:** Tier-1 structured meta-prompts for generating advertising image prompts across 17 industry verticals with strict print/screen controls.

## Included Prompt Files (17)

- `advertising_automotive_vehicle.md`
- `advertising_b2b_professional_services.md`
- `advertising_beauty_cosmetics.md`
- `advertising_education_online_course.md`
- `advertising_event_conference.md`
- `advertising_fashion_apparel.md`
- `advertising_financial_services_fintech.md`
- `advertising_food_beverage_launch.md`
- `advertising_health_wellness_supplements.md`
- `advertising_home_improvement_furniture.md`
- `advertising_local_small_business.md`
- `advertising_nonprofit_cause_marketing.md`
- `advertising_pet_products_services.md`
- `advertising_premium_service_provider.md`
- `advertising_real_estate_property.md`
- `advertising_tech_product_saas.md`
- `advertising_travel_hospitality.md`

## Standard Prompt Contract (applies to every file)

Each advertising prompt includes:
- interview intake for product, audience, key message, palette, CTA
- print/screen output locking
- anti-UI constraints
- anti-mockup constraints
- redundant no-gradient/no-shadow rules
- model-specific sections for DALL-E, Midjourney, Stable Diffusion, Gemini
- final validation checklist

## 8-Technique Confirmation (all files)

All 17 prompts explicitly include and enforce:
- SV-11 Terminology Steering
- SV-12 Grid Forcing + Enumerated Slots
- SV-13 Constraint Redundancy
- SV-14 Negative Space Control
- SV-15 Allowed vs Forbidden Distinction
- SV-16 Physical Context Anchoring
- SV-17 Deliverables Locking
- SV-18 Image Validation Checklist

## Session 10 Cross-Links (visual-planning)

These advertising prompts cross-link to Session 10 visual-planning references:
- `domain-presentations/visual-planning/visual_frontier_map.md`
- `domain-presentations/visual-planning/visual_qa_harness.md`
- `domain-presentations/visual-planning/visual_workflow_router.md`

## Route elsewhere for

**This domain is an image-prompt set, not an advertising domain.** Every file here builds
a prompt for *generating an advertising image* — the 8 image techniques (SV-11…SV-18),
print/screen locking, anti-mockup constraints, per-model sections. Ad strategy, copy,
targeting and testing were never in scope, and they already exist elsewhere. The absence
of this section is why that was not obvious.

| You need | Go to |
|---|---|
| Ad creative concepts, angles, headline variants at scale | `domain-agentic-resources/skills/marketing/ad-creative/` |
| Landing page, hero, pricing-page and CTA copy | `domain-agentic-resources/skills/marketing/copywriting/` |
| Channel selection, platform targeting, budget split | `domain-agentic-resources/skills/marketing/paid-ads/` |
| Creative testing and experiment design | `domain-agentic-resources/skills/marketing/ab-test-setup/` |
| Audience, ICP, persona and jobs-to-be-done definition | `domain-agentic-resources/skills/marketing/customer-research/` |
| Persuasion and behavioural principles applied to copy | `domain-agentic-resources/skills/marketing/marketing-psychology/` |
| Ad-to-page message match | `domain-agentic-resources/skills/marketing/page-cro/` (see `references/experiments.md`) |
| Campaign briefs, launch plans, go-to-market | `domain-business-strategy/go-to-market/` |
| Objection handling in copy and collateral | `domain-agentic-resources/skills/marketing/sales-enablement/` |
| Any other image-generation work | `domain-image-generation/` |

## Backlog Status

- ✅ Advertising image-generation prompts complete (17/17).
- Ad strategy and copy are **deliberately out of scope** — see *Route elsewhere for*.
