# Field Guide: Business & Stakeholder Communication

> Part of the [Non-Coding Quick Start](../NON_CODING_QUICK_START.md) system.
> Craft reference for business documents, stakeholder communication, proposals,
> PRDs, and organizational communication — what makes them work, how they fail,
> and skeleton templates for the five recurring document types.

> **Where this came from.** This was the guide for `domain-professional-communication/`,
> a domain dissolved in the 2026-08 reorganization because every prompt in it was
> product work filed under a name that described none of it. The prompts moved to
> [`domain-product-management/`](../domain-product-management/); the craft guidance
> is here, next to the business-writing prompts it actually supports.

---

## When This Domain Applies

### Trigger Phrases

Route to this domain when the request mentions:

| Category | Trigger Phrases |
|----------|----------------|
| **Product Documents** | "PRD", "product requirements", "feature spec", "user stories", "acceptance criteria" |
| **Strategy/Planning** | "business case", "roadmap", "OKRs", "strategic plan", "initiative proposal" |
| **Stakeholder Communication** | "executive summary", "board presentation", "stakeholder update", "status report" |
| **Proposals** | "proposal", "pitch deck", "business justification", "ROI analysis" |
| **Analysis Documents** | "SWOT", "competitive analysis", "market sizing", "assessment" |
| **Organizational** | "announcement", "change communication", "policy document", "process documentation" |

### User Personas

| Persona | Typical Needs |
|---------|--------------|
| **Product Managers** | PRDs, feature specs, stakeholder alignment, roadmaps |
| **Project Managers** | Status reports, risk assessments, project proposals |
| **Executives** | Board decks, strategic communications, investor updates |
| **Team Leads** | Team communications, process docs, change announcements |
| **Consultants** | Client proposals, assessment reports, recommendations |
| **Analysts** | Research reports, competitive analysis, market assessments |

### Out of Scope

- **Personal communication** (emails to friends/family) → General COMMUNICATE pattern
- **Creative marketing copy** → domain-creative-writing
- **Technical documentation** (API docs, code comments) → Coding prompts
- **Academic research papers** → domain-research-academic

---

## Domain-Specific Considerations

### What Makes Professional Communication Unique

Professional documents operate in environments where:

1. **Stakes Are Political** - Documents affect careers, budgets, and organizational power
2. **Audience Is Heterogeneous** - Multiple readers with different priorities and expertise
3. **Decisions Follow** - Documents lead to actions, approvals, or resource allocation
4. **Context Is Implicit** - Organizational dynamics, history, and relationships matter
5. **Brevity Is Valued** - Executives have limited attention; respect their time
6. **Credibility Is Essential** - One unsupported claim can undermine the entire document

### The Business Document Difference

| Dimension | Academic/Technical Writing | Professional Communication |
|-----------|---------------------------|---------------------------|
| **Goal** | Inform, document | Persuade, enable decisions |
| **Tone** | Objective, comprehensive | Confident, action-oriented |
| **Structure** | Linear, detailed | Executive summary first, details on request |
| **Evidence** | Citations, methodology | Business metrics, stakeholder impact |
| **Length** | Complete coverage | As short as possible while being effective |
| **Success Metric** | Accuracy | Action taken |

### Critical Success Factors

1. **Know Your Audience** - Who decides? What do they care about? What's their background?
2. **Lead with the Ask** - Don't bury the conclusion; state it upfront
3. **Quantify Impact** - Numbers are more persuasive than adjectives
4. **Address Objections** - Anticipate and preempt concerns
5. **Enable Decision-Making** - Provide clear options with trade-offs
6. **Respect Hierarchy** - Match tone and detail to the seniority of readers

### Common Failure Modes

| Failure | Example | Prevention |
|---------|---------|------------|
| **Buried lede** | Putting the ask on page 5 | Executive summary with recommendation first |
| **Missing "so what"** | Presenting data without implications | Every data point should support a conclusion |
| **Ignoring politics** | Recommending something leadership already rejected | Research organizational context |
| **Over-engineering** | 50-page PRD for MVP | Match scope to stage |
| **Unsupported claims** | "This will be huge" | Quantify: "TAM is $2B with 15% CAGR" |
| **Wrong audience** | Technical deep-dive for executives | Layer content (summary → details) |

