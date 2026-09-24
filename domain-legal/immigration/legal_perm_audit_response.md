---
title: "PERM Labor Certification Audit Response"
category: legal/immigration
description: "Attorney-facing response to a DOL PERM audit notification — requirement-by-requirement reconstruction of the recruitment file, applicant-disposition review for lawful job-related rejections, prevailing wage and job-requirement consistency, business-necessity support, and ability-to-pay evidence — with the audit deadline taken only from the notice and every regulatory reference marked for verification."
techniques:
  - ST-02
  - RT-05
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - immigration
  - perm
  - labor-certification
  - audit-response
  - recruitment
  - prevailing-wage
updated: "2026-09-24"
reasoning:
  styles: [evidential, procedural, analytic]
  stakes: critical
  horizon: weeks
  uncertainty: risk
  evidence_quality: moderate
  domain_complexity: regulated
  collaboration: small_team
  output_format: structured
  user_role: [lawyer]
  mode: [respond, audit]
related_prompts:
  - domain-legal/immigration/legal_h1b_rfe_response.md
  - domain-legal/immigration/legal_eb1_extraordinary_ability_petition.md
  - domain-legal/employment-labor/legal_workplace_investigation_plan_and_report.md
  - domain-legal/discovery/legal_document_review_coding_taxonomy.md
---

# PERM Labor Certification Audit Response

**Objective:** Produce a complete, internally consistent audit response package: every document the audit notification requests, a recruitment report that accounts for every applicant with a lawful, job-related reason for each rejection, proof that each recruitment step occurred in the required window, consistency between the job requirements, the prevailing wage determination, and the application, and — where requested — business-necessity and ability-to-pay support. The response surfaces defects the attorney must decide how to handle rather than papering over them.

> **Scope guard — attorney-facing only.** For immigration counsel preparing a response on behalf of the employer. It does not advise the foreign worker on status or options. If the person running it is the employee or an unrepresented employer, stop and route to `domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_authority_router.md`.

**When to use:**
- A PERM audit notification has issued on a filed labor certification.
- Pre-filing internal audit of a recruitment file before submitting the application.

**Distinct from:**
- `legal_h1b_rfe_response.md` (this folder) — USCIS nonimmigrant adjudication; PERM audits are DOL and test the labor-market test.
- `domain-legal/employment-labor/legal_workplace_investigation_plan_and_report.md` — internal HR investigations; the only overlap is document gathering.
- Supervised recruitment orders and denials/requests for review — different posture; flag and stop.

**Audience:** Immigration attorneys and supervised paralegals representing employers.

---

## Your Input

- **Audit notification:** [Paste in full, including the response due date as printed]
- **Application as filed:** [Job title, duties, minimum requirements (education, experience, alternative requirements, special skills), worksite, offered wage]
- **Prevailing wage determination:** [PWD, SOC code, wage level, validity dates]
- **Recruitment file:** [Each mandatory and additional recruitment step with dates, tear sheets, postings, notice of filing with posting dates and locations]
- **Applicant file:** [Every applicant, résumé, contact attempts with dates and methods, interview notes, disposition and reason]
- **Business-necessity facts:** [If requirements exceed normal for the occupation — why the business needs them]
- **Ability to pay:** [Tax returns, audited financials, annual reports, payroll records for the beneficiary]
- **Current rules you have verified:** [Recruitment timing windows, required steps, audit response period — or leave blank for `[VERIFY]`]

---

## Constraints

### Must
- Take the **response deadline only from the audit notification**; state the consequence of missing it `[VERIFY: 20 CFR 656.20]`.
- Build a **document-request checklist** from the notification text and mark each Produced / Partially produced / Unavailable (with explanation).
- Reconstruct the **recruitment timeline** and test each step against the required timing window and content `[VERIFY: 20 CFR 656.17(e) and 656.10(d)]`.
- Account for **every applicant**: contact attempts (timely and by more than one method where applicable), and a **lawful, job-related** rejection reason tied to the stated minimum requirements.
- Flag rejections that rely on requirements **not in the application**, on overqualification without basis, or on failure to respond where contact was inadequate.
- Test **consistency**: application requirements = posting requirements = PWD requirements; wage offered ≥ PWD.
- Support **business necessity** only where requirements exceed normal and only with real business facts `[VERIFY: business-necessity standard]`.
- Present **ability-to-pay** evidence for the relevant period `[VERIFY: 8 CFR 204.5(g)(2) evidence types]`.

