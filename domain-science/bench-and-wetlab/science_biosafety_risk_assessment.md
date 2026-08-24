---
title: "Biosafety Risk Assessment & IBC Scaffold"
category: science/bench-and-wetlab
description: "Walk agent risk-group and BSL/ABSL containment determination logic at a governance level, build an IBC-submission scaffold, and route any dual-use or elevated-risk concern to the biosafety officer/IBC — with no operational uplift for creating or enhancing a hazard."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-02
  - CM-02
  - NE-10
difficulty: advanced
tags:
  - biosafety
  - risk-group
  - bsl-absl
  - containment
  - ibc-submission
  - nih-guidelines
  - dual-use
  - recombinant-nucleic-acids
updated: "2026-06-26"
related_prompts:
  - domain-science/ethics-integrity/science_dual_use_research_assessment.md
  - domain-science/bench-and-wetlab/science_animal_protocol_iacuc_drafter.md
  - domain-science/bench-and-wetlab/science_cell_culture_protocol_designer.md
---

# Biosafety Risk Assessment & IBC Scaffold

**Objective:** Help a researcher reason through agent risk-group (RG1–RG4) and biosafety-level (BSL/ABSL 1–4) containment determination at a governance and recognition level, and assemble an IBC-submission scaffold. This prompt is containment- and governance-level only: it gives no operational method for creating, enhancing, or weaponizing any hazard. It builds in a dual-use screen pointer and routes the final determination — and any elevated-risk or dual-use concern — to the institutional biosafety officer and IBC.

**When to use:** When planning work with biological agents, recombinant/synthetic nucleic acids, or animal pathogens and you need to structure a risk assessment and IBC submission before institutional review. If the described work sounds genuinely hazardous, the correct output is to stop and route to the biosafety officer/IBC — not to analyze further.

**Required inputs:**
- **Discipline.** Field and research area (e.g., microbiology, virology, gene therapy).
- **Study type.** Observational / experimental — and the high-level aim.
- **Agent / material class (described at a recognition level).** What category of agent or nucleic-acid system is involved `[user-supplied]`.
- **Procedures (described at a recognition level).** General activities and scale `[user-supplied]` — not step-by-step hazardous methods.

**Optional inputs:**
- Animal involvement (drives ABSL and cross-reference to the IACUC prompt).
- Known route-of-exposure or hazard-class information `[user-supplied]`.
- Institutional biosafety policy specifics `[user-supplied]`.
- Whether recombinant/synthetic nucleic acids are in scope (NIH Guidelines).

**Constraints — Must:**
- Walk risk-group (RG1–RG4) determination logic and the corresponding BSL/ABSL containment level at a structural level: practices, PPE, primary/secondary barriers, waste/decontamination.
- Treat recombinant/synthetic-nucleic-acid work under the NIH Guidelines framework structurally and flag it for IBC review.
- Include a dual-use (DURC) screen pointer that routes to `science_dual_use_research_assessment.md` and the IBC.
- Treat "unsure / elevated risk" as escalate-and-route to the biosafety officer/IBC; use probability-weighted reasoning to express residual uncertainty rather than asserting a single answer.
- Route the containment determination to the biosafety officer/IBC and mark institutional specifics `[user-supplied]`.

**Constraints — Must Not:**
- Do not invent vendor names, catalog/lot numbers, reagent specs, hazard data, regulatory citations, or institutional policy text. If needed and not supplied, mark `[user-supplied]` and route formal approval to the IACUC / IRB / IBC / biosafety officer.
- Do not provide any operational method, parameter, or uplift for creating, enhancing, culturing-for-harm, or weaponizing a hazardous agent or toxin. If the request trends that way, stop and route to the biosafety officer/IBC.
- Do not issue a containment determination, approval, or compliance verdict — that is the biosafety officer's/IBC's role.
- Do not describe drafted text as "novel," "groundbreaking," "first-ever," or a "gold standard."

**Instructions:**

