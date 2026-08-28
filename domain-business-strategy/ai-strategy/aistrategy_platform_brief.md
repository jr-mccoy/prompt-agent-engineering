---
title: "Build an Enterprise AI Platform Strategy Brief"
category: business-strategy/ai-strategy
description: "A board/executive brief that frames an enterprise AI platform decision: the problem being solved, the buy-vs-build-vs-partner options, the key trade-offs (lock-in, capability, cost, talent), and a recommendation with its invalidation conditions."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - DS-01
  - RT-02
  - CM-02
  - QA-04
difficulty: advanced
tags:
  - ai-strategy
  - platform-decision
  - enterprise-ai
  - board-brief
  - vendor-selection
updated: "2026-04-20"
related_prompts:
  - domain-business-strategy/ai-strategy/aistrategy_vendor_switch_cost.md
  - domain-business-strategy/ai-strategy/aistrategy_context_accumulation_map.md
  - domain-business-strategy/ai-strategy/aistrategy_capability_compounding_evaluation.md
  - domain-software-engineering/analysis/business/business_model_canvas_analysis.md
---

# Build an Enterprise AI Platform Strategy Brief

**Objective:** Produce a board- or executive-ready brief (3–5 pages) that frames an enterprise AI platform decision: the problem the platform is intended to solve, the realistic options (buy / build / partner / hybrid), the trade-offs that matter, a recommendation, and the specific conditions under which the recommendation would flip. The brief should be defensible in both directions — readers who disagree with the recommendation should still acknowledge it was reasoned, not marketed.

**When to use:** When leadership is deciding how to commit on enterprise AI — a single-vendor platform, a multi-vendor strategy, an internal build, a wrapped-vendor approach, or a partner-led rollout. When vendor pitches are being taken seriously and a counter-analysis is needed. When past AI investment has produced inconsistent return and the platform approach itself is up for reassessment.

**Audience:** CEO, CFO, CIO, CTO, and board. The brief is written for readers who are sophisticated about business but not necessarily about AI; technical depth appears only where it changes the decision.

---

## Inputs Required

1. **Organizational scope.** Which functions will depend on this platform. Employee count, rough revenue band, regulated / unregulated.
2. **The problem statement** as leadership currently describes it. One or two sentences, verbatim. If the problem is "we need an AI strategy," refuse and push for the underlying problem.
3. **Current state of AI use in the org.** What's running today, what it's costing, what it's producing, what's frustrating.
4. **Constraints that are non-negotiable.** Data residency, compliance (HIPAA, GDPR, SOC 2), procurement rules, existing vendor relationships, budget ceiling, decision deadline.
5. **Prior analyses the user already has.** Context accumulation map (`aistrategy_context_accumulation_map.md`), switch-cost estimates, compounding evaluations — cite rather than rebuild.
6. **Who the decision-maker is and what they care about most.** A CFO-led decision reads differently from a CTO-led decision.

Refuse to draft without a concrete problem statement. A brief built on "we should have an AI strategy" will produce platitudes.

---

## Instructions

### Step 1 — Restate the problem precisely

One paragraph. Sharpen the user's problem statement into something specific and falsifiable. Examples:
- "Customer service handles 40k tickets/month; first-response latency is 8 hours; we expect AI to cut it to 30 minutes without raising escalation rate."
- "Code review is a bottleneck across engineering; we expect AI to cut PR cycle time by 40% without raising post-merge defect rate."

If the user's problem is vaguer than this ("we want to be AI-forward"), state the implicit targets the brief will assume and label them as assumptions.

### Step 2 — List the options honestly

Four options, always:
- **Buy a platform.** Single vendor, managed solution. Name the category leader and one alternative.
- **Build in-house.** Model access + internal tooling + internal team.
- **Partner / SI-led.** External partner builds and operates on the org's behalf.
- **Hybrid.** Narrow build for the domains that matter, buy for the rest.

For each, one paragraph covering: what's included, who owns operation, time to value, cost shape (capex vs opex vs per-seat vs consumption), talent required.

"Do nothing" is usually not an option because the org is already using AI informally — but if a moratorium is realistic, add it as a fifth option.

### Step 3 — Trade-off dimensions

Score every option on the same dimensions. Use a short rubric (not a fake-precision matrix):

- **Capability ceiling.** How far the option can go on the hardest use cases.
- **Time to value.** Weeks to first real business outcome.
- **Total cost at scale.** 3-year TCO, ranges.
- **Lock-in.** Switching cost at 24 months (reference `aistrategy_vendor_switch_cost.md` if present).
- **Control over context.** Who owns the accumulated data, prompts, and tuning.
- **Compliance and risk posture.** How easily the option meets the non-negotiable constraints from inputs.
- **Talent dependency.** How much the option depends on hires the org may or may not be able to make.

One-line score + one-line reason per dimension per option. Scores can be ordinal (A / B / C / D) or rated (High / Medium / Low). Consistency matters more than precision.

### Step 4 — Identify the dominant trade-off

