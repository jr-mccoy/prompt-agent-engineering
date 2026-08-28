---
title: "Market Size (TAM/SAM/SOM) — Rapid or Comprehensive Mode"
category: product-management/prompts
description: "Calculate Total / Serviceable / Obtainable market sizes using three independent methodologies (top-down, bottom-up, value-based) and triangulate. Runs in rapid mode (time-boxed, single-source-per-method) or comprehensive mode (multi-source, explicit sensitivity analysis)."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-02
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - product-management
  - market-sizing
  - tam-sam-som
  - business-strategy
  - estimation
updated: "2026-04-23"
related_prompts:
  - domain-product-management/prompts/product_create_prd.md
  - domain-business-strategy/research/research_competitive_landscape.md
  - domain-software-engineering/analysis/business/business_model_canvas_analysis.md
---

# Market Size (TAM/SAM/SOM) — Rapid or Comprehensive Mode

**Objective:** Produce a defensible TAM / SAM / SOM estimate for a product or feature using three independent methodologies (top-down, bottom-up, value-based). Triangulate them, surface where they disagree, and state the confidence range. Offer two modes: **rapid** (≈45 minutes, one source per method, directional answer) and **comprehensive** (multi-source per method, sensitivity analysis, board-ready).

**When to use:**
- A pitch, PRD, or business case requires a market size number you will be asked to defend.
- You already have a "number" but you don't know how it was derived and need to rebuild it.
- You want to stress-test a claim ("this is a $50B market") someone else has made.

**Do not use** for retrospective revenue accounting or investor returns modeling — those are different artifacts.

**Audience:** Product managers, founders, strategy leads, or investors. Assumes access to at least some public data (industry reports, company filings, census figures, pricing pages).

---

## Definitions

- **TAM (Total Addressable Market):** Revenue if *every* potential customer in the category bought from you at a reasonable price. Ceiling.
- **SAM (Serviceable Addressable Market):** Portion of TAM your product, geography, and go-to-market can actually reach today.
- **SOM (Serviceable Obtainable Market):** Realistic share of SAM you can capture in a defined window (typically 3–5 years). Floor for "is this worth building."

---

## Inputs / Context

Ask the user (or fill in):

1. **Mode.** `rapid` or `comprehensive`.
2. **Product / feature being sized.** One sentence.
3. **Target customer.** Role, company size, industry, geography. Specificity changes the answer by orders of magnitude.
4. **Pricing assumption.** Your expected ACV/ARPU or transaction revenue per customer per year. If unknown, mark as a range.
5. **Geography.** Global, region, country, state. Default to the most realistic first market.
6. **Time horizon for SOM.** Default: 3 years.
7. **Known data sources the user already has.** Industry reports, prior estimates, competitor disclosures.
8. **Constraints.** Regulatory limits, language/localization, distribution channels available.

If inputs 2, 3, or 4 are missing, **stop** and ask. Sizing without a target customer or pricing is theater.

---

## Methodology

### Method A — Top-Down
Start from a published industry total and narrow.

```
TAM_topdown = (Industry total revenue or spending in category) × (relevant slice %)
SAM_topdown = TAM_topdown × (geographic reach %) × (segment fit %)
```

Cite the industry source. If the source is more than 3 years old, flag it.

### Method B — Bottom-Up
Build from the customer count up.

```
TAM_bottomup = (# of target customers in world/region) × (annual spend per customer at your pricing)
SAM_bottomup = TAM_bottomup × (% reachable via your GTM today)
```

For the customer count: use census, company directories (e.g., SEC filings, government business registries, published statistical series). Name the source.

### Method C — Value-Based
Estimate the economic value created for a customer, then assume capture.

```
Value per customer per year = (cost or revenue moved by your product)
TAM_value = (# target customers) × (value per customer) × (capture rate assumption, typically 10–30%)
```

State the capture rate assumption explicitly. Anything above 30% requires justification (monopoly pricing power, legal mandate, etc.).

### Triangulation
Compare the three TAMs. If they disagree by more than 3× , something is wrong — check your customer-count or pricing assumption. Report the median as the headline number and the range as the confidence band.

### SOM
`SOM = SAM × (realistic share within time horizon)`. Realistic share benchmarks:
- Early-stage entrant, no network effects: 1–5% of SAM in 3 years.
- Known brand, direct sales motion: 5–15% in 3 years.
- Dominant incumbent launching adjacent product: 15–30% in 3 years.
- Above 30%: justify with a concrete mechanism (exclusivity, regulation, network effect).

---

## Constraints

### Must
- Use all three methods. A single-method answer is not acceptable even in rapid mode.
- Cite a named source for every input (industry total, customer count, price). "Estimated from experience" is only acceptable when labeled as an assumption with a plausibility note.
- Report the triangulated range, not a single point estimate, unless the three methods agree within 30%.
- Show the arithmetic. Every number must be reproducible from the inputs.
- Mark every assumption with a sensitivity note: "If assumption X is off by 50%, the answer moves by $Y."
- In **comprehensive mode**, run low / base / high sensitivity on the two most load-bearing assumptions and report the range.

