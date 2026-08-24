---
title: "Cell Culture Protocol Designer"
category: science/bench-and-wetlab
description: "Design a line-specific cell culture protocol with STR authentication, mycoplasma testing, passage tracking, cryopreservation, and a QC-cadence log aligned to NIH rigor guidance."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-01
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - cell-culture
  - str-authentication
  - mycoplasma-testing
  - reproducibility
  - passage-tracking
  - cryopreservation
  - quality-control
  - nih-rigor
updated: "2026-06-26"
related_prompts:
  - domain-science/bench-and-wetlab/science_biosafety_risk_assessment.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
  - domain-science/ethics-integrity/science_open_science_practices_self_audit.md
---

# Cell Culture Protocol Designer

**Objective:** Produce a line-specific cell culture protocol that treats authentication and mycoplasma testing as reproducibility-critical controls, not optional extras. The protocol covers media and passaging conditions, passage-number tracking and drift, cryopreservation/thaw, contamination prevention, and a QC-cadence log so the line's identity and health are documented from receipt to retirement.

**When to use:** Before establishing, banking, or publishing work with a continuous or primary cell line — especially when results must be reproducible and the line's provenance, authentication, and mycoplasma status are not yet documented.

**Required inputs:**
- **Discipline.** Field and biological context (e.g., cancer biology, immunology, stem-cell work).
- **Study type.** Observational / experimental — and whether the line is the model system or a tool.
- **Cell line / source.** Designation, supplier or originating lab, and any provided authentication or passage history `[user-supplied]`.
- **Culture conditions known so far.** Adherent vs. suspension, recommended media/supplements, incubator settings `[user-supplied]`.

**Optional inputs:**
- Intended downstream assays (drift sensitivity differs by readout).
- Existing STR profile or mycoplasma certificate `[user-supplied]`.
- Biosafety/risk-group context (route containment questions to the biosafety prompt).
- Banking strategy (master/working cell bank tiers).

**Constraints — Must:**
- Require STR profiling (or species-appropriate authentication) for human and other STR-amenable lines, and require checking the designation against misidentified/cross-contaminated cell-line registers (ICLAC register — concept; specifics `[user-supplied]`).
- Specify a mycoplasma-testing method and cadence (e.g., on receipt, before banking, periodically in culture, before key experiments) consistent with NIH rigor and reproducibility expectations.
- Track passage number from a defined P0 and flag senescence/drift windows; tie passage limits to the line, not a generic default.
- Include cryopreservation and thaw conditions and a master/working bank structure so early, authenticated stocks are preserved.
- Output a QC-cadence table covering authentication, mycoplasma, morphology, and contamination checks.

**Constraints — Must Not:**
- Do not invent vendor names, catalog/lot numbers, reagent specs, hazard data, regulatory citations, or institutional policy text. If needed and not supplied, mark `[user-supplied]` and route formal approval to the IACUC / IRB / IBC / biosafety officer.
- Do not invent media formulations, supplement concentrations, or authentication results; unknowns are `[user-supplied]` and authentication results come from an actual assay.
- Do not describe drafted protocol steps as "novel," "groundbreaking," "first-ever," or a "gold standard."
- Do not treat an unauthenticated or untested line as fit for publication-grade work.

**Instructions:**

1. **Anchor the line and provenance.** Record discipline, study type, line designation, source, and supplied passage/authentication history. Note explicitly what is `[user-supplied]` vs. unknown.
2. **Plan authentication.** Specify STR profiling (or species-appropriate method) and the requirement to cross-check the designation against misidentified-line registers; define when authentication is repeated (on receipt, before banking, periodically).
3. **Plan mycoplasma testing.** Choose method(s) and set a cadence; mark contaminated-line handling as quarantine-and-route, not continued use.
4. **Specify media and passaging.** Define media, supplements, feeding schedule, confluence triggers, and passaging method using `[user-supplied]` values where not known — never invented formulations.
5. **Define passage tracking and drift limits.** Set P0, maximum passage window, and senescence/morphological-drift watch points tied to the line and downstream assay sensitivity.
6. **Specify cryopreservation and thaw.** Define banking tiers (master/working), freeze medium structure, controlled-rate freezing concept, storage, and thaw/recovery checks `[user-supplied]` for line-specific details.
7. **Specify contamination prevention.** Aseptic practice, antibiotic-use caution (does not mask mycoplasma), incubator hygiene, and segregation of unauthenticated/untested lines.
8. **Build the QC-cadence log.** Assemble the locked QC table with checkpoints, methods, frequency, pass criteria, and escalation path.
9. **Self-check and Open Science branch.** Run the verification checklist; where compatible, recommend depositing the protocol (e.g., protocols.io) and sharing the authenticated STR profile and mycoplasma status with the line.

**Output format (locked):**

```
## Line & Provenance
- Designation / source / study context:
- Supplied vs. unknown ([user-supplied] flags):

## Authentication Plan
- Method (STR / species-appropriate):
- Register cross-check (misidentified-line registers — concept):
- Repeat cadence:

## Mycoplasma Testing Plan
- Method(s):
- Cadence and contaminated-line handling (quarantine + route):

## Media & Passaging
- Media / supplements / feeding [user-supplied where unknown]:
- Confluence triggers / passaging method:

## Passage Tracking & Drift
- P0 definition / max passage window:
- Senescence / drift watch points:

## Cryopreservation & Thaw
- Banking tiers (master / working):
- Freeze medium structure / storage / thaw checks [user-supplied]:

## Contamination Prevention
- Aseptic practice / segregation / antibiotic caution:

## QC-Cadence Log
| Checkpoint | Method | Frequency | Pass criteria | Escalation |
|---|---|---|---|---|

## Open Science / Reproducibility
- Protocol deposit / STR & mycoplasma sharing:
```

**Reporting-standard alignment:** NIH rigor and reproducibility guidance on cell-line authentication and mycoplasma testing; STR profiling for authentication; misidentified/cross-contaminated cell-line registers (ICLAC — concept).

**Verification checklist (before delivering):**
- [ ] Discipline and study type captured as first inputs.
- [ ] Authentication method specified and a register cross-check required.
- [ ] Mycoplasma method and cadence specified, with quarantine-and-route handling.
- [ ] Passage tracking from a defined P0 with drift/senescence limits.
- [ ] Cryopreservation/thaw and master/working bank structure included.
- [ ] No invented media formulations, catalog numbers, or authentication results; unknowns marked `[user-supplied]`.
- [ ] QC-cadence table present and complete.
- [ ] No banned promotional language in drafted text; Open Science branch offered where compatible.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Misidentified line | A named, "well-known" line treated as authentic without STR data | Require STR profiling + register cross-check before publication-grade use |
| Hidden mycoplasma | Healthy-looking, fast-growing culture assumed clean | Schedule mycoplasma testing; caution that antibiotics can mask it |
| Passage drift | Late-passage cells assumed equivalent to early stock | Track from P0, set max-passage window, work from authenticated banks |
| Fabricated specs | Plausible media/catalog numbers filling gaps | Mark unknowns `[user-supplied]`; never invent formulations |