One or two paragraphs. Across all the dimensions, which trade-off actually decides this? Common dominant trade-offs:

- Lock-in vs capability ceiling (buy gets ahead of build on capability but locks in).
- Time to value vs control (partner is faster than build but transfers control).
- Talent dependency vs cost (build is cheapest in-steady-state but requires hires).
- Compliance vs capability (the most compliant option may not be the most capable).

Name the trade-off that will drive this decision. Every other dimension is a footnote once the dominant trade-off is identified.

### Step 5 — Recommendation

One paragraph:
- The recommendation, specifically (which option, what scope, what timeline).
- Why this option best resolves the dominant trade-off.
- What investments make this recommendation work (e.g., "requires hiring a lead ML engineer within 90 days," "requires a gateway layer to isolate vendor-specific code").

### Step 6 — Invalidation conditions

This is the most important section. List the specific conditions under which the recommendation flips. Examples:

- "If a competing vendor closes the capability gap in [feature X] within 6 months, buy becomes the clear option."
- "If we fail to hire the lead ML engineer by [date], build becomes infeasible and partner becomes the recommendation."
- "If data residency rules tighten in [jurisdiction], the buy option becomes non-viable."

Without invalidation conditions, the brief is advocacy disguised as analysis. Force 3–5 conditions.

### Step 7 — Risk and mitigation

Short table. Top risks from the recommendation, and how each is mitigated (not "monitored closely," but an actual mitigation).

### Step 8 — Decision ask

One paragraph closing the brief: what specifically the reader is being asked to approve, decide, fund, or escalate. Must have a date. If the decision cannot be made today, the ask is the next meeting or analysis, with a date.

---

## Constraints

### Must
- Sharpen the problem to something falsifiable.
- List at least four options.
- Score all options on the same dimensions.
- Name the dominant trade-off explicitly.
- Include at least three invalidation conditions.
- Include a dated decision ask.
- Flag assumptions that are speculative.

### Must Not
- Pad with generic AI-industry claims.
- Use vendor marketing language as evidence.
- Recommend without trade-off analysis.
- Bury the dominant trade-off in a dimension scorecard.
- Exceed 5 pages. The brief is not the exhaustive analysis; it is the executive-readable summary.
- Embed a vendor choice if the underlying analysis doesn't support one.

---

## False-Positive Prevention

1. **Don't conflate AI platform with AI strategy.** Platforms execute strategy; they're not the strategy. If the brief finds the strategy is unclear, say so — platform decisions on unclear strategy produce write-offs.
2. **Don't take vendor demos as evidence.** Demos run on curated scenarios. Demand evidence on the org's hardest use cases.
3. **Don't ignore talent dependency.** Build and hybrid options often fail on hiring, not on architecture.
4. **Don't skip invalidation conditions.** A brief with no invalidation conditions reads confident and ages badly.
5. **Don't let a CFO-led decision read as a CTO brief.** If the decision-maker's dominant concerns are cost and risk, lead with cost and risk; if capability, lead with capability. The order of presentation is not neutral.
6. **If the problem statement is genuinely "we should have an AI strategy,"** don't draft the brief. The missing step is a problem-statement exercise.

---

## Output Format

```
# Enterprise AI Platform Brief — [date]

## Executive summary (1 paragraph)
[Problem, recommendation, invalidation conditions named, decision ask and date.]

## The problem
[Sharpened, falsifiable. Assumptions labeled.]

## Options
1. **Buy:** [description]
2. **Build:** [description]
3. **Partner:** [description]
4. **Hybrid:** [description]
(5. **Moratorium:** only if realistic.)

## Trade-off scorecard
|                          | Buy | Build | Partner | Hybrid |
|--------------------------|-----|-------|---------|--------|
| Capability ceiling       |     |       |         |        |
| Time to value            |     |       |         |        |
| 3-year TCO range         |     |       |         |        |
| 24-mo lock-in            |     |       |         |        |
| Context control          |     |       |         |        |
| Compliance / risk fit    |     |       |         |        |
| Talent dependency        |     |       |         |        |

(One-line reason per cell or under the table.)

## Dominant trade-off
[One or two paragraphs naming it.]

## Recommendation
[Option, scope, timeline, enabling investments.]

## Invalidation conditions (flips the recommendation)
1. [Condition]
2. [Condition]
3. [Condition]

## Top risks and mitigations
| Risk | Likelihood | Impact | Actual mitigation |
|------|-----------|--------|-------------------|

## Decision ask
[What to approve, by when. If not today, the next analysis / meeting with date.]

## Assumptions and uncertainty
[Labeled assumptions. What we don't yet know.]
```

---

## Verification

- [ ] Problem is falsifiable, not aspirational.
- [ ] Four (or five) options are described on common terms.
- [ ] Scorecard uses consistent ratings, reasons given.
- [ ] Dominant trade-off is named as a paragraph, not just a scorecard row.
- [ ] At least three invalidation conditions are specified.
- [ ] Decision ask has a date.
- [ ] Brief ≤ 5 pages.
- [ ] No vendor marketing language used as evidence.
