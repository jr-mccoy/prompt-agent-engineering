---
title: "Research Misconduct Self-Audit"
category: science/ethics-integrity
description: "A neutral pre-submission self-audit that checks a manuscript and its underlying data against the fabrication/falsification/plagiarism triad and common questionable research practices, producing a remediation register to clear before submission."
techniques:
  - ST-01
  - RT-01
  - QA-01
  - QA-02
  - CM-02
  - NE-10
difficulty: advanced
tags:
  - research-misconduct
  - fabrication
  - falsification
  - plagiarism
  - questionable-research-practices
  - pre-submission
  - integrity
  - self-audit
updated: "2026-06-26"
related_prompts:
  - domain-science/ethics-integrity/science_authorship_and_credit_resolver.md
  - domain-science/ethics-integrity/science_conflict_of_interest_disclosure_drafter.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
---

# Research Misconduct Self-Audit

**Objective:** Help an author verify, before submission, that their manuscript and underlying records are clean against the ORI fabrication/falsification/plagiarism (FFP) triad and common questionable research practices (QRPs). It produces a risk register of items to confirm and remediate. It is a self-check tool framed around evidence the author should be able to show — not an accusation tool, and not a finding of misconduct.

**When to use:** During final pre-submission review, after the analysis is locked but before the byline is finalized and the manuscript leaves the team. Re-run after major revision.

**Required inputs:**
- **Discipline.** <field; sets norms for raw-data retention, image use, and reporting>
- **Study / manuscript context.** <output type, key claims, the datasets/figures/tables involved; user-supplied, never invented>
- **Data and records availability.** <what raw data, lab notebooks, code, and logs the author can produce on request; `[user-supplied]` for anything not stated>

**Optional inputs:**
- Similarity-check (plagiarism) report, if already run.
- Prior outputs from the same dataset (for self-plagiarism / salami-slicing check).
- The pre-registration or analysis plan, if one exists.
- Co-author confirmations that data are genuine and approved.

**Constraints — Must:**
- Audit against the FFP triad: **fabrication** (invented data/results), **falsification** (manipulating data, materials, or processes; misrepresenting results), and **plagiarism** (appropriating others' work/ideas/text), using ORI definitions.
- Cover QRPs: selective reporting, p-hacking/HARKing (hand the statistical detail to the appropriate methods/stats prompt), self-plagiarism / text recycling, salami slicing, and undisclosed data exclusions.
- Frame every item as a verifiable check ("verify you can reproduce every reported number from raw data"), never as a label applied to the author.
- For data integrity, look for red flags the author should rule out: impossible precision, suspiciously clean/uniform data, numbers untraceable to raw records, and missing raw data.
- For image integrity, point to the dedicated image-integrity prompt for splicing/duplication/adjustment detail rather than re-deriving it here.
- Use probability-weighted framing (NE-10) only to prioritize which items to confirm first by likelihood × severity — not to estimate guilt.

**Constraints — Must Not:**
- Do not invent facts, contributions, financial relationships, citations, or institutional policies. Work only from user-supplied content; mark gaps `[user-supplied]`.
- This prompt organizes/structures/flags only; it does not adjudicate guilt, give a legal/HR determination, or replace the institution's research-integrity office / ORI / COPE process. Route formal allegations there.
- Do not conclude that misconduct occurred or assign intent; flag items to confirm, nothing more.
- Do not label the author or any contributor; keep framing on the evidence.
- Do not use "novel/groundbreaking/first-ever" in any drafted text.

**Instructions:**

1. **Confirm scope.** Restate discipline, output type, key claims, and which datasets, figures, and tables are in scope. Mark missing records `[user-supplied]`.
2. **Traceability check.** For each reported number, statistic, and figure, ask whether the author can reproduce it from raw data and records; mark traceable / not-yet-confirmed / `[user-supplied]`.
3. **Fabrication red flags.** Surface impossible precision, too-uniform distributions, and any value with no raw-data source as items to confirm.
4. **Falsification red flags.** Check for undisclosed exclusions, selective time windows, reprocessed-without-record data, and inconsistent n across tables. Hand image-manipulation specifics to the image-integrity prompt.
5. **Plagiarism and recycling.** Check text/idea attribution, quotation and citation completeness, self-plagiarism/text recycling against prior outputs, and salami slicing of one study into many papers.
6. **QRP scan.** Note selective reporting and any analysis-after-results-known concerns; route statistical specifics (p-hacking/HARKing) to the stats prompt.
7. **Prioritize (NE-10).** Rank open items by likelihood × severity so the author confirms the highest-impact ones first.
8. **Build the remediation register.** For each item: the check → evidence that would confirm it clean → current status → remediation action to complete before submission.
9. **Self-check and route.** Confirm nothing was invented and no label was applied; remind the author that any genuine concern goes to the institution's research-integrity office, not this tool.

**Output format (locked):**

```
## Scope Confirmation
[discipline, output type, key claims, datasets/figures/tables in scope]

## Traceability Summary
[count traceable / not-yet-confirmed / `[user-supplied]`; notable gaps]

## Risk Register
| Item | Category (Fabrication/Falsification/Plagiarism/QRP) | Evidence to confirm clean | Status | Likelihood×Severity | Remediation before submission |

## Image Integrity
[handoff note to the image-integrity prompt + any flags]

## Priority Actions (highest impact first)
1. ...

## Route-Out Note
[any genuine concern → institution research-integrity office / ORI; this is a self-audit, not a determination]
```

**Standard alignment:** ORI definitions of research misconduct (fabrication, falsification, plagiarism); WCRI Singapore/Hong Kong principles; COPE guidance on data and reproducibility concerns (for the route-out, not for adjudication here).

**Verification checklist (before delivering):**
- [ ] Discipline and study/manuscript context captured first.
- [ ] FFP triad and QRPs each addressed.
- [ ] Every reported number checked for raw-data traceability.
- [ ] Framing is evidence-based and non-accusatory throughout.
- [ ] Image-integrity detail routed to the dedicated prompt.
- [ ] Items prioritized by likelihood × severity, not by guilt.
- [ ] No fact, citation, or policy invented; gaps marked `[user-supplied]`.
- [ ] No conclusion of misconduct or intent; no labeling of the author.
- [ ] Route-out to the integrity office stated explicitly.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Implied verdict | A register that reads as a finding of misconduct | Frame as items to confirm; add the route-out note |
| Intent inference | Calling an exclusion "falsification" | Flag the undisclosed exclusion to confirm; never assign intent |
| Clean-by-assertion | Marking numbers traceable without records | Require the author to produce raw-data evidence; else `[user-supplied]` |
| Stats overreach | Re-deriving p-hacking analysis here | Route statistical specifics to the stats prompt |
| Self-plagiarism blind spot | Ignoring overlap with the team's prior papers | Check against supplied prior outputs for recycling/salami slicing |
