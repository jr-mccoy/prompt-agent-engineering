---
title: "Jobs to be Done (JTBD) Analysis for Codebase"
category: business/analysis
description: "Apply the Jobs to be Done framework to understand the underlying customer motivations, functional/emotional/social jobs, and hiring criteria that drive product adoption and usage"
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - DS-01  # Framework Application
  - RT-02  # Multi-Dimensional Analysis
  - QA-02  # Adversarial Thinking
  - DS-06  # Prioritization Guidance
difficulty: intermediate
tags:
  - customer-research
  - product-strategy
  - innovation
  - user-needs
  - product-development
updated: "2026-01-25"
related_prompts:
  - domain-business-strategy/analysis/value_proposition_canvas_analysis.md
  - domain-business-strategy/analysis/product_market_fit_analysis.md
  - domain-business-strategy/analysis/kano_model_analysis.md
  - domain-business-strategy/analysis/customer_journey_map_analysis.md
---

# Jobs to be Done (JTBD) Analysis for Codebase

**Objective:** Analyze the codebase using the Jobs to be Done framework to understand the core functional, emotional, and social jobs customers are trying to accomplish, identify where the product excels or falls short in helping customers make progress, and uncover opportunities for innovation based on underserved or overserved jobs.

## When to Use

- **Use when:** Trying to understand why customers hire (or fire) your product
- **Use when:** Prioritizing features based on customer needs rather than competitor features
- **Use when:** Seeking innovation opportunities in existing markets
- **Use when:** Repositioning a product or exploring new market segments
- **Use when:** Customer behavior doesn't match stated preferences (say-do gap)
- **Don't use when:** You need demographic segmentation (JTBD focuses on situational jobs, not personas)
- **Don't use when:** The product is infrastructure with no end-user (use technical analysis instead)
- **Don't use when:** You have zero customer interaction data (JTBD requires observation/interview insights)

## Instructions

1. **Identify the Core Job(s) the Product Addresses**
   - What fundamental progress is the customer trying to make?
   - Express the job in customer language, not product features
   - Use the job statement format: "When _______, I want to _______, so I can _______."
   - Identify the main job and related jobs (jobs rarely come alone)
   - **Evidence to collect:** Customer interviews, support tickets, search queries, review analysis

