---
title: "Sample Logging & Chain-of-Custody Designer"
category: science/bench-and-wetlab
description: "Design a collision-proof sample-ID schema, freezer location model, ELN linkage, FAIR collection metadata, chain-of-custody hand-offs, and a retention/destruction schedule for biospecimens or physical samples."
techniques:
  - ST-01
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - chain-of-custody
  - sample-id-schema
  - biospecimen
  - freezer-location
  - eln-linkage
  - fair-metadata
  - retention-schedule
  - barcoding
updated: "2026-06-26"
related_prompts:
  - domain-science/bench-and-wetlab/science_lab_notebook_entry_writer.md
  - domain-science/bench-and-wetlab/science_reagent_validation_workflow.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
---

# Sample Logging & Chain-of-Custody Designer

**Objective:** Produce a complete sample-management design for a lab or study: a unique, collision-proof sample-ID schema (machine-readable + barcodable), a hierarchical freezer/box/position location model, explicit ELN linkage between sample, experiment, protocol, and data, FAIR-compliant collection metadata, documented chain-of-custody hand-offs, and a retention/destruction schedule grounded in a stated policy basis. The design must satisfy ALCOA+ data-integrity principles and prevent ID reuse and ambiguous identifiers.

**When to use:** Before a study begins collecting, aliquoting, or storing physical samples, or when an existing lab needs to formalize an ad-hoc, error-prone sample-tracking practice into an auditable system.

**Required inputs:**
- **Discipline.** [user-supplied] (e.g., molecular biology, clinical biobanking, environmental sampling)
- **Study type.** [user-supplied] (observational / experimental / longitudinal cohort / one-off collection)
- **Sample classes and expected volume.** Types of physical sample (blood, tissue, DNA aliquots, soil cores, etc.) and approximate counts over the study lifetime.
- **Storage hardware.** Freezers/fridges/ambient storage available, their numbering, and box/rack capacities (e.g., 9×9 cryobox).
- **ELN / LIMS in use.** [user-supplied] system name, or "none yet".

**Optional inputs:**
- Regulatory / IRB / IBC constraints, human-subjects status, or consent-driven destruction triggers.
- Existing ID conventions to migrate from (note: never reuse retired IDs).
- Multi-site / multi-operator hand-off requirements.
- Hazard classification (biohazard, controlled substance) affecting custody.

**Constraints — Must:**
- Design IDs that are **globally unique within the lab and never reused**, opaque-but-unambiguous, and barcode/QR-encodable; avoid human-friendly-but-collision-prone schemes (date-only, initials-only, sequential-without-namespace).
- Apply **ALCOA+** (Attributable, Legible, Contemporaneous, Original, Accurate, + Complete, Consistent, Enduring, Available) to every logged field.
- Capture collection metadata to a **FAIR** standard (Findable, Accessible, Interoperable, Reusable) with controlled vocabularies where they exist.
- Model location as a resolvable hierarchy (facility → freezer → shelf/rack → box → position) so any ID resolves to a single physical position and vice versa.
- Make ELN/LIMS linkage bidirectional: sample ↔ experiment ↔ protocol ↔ raw data, each by stable identifier.
- Reference **ISBER biospecimen best-practice** concepts and **good documentation practice** for any human/clinical biospecimen handling.
- State a **policy basis** for every retention/destruction rule (regulation, IRB protocol, funder mandate, or internal SOP).

**Constraints — Must Not:**
- Do not invent vendor names, catalog/lot numbers, reagent specs, or results/observations. If needed and not supplied, mark `[user-supplied]` and ask; the prompt records what the user supplies, it never fabricates data.
- Do not design IDs that can collide, be reused after destruction, or be ambiguous (no bare dates, no operator-initials-only, no non-namespaced counters).
- Do not embed sensitive PHI/PII inside the sample ID itself.
- Do not use promotional language ("novel", "groundbreaking", "first-ever", "gold standard") in drafted text.
- Do not assume an Open Science deposit is permissible for restricted human samples — gate metadata sharing on consent/regulatory status.

**Instructions:**

