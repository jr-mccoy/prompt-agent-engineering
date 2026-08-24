---
title: "Board Resolution Drafter (Transactional Approvals)"
category: legal/corporate-ma
description: "Draft board (and, where required, stockholder) resolutions for M&A transactional approvals: WHEREAS recitals, RESOLVED clauses tied to authority required under the charter/bylaws and state corporate law, omnibus authorization, secretary's certificate, and exhibit list."
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
  - m-and-a
  - corporate
  - board-resolution
  - corporate-governance
  - secretary-certificate
updated: "2026-05-11"
related_prompts:
  - domain-legal/corporate-ma/legal_disclosure_schedule_drafter.md
  - domain-legal/corporate-ma/legal_post_closing_integration_legal_checklist.md
  - domain-legal/contracts-transactional/legal_msa_drafter.md
  - domain-legal/research/legal_research_memo_irac.md
---

**Purpose:** Produce board (and, where required, stockholder) resolutions that authorize a transaction with the specificity required for the closing officer's certificate, opinions, and good-standing of corporate action. Each RESOLVED clause traces to a specific approval requirement under the charter, bylaws, or state corporate code.

**When to use:** Pre-signing and pre-closing approvals on either side; reorganization approvals (F-reorg, drop-down, conversion); merger approvals under DGCL §251 / §253 / §262 (or equivalent); stock issuances; equity plan amendments; §280G cleansing votes.

---

## Your Input

- **Deal structure:** [Asset purchase / stock purchase / forward merger / reverse triangular merger / 338(h)(10) / F-reorg / drop-down / conversion]
- **Governing law of the resolution entity:** [State of formation/incorporation; default Delaware]
- **Entity type:** [C-corp / S-corp / LLC / LP — drives statutory citations]
- **Industry:** [Industry — drives any industry-specific approvals, e.g., regulated-entity board approvals]
- **Posture:** [Buyer / Seller / Target / Acquisition Sub / Parent]
- **Approving body:** [Board / Sole stockholder / Stockholders (vote required and threshold) / Sole member / Manager / GP]
- **Authority basis:** [Charter section, bylaws section, DGCL §141 (board generally), §251 (merger), §271 (sale of substantially all assets), §228 (written consent in lieu), §242 (charter amendment), §262 (appraisal notice); LLC operating agreement section]
- **Transaction documents to approve:** [List — APA, SPA, Merger Agreement, escrow agreement, paying agent, R&W policy, employment agreements, restrictive covenants, transition services, etc.]
- **Ancillary actions:** [Adoption of plan of merger, filing of certificate of merger, amendment of charter, increase of authorized shares, designation of preferred series, equity grants, equity acceleration, §280G cleansing, dissolution of subsidiary, conversion]
- **§280G cleansing vote needed:** [Yes — requires separate stockholder approval by disinterested holders of more than 75% of voting power eligible to vote] / [No]
- **Appraisal / dissenters' rights applicable:** [Yes/No — drives notice resolution]
- **Officers to be authorized:** [Titles for omnibus / "officers' certificate" execution authority]
- **Format:** [Meeting minutes with resolutions / Written consent in lieu of meeting under §141(f) / §228]

---

## Constraints

**Must:**
- Open with WHEREAS recitals laying the factual predicate and the authority basis. Recitals are non-operative but frame the resolutions; keep them factual and concise.
- Each RESOLVED clause maps to a specific action requiring board (or stockholder) approval under the charter, bylaws, or controlling statute.
- For merger or sale-of-substantially-all-assets, cite the controlling statutory section (e.g., DGCL §251 for merger, §271 for asset sale) and include the statutorily required declarations (advisability of the merger, recommendation to stockholders, etc.).
- Include an **omnibus authorization** resolution authorizing officers to execute and deliver the transaction documents and "any and all" further documents, certificates, and instruments reasonably necessary or appropriate to consummate the transactions.
- Include a **ratification** resolution covering prior officer actions taken in furtherance of the transaction.
- Attach the form of each transaction document as an exhibit (or reference VDR location) and identify in the resolution that the approved form is "substantially in the form attached as Exhibit [X], with such changes as the officers executing the same may approve, such approval to be conclusively evidenced by such execution."
- Include a **Secretary's Certificate** at the end (or as a companion document) certifying (a) the resolutions are in full force and effect, (b) the charter and bylaws attached are in effect, (c) incumbency of signing officers, and (d) good standing.
- For written consents in lieu of meeting, recite the statutory authority (DGCL §141(f) for directors, §228 for stockholders) and the unanimous / majority requirement satisfied.
- For §280G cleansing votes, follow Treas. Reg. §1.280G-1 Q&A-7 mechanics: full disclosure, separate vote, more-than-75% of voting power held by disinterested holders, contingent on stockholder approval.
- For stockholder votes, address §262 appraisal-rights notice if applicable.

