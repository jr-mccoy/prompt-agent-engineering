---
title: "Funder-Aware Data Management Plan Drafter"
category: science/computational
description: "Draft a funder-aligned Data Management & Sharing Plan covering data types, standards, storage, security, preservation, sharing mechanism, and roles, mapped to the applicable funder template."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-01
  - CM-02
  - DS-02
updated: "2026-06-26"
related_prompts:
  - domain-science/computational/science_data_dictionary_designer.md
  - domain-science/computational/science_metadata_schema_builder.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
---

# Funder-Aware Data Management Plan Drafter

**Objective:** Produce a section-by-section Data Management & Sharing Plan (DMP/DMSP) skeleton aligned to a specific funder's template structure, covering the full data lifecycle: types and volume, standards and formats, metadata, in-project storage and backup, security, preservation and retention, the sharing mechanism (repository, access tier, license, timeline), and roles, responsibilities, and cost. The plan defaults to FAIR open deposit and routes human or sensitive data to a justified controlled-access exception.

**When to use:** You are preparing a grant proposal or a post-award compliance update and need a DMP scaffold structured for the funder reviewing it, before you write final prose.

**Required inputs:**
- **Discipline.** Field of study (e.g., genomics, social science, climate modeling).
- **Study type.** Observational / experimental / computational / secondary data reuse / mixed.
- **Funder.** Which funder applies (e.g., NIH, NSF, Wellcome, ERC, other) — determines the template structure. If unknown, mark `[user-supplied]`.
- **Data types & estimated volume.** What data are generated/collected and rough size.
- **Human or sensitive data?** Yes/no, and if yes, what category (identifiable human subjects, Indigenous data, location-sensitive species, export-controlled, commercially confidential).

**Optional inputs:**
- Target repository or repository shortlist.
- Existing institutional storage/backup infrastructure.
- Budget ceiling for data management costs.
- Consent language or governance constraints already in place.
- Whether a machine-actionable DMP (maDMP) output is required by the funder/institution.

**Constraints — Must:**
- Map the plan to the named funder's template *structure* (section headings and ordering) and state which funder structure is being used.
- Cover all standard lifecycle sections: (1) data types & volume, (2) standards/formats, (3) metadata & documentation, (4) storage & backup during the project, (5) security/access control, (6) preservation & retention period, (7) sharing mechanism (repository + access tier + license + timeline), (8) roles/responsibilities, (9) cost.
- Default to a FAIR open deposit branch: deposit in a TRUST-aligned repository, assign a persistent identifier (DOI), apply an open license (e.g., CC0/CC-BY for data; mark exact choice `[user-supplied]`).
- Name the standards invoked explicitly: FAIR principles, TRUST repository principles, and CARE principles where Indigenous data are involved.
- For human/sensitive data, present controlled or restricted access as the explicit non-default exception, with a stated justification, governance route, and access-request process.
- Recommend domain-appropriate metadata and file-format standards by name where they exist; otherwise mark `[user-supplied]`.
- Distinguish pre-specified commitments (what you will do) from exploratory/contingent items (what depends on as-yet-unknown data).

**Constraints — Must Not:**
- Do not invent citations, DOIs, funder policy text, repository names, or accession numbers. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not quote specific funder policy clauses, thresholds, or deadlines from memory — reference the section's intent and mark exact text `[user-supplied]`/verify against the current official policy.
- Do not assert that data are "fully anonymized" or "non-identifiable" without a stated basis; flag re-identification risk as a reviewer concern.
- Do not use promotional language ("novel", "groundbreaking", "first-ever", "gold standard") in drafted plan text.
- Do not present open sharing as compulsory where consent or law forbids it; route those to the controlled branch.

**Instructions:**

