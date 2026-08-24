---
title: "NSF Proposal Outliner (Intellectual Merit + Broader Impacts)"
category: science/grants-funding
description: "Outline an NSF proposal with Intellectual Merit and Broader Impacts woven throughout the Project Summary and Project Description, mapped to the five merit-review elements."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-01
  - QA-02
  - CM-02
difficulty: advanced
tags:
  - nsf
  - intellectual-merit
  - broader-impacts
  - merit-review
  - project-description
  - grant-writing
  - research-funding
updated: "2026-06-26"
related_prompts:
  - domain-science/grants-funding/science_specific_aims_drafter.md
  - domain-science/grants-funding/science_nih_r01_outline_drafter.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
---

# NSF Proposal Outliner (Intellectual Merit + Broader Impacts)

**Objective:** Produce an NSF proposal outline in which Intellectual Merit (IM) and Broader Impacts (BI) are woven through the Project Summary and Project Description rather than bolted on as an afterthought paragraph. The outline maps the user's science to the five NSF merit-review elements and includes a concrete Broader Impacts plan with activities and assessment.

**When to use:** You have a defined research project and need a structured NSF-style outline (Project Summary + Project Description + Broader Impacts plan) before drafting prose, for a target NSF solicitation or the standard program announcement.

**Required inputs:**
- **Discipline.** The scientific field and NSF directorate/division if known.
- **Study type.** Observational / experimental / computational / theoretical / mixed.
- **Funding mechanism.** The target NSF solicitation or program (e.g., CAREER, standard research grant) — review elements and required sections follow it.
- **The science.** Objectives, the gap, the planned activities, and the intellectual contribution, in the user's words.

**Optional inputs:**
- **Results from prior NSF support.** Required if the PI/co-PIs had NSF support in the prior five years (`[user-supplied]`).
- **Broader Impacts assets.** Existing outreach, education, broadening-participation, or infrastructure activities to build on (`[user-supplied]`).
- **Team and institutional context.** Collaborators, facilities, partnerships (`[user-supplied]`).

**Constraints — Must:**
- Map content to the five NSF merit-review elements (what is the activity; how well conceived/organized; qualifications; access to resources; and the IM/BI of the proposed activity).
- Weave IM and BI into the Project Summary (which must explicitly address both) and into the Project Description narrative, not isolate BI in a single trailing paragraph.
- Make Broader Impacts concrete: specific activities, who they reach, and how outcomes are assessed.
- Surface rigor and reproducibility / data-management expectations and a Data Management Plan placeholder.

**Constraints — Must Not:**
- Do not invent citations, DOIs, preliminary data, collaborator names, institutional resources, or specific funding-program rules/budget caps. If needed and not supplied, mark `[user-supplied]` and ask; funder-specific policy/figures are `[user-supplied]`/verify against the current solicitation/PAPPG.
- Do not fabricate "results from prior NSF support"; if applicable and not supplied, mark `[user-supplied]`.
- Do not use "novel," "groundbreaking," "first-ever," or "gold standard" as empty descriptors in drafted text; state the intellectual contribution as a specific delta.
- Do not treat Broader Impacts as a generic "we will give talks" placeholder; require specificity and assessment.

**Instructions:**

