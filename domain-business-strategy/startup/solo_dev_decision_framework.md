---
title: "Solo Developer Decision Framework"
category: startup/business-operations
description: "Decision framework for a solo app developer — build vs buy vs skip analysis, feature request evaluation, technical investment ROI, avoiding the perfectionism trap, reversible vs irreversible decisions, and the 'default to action' principle — with decision matrices, scoring frameworks, and ROI calculators"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-03
  - CM-01
  - DS-06
difficulty: intermediate
tags:
  - solo-developer
  - startup
  - decision-making
  - prioritization
  - android
  - strategy
  - build-vs-buy
updated: "2026-02-11"
---

# Solo Developer Decision Framework

**Objective:** Build a practical decision-making system for a solo app developer — covering build vs. buy vs. skip analysis, feature request evaluation using revenue and churn impact, technical investment ROI, strategies for avoiding the perfectionism trap, the distinction between reversible and irreversible decisions, and the "default to action" principle — producing a repeatable decision process that replaces agonizing with action.

**When to Use:** Use this prompt when you're stuck deciding what to build next, when your feature request list is growing faster than your ability to ship, when you're debating whether to build a feature yourself or use a third-party service, when you've been "thinking about" a decision for more than a week without acting, or when you catch yourself gold-plating a feature instead of shipping it. Solo developers make dozens of business and technical decisions every week — the quality and speed of those decisions determine whether the business thrives or stalls.

**Important context:** The biggest productivity killer for solo developers is not lack of time — it's decision paralysis. When you're the only person making every decision (technical architecture, feature priority, pricing, marketing, support), the cognitive load is enormous. Most decisions don't need extensive analysis. They need a quick framework, a clear answer, and forward motion. This guide gives you that framework. The goal is not perfect decisions. The goal is good-enough decisions made fast enough to maintain momentum.

---

## Context Gathering

Before applying the decision framework, understand the context:

1. **Decision Inventory:**
   - "What decisions are you currently stuck on?"
   - "How long have you been deliberating on these decisions?"
   - "What is the cost of NOT deciding (delay, lost revenue, technical debt)?"
   - "Have you made similar decisions before? What happened?"

2. **Business Stage:**
   - "What stage is your app (pre-launch, early traction, growing, established)?"
   - "What is your current monthly revenue?"
   - "How many active users do you have?"
   - "What are your top 3 business goals for the next 3 months?"

3. **Resource Constraints:**
   - "How many hours per week do you have for development?"
   - "What is your monthly budget for tools and services?"
   - "What are your strongest technical skills?"
   - "What skills would you need to learn for the options you're considering?"

4. **Decision Patterns:**
   - "Do you tend to over-analyze decisions or act impulsively?"
   - "Have you ever regretted NOT acting fast enough?"
   - "Do you tend to build things yourself even when a good solution exists?"
   - "Do you have a hard time killing features or projects that aren't working?"

---

## Instructions

### CRITICAL: Verification Requirements

1. **Decision frameworks must be applied to the ACTUAL decision, not hypotheticals** — Abstract frameworks are useless without concrete application. Always map the framework to the developer's specific situation.
2. **ROI calculations must use realistic inputs** — Don't assume a feature will "probably increase revenue 30%." Use conservative estimates based on available data or comparable benchmarks.
3. **Build vs. buy analysis must include total cost of ownership, not just initial cost** — Building a feature yourself costs development time AND ongoing maintenance time. Buying a service costs money AND creates a dependency.
4. **Time estimates must account for the "2x-3x reality"** — Everything takes 2-3x longer than developers estimate. Build that multiplier into any time-based ROI calculation.
5. **The framework must produce a clear recommendation** — "It depends" is not an answer. The framework should lead to "Do X because Y."
6. **Acceptable null result:** If the decision is genuinely irreversible with high stakes (e.g., choosing a database technology for a large dataset, pricing model for a launched product with 10K+ subscribers), slower deliberation is appropriate. Not every decision should be fast.