### Must Not
- Create, recreate, or backdate recruitment documents, résumés, or notes. Missing documents are disclosed as unavailable with explanation.
- Offer post hoc rejection reasons not recorded at the time; if the contemporaneous reason is missing, flag it.
- Characterize a U.S. applicant as unqualified if the applicant could acquire the skill during a reasonable training period, without addressing that question `[VERIFY: applicable standard]`.
- Invent regulation sections, timing windows, or DOL form fields.
- Advise the beneficiary directly.

---

## Instructions

1. **Parse the notification** into a checklist of requested items.
2. **Timeline reconstruction** — every recruitment step with dates; test against windows.
3. **Content check** — each ad and posting contains required elements and matches the application.
4. **Applicant disposition review** — table of every applicant with contact log and reason; categorize each as Defensible / At risk / Defective.
5. **Consistency check** — application vs. postings vs. PWD vs. offered wage.
6. **Business necessity** (if triggered).
7. **Ability to pay** evidence.
8. **Defect report for the attorney** — defects found, whether they are curable, and the attorney's options (respond with explanation, withdraw and re-file) — the decision is the attorney's.
9. **Response package** — cover letter, index, recruitment report.

---

## Output Format

```markdown
# PERM Audit Response — {Employer} / Case No. {…}
**Audit notification date:** {…}  |  **Response due (per notice):** {…}  |  **Attorney Work Product**

## 1. Requested-Items Checklist
| # | Item requested (quoted) | Status | Exhibit | Note |
## 2. Recruitment Timeline
| Step | Required? | Date(s) | Window check [VERIFY] | Content check | Evidence |
## 3. Applicant Disposition Review
| Applicant | Contact attempts (date / method) | Response | Disposition | Reason (contemporaneous?) | Rating |
## 4. Consistency Check
| Requirement | Application | Postings | PWD | Consistent? |
## 5. Business Necessity (if applicable)
## 6. Ability to Pay
| Year | Evidence | Wage offered | Test | Result |
## 7. Defect Report (for attorney decision)
## 8. Response Cover Letter (draft) and Exhibit Index
```

---

## Worked Example

**Input (abridged):** Employer: software firm. Position requires Master's + 2 years' experience with a specified streaming framework. Recruitment: two Sunday newspaper ads, job order, notice of filing, three additional steps. Eleven applicants; employer rejected four as "not enough experience with the framework," one as "overqualified," and six did not respond to a single email.

**Output (excerpt):**

> **Applicant review:** Six non-responders were contacted by one email each with no follow-up — **At risk**: a single contact attempt may be found inadequate `[VERIFY: DOL standard on good-faith contact]`; check whether phone numbers were available on résumés. The "overqualified" rejection — **Defective** unless the contemporaneous record shows a lawful job-related reason; overqualification alone is generally not a lawful reason `[VERIFY]`. Four framework rejections — **Defensible** only if the framework requirement appears in the application, the postings, and the PWD request; consistency table shows the notice of filing omitted it → **At risk**.
>
> **Defect report:** Two issues may not be curable by explanation (overqualified rejection; posting inconsistency). Attorney options: respond with full disclosure and explanation, or withdraw and re-recruit. The response package will not add reasons that were not recorded at the time.

---

## Verification

- [ ] Jurisdiction lock: DOL PERM regulations; regulation version tied to filing date `[VERIFY]`.
- [ ] Response deadline taken from the notification and stated prominently.
- [ ] Every requested item accounted for.
- [ ] Every recruitment step tested for timing and content.
- [ ] Every applicant accounted for with contemporaneous reasons.
- [ ] Application, postings, and PWD requirements consistent — or inconsistency flagged.
- [ ] Defects reported for attorney decision, not concealed.
- [ ] No created, recreated, or backdated documents; no invented rules.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Supplying post hoc rejection reasons | Use only contemporaneous reasons; flag missing ones |
| Treating one unanswered email as adequate contact | Check contact methods and follow-up against the standard |
| Rejecting for requirements not in the application | Compare each rejection reason to the stated minimums |
| Missing posting-content inconsistencies | Compare every posting to the application line by line |
| Rejecting as overqualified | Flag as defective absent a lawful job-related reason |
| "Recreating" lost tear sheets or notices | Disclose as unavailable with explanation; never recreate |
| Estimating the response deadline | Use the date on the notification |