1. **Intake and gate.** Confirm discipline/directorate, study type, the target solicitation, and the science. If objectives or BI plans are missing, mark `[user-supplied]` and ask before outlining.
2. **Draft the Project Summary.** Produce three bulleted components: Overview, Intellectual Merit, and Broader Impacts — each addressed explicitly, since NSF requires the summary to cover IM and BI separately.
3. **Outline objectives and the gap.** Bullet the specific objectives and the knowledge gap, framing the intellectual contribution as a concrete delta versus the current state of the field.
4. **Insert Results from Prior NSF Support (conditional).** If applicable, outline the required summary of prior outcomes (IM and BI); mark all specifics `[user-supplied]`. If not applicable, state so.
5. **Outline the research plan.** Bullet the approach, methods, and expected outcomes. Where the science warrants, note rigor and reproducibility considerations and validation.
6. **Weave IM through the narrative.** At each major activity, note its intellectual contribution explicitly so IM is distributed across the Project Description, not summarized once.
7. **Build the Broader Impacts plan.** Specify activities (e.g., education, broadening participation, public engagement, infrastructure, societal benefit), the audiences/partners, the timeline, and the assessment method for each. Tie BI to the research where integration is genuine.
8. **Add the Data Management / sharing plan placeholder.** Note the data types, formats, sharing approach, and any open-science commitments; mark specifics `[user-supplied]`.
9. **Map to merit-review elements and critique.** Produce a short table mapping outline content to the five review elements, then a reviewer-lens critique flagging where IM or BI is thin, generic, or unassessed.

**Output format (locked):**

```
## Project Summary
- Overview: [...]
- Intellectual Merit: [...]
- Broader Impacts: [...]

## Project Description — Objectives & Gap
- Objectives: [...]
- Gap / intellectual contribution (as a delta): [...]

## Results from Prior NSF Support
- [Applicable? If yes: prior outcomes incl. IM and BI — [user-supplied]. If no: "Not applicable."]

## Research Plan
- Approach & methods: [...]
- Expected outcomes: [...]
- Rigor / reproducibility considerations: [...]
- Intellectual Merit woven per activity: [...]

## Broader Impacts Plan
- Activity 1: [what / who it reaches / timeline / assessment]
- Activity 2: [...]
- Integration with the research: [...]

## Data Management / Sharing Plan
- [Data types, formats, sharing, open-science commitments — [user-supplied]]

## Merit-Review Element Map
| Review element | Where addressed |
|---|---|
| Activity / what is proposed | [...] |
| Conception / organization | [...] |
| Qualifications | [...] |
| Resources / access | [...] |
| IM & BI of the activity | [...] |

## Reviewer-Lens Critique
- IM distributed vs concentrated: [...]
- BI specificity & assessment: [...]
- Hype scan: [...]

## Open Items ([user-supplied])
- [Citations, prior-support outcomes, BI partners, DMP specifics, solicitation rules to verify]
```

**Reporting-standard alignment:** NSF merit-review criteria (Intellectual Merit and Broader Impacts) and the five review elements; Project Summary IM/BI requirement; Data Management Plan expectation. Solicitation-specific sections, page limits, and program rules are `[user-supplied]`/verify against the current solicitation and PAPPG.

**Verification checklist (before delivering):**
- [ ] Discipline/directorate, study type, and solicitation captured.
- [ ] Project Summary addresses Overview, IM, and BI separately.
- [ ] IM is woven across the Project Description, not isolated.
- [ ] Broader Impacts plan has specific activities, audiences, and assessment.
- [ ] Results from Prior NSF Support handled (applicable or explicitly N/A); specifics `[user-supplied]`.
- [ ] Data Management / sharing plan placeholder present.
- [ ] Content mapped to the five merit-review elements.
- [ ] No fabricated citations, prior outcomes, partners, or program rules; all `[user-supplied]`.
- [ ] No empty hype descriptors; contribution stated as a delta.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| BI bolt-on | One trailing "broader impacts" paragraph of generic outreach | Require BI woven in plus a concrete plan with activities and assessment |
| Fabricated prior support | Inventing outcomes from "prior NSF award" | Mark all prior-support specifics `[user-supplied]`; state N/A if none |
| IM concentrated, not distributed | Strong IM only in the summary, absent from activities | Annotate intellectual contribution at each major activity |
| Vague BI assessment | "We will measure success" with no method | Require an assessment method per BI activity |
| Hype as merit | "Groundbreaking, first-ever" intellectual contribution | Ban empty descriptors; force a specific delta vs the field |
| Stale solicitation assumptions | Asserting page limits/sections from memory | Mark solicitation/PAPPG specifics `[user-supplied]`/verify |