### False-Positive Prevention

- Do NOT recommend "just ship it" for decisions with significant irreversible consequences (e.g., data model changes, pricing structure, legal agreements)
- Do NOT treat all feature requests equally — a request from a paying customer at risk of churning is fundamentally different from a random suggestion on Reddit
- Do NOT apply ROI calculations to decisions where the data doesn't exist — for pre-launch apps, intuition and user research beat spreadsheets
- Do NOT encourage "building everything yourself" as a default — solo developers who refuse to buy services waste their most scarce resource (time)
- Do NOT dismiss technical investment (refactoring, testing, CI/CD) as "not adding value" — these investments reduce future decision costs and shipping friction
- Do NOT confuse "default to action" with "act recklessly" — the principle applies to reversible decisions, not all decisions
- DO acknowledge that some indecision is caused by fear of failure, not lack of information
- DO differentiate between decisions that need data and decisions that need courage
- DO recommend time-boxing decision-making (set a deadline, then decide)

---

### Phase 1: Decision Classification

#### 1.1 The Two Types of Decisions

Jeff Bezos popularized the distinction between Type 1 and Type 2 decisions, and it's incredibly useful for solo developers:

| Type | Characteristics | Approach | Time to Decide |
|------|----------------|----------|---------------|
| **Type 1 (Irreversible)** | Can't easily undo. High cost of reversal. Long-term consequences. | Deliberate carefully. Gather data. Sleep on it. | Days to weeks |
| **Type 2 (Reversible)** | Easy to undo or change. Low cost of reversal. Limited blast radius. | Decide quickly. Default to action. Course-correct later. | Minutes to hours |

**The solo developer mistake:** Treating every decision like a Type 1 decision. Most decisions in an early-stage app business are Type 2 — easily reversible and not worth agonizing over.

#### 1.2 Decision Classification Exercise

For any decision you're facing, answer these three questions:

```markdown
## Decision Classification: [Describe the decision]

1. If this turns out to be wrong, how hard is it to undo?
   [ ] Easy — I can revert, change, or pivot with minimal cost
   [ ] Medium — Some work to undo, but not catastrophic
   [ ] Hard — Significant cost or damage if I reverse course

2. What's the blast radius if it goes wrong?
   [ ] Just me — affects my workflow, not users
   [ ] Small — affects some users mildly
   [ ] Large — affects many users significantly or damages revenue

3. How much information will I realistically gain by waiting?
   [ ] None — I'm just avoiding the decision
   [ ] Some — a specific data point is coming (e.g., next month's metrics)
   [ ] A lot — I need to research or test something first

Scoring:
- Mostly "Easy/Just me/None" → Type 2. Decide in 10 minutes.
- Mostly "Hard/Large/A lot" → Type 1. Take your time.
- Mixed → Default to Type 2 unless the "Hard/Large" factor is dominant.
```

#### 1.3 Common Solo Developer Decisions by Type

**Type 2 (Decide Quickly):**

| Decision | Why It's Reversible |
|----------|-------------------|
| Which analytics tool to use | Can switch later; data is the asset, not the tool |
| Color scheme / UI tweaks | Can change in the next release |
| Which social media platform to focus on | Can shift in a week |
| Blog post topic | Can write a different one next week |
| Price of first release | Can adjust based on data |
| Feature flag on/off | Literally one line of code to revert |
| Which CI/CD service to use | Can migrate; most are similar |

**Type 1 (Deliberate Carefully):**

| Decision | Why It's Hard to Reverse |
|----------|------------------------|
| Core database technology | Data migration is expensive and risky |
| Programming language for core app | Rewrite is massive effort |
| Business entity type (for tax purposes) | Legal and tax implications |
| Pricing model (subscription vs. one-time) | User expectations are set once launched |
| Privacy / data collection scope | Reducing data collection later is easy, but users don't forget over-collection |
| Giving equity to a co-founder | Legal entanglement |

