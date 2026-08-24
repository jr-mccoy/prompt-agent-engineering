---
title: "Design a Multi-Tab Intelligence-Gathering Operation"
category: business-strategy/browser-automation
description: "Design a multi-tab intelligence-gathering operation — the kind where an agent (AI or scripted) opens several sources in parallel, extracts structured signal, synthesizes, and delivers a briefing — with source selection, schema, deduplication, citation, and rot-detection baked in."
techniques:
  - ST-01
  - ST-02
  - DS-01
  - RT-02
  - CM-02
  - QA-01
  - ST-03
difficulty: advanced
tags:
  - browser-automation
  - intelligence-gathering
  - multi-tab
  - research-agent
  - synthesis
updated: "2026-04-20"
related_prompts:
  - domain-business-strategy/browser-automation/browserauto_recording_blueprint.md
  - domain-business-strategy/browser-automation/browserauto_safety_check.md
  - domain-business-strategy/research/research_competitive_landscape.md
---

# Design a Multi-Tab Intelligence-Gathering Operation

**Objective:** Design an operation where an agent (AI agent with browser access, scripted headless browser, or a human following a structured process) opens multiple sources in parallel, extracts structured signal per source, deduplicates and synthesizes across sources, and delivers a briefing. The design specifies source selection, extraction schema, trust ranking, deduplication, citation, and rot-detection so the briefing is useful on day 1 and day 90.

**When to use:** Recurring competitive intelligence. Regulatory or policy monitoring. Pricing / market surveillance. Pipeline enrichment. Any operation where the value is in synthesized signal from 5–30 sources on a cadence, not a one-off research task.

**Audience:** Automation engineer, ops lead, or analyst designing the operation. The briefing consumer is a separate audience (exec, sales, strategy) — this design produces what they read, but is not read by them.

---

## Inputs Required

1. **The question the briefing answers.** One sentence, specific. "What did competitors announce this week in [segment]?" — not "competitive intelligence."
2. **The consumer.** Who reads the briefing and what they do with it.
3. **Cadence.** Daily / weekly / event-triggered.
4. **Source candidates.** The user's current best list of sources — sites, RSS feeds, company blogs, news outlets, regulatory portals, social channels. If fewer than 5, the operation is probably too narrow or too wide.
5. **Known failure modes of past intelligence efforts,** if any. Common ones: too much noise, same items cited repeatedly, source rot, missed something obvious in a source not on the list.
6. **Trust priors.** Any known biases, reliability gaps, or access limits of named sources.
7. **Legal / ToS constraints.** Which sources forbid automated access, require rate limits, or require authenticated access.

Refuse to design without input 1 (the question) and input 2 (the consumer). Intelligence operations without a specific question produce long, expensive briefings nobody reads.

---

## Instructions

### Step 1 — Tighten the question and the decision

Restate the question precisely, and name the decision the briefing supports. Examples:

- **Question:** "Which competitors launched new features touching [capability] this week?"
- **Decision supported:** "Whether our roadmap prioritization meeting on Thursday needs to react."

If no downstream decision exists, the operation is a read-for-entertainment, not an intelligence operation. Say so before continuing.

### Step 2 — Rank sources into tiers

Three tiers:
- **Tier 1 — Primary.** First-hand sources (company blogs, official filings, press releases, regulatory portals, product pages). Authoritative.
- **Tier 2 — Trusted aggregators / analysts.** Secondary sources with track records. Include the analyst bias explicitly.
- **Tier 3 — Signal sources.** Social, community, chatter. High noise, occasional first-to-know value.

For every source, assign a tier and note:
- Access method (public, authenticated, API, RSS, HTML scrape).
- Rate limit or ToS constraint.
- Rot risk: how often this source has changed layout in the past year.
- Expected signal volume per cadence (handful of items / dozens / hundreds).

### Step 3 — Define the extraction schema

The operation extracts structured items per source. Define the schema:
- **Item type** (announcement / launch / filing / hire / pricing change / quote / other).
- **Who** (entity involved).
- **What** (one line description).
- **When** (date of event, distinct from date fetched).
- **Source** (URL + tier).
- **Quote** (direct quote if available, for citation).
- **Confidence** (high / medium / low, based on source tier and corroboration).

Every item in the briefing uses this schema. Items not mapped to the schema are discarded or escalated.

### Step 4 — Deduplicate and rank

Across sources, the same event may appear multiple times. Design the dedup:
- **Matching rule.** How two items are determined to be the same event (entity + date + event-type + keyword overlap).
- **Merge rule.** The higher-tier source wins attribution; lower-tier sources become corroboration.
- **Corroboration boost.** Items that appear in multiple independent sources get a confidence uplift.

Then rank items for the briefing:
- **By relevance to the question** — items outside the question's scope are parked, not included.
- **By confidence** — high-confidence events rank above speculative ones.
- **By recency** — within a tier, newer events first.

### Step 5 — Synthesis rules

