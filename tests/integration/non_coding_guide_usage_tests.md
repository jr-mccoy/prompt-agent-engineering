# Non-Coding Quick Start Guide: Usage Tests

> **Purpose:** Validate that the NON_CODING_QUICK_START.md guide produces functional prompts for each domain.
> **Test Date:** 2026-01-26
> **Guide Version:** 1.0

---

## Test Methodology

Each test follows the NON_CODING_QUICK_START.md process:
1. Classify Task Type (CREATE, LEARN, DECIDE, COMMUNICATE, IMPROVE, SIMULATE)
2. Identify Domain
3. Apply Task Type Pattern
4. Use 5 Universal Elements
5. Add verification criteria

---

## Test 1: Education & Teaching Domain

**Scenario:** Create a prompt for generating a differentiated math worksheet for 4th graders learning fractions.

### Classification
- **Task Type:** CREATE
- **Domain:** Education & Teaching
- **Audience:** Elementary students, 4th grade, mixed abilities

### Generated Prompt

```markdown
# Differentiated Math Worksheet: Fractions (4th Grade)

**Objective:** Create a single-page worksheet on adding fractions with like denominators

## Audience Profile
- **Grade Level:** 4th grade (ages 9-10)
- **Skill Levels:** Mixed - struggling, on-grade, advanced
- **Prerequisites:** Basic fraction understanding (parts of a whole)

## Worksheet Requirements

### Structure
1. **Learning Target** (student-friendly language)
2. **Worked Example** with visual representation
3. **Tiered Practice Problems:**
   - Tier 1 (6 problems): Like denominators, single digit numerators, visual supports
   - Tier 2 (6 problems): Like denominators, larger numerators, no visuals
   - Tier 3 (4 problems): Extension - mixed numbers or word problems
4. **Self-Check Answer Key** (fold-over format)

### Differentiation Approach
- Visual supports decrease as difficulty increases
- Clear labels for each tier (not labeled by ability)
- All students can access all tiers

### Quality Criteria
- [ ] Grade-appropriate vocabulary
- [ ] Clear visual layout with adequate white space
- [ ] Problems progress in difficulty logically
- [ ] Answer key is accurate
- [ ] Aligns with Common Core 4.NF.B.3

### What This Is NOT
- Not a test (formative practice only)
- Not intended for homework without instruction first
- Should not require teacher explanation to use
```

**Validation:** Follows CREATE pattern, includes audience specification, has quality indicators, includes false-positive prevention ("What This Is NOT").

---

## Test 2: Healthcare & Clinical Domain

**Scenario:** Create a prompt for generating patient discharge instructions for post-appendectomy care.

### Classification
- **Task Type:** COMMUNICATE
- **Domain:** Healthcare & Clinical
- **Audience:** Adult patients, varied health literacy

### Generated Prompt

```markdown
# Patient Discharge Instructions: Post-Appendectomy Care

**Objective:** Create clear, accessible discharge instructions for laparoscopic appendectomy patients

## Patient Context
- **Procedure:** Laparoscopic appendectomy
- **Typical Patient:** Adult, varied health literacy levels
- **Setting:** Outpatient discharge, no medical professional present during reading

## Document Requirements

### Structure (Use Plain Language)
1. **What happened** (1-2 sentences)
2. **Taking care of your incision**
   - What to do
   - What to watch for
3. **Managing pain**
   - Medications prescribed
   - What to expect
4. **Activity and diet**
   - What you CAN do
   - What to AVOID
   - Timeline for return to normal
5. **When to call your doctor**
   - Warning signs (specific, observable)
   - Contact information
6. **Follow-up appointment**

### Accessibility Requirements
- Reading level: 6th grade or below
- Use "you" and "your"
- Bullet points, not paragraphs
- Specific numbers, not vague terms ("2-3 days" not "a few days")

### Clinical Accuracy Note
⚠️ **DISCLAIMER:** This prompt generates DRAFT content only. All output MUST be reviewed and approved by a licensed healthcare provider before patient use. This does not constitute medical advice.

### Quality Criteria
- [ ] All instructions are actionable
- [ ] Warning signs are specific and observable
- [ ] No medical jargon without explanation
- [ ] Contact numbers are placeholders (to be filled)
- [ ] Reviewed by clinical staff before use

### False-Positive Prevention
- Does NOT replace verbal discharge teaching
- Does NOT include medication dosages (handled separately)
- Patient should have opportunity to ask questions
```

