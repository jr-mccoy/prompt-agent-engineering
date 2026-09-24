---
title: "Media Plan and Budget Allocation — Test Budget, Learning Phase, and Pacing From Your Own Numbers"
category: advertising/campaign
description: "Build a flight-level media plan from the advertiser's own economics: the break-even cost per acquisition, a test budget sized from that number and the cells to be read, an allocation across placements with a stated reason for each line, a learning-period hold that uses the platform's own current guidance rather than a remembered rule, a weekly pacing table, and pre-committed scale, hold, and kill rules. Uses no industry benchmark it cannot source — unknowns are marked [MEASURE] or [VERIFY]. Distinct from the paid-ads skill (channel choice, targeting, bidding, optimisation), workflow_marketing_campaign_brief_development (the brief and strategy-level budget split), and the ab-test-setup skill (statistical design)."
techniques:
  - DS-02
  - RT-05
  - QA-04
  - OC-03
difficulty: intermediate
tags:
  - advertising
  - media-planning
  - budget
  - paid-media
  - campaign
  - pacing
updated: "2026-09-24"
related_prompts:
  - domain-agentic-resources/skills/marketing/paid-ads/SKILL.md
  - domain-business-strategy/go-to-market/workflow_marketing_campaign_brief_development.md
  - domain-agentic-resources/skills/marketing/ab-test-setup/SKILL.md
---

# Media Plan and Budget Allocation

**Objective:** Produce a media plan a buyer can execute and a finance owner can
audit — every line of spend traceable to the advertiser's own numbers or to a
sourced figure, every decision rule written before the money is spent.

**When to Use:**
- A brief has a total budget and you need to turn it into lines, weeks, and rules.
- Last campaign was paused, scaled, or reshuffled on feel, and nobody can say why.
- You are about to test a new channel and need to know how much it takes to learn
  anything.

**When NOT to use:**
- You have not chosen channels, audiences, or bid strategy — `skills/marketing/paid-ads/`.
- You need the campaign brief itself — `domain-business-strategy/go-to-market/workflow_marketing_campaign_brief_development.md`.
- You need the sample size or significance rule for a creative test — `skills/marketing/ab-test-setup/`.
- You need attribution or tracking set up — `skills/marketing/analytics-tracking/`.

## Inputs / Context

1. **Total budget and flight dates.**
2. **Unit economics**: price or average order value, gross margin, and — if known —
   customer value over a period you trust. These produce the break-even CPA.
3. **Historical results you hold**: CPA, conversion rate, CPM by placement, with
   dates. If none, say so.
4. **Placements and cells** from the copy matrix and channel choice.
5. **The platform's current guidance** on learning periods and budget changes, if
   the operator has read it (source and date), or `[VERIFY]`.
6. **Risk tolerance**: the maximum the advertiser will spend to learn nothing.

## Method

1. **Compute break-even CPA from the advertiser's numbers.** Show the arithmetic.
   If customer value is uncertain, compute on first-order margin and state that the
   plan is conservative. Never substitute an "industry average" CPA.
2. **Label every input by provenance.** `[OWN DATA, date]`, `[SOURCED: url, date]`,
   `[ASSUMPTION — why]`, or `[MEASURE]`. An assumption drives a line only if it is
   named and has a test that would replace it.
3. **Size the test budget.** For each cell to be read, estimate what reaching a
   readable number of conversions costs at the break-even CPA; sum it. If the sum
   exceeds the budget, cut cells (feed back to the copy matrix), not the read.
4. **Allocate the rest.** Proven placements get the remainder, each line with a
   written reason. A line with no reason is removed.
5. **Handle the learning period from source.** Record what the platform's current
   documentation says about learning periods and budget changes, with source and
   date — or mark `[VERIFY current platform guidance]`. Plan no edits inside it
   except kill-rule triggers.
6. **Build the pacing table.** Week by week: planned spend per line, cumulative,
   and the acceptable variance band before a human looks.
7. **Pre-commit the rules.** Scale (what result, how much, how often), hold, and
   kill (the spend-with-no-result ceiling per cell, tied to break-even CPA).
8. **Name the reporting cadence and owner.**

## Output Format

