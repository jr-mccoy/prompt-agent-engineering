---
title: "Capital Raise Readiness Assessment — Debt or Equity Readiness, Gaps, and Remediation Plan"
category: finance/treasury-capital-markets
description: "Assess readiness for a debt or equity capital raise across financials, story, governance, diligence, and process — producing a scored gap list and a prioritized remediation plan."
techniques:
  - NE-11
  - QA-02
  - DS-02
  - QA-01
  - RT-03
difficulty: intermediate
tags:
  - capital-raise
  - readiness
  - due-diligence
  - equity
  - debt-financing
updated: "2026-06-08"
related_prompts:
  - domain-finance/treasury-capital-markets/finance_debt_issuance_analysis.md
  - domain-finance/treasury-capital-markets/finance_capital_structure_optimization.md
  - domain-finance/treasury-capital-markets/finance_bank_relationship_rfp_framework.md
  - domain-finance/field_guide.md
---

**Informational only — not financial, investment, or hedge-accounting advice.**

## Objective

Assess an organization's readiness to execute a capital raise — debt or equity — across the dimensions investors and lenders scrutinize (financials and forecast quality, equity/credit story, capital structure fit, governance, diligence preparedness, and process), produce a scored readiness assessment, and deliver a prioritized gap-remediation plan with owners and timing before approaching the market.

---

## When to Use

- Pre-raise self-assessment before launching a debt or equity process.
- Board/management decision on whether the company is "market-ready."
- Diagnosing why a prior raise stalled and what to fix.
- Comparing debt vs equity readiness to inform the financing path.
- **Do not use** to value the company, set raise size/price (route to valuation and `finance_debt_issuance_analysis.md`), or as a substitute for legal/securities counsel on a specific offering.

---

## Inputs / Context Required

```
<capital_raise_inputs>
Company:
Currency:                       [CCY]
Jurisdiction / likely venue:    [private placement, public, bank market — verify securities rules as of date]
Raise type under consideration: Debt | Equity | Either (assess both)
Target use of proceeds:
Indicative size / timing (if known):

FINANCIALS
- Audited/reviewed historicals available? (years, auditor):
- Quality of forecast model (driver-based? scenario-capable?):
- KPI/metrics package maturity:
- Revenue/EBITDA trajectory and predictability:

STORY / POSITIONING
- Equity story or credit story drafted?
- Comparable companies / precedent transactions identified?
- Differentiation / competitive moat articulated?

CAPITAL STRUCTURE
- Current leverage, coverage, maturity profile:
- Cap table cleanliness (for equity): option pool, prior rounds, preferences:
- Existing lender/investor relationships:

GOVERNANCE & DILIGENCE
- Board composition / independence:
- Data room readiness (legal, financial, commercial, tax):
- Material contracts, IP, litigation, related-party items:
- Internal controls / management depth (CFO, FP&A):

PROCESS
- Advisors engaged (banker, counsel, auditor)?
- Timeline expectations:
</capital_raise_inputs>
```

---

## Constraints

### Must
- Assess readiness across **defined dimensions** with a scored rubric (e.g., 1–5 per dimension), and produce an **overall readiness score**.
- Tailor criteria to the **raise type**: equity emphasizes story/cap table/growth; debt emphasizes cash flow stability/coverage/covenant capacity. If "either," assess both and recommend the path (RT-03 tradeoff).
- For each gap, state **severity**, **owner**, and **time-to-remediate**.
- Apply an **adversarial diligence pass (QA-02)**: surface the questions a skeptical investor/lender will ask and whether the company can answer them today.
- Quantify the credit/coverage readiness for a debt raise:
  - `Pro forma Net Debt/EBITDA`, `EBITDA/Interest`, debt capacity headroom.
- Trace each rating/score to evidence in the inputs; do not assert readiness without support.
- Flag jurisdiction/securities-law dependence; "verify offering rules and disclosure obligations with counsel as of [date]."

### Must Not
- Declare the company "ready" without evidence for each dimension.
- Invent diligence findings, comparable transactions, or investor appetite.
- Conflate equity and debt readiness criteria.
- Provide a securities-law conclusion (route to counsel).
- Present the readiness score without the underlying gap list.

---

## Instructions

1. **Confirm raise type and frame.** Set the assessment criteria to debt, equity, or both.

2. **Score the dimensions (rubric, NE-11).** Rate each 1–5 with evidence:
   - Financials & forecast quality
   - Story (equity story / credit story)
   - Capital-structure fit & cap-table cleanliness
   - Governance & management depth
   - Diligence/data-room readiness
   - Process & advisor readiness

3. **Compute debt-readiness metrics (if debt).**
   ```
   Pro forma Net Debt/EBITDA = (Debt + New Debt − Cash) / EBITDA
   EBITDA/Interest (pro forma) = EBITDA / (Existing + New Interest)
   Debt capacity headroom: cross-check vs finance_debt_capacity_sizing.md
   ```

