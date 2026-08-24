# Domain: Science (Practitioner Library)

**Audience:** Working scientists, lab heads, postdocs, PhD students, research engineers, computational scientists, science writers, peer reviewers, grant-writers, and research-integrity officers.

**Scope:** End-to-end research practice — from refining a question through bench/field/computational execution, statistical analysis, writing, peer review, funding, mentorship, ethics, and public communication. This domain is the **doing** of science; it is not the same as the upstream `domain-research-academic/` directory, which covers generic research **methodology** patterns that apply across the humanities and social sciences.

**Status as of 2026-06-26:** Migrated from `domain-specialized-fields/science/` to a top-level domain. **Phase 1 (3 prompts), Phase 2J (`disciplines/`, 24 prompts), and Phase 2A (`methods-foundations/`, 14 prompts) shipped.** The 3 Phase 1 prompts were relocated into `methods-foundations/` when Phase 2A shipped. See [`EXPANSION_ROADMAP.md`](EXPANSION_ROADMAP.md) for the full ~141-prompt plan across 12 subdirectories and the remaining phases (2B–2L).

---

## Boundary with adjacent domains

| If the task is... | Use... |
|---|---|
| Generic research methodology (lit search strategy, qualitative coding, survey instruments) usable across all academic fields | [`domain-research-academic/`](../domain-research-academic/) |
| A health-professions clinical practitioner workflow (differential dx, SOAP, prior auth, etc.) | [`domain-healthcare-clinical/`](../domain-healthcare-clinical/) |
| Health-professions education (curriculum, OSCE, milestone narratives, CBME, learner self-study) | [`domain-healthcare-clinical/prompts/medical-education/`](../domain-healthcare-clinical/prompts/medical-education/) |
| Academic K-12 / higher-ed teaching workflows, accreditation, faculty development | [`domain-education-teaching/`](../domain-education-teaching/) |
| Psychology / therapy / behavioral health *practice* (clinical) | [`domain-psychology/`](../domain-psychology/) |
| Image generation for science (figure mockup, conceptual diagram, infographic) | [`domain-image-generation/`](../domain-image-generation/) — pair with science prompts from this domain for the figure planning step |
| Software engineering of scientific code (CI, testing, architecture review) | [`domain-software-engineering/`](../domain-software-engineering/) — pair with `science_open_source_research_software_repo_layout` from this domain for science-specific guidance |

A scientific lifecycle task often spans both this domain and one of the above. The convention is: **scientific judgment lives here; generic methodology / generic teaching / generic software craft lives in the corresponding adjacent domain.** Compose prompts across domains rather than duplicating.

---

## Conventions

Every prompt in `domain-science/` is built to the same structural floor:

1. **Required inputs** — discipline (e.g., molecular biology, condensed matter physics, ecology), study type, career stage, and any field-specific context the prompt needs.
2. **No fabrication of citations, datasets, results, or instrument specifications.** If a fact is required and not supplied, the prompt asks for it or flags the gap explicitly. No invented DOIs, journal names, grant program names, or vendor catalog numbers.
3. **Locked output format** — most outputs are structured (tables, IMRaD-aligned sections, numbered protocols, point-by-point response, decision matrices). No prose blobs where a table would communicate better.
4. **Reporting-standard alignment** — where a community standard exists, the prompt aligns to it: ARRIVE 2.0 (animal research), CONSORT (clinical trials), STROBE (observational), PRISMA (systematic reviews), MIBBI family (omics), STAR Methods (Cell), FAIR/CARE/TRUST (data), CRediT (authorship), ROSES / SAFE (synthesis).
5. **Pre-specification bias** — any prompt that affects analysis or interpretation distinguishes pre-specified vs exploratory work and flags garden-of-forking-paths risk.
6. **Verification checklist + false-positive matrix** at the end of each prompt, modeled on `PROMPT_QUALITY_STANDARDS.md`.
7. **Calibrated uncertainty in outputs** — effect sizes with CIs over isolated p-values; explicit statements of where evidence is thin; no rhetorical inflation ("groundbreaking," "novel," "first-ever") in drafted text.
8. **Open Science default** — preregistration, data sharing, and code release are surfaced as the default option, not an afterthought. Closed-data or proprietary-instrument cases are accommodated but flagged.

