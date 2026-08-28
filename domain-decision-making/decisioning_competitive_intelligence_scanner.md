---
title: "Competitive Intelligence Scanner (Decision-Feeding)"
category: decision-making
description: "Run a structured scan of a competitive landscape that feeds a single specified decision rather than producing a research dump. Output: a named-competitor inventory, claimed differentiation per competitor, observable gaps you can exploit, signals to monitor, and a one-paragraph 'what this changes' for the named decision."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-02
  - DS-02
  - DS-06
  - QA-01
  - QA-02
difficulty: intermediate
tags:
  - decision-making
  - competitive-intelligence
  - market-scanning
  - decision-input
  - signals
updated: "2026-04-26"
related_prompts:
  - domain-decision-making/decisioning_comprehensive_rapid_tradeoff_analyzer.md
  - domain-software-engineering/analysis/business/competitive_positioning_map.md
  - domain-software-engineering/analysis/business/blue_ocean_strategy_analysis.md
  - domain-business-strategy/research/research_competitive_landscape.md
---

# Competitive Intelligence Scanner (Decision-Feeding)

**Objective:** Produce a competitive scan that is shaped by, and ends in, a single named decision the user is about to make. The output is a tight inventory — named competitors, what each *claims* to do differently, what each *actually* does (observable behavior), the gaps the user can exploit, the signals worth monitoring, and a one-paragraph "what this changes about the decision." It is not a market-research dossier and not a positioning map; it is the briefing document a decision-maker reads in the 30 minutes before a decision.

**When to Use:**
- A specific decision is up: pricing, positioning, feature scope, channel choice, hire, funding round, partnership.
- The user already knows roughly who the competitors are and needs the scan to *change or confirm* a decision they're leaning toward.
- Periodic landscape refresh tied to a planning cycle that ends in concrete decisions.

**When NOT to use:**
- The user has no specific decision in view. Use a general competitive landscape research prompt (`research_competitive_landscape.md`).
- The user wants a 2x2 visual positioning map. Use `competitive_positioning_map.md`.
- The user is exploring blue-ocean reframing. Use `blue_ocean_strategy_analysis.md`.
- The user wants a deep-dive on a single competitor. Use `research_company_deep_dive.md`.

**Audience:** Founders, product leads, marketing leads, strategy and corp-dev partners, anyone who must make a decision under time pressure with imperfect competitive information.

---

## Inputs / Context

1. **The decision in scope.** One sentence: what choice is being made, by when, and by whom. Example: "By next Friday, we will choose whether to ship a free tier or stay paid-only."
2. **Working hypothesis.** The user's current lean. The scan will test it.
3. **Competitor list.** 3–8 named competitors. If the user lists only one or two, prompt for at least 3. Include adjacent and substitute competitors (a spreadsheet can be a competitor to a CRM).
4. **What is observable.** Sources the user has access to: pricing pages, public reviews, sales-call notes, win/loss notes, customer-mentioned alternatives, public filings, job postings, conference talks, GitHub activity, support forums.
5. **Time available for the scan.** 30 minutes, half-day, week. Calibrates depth.
6. **Confidentiality constraint.** Anything excluded from public output (e.g., a customer or partner name).

If the decision in scope is missing, **stop**. The whole prompt's value is decision-shaped scanning. A generic "tell me about competitors" request goes to a different prompt.

---

## Constraints

### Must
- Tie every section back to the named decision. Each output bullet must answer "how does this change the decision?"
- For each competitor, separate **claimed differentiation** (what they say in marketing) from **observable behavior** (what they actually do — pricing, hiring, release cadence, what customers say).
- Identify gaps from the *intersection* of (a) what no competitor is doing and (b) what the user can credibly do. A gap nobody can fill is not a gap.
- Limit signals-to-monitor to 3–7 specific, observable signals with a check-cadence per signal.
- Conclude with a "what this changes" paragraph that takes a position: **confirm** the working hypothesis, **revise** it (state how), or **invalidate** it (state why).
- Tag every claim as `[evidence-based]` (cite the source) or `[inferred]` (state the inference).

### Must Not
- Produce a generic market overview untethered from the named decision.
- Treat absence of public information as absence of competitor activity.
- Assume claimed differentiation matches observable behavior. The whole exercise is about the gap between them.
- Recommend exploiting a gap the user has no credible right to win.
- Output more than 8 competitors — past 8, the scan loses focus and the decision blurs.
- Skip the "what this changes" paragraph. Without a position, the scan is a dump.

---

## Instructions

### Step 1 — Restate the decision and working hypothesis
Restate the decision in one sentence. Restate the working hypothesis. State what evidence would confirm it, revise it, or invalidate it.

### Step 2 — Build the competitor inventory
For each of the 3–8 competitors, produce a row with:
- **Competitor:** name.
- **Type:** direct / adjacent / substitute / aspirational.
- **Claimed differentiation:** in their words (one line, paraphrased).
- **Observable behavior:** what they actually do (pricing, segment served, release cadence, hiring focus, latest move). Tag each observation `[evidence-based]` with source or `[inferred]`.
- **Gap between claim and behavior:** if any.