The briefing is not a list of raw items. Design the synthesis:
- **Grouping.** Cluster items by theme (by competitor, by capability, by event type — pick one axis based on the question).
- **Abstraction.** One paragraph per group: what happened across the group, what the group collectively suggests.
- **Named items.** The briefing names the top 3–5 individual items verbatim.
- **Signal-to-noise.** A threshold below which items are suppressed (low confidence + no corroboration + high-noise tier).

No synthesis without citation. Every claim traces back to at least one source.

### Step 6 — Rot detection

Multi-source operations rot silently. Design the rot signals:
- **Source-level:** an expected source produces zero items for N consecutive runs — flag (site may have changed, feed may be broken).
- **Volume anomaly:** total item count per run deviates by >3× from rolling baseline — flag (over-fetch, parser break, or real event).
- **Schema drop:** a field fails to populate in >20% of items from a source — flag (layout change).
- **Consumer signal:** the downstream reader stops acting on the briefing — the most important rot signal of all.

For each, name the automatic alert path.

### Step 7 — Failure modes and handling

Common failures and responses:
- **Source blocked or ToS updated.** Drop the source, notify the designer, do not silently skip in briefings.
- **Rate limit hit mid-run.** Retry with backoff; if exhausted, produce a partial briefing with a clear "incomplete" marker — don't publish as complete.
- **Scraped content is JavaScript-rendered.** Upgrade fetch strategy (headless browser) or drop the source.
- **The agent hallucinates synthesis.** For AI-driven synthesis: require every claim to include a citation from the retrieved items. No citation, no claim.

### Step 8 — Briefing format and consumer contract

Specify what the consumer receives:
- Format (email, Slack post, doc, dashboard).
- Length bounds (executive briefings usually 1 page; analyst briefings longer).
- Freshness stamp and confidence disclosure.
- Named items vs aggregates.
- Link-through to primary sources for every named item.

### Step 9 — Review cadence

Weekly or monthly review:
- Which items from last period actually mattered? (The feedback loop.)
- Which sources contributed useful items? Which didn't?
- What decision did the briefing actually drive?
- Is the question still the right question?

Intelligence operations that aren't reviewed drift into noise factories.

---

## Constraints

### Must
- Tighten the question to name a decision.
- Classify every source into a tier with access/rot/volume notes.
- Define an extraction schema every item maps to.
- Specify matching, merging, and ranking rules.
- Name at least 3 rot-detection signals.
- Require citations for every synthesis claim.
- Set a review cadence.

### Must Not
- Design an operation without a named decision it supports.
- Use sources whose ToS forbids automation without explicit permission.
- Allow AI synthesis without per-claim citation.
- Publish partial briefings marked "complete."
- Mix tiers silently — Tier 1 attribution must outweigh Tier 3.
- Skip the consumer-feedback loop. Briefings decay without it.

---

## False-Positive Prevention

1. **Don't design for breadth when the question needs depth.** 30 Tier-3 sources scanned shallowly usually produce worse briefings than 5 Tier-1 sources read carefully.
2. **Don't let an AI synthesizer invent attribution.** If the agent cannot cite a retrieved item, the claim does not appear in the briefing.
3. **Don't trust a source that doesn't rot.** Either the source is genuinely stable, or no one is watching.
4. **Don't confuse dedup with suppression.** Multiple sources reporting the same event is confirmation, not redundancy. Merge, don't drop.
5. **Don't skip the ToS / legal check.** Scraping a source in violation of its ToS is the organization's liability, not the agent's.
6. **If the downstream decision is not taken,** the briefing is producing work without creating value. Retire or redesign.

---

## Output Format

```
# Intelligence operation design — [name]

## Question and decision
- Question: [one sentence, specific]
- Decision supported: [what the reader does differently]
- Consumer: [named role]
- Cadence: [daily/weekly/event]

## Sources (by tier)
| Tier | Source | Access method | ToS / rate limit | Rot risk | Expected volume/run |
|------|--------|---------------|------------------|----------|---------------------|

## Extraction schema
[Fields: Item type, Who, What, When, Source, Quote, Confidence]

## Dedup / ranking rules
- Matching: [rule]
- Merging: [rule, tier precedence]
- Corroboration boost: [rule]
- Ranking: [relevance → confidence → recency]

## Synthesis rules
- Grouping axis: [by entity / capability / event type]
- Abstraction per group: [paragraph rule]
- Named items: [top N]
- Signal-to-noise threshold: [rule]
- Citation requirement: [every claim]

## Rot detection
- Signal: [what to watch] → alert to [where]

## Failure modes and handling
- [Failure] → [response]

## Briefing contract
- Format, length, freshness stamp, confidence disclosure, link-through requirements.

## Review cadence
- [Weekly / monthly] — evaluates: decision impact, source contribution, question relevance.
```

---

## Verification

- [ ] Question and named decision exist.
- [ ] Every source has tier, access, ToS, rot, volume attributes.
- [ ] Schema covers all required fields.
- [ ] Dedup and ranking rules are explicit.
- [ ] Synthesis rules require citation per claim.
- [ ] At least 3 rot-detection signals with alert paths.
- [ ] Failure modes mapped to responses.
- [ ] Review cadence includes consumer-feedback loop.