```
# Media plan — [campaign]   Flight: [dates]   Total: [amount]

## Economics
| Input | Value | Provenance |
|---|---|---|
Break-even CPA = [formula with numbers] = [value]

## Allocation
| Line | Placement | Purpose (test/proven) | Budget | Reason |
|---|---|---|---|---|
Test budget sizing: [cells × conversions to read × break-even CPA = ...]

## Learning period
Platform guidance: [summary] — Source: [url/screen], checked [date]   or [VERIFY current platform guidance]
No planned edits: [dates]

## Pacing
| Week | Line | Planned | Cumulative | Variance band |
|---|---|---|---|---|

## Decision rules
| Rule | Trigger | Action | Owner |
|---|---|---|---|
| Kill | [...] | [...] | [...] |
| Hold | [...] | [...] | [...] |
| Scale | [...] | [...] | [...] |

## Assumptions to replace
| Assumption | Replaced by | When |
|---|---|---|
```

## Verification

- [ ] Break-even CPA arithmetic is shown and uses only the advertiser's figures.
- [ ] Every input carries a provenance label.
- [ ] Test budget is sized from cells × readable conversions × break-even CPA.
- [ ] Every allocation line has a reason.
- [ ] Learning-period handling cites a dated source or is marked `[VERIFY]`.
- [ ] Kill, hold, and scale rules are written with numeric triggers before launch.
- [ ] Pacing weeks sum to the total budget.

## False-Positive Prevention

1. **No borrowed benchmarks.** "Average CPC in this industry is…" without a source
   and date is removed. Your own history, or `[MEASURE]`.
2. **Do not state learning-phase rules from memory.** How many conversions, how
   long, and what resets it are platform- and date-specific — cite or verify.
3. **A 70/30 split is not a reason.** Fixed ratios from habit are replaced by the
   test-budget arithmetic.
4. **Cut cells, not the read.** Underfunding every cell produces results that look
   like findings and are noise.
5. **Rules written after launch are rationalisations.** Pre-commit them.
6. **ROAS is not margin.** Break-even uses gross margin, not revenue.
7. **Do not promise outcomes.** The plan states what it will learn and what it will
   stop, not what it will return.

## Example

**Input:** Meal-kit brand. Budget 20,000 over 6 weeks. First-box price 60 after the
half-price offer; gross margin on first box 12 (own data, finance, 2026-09); customer
value uncertain. History: prior social feed CPA 38 (own data, Q2). Copy matrix: 4
test cells. Readable conversions per cell: per ab-test-setup, taken as 25 for planning
`[ASSUMPTION — replace with ab-test-setup output]`.

```
## Economics
| First-box margin | 12 | OWN DATA, finance 2026-09 |
| Customer value (90 days) | [MEASURE] | not trusted yet |
Break-even CPA (first-order) = 12. Conservative: ignores repeat orders.

## Allocation
| L1 | Social feed | Test (C1–C4) | 3,800 | 4 cells × 25 × 38 historic CPA |
| L2 | Social feed | Proven retargeting | 9,000 | Prior Q2 CPA 38 — above break-even; see note |
| L3 | Short video | Held | 0 | Flight 2 (copy matrix kill list) |
| Reserve | — | — | 7,200 | Released only by Scale rule |

## Learning period
[VERIFY current platform guidance] — no planned edits weeks 1–2.

## Decision rules
| Kill | Cell spends 2× break-even (24) with 0 conversions | Pause cell | Buyer |
| Scale | Cell CPA ≤ 12 over ≥ 25 conversions | Release reserve in steps per verified guidance | Buyer + finance |
```

**The plan's own finding:** historic CPA (38) is over three times first-order
break-even (12). Either customer value justifies it — which is `[MEASURE]` — or the
proven line is losing money. The plan routes 7,200 to reserve until the 90-day value
is measured, rather than scaling a line that may not pay.

## Techniques Used

- **DS-02 Metric Specification** — break-even CPA and numeric kill/scale triggers.
- **RT-05 Evidence-Based Reasoning** — every line traced to own data or a source.
- **QA-04 Uncertainty Acknowledgment** — provenance labels and `[MEASURE]` / `[VERIFY]`.
- **OC-03 Markdown Table Specification** — allocation, pacing, and rules tables.

## Related Prompts

- `domain-agentic-resources/skills/marketing/paid-ads/` — channel, targeting, bidding.
- `domain-business-strategy/go-to-market/workflow_marketing_campaign_brief_development.md` — the brief upstream.
- `adcampaign_copy_variant_matrix.md` — the cells this plan funds.
