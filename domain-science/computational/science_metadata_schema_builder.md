---
title: "Discipline-Appropriate Metadata Schema Builder"
category: science/computational
description: "Select the right metadata standard for a discipline (MIBBI family, ISA model, Dublin Core, DataCite, schema.org/Bioschemas, DDI) and build a field list with cardinality, ontology bindings, and a crosswalk to the deposit repository's required fields."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - RT-03
  - QA-01
  - CM-02
updated: "2026-06-26"
related_prompts:
  - domain-science/computational/science_data_dictionary_designer.md
  - domain-science/computational/science_data_management_plan_drafter.md
  - domain-science/disciplines/biology/bio_omics_study_metadata_planner.md
---

# Discipline-Appropriate Metadata Schema Builder

**Objective:** Choose the metadata standard best suited to a discipline and deposit goal, then build a concrete field list — each field with cardinality, controlled-vocabulary/ontology binding, and obligation level — plus a crosswalk that maps the chosen schema's fields to the target repository's required fields. The result makes a dataset findable and interoperable (the F and I of FAIR) without fabricating ontology term identifiers.

**When to use:** You are preparing to deposit data and need a documented, repository-ready metadata schema, or you need to harmonize study metadata across assays or against a discovery layer.

**Required inputs:**
- **Discipline.** Field of study (e.g., transcriptomics, environmental microbiology, survey research, materials science).
- **Study type.** Single-assay / multi-assay / observational / survey / computational.
- **Deposit goal.** General archival deposit, domain-repository submission, and/or web discoverability.
- **Target repository (if known).** Determines required-field crosswalk; mark `[user-supplied]` if not chosen.

**Optional inputs:**
- Existing variable list or data dictionary.
- Whether multiple assay types share one study (favors the ISA model).
- Required minimum-information standard already mandated by a journal/funder.
- Preferred ontologies or controlled vocabularies.
- Whether machine-readable JSON-LD output is needed (favors schema.org/Bioschemas).

**Constraints — Must:**
- Recommend the schema by an explicit selection rationale, considering candidates and naming the chosen one: MIBBI-family minimum-information standard (e.g., MIAME, MINSEQE, MIxS, MIAPE) for life-science assays; the ISA model / ISA-Tab for multi-assay studies; Dublin Core or the DataCite metadata schema for general deposit and DOI minting; schema.org / Bioschemas for web discoverability; DDI for survey/social-science data.
- Build a field table where each field has: name, obligation (mandatory / recommended / optional), cardinality (0..1, 1, 0..n, 1..n), controlled vocabulary/ontology binding, and a short definition.
- Bind fields to controlled vocabularies/ontologies by name (e.g., OBO Foundry ontologies, MIxS environment packages) and mark specific term IDs `[user-supplied]`/verify.
- Provide a crosswalk table mapping chosen-schema fields → target repository required fields, flagging unmapped-but-required repository fields as gaps.
- Use persistent identifiers in the schema where applicable: DOI (datasets), ORCID (people), ROR (organizations).
- Default to an open, FAIR-aligned deposit (TRUST-aligned repository, open license); name controlled/restricted metadata handling as the non-default exception when records are sensitive.

**Constraints — Must Not:**
- Do not invent citations, DOIs, funder policy text, repository names, or accession numbers. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not invent ontology term identifiers, accession prefixes, or schema field names that do not exist in the named standard — mark `[user-supplied]`/verify.
- Do not assert a standard's exact required-field list from memory if uncertain; mark it `[user-supplied]`/verify against the current specification.
- Do not use promotional language ("novel", "groundbreaking", "first-ever", "gold standard") in the schema or rationale.
- Do not pick a single schema without stating why the alternatives were rejected.

**Instructions:**

