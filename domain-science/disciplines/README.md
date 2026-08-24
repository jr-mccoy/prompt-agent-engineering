# `domain-science/disciplines/`

Discipline-specific prompts for the working scientist. Each prompt encodes discipline-specific decisions that the general-purpose Phase 2A–D prompts in `domain-science/methods-foundations/`, `statistics/`, `bench-and-wetlab/`, and `computational/` would otherwise leave ambiguous.

**Convention:** discipline-specific prompts live here only when a generic counterpart would lose force. Anything that applies across disciplines stays in the parent phase directories.

## Map

| Subdirectory | Count | Coverage |
|---|---|---|
| [`biology/`](biology/) | 5 | Genomics study design, microscopy, clinical-trial protocol outliner, omics metadata, field ecology |
| [`chemistry/`](chemistry/) | 4 | Synthesis-route critique, characterization battery, reaction kinetics, computational chemistry validation |
| [`physics-astronomy/`](physics-astronomy/) | 4 | Observable + measurement chain, systematic-uncertainty budget, observing proposal, astronomical reduction pipeline |
| [`earth-climate/`](earth-climate/) | 4 | Field campaign design, climate model intercomparison, remote-sensing validation, geochronology / age-model |
| [`neuroscience/`](neuroscience/) | 4 | Animal-behavior design, neuroimaging analysis plan, electrophysiology protocol, circuit-perturbation design |
| [`materials-engineering/`](materials-engineering/) | 3 | Synthesis-characterization-property planning, failure analysis, DOE plan |
| **Total** | **24** | |

## Floor (per `domain-science/README.md`)

Every prompt in this tree:
- requires the user to state discipline + study type + claim
- forbids fabricated catalog numbers, lab codes, citation references, reagent / opsin / instrument specifications
- locks the output format
- aligns to the relevant community reporting standard explicitly (ARRIVE 2.0, CONSORT, SPIRIT, MIAME / MINSEQE / MIxS / MIAPE / MSI, COBIDAS, NWB / DANDI, ASTM / ISO, CEOS-WGCV, CMIP / CF, BIDS, FAIR / CARE)
- pre-specifies analyses and exclusion criteria before data are inspected
- includes a verification checklist and false-positive matrix

## Open questions for future expansion

- Cognitive / behavioral science (psychology overlap with `domain-psychology/` and `domain-research-academic/`).
- Quantitative social science (overlap with `domain-research-academic/`).
- Clinical-trial execution (boundary with `domain-healthcare-clinical/`).
- A dedicated `ml-for-science/` cross-cutting set, deferred until usage signals demand.

See `domain-science/EXPANSION_ROADMAP.md` for the broader plan and the deferred decisions list.
