---
title: "Privacy Impact Assessment / DPIA — Lawful Basis, Data Flows, Risk, Mitigations"
category: legal/privacy-data
description: "Draft a data protection impact assessment (DPIA) or privacy impact assessment for a proposed processing operation: screening for whether one is required, systematic description and data-flow map, lawful basis and necessity/proportionality analysis, risk assessment to individuals (likelihood × severity), mitigations with residual risk, and the prior-consultation decision. Counsel-facing and jurisdiction-locked to the supplied regime."
techniques:
  - DS-01
  - RT-02
  - DS-02
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - privacy
  - data-protection
  - dpia
  - pia
  - gdpr
  - lawful-basis
  - risk-assessment
updated: "2026-09-24"
reasoning:
  styles: [analytic, systematic, evaluative]
  stakes: high
  horizon: weeks
  uncertainty: ambiguity
  evidence_quality: mixed
  domain_complexity: regulated
  collaboration: small_team
  output_format: [structured, matrix]
  user_role: [attorney, privacy_counsel, dpo]
related_prompts:
  - domain-legal/contracts-transactional/legal_dpa_gdpr_drafter.md
  - domain-legal/privacy-data/legal_vendor_privacy_assessment.md
  - domain-legal/privacy-data/legal_records_retention_schedule_design.md
  - domain-AI-ML/responsible-ai-governance/rai_gdpr_automated_decisioning_assessment.md
  - domain-software-engineering/analysis/security/security_privacy_by_design_architecture.md
---

# Privacy Impact Assessment / DPIA

**Objective:** Produce the legal assessment document for a proposed processing operation: decide whether a DPIA is required under the supplied regime, describe the processing and map the data flows, establish the lawful basis (and any special-category condition) for each purpose, test necessity and proportionality, assess risks to individuals' rights and freedoms by likelihood and severity, specify mitigations with an owner, rate residual risk, and decide whether prior consultation with the supervisory authority is required. The output is the record the organization keeps to demonstrate accountability.

**When to use:**
- A new product, feature, vendor, monitoring program, or analytics use involves personal data and may be high-risk (large scale, special categories, systematic monitoring, profiling with significant effects, new technology, vulnerable individuals, data matching).
- An existing processing operation changes purpose, scale, data categories, or recipients.
- A regulator, customer, or auditor asks for the DPIA record.

**Distinct from:**
- `domain-software-engineering/analysis/security/security_gdpr_implementation_guide.md` and `security_privacy_by_design_architecture.md` — engineering implementation (consent flows, data-subject-request tooling, pseudonymization). This prompt is the legal assessment that decides what engineering must deliver.
- `domain-agentic-resources/skills/security/gdpr-data-handling` — a skill for building GDPR-compliant systems; not a legal DPIA record.
- `domain-AI-ML/responsible-ai-governance/rai_gdpr_automated_decisioning_assessment.md` and `rai_privacy_pii_assessment.md` — ML-specific automated-decisioning and model-privacy risk; use them as inputs to this DPIA when the processing is an ML system.
- `domain-written-advocacy/privacy-and-data/` — letters an individual sends to exercise their own rights.

---

## Your Input

