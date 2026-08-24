---
title: "Omics Study Metadata Planner"
category: science/disciplines/biology
description: "Plan FAIR-compliant metadata for an omics study up front so samples and processing are discoverable, reproducible, and depositable without retrospective archaeology"
techniques:
  - ST-01
  - ST-03
  - CM-02
  - DS-02
  - QA-02
difficulty: intermediate
tags:
  - omics
  - metadata
  - fair
  - miame
  - minseqe
  - mixs
  - data-management-plan
updated: "2026-05-19"
related_prompts:
  - domain-science/disciplines/biology/bio_genomics_study_design.md
  - domain-science/methods-foundations/science_experimental_design_advisor.md
---

# Omics Study Metadata Planner

**Objective:** Produce a complete, FAIR-aligned metadata plan for an omics study (genomics, transcriptomics, proteomics, metabolomics, microbiome, epigenomics, multi-omics) before sample collection begins, so the sample, processing, batch, and analysis metadata required at deposition are captured at the source rather than reconstructed from email later.

**When to use:** As soon as a study is funded or scoped, well before sample collection. Use again at any point you realize your sample sheet is fragile or your batch covariates are missing. If samples have already been collected, the prompt still works as a triage tool — see Step 9.

**Required inputs:**
- **Assay family** (RNA-seq, scRNA-seq, ATAC-seq, ChIP-seq, WGS / WES, bisulfite, ribo-seq, proteomics LC-MS/MS, untargeted metabolomics, 16S, metagenomics, multi-omics combination).
- **Organism, tissue / cell type, condition.**
- **Sample origin.** Newly collected, biobank, clinical, public-data integration.
- **Target deposit archive.** GEO / ArrayExpress / SRA / ENA / dbGaP / EGA / MetaboLights / Metabolomics Workbench / PRIDE / iProX / MG-RAST / MGnify — user states the destination(s).
- **Open vs. controlled access.** Affects what metadata must be captured for the data-use agreement.

**Optional inputs:**
- Whether the study is human-subjects (changes required PII handling).
- Whether samples are longitudinal or cross-sectional.
- LIMS / ELN already in place.
- Whether a Data Management Plan (DMP) is required by the funder.

**Constraints — Must:**
- Align to the assay's community metadata standard: MIAME / MINSEQE for transcriptomics, MIATA for adaptive immunity, MIRAGE for glycomics, MIxS family for environmental / microbiome, MIAPE for proteomics, MSI for metabolomics. Name the standard explicitly.
- Distinguish four metadata layers and require fields at each layer: (1) *biological* — what the sample is; (2) *processing* — what was done to it; (3) *batch* — when / where / by whom / with what; (4) *analytic* — software versions, references, pipelines.
- Use controlled vocabularies and ontology IDs where they exist (Cell Ontology, Uberon, NCBI Taxonomy, EFO, MONDO, ChEBI, EDAM, OBI). Forbid free-text where a CV exists.
- Capture batch covariates **at sample registration**, not retrospectively. Every batch axis present in `bio_genomics_study_design.md` must have a metadata field.
- Treat the sample sheet as a versioned artifact with provenance: who edited what, when, why.
- Bake in PII handling for human studies: what is captured, what is hashed, what is never captured, who has access.

**Constraints — Must Not:**
- Do not invent ontology term IDs. If a candidate CV term is unclear, mark `[ontology lookup required]`.
- Do not propose free-text fields where a CV exists.
- Do not produce a metadata schema that drops fields required by the target archive.
- Do not write a metadata field that includes any PII directly identifiable per HIPAA Safe Harbor or GDPR for human studies — those go in a separate restricted file.
- Do not omit batch axes the design depends on (extraction day, library prep day, sequencing run, instrument, etc.).

**Instructions:**

1. **List target archives and pull their required field set.** For each destination archive, output a header row and a field list. If the user has not named an archive, ask. If multiple archives are needed (e.g., dbGaP + GEO for human transcriptomics), merge into a superset and note which fields are required where.

2. **Map the four metadata layers.** Build a table with the four columns (biological / processing / batch / analytic). Populate each column with the minimum field set required for the target archive(s) plus the additional fields the analysis will need (e.g., known biological covariates: age, sex, BMI, drug treatment, cell-cycle stage).

3. **Pick ontology / CV for each field.** For every controlled-vocabulary field, name the ontology, the example CV term format, and the lookup URL pattern (`http://purl.obolibrary.org/obo/...`-style). Where an ontology term must be looked up by the user, mark `[ontology lookup required]`.

