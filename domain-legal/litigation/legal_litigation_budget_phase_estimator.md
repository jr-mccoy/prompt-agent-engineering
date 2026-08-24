---
title: "Phased Litigation Budget Estimator"
category: legal/litigation
description: "Build a phased litigation budget by stage (pleading, written discovery, depositions, dispositive motions, expert work, trial, appeal) with hours, rates, expenses, assumptions, and contingency."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: intermediate
tags:
  - legal
  - litigation
  - budget
  - matter-management
  - legal-ops
updated: "2026-05-11"
related_prompts:
  - domain-legal/litigation/legal_case_strategy_assessment.md
  - domain-legal/litigation/legal_settlement_value_range_analysis.md
  - domain-legal/in-house-legalops/legal_legal_spend_anomaly_analyzer.md
---

**Purpose:** Produce a phased budget that a partner can defend to a GC or a GC can defend to a CFO — broken into named stages, with hours by timekeeper, rates, expenses, and explicit assumptions.

**When to use:** New matter intake, annual matter review, settlement-vs-fight cost analysis, outside-counsel-guideline compliance, response to GC budget request.

---

## Your Input

- **Matter type:** [Commercial, employment, IP, securities, etc.]
- **Jurisdiction / forum:** [Federal/state, complexity tier of forum]
- **Posture:** [Plaintiff / defendant; bet-the-company / commercial / routine]
- **Case profile:**
  - Number of parties, claims, defenses
  - Document volume estimate (GB or doc count)
  - Number of fact witnesses, custodians
  - Expert disciplines anticipated
  - Likely dispositive-motion practice
  - Trial length estimate
- **Staffing model:** [Partner / counsel / senior associate / mid-level / junior / paralegal blended rates]
- **Rate sheet:** [Hourly rates by timekeeper, or AFA structure]
- **Expense assumptions:** [E-discovery platform, hosting, experts, depositions, travel, mediation]
- **Probability assumptions:** [P(MTD granted), P(MSJ resolves case), P(trial), P(appeal)]
- **Contingency posture:** [Add % buffer? Stage-specific contingency?]

---

## Constraints

**Must:**
- Break the budget into **named stages** with start/end events.
- Provide a **most-likely scenario** and an **expected-value scenario** (probability-weighted across paths).
- Show **hours per timekeeper per stage**, not just a total.
- Separate **fees** from **expenses** in every table.
- State every **assumption** that drives a number (e.g., "10 custodians × 25 GB × $X/GB").
- Include a **contingency line** with explicit basis (e.g., "15% on discovery; 25% on trial").
- Identify the **decision points** where the budget should be revisited.

**Must Not:**
- Produce a single bottom-line number without staged breakdown.
- Invent rates if not supplied — use placeholders (`[RATE: partner]`).
- Treat e-discovery hosting as a one-time cost (it accrues monthly).
- Omit expert costs from the discovery and trial stages.
- Use the same hour assumptions for plaintiff and defendant posture (asymmetric work).

---

## Instructions

1. **Validate inputs.** If staffing model, rates, or case profile are missing, flag them and proceed with placeholders.
2. **Map the case to stages.** Default federal civil stages: Pre-suit / Pleadings → Initial Disclosures & Written Discovery → Document Review & Production → Depositions → Expert Work → Dispositive Motions → Pretrial → Trial → Post-Trial / Appeal. Adjust for state procedure or transactional litigation (e.g., arbitration phases).
3. **For each stage, compute:**
   - Hours per timekeeper × rate = fees
   - Expenses (itemized)
   - Stage subtotal
4. **Build the most-likely scenario** assuming linear progression to trial (or to the most likely off-ramp).
5. **Build the expected-value scenario** by applying probability weights across decision branches:
   - EV = Σ (path cost × P(path))
6. **Identify decision points** — where the case "branches" (post-MTD, post-class-cert, post-summary-judgment, mediation windows). Budget should be re-baselined at each.
7. **Apply contingency** to high-variance stages.
8. **Output a one-page executive summary** plus the detailed schedule.

---

## Output Format

```markdown
# LITIGATION BUDGET — {Matter Name}

## Executive Summary
- **Most-likely total (through trial):** ${X}
- **Expected value (probability-weighted):** ${Y}
- **Largest cost drivers:** {top 3 stages}
- **Key assumptions:** {3–5 bullets}
- **Re-baseline triggers:** {decision points}

## Phased Schedule (Most-Likely Scenario)

| Stage | Duration | Partner hrs | Counsel hrs | Sr Assoc hrs | Mid hrs | Jr hrs | Paralegal hrs | Fees | Expenses | Subtotal |
|---|---|---|---|---|---|---|---|---|---|---|
| Pre-suit & Pleadings | 0–3 mo | | | | | | | | | |
| Initial Disclosures & Written Discovery | 3–9 mo | | | | | | | | | |
| Document Review & Production | 6–12 mo | | | | | | | | | |
| Depositions | 9–15 mo | | | | | | | | | |
| Expert Work | 12–18 mo | | | | | | | | | |
| Dispositive Motions | 15–18 mo | | | | | | | | | |
| Pretrial | 18–22 mo | | | | | | | | | |
| Trial (X days) | 22–24 mo | | | | | | | | | |
| Post-Trial / Appeal | 24–36 mo | | | | | | | | | |
| **Contingency ({X}%)** | | | | | | | | | | |
| **Total** | | | | | | | | | | |

## Expected-Value Scenario

| Path | P | Cost | Weighted |
|---|---|---|---|
| MTD granted, dismissed | {P1} | ${C1} | ${P1 × C1} |
| MTD denied, settles after discovery | {P2} | ${C2} | ${P2 × C2} |
| MSJ granted | {P3} | ${C3} | ${P3 × C3} |
| Trial, prevail | {P4} | ${C4} | ${P4 × C4} |
| Trial, lose + appeal | {P5} | ${C5} | ${P5 × C5} |
| **Expected Value** | 1.00 | | ${EV} |

## Assumptions
1. {Stated assumption} — {source/basis}
2. ...

## Re-Baseline Triggers
- After MTD ruling
- After substantial completion of document production
- After expert reports exchanged
- After dispositive-motion ruling
- 90 days pre-trial
```

---

## Verification

- [ ] Every stage has hours by timekeeper, fees, and expenses separately.
- [ ] Every cost driver is tied to a stated assumption.
- [ ] Both most-likely and expected-value scenarios provided.
- [ ] Probabilities sum to 1.00 in the EV table.
- [ ] Contingency line is present with basis.
- [ ] Decision-point re-baseline triggers identified.
- [ ] Expert costs appear in both discovery and trial stages.
- [ ] E-discovery hosting modeled as recurring, not one-time.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| One bottom-line number with no staging | Always break into stages with separate fees and expenses |
| Ignoring asymmetry between plaintiff and defendant work | Plaintiff bears proof burden in discovery; defendant bears motion-practice volume — model accordingly |
| Treating e-discovery as a fixed line item | Hosting and processing accrue monthly; budget per GB per month for projected duration |
| Omitting expert fees from trial stage | Trial-day expert charges, prep, and rebuttal stand separately from report drafting |
| Probabilities that do not sum to 1.00 | Force-balance the EV decision tree; identify the residual path |
| Assuming case settles "at mediation" without modeling pre-mediation costs | Mediation typically follows substantial discovery; pre-mediation spend is unavoidable |
| Using current rates for all future stages | Apply rate-step assumption for multi-year cases |
| No contingency on trial | Trial overruns are the rule, not the exception — minimum 20% buffer |