---

### Phase 2: Build vs. Buy vs. Skip

#### 2.1 The Three Options

For every feature, capability, or tool you're considering, there are actually three options — and the third is the most underrated:

| Option | What It Means | When It Wins |
|--------|--------------|-------------|
| **Build** | Write the code yourself | Core differentiator, unique to your app, no good existing solution |
| **Buy** | Use a third-party service, library, or contractor | Commodity functionality, someone else does it better, your time is better spent elsewhere |
| **Skip** | Don't do it at all (at least not now) | Doesn't move the needle on revenue or retention, nice-to-have, low user demand |

**The secret:** "Skip" is the right answer more often than most solo developers realize. Every feature you build or buy is a feature you maintain. Every feature you skip is time and money preserved for what actually matters.

#### 2.2 Build vs. Buy vs. Skip Decision Matrix

Score each factor on a 1-5 scale:

```markdown
## Build/Buy/Skip Analysis: [Feature or Capability]

### Scoring (1 = low, 5 = high)

| Factor | Build | Buy | Skip |
|--------|-------|-----|------|
| **Revenue impact** | How much will building this increase revenue? | Same benefit from buying? | What's lost by not doing it? |
| Score: | __/5 | __/5 | __/5 |
| **Time cost** | Hours to build + maintain | Hours to integrate + cost | 0 hours |
| Score (inverse — less time = higher): | __/5 | __/5 | 5/5 |
| **Quality** | Can you build it well? | Is the third-party good? | N/A |
| Score: | __/5 | __/5 | __/5 |
| **Control** | Full control over behavior | Dependent on third party | N/A |
| Score: | __/5 | __/5 | __/5 |
| **Maintenance burden** | Ongoing code to maintain | Ongoing cost + dependency | 0 burden |
| Score (inverse — less burden = higher): | __/5 | __/5 | 5/5 |
| **Learning value** | Will building this teach you something valuable? | No learning | No learning |
| Score: | __/5 | __/5 | __/5 |
| **TOTAL** | __/30 | __/30 | __/30 |

### Decision: [Build / Buy / Skip] because [reason]
```

#### 2.3 Build vs. Buy Quick Rules

These heuristics cover 80% of decisions:

| Situation | Default Answer | Why |
|-----------|---------------|-----|
| **Authentication / login** | Buy (Firebase Auth, Auth0) | Security-critical; don't roll your own |
| **Payment processing** | Buy (RevenueCat, Google Billing Library) | Compliance complexity; don't DIY |
| **Analytics** | Buy (Firebase Analytics, Mixpanel) | You need data fast, not custom dashboards |
| **Push notifications** | Buy (Firebase Cloud Messaging) | Infrastructure you don't want to maintain |
| **Crash reporting** | Buy (Firebase Crashlytics) | Industry-standard, free, better than anything you'd build |
| **Core app UI** | Build | This IS your product |
| **Core business logic** | Build | This IS your competitive advantage |
| **Unique features** | Build | This is what differentiates your app |
| **Admin dashboard** | Skip (or buy later) | You can use Firebase Console or database tools directly |
| **Social features** | Skip (usually) | Massive scope; only build if social IS the product |
| **AI/ML features** | Buy (API) or Skip | Training models is a full-time job by itself |
| **Localization** | Buy (translation service) or Skip | Machine translation quality varies; professional is better |

#### 2.4 The Total Cost of Ownership Formula

When comparing build vs. buy, calculate the full cost over 12 months:

```
BUILD Total Cost:
  Development time:      ________ hours × $________/hour (your effective rate)
  + Maintenance time:    ________ hours/year × $________/hour
  + Infrastructure cost: $________/year (if applicable)
  = Total Build Cost:    $________/year

BUY Total Cost:
  Service cost:          $________/month × 12 = $________/year
  + Integration time:    ________ hours × $________/hour (one-time)
  + Vendor lock-in risk: [Low / Medium / High] (qualitative)
  = Total Buy Cost:      $________/year

SKIP Total Cost:
  Lost revenue (estimated): $________/year (be honest — is it really lost?)
  + User churn risk:        [Low / Medium / High]
  = Total Skip Cost:        $________/year (often much lower than you think)
```

