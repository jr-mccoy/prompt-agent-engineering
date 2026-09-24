---
title: "Internal Investigation Plan — Privilege Framing, Collection, Witness Order, Reporting"
category: legal/regulatory-compliance
description: "Plan a counsel-directed internal investigation of suspected corporate misconduct with regulatory or criminal exposure (bribery, fraud, sanctions, antitrust, accounting): who directs it and why, privilege framing, preservation and document collection, witness order and Upjohn protocol, independence and conflicts, government-contact posture, and the reporting path to the board or special committee. Plans the investigation; does not reach findings."
techniques:
  - ST-02
  - CM-02
  - ST-43
  - QA-04
  - QA-01
difficulty: advanced
tags:
  - legal
  - regulatory-compliance
  - internal-investigation
  - privilege
  - upjohn
  - white-collar
  - special-committee
  - whistleblower-complaint
updated: "2026-09-24"
reasoning:
  styles: [systematic, strategic, decomposition]
  stakes: high
  horizon: weeks
  uncertainty: ambiguity
  evidence_quality: sparse
  domain_complexity: regulated
  collaboration: small_team
  output_format: structured
  user_role: [attorney, in_house_counsel, board_member]
related_prompts:
  - domain-legal/employment-labor/legal_workplace_investigation_plan_and_report.md
  - domain-legal/discovery/legal_ediscovery_custodian_interview.md
  - domain-legal/regulatory-compliance/legal_voluntary_disclosure_decision_memo.md
  - domain-legal/regulatory-compliance/legal_subpoena_or_cid_response_strategy.md
---

# Internal Investigation Plan

**Objective:** Produce the plan for a counsel-directed internal investigation into allegations of corporate misconduct that carries regulatory, civil-enforcement, or criminal exposure. The plan decides who directs the investigation and who reports to whom, frames privilege and work-product protection from the first day, preserves and collects evidence in a defensible order, sequences witnesses so that documents precede interviews and lower-level witnesses precede decision-makers, sets the government-contact and disclosure posture, and fixes the reporting path — without prejudging what the investigation will find.

**When to use:**
- A whistleblower report, audit finding, or media inquiry alleges bribery, fraud, sanctions or export violations, antitrust conduct, or accounting irregularities.
- A government inquiry has begun or is likely, and the company needs its own facts.
- The board or audit committee must decide whether to form a special committee.

**Distinct from:**
- `domain-legal/employment-labor/legal_workplace_investigation_plan_and_report.md` — HR-type investigations of harassment, discrimination, or retaliation complaints, including findings-of-fact reports. This prompt covers enterprise-exposure misconduct where government enforcement, disclosure, and board independence drive the design.
- `domain-legal/regulatory-compliance/legal_subpoena_or_cid_response_strategy.md` — responding to compulsory process; often runs in parallel.
- `domain-legal/regulatory-compliance/legal_voluntary_disclosure_decision_memo.md` — the disclosure decision this investigation informs.

---

## Your Input

- **Allegation(s):** [What is alleged, by whom (anonymized if needed), when received, through what channel]
- **Jurisdiction(s) and potential enforcers:** [Countries, regulators, prosecutors potentially interested]
- **Implicated persons and roles:** [Titles and reporting lines; whether any senior executive, director, or in-house lawyer is implicated]
- **Business context:** [Unit, geography, time period, transaction or relationship at issue]
- **Data landscape:** [Systems, custodians, devices (company and personal), messaging apps, third-party data, cross-border data restrictions]
- **Government status:** [None known / inquiry received / subpoena served / whistleblower may have gone to a regulator]
- **Governance:** [Audit committee composition, independence, existing outside counsel relationships, D&O and indemnification context]
- **Public-company or regulated-entity status:** [Disclosure and auditor-communication obligations]
- **Employment-law constraints:** [Works councils, data-protection law, union agreements, local interview rules]

---

## Constraints

**Must:**
- Decide direction and independence first: management-directed, audit-committee-directed, or special-committee-directed, with the reason (seniority of implicated persons, existing counsel relationships, auditor expectations).
- Frame privilege explicitly: engagement by counsel for the purpose of legal advice; retention of forensic accountants or consultants through counsel; labeling; a limited distribution list; and a note on how any later disclosure to the government could affect waiver (`[VERIFY: controlling jurisdiction's selective-waiver position]`).
- Preserve before investigating: hold notice, imaging of implicated custodians' devices, suspension of auto-deletion, and a plan for personal devices and ephemeral messaging within applicable employment and privacy law.
- Sequence witnesses: document review before interviews; peripheral witnesses before central ones; implicated persons last unless flight or destruction risk dictates otherwise.
- Include the corporate-counsel warning (Upjohn) protocol for every interview, and flag when a witness should be advised to consider separate counsel.
- Stratify risk: identify decisions whose error is irreversible (e.g., interviewing an implicated executive before imaging; tipping off; retaliation against a whistleblower) and put controls on each.
- State the reporting plan: oral versus written reports, to whom, and at what milestones.

**Must Not:**
- State conclusions, likely findings, or who is culpable. The plan is fact-neutral.
- Invent statutes, whistleblower-protection rules, self-reporting deadlines, or agency policies. Use `[CITE: ...]`, `[VERIFY: ...]`.
- Recommend interviewing the whistleblower's supervisor about the report in a way that reveals the whistleblower's identity.
- Recommend collection from personal devices or cross-border data transfers without flagging the employment and data-protection constraints.
- Use generic "consult counsel" boilerplate; the plan is for counsel.

