---
title: "Privilege Review Protocol Designer"
category: legal/discovery
description: "Design a defensible privilege-review protocol for large document productions: TAR/keyword/seed-set strategy, reviewer training, sampling and validation thresholds, privilege-log architecture, and clawback procedure."
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
  - discovery
  - privilege
  - ediscovery
  - tar
updated: "2026-05-11"
related_prompts:
  - domain-legal/discovery/legal_privilege_log_generator.md
  - domain-legal/discovery/legal_document_review_coding_taxonomy.md
  - domain-legal/discovery/legal_ediscovery_custodian_interview.md
---

**Purpose:** Design a privilege-review protocol for a specific production with defensible defaults: how privileged material is identified (TAR, keyword, seed set), how reviewers are trained, how sampling validates the review, how the log is generated, and how clawbacks are handled under FRE 502(d) or the state equivalent.

**When to use:** Large-volume productions (≥50,000 documents), regulatory productions, productions where adverse counsel has a history of challenging logs, productions where attorney-client and work-product analyses are non-trivial.

---

## Your Input

- **Matter / posture:** [Civil / regulatory; plaintiff / defendant / producing party]
- **Jurisdiction & privilege rules:** [Federal common law; state law; choice-of-law per FRE 501]
- **Production volume:** [Document count, GB, custodian count]
- **Date range:** [Production scope]
- **Privilege categories at play:** [Attorney-client; work product (opinion vs fact); joint defense / common interest; spousal; clergy; trade secret protective designations]
- **Counsel population:** [Inside counsel names; outside counsel firms; foreign counsel raising 502(b)(2) issues]
- **Tooling:** [Relativity, Reveal, DISCO, Everlaw — and TAR engine if any]
- **502(d) order status:** [Entered / negotiating / declined]
- **Protective order tier:** [Confidential, AEO, Source Code, etc.]
- **Opposing counsel posture:** [Aggressive / collaborative; prior log challenges]
- **Deadline & budget:** [Production date; budget envelope]

---

## Constraints

**Must:**
- Specify a **defensible methodology** (TAR 2.0 / TAR 1.0 / keyword + targeted review / linear review) with rationale tied to volume, time, and budget.
- Define the **privilege seed set** and how it is built (counsel name list, law-firm domain list, common-interest party domains).
- Build a **reviewer training packet** with privilege-category definitions, examples, and quality-control rules.
- Define **sampling and validation thresholds** (e.g., elusion testing on null set; recall/precision targets).
- Specify the **log architecture** (categorical vs document-by-document; metadata fields; redaction protocol).
- Build the **clawback workflow** under FRE 502(d) or applicable equivalent.
- Define **escalation paths** for ambiguous documents (second-level review, counsel review, withhold-pending-resolution).

**Must Not:**
- Treat TAR as a substitute for second-level privilege review by counsel.
- Withhold non-privileged "highly sensitive" material under a privilege flag — sensitivity ≠ privilege.
- Log privilege without a basis identifying privilege category, sender, recipients, and subject matter.
- Promise that a 502(d) order eliminates the need for reasonable steps — courts still require them.
- Apply attorney-client to communications where the predominant purpose is business, not legal, advice.

---

## Instructions

1. **Methodology selection.** Apply the decision matrix:
   - <10K docs → targeted/linear review
   - 10K–100K → keyword + counsel/domain hit + reviewer pass
   - 100K–1M → TAR (CAL / CAL 2.0) with privilege focus, then reviewer second pass
   - >1M → multi-stage TAR with statistical validation
2. **Build the privilege seed set.**
   - Counsel name list (inside + outside, foreign)
   - Domain list (law-firm domains, common-interest parties)
   - Subject-line patterns ("Privileged & Confidential," "Attorney-Client," request-for-advice language)
   - Common-interest party list (with the underlying agreement supplied or flagged)
3. **Define reviewer training.**
   - Attorney-client: client + attorney + confidentiality + predominant legal purpose
   - Work product: anticipation of litigation; opinion vs fact distinction
   - Common interest / joint defense: agreement scope; what falls in vs out
   - Inadvertent disclosure: examples
   - Coding decisions with examples of each
