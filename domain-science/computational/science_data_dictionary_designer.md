---
title: "Variable-Level Data Dictionary Designer"
category: science/computational
description: "Build a tidy-data-compliant variable-level dictionary with units, allowed values, missingness codes, valid ranges, provenance, and sensitivity flags from user-supplied variable definitions."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-01
  - CM-02
  - DS-02
updated: "2026-06-26"
related_prompts:
  - domain-science/computational/science_metadata_schema_builder.md
  - domain-science/computational/science_data_management_plan_drafter.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
---

# Variable-Level Data Dictionary Designer

**Objective:** Structure a complete, machine-readable data dictionary (codebook) at the variable level — one row per variable — capturing name, label, type, unit, allowed values, valid range, missing-value codes and their meanings, derivation/provenance, source instrument, and a PII/sensitivity flag. The dictionary enforces tidy-data discipline and consistent missingness conventions so that the dataset is interpretable, shareable, and reproducible. The prompt structures what the user supplies; it does not invent variable meanings.

**When to use:** You have a dataset (or a planned dataset schema) and need an authoritative codebook before deposit, analysis, or handoff — or you are documenting an existing messy dataset for FAIR sharing.

**Required inputs:**
- **Discipline.** Field of study.
- **Study type.** Observational / experimental / computational / survey / secondary reuse.
- **Variable list.** The variables to document, with whatever definitions, units, and value labels the user already has (incomplete is fine — gaps become `[user-supplied]`).
- **Unit of observation.** What one row in the dataset represents (e.g., patient-visit, sample, site-year).

**Optional inputs:**
- Existing raw data sample or column headers.
- Instrument/protocol names producing each variable.
- Known missingness conventions already in use.
- Controlled vocabularies the project must align to.
- Target repository's required codebook format (e.g., DDI, CDISC define.xml).

**Constraints — Must:**
- Produce a dictionary as a TABLE with exactly one row per variable.
- For every variable, capture: name, label, type, unit, allowed values / value labels, valid range, missingness codes + meanings, derivation/provenance, source instrument, sensitivity flag.
- Enforce tidy-data principles: one variable per column, one observation per row, one value per cell; flag any supplied variable that violates this (e.g., multiple measures packed into one field).
- Use a single, consistent set of missing-value codes across the dictionary and document each code's meaning (e.g., distinguishing "not applicable", "not measured", "declined", "unknown").
- Name the codebook standard explicitly where one is targeted (DDI for social science, CDISC for clinical, or a generic tidy-data codebook otherwise).
- Mark categorical variables with their full level set and human-readable value labels.
- Flag any variable that is direct or indirect PII / sensitive, and route those toward the controlled-access branch documented in the DMP.

**Constraints — Must Not:**
- Do not invent citations, DOIs, funder policy text, repository names, or accession numbers. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not invent variable meanings, units, allowed values, or derivations — all definitional content is `[user-supplied]`; the prompt only structures and checks it.
- Do not silently merge distinct missingness reasons into one code.
- Do not use promotional language ("novel", "groundbreaking", "first-ever", "gold standard") in the dictionary.
- Do not assume a variable is non-sensitive by default; require an explicit basis before clearing the sensitivity flag.

**Instructions:**

1. **Confirm scope.** Restate discipline, study type, unit of observation, and the variable list. State the codebook standard being targeted (or generic tidy-data codebook).
2. **Normalize the unit of observation.** Confirm one row represents one observation. Flag variables that imply a different grain (these may need a separate table / long format).
3. **Draft the codebook header.** Capture dataset title, version, unit of observation, row/column counts (mark `[user-supplied]` if unknown), the missing-value code legend, and the responsible curator (ORCID `[user-supplied]`).
4. **Classify each variable's type.** Assign type (integer, float, categorical-nominal, categorical-ordinal, boolean, date/time, free-text, identifier) and unit. Mark unknown types/units `[user-supplied]`.
5. **Specify allowed values & ranges.** For categoricals, list the full level set with value labels; for continuous variables, give the valid range. Where the user did not supply these, mark `[user-supplied]` rather than guessing.
6. **Standardize missingness.** Apply the consistent missing-value legend to every variable; ensure distinct reasons (NA, not measured, declined, unknown) map to distinct codes.
7. **Record provenance.** For each variable, note whether it is raw or derived; for derived variables, capture the derivation rule and source variables (mark `[user-supplied]` if the rule is not provided).
8. **Flag sensitivity.** Mark each variable as Not-sensitive / Indirect-identifier / Direct-PII / Special-category, with a one-line basis. Route flagged variables to controlled handling.
9. **Run tidy-data and consistency checks.** Surface violations (packed fields, inconsistent units, duplicate names, level sets that overlap, undocumented codes) as an issues list.

**Output format (locked):**

```
## Codebook header
Dataset: [user-supplied] | Version: [...] | Unit of observation: [...]
Rows × Columns: [user-supplied] | Curator (ORCID): [user-supplied]
Codebook standard: [DDI | CDISC | generic tidy-data codebook]
Missing-value legend: [e.g., .a=not applicable | .m=not measured | .d=declined | .u=unknown]

## Data dictionary (one row per variable)
| Variable | Label | Type | Unit | Allowed values / value labels | Valid range | Missing codes | Provenance (raw/derived + rule) | Source instrument | Sensitivity |
|---|---|---|---|---|---|---|---|---|---|
| [...] | [...] | [...] | [...] | [...] / [user-supplied] | [...] | [...] | [...] | [...] | [Not-sensitive/Indirect/Direct-PII/Special] |

## Tidy-data & consistency issues
- [ ] [issue + affected variable]

## Open items requiring user input
- [ ] [user-supplied] ...
```

**Reporting-standard alignment:** Tidy-data principles; DDI (social science) or CDISC define.xml (clinical) where targeted; FAIR principles (the dictionary supports Interoperability and Reusability). Provenance fields are PROV-O-compatible at the concept level.

**Verification checklist (before delivering):**
- [ ] Discipline, study type, and unit of observation are stated.
- [ ] Exactly one row per variable; no packed/multi-value fields left unflagged.
- [ ] Every variable has type, unit, allowed values/range, and missingness codes (or `[user-supplied]`).
- [ ] A single consistent missing-value legend is applied throughout.
- [ ] Distinct missingness reasons map to distinct codes.
- [ ] No variable meaning, unit, or value label is invented; gaps are `[user-supplied]`.
- [ ] Every variable carries a sensitivity flag with a basis.
- [ ] The codebook standard is named; no promotional language appears.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Invented value labels | Plausible category labels filled in for an unlabeled categorical | Mark allowed values `[user-supplied]`; never infer levels not provided |
| Missingness collapse | One "missing" code hides distinct reasons (declined vs not measured) | Require distinct codes per reason; document each in the legend |
| Packed field passes | A column like `bp="120/80"` is treated as one tidy variable | Flag as a tidy-data violation; recommend splitting into separate columns |
| Sensitivity blind spot | An indirect identifier (zip, rare diagnosis) marked Not-sensitive | Default to flagging; require explicit basis to clear; consider linkage risk |
| Derived-as-raw | A computed variable documented with no derivation rule | Require provenance = derived + rule, or mark rule `[user-supplied]` |
