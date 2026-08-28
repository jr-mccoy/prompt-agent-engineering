---
title: "Blue Ocean Strategy Analysis for Codebase"
category: software-engineering/analysis/business
description: "Apply Blue Ocean Strategy to identify opportunities for creating uncontested market space through value innovation, using the Four Actions Framework (Eliminate, Reduce, Raise, Create) to differentiate from competitors"
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - DS-01  # Framework Application
  - RT-02  # Multi-Dimensional Analysis
  - QA-02  # Adversarial Thinking
  - DS-06  # Prioritization Guidance
difficulty: advanced
tags:
  - strategic-analysis
  - competitive-strategy
  - value-innovation
  - market-creation
  - differentiation
updated: "2026-01-25"
related_prompts:
  - domain-software-engineering/analysis/business/competitive_positioning_map.md
  - domain-software-engineering/analysis/business/value_proposition_canvas_analysis.md
  - domain-software-engineering/analysis/business/porters_five_forces_analysis.md
  - domain-software-engineering/analysis/business/ansoff_matrix_analysis.md
---

# Blue Ocean Strategy Analysis for Codebase

**Objective:** Analyze the codebase and its associated product to identify opportunities for creating uncontested market space through value innovation, using the Four Actions Framework to systematically evaluate what to eliminate, reduce, raise, and create to break the value-cost tradeoff and escape red ocean competition.

## When to Use

- **Use when:** Competing in a crowded market with commodity features and price pressure
- **Use when:** Seeking to differentiate beyond incremental improvements
- **Use when:** Evaluating whether to compete head-on or create new market space
- **Use when:** Planning major product strategy shifts or new product lines
- **Don't use when:** You have strong PMF and just need to scale existing approach
- **Don't use when:** Immediate competitive response is needed (Blue Ocean requires longer-term thinking)
- **Don't use when:** Market is nascent—there's no "red ocean" to escape yet

## Instructions

1. **Map the Current Competitive Landscape**
   - Identify the product's industry and primary competitive arena
   - List the top 5-10 competitors in the space
   - Identify the factors the industry competes on (features, price, quality, speed, etc.)
   - Note which factors receive the most investment and attention
   - **Evidence to collect:** Competitor feature matrices, pricing data, marketing positioning

2. **Build the Strategy Canvas (As-Is State)**
   - Plot your product against competitors on key competitive factors
   - Identify where your product over-invests (doing more than needed)
   - Identify where your product under-invests (falling behind)
   - Note where all competitors look similar (convergence = red ocean)
   - **Evidence to collect:** Feature audits, user research on what matters, competitive intelligence

3. **Analyze Non-Customers (The Three Tiers)**

   **a. Soon-to-be Non-Customers (Tier 1):**
   - Who is on the edge of your market, minimally using solutions?
   - Why are they not fully committed to current offerings?
   - What would pull them in more deeply?

   **b. Refusing Non-Customers (Tier 2):**
   - Who consciously chose against your industry's offerings?
   - What do they find unacceptable or insufficient?
   - What alternative solutions do they use instead?

   **c. Unexplored Non-Customers (Tier 3):**
   - Who has never considered your industry as an option?
   - What distant markets might have similar underlying needs?
   - What assumptions make them seem "not our customer"?

   - **Evidence to collect:** Lost deal analysis, survey of non-users, adjacent market research

4. **Apply the Four Actions Framework**

   **a. ELIMINATE - Which factors that the industry takes for granted should be eliminated?**
   - What features do competitors offer that no one actually values?
   - What legacy features exist only because "we've always had them"?
   - What costs can be removed without meaningful value loss?
   - **Red flags:** Features with low usage but high maintenance cost

   **b. REDUCE - Which factors should be reduced well below the industry standard?**
   - What features are "good enough" at a lower level than competitors offer?
   - Where is the industry over-serving customer needs?
   - What premium features could be simplified without losing core value?
   - **Red flags:** Features users say are "nice to have" but won't pay extra for

   **c. RAISE - Which factors should be raised well above the industry standard?**
   - What do customers truly value that the industry under-delivers?
   - What pain points does the industry ignore or minimize?
   - Where could exceptional performance create breakthrough value?
   - **Red flags:** Features where users complain but accept industry norms

   **d. CREATE - Which factors should be created that the industry has never offered?**
   - What new value could address jobs-to-be-done in novel ways?
   - What adjacent needs could be bundled into the solution?
   - What would make non-customers suddenly interested?
   - **Red flags:** Look for workarounds users build themselves

