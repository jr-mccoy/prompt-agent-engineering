---
title: "Data Breach Legal Response Runbook — Notification Triage Across US States and International Regimes"
category: legal/privacy-data
description: "Counsel's runbook for a personal-data security incident: privilege structure for the forensic work, fact-gathering against each regime's breach definition, a notification-triage matrix across US states, federal sectoral rules, and international regimes built from supplied statutory text, regulator and individual notice drafting, contractual and insurer notices, and mitigation offers. Every clock and threshold comes from supplied law or is marked [VERIFY]; none is asserted from memory."
techniques:
  - ST-02
  - ST-43
  - CM-02
  - QA-05
  - QA-01
difficulty: advanced
tags:
  - legal
  - privacy
  - data-breach
  - incident-response
  - breach-notification
  - regulator-notice
  - consumer-notice
updated: "2026-09-24"
reasoning:
  styles: [systematic, decomposition, time_critical]
  stakes: critical
  horizon: hours_to_days
  uncertainty: ambiguity
  evidence_quality: sparse
  domain_complexity: regulated
  collaboration: small_team
  output_format: [structured, matrix]
  user_role: [attorney, privacy_counsel, in_house_counsel]
related_prompts:
  - domain-risk/risk_security_incident_response_playbook.md
  - domain-legal/privacy-data/legal_vendor_privacy_assessment.md
  - domain-legal/contracts-transactional/legal_dpa_gdpr_drafter.md
  - domain-legal/in-house-legalops/legal_matter_summary_for_executive.md
---

# Data Breach Legal Response Runbook

**Objective:** Run the legal workstream of a personal-data security incident from first notice to closure: put forensic work under privilege, gather the facts each regime's breach definition turns on, triage notification obligations for every affected jurisdiction (US states, federal sectoral rules, and international regimes) from supplied legal text, draft regulator and individual notices, handle contractual, insurer, and law-enforcement notices, and decide mitigation offers — with every deadline tracked from the correct trigger.

**When to use:**
- An incident has exposed, or may have exposed, personal data (ransomware with exfiltration, misdirected files, credential compromise, lost device, vendor incident).
- The organization is a processor or service provider and must notify its customers under contract.
- A vendor has notified the organization of an incident affecting its data.

**Distinct from:**
- `domain-risk/risk_security_incident_response_playbook.md` — the organization's operational response (containment, evidence, decision authority) that deliberately routes notification clocks to counsel. This runbook is that counsel workstream.
- `domain-agentic-resources/commands/troubleshooting/incident_response.md` and technical incident runbooks in `domain-software-engineering/` — system recovery, not legal notification.
- `domain-legal/personal-self-advocacy/` — for the individual whose data was exposed.

---

## Your Input

