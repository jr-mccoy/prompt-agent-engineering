---
title: "H-1B Request for Evidence (RFE) Response"
category: legal/immigration
description: "Attorney-facing response to an H-1B Request for Evidence — issue-by-issue decomposition of the RFE, specialty-occupation argument tied to the position's actual duties and degree requirement, bona fide employment / employer-employee and third-site evidence, LCA and prevailing-wage consistency, an exhibit plan, and a cover brief — with the response deadline taken only from the notice and every regulatory standard marked for verification against current rules and policy."
techniques:
  - ST-02
  - RT-05
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - immigration
  - h-1b
  - rfe
  - specialty-occupation
  - prevailing-wage
  - uscis
updated: "2026-09-24"
reasoning:
  styles: [evidential, adversarial, analytic]
  stakes: critical
  horizon: weeks
  uncertainty: risk
  evidence_quality: moderate
  domain_complexity: regulated
  collaboration: small_team
  output_format: [memo, structured]
  user_role: [lawyer]
  mode: [respond, document]
related_prompts:
  - domain-legal/immigration/legal_perm_audit_response.md
  - domain-legal/immigration/legal_eb1_extraordinary_ability_petition.md
  - domain-legal/employment-labor/legal_wage_hour_classification_analysis.md
  - domain-legal/research/legal_research_memo_irac.md
---

# H-1B Request for Evidence (RFE) Response

**Objective:** Build a response that answers every issue the RFE raises — not just the headline one — with evidence matched to the standard the officer is applying: a specialty-occupation argument grounded in the petitioner's actual duties, industry norms, and its own hiring history; proof of a bona fide job and the petitioner's right to control the work (including at third-party sites); and consistency among the petition, the LCA, the offered wage, and the occupational classification. The output is an issue map, an exhibit plan, and a cover brief ready for attorney review.

> **Scope guard — attorney-facing only.** This prompt is for a licensed immigration attorney or an accredited representative preparing a filing. It does not assess any individual's status, eligibility, or options. If the person running it is the beneficiary or an employer without counsel, stop and route to `domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_authority_router.md` to find qualified representation.

**When to use:**
- An RFE issued on an H-1B petition (cap, change of employer, extension, amendment).
- Pre-filing stress test of a petition against the issues RFEs typically raise for this occupation.

**Distinct from:**
- `legal_perm_audit_response.md` (this folder) — DOL audit of a permanent labor certification, a different agency and standard.
- `domain-legal/employment-labor/legal_wage_hour_classification_analysis.md` — FLSA wage-hour classification, not LCA prevailing-wage compliance.
- NOIDs and denials — a notice of intent to deny or an appeal/motion needs different posture and deadlines; flag and stop.

**Audience:** Immigration attorneys and supervised paralegals.

---

## Your Input

- **RFE text:** [Paste in full, including the response due date as printed on the notice]
- **Petition as filed:** [Job title, duties with percentages, minimum requirements, worksite(s), SOC code and wage level on the LCA, offered wage]
- **Petitioner facts:** [Industry, size, organizational chart, hiring history for this role, degree requirements in past postings]
- **Beneficiary facts:** [Degree(s), field, evaluations, experience — relevant only to the issues raised]
- **Worksite facts:** [Petitioner premises / remote / third-party client site; contracts, SOWs, client letters, itinerary]
- **Evidence available:** [Expert opinion letters, industry surveys, job postings from peers, internal documents]
- **Current rules you have verified:** [Applicable regulatory definition of specialty occupation and effective date, current policy guidance — or leave blank for `[VERIFY]`]

---

## Constraints

### Must
- **Decompose the RFE** into each separate issue and the specific evidence requested; answer every one, including those that appear boilerplate.
- Take the **response deadline only from the notice**; state it prominently and mark any internal target dates. Never compute it from a general rule.
- Tie the **specialty-occupation** argument to the regulatory criteria in force for the filing date `[VERIFY: 8 CFR 214.2(h)(4) as amended and effective date]` — the position's duties, the degree requirement, and the direct relationship between the required field of study and the duties.
- Show **LCA consistency**: SOC code, wage level, worksite(s), and duties must align; an officer can treat a low wage level as inconsistent with a claim of complex, specialized duties.
- Address **bona fide employment** and the petitioner's control over the work, including third-party placement evidence, as the current rule and policy require `[VERIFY]`.
- Build an **exhibit plan**: each exhibit, what it proves, which RFE issue it answers, and its source.
- Mark every regulatory cite, policy-manual reference, and form edition `[VERIFY]` unless supplied.

### Must Not
- Invent duties, hiring history, client contracts, or expert credentials; missing evidence becomes `[NEED: …]`.
- Draft or suggest altered, backdated, or newly created documents presented as contemporaneous.
- Rely on the job title or on the occupation's general reputation instead of the actual duties.
- Change the position described in the petition to fit the argument — a material change can require a new petition.
- Cite AAO decisions or cases not supplied; use `[CITE: …]` / `[NEED HOLDING: …]`.
- Advise the beneficiary directly on status, travel, or alternatives.

