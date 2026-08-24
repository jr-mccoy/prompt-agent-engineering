---
title: "Carpentries-Style Data-Analysis Workshop Designer"
category: science/teaching-research-methods
description: "Design a hands-on, live-coded data-analysis workshop with learning outcomes, formative checks, scripted-not-clicked reproducibility, assessment, and post-workshop scaffolding."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-01
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - workshop-design
  - data-analysis
  - the-carpentries
  - live-coding
  - formative-assessment
  - reproducibility
  - backward-design
  - open-science
updated: "2026-06-26"
related_prompts:
  - domain-science/teaching-research-methods/science_reproducibility_workshop_designer.md
  - domain-science/teaching-research-methods/science_code_review_for_science_software.md
  - domain-science/computational/science_computational_reproducibility_environment.md
  - domain-science/computational/science_open_source_research_software_repo_layout.md
---

# Carpentries-Style Data-Analysis Workshop Designer

**Objective:** Design a hands-on data-analysis workshop in The Carpentries style: backward-designed from concrete learning outcomes, delivered through live coding broken into episodes, with frequent formative assessment, a realistic user-supplied dataset, scripted (not point-and-click) analysis so the work is reproducible, an end-of-workshop assessment, and post-workshop scaffolding that keeps participants going. The output is an episode-by-episode plan plus assessment and a materials checklist.

**When to use:** A scientist or instructor needs to teach a group (lab, course module, summer school, departmental training) to analyze data reproducibly and wants a concrete, runnable workshop rather than slides.

**Required inputs:**
- **Discipline.** The scientific field the data and examples come from.
- **Level / audience.** Workshop participants and their starting point (e.g., grad students who know no scripting; postdocs who use point-and-click tools; mixed lab).
- **Tool/stack.** The language/environment to teach (e.g., R/tidyverse, Python/pandas, shell + a stats tool) (`[user-supplied]` if undecided — recommend one).
- **Dataset.** A realistic dataset to build episodes around (`[user-supplied]`; if not provided, mark it and request one — do not invent data).

**Optional inputs:**
- **Duration.** Half-day, one day, or two days.
- **Prior workshops.** What participants have already done.
- **Logistics.** In-person/online, helper availability, machines/cloud.
- **Target analysis.** A specific end-goal figure or result participants should be able to produce.

**Constraints — Must:**
- Confirm discipline and level first; backward-design every episode from a stated, assessable learning outcome.
- Use live coding as the primary mode; include "type-along" segments and frequent formative checks (e.g., minute questions, multiple-choice diagnostics, sticky-note red/green progress signals).
- Make the analysis scripted and reproducible: scripts under version control, fixed seeds where stochastic, documented environment, raw-to-result path — not a sequence of GUI clicks.
- Build exercises and a worked end-to-end analysis on the user's dataset; never substitute invented data.
- Weave Open-Science defaults (sharing scripts, citing data, recording environment) into the content itself.
- Include both formative (during) and summative (end) assessment, plus post-workshop scaffolding (cheat-sheet, follow-up, community/help channel).

**Constraints — Must Not:**
- Do not invent papers, datasets, code facts, or citations the user hasn't supplied. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not design a lecture-only or demo-only session; hands-on live coding is required.
- Do not teach point-and-click workflows that cannot be reproduced from a script.
- Do not use "novel," "groundbreaking," "first-ever," or "gold standard" in any drafted text.

**Instructions:**