**Must Not:**
- Invent charter/bylaws sections, statutory citations, transaction document names, signing officer names, or share counts. Use `[NEED: ...]` and `[CITE: ...]` placeholders.
- Use a single vague resolution to approve "the transaction" — itemize each material action.
- Omit the omnibus authorization or ratification clauses.
- Skip the form-of-document exhibit reference (creates ambiguity about what was actually approved).
- Conflate board approval with stockholder approval (DGCL §251 requires both; §251(h) and §253 have specific carve-outs).
- Include "consult counsel" disclaimers — the resolutions are the work product.
- Use approval thresholds (majority, supermajority, unanimous) without confirming the charter/bylaws/statutory requirement.

---

## Instructions

1. **Header.** Entity name, type of action (Action by Written Consent of the Board of Directors in Lieu of Meeting; Minutes of Special Meeting of the Board of Directors; Action by Written Consent of the Stockholders), date.
2. **Recitals (WHEREAS clauses).** Identify:
   - The transaction parties and the transaction summary.
   - The transaction documents.
   - The authority basis (charter section, bylaws section, statute).
   - Prior actions or approvals being incorporated.
   - For mergers, the determination of advisability and recommendation to stockholders.
   - For §280G cleansing, the parachute payment determination and disclosure to stockholders.
3. **RESOLVED clauses.** One per material action. Typical set for a sell-side merger approval:
   - Approval of the merger and merger agreement (declare advisable, approve form, authorize execution).
   - Recommendation to stockholders (where stockholder approval required).
   - Approval of the form of each ancillary document (disclosure schedule, escrow agreement, paying agent agreement, etc.).
   - Approval of payment of fees and expenses.
   - Approval of equity treatment (acceleration, cash-out, rollover).
   - Authorization of §228 written consent solicitation or special meeting notice (with §262 appraisal-rights notice if applicable).
   - §280G cleansing vote authorization (separate stockholder consent prepared and circulated).
   - D&O tail policy approval.
   - Officer authorization (omnibus).
   - Ratification.
4. **Signature block.** Names and titles of all directors signing (or chair signature for minutes).
5. **Exhibits.** A — Merger Agreement (form); B — Disclosure Schedule (form); C — Escrow Agreement (form); D — Officer Certificate forms; etc.
6. **Secretary's Certificate** as a separate document, attaching the resolutions, charter, bylaws, and incumbency.
7. **§280G cleansing vote materials** (if applicable) as a separate stockholder consent with disclosure statement.

---

## Output Format