2. **Map the Job Dimensions**

   **a. Functional Job (What they're trying to accomplish):**
   - What practical task does the product help complete?
   - What process does it make more efficient or effective?
   - What would happen if this job weren't done?
   - What metrics indicate job completion?

   **b. Emotional Job (How they want to feel):**
   - What emotional state are they seeking?
   - What fears or anxieties does the job relieve?
   - What aspirations does it fulfill?
   - How do they want to feel during and after using the product?

   **c. Social Job (How they want to be perceived):**
   - How does this affect their status or reputation?
   - Who is watching when they do this job?
   - What does using this product signal to others?
   - What social risks are they managing?

3. **Analyze the Circumstance (Context Matters)**
   - **When:** What triggers the need to do this job? (time, event, situation)
   - **Where:** In what physical or digital context does the job arise?
   - **While:** What else is the customer doing when this job surfaces?
   - **With whom:** Are others involved in or affected by the job?
   - **Struggling with:** What makes this job difficult right now?
   - **Evidence to collect:** User session recordings, contextual inquiry, day-in-the-life interviews

4. **Map the Competitive Landscape (Hired & Fired)**
   - What did customers use BEFORE hiring this product?
   - What competing solutions could customers "hire" instead?
   - Include non-obvious competitors (Excel, email, pen and paper, doing nothing)
   - What would cause customers to "fire" this product?
   - What anxieties prevent switching (inertia, migration cost, learning curve)?
   - **Evidence to collect:** Churn reasons, competitive win/loss analysis, switching stories

5. **Assess Job Performance (Over/Under-Served)**
   - For each job dimension, evaluate:
     - **Importance:** How critical is this job to the customer?
     - **Satisfaction:** How well does the product perform this job?
   - Identify patterns:
     - **Underserved jobs:** High importance, low satisfaction → opportunity
     - **Overserved jobs:** Low importance, high investment → simplification opportunity
     - **Well-served jobs:** High importance, high satisfaction → protect and maintain
     - **Table stakes:** Low importance, expected → don't over-invest

6. **CRITICAL: Validate Job Insights Before Reporting**
   - For each identified job:
     - Is this a real job customers articulate, or our interpretation?
     - Do we have evidence from multiple customers, or a single anecdote?
     - Is the job specific enough to be actionable?
     - Could we be confusing a solution preference with the underlying job?
   - Test for outcome-driven innovation:
     - Can we measure job completion independently of our product?
     - Would the job exist even if our product didn't?
   - Check for hired/fired evidence:
     - Do we have stories of customers switching TO and FROM us?
     - What were the real reasons (not just stated reasons)?

7. **Develop Prioritized Recommendations**
   - Rank opportunities by job importance and underservedness
   - Identify quick wins (improve existing features for key jobs)
   - Identify innovation opportunities (new features for underserved jobs)
   - Identify simplification opportunities (reduce for overserved jobs)
   - Consider job-based segmentation vs. demographic segmentation

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Confuse features with jobs (customers don't hire "notifications"—they hire "staying informed without effort")
- Accept customer-stated preferences as jobs (dig for the underlying progress)
- Define jobs so broadly they're meaningless ("be productive")
- Define jobs so narrowly they're just tasks ("click the submit button")
- Assume your product categories define the competitive set
- Treat all jobs as equal—importance varies dramatically
- Ignore the circumstance—the same person has different jobs in different contexts

✅ **DO:**
- Express jobs in customer language, not product/feature language
- Include emotional and social dimensions, not just functional
- Validate jobs with "switch stories" (when customers hired/fired products)
- Identify the Forces of Progress (push, pull, anxiety, habit) for each job
- Test whether jobs are "must-have" (pain if not done) vs. "nice-to-have"
- Consider the job's timeline (short-term task vs. ongoing job)
- Acknowledge when you're inferring vs. when you have direct evidence

## Confidence Levels

Rate each job insight with a confidence level:

- **Validated:** Direct customer evidence (interviews, switch stories, behavioral data)
- **Inferred:** Indirect signals (support tickets, feature requests, usage patterns)
- **Hypothesis:** Logical reasoning based on job structure; needs validation

## Expected Output

A comprehensive JTBD analysis including:
- Core job statement(s) with circumstance context
- Job dimension breakdown (functional, emotional, social)
- Competitive landscape mapping
- Job performance assessment (over/underserved)
- Prioritized opportunity recommendations

### Output Format

```markdown
## Jobs to be Done Analysis: [Product Name]

### Executive Summary
[3-5 sentences summarizing the core jobs, key insights, and top opportunities]

### Core Jobs Identified

#### Primary Job
**Job Statement:** When [circumstance], I want to [progress], so I can [outcome].

**Example:** "When I'm leading a remote team and lose track of who's doing what, I want to see everyone's status at a glance, so I can intervene early if something is off track."

**Importance:** Critical | Important | Nice-to-Have
**Current Performance:** Well-Served | Underserved | Overserved
**Confidence:** Validated | Inferred | Hypothesis

#### Related Jobs
[List 2-4 related jobs with same structure]

### Job Dimension Analysis

#### Functional Jobs
| Job | Evidence | Importance | Product Performance | Gap |
|-----|----------|------------|---------------------|-----|
| [Job] | [How we know] | High/Med/Low | Strong/Adequate/Weak | [Opportunity] |

#### Emotional Jobs
| Job | Evidence | Importance | Product Performance | Gap |
|-----|----------|------------|---------------------|-----|
| [Feeling sought] | [How we know] | High/Med/Low | Strong/Adequate/Weak | [Opportunity] |

#### Social Jobs
| Job | Evidence | Importance | Product Performance | Gap |
|-----|----------|------------|---------------------|-----|
| [Perception sought] | [How we know] | High/Med/Low | Strong/Adequate/Weak | [Opportunity] |

### Circumstance Analysis

| Factor | Details | Evidence |
|--------|---------|----------|
| **When (Trigger)** | [What triggers the job] | [How we know] |
| **Where (Context)** | [Physical/digital environment] | [How we know] |
| **While (Concurrent)** | [Other activities] | [How we know] |
| **With Whom** | [Others involved] | [How we know] |
| **Struggling With** | [Current pain points] | [How we know] |

### Competitive Landscape (Hiring/Firing)

#### What Customers Hired Before Us
| Solution | Jobs It Served | Why Fired |
|----------|---------------|-----------|
| [Competitor/alternative] | [Which jobs] | [Why they switched] |

#### What Customers Might Hire Instead
| Alternative | Jobs It Serves Better | When They'd Switch |
|-------------|----------------------|-------------------|
| [Competitor/alternative] | [Which jobs] | [Trigger for switch] |

#### Forces of Progress
```
FORCES PUSHING AWAY FROM STATUS QUO:
├── Push (Problems with current solution)
│   └── [Specific pushes]
└── Pull (Attraction to new solution)
    └── [Specific pulls]

FORCES RESISTING CHANGE:
├── Anxiety (Concerns about new solution)
│   └── [Specific anxieties]
└── Habit (Attachment to current solution)
    └── [Specific habits]
```

### Job Performance Assessment

#### Opportunity Matrix
```
                    HIGH IMPORTANCE
                          │
    UNDERSERVED           │          WELL-SERVED
    (Opportunity)         │          (Protect)
                          │
    ──────────────────────┼──────────────────────
                          │
    TABLE STAKES          │          OVERSERVED
    (Don't over-invest)   │          (Simplify)
                          │
                    LOW IMPORTANCE

          LOW SATISFACTION ──────► HIGH SATISFACTION
```

| Job | Importance | Satisfaction | Quadrant | Opportunity |
|-----|------------|--------------|----------|-------------|
| [Job] | 8/10 | 4/10 | Underserved | [Specific opportunity] |

### Prioritized Recommendations

| # | Opportunity | Job Addressed | Type | Impact | Confidence | Priority |
|---|-------------|---------------|------|--------|------------|----------|
| 1 | [Recommendation] | [Job] | Innovation/Improve/Simplify | High/Med/Low | Level | P0/P1/P2 |

### Validation Needed
[List key hypotheses that need customer validation before acting]
```

## Example Output

```markdown
## Jobs to be Done Analysis: CodeReview Pro (AI Code Review Tool)

### Executive Summary

CodeReview Pro is primarily hired to help developers **catch bugs before they embarrass themselves in code review**—the job is as much emotional (confidence, reputation) as functional (finding defects). The product performs well on the functional job of finding issues but underserves the emotional job of **reducing review anxiety** and the social job of **appearing thorough to senior reviewers**. The biggest opportunity is addressing the circumstance of "5 minutes before submitting a PR"—developers want instant confidence, not a comprehensive report. Competitors include manual checklist review, senior developer review, and "just hoping it's fine."

### Core Jobs Identified

#### Primary Job
**Job Statement:** When I'm about to submit a pull request and worried I've missed something obvious, I want to get a quick sanity check of my code, so I can submit with confidence and avoid embarrassment in review.

**Importance:** Critical
**Current Performance:** Underserved (functional OK, emotional/social weak)
**Confidence:** **Validated** (15 customer interviews, churn analysis)

**Evidence:**
- "I use it to make sure I didn't do something stupid before my tech lead sees it" - Customer interview
- 73% of users run the tool immediately before PR submission
- Top feature request: "faster results" (not "more thorough")

---

#### Related Jobs

**Job 2: Learning from mistakes to improve coding skills**
**Job Statement:** When I get feedback on my code, I want to understand the pattern of my mistakes, so I can level up as a developer and make fewer errors over time.

**Importance:** Important
**Current Performance:** Underserved
**Confidence:** **Inferred** (feature requests, but no switch stories)

---

**Job 3: Demonstrating code quality to stakeholders**
**Job Statement:** When leadership asks about code quality, I want to show metrics and trends, so I can demonstrate engineering excellence and justify technical decisions.

**Importance:** Nice-to-Have (for individual developers), Critical (for engineering managers)
**Current Performance:** Well-Served (reports exist)
**Confidence:** **Validated** (manager interviews)

---

**Job 4: Maintaining consistency across a large codebase**
**Job Statement:** When our team ships code from multiple contributors, I want to ensure consistent patterns and standards, so our codebase stays maintainable as we grow.

**Importance:** Important
**Current Performance:** Adequate
**Confidence:** **Inferred** (usage patterns suggest team accounts use rule customization heavily)

---

### Job Dimension Analysis

#### Functional Jobs

| Job | Evidence | Importance | Performance | Gap |
|-----|----------|------------|-------------|-----|
| Find bugs and code issues | Usage data: 89% of findings are viewed | **High** | Strong | Minimal |
| Reduce false positives | NPS comments: "too noisy" appears 23 times | **High** | Weak | **Major gap** |
| Provide actionable fixes | 45% of suggestions are applied | Medium | Adequate | Improvement needed |
| Integrate into workflow | GitHub/VS Code integration rated 4.2/5 | **High** | Strong | Minimal |
| Run fast (< 60 sec) | "Speed" is #1 feature request | **High** | Weak | **Major gap** |

#### Emotional Jobs

| Job | Evidence | Importance | Performance | Gap |
|-----|----------|------------|-------------|-----|
| Feel confident before submitting PR | "peace of mind" mentioned in 8/15 interviews | **High** | Weak | **Major gap** |
| Avoid embarrassment from obvious mistakes | "stupid mistake" / "caught before review" themes | **High** | Adequate | Some gap |
| Feel like a skilled developer | "learning" mentioned, but tool feels punitive | Medium | Weak | **Major gap** |
| Reduce anxiety about code quality | Anxiety about "what am I missing" persists | **High** | Weak | **Major gap** |

#### Social Jobs

| Job | Evidence | Importance | Performance | Gap |
|-----|----------|------------|-------------|-----|
| Appear thorough to reviewers | "I want my lead to see I checked" | **High** | Weak | **Major gap** |
| Demonstrate professionalism | Tool badge/report sharing rarely used | Medium | Weak | Opportunity |
| Be seen as proactive about quality | Team leaders want to show mgmt | Medium | Adequate | - |
| Not be the one who breaks the build | "I don't want to be that guy" | **High** | Adequate | - |

### Circumstance Analysis

| Factor | Details | Evidence |
|--------|---------|----------|
| **When (Trigger)** | 5-10 minutes before PR submission; after significant changes; before major release | 73% of runs happen within 15 min of PR creation |
| **Where (Context)** | IDE or terminal; often with PR interface open in another tab | Session recordings show split-screen workflow |
| **While (Concurrent)** | Writing PR description; mentally rehearsing response to review comments | Interview theme: "I'm already thinking about the review" |
| **With Whom** | Solo, but imagining the reviewer (often a senior dev) | "I think about what [senior] will say" |
| **Struggling With** | Time pressure; uncertainty about what reviewers will catch; past experiences of embarrassment | Churn interviews: "too slow" and "still got review comments" |

### Competitive Landscape (Hiring/Firing)

#### What Customers Hired Before Us

| Solution | Jobs It Served | Why Fired |
|----------|---------------|-----------|
| **Manual review checklist** | Thoroughness, peace of mind | "Tedious, I skip steps when rushed" |
| **Linting only** | Catch syntax/style issues | "Doesn't catch logic bugs" |
| **Senior dev pre-review** | Confidence, learning | "Can't always bother them" |
| **Nothing (YOLO)** | Speed (no time cost) | "Got burned too many times" |
| **Competing tool X** | Similar functional job | "Too many false positives" |

#### What Customers Might Hire Instead

| Alternative | Jobs It Serves Better | When They'd Switch |
|-------------|----------------------|-------------------|
| **GitHub Copilot code review** | Speed (inline, instant) | If accuracy matches ours |
| **Stricter CI/CD pipeline** | Team consistency | If they prioritize automation over feedback |
| **Pair programming** | Learning, confidence | If remote work decreases |
| **Doing nothing** | Speed, no friction | If time pressure is extreme |

#### Forces of Progress

```
FORCES PUSHING AWAY FROM STATUS QUO:
├── Push (Problems with current solution)
│   ├── Past embarrassment from missed bugs
│   ├── Inconsistent feedback from manual review
│   ├── Senior devs don't have time to pre-review
│   └── Growing codebase makes manual checking harder
└── Pull (Attraction to CodeReview Pro)
    ├── Automation promises thoroughness
    ├── AI might catch things humans miss
    ├── Demonstrates proactive quality approach
    └── Other respected developers use it

FORCES RESISTING CHANGE:
├── Anxiety (Concerns about new solution)
│   ├── "What if it misses something important?"
│   ├── "Will it slow down my workflow?"
│   ├── "False positives will waste my time"
│   └── "Will it make me look like I need help?"
└── Habit (Attachment to current solution)
    ├── "My checklist works well enough"
    ├── "I trust my own review process"
    ├── "Overhead of learning new tool"
    └── "I already have too many tools"
```

### Job Performance Assessment

#### Opportunity Matrix

```
                    HIGH IMPORTANCE
                          │
    UNDERSERVED           │          WELL-SERVED
    • Confidence/anxiety  │          • Find bugs
    • Speed of results    │          • Workflow integration
    • Appear thorough     │          • Team reporting
    • Learn from feedback │
    ──────────────────────┼──────────────────────
                          │
    TABLE STAKES          │          OVERSERVED
    • Support common      │          • Advanced rule
      languages           │            customization
    • Basic integration   │          • Enterprise audit
                          │            features
                    LOW IMPORTANCE

          LOW SATISFACTION ──────► HIGH SATISFACTION
```

| Job | Importance | Satisfaction | Quadrant | Opportunity |
|-----|------------|--------------|----------|-------------|
| Find bugs | 9/10 | 7/10 | Well-Served | Protect; incremental improve |
| Speed of results | 9/10 | 4/10 | **Underserved** | **Critical opportunity** |
| Confidence before PR | 9/10 | 3/10 | **Underserved** | **Critical opportunity** |
| Reduce false positives | 8/10 | 4/10 | **Underserved** | High opportunity |
| Appear thorough | 7/10 | 3/10 | Underserved | Medium opportunity |
| Learn from mistakes | 6/10 | 3/10 | Underserved | Medium opportunity |
| Rule customization | 4/10 | 8/10 | Overserved | Simplify |
| Enterprise audit | 3/10 | 9/10 | Overserved | Don't over-invest |

### Prioritized Recommendations

| # | Opportunity | Job Addressed | Type | Impact | Confidence | Priority |
|---|-------------|---------------|------|--------|------------|----------|
| 1 | **"Quick Check" mode** (< 30 sec, high-confidence issues only) | Speed, Confidence | Innovation | High | Validated | **P0** |
| 2 | **Confidence indicator** ("CodeReview Pro found no critical issues") | Confidence, Appear thorough | Innovation | High | Validated | **P0** |
| 3 | **Shareable badge** for PRs ("Reviewed by CodeReview Pro") | Appear thorough, Social proof | Innovation | Medium | Inferred | **P1** |
| 4 | Improve false-positive filtering with user feedback loop | Reduce noise | Improve | High | Validated | **P1** |
| 5 | **"What I learned" summary** after each review | Learn from mistakes | Innovation | Medium | Inferred | **P2** |
| 6 | Simplify rule customization UI (hide advanced options) | Reduce complexity | Simplify | Low | Inferred | **P2** |
| 7 | Reduce enterprise-only features in core product | Focus | Simplify | Low | Hypothesis | **P3** |

### Validation Needed

1. **Quick Check hypothesis:** Do users actually want speed over thoroughness? Run A/B test with 30-sec mode vs. current.
2. **Confidence indicator value:** Will a "no issues found" message actually increase confidence? Prototype and user test.
3. **Badge adoption:** Would developers actually share badges on PRs? Survey + prototype.
4. **Learning job importance:** Is "learning from mistakes" a nice-to-have or would users pay more for it?

### Key Insights Summary

1. **The job is emotional as much as functional.** Developers want to *feel* confident, not just *be* told about bugs. The product overserves the "find issues" job and underserves the "feel confident" job.

2. **Speed is critical because of when the job arises.** The circumstance is "5 minutes before PR submission"—users don't want a thorough report, they want quick reassurance.

3. **The social job is invisible but important.** Developers want their reviewers to see they used the tool. This is an unexploited opportunity.

4. **"Doing nothing" is real competition.** Time pressure makes skipping code review a valid alternative. If the tool is too slow or noisy, users won't use it.
```

## Customization Guide

- **For B2B Products:** Separate the buyer's job from the user's job—they may be different people with different jobs
- **For Platform Products:** Analyze jobs for each side of the platform (e.g., marketplace sellers vs. buyers)
- **For Commoditized Markets:** Focus on emotional and social jobs—functional jobs are often table stakes
- **For Emerging Categories:** Focus on circumstance and alternatives—the job exists even if solutions don't

## Techniques Used

- **ST-01 (Clear Objective Statement):** Explicit goal of understanding customer jobs and identifying opportunities
- **ST-02 (Structured Sequential Instructions):** Systematic progression from job identification through analysis to recommendations
- **DS-01 (Framework Application):** Direct application of Jobs to be Done methodology (functional/emotional/social, Forces of Progress)
- **RT-02 (Multi-Dimensional Analysis):** Evaluation across job dimensions, circumstances, and competitive alternatives
- **QA-02 (Adversarial Thinking):** False-positive prevention distinguishes real jobs from assumed jobs
- **DS-06 (Prioritization Guidance):** Recommendations prioritized by job importance and underservedness

## Related Prompts

- [Value Proposition Canvas Analysis](value_proposition_canvas_analysis.md) - Maps jobs to product value delivery
- [Product-Market Fit Analysis](product_market_fit_analysis.md) - Evaluates how well product serves jobs
- [Kano Model Analysis](../../domain-business-strategy/analysis/kano_model_analysis.md) - Feature categorization by job importance
- [Customer Journey Map Analysis](../../domain-business-strategy/analysis/customer_journey_map_analysis.md) - Jobs across the customer lifecycle
