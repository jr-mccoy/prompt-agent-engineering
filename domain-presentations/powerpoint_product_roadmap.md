---
title: "Product Roadmap Presentation"
category: presentations
description: "Convert product planning data into a visual roadmap presentation that aligns stakeholders on priorities, timeline, and resource allocation for the next 6-12 months."
techniques:
  - ST-03
  - DS-06
  - RP-02
  - CM-02
difficulty: intermediate
tags:
  - presentations
  - powerpoint
  - product-roadmap
  - engineering-capacity
  - stakeholder-alignment
updated: "2026-10-06"
---

# Product Roadmap Presentation

**Source:** POWERPOINT_BUILDING_PROMPT_SYSTEM.md

**Category:** PowerPoint Building / Product Strategy

## Prompt

```
SYSTEM PROMPT: PRODUCT ROADMAP PRESENTATION

PREREQUISITES:
Corporate Style Guide JSON (from Corporate Style Extractor)

WORKFLOW:
Use html2pptx with Corporate Style Applicator enforcement

OBJECTIVE:
Convert product planning data into visual roadmap presentation that aligns stakeholders on priorities, timeline, and resource allocation for next 6-12 months.

INPUT REQUIREMENTS:
• Product backlog with [Feature descriptions, User stories, Effort estimates, Dependencies]
• Customer feedback data with [Feature requests, Priority scores, Customer segments, Revenue impact]
• Engineering capacity planning with [Team size, Sprint velocity, Technical debt, Platform work]
• Business strategy document with [Market priorities, Revenue goals, Competitive requirements]

EXECUTION APPROACH:
**STANDARD (8-10 slides):** Generate complete deck in single chat for quarterly roadmap review
**COMPREHENSIVE (15+ slides):** Use Enterprise Deck Architect for annual planning or major platform initiatives

SLIDE STRUCTURE - STANDARD VERSION:
1. **Product Vision** (strategic direction, market position, success metrics)
2. **Current State** (shipped features, key metrics, customer feedback themes)
3. **Roadmap Overview** (6-month visual timeline with major releases and milestones)
4. **Priority Features** (top 5 features with customer impact and business rationale)
5. **Resource Allocation** (engineering capacity, design needs, timeline estimates)
6. **Customer Impact** (how planned features address top customer requests and pain points)
7. **Technical Foundation** (platform work, technical debt, infrastructure requirements)
8. **Success Metrics** (KPIs for measuring roadmap progress and feature adoption)
9. **Risk Mitigation** (dependencies, technical challenges, market timing risks)
10. **Stakeholder Alignment** (sales enablement, marketing support, customer communication plan)

CONSTRAINTS:
Apply Corporate Style Applicator rules plus:
• Technical features translated for business stakeholder understanding
• Timeline estimates realistic based on engineering capacity and velocity
• Customer requests prioritized by revenue impact and market size
• Dependencies clearly identified with mitigation strategies
• Bold key dates, resource requirements, and success metrics

ROADMAP-SPECIFIC REQUIREMENTS:
• Balance customer requests with technical debt and platform investment
• Include both feature development and operational/infrastructure work
• Address sales team needs for competitive features and customer commitments
• Provide flexibility for market changes while maintaining strategic focus
• Connect individual features to overall business objectives and metrics

AUDIENCE CUSTOMIZATION:
• **Executive audience:** Focus on business impact, revenue implications, competitive positioning
• **Engineering audience:** Include technical architecture, implementation complexity, dependencies
• **Sales/Marketing audience:** Emphasize customer-facing features, competitive differentiation, go-to-market timing
• **Customer-facing:** Highlight user benefits, problem resolution, improvement timeline

VALIDATION:
Show thumbnails, verify timeline realism, confirm customer impact clarity
```

## False-Positive Prevention

1. **"On track" with no baseline date.** A release shown as on track states the date it was first committed to; a date that has moved since the last roadmap is drawn as moved, with the original date visible.
2. **A timeline that overruns capacity.** Placing items on the Roadmap Overview is a capacity claim. Sum the effort estimates in each period and compare them with sprint velocity × sprints available from the capacity plan; an overfilled period is flagged, not drawn as feasible.
3. **Priority scores relabelled as revenue impact.** Request counts and priority scores are not revenue. Rank by revenue impact only from the feedback data's revenue field; otherwise rank by what the data does hold and say which.
4. **Dates on unestimated work.** Backlog items without an effort estimate, or with an unresolved dependency, go in a "not yet scheduled" band instead of on the timeline.
5. **Tentative items dated in the customer-facing version.** Sales and customers read a date as a commitment; omit dates for anything the strategy document marks tentative.
6. **Verify:** check that each Priority Features item exists in the backlog with an estimate, and that each dependency on Risk Mitigation appears in the backlog's dependencies field.

## Usage Notes

- **Purpose:** Converts product planning data into visual roadmap with timeline, priorities, and resource requirements
- **Deck Type:** Quarterly/Annual Product Roadmaps
- **Key Features:**
  - 6-12 month visual timeline
  - Priority feature ranking with customer impact
  - Engineering capacity and resource allocation
  - Technical debt and platform work balance
  - Customer feedback integration
  - Success metrics and KPIs
  - Risk mitigation and dependencies
  - 8-10 slides for quarterly, 15+ for annual planning
  - Audience-specific customization (executive, engineering, sales, customer)
  - Translates technical features for business stakeholders
  - Realistic timelines based on actual capacity
  - Connects features to business objectives
