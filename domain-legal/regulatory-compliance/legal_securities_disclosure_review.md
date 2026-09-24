---
title: "Securities Disclosure Review — 10-K / 10-Q Risk Factors and MD&A Through a Liability Lens"
category: legal/regulatory-compliance
description: "Securities-counsel review of periodic-report risk factors and MD&A for misleading-statement and omission exposure — stale hypothetical risks, generic risk factors, undisclosed known trends, half-truths, safe-harbor hygiene, and inconsistency with the issuer's other public statements — distinct from a finance-team completeness check of MD&A against the financial statements and from an investor's filing teardown."
techniques:
  - DT-05
  - RT-06
  - QA-05
  - QA-12
  - IPC-07
difficulty: advanced
tags:
  - legal
  - securities
  - sec-reporting
  - risk-factors
  - mdna
  - 10-k-review
  - public-company-filing
updated: "2026-09-24"
related_prompts:
  - domain-finance/regulatory-compliance/finance_mdna_disclosure_review.md
  - domain-finance/investing-research/finance_10k_10q_teardown.md
  - domain-legal/regulatory-compliance/legal_regulatory_change_impact_assessment.md
---

# Securities Disclosure Review — 10-K / 10-Q Risk Factors and MD&A Through a Liability Lens

> **Scope guard — attorney-facing only.** This prompt is for securities counsel (outside or in-house) and disclosure-committee members working under counsel's direction. It does not give investment advice or evaluate whether anyone should buy or sell the issuer's securities. An investor researching a company should use `domain-finance/investing-research/finance_10k_10q_teardown.md`.

> **No-fabrication rule.** Do not invent Regulation S-K item numbers, SEC guidance, comment-letter language, case names, or quotations from the draft or from other public statements. Quote only text the user supplied, with its location. Use `[CITE: …]`, `[NEED PIN: …]`, `[NEED HOLDING: …]` for unsupplied authority.

## When to Use

- Pre-filing legal review of a 10-K or 10-Q draft, especially the risk-factor section and MD&A known-trends discussion.
- After a material event (cyber incident, customer loss, investigation, restatement) to check whether existing disclosure has gone stale.
- Responding to or remediating after an SEC comment letter on risk factors or MD&A.

**Not this prompt if:**
- The finance team needs a completeness and number-consistency check of MD&A against the financial statements — use `domain-finance/regulatory-compliance/finance_mdna_disclosure_review.md` (run it first; this prompt assumes the numbers tie).
- You are analysing the filing as an investor — use `domain-finance/investing-research/finance_10k_10q_teardown.md`.
- A new disclosure rule is being adopted and you need a program-level impact plan — use `domain-legal/regulatory-compliance/legal_regulatory_change_impact_assessment.md`.

## Inputs

- **Jurisdiction and regime (required):** US federal (Exchange Act periodic reporting) or another securities regulator; filer status (large accelerated, accelerated, non-accelerated, smaller reporting company, foreign private issuer) `[VERIFY: current status determination]`.
- **Form and period:** 10-K, 10-Q, or equivalent; fiscal period; filing target date.
- **Draft text:** Risk factors and MD&A in full, with page or paragraph numbers.
- **Prior filing:** Same sections from the last annual and quarterly report (to detect stale or dropped disclosure).
- **Known facts inside the company:** Events, trends, incidents, investigations, customer or supplier changes, internal forecasts that management is aware of — as disclosed to counsel.
- **Other public statements:** Earnings release and call script, investor deck, sustainability report, press releases for the period.
- **Comment letters and responses**, if any.

## Method

1. **Jurisdiction and form lock.** State the regime, form, filer status, and which disclosure items apply `[VERIFY: current Regulation S-K items for risk factors, MD&A, legal proceedings, and any topic-specific items such as cybersecurity]`. Do not rely on memory for item numbers or page-length triggers.
2. **Known-facts matrix.** List each internal fact counsel supplied. For each, find where (if anywhere) the draft addresses it. An internal fact with no disclosure home is a candidate omission.
3. **Risk-factor pass — one row per risk factor.**
   - *Stale hypothetical:* the risk is framed as something that "could" or "may" happen, but the known-facts matrix shows it has already occurred in whole or part. This is the highest-priority finding; treatment varies by circuit `[VERIFY]`.
   - *Generic:* the risk could appear in any issuer's filing without change; recommend tailoring or moving to a general-risks section `[VERIFY: current SEC expectations]`.
   - *Buried or mis-headed:* the heading understates the body.
   - *Dropped:* a risk in the prior filing is missing without a known reason.
