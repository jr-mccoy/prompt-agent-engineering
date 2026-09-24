# Domain: Advertising

**Purpose:** Two sets of practitioner prompts for paid advertising:

1. **Image prompts (17, root)** — Tier-1 structured meta-prompts for generating advertising
   images across 17 industry verticals with strict print/screen controls.
2. **Campaign prompts (5, `campaign/`)** — scoped, single-run deliverables for taking an ad
   campaign from test design to launch: the copy test matrix, the UGC video script, the
   placement spec checklist, the media plan, and the pre-launch claims review.

These are **prompts, not skills.** The marketing skills in `domain-agentic-resources/skills/marketing/`
remain the home for open-ended, multi-session work (volume copy generation, channel strategy,
experimentation programmes, tracking). Each campaign prompt states what it is distinct from.

## Campaign Prompts — `campaign/` (5)

Prefix `adcampaign_`. They chain: matrix → placement checklist → media plan → UGC script →
claims review, and each can run alone.

| File | Produces | Distinct from |
|---|---|---|
| `campaign/adcampaign_copy_variant_matrix.md` | Angle × audience × format grid, one variable per group, hypotheses, kill list; every limit `[VERIFY current platform spec]` | `ad-creative` skill (volume variants, iteration), `ab-test-setup` (stats) |
| `campaign/adcampaign_ugc_video_script_beats.md` | Creator brief, three hooks, timed beat sheet, do-not-say list, rights and disclosure items to settle | `video` skill (AI/programmatic production), `content_video_shot_list_preproduction` |
| `campaign/adcampaign_placement_spec_checklist.md` | Per-placement spec checklist, every value blank with source + date, pre-upload gate | `ad-creative/references/platform-specs.md` (static table), `paid-ads` setup checklists |
| `campaign/adcampaign_media_plan_budget_allocation.md` | Break-even CPA, test-budget sizing, allocation with reasons, pacing, pre-committed kill/hold/scale rules | `paid-ads` skill (channels, targeting, bidding), `workflow_marketing_campaign_brief_development` |
| `campaign/adcampaign_claims_compliance_review.md` | Claims register vs. substantiation, disclosure and restricted-category questions, ranked findings, counsel queue | `domain-legal/` (counsel's opinion), `quality_slop_ad_copy` (persuasiveness) |

**Campaign-prompt guards (all five):**
- **No platform spec from memory.** Character limits, dimensions, durations, safe zones, and
  learning-period rules are marked `[VERIFY current platform spec]` / `[VERIFY current platform
  guidance]` and filled only from current official documentation, with source and date.
- **No invented benchmarks.** CPA, CPC, CTR, and conversion rates come from the advertiser's own
  data or a dated source; otherwise `[MEASURE]`.
- **No regulatory rule asserted.** Substantiation, disclosure, and restricted-category rules are
  raised as questions for counsel and the platform's current policy — never stated, never
  "cleared."

## Image Prompts — root (17)

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

## Standard Prompt Contract (applies to every image prompt)

Each advertising prompt includes:
- interview intake for product, audience, key message, palette, CTA
- print/screen output locking
- anti-UI constraints
- anti-mockup constraints
- redundant no-gradient/no-shadow rules
- model-specific sections for DALL-E, Midjourney, Stable Diffusion, Gemini
- final validation checklist

## 8-Technique Confirmation (all 17 image prompts)

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
- [`visualplan_capability_frontier_map.md`](../domain-presentations/visual-planning/visualplan_capability_frontier_map.md)
- [`visualplan_visual_qa_harness.md`](../domain-presentations/visual-planning/visualplan_visual_qa_harness.md)
- [`visualplan_modality_router.md`](../domain-presentations/visual-planning/visualplan_modality_router.md)

## Route elsewhere for

**Scope:** advertising images (root) and campaign deliverables (`campaign/`). Open-ended
marketing work — volume generation, channel strategy, experimentation programmes, tracking,
conversion optimisation — stays with the marketing skills.

| You need | Go to |
|---|---|
| Dozens of headline/description variants for a chosen angle, or iteration from performance data | `domain-agentic-resources/skills/marketing/ad-creative/` |
| Channel selection, platform targeting, bidding, ongoing optimisation, retargeting | `domain-agentic-resources/skills/marketing/paid-ads/` |
| Sample size, significance, run length, or an experimentation programme | `domain-agentic-resources/skills/marketing/ab-test-setup/` |
| Conversion tracking, pixels, attribution setup | `domain-agentic-resources/skills/marketing/analytics-tracking/` |
| Landing page, hero, pricing-page and CTA copy | `domain-agentic-resources/skills/marketing/copywriting/` |
| Ad-to-page message match and full landing-page CRO | `domain-agentic-resources/skills/marketing/page-cro/` (see `references/experiments.md`) |
| AI-generated, avatar, or programmatic video production | `domain-agentic-resources/skills/marketing/video/` |
| Audience, ICP, persona and jobs-to-be-done definition | `domain-agentic-resources/skills/marketing/customer-research/` |
| Persuasion and behavioural principles applied to copy | `domain-agentic-resources/skills/marketing/marketing-psychology/` |
| Objection handling in copy and collateral | `domain-agentic-resources/skills/marketing/sales-enablement/` |
| Campaign briefs, launch plans, go-to-market strategy | `domain-business-strategy/go-to-market/` |
| Scoring finished ad copy or a video script | `domain-professional-writing/content-quality/quality_slop_ad_copy.md`, `quality_slop_video_script.md` |
| A legal opinion on a claim, disclosure, or regulated category | `domain-legal/` — the claims review prepares the counsel queue; it does not clear |
| Any other image-generation work | `domain-image-generation/` |

## Backlog Status

- ✅ Advertising image-generation prompts complete (17/17).
- ✅ Campaign prompts (5/5): copy matrix, UGC script, placement spec checklist, media plan, claims review.
