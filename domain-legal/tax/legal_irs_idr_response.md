---
title: "IRS Information Document Request (IDR) Response"
category: legal/tax
description: "Plan and draft a response to an IRS Information Document Request — request-by-request scope analysis, objections to overbreadth and relevance, privilege screening (attorney-client, work product, federally authorized tax practitioner), production plan with custodians and dates, and a cover letter — keeping the examination cooperative while protecting privileged material, and marking every enforcement step and deadline for verification."
techniques:
  - CM-03
  - ST-03
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - tax
  - irs-examination
  - idr
  - tax-controversy
  - privilege
  - document-production
updated: "2026-09-24"
reasoning:
  styles: [procedural, protective, analytic]
  stakes: high
  horizon: weeks
  uncertainty: risk
  evidence_quality: moderate
  domain_complexity: regulated
  collaboration: small_team
  output_format: structured
  user_role: [lawyer, analyst]
  mode: [respond, plan]
related_prompts:
  - domain-legal/discovery/legal_discovery_response_objections.md
  - domain-legal/discovery/legal_privilege_log_generator.md
  - domain-legal/discovery/legal_privilege_review_protocol.md
  - domain-legal/tax/legal_rd_credit_position_memo.md
---

# IRS Information Document Request (IDR) Response

**Objective:** Turn an IDR into a managed production: each numbered request analyzed for scope and relevance to the issue under examination, negotiable overbreadth identified and a narrowed alternative proposed, privileged and protected material screened out and logged, and a dated production plan with owners — plus a cover letter that preserves objections and the working relationship with the examination team. Where the IDR is a response to a delinquency notice or pre-summons step, the plan escalates accordingly.

**When to use:**
- An IDR arrives in an examination (any size of business or individual under exam).
- A follow-up IDR expands scope or re-requests material believed already produced.
- The examiner has issued a delinquency notice or signaled a summons.

**Distinct from:**
- `domain-legal/discovery/legal_discovery_response_objections.md` — civil-litigation discovery responses under court rules; IDRs are administrative, with different enforcement (summons) and no court-supervised meet-and-confer.
- `domain-legal/discovery/legal_privilege_log_generator.md` — reuse it for the log format; this prompt decides what is privileged in a tax exam, including tax-practitioner privilege limits.
- `legal_rd_credit_position_memo.md` / `legal_transfer_pricing_position_paper.md` (this folder) — the substantive positions; this prompt manages what is produced in support.

**Audience:** Tax-controversy counsel, in-house tax directors working with counsel.

---

## Your Input

- **IDR text:** [Paste in full — number, date, issue, requested items, response date]
- **Examination context:** [Taxpayer, years, examination type and team, issues under exam, prior IDRs and responses]
- **Stage:** [Initial IDR / follow-up / delinquency notice received / pre-summons letter received — paste any notice]
- **Documents available:** [Systems and custodians holding responsive material; volume estimates]
- **Potentially privileged material:** [Tax memos, advisor communications, accrual workpapers, audit-committee materials, opinions]
- **Business constraints:** [Close calendar, staff availability, confidentiality concerns]
- **Enforcement procedures you have verified:** [Current IDR enforcement process in the IRM or directive — or leave blank for `[VERIFY]`]

---

## Constraints

### Must
- Analyze **each numbered request** separately: what it asks, its tie to an issue under examination, scope (years, entities, custodians), and burden.
- **Negotiate before objecting** where possible: propose a narrowed scope, sampling, or a rolling production; document the proposal.
- Screen for **attorney-client privilege**, **work product** (anticipation of litigation), and the **federally authorized tax practitioner privilege**, with its limits — it does not apply in criminal matters or to written communications promoting certain tax shelters `[VERIFY: §7525]`.
- Flag **tax accrual workpapers** and audit-related materials as sensitive categories subject to IRS policy and case law `[VERIFY: current IRS policy] [NEED HOLDING: circuit authority]`.
- Build a **privilege log** plan for withheld items.
- Produce a **production plan**: item, custodian, source, date, reviewer, and whether produced in full, in part, or withheld.
- Mark **response dates and enforcement steps** (delinquency notice, pre-summons, summons) `[VERIFY: current IRM / directive]`; never compute them from memory.

### Must Not
- Produce privileged material inadvertently by agreeing to broad "all documents" categories without review.
- Assert blanket objections without a request-specific basis — they erode credibility with the exam team.
- Create or alter documents in response to an IDR; produce what exists and explain gaps.
- Characterize the facts in the cover letter in ways that concede issues; the letter transmits, it does not argue the merits unless intended.
- Ignore that waiver in one production can extend to related material; flag subject-matter waiver risk.
- Invent IRM sections, directive numbers, or deadlines.

