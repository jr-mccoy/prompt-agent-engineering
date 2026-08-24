---
title: "Open Science Practices Self-Audit"
category: science/ethics-integrity
description: "Score a research project against FAIR, CARE, and TRUST plus preregistration, open materials/code, and open access, producing a framework-scored audit table to run at submission and again at study close."
techniques:
  - ST-01
  - RT-01
  - ST-03
  - DS-02
  - QA-01
  - CM-02
difficulty: advanced
tags:
  - open-science
  - fair-data
  - care-principles
  - trust-principles
  - preregistration
  - reproducibility
  - data-governance
  - self-audit
updated: "2026-06-26"
related_prompts:
  - domain-science/ethics-integrity/science_conflict_of_interest_disclosure_drafter.md
  - domain-science/ethics-integrity/science_misconduct_self_audit.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
---

# Open Science Practices Self-Audit

**Objective:** Audit a project's open-science posture against FAIR (data Findable, Accessible, Interoperable, Reusable), CARE (Indigenous/community data governance), and TRUST (trustworthy repositories), plus preregistration, open materials/code, open access, and a reproducibility statement. It produces a scored table with per-framework sub-scores and concrete fixes, designed to run at submission and again at study close. Open practices are the default; closed/sensitive/Indigenous-governed data route to a named controlled branch, not a failing grade.

**When to use:** At manuscript or data-release submission, and again at study close (final archiving). Useful earlier as a planning checklist.

**Required inputs:**
- **Discipline.** <field; sets repository norms, metadata standards, and what "open" means>
- **Study / manuscript context.** <output type, the datasets/code/materials produced, and where they currently live; user-supplied, never invented>
- **Audit point.** <at-submission or at-study-close>

**Optional inputs:**
- Target repository/repositories and their certifications (e.g., CoreTrustSeal).
- Whether any data involve Indigenous, community, or otherwise sovereignty-governed populations.
- Pre-registration / registered-report status and link.
- Funder or journal open-science mandates.
- Licensing intentions for data, code, and materials.

**Constraints — Must:**
- Score each FAIR facet (F, A, I, R), each CARE principle where applicable (Collective benefit, Authority to control, Responsibility, Ethics), and TRUST repository criteria (Transparency, Responsibility, User focus, Sustainability, Technology).
- Use a fixed three-level rating (present / partial / absent) per practice and compute per-framework sub-scores (DS-02), with the rating definitions stated.
- Include preregistration, open materials, open code, open access, persistent identifiers (DOIs), metadata/standards, and a reproducibility statement as audited practices.
- Treat closed/sensitive/Indigenous-governed data via the **controlled / CARE branch**, named explicitly: "as open as possible, as closed as necessary," with access governance described — not scored as a FAIR failure.
- Distinguish "Accessible" (the protocol and metadata are open even if the data are restricted) from "open data," so controlled data still score on FAIR-A correctly.

**Constraints — Must Not:**
- Do not invent facts, contributions, financial relationships, citations, or institutional policies. Work only from user-supplied content; mark gaps `[user-supplied]`.
- This prompt organizes/structures/flags only; it does not adjudicate guilt, give a legal/HR determination, or replace the institution's research-integrity office / ORI / COPE process. Route formal allegations there.
- Do not recommend releasing sensitive, personally identifying, or Indigenous-governed data without the governing community's authority and consent.
- Do not treat a justified controlled-access decision as a deficiency or use "novel/groundbreaking/first-ever" in drafted text.

**Instructions:**

1. **Confirm scope.** Restate discipline, output type, the artifacts produced (data/code/materials), where they live, and the audit point (submission vs. close). Mark gaps `[user-supplied]`.
2. **Classify data sensitivity.** Determine whether any artifact is sensitive or Indigenous/community-governed; if so, route it to the controlled / CARE branch before scoring.
3. **Score FAIR.** Rate F, A, I, R per artifact (present/partial/absent), checking persistent IDs, metadata, accessible protocols, standard formats, and reuse licensing.
4. **Score CARE (where applicable).** Rate Collective benefit, Authority to control, Responsibility, and Ethics for community-governed data; describe the governance arrangement.
5. **Score TRUST.** Rate the chosen repository against Transparency, Responsibility, User focus, Sustainability, and Technology; note any certification.
6. **Audit additional practices.** Rate preregistration, open materials, open code, open access, and the reproducibility statement.
7. **Compute sub-scores (DS-02).** Produce per-framework sub-scores and an overall summary, stating the rating scale.
8. **Write fixes.** For each partial/absent item, give a specific, actionable fix and whether it is feasible by the audit point.
9. **Self-check.** Confirm controlled data are not scored as failures, nothing was invented, and gaps are marked `[user-supplied]`.

**Output format (locked):**

```
## Scope Confirmation
[discipline, output type, artifacts + locations, audit point]

## Data Sensitivity Classification
[open / controlled / Indigenous-community-governed per artifact; routing decisions]

## FAIR Audit
| Artifact | Facet (F/A/I/R) | Rating (present/partial/absent) | Gap | Fix |
FAIR sub-score: [x/total]

## CARE Audit (if applicable)
| Principle | Rating | Governance arrangement | Gap | Fix |
CARE sub-score: [x/total]  (or "Not applicable — no community-governed data")

## TRUST Audit (repository)
| Criterion | Rating | Notes / certification | Gap | Fix |
TRUST sub-score: [x/total]

## Additional Open-Science Practices
| Practice (preregistration / open materials / open code / open access / reproducibility statement) | Rating | Gap | Fix |

## Controlled / CARE Branch
[for sensitive or community-governed data: "as open as possible, as closed as necessary," access governance, consent/authority basis — not a deficiency]

## Summary & Priority Fixes
- Overall posture + per-framework sub-scores
- Priority fixes feasible by [audit point]
- Open items: [ ] [user-supplied gap]
```

**Standard alignment:** FAIR principles (Wilkinson et al. 2016); CARE principles for Indigenous data governance; TRUST principles for digital repositories; preregistration and open-access norms; reproducibility-statement conventions.

**Verification checklist (before delivering):**
- [ ] Discipline, artifacts, and audit point captured first.
- [ ] Data sensitivity classified before scoring.
- [ ] FAIR scored facet by facet with stated rating scale.
- [ ] CARE applied wherever community-governed data exist (or marked N/A with reason).
- [ ] TRUST scored against the named repository.
- [ ] Preregistration, open materials/code, open access, and reproducibility statement audited.
- [ ] Per-framework sub-scores computed; controlled data not scored as failures.
- [ ] No release recommended for sensitive/Indigenous data without authority/consent.
- [ ] No fact, repository, or policy invented; gaps marked `[user-supplied]`.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Open-by-default overreach | Scoring controlled data as a FAIR failure | Route to the controlled / CARE branch; score FAIR-A on metadata/protocol |
| CARE skipped | Treating Indigenous data like any open dataset | Apply CARE and require community authority/consent |
| Accessible ≠ open confusion | Marking restricted data "absent" on Accessibility | Credit accessible metadata/protocol even when data are restricted |
| Repository assumed trusted | Claiming TRUST without checking criteria | Score each TRUST criterion; note certification or `[user-supplied]` |
| Inflated sub-scores | Generous ratings to look compliant | State the present/partial/absent definitions and apply them consistently |