5. **CRITICAL: Validate Blue Ocean Opportunities Before Reporting**
   - For each opportunity, answer:
     - Is this a real customer need or our assumption?
     - Have we validated that customers would value this change?
     - Is this truly differentiated or will competitors follow quickly?
     - Is this operationally feasible to deliver?
   - Test against the "Three Characteristics of a Good Strategy":
     - **Focus:** Does it concentrate resources on key factors?
     - **Divergence:** Does the strategy canvas look different from competitors?
     - **Compelling Tagline:** Can you describe it in one sentence that resonates?
   - Assess risks of each recommendation

6. **Develop the To-Be Strategy Canvas**
   - Plot the new value curve after implementing Four Actions changes
   - Ensure the curve looks distinctly different from competitors (divergence)
   - Verify the curve focuses resources rather than spreading thin
   - Create a compelling tagline that captures the new value proposition

7. **Prioritize and Plan Implementation**
   - Rank opportunities by impact and feasibility
   - Identify quick wins vs. long-term initiatives
   - Note dependencies and sequencing requirements
   - Flag capabilities that need to be built or acquired

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Propose eliminating features without verifying customers don't value them
- Assume "create" ideas are blue oceans without checking competitor roadmaps
- Confuse niche segmentation with blue ocean (smaller pond ≠ uncontested water)
- Recommend changes that sacrifice profitability (Blue Ocean ≠ low price)
- Present theoretical opportunities without evidence of customer need
- Assume non-customers don't use the category—verify why they don't
- Ignore execution complexity; the best strategy fails if it can't be built

✅ **DO:**
- Validate each ERRC (Eliminate, Reduce, Raise, Create) action with evidence
- Distinguish between "different" and "valuable different"
- Test blue ocean hypotheses with actual non-customer research
- Verify that proposed changes create value AND reduce/maintain costs
- Challenge whether opportunities are defensible or easily copied
- Consider the transition path from current state to blue ocean position
- Acknowledge limitations and assumptions in the analysis

## Confidence Levels

Rate each Four Actions recommendation with a confidence level:

- **Validated:** Customer evidence (interviews, usage data, surveys) supports this change
- **Inferred:** Market signals suggest this but no direct validation; needs testing
- **Hypothesis:** Logical reasoning suggests opportunity; significant validation needed

## Expected Output

A comprehensive Blue Ocean Strategy analysis including:
- Current strategy canvas (as-is competitive position)
- Non-customer analysis with opportunity insights
- Four Actions Framework recommendations with evidence
- To-Be strategy canvas (differentiated value curve)
- Prioritized implementation roadmap

### Output Format

