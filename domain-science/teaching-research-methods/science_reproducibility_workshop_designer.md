---
title: "One-Day Paper-to-Reproducible-Artifact Workshop Designer"
category: science/teaching-research-methods
description: "Design a one-day workshop in which participants convert a paper into a fully reproducible artifact through hands-on stations and leave with a reproducibility self-audit and follow-up plan."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-01
  - QA-02
  - CM-02
difficulty: advanced
tags:
  - reproducibility
  - workshop-design
  - fair4rs
  - version-control
  - environment-capture
  - data-archiving
  - the-carpentries
  - open-science
updated: "2026-06-26"
related_prompts:
  - domain-science/teaching-research-methods/science_data_analysis_workshop_designer.md
  - domain-science/teaching-research-methods/science_code_review_for_science_software.md
  - domain-science/computational/science_computational_reproducibility_environment.md
  - domain-science/computational/science_open_source_research_software_repo_layout.md
---

# One-Day Paper-to-Reproducible-Artifact Workshop Designer

**Objective:** Design a one-day, hands-on workshop in which each participant takes a paper — their own or a supplied one — and walks it through a sequence of stations that leave them with a reproducible artifact: code under version control, a captured environment, organized data and code, a one-command reproduce path, and an archived release with a DOI. Participants finish with a completed reproducibility self-audit and a follow-up plan. The output is the agenda, per-station guides, a participant checklist, and success criteria.

**When to use:** A department, lab, journal-club, or training program wants to move a group from "the analysis is on my laptop" to "anyone can regenerate the result" in a single intensive day, using real papers.