4. **MD&A pass.** Test known trends, events, demands, commitments, and uncertainties that are reasonably likely to have a material effect `[VERIFY: current Item 303 standard]` against the known-facts matrix. Distinguish (a) a pure omission, whose private-liability consequences depend on the claim and current law `[VERIFY]`, from (b) a half-truth — a statement made that becomes misleading because of what is left out. Half-truths are the priority.
5. **Opinion and forward-looking statements.** Identify statements of belief or expectation; check whether embedded facts are true and whether the issuer omitted facts about its basis that conflict with what a reasonable investor would take from the statement `[CITE: opinion-statement authority]`. For forward-looking statements, check identification and meaningful, specific cautionary language `[VERIFY: statutory safe-harbor scope and exclusions for this issuer]`.
6. **Consistency sweep.** Compare the draft against the earnings call, investor deck, sustainability report, and press releases. Flag any number, characterization, or tone that differs.
7. **Materiality framing.** For each finding, state why a reasonable investor might consider it important (qualitative and quantitative), without asserting a bright-line percentage test.
8. **Redline and questions.** Propose specific replacement language, and list the sub-certification or disclosure-committee questions that must be answered before the language can be finalized.

## Output Format

```markdown
# Securities Disclosure Review — {Issuer} — {Form} for {Period}
**Regime / filer status:** {…} [VERIFY]  |  **Target filing date:** {…}  |  **Privileged & Confidential — Attorney Work Product**

## 1. Applicable Items (verified / [VERIFY])
## 2. Known-Facts Matrix
| # | Internal fact | Source | Disclosed where? | Gap? |
## 3. Findings Register
| # | Location | Category (stale hypothetical / generic / omission / half-truth / opinion / FLS / inconsistency / dropped) | Draft text (quoted) | Why it matters to a reasonable investor | Proposed language | Severity (H/M/L) |
## 4. Consistency Sweep
| Topic | Draft says | Other statement says (source) | Resolution |
## 5. Questions for Management / Sub-Certifiers
## 6. Open Verification Items
```

## Verification

- [ ] Jurisdiction lock: regime, form, and filer status stated; item requirements marked `[VERIFY]` unless supplied.
- [ ] Citation discipline: no item numbers, SEC releases, or cases asserted from memory without `[CITE]` / `[VERIFY]`.
- [ ] Scope discipline: review covers disclosure exposure, not accounting judgments or investment merit.
- [ ] Every internal fact in the known-facts matrix is either located in the draft or logged as a gap.
- [ ] Every "may/could" risk factor has been checked against facts that show it already materialized.
- [ ] Half-truths distinguished from pure omissions, with the difference in exposure explained.
- [ ] Every quoted phrase is quoted exactly from the supplied draft or statement, with location.
- [ ] Proposed language does not introduce new unsupported factual claims.
- [ ] Any event that may trigger a separate current-report obligation is flagged with its trigger and `[VERIFY]` deadline.

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Adding more generic risk factors as the fix | Tailor to the issuer's facts; length is not protection and generic factors draw comments |
| Missing the stale-hypothetical problem | Cross-check every conditional risk against the known-facts matrix before anything else |
| Treating every omission as actionable | Separate pure omissions from half-truths; the liability analysis differs `[VERIFY]` |
| Reviewing the 10-K in isolation | Run the consistency sweep against calls, decks, and releases for the same period |
| Asserting a quantitative materiality threshold | Explain qualitative and quantitative significance; no bright-line percentage |
| Rewriting disclosure to be more optimistic | The goal is accuracy and balance; flag promotional tone rather than amplifying it |
| Relying on boilerplate cautionary language for safe-harbor protection | Cautionary statements must be specific to the forward-looking statement and the risks known now |

## Example

**Input (abridged):** US filer, 10-Q. Fictional issuer Northwind Sensors Inc. Existing risk factor: "We may experience security incidents that could disrupt operations." Counsel's known facts: a ransomware incident six weeks before quarter-end took one plant offline for nine days; investigation ongoing. Earnings call script says "no material operational disruptions this quarter." MD&A attributes the revenue dip to "customer timing."

**Output (excerpt):**

> **Finding 1 — Stale hypothetical (H).** Risk factor at p. 34 frames a security incident as hypothetical; one has occurred. Proposed: disclose that the company experienced a ransomware incident affecting one facility during the quarter, that the investigation is ongoing, and describe the risk of further effects. Separately confirm whether a current-report obligation was triggered `[VERIFY: current cybersecurity incident disclosure item and materiality determination date]`.
>
> **Finding 2 — Half-truth risk (H).** MD&A attributes the revenue decline to "customer timing." If the plant outage contributed, the explanation is incomplete in a way that could mislead. Question for management: quantify the outage's revenue effect.
>
> **Finding 3 — Inconsistency (H).** Call script says "no material operational disruptions." Reconcile before the call or the filing; the two statements cannot both stand unqualified.