---

### Phase 3: Feature Request Evaluation

#### 3.1 The Core Question

When evaluating any feature request, ask one question:

**"Will this grow revenue or reduce churn?"**

If the answer is no, or "maybe, someday," the feature goes to the bottom of the list. If the answer is "yes, and here's how," the feature gets scored.

#### 3.2 Feature Scoring Framework (Adapted RICE)

RICE is a popular prioritization framework (Reach, Impact, Confidence, Effort). Here's a version adapted for solo developers:

```markdown
## Feature Scoring: [Feature Name]

### Reach: How many users will this affect?
- All users: 5
- Most users (50%+): 4
- Many users (20-50%): 3
- Some users (5-20%): 2
- Few users (< 5%): 1
Score: __/5

### Impact: How much will it affect those users?
- Massive — directly increases willingness to pay or dramatically reduces churn: 5
- High — significantly improves experience for a core use case: 4
- Medium — noticeable improvement: 3
- Low — nice to have: 2
- Minimal — cosmetic or edge case: 1
Score: __/5

### Confidence: How sure are you about Reach and Impact?
- Data-backed — user research, analytics, multiple requests: 5
- Strong signals — several user requests, competitive analysis supports it: 4
- Moderate — a few requests, reasonable intuition: 3
- Speculative — sounds good but limited evidence: 2
- Guess — no data, just an idea: 1
Score: __/5

### Effort: How much work is this? (INVERTED — less effort = higher score)
- Tiny — < 4 hours: 5
- Small — 1-2 days: 4
- Medium — 3-5 days: 3
- Large — 1-2 weeks: 2
- Massive — 3+ weeks: 1
Score: __/5

### RICE Score = (Reach × Impact × Confidence) / (6 - Effort)
Score: ________

### Revenue Signal
- Paying user requested it: +2 bonus
- User mentioned they'd pay/upgrade for it: +3 bonus
- User threatened to cancel without it: +3 bonus
- Just a "nice idea" from Reddit/forum: +0
Adjusted Score: ________
```

#### 3.3 Feature Request Tracking Template

Keep a simple spreadsheet or document tracking all requests:

```markdown
## Feature Request Log

| # | Feature | Source | RICE Score | Revenue Signal | Status | Decision Date |
|---|---------|--------|-----------|---------------|--------|--------------|
| 1 | [Feature] | [User email / review / idea] | [Score] | [+bonus] | [Backlog/Planned/Building/Shipped/Rejected] | [Date] |
| 2 | [Feature] | [Source] | [Score] | [+bonus] | [Status] | [Date] |
```

**Review this log monthly.** Patterns emerge: if 10 different users request the same feature, that's a signal worth acting on regardless of individual scores.

#### 3.4 When to Say No

Saying no is the most important skill for a solo developer. Here's when to say it:

| Reject When | Why |
|-------------|-----|
| **One user asks loudly** | One vocal user is not a market. Wait for pattern. |
| **Feature doesn't align with product vision** | Feature creep kills apps. Stay focused. |
| **Effort >> impact** | A 2-week feature used by 3 people is a bad trade. |
| **You'd need to learn an entirely new skill** | Unless learning that skill is strategically valuable. |
| **It mainly serves non-paying users** | Paying customers fund development. Prioritize them. |
| **A competitor has it** | You don't need feature parity. You need differentiation. |

**How to say no gracefully:**
> "Thanks for the suggestion! This isn't on my roadmap for the near term because I'm focused on [what you ARE working on], but I've noted it and will revisit as the app evolves."

---

### Phase 4: Technical Investment Decisions

#### 4.1 The Technical Debt Dilemma