---

## Recommended Techniques

### Core Techniques (Always Use)

| Technique | Application in Professional Comm | Example |
|-----------|----------------------------------|---------|
| **ST-01 Clear Objective** | Define purpose and desired outcome | "Gain approval for $500K Q2 budget" |
| **CM-01 Context Framing** | Stakeholder analysis and political context | "CFO prioritizes cost control; CTO wants innovation" |
| **OC-01 Output Templates** | Structured professional formats | Executive summary, BLUF, pyramid structure |
| **RT-05 Evidence-Based** | Support claims with data and sources | "Revenue impact: $2M based on 15% conversion lift" |
| **QA-02 Adversarial Thinking** | Anticipate objections and address them | "Objection handling" section |

### Situational Techniques

| Situation | Add Technique | Why |
|-----------|--------------|-----|
| Major decision | RT-02 Multi-Dimensional Analysis | Compare options across multiple criteria |
| Executive audience | CM-02 Audience Adaptation | Extreme brevity, focus on strategic impact |
| Controversial proposal | QA-01 Self-Verification | Show you've considered opposing views |
| Cross-functional | DS-01 Framework Application | Use shared frameworks (RACI, OKRs) |
| Change communication | RT-04 Emotional Intelligence | Address human reactions to change |

---

## Quality Indicators for Professional Communication

### What "Good" Looks Like

**A high-quality professional document:**

1. **Leads with the Conclusion**
   - Executive summary in first paragraph
   - Recommendation or ask is immediately clear
   - Supporting details follow, not precede

2. **Knows Its Audience**
   - Appropriate level of detail for readers
   - Addresses what THEY care about, not what YOU find interesting
   - Anticipates their questions and concerns

3. **Supports Every Claim**
   - Numbers have sources
   - Projections show assumptions
   - Qualitative claims have evidence

4. **Enables Decisions**
   - Clear options presented
   - Trade-offs explained
   - Recommended path identified with rationale

5. **Respects Time**
   - As short as possible
   - Scannable structure (headers, bullets, tables)
   - Details in appendix, not body

### Confidence Calibration for Business Claims

```markdown
## Certainty Framework for Business Projections

**High Confidence:**
- Based on historical data from similar initiatives
- Validated through customer research or pilot
- Conservative assumptions documented
- "Based on our 2023 pilot, conversion increased 15%"

**Medium Confidence:**
- Extrapolated from related data
- Industry benchmarks applied
- Key assumptions identified
- "Industry benchmarks suggest 10-20% efficiency gain"

**Low Confidence:**
- Novel situation with no direct precedent
- Multiple unvalidated assumptions
- Wide range of outcomes possible
- "Early signals suggest potential, but we need pilot data"
```

### False-Positive Prevention for Professional Communication

**DON'T:**

- Overstate market size without methodology
- Claim competitive advantage without evidence
- Project revenue without stating assumptions
- Guarantee timelines on novel initiatives
- Present one option as if alternatives don't exist
- Ignore organizational politics and history
- Use corporate jargon as a substitute for substance
- Bury risks in footnotes

**DO:**

- State methodology for any projection
- Show your math on ROI calculations
- Acknowledge key assumptions and their sensitivity
- Present 2-3 options with trade-offs
- Research stakeholder positions before finalizing
- Define terms that different audiences interpret differently
- Put risks in a dedicated, prominent section
- Include "what could go wrong" and mitigation

---

## Existing Prompts in This Repository

Use the templates in this guide when you want a document skeleton. Use a prompt
when you want the model to do the work:

