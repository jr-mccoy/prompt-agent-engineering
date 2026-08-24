---
title: "GDPR Data Processing Addendum Drafter"
category: legal/contracts-transactional
description: "Draft a GDPR-compliant Data Processing Addendum with Article 28 obligations, Standard Contractual Clauses for cross-border transfers, sub-processor flow-down, audit rights, breach notification, and data return/deletion. Posture-calibrated for controller or processor."
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
  - contracts
  - gdpr
  - data-protection
  - dpa
  - sccs
  - privacy
updated: "2026-05-11"
related_prompts:
  - domain-legal/contracts-transactional/legal_msa_drafter.md
  - domain-legal/contracts-transactional/legal_saas_subscription_agreement_drafter.md
  - domain-legal/contracts-transactional/legal_contract_review_full_redline.md
  - domain-legal/research/legal_research_memo_irac.md
---

**Purpose:** Draft a Data Processing Addendum (DPA) attached to an MSA, SaaS agreement, or other principal contract, covering GDPR Article 28 processor obligations, EU Standard Contractual Clauses (SCCs) for international transfers, UK IDTA / UK Addendum where applicable, sub-processor flow-down, audit rights, breach notification, and data return / deletion. Output is posture-calibrated (controller / processor) and references the principal contract correctly.

**When to use:** Principal contract involves processing of EU / UK / EEA personal data by the counterparty as processor (e.g., SaaS, managed services, analytics, customer-support outsourcing). Use the SaaS or MSA drafter for the principal contract. For pure US data (no EU nexus), a US-only DPA is shorter; this prompt covers the full EU framework.

---

## Your Input

- **Principal contract:** [MSA, SaaS Agreement, or other — reference date and parties]
- **Posture:** [Controller (customer) OR Processor (supplier)]
- **Data exporter location:** [EEA / UK / Switzerland / other]
- **Data importer location:** [Country of importer; adequacy status]
- **Adequacy decision applicable:** [Yes (no SCCs needed) / No (SCCs required)]
- **Module of SCCs:** [Controller-to-Processor (Module 2) / Processor-to-Subprocessor (Module 3) / Processor-to-Controller (Module 4) / Controller-to-Controller (Module 1)]
- **UK transfers:** [Yes — include UK Addendum / No]
- **Swiss transfers:** [Yes — include Swiss FADP adjustments / No]
- **Categories of data subjects:** [Customer employees / customer end-users / website visitors / etc.]
- **Categories of personal data:** [Name, email, IP address, device ID, employment data, financial data, health data, special categories per GDPR Art. 9]
- **Special categories or criminal-conviction data:** [Yes/No — if yes, additional safeguards required]
- **Processing purposes:** [Listed in principal contract or summarized here]
- **Retention period:** [Specific or "duration of principal contract"]
- **Sub-processors:** [Approved list / general authorization with notice / case-by-case approval]
- **Audit rights:** [Annual / on incident / on regulator inquiry]
- **Breach notification timeline:** [Hours after processor awareness]
- **Liability cap interplay:** [DPA capped under principal contract LoL / separate cap / uncapped for data-protection breaches]
- **TIA (Transfer Impact Assessment) completed:** [Yes — reference / No — flag for completion]

---

## Constraints

**Must:**
- Include all eight categories of Article 28(3) processor obligations: (a) process only on documented instructions including for transfers; (b) confidentiality commitments from personnel; (c) Article 32 security measures; (d) sub-processor conditions (Article 28(2) and (4)); (e) cooperation in fulfilling data-subject rights (Articles 12–22); (f) assistance with Articles 32–36 obligations; (g) deletion or return at end of services; (h) information sufficient for controller to demonstrate compliance + audits.
- Reference the **EU Commission 2021 SCCs** (Commission Implementing Decision (EU) 2021/914) with the correct Module selected.
- Where UK transfers occur, attach the **ICO International Data Transfer Addendum** (UK Addendum) or the UK IDTA.
- Where Swiss data is involved, include Swiss FADP adjustments (references to FDPIC, Swiss law overlay).
- Include a **Transfer Impact Assessment (TIA)** reference and require cooperation in updating.
- Specify **breach notification timing** ("without undue delay and in any event within {N} hours" — typical 24–72 hours).
- Specify **sub-processor mechanism**: list of approved sub-processors as attachment; notification timing for changes (typically 14–30 days); controller objection right.
- Specify **audit rights**: scope, frequency, advance notice, cost, alternative of third-party audit reports (SOC 2 Type II, ISO 27001).
- Specify **data return and deletion** at end of processing with certification.
- Include **liability section** that interplays clearly with principal contract LoL — GDPR fines, regulator penalties, and data-subject claims are common cap carve-outs.
- Use defined terms consistent with GDPR Article 4: "Controller," "Processor," "Sub-processor," "Data Subject," "Personal Data," "Processing," "Personal Data Breach," "Supervisory Authority."

