---
title: "Statement of Work Drafter"
category: legal/contracts-transactional
description: "Draft a Statement of Work attached to an existing MSA with specific scope, deliverables, milestones, acceptance criteria, pricing model, assumptions, dependencies, and change-order procedures. Output is enforceable as both a commercial and a legal document."
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
  - contracts
  - sow
  - statement-of-work
  - acceptance
  - change-order
updated: "2026-05-11"
related_prompts:
  - domain-legal/contracts-transactional/legal_msa_drafter.md
  - domain-legal/contracts-transactional/legal_contract_review_full_redline.md
  - domain-legal/contracts-transactional/legal_negotiation_position_paper.md
  - domain-legal/research/legal_research_memo_irac.md
---

**Purpose:** Draft a Statement of Work (SOW) that attaches to a previously executed MSA. The SOW defines the engagement-specific scope, deliverables, acceptance criteria, pricing, and timeline; the MSA controls framework terms (indemnity, LoL, IP, confidentiality, etc.). Output is calibrated to posture and includes a clean change-order mechanism.

**When to use:** Initiating a new engagement under a standing MSA; renewing or expanding an existing engagement; converting an informal scope document into an enforceable SOW. Use the MSA drafter if no MSA exists; use targeted redline for inbound counterparty SOWs.

---

## Your Input

- **Reference MSA:** [MSA title, effective date, parties; or paste relevant provisions if there is no separately executed MSA]
- **Posture:** [Customer OR Supplier]
- **Governing law (from MSA):** [State]
- **Engagement title and SOW number:** [For tracking — e.g., "SOW-2026-003"]
- **Effective date and target completion:** [Start date / end date or duration]
- **Scope summary:** [3–5 sentence description of what will be done]
- **Deliverables list:** [Itemized list with target dates]
- **Pricing model:** [T&M with rates / fixed fee / milestone / hybrid; with caps and not-to-exceed if any]
- **Payment milestones:** [Tied to deliverables, dates, or invoicing cadence]
- **Acceptance criteria:** [How each deliverable will be evaluated as complete]
- **Acceptance period:** [Number of days customer has to accept or reject]
- **Customer dependencies:** [Inputs, approvals, access, personnel customer must provide]
- **Supplier resources / key personnel:** [Named personnel, role, replacement consent rights]
- **Assumptions:** [Specific assumptions whose change triggers change-order]
- **Out-of-scope items:** [What is explicitly excluded]
- **Change-order mechanic:** [Form, approval levels, mid-engagement price adjustment formula]
- **Service levels / SLAs (if applicable):** [Response times, uptime, credits]
- **Data and security overlay (if different from MSA):** [Engagement-specific PII access, security controls]

---

## Constraints

**Must:**
- Open with a reference to the controlling MSA and confirm SOW is governed by MSA terms.
- Include an **order of precedence** statement (typically: MSA controls except where this SOW expressly references and overrides a specific MSA section).
- State **deliverables in measurable terms** with acceptance criteria. "Develop user portal" is not a deliverable; "Functional user portal supporting login, profile edit, and password reset, deployed to staging environment by {date}" is.
- Distinguish **deliverable acceptance** from **invoice acceptance** — they are separate.
- Specify **acceptance procedure**: review period, deemed-acceptance rule, rejection procedure with specificity requirements, re-submission cycle, ultimate failure consequences.
- For fixed fee: state the **scope envelope** — what is included; what triggers change-order.
- For T&M: state **rates, rate-card source, escalators, not-to-exceed cap, reporting cadence**.
- For milestone billing: tie each invoice to a specific deliverable acceptance.
- Include **customer dependencies** with the consequence of customer delay (timeline extension, scope reduction, fee adjustment).
- Include **change-order form and authority**: who can sign; whether email approval is acceptable; price adjustment formula.
- Include **assumptions** as a list — these are the inputs whose change triggers re-pricing.
- For posture = supplier: protect against scope creep with tight change-order discipline and a deemed-acceptance clause.
- For posture = customer: protect against weak deliverables with measurable acceptance and rejection rights.

**Must Not:**
- Restate MSA framework provisions (indemnity, LoL, warranties, IP). The MSA controls; restating creates conflict.
- Use vague deliverables ("provide consulting services" — not a deliverable).
- Omit acceptance criteria for any deliverable.
- Invent statutes, regulations, or counterparty terms. Use `[CITE: ...]` / `[NEED: ...]`.
- Use "TBD" or "to be discussed" in the final SOW — drive to specificity.
- Embed change-order pricing without an explicit formula or approval mechanic.
- Use generic disclaimers.

