---
title: "Subcontractor Flow-Down Check"
category: legal/contracts-transactional
description: "Check that obligations owed to a client pass through correctly to subcontractors: confidentiality, IP assignment, liability caps and insurance, data protection, warranties, audit and termination rights — and identify the gaps where the prime holds an obligation it cannot enforce downstream."
techniques:
  - ST-02
  - ST-03
  - CM-02
  - QA-01
  - OC-03
difficulty: advanced
tags:
  - legal
  - contracts
  - subcontracting
  - flow-down
  - back-to-back
  - liability-cap
  - supplier-side
updated: "2026-09-21"
related_prompts:
  - domain-legal/contracts-transactional/legal_contract_clause_redline_targeted.md
  - domain-legal/contracts-transactional/legal_dpa_gdpr_drafter.md
  - domain-legal/contracts-transactional/legal_msa_drafter.md
  - domain-legal/employment-labor/solo_dev_contractor_management.md
---

**Purpose:** Compare the obligations you owe a client against the obligations your
subcontractors owe you, clause family by clause family, and identify every **gap** —
a place where you carry an obligation upstream that you cannot enforce downstream.
Output is a gap register with the residual exposure quantified and the amendments
required to close each.

**When to use:** Before engaging a subcontractor on client work; when a client
agreement is signed that tightens obligations above what existing subcontracts carry;
and at renewal, where terms on both sides have drifted independently.

**Why this exists as a separate prompt.** `legal_dpa_gdpr_drafter.md` covers
sub-processor flow-down for **data protection only**.
`../employment-labor/solo_dev_contractor_management.md` covers the management
relationship — when to outsource, scopes of work, IP assignment, payment structures,
quality control, tax classification. Neither performs a systematic back-to-back
comparison across the full set of commercial obligations, which is where prime
contractors accumulate uninsured exposure quietly.

**This is not legal advice.** Flow-down enforceability, pay-when-paid validity,
worker classification and mandatory terms vary by jurisdiction and contract type.
This produces a gap register and questions for counsel.

---

## Inputs required

- The client agreement (MSA, SOW, DPA, any order form) — the upstream obligations
- Each subcontract, or the intended terms — the downstream obligations
- The subcontractor's insurance certificates, if any
- What work is being subcontracted, and what the subcontractor will access
- Governing law on both sides — they may differ, which is itself a finding

---

## Method

### Step 1 — Extract upstream obligations by family

From the client agreement, list what you owe across these families. This is the
benchmark everything downstream is measured against.

| Family | Extract |
|---|---|
| Confidentiality | Scope, duration, permitted disclosures, return/destruction |
| IP ownership | What vests in the client, when, and what you warrant about provenance |
| Liability | Cap, uncapped carve-outs, indemnities given |
| Insurance | Types and minimum levels required of you |
| Data protection | Processor obligations, sub-processor consent, security measures, breach notice |
| Warranties | Standard of performance, non-infringement, personnel |
| Compliance | Codes of conduct, anti-bribery, sanctions, modern slavery, background checks |
| Audit | Client rights to audit you, and over what |
| Personnel | Named key personnel, substitution restrictions, non-solicit |
| Termination | What you must do on termination, including transition assistance |
| Records | Retention periods, timesheet and evidence obligations |

### Step 2 — Compare each against the subcontract

For each family, mark one of:

- **Matched** — downstream obligation equals or exceeds upstream
- **Gap** — downstream is weaker; you carry the difference
- **Absent** — no downstream equivalent at all
- **Unenforceable in practice** — present, but the subcontractor could not satisfy it

The fourth category matters as much as the second. A liability clause requiring an
individual contractor to carry £5m of exposure is present, matched on paper, and
worthless — the obligation exceeds their capacity to meet it.

### Step 3 — Examine the five families where gaps are most expensive

**Liability cap.** The classic prime-contractor trap: you accept a £2m cap to the
client and cap your subcontractor at their fee. The difference is your uninsured
exposure. Check also that uncapped carve-outs upstream — typically confidentiality
breach, data breach, IP infringement, wilful misconduct — are also uncapped
downstream. An upstream uncapped IP indemnity against a downstream capped one is the
single most common serious gap.

**IP assignment.** You cannot assign to the client what you do not own. Verify: the
subcontract assigns present and future rights, covers moral rights so far as
permitted, deals with pre-existing and third-party materials, and covers open-source
inclusion. Where the subcontractor is an individual in a jurisdiction where
assignment of future rights is restricted, flag for counsel — a chain that is broken
here breaks your warranty to the client.

**Insurance.** Confirm the subcontractor actually holds what the client requires of
you: type, level, occurrence versus claims-made, and that the policy responds to this
kind of work. Obtain certificates; do not accept assertions. Check the expiry date
and whether renewal is tracked.