Filing convention: `science_{specific_function}.md` inside the relevant phase subdirectory (once subdirectories are created in Phase 2).

---

## Shipped subdirectories

### `methods-foundations/` (Phase 2A — 14 prompts + 3 relocated Phase 1 prompts)

The reusable methodology layer: question refinement, preregistration / Registered Reports, power and sample size, controls, blinding/randomization, confound and validity audits, replicability and reproducibility, and methods-section drafting. The 3 original Phase 1 prompts (`science_experimental_design_advisor`, `science_hypothesis_generator`, `science_literature_review_synthesizer`) were relocated here. See [`methods-foundations/README.md`](methods-foundations/README.md).

### `disciplines/` (Phase 2J — 24 prompts)

Discipline-specific prompts across biology, chemistry, physics-astronomy, earth-climate, neuroscience, and materials-engineering. See [`disciplines/README.md`](disciplines/README.md).

---

## Reputable open resources this domain draws on

The expansion roadmap is grounded in publicly available, openly licensed scientific community standards and handbooks rather than any single proprietary source. Key references include:

- **The Turing Way** (CC-BY-4.0) — reproducible, ethical, collaborative data science handbook
- **EQUATOR Network** — registry of reporting guidelines (CONSORT, STROBE, PRISMA, ARRIVE 2.0, SPIRIT, STARD, COREQ, SQUIRE, CHEERS, TRIPOD, MIBBI family)
- **Center for Open Science / OSF** — preregistration templates, Registered Reports workflow
- **FAIR Principles** (Wilkinson et al., 2016) and **CARE Principles** for Indigenous data governance
- **CRediT** contributor-role taxonomy (NISO Z39.104-2022)
- **NIH Rigor & Reproducibility** guidance and authentication-of-key-resources language
- **NSF DMP** and **DMPTool** institutional templates
- **Cochrane Handbook** for systematic reviews of interventions (open access)
- **rOpenSci** Packages: Development, Maintenance, and Peer Review guide
- **Carpentries** (Software / Data / Library Carpentry) lessons — CC-BY teaching curriculum
- **STAR Methods** (Cell Press) — structured methods format
- **ARRIVE 2.0** — animal research reporting
- **PRINCIPLES of digital data management** as articulated in Nature Scientific Data
- **DORA** (Declaration on Research Assessment) — assessment criteria

Where a Phase 2 prompt closely parallels one of these standards, the prompt cites the standard by name in its instruction body so the user can verify directly against the source.

The roadmap also takes inspiration from publicly available Anthropic prompt and skill collections (Anthropic Cookbook, Claude Skills repository), the prompt-engineering patterns codified elsewhere in this repository (`techniques/MASTER_TECHNIQUE_INDEX.md`), and the structural conventions established by `domain-legal/` and `domain-healthcare-clinical/`.

---

## How to use

- **Find a prompt for an existing task:** browse the table in `EXPANSION_ROADMAP.md` (Shipped + Planned) or grep this directory.
- **Need a related but missing prompt:** the roadmap lists ~120 planned prompts with one-line descriptions; if your need maps to a planned slot, that's the right next thing to build.
- **Need to compose across domains:** see the boundary table above.

**Pairs especially well with:**

- `domain-research-academic/research_systematic_review_protocol.md` (when this domain's `science_meta_analysis_protocol` ships in Phase 2D)
- `domain-prompt-engineering/evaluation/correctness_*` prompts when validating ML-for-science outputs
- `domain-presentations/` for conference talks and seminar decks
- `domain-image-generation/` for figure mockup and conceptual diagram generation