```markdown
## Blue Ocean Strategy Analysis: [Product Name]

### Executive Summary
[3-5 sentences summarizing key opportunities for creating uncontested market space]

### Current Competitive Landscape

#### Strategy Canvas (As-Is)
[Visual representation showing your product vs competitors across competitive factors]

```
Factor          | Low ←───────────────────────→ High |
----------------|-------------------------------------|
Price           | [Your product: ●] [Comp A: ○] [Comp B: □]
Features        | ...
Ease of Use     | ...
Performance     | ...
Support         | ...
[etc.]          | ...
```

#### Convergence Points
[Where all competitors cluster = red ocean territory]

#### Your Current Position
[How you compare; over-investment and under-investment areas]

### Non-Customer Analysis

#### Tier 1: Soon-to-be Non-Customers
- **Who:** [Description]
- **Why leaving/minimal engagement:** [Reasons]
- **Opportunity:** [What could pull them in]

#### Tier 2: Refusing Non-Customers
- **Who:** [Description]
- **Why refusing:** [Reasons]
- **Alternative solutions:** [What they use instead]
- **Opportunity:** [What would change their mind]

#### Tier 3: Unexplored Non-Customers
- **Who:** [Description]
- **Why never considered:** [Assumptions blocking them]
- **Opportunity:** [How to reach them]

### Four Actions Framework

#### ELIMINATE (Stop Doing)
| Factor | Industry Status | Evidence to Eliminate | Impact | Confidence |
|--------|-----------------|----------------------|--------|------------|
| [Factor] | Standard feature | [Why not valued] | [Cost/complexity savings] | Validated/Inferred/Hypothesis |

#### REDUCE (Do Less)
| Factor | Industry Level | Proposed Level | Evidence | Impact | Confidence |
|--------|---------------|----------------|----------|--------|------------|
| [Factor] | High investment | Adequate | [Why less is enough] | [Savings] | Validated/Inferred/Hypothesis |

#### RAISE (Do More)
| Factor | Industry Level | Proposed Level | Evidence | Impact | Confidence |
|--------|---------------|----------------|----------|--------|------------|
| [Factor] | Underserved | Exceptional | [Customer pain points] | [Value created] | Validated/Inferred/Hypothesis |

#### CREATE (Start Doing)
| Factor | Status | Opportunity | Evidence | Impact | Confidence |
|--------|--------|-------------|----------|--------|------------|
| [New factor] | Doesn't exist | [What to create] | [Customer need] | [Value created] | Validated/Inferred/Hypothesis |

### To-Be Strategy Canvas

```
Factor          | Low ←───────────────────────→ High |
----------------|-------------------------------------|
[New mix of factors with differentiated value curve]
```

**Compelling Tagline:** [One sentence capturing the new value proposition]

### Three Characteristics Test

| Characteristic | Assessment | Evidence |
|----------------|------------|----------|
| **Focus** | [Pass/Fail] | [Does it concentrate on key factors?] |
| **Divergence** | [Pass/Fail] | [Does strategy canvas look different?] |
| **Compelling Tagline** | [Pass/Fail] | [Is it clear and resonant?] |

### Prioritized Recommendations

| # | Action | Type | Impact | Feasibility | Confidence | Priority |
|---|--------|------|--------|-------------|------------|----------|
| 1 | [Action] | Eliminate/Reduce/Raise/Create | High/Med/Low | High/Med/Low | Level | P0/P1/P2 |

### Implementation Roadmap

**Phase 1: Quick Wins (Eliminate & Reduce)**
- [Actions that free up resources]

**Phase 2: Differentiation (Raise)**
- [Actions that improve key value drivers]

**Phase 3: Innovation (Create)**
- [Actions that create new value curves]

### Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk] | High/Med/Low | High/Med/Low | [Strategy] |
```

## Example Output

