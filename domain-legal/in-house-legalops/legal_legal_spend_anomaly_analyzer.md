---
title: "Outside-Counsel Invoice Anomaly Analyzer"
category: legal/in-house-legalops
description: "Review outside-counsel invoice line items against the company's outside-counsel guidelines and statistical norms to flag billing anomalies — block billing, vague entries, overstaffing, partner-level work that should be associate-level, duplicate billing, unauthorized travel, expert markups, rate-step increases, conflicts failures — with severity tiers and pay/negotiate/dispute/revise recommendations."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - legal-ops
  - outside-counsel-management
  - billing
  - spend-management
updated: "2026-05-11"
related_prompts:
  - domain-legal/in-house-legalops/legal_matter_summary_for_executive.md
  - domain-legal/in-house-legalops/legal_playbook_builder_for_contract_type.md
  - domain-legal/litigation/legal_litigation_budget_phase_estimator.md
---

**Purpose:** Audit an outside-counsel invoice against (a) the company's outside-counsel guidelines (OCGs), (b) statistical norms for the matter type and phase, and (c) prior-period invoices on the same matter. Output is a triage of line items with severity tiers and a recommendation per anomaly: pay-in-full, negotiate write-off, dispute, or require revised invoice.

**When to use:** Pre-payment review on a material invoice, e-billing rejection triage, annual spend audit, post-matter close reconciliation, preparation for a rate-setting conversation with a firm, quarterly OCG-compliance scorecard.

---

## Your Input

