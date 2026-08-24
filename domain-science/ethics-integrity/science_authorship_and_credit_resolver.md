---
title: "Authorship and Credit Resolver"
category: science/ethics-integrity
description: "Walk every contributor through the CRediT 14 roles and the ICMJE four authorship criteria to classify each person as author, acknowledged contributor, or neither, surface guest/ghost-authorship risk, and structure a fair author-order conversation."
techniques:
  - ST-01
  - RT-01
  - RT-03
  - ST-03
  - QA-01
  - CM-02
difficulty: advanced
tags:
  - authorship
  - credit-taxonomy
  - icmje
  - contributor-roles
  - research-ethics
  - author-order
  - guest-ghost-authorship
  - integrity
updated: "2026-06-26"
related_prompts:
  - domain-science/ethics-integrity/science_conflict_of_interest_disclosure_drafter.md
  - domain-science/ethics-integrity/science_misconduct_self_audit.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
---

# Authorship and Credit Resolver

**Objective:** Structure a transparent, standards-based conversation about who is an author, who is an acknowledged contributor, and how authors are ordered on a scholarly output. It maps each named contributor against the CRediT 14 contributor roles and the four ICMJE authorship criteria, surfaces guest- and ghost-authorship risk, and offers author-order options grounded in discipline conventions. It organizes the discussion; it does not adjudicate a genuine dispute.

**When to use:** During manuscript preparation, ideally before drafting the byline and well before submission — and again if the contributor set or contribution balance changes materially during the project.

**Required inputs:**
- **Discipline.** <field; sets author-order conventions, e.g. life sciences first/last vs. some fields alphabetical>
- **Study / manuscript context.** <working title, output type (article / preprint / dataset / software / chapter), target venue if known; user-supplied, never invented>
- **Contributor list.** <each named person and what they actually did, in the user's own words; `[user-supplied]` for any contribution not stated>

**Optional inputs:**
- Journal/venue authorship policy text (if it differs from ICMJE).
- Any prior agreement (e.g., a project contributorship plan).
- Funder or institutional authorship requirements.
- Known points of disagreement among contributors.

**Constraints — Must:**
- Apply the CRediT taxonomy (NISO Z39.104-2022) — all 14 roles — and record degree of contribution where the user supplies it (lead / equal / supporting).
- Apply the ICMJE four authorship criteria; require that an author meets **all four** (1: substantial contribution to conception/design or acquisition/analysis/interpretation; 2: drafting or critical revision; 3: final approval; 4: accountability), and preserve the "acknowledged but not an author" category for those who do not.
- Name guest authorship (named without qualifying) and ghost authorship (qualifies or wrote but omitted) explicitly when the inputs suggest either.
- Present author-order as options with rationale, naming the relevant discipline convention (first author, last/senior author, corresponding author, co-first/equal-contribution designation, alphabetical).
- Reflect contributions back verbatim or near-verbatim so the user can confirm accuracy before any classification.

**Constraints — Must Not:**
- Do not invent facts, contributions, financial relationships, citations, or institutional policies. Work only from user-supplied content; mark gaps `[user-supplied]`.
- This prompt organizes/structures/flags only; it does not adjudicate guilt, give a legal/HR determination, or replace the institution's research-integrity office / ORI / COPE process. Route formal allegations or unresolved disputes there.
- Do not assign or remove authorship unilaterally, settle a contested byline, or overrule a venue's stated policy.
- Do not use "novel," "groundbreaking," or "first-ever" in any drafted text.

**Instructions:**

