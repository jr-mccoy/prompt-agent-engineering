---
title: "Vendor Privacy Assessment — DPA, SCC, and Transfer Impact Review"
category: legal/privacy-data
description: "Review a vendor's (processor's or service provider's) privacy paper from the customer side: role characterization, the vendor's DPA against the supplied regime's mandatory processor terms, the international-transfer mechanism and SCC module fit, the transfer impact assessment (TIA) and supplementary measures, sub-processor flow-down, and US state-law service-provider terms. Ends in accept / accept-with-changes / escalate / reject with a redline list. Reviews the vendor's paper; does not draft a DPA from scratch."
techniques:
  - DS-01
  - CM-02
  - RT-02
  - QA-05
  - QA-01
difficulty: advanced
tags:
  - legal
  - privacy
  - vendor-management
  - dpa
  - sccs
  - transfer-impact-assessment
  - sub-processors
  - third-party-risk
  - signing-new-supplier
updated: "2026-09-24"
reasoning:
  styles: [analytic, evaluative, systematic]
  stakes: high
  horizon: days
  uncertainty: ambiguity
  evidence_quality: mixed
  domain_complexity: regulated
  collaboration: small_team
  output_format: [structured, matrix]
  user_role: [attorney, privacy_counsel, procurement_counsel]
related_prompts:
  - domain-legal/contracts-transactional/legal_dpa_gdpr_drafter.md
  - domain-legal/contracts-transactional/legal_subcontractor_flow_down_check.md
  - domain-legal/privacy-data/legal_privacy_impact_assessment_dpia.md
  - domain-risk/risk_vendor_security_questionnaire_review.md
---

# Vendor Privacy Assessment

**Objective:** Decide whether a vendor's privacy terms and transfer arrangements are adequate for the personal data the vendor will process, and what must change before signature. The assessment characterizes the vendor's role, checks the vendor's DPA against the supplied regime's mandatory processor / service-provider terms, tests the transfer mechanism and SCC module against the actual data flow, reviews the TIA and supplementary measures, verifies sub-processor flow-down, and produces a disposition with a prioritized redline list.

**When to use:**
- Procurement or legal receives a vendor's standard DPA, SCCs, sub-processor list, and TIA for a new engagement.
- An existing vendor adds a sub-processor, changes hosting region, or updates its DPA.
- A periodic vendor-privacy recertification is due.

**Distinct from:**
- `domain-legal/contracts-transactional/legal_dpa_gdpr_drafter.md` — drafts a DPA from your own position. This prompt reviews the vendor's paper and the transfer analysis behind it.
- `domain-risk/risk_vendor_security_questionnaire_review.md` — grades the vendor's security answers. Use it alongside; this prompt covers legal terms and transfers, relying on that review for technical measures.
- `domain-legal/contracts-transactional/legal_subcontractor_flow_down_check.md` — general flow-down of prime-contract obligations; this prompt checks data-protection flow-down specifically.
- `domain-agentic-resources/skills/security/gdpr-data-handling` — building systems, not reviewing vendor contracts.

---

## Your Input

- **Regime(s):** [EU GDPR / UK GDPR / Swiss FADP / US state comprehensive privacy law(s) / sectoral (e.g., health, financial) / other]
- **Regime text supplied:** [Mandatory processor / service-provider terms, transfer rules, and any official SCC text or transfer-tool text, with version dates]
- **Engagement:** [Service, purpose, data subjects, data categories (flag special-category / sensitive), volume, access model (vendor staff access? support access from which countries?)]
- **Data flow:** [Exporter location(s), hosting region(s), support locations, sub-processor locations]
- **Vendor documents:** [DPA, SCCs / transfer addendum, sub-processor list, TIA or transfer-risk summary, security annex / TOMs, certifications, government-access transparency report]
- **Customer's posture and leverage:** [Deal size, alternatives, internal playbook positions]
- **Security review outcome (if done):** [Summary from the security team]

---

## Constraints

**Must:**
- Characterize the vendor's role for each processing activity (processor / service provider / independent controller / joint controller); flag any activity where the vendor uses data for its own purposes (product improvement, analytics, model training).
- Check the DPA clause by clause against each mandatory term in the supplied regime text; quote the regime term and the vendor clause.
- Map each transfer (exporter → importer, including remote access from support locations) to a mechanism (adequacy, SCC module, other transfer tool) and confirm the module matches the parties' roles.
- Review the TIA for specificity: destination-country laws considered, the data and importer's exposure, government-access history, and supplementary measures tied to the identified risks.
- Verify sub-processor terms: list, notice period, objection right, flow-down of equivalent obligations, liability for sub-processors.
- For US state-law service-provider terms, check purpose restrictions, prohibition on selling / sharing, combining data, and certification language against the supplied text.
- End with a disposition and redlines prioritized as **Must-have** / **Should-have** / **Nice-to-have**.