1. **Confirm scope.** Restate discipline, study type, funder, data types/volume, and whether human/sensitive data are present. If funder or sensitivity is unstated, mark `[user-supplied]` and proceed with the FAIR open default while flagging the gap.
2. **Select the template structure.** State which funder structure you are mapping to and list its section headings. If the funder is unknown, use a generic DMP Common Standard / RDA maDMP-compatible structure and say so.
3. **Inventory data.** Enumerate each dataset: type, source, estimated volume, generation method, and format. Recommend preservation-friendly, open formats where they exist (mark format names `[user-supplied]` if discipline-specific and unknown).
4. **Specify standards & metadata.** Name the metadata standard and any controlled vocabularies/ontologies for the discipline; cross-reference a metadata schema builder if deeper schema work is needed. Mark unknown standard names `[user-supplied]`.
5. **Plan storage, backup, and security.** Describe active-phase storage location, backup cadence (e.g., 3-2-1 pattern), access controls, and encryption. For sensitive data, escalate security controls and name the governance authority.
6. **Plan preservation & sharing.** Choose the repository (or repository criteria — TRUST-aligned, issues PIDs, domain-appropriate), the access tier (open / registered / controlled), the license, the retention period, and the sharing timeline relative to publication/award end. Default open; justify any deviation.
7. **Assign roles & cost.** Identify who is responsible for each lifecycle stage (PI, data steward, repository) using ORCID/ROR identifiers where available (mark `[user-supplied]`), and itemize anticipated data-management costs.
8. **Flag the sharing branch.** Explicitly label the plan as open-default or controlled-access-exception, and for the latter give the justification and the access-request mechanism.
9. **Note machine-actionability.** If a maDMP is required, indicate which fields map to the RDA maDMP / DMP Common Standard model and flag any fields the user must populate.

**Output format (locked):**

```
## DMP Skeleton — [Funder structure | generic DMP Common Standard]
Discipline: [...] | Study type: [...] | Sharing branch: [Open default | Controlled exception]
Standards invoked: FAIR; TRUST (repositories); CARE (if Indigenous data) | Policy specifics: [user-supplied]/verify

### 1. Data types & volume
[...]

### 2. Standards & formats
[...]

### 3. Metadata & documentation
[...]

### 4. Storage & backup (active phase)
[...]

### 5. Security & access control
[...]

### 6. Preservation & retention
[...]

### 7. Sharing mechanism
| Element | Plan | Default? | Justification if non-default |
|---|---|---|---|
| Repository | [...] / [user-supplied] | — | — |
| Access tier | [Open/Registered/Controlled] | Open | [...] |
| License | [...] / [user-supplied] | Open (CC0/CC-BY) | [...] |
| Timeline | [...] | At/Before publication | [...] |

### 8. Roles & responsibilities
[...]

### 9. Cost
[...]

### Open items requiring user input
- [ ] [user-supplied] ...
```

**Reporting-standard alignment:** FAIR principles; TRUST repository principles; CARE principles (Indigenous data governance); DMP Common Standard / RDA machine-actionable DMP model. Funder policy specifics (NIH DMS, NSF, Wellcome, ERC) referenced by structure only — exact text `[user-supplied]`/verify.

**Verification checklist (before delivering):**
- [ ] Discipline, study type, and funder are stated (or marked `[user-supplied]`).
- [ ] All nine lifecycle sections are present.
- [ ] The funder template structure is named, or generic structure is declared.
- [ ] No funder policy text, DOI, repository name, or accession is fabricated; gaps are `[user-supplied]`.
- [ ] Sharing branch is explicitly labeled open-default or controlled-exception with justification.
- [ ] FAIR, TRUST, and (where relevant) CARE are named explicitly.
- [ ] License and access tier are specified or marked `[user-supplied]`.
- [ ] No promotional language appears in drafted plan text.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Anonymization overclaim | Plan states data are "anonymized" so open sharing is fine | Require a stated de-identification basis; flag re-identification risk; default sensitive data to controlled branch |
| Fabricated policy text | Confident quotation of a funder's exact sharing deadline or threshold | Reference section intent only; mark exact clauses `[user-supplied]`/verify |
| Repository hallucination | A named repository "fits" but isn't real or isn't domain-appropriate | Use TRUST-aligned selection criteria; mark specific repository `[user-supplied]` unless given |
| Open-by-reflex | Forcing open deposit where consent/law forbids it | Route human/sensitive/CARE data to controlled exception with justification |
| Cost hand-waving | Cost section says "minimal" with no basis | Itemize storage, curation, and repository fees; mark figures `[user-supplied]` |