1. **Confirm scope.** Restate discipline, output type, target venue, and the full contributor list as given. Mark any missing contribution detail `[user-supplied]` and ask the user to fill it before classifying.
2. **Catalog contributions.** For each contributor, mirror back what they did in their own words, then map it to one or more of the 14 CRediT roles, recording lead/equal/supporting where stated.
3. **Apply ICMJE criteria.** For each contributor, check each of the four criteria against the stated contributions. Mark each criterion met / not met / `[user-supplied]`.
4. **Classify each person.** Author (all four met) → acknowledged contributor (contributed but not all four) → neither. State the rationale per person; never infer a contribution that was not provided.
5. **Flag risk.** Identify possible guest authorship (proposed author missing criteria) and ghost authorship (a qualifying or writing contributor omitted, e.g. a medical writer). Frame as items to verify, not accusations.
6. **Compare order options (Tree of Thoughts).** Lay out 2-3 author-order arrangements consistent with discipline convention; for each, give who-leads/who-is-senior rationale, note co-first or equal-contribution footnote options, and name the corresponding-author duties.
7. **Define a fair process for disagreement.** Recommend a documented contributorship discussion, written confirmation from each author, and — for genuine impasse — escalation to the department/institution authorship policy or a COPE authorship-dispute pathway. Do not resolve the dispute here.
8. **Assemble deliverables.** Produce the contributor × CRediT matrix, the per-person determination, the order options, and the acknowledgments/contributorship-statement draft using calibrated language.
9. **Self-check.** Confirm no contribution, person, or policy was invented and that every gap is marked `[user-supplied]`.

**Output format (locked):**

```
## Scope Confirmation
[discipline, output type, venue, contributor list as given; gaps flagged]

## Contributor × CRediT Role Matrix
| Contributor | Conceptualization | Methodology | Software | Validation | Formal Analysis | Investigation | Resources | Data Curation | Writing – Original Draft | Writing – Review & Editing | Visualization | Supervision | Project Administration | Funding Acquisition |
[lead / equal / supporting / — per cell; `[user-supplied]` where unknown]

## ICMJE Four-Criteria Check
| Contributor | (1) Substantial contribution | (2) Draft/revise | (3) Final approval | (4) Accountability | All four met? |

## Authorship Determination (per person)
- [Name] → Author / Acknowledged contributor / Neither — rationale: ...

## Guest / Ghost Authorship Flags
[items to verify, neutral framing; or "none indicated by inputs"]

## Author-Order Options
- Option A: [order] — rationale, convention, corresponding author, co-first notes
- Option B: ...
- Option C: ...

## Disagreement Process (if needed)
[documented discussion → written confirmation → escalation route to institution / COPE]

## Draft Contributorship & Acknowledgments Statement
[CRediT-formatted statement + acknowledgments for non-author contributors]

## Open Items
- [ ] [user-supplied gap]
```

**Standard alignment:** CRediT (NISO Z39.104-2022) 14 contributor roles; ICMJE four authorship criteria and the author-vs-acknowledged distinction; COPE guidance on authorship and authorship disputes.

**Verification checklist (before delivering):**
- [ ] Discipline and study/manuscript context captured before any classification.
- [ ] Every contributor mapped to CRediT roles using only stated contributions.
- [ ] All four ICMJE criteria checked per contributor; authorship requires all four.
- [ ] Acknowledged-contributor and "neither" categories used where criteria are unmet.
- [ ] Guest- and ghost-authorship risk surfaced as verification items, not verdicts.
- [ ] Author-order presented as options with named discipline convention.
- [ ] No contribution, person, policy, or citation invented; gaps marked `[user-supplied]`.
- [ ] Drafted text free of "novel/groundbreaking/first-ever" and accusatory language.
- [ ] Genuine-dispute escalation routed to institution / COPE, not resolved here.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Inferred contribution | Assigning a CRediT role the user never described | Map only stated work; mark unstated as `[user-supplied]` |
| Criterion shortcut | Granting authorship on one strong contribution | Require all four ICMJE criteria explicitly |
| Order as ranking truth | Presenting one author order as the "correct" one | Offer options + rationale; name convention, do not decide |
| Hidden ghost author | Treating an omitted medical writer as a non-issue | Flag writing/qualifying contributors for explicit acknowledgment |
| Dispute adjudication | Declaring who "deserves" authorship | Route impasse to institution/COPE; structure only |