| You need | Prompt |
|---|---|
| Executive brief / decision memo | [`business-writing/business_writing_executive_brief.md`](business-writing/business_writing_executive_brief.md) |
| Status report / stakeholder update | [`business-writing/business_writing_status_report.md`](business-writing/business_writing_status_report.md) |
| Proposal | [`business-writing/business_writing_proposal.md`](business-writing/business_writing_proposal.md) |
| PRD | [`business-writing/business_writing_prd_document.md`](business-writing/business_writing_prd_document.md) (prose craft) or [`domain-product-management/prompts/product_create_prd.md`](../domain-product-management/prompts/product_create_prd.md) (interrogative build) |
| Post-mortem / incident report | [`business-writing/business_writing_post_mortem.md`](business-writing/business_writing_post_mortem.md) |
| SOP / technical documentation | [`business-writing/business_writing_sop.md`](business-writing/business_writing_sop.md), [`business_writing_technical_doc.md`](business-writing/business_writing_technical_doc.md) |
| Competitive analysis | [`domain-product-management/prompts/product_competitor_feature_teardown.md`](../domain-product-management/prompts/product_competitor_feature_teardown.md), [`domain-business-strategy/research/competitor_teardown.md`](../domain-business-strategy/research/competitor_teardown.md) |
| Stakeholder navigation | [`domain-personal-development/prompts/stakeholder/stakeholder_navigation_guide.md`](../domain-personal-development/prompts/stakeholder/stakeholder_navigation_guide.md) |
| Design direction | [`domain-frontend-development/design-direction/`](../domain-frontend-development/design-direction/) |
| Is the draft any good? | [`content-quality/`](content-quality/) — 19 slop evaluators by document type |

---

## Templates

### Template 1: Executive Proposal (BLUF Format)

```markdown
# [Proposal Title]

**Prepared for:** [Decision maker(s)]
**Prepared by:** [Author]
**Date:** [Date]

---

## BLUF (Bottom Line Up Front)

**Request:** [What you're asking for - budget, approval, resources, decision]

**Recommendation:** [Your recommended course of action]

**Why Now:** [Urgency or opportunity cost of delay]

**Expected Outcome:** [Quantified benefit]

---

## Executive Summary (One Page Maximum)

### The Opportunity
[2-3 sentences on what's possible]

### The Problem/Gap
[2-3 sentences on what's holding us back]

### Proposed Solution
[2-3 sentences on what you want to do]

### Investment Required
- Budget: [$X]
- Timeline: [Duration]
- Resources: [Team, tools]

### Expected Return
- [Metric 1]: [Projected improvement]
- [Metric 2]: [Projected improvement]
- ROI: [X%] over [timeframe]

### Key Risks and Mitigation
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk 1] | [H/M/L] | [H/M/L] | [Strategy] |

### Decision Needed
[Specific decision with options if applicable]

---

## Supporting Detail

### Business Context
[Expand on opportunity/problem - market data, competitive pressure, customer feedback]

### Solution Deep Dive
[More detail on proposed approach]

### Financial Analysis
[ROI calculation with assumptions stated]

### Implementation Plan
[High-level timeline and milestones]

### Alternatives Considered
| Option | Pros | Cons | Why Not Recommended |
|--------|------|------|---------------------|
| [Alt 1] | [Pros] | [Cons] | [Reason] |
| [Alt 2] | [Pros] | [Cons] | [Reason] |

---

## Appendix
[Detailed data, research, methodology - for those who want to dig deeper]
```

### Template 2: Product Requirements Document (MVP)