- **Regime(s) and jurisdiction:** [EU GDPR / UK GDPR / Swiss FADP / US state comprehensive privacy law(s) / sectoral law / other — the assessment is locked to the regimes named]
- **Regime text or regulator guidance supplied:** [Paste relevant articles / sections and any supervisory-authority list of processing requiring a DPIA, with version date]
- **Controller(s) and role:** [Controller / joint controller / processor; establishments]
- **Processing description:** [Purpose(s), data subjects, data categories (flag special-category, children's, criminal-offence, precise location, biometric), sources, recipients, processors, international transfers, retention, systems]
- **Technology:** [New technology, AI/ML, automated decisions, monitoring]
- **Scale:** [Number of individuals, geographic reach, volume, frequency]
- **Existing controls:** [Security, access, minimization, transparency, rights handling]
- **Stakeholder input:** [DPO advice, data-subject or representative views, security team assessment]

---

## Constraints

**Must:**
- Start with a **screening decision** — required / not required / recommended — reasoned against the supplied regime's triggers and any supplied supervisory-authority list.
- Give each purpose its own lawful basis with the reasoning, and a separate special-category / sensitive-data condition where relevant. Where legitimate interests is relied on, include the three-part test (purpose, necessity, balancing).
- Test necessity and proportionality: could the purpose be achieved with less data, less identifiability, shorter retention, or fewer recipients?
- Assess risk **to individuals** (not to the company): harm type (discrimination, financial loss, loss of confidentiality, identity theft, reputational damage, loss of control, chilling effect), likelihood, severity, inherent risk.
- Specify each mitigation with an owner and a status, and rate residual risk after mitigation.
- Record the prior-consultation decision where the regime requires consultation for residual high risk, with the reason.
- Record DPO advice and whether it was followed.

**Must Not:**
- Invent article numbers, regulator lists, guidance, or thresholds. Use `[CITE: ...]`, `[NEED PIN: ...]`, `[VERIFY: ...]`.
- Treat consent as the default lawful basis, or rely on consent where there is a clear imbalance of power (e.g., employer–employee) without addressing it.
- Rate risk to the organization (fines, reputation) in place of risk to individuals; organizational risk can appear separately.
- List mitigations that are generic ("industry-standard security") rather than specific and owned.
- Assess a US state-law risk assessment as if it were a GDPR DPIA, or vice versa; each regime's required content differs.
- Use generic "consult counsel" boilerplate.

---

## Instructions

1. **Screening.** Walk the supplied triggers; decide and record reasons.
2. **Systematic description.** Purposes, context, nature, scope; data inventory table.
3. **Data-flow map.** Collection → storage → use → sharing → transfer → deletion, with systems and recipients at each hop (text or table).
4. **Lawful basis per purpose.** Basis, special-category condition, transparency notice location, legitimate-interests test where used.
5. **Necessity and proportionality.** Minimization, accuracy, retention, rights handling, processor terms, transfer mechanism.
6. **Risk register.** Each risk: source, harm to individuals, likelihood (Remote / Possible / Probable), severity (Minimal / Significant / Severe), inherent rating.
7. **Mitigations.** Measure, owner, status, residual likelihood and severity, residual rating.
8. **Sign-off and consultation.** DPO advice, residual-risk acceptance by the accountable owner, prior-consultation decision, review date and change triggers.

---

## Output Format

```markdown
# Data Protection Impact Assessment — {Processing operation}
**Regime(s):** {as named} | **Controller:** {entity} | **Version / date:** {...} | **Privileged draft** {if prepared by counsel before finalization}

## 1. Screening Decision
| Trigger (from supplied text) | Present? | Reason |
|---|---|---|
**Decision:** {Required / Not required / Recommended}

## 2. Description of Processing
| Purpose | Data subjects | Data categories | Source | Recipients / processors | Transfers | Retention |
|---|---|---|---|---|---|---|

## 3. Data-Flow Map
## 4. Lawful Basis
| Purpose | Lawful basis | Special-category condition | Notice | Legitimate-interests test (if used) |
|---|---|---|---|---|

## 5. Necessity and Proportionality
## 6. Risk Assessment
| # | Risk source | Harm to individuals | Likelihood | Severity | Inherent |
|---|---|---|---|---|---|

## 7. Mitigations and Residual Risk
| Risk # | Measure | Owner | Status | Residual likelihood | Residual severity | Residual |
|---|---|---|---|---|---|---|

## 8. DPO Advice, Sign-Off, Prior Consultation
## 9. Review Triggers
## 10. Open Items and Placeholders
```

---

## Worked Example

**Input (abridged):** An EU-established logistics employer plans to install telematics and driver-facing cameras in 400 delivery vans, with AI detection of "distracted driving" events that feed a driver-scoring dashboard used in performance reviews. Regime: EU GDPR; the user pasted the relevant articles and their national supervisory authority's DPIA list.

**Output (excerpt):**
- **Screening:** Required — systematic monitoring of employees, new technology, and evaluation/scoring (each matched to supplied text).
- **Lawful basis:** Road-safety event detection — legitimate interests (three-part test completed); performance scoring — legitimate interests fails balancing as designed (continuous in-cab video, power imbalance); consent rejected as a basis because of the employment relationship.
- **Risk #3:** Continuous in-cab video → loss of privacy during breaks and chilling effect. Likelihood Probable, Severity Significant → **High**.
- **Mitigation:** Event-triggered 10-second clips only; camera off during logged breaks; clips auto-deleted after the stated review window unless attached to an incident; human review before any score affects a review. Owner: Fleet Safety Lead. Residual: Possible / Significant → **Medium**.
- **Works-council / employee-consultation obligations:** `[VERIFY: national labour-law consultation requirements]`.
- **Prior consultation:** Not required if mitigations are implemented as specified; re-assess if scoring is reinstated.

---

## Verification

- [ ] Jurisdiction and regime lock: triggers, bases, and required content drawn from the named regime's supplied text only.
- [ ] Citation discipline: no invented articles, regulator lists, or guidance; placeholders listed.
- [ ] Screening decision reasoned per trigger.
- [ ] One lawful basis per purpose; special-category conditions separate; legitimate-interests test shown where used.
- [ ] Risks framed as harms to individuals with likelihood and severity.
- [ ] Every mitigation specific, owned, and followed by a residual rating.
- [ ] Prior-consultation decision recorded with reason.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Screening concludes "not required" because the company has done similar processing before | Screen against the triggers for this operation; prior practice is not a trigger exemption |
| Consent chosen by default, including for employees | Choose the basis that fits the purpose; address power imbalance explicitly |
| One lawful basis for the whole project | Each purpose gets its own basis; secondary uses often fail |
| Risk register lists fines and reputational damage as the risks | Frame risks as harms to individuals; organizational risk may appear separately |
| "Encryption and access controls" offered as the fix for a necessity problem | Security does not cure excessive collection; address minimization and purpose |
| Residual risk rated Low without changing likelihood or severity | Each mitigation must move a specific axis; explain which |
| Applying GDPR DPIA structure to a US state-law risk assessment without adjustment | Lock to the named regime's required content and terminology |
