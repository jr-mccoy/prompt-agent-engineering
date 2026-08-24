# PRD (Product Requirements Document)

**Source:** BUSINESS_WRITING_PROMPTS.md

**Category:** Business Writing / Product Development

## Prompt

```
You are writing a PRD that bridges what we're building (product/business) with how we'll build it (engineering).

CONTEXT:
Feature/Product name: [NAME]
Product owner: [WHO OWNS THIS]
Target release: [WHEN THIS SHIPS]
User problem being solved: [THE CORE PROBLEM]

INPUT PROVIDED:
[PASTE YOUR USER RESEARCH, TECHNICAL CONSTRAINTS, BUSINESS REQUIREMENTS, DESIGN MOCKS HERE]

YOUR TASK:
Create a PRD that gives engineering everything they need to build this without constant back-and-forth. This document will be referenced during implementation, so precision matters more than polish.

REQUIRED STRUCTURE:
1. **What We're Building** (2-3 sentences: the feature in user terms, not technical terms)
2. **Why Now** (The business case and user problem - include data)
3. **Success Criteria** (3 specific, measurable outcomes with targets)
4. **User Stories** (5-8 stories in format: "As [user type], I want to [action] so that [benefit]")
5. **Acceptance Criteria** (For each user story, the testable conditions that define "done")
6. **Non-Goals** (What we're explicitly NOT building - prevents scope creep)
7. **Technical Constraints** (What engineering must work within - APIs, performance, scale)
8. **Open Questions** (What's undecided and who will decide it by when)

CONSTRAINTS:
- Total length: 800 words maximum
- What We're Building: Must be understandable to non-technical stakeholders
- Why Now: Must include quantified user problem ("42% of users abandon at this step") and business impact
- Success criteria: Must be measurable at launch ("85% of flows complete without errors" not "improve reliability")
- User stories: Must follow exact format and include user type, action, and benefit
- Acceptance criteria: Must be testable ("User can upload files up to 50MB" not "File upload works well")
- Non-Goals: Must be as specific as user stories (prevents "I thought we were building that" conversations)
- Technical constraints: Must include performance targets ("API response <200ms at P95 under 1000 RPS")
- Open questions: Must have owner and decision deadline
- DO NOT include: solution details (that's engineering's job), UI mockups (link them), exact implementation steps
- DO NOT assume: If a requirement isn't explicit, it goes in Open Questions
- Use only information from input - do not infer user needs or technical constraints

TONE:
- Precise and testable, not aspirational
- Declarative ("The system will X") not suggestive ("The system should probably X")
- Specific about edge cases ("What happens when user uploads 100MB file?")
- Clear about what's decided vs. what's open

QUALITY CHECKS - Before outputting, verify:
- [ ] Every user story follows format: "As [type], I want to [action] so that [benefit]"
- [ ] Every user story has corresponding acceptance criteria
- [ ] All acceptance criteria are testable (QA can verify pass/fail)
- [ ] Success criteria are measurable at launch (not 6 months later)
- [ ] Non-Goals section exists and has at least 4 items
- [ ] Every technical constraint has a number (response time, data size, load, etc.)
- [ ] Every open question has owner and deadline
- [ ] No solution prescribed (no "use Redis" or "implement with React")
- [ ] Edge cases are addressed ("What if user has no internet?")
- [ ] Total word count is under 800 words

If any check fails, revise before outputting.
```

## Usage Notes

**Purpose:** PRDs exist to align product and engineering, preventing the "that's not what I meant" conversation during development.

**Customization Options:**
- Adjust for engineering culture (who owns solutions - product vs. engineering)
- Modify for product process (design-first, validation-in-production, iterative)
- Add sections for different feature types (API, data, performance, platform, experimental)

**Common Pitfalls:**
- Vague requirements ("improve user experience")
- Missing edge cases (only happy path)
- Prescribing solutions instead of describing problems
- Success criteria that can't be measured at launch
- No non-goals section (scope creep)
- Unstated technical constraints
