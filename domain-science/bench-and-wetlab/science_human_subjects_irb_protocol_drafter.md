---
title: "Human Subjects IRB Protocol Drafter"
category: science/bench-and-wetlab
description: "Draft a section-by-section IRB-submission scaffold with risk-benefit analysis, informed consent and assent, vulnerable-population protections, and a privacy/data-security plan grounded in Belmont, the Common Rule, and Helsinki — routing approval to the IRB."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-01
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - irb
  - human-subjects
  - informed-consent
  - belmont
  - common-rule
  - vulnerable-populations
  - data-security
  - risk-benefit
updated: "2026-06-26"
related_prompts:
  - domain-science/statistics/science_pre_specified_analysis_plan.md
  - domain-science/methods-foundations/science_power_and_sample_size_calculator.md
  - domain-science/bench-and-wetlab/science_animal_protocol_iacuc_drafter.md
---

# Human Subjects IRB Protocol Drafter

**Objective:** Produce a section-by-section IRB-submission scaffold that operationalizes the Belmont principles (respect for persons, beneficence, justice) through a structured risk-benefit analysis, informed-consent and assent elements, vulnerable-population protections, equitable selection, and a privacy/confidentiality and data-security plan. The draft structures the submission; the IRB makes the determination.

**When to use:** When preparing a new or amended human-subjects research protocol and you need a rigorous, ethics-first scaffold before institutional submission and review.

**Required inputs:**
- **Discipline.** Field and research area (e.g., clinical psychology, public health, HCI).
- **Study type.** Observational / interventional / survey / secondary-data — and the core aim.
- **Population (proposed).** Who will be recruited, including any vulnerable groups `[user-supplied]`.
- **Procedures and data collected.** What participants do and what data is gathered `[user-supplied]`.

**Optional inputs:**
- Prior analysis/sample-size estimates (cross-reference the SAP and power prompts).
- Recruitment channels and incentives under consideration `[user-supplied]`.
- Institutional data-security/HIPAA policy specifics `[user-supplied]`.
- Whether a data and safety monitoring plan is anticipated.

**Constraints — Must:**
- Structure the protocol around Belmont principles and Common Rule / Declaration of Helsinki / GCP expectations at a structural level (specific text `[user-supplied]`/verify).
- Include a risk-benefit analysis that minimizes and justifies risk and states anticipated benefit honestly.
- Include informed-consent elements (and assent where minors/limited-capacity participants are involved) and a comprehension/voluntariness plan.
- Include vulnerable-population protections and equitable, justice-aligned selection.
- Include a privacy/confidentiality and data-security plan addressing identifiers, storage, access, and de-identification at a structural level (HIPAA where applicable, `[user-supplied]`).
- Cross-reference the SAP and power prompts for pre-specified analysis and sample size; route approval to the IRB.

**Constraints — Must Not:**
- Do not invent vendor names, catalog/lot numbers, reagent specs, hazard data, regulatory citations, or institutional policy text. If needed and not supplied, mark `[user-supplied]` and route formal approval to the IACUC / IRB / IBC / biosafety officer.
- Do not assert a specific exemption or expedited category as settled — that determination belongs to the IRB.
- Do not draft verbatim consent or regulatory text from memory; mark `[user-supplied]`/verify.
- Do not describe drafted protocol text as "novel," "groundbreaking," "first-ever," or a "gold standard," and do not understate risk to ease approval.

**Instructions:**

1. **Frame background and aims.** Capture discipline, study type, aim, and significance without promotional language.
2. **Risk-benefit analysis.** Draft the risks (physical, psychological, social, legal, economic), minimization steps, and an honest statement of anticipated benefit; mark uncertain magnitudes `[user-supplied]`.
3. **Recruitment and eligibility.** Draft recruitment channels, inclusion/exclusion criteria, and equitable-selection rationale (justice).
4. **Informed consent and assent.** Scaffold the consent elements, comprehension and voluntariness plan, and assent for minors/limited-capacity participants; mark verbatim language `[user-supplied]`/verify.
5. **Vulnerable-population protections.** Identify any vulnerable groups and draft the additional safeguards appropriate to them.
6. **Privacy and data security.** Draft identifier handling, storage/access controls, de-identification, and HIPAA-relevant structure `[user-supplied]` for institutional specifics.
7. **Analysis and sample size.** Cross-reference the SAP and power prompts; require pre-specified analysis and a sample-size justification rather than invented numbers.
8. **Data and safety monitoring.** Scaffold monitoring, adverse-event reporting, and stopping considerations where applicable.
9. **Self-check and route.** Run the verification checklist and state plainly that the IRB holds determination authority; offer compatible Open Science steps only where consent and confidentiality permit.

**Output format (locked):**

```
## Background & Aims
- Discipline / study type / aim:

## Risk-Benefit Analysis
- Risks / minimization / anticipated benefit [user-supplied where uncertain]:

## Recruitment & Eligibility
- Channels / inclusion-exclusion / equitable selection:

## Informed Consent & Assent
- Consent elements / comprehension & voluntariness / assent [user-supplied/verify]:

## Vulnerable-Population Protections
- Groups / additional safeguards:

## Privacy, Confidentiality & Data Security
- Identifiers / storage & access / de-identification / HIPAA structure [user-supplied]:

## Analysis & Sample Size
- Pre-specified analysis (xref SAP) / sample size (xref power prompt):

## Data & Safety Monitoring
- Monitoring / adverse-event reporting / stopping:

## Belmont Mapping & Routing
- Principle map / IRB-determination statement:
```

**Reporting-standard alignment:** Belmont Report principles; US Common Rule; Declaration of Helsinki; Good Clinical Practice (GCP); HIPAA at a structural level (specific text `[user-supplied]`/verify).

**Verification checklist (before delivering):**
- [ ] Discipline and study type captured as first inputs.
- [ ] Risk-benefit analysis minimizes and justifies risk and states benefit honestly.
- [ ] Informed-consent elements present, with assent where relevant.
- [ ] Vulnerable populations identified with tailored protections.
- [ ] Privacy/data-security plan present (HIPAA structure where applicable).
- [ ] Analysis and sample size cross-reference the SAP and power prompts; no invented numbers.
- [ ] No exemption/expedited category asserted as settled; consent/regulatory text marked `[user-supplied]`/verify.
- [ ] Approval routed to the IRB; no banned promotional language in drafted text.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Exemption assumed | Draft declares the study "exempt" | Route the determination to the IRB; never assert a category as settled |
| Risk under-stated | Risks softened to ease approval | Require honest enumeration + minimization and benefit statement |
| Weak consent | Generic consent without comprehension plan | Require consent elements + voluntariness/comprehension; verbatim `[user-supplied]` |
| Data exposure | "Data is anonymous" asserted without controls | Require identifier handling, storage/access, and de-identification plan |
