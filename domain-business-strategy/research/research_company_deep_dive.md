---
title: "Company Deep Dive"
category: business-strategy/research
description: "Conduct a comprehensive, source-cited analysis of a company — business model, market position, financials, recent developments, and risks — for sales prep, partnership, investment research, or competitive intelligence, with strict separation of fact, company claim, and inference."
techniques:
  - ST-01
  - RT-02
  - DS-02
  - RT-05
  - QA-01
difficulty: intermediate
tags:
  - research
  - company-analysis
  - competitive-intelligence
  - due-diligence
  - web-research
updated: "2026-06-07"
related_prompts:
  - domain-business-strategy/research/research_competitive_landscape.md
  - domain-business-strategy/research/research_industry_trends.md
  - domain-business-strategy/go-to-market/research_person_background.md
---

# Company Deep Dive

**Objective:** Produce a comprehensive, source-cited profile of a company — what they do, how they make money, where they sit in the market, their financial situation, recent developments, and risks — that cleanly separates verified fact, company claim, and the researcher's inference.

**When to use:**
- Sales prospecting and account preparation.
- Partnership or vendor evaluation.
- Early-stage investment research (initial, not formal DD).
- Competitive or acquisition-target intelligence.

**When NOT to use:**
- You need audited financials or legal due diligence — engage professionals, not a research prompt.
- The company is too small/private to have a verifiable public footprint (the result would be speculation).
- You need real-time market data — pull live sources directly.

**Audience:** Salespeople, BD/partnership leads, founders, analysts, and investors doing initial research.

---

## Inputs / Context

The user should supply (or the research should flag what is missing):

1. **Company name** (and website/ticker if known to disambiguate).
2. **Purpose** of the research (sales, partnership, investment, competitive) — this focuses depth.
3. **Available sources** the researcher can actually access (web, Crunchbase/PitchBook, LinkedIn, SEC filings, analyst reports).
4. **Recency window** (default: prioritize the past 12 months).
5. **Any known facts** the user already has, to anchor and avoid restating guesses.

---

## Constraints

### Must
- **Cite a source for every factual claim** (link + date). Never assert a fact without one.
- **Never invent** sources, figures, funding amounts, dates, quotes, customer names, or executives. If a data point can't be found, write "Not found" and say what was searched.
- Clearly separate **verified fact** vs. **company claim** (what they say about themselves) vs. **inference** (what the researcher concludes).
- Cover the standard dimensions: overview, business model, market position, financials, recent developments, risks.
- For financial figures, **always attach source and date**; if a figure is a range/estimate, label it as such.
- Flag any claim resting on a single unverified source with `[SINGLE SOURCE]`, and end with a **Confidence Assessment** (High/Medium/Low) with reasoning.
- If sources conflict, present both and note the discrepancy; prefer the more recent/authoritative.

### Must Not
- Speculate about private financials or present estimates as disclosed figures.
- Treat marketing copy or a company blog as a neutral third-party fact.
- Pad thin findings with generic boilerplate; absence of data is itself a finding.
- Present inference as established fact.

---

## Instructions

1. **Confirm the subject and purpose.** Disambiguate the company; note the research goal and recency window.
2. **Company overview.** What they do (plain language), founding year, HQ, stage, employee count and growth trend — each cited.
3. **Business model.** Revenue model, target customers, pricing (if public), key products — distinguish company claims from verified facts.
4. **Market position.** Named competitors, claimed differentiation (labeled as their claim), notable customers/case studies (cited), market opportunity only if a credible source states it.
5. **Financial situation.** Funding history, revenue (only if disclosed or credibly reported, with source/date), profitability indicators, recent financial news — `[SINGLE SOURCE]` where applicable.
6. **Recent developments.** Major announcements, launches, leadership changes, strategic shifts in the recency window, each cited and dated.
7. **Risks and red flags.** Layoffs, executive departures, negative coverage, competitive threats — sourced, with inference labeled.
8. **Compile sources and verify (verification step).** List all sources by section. Re-read: is every fact cited? Any invented figure or quote? Are claims, facts, and inference distinguished? Add the Confidence Assessment.

---

## False-Positive Prevention

❌ **DON'T:**
- State a revenue or funding figure without a source and date.
- Invent a customer name, investor, executive, or quote to fill a section.
- Repeat the company's marketing claim as an objective fact.
- Present a single-blog-post rumor as confirmed.
- Conclude "they're struggling" as fact when it's an inference from indirect signals.

✅ **DO:**
- Attach a dated source link to every factual claim; write "Not found" when you can't.
- Label each item as verified fact, company claim, or inference.
- Flag single-source claims with `[SINGLE SOURCE]` and note conflicts between sources.
- Acknowledge what couldn't be verified and suggest how to confirm it.
- Close with an honest Confidence Assessment and the data that would raise it.

---

## Output Format