**Must Not:**
- Use outdated 2010 SCCs (no longer valid after December 27, 2022 transition deadline).
- Mix SCC modules — pick one Module per data flow.
- Insert the SCCs as paraphrased text — they must be attached verbatim as an annex.
- Use indemnification language that contradicts SCC Clause 12 (which has its own liability mechanism).
- Cap liability for the SCCs' Section III (data subjects' rights as third-party beneficiaries) in a way that would defeat the SCCs.
- Reference the UK GDPR without confirming UK Addendum or IDTA is attached for UK flows.
- Invent regulator-specific guidance. Use `[CITE: ...]` for specific guidance documents.
- Use generic disclaimers about consulting counsel.

---

## Posture Calibration Reference

| Provision | Controller (Customer) Posture | Processor (Supplier) Posture |
|---|---|---|
| Sub-processor approval | Specific list + prior written consent for new | General authorization + 30-day notice |
| Audit | On-site at controller cost, annual + on incident | Third-party audit report (SOC 2 / ISO) acceptable, on-site only on regulator request |
| Breach notification timing | 24 hours | 72 hours |
| Assistance with data-subject requests | At processor cost up to reasonable threshold | At controller cost with rate card |
| Liability for fines and penalties | Outside LoL, allocated to responsible party | Within LoL or capped separately |
| Return / deletion | Both options, controller choice, certification within 30 days | Deletion only, certification within 60–90 days, archival carve-out |
| Documentation of processing | Provided on request, no cost | Provided on request, reasonable cost |

---

## Instructions

1. **Anchor and definitions.** Reference principal contract; incorporate by reference defined terms; add GDPR Article 4 terms.
2. **Subject matter and details.** Article 28(3) opening: subject matter, duration, nature, purpose, types of data, categories of data subjects, controller obligations. Tabular format works well.
3. **Processor obligations.** Walk through Article 28(3)(a)–(h) systematically.
4. **Security.** Article 32 measures — reference Security Addendum if separate; specify minimum technical/organizational measures (encryption in transit/at rest, access controls, logging, vulnerability management, incident response, personnel training).
5. **Sub-processors.** Mechanism for engagement (approved list + notice + objection right); flow-down requirement (same obligations); liability for sub-processor acts.
6. **Data subject rights.** Cooperation in responding to access, rectification, erasure, restriction, portability, objection, automated-decision objections.
7. **Personal data breach.** Definition (Article 4(12)); processor notification to controller without undue delay; content of notification (categories of data subjects, categories and approximate number of personal data records, likely consequences, measures taken); cooperation with controller's Article 33–34 obligations.
8. **DPIA assistance.** Cooperation in Article 35 data protection impact assessments where required.
9. **International transfers.** SCC Module selection; UK Addendum / IDTA if applicable; TIA reference; supplementary measures (encryption, pseudonymization, organizational measures).
10. **Audit rights.** Scope, frequency, notice, cost, third-party audit acceptance.
11. **Return and deletion.** At end of services or earlier on controller instruction; certification; archival and backup carve-out.
12. **Liability and indemnity.** Interplay with principal contract LoL; carve-outs for regulator fines, data-subject claims; SCC Clause 12 preserved.
13. **Annexes.** Annex I (List of Parties, Description of Transfer, Competent Supervisory Authority); Annex II (Technical and Organizational Measures); Annex III (Sub-processor List); UK Addendum if applicable.
14. **Signature block** (DPAs typically incorporated by reference into principal contract signature; standalone signature if separately executed).

---

## Output Format

