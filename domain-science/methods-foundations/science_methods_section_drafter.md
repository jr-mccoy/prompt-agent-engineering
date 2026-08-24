---
title: "Methods Section Drafter (IMRaD)"
category: science/methods-foundations
description: "Drafts an IMRaD Methods section skeleton-first, binds it to the correct reporting checklist for the study design, and fills only from user-supplied facts with every gap flagged."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - CM-02
  - QA-01
  - DS-02
difficulty: advanced
tags:
  - imrad
  - methods-section
  - reporting-standards
  - consort
  - strobe
  - prisma
  - arrive
  - scientific-writing
updated: "2026-06-26"
related_prompts:
  - domain-science/methods-foundations/science_experimental_design_advisor.md
  - domain-science/methods-foundations/science_replicability_premortem.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
---

# Methods Section Drafter (IMRaD)

**Objective:** Produce a publication-ready IMRaD Methods section that a reviewer could not fault for missing reporting items and that another lab could follow to repeat the study. The prompt builds the subsection skeleton first, binds it to the reporting checklist required by the study design, then fills the prose strictly from user-supplied facts — flagging every required number, citation, or specification that has not been supplied rather than inventing it.

**When to use:** When drafting or revising the Methods section of a manuscript, or when a journal has returned a reporting-checklist requirement (e.g., a CONSORT/STROBE/PRISMA submission flowchart) and the Methods must be brought into alignment.

**Required inputs:**
- **Discipline.** <field> `[user-supplied]`
- **Study type.** <randomized trial / observational cohort or case-control / systematic review or meta-analysis / animal study / diagnostic-accuracy / prediction-model / qualitative / computational> `[user-supplied]`
- **Reporting checklist that applies.** If known, name it; if not, the prompt selects it from the study type (see mapping below). `[user-supplied]`
- **Core method facts.** Sample/participants, materials/instruments, design, procedure, measures, and analysis plan — as far as they exist. `[user-supplied]`

**Optional inputs:**
- Pre-registration / protocol ID `[user-supplied]`.
- Ethics approval body and protocol number `[user-supplied]`.
- Power/sample-size justification and its assumptions.
- Software, package names, and versions for the analysis.
- Data/code availability details (link to `science_reproducibility_self_audit.md` output).

**Constraints — Must:**
- Emit the **subsection skeleton first** (headers only), then fill — never fill before the structure is agreed (ST-03).
- Select and name the reporting checklist by design, then emit **only the checklist items relevant to that design**, each mapped to a Methods subsection (CM-02).
- Mark every place a number, citation, instrument/vendor spec, or version is required but not supplied as `[user-supplied]` and list these as open items.
- Distinguish **pre-specified** (protocol/pre-registered) analyses from **exploratory/post-hoc** analyses in the Analysis subsection.
- Include a **Reproducibility/transparency statement** subsection (data, code, environment, materials availability), consistent with the FAIR self-audit.
- Use calibrated language only.

**Constraints — Must Not:**
- Do not invent citations, DOIs, dataset names, repository URLs, or instrument/vendor specs. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not write Results, Discussion, or interpretive claims into Methods.
- Do not assert ethics approval, consent, randomization, or blinding unless supplied — flag as `[user-supplied]`.
- Do not use promotional language: ban "novel," "groundbreaking," "first-ever," "gold standard," "state-of-the-art."

**Reporting-checklist mapping (select by study type):**
- Randomized controlled trial → **CONSORT** (+ **SPIRIT** for the protocol).
- Observational (cohort / case-control / cross-sectional) → **STROBE**.
- Systematic review / meta-analysis → **PRISMA**.
- Animal (in vivo) research → **ARRIVE 2.0**.
- Diagnostic-accuracy study → **STARD**.
- Prediction-model development/validation → **TRIPOD**.
- Qualitative research → **COREQ** or **SRQR**.

**Instructions:**