```markdown
# PRD: [Feature/Product Name]

**Status:** [Draft / In Review / Approved]
**Author:** [Name]
**Last Updated:** [Date]
**Target Release:** [Quarter/Date]

---

## Overview

### Problem Statement
[What problem are we solving? Who has this problem? How do we know it's a real problem?]

### Solution Summary
[One paragraph describing what we're building]

### Success Metrics
| Metric | Current | Target | Measurement |
|--------|---------|--------|-------------|
| [Primary KPI] | [Baseline] | [Goal] | [How measured] |
| [Secondary KPI] | [Baseline] | [Goal] | [How measured] |

### Scope (MVP)
**In Scope:**
- [Feature/capability 1]
- [Feature/capability 2]
- [Feature/capability 3]

**Explicitly Out of Scope (Future):**
- [Deferred item 1] - Reason: [Why not MVP]
- [Deferred item 2] - Reason: [Why not MVP]

---

## User Stories

### Primary Persona: [Persona Name]
[Brief description: role, goals, pain points]

### User Stories (Prioritized)

**Must Have (P0):**
1. As a [persona], I want to [action] so that [outcome]
   - Acceptance Criteria:
     - [ ] [Criterion 1]
     - [ ] [Criterion 2]

**Should Have (P1):**
1. As a [persona], I want to [action] so that [outcome]
   - Acceptance Criteria: [...]

**Nice to Have (P2):**
1. [Future consideration]

---

## Requirements

### Functional Requirements
| ID | Requirement | Priority | Acceptance Criteria |
|----|-------------|----------|---------------------|
| FR-01 | [Requirement] | P0 | [How to verify] |
| FR-02 | [Requirement] | P0 | [How to verify] |

### Non-Functional Requirements
- **Performance:** [Response time, throughput]
- **Security:** [Auth, data protection]
- **Scalability:** [User/data volume]
- **Accessibility:** [WCAG level]

### Dependencies
| Dependency | Owner | Status | Risk if Delayed |
|------------|-------|--------|-----------------|
| [System/team] | [Name] | [Status] | [Impact] |

---

## Design

### User Flow
[Link to design files or describe flow]

### Key Screens/Interactions
[Wireframes or descriptions]

### Edge Cases
| Scenario | Expected Behavior |
|----------|-------------------|
| [Edge case 1] | [How system handles it] |

---

## Technical Approach

### Architecture Overview
[High-level technical approach - not detailed design]

### Data Requirements
[What data is needed, where it comes from, privacy considerations]

### Integration Points
[APIs, services, third-party systems]

---

## Launch Plan

### Rollout Strategy
- [ ] Internal testing
- [ ] Beta/limited release
- [ ] GA release

### Success Criteria for Each Phase
| Phase | Duration | Success Criteria | Go/No-Go Decision |
|-------|----------|------------------|-------------------|
| Beta | [Time] | [Metrics] | [Who decides] |

### Rollback Plan
[If things go wrong, how do we revert?]

---

## Open Questions
| Question | Owner | Due Date | Impact if Unresolved |
|----------|-------|----------|---------------------|
| [Question] | [Name] | [Date] | [What's blocked] |

---

## Appendix
- Competitive analysis
- User research findings
- Technical spike results
```

### Template 3: Status Report / Stakeholder Update

```markdown
# [Project/Initiative] Status Update

**Period:** [Date range]
**Author:** [Name]
**Distribution:** [Stakeholders]

---

## TL;DR

**Overall Status:** [GREEN / YELLOW / RED]

**Key Update:** [One sentence on most important thing]

**Decisions Needed:** [Any blockers requiring stakeholder input]

---

## Status Summary

| Workstream | Status | Trend | Notes |
|------------|--------|-------|-------|
| [Stream 1] | 🟢 | → | On track |
| [Stream 2] | 🟡 | ↓ | [Issue] |
| [Stream 3] | 🔴 | ↓ | [Blocked by X] |

---

## Progress This Period

### Completed
- ✅ [Accomplishment 1]
- ✅ [Accomplishment 2]

### In Progress
- 🔄 [Activity 1] - [% complete or expected completion]
- 🔄 [Activity 2] - [% complete or expected completion]

### Planned Next Period
- 📋 [Planned item 1]
- 📋 [Planned item 2]

---

## Metrics

| Metric | Target | Actual | Trend | Notes |
|--------|--------|--------|-------|-------|
| [KPI 1] | [Target] | [Actual] | [↑↓→] | [Context] |

---

## Risks and Issues

### Active Issues (Requiring Attention)
| Issue | Impact | Owner | Action | Due |
|-------|--------|-------|--------|-----|
| [Issue 1] | [H/M/L] | [Name] | [What's being done] | [Date] |

### Risks (Potential Future Issues)
| Risk | Probability | Impact | Mitigation | Owner |
|------|-------------|--------|------------|-------|
| [Risk 1] | [H/M/L] | [H/M/L] | [Strategy] | [Name] |

---

## Decisions Needed

| Decision | Options | Recommendation | Deadline | Decider |
|----------|---------|----------------|----------|---------|
| [Decision] | [A, B, C] | [Your rec] | [Date] | [Who] |

---

## Resource/Budget Update

**Budget Status:**
- Allocated: $[X]
- Spent to Date: $[Y]
- Remaining: $[Z]
- Forecast: [On track / Over / Under]

**Resource Notes:**
[Any staffing changes, needs, or concerns]
```