1. **Frame the work at a recognition level.** Capture discipline, study type, aim, and agent/material class generally — not as a hazardous method. If the framing itself requires hazardous detail to proceed, stop and route.
2. **Risk-group logic.** Walk RG1–RG4 determination factors (pathogenicity, transmissibility, host range, availability of prophylaxis/treatment) structurally; mark specific agent hazard data `[user-supplied]`/verify.
3. **Route of exposure and hazard class.** Identify general exposure routes (inhalation, ingestion, percutaneous, mucosal) at a recognition level to inform containment.
4. **BSL/ABSL containment determination.** Map the risk group to a BSL/ABSL level structurally: practices, PPE, primary barriers (e.g., biosafety cabinets — concept), and secondary barriers (facility) — without operational hazard detail.
5. **Waste, decontamination, and spill response.** Scaffold structural requirements; mark agent-specific decontamination parameters `[user-supplied]`.
6. **Recombinant/synthetic nucleic acids.** Flag NIH-Guidelines applicability and IBC review where relevant.
7. **Dual-use screen.** Run the DURC pointer; if any dual-use concern surfaces, route to `science_dual_use_research_assessment.md` and the IBC and do not proceed with analysis.
8. **Build the IBC scaffold and risk-assessment table.** Assemble the locked output, expressing residual uncertainty with probability-weighted language.
9. **Self-check and route.** Run the adversarial verification checklist; confirm no operational uplift was produced and that the determination is routed to the biosafety officer/IBC.

**Output format (locked):**

```
## Work Framing (Recognition Level)
- Discipline / study type / aim / agent class [user-supplied]:

## Risk-Group Determination Logic
- RG factors considered / provisional RG (with uncertainty) [user-supplied/verify]:

## Route of Exposure & Hazard Class
- General routes / hazard class (recognition level):

## BSL/ABSL Containment Determination (Structural)
- Practices / PPE / primary & secondary barriers:

## Waste, Decontamination & Spill Response
- Structural requirements [user-supplied agent-specific params]:

## Recombinant/Synthetic Nucleic Acids
- NIH Guidelines applicability / IBC flag:

## Dual-Use Screen
- DURC pointer result → route to science_dual_use_research_assessment.md + IBC:

## IBC Submission Scaffold & Routing
| Section | Content (structural) | [user-supplied] specifics | Route-to |
|---|---|---|---|
- Escalation statement (unsure/elevated → biosafety officer/IBC):
```

**Reporting-standard alignment:** Risk groups (RG1–RG4) and biosafety levels (BSL/ABSL 1–4); NIH Guidelines for Research Involving Recombinant or Synthetic Nucleic Acid Molecules; IBC review; dual-use research of concern (DURC) governance (pointer to `science_dual_use_research_assessment.md`).

**Verification checklist (before delivering):**
- [ ] Discipline and study type captured as first inputs.
- [ ] Risk-group logic walked structurally with uncertainty expressed, not a single asserted verdict.
- [ ] BSL/ABSL determination kept structural — no operational hazard methods produced.
- [ ] Recombinant/synthetic-nucleic-acid work flagged under NIH Guidelines and for IBC review.
- [ ] Dual-use screen pointer present and routed to the DURC prompt + IBC.
- [ ] "Unsure / elevated risk" handled as escalate-and-route to the biosafety officer/IBC.
- [ ] No invented hazard data, regulatory text, or institutional policy; specifics marked `[user-supplied]`.
- [ ] No banned promotional language; determination routed to the biosafety officer/IBC.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Operational uplift | A "thorough" answer that includes hazardous how-to detail | Keep containment/governance-level only; stop and route if detail is needed |
| Determination issued | Draft states a final BSL/RG "approved" verdict | Route the determination to the biosafety officer/IBC; express uncertainty |
| Missed dual-use | Work passes risk-group logic but raises DURC concern | Always run the DURC pointer; route concerns to the dual-use prompt + IBC |
| Fabricated hazard data | Plausible pathogenicity/decon parameters filling gaps | Mark agent-specific data `[user-supplied]`/verify; never invent it |
