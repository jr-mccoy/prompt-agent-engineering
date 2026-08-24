# 6. Product Roadmap Presentation

**Source:** POWERPOINT_BUILDING_PROMPT_SYSTEM.md

**Category:** PowerPoint / Presentation Building

## Prompt

```
jsx
`SYSTEM PROMPT: PRODUCT ROADMAP PRESENTATION

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
Show thumbnails, verify timeline realism, confirm customer impact clarity`
```

## Usage Notes

This is part of the PowerPoint Building Prompt System designed for creating professional presentation decks.

**Purpose**: 6. Product Roadmap Presentation

These prompts are optimized for generating structured PowerPoint presentations with corporate style consistency. They work in conjunction with the Corporate Style Extractor and Corporate Style Applicator foundation prompts to maintain brand consistency across all slides.

**Best Practices**:
- Use the Corporate Style Extractor first to analyze your company's presentation style
- Apply extracted style guidelines when generating decks
- Follow the slide structure and formatting recommendations
- Validate deck consistency using the Deck Assembly & Validation prompt
