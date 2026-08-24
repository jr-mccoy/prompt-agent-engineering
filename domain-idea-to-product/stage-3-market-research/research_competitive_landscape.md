---
title: "Competitive Landscape Analysis"
category: business-strategy/research
description: "Research direct competitors in a market and produce a structured, source-cited comparison table (CSV) for strategic planning — every row backed by a verifiable source URL, with unfound data marked rather than guessed."
techniques:
  - ST-01
  - RT-02
  - DS-02
  - RT-05
  - QA-02
difficulty: intermediate
tags:
  - research
  - competitive-analysis
  - market-research
  - benchmarking
  - web-research
updated: "2026-06-07"
related_prompts:
  - domain-business-strategy/research/research_company_deep_dive.md
  - domain-business-strategy/research/research_tool_comparison.md
  - domain-business-strategy/research/research_industry_trends.md
---

# Competitive Landscape Analysis

**Objective:** Research the direct competitors in a defined market and produce a structured, source-cited comparison (CSV) — covering positioning, size, funding, pricing, and differentiation — where every row is verifiable from a primary source and unfound data is marked, not invented.

**When to use:**
- Strategic planning, positioning, or market-entry decisions.
- Building a competitor table for an investor deck or board review.
- Establishing a shareable, maintainable competitive baseline for the team.

**When NOT to use:**
- You need a deep single-company profile — use the company deep dive prompt.
- You're comparing tools for a purchase decision — use the tool comparison prompt.
- The market has no clear direct competitors yet (the table would be padded with stretches).

**Audience:** Founders, product marketers, strategy/BD leads, and analysts.

---

## Inputs / Context

The user should supply (or the research should flag what is missing):

1. **Your company/product** and the **market/industry** to scope competitors against.
2. **Definition of "direct"**: same problem, same customer — to keep the set focused.
3. **Number of competitors** to include (5–15 typical), prioritized by market relevance.
4. **Available sources** the researcher can reach (official sites, LinkedIn, Crunchbase, reputable business press).
5. **Recency window** (default: prioritize the past 12 months).

---

## Constraints

### Must
- Restrict to **direct competitors** (same problem, same customer); exclude tangential players and state exclusions.
- **Cite a Primary Source URL for every row** that a reader can click to verify the key claims.
- Visit the **official pricing page** for each company; never guess pricing or rely on stale third-party data.
- **Never invent** company facts, figures, or sources. If a data point isn't found after checking multiple sources, write "Not found" and note what was searched.
- Flag any data point below ~90% confidence with `[VERIFY]`; on conflicts, use the most recent source and note the discrepancy.
- Use the exact column structure so the output is comparable and shareable.

### Must Not
- Use Wikipedia or user-generated content as a primary source for factual claims.
- Fill cells with plausible-sounding guesses instead of "Not found."
- Include companies serving a different primary market to pad the count.
- Present a single-source or outdated figure as confirmed.

---

## Instructions

1. **Scope the set.** Define the market and "direct" criteria; identify and rank competitors by relevance to the target count. State exclusions.
2. **Gather per competitor.** From official sources and reputable databases, collect each column field; visit the official pricing page for pricing.
3. **Record sources.** Capture a Primary Source URL per row plus any pricing URL.
4. **Mark uncertainty.** Use "Not found" for missing data (with a note on what was searched) and `[VERIFY]` for low-confidence cells.
5. **Resolve conflicts.** Prefer the most recent/authoritative source; note any conflict.
6. **Assemble the CSV.** Use the exact columns below.
7. **Verify (verification step).** Re-read: does every row have a working source URL? Any invented value? Any pricing not from the official page? Any guess that should be "Not found"? Confirm `[VERIFY]` flags.

---

## False-Positive Prevention

❌ **DON'T:**
- Enter a funding amount, employee range, or price you didn't source.
- Guess pricing from a third-party listicle instead of the official page.
- Include a company that serves a different customer just to reach the count.
- Treat a single uncorroborated source as confirmed.
- Leave low-confidence data unflagged.