```markdown
DATA PROCESSING ADDENDUM

This Data Processing Addendum ("DPA") supplements and is incorporated into the {Principal Contract Name} dated {Date} (the "Principal Contract") between {Controller Legal Name} ("Controller") and {Processor Legal Name} ("Processor"). Capitalized terms not defined herein have the meanings set forth in the Principal Contract or, where applicable, in the GDPR.

1. DEFINITIONS
1.1 "GDPR" means Regulation (EU) 2016/679.
1.2 "UK GDPR" means the GDPR as incorporated into UK law by the Data Protection Act 2018.
1.3 "Personal Data," "Processing," "Controller," "Processor," "Sub-processor," "Data Subject," "Personal Data Breach," and "Supervisory Authority" have the meanings set forth in Article 4 of the GDPR.
1.4 "SCCs" means the Standard Contractual Clauses approved by Commission Implementing Decision (EU) 2021/914 of 4 June 2021.
1.5 "UK Addendum" means the International Data Transfer Addendum to the EU Commission Standard Contractual Clauses issued by the UK Information Commissioner's Office.

2. SUBJECT MATTER AND DETAILS OF PROCESSING
| Item | Detail |
|---|---|
| Subject matter | {description} |
| Duration | Duration of the Principal Contract |
| Nature and purpose | {description} |
| Type of Personal Data | {categories} |
| Categories of Data Subjects | {categories} |
| Special categories (Art. 9) | {yes/no — if yes, additional safeguards in Section 5} |

3. PROCESSOR OBLIGATIONS (Article 28(3))
3.1 Processing Only on Instructions. Processor will process Personal Data only on documented instructions from Controller, including with regard to transfers, unless required by EU or Member State law (in which case Processor will inform Controller unless prohibited).
3.2 Confidentiality. Processor will ensure that persons authorized to process Personal Data are bound by written or statutory confidentiality obligations.
3.3 Security. Processor will implement the technical and organizational measures described in Annex II.
3.4 Sub-processors. As set forth in Section 6.
3.5 Data Subject Rights. As set forth in Section 7.
3.6 Assistance. Processor will assist Controller in complying with Articles 32–36, taking into account the nature of Processing and the information available to Processor.
3.7 Return or Deletion. As set forth in Section 11.
3.8 Information and Audits. As set forth in Section 10.

4. CONTROLLER OBLIGATIONS
Controller represents that it has provided required notices to and obtained required consents from Data Subjects, and that its instructions to Processor comply with applicable Data Protection Law.

5. SECURITY MEASURES
Processor will implement and maintain the technical and organizational measures set forth in Annex II, including, at a minimum: encryption in transit and at rest; role-based access controls; logging and monitoring; vulnerability management; secure software development; personnel training; incident response; business continuity.

6. SUB-PROCESSORS
6.1 General Authorization. Controller {grants general authorization for Processor to engage sub-processors listed in Annex III / requires prior written approval for each sub-processor}.
6.2 Notice of Changes. Processor will provide {14 / 30} days' prior written notice of any addition or replacement of sub-processors.
6.3 Objection. Controller may object on reasonable grounds. If the Parties cannot resolve the objection, Controller may terminate the affected Services without penalty.
6.4 Flow-Down. Processor will impose on each sub-processor data protection obligations no less protective than those set forth in this DPA.
6.5 Liability. Processor remains fully liable to Controller for the performance of each sub-processor's obligations.

7. DATA SUBJECT RIGHTS
Processor will, taking into account the nature of the Processing, assist Controller by appropriate technical and organizational measures, insofar as possible, in fulfilling Controller's obligation to respond to requests from Data Subjects exercising rights under Chapter III of the GDPR (access, rectification, erasure, restriction, portability, objection, automated decision-making).

8. PERSONAL DATA BREACH
8.1 Notification. Processor will notify Controller of any Personal Data Breach without undue delay and in any event within {24 / 72} hours of becoming aware.
8.2 Content. The notification will include, to the extent known: (a) nature of the Breach, including categories and approximate number of Data Subjects and Personal Data records concerned; (b) likely consequences; (c) measures taken or proposed; (d) contact point.
8.3 Cooperation. Processor will cooperate with Controller and provide reasonable assistance in Controller's compliance with Articles 33 and 34.

9. DATA PROTECTION IMPACT ASSESSMENTS
Processor will provide reasonable assistance to Controller in conducting any DPIA required under Article 35 and in consulting with the Supervisory Authority under Article 36.

10. AUDITS
10.1 Information. Processor will make available to Controller information necessary to demonstrate compliance with this DPA.
10.2 Audit Reports. Processor's then-current SOC 2 Type II or ISO 27001 report constitutes an acceptable audit response.
10.3 On-Site Audits. Controller may conduct on-site audits at its cost, on {30 / 60} days' prior notice, no more than once per year, subject to Processor's reasonable confidentiality and operational restrictions. The frequency limit does not apply following a Personal Data Breach or on Supervisory Authority demand.

11. INTERNATIONAL TRANSFERS
11.1 SCCs. To the extent Processor transfers Personal Data subject to the GDPR to a country outside the EEA without an adequacy decision, the SCCs (Module {2/3/4}) are incorporated by reference and form part of this DPA. The Parties agree the SCC Annexes are as set forth in Annex I (Parties and Description of Transfer) and Annex II (Security Measures).
11.2 UK Transfers. For transfers subject to UK GDPR, the UK Addendum (attached as Annex IV) is incorporated and forms part of this DPA. The UK Addendum Table 4 is completed with {Importer / Exporter / both} able to terminate.
11.3 Swiss Transfers. For transfers subject to the Swiss FADP, references to the GDPR are deemed to include the FADP, references to the Supervisory Authority include the FDPIC, and "Member State" is deemed to include Switzerland.
11.4 TIA. The Parties acknowledge that a Transfer Impact Assessment has been conducted and is documented {at location / attached as Annex V}. Each Party will cooperate in updating the TIA as required by changes in applicable law or circumstances.
11.5 Supplementary Measures. Processor implements supplementary measures including {encryption, pseudonymization, organizational measures} to mitigate risks identified in the TIA.

12. RETURN AND DELETION
Upon termination of the Principal Contract or earlier on Controller's instruction, Processor will, at Controller's choice, return or delete all Personal Data and certify deletion in writing within {30 / 60 / 90} days. Processor may retain Personal Data to the extent and for the period required by applicable law, subject to continuing protections.

13. LIABILITY
13.1 General. Liability under this DPA is governed by the Principal Contract, except as expressly modified in this Section 13.
13.2 Carve-Outs. {Regulator fines, data-subject claims, third-party-beneficiary claims under the SCCs} are {excluded from / subject to a separate cap in / capped under} the Principal Contract LoL.
13.3 SCC Clause 12. Nothing in this DPA limits the operation of SCC Clause 12 (Liability) as between Processor and Data Subjects.

14. GENERAL
14.1 Order of Precedence. In case of conflict, the SCCs control over this DPA, this DPA controls over the Principal Contract.
14.2 Governing Law. As set forth in the Principal Contract, except as required by the SCCs.
14.3 Updates. The Parties will negotiate in good faith any amendments necessary to reflect changes in Data Protection Law.

ANNEX I — LIST OF PARTIES, DESCRIPTION OF TRANSFER, COMPETENT SUPERVISORY AUTHORITY
{Parties identified as Data Exporter / Data Importer; description; competent supervisory authority for SCC Module purposes}

ANNEX II — TECHNICAL AND ORGANIZATIONAL MEASURES
{Detailed list per SCC Annex II requirements}

ANNEX III — SUB-PROCESSORS
{List with name, location, processing description}

ANNEX IV — UK INTERNATIONAL DATA TRANSFER ADDENDUM
{If applicable}

ANNEX V — TRANSFER IMPACT ASSESSMENT REFERENCE
{Location and date}
```