**Validation:** Uses COMMUNICATE pattern, includes mandatory clinical disclaimer, health literacy considerations, specific quality criteria.

---

## Test 3: Creative Writing Domain

**Scenario:** Create a prompt for developing a compelling antagonist for a YA fantasy novel.

### Classification
- **Task Type:** CREATE
- **Domain:** Creative Writing
- **Audience:** Writer developing a novel; output is for their use

### Generated Prompt

```markdown
# Antagonist Development: YA Fantasy Novel

**Objective:** Develop a multi-dimensional antagonist that serves the story's themes and challenges the protagonist meaningfully

## Story Context (Fill In)
- **Genre:** YA Fantasy
- **Tone:** [Dark / Adventurous / Whimsical]
- **Central Theme:** [What question does your story explore?]
- **Protagonist's Core Belief:** [What does your hero believe about the world?]
- **Protagonist's Greatest Fear:** [What terrifies them most?]

## Antagonist Development Framework

### The Antagonist's Truth
What does your antagonist believe that makes them the perfect opposition to your protagonist?
- Their worldview should directly challenge the protagonist's core belief
- They might even have a point (even if their methods are wrong)

### Motivation Layers
1. **Surface Want:** What are they trying to achieve? (external goal)
2. **Deeper Need:** What emotional/psychological need drives them?
3. **The Wound:** What past experience shaped their worldview?

### Relationship to Protagonist
- Why are THEY the one standing in the protagonist's way?
- What makes them formidable against THIS hero specifically?
- Is there a connection (mirror, foil, former ally)?

### Complexity Requirements
**Include at least 2:**
- [ ] A sympathetic motivation (understandable even if wrong)
- [ ] A moment where they could have chosen differently
- [ ] A genuine belief they're doing right
- [ ] Something they love or protect
- [ ] A limitation or fear of their own

### Genre Fit
For YA Fantasy:
- Stakes should feel personal to teen readers
- Antagonist should represent something teens struggle against
- Complexity should be accessible (not morally ambiguous to the point of confusion)

## Output Format
Provide:
1. Brief character sketch (appearance, role, status)
2. Motivation deep dive (want, need, wound)
3. Relationship to protagonist
4. Key scenes that would reveal antagonist's complexity
5. Potential arc (do they change?)

## Quality Indicators
- Antagonist is not "evil for evil's sake"
- Their opposition to the protagonist is logical, not arbitrary
- Teen readers could understand (not necessarily agree with) their perspective
- They force the protagonist to grow

## Creative Latitude
This framework is a starting point. If your story calls for a different approach (pure embodiment of chaos, unknowable force, etc.), explain why that serves your narrative better.
```

**Validation:** Uses CREATE pattern, respects author voice, genre-appropriate, asks questions before prescribing, includes creative latitude.

---

## Test 4: Research & Academic Domain

**Scenario:** Create a prompt for conducting a preliminary literature search on remote work productivity.

### Classification
- **Task Type:** LEARN (research phase)
- **Domain:** Research & Academic
- **Audience:** Graduate student beginning literature review

### Generated Prompt