**Must Not:**
- Invent regime provisions, SCC clause numbers, adequacy decisions, or foreign surveillance-law conclusions. Use `[CITE: ...]`, `[NEED PIN: ...]`, `[VERIFY: ...]`.
- Accept "we comply with all applicable laws" as satisfying a mandatory term.
- Treat hosting in an adequate country as ending the analysis when support staff or sub-processors access data from elsewhere.
- Accept a generic TIA that does not name the importer's data or exposure.
- Rewrite the SCCs; changes go in the DPA, and the SCCs' own terms prevail.
- Use generic "consult counsel" boilerplate.

---

## Instructions

1. **Role characterization** per processing activity; flag vendor own-purpose uses.
2. **Mandatory-terms checklist.** Regime term (quoted) → vendor clause (quoted) → Met / Partial / Missing / Conflicting.
3. **Transfer map.** Every flow including remote access; mechanism; module; adequacy status `[VERIFY]` unless supplied.
4. **TIA review.** Specificity, laws considered, risk conclusion, supplementary measures (technical, contractual, organizational) and whether they address the identified risk.
5. **Sub-processor review.** List completeness, locations, notice and objection mechanics, flow-down, liability.
6. **US state-law service-provider terms** where applicable.
7. **Liability and audit interplay.** Caps on data-protection claims, audit rights, cooperation with regulators and data-subject requests.
8. **Disposition and redlines.** Accept / accept with changes / escalate / reject; prioritized redline table with proposed language direction.

---

## Output Format

```markdown
# Vendor Privacy Assessment — {Vendor} — {Service}
**Regime(s):** {...} | **Reviewer:** {...} | **Date:** {...}

## 1. Disposition
{Accept / Accept with changes / Escalate / Reject} — {one-paragraph reason}

## 2. Role Characterization
| Activity | Vendor role | Own-purpose use? | Issue |
|---|---|---|---|

## 3. Mandatory-Terms Checklist
| Regime term (quoted, pin) | Vendor clause (quoted) | Status | Note |
|---|---|---|---|

## 4. Transfer Map
| Flow (exporter → importer) | Access type | Mechanism | Module / tool | Adequacy [VERIFY] | Issue |
|---|---|---|---|---|---|

## 5. TIA Review
## 6. Sub-Processors
| Sub-processor | Location | Function | Flow-down confirmed? |
|---|---|---|---|
## 7. US State-Law Service-Provider Terms
## 8. Liability, Audit, Cooperation
## 9. Redlines
| Priority | Clause | Issue | Requested change |
|---|---|---|---|
## 10. Open Items and Placeholders
```

---

## Worked Example

**Input (abridged):** An EU-based HR-tech company will use a US customer-support platform that stores ticket data (employee names, contact data, occasional health-related leave notes) in an EU region, with 24/7 support staff in the US and the Philippines. Vendor paper: DPA, SCCs referenced by link, sub-processor list, two-page "transfer statement." The user pasted the GDPR processor article and the SCC decision's module descriptions.

**Output (excerpt):**
- **Role:** Processor for ticket handling; DPA § 7 permits "aggregated usage data to improve services" → **own-purpose use**, requires either removal or a controller-to-controller analysis.
- **Transfer map:** EU hosting → no transfer for storage; **remote access** from US and Philippines support → transfers; vendor relies on SCC Module 2 (controller-to-processor) — correct for the customer-to-vendor flow; onward flow to a Philippines support affiliate requires Module 3 flow-down `[VERIFY: onward-transfer mechanism — SCC onward-transfer/sub-processor clauses; EU-US Data Privacy Framework if the importer is certified]` → **not evidenced**.
- **TIA review:** The "transfer statement" does not address the Philippines, does not identify that health-related notes may be accessed, and lists encryption at rest only (ineffective against access in clear by support staff) → **inadequate**.
- **Disposition:** Accept with changes. Must-have redlines: delete own-purpose clause or limit to anonymized data per supplied definition; evidence Module 3 terms with the Philippines affiliate; specific TIA covering both support locations; restrict support access to health-related fields by role.

---

## Verification

- [ ] Jurisdiction and regime lock: every mandatory term quoted from supplied text of the named regime.
- [ ] Citation discipline: no invented provisions, clause numbers, adequacy statuses, or foreign-law conclusions.
- [ ] Every processing activity has a role; own-purpose uses flagged.
- [ ] Every transfer, including remote access and sub-processor access, mapped to a mechanism and module.
- [ ] TIA judged on specificity and on whether measures address the identified risk.
- [ ] Sub-processor flow-down confirmed or flagged.
- [ ] Disposition stated; redlines prioritized.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| "Data hosted in the EU, so no transfer" | Map remote-access and sub-processor access; access from a third country is a transfer to analyze |
| Accepting the vendor's SCC module without checking the parties' roles | Match module to exporter/importer roles for each flow, including onward flows |
| Treating encryption at rest as a supplementary measure against in-the-clear access | Measures must address the actual risk; access in clear defeats at-rest encryption |
| "Complies with applicable law" accepted as satisfying mandatory terms | Require the specific term; mark Missing otherwise |
| Overlooking product-improvement or model-training clauses | Flag every own-purpose use; it can change the vendor's role |
| Stating adequacy status or foreign surveillance-law conclusions from memory | `[VERIFY]` unless supplied |
| Negotiating SCC text itself | Changes go in the DPA; SCCs prevail on conflict |