---

## Instructions

1. **Issue map.** Number each RFE issue; quote the operative language; list the evidence the officer asked for.
2. **Standard per issue.** State the standard the officer applies `[VERIFY]` and the burden (preponderance of the evidence).
3. **Specialty-occupation argument.** Duties breakdown with percentages → specialized knowledge required → degree in a specific specialty (or equivalent) normally required → evidence: petitioner's hiring history, peer postings, expert opinion with a disclosed basis.
4. **LCA and wage consistency.** Compare duties to the SOC description and wage level; explain any apparent inconsistency truthfully.
5. **Employment and control.** Bona fide position; itinerary or client documentation for off-site work.
6. **Beneficiary qualifications** (only if raised): degree equivalence and field match.
7. **Exhibit plan** with index.
8. **Cover brief** — issue-by-issue, each heading mirroring the RFE's language.
9. **Risk note** for the attorney: weakest issue, whether the evidence cures it, and whether a withdrawal-and-refile or alternative strategy should be considered (attorney decision).

---

## Output Format

```markdown
# H-1B RFE Response — {Petitioner} / {Beneficiary} — Receipt No. {…}
**RFE issued:** {date}  |  **Response due (per notice):** {date}  |  **Internal target:** {date}  |  **Attorney Work Product**

## 1. Issue Map
| # | RFE issue (quoted) | Evidence requested | Standard [VERIFY] | Evidence we have | Gaps |
## 2. Specialty-Occupation Analysis
| Duty | % time | Specialized knowledge required | Degree field link | Evidence |
## 3. LCA / Wage Consistency Check
## 4. Employment and Control / Worksite
## 5. Beneficiary Qualifications (if raised)
## 6. Exhibit Plan
| Ex. | Document | Proves | RFE issue | Source | Status |
## 7. Cover Brief (draft)
## 8. Attorney Risk Note
## 9. Verification Items
```

---

## Worked Example

**Input (abridged):** Petitioner: 40-person fintech. Position: "Data Engineer," LCA at Level I under a computer-occupation SOC code. RFE raises (1) specialty occupation — duties "generic" and degree requirement "not in a specific specialty"; (2) request for evidence of the actual work location. Petition lists minimum requirement: "Bachelor's in Computer Science, Engineering, or related field." Response due per notice: printed date.

**Output (excerpt):**

> **Issue 1 — degree field.** The requirement "Computer Science, Engineering, or related field" invites the officer's concern that a range of unrelated engineering disciplines qualifies. The response must show each accepted field is directly related to the duties (e.g., data-pipeline design requires coursework in data structures, distributed systems, databases) — not rewrite the requirement. Evidence: petitioner's last four hires into the role (degrees and fields) `[NEED: HR records]`; three peer postings with the same requirement; an expert opinion that states its basis in the duties, not the title.
>
> **Issue 1 — wage-level tension.** The petition describes designing streaming architecture (complex) while the LCA is Level I. Address directly: Level I reflects the petitioner's experience requirement, not the complexity of duties, *if* the duties are performed under supervision as described `[VERIFY: current DOL wage-level guidance]`. If the duties as performed exceed Level I, flag to the attorney — this may be an LCA problem, not a briefing problem.
>
> **Issue 2 — work location.** Beneficiary works hybrid from petitioner's office and home; confirm the home address was covered by the LCA or a posting obligation was met `[VERIFY: LCA worksite rules]`; if not, flag as a compliance issue for attorney decision before responding.

---

## Verification

- [ ] Jurisdiction lock: USCIS adjudication; regulation version tied to filing date `[VERIFY]`.
- [ ] Every RFE issue answered, including boilerplate items.
- [ ] Response deadline taken from the notice and stated prominently.
- [ ] Specialty-occupation argument built from duties and evidence, not job title.
- [ ] LCA, wage level, SOC code, worksite, and duties checked for consistency.
- [ ] Exhibit plan maps each exhibit to an issue.
- [ ] No invented evidence, credentials, AAO decisions, or cases; no altered documents.
- [ ] No advice addressed to the beneficiary.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Answering only the headline issue | Map and answer every numbered issue; unanswered items support denial |
| Arguing the title ("engineers always need degrees") | Argue the duties, the required field, and the direct relationship |
| Ignoring LCA wage level vs. duty complexity | Reconcile truthfully or flag the LCA problem to the attorney |
| Changing duties in the response to fit the argument | Material changes may require a new petition; explain, don't rewrite |
| Expert letter that recites conclusions | Require the expert to state the basis in the specific duties |
| Computing the response deadline from a general rule | Use the date printed on the notice; flag mailing and filing method |
| Addressing the beneficiary about status or travel | Out of scope; attorney-facing only |