### Template 4: Competitive Analysis

```markdown
# Competitive Analysis: [Market/Product]

**Prepared by:** [Name]
**Date:** [Date]
**Purpose:** [Why this analysis, what decision it supports]

---

## Executive Summary

**Competitive Position:** [Our overall market position in one sentence]

**Key Findings:**
1. [Most important insight]
2. [Second insight]
3. [Third insight]

**Recommended Actions:**
1. [Action with expected impact]
2. [Action with expected impact]

---

## Market Overview

**Market Size:**
- TAM: $[X] ([Source])
- SAM: $[X] ([Methodology])
- SOM: $[X] ([Our realistic capture])

**Growth Rate:** [X%] CAGR ([Years], [Source])

**Key Trends:**
1. [Trend] - Impact on us: [Positive/Negative/Neutral]
2. [Trend] - Impact on us: [Positive/Negative/Neutral]

---

## Competitive Landscape

### Competitor Overview

| Competitor | Market Share | Positioning | Primary Strength | Primary Weakness |
|------------|--------------|-------------|------------------|------------------|
| Us | [%] | [Positioning] | [Strength] | [Weakness] |
| [Comp A] | [%] | [Positioning] | [Strength] | [Weakness] |
| [Comp B] | [%] | [Positioning] | [Strength] | [Weakness] |

### Detailed Competitor Profiles

#### [Competitor A]

**Overview:** [Company size, funding, history]

**Product/Service:**
- Strengths: [What they do well]
- Weaknesses: [Where they fall short]

**Go-to-Market:**
- Target customer: [Who they sell to]
- Pricing: [Model and approximate range]
- Channels: [How they reach customers]

**Recent Moves:** [Last 6-12 months of news, launches, changes]

**Threat Level:** [High/Medium/Low] - [Rationale]

[Repeat for each major competitor]

---

## Feature Comparison

| Feature | Us | Comp A | Comp B | Comp C |
|---------|-----|--------|--------|--------|
| [Feature 1] | ✅ | ✅ | ❌ | ✅ |
| [Feature 2] | ✅ | ❌ | ✅ | ✅ |
| [Feature 3] | ❌ | ✅ | ✅ | ❌ |

**Legend:** ✅ Strong | ⚠️ Partial | ❌ Missing

---

## Positioning Analysis

### Perceptual Map
[Describe or include visual: e.g., Price vs. Features quadrant]

### Our Differentiation
**What we do that no one else does:**
- [Unique capability 1]
- [Unique capability 2]

**What we do better:**
- [Superior capability with evidence]

**Where we lag:**
- [Competitor advantage with evidence]

---

## Strategic Implications

### Threats to Monitor
| Threat | Trigger to Watch | Response if Triggered |
|--------|-----------------|----------------------|
| [Threat] | [What would indicate it's happening] | [What we'd do] |

### Opportunities to Pursue
| Opportunity | Required Investment | Expected Return | Timeline |
|-------------|--------------------| ----------------|----------|
| [Opportunity] | [What it takes] | [Projected benefit] | [When] |

---

## Recommendations

### Immediate Actions (Next Quarter)
1. [Action] - Addresses [finding]
2. [Action] - Addresses [finding]

### Strategic Initiatives (This Year)
1. [Initiative] - Competitive rationale: [Why]

### Watch List (Monitor, No Action Yet)
1. [Item] - Trigger for action: [What would make us act]

---

## Appendix

### Methodology
[How analysis was conducted, sources used, limitations]

### Data Sources
- [Source 1] - [What it provided]
- [Source 2] - [What it provided]

### Confidence Assessment
| Section | Confidence | Reasoning |
|---------|------------|-----------|
| Market size | Medium | [Based on analyst reports, not primary research] |
| Competitor pricing | Low | [Limited public data, estimates] |
```

### Template 5: Change Communication