1. **Confirm scope.** Restate discipline, study type, sample classes, volume, storage hardware, and ELN/LIMS. Flag any required input left as `[user-supplied]`.
2. **Design the ID schema.** Specify a namespaced, fixed-grammar identifier (e.g., `LAB-PROJ-YYYY-NNNNN-AA` where `AA` is an aliquot suffix), state the character set, length, check-digit or checksum if used, and the barcode/QR encoding. Document the explicit rule that IDs are never reused and retired IDs are tombstoned, not recycled.
3. **Model storage location.** Define the location hierarchy and a canonical location string; define how a position maps 1:1 to one occupied ID, and how vacancy/transfer is recorded.
4. **Define collection metadata (FAIR).** Enumerate mandatory fields captured at collection (collector, timestamp, source, method, processing steps, consent reference if applicable) with units and controlled vocabularies; mark anything not supplied as `[user-supplied]`.
5. **Wire ELN/LIMS linkage.** Specify the bidirectional links sample ↔ experiment ↔ protocol ↔ data and the stable identifiers used on each side; note how a sample record points to its originating protocol and downstream datasets.
6. **Specify chain-of-custody.** Define each hand-off event (who, when, from→to, condition, freeze-thaw count) and how it is logged contemporaneously and attributably per ALCOA+.
7. **Set retention/destruction schedule.** For each sample class, give retention duration, destruction method, trigger conditions (including consent withdrawal), and the policy basis citation; record disposition events.
8. **Emit the locked outputs.** Produce the ID-schema specification and the sample-register table template.
9. **Open Science branch.** If samples and consent permit, recommend depositing the de-identified sample-metadata schema and a FAIR sample manifest alongside the ELN/protocol deposit; otherwise state why sharing is gated.

**Output format (locked):**

```
## Scope
- Discipline / study type:
- Sample classes & volume:
- Storage hardware:
- ELN/LIMS:
- Open items ([user-supplied]):

## Sample-ID Schema Specification
- ID grammar (with example):
- Character set / length / checksum:
- Barcode/QR encoding:
- Uniqueness & non-reuse rule:
- Tombstoning of retired IDs:

## Storage Location Model
- Hierarchy & canonical location string:
- Position ↔ ID mapping rule:
- Transfer/vacancy logging:

## Collection Metadata (FAIR)
| Field | Mandatory? | Controlled vocab/units | Source |
|---|---|---|---|

## ELN/LIMS Linkage
- sample ↔ experiment:
- sample ↔ protocol:
- sample ↔ data:

## Sample-Register Table Template
| Sample ID | Parent ID | Sample class | Collection ts | Collector | Location | Freeze-thaw n | ELN link | Data link | Status | Retention until | Disposition |
|---|---|---|---|---|---|---|---|---|---|---|---|

## Chain-of-Custody Log Template
| Event ts | From | To | Condition | Reason | Logged by |
|---|---|---|---|---|---|

## Retention & Destruction Schedule
| Sample class | Retention | Destruction method | Trigger(s) | Policy basis |
|---|---|---|---|---|

## Open Science Disposition
- Shareable? (yes/gated/no) + rationale:
```

**Reporting-standard alignment:** ALCOA+ data-integrity principles; ISBER biospecimen best practices (concept); FAIR metadata; good documentation practice; STAR Methods (Resource/Reagent table linkage for any deposited samples).

**Verification checklist (before delivering):**
- [ ] ID grammar is namespaced, fixed-length/parseable, and barcodable; an example resolves unambiguously.
- [ ] Non-reuse and tombstoning rules are explicit; no bare-date or initials-only IDs anywhere.
- [ ] No PHI/PII embedded in the ID.
- [ ] Location model resolves any ID to exactly one physical position.
- [ ] ELN linkage is bidirectional across sample/experiment/protocol/data by stable IDs.
- [ ] Every metadata field has units/vocabulary or is marked `[user-supplied]`.
- [ ] Each retention/destruction rule cites a policy basis.
- [ ] No fabricated vendors, catalog/lot numbers, or sample counts; banned promotional terms absent.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| ID collision | Date+initials ID looks unique until two operators sample the same day | Require namespaced counter + checksum; forbid date-only/initials-only schemes |
| ID reuse | Recycling a freed ID after destruction "saves space" | Tombstone retired IDs; uniqueness is over the full study lifetime, not current inventory |
| Orphaned sample | Sample logged but no link back to protocol/data feels complete | Enforce bidirectional ELN linkage as a mandatory register column |
| Stale location | Register shows a box that was already moved | Log transfer/vacancy events; position↔ID mapping is 1:1 and updated contemporaneously |
| Improper sharing | De-identified metadata deposited despite consent limits | Gate Open Science branch on consent/regulatory status before any deposit |