4. **Assess equity-readiness specifics (if equity).** Cap-table cleanliness, dilution/option pool, prior-round preferences/overhang, growth narrative vs comps, KPI credibility.

5. **Adversarial diligence pass (QA-02).** List the top questions a skeptical counterparty asks (e.g., customer concentration, churn, covenant headroom under stress, related-party items, forecast credibility) and grade the company's current ability to answer each.

6. **Build the gap list (RT-03 prioritization).** For each gap: dimension, severity (High/Med/Low), owner, time-to-remediate, dependency. Distinguish **blockers** (must fix before launch) from **enhancers** (improve terms).

7. **Recommend the path (if "either").** Weigh debt vs equity on cost, dilution, flexibility, and current readiness; state which is more executable now and why.

8. **Timeline.** Map remediation items to a pre-launch timeline; identify the critical path.

9. **Bias check + verification (QA-01).** Named pitfall: optimism/overconfidence on readiness (insider familiarity masking gaps). Disconfirming check: would an external banker score it the same? Confirm each score has cited evidence and metrics arithmetic is correct.

---

## Output Format

```
## Capital Raise Readiness Assessment — [Company]
Raise type: [Debt / Equity / Either] | Currency: [CCY] | Prepared: [date] | Data: user-supplied
(All figures illustrative unless traced to an input; securities-law items routed to counsel)

### Overall Readiness: [X / 5] — [Not ready / Conditional / Market-ready]

| Dimension                    | Score (1–5) | Evidence / Gap |
|------------------------------|-------------|----------------|
| Financials & forecast        | 3           | Reviewed (not audited) historicals; driver model OK |
| Story (equity/credit)        | 2           | No drafted story; comps not assembled |
| Capital structure / cap table| 4           | Clean; modest leverage |
| Governance & mgmt depth      | 3           | CFO in seat; no FP&A bench |
| Diligence / data room        | 2           | No data room; material contracts unindexed |
| Process / advisors           | 2           | No banker/counsel engaged |

### Debt-Readiness Metrics (if debt; illustrative)
| Metric                     | Pro forma | Note |
|----------------------------|-----------|------|
| Net Debt/EBITDA            | 3.0x      | within capacity |
| EBITDA/Interest            | 3.8x      | adequate |
| Capacity headroom          | $50M      | vs. sizing analysis |

### Adversarial Diligence Pass
| Likely investor/lender question | Can answer today? | Gap |
|---------------------------------|-------------------|-----|
| Customer concentration / churn  | Partial           | Need cohort data |
| Covenant headroom under stress  | No                | Build stress case |
| Related-party transactions      | No                | Compile schedule |
| Forecast credibility vs history | Partial           | Back-test variance |

### Gap List & Remediation Plan
| Gap                        | Severity | Type     | Owner   | Time | Dependency |
|----------------------------|----------|----------|---------|------|------------|
| No drafted equity/credit story | High | Blocker  | CFO/IR  | 3 wk | comps first |
| Data room not built        | High     | Blocker  | Legal   | 4 wk | contract index |
| No FP&A bench / variance back-test | Med | Enhancer | Finance | 6 wk | — |
| Audited (not reviewed) financials | Med | Enhancer | Auditor | 8 wk | — |

### Path Recommendation (if "either")
Debt vs equity: [recommendation] — rationale: cost vs dilution vs flexibility vs current readiness.

### Pre-Launch Timeline (critical path)
[Sequenced milestones to "market-ready"]

**Disconfirming check:** Would an external banker score this the same? If insider familiarity is inflating any score, downgrade until evidence exists.
```

---

## Verification

- [ ] Each dimension scored 1–5 with cited evidence.
- [ ] Criteria tailored to raise type; both assessed if "either."
- [ ] Debt metrics (pro forma leverage/coverage) computed where relevant.
- [ ] Adversarial diligence questions listed with answer-readiness graded.
- [ ] Gap list includes severity, owner, time, and blocker/enhancer classification.
- [ ] Path recommendation reasoned on cost/dilution/flexibility/readiness.
- [ ] Securities-law items routed to counsel; jurisdiction flagged.
- [ ] Overconfidence disconfirming check applied.

---

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Declaring "ready" without evidence | Each score requires cited evidence; external-banker disconfirming check |
| Mixing equity and debt criteria | Tailor rubric to raise type; assess separately if both |
| Inventing investor appetite or comps | Use only supplied/identified data; no fabricated demand |
| Giving a securities-law conclusion | Route offering/disclosure questions to counsel |
| Score without gap list | Readiness score must be backed by the underlying gaps |
| Insider optimism inflating scores | Adversarial diligence pass + external-perspective check |