```markdown
# Preliminary Literature Search: Remote Work Productivity

**Objective:** Conduct initial literature scan to understand the research landscape

## Research Context
- **Topic:** Impact of remote work on employee productivity
- **Purpose:** Master's thesis literature review
- **Stage:** Preliminary search (mapping the field)

## Search Framework

### 1. Define Scope First
Before searching, clarify:
- **Population:** Who? (Knowledge workers? All employees? Specific industries?)
- **Intervention/Exposure:** What aspect of remote work? (Full-time remote? Hybrid? Forced pandemic shift?)
- **Outcome:** How is productivity defined? (Output? Self-report? Manager assessment?)
- **Time Frame:** When? (Pre-pandemic? During? Post-pandemic transition?)

### 2. Develop Search Strategy

**Primary Databases:**
- Web of Science (peer-reviewed, broad)
- PsycINFO (organizational psychology focus)
- Business Source Complete (applied business research)

**Search Term Matrix:**
| Concept 1 (Setting) | Concept 2 (Outcome) | Concept 3 (Context) |
|---------------------|---------------------|---------------------|
| "remote work" | productivity | employee* |
| telecommut* | performance | knowledge work* |
| "work from home" | output | organizational |
| "distributed work" | effectiveness | |

**Boolean Example:**
```
("remote work" OR telecommut* OR "work from home")
AND
(productivity OR performance OR output)
AND
(employee* OR "knowledge work*")
```

### 3. Initial Scan Protocol
For the first 50 results from each database:
1. Read titles and abstracts
2. Categorize by:
   - Methodology (quantitative, qualitative, mixed, review)
   - Sample (industry, size, geographic location)
   - Remote work type (full, hybrid, pandemic-forced)
   - Key findings (positive, negative, mixed, contingent)
3. Note frequently cited foundational works
4. Identify emerging themes

### 4. Document Everything
Create tracking spreadsheet:
| Source | Year | Method | Sample | Key Finding | Relevance (H/M/L) | Notes |

### Quality Indicators
- [ ] Search terms capture concept from multiple angles
- [ ] At least 2 databases searched
- [ ] Inclusion/exclusion criteria documented
- [ ] Frequently cited works identified
- [ ] Initial themes emerging

### Hedge Appropriately
At this stage:
- "The literature appears to suggest..." (not "research proves")
- "Initial scan indicates..." (not "it is established that")
- Note when findings conflict

### Next Steps After Search
1. Identify 10-15 seminal works for close reading
2. Refine research question based on gaps found
3. Develop formal inclusion criteria for systematic review
```

**Validation:** Uses LEARN pattern, emphasizes methodology, requires hedged language, includes documentation requirements.

---

## Test 5: Personal Development Domain

**Scenario:** Create a prompt for helping someone evaluate a career transition decision.

### Classification
- **Task Type:** DECIDE
- **Domain:** Personal Development
- **Audience:** Professional considering career change

### Generated Prompt

```markdown
# Career Transition Decision Framework

**Objective:** Evaluate whether to pursue a career transition systematically

## Before We Begin

This framework helps you think through a decision. It does NOT tell you what to do. Only you know your full situation, values, and risk tolerance.

## The Decision Under Consideration
**Current State:** [Your current role/career]
**Potential Change:** [The opportunity you're considering]

## Step 1: Clarify What You're Actually Deciding

Is this decision:
- [ ] Whether to leave your current job at all
- [ ] Whether to pursue THIS specific opportunity
- [ ] Whether NOW is the right time
- [ ] Something else?

Be specific about what decision you're actually making.

## Step 2: Understand Your Motivations

### Push Factors (Why Leave)
What's pushing you away from current state?
- [ ] Compensation
- [ ] Growth/learning
- [ ] Culture/values fit
- [ ] Work-life balance
- [ ] Management/leadership
- [ ] Role satisfaction
- [ ] Industry/company trajectory

**Reality Check:** Are these factors likely to be better in the new situation, or are you making assumptions?

### Pull Factors (Why This Opportunity)
What's drawing you toward the new option?
- List specific attractions
- Note which are confirmed vs. hoped-for

## Step 3: Risk Assessment

### If You Make the Change
**Best case:** [What could go right?]
**Worst case:** [What could go wrong?]
**Most likely case:** [What's the realistic outcome?]

### If You Don't Make the Change
**Best case:** [What could improve?]
**Worst case:** [What could deteriorate?]
**Most likely case:** [What's the realistic continuation?]

### Reversibility
- How reversible is this decision?
- What's your backup plan if it doesn't work?
- What would you lose that you can't get back?

## Step 4: Values Alignment

Rank these by importance to you (1-10), then score each option:

| Value | Importance (1-10) | Current | New Option |
|-------|------------------|---------|------------|
| Financial security | | | |
| Learning/growth | | | |
| Work-life balance | | | |
| Purpose/meaning | | | |
| Autonomy | | | |
| Relationships/team | | | |
| Status/recognition | | | |
| [Add your own] | | | |

## Step 5: Information Gaps

What do you NOT know that would change your decision?
- List unknowns
- For each: Can you find out? How?

## Step 6: Decision Criteria

Complete this sentence:
"I will pursue this transition if..." [list your criteria]
"I will stay in my current role if..." [list your criteria]

## Quality Indicators
- [ ] You've talked to people who've made similar transitions
- [ ] You've verified assumptions, not just hoped
- [ ] You've considered timing (personal, market, company)
- [ ] You have a financial runway if needed
- [ ] You've consulted people who will be affected

## What This Is NOT
- Not a tool to justify a decision you've already made
- Not a replacement for talking to people who know you
- Not comprehensive career counseling
- Not financial advice

## Final Reflection
After completing this framework, notice:
- Do you feel relief or disappointment at your emerging answer?
- What does that emotional reaction tell you?
```