1. **Set scope and outcomes (backward design).** Confirm discipline, level, tool, dataset, and duration. Write 3–6 concrete learning outcomes ("by the end, participants can …") that are observable and assessable. Everything downstream derives from these.
2. **Map outcomes to episodes.** Break the workshop into 45–90 minute episodes, each owning one or two outcomes: typically load/inspect data → clean/tidy → explore/visualize → model/test → script + reproduce → share. Sequence from concrete to abstract.
3. **Design each episode for live coding.** For each: the live-coding narrative the instructor types, the dataset slice used, 1–2 formative checks, and a short hands-on exercise with a stated solution. Note predicted sticking points and how helpers triage them.
4. **Build in reproducibility as content.** Add an episode (or thread through episodes) where participants put their analysis in a script under version control, set a seed, capture the environment, and re-run from raw data to result. Cross-reference `domain-science/computational/science_computational_reproducibility_environment.md`.
5. **Weave Open-Science defaults.** Show how to share the script, cite the dataset, and record provenance so the analysis is FAIR. Keep it practical and embedded in the tasks, not a separate lecture.
6. **Design assessment.** Formative: per-episode checks and a mid-point pulse. Summative: a short end-task on the same dataset (or a held-out slice) that maps directly back to the learning outcomes, with a rubric. Include a pre/post self-assessment of confidence.
7. **Plan post-workshop scaffolding.** A one-page cheat-sheet, a follow-up exercise, where to get help (office hours / channel / community of practice), and next-step resources.
8. **Compile the materials checklist.** Setup instructions, dataset + data dictionary, episode scripts, exercise/solution files, slides (minimal), feedback form, helper guide.
9. **Assemble outputs and verify.** Emit the locked format and run the verification checklist.

**Output format (locked):**

```
## Workshop Overview
Discipline: [...] | Audience & level: [...] | Tool/stack: [...] | Duration: [...]
Dataset: [...] ([user-supplied] if missing)

## Learning Outcomes (backward-designed)
1. By the end, participants can [...]
[...]

## Episode Plan
### Episode N — <title> (<minutes>) → Outcome(s): [...]
- Live-coding narrative: [...]
- Dataset slice used: [...]
- Formative checks: [...]
- Hands-on exercise + solution: [...]
- Predicted sticking points / helper triage: [...]
[repeat per episode]

### Reproducibility thread
[version control, seed, environment capture, raw→result re-run]

## Open-Science Integration
[sharing scripts, citing data, provenance]

## Assessment
- Formative (per-episode + mid-point pulse): [...]
- Summative end-task + rubric: [...]
- Pre/post confidence self-assessment: [...]

## Post-Workshop Scaffolding
- Cheat-sheet: [...]
- Follow-up exercise: [...]
- Help / community: [...]
- Next-step resources: [...]

## Materials Checklist
[ ] Setup instructions  [ ] Dataset + data dictionary  [ ] Episode scripts
[ ] Exercise + solution files  [ ] Helper guide  [ ] Feedback form  [...]

## Open Items Needing User Input
[user-supplied] markers: [...]
```

**Reporting-standard alignment:** Aligns to The Carpentries pedagogy (live coding, formative assessment via minute questions and sticky notes, backward design from learning outcomes) and FAIR/FAIR4RS for the scripted, shareable analysis artifacts.

**Verification checklist (before delivering):**
- [ ] Discipline and audience level confirmed and reflected throughout.
- [ ] 3–6 observable, assessable learning outcomes drive the episodes (backward design).
- [ ] Every episode uses live coding and includes at least one formative check.
- [ ] Analysis is scripted and reproducible (version control, seed, environment, raw→result), not point-and-click.
- [ ] Exercises and worked analysis use the user-supplied dataset; no invented data.
- [ ] Open-Science defaults are embedded in tasks, not bolted on.
- [ ] Both formative and summative assessment present, with a rubric mapped to outcomes.
- [ ] Post-workshop scaffolding and a materials checklist included.
- [ ] No fabricated papers/datasets/citations; gaps marked `[user-supplied]`.
- [ ] No banned promotional language in any drafted text.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Lecture in disguise | Episodes are slides with a demo, no participant coding | Require live coding + a hands-on exercise per episode |
| Outcomes too vague | "Understand data analysis" — unassessable | Outcomes must be observable verbs tied to a summative check |
| Irreproducible workflow | Taught via GUI clicks that can't be re-run | Mandate scripted analysis under version control with seeds/environment |
| Toy data masquerading as realistic | Clean invented dataset hides messy real-data skills | Use the user's realistic dataset; if missing, mark `[user-supplied]` |
| Assessment theater | A quiz unrelated to what was practiced | Map every summative item back to a stated learning outcome |
| Workshop ends cold | No path forward, skills decay | Require cheat-sheet, follow-up exercise, and a help/community channel |