4. **Specify the sample-ID schema.** Use a stable, opaque, human-readable ID that does not leak biology (no `case_01`, no patient initials). Encode the project, batch, replicate cleanly. State the regex it should match. Specify the link between this ID and any external identifiers (subject ID, biobank ID) and where the linkage table lives.

5. **Specify the sample-sheet artifact.** What columns, what types, what allowed values, what units. Use a schema language (JSON Schema, Frictionless Data Package, ISA-Tab) and produce a stub. State that the sheet is committed to a versioned location (git, LIMS export) and that all edits trace to an author / timestamp / reason.

6. **Specify processing-step capture.** For each protocol step (extraction → library prep → sequencing → primary analysis), specify what is recorded: protocol name + version, reagent lot, operator, instrument ID, run date, kit catalog number (user-supplied), Cq / fragment-size QC numbers.

7. **Specify PII / privacy handling (if human).** What goes in the metadata table, what goes in a restricted linkage table, what hash is used, who holds keys, how re-identification risk is assessed, how the metadata posture matches the consent posture and the target archive's access tier.

8. **Specify provenance and versioning of the metadata itself.** Sample sheet under version control (git or LIMS export); changes logged with author, date, reason; immutable snapshot at the point of deposition.

9. **Triage path (if samples already collected).** If sample collection has already happened: build a gap analysis between fields actually captured and fields the target archive requires; identify which gaps can be filled from external records (LIMS, calendar, instrument logs) and which are unrecoverable; flag the unrecoverable gaps to the user and the consequence (e.g., GEO deposit may be rejected, batch effects irreducible).

10. **Deliver the schema stub.** Output a usable starter schema (JSON Schema or ISA-Tab) the user can drop into a sample-sheet template. Do not invent field values, only the schema.

**Output format (locked):**

```
## Target archive(s)
| Archive | Required fields (named) | Access tier |

## Four-layer metadata table
| Layer | Field | CV / ontology | Units | Required? | Source of value |
| Biological | ... | ... | ... | yes | sample registration |
| Processing | ... | ... | ... | yes | bench worksheet |
| Batch | ... | ... | ... | yes | LIMS / instrument log |
| Analytic | ... | ... | ... | yes | pipeline metadata |

## Sample-ID schema
- Regex:
- Components:
- Linkage table location (restricted):

## Sample-sheet artifact spec
[schema language; field types and allowed values]

## Processing-step capture spec
| Step | Recorded fields |

## PII / privacy spec (if human)
- Captured in metadata:
- Captured in restricted linkage table:
- Hash / key custody:
- Consent ↔ access-tier match:

## Versioning and provenance
- Storage:
- Edit-log policy:
- Snapshot-at-deposit policy:

## Triage (if samples already collected)
| Required field | Currently captured? | Recoverable from? | Risk |

## Schema stub
[ISA-Tab / JSON Schema starter, locked]

## Open questions for the user
[gaps marked [ontology lookup required] or [user-supplied]]
```

**Reporting-standard alignment:** MIAME / MINSEQE / MIATA / MIxS / MIAPE / MSI per assay; FAIR principles (Wilkinson et al. 2016); CARE principles (if Indigenous data); applicable ontologies via OBO Foundry / EBI Ontology Lookup Service; archive-specific submission templates.

**Verification checklist:**
- [ ] Community metadata standard for the assay named.
- [ ] All four layers (biological / processing / batch / analytic) populated.
- [ ] Every batch axis from the study design has a metadata field.
- [ ] Sample-ID schema is opaque and does not leak biology.
- [ ] Every CV field maps to a named ontology or is marked `[ontology lookup required]`.
- [ ] PII handling matches consent and archive access tier (human studies).
- [ ] Schema stub is syntactically valid in the chosen format.
- [ ] No invented ontology term IDs or catalog numbers.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Retrospective metadata reconstruction | Fields filled from memory at deposit time | Capture at sample registration; immutable log |
| Free-text drift | "tissue" filled as `liver`, `Liver`, `hepatic`, `LIVER` | CV constraint per field |
| Missing batch covariate | Run date not captured; batch effects unmodelable | Every design batch axis has a field |
| Biology-leaking sample ID | `Case_Diseased_03` reveals condition | Opaque ID regex |
| Archive rejection at deposit | Required field absent | Archive field list pulled at planning, not at deposit |
| PII leakage in open archive | DOB / ZIP in metadata uploaded to public archive | Two-table separation + access-tier match |
| Invented ontology term | Plausible-looking term ID that doesn't exist | Lookup-required marker; no invention |
| Schema rot | Sample sheet edited by hand without log | Versioned storage; edit-log policy stated |