Technical debt is like financial debt — a little is manageable, too much is crippling. As a solo developer, you need a framework for when to invest in technical improvements vs. when to ship features.

#### 4.2 Technical Investment ROI Calculator

```markdown
## Technical Investment Analysis: [Investment Description]

### What is the investment?
[e.g., "Add automated testing for checkout flow"]

### Time cost
- Implementation time: ________ hours
- At your effective hourly rate ($________): $________

### Expected return

#### Time savings (ongoing)
- Current time spent on [related manual work] per month: ________ hours
- Expected time reduction: ________%
- Monthly time saved: ________ hours
- Annual time saved: ________ hours × $________/hour = $________

#### Risk reduction
- Probability of [bad event] without this investment: ________%
- Cost of [bad event] if it happens: $________
- Expected cost avoided: ________% × $________ = $________

#### Quality improvement
- Expected reduction in related bugs/support: ________%
- Current monthly support time for this area: ________ hours
- Monthly support time saved: ________ hours

### Payback period
Total investment cost: $________
Monthly return (time saved + risk avoided + support saved): $________
Payback period: ________ months

### Decision
- Payback < 3 months: DO IT NOW
- Payback 3-6 months: PLAN IT (schedule within next quarter)
- Payback 6-12 months: CONSIDER IT (do when there's slack time)
- Payback > 12 months: SKIP IT (unless it prevents a catastrophic risk)
```

#### 4.3 The 20% Rule for Technical Investment

Allocate roughly 20% of your development time to technical investment:

| Week Type | Feature Development | Technical Investment |
|-----------|-------------------|---------------------|
| Normal week (20h dev) | 16 hours | 4 hours |
| Release week | 20 hours features | 0 hours (ship first) |
| Post-release week | 12 hours features | 8 hours (fix what broke) |
| Quarterly tech debt sprint | 0 hours features | 20 hours (focused cleanup) |

**What counts as technical investment:**
- Adding or improving tests
- Refactoring messy code
- Upgrading dependencies
- Improving CI/CD pipeline
- Performance optimization
- Security improvements
- Documentation

