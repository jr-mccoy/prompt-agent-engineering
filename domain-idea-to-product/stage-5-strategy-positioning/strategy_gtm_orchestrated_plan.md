---
title: "Orchestrated Go-to-Market Plan (First 90 Days, First 100 Customers)"
category: idea-to-product/strategy
description: "Produce a complete 90-day go-to-market plan for a software/platform product: ICP definition, ranked channel selection (3 channels), launch sequence (pre/at/post), positioning narrative, first-100-customers playbook, and week-by-week activities with measurable milestones."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-02
  - DS-06
  - RT-02
  - QA-01
difficulty: intermediate
tags:
  - go-to-market
  - launch
  - distribution
  - positioning
  - first-100-customers
updated: "2026-05-19"
related_prompts:
  - domain-idea-to-product/stage-5-strategy-positioning/swot_analysis.md
  - domain-idea-to-product/stage-5-strategy-positioning/marketing_competitive_differentiation.md
  - domain-idea-to-product/stage-5-strategy-positioning/startup_value_proposition.md
  - domain-idea-to-product/stage-3-market-research/research_competitive_landscape.md
---

# Orchestrated Go-to-Market Plan (First 90 Days, First 100 Customers)

**Objective:** Produce a single, cohesive 90-day GTM plan that ties together ICP, channel selection, launch sequence, positioning, and the first-100-customers playbook. The output must be specific enough to assign each week's activities to an owner, with measurable milestones at week 4, week 8, and week 12.

## When to Use

- Stage 7 (PRD) is in motion or complete; you're 30-60 days from a usable MVP.
- You're staring at a pile of disconnected tactics (a landing page here, a Substack there, "we should do SEO") and need an orchestrated plan, not a tactics dump.
- You're a solo founder or small team and need realistic-capacity sequencing, not enterprise-marketing-team scope.

## Inputs

The user must provide:
1. **Product one-liner** and **PRD link/summary** (from stage 7).
2. **Validated ICP signals** from stage 2 (which segments scored highest in customer discovery).
3. **Unit economics verdict** from stage 3 (GREEN/YELLOW/RED — informs how aggressive paid acquisition can be).
4. **Founder distribution wedge** identified in stage 1 (existing audience, employer relationship, community access, etc.).
5. **Launch capacity**: how many hours/week the founder can spend on GTM (vs. building).
6. **Hard launch date or window** (e.g., "first week of August" or "any time in Q3").

If any input is missing, ask. Do not guess the ICP.

## Constraints

**Must:**
- Define ICP at three levels of resolution: firmographic, role/persona, and use-case trigger.
- Recommend exactly 3 channels, ranked. Justify each pick against the ICP and the founder's distribution wedge. Explicitly REJECT 2-3 channels with reasoning.
- Provide a launch sequence with named phases: T-30 (build audience), T-0 (launch week), T+30 (signal harvest), T+60 (iterate), T+90 (commit/pivot).
- Every week of the 12-week plan must list 2-5 specific activities with named owner and time budget.
- Provide measurable milestones at weeks 4, 8, 12 — with the activity that triggers KILL the plan if missed.
- Distinguish "first-10-customers" (high-touch, often manual) from "first-100" (channel-driven). Most founders blur this.

**Must Not:**
- Recommend channels the founder has no proven access to. "Content marketing" is not a channel unless they have writing distribution.
- Include "viral loop" or "growth hacking" as a strategy.
- Mix up brand-building (12+ months) with demand-generation (this quarter).
- Promise specific conversion rates or CAC numbers — those are outputs of the plan, not inputs.
- Recommend simultaneous activation on 5+ channels with a 2-person team.

## Instructions

### Step 1: ICP at three resolutions
- **Firmographic:** company size, stage, geography, vertical.
- **Role/persona:** title, seniority, what they own, how they get evaluated.
- **Trigger context:** what event in their week/quarter makes them aware they have the problem your product solves.

