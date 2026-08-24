---
title: "MD&A / Disclosure Review — Completeness, Consistency, and Required-Item Check"
category: finance/regulatory-compliance
description: "Review a Management's Discussion & Analysis (MD&A) and related disclosures for completeness against required items, internal consistency with the financial statements, balanced presentation, and forward-looking-statement hygiene — with no-fabrication and verify-against-current-source guardrails."
techniques:
  - DT-02
  - ST-02
  - DS-04
  - QA-02
  - CM-02
difficulty: intermediate
tags:
  - mdna
  - disclosure
  - sec-reporting
  - consistency
  - completeness
updated: "2026-06-08"
related_prompts:
  - domain-finance/regulatory-compliance/finance_compliance_gap_analysis.md
  - domain-finance/accounting-controllership/finance_audit_pbc_preparation.md
  - domain-finance/financial-statement-analysis/finance_peer_benchmarking_builder.md
  - domain-finance/field_guide.md
---

**Informational analysis only — not legal, accounting, or compliance advice. Disclosure requirements (e.g., SEC MD&A rules, IFRS management-commentary guidance, segment and non-GAAP/APM rules) change and vary by jurisdiction and filer status; confirm all required items against current official sources (SEC, applicable securities regulator, accounting standards) and qualified counsel/auditors before filing.**

## Objective

Review an MD&A and related narrative disclosures to flag (1) **completeness** gaps against the required disclosure items for the applicable regime/filer status, (2) **consistency** breaks between the narrative and the financial statements/footnotes, (3) **balance** issues (overly promotional or one-sided presentation), and (4) **forward-looking-statement and non-GAAP/APM hygiene**. The output is a reviewer's findings register, not a determination of disclosure adequacy; final sufficiency is for counsel and auditors.

## When to Use

- Pre-filing quality review of a periodic report's MD&A / management commentary
- Drafting feedback loop between finance, legal, and the disclosure committee
- Post-comment-letter remediation review
- Benchmarking MD&A completeness when adopting a new requirement or reporting change

## Inputs / Context Required

```
<mdna_review_context>
FILER / REGIME:
- Filer type and status (e.g., large accelerated / smaller reporting; domestic / foreign private issuer)
- Reporting regime and form/report type (verify required items against current rules)
- Jurisdiction and regulator

DOCUMENTS PROVIDED:
- MD&A / management-commentary draft (full text)
- Financial statements and footnotes (to check consistency)
- Prior-period MD&A (for comparability)
- Non-GAAP / APM reconciliations, if any
- Known issues, prior comment letters, audit-flagged items

CONTEXT:
- Material events in the period (acquisitions, impairments, going-concern, segment changes)
- Critical accounting estimates in play
- Date of review: __________
</mdna_review_context>
```

## Constraints

### Must
- State the **regime, filer status, jurisdiction, and regulator**; required items differ by these.
- Mark every reference to a specific required item, rule, or threshold as **"[verify required items against current {regulator} disclosure rules]"** — do not assert specific rule numbers or item lists as authoritative from memory.
- Check **completeness** against a generic required-item checklist (results of operations, liquidity & capital resources, material trends/uncertainties, critical accounting estimates, off-balance-sheet/contractual obligations where applicable, material risks) — and require the user to confirm the current required-item set.
- Check **consistency**: every quantified statement in the narrative must tie to the financial statements/footnotes; flag figures in MD&A not traceable to the statements (DS-04).
- Check **balance**: flag one-sided/promotional language and require both favorable and unfavorable drivers be discussed.
- Check **forward-looking statements**: presence and adequacy of cautionary framing; check that projections are not presented as assured outcomes.
- Check **non-GAAP/APM hygiene**: each non-GAAP measure reconciled to the most directly comparable GAAP/IFRS measure and not given undue prominence (mark prominence/reconciliation rules for verification).
- Run an **adversarial review (QA-02)**: what material trend, risk, or known uncertainty is omitted or buried?

### Must Not
- Assert a definitive list of required items or rule citations as authoritative.
- Rewrite or invent quantitative disclosures; only flag, never fabricate figures.
- Conclude the disclosure is "adequate" or "compliant" — that is for counsel/auditors.
- Treat boilerplate carry-forward from the prior period as automatically sufficient (over-reliance on prior-year mapping).