---

## Posture Calibration Reference

| Provision | Customer Posture Default | Supplier Posture Default |
|---|---|---|
| Acceptance period | Long enough to evaluate (10–30 business days) with specific rejection rights | Short period (5–10 business days) with deemed-acceptance |
| Acceptance criteria | Detailed, objective, measurable | High-level, deliverable-by-deliverable |
| Fixed-fee scope envelope | Tight definition with itemized inclusions | Broad with explicit exclusions and change-order trigger |
| T&M not-to-exceed | Hard cap with no overage absent change order | Soft cap with overage notification, rates continue |
| Change order approval | Customer must sign before work begins | Email approval from named PM acceptable |
| Customer delay consequence | Limited extension; no fee adjustment for short delays | Day-for-day extension + fee adjustment for resource holding |
| Key personnel | Named, with consent for replacement | Replaced with equivalent personnel on notice |
| Warranty (within MSA framework) | Express performance plus re-perform + refund | Re-perform as sole remedy |

---

## Instructions

1. **Anchor.** Reference the MSA explicitly: title, date, parties. Confirm SOW governed by MSA.
2. **Scope.** 3–5 sentence engagement summary, then itemized scope list.
3. **Out of scope.** Explicit exclusions to prevent scope creep arguments.
4. **Deliverables.** Each deliverable: (a) name, (b) description, (c) acceptance criteria, (d) target date, (e) format and delivery method.
5. **Acceptance procedure.** Review period, rejection mechanics, re-submission cycle, escalation, final failure.
6. **Timeline.** Milestones and dates. Note dependencies between milestones.
7. **Pricing and payment.** Fee model, invoicing tied to milestones or cadence, expenses (pre-approval threshold), taxes, late fees per MSA.
8. **Resources.** Supplier key personnel (named, with consent rights for replacement); customer personnel and roles.
9. **Customer dependencies.** Each dependency: input, who provides, due date, consequence of delay.
10. **Assumptions.** Specific assumptions whose change triggers change-order.
11. **Change-order procedure.** Form, signature authority, pricing formula for additional scope (rate-card + multiplier? blended rate? new SOW?).
12. **Service levels (if applicable).** Response targets, credits, exclusions.
13. **Data and security (if engagement-specific).** Reference MSA + Security Addendum, add engagement-specific controls.
14. **Term.** Effective date; expiration on acceptance of final deliverable or end date; early termination per MSA.
15. **Signature.** Authority representation; consistent with MSA signature requirements.

---

## Output Format