### Step 2: Channel selection (3 ranked, with 2-3 rejected)
For each channel CANDIDATE, score:
- ICP density (where does the ICP actually congregate?)
- Founder access (existing relationship/audience?)
- Time-to-first-signal (days/weeks to know if it's working?)
- Cost per qualified conversation
- Compounding vs. linear (does effort today pay off forever or only this week?)

Pick 3 to activate. Explicitly reject the others with reasoning.

### Step 3: Positioning narrative (one paragraph, max 80 words)
Must contain: who it's for, what category it's in (or anti-category), what unique value, against what alternative. Do NOT use words like "innovative," "cutting-edge," "next-generation."

### Step 4: Launch sequence (5 phases)
- **T-30 (audience prep):** What you do to have a warm cohort to launch to.
- **T-0 (launch week):** Concrete activities Mon-Fri.
- **T+30 (signal harvest):** What metrics you gather, what conversations you have, what you change.
- **T+60 (iterate):** Pricing test, positioning test, or channel double-down based on T+30 data.
- **T+90 (commit/pivot):** GO (scale the winner) / RESHAPE (different ICP) / PAUSE (kill GTM, return to product).

### Step 5: First-100-customers playbook (split into two phases)
- **Customers 1-10 (manual):** Specific people the founder will personally reach out to. Named where possible. Outreach script. Onboarding white-glove plan.
- **Customers 11-100 (channel-driven):** Which of the 3 channels delivers each cohort. Expected conversion at each funnel stage with sensitivity flag.

### Step 6: 12-week activity calendar
Week-by-week, 2-5 activities, each with: activity / owner / time budget / dependency. Use a table.

### Step 7: Milestones and kill conditions
- **Week 4 checkpoint:** [specific signal]. If missed → [revise plan or kill specific channel].
- **Week 8 checkpoint:** [specific signal]. If missed → [revise].
- **Week 12 verdict:** [GO/RESHAPE/PAUSE thresholds].

## Output Format

```
## GTM Plan: [product name]

### ICP
- **Firmographic:** ...
- **Role/persona:** ...
- **Trigger context:** ...

### Positioning
> [one paragraph, ≤80 words]

### Channels (3 ranked)
1. [Channel A] — why it wins for this ICP, founder access, expected time-to-signal
2. [Channel B] — ...
3. [Channel C] — ...

**Rejected:** [Channel X] — because [reason]; [Channel Y] — because [reason]

### Launch sequence
- **T-30:** ...
- **T-0:** ...
- **T+30:** ...
- **T+60:** ...
- **T+90:** ...

### First-10 (manual)
[List of named or specifically-described people, outreach script, onboarding plan]

### Customers 11-100 (channel-driven)
[Funnel by channel, expected conversion at each stage]

### 12-week activity calendar
| Week | Activity | Owner | Hrs | Dep |
|------|----------|-------|-----|-----|
| 1 | ... | ... | ... | ... |
... [through week 12] ...

### Milestones
- **Week 4:** [signal]. Kill condition: [if X then Y].
- **Week 8:** [signal]. Kill condition: [if X then Y].
- **Week 12 verdict thresholds:**
  - GO: ...
  - RESHAPE: ...
  - PAUSE: ...
```

## Verification

- [ ] ICP defined at all 3 resolution levels
- [ ] Exactly 3 channels chosen, 2-3 rejected with reasoning
- [ ] Positioning ≤80 words, no banned words
- [ ] 5 launch phases present
- [ ] First-10 and first-11-to-100 differentiated
- [ ] 12 weeks each have 2-5 activities with owner + hours
- [ ] Week 4, 8, 12 checkpoints have measurable signals AND kill conditions

## False-Positive Prevention

- **"Content marketing" as a channel is almost always wrong** unless the founder already has 1,000+ subscribers or domain authority. Otherwise it's an 18-month asset, not a launch channel.
- **PH/HN launches are events, not channels.** Plan them as T-0 spikes that feed one real channel (usually email capture), not as growth strategies.
- **First-10 customers cannot be channel-acquired.** If the plan tries to channel-acquire customers 1-10, it's wrong. Channels require iteration; the first 10 require manual love.
- **Capacity overruns kill plans.** Total weekly hours across activities must be ≤ stated founder capacity. Validate the sum.
- **Vanity milestones masquerade as kill conditions.** "We'll have a beta list of 500" is not a kill condition unless missing it actually triggers a different action.