```markdown
# [Change] Announcement

**Audience:** [Who receives this]
**Effective Date:** [When change takes effect]
**Sent By:** [Leadership level appropriate to change magnitude]

---

## The Change

**What's Happening:**
[Clear, jargon-free description of the change]

**Why:**
[Honest explanation - business rationale]

**When:**
- Announcement: [Today's date]
- Effective: [When it starts]
- Transition period: [If applicable]

---

## What This Means for You

### [Audience Segment 1]
**Impact:** [How it affects them specifically]
**Action Required:** [What they need to do]
**Support Available:** [Where to get help]

### [Audience Segment 2]
[Same structure]

---

## What's NOT Changing

[List things people might worry about that remain the same]

---

## Timeline

| Date | Milestone |
|------|-----------|
| [Date] | Announcement (today) |
| [Date] | [Next step] |
| [Date] | Full implementation |

---

## Support Resources

**Questions?**
- FAQ: [Link]
- Contact: [Person/team and how to reach them]
- Town Hall/Q&A: [Date/time if applicable]

**Training/Enablement:**
- [Resource 1]: [Link/date]
- [Resource 2]: [Link/date]

---

## Leadership Message

[Personal note from appropriate leader - empathetic, forward-looking]

---

## FAQ

**Q: [Anticipated question]**
A: [Clear answer]

**Q: [Anticipated question]**
A: [Clear answer]

[Continue for common concerns]
```

---

## Worked Example

### Scenario: Product Manager Proposing a New Feature Investment

**User says:** "I need to convince my leadership to invest in a new customer analytics platform. We need about $150K and it could reduce churn significantly."

**Step 1: Classification**

- Task Type: COMMUNICATE (persuasive proposal)
- Domain: Professional Communication
- Specific Type: Executive proposal / business case

**Step 2: Context Gathering**

**From the request:**
- Investment: ~$150K
- Benefit: Churn reduction (not quantified)
- Audience: Leadership (level unclear)

**Need to determine:**
- Current churn rate and cost
- Expected improvement (quantified)
- Decision maker(s) and their priorities
- Competing initiatives
- Timeline requirements

**Step 3: Template Selection**

Use **Template 1: Executive Proposal (BLUF Format)**

**Why:** This is a budget request requiring clear ask, quantified ROI, and anticipation of objections.

**Step 4: Customization**

Apply to analytics platform investment:

**Strengthen with:**
- Specific churn cost calculation
- ROI timeline
- Competitive pressure data
- Alternative approaches considered
- Risk mitigation

**Step 5: Quality Check**

Before finalizing, verify:
- [ ] Ask is crystal clear in first paragraph
- [ ] ROI is quantified with stated assumptions
- [ ] Stakeholder concerns are anticipated
- [ ] Alternatives were considered
- [ ] Timeline and milestones are realistic
- [ ] Risks are acknowledged and mitigated

**Final Prompt:**

