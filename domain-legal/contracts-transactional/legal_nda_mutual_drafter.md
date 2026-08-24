---
title: "Mutual NDA Drafter"
category: legal/contracts-transactional
description: "Draft a mutual non-disclosure agreement with calibrated definition of Confidential Information, standard exclusions, term and survival, residuals treatment, return-or-destroy obligation, and IP / no-license language. Calibrated to evaluation, transaction-process, or operational-disclosure use."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: beginner
tags:
  - legal
  - contracts
  - nda
  - confidentiality
  - residuals
  - drafting
updated: "2026-05-11"
related_prompts:
  - domain-legal/contracts-transactional/legal_msa_drafter.md
  - domain-legal/contracts-transactional/legal_contract_review_full_redline.md
  - domain-legal/contracts-transactional/legal_clause_library_extractor.md
  - domain-legal/research/legal_research_memo_irac.md
---

**Purpose:** Draft a mutual non-disclosure agreement calibrated to use case (evaluation / transaction / operational), data sensitivity (general business / trade secret / personal data), and term. Output is a complete NDA ready for execution with no embedded markup or placeholders that survive.

**When to use:** Pre-transaction discussions, vendor evaluation, technology evaluation, hiring of a senior advisor, joint development discussions. For one-way NDAs (employee, contractor, recipient-only), use a unilateral form; this prompt produces mutual.

---

## Your Input

