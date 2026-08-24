# Product Requirements Document (PRD) Template

> Copy this template for feature specifications, product initiatives, and capability development.
> Designed for MVP-focused development with iterative refinement.

---

```markdown
# PRD: [Feature/Product Name]

**Status:** [Draft / In Review / Approved / In Development]
**Author:** [Name]
**Stakeholders:** [Key reviewers and approvers]
**Last Updated:** [Date]
**Target Release:** [Quarter/Sprint/Date]

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | [Date] | [Name] | Initial draft |
| [Continue...] | | | |

---

## Overview

### Problem Statement

**The Problem:**
[What problem are we solving? Be specific and measurable.]

**Who Has This Problem:**
[Target users - be specific about segment, not "all users"]

**How We Know It's a Problem:**
- Evidence 1: [Customer feedback, support tickets, churn data, etc.]
- Evidence 2: [Research, analytics, competitive pressure, etc.]
- Evidence 3: [Business impact - lost revenue, inefficiency, etc.]

**Current Workarounds:**
[How do users solve this today? What's inadequate about those solutions?]

### Solution Summary

[One paragraph describing what we're building. Focus on outcomes, not features.]

### Success Metrics

**Primary Metric (North Star):**
| Metric | Baseline | Target | Timeline | How Measured |
|--------|----------|--------|----------|--------------|
| [KPI] | [Current] | [Goal] | [By when] | [Instrumentation] |

**Secondary Metrics:**
| Metric | Baseline | Target | Purpose |
|--------|----------|--------|---------|
| [Metric 2] | [Current] | [Goal] | [Why we track this] |
| [Metric 3] | [Current] | [Goal] | [Why we track this] |

**Guardrail Metrics (Must Not Degrade):**
- [Metric that could be negatively affected]
- [Another metric to protect]

### Scope Definition

**In Scope (MVP):**
- ✅ [Capability 1]
- ✅ [Capability 2]
- ✅ [Capability 3]

**Explicitly Out of Scope:**
| Item | Reason for Exclusion | Future Consideration |
|------|---------------------|---------------------|
| [Feature X] | [Why not now] | [When we might add it] |
| [Feature Y] | [Why not now] | [When we might add it] |

---

## User Research

### Target Personas

**Primary Persona: [Name]**

| Attribute | Description |
|-----------|-------------|
| Role | [Job title, function] |
| Goals | [What they're trying to accomplish] |
| Pain Points | [Current frustrations] |
| Tech Savviness | [Low / Medium / High] |
| Usage Frequency | [How often they'd use this] |

**Secondary Persona: [Name]**
[Same structure]

### User Journey

**Current State (Pain Points Highlighted):**
```
[Step 1] → [Step 2] → ⚠️ [Pain Point] → [Step 3] → ⚠️ [Pain Point] → [End]
```

**Future State (With This Feature):**
```
[Step 1] → [Step 2] → ✅ [Improved] → [Step 3] → ✅ [Improved] → [End]
```

---

## User Stories

### Prioritization Framework

**P0 - Must Have:** MVP cannot ship without this
**P1 - Should Have:** Expected for quality product, but could ship without
**P2 - Nice to Have:** Adds value, lower priority
**P3 - Future:** Documented for later consideration

### User Stories by Priority

**P0 - Must Have:**

**US-001:** As a [persona], I want to [action] so that [outcome]

*Acceptance Criteria:*
- [ ] Given [context], when [action], then [result]
- [ ] Given [context], when [action], then [result]
- [ ] [Edge case handled]

*Notes:* [Design considerations, technical constraints]

---

**US-002:** As a [persona], I want to [action] so that [outcome]

*Acceptance Criteria:*
- [ ] [Criterion 1]
- [ ] [Criterion 2]

---

**P1 - Should Have:**

**US-003:** [Same format]

---

**P2 - Nice to Have:**

**US-004:** [Same format]

---

## Detailed Requirements

### Functional Requirements

| ID | Requirement | Priority | Acceptance Criteria | Notes |
|----|-------------|----------|---------------------|-------|
| FR-001 | [Requirement description] | P0 | [How to verify] | [Context] |
| FR-002 | [Requirement description] | P0 | [How to verify] | [Context] |
| FR-003 | [Requirement description] | P1 | [How to verify] | [Context] |

### Non-Functional Requirements

**Performance:**
- Page load time: < [X]ms for 95th percentile
- API response time: < [X]ms
- Concurrent users supported: [X]

**Reliability:**
- Uptime target: [X]%
- Error rate: < [X]%
- Data durability: [Requirements]

**Security:**
- Authentication: [Requirements]
- Authorization: [Requirements]
- Data protection: [Requirements]
- Compliance: [Requirements - GDPR, SOC2, etc.]

**Scalability:**
- Current scale: [Users, data volume]
- Target scale: [Growth expectations]
- Architecture requirements: [Implications]

**Accessibility:**
- WCAG level: [AA / AAA]
- Specific requirements: [Screen reader, keyboard nav, etc.]

### Dependencies

| Dependency | Type | Owner | Status | Risk if Delayed |
|------------|------|-------|--------|-----------------|
| [System/API/Team] | [Blocks/Informs] | [Name] | [Status] | [Impact] |

---

## Design

### Information Architecture

[Describe or link to IA diagrams]

### Wireframes/Mockups

[Link to design files: Figma, Sketch, etc.]

**Key Screens:**
1. [Screen 1]: [Purpose and key interactions]
2. [Screen 2]: [Purpose and key interactions]

### Design Decisions

| Decision | Options Considered | Choice | Rationale |
|----------|-------------------|--------|-----------|
| [Decision point] | [A, B, C] | [Choice] | [Why] |

### Edge Cases

| Scenario | Expected Behavior | Design Handling |
|----------|-------------------|-----------------|
| [Edge case 1] | [What should happen] | [How design addresses] |
| [Empty state] | [What user sees] | [Design approach] |
| [Error state] | [What user sees] | [Design approach] |

---

## Technical Approach

*Note: Detailed technical design in separate document. This is high-level only.*

### Architecture Overview

[High-level description of technical approach]

### Data Requirements

**Data Needed:**
- [Data type 1]: Source [X], Update frequency [Y]
- [Data type 2]: Source [X], Update frequency [Y]

**Data Created:**
- [New data type]: Storage [X], Retention [Y]

**Privacy Considerations:**
- [PII handling]
- [Data minimization]

### Integration Points

| System | Integration Type | Purpose | Owner |
|--------|-----------------|---------|-------|
| [System 1] | [API/Event/DB] | [What it enables] | [Team] |

### Technical Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| [Risk 1] | [H/M/L] | [H/M/L] | [Approach] |

---

## Go-to-Market

### Launch Strategy

**Rollout Phases:**

| Phase | Audience | Duration | Success Criteria | Go/No-Go |
|-------|----------|----------|------------------|----------|
| Internal | [Who] | [Time] | [Metrics] | [Decider] |
| Beta | [% or segment] | [Time] | [Metrics] | [Decider] |
| GA | All users | Ongoing | [Metrics] | N/A |

### Communication Plan

**Internal:**
- [Team/channel]: [Timing and message]

**External:**
- [Channel]: [Timing and message]

### Training/Enablement

- Documentation: [What's needed]
- Training: [Who needs it]
- Support: [How to prepare support team]

---

## Rollback Plan

**If Things Go Wrong:**

**Criteria for Rollback:**
- [Metric exceeds threshold X]
- [Critical bug of type Y]

**Rollback Process:**
1. [Step 1]
2. [Step 2]
3. [Communication]

**Recovery Time Objective:** [How fast we need to roll back]

---

## Open Questions

| # | Question | Owner | Due Date | Status | Impact if Unresolved |
|---|----------|-------|----------|--------|---------------------|
| 1 | [Question] | [Name] | [Date] | [Open/Resolved] | [What's blocked] |

---

## Appendix

### A. Research Data
[Links to user research, analytics, customer feedback]

### B. Competitive Analysis
[How competitors handle this]

### C. Technical Spike Results
[If exploration was done]

### D. Glossary
[Define terms specific to this feature]
```

---

## Tips for Effective PRDs

**Keep MVP Focused:**
- Challenge every requirement: "Can we ship without this?"
- Default to "out of scope" and require justification to include

**Make It Actionable:**
- Acceptance criteria should be testable
- Requirements should be unambiguous
- Edge cases should be explicitly addressed

**Keep It Current:**
- Update as decisions are made
- Mark resolved questions
- Communicate changes to stakeholders

---

## Quality Checklist

- [ ] Problem is validated (not assumed)
- [ ] Success metrics are measurable and baselined
- [ ] Scope is clearly defined (in/out)
- [ ] User stories have acceptance criteria
- [ ] Edge cases are addressed
- [ ] Dependencies are identified with owners
- [ ] Risks have mitigations
- [ ] Rollout plan exists with go/no-go criteria
- [ ] Open questions have owners and due dates
