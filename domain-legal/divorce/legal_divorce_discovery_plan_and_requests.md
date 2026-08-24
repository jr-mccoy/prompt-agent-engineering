---
title: "Divorce Discovery Plan and Requests"
category: legal/divorce
description: "Build a divorce discovery plan and draft the core requests: a discovery roadmap tied to the contested financial and custody issues, requests for production targeting financial records, interrogatories on income/assets/separate-property claims, third-party subpoenas (banks, employers, businesses), document categories for lifestyle and dissipation analysis, and a proportionality/privacy check — sized to the controlling state's family-discovery rules and mandatory-disclosure regime."
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
  - divorce
  - family-law
  - discovery
  - document-requests
  - interrogatories
updated: "2026-06-01"
related_prompts:
  - domain-legal/divorce/legal_financial_affidavit_and_disclosure_builder.md
  - domain-legal/divorce/legal_hidden_asset_and_dissipation_investigation.md
  - domain-legal/divorce/legal_divorce_trial_prep_and_findings_plan.md
  - domain-legal/discovery/legal_document_request_drafter.md
  - domain-legal/discovery/legal_interrogatory_drafter.md
---

**Purpose:** Produce a focused divorce discovery plan and the core written discovery to obtain it, tied to the actual contested issues (income, asset value, separate-property claims, dissipation, custody-relevant facts) and conformed to the state's family-discovery rules and mandatory disclosures. Output is a discovery plan plus drafted requests, not a memo.

**When to use:** After initial disclosures, when issues are contested; building the evidentiary record for support, property division, or custody; pursuing suspected hidden assets or dissipation.

---

## Your Input

- **Jurisdiction:** [State; family-discovery rules; mandatory-disclosure regime; numerical limits and deadlines `[CITE: …]`]
- **Contested issues:** [Income determination, asset valuation, separate-property claims, dissipation, custody factors, support]
- **Known gaps:** [What disclosure has not produced]
- **Financial complexity:** [Business interests, multiple accounts, real property, deferred comp, crypto]
- **Third parties:** [Banks, employers, businesses, accountants needing subpoenas]
- **Custody facts needed:** [School, medical, communications, third-party witnesses — if custody is contested]
- **Proportionality/privacy:** [Sensitivity of records; protective-order needs]
- **Timing:** [Discovery cutoff; expert disclosure deadlines]

---

## Constraints

**Must:**
- Tie each discovery request to a **specific contested issue** — do not draft boilerplate that ignores the case.
- Respect the state's **numerical limits, format, and deadlines** for interrogatories, RFPs, and subpoenas `[CITE: …]`, and avoid duplicating mandatory disclosures.
- Target **financial records** with specificity (account statements by institution and period, tax returns and schedules, business GL, loan applications, pay records, deferred comp).
- Where custody is contested, include **custody-relevant** discovery (school/medical records, communications, third-party witnesses) consistent with the child's privacy.
- Use **third-party subpoenas** for records the spouse will not or cannot produce, with notice as the rules require.
- Apply a **proportionality and privacy check**; propose a **protective order** for sensitive financial or child records.
- Use placeholders `[CITE: ...]`, `[NEED LIMIT: ...]`, `[NEED: ...]` for unsupplied rules, limits, or facts.

**Must Not:**
- Draft overbroad, all-encompassing requests untethered to issues (subject to objection/sanction).
- Exceed the state's numerical/scope limits without leave.
- Seek the child's private records without a legitimate custody purpose and privacy safeguards.
- Invent the state's discovery limits, deadlines, or rules.
- Use discovery for harassment or to drive up cost.
- Insert generic "consult counsel" disclaimers.

---

## Instructions

1. **Issue-to-discovery map.** For each contested issue, list the proof needed and the discovery device best suited to obtain it.
2. **Requests for production.** Draft RFPs for financial records by category, institution, and period; tie each to an issue.
3. **Interrogatories.** Draft interrogatories on income sources, asset identification, separate-property bases, transfers, and (if contested) custody facts — within the numerical limit.
4. **Third-party subpoenas.** Identify custodians and draft subpoena scope with required notice.
5. **Custody discovery (if applicable).** School/medical/communications with privacy safeguards.
6. **Proportionality & protective order.** Note sensitive categories; propose protective-order terms.
7. **Sequencing & deadlines.** Order the discovery against the cutoff and expert-disclosure deadlines.

---

## Output Format

```markdown
# DIVORCE DISCOVERY PLAN — Case No. {____}
**State rules / limits / deadlines:** {…} [CITE: …] [NEED LIMIT: …]

## A. Issue-to-Discovery Map
| Contested issue | Proof needed | Device |
|---|---|---|
| {Income determination} | {tax returns, pay records, K-1} | RFP/Rog/subpoena |

## B. Requests for Production (excerpt)
1. All statements for {account/institution} from {period}.
2. Federal and state tax returns with all schedules and K-1s for {years}.
3. {Business GL / loan applications / deferred-comp statements} …

## C. Interrogatories (excerpt — within limit of {N})
1. Identify all sources of income for {periods}, with amounts and payors.
2. Identify each asset claimed to be separate property and the factual basis.
3. Identify all transfers of assets over {$} since {date}, the recipient, and the purpose. …

## D. Third-Party Subpoenas
| Custodian | Records | Notice required |
|---|---|---|
| {Bank} | {statements} | {to opposing party} |

## E. Custody Discovery (if contested)
- {School/medical/communications} with {privacy safeguards / protective order}

## F. Proportionality & Protective Order
- Sensitive categories: {…}; proposed protective-order terms: {…}

## G. Sequencing & Deadlines
- {Order of service vs. discovery cutoff and expert deadlines}
```

---

## Verification

- [ ] Each request tied to a specific contested issue (no untethered boilerplate).
- [ ] State numerical limits, format, and deadlines respected; mandatory disclosures not duplicated.
- [ ] Financial RFPs specific by institution, account, and period.
- [ ] Interrogatories cover income, assets, separate-property bases, and transfers (and custody facts if applicable).
- [ ] Third-party subpoenas identified with required notice.
- [ ] Custody discovery limited to legitimate purposes with privacy safeguards.
- [ ] Proportionality/privacy check and protective-order proposal included.
- [ ] Sequencing aligned to the cutoff and expert deadlines.
- [ ] No invented limits, deadlines, or rules.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Drafting overbroad "any and all documents" requests | Tie each request to an issue, institution, and period |
| Exceeding the state's interrogatory/RFP limits | Stay within the numerical limit or seek leave [NEED LIMIT] |
| Duplicating mandatory disclosures | Target only what disclosures did not produce |
| Seeking the child's records without a custody purpose | Limit to legitimate purposes; add privacy safeguards/protective order |
| Omitting tax-return schedules and K-1s | Request full returns with schedules to find income sources |
| Forgetting third-party notice requirements | Provide the notice the rules require before subpoenaing records |
| Using discovery to harass or inflate cost | Apply proportionality; keep requests issue-driven |
| Inventing the discovery cutoff or rules | Use [CITE]/[NEED] placeholders |
| No protective order for sensitive financials | Propose protective-order terms for confidential records |
| Ignoring expert-disclosure deadlines | Sequence valuation/forensic discovery before expert deadlines |