---

## Verification

- [ ] All Article 28(3)(a)–(h) processor obligations covered.
- [ ] Correct SCC Module selected and incorporated; Annex I and II completed.
- [ ] UK Addendum attached for UK transfers; Swiss adjustments where applicable.
- [ ] TIA referenced and cooperation in updates required.
- [ ] Breach notification timing specified (24–72 hours).
- [ ] Sub-processor mechanism (general authorization vs specific approval) consistent with posture.
- [ ] Audit rights include both information and on-site mechanisms, with third-party audit acceptance.
- [ ] Return / deletion mechanism with certification and carve-outs.
- [ ] Liability interplay with Principal Contract LoL is explicit.
- [ ] No invented regulator guidance; placeholders for missing data.
- [ ] Order of precedence clause resolves SCCs vs DPA vs Principal Contract conflicts.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Using 2010 SCCs (Decision 87/2001 or 2010/87) | These were invalidated/transitioned; use 2021 SCCs (Commission Implementing Decision (EU) 2021/914) |
| Selecting Module 2 (Controller-to-Processor) for a Processor-to-Subprocessor flow | Match the SCC Module to the data flow; Module 3 for P-to-Sub |
| Paraphrasing the SCCs in the DPA body | SCCs must be incorporated verbatim as an annex, not paraphrased; paraphrase has no legal effect |
| Omitting the UK Addendum for UK transfers post-Brexit | UK is no longer covered by EU SCCs; attach the ICO UK Addendum or use the UK IDTA |
| Capping data-protection liability under the Principal Contract LoL without addressing GDPR fines | GDPR fines are often outside LoL or have a separate cap; address explicitly |
| Sub-processor mechanism with no flow-down requirement | Article 28(4) requires flow-down of substantially same obligations; always include |
| Audit rights with only on-site option | Most processors operate at scale; SOC 2 / ISO 27001 reports are acceptable for routine audits; reserve on-site for incident or regulator demand |
| Breach notification "as soon as practicable" without a number | Specify hours; 24 is aggressive, 72 is the GDPR Article 33 controller-to-supervisory-authority outer bound |
| Omitting the TIA reference | Post-Schrems II, TIAs are an expected practice for non-adequacy-country transfers |
| Generic data-subject rights cooperation without specifying cost allocation | Specify whether assistance is at processor cost (controller posture) or controller cost (processor posture); leaves disputes otherwise |
| Treating special categories (Art. 9) as ordinary personal data | Special categories require additional Art. 9 safeguards; flag in Section 2 and require additional measures in Annex II |
| Missing Annex II detail | Annex II must include actual TOMs, not "industry standard"; SCCs require specificity |
