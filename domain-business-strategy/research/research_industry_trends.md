---
title: "Industry Trend Report"
category: business-strategy/research
description: "Research and synthesize the major trends shaping a market into a role-targeted, source-cited briefing — with executive summary, per-trend analysis, emerging signals, and contrarian takes, each trend backed by multiple independent sources."
techniques:
  - ST-01
  - RT-02
  - DS-02
  - RT-05
  - QA-01
difficulty: intermediate
tags:
  - research
  - industry-trends
  - market-research
  - strategic-planning
  - web-research
updated: "2026-06-07"
related_prompts:
  - domain-business-strategy/research/research_competitive_landscape.md
  - domain-business-strategy/research/research_company_deep_dive.md
  - domain-business-strategy/research/research_content_research.md
---

# Industry Trend Report

**Objective:** Research and summarize the major trends shaping a market into a role-targeted briefing — executive summary, per-trend analysis, emerging signals, and contrarian takes — where each trend is backed by multiple independent, dated sources and hype is distinguished from substance.

**When to use:**
- Annual or quarterly strategic planning.
- Board presentations or investment-thesis development.
- Staying current in a fast-moving market in a structured, actionable way.
- Market-entry or career-direction decisions.

**When NOT to use:**
- You need a numeric forecast or market sizing — use a dedicated quantitative prompt.
- You want one company's profile — use the company deep dive.
- You need the latest breaking news, not synthesized trends — go to live sources.

**Audience:** Executives, product managers, investors, strategists, and anyone planning around market direction.

---

## Inputs / Context

The user should supply (or the research should flag what is missing):

1. **Industry/market** to analyze.
2. **Your role/context** (CEO, PM, investor, etc.) — so the report prioritizes what's actionable for you.
3. **Recency window** (e.g., past 6/12/18 months).
4. **Number of trends** to cover (3–7 typical).
5. **Available sources** the researcher can reach (trade media, analyst reports, earnings calls, conference talks).

---

## Constraints

### Must
- Back **each trend with at least two independent sources**, all dated.
- **Never invent** trends, statistics, analyst quotes, or sources. If support is thin, say so or drop the trend.
- Distinguish **independent analysis from vendor marketing**, and note when a trend rests primarily on vendor hype.
- Prioritize trends a person in the **stated role can actually act on**; flag buzzword-heavy, low-substance items skeptically.
- Include **contrarian takes** and present both sides where experts disagree.
- Flag any trend whose sources are **older than the recency window** or thinner than required.

### Must Not
- Repackage a single vendor's marketing as an industry trend.
- Present already-played-out shifts as emerging.
- Assert a statistic or analyst claim without a dated source.
- Echo conventional wisdom without testing it against a contrarian view.

---

## Instructions

1. **Restate scope.** Market, your role, recency window, number of trends.
2. **Write the executive summary.** 3–5 bullets of the most important shifts; the single most important thing to know now.
3. **Analyze each trend.** Name (3–6 words), what's happening, why it matters for this role, who's leading (1–2 cited examples), what to watch as an accelerate/stall signal, and the key sources (≥2 independent).
4. **Identify emerging signals.** 2–3 things not yet mainstream but showing momentum, and why they may matter in 12–24 months.
5. **Add contrarian takes.** 1–2 well-sourced pushbacks on the consensus, with reasoning.
6. **List further reading.** A few specific reports/articles worth reading in full, each with a one-line why.
7. **Verify (verification step).** Re-read: does each trend have ≥2 dated, independent sources? Any vendor-marketing-only trend unflagged? Any invented stat/quote? Are stale-source trends flagged and contrarian views genuinely included?

---

## False-Positive Prevention

❌ **DON'T:**
- Promote a single vendor's product narrative to "industry trend."
- State adoption percentages or analyst projections without a dated source.
- Pass off a trend that already fully played out as still-emerging.
- Present consensus with no contrarian counterweight.
- Treat a trend with one source as established.

✅ **DO:**
- Require ≥2 independent, dated sources per trend; drop or flag those that fall short.
- Separate independent analysis from vendor marketing and label the difference.
- Prioritize action-relevant trends for the stated role.
- Include contrarian takes and note expert disagreement.
- Flag stale or thin sourcing and label inference vs. sourced fact.

