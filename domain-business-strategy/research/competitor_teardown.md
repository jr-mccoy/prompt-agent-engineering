---
title: "Competitor Teardown — Product, Positioning, Distribution, Economics, Team, and Stated vs. Revealed Strategy"
category: business-strategy/research
description: "Structured single-competitor teardown across product, positioning, distribution, unit-economics signals, team, funding/runway, and recent moves — ending in stated-versus-revealed strategy and 3–5 strategic takeaways for the user's own positioning. Counters the failure of describing a competitor's marketing back to yourself instead of inferring what they are actually doing from observable signals."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - DS-02
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - competitive-analysis
  - teardown
  - market-research
  - positioning
  - strategy
updated: "2026-06-18"
reasoning:
  styles: [analytic, abductive, comparative, strategic]
  stakes: moderate
  horizon: days
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: single_domain
  collaboration: solo_or_team
  output_format: [structured, narrative]
  user_role: [founder, pm, strategist, analyst, marketer]
  mode: [diagnose, synthesize, decide]
related_prompts:
  - domain-business-strategy/research/research_competitive_landscape.md
  - domain-business-strategy/research/user_research_synthesis.md
  - domain-business-strategy/research/research_company_deep_dive.md
---

# Competitor Teardown

**Objective:** Tear down a single competitor's product, strategy, and organization from observable signals, and convert the analysis into 3–5 strategic takeaways for the user's own positioning. The teardown covers product (features, UX, performance, pricing), positioning (claimed vs. actual value prop, target customer), distribution (channels, partnerships, paid vs. organic), unit-economics signals, team (hires, departures, public statements), funding and runway, and recent moves — and it ends by separating what the competitor *says* its strategy is from what its behavior *reveals*. The deliverable is teardown-deck-style sections, not a paragraph of impressions.

A teardown fails when it parrots the competitor's own marketing back as analysis. The discipline here is inference from signal: what does their pricing page reveal about their target customer; what does a wave of enterprise-sales hires reveal about a move upmarket; what does the gap between the homepage promise and the actual product reveal about where they're stuck.

**When to use:**
- Sharpening your own positioning against a specific competitor.
- Preparing a competitive section for a board deck, investor update, or strategy offsite.
- A competitor just made a move (launch, pivot, raise, hire) and you need to read it.
- Win/loss analysis pointing at one rival you keep encountering.

**When NOT to use:**
- You need a broad market map across many players — use `research_competitive_landscape.md`.
- You need a full neutral company profile rather than a strategy read — use `research_company_deep_dive.md`.
- There's no observable signal to work from (pre-launch stealth competitor) — the teardown would be speculation.

**Audience:** Founders, product managers, strategists, competitive-intelligence analysts, and product marketers.

---

## Inputs / Context

1. **The competitor.** The specific company/product to tear down.
2. **Your vantage.** Your own product and positioning — the teardown is relative to you.
3. **Accessible signals.** Website, pricing page, app/product (trial or screenshots), job postings, press, social, reviews, filings, LinkedIn.
4. **The question.** What decision this teardown informs (positioning, pricing, roadmap, GTM).
5. **Recency window.** How far back "recent moves" should look (default ~6 months).

---

## Constraints

### Must
- Cover all sections: **product, positioning, distribution, unit-economics signals, team, funding/runway, recent moves, stated vs. revealed strategy.**
- **Distinguish observation from inference.** State the signal, then the inference drawn from it. "They hired 6 enterprise AEs (observed) → moving upmarket (inferred)."
- Separate **claimed value prop** (what the homepage says) from **actual value prop** (what the product delivers and what customers actually buy it for).
- Read **unit economics from signals** where direct numbers are absent — pricing structure, sales motion (self-serve vs. sales-led), free-tier generosity, discounting — and label these as estimates.
- Track **recent moves** in the window and read each one for what it implies about strategy.
- End with **stated vs. revealed strategy**: what they say they're doing vs. what their hiring, pricing, roadmap, and spend reveal.
- Produce **3–5 strategic takeaways for the user's own positioning** — the teardown exists to inform the user's moves, not to admire the competitor's.
- Mark **confidence** on inferences; flag low-confidence reads rather than asserting them.

### Must Not
- Restate the competitor's marketing as if it were analysis.
- Present an inference as an observed fact. Keep the signal and the inference distinct.
- Assume the claimed value prop is the real one without checking the product and customer behavior.
- Invent unit-economics numbers; estimate from signals and label as estimates.
- Produce a teardown with no takeaways for the user — analysis without an action is theater.
- Treat the competitor as static; the recent-moves and revealed-strategy sections are where the live picture lives.

---

## Instructions