**Data protection.** Where personal data is involved, check: is sub-processing
permitted by the client contract at all, and does it require prior consent or
notification? Are the processor obligations passed through in substance? Are
international transfer mechanisms in place on both legs? Use
`legal_dpa_gdpr_drafter.md` for the detail.

**Compliance obligations.** Codes of conduct, anti-bribery, sanctions screening,
background checks and modern-slavery obligations routinely appear upstream and are
routinely absent downstream. They are cheap to flow down and awkward to explain if
breached.

### Step 4 — Check the payment interaction

Distinct from the obligation families but belonging to the same review:

- Do inbound and outbound payment terms align, or do you fund the gap?
- Is there a pay-when-paid or pay-if-paid clause? Flag that its enforceability is
  restricted or void in several jurisdictions — a question for counsel, and do not
  rely on it commercially.
- Does client termination leave you owing a subcontractor commitment? Cross-check
  `legal_termination_economics_provider_side.md`.

Quantify in
`../../domain-finance/corporate-finance-fpa/finance_subcontractor_margin_model.md`.

### Step 5 — Check what survives termination

Confidentiality, IP assignment, data-deletion and record-retention obligations
typically survive termination upstream. Confirm the downstream equivalents survive
too, and for at least as long. A subcontract whose confidentiality obligation expires
in two years, against a five-year upstream obligation, leaves three years uncovered.

### Step 6 — Quantify residual exposure and decide

For each gap, state the residual exposure and choose one:

| Response | When |
|---|---|
| **Amend the subcontract** | Default. Usually straightforward before engagement |
| **Accept, insured** | Your own insurance responds. Confirm it does, in writing |
| **Accept, uninsured** | Small, bounded exposure. Record the decision and its size |
| **Restructure** | Do not subcontract this element; or introduce the subcontractor to the client directly |
| **Do not proceed** | The gap exceeds what the engagement earns |

The restructure option is under-used. Where the flow-down gap on a component is
irreducible, a direct contract between client and specialist — with you coordinating
for a fee — removes the exposure entirely.

---

## Output format

```markdown
# Flow-down check — [client agreement] → [subcontractor]
**Upstream governing law:** [x] · **Downstream:** [x] · **Counsel review:** required

## Gap register
| # | Family | Upstream obligation | Downstream | Status | Residual exposure | Response |
|---|---|---|---|---|---|---|

## Liability detail
| | Upstream | Downstream | Gap |
|---|---|---|---|
| General cap | | | |
| Uncapped carve-outs | | | |
| IP indemnity | | | |
| Data breach | | | |

## Insurance verification
| Type | Client requires | Subcontractor holds | Certificate seen | Expiry |
|---|---|---|---|---|

## Survival
| Obligation | Upstream survives | Downstream survives | Uncovered period |
|---|---|---|---|

## Payment interaction
| | |
|---|---|
| Inbound terms | |
| Outbound terms | |
| Funding gap | |
| Pay-when-paid present | [y/n — enforceability unverified] |
| Exposure if client terminates | |

## Amendments required before engagement
1. [clause] — [proposed wording]

## Questions for counsel
1. [assignment of future IP rights by an individual under [law]]
2. [pay-when-paid enforceability under [law]]

## Decision
[proceed with amendments / proceed accepting [x] exposure / restructure / do not proceed]
```

---

## Verification

- [ ] Every family in the table is assessed; none skipped as "not applicable" without
      a reason.
- [ ] "Unenforceable in practice" is used where the subcontractor could not meet the
      obligation, even if the clause matches.
- [ ] Uncapped upstream carve-outs are checked individually against downstream caps.
- [ ] Insurance is verified by certificate, with expiry recorded.
- [ ] Survival periods are compared and uncovered periods stated.
- [ ] Governing-law mismatch between the two agreements is flagged.
- [ ] Each gap has a chosen response, and "accept" states the exposure in money.

**False-positive prevention.** The dominant failure is checking that a clause exists
rather than that it matches. A confidentiality clause in both agreements is not a
match if the downstream one is narrower in scope or shorter in duration. Compare
substance, not presence.

The second is accepting a liability cap that the subcontractor cannot satisfy.
A cap of £1m against an individual with no assets and no insurance is a number, not a
recovery. The practical test: if this went wrong, what could actually be collected?
That figure, not the cap, is your real downstream protection.

The third is assuming pay-when-paid protects you. Its validity is restricted or void
in several jurisdictions. Model your exposure on the assumption you must pay
regardless, and treat any protection as upside.

The fourth is running this after the subcontractor has started. Amendments are
straightforward before engagement and contested afterwards.

---

## Related

- `legal_dpa_gdpr_drafter.md` — the data-protection leg in detail
- `legal_contract_clause_redline_targeted.md` — the upstream clause positions
- `legal_termination_economics_provider_side.md` — commitments surviving client termination
- `../employment-labor/solo_dev_contractor_management.md` — the management relationship
- `../../domain-finance/corporate-finance-fpa/finance_subcontractor_margin_model.md` — quantifying the payment and commitment exposure
