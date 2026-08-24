---
title: "Open-Source Research Software Repository Layout"
category: science/computational
description: "Design an rOpenSci- and FAIR4RS-aligned repository skeleton for research software — tests, CI, docs, OSI license, CITATION.cff, semantic-version releases, and a Zenodo/Software-Heritage archived DOI — bridging scientific reproducibility with software-engineering practice."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-01
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - research-software
  - repository-layout
  - citation-cff
  - semantic-versioning
  - zenodo-archiving
  - ropensci
  - fair4rs
  - joss
updated: "2026-06-26"
related_prompts:
  - domain-science/computational/science_computational_reproducibility_environment.md
  - domain-science/computational/science_simulation_validation_protocol.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
  - domain-software-engineering/analysis/architecture/architecture_layer_identification.md
---

# Open-Source Research Software Repository Layout

**Objective:** Produce a complete, rOpenSci- and FAIR4RS-aligned repository skeleton for research software: source layout, tests with coverage, continuous integration, documentation (README, API docs, tutorials/vignettes), an OSI-approved license, a `CITATION.cff` with how-to-cite guidance, contribution and conduct files, a changelog with semantic-version release tags, and an archived release carrying a persistent DOI (Zenodo or Software Heritage), plus a JOSS-readiness note. This is the **bridge** prompt between `domain-science/` and `domain-software-engineering/`: it owns the research-software-specific concerns — citability, archiving, scientific test fixtures, reproducibility — and explicitly defers generic engineering depth (CI mechanics, testing strategy, code architecture, packaging internals) to `domain-software-engineering/`.

**When to use:** When releasing research code as an open-source package, preparing a software paper (e.g., for JOSS), or making an existing analysis/simulation codebase citable, contributable, and archivable.

**Required inputs:**
- **Discipline.** [user-supplied] (e.g., ecology, astronomy, genomics, computational social science)
- **Study type.** [user-supplied — typically `computational`; note if the software underpins a forthcoming publication]
- **Language / packaging ecosystem.** R, Python, Julia, etc. (drives directory conventions, docs tooling, and rOpenSci vs. PyOpenSci-style norms).
- **Software maturity & audience.** Internal script, lab tool, or community package; expected external users/contributors.
- **Intended archive & citation target.** Zenodo, Software Heritage, an institutional repository; and whether a software paper (JOSS or similar) is planned. Mark `[user-supplied]` if undecided.

**Optional inputs:**
- Existing repo contents (so the skeleton is a gap-fill, not a greenfield).
- Funding/affiliation and the preferred author/contributor metadata for citation.
- Any domain reporting or data standards the software must interoperate with.
- A reproducibility environment already specified (link rather than duplicate).

**Constraints — Must:**
- Provide a directory **tree** covering: source, tests, CI config, docs, examples/tutorials, `LICENSE`, `README`, `CITATION.cff`, `CONTRIBUTING`, code of conduct, and `CHANGELOG`.
- Use an **OSI-approved license** and state it explicitly; do not leave licensing implicit (unlicensed code is not reusable).
- Include a **`CITATION.cff`** and a "How to cite" section, so the software is citable independently of any paper.
- Adopt **semantic versioning** and **release tags**, with a `CHANGELOG` mapping versions to changes.
- Specify an **archived release with a persistent DOI** (Zenodo via the GitHub integration, or Software Heritage), so a citable, immutable snapshot exists.
- Include **tests with coverage** and **CI** that runs them — but reference `domain-software-engineering/` for the generic testing/CI/architecture depth rather than re-deriving it here.
- Align with **rOpenSci/PyOpenSci packaging & peer-review** norms and **FAIR4RS** principles; name them where a file maps to them.
- Add a **JOSS-readiness** note (substantial scholarly effort, documentation, tests, license, and a short paper) when a software paper is intended.
- Keep the **research-software-specific** items as this prompt's core: citability, archiving/DOI, scientific test fixtures (e.g., known-answer/regression cases), and the link to the reproducibility environment.

**Constraints — Must Not:**
- Do not invent citations, DOIs, tool version numbers, benchmark values, or convergence thresholds. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not re-author generic software-engineering guidance that already lives in `domain-software-engineering/` — cross-reference it instead, and keep this prompt focused on research-software specifics.
- Do not present a release as archived/citable without an actual persistent-DOI archiving step.
- Do not omit a license or treat "it's on GitHub" as a license.
- Do not use promotional language ("novel", "groundbreaking", "first-ever", "gold standard") in the drafted README or paper note.

**Instructions:**