### Must Not
- Use "the market is growing rapidly" as a substitute for a number.
- Apply a growth rate to pad TAM without citing the growth source.
- Report a point estimate (no range) as authoritative in rapid mode.
- Mix geographies without noting the mix.
- Use a 3+-year-old industry report as the only source in comprehensive mode. Flag or replace.
- Claim a capture rate above 30% without a concrete mechanism.

---

## Instructions

### Step 1 — Mode and scoping
Confirm the user's mode. If rapid, time-box the exercise to 45 minutes and commit to one source per method. If comprehensive, plan 2–4 hours and budget time for sensitivity analysis.

### Step 2 — Normalize the target customer
Rewrite the target customer into a countable unit. Examples: "small US law firms with 2–10 attorneys," "households in EU-27 with broadband and annual income > €40k," "engineering teams at SaaS companies with > 50 engineers." Imprecision here is the number-one driver of bad TAMs.

### Step 3 — Run all three methods
Build TAM_topdown, TAM_bottomup, TAM_value with explicit arithmetic. Cite every source.

### Step 4 — Triangulate
Compute median and range. If the spread is > 3×, name the load-bearing disagreement and resolve it (usually customer count or pricing).

### Step 5 — Compute SAM and SOM
Apply geographic and GTM filters for SAM. Apply capture-rate band for SOM. State the time horizon.

### Step 6 — Sensitivity (comprehensive mode only)
Pick the two highest-leverage assumptions. Run low / base / high. Report the resulting SOM range.

### Step 7 — Confidence statement
End with one paragraph: your confidence in the number and what would need to change to move it by >50%.

---

## False-Positive Prevention

1. **Don't mistake a feature category for a market.** "AI agents" is not a market; "AI customer support agents sold to SaaS companies in North America" might be.
2. **Don't multiply one large number by one guessed percentage and call it a market.** That is a top-down-only answer in disguise.
3. **Don't assume capture rates above 30% without a mechanism.** The planning fallacy is strongest here.
4. **Don't use revenue multiples from adjacent categories without saying so.** "Like Slack but for X" only sizes the market if the target customer base and pricing genuinely map.
5. **Don't confuse TAM growth with your growth.** A market growing 20%/yr does not mean your SOM grows 20%/yr.
6. **Don't publish a number without the arithmetic.** If the reviewer cannot reproduce it, you cannot defend it.
7. **Don't hide disagreement between methods.** If top-down says $2B and bottom-up says $200M, say so and investigate.

---

## Output Format

```
# Market size — [product/feature]

**Mode:** rapid / comprehensive
**Date:** [date]
**Target customer:** [countable definition]
**Geography:** [region]
**Time horizon for SOM:** [N years]
**Pricing assumption:** [ACV/ARPU with range]

## Headline
- TAM: $X [range $Y–$Z]
- SAM: $X [range]
- SOM: $X [range] over [N] years
- Confidence: low / medium / high — [one-sentence why]

## Method A — Top-Down
- Industry total: $X — source: [citation, year]
- Relevant slice: Y% — rationale: [why]
- Geographic reach: Z% — rationale: [why]
- **TAM_topdown:** $___

## Method B — Bottom-Up
- Target customer count: N — source: [citation, year]
- Annual spend per customer: $M — source/pricing basis: [citation]
- **TAM_bottomup:** $___

## Method C — Value-Based
- Value per customer per year: $V — mechanism: [cost saved / revenue moved]
- Capture rate: C% — justification: [why this band]
- **TAM_value:** $___

## Triangulation
- Median TAM: $___
- Range: $___ – $___ (spread: Nx)
- Disagreements: [where methods diverged and why]

## SAM
- Filters applied: [geography, language, channel]
- SAM: $___

## SOM
- Capture band: C% over [N] years
- Rationale for the band: [competitor benchmarks or mechanism]
- SOM: $___

## Sensitivity (comprehensive mode only)
| Assumption          | Low    | Base   | High   | SOM impact |
|---------------------|--------|--------|--------|------------|
| [e.g., ARPU]        | $X     | $Y     | $Z     | ±$W        |
| [e.g., cust count]  | N1     | N2     | N3     | ±$W        |

## Confidence statement
[One paragraph: what you believe, what would move the number by >50%, and what to sharpen next.]

## Sources
- [Full citations, with year and URL or publication]
```

---

## Verification

- [ ] Mode is stated.
- [ ] Target customer is a countable unit (not "small businesses" or "users").
- [ ] All three methods produced a TAM figure, each with a cited source.
- [ ] Triangulation is shown; range is reported.
- [ ] SAM and SOM filters and rationales are stated.
- [ ] In comprehensive mode, sensitivity table is present with two highest-leverage assumptions.
- [ ] No capture rate > 30% without a mechanism.
- [ ] Every assumption has a source or is marked as an assumption.
- [ ] Confidence statement names what would move the number by >50%.
- [ ] Arithmetic is reproducible — every published number traces to inputs.
