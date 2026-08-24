# 2. Crisis Management Deck

**Source:** POWERPOINT_BUILDING_PROMPT_SYSTEM.md

**Category:** PowerPoint / Presentation Building

## Prompt

```
jsx
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

## Usage Notes

This is part of the PowerPoint Building Prompt System designed for creating professional presentation decks.

**Purpose**: 2. Crisis Management Deck

These prompts are optimized for generating structured PowerPoint presentations with corporate style consistency. They work in conjunction with the Corporate Style Extractor and Corporate Style Applicator foundation prompts to maintain brand consistency across all slides.

**Best Practices**:
- Use the Corporate Style Extractor first to analyze your company's presentation style
- Apply extracted style guidelines when generating decks
- Follow the slide structure and formatting recommendations
- Validate deck consistency using the Deck Assembly & Validation prompt
