---
title: "Portfolio Construction Review — Concentration, Factor Tilt, Correlation, Sizing Discipline"
category: finance/investing-research
description: "Review a portfolio for hidden concentration, unintended factor and sector tilts, correlation clustering that defeats diversification, and consistency between position sizes and stated conviction — with quantified flags and rebalancing options."
techniques:
  - RT-06
  - RT-02
  - NE-11
  - DS-06
  - QA-02
difficulty: advanced
tags:
  - portfolio-construction
  - concentration
  - factor-tilt
  - correlation
  - diversification
  - risk-budget
updated: "2026-06-08"
related_prompts:
  - domain-finance/investing-research/finance_position_sizing_framework.md
  - domain-finance/risk-management/finance_portfolio_risk_review.md
  - domain-finance/investing-research/finance_investment_thesis_builder.md
  - domain-finance/field_guide.md
---

*For informational purposes only. Not financial, investment, or tax advice.*

## Objective

Review a portfolio as a whole — not name by name — to surface the risks that only appear at the aggregate level: hidden concentration (single name, sector, factor, or shared driver), unintended factor and style tilts, correlation clustering that makes a "diversified" book behave like one bet, and mismatches between position size and stated conviction. The output quantifies each issue, ranks it by severity, and offers rebalancing options without prescribing a single "right" portfolio.

## When to Use

- Periodic (monthly/quarterly) portfolio health check
- After adding several correlated positions that individually seemed fine
- Diagnosing why the book moves more (or less) than expected on certain days
- Pre-committing a risk budget and checking the current book against it
- Reviewing a concentrated book where a few names dominate the risk

## Inputs / Context Required

**Holdings**
- Position list: name, ticker, weight (% of portfolio), and the thesis conviction (High/Med/Low) for each
- Sector / industry classification per name; geography if relevant
- Long/short designation and gross/net exposure if applicable

**Risk descriptors**
- Factor exposures if available (value/growth, size, momentum, quality, beta) — or sectors as a proxy
- Pairwise correlations or shared-driver notes (same end market, same commodity, same rate sensitivity)
- Liquidity per name (days-to-exit) if available

**Mandate & limits**
- Stated risk budget, per-name and per-sector caps, target net/gross exposure
- Benchmark, if the book is measured against one
- Any concentration or factor constraints the mandate imposes

## Constraints

### Must
- Compute concentration quantitatively (top-N weight, Herfindahl-Hirschman Index) (NE-11).
- Detect tilts across sector, factor/style, and shared-driver dimensions (RT-02).
- Assess correlation clustering: identify groups of positions that are effectively one bet (RT-06).
- Check sizing discipline: do position sizes track stated conviction, or do low-conviction names carry high weight (and vice versa)?
- Rank flags by severity and quantify each (DS-06).
- Stress the book against a shared-driver shock (QA-02).

### Must Not
- Invent correlations, factor loadings, or benchmark weights. Mark `[ASSUMED]`/`[NOT PROVIDED]`.
- Prescribe a single optimal portfolio; offer options with tradeoffs.
- Treat low pairwise correlation as safety when positions share a latent driver (correlations rise in stress).
- Confuse name-count diversification with risk diversification.

## Instructions

1. **Measure concentration (NE-11).**
```
Top-5 weight = Σ (five largest position weights)
HHI = Σ (weight_i)^2     (range: 1/N for equal-weight → 1 for a single name)
Effective number of positions ≈ 1 / HHI
```
   Compare to per-name caps and the mandate.

2. **Map tilts (RT-02).** Aggregate weights by sector, then by factor/style (using loadings if provided, sectors as a proxy if not). Compare to the benchmark or to a neutral baseline. Flag unintended tilts (e.g., a "diversified" book that is 60% long-duration growth).

3. **Cluster by correlation and shared drivers (RT-06).** Group positions that share a latent driver — same end market, commodity, interest-rate sensitivity, or customer. Treat each cluster as a single risk unit:
```
Cluster weight = Σ weights in the cluster
   A book of 20 names with three names = 50% in one rate-sensitive cluster is effectively concentrated.
```

4. **Check sizing discipline.** Cross-tabulate position weight against stated conviction. Flag inversions (large low-conviction, small high-conviction) and concentration that exceeds what the sizing framework would justify.

5. **Stress-test a shared-driver shock (QA-02).** Apply a hypothetical shock to the dominant cluster/factor and estimate the book impact, noting that correlations tend to converge toward 1 in stress.

6. **Rank flags by severity (DS-06).** List the top issues (concentration / tilt / cluster / sizing) Critical → Watch, each quantified.

7. **Offer rebalancing options.** For each major flag, give 1–2 options (trim, hedge, diversify the cluster, resize to conviction) with the tradeoff — never a single mandate.

## Output Format

```
## PORTFOLIO REVIEW: [Book name] | [# positions] | Net/Gross: [ ] | As of [date]
```

### Concentration
```
Top-5 weight = [%]
HHI = [ ]   → Effective # positions ≈ 1/HHI = [ ]
Largest position = [%] vs. per-name cap [%]
```

### Tilt Map
| Dimension | Largest exposures | Weight | vs. benchmark/neutral | Flag |
|---|---|---|---|---|
| Sector | | | | |
| Factor / style | | | | |
| Geography | | | | |

### Correlation Clusters
| Cluster (shared driver) | Members | Cluster weight | Note |
|---|---|---|---|

### Sizing Discipline
| Position | Weight | Conviction | Aligned? |
|---|---|---|---|
- **Inversions flagged:** [large low-conviction / small high-conviction names]

### Shared-Driver Stress
| Shock | Affected cluster | Est. book impact | Note (correlations → 1 in stress) |
|---|---|---|---|

### Severity-Ranked Flags
| Priority | Issue | Quantified | Rebalancing options (with tradeoff) |
|---|---|---|---|
| Critical | | | |
| Elevated | | | |
| Watch | | | |

## Verification

- [ ] Concentration is quantified (top-N, HHI, effective # of positions).
- [ ] Sector, factor/style, and geography tilts are mapped vs. a benchmark or neutral baseline.
- [ ] Correlation/shared-driver clusters are identified and weighted as single risk units.
- [ ] Position sizes are cross-checked against stated conviction; inversions flagged.
- [ ] A shared-driver shock is stressed, noting correlation convergence in stress.
- [ ] Flags are ranked by severity and quantified.
- [ ] Rebalancing options include tradeoffs; no single portfolio is prescribed.
- [ ] No invented correlations/loadings/benchmark weights; gaps `[ASSUMED]`/`[NOT PROVIDED]`.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Treating name count as diversification | HHI and shared-driver clustering measure true diversification, not position count |
| Trusting low pairwise correlation | Stress test assumes correlations rise toward 1; latent shared drivers surfaced |
| Missing concentration hidden across names | Cluster weights aggregate same-driver names into one risk unit |
| Prescribing a single "correct" book | Rebalancing presented as options with tradeoffs |
| Inventing factor loadings or benchmark weights | Mark `[NOT PROVIDED]`; sectors used as a proxy with the caveat stated |
| Ignoring sizing/conviction mismatch | Sizing-discipline cross-tab flags inversions explicitly |
| Recency bias from recent calm | Stress scenario is mandatory; calm-period correlations not assumed to persist |