```markdown
## Blue Ocean Strategy Analysis: TaskFlow (Project Management SaaS)

### Executive Summary

TaskFlow operates in a crowded project management space dominated by Asana, Monday.com, and Jira—classic red ocean with feature parity and price competition. The biggest blue ocean opportunity lies in serving the **"reluctant project managers"** (Tier 2 non-customers)—team leads who hate PM tools but are forced to use them. By **eliminating** enterprise complexity, **reducing** setup/configuration burden, **raising** the "just works" factor, and **creating** an AI autopilot that manages projects without human input, TaskFlow could create a new market of "invisible project management" that competitors would struggle to copy without cannibalizing their existing enterprise-focused customers.

### Current Competitive Landscape

#### Strategy Canvas (As-Is)

```
Factor              | Low ←─────────────────────────→ High |
--------------------|---------------------------------------|
Price               | TaskFlow: ●──────○ Asana ○ Monday □ Jira
Features            |        ●─────────────○────○────□
Customization       |    ●───────────────────○───○────□
Enterprise features |  ●───────────────────────○──○───□
Ease of setup       |         ●────○───□───────────○
Integrations        |      ●───────────○───○────□
Reporting           |   ●─────────────────○───○────□
Collaboration       |       ●────────○────○────□
Mobile experience   |            ●───○───○───□
AI/Automation       |  ●──○───○───□
```

**Legend:** ● = TaskFlow, ○ = Asana, ○ = Monday, □ = Jira

#### Convergence Points (Red Ocean Territory)

All competitors cluster around:
- **Heavy customization:** Templates, fields, workflows for every use case
- **Enterprise features:** Permissions, audit logs, SSO, compliance
- **Comprehensive reporting:** Dashboards, burndown charts, resource planning
- **Extensive integrations:** 100+ app connections as table stakes

This is where the fight for incremental differentiation happens—and where margins erode.

#### TaskFlow's Current Position

**Over-investing in (following competitors):**
- Building enterprise features despite SMB focus (SSO, advanced permissions)
- Creating custom templates for every industry vertical
- Expanding integration count (90+ integrations, most rarely used)

**Under-investing in (falling behind):**
- AI and automation (competitors adding AI writing, task suggestions)
- Mobile experience (web-first design, mobile is afterthought)
- Setup simplicity (still requires 30+ min onboarding)

### Non-Customer Analysis

#### Tier 1: Soon-to-be Non-Customers
**Who:** Small teams (5-15 people) using TaskFlow minimally—created account, set up one project, but defaulted back to spreadsheets or Slack for daily work.

**Why leaving/minimal engagement:**
- "Too much overhead for simple projects"
- "Have to remind team to update tasks—double work"
- "By the time I log it, I could have just done it"

**Evidence:** 62% of trial accounts create fewer than 10 tasks; 45% don't return after day 7.

**Opportunity:** Radically reduce friction. Make updating tasks effortless or automatic.

---

#### Tier 2: Refusing Non-Customers (PRIMARY OPPORTUNITY)
**Who:** "Reluctant project managers"—engineering leads, creative directors, startup founders who **must** coordinate work but **hate** project management tools.

**Why refusing:**
- "PM tools are where productivity goes to die"
- "I spend more time managing the tool than managing the project"
- "Built for project managers, not people who build things"
- "If I wanted paperwork, I'd go back to enterprise"

**Alternative solutions:**
- GitHub Issues + Slack (engineers)
- Notion pages + standup meetings (startups)
- Spreadsheets + email (small agencies)
- Whiteboard + memory (micro teams)

**Evidence:** Interviewed 23 startup CTOs—18 refused to use PM tools despite pain.

**Opportunity:** "Invisible project management"—tool that manages itself, requires zero maintenance.

---

#### Tier 3: Unexplored Non-Customers
**Who:** Solo professionals and micro-businesses (1-3 people) who never considered PM tools because "I'm just one person."

**Why never considered:**
- "Project management is for teams"
- "I just use my calendar and a to-do list"
- "Those tools cost money; I'm bootstrapped"

**Alternative solutions:** Apple Reminders, Notion personal, paper notebooks, calendar blocking.

**Evidence:** 15M+ sole proprietors in US alone; $0 spent on PM tools.

**Opportunity:** If PM was automatic and free, would they use it? Could AI make a solo professional's work visible and organized without effort?

### Four Actions Framework

#### ELIMINATE (Stop Doing)

| Factor | Industry Status | Evidence to Eliminate | Impact | Confidence |
|--------|-----------------|----------------------|--------|------------|
| **Enterprise permissions** | Table stakes for competitors | Only 8% of TaskFlow users use advanced permissions; SMB don't need complex role hierarchies | Save 2 engineers; reduce complexity | **Validated** |
| **Custom field types** | 15+ field types standard | Usage data shows 90% of users only use 3 types: text, date, dropdown | Simplify UI; reduce bugs | **Validated** |
| **Template marketplace** | Competitors have 500+ templates | 73% of users start with blank project; templates create decision paralysis | Reduce maintenance | **Inferred** |
| **Annual planning features** | Enterprise focus | No SMB uses roadmap planning; they plan 2-4 weeks ahead | Focus on short-cycle work | **Validated** |

**Savings:** ~$300K/year in engineering costs; faster development velocity.

---

#### REDUCE (Do Less)

| Factor | Industry Level | Proposed Level | Evidence | Impact | Confidence |
|--------|---------------|----------------|----------|--------|------------|
| **Integrations** | 100-300 apps | 15 critical integrations | Usage data: 12 integrations = 89% of actual usage; long tail is vanity | 80% less integration maintenance | **Validated** |
| **Customization options** | Extensive (colors, icons, layouts) | Smart defaults only | User interviews: "I don't want choices; I want it to work" | Faster setup; less confusion | **Inferred** |
| **Reporting granularity** | Detailed dashboards | One-page summary | SMB don't analyze data; they need "is project on track? yes/no" | Simpler product | **Inferred** |
| **Onboarding length** | 30-60 min setup | 5 min or less | 70% drop-off during onboarding correlates with setup length | Higher activation | **Validated** |

---

#### RAISE (Do More)

| Factor | Industry Level | Proposed Level | Evidence | Impact | Confidence |
|--------|---------------|----------------|----------|--------|------------|
| **Zero-config setup** | Requires configuration | Works immediately | #1 complaint in churn surveys: "too much setup" | 3x activation rate (hypothesis) | **Inferred** |
| **Automatic status updates** | Manual updates | Auto-detect from activity | "Updating tasks is busywork"—team leads hate it | Remove #1 friction | **Inferred** |
| **Mobile-first design** | Mobile is secondary | Mobile is primary | 67% of task updates happen outside dedicated work time | Fits real workflow | **Validated** |
| **Speed/performance** | Acceptable | Instant | Notion killed Evernote partly on speed; responsiveness is joy | Emotional differentiation | **Inferred** |

---

#### CREATE (Start Doing)

| Factor | Status | Opportunity | Evidence | Impact | Confidence |
|--------|--------|-------------|----------|--------|------------|
| **AI Autopilot** | Doesn't exist | AI that runs projects: creates tasks from conversations, updates status from signals, surfaces blockers before humans notice | "I want a tool that manages my project for me"—verbatim from 7/23 interviews | Category-creating feature | **Hypothesis** |
| **Conversation-first interface** | None | Natural language: "What's the status of Project X?" rather than clicking through UI | Teams live in Slack/Teams; PM tools are foreign context | Meets users where they are | **Hypothesis** |
| **Automatic team sync** | None | Tool that detects when sync is needed and schedules it, rather than requiring regular standups | Standup fatigue is real; teams want async-first | Eliminates overhead | **Hypothesis** |
| **One-number health score** | None | Single metric: "Project health: 7.2/10" with AI explanation, instead of 47 charts | Decision-makers want signal, not data | Executive buy-in | **Inferred** |

### To-Be Strategy Canvas

```
Factor                  | Low ←────────────────────────→ High |
------------------------|---------------------------------------|
Price                   |      ●────────────────── (competitors)
Enterprise features     | ●──────────────────────── (competitors)
Customization           |  ●─────────────────────── (competitors)
Number of integrations  |   ●────────────────────── (competitors)
Reporting granularity   |  ●─────────────────────── (competitors)
Setup time required     | ●─────────────────────── (competitors ↓)
Manual updates needed   | ●────────────────────── (competitors ↓)
Mobile experience       |            ●────── (competitors)
Speed/performance       |               ●─── (competitors)
AI automation           |                     ●── (competitors minimal)
Conversation interface  |                        ●  (competitors: none)
Auto status detection   |                        ●  (competitors: none)
```

**The Blue Ocean:** TaskFlow as "Invisible PM"—the project management tool for people who hate project management tools.

**Compelling Tagline:** "Projects manage themselves."

### Three Characteristics Test

| Characteristic | Assessment | Evidence |
|----------------|------------|----------|
| **Focus** | ✅ **Pass** | Concentrates on automation, simplicity, zero-maintenance—ignores enterprise, customization |
| **Divergence** | ✅ **Pass** | Strategy canvas dramatically different—low on industry standards, high on new factors |
| **Compelling Tagline** | ✅ **Pass** | "Projects manage themselves" is clear, memorable, differentiated |

### Prioritized Recommendations

| # | Action | Type | Impact | Feasibility | Confidence | Priority |
|---|--------|------|--------|-------------|------------|----------|
| 1 | Kill enterprise permissions module | Eliminate | Medium | High | Validated | **P0** |
| 2 | Reduce integrations to top 15 | Reduce | Medium | High | Validated | **P0** |
| 3 | Launch 5-min onboarding experience | Raise | High | Medium | Validated | **P0** |
| 4 | Build auto-status detection from Git/Slack | Create | High | Medium | Hypothesis | **P1** |
| 5 | Remove template marketplace | Eliminate | Low | High | Inferred | **P1** |
| 6 | Develop one-number health score | Create | Medium | Medium | Inferred | **P1** |
| 7 | Mobile-first redesign | Raise | High | Low | Validated | **P2** |
| 8 | Build AI Autopilot MVP | Create | High | Low | Hypothesis | **P2** |
| 9 | Create conversation-first interface | Create | High | Low | Hypothesis | **P3** |

### Implementation Roadmap

**Phase 1: Simplification (Q1) - Eliminate & Reduce**
- Remove enterprise permissions, complex fields, template marketplace
- Consolidate to 15 core integrations
- Reduce onboarding to under 5 minutes
- **Goal:** 50% reduction in product surface area; 20% faster development

**Phase 2: Core Differentiation (Q2) - Raise**
- Mobile-first redesign
- Performance optimization (sub-100ms interactions)
- Smart defaults that eliminate configuration
- **Goal:** Activation rate from 30% to 60%

**Phase 3: Blue Ocean Features (Q3-Q4) - Create**
- Auto-status detection (integrate with Git, Slack, Calendar)
- One-number project health score
- AI Autopilot beta (invite-only)
- Conversation-first interface prototype
- **Goal:** Create defensible differentiation; category leadership

### Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| **Existing customers churn** due to removed features | Medium | Medium | Grandfather enterprise features for current paying customers; sunset over 12 months |
| **AI autopilot doesn't work** well enough | Medium | High | Launch as beta/experimental; set expectations; iterate rapidly |
| **Competitors copy quickly** | Low | Medium | Simplification is hard to copy for bloated products (innovator's dilemma protects us) |
| **"Invisible PM" positioning confuses market** | Medium | Medium | Focus messaging on "project management for people who hate PM"—negative positioning is clearer |
| **Engineering capacity** for Create features | High | Medium | Offset with savings from Eliminate/Reduce; hire 2 AI/ML engineers |

### Validation Next Steps

Before committing to full implementation:

1. **Customer interviews (2 weeks):** Test "invisible PM" positioning with 20 Tier 2 non-customers
2. **Prototype test (4 weeks):** Build auto-status detection proof-of-concept; measure accuracy
3. **Pricing experiment (2 weeks):** Test willingness to pay for AI autopilot feature
4. **Competitive analysis (1 week):** Deep dive on competitor AI roadmaps; assess window of opportunity
```