✅ **DO:**
- Give every row a clickable Primary Source URL; visit official pricing pages.
- Write "Not found" (with search notes) rather than guessing.
- Flag uncertain cells with `[VERIFY]` and note source conflicts.
- Keep the set strictly to direct competitors and state exclusions.
- Distinguish a company's own claim (e.g., differentiator) from verified facts.

---

## Output Format

```
Competitive landscape — [Your Company/Product] in [Market]
Direct-competitor criteria: [same problem + same customer]; excluded: [list]

CSV columns (exact order):
1. Company Name
2. Website URL
3. Headquarters Location
4. Founded Year
5. Employee Count Range (1-10, 11-50, 51-200, 201-500, 500+)
6. Funding Status (Bootstrapped, Seed, Series A/B/C, Public, Unknown)
7. Total Funding Amount ("Not disclosed" if unavailable)
8. Primary Product/Service (≤15 words)
9. Target Customer (one sentence)
10. Pricing Model (Free, Freemium, Subscription, Usage-based, Enterprise/Contact Sales)
11. Starting Price (monthly, or "Contact sales")
12. Key Differentiator (their claim, one sentence)
13. Primary Source URL

Notes:
- "Not found" entries: [what was searched]
- [VERIFY] flags: [which cells, why]
- Source conflicts: [...]
```

---

## Example Output

```csv
Company Name,Website URL,HQ,Founded,Employees,Funding Status,Total Funding,Primary Product,Target Customer,Pricing Model,Starting Price,Key Differentiator (claim),Primary Source URL
CompetitorA (placeholder),competitora.example,San Francisco CA,2016,201-500,Series C,"$120M [VERIFY]",Workflow automation for ops teams,Mid-market operations teams,Subscription,$29/user/mo,"""Fastest setup in category""",https://competitora.example/pricing
CompetitorB (placeholder),competitorb.example,Remote,2019,51-200,Series A,Not disclosed,Lightweight task automation,SMB teams,Freemium,$0 (free tier); $15/user/mo,"""No-code first""",https://competitorb.example/pricing
CompetitorC (placeholder),competitorc.example,London UK,2014,500+,Public,Not disclosed,Enterprise process automation,Large enterprises,Enterprise/Contact Sales,Contact sales,"""Compliance-grade controls""",https://competitorc.example/product

Notes:
- "Not found": CompetitorB total funding — checked official site, Crunchbase, and one press article; no figure disclosed.
- [VERIFY]: CompetitorA total funding ($120M) — one press source dated 2025-09; not corroborated by Crunchbase.
- Source conflicts: CompetitorA founded year listed as 2015 on Crunchbase vs. 2016 on their site; used the company site (more authoritative), noted here.
- Excluded: GenericPlatformX — serves consumer market, not direct.
```

---

## Verification

- [ ] Only direct competitors included; exclusions stated.
- [ ] Every row has a working Primary Source URL.
- [ ] Pricing taken from official pricing pages, not third parties.
- [ ] Unfound data marked "Not found" with search notes — no guesses.
- [ ] Low-confidence cells flagged `[VERIFY]`; conflicts noted.
- [ ] No Wikipedia/UGC used as a primary factual source.
- [ ] Differentiator claims attributed to the company, not stated as fact.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the task as a source-verifiable, comparable competitor table.
- **RT-02 (Multi-Dimensional Analysis Framework):** Compares competitors across size, funding, pricing, audience, and differentiation.
- **DS-02 (Evidence-Based Decision Making):** Requires a primary source URL per row and forbids fabricated values.
- **RT-05 (Evidence-Based Reasoning):** Rankings and inclusion decisions follow from sourced relevance, not assumption.
- **QA-02 (Adversarial Thinking Prompts):** `[VERIFY]` flagging and conflict-checking pressure-test uncertain data before use.

---

## Related Prompts

- `domain-business-strategy/research/research_company_deep_dive.md` — Go deep on any single competitor in the table.
- `domain-business-strategy/research/research_tool_comparison.md` — Compare products for a purchase decision rather than market positioning.
- `domain-business-strategy/research/research_industry_trends.md` — Understand the trends reshaping this competitive set.