- **Incident facts known now:** [Discovery date/time and by whom; attack vector; systems; whether data was accessed, acquired, or exfiltrated; encryption status and whether keys were compromised; containment status]
- **Data elements:** [Per system: names plus which identifiers (SSN / national ID, driver's licence, account or card number with access code, health, biometric, credentials, precise location, children's data)]
- **Affected individuals by residence:** [Counts per US state and per country; if unknown, the best current estimate and how it will be refined]
- **Organization's role:** [Controller / owner / licensee vs processor / service provider; sector (health, financial, education, government contractor, publicly listed)]
- **Legal text supplied:** [Paste each applicable breach-notification statute or regulation, or the user's current statutory survey with its as-of date. Anything not supplied is marked `[VERIFY]`.]
- **Contracts:** [Customer, vendor, and DPA notice clauses; cyber-insurance policy notice provisions]
- **Law enforcement:** [Contacted? Any request to delay notification (in writing?)]
- **Forensic engagement:** [Firm, engaged by whom, under what terms]

---

## Constraints

**Must:**
- Establish privilege on day one: outside counsel engages the forensic firm; scope of work is legal advice; separate any business-purpose remediation report; restrict distribution.
- Record the **trigger event for every clock** (discovery, determination of breach, reasonable belief of acquisition, awareness by processor) exactly as the supplied text defines it — clocks do not all start at the same moment.
- Build the triage matrix jurisdiction by jurisdiction: breach definition met? (data elements, encryption safe harbor, risk-of-harm exception as the text states), individual notice, regulator / attorney-general notice, consumer-reporting-agency notice, content requirements, timing, and method.
- Stratify decisions by irreversibility: notices cannot be withdrawn; over-notification has costs; under-notification creates enforcement exposure. Document the reasoning for any decision not to notify.
- Draft notices to the content requirements of the supplied text, in plain language, without speculation, and consistent with each other.
- Track contractual notices (customers, vendors) and insurer notice, which often have shorter or different clocks than statutes.
- Keep a decision log with timestamps.

**Must Not:**
- Assert any notification deadline, threshold, risk-of-harm exception, content requirement, or regulator address from memory. Use `[VERIFY: {jurisdiction} {element}]` or `[CITE: ...]`.
- Apply a single "strictest-state" rule as if it satisfied every jurisdiction's content and method requirements.
- Treat encrypted data as safe-harbored without confirming the keys were not compromised.
- State facts in a notice that forensics has not confirmed, or minimize ("no evidence of misuse") without basis.
- Admit liability in notices.
- Use generic "consult counsel" boilerplate.

---

## Instructions

1. **Hour 0–24: privilege and preservation.** Engagement structure; preserve logs and images; open the decision log; notify insurer per policy `[VERIFY: policy notice clause]`.
2. **Fact-gathering questions.** List the facts each supplied breach definition needs (element types, encryption and key status, access vs acquisition, residence of individuals) and assign each to forensics or the data owner with a due time.
3. **Clock register.** Every potential obligation, its trigger per the supplied text, the earliest possible trigger date, and the resulting deadline or `[VERIFY]`.
4. **Triage matrix.** Jurisdiction × obligation (individual, regulator, AG, CRAs, sector regulator, supervisory authority, customers). Mark Required / Not required (reason) / Pending facts.
5. **Law-enforcement delay.** If requested, document the request and its form; note whether each supplied statute permits delay and on what conditions.
6. **Notice drafting.** Regulator notice(s), individual notice (base template plus jurisdiction-specific inserts), customer notice (if processor), substitute-notice analysis if contact data is insufficient.
7. **Mitigation offer.** Credit monitoring / identity protection where required by supplied text or adopted as policy; call centre; FAQ.
8. **Closure.** Final decision log, regulator follow-up, lessons learned, contract and DPA amendments, litigation-hold continuation.

---

## Output Format

```markdown
# Breach Response Runbook — {Incident code name}
**Privileged & Confidential — Attorney-Client Communication / Work Product** | **Status as of:** {timestamp}

## 1. Incident Snapshot (confirmed vs unconfirmed)
## 2. Privilege and Engagement Structure
## 3. Open Fact Questions
| Question | Why it matters (which regimes) | Owner | Due |
|---|---|---|---|
## 4. Clock Register
| Obligation | Jurisdiction | Trigger (per supplied text) | Trigger date | Deadline | Source / [VERIFY] |
|---|---|---|---|---|---|
## 5. Notification Triage Matrix
| Jurisdiction | Breach definition met? | Individuals | Regulator / AG | CRAs | Other | Content / method notes |
|---|---|---|---|---|---|---|
## 6. Contractual and Insurer Notices
## 7. Law-Enforcement Delay Log
## 8. Notice Drafts
### 8.1 Regulator notice — {jurisdiction}
### 8.2 Individual notice — base template + inserts
### 8.3 Customer notice (processor role)
## 9. Mitigation Offer
## 10. Decision Log
| Timestamp | Decision | Basis | Decided by |
|---|---|---|---|
## 11. Open Items and Placeholders
```

---

## Worked Example

**Input (abridged):** A US-based online retailer with EU customers discovers on a Monday that an attacker exfiltrated a customer table (names, emails, hashed passwords, last four card digits, shipping addresses) over the prior weekend. About 38,000 US residents across 41 states and 2,100 EU residents. Passwords hashed with a salted algorithm; salts stored separately and not accessed per preliminary forensics. The user supplied their firm's 50-state survey (as-of date stated) and the GDPR articles on breach notification.

**Output (excerpt):**
- **Open fact question:** Were password hashes crackable at scale and are credentials in the dataset reused for account access? Many supplied state definitions include "username or email plus password or security question" only where the credential would permit access `[VERIFY per state in survey]`. Owner: forensics; due Wednesday.
- **Clock register:** EU supervisory-authority notice — trigger is the controller "becoming aware" as defined in the supplied text; the 72-hour period is stated in the supplied article; earliest awareness Monday 09:40 → deadline Thursday 09:40, with phased notification permitted where facts are incomplete (per supplied text). US states — per survey; three states in the survey have fixed-day deadlines keyed to "determination," which is not yet made; others require notice "without unreasonable delay."
- **Triage row:** State X — breach definition met only if the credential element applies → **Pending facts**; AG notice threshold in survey is 500 residents; State X count 612 → AG notice required if individual notice is.
- **Decision log entry:** "Tuesday 16:00 — Notify EU supervisory authority on Wednesday with phased update; do not wait for final US determination. Basis: EU clock running from awareness; decided by GC."

---

## Verification

- [ ] Jurisdiction lock: every clock, threshold, and content rule traced to supplied text or marked `[VERIFY]`.
- [ ] Citation discipline: no deadlines, thresholds, or regulator details asserted from memory.
- [ ] Each clock's trigger event recorded separately; no single "discovery date" for all regimes.
- [ ] Privilege structure established before forensic reporting.
- [ ] Encryption safe harbor claimed only with key-status confirmed.
- [ ] Notices contain only confirmed facts, meet supplied content requirements, and are mutually consistent.
- [ ] Contractual and insurer notices tracked with their own clocks.
- [ ] Decision log includes reasons for any decision not to notify.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Asserting "state X requires notice within N days" from memory | Use the supplied survey or statute; otherwise `[VERIFY]` in the clock register |
| Starting every clock at discovery | Record each regime's trigger as defined; some run from awareness, some from determination |
| "Strictest-state" notice sent everywhere | Base template plus jurisdiction inserts for content and method |
| Encrypted data treated as exempt though keys were exposed | Confirm key status before applying any safe harbor |
| Notice says "no evidence of misuse" before forensics can support it | State only confirmed facts; describe what is being done |
| Forgetting customer and insurer notice clauses | Contractual clocks are in the register alongside statutory ones |
| Forensic report commissioned by IT directly | Counsel engages forensics for legal advice; business report separate |
| Treating processor role as "no obligations" | Processors notify controllers under contract and applicable law; track that clock |