1. **Confirm design and checklist.** From the study type, state which reporting checklist governs; if ambiguous, ask before drafting. List the checklist's Methods-relevant items.
2. **Emit the subsection skeleton.** Produce design-appropriate headers — typically: Participants/Materials; Design; Procedure; Measures/Outcomes; Sample-size/Power; Statistical (or Computational) Analysis; Ethics & Consent; Reproducibility/Transparency. Add or drop subsections to fit the design.
3. **Map checklist items to subsections.** Build a crosswalk table: each relevant checklist item → the subsection that must report it → supplied / `[user-supplied]`.
4. **Fill from facts only.** Draft each subsection using supplied facts; where a checklist item needs a value not supplied, insert `[user-supplied]` inline and log it.
5. **Specify the analysis precisely.** State the model, estimands, covariates, handling of missing data, multiplicity correction, and software/versions (DS-02). Separate pre-specified from exploratory analyses.
6. **Write the ethics subsection.** Report approval body, protocol number, consent procedure, and any data-protection measures — each as fact or `[user-supplied]`.
7. **Write the reproducibility/transparency statement.** State data, code, materials, and environment availability and identifiers, drawing from the reproducibility self-audit.
8. **Self-check against the checklist.** Verify every relevant checklist item is either reported or flagged; list residual open items.

**Output format (locked):**

```
## Governing Reporting Checklist
- Study type → checklist: 
- Methods-relevant checklist items: [enumerated]

## Methods Skeleton (headers)
[list of subsection headers for this design]

## Checklist → Subsection Crosswalk
| Checklist item | Subsection | Supplied? |
|---|---|---|

## Drafted Methods
### [Participants / Materials]
[prose with inline [user-supplied] flags]
### [Design]
### [Procedure]
### [Measures / Outcomes]
### [Sample Size / Power]
### [Statistical / Computational Analysis]
(pre-specified vs exploratory clearly separated)
### [Ethics & Consent]
### [Reproducibility / Transparency Statement]

## Open Items ([user-supplied])
- [list every flagged gap, by subsection]
```

**Reporting-standard alignment:** IMRaD structure for the Methods section, bound to the design-appropriate EQUATOR-network checklist — CONSORT, SPIRIT, STROBE, PRISMA, ARRIVE 2.0, STARD, TRIPOD, COREQ, or SRQR (selected per the mapping above). The transparency subsection aligns with the TOP Guidelines and FAIR principles via `science_reproducibility_self_audit.md`.

**Verification checklist (before delivering):**
- [ ] Study type stated and the correct reporting checklist named.
- [ ] Skeleton emitted before prose; subsections fit the design.
- [ ] Only checklist items relevant to this design emitted, each mapped to a subsection.
- [ ] Every required-but-missing value flagged `[user-supplied]` inline and in Open Items.
- [ ] Pre-specified vs exploratory analyses separated.
- [ ] Ethics/consent reported or flagged, never assumed.
- [ ] Reproducibility/transparency statement present.
- [ ] No fabricated citations/specs/versions; no promotional language.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Plausible-but-invented specs | Filling in a vendor, catalog number, or software version that "sounds right" | Any unsupplied spec must be `[user-supplied]`; never auto-fill |
| Wrong checklist | Drafting a CONSORT-shaped Methods for an observational study | Re-confirm study type → checklist mapping in step 1 before drafting |
| Checklist over-emit | Listing every item of a 27-item checklist including Results-section items | Emit only Methods-relevant items per the crosswalk |
| Smuggled results | Reporting outcomes or effect estimates inside Methods | Strip any value/finding; Methods describes procedure, not results |
| Assumed ethics | Writing "approved by the IRB" without a supplied protocol number | Flag approval body and number as `[user-supplied]` |
| Exploratory passed as confirmatory | Describing post-hoc analyses in the pre-specified plan | Force the pre-specified/exploratory split in the Analysis subsection |