---

## Output Format

```
# Industry Trend Report: [Industry/Market] — for a [Role]
*Recency window: [...] | Trends covered: [...]*

## Executive Summary
- [Shift] — [2–3 sentences]
- Most important right now: [...]

## Trend Analysis
### [Trend name]
- What's happening: [...]
- Why it matters (for a [role]): [...]
- Who's leading: [example 1] — [source]; [example 2] — [source]
- What to watch: [accelerate/stall indicator]
- Key sources (≥2 independent, dated): [...]

## Emerging Signals
- [Signal] — why it may matter in 12–24 months — [source]

## Contrarian Takes
- [Pushback on consensus] — reasoning — [source]

## Further Reading
- [Report/article] — why it's worth reading in full
```

---

## Example Output

```
# Industry Trend Report: B2B SaaS Tooling — for a Head of Product (placeholder)
*Recency window: 12 months | Trends covered: 4*

## Executive Summary
- Usage-based pricing is displacing pure per-seat models in mid-market SaaS (multiple independent sources).
- AI features are shifting from differentiators to table stakes; pricing for them is unsettled.
- Most important right now: re-examine your packaging before competitors reset buyer expectations on price.

## Trend Analysis
### Usage-Based Pricing Shift
- What's happening: more vendors blend seats with consumption metering.
- Why it matters (for a Head of Product): affects packaging, forecasting, and product instrumentation needs.
- Who's leading: [Vendor A, placeholder] — [trade publication, 2026-02]; [Vendor B, placeholder] — [analyst note, 2026-01].
- What to watch: whether enterprise buyers accept consumption unpredictability (procurement pushback = stall signal).
- Key sources: [trade publication, 2026-02]; [independent analyst report, 2026-01].

### AI Features as Table Stakes
- What's happening: AI assist features are becoming expected, not premium.
- Why it matters: erodes the ability to charge a premium for "AI" alone.
- Who's leading: [Vendor C, placeholder] bundling AI into base tiers — [their pricing page, 2026-04] (vendor source — corroborate).
- What to watch: whether buyers will pay a separate AI line item (independent survey, 2026-03).
- Key sources: [independent survey, 2026-03]; [analyst commentary, 2026-02]. (Vendor pricing page used only as corroboration.)

## Emerging Signals
- Agentic workflow features in early pilots — not mainstream, but several vendors signaling roadmaps — [conference keynote, 2026-05]. May matter in 12–24 months.

## Contrarian Takes
- A contrarian view holds usage-based pricing increases churn risk for budget-constrained buyers — [independent analyst, 2026-03]. Reasoning: unpredictable bills trigger renewal scrutiny.

## Further Reading
- [Independent analyst report on SaaS pricing, 2026-01] — the most rigorous data behind the pricing-shift trend.
```

---

## Verification

- [ ] Each trend backed by ≥2 independent, dated sources.
- [ ] Vendor marketing distinguished from independent analysis and labeled.
- [ ] No invented trends, statistics, quotes, or sources.
- [ ] Trends prioritized for the stated role's actionability.
- [ ] Contrarian takes included; expert disagreement noted.
- [ ] Stale or thin-sourced trends flagged.
- [ ] Inference separated from sourced fact.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the task as a role-targeted, multi-source trend briefing.
- **RT-02 (Multi-Dimensional Analysis Framework):** Structures each trend across what/why/who/watch and adds emerging and contrarian layers.
- **DS-02 (Evidence-Based Decision Making):** Requires ≥2 dated, independent sources per trend and forbids fabrication.
- **RT-05 (Evidence-Based Reasoning):** Trend significance follows from corroborated evidence, with hype flagged.
- **QA-01 (Self-Critique Triggers):** Final verification audits sourcing depth, vendor-marketing leakage, and contrarian balance.

---

## Related Prompts

- `domain-business-strategy/research/research_competitive_landscape.md` — Map the competitors moving within these trends.
- `domain-business-strategy/research/research_company_deep_dive.md` — Profile a specific player driving a trend.
- `domain-business-strategy/research/research_content_research.md` — Turn trend findings into sourced writing material.
