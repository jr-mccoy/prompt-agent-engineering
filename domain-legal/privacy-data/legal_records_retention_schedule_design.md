---
title: "Records Retention Schedule Design — Record Classes, Jurisdictions, and Legal-Hold Override"
category: legal/privacy-data
description: "Design an enterprise records retention schedule: define record classes by function, attach each class's retention driver (statutory or regulatory minimum, limitation period, business need, privacy maximum) per jurisdiction from supplied sources, resolve conflicts between minimums and data-minimization limits, specify trigger events and disposition methods, and wire in the legal-hold override so no scheduled deletion touches held records. Every retention period is sourced or marked [VERIFY]."
techniques:
  - ST-03
  - DS-01
  - CM-02
  - QA-05
  - QA-01
difficulty: advanced
tags:
  - legal
  - privacy
  - records-management
  - retention-schedule
  - legal-hold
  - data-minimization
  - information-governance
  - how-long-to-keep
updated: "2026-09-24"
reasoning:
  styles: [classificatory, systematic, analytic]
  stakes: high
  horizon: months
  uncertainty: ambiguity
  evidence_quality: mixed
  domain_complexity: regulated
  collaboration: cross_functional
  output_format: [matrix, structured]
  user_role: [attorney, privacy_counsel, records_manager]
related_prompts:
  - domain-legal/discovery/legal_ediscovery_custodian_interview.md
  - domain-legal/privacy-data/legal_privacy_impact_assessment_dpia.md
  - domain-legal/regulatory-compliance/legal_subpoena_or_cid_response_strategy.md
  - domain-software-engineering/mobile/ios/planning/ios_data_retention_policy_design.md
---

# Records Retention Schedule Design

**Objective:** Produce a retention schedule an organization can operate and defend: a taxonomy of record classes defined by business function (not by system), a retention rule for each class in each relevant jurisdiction with its legal source, a resolution for every conflict between "keep at least" obligations and privacy "keep no longer than necessary" limits, a trigger event and disposition method per class, and a legal-hold mechanism that suspends disposition for anything under hold. The schedule is the legal layer; systems teams implement it.

**When to use:**
- The organization has no schedule, an outdated one, or several inconsistent schedules after an acquisition.
- A privacy program needs defined maximum retention periods for personal data.
- Litigation or an investigation exposed over-retention (costly discovery) or under-retention (spoliation risk).
- A new jurisdiction, business line, or regulated activity changes record-keeping obligations.

**Distinct from:**
- `domain-software-engineering/mobile/ios/planning/ios_data_retention_policy_design.md` and `domain-software-engineering/mobile/android/planning/android_data_retention_policy_design.md` — implement retention in an app's data layer; this prompt decides the legal periods those implementations enforce.
- `domain-agentic-resources/skills/security/gdpr-data-handling` — engineering guidance for GDPR-compliant systems, not an enterprise legal schedule.
- `domain-legal/discovery/legal_ediscovery_custodian_interview.md` — gathers custodian data facts for a specific matter; this prompt sets organization-wide rules including hold interaction.

---

## Your Input