### Step 3 — Map gaps the user can exploit
For each candidate gap, evaluate:
- **Is it a real gap?** (No competitor is filling it.)
- **Can the user credibly fill it?** (Capability, brand, distribution, capital match.)
- **Does it move the named decision?** (If exploiting this gap doesn't change what the user does next, it doesn't belong in this scan.)

Output 1–4 gaps that pass all three filters. Discard the rest.

### Step 4 — Signals to monitor
Pick 3–7 signals that, if observed in the next 30–90 days, would change the user's decision. Each signal has:
- What to watch (specific URL, channel, behavior).
- What change would be meaningful (the threshold).
- How often to check (cadence).
- Who owns the check.

### Step 5 — Adversarial pass
Ask three adversarial questions:
- "If a competitor I haven't named entered this space tomorrow, who would they be and what would they do?"
- "If my working hypothesis is wrong, what is the most likely actual answer?"
- "What would a smart competitor do *to me* in response to the decision I'm leaning toward?"

Surface answers in 2–3 sentences each. These often reorder gaps and signals.

### Step 6 — Position on the decision
Write a one-paragraph "what this changes." Take a position:
- **Confirm:** the working hypothesis stands; here's the strongest piece of evidence supporting it.
- **Revise:** the hypothesis needs adjustment; here's the specific revision and why.
- **Invalidate:** the hypothesis does not survive the scan; here's the alternative the evidence points to.

If the scan is genuinely inconclusive, say so explicitly and name the single piece of evidence that would resolve it.

---

## False-Positive Prevention

1. **Marketing copy as truth.** A competitor's website says they "lead the industry"; their hiring page says they're hiring three SDRs. The hiring page is the truth. Always weight observable behavior over claimed differentiation.
2. **Selection bias from loud competitors.** A competitor that markets aggressively is more visible but not necessarily more dangerous. Include quiet, fast-growing competitors even when they are harder to see.
3. **Gap fantasy.** A gap that exists because nobody can profitably serve it is not a gap. Apply the credibility filter.
4. **Adjacent-substitute blindness.** Most failed competitive scans missed the substitute (spreadsheet, manual process, in-house build). Always include at least one substitute.
5. **Signal noise.** "Monitor their Twitter" is not a signal. "If their pricing page changes the Pro tier from $X to anything ≥ $Y in the next 60 days, that's a signal" is.
6. **No-position cop-out.** A scan that ends in "interesting findings, more research needed" produces no decision. Force a position or name the single resolving piece of evidence.
7. **Confidence inflation.** Inferred observations are useful but should not be presented as evidence. Tagging is mandatory, not cosmetic.
8. **Recency over-weighting.** A competitor's last-quarter move can be over-weighted. Look for behavior patterns over 12+ months when possible.

---

## Output Format

```
# Competitive scan — [decision name] — [date]

**Decision in scope:** [one sentence]
**Working hypothesis:** [one sentence]
**Time horizon for decision:** [date]

## Competitor inventory

| Competitor | Type | Claimed differentiation | Observable behavior | Claim-vs-behavior gap |
|------------|------|--------------------------|----------------------|------------------------|
| [Name]     | direct/adjacent/substitute/aspirational | [paraphrase] | [observation] [evidence/inferred] | [gap] |

## Gaps the user can exploit

| Gap | Real gap? | User credibility to fill | Moves the decision? |
|-----|-----------|---------------------------|----------------------|
| [...] | yes/no   | high/med/low + reason     | yes/no + how         |

## Signals to monitor

| Signal | Watch where | Meaningful change | Cadence | Owner |
|--------|--------------|--------------------|---------|-------|
| [...]  | [...]        | [...]              | [...]   | [...] |

## Adversarial pass

- **Unnamed competitor:** [2–3 sentences]
- **If my hypothesis is wrong:** [2–3 sentences]
- **What a smart competitor does to me in response:** [2–3 sentences]

## What this changes

**Position:** confirm / revise / invalidate

[One paragraph naming the strongest piece of evidence and the resulting move on the decision. If revise, state the revision. If invalidate, state the alternative.]
```

---

## Verification

- [ ] The decision in scope is stated in one sentence and referenced in every section.
- [ ] Between 3 and 8 competitors are inventoried, with at least one substitute or adjacent.
- [ ] Each competitor row separates claimed differentiation from observable behavior, with `[evidence-based]` or `[inferred]` tags.
- [ ] Gaps have passed the real-gap, credibility, and decision-moving filters.
- [ ] Signals are specific, observable, and have thresholds, cadences, and owners.
- [ ] The adversarial pass produced three responses.
- [ ] The "what this changes" paragraph takes one of three positions: confirm, revise, or invalidate.
- [ ] If inconclusive, the single piece of resolving evidence is named.