- **Invoice file or extracted line items:** [PDF, LEDES 1998B/2000, or extracted CSV with timekeeper, date, task/activity codes (UTBMS L/E/A codes if available), narrative, hours, rate, fee, expense category, amount]
- **Matter context:** [Matter name, matter type, phase, current procedural posture, approved budget, prior-period spend]
- **Outside-counsel guidelines (OCGs) in force:** [Block-billing prohibition, narrative granularity, time-entry minimum unit (e.g., 0.1h), staffing rules (lead partner + associate cap, no-charge for first-year associates, no client-relationship-partner billing), pre-approval thresholds for travel / experts / vendors, conflicts certification, rate-step rules]
- **Rate sheet on file:** [Approved timekeepers and rates; effective dates]
- **Benchmark data (optional):** [Vendor-cohort blended rate for this matter type, internal task-code unit-rate norms, prior-period comparable invoices]
- **Authority:** [Reviewer's authority — flag-only, propose write-offs, withhold payment]

---

## Constraints

**Must:**
- Anchor every flag to a **specific OCG provision, rate-sheet entry, or statistical norm** — never a general "looks high" judgment.
- Quote the offending line-item narrative **verbatim** when flagging it.
- Assign a **severity tier** to every flag:
  - **S1 (Hard violation):** Direct OCG breach (block billing, unapproved rate, unapproved timekeeper, prohibited expense). Default action: require revised invoice or dispute.
  - **S2 (Soft violation / efficiency):** Probable overstaffing, partner-level work that should be associate-level, vague-but-not-blocked entries, duplicate-effort signal. Default action: negotiate write-off.
  - **S3 (Watch item):** Pattern that warrants attention but no immediate action. Default action: pay; raise in next quarterly review.
- For statistical anomalies, identify the **comparison set** (vendor-cohort, period-over-period on this matter, task-code unit-rate) and the magnitude of deviation.
- Produce a **per-line recommendation**: pay-in-full / negotiate write-off (with dollar amount) / dispute / require revised invoice.
- Total proposed adjustments to a **dollar figure** for the invoice.

**Must Not:**
- Invent OCG provisions, rate-sheet entries, timekeeper names, hours, or dollar amounts. If a field is missing from the input, write "[not in input]" and flag the gap.
- Flag a line item as a violation without citing the specific OCG section or rate-sheet entry that is violated.
- Treat every long narrative or high hour count as anomalous — anomalies require a comparison anchor.
- Recommend dispute on items where the OCG is silent or ambiguous — those go to S2 negotiation, not S1 dispute.
- Use boilerplate "all entries reviewed" language without listing what was reviewed.
- Issue legal advice on the underlying matter — this is a billing review, not a matter strategy memo.

---

## Instructions

1. **Ingest and normalize.** Parse line items into a uniform schema: date, timekeeper, title/level, task/activity code, narrative, hours, rate, fee, expense category, amount.
2. **Cross-check the rate sheet.** For every timekeeper: are they on the approved list? Is the billed rate the approved rate? Has there been an unauthorized step-up since the last approved rate sheet?
3. **Cross-check the OCG provisions.** Walk each line item against the OCG checklist:
   - **Block billing** — multiple tasks in one entry without separate time allocations.
   - **Vague narratives** — "review correspondence," "attention to file," "various tasks."
   - **Unauthorized timekeepers** — first-year associates, paralegals on professional work, summer associates, contract attorneys without pre-approval.
   - **Partner-level work that should be associate-level** — document review, cite-checking, deposition summaries by partners at partner rates.
   - **Duplicate billing across timekeepers** — multiple attendees at meetings/depositions/calls without justification; same task narrative from two timekeepers same day.
   - **Travel charges** — flights/hotels/meals against OCG caps; travel time billing at full rate when half-rate is policy; first-class violations.
   - **Expert / vendor markups** — pass-through expenses with an administrative markup the OCG forbids.
   - **Conflicts certification** — was a conflicts certification provided for this billing period?
   - **Pre-approval thresholds** — items over the OCG pre-approval threshold without a documented approval.
4. **Statistical anomaly pass.**
   - **Vendor-cohort comparison:** Does any timekeeper's effective rate or hours sit outside the benchmark for this matter type and phase?
   - **Period-over-period:** Has the burn rate on this matter shifted materially without a docket event explanation?
   - **Task-code unit-rate:** Cost per task code (e.g., L210 pleadings, L320 document production) outside the norm?
5. **Tier and recommend.** Apply S1 / S2 / S3. Recommend pay-in-full / negotiate write-off / dispute / require revised invoice with a dollar adjustment.
6. **Roll up.** Total invoice amount, total flagged, recommended adjustment, net payable.
7. **Note the gaps.** What you could not check because of missing inputs (rate sheet, OCG, benchmark data).

---

## Output Format

```markdown
# Invoice Anomaly Review — {Matter Name} — Invoice {No.} — {Period}

## Summary
- **Invoice total:** ${amount}
- **Flagged line items:** {count} ({S1: x | S2: y | S3: z})
- **Recommended adjustment:** ${amount} ({% of invoice})
- **Net payable (if recommendations adopted):** ${amount}
- **Action posture:** {pay-with-adjustments / negotiate / dispute / require-revised-invoice}

## Flagged Items

### S1 — Hard Violations
| Line | Date | Timekeeper | Hours | Fee | Narrative (verbatim) | OCG / Rate-Sheet Citation | Recommended Action | $ Adjustment |
|---|---|---|---|---|---|---|---|---|
| {n} | {date} | {name, level} | {h} | ${f} | "{narrative}" | OCG §{x} — {provision} | Require revised invoice | ${a} |

### S2 — Soft Violations / Efficiency
| Line | Date | Timekeeper | Hours | Fee | Narrative (verbatim) | Concern | Comparison Anchor | Recommended Action | $ Adjustment |
|---|---|---|---|---|---|---|---|---|---|
| {n} | {date} | {name, level} | {h} | ${f} | "{narrative}" | {e.g., partner-level work at partner rate; document review by 3 partners} | {cohort / prior period / task-code norm} | Negotiate write-off | ${a} |

### S3 — Watch Items
| Pattern | Evidence | Comparison Anchor | Next-Review Trigger |
|---|---|---|---|
| {pattern} | {lines / hours / $} | {benchmark} | {next-quarter review / next invoice} |

## Statistical Findings
- **Vendor-cohort comparison:** {finding or "no benchmark available"}
- **Period-over-period (this matter):** {finding}
- **Task-code unit-rate:** {finding}

## Gaps in This Review
- {Field / data the reviewer could not check, and why}

## Recommendation
{Pay-in-full / Pay with negotiated write-off of $X / Dispute lines {n, n, n} / Require revised invoice}.
Rationale: {2–3 sentences}.
Next step: {specific outreach — partner-in-charge call, e-billing rejection with code, dispute letter draft}.
```

---

## Verification

- [ ] Every flag is anchored to a specific OCG provision, rate-sheet entry, or statistical comparison.
- [ ] Narratives are quoted verbatim, not paraphrased.
- [ ] Severity tiers (S1/S2/S3) are applied consistently per the definitions above.
- [ ] Recommendation per flag (pay / negotiate / dispute / revise) is explicit.
- [ ] Dollar adjustments sum to the headline figure.
- [ ] Gaps in input data are disclosed, not silently ignored.
- [ ] No invented timekeepers, rates, hours, OCG provisions, or benchmarks.
- [ ] Review distinguishes hard OCG violations from efficiency concerns.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Flagging block billing without quoting the entry | Quote the narrative verbatim; if it bundles tasks without separate times, S1 |
| Calling any partner-on-document-review entry an S1 violation | OCG usually permits with cause; absent cause it is S2 (negotiate), not S1 (dispute) |
| Flagging "review correspondence" as vague when the OCG permits one-line narratives under 0.3h | Check the OCG narrative-granularity threshold before flagging |
| Asserting a rate is unapproved without checking the dated rate sheet | If the rate sheet on file shows a step-up effective date covering the period, it is approved |
| Flagging duplicate billing for two attendees at a deposition where defense of a witness reasonably requires two | Multiple-attendee billing is S2 unless the OCG forbids it outright; cite the provision |
| Statistical anomaly without a named comparison set | "Above average" is not a flag; "$X vs cohort median $Y for L210 pleadings" is |
| Generic "the firm should be more efficient" comments | Tie every efficiency comment to a line item, a comparison, and a dollar adjustment |
| Recommending dispute on every flag | Dispute is for S1 hard violations only; S2 is negotiate, S3 is watch |
| Pasting hours totals without sanity-checking against approved budget | Cross-check matter spend to budget; flag burn-rate anomalies separately |
| Boilerplate "consult an auditor" disclaimer | Remove — this output is the audit |
| Failing to disclose missing OCG or rate-sheet inputs | Disclose gaps in the "Gaps in This Review" section; do not silently skip checks |
