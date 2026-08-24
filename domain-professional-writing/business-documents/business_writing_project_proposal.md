# Project Proposal (Resource Allocation Request)

**Source:** BUSINESS_WRITING_PROMPTS.md

**Category:** Business Writing / Resource Allocation

## Prompt

```
You are writing a project proposal that secures approval and resources for a specific initiative.

CONTEXT:
Project name: [PROJECT NAME]
Goal: [WHAT THIS PROJECT WILL ACHIEVE]
Requesting from: [WHO APPROVES THIS - name/role]
Resources needed: [SUMMARY - e.g. "2 engineers for 8 weeks, $50K budget"]
Approval deadline: [WHEN YOU NEED APPROVAL]

INPUT PROVIDED:
[PASTE YOUR PROJECT DETAILS, RESEARCH, ESTIMATES, REQUIREMENTS HERE]

YOUR TASK:
Create a project proposal that makes the case for investment and clearly defines scope. This will be used to allocate resources and set expectations, so scope boundaries matter as much as scope itself.

REQUIRED STRUCTURE:
1. **The Problem** (What's broken or missing that this fixes - 2-3 sentences max)
2. **The Solution** (What you'll build/do - 2-3 sentences, outcomes not features)
3. **Success Metrics** (3 specific KPIs that define success, with targets and timeframe)
4. **Resource Requirements** (People, budget, timeline - be specific)
5. **Scope Boundaries** (What's IN scope, what's explicitly OUT of scope)
6. **Dependencies** (What you need from other teams, when you need it)
7. **Risks** (Top 3 risks with likelihood and mitigation)

CONSTRAINTS:
- Total length: 600 words maximum
- Problem: Must be specific ("Support tickets increased 40% with no headcount increase") not generic ("Support is struggling")
- Solution: Must be stated as outcome ("Reduce average ticket resolution time from 4 hours to 90 minutes") not activity ("Build automation")
- Success metrics: Must include number, timeframe, measurement method ("Increase NPS from 42 to 55 by Q2, measured via post-interaction survey")
- Resources: Must include costs ("2 senior engineers @ $200K fully loaded = $400K")
- Scope boundaries: OUT OF SCOPE section must be as detailed as IN SCOPE (prevents scope creep)
- Dependencies: Must include team name, deliverable, date needed ("Need: API access from Platform team by Nov 15")
- Timeline: Must be broken into phases with deliverables ("Phase 1 (Weeks 1-3): Core routing logic - deliverable: 50% of tickets auto-routed")
- DO NOT include: nice-to-haves in main scope, aspirational metrics, vague resource needs
- DO NOT soften: If timeline is aggressive, say so. If dependencies are risky, say so.
- Use only data from input - do not estimate effort or cost without engineering input

TONE:
- Specific and scoped, not ambitious and expansive
- State constraints clearly ("This does NOT include mobile, which would require +6 weeks")
- Be realistic about risks, not optimistic
- Focus on outcomes and metrics, not features and activities

QUALITY CHECKS - Before outputting, verify:
- [ ] Problem is quantified with specific data
- [ ] Solution is stated as measurable outcome
- [ ] All 3 success metrics have number + timeframe + measurement method
- [ ] Resource costs are fully loaded (not just salary)
- [ ] OUT OF SCOPE section exists and lists at least 3 things
- [ ] Every dependency has team name, deliverable, and date
- [ ] Timeline has phases with specific deliverables per phase
- [ ] Each risk has likelihood (high/medium/low) and specific mitigation
- [ ] No feature is included without clear connection to success metric
- [ ] Total word count is under 600 words

If any check fails, revise before outputting.
```

## Usage Notes

**Purpose:** Proposals exist to get a yes/no decision on resource allocation. The structure forces you to define success before defining the work.

**Customization Options:**
- Adjust for different approval processes (executive sign-off, finance approval, multi-team buy-in)
- Modify for different project types (technical, research, process improvement, experimental, urgent)
- Add sections for OKRs, budget breakdown, stakeholder impact

**Common Pitfalls:**
- Vague problem statement without urgency
- Solution describes features, not outcomes
- Aspirational metrics ("significantly improve")
- Underestimated resources
- Scope creep (everything in scope, nothing out of scope)
- Hidden dependencies
