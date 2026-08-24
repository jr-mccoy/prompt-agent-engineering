---
title: "Solo Developer Roadmap Planner"
category: startup/business-operations
description: "Create a realistic, capacity-aware product roadmap for a solo app developer — covering honest capacity assessment, user feedback integration weighted by revenue impact, RICE-adapted prioritization, technical debt allocation, and communicating timelines to users"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-01
  - CM-02
  - DS-06
difficulty: intermediate
tags:
  - solo-developer
  - startup
  - roadmap
  - prioritization
  - android
  - product-planning
  - capacity
updated: "2026-02-11"
---

# Solo Developer Roadmap Planner

**Objective:** Create a realistic product roadmap for a solo developer — starting from an honest assessment of your actual capacity (you're one person with 20-25 productive coding hours per week at best), integrating user feedback weighted by revenue impact, prioritizing features using an adapted RICE framework, allocating time for technical debt (the 20% rule), and communicating timeline expectations to users without over-promising — producing a quarterly roadmap, capacity plan, and user-facing communication template.

**When to Use:** Use this prompt when you have more ideas and feature requests than time, when users are asking "when will feature X be ready?" and you don't have a good answer, when you realize you've been building features randomly instead of strategically, when you feel overwhelmed by all the things you "should" be working on, or when you need to plan the next quarter and want to do it with discipline rather than wishful thinking.

**Important context:** The #1 mistake solo developers make with roadmaps is planning as if they have 40 productive coding hours per week. They don't. Between support, marketing, business operations, context switching, and the reality of human energy levels, most solo developers get 20-25 hours of actual productive development per week — even when working "full time." Part-timers get 8-15 hours. A roadmap built on fantasy capacity guarantees missed deadlines, user disappointment, and developer burnout. This guide starts with truth and builds from there.

---

## Context Gathering

Before building your roadmap, get honest about your situation:

1. **Capacity Reality Check:**
   - "How many total hours per week do you work on your app business?"
   - "Of those hours, how many are actual coding/development (not support, marketing, admin)?"
   - "Are you full-time on the app or do you have a day job?"
   - "Do you have regular commitments that reduce availability (family, other projects, health)?"

2. **Current State:**
   - "What is your app's current feature set (list the major features)?"
   - "What are you currently building or halfway through?"
   - "What is your backlog size (number of features/improvements you're considering)?"
   - "When was your last release, and what was in it?"

3. **User Input:**
   - "How many feature requests do you have from users?"
   - "Which requests come from paying customers vs. free users?"
   - "What do your app store reviews say users want most?"
   - "Have you done any user surveys or interviews recently?"

4. **Technical Context:**
   - "How much technical debt do you currently have?"
   - "Are there known bugs that affect users but you haven't fixed?"
   - "Are there infrastructure upgrades you've been deferring?"
   - "What's the state of your test coverage?"

---

## Instructions

### CRITICAL: Verification Requirements

1. **Capacity estimates must be based on actual tracked time, not aspirational goals** — If you haven't tracked your time for at least 2 weeks, your estimate is probably 30-50% too high. Track before planning.
2. **Feature time estimates must include the 2-3x multiplier** — Developers consistently underestimate. If you think something takes 8 hours, budget 16-24 hours. This is not pessimism; it's realism.
3. **Roadmap must include technical debt allocation** — Skipping maintenance to ship features faster is borrowing from your future self at high interest. Budget 20% of development time for tech debt.
4. **User-facing timelines must use ranges, not specific dates** — "Q2 2026" not "April 15, 2026." Specific dates create hard expectations you probably can't meet.
5. **Prioritization must be driven by revenue impact, not personal interest** — Building the feature YOU think is cool instead of the feature users will PAY for is a luxury solo developers can't afford.
6. **Acceptable null result:** If capacity analysis reveals the developer is already over-committed, the right answer may be "cut scope" or "delay the roadmap" rather than cramming more in.

### False-Positive Prevention

- Do NOT plan more than 60-70% of your available capacity — leave room for bugs, support spikes, unexpected issues, and rest
- Do NOT create a 12-month detailed roadmap — for a solo developer, anything beyond one quarter is speculation. Plan in detail for 1 quarter, loosely for 2 quarters, and directionally for beyond.
- Do NOT treat all feature requests as equal — paying customers and churn-risk signals outweigh everything else
- Do NOT skip the capacity assessment because "I already know how much time I have" — you probably don't, and being wrong here invalidates the entire roadmap
- Do NOT promise features publicly before you've estimated them properly — public commitments feel good in the moment and terrible when you miss them
- Do NOT ignore technical debt in the roadmap — it doesn't go away; it compounds
- DO accept that you can't build everything users ask for — and that's fine
- DO build in buffer time for every quarter (at least 20% unallocated)
- DO review and adjust the roadmap monthly — it's a living document, not a contract
- DO distinguish between "we're building this" and "we're considering this" in user communication

---

### Phase 1: Capacity Assessment

#### 1.1 The Honest Hours Exercise

Track your actual time for 2 weeks before building a roadmap. Use a simple spreadsheet or time tracker:

```markdown
## Time Tracking Worksheet (1 Week)

| Day | Development | Support | Marketing | Business Ops | Learning | Other | Total |
|-----|------------|---------|-----------|-------------|----------|-------|-------|
| Mon | ____h | ____h | ____h | ____h | ____h | ____h | ____h |
| Tue | ____h | ____h | ____h | ____h | ____h | ____h | ____h |
| Wed | ____h | ____h | ____h | ____h | ____h | ____h | ____h |
| Thu | ____h | ____h | ____h | ____h | ____h | ____h | ____h |
| Fri | ____h | ____h | ____h | ____h | ____h | ____h | ____h |
| Sat | ____h | ____h | ____h | ____h | ____h | ____h | ____h |
| Sun | ____h | ____h | ____h | ____h | ____h | ____h | ____h |
| **TOTAL** | **____h** | **____h** | **____h** | **____h** | **____h** | **____h** | **____h** |
```

**Repeat for week 2. Average the results.**

#### 1.2 The Capacity Calculator

```markdown
## Weekly Development Capacity

### Raw Development Hours
Average weekly development hours (from tracking): ____h

### Adjustments
- Subtract 20% for context switching and overhead: -____h
  (Every time you switch tasks, you lose 10-15 minutes getting back in flow)
- Subtract 20% for technical debt allocation: -____h
  (This is non-negotiable if you want a sustainable codebase)
- Subtract buffer for support spikes and bugs: -____h
  (Minimum 10% — more if your app is early-stage)

### Available Feature Development Capacity
= ____h per week

### Quarterly Capacity
= ____h/week × 12 weeks = ____h per quarter

### Capacity Reality Check
| Scenario | Weekly Dev Hours | What You Can Ship Per Quarter |
|----------|-----------------|------------------------------|
| Full-time, focused | 20-25h | 2-3 medium features or 1 large feature |
| Full-time, lots of support | 15-20h | 1-2 medium features |
| Part-time (evenings + weekend) | 8-15h | 1 medium feature or 2-3 small features |
| Part-time (evenings only) | 4-8h | 1 small feature or bug fixes + improvements |
```

#### 1.3 Feature Sizing Guide

Assign T-shirt sizes to features based on development hours (with the 2-3x multiplier already included):

| Size | Hours (with buffer) | Calendar Time (solo, at 20h/week) | Examples |
|------|-------------------|----------------------------------|---------|
| **XS** | 1-4 hours | Half a day | Bug fix, copy change, small UI tweak |
| **S** | 4-16 hours | 1-3 days | New screen, simple feature, API integration |
| **M** | 16-40 hours | 1-2 weeks | Significant feature, payment integration, sync |
| **L** | 40-80 hours | 2-4 weeks | Major feature, new module, redesign of a section |
| **XL** | 80-160 hours | 4-8 weeks | Core feature overhaul, new platform, major refactor |
| **XXL** | 160+ hours | 8+ weeks | Rewrite, new app version, entirely new feature set |

**Rule of thumb:** If a feature is XL or larger, break it into smaller phases that can ship independently. Solo developers should almost never have a single feature in progress for more than 4 weeks — the risk of scope creep, lost motivation, and zero shipping momentum is too high.

---

### Phase 2: Feedback Collection and Weighting

#### 2.1 Feedback Sources

Collect user input from every available channel:

| Source | How to Collect | Signal Strength |
|--------|---------------|----------------|
| **App store reviews** | Download weekly from Play Console | Medium — public and visible, but often vague |
| **Support emails** | Tag by feature request in your support tool | High — users took time to write personally |
| **In-app feedback** | Optional feedback form or survey | High — contextual (you know what they were doing) |
| **Social media** | Monitor mentions and DMs | Medium — can be noisy |
| **User surveys** | Send quarterly to active users | Very High — structured, targeted data |
| **Behavioral data** | Analytics on feature usage | Very High — what users DO, not what they SAY |
| **Competitor reviews** | Read competitor app reviews | Medium — shows unmet needs in the market |
| **Churn surveys** | Ask why when users cancel subscription | Very High — directly tied to revenue |

#### 2.2 Revenue-Weighted Feedback

Not all feedback is equal. Weight it by revenue impact:

| Source | Weight Multiplier | Reasoning |
|--------|------------------|-----------|
| Paying subscriber who threatens to cancel | 5x | Direct revenue risk |
| Paying subscriber request | 3x | Paying customer retention |
| Churn survey response | 4x | Understanding revenue loss |
| Free user with high engagement | 2x | Likely future subscriber |
| Free user, casual request | 1x | Base weight |
| Random internet comment | 0.5x | No verified connection to your product |
| Your own idea (not user-requested) | 0.5x | Validate before investing — you're biased |

**How to apply:**
```
Weighted request count = (number of requests) × (weight multiplier)

Example:
- 3 paying users ask for dark mode (3 × 3x = 9)
- 12 free users ask for dark mode (12 × 1x = 12)
- 1 paying user threatens to cancel without offline mode (1 × 5x = 5)

Dark mode weighted score: 21
Offline mode weighted score: 5

BUT — offline mode has direct revenue risk. Both deserve consideration.
```

#### 2.3 Feedback Consolidation Template

Maintain a running tally updated monthly:

```markdown
## Feature Request Consolidation — [Month Year]

| Feature | Total Requests | Weighted Score | Top Source | Revenue Signal | Trend |
|---------|---------------|---------------|-----------|---------------|-------|
| [Feature A] | [N] | [Weighted] | [Where most came from] | [Direct/Indirect/None] | [Growing/Stable/Declining] |
| [Feature B] | [N] | [Weighted] | [Where most came from] | [Direct/Indirect/None] | [Growing/Stable/Declining] |
```

---

### Phase 3: Prioritization

#### 3.1 RICE Scoring (Solo Developer Adapted)

Score each feature candidate. This version of RICE is adapted for one-person operations where your time is the scarcest resource:

```markdown
## Feature Prioritization: [Quarter]

| Feature | Reach (1-5) | Impact (1-5) | Confidence (1-5) | Effort (T-shirt) | Effort Score (1-5, inverted) | RICE Score | Revenue Signal Bonus | Final Score |
|---------|------------|-------------|------------------|------------------|------------------------------|-----------|---------------------|-------------|
| [Feature A] | __ | __ | __ | [S/M/L] | __ | __ | +__ | __ |
| [Feature B] | __ | __ | __ | [S/M/L] | __ | __ | +__ | __ |
```

**Scoring guide:**

**Reach:** How many active users will this affect in the next quarter?
- 5 = All or nearly all users
- 4 = Most users (50%+)
- 3 = Many users (20-50%)
- 2 = Some users (5-20%)
- 1 = Few users (< 5%)

**Impact:** How significantly will this affect those users?
- 5 = Massive — unlocks a new use case, dramatically improves core experience
- 4 = High — significantly improves a frequent workflow
- 3 = Medium — noticeable improvement to some aspect
- 2 = Low — nice-to-have improvement
- 1 = Minimal — cosmetic or marginal

**Confidence:** How sure are you about Reach and Impact scores?
- 5 = Data-backed (analytics, surveys, 10+ user requests)
- 4 = Strong signals (5+ requests, competitive data)
- 3 = Moderate (a few requests, reasonable hypothesis)
- 2 = Speculative (sounds right but limited evidence)
- 1 = Pure guess

**Effort Score (inverted — lower effort = higher score):**
- 5 = XS (< 4 hours)
- 4 = S (4-16 hours)
- 3 = M (16-40 hours)
- 2 = L (40-80 hours)
- 1 = XL+ (80+ hours)

**RICE Score** = Reach x Impact x Confidence x Effort Score

**Revenue Signal Bonus:**
- +5 if paying customers threatened to churn without it
- +3 if paying customers specifically requested it
- +2 if non-paying users indicate they'd upgrade for it
- +0 for all other features

#### 3.2 Prioritization Rules

After scoring, apply these tiebreaker rules:

1. **Revenue-protecting features always come first** — If paying customers are at risk of churning, that's a P1 regardless of RICE score.
2. **Small wins before big bets** — If two features have similar Final Scores but different sizes, ship the smaller one first. Momentum matters.
3. **Bugs before features** — Known bugs that affect users should be fixed before new features are built. Users forgive missing features; they don't forgive broken ones.
4. **Sequential dependencies** — If Feature B depends on Feature A, schedule A first even if B has a higher score.
5. **One "passion project" per quarter** — It's your app. Allow yourself one feature that YOU want to build even if the RICE score doesn't justify it. Motivation matters.

---

### Phase 4: Roadmap Construction

#### 4.1 Quarterly Roadmap Template

```markdown
## Product Roadmap: Q[N] [Year]

### Capacity Budget
- Available feature development hours: ____h
- Technical debt allocation (20%): ____h
- Bug fix allocation: ____h
- Buffer (unallocated, 15-20%): ____h
- **Total quarter hours: ____h**

### Committed (Will Ship This Quarter)
These features are planned, estimated, and committed. Barring emergencies, they will ship.

| Priority | Feature | Size | Hours | Target Release | Status |
|----------|---------|------|-------|---------------|--------|
| 1 | [Feature] | [S/M/L] | [N]h | [Month or early/mid/late Q] | [Not started / In progress / Done] |
| 2 | [Feature] | [S/M/L] | [N]h | [Month] | [Status] |
| 3 | [Feature] | [S/M/L] | [N]h | [Month] | [Status] |

**Total committed hours: ____h (should be ≤ 70% of available hours)**

### Stretch Goals (May Ship If Time Allows)
These features are estimated and designed but not committed. They ship if the committed items finish early.

| Feature | Size | Hours | Notes |
|---------|------|-------|-------|
| [Feature] | [S/M] | [N]h | [Context] |
| [Feature] | [S/M] | [N]h | [Context] |

### Technical Debt Items (20% Allocation)
| Item | Hours | Impact |
|------|-------|--------|
| [Debt item] | [N]h | [What it improves] |
| [Debt item] | [N]h | [What it improves] |

### Explicitly NOT Doing This Quarter
| Feature | Why Not | When to Revisit |
|---------|---------|-----------------|
| [Feature] | [Reason: low RICE, too large, not now] | [Next quarter / Q3 / Backlog] |
| [Feature] | [Reason] | [When] |
```

#### 4.2 Monthly Roadmap Review

On the first Monday of each month, review and adjust:

```markdown
## Monthly Roadmap Check-In: [Month Year]

### Progress
- Committed features: [N] of [N] shipped
- Hours used this month: ____h of ____h planned
- On track for quarter? [Yes / At risk / Behind]

### Adjustments
- Features moved up: [Any features promoted from stretch to committed]
- Features pushed back: [Any committed features moved to next quarter]
- New additions: [Anything added based on new data]
- Removed: [Anything dropped from the roadmap entirely]

### Capacity Reality Check
- Planned weekly hours: ____h
- Actual average weekly hours this month: ____h
- Variance: ____h ([over/under] plan)
- Adjustment for remaining quarter: [If consistently under, reduce scope]

### Key Decisions
- [Decision 1 and reasoning]
- [Decision 2 and reasoning]
```

#### 4.3 The Two-Quarter Horizon

Beyond the current quarter, keep planning loose:

| Time Horizon | Planning Detail | Commitment Level |
|-------------|----------------|-----------------|
| **This month** | Specific tasks, in-progress work | Committed |
| **This quarter** | Named features with sizes | Mostly committed |
| **Next quarter** | Themes and areas of focus | Planned, not committed |
| **6+ months** | Directional goals only | Aspirational |

**Example:**
```
Q1 2026 (Current): Ship offline mode (M), redesign settings (S), fix sync bugs (XS x 3)
Q2 2026 (Next): Focus on premium features and monetization improvements
2026 H2: Explore tablet support and new market expansion
```

Don't plan further than this. The app, market, and your priorities will change.

---

### Phase 5: Communicating the Roadmap

#### 5.1 What to Share Publicly

| Share | Don't Share |
|-------|------------|
| General themes and focus areas | Specific dates or deadlines |
| Features you've already started building | Features you're only considering |
| Known issues and your commitment to fixing them | Internal prioritization scores |
| Your development philosophy | Revenue numbers or business metrics |
| How to give feedback | Reasons you rejected a specific request |

#### 5.2 User-Facing Roadmap Template

```markdown
## [App Name] — What's Coming

Last updated: [Date]

### Currently Building 🔨
These features are in active development and coming in the next update:
- **[Feature name]** — [1-sentence description of what it does for the user]
- **[Bug fix]** — [What was broken and that it's being fixed]

### Coming Soon 📋
These are planned for the next 1-3 months:
- **[Feature name]** — [1-sentence description]
- **[Feature name]** — [1-sentence description]

### Considering 💭
These are on my radar based on your feedback. No timeline yet:
- **[Feature name]** — Requested by many of you!
- **[Feature name]** — Exploring feasibility

### Recently Shipped ✅
- **[Feature]** — [Version X.Y] — [Date]
- **[Feature]** — [Version X.Y] — [Date]

### How to Suggest Features
[Link to feedback form or email address]

---
*I'm a solo developer, so I work on one major feature at a time. Your patience
and feedback keep this app moving forward. Thank you!*
```

#### 5.3 Responding to "When Will Feature X Be Ready?"

**Template response (honest and professional):**

```
Hi [Name],

Thanks for asking about [feature]! It's definitely on my list — [several users
have requested it / I've been wanting to add it].

I'm currently focused on [what you're building now], which I expect to ship
in [timeframe]. After that, [feature] is [high on my priority list / something
I'll evaluate for the next planning cycle].

I don't commit to specific dates because I'm a solo developer and timelines
can shift, but I'll share updates on my [changelog / blog / in-app announcements]
when there's news.

If you want to make sure your voice is counted, leaving a review on the Play
Store mentioning this feature helps me prioritize!

[Your name]
```

**What this response does well:**
- Acknowledges the request
- Shows you have a process (not random)
- Sets realistic expectations without committing to a date
- Directs them to a public action (review) that helps you

#### 5.4 Managing Expectations After Missing a Target

It happens. You told users something was "coming soon" and it's been 3 months. Here's how to handle it:

```
Hi everyone,

Quick update on [feature]: it's taking longer than I expected. [Brief honest
reason — "the technical complexity was greater than I anticipated" or "I
prioritized fixing [critical bug] first because it was affecting your experience"].

I'm still committed to delivering this. My current estimate is [timeframe].
I'll share progress updates as I go.

I appreciate your patience. Building a quality feature takes time, and I'd
rather get it right than rush something that doesn't work well.

[Your name]
```

---

### Phase 6: Roadmap Anti-Patterns

#### 6.1 Common Mistakes

| Anti-Pattern | Symptom | Fix |
|-------------|---------|-----|
| **The Fantasy Roadmap** | Plans 40h/week of coding, ships 15h/week | Start from tracked capacity, not wishes |
| **The Buffet Roadmap** | 15 features planned for one quarter | Cut to 3-5. Seriously. Less is more. |
| **The Democracy Roadmap** | Every user request becomes a planned feature | Prioritize by revenue impact, not volume |
| **The Shiny Object Roadmap** | Changes direction every week based on latest idea | Commit to quarterly focus areas, resist mid-quarter pivots |
| **The Secret Roadmap** | Users have no idea what's coming or why | Share a lightweight public roadmap |
| **The No-Debt Roadmap** | 100% features, 0% maintenance | Allocate 20% for tech debt or face future crises |
| **The Scope Creep Roadmap** | Features keep growing mid-development | Define MVP scope before starting, ship that, iterate later |
| **The Commitment-Phobic Roadmap** | Nothing is ever committed, everything is "exploring" | Commit to at least 1-2 features per quarter and ship them |

#### 6.2 The Mid-Quarter Pivot Test

When you're tempted to change the roadmap mid-quarter (and you will be), ask:

```markdown
## Mid-Quarter Pivot Test

New idea / opportunity: [What you want to switch to]

1. Is this more urgent than what I'm currently building?
   [ ] Yes — it's blocking users or losing revenue NOW
   [ ] No — it's exciting but not time-sensitive

2. If I pivot, what committed feature gets delayed?
   Feature delayed: [Name]
   Impact of delay: [Who is affected, how]

3. Will this new thing still seem important in 2 weeks?
   [ ] Probably yes
   [ ] Honestly, maybe not

4. Can I do this AFTER the current committed feature ships?
   [ ] Yes — it can wait
   [ ] No — there's a genuine time constraint

Decision:
- If #1 = Yes AND #4 = No → Pivot is justified
- Otherwise → Stay the course, add to next quarter's backlog
```

---

## Expected Output

```markdown
# Product Roadmap: [App Name]
## Q[N] [Year]

### Capacity
- Weekly development hours: [N]h
- Quarterly capacity: [N]h
- Feature development (70%): [N]h
- Technical debt (20%): [N]h
- Buffer (10%): [N]h

### Prioritized Feature List

| Rank | Feature | RICE + Revenue Score | Size | Hours | Status |
|------|---------|---------------------|------|-------|--------|
| 1 | [Feature] | [Score] | [Size] | [N]h | [Status] |
| 2 | [Feature] | [Score] | [Size] | [N]h | [Status] |
| 3 | [Feature] | [Score] | [Size] | [N]h | [Status] |

### Technical Debt Plan
| Item | Hours | Payoff |
|------|-------|--------|
| [Item] | [N]h | [What improves] |

### Stretch Goals
- [Feature] if capacity allows
- [Feature] if capacity allows

### Not This Quarter
- [Feature] — revisit [when]

### Next Quarter Direction
- Theme: [Area of focus]
- Candidate features: [Rough list]

### User-Facing Roadmap
- Published at: [URL or location]
- Last updated: [Date]
- Update frequency: [Monthly / after each release]

### Review Schedule
- Monthly check-in: [1st Monday of each month]
- Quarterly planning: [Last week of quarter]
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) — Focused on realistic, capacity-aware roadmap planning for one person
- **ST-02** (Structured Sequential Instructions) — Phased approach from capacity assessment through communication
- **RT-02** (Multi-Dimensional Analysis) — Evaluating features across reach, impact, confidence, effort, and revenue dimensions
- **CM-01** (Explicit Context Framing) — Solo developer constraints: limited hours, no team, all responsibilities fall to one person
- **CM-02** (Constraint Specification) — Capacity limits, 20% tech debt rule, buffer requirements
- **DS-06** (Prioritization Guidance) — RICE scoring adapted for solo developers, revenue-weighted feedback

---

## Related Prompts

- `solo_dev_decision_framework.md` — Build/buy/skip analysis for features on the roadmap
- `solo_dev_metrics_dashboard.md` — Data inputs for roadmap prioritization (retention, conversion, usage)
- `solo_dev_weekly_operating_rhythm.md` — Executing the roadmap within your weekly schedule
- `solo_dev_support_system.md` — User feedback as input to roadmap priorities
- `solo_dev_contractor_management.md` — Outsourcing features on the roadmap to increase capacity
- `solo_dev_financial_planning.md` — Revenue milestones that guide roadmap focus areas

---

## Customization Guide

- **For pre-launch developers:** Your roadmap is simple — ship the MVP. List the features needed for launch, size them, and work through them in order. Your "user feedback" is beta tester input. Don't build a complex prioritization system before you have real users.
- **For part-time developers (< 15h/week):** Your quarterly capacity is 1-2 medium features at most. Accept this. Focus on one thing at a time and ship it completely before starting the next. A roadmap with one committed feature shipped well beats a roadmap with five half-finished features.
- **For developers with high support volume:** Your effective development capacity is lower than you think. Track support time separately and subtract it from capacity BEFORE planning features. If support is eating more than 25% of your time, invest in self-service content before building new features — it frees future capacity.
- **For developers with rapid growth:** Your priorities may shift faster than a quarterly cadence allows. Consider monthly roadmap reviews and shorter commitment windows (monthly instead of quarterly). But still commit — rapid growth without focus leads to chaotic development.
- **For developers considering hiring:** If your feature backlog consistently exceeds your capacity by 3-4x and revenue supports it, a contractor or part-time hire can increase throughput. But adding people adds management overhead. See `solo_dev_contractor_management.md` for how to do this well.
- **For developers who hate planning:** Start with the minimum: write down your top 3 priorities for the next month. That's your roadmap. Review in 30 days. It takes 15 minutes and is infinitely better than no plan. Add structure gradually as the habit forms.