```markdown
# Executive Proposal: Customer Analytics Platform Investment

**Prepared for:** VP of Operations, CFO
**Prepared by:** [Product Manager Name]
**Date:** [Date]
**Decision Requested By:** [Date]

---

## BLUF

**Request:** Approval for $150K investment in customer analytics platform

**Recommendation:** Proceed with implementation in Q2, targeting 8% churn reduction

**Why Now:** Current churn rate (12%) costs us $2M annually; each quarter of delay = $500K in preventable losses

**Expected Outcome:** $400K annual savings from churn reduction (payback in 4.5 months)

---

## Executive Summary

### The Problem
We're losing customers we could retain. Our current 12% annual churn costs us approximately $2M in revenue. Customer success teams operate reactively—learning about at-risk customers only after they've churned.

### The Opportunity
Customers exhibit warning signs 60-90 days before churning (reduced usage, support ticket patterns, engagement decline). With the right analytics, we can intervene before it's too late.

### Proposed Solution
Implement [Platform Name], a customer health scoring platform that:
- Aggregates usage, support, and engagement data
- Generates predictive churn risk scores
- Alerts customer success to intervention opportunities

### Investment Required
| Category | Cost |
|----------|------|
| Platform license (Year 1) | $80K |
| Implementation services | $40K |
| Internal resources (0.5 FTE for 3 months) | $25K |
| Training and enablement | $5K |
| **Total** | **$150K** |

### Expected Return
| Metric | Projection | Confidence |
|--------|------------|------------|
| Churn reduction | 8% → ~11% (from 12%) | Medium - based on vendor case studies |
| Annual revenue retained | $400K | Medium - [calculation below] |
| Payback period | 4.5 months | Medium |
| 3-year ROI | 680% | Medium |

**Calculation:**
- Current churn: 12% of $16.7M ARR = $2M lost annually
- Target churn: 11% = $1.84M lost (conservative estimate)
- Improvement: $160K-$400K saved annually
- Conservative estimate used: $400K

### Key Risks
| Risk | Mitigation |
|------|------------|
| Adoption by CS team | Phased rollout with champions, tied to MBOs |
| Data quality issues | 60-day data audit before go-live |
| Vendor viability | Selected vendor has $50M funding, 500+ customers |

---

## Decision Needed

**Approve $150K Q2 budget allocation for customer analytics platform**

**Options:**
1. **Approve as proposed** - Proceed with Q2 implementation
2. **Pilot first** - $50K pilot with 2 CSMs for 90 days, then full decision
3. **Defer to Q3** - Delay 1 quarter (opportunity cost: ~$100K)
4. **Decline** - Accept current churn rate

**Recommendation:** Option 1 (full implementation) based on ROI analysis and competitive pressure

---

## Anticipated Objections

**"We tried analytics before and it didn't work."**
Previous attempt (2022) failed due to poor data integration. This platform has native connectors to our stack (Salesforce, Intercom, Mixpanel) and dedicated implementation support.

**"Budget is tight this year."**
Payback in 4.5 months means Q2 investment generates Q3-Q4 returns this fiscal year. Delay costs us $100K+ per quarter in preventable churn.

**"Can IT support another platform?"**
Vendor handles implementation and provides managed services. IT involvement limited to security review and SSO setup (estimated 20 hours).

---

## Next Steps If Approved

| Week | Activity |
|------|----------|
| 1 | Contract execution, kickoff |
| 2-4 | Data integration and validation |
| 5-6 | Model training, CS team training |
| 7-8 | Pilot with top 50 at-risk accounts |
| 9+ | Full rollout, ongoing optimization |

---

## Appendix

### A. Competitive Analysis
[Details on competitor churn rates and analytics usage]

### B. Vendor Evaluation
[Selection criteria and scoring]

### C. Detailed ROI Model
[Spreadsheet with sensitivity analysis]
```

---

## Anti-Patterns for Professional Communication

### Mistake 1: Burying the Ask

**Problem:** Decision makers have to hunt for what you want

**Bad:**
```
Page 1: Background on the market
Page 2: Technical analysis
Page 3: Options explored
Page 4: Recommendation
Page 5: The actual request for approval
```

**Good:**
```
First paragraph: "Request: Approval for $150K investment in customer analytics platform, with expected 4-month payback."
Rest of document: Supporting evidence
```

**Why it matters:** Executives decide in the first 30 seconds whether to engage. If they don't know what you're asking, you've lost them.

---

### Mistake 2: Presenting One Option

**Problem:** Looks like you didn't think it through

**Bad:**
```
"We should implement Platform X for $150K."
[No alternatives discussed]
```

**Good:**
```
"Three options considered:
1. Platform X ($150K, 8% churn reduction) - Recommended
2. Build internally ($300K, 12-month timeline) - Too slow
3. Hire more CSMs ($200K ongoing) - Doesn't address root cause
Recommendation: Platform X offers best ROI and fastest time to value."
```

**Why it matters:** Showing alternatives demonstrates rigor and helps stakeholders understand trade-offs.

---

### Mistake 3: Unsupported Projections

**Problem:** Numbers without methodology destroy credibility

**Bad:**
```
"This will reduce churn by 8% and save $400K annually."
```

**Good:**
```
"Projected churn reduction: 8% (from 12% to 11%)
Basis: Average improvement from vendor case studies (5-12% range)
Calculation: 1% of $16.7M ARR = $167K × 2.4 points improvement = ~$400K
Confidence: Medium - actual results depend on adoption and data quality
Sensitivity: Even 4% improvement ($200K) achieves 15-month payback"
```

**Why it matters:** Leadership has seen too many "guaranteed" projections fail. Transparency about assumptions builds trust.

---

### Mistake 4: Ignoring Politics

**Problem:** Technically sound proposal fails because of organizational dynamics