```markdown
[ENTITY NAME]
a [State] [Entity Type]

ACTION BY WRITTEN CONSENT
OF THE BOARD OF DIRECTORS
IN LIEU OF A SPECIAL MEETING

[Date]

The undersigned, constituting [all / a majority of] the members of the Board of Directors (the "Board") of [Entity Name], a [State] [corporation / limited liability company] (the "Company"), pursuant to [DGCL §141(f) / applicable statute / Section [X] of the Bylaws], hereby take the following actions and adopt the following resolutions by written consent in lieu of a special meeting:

## RECITALS

WHEREAS, the Company has been negotiating a [merger / stock purchase / asset purchase] transaction (the "Transaction") with [Buyer/Counterparty Name], a [State] [Entity Type] ("[Buyer]");

WHEREAS, in connection with the Transaction, the Company proposes to enter into (i) an Agreement and Plan of Merger by and among the Company, [Buyer], and [Merger Sub], in substantially the form attached hereto as Exhibit A (the "Merger Agreement"), and (ii) the ancillary agreements identified in the Merger Agreement (collectively with the Merger Agreement, the "Transaction Documents");

WHEREAS, the Board has reviewed the Transaction Documents and has been advised by management and outside counsel regarding the terms and conditions thereof;

WHEREAS, the Board has determined that the Transaction is advisable and in the best interests of the Company and its stockholders;

WHEREAS, [the Transaction requires approval by the stockholders pursuant to DGCL §251(c)] [the Board will recommend that stockholders approve the Transaction];

WHEREAS, [the Transaction may result in payments that could be considered "parachute payments" under Section 280G of the Internal Revenue Code, and the Board has determined to seek a cleansing stockholder vote pursuant to Section 280G(b)(5) and Treas. Reg. §1.280G-1 Q&A-7];

NOW, THEREFORE, BE IT RESOLVED, that:

## RESOLUTIONS

### Approval of the Merger
RESOLVED, that the Merger, the Merger Agreement, and the transactions contemplated thereby are hereby declared advisable, fair to, and in the best interests of the Company and its stockholders, and the same are hereby approved and adopted, in substantially the form attached as Exhibit A, with such changes thereto as the officers executing the same may approve, such approval to be conclusively evidenced by such execution.

### Recommendation to Stockholders
RESOLVED FURTHER, that the Board hereby recommends that the stockholders of the Company adopt the Merger Agreement and approve the Merger, and directs that the Merger Agreement be submitted to the stockholders for their approval pursuant to DGCL §251(c) and §228, including by means of a written consent of stockholders in lieu of meeting.

### Approval of Ancillary Documents
RESOLVED FURTHER, that each of the [Disclosure Schedule, Escrow Agreement, Paying Agent Agreement, Letter of Transmittal, R&W Insurance Policy, D&O Tail Policy, Employment Agreements, Restrictive Covenant Agreements, Transition Services Agreement], in substantially the forms attached as Exhibits [B–K] hereto, is hereby approved.

### Approval of Equity Treatment
RESOLVED FURTHER, that the treatment of outstanding equity awards under the Company's [Equity Plan], including the [acceleration of vesting / cash-out at the per-share merger consideration / rollover into Buyer equity] as set forth in the Merger Agreement, is hereby approved.

### §280G Cleansing Vote
RESOLVED FURTHER, that the Board hereby authorizes the solicitation of a stockholder vote pursuant to Section 280G(b)(5) of the Internal Revenue Code and Treas. Reg. §1.280G-1 Q&A-7, to be conducted in accordance with the requirements of such regulation (including disclosure to disinterested stockholders and approval by more than 75% of the voting power held by such disinterested stockholders), and the officers of the Company are authorized to prepare and distribute the disclosure statement and form of stockholder consent attached as Exhibit [L].

### §262 Appraisal Rights Notice
RESOLVED FURTHER, that the officers of the Company are authorized to deliver the notice required by DGCL §262(d)(1) to all stockholders entitled to appraisal rights in connection with the Merger.

### D&O Tail Insurance
RESOLVED FURTHER, that the procurement of a [six-year] "tail" policy for directors and officers covering acts and omissions prior to the Effective Time, on the terms summarized in Exhibit [M], is hereby approved.

### Fees and Expenses
RESOLVED FURTHER, that the payment of all fees and expenses incurred by the Company in connection with the Transaction, including legal, financial advisory, accounting, and other professional fees as set forth in Exhibit [N], is hereby approved.

### Omnibus Authorization
RESOLVED FURTHER, that the officers of the Company (each, an "Authorized Officer") are, and each of them hereby is, authorized, empowered, and directed, in the name and on behalf of the Company, to negotiate, execute, deliver, and perform the Transaction Documents and to take any and all such further actions and to execute and deliver any and all such further documents, certificates, instruments, notices, and filings (including filings with the Secretary of State and any applicable regulatory authorities) as such Authorized Officer may deem necessary, appropriate, or advisable to carry out the intent and purpose of these resolutions, the taking of such actions and the execution and delivery of such documents to be conclusive evidence of such Authorized Officer's authorization hereunder and the Board's approval thereof.

### Ratification
RESOLVED FURTHER, that all actions previously taken by any director, officer, employee, agent, or representative of the Company in connection with the Transaction and the matters contemplated by these resolutions are hereby ratified, confirmed, and approved in all respects.

### Effective Date
RESOLVED FURTHER, that this written consent shall be effective as of the date first written above and shall be filed with the minutes of the Company.

## SIGNATURES
This written consent may be executed in one or more counterparts (including by PDF or DocuSign), each of which shall be an original and all of which together shall constitute one and the same instrument.

_______________________________
[Director Name 1]

_______________________________
[Director Name 2]

[Continue for all directors]

## EXHIBITS
- Exhibit A — Merger Agreement (form)
- Exhibit B — Disclosure Schedule (form)
- Exhibit C — Escrow Agreement (form)
- Exhibit D — Paying Agent Agreement (form)
- Exhibit E — Letter of Transmittal (form)
- Exhibit F — R&W Insurance Policy
- Exhibit G — Employment Agreements
- Exhibit H — Restrictive Covenant Agreements
- Exhibit I — Transition Services Agreement (form)
- Exhibit L — §280G Disclosure and Stockholder Consent
- Exhibit M — D&O Tail Policy Summary
- Exhibit N — Fee Schedule

---

# SECRETARY'S CERTIFICATE
I, [Name], the duly elected and qualified Secretary of [Entity Name], a [State] [Entity Type] (the "Company"), do hereby certify, in connection with the closing of the Transaction, as follows:

1. Attached as Exhibit 1 is a true, correct, and complete copy of the [Certificate of Incorporation / Articles of Organization] of the Company, as amended through and in effect on the date hereof.
2. Attached as Exhibit 2 is a true, correct, and complete copy of the Bylaws of the Company as amended through and in effect on the date hereof.
3. Attached as Exhibit 3 is a true, correct, and complete copy of the resolutions duly adopted by [the Board of Directors / the Stockholders] of the Company by [written consent dated [Date] / at a meeting held on [Date]], which resolutions are in full force and effect as of the date hereof and have not been amended, modified, or rescinded.
4. The persons named below are the duly elected, qualified, and acting officers of the Company holding the offices set forth opposite their names, and the signatures appearing opposite their names are their genuine signatures:

| Name | Office | Signature |
|---|---|---|
| [Name] | CEO | _________________ |
| [Name] | CFO | _________________ |
| [Name] | Secretary | _________________ |

5. Attached as Exhibit 4 is a [long-form / short-form] certificate of good standing for the Company from the Secretary of State of [State of Formation] dated within [N] days of the date hereof.

IN WITNESS WHEREOF, the undersigned has executed this Secretary's Certificate as of [Date].

_______________________________
[Name], Secretary
```