**What does NOT count:**
- Building new features (that's feature development)
- Rewriting something that works because it's "not elegant" (that's perfectionism)
- Switching frameworks because the new one is trendy (that's shiny object syndrome)

---

### Phase 5: Avoiding the Perfectionism Trap

#### 5.1 The Perfectionism-Progress Spectrum

```
[PERFECTIONISM]                                              [RECKLESSNESS]
    ←━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━→

    Never ships      Ships polished      Ships good         Ships broken
    Rewrites         but slow            enough, fast       and ugly
    endlessly

                              ↑
                       YOUR TARGET ZONE
                    "Good enough to ship,
                     proud enough to sign"
```

#### 5.2 Signs You're in the Perfectionism Trap

| Symptom | Reality Check |
|---------|--------------|
| **"Just one more thing before I ship"** | There will always be one more thing. Ship. |
| **Rewriting code that works** | If it works and isn't causing problems, leave it alone. |
| **Spending 4 hours on an animation** | Users notice features, not animation easing curves. |
| **Delaying launch for edge cases** | Launch handles 95% of cases. Fix the 5% after feedback. |
| **Comparing your V1 to a competitor's V5** | They had years and a team. Your V1 needs to be YOUR best V1. |
| **Refactoring without user-facing benefit** | Refactoring is justified when it enables future features. "Cleaner code" alone is not justification. |
| **Reading articles about best practices instead of coding** | You already know enough to build. Build, then optimize. |

#### 5.3 The "Ship It" Checklist

Before declaring a feature "done," run through this minimum-bar checklist. If everything passes, ship it:

```markdown
## Ship-It Checklist: [Feature Name]

### Must Pass (non-negotiable)
- [ ] Core functionality works for the primary use case
- [ ] No data loss risk
- [ ] No security vulnerabilities
- [ ] No crash on common devices (test on 2-3 devices)
- [ ] Looks acceptable (not beautiful — acceptable)
- [ ] User can discover and use the feature without instructions

### Nice to Have (ship without these)
- [ ] Edge cases handled gracefully
- [ ] Animations and polish
- [ ] Perfect error messages
- [ ] Comprehensive tests
- [ ] Documentation

### DECISION: Everything in "Must Pass" checks out?
→ YES: SHIP IT. Improve in the next release.
→ NO: Fix only the failing "Must Pass" items. Then ship.
```

#### 5.4 The "Good Enough" Principle

For most decisions and features, there's a point of diminishing returns. The framework:

```
Effort:     0%────────────50%────────────80%────────────95%────100%
Quality:    0%────────────70%────────────90%────────────97%────100%
Value:      None──────────High──────────Very High───────Marginal──Marginal

                                          ↑
                                     SHIP HERE
                                   (80% effort,
                                    90% quality)
```

The last 10% of quality takes 50% of the effort. For a solo developer, that 50% is better spent on the next feature, fixing a bug, or going outside.

---

### Phase 6: Decision Speed

#### 6.1 The "Default to Action" Principle

For Type 2 (reversible) decisions, the default should be action. Here's why:

| Acting | Not Acting |
|--------|-----------|
| You learn whether it works | You learn nothing |
| You can course-correct with real data | You keep guessing |
| Users see progress | Users see stagnation |
| You build momentum | You build anxiety |
| Worst case: you revert the change | Worst case: you're still stuck |

**The cost of inaction is almost always higher than the cost of a wrong reversible decision.**

#### 6.2 Time-Boxed Decision Making

For any decision you've been stuck on for more than 48 hours, apply a time box:

```markdown
## Decision Time Box: [Decision]

Classification: [Type 1 / Type 2]

If Type 2:
  - Set a timer for 25 minutes
  - List pros and cons (max 5 each)
  - Pick the option with the most pros
  - Execute immediately
  - Review the decision in 30 days

If Type 1:
  - Set a deadline: [date, max 1 week from now]
  - Identify the 1-2 pieces of information that would change your decision
  - If you can get that information before the deadline, get it
  - If you can't, decide with what you have on the deadline date
  - No extensions
```

#### 6.3 The Two-Minute Rule for Micro-Decisions

Solo developers face hundreds of micro-decisions daily: naming a variable, choosing a color, deciding where to put a button, picking between two APIs. For any decision that:
- Takes less than 2 minutes to execute either way
- Is easily changeable later
- Won't be noticed by users

**Just pick one and move on.** Don't research, don't poll friends, don't spend 30 minutes comparing. The compound time cost of micro-decision agonizing is enormous.

#### 6.4 Decision Journal

Keep a brief log of significant decisions to learn from your patterns:

```markdown
## Decision Journal

| Date | Decision | Type | Time Spent Deciding | Outcome (review in 30 days) | Lesson |
|------|----------|------|--------------------|-----------------------------|--------|
| [Date] | [What you decided] | [1/2] | [Time] | [Good/Bad/Neutral] | [What you learned] |
```

Review this journal quarterly. You'll notice patterns — maybe you overthink technical decisions but nail marketing ones, or vice versa. Self-awareness about your decision-making patterns is the meta-skill that makes all other frameworks work better.

---

## Expected Output

```markdown
# Decision Framework: [App Name]

## Active Decisions

### Decision 1: [Description]
- Classification: [Type 1 / Type 2]
- Build/Buy/Skip analysis: [Summary]
- Deadline: [Date]
- Decision: [What you decided]
- Reasoning: [Why]
- Review date: [30 days out]

### Decision 2: [Description]
- Classification: [Type 1 / Type 2]
- Decision: [What you decided]
- Reasoning: [Why]
- Review date: [30 days out]

## Feature Prioritization (Current Quarter)

| Rank | Feature | RICE Score | Revenue Signal | Effort | Decision |
|------|---------|-----------|---------------|--------|----------|
| 1 | [Feature] | [Score] | [Signal] | [Size] | Build / Buy / Skip |
| 2 | [Feature] | [Score] | [Signal] | [Size] | Build / Buy / Skip |
| 3 | [Feature] | [Score] | [Signal] | [Size] | Build / Buy / Skip |

## Technical Investment Plan (This Quarter)
- Weekly allocation: [N] hours (20% of dev time)
- Priority investments:
  1. [Investment] — Payback: [N] months
  2. [Investment] — Payback: [N] months
- Quarterly tech debt sprint: [Date]

## Decision Speed Rules
- Type 2 decisions: Decide within 24 hours
- Type 1 decisions: Decide within 1 week, with deadline
- Micro-decisions: 2-minute rule, no research
- Feature requests: Score with RICE, review monthly

## Perfectionism Guardrails
- Ship when "Must Pass" checklist clears
- No more than [N] rounds of revision on any feature
- If I've been working on something for [N] days without shipping, I'm over-engineering

## Decision Journal
[Link to decision journal document]
- Review frequency: Quarterly
- Last review: [Date]
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) — Focused on decision-making speed and quality for solo developers
- **ST-02** (Structured Sequential Instructions) — Phased approach from classification through decision speed
- **RT-02** (Multi-Dimensional Analysis) — Evaluating decisions across reversibility, impact, cost, and time dimensions
- **RT-03** (Tree of Thoughts) — Multiple decision paths (build/buy/skip) with distinct evaluation criteria
- **CM-01** (Explicit Context Framing) — Solo developer constraints: limited time, all decisions fall to one person, perfectionism risk
- **DS-06** (Prioritization Guidance) — RICE scoring and feature ranking by revenue impact

---

## Related Prompts

- `domain-engineering-workflows/workflows/engineering_solo_dev_roadmap_planner.md` — Apply feature decisions to a concrete product roadmap
- `solo_dev_financial_planning.md` — Financial context for build vs. buy decisions
- `solo_dev_metrics_dashboard.md` — Metrics that inform data-driven decisions
- `domain-productivity/reviews/reviews_solo_dev_weekly_operating_rhythm.md` — Scheduling decision-making time ("CEO time")
- `solo_dev_contractor_management.md` — Executing "buy" decisions through outsourcing
- `solo_dev_support_system.md` — Feature requests from support as decision inputs

---

## Customization Guide

- **For pre-launch developers:** Ignore the RICE scoring framework for now — you don't have enough users for Reach to be meaningful. Focus on Phase 1 (decision classification) and Phase 5 (perfectionism prevention). Your #1 decision framework is: "Does this get me to launch faster?" If yes, do it. If no, skip it.
- **For developers with analysis paralysis:** Start with Phase 6 (decision speed) before anything else. Force yourself to use the 25-minute time box for your current stuck decision. The discomfort of fast decisions is temporary; the cost of ongoing paralysis is cumulative.
- **For developers who ship too fast and break things:** Focus on Phase 1 (classifying decisions) and Phase 4 (technical investment). You need to slow down on Type 1 decisions and invest more in testing and architecture. The "default to action" principle applies to Type 2 decisions, not all decisions.
- **For developers with many paying subscribers ($10K+ MRR):** Your decisions have higher stakes because more users are affected. Invest more time in the RICE scoring framework and involve user research (surveys, interviews) before major feature decisions. The time investment in better decisions pays for itself at scale.
- **For developers who struggle to say no:** Practice the "by saying yes to X, I'm saying no to Y" reframe. Every feature you build is time you can't spend on something else. Keep a "not now" list that you review quarterly — most items on it will feel less important over time, confirming your decision to skip them.
- **For developers considering pivoting their entire app:** That's a Type 1 decision. Don't rush it. Set a 2-week evaluation period. Talk to your users. Look at your data. Consider whether the pivot is driven by insight or by frustration. If you're pivoting because you're bored, that's a different problem than pivoting because the market is telling you to.