```
# Company Deep Dive: [Company Name]
*Purpose: [...] | Recency window: [...] | Research date: [...]*

## Company Overview
- What they do: [...] — [source, date]
- Founded / HQ / stage: [...] — [source]
- Employees & trend: [...] — [source, date]

## Business Model
- Revenue model / customers / pricing / products: [...] (fact / company claim) — [source]

## Market Position
- Competitors: [...] — [source]
- Claimed differentiation: [...] (company claim)
- Notable customers: [...] — [source]

## Financial Situation
- Funding history: [...] — [source, date]
- Revenue / profitability: [...] — [source, date] [SINGLE SOURCE if applicable]
- Recent financial news: [...] — [source, date]

## Recent Developments (past [window])
- [Announcement / launch / leadership change] — [source, date]

## Risks & Red Flags
- [Signal] — [source]; (inference noted where applicable)

## Sources
- [Section] → [links]

## Confidence Assessment
- Overall: [High/Medium/Low] — [reasoning; key gaps; what would raise confidence]
- Not found / unverifiable: [list]
```

---

## Example Output

```
# Company Deep Dive: ExampleCo Inc. (placeholder)
*Purpose: partnership evaluation | Recency window: 12 months | Research date: 2026-06-07*

## Company Overview
- What they do: cloud-based logistics coordination for mid-market shippers — [examplecoco.example/about, 2026-05].
- Founded 2017, HQ Austin TX, growth-stage — [Crunchbase profile, accessed 2026-06].
- ~250 employees, up from ~180 a year ago — [LinkedIn company page, 2026-06] (LinkedIn counts are approximate).

## Business Model
- Revenue model: per-shipment SaaS + usage fees (company claim) — [examplecoco.example/pricing, 2026-06]; pricing page lists tiers but not enterprise rates.
- Target customers: mid-market retail and manufacturing shippers — [examplecoco.example, 2026-06].

## Market Position
- Competitors: CompetitorA, CompetitorB (placeholders) — [trade publication roundup, 2026-03].
- Claimed differentiation: "real-time multimodal tracking" (company claim) — [examplecoco.example/product].
- Notable customers: two named logos on their site (marketing material) — [examplecoco.example/customers].

## Financial Situation
- Funding: Series B, reported ~$40M led by [Investor X] — [TechPress article, 2025-11] [SINGLE SOURCE].
- Revenue: not disclosed; an analyst note estimates "8-figure ARR" — [Analyst blog, 2026-01] (estimate, not confirmed).
- Recent financial news: none found in the past 6 months — Not found.

## Recent Developments (past 12 months)
- Launched an EU data region — [examplecoco.example/blog, 2026-04].
- New VP of Sales hired — [LinkedIn post, 2026-02].

## Risks & Red Flags
- Glassdoor shows declining ratings over the past year (small sample, ~40 reviews) — [Glassdoor, 2026-06]; treat cautiously (inference: possible morale/scaling strain).
- Competitive pressure from CompetitorA's recent price cut — [trade publication, 2026-03].

## Sources
- Overview/business model → company site, Crunchbase, LinkedIn
- Financials → TechPress, Analyst blog
- Developments → company blog, LinkedIn
- Risks → Glassdoor, trade publication

## Confidence Assessment
- Overall: Medium — public footprint is reasonable, but funding rests on a single source and revenue is an unconfirmed estimate.
- Not found / unverifiable: confirmed revenue, current cash position, enterprise pricing.
- Would raise confidence: a second source on the Series B; any disclosed revenue; a recent independent analyst report.
```

---

## Verification

- [ ] Every factual claim has a dated source link; unfound data marked "Not found."
- [ ] No invented figures, funding amounts, quotes, customers, or executives.
- [ ] Verified fact, company claim, and inference are distinguished throughout.
- [ ] Financial figures carry source and date; estimates labeled as estimates.
- [ ] Single-source claims flagged `[SINGLE SOURCE]`; conflicts noted.
- [ ] All six dimensions covered (or absence noted as a finding).
- [ ] Confidence Assessment present with reasoning and gaps.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the task as a source-disciplined company profile separating fact, claim, and inference.
- **RT-02 (Multi-Dimensional Analysis Framework):** Covers overview, model, market, financials, developments, and risks.
- **DS-02 (Evidence-Based Decision Making):** Requires a cited, dated source for every factual claim and forbids fabrication.
- **RT-05 (Evidence-Based Reasoning):** Conclusions and risk signals must follow from sourced evidence, with inference labeled.
- **QA-01 (Self-Critique Triggers):** Final verification audits citations, fabrication, and the Confidence Assessment.

---

## Related Prompts

- `domain-business-strategy/research/research_competitive_landscape.md` — Compare this company against its direct competitors.
- `domain-business-strategy/research/research_industry_trends.md` — Place the company within its market's trends.
- `domain-business-strategy/go-to-market/research_person_background.md` — Profile a specific person at the company before a meeting.