---

## Verification

- [ ] WHEREAS recitals identify transaction, documents, authority basis, and (for mergers) advisability determination.
- [ ] Each material action has a separate RESOLVED clause (no umbrella "approve the transaction" clauses).
- [ ] Statutory authority cited for stockholder approval, merger, asset sale (e.g., DGCL §251, §271).
- [ ] Form-of-document exhibits referenced with "substantially in the form" approval language.
- [ ] Omnibus authorization and ratification clauses included.
- [ ] §280G cleansing vote handled in a separate, properly-structured stockholder consent if applicable.
- [ ] §262 appraisal-rights notice authorization included if applicable.
- [ ] D&O tail policy approval included.
- [ ] Secretary's Certificate companion document drafted with incumbency, charter, bylaws, resolutions, good standing.
- [ ] No invented officer names, share counts, statutory citations, or document names; placeholders used.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Single "approve the transaction" resolution | Each material action gets its own RESOLVED clause; closing officer's certificate requires specificity |
| Approving a transaction document without attaching the form | Attach the form and use "substantially in the form attached as Exhibit X, with such changes as the officers executing the same may approve" language |
| Combining board approval and stockholder approval in one consent | DGCL §251 requires both; draft separately. Board declares advisable and recommends; stockholders adopt |
| §280G cleansing vote conducted as part of merger approval vote | §280G(b)(5) and Treas. Reg. §1.280G-1 Q&A-7 require a separate vote of disinterested stockholders with full disclosure; contingent on stockholder approval; payment subject to and contingent on the cleansing vote |
| Skipping §262 appraisal-rights notice in mergers requiring stockholder vote | DGCL §262(d)(1) notice is mandatory; failure can extend appraisal demand windows |
| Approving the merger without recommendation to stockholders | DGCL §251(b) requires the board to declare advisable and (in a stockholder-vote merger) recommend to stockholders |
| §253 short-form merger drafted as §251 long-form | Short-form merger (DGCL §253) of a 90%-owned subsidiary doesn't require minority stockholder vote; use the correct statutory pathway |
| §251(h) medium-form merger missing the offer-tender mechanics | §251(h) requires a successful tender offer for a majority of outstanding shares before the back-end merger; recite the offer completion |
| Asset deal that is "substantially all the assets" without §271 stockholder approval | DGCL §271 requires stockholder approval for sale of substantially all assets; analyze under Gimbel / Hollinger and approve accordingly |
| Resolutions not in force at closing (e.g., bylaws amended after resolutions) | Secretary's certificate certifies "in full force and effect as of the date hereof"; if anything changes between approval and closing, supplement |
| Wrong consent threshold (majority where supermajority required) | Check the charter for any supermajority requirement (e.g., for mergers, charter amendments); some companies have 2/3 or 75% requirements |
| Approving D&O tail at "commercially reasonable terms" without sizing | Reference the tail term (typically 6 years) and aggregate cost cap (typically 250–300% of annual premium); attach summary |
| Missing ratification clause | Include — covers prior officer actions taken in negotiation before the formal approval |