1. **Confirm scope.** Restate discipline, study type, deposit goal, and target repository (or `[user-supplied]`).
2. **Enumerate candidate schemas (Tree of Thoughts).** List the plausible standards for this case (MIBBI member, ISA, Dublin Core, DataCite, schema.org/Bioschemas, DDI), and for each give a one-line fit/misfit note.
3. **Select and justify.** Choose the primary schema (and any secondary, e.g., DataCite for the DOI layer + a domain MIBBI standard for assay detail). State the rationale and what was rejected and why.
4. **Build the field list.** Populate the field table with obligation, cardinality, ontology binding, and definition. Mark fields whose exact names/requirements you cannot confirm `[user-supplied]`/verify.
5. **Bind vocabularies.** For controlled fields, name the ontology/vocabulary; leave specific term IDs as `[user-supplied]`/verify.
6. **Add persistent identifiers.** Ensure DOI/ORCID/ROR fields are present where applicable.
7. **Build the crosswalk.** Map each chosen-schema field to the target repository's required field; flag repository-required fields with no source as gaps to fill.
8. **Set the deposit branch.** Confirm open FAIR deposit as default; if metadata themselves are sensitive (e.g., precise endangered-species locations), document the restricted exception and justification.
9. **Self-check.** Verify cardinalities are consistent with the data, no invented term IDs remain unmarked, and every repository-required field is either mapped or flagged.

**Output format (locked):**

```
## Schema selection
Discipline: [...] | Study type: [...] | Deposit goal: [...] | Repository: [...]/[user-supplied]
Candidates considered: [list with fit/misfit notes]
Chosen schema(s): [primary (+secondary)] | Rationale: [...] | Rejected: [why]
Deposit branch: [Open FAIR default | Restricted exception + justification]

## Metadata field list
| Field | Obligation | Cardinality | Vocabulary/Ontology binding | Definition |
|---|---|---|---|---|
| [...] | [Mandatory/Recommended/Optional] | [0..1/1/0..n/1..n] | [ontology name; term ID user-supplied] | [...] |

## Crosswalk: chosen schema → target repository
| Chosen-schema field | Repository required field | Mapping | Gap? |
|---|---|---|---|
| [...] | [...]/[user-supplied] | [direct/transform/none] | [yes/no] |

## Open items requiring user input
- [ ] [user-supplied] ...
```

**Reporting-standard alignment:** MIBBI family (MIAME/MINSEQE/MIxS/MIAPE/etc.); ISA model / ISA-Tab; Dublin Core; DataCite metadata schema; schema.org / Bioschemas; DDI; OBO Foundry ontologies; FAIR and TRUST principles. Specific field lists and term IDs referenced by standard name only — exact values `[user-supplied]`/verify.

**Verification checklist (before delivering):**
- [ ] Discipline, study type, and deposit goal are stated.
- [ ] Multiple candidate schemas were considered before selection.
- [ ] The chosen schema is named with rationale and rejected alternatives.
- [ ] Every field has obligation, cardinality, vocabulary binding, and definition.
- [ ] No ontology term ID, accession prefix, or non-existent field name is asserted; gaps are `[user-supplied]`/verify.
- [ ] Persistent identifiers (DOI/ORCID/ROR) appear where applicable.
- [ ] A crosswalk to the target repository is present, with gaps flagged.
- [ ] Deposit branch is set (open default or restricted exception); no promotional language.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Invented term IDs | A confident-looking ontology accession (e.g., `XXX:0001234`) that is fabricated | Bind ontology by name only; mark specific term IDs `[user-supplied]`/verify |
| Wrong-standard fit | Picking Dublin Core for a sequencing study that needs MIxS detail | Run the candidate enumeration; justify against the deposit goal and discipline |
| Phantom required field | Asserting a repository's required-field set from memory | Mark required-field lists `[user-supplied]`/verify; flag unconfirmed fields |
| Cardinality mismatch | Marking a repeatable field as 0..1, blocking valid records | Cross-check cardinality against the data dictionary and the standard |
| Sensitive metadata leak | Open-depositing metadata containing precise sensitive locations | Route to restricted exception; generalize or withhold sensitive fields |