## Customization Guide

- **For B2B Products:** Focus heavily on Tier 2 (refusing non-customers)—enterprises often have non-adopters who are forced to use inferior alternatives
- **For B2C Products:** Tier 3 (unexplored) often has the biggest opportunities—look at adjacent consumer behaviors
- **For Hardware Products:** Eliminate is often about component cost; Create is often about software/service layers
- **For Service Businesses:** Eliminate manual/high-touch elements; Create self-service or AI-assisted options

## Techniques Used

- **ST-01 (Clear Objective Statement):** Explicit goal of identifying uncontested market space through value innovation
- **ST-02 (Structured Sequential Instructions):** Systematic progression from landscape analysis through four actions to implementation
- **DS-01 (Framework Application):** Direct application of Blue Ocean Strategy methodology (Strategy Canvas, Four Actions, Three Tiers)
- **RT-02 (Multi-Dimensional Analysis):** Evaluation across elimination, reduction, raising, and creation dimensions
- **QA-02 (Adversarial Thinking):** False-positive prevention challenges assumptions about blue ocean validity
- **DS-06 (Prioritization Guidance):** Recommendations prioritized by impact, feasibility, and confidence

## Related Prompts

- [Competitive Positioning Map](competitive_positioning_map.md) - Visual competitive analysis foundation for Blue Ocean
- [Value Proposition Canvas Analysis](value_proposition_canvas_analysis.md) - Deep dive on customer value alignment
- [Porter's Five Forces Analysis](porters_five_forces_analysis.md) - Red ocean industry structure analysis
- [Ansoff Matrix Analysis](ansoff_matrix_analysis.md) - Growth strategy alternatives to Blue Ocean