**Bad:**
Creating a proposal without knowing:
- Who has been burned by similar initiatives
- What competing priorities exist
- Who needs to be consulted before the meeting

**Good:**
Before finalizing:
- "CFO rejected a $200K MarTech request last quarter—what was the objection?"
- "VP Sales is also asking for analytics budget—should we partner?"
- "IT has concerns about vendor security—let's address preemptively"

**Why it matters:** The best analysis loses to political missteps.

---

### Mistake 5: Too Much Detail for the Audience

**Problem:** Executives drowning in information they didn't ask for

**Bad:**
50-page proposal with extensive technical specifications for a budget meeting

**Good:**
```
Executive Version: 2-page summary with clear ask, ROI, risks
Supporting Materials: Available upon request or in appendix
Technical Details: Separate document for implementation team
```

**Why it matters:** Detail doesn't equal thoroughness. Knowing what to include—and what to leave out—shows judgment.

---

## Quick Reference Card

```
╔═══════════════════════════════════════════════════════════════════════════╗
║            PROFESSIONAL COMMUNICATION QUICK REFERENCE                      ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║  CORE PRINCIPLES:                                                         ║
║  □ Lead with the ask (BLUF - Bottom Line Up Front)                       ║
║  □ Quantify everything (replace adjectives with numbers)                 ║
║  □ Show alternatives (never just one option)                             ║
║  □ Anticipate objections (address them before they're raised)            ║
║  □ Respect time (shorter is better; details in appendix)                 ║
║                                                                           ║
║  BEFORE WRITING, KNOW:                                                    ║
║  • Who decides?                                                           ║
║  • What do they care about? (not what YOU care about)                    ║
║  • What are the competing priorities?                                     ║
║  • Who tried something similar before? What happened?                     ║
║  • What objections will arise?                                            ║
║                                                                           ║
║  STRUCTURE FOR PROPOSALS:                                                 ║
║  1. BLUF (Ask + Recommendation + Why Now)                                ║
║  2. Executive Summary (1 page max)                                        ║
║  3. Supporting Analysis                                                   ║
║  4. Risks and Mitigation                                                  ║
║  5. Decision/Next Steps                                                   ║
║  6. Appendix (for detail-seekers)                                        ║
║                                                                           ║
║  EVERY CLAIM NEEDS:                                                       ║
║  • Source or methodology                                                  ║
║  • Confidence level                                                       ║
║  • Key assumptions                                                        ║
║  • Sensitivity analysis for projections                                   ║
║                                                                           ║
║  RED FLAGS IN YOUR DOCUMENT:                                              ║
║  ✗ "This will be huge" → ✓ "TAM is $2B growing at 15% CAGR"             ║
║  ✗ "Obviously the right choice" → ✓ "Recommended based on [criteria]"   ║
║  ✗ "No real alternatives" → ✓ "Three options evaluated..."              ║
║  ✗ "Minimal risk" → ✓ "Key risks: [list] with mitigation: [list]"       ║
║                                                                           ║
║  EXEMPLAR PROMPTS TO STUDY:                                               ║
║  • swot_analysis.md (evidence requirements)                               ║
║  • board_deck_opportunity_solution_tree.md (executive format)             ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

## Related Resources

| Resource | Purpose |
|----------|---------|
| [NON_CODING_QUICK_START.md](../NON_CODING_QUICK_START.md) | Universal non-coding principles |
| [business-writing/](business-writing/) | The prompts this guide supports |
| [business-writing/business_writing_principles.md](business-writing/business_writing_principles.md) | The nine principles of prose quality — sentence level, where this guide is document level |
| [content-quality/](content-quality/) | Slop evaluators for finished drafts |
| [domain-product-management/](../domain-product-management/) | PRDs, market sizing, competitor teardown |
| [domain-business-strategy/](../domain-business-strategy/) | Company strategy and go-to-market |
| [domain-presentations/](../domain-presentations/) | Board decks and presentations |
| [PROMPT_QUALITY_STANDARDS.md](../PROMPT_QUALITY_STANDARDS.md) | Quality tier definitions |

---

*Created: 2026-01-26 · Relocated from `domain-product-management/README.md`: 2026-08-28*
*Domain: Professional Writing*