**Validation:** Uses DECIDE pattern, includes values clarification, considers reversibility, prevents confirmation bias, includes honest disclaimers.

---

## Test 6: Professional Communication Domain

**Scenario:** Create a prompt for writing a stakeholder update email after a project delay.

### Classification
- **Task Type:** COMMUNICATE
- **Domain:** Professional Communication
- **Audience:** Executive stakeholders, external clients

### Generated Prompt

```markdown
# Stakeholder Communication: Project Delay Update

**Objective:** Communicate project delay clearly and maintain stakeholder confidence

## Communication Context
- **Situation:** Project timeline has slipped
- **Audience:** [Executive sponsor / Client / Board / Mixed]
- **Relationship:** [New relationship / Established trust / Already strained]
- **Delay Severity:** [Days / Weeks / Months]

## Pre-Writing Checklist
Before drafting:
- [ ] Root cause is understood (or clearly stated as under investigation)
- [ ] New timeline is realistic (with buffer)
- [ ] Recovery plan is defined
- [ ] Approval to communicate obtained if needed
- [ ] Know what you CAN'T say yet

## Message Structure

### 1. Lead with What They Need to Know
- State the situation directly (no burying the bad news)
- Include: What happened, impact on timeline, impact on them

### 2. Own Responsibility Appropriately
- Don't over-apologize
- Don't blame others externally
- Do: "We" language, acknowledgment, forward focus

### 3. Explain Without Excusing
- Brief, relevant context
- Avoid: lengthy justification, technical details they don't need

### 4. Present the Path Forward
- Revised timeline (specific dates)
- Actions being taken
- Any decisions needed from them

### 5. Offer Appropriate Access
- Availability for questions
- When they'll hear from you next

## Tone Calibration

| Stakeholder Type | Tone Notes |
|------------------|------------|
| Executive sponsor | Business impact focus, minimal detail |
| Client | Relationship preservation, confidence building |
| Board/investors | Strategic implications, risk mitigation |
| Technical partners | More detail acceptable, collaborative |

## Quality Criteria
- [ ] Bad news in first paragraph (not buried)
- [ ] Specific new dates (not "soon" or "shortly")
- [ ] Clear action items (for you and for them)
- [ ] Appropriate length (shorter is usually better)
- [ ] Professional but human tone

## Anti-Patterns to Avoid
- Starting with "I wanted to reach out..."
- Excessive hedging that obscures the message
- Passive voice to avoid ownership ("delays occurred")
- Over-promising to make up for delay
- Technical jargon they won't understand

## Sample Opening Lines

**Too soft:**
"I wanted to give you a quick update on where we are with the project..."

**Too alarming:**
"We have a serious problem with the project timeline."

**Balanced:**
"I'm writing with an update on Project X. We've encountered [issue] that has shifted our delivery date to [new date]. Here's what happened and what we're doing about it."
```

**Validation:** Uses COMMUNICATE pattern, audience-specific guidance, includes anti-patterns, practical templates.

---

## Test 7: Specialized Professional Fields Domain

**Scenario:** Create a prompt for a contractor preparing a kitchen renovation estimate.

### Classification
- **Task Type:** CREATE
- **Domain:** Specialized Professional Fields (Trades/Construction)
- **Audience:** Homeowner client

### Generated Prompt