---

## Instructions

1. **Parse the IDR** into a request table with the issue each request supports.
2. **Scope analysis** per request: relevant to the issue? Years and entities within the exam? Clear enough to answer?
3. **Burden estimate** per request (custodians, volume, time).
4. **Privilege screen** per request: categories of potentially protected material and the privilege asserted.
5. **Negotiation proposals** for overbroad or unclear requests (narrowed definitions, sampling, date limits, rolling production).
6. **Production plan** with dates and owners; flag items needing an extension request.
7. **Privilege log plan** (reuse the discovery privilege log format).
8. **Cover letter** transmitting the response, stating what is produced, what is withheld and why, and what is to follow — preserving objections.
9. **Escalation plan** if the IDR is at the delinquency or pre-summons stage.

---

## Output Format

```markdown
# IDR Response Plan — IDR No. {…} — {Taxpayer}, Tax Year(s) {…}
**Received:** {date}  |  **Response date requested:** {from IDR}  |  **Stage:** {…}  |  **Privileged & Confidential**

## 1. Request Analysis
| Req. # | Summary | Issue supported | Scope concern | Burden | Privilege flag | Proposed approach |
## 2. Negotiation Proposals (for exam team call)
## 3. Privilege Screen
| Category | Privilege / protection | Basis | Withhold / redact / produce |
## 4. Production Plan
| Req. # | Documents | Custodian / system | Reviewer | Target date | Status |
## 5. Privilege Log Plan
## 6. Cover Letter (draft)
## 7. Enforcement and Timing   ([VERIFY] each step)
## 8. Open Items
```

---

## Worked Example

**Input (abridged):** Exam of a mid-size manufacturer's 2023–2024 returns, issue: research credit. IDR #7 requests: (1) "all documents relating to research activities for 2020–2024"; (2) payroll registers for employees included in QREs; (3) the credit study and "all communications with the preparer"; (4) board minutes discussing tax positions. Response date on IDR: 30 days out.

**Output (excerpt):**

> | Req. | Scope concern | Proposed approach |
> |---|---|---|
> | 1 | Years 2020–2022 are outside the exam; "all documents" is unbounded | Propose: project-level documentation for the business components claimed, 2023–2024 only; rolling production by component |
> | 2 | Tied to the issue | Produce in full for employees included in QREs; redact SSNs |
> | 3 | Credit study — produce (the return relies on it). "All communications with the preparer" — screen: preparer is a CPA firm; §7525 may protect tax-advice communications in a non-criminal matter but not business or accounting communications `[VERIFY: §7525 scope]` | Produce the study; log withheld advice communications |
> | 4 | Board minutes may contain counsel's advice and reserve discussions | Produce minutes with privileged portions redacted and logged; flag accrual-workpaper sensitivity |
>
> **Cover letter (excerpt):** "Enclosed are documents responsive to Requests 2 and 3 (credit study). As discussed with [examiner] on [date], the Taxpayer will produce component-level documentation responsive to Request 1 for tax years 2023 and 2024 on a rolling basis beginning [date]. Certain communications responsive to Request 3 and portions of the materials responsive to Request 4 are withheld or redacted as privileged; a log is enclosed. The Taxpayer reserves all objections."

---

## Verification

- [ ] Jurisdiction lock: federal examination; state audit handled separately if present.
- [ ] Every request analyzed individually with an issue tie.
- [ ] Negotiated narrowing proposed before objection.
- [ ] Privilege screen covers attorney-client, work product, and §7525 with its limits.
- [ ] Production plan has owners and dates.
- [ ] Withheld items have a log plan.
- [ ] Enforcement steps and deadlines marked `[VERIFY]`.
- [ ] No invented IRM sections, directive numbers, or deadlines; no altered or created documents.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Agreeing to "all documents" requests to appear cooperative | Negotiate scope first; broad agreement risks privileged and irrelevant production |
| Blanket privilege objections | Assert request-specific privileges with a log |
| Treating §7525 as equivalent to attorney-client privilege | It is narrower — no criminal matters, no tax-shelter promotion communications, and only tax advice |
| Ignoring subject-matter waiver | Producing part of an advice memo can waive related material |
| Arguing the merits in the cover letter | Transmit and preserve; argue positions in a separate submission |
| Missing that a delinquency or pre-summons notice changes the timeline | Identify the stage and escalate |
| Stating IDR enforcement deadlines from memory | Mark `[VERIFY]` against current IRM / directive |