- **Parties:** [Both legal names + state of formation + entity type]
- **Use case:** [Evaluation of business opportunity / M&A or financing process / vendor or partner evaluation / joint development / operational disclosure]
- **State of governing law / venue:** [State]
- **Permitted purpose:** [Specific description — "to evaluate a potential commercial relationship for the supply of X" — narrow is better]
- **Information categories likely to be exchanged:** [Financial, technical, source code, customer lists, trade secrets, PII, employee data, roadmap]
- **Term (confidentiality period):** [Years from disclosure or from termination of NDA]
- **NDA duration (term of the agreement itself):** [Often 1–3 years; can be evergreen]
- **Residuals position:** [Include / exclude / narrow]
- **Trade-secret handling:** [Indefinite protection for trade secrets / treat as Confidential Information only]
- **Return-or-destroy:** [Return / destroy / both at recipient's option]
- **Permitted recipients:** [Affiliates / advisors / financing sources / employees on need-to-know]
- **Special restrictions:** [No solicitation of employees during NDA term; standstill (for M&A); export controls; sanctions]
- **Counterparty leverage:** [High / equal / low]

---

## Constraints

**Must:**
- Define **Confidential Information** broadly enough to cover oral, written, and observed disclosures, but narrowly enough to be defensible (information disclosed in connection with the Purpose; marking or follow-up confirmation for oral disclosures within 30 days).
- Include the **five standard exclusions** from Confidential Information: (i) publicly available, (ii) already known without obligation, (iii) independently developed without use of disclosed information, (iv) lawfully received from a third party without confidentiality obligation, (v) compelled disclosure (with notice and cooperation obligation).
- State **purpose** clearly and narrowly — use restrictions outside the Purpose are a separate covenant.
- State **term and survival**: NDA term (when new disclosures stop) and Confidentiality Term (how long obligations last for information disclosed during NDA term).
- Address **trade secrets** explicitly — most U.S. jurisdictions allow indefinite protection for trade secrets (DTSA + UTSA); the NDA term should not artificially cut this off.
- Specify **return-or-destroy** with carve-outs for: (a) one archival copy retained for legal/compliance, (b) automated backups not subject to ordinary access.
- Address **residuals** explicitly: include only if posture and use case support; otherwise exclude.
- Include **no-license clause**: nothing in the NDA grants any license to IP, except a narrow use-for-purpose license to Confidential Information.
- Include **compelled disclosure** procedure: notice (where legally permitted), cooperation, narrow disclosure.
- Include **no warranty / as-is** for the accuracy of Confidential Information — the discloser warrants nothing about the substance.
- Include **injunctive relief** acknowledgment — money damages are inadequate; equitable relief without bond (in jurisdictions that allow waiver).
- Include **no obligation to enter further agreements** — common for evaluation NDAs.

**Must Not:**
- Use a perpetual confidentiality term for non-trade-secret information (often unenforceable; some jurisdictions cap at 3–7 years for general business information).
- Define Confidential Information as "all information" without exclusions (overbroad and unenforceable).
- Omit the compelled-disclosure procedure — it converts subpoenas into breaches.
- Include a "non-disparagement" clause in a basic NDA (belongs elsewhere).
- Include a "non-circumvention" clause without clear scope — often overbroad and unenforceable.
- Convert the NDA into a teaming or exclusivity agreement.
- Invent statutes (DTSA, UTSA citations are acceptable but state-specific provisions need `[CITE: ...]`).
- Use generic "consult counsel" disclaimers.

---

## Use-Case Calibration

| Use Case | Term | Residuals | Standstill | Non-Solicit |
|---|---|---|---|---|
| Vendor / partner evaluation | NDA 1–2 yr; Conf 3–5 yr | Exclude | No | Optional |
| M&A or financing process | NDA 2 yr; Conf 3 yr | Exclude | Yes (12–18 mo) | Yes (12–24 mo) |
| Joint development discussion | NDA 2 yr; Conf 5 yr; trade-secret indefinite | Narrow if at all | No | Optional |
| Operational disclosure (vendor implementation) | NDA term = contract term; Conf 3–5 yr post | Exclude | No | Yes |
| Hiring senior advisor / consultant | NDA 1–2 yr; Conf 3 yr | Exclude | No | Yes |

---

## Instructions

1. **Frame.** Parties, effective date, recital identifying the Purpose.
2. **Definitions.** Confidential Information, Purpose, Representatives, Trade Secret (cross-reference DTSA / UTSA).
3. **Confidentiality obligations.** Use restriction (only for Purpose), care standard (same as own confidential, no less than reasonable), permitted recipients (Representatives on need-to-know who are bound by similar obligations).
4. **Exclusions.** The five standard exclusions.
5. **Compelled disclosure.** Notice (where legal), cooperation, narrow disclosure.
6. **No license.** No IP rights granted except limited use for Purpose.
7. **No warranty.** Confidential Information provided "as is."
8. **Term and survival.** NDA term + Confidentiality term + trade-secret indefinite protection.
9. **Return-or-destroy.** Mechanism, certification, carve-outs.
10. **Residuals** (if included). Narrow definition: general skills, ideas, know-how retained in unaided memory of personnel not specifically tasked to recall.
11. **Special provisions.** Standstill (M&A), non-solicit, export controls, sanctions, DTSA whistleblower notice (18 U.S.C. § 1833(b)).
12. **Remedies.** Money damages plus injunctive relief; acknowledgment of irreparable harm.
13. **General.** Governing law, venue, assignment (typically not without consent), notices, integration, counterparts, electronic signature, severability.
14. **Signature block.**

---

## Output Format

```markdown
MUTUAL NON-DISCLOSURE AGREEMENT

This Mutual Non-Disclosure Agreement ("Agreement") is entered into as of {Effective Date} by and between {Party A Legal Name}, a {state} {entity type} ("Party A"), and {Party B Legal Name}, a {state} {entity type} ("Party B") (each a "Party"; together, the "Parties").

WHEREAS, the Parties wish to explore {Purpose} (the "Purpose"); and
WHEREAS, in connection with the Purpose, each Party may disclose to the other certain Confidential Information;
NOW, THEREFORE, the Parties agree as follows:

1. DEFINITIONS
1.1 "Confidential Information" means any non-public information disclosed by one Party (the "Discloser") to the other (the "Recipient") in connection with the Purpose, in any form (oral, written, electronic, visual, or observed), whether or not marked confidential, that a reasonable person would understand to be confidential given the nature of the information and the circumstances of disclosure. Confidential Information includes, without limitation: technical, financial, business, customer, employee, marketing, and product information; software, source code, designs, specifications, and know-how; and any analyses, compilations, studies, or other documents prepared by Recipient that contain or reflect Confidential Information.
1.2 "Representatives" means a Party's directors, officers, employees, agents, attorneys, accountants, financial advisors, and other consultants with a need to know in connection with the Purpose, who are bound by written or professional confidentiality obligations no less protective than those in this Agreement.
1.3 "Trade Secret" has the meaning set forth in the Defend Trade Secrets Act (18 U.S.C. § 1839) and applicable state Uniform Trade Secrets Act.

2. USE AND DISCLOSURE
2.1 Use Restriction. Recipient will use Confidential Information solely for the Purpose and for no other purpose.
2.2 Disclosure Restriction. Recipient will not disclose Confidential Information to any third party except to its Representatives on a need-to-know basis for the Purpose. Recipient is responsible for any breach of this Agreement by its Representatives.
2.3 Care Standard. Recipient will protect Confidential Information using the same degree of care it uses for its own confidential information, but no less than reasonable care.

3. EXCLUSIONS
Confidential Information does not include information that:
(a) is or becomes publicly available through no fault of Recipient;
(b) was known to Recipient without obligation of confidentiality prior to disclosure;
(c) is independently developed by Recipient without use of or reference to Confidential Information, as evidenced by contemporaneous records;
(d) is lawfully received by Recipient from a third party not subject to an obligation of confidentiality; or
(e) is required to be disclosed by law, regulation, or valid legal process, subject to Section 4.

4. COMPELLED DISCLOSURE
If Recipient is required by law, regulation, or valid legal process to disclose Confidential Information, Recipient will, to the extent legally permitted, (a) promptly notify Discloser to allow Discloser to seek a protective order or other appropriate remedy; (b) cooperate with Discloser, at Discloser's expense, in seeking such remedy; and (c) disclose only the portion of Confidential Information legally required to be disclosed.

5. NO LICENSE; NO OBLIGATION
5.1 No License. Nothing in this Agreement grants any license to any intellectual property, except a limited, non-exclusive, non-transferable license to use Confidential Information solely for the Purpose.
5.2 No Obligation. Nothing in this Agreement obligates either Party to enter into any further agreement or transaction.
5.3 No Warranty. Confidential Information is provided "as is" without warranty of accuracy or completeness.

6. TERM AND SURVIVAL
6.1 NDA Term. This Agreement is effective from the Effective Date and continues for {N} years, unless earlier terminated by either Party on thirty (30) days' written notice.
6.2 Confidentiality Survival. Recipient's obligations with respect to Confidential Information continue for {N} years following the date of disclosure of such information. Notwithstanding the foregoing, obligations with respect to Trade Secrets continue for so long as the information qualifies as a Trade Secret under applicable law.

7. RETURN OR DESTRUCTION
Upon Discloser's written request or termination of this Agreement, Recipient will, at Discloser's option, return or destroy all Confidential Information in its possession and certify such return or destruction in writing within thirty (30) days. The following are excepted: (a) one archival copy retained by Recipient's legal department for compliance purposes, subject to continuing confidentiality obligations; and (b) automated backups not subject to ordinary access, which will be destroyed in the ordinary course.

8. {OPTIONAL — RESIDUALS}
8.1 Residuals. Notwithstanding Section 2, Recipient may use Residuals for any purpose without obligation to Discloser. "Residuals" means information in non-tangible form that may be incidentally retained in the unaided memory of Recipient's Representatives who have had access to Confidential Information in the ordinary course of the Purpose, provided that nothing in this Section permits use of Discloser's Trade Secrets, patents, copyrights, or trademarks.

9. {OPTIONAL — STANDSTILL}
For a period of {12–18} months from the Effective Date, neither Party will, without the prior written consent of the other, acquire or propose to acquire any equity securities of the other Party.

10. {OPTIONAL — NON-SOLICITATION}
During the term of this Agreement and for {N} months thereafter, neither Party will solicit for employment any employee of the other Party with whom such Party has had material contact in connection with the Purpose; provided that general advertisements and recruitment efforts not specifically directed at such employees are permitted.

11. DTSA NOTICE
Pursuant to 18 U.S.C. § 1833(b), an individual will not be held criminally or civilly liable under any federal or state trade secret law for the disclosure of a trade secret that is made (a) in confidence to a federal, state, or local government official or to an attorney, and solely for the purpose of reporting or investigating a suspected violation of law; or (b) in a complaint or other document filed in a lawsuit or other proceeding, if such filing is made under seal.

12. REMEDIES
The Parties acknowledge that money damages may be inadequate to remedy a breach of this Agreement, and that the non-breaching Party is entitled to seek equitable relief, including injunctive relief and specific performance, without the requirement of posting a bond, in addition to any other remedies at law or in equity.

13. GENERAL
13.1 Governing Law. This Agreement is governed by the laws of {state}, without regard to conflict-of-laws principles.
13.2 Venue. The Parties consent to the exclusive jurisdiction of the state and federal courts located in {county/district, state}.
13.3 Assignment. Neither Party may assign this Agreement without the prior written consent of the other, except to a successor in interest by merger, acquisition, or sale of all or substantially all assets.
13.4 Notices. Notices must be in writing and delivered by hand, certified mail, or overnight courier to the addresses set forth below the signature block.
13.5 Integration. This Agreement constitutes the entire agreement of the Parties with respect to the Purpose and supersedes all prior or contemporaneous communications.
13.6 Severability. If any provision is held unenforceable, the remaining provisions remain in full force.
13.7 No Waiver. No waiver is effective unless in writing.
13.8 Counterparts; Electronic Signature. This Agreement may be executed in counterparts, including by electronic signature under E-SIGN and UETA.

SIGNATURES
{Party A block} | {Party B block}
```

---

## Verification

- [ ] Purpose stated narrowly and specifically.
- [ ] Five standard exclusions present.
- [ ] Compelled-disclosure procedure includes notice and cooperation.
- [ ] No-license clause present.
- [ ] NDA term and Confidentiality term separately stated.
- [ ] Trade-secret indefinite protection preserved.
- [ ] Return-or-destroy mechanism with archival and backup carve-outs.
- [ ] Residuals included or excluded consistent with posture (not silently included).
- [ ] DTSA whistleblower notice included.
- [ ] Injunctive relief / irreparable harm acknowledgment present.
- [ ] Governing law and venue specified.
- [ ] No invented citations beyond DTSA/UTSA framework.
- [ ] No restated MSA-style provisions (indemnity, LoL, etc.) — NDAs do not need them.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Perpetual confidentiality term for all information | Most non-trade-secret information should have a defined term (3–7 years typical); trade secrets get indefinite protection separately |
| Defining Confidential Information as "all information disclosed" without need-to-mark or follow-up confirmation | Default should cover both marked and reasonably-understood-as-confidential; oral disclosures often require 30-day written confirmation in stricter forms |
| Omitting the compelled-disclosure procedure | Without it, a subpoena response is a breach; always include notice + cooperation + narrow disclosure |
| Including residuals in a sensitive trade-secret context | Residuals gut trade-secret protection; exclude or narrowly scope |
| Standstill in a non-M&A NDA | Standstill belongs in M&A or financing-process NDAs only; do not include in vendor-evaluation NDAs |
| Non-circumvention clause without defined scope | Often unenforceable; replace with non-solicitation of customers or employees with defined scope |
| Omitting the DTSA whistleblower notice | 18 U.S.C. § 1833(b) requires this notice for the Discloser to recover punitive damages or attorneys' fees under DTSA — always include |
| Restating MSA-level provisions in an NDA | NDA should not include indemnity, LoL, or warranties — keep narrow |
| Treating a one-way disclosure scenario as mutual | If only one party will disclose, use a unilateral form; mutual creates obligations on the discloser that don't exist |
| Auto-renewal of NDA term | NDAs typically should not auto-renew; require affirmative extension |
| "Return or destroy at Recipient's option" without retention carve-outs | Always include archival + backup carve-outs; otherwise certification of destruction is unworkable |
| Failing to specify "without bond" for injunctive relief | Some jurisdictions require bond absent waiver; specify if local law permits waiver |