1. **Establish scope and ecosystem.** Confirm language, maturity, audience, and whether a software paper is planned. Map to the relevant community packaging norms (rOpenSci for R, PyOpenSci for Python, etc.).
2. **Lay out source and tests.** Define the source directory convention for the ecosystem and a tests directory that includes scientific fixtures — known-answer/regression cases that protect the software's *scientific* correctness, not just its plumbing. Defer general test-strategy depth to `domain-software-engineering/`.
3. **Wire documentation.** Specify a `README` (what it does, install, minimal example, how to cite), API/reference docs, and at least one tutorial/vignette. Documentation completeness is a FAIR/rOpenSci review criterion.
4. **Add licensing and conduct.** Choose an OSI-approved license; add `CONTRIBUTING` and a code of conduct to make external contribution viable.
5. **Make it citable.** Add `CITATION.cff` with author/version metadata and a "How to cite" block referencing the archived DOI (filled in after archiving; `[user-supplied]` until then).
6. **Version, changelog, release.** Adopt semantic versioning, maintain a `CHANGELOG`, and tag releases. Tie each release to a changelog entry.
7. **Archive for a persistent DOI.** Configure Zenodo (GitHub release integration) or Software Heritage so a tagged release produces an immutable, citable snapshot with a DOI; record the concept-DOI vs. version-DOI distinction.
8. **Reference CI/engineering and check JOSS readiness.** Point to `domain-software-engineering/` for CI mechanics, architecture, and testing strategy; then assess JOSS-readiness (license, tests, docs, scholarly effort, paper.md) if a software paper is planned.
9. **Self-check.** Confirm every checklist item maps to a concrete file or step, and that nothing claimed as "citable/archived" lacks a real archiving action.

**Output format (locked):**

```
## Repository Scope
- Discipline / study type:
- Ecosystem & community norm (rOpenSci / PyOpenSci / other):
- Maturity & audience:
- Archive & citation target:

## Directory Tree
```
project/
├── README.md
├── LICENSE                # OSI-approved [user-supplied choice]
├── CITATION.cff
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── CHANGELOG.md
├── <source dir>/          # ecosystem convention
├── tests/                 # incl. scientific known-answer/regression fixtures
├── docs/                  # API reference + tutorial/vignette
├── examples/
├── <ci config>/           # → see domain-software-engineering/ for depth
└── <reproducibility env>  # → link reproducibility-environment prompt
```

## Research-Software-Specific Items
- Scientific test fixtures (known-answer / regression):
- Citability (CITATION.cff + How-to-cite):
- Archiving (Zenodo / Software Heritage, concept vs. version DOI):
- Reproducibility-environment link:

## Engineering Cross-References (deferred to domain-software-engineering/)
- CI mechanics:
- Testing strategy / coverage tooling:
- Code architecture / packaging internals:

## Release & Citation Checklist
- [ ] OSI license present and stated
- [ ] CITATION.cff + How-to-cite
- [ ] Semantic version + tagged release + CHANGELOG entry
- [ ] Archived release with persistent DOI
- [ ] Tests (incl. scientific fixtures) run in CI
- [ ] Docs: README + API + ≥1 tutorial
- [ ] JOSS-readiness note (if software paper planned)
```

**Reporting-standard alignment:** rOpenSci/PyOpenSci packaging & peer-review guides, FAIR4RS (FAIR Principles for Research Software), Citation File Format (`CITATION.cff`), Semantic Versioning, Zenodo / Software Heritage archiving, and JOSS submission criteria. Generic engineering practice is delegated to `domain-software-engineering/`.

**Verification checklist (before delivering):**
- [ ] Directory tree includes source, tests, CI, docs, license, citation, contributing, conduct, and changelog.
- [ ] An OSI-approved license is named (not implicit).
- [ ] `CITATION.cff` and a How-to-cite section are present.
- [ ] Semantic versioning, release tags, and a changelog are specified.
- [ ] An archived release with a persistent DOI (Zenodo/Software Heritage) is included.
- [ ] Scientific test fixtures (known-answer/regression) are distinguished from generic tests.
- [ ] Generic CI/testing/architecture is cross-referenced to `domain-software-engineering/`, not re-derived.
- [ ] No fabricated DOIs, version numbers, or citations; unknowns marked `[user-supplied]`.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Implicit license | "It's public on GitHub, so it's reusable" | Require an OSI-approved license file, stated explicitly |
| Citable without archive | CITATION.cff present but no DOI snapshot | Require a Zenodo/Software Heritage archived release |
| Scope creep into SWE | Re-deriving CI/test/architecture guidance here | Cross-reference `domain-software-engineering/`; keep research-software focus |
| Plumbing-only tests | Coverage is high but scientific correctness untested | Add known-answer/regression scientific fixtures |
| Version churn confusion | Concept-DOI vs. version-DOI conflated in citations | Distinguish concept vs. version DOI in CITATION/How-to-cite |
| JOSS mismatch | "Paper-ready" without docs/tests/scholarly effort | Check JOSS criteria before claiming readiness |