4. **Set sampling protocol.**
   - Null-set elusion sample: random 384 (or per power calc) → reviewed for missed privilege
   - Privilege-flag sample: random N from withheld set → reviewed for over-claims
   - Targets: ≥{X}% recall on privilege; ≤{Y}% over-claim rate
5. **Design the log.**
   - Fields: Bates, date, sender, recipients (To/CC/BCC), counsel-status flag, subject, privilege type, basis, redaction marker, custodian
   - Categorical logging acceptable where supported by local rule (e.g., communications with counsel re: subject matter X during date range Y)
6. **Clawback workflow.**
   - 502(d) order language reference
   - Discovery of inadvertent production → notice within {X} days
   - Recipient obligations (sequester, return/destroy, no use)
   - Court-resolution path if dispute
7. **Output the full protocol** plus a one-page reviewer card.

---

## Output Format

```markdown
# PRIVILEGE REVIEW PROTOCOL — {Matter}

## 1. Methodology
- Approach: {TAR 2.0 / keyword+review / linear}
- Rationale: {volume, time, budget, opposing-counsel posture}

## 2. Privilege Seed
### Counsel List
| Name | Role | Email Domain |
|---|---|---|

### Domains
- Law firms: {list}
- Common-interest parties: {list, agreement ref}

### Subject Patterns
- {regex / phrase list}

## 3. Reviewer Training Packet
### A. Attorney-Client
- Elements: {client + attorney + confidentiality + legal purpose}
- Examples: {2 privileged, 2 non-privileged}
### B. Work Product
- Anticipation of litigation triggers: {events}
- Opinion vs fact: {definitions; examples}
### C. Common Interest
- Agreement scope: {ref}
- In-scope vs out: {examples}
### D. Redaction Rules
- {Inline redaction labels; metadata redaction handling}

## 4. Sampling & Validation
| Sample | Source | Size | Reviewer | Target | Action if Off-Target |
|---|---|---|---|---|---|
| Null-set elusion | Not-privileged set | 384 | Senior reviewer | ≥95% recall | Retrain; re-run |
| Over-claim audit | Withheld set | 200 | Counsel | ≤5% over-claim | Demote false positives |

## 5. Log Architecture
- Format: {document-by-document / categorical / hybrid}
- Fields: {schema}
- Redaction marker: {convention}

## 6. Clawback Workflow
- 502(d) order: {entered / pending}
- Discovery → notice deadline: {X days}
- Recipient obligations: {return, sequester, no use}
- Dispute resolution: {court / special master}

## 7. Reviewer One-Page Card
{Boxed quick reference}
```

---

## Verification

- [ ] Methodology selection is tied to volume, time, and budget — not a default choice.
- [ ] Seed set covers counsel names, domains, common-interest parties, and subject-line patterns.
- [ ] Reviewer training packet defines each privilege category with examples.
- [ ] Sampling has both elusion and over-claim audits with numeric targets.
- [ ] Log architecture identifies required fields and supports local-rule compliance.
- [ ] Clawback workflow references applicable 502(d) order and notice timeline.
- [ ] Escalation paths for ambiguous documents are defined.
- [ ] Predominant-purpose test addressed for business-vs-legal communications.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Withholding business communications because counsel is CC'd | Privilege requires predominant legal purpose, not mere counsel presence |
| Treating all in-house counsel email as privileged | In-house counsel acting in business roles is not protected — analyze role at time of communication |
| Logging "communication with counsel re: legal advice" with no other detail | Logs require sender, recipients, date, subject matter, and basis — categorical only where rule allows |
| Sensitivity ≠ privilege | Highly sensitive non-privileged material must be produced with appropriate confidentiality designation |
| Common-interest claim without a written agreement | Court will not infer common interest from convenience — require the agreement or document the basis |
| Relying on 502(d) order as a substitute for reasonable steps | Courts still examine the protocol; 502(d) limits waiver consequences, not the duty |
| Sampling only on the withheld set | Elusion (null-set) sampling catches false negatives, which are the bigger waiver risk |
| TAR results applied without a counsel second pass on privilege | Privilege coding requires counsel judgment, not algorithm output alone |