---

## Instructions

1. **Frame the questions.** Convert the allegation into 3–6 investigative questions (who, what, when, knowledge, intent-relevant facts, control failures). No answers.
2. **Direction and independence.** Recommend who directs and who conducts; identify conflicts (implicated executives, regular outside counsel's prior work on the matter).
3. **Privilege framing.** Engagement letter language points, consultant retention through counsel, document labeling, distribution list, oral-versus-written report posture.
4. **Preservation.** Hold scope, device imaging order, messaging-app handling, backup suspension, third-party preservation letters.
5. **Collection and review.** Custodians by priority tier, date range, search methodology, review protocol, key-document identification.
6. **Witness plan.** Ordered list with rationale, interview purpose, documents to show, Upjohn protocol, separate-counsel flags, note-taking and memo format.
7. **Risk-stratified controls.** Table of irreversible-error risks with controls and owners.
8. **Government and disclosure posture.** Current status, triggers for a disclosure decision, auditor and public-disclosure obligations, whistleblower-protection constraints (`[VERIFY]`).
9. **Reporting and remediation path.** Milestone reports, final report form, interim remediation (e.g., suspending payments to an implicated third party), and discipline decisions deferred until facts are established.
10. **Budget and timeline.** Phased estimate with assumptions.

---

## Output Format

```markdown
# Internal Investigation Plan — {Matter code name}
**Privileged & Confidential — Attorney-Client Communication / Attorney Work Product — Prepared at the Direction of {Committee / Counsel}**

## 1. Investigative Questions
## 2. Direction, Independence, and Conflicts
## 3. Privilege Framework
## 4. Preservation
| Action | Scope | Owner | Deadline |
|---|---|---|---|
## 5. Collection and Review
## 6. Witness Plan
| Order | Witness (role) | Purpose | Key documents | Upjohn / separate-counsel note |
|---|---|---|---|---|
## 7. Irreversible-Error Risks and Controls
| Risk | Why irreversible | Control | Owner |
|---|---|---|---|
## 8. Government Contact and Disclosure Posture
## 9. Reporting Plan and Interim Remediation
## 10. Budget, Timeline, Assumptions
## 11. Open Items and Placeholders
```

---

## Worked Example

**Input (abridged):** An anonymous hotline report alleges that the head of a Latin American sales region approved inflated "marketing fees" to a customs broker to clear goods faster. The regional head reports to the COO. The company is publicly listed. No government contact yet.

**Output (excerpt):**
- **Direction:** Audit-committee-directed, conducted by outside counsel with no prior work for the region, because the COO's reporting line is implicated and auditors will ask about independence.
- **Preservation first:** Image the regional head's and two finance approvers' company devices before any interview; suspend auto-deletion on the region's email and chat tenant; customs-broker preservation letter: decision for counsel — sending it after the key-document review reduces tip-off risk, but delay risks deletion of the broker's records; check first whether the broker contract gives audit or record-preservation rights that can be invoked without disclosing the investigation's subject `[VERIFY: contract terms]`.
- **Witness order:** (1) AP clerk who processed the invoices; (2) regional controller; (3) logistics manager who used the broker; (4) finance approvers; (5) regional head, last, after documents and payment-flow analysis. Upjohn warning at every interview; flag separate counsel for the regional head.
- **Irreversible-error risk:** Regional head learns of the review and deletes messages from a personal messaging app → control: imaging and hold issued together, with interviews deferred; personal-device access evaluated under local employment and data-protection law `[VERIFY]`.
- **Disclosure posture:** No decision yet; triggers for a voluntary-disclosure memo listed (evidence of payment to an official; payments across more than one country).

---

## Verification

- [ ] Jurisdiction lock: every legal constraint (employment, data protection, whistleblower, privilege) tied to the named jurisdictions; unknowns marked `[VERIFY]`.
- [ ] Citation discipline: no invented statutes, agency policies, or deadlines.
- [ ] Plan is fact-neutral: no findings, culpability judgments, or predicted outcomes.
- [ ] Direction and independence decided with a reason.
- [ ] Preservation precedes interviews; imaging precedes interviews of implicated persons.
- [ ] Witness order justified; Upjohn protocol and separate-counsel flags present.
- [ ] Irreversible-error risks each have a control and owner.
- [ ] Whistleblower confidentiality and anti-retaliation protected in the plan's mechanics.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Plan drifts into conclusions ("the payments were likely bribes") | Keep to investigative questions; findings belong in a later report |
| Interviewing the implicated executive early "to hear their side" | Documents first; implicated persons last unless a stated risk requires otherwise |
| Management-directed investigation when a senior manager is implicated | Escalate direction to the audit or special committee; state the reason |
| Consultants retained directly by the business | Retain through counsel to support work-product protection |
| Hold issued after interviews begin | Preservation is Step 4 and precedes any contact with implicated persons |
| Identifying the whistleblower in interview questions | Frame questions around documents and processes, not the report |
| Recommending personal-device collection without legal constraints | Flag employment and data-protection limits by jurisdiction |
| Asserting self-reporting deadlines or selective-waiver rules from memory | `[VERIFY]` against the controlling jurisdiction's law and the agency's current policy |