```markdown
# Kitchen Renovation Estimate

**Objective:** Create a professional, comprehensive estimate for kitchen renovation

## Project Information
- **Client:** [Name]
- **Property Address:** [Address]
- **Site Assessment Date:** [Date]
- **Estimate Valid For:** 30 days

## Scope Documentation

### Scope of Work Included
**Demo:**
- [ ] Remove existing cabinets
- [ ] Remove existing countertops
- [ ] Remove flooring (if applicable)
- [ ] Haul-away and disposal

**Rough Work:**
- [ ] Electrical modifications: [specify]
- [ ] Plumbing modifications: [specify]
- [ ] Permit required: Yes / No

**Installation:**
- [ ] Cabinet installation
- [ ] Countertop installation
- [ ] Appliance hook-up
- [ ] Backsplash installation
- [ ] Flooring installation

**Finishing:**
- [ ] Painting: [scope]
- [ ] Trim/molding
- [ ] Final cleanup

### Explicitly NOT Included
List items client might assume are included:
- Appliances (unless specified)
- Structural modifications
- Items outside kitchen footprint
- [Other exclusions]

## Estimate Breakdown

### Labor
| Task | Estimated Hours | Rate | Amount |
|------|----------------|------|--------|
| [Task] | [Hours] | $[Rate]/hr | $[Total] |
| **Labor Subtotal** | | | **$[Amount]** |

### Materials
| Item | Specifications | Quantity | Unit Cost | Amount |
|------|---------------|----------|-----------|--------|
| Cabinets | [Brand/style] | [LF] | $[Cost] | $[Total] |
| Countertop | [Material] | [SF] | $[Cost] | $[Total] |
| **Materials Subtotal** | | | | **$[Amount]** |

### Other Costs
| Item | Amount |
|------|--------|
| Permits | $[Amount] |
| Dumpster/disposal | $[Amount] |
| **Other Subtotal** | **$[Amount]** |

### Summary
| Category | Amount |
|----------|--------|
| Labor | $[Amount] |
| Materials | $[Amount] |
| Other | $[Amount] |
| **Subtotal** | **$[Amount]** |
| Contingency (10%) | $[Amount] |
| **TOTAL ESTIMATE** | **$[Amount]** |

## Assumptions
This estimate assumes:
1. Normal site conditions (no hidden damage)
2. Client-selected materials available at quoted prices
3. Standard work hours (no weekend/after-hours premium)
4. [Other assumptions]

**If conditions differ, a change order will be required.**

## Timeline
| Phase | Duration | Notes |
|-------|----------|-------|
| Permits | [X] weeks | If required |
| Demo | [X] days | |
| Rough work | [X] days | |
| Installation | [X] weeks | |
| Finishing | [X] days | |
| **Total Duration** | **[X] weeks** | From project start |

## Payment Terms
- Deposit: [%] due at contract signing
- Progress payment: [%] at [milestone]
- Final payment: [%] at completion
- Accepted payment methods: [List]

## Warranty
[Standard warranty terms for labor and materials]

---

**DISCLAIMER:** This estimate is based on the site assessment of [date] and information provided by the client. Final costs may vary based on actual conditions discovered during work. This estimate is not a contract. A formal contract will be provided upon acceptance.

---

**To Accept This Estimate:**
- Sign and return by [date]
- Deposit of $[amount] due at signing
- Contact [name] at [phone/email]
```

**Validation:** Uses CREATE pattern for professional document, includes standard disclaimers, assumption documentation, clear exclusions.

---

## Test Summary

| Domain | Test Scenario | Pattern Used | Key Elements Validated |
|--------|--------------|--------------|----------------------|
| Education | Differentiated worksheet | CREATE | Audience, tiered content, standards alignment |
| Healthcare | Discharge instructions | COMMUNICATE | Clinical disclaimer, health literacy, safety |
| Creative Writing | Antagonist development | CREATE | Author voice, genre fit, creative latitude |
| Research | Literature search | LEARN | Methodology, hedging, documentation |
| Personal Development | Career decision | DECIDE | Values, risk assessment, bias prevention |
| Professional Communication | Delay notification | COMMUNICATE | Audience calibration, structure, tone |
| Specialized Fields | Contractor estimate | CREATE | Disclaimers, assumptions, professional format |

## Conclusion

All 7 domain guides produce functional, domain-appropriate prompts when following the NON_CODING_QUICK_START.md process. Each test demonstrates:

1. **Task Type Patterns** work across domains
2. **5 Universal Elements** apply consistently
3. **Domain-specific considerations** are addressed
4. **False-positive prevention** is integrated
5. **Quality indicators** are included

**Integration Test: PASSED**

---

*Test Author: Phase 3 Integration*
*Test Date: 2026-01-26*