**Required inputs:**
- **Discipline.** The field of the papers/participants; shapes data-archiving norms and repository choices.
- **Level / audience.** Participants and their starting reproducibility maturity (e.g., students who don't use version control; postdocs with scripts but no environment capture).
- **Paper source.** Whether participants bring their own paper/analysis or work from a single supplied one (`[user-supplied]`; do not invent a paper).
- **Tooling baseline.** What participants already use (`[user-supplied]`) — version control system, language, container/environment tools, archive (e.g., a Zenodo-style repository).

**Optional inputs:**
- **Group size and helpers.** Participant count and number of helpers/instructors.
- **Format.** In-person or online; machine/cloud setup.
- **Constraints.** Sensitive/embargoed data, licensing, institutional repository requirements.
- **Target depth.** Whether the day ends at "runs from one command" or pushes to a published, DOI-bearing release.

**Constraints — Must:**
- Confirm discipline and level first; backward-design the day from the success criterion "an independent person can regenerate the central result."
- Structure the day as hands-on stations with a clear timeline; each station produces a tangible piece of the artifact.
- Cover the full chain: version control, environment capture, data/code organization, one-command reproduce, and archiving with a DOI.
- Cross-reference `domain-science/computational/science_computational_reproducibility_environment.md` (environment capture) and `domain-science/computational/science_open_source_research_software_repo_layout.md` (organization/citability).
- Deliver a reproducibility self-audit as a participant artifact, plus a follow-up plan.
- Handle sensitive-data cases (share metadata/derived data, document access, never force public release of restricted data).
- Use The Carpentries pedagogy (live demonstration, formative checks, sticky-note progress signals, helpers).

**Constraints — Must Not:**
- Do not invent papers, datasets, code facts, or citations the user hasn't supplied. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not require public release of restricted, sensitive, or embargoed data; offer compliant alternatives.
- Do not present reproducibility as a checkbox; the artifact must actually re-run.
- Do not use "novel," "groundbreaking," "first-ever," or "gold standard" in any drafted text.

**Instructions:**

1. **Set the success criterion and scope.** Confirm discipline, level, paper source, and tooling baseline. State the day's success criterion (independent regeneration of the central result) and the target depth (one-command reproduce vs. archived DOI release). Identify any sensitive-data constraints up front.
2. **Build the timeline/agenda.** Lay out a one-day schedule: opening framing → stations with breaks → integration and self-audit → wrap-up and follow-up planning. Allocate realistic time per station and buffer for setup friction.
3. **Station — Version control.** Get the paper's code and key files into a version-controlled repository with a sensible history and a README. Formative check: each participant has a repo with the analysis committed.
4. **Station — Environment capture.** Capture exact dependencies/versions (lockfile/container/environment spec) so the analysis runs elsewhere. Cross-reference the reproducibility-environment prompt. Check: environment can be rebuilt from the spec.
5. **Station — Data & code organization.** Organize raw vs. processed data, scripts, and outputs; record data provenance and checksums; document the data dictionary. Cross-reference the repo-layout prompt. Handle sensitive data with metadata/derived-data sharing and access documentation.
6. **Station — One-command reproduce.** Wire raw inputs → result behind a single documented command (script/Make/pipeline), with seeds fixed for stochastic steps. Check: a neighbor can run it and get the central result within stated tolerance.
7. **Station — Archiving with a DOI.** Deposit a versioned release in an archive that mints a DOI, add a license and citation file, and link the artifact to the paper. For restricted data, archive code + metadata + access instructions. Check: a citable, versioned record exists (or is staged, respecting embargo).
8. **Integration — reproducibility self-audit.** Each participant completes a self-audit deliverable scoring their artifact across the chain (version control, environment, data, reproduce, archive, documentation) with concrete gaps and next actions.
9. **Wrap-up and follow-up plan, then verify.** Define a 30/60/90-day follow-up (finish gaps, peer-reproduce a colleague's artifact, adopt as lab default), list success criteria, then emit the locked format and run the verification checklist.

**Output format (locked):**

```
## Workshop Overview
Discipline: [...] | Audience & level: [...] | Paper source: [...] | Tooling baseline: [...]
Success criterion: [...] | Target depth: [one-command reproduce / archived DOI release]
Sensitive-data handling: [...]

## Agenda (one day)
| Time | Block | Output produced |
|---|---|---|
| [...] | Opening framing | [...] |
| [...] | Station 1 — Version control | [...] |
| [...] | Station 2 — Environment capture | [...] |
| [...] | Station 3 — Data & code organization | [...] |
| [...] | Station 4 — One-command reproduce | [...] |
| [...] | Station 5 — Archiving with a DOI | [...] |
| [...] | Integration — self-audit | [...] |
| [...] | Wrap-up & follow-up planning | [...] |

## Station Guides
### Station N — <name>
- Goal / artifact piece: [...]
- Live demonstration: [...]
- Hands-on steps: [...]
- Formative check (sticky-note signal): [...]
- Helper triage for common failures: [...]
- Cross-reference: [...]
[repeat per station]

## Participant Checklist
[ ] Repo under version control with README
[ ] Environment captured and rebuildable
[ ] Raw/processed data organized + provenance + data dictionary
[ ] One command reproduces the central result (seeds fixed)
[ ] Archived release with license, citation file, DOI (or compliant alternative)
[ ] Reproducibility self-audit completed

## Reproducibility Self-Audit (deliverable)
| Dimension | Status | Gap | Next action |
|---|---|---|---|
| Version control | [...] | [...] | [...] |
| Environment | [...] | [...] | [...] |
| Data & provenance | [...] | [...] | [...] |
| One-command reproduce | [...] | [...] | [...] |
| Archiving & citability | [...] | [...] | [...] |
| Documentation | [...] | [...] | [...] |

## Success Criteria
[...]

## Follow-Up Plan (30/60/90 day)
[...]

## Open Items Needing User Input
[user-supplied] markers: [...]
```

**Reporting-standard alignment:** Aligns to FAIR/FAIR4RS (findable/accessible/interoperable/reusable, citable research software) and The Carpentries pedagogy (live demonstration, formative checks, hands-on stations).

**Verification checklist (before delivering):**
- [ ] Discipline and participant level confirmed and used to shape stations.
- [ ] Day is backward-designed from "independent regeneration of the central result."
- [ ] All five stations present: version control, environment capture, data/code organization, one-command reproduce, archiving with DOI.
- [ ] Each station produces a tangible artifact piece and has a formative check.
- [ ] Sensitive/embargoed-data path provided; no forced public release of restricted data.
- [ ] Reproducibility self-audit deliverable and a 30/60/90-day follow-up plan included.
- [ ] Cross-references to the reproducibility-environment and repo-layout prompts present.
- [ ] No fabricated papers/datasets/citations; gaps marked `[user-supplied]`.
- [ ] No banned promotional language in any drafted text.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Reproducibility as checkbox | All boxes ticked but the artifact never actually re-runs | Require a neighbor to run one command and reproduce the central result |
| Environment drift hidden | Runs today on the author's machine, not captured | Mandate a rebuildable environment spec verified independently |
| Data over-exposure | Pushing restricted/sensitive data public to "be FAIR" | Offer metadata/derived-data + documented access; respect embargo/license |
| DOI without substance | Archived release that omits the code/data needed to reproduce | Archive must include code + provenance + run instructions, not just a PDF |
| Stations too ambitious for a day | Agenda overruns; participants leave with nothing finished | Realistic per-station timing + buffer; define minimum viable artifact |
| Skills evaporate after the day | No follow-up; nothing adopted as default | Require self-audit gaps + 30/60/90-day plan and a lab-default adoption step |
