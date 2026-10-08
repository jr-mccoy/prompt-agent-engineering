---
title: "Crisis Management Deck"
category: presentations
description: "Synthesize crisis-related data from multiple sources into a controlled executive response presentation with clear scenarios and an immediate action plan."
techniques:
  - ST-03
  - OC-08
  - DS-19
  - QA-04
difficulty: advanced
tags:
  - presentations
  - powerpoint
  - crisis-management
  - crisis-communication
  - scenario-analysis
updated: "2026-10-06"
---

# Crisis Management Deck

**Source:** POWERPOINT_BUILDING_PROMPT_SYSTEM.md

**Category:** PowerPoint Building / Strategic Decision Making

## Prompt

```
SYSTEM PROMPT: CRISIS MANAGEMENT DECK

PREREQUISITES:
Corporate Style Guide JSON (from Corporate Style Extractor)

WORKFLOW:
Use html2pptx with Corporate Style Applicator enforcement

OBJECTIVE:
Synthesize crisis-related data from multiple sources into controlled executive response presentation with clear scenarios and immediate action plan.

INPUT REQUIREMENTS:
• Financial impact data Excel with [Revenue impact, Cost implications, Cash flow effects]
• Crisis timeline document with [Key events, Response actions taken, Current status]
• Stakeholder communication log with [Internal/external messaging, Media coverage]
• Email thread or memo with [Leadership perspectives, Conflicting viewpoints]

EXECUTION APPROACH:
**URGENT (6-8 slides):** Generate complete deck in single chat for immediate board call
**COMPREHENSIVE (12+ slides):** Use Enterprise Deck Architect for complex crisis with multiple workstreams

SLIDE STRUCTURE - URGENT VERSION:
1. **Crisis Definition** (what happened, scope, timeline)
2. **Current Impact** (financial, operational, reputational effects)
3. **Immediate Response** (actions taken, resources deployed)
4. **Scenario Analysis** (3 paths: conservative, moderate, aggressive response)
5. **Recommended Action** (preferred scenario with rationale)
6. **Resource Requirements** (budget, personnel, timeline for execution)
7. **Communication Plan** (stakeholder messaging, media strategy)
8. **Next Steps** (immediate actions, decision points, follow-up timeline)

CONSTRAINTS:
Apply Corporate Style Applicator rules plus:
• Crisis tone: professional urgency without panic
• Reconcile conflicting stakeholder viewpoints from source materials
• Present scenarios with clear trade-offs and financial implications
• Bold all financial impact figures and resource requirements
• Frame as "controlled response" not "company in crisis"

CRISIS-SPECIFIC REQUIREMENTS:
• Acknowledge uncertainty with confidence intervals on projections
• Address stakeholder concerns proactively
• Clear timeline for decision-making and implementation
• Balance transparency with appropriate confidentiality

VALIDATION:
Show thumbnails, verify tone appropriateness for crisis communication, confirm actionability
```

## False-Positive Prevention

1. **Unconfirmed facts stated as established.** Early timelines mix confirmed events with reports and media claims. Tag every statement on Crisis Definition and Current Impact as confirmed (with its source in the timeline document) or unconfirmed; unconfirmed items never appear as headline facts.
2. **Remedies promised before legal has cleared them.** Customer credits, refunds, admissions of fault, and regulator-facing statements on Recommended Action or Communication Plan are marked "pending legal review" unless the inputs record legal sign-off.
3. **"Controlled response" framing that overstates containment.** The framing rule governs tone, not facts. If the timeline's current status is ongoing, the deck says ongoing, not resolved.
4. **Conflicting viewpoints "reconciled" by dropping one.** When leadership emails disagree, show the disagreement and who decides it on Scenario Analysis rather than keeping only the view that suits the recommendation.
5. **Impact ranges with nothing behind them.** A range on revenue or cost impact must come from the financial impact data or stated assumptions; show the assumption next to the figure.
6. **Verify:** cross-check each date and figure on Crisis Definition and Current Impact against the timeline document and the financial impact sheet, and each media claim against the stakeholder communication log.

## Usage Notes

- **Purpose:** Synthesizes multi-source crisis data into controlled executive response plan with scenarios
- **Deck Type:** Crisis Response / Emergency Board Calls
- **Key Features:**
  - Urgent timeline (6-8 slides for immediate use)
  - Multi-scenario analysis (conservative, moderate, aggressive)
  - Reconciles conflicting stakeholder viewpoints
  - Professional urgency without panic
  - Clear resource requirements and timeline
  - Stakeholder communication strategy
  - Financial impact quantification
  - Frames situation as controlled response
  - Suitable for outages, PR crises, financial shocks, operational disruptions