- **Organization profile:** [Entities, industries, regulated activities, public / private, employee count]
- **Jurisdictions:** [Countries and states / provinces where records are created or held, or where individuals reside]
- **Retention sources supplied:** [Statutes, regulations, regulator guidance, or the user's existing retention-law survey with as-of date. Anything not supplied is marked `[VERIFY]`.]
- **Record inventory:** [Functions and record types (HR, payroll, finance, tax, contracts, customer, marketing, product, health & safety, IT logs, board), systems of record, formats]
- **Privacy regime(s):** [Storage-limitation or data-minimization rules that set maximums]
- **Litigation and hold landscape:** [Current holds, typical litigation types, limitation periods relevant to the business (supplied)]
- **Operational constraints:** [Systems capable of automated deletion; backups; archives; email and chat retention settings]
- **Existing schedule:** [If any]

---

## Constraints

**Must:**
- Define record classes by function and content ("Employee payroll records"), not by system ("SAP data"); map systems to classes separately.
- For each class and jurisdiction, record every retention driver separately: (a) legal minimum with source, (b) limitation-period-based business need with source, (c) operational need, (d) privacy maximum or justification. The rule is the longest applicable minimum that does not exceed a justified privacy maximum.
- Specify the **trigger event** that starts the clock (creation, end of fiscal year, termination of employment, contract expiry, account closure, last activity).
- Specify disposition method (secure deletion, anonymization, transfer to archive) and who approves.
- Resolve every minimum-versus-maximum conflict explicitly and record the reasoning.
- Include the legal-hold override: holds suspend disposition across all systems, including backups and chat, from issuance until written release; disposition jobs check hold status before running.
- Address non-records (drafts, convenience copies, transitory messages) with a short rule.

**Must Not:**
- Invent retention periods, statutory citations, limitation periods, or regulator guidance. Use `[CITE: ...]`, `[NEED PIN: ...]`, `[VERIFY: {jurisdiction} {record class}]`.
- Default to "retain permanently" or a blanket long period to avoid analysis; over-retention has privacy and discovery costs.
- Apply one jurisdiction's period to records governed by another's.
- Treat backups as outside the schedule.
- Let a scheduled deletion run on held records.
- Use generic "consult counsel" boilerplate.

---

## Instructions

1. **Build the taxonomy.** Group records into 20–60 functional classes with definitions and examples; add a non-records rule.
2. **Map systems to classes.** System → classes it holds → owner.
3. **Gather drivers.** For each class × jurisdiction, list legal minimums, limitation-period rationale, operational need, and privacy maximum — each with its supplied source or `[VERIFY]`.
4. **Set the rule.** Retention period + trigger; state the governing driver.
5. **Resolve conflicts.** Where a minimum exceeds a privacy maximum or two jurisdictions conflict, decide (e.g., keep for the minimum in a restricted archive; segregate by jurisdiction) and record why.
6. **Disposition.** Method, approver, evidence of disposition.
7. **Legal-hold integration.** Issuance, scope mapping to classes and systems, suspension mechanics, release, audit.
8. **Governance.** Owner of the schedule, review cadence, change triggers, training, and defensible-disposition documentation.

---

## Output Format

```markdown
# Records Retention Schedule — {Organization}
**Version:** {...} | **Effective:** {...} | **Owner:** {role} | **Sources as of:** {date}

## 1. Principles and Non-Records Rule
## 2. Record Class Taxonomy
| Class code | Class | Definition | Examples |
|---|---|---|---|

## 3. Retention Rules
| Class code | Jurisdiction | Legal minimum (source) | Limitation / business need (source) | Privacy maximum / justification | Rule | Trigger | Disposition |
|---|---|---|---|---|---|---|---|

## 4. Conflict Resolutions
| Class | Conflict | Resolution | Reason |
|---|---|---|---|

## 5. System-to-Class Map
| System | Classes | System owner | Automated disposition? |
|---|---|---|---|

## 6. Legal-Hold Override Procedure
## 7. Disposition Procedure and Evidence
## 8. Governance and Review
## 9. Open Items and Placeholders ([VERIFY] list)
```

---

## Worked Example

**Input (abridged):** A mid-size staffing company operating in two US states and Ontario supplies its outside counsel's retention survey (as-of date stated) covering employment, payroll, and tax records, but nothing on applicant data or chat logs. Current practice: keep everything forever; Slack retention unlimited. One pending wage-and-hour class action.

**Output (excerpt):**

| Class code | Jurisdiction | Legal minimum (source) | Limitation / business need | Privacy maximum | Rule | Trigger | Disposition |
|---|---|---|---|---|---|---|---|
| HR-03 Payroll records | State A | Period stated in survey § 2.1 | Wage-claim limitation period per survey § 4.3 (longer) | Not applicable (legal minimum governs) | Longer of the two | End of calendar year of last pay date | Secure deletion; HR director approves |
| HR-07 Rejected applicant files | Ontario | `[VERIFY: Ontario applicant-record retention requirement]` | Discrimination-claim window `[VERIFY]` | Privacy maximum: no longer than needed for the purpose `[VERIFY: applicable Ontario/Canadian privacy regime]` | Provisional: survey-derived minimum pending verification | Date of hiring decision | Secure deletion |
| IT-02 Chat messages (transitory) | All | None identified in survey | Operational | Minimization | 90 days, except business-record content moved to the relevant class | Message date | Automated deletion |

- **Legal-hold override:** The pending class action places HR-03 and chat messages of named payroll custodians on hold; the 90-day chat deletion job must exclude held custodians before it is enabled.
- **Conflict resolution:** Legacy payroll deletion is suspended for the whole HR-03 record class — not only for employees inside the proposed class definition, which can change before certification — until class certification is decided and the case is resolved, or litigation counsel issues a written hold release covering the records; the suspension and any later release are recorded with counsel sign-off.

---

## Verification

- [ ] Jurisdiction lock: each rule tied to the jurisdiction whose law governs that class.
- [ ] Citation discipline: every period sourced to supplied material or marked `[VERIFY]`; none invented.
- [ ] Classes defined by function; systems mapped separately.
- [ ] Every rule has a trigger event and disposition method.
- [ ] Every minimum-versus-maximum conflict resolved with a reason.
- [ ] Legal-hold override covers all systems including backups and chat, and disposition jobs check hold status.
- [ ] Non-records rule present.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Stating "keep payroll records for N years" from memory | Source to supplied survey or statute; otherwise `[VERIFY]` |
| Classes defined by system, so one class mixes payroll and marketing data | Define by function; map systems to classes separately |
| Retention period with no trigger event | Every rule states when the clock starts |
| "Retain permanently" used to avoid conflicts | Resolve conflicts; justify any permanent retention by a specific driver |
| Backups and chat left out of scope | Include them; they are discoverable and subject to privacy limits |
| Enabling automated deletion before hold checks are wired in | Hold override is a precondition to any automated disposition |
| Applying the headquarters jurisdiction's periods to all records | Rule per class × jurisdiction |
