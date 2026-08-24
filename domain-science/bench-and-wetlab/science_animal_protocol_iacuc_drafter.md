---
title: "Animal Protocol IACUC Drafter"
category: science/bench-and-wetlab
description: "Draft a section-by-section IACUC protocol scaffold aligned to ARRIVE 2.0 and the 3Rs, with non-animal-alternative search, sample-size justification, humane endpoints, and randomization/blinding — routing final approval to the IACUC."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-01
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - iacuc
  - arrive-2.0
  - 3rs
  - humane-endpoints
  - animal-welfare
  - sample-size-justification
  - randomization-blinding
  - prepare-guidelines
updated: "2026-06-26"
related_prompts:
  - domain-science/methods-foundations/science_power_and_sample_size_calculator.md
  - domain-science/bench-and-wetlab/science_human_subjects_irb_protocol_drafter.md
  - domain-science/methods-foundations/science_blinding_and_randomization_protocol.md
---

# Animal Protocol IACUC Drafter

**Objective:** Produce a section-by-section IACUC-submission scaffold that embeds ARRIVE 2.0 reporting structure, the PREPARE planning mindset, and the 3Rs (Replacement, Reduction, Refinement). It forces a non-animal-alternative search, a sample-size justification that minimizes animal numbers, explicit pain/distress categorization with anesthesia/analgesia and humane endpoints, and randomization/blinding. The protocol draft structures the submission; the IACUC makes the decision.

**When to use:** When preparing a new or amended animal-use protocol and you need a rigorous, welfare-first scaffold before institutional submission and review.

**Required inputs:**
- **Discipline.** Field and scientific area (e.g., neuroscience, immunology, toxicology).
- **Study type.** Observational / experimental — and the core hypothesis or aim.
- **Species/strain (proposed).** With any provided justification `[user-supplied]`.
- **Procedures (proposed).** Interventions, anticipated pain/distress, expected duration `[user-supplied]`.

**Optional inputs:**
- Prior power/effect-size estimates or pilot data (cross-reference the power prompt).
- Known non-animal alternatives considered `[user-supplied]`.
- Institutional veterinary/humane-endpoint policy specifics `[user-supplied]`.
- Anesthesia/analgesia regimen under consideration `[user-supplied]`.

**Constraints — Must:**
- Structure the protocol so every section maps to ARRIVE 2.0 reporting items and the 3Rs are addressed explicitly and separately.
- Require a documented non-animal-alternative (Replacement) literature/database search.
- Require a sample-size/statistical justification that minimizes animal numbers (Reduction); cross-reference `science_power_and_sample_size_calculator.md` for the calculation.
- Require a pain/distress category, anesthesia/analgesia plan, and pre-defined humane endpoints and euthanasia criteria (Refinement).
- Require randomization and blinding plans and species/strain justification.
- Route the final decision to the IACUC and mark institutional specifics `[user-supplied]`.

**Constraints — Must Not:**
- Do not invent vendor names, catalog/lot numbers, reagent specs, hazard data, regulatory citations, or institutional policy text. If needed and not supplied, mark `[user-supplied]` and route formal approval to the IACUC / IRB / IBC / biosafety officer.
- Do not assert that the protocol is approved, exempt, or compliant — that determination is the IACUC's.
- Do not describe drafted protocol text as "novel," "groundbreaking," "first-ever," or a "gold standard."
- Do not minimize anticipated pain/distress to ease approval, or omit humane endpoints.

**Instructions:**

1. **Frame the science.** Capture discipline, study type, aim/hypothesis, and why the question matters scientifically — without promotional language.
2. **Replacement search.** Draft the non-animal-alternative search section: databases/strategy concept, what was considered, and why animal use is necessary.
3. **Reduction / sample size.** Draft the statistical-justification section that minimizes numbers; cross-reference the power prompt and require effect-size and analysis assumptions to be `[user-supplied]` rather than invented.
4. **Species/strain justification.** Justify the proposed species and strain against the aim; note welfare and translational considerations.
5. **Procedures and pain/distress.** Describe procedures, assign a pain/distress category, and draft the anesthesia/analgesia plan `[user-supplied]` for regimen specifics.
6. **Refinement and humane endpoints.** Draft pre-defined humane endpoints, monitoring frequency, adverse-event response, and euthanasia criteria.
7. **Randomization and blinding.** Draft allocation, randomization, and blinding plans to reduce bias; cross-reference the blinding/randomization prompt.
8. **Personnel, housing, and welfare.** Scaffold personnel/training, housing/husbandry, and enrichment sections with `[user-supplied]` institutional specifics.
9. **Self-check and route.** Run the verification checklist, map sections to ARRIVE 2.0, and state plainly that the IACUC holds approval authority; where compatible, recommend protocol deposition/pre-registration.

**Output format (locked):**

```
## Scientific Justification & Aims
- Discipline / study type / aim:

## Replacement (Non-Animal Alternatives)
- Search strategy (concept) / alternatives considered / necessity:

## Reduction (Sample-Size Justification)
- Effect size & assumptions [user-supplied]:
- Sample size & minimization rationale (xref power prompt):

## Species / Strain Justification
- Choice and rationale:

## Procedures & Pain/Distress Category
- Procedures / category / anesthesia & analgesia [user-supplied]:

## Refinement & Humane Endpoints
- Endpoints / monitoring / adverse-event & euthanasia criteria:

## Randomization & Blinding
- Allocation / randomization / blinding plan:

## Personnel, Housing & Welfare
- Training / husbandry / enrichment [user-supplied]:

## ARRIVE 2.0 Mapping & Routing
- Section-to-item map / IACUC-approval statement:
```

**Reporting-standard alignment:** ARRIVE 2.0 reporting guidelines; PREPARE planning guidelines; the 3Rs (Replacement, Reduction, Refinement); IACUC review structure; humane endpoints.

**Verification checklist (before delivering):**
- [ ] Discipline and study type captured as first inputs.
- [ ] Replacement search section present with necessity rationale.
- [ ] Sample-size justification minimizes numbers and cross-references the power prompt.
- [ ] Species/strain justified against the aim.
- [ ] Pain/distress category, anesthesia/analgesia, and humane endpoints all present.
- [ ] Randomization and blinding plans included.
- [ ] No invented vendors, regulatory text, or institutional policy; specifics marked `[user-supplied]`.
- [ ] Final approval routed to the IACUC; no banned promotional language in drafted text.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Skipped Replacement | "No alternatives exist" asserted without a search | Require a documented alternative-search section |
| Underpowered or inflated N | A round number with no justification | Require effect-size-based justification; cross-reference power prompt |
| Welfare under-stated | Pain/distress downgraded to ease approval | Require honest category + pre-defined humane endpoints |
| Approval implied | Draft reads as "compliant/approved" | State the IACUC holds approval authority; mark specifics `[user-supplied]` |