1. **Frame the teardown around your decision.** State what decision this informs and what about this competitor matters most to it. That focuses depth where it pays.
2. **Tear down the product.** Catalog the core features, UX quality, performance, and pricing structure. Note where the product is strong, where it's thin, and what the pricing page reveals about who they're built for. Observation → inference throughout.
3. **Read the positioning.** Capture the claimed value prop (their words) and the actual value prop (what the product delivers and what reviews/customers say they buy it for). Identify the real target customer — often narrower or different from the stated one.
4. **Map distribution.** Identify channels (self-serve, sales-led, PLG, partnerships, marketplace), paid vs. organic mix (ads, SEO, content, community), and key partnerships. Infer the dominant motion and what it costs them.
5. **Estimate unit economics from signals.** Without internal numbers, read the sales motion, ACV band, free-tier design, expansion mechanics, and discounting. Estimate whether the model looks efficient or burn-heavy, and label confidence.
6. **Analyze the team.** Note key hires and departures, the functional shape of recent hiring (what they're staffing up tells you the next move), and notable public statements from leadership. Read leadership pedigree for playbook signals.
7. **Assess funding and runway.** Capture last raise, total raised, investors, and any public runway signals (hiring freezes, layoffs, pricing changes). Infer pressure level.
8. **Track recent moves.** List launches, pivots, repricing, partnerships, and messaging shifts in the window. For each, read the implied strategic intent.
9. **Separate stated vs. revealed strategy and extract takeaways.** Write what the competitor says it's doing, then what its behavior reveals — and where they diverge. Close with 3–5 takeaways for the user's own positioning: where the competitor is exposed, where it is strong and should be avoided, and what move it enables or forces for the user.

---

## False-Positive Prevention

1. **Marketing-as-analysis.** Repeating the competitor's homepage claims as findings. Anchor every claim to an independent signal and your inference.
2. **Inference-as-fact.** Stating "they're moving upmarket" without the signal that led there. Always show observation → inference.
3. **Claimed-equals-actual.** Accepting the stated value prop without checking the product and what customers actually buy. The gap is the insight.
4. **Invented economics.** Fabricating CAC/LTV/margins. Estimate from sales motion and pricing signals, and label as estimates with confidence.
5. **Static snapshot.** Tearing down today's website with no recent-moves analysis, missing the trajectory.
6. **Admiration drift.** Producing a flattering profile with no takeaways for the user. The output is for the user's moves, not a fan page.
7. **Single-signal overreach.** Building a strong conclusion on one data point (one job posting, one tweet). Corroborate before asserting; flag thin reads.
8. **Stated-strategy credulity.** Believing the public strategy narrative when hiring and spend reveal a different one. Reconcile the two.
9. **Generic takeaways.** "We should differentiate" — vague. Takeaways name the specific exposure, the specific move, and the specific positioning.
10. **Confidence flattening.** Presenting low-confidence inferences with the same certainty as observed facts. Mark confidence.

---

## Output Format

```
# COMPETITOR TEARDOWN — [competitor]
Vantage (your product): [...] | Decision this informs: [...]
Recency window: [...]

## Product
| Dimension | Observation | Inference | Confidence |
|-----------|-------------|-----------|------------|
| Features  | [...]       | [...]     | [...]      |
| UX / performance | [...] | [...]    | [...]      |
| Pricing structure | [...] | what it reveals about target | [...] |

## Positioning
- Claimed value prop: "[...]"
- Actual value prop (product + customer behavior): [...]
- Real target customer: [...] (vs. stated: [...])

## Distribution
- Channels: [self-serve / sales-led / PLG / partnerships]
- Paid vs. organic: [...]
- Key partnerships: [...]
- Dominant motion (inferred) + cost signal: [...]

## Unit-economics signals (estimates)
- Sales motion / ACV band: [...]
- Free tier / expansion / discounting: [...]
- Efficiency read: [efficient / burn-heavy] | confidence: [...]

## Team
- Key hires (and what they signal): [...]
- Departures: [...]
- Hiring shape (next-move signal): [...]
- Leadership statements: [...]

## Funding / runway
- Last raise / total / investors: [...]
- Runway signals: [...]
- Pressure level (inferred): [...]

## Recent moves ([window])
| Move | Date | Implied strategic intent |
|------|------|--------------------------|
| [...]| [...]| [...]                    |

## Stated vs. revealed strategy
- Stated: [...]
- Revealed (by hiring / pricing / roadmap / spend): [...]
- Divergence: [...]

## Strategic takeaways for [your product]
1. [Exposure / move / positioning — specific]
2. [...]
3. [...]
(4–5 as warranted)
```

---

## Verification

- [ ] All sections covered: product, positioning, distribution, economics, team, funding, recent moves, stated vs. revealed.
- [ ] Observation distinguished from inference throughout.
- [ ] Claimed value prop separated from actual value prop.
- [ ] Unit economics estimated from signals and labeled as estimates with confidence.
- [ ] Recent moves tracked with implied intent.
- [ ] Stated vs. revealed strategy reconciled.
- [ ] 3–5 specific strategic takeaways for the user's positioning.
- [ ] Inferences marked with confidence; thin reads flagged.
- [ ] No marketing restated as analysis.
- [ ] No invented economics.
- [ ] Takeaways are specific, not generic.