## Instructions

**Step 1 — Confirm regime and required-item baseline (CM-01).**
State filer status, regime, jurisdiction. List the required-item categories generically and mark "[verify required items against current {regulator} disclosure rules]". Ask the user to confirm/supply the current item set.

**Step 2 — Completeness pass (DT-02).**
For each required-item category, locate the corresponding MD&A coverage. Rate: Present & substantive / Present but thin / Absent / N/A. Flag absent or thin items as completeness findings.

**Step 3 — Consistency pass (DS-04, RT-05).**
Trace each material quantified claim in the narrative to the financial statements/footnotes:
- Do revenue/margin/cash-flow figures and trends described match the statements?
- Do segment, liquidity, and debt disclosures reconcile to the notes?
- Are period-over-period change drivers (price/volume/mix/FX) internally consistent and additive to the reported change?
Flag any figure in MD&A with no traceable source as an **untraceable-figure** finding.

**Step 4 — Balance and tone pass.**
Identify promotional or one-sided language. For each major positive driver discussed, confirm material negative drivers (and known headwinds/uncertainties) receive commensurate discussion.

**Step 5 — Forward-looking and non-GAAP/APM pass.**
- Forward-looking: confirm cautionary language accompanies projections; flag any forecast presented as certain.
- Non-GAAP/APM: confirm each measure is defined, reconciled to the comparable standard measure, used consistently period to period, and not given greater prominence than the comparable measure (mark prominence/reconciliation rules for verification).

**Step 6 — Adversarial review and omission scan (QA-02 / NE-06).**
Ask: What known trend, uncertainty, contingency, or risk in the period is not surfaced, or is buried? What did the prior period disclose that is missing now without explanation? Name the **checkbox/boilerplate** pitfall and require a disconfirming check on omitted material trends.

## Output Format

### Review Summary
- Regime/filer status/jurisdiction; documents reviewed; date.

### Completeness Findings

| # | Required item (verify) | Coverage status | Location | Finding | Severity |
|---|---|---|---|---|---|
| 1 | Liquidity & capital resources | Present but thin | §… | No discussion of covenant headroom | High |

### Consistency Findings

| # | Narrative statement | Source in financials | Tie-out result | Finding |
|---|---|---|---|---|
| 1 | "Revenue grew on volume" | Income stmt + note X | Untraceable — drivers not in notes | Flag |

### Balance & Tone Findings

| # | Issue | Example language | Suggested remediation |
|---|---|---|---|

### Forward-Looking & Non-GAAP/APM Findings

| # | Item | Issue | Verification needed |
|---|---|---|---|

### Omission / Adversarial Scan
- Material trends/risks omitted or buried: …
- Prior-period disclosures missing now (unexplained): …

### Verify-Against-Current Instruction
> Confirm the complete required-item set, non-GAAP/APM prominence and reconciliation rules, and any thresholds against current official disclosure rules for the applicable regulator and filer status **as of [date]**. Final disclosure adequacy is for qualified counsel and auditors.

## Verification

- [ ] Regime, filer status, jurisdiction, and regulator stated.
- [ ] Required items referenced generically and marked "[verify against current rules]".
- [ ] Every required-item category assessed for coverage.
- [ ] Material quantified narrative claims traced to the financial statements; untraceable figures flagged.
- [ ] Balance/tone assessed; one-sided presentation flagged.
- [ ] Forward-looking cautionary framing and non-GAAP/APM reconciliation/prominence reviewed.
- [ ] Adversarial omission scan completed against prior period and known events.
- [ ] No fabricated figures; adequacy not asserted.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Asserting a definitive required-item list or rule citation | Items marked "[verify against current rules]"; user confirms current set |
| Concluding the MD&A is "compliant/adequate" | Output is findings only; adequacy routed to counsel/auditors |
| Checkbox/boilerplate illusion (prior text carried forward) | Adversarial scan compares to prior period and known events; over-reliance pitfall named |
| Accepting MD&A figures at face value | Every material figure must tie to the statements; untraceable figures flagged |
| Promotional narrative read as informative | Balance pass requires commensurate negative-driver discussion |
| Non-GAAP measure presented without context | Reconciliation and prominence checked; rules marked for verification |