```markdown
STATEMENT OF WORK NO. {SOW-NUMBER}

This Statement of Work ("SOW") is entered into as of {Effective Date} by and between {Customer Legal Name} ("Customer") and {Supplier Legal Name} ("Supplier") under the Master Services Agreement dated {MSA Date} (the "MSA"). Capitalized terms used but not defined in this SOW have the meanings set forth in the MSA. In the event of conflict between this SOW and the MSA, the MSA controls except where this SOW expressly references and overrides a specific MSA section.

1. ENGAGEMENT OVERVIEW
{3–5 sentence summary}

2. SCOPE OF SERVICES
2.1 Included Scope:
- {item}
- {item}
2.2 Out of Scope (Explicit Exclusions):
- {item}
- {item}

3. DELIVERABLES
| # | Deliverable | Description | Acceptance Criteria | Target Date | Format |
|---|---|---|---|---|---|
| 1 | {name} | {description} | {measurable criteria} | {date} | {format} |
| 2 | | | | | |

4. ACCEPTANCE PROCEDURE
4.1 Review Period. Customer will have {N} business days from delivery to accept or reject each Deliverable.
4.2 Rejection. A rejection must be in writing and state with reasonable specificity each respect in which the Deliverable fails to meet its Acceptance Criteria.
4.3 Cure. Supplier will have {N} business days to cure and re-submit.
4.4 Deemed Acceptance. Failure to provide written rejection within the Review Period constitutes acceptance. {Posture-dependent}
4.5 Final Failure. After {N} cure cycles, Customer may {refund/reperform/terminate this SOW}.

5. TIMELINE AND MILESTONES
| Milestone | Date | Dependencies |
|---|---|---|
| {name} | {date} | {predecessor milestone or customer input} |

6. FEES AND PAYMENT
6.1 Pricing Model. {Fixed fee / T&M / milestone}.
6.2 Total Fees. {Amount or formula}.
6.3 Not-to-Exceed. {If T&M: cap; mechanic when cap is approached}.
6.4 Invoicing Schedule. {Tied to milestones or cadence}.
6.5 Expenses. {Pre-approval threshold, reimbursement basis}.
6.6 Payment Terms. As set forth in MSA § __.

7. PERSONNEL
7.1 Supplier Key Personnel:
| Name | Role | Allocation | Replacement Consent |
|---|---|---|---|
| | | | Yes/No |
7.2 Customer Personnel and Responsibilities:
{role and time commitment}

8. CUSTOMER DEPENDENCIES
| Dependency | Owner | Due Date | Consequence of Delay |
|---|---|---|---|
| {input/approval/access} | Customer | {date} | {extension/fee adjustment} |

9. ASSUMPTIONS
- {assumption that, if changed, triggers change-order}
- {assumption}

10. CHANGE-ORDER PROCEDURE
10.1 Trigger. A Change Order is required for: (a) any change to Scope or Deliverables; (b) any change to Timeline of more than {N} business days; (c) any change to Fees; (d) any material change to assumptions in Section 9.
10.2 Form. Written change order signed by authorized representatives of both Parties. Email approval from {named role} is acceptable for changes under {threshold}.
10.3 Pricing for Additional Scope. {Rate card + multiplier / blended rate / new SOW}.
10.4 Disputed Change Orders. {Mechanism}.

11. SERVICE LEVELS {if applicable}
{Response targets, uptime, credits, exclusions}

12. DATA AND SECURITY {if engagement-specific}
{Engagement-specific controls supplementing MSA + Security Addendum}

13. TERM
This SOW commences on the Effective Date and expires upon acceptance of the final Deliverable or {End Date}, whichever is earlier. Either Party may terminate this SOW in accordance with the MSA.

14. SIGNATURES
{Customer block} | {Supplier block}
```

---

## Verification

- [ ] Reference to MSA is explicit, including date and parties.
- [ ] Order-of-precedence statement included.
- [ ] Every deliverable has measurable acceptance criteria.
- [ ] Acceptance procedure specifies review period, rejection specificity, cure cycles, and final failure consequences.
- [ ] Customer dependencies listed with owners, dates, and delay consequences.
- [ ] Assumptions itemized; change-order trigger tied to assumption change.
- [ ] Change-order form and signature authority specified.
- [ ] Fees, invoicing schedule, and not-to-exceed (if T&M) all present.
- [ ] No restatement of MSA framework provisions.
- [ ] No invented citations or counterparty terms; placeholders for missing inputs.
- [ ] Posture calibration applied to acceptance period, scope envelope, and key personnel.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Deliverables like "provide consulting services" with no measurable criteria | Each deliverable must have a specific output (document / system / report) with objective acceptance criteria |
| Restating MSA indemnity / LoL / IP provisions in the SOW | The MSA controls. Restating creates conflict and risks the SOW overriding the MSA unintentionally |
| "TBD" placeholders in the executed SOW | Drive every TBD to specificity before signature, or use `[NEED: ...]` flags to flag for client decision |
| Fixed-fee SOW with no scope envelope | Always define what is included; absent envelope, every customer request becomes a scope dispute |
| T&M SOW with no not-to-exceed | Customer paper requires hard cap; supplier paper may use soft cap with notification, but always with a number |
| Acceptance period that runs from "completion" rather than "delivery" | Tie acceptance period to delivery; otherwise supplier waits indefinitely for customer to declare completion |
| Deemed acceptance favoring customer in supplier paper | Supplier paper should include deemed-acceptance after a defined review period to prevent indefinite delay |
| Change-order pricing left to "good faith negotiation" | Specify the formula (rate card, blended rate, or new SOW); good-faith pricing is unenforceable |
| Key personnel commitment without replacement consent | Customer paper should name key personnel with consent for replacement; otherwise supplier can rotate at will |
| Customer-dependency delays with no fee or timeline adjustment | Supplier paper should include day-for-day extension and resource-holding fee; customer paper limits both |
| SLA credits as sole remedy without breach right at threshold | Above a defined credit threshold, customer should have right to terminate the SOW without penalty |
| Mixing T&M and fixed fee without clear segregation | If hybrid, segregate by deliverable; never bill T&M against a fixed-fee envelope |
