# Children's Book Studio — Pipeline Overview

The flow from a raw idea to a finished, queryable children's book. Use this in **manual mode** (pick a stage and run its prompt) or as a map while the orchestrator drives in **guided mode**.

---

## Visual flow

```
                          ┌──────────────────────────────────────────────┐
   raw idea  ───────────▶ │ STAGE 0  Project Setup                        │
                          │ form · age band · fiction/NF · concept        │
                          └───────────────┬──────────────────────────────┘
                                          │  GATE 0 — Age boundary
                                          │  (valid form+age; mature-YA → redirect out)
                                          ▼
                          ┌──────────────────────────────────────────────┐
                          │ STAGE 1  Concept Foundation                   │
                          │ premise · protagonist + agency · theme        │
                          │ NF: topic narrowing + source plan             │
                          └───────────────┬──────────────────────────────┘
                                          ▼
                          ┌──────────────────────────────────────────────┐
                          │ STAGE 2  Structure & Beat Map                 │
                          │ form-specific outline                         │
                          └───────────────┬──────────────────────────────┘
                                          ▼
                          ┌──────────────────────────────────────────────┐
                          │ STAGE 3  Draft Generation                     │
                          │ full manuscript (+ [art notes] if illustrated)│
                          └───────────────┬──────────────────────────────┘
                                          ▼
              ┌──────────────────────────────────────────────────────────┐
              │ STAGE 4  Revision Triage   ◀── loops until gate passes    │
              │ diagnose → route to craft tools → fix-queue → apply       │
              └───────────────┬──────────────────────────────────────────┘
                              │  GATE A — Craft integrity
                              │  (agency · no preaching · read-aloud · reading level)
                              ▼
                          ┌──────────────────────────────────────────────┐
                          │ STAGE 5  Format Polish & Accuracy             │
                          │ illustrator/dummy · rhyme · accessibility     │
                          │ NF: accuracy verify + back matter             │
                          └───────────────┬──────────────────────────────┘
                                          │  GATE B — Truth & representation
                                          │  (NF sourced+back matter · audit=flags-only · no mature content)
                                          ▼
                          ┌──────────────────────────────────────────────┐
                          │ STAGE 6  Publishing Package                   │
                          │ pitch/comps → query → synopsis → package      │
                          └───────────────┬──────────────────────────────┘
                                          │  GATE C — Publishing honesty
                                          │  (no invented comps/agents · manifest complete)
                                          ▼
                              DELIVERABLE BUNDLE
                  manuscript · art notes/back matter · submission package · audit summary
```

---

## Stage I/O table

| Stage | Prompt | Inputs | Output | Routes to (in `domain-childrens-writing/`) |
|-------|--------|--------|--------|---------------------------------------------|
| 0 | `prompts/stage-0-project-setup.md` | the raw idea | project spec + convention contract | README routing table |
| 1 | `prompts/stage-1-concept-foundation.md` | project spec | premise, protagonist+agency, theme; NF source plan | matching `fiction-workshops/*` or `nonfiction-workshops/*`; `craft-tools/childrens_character_creation.md` |
| 2 | `prompts/stage-2-structure-beatmap.md` | concept foundation | form-specific structure/outline | the matching workshop prompt |
| 3 | `prompts/stage-3-draft-generation.md` | beat map | full first-draft manuscript | the matching workshop prompt |
| 4 | `prompts/stage-4-revision-triage.md` | draft | prioritized fix queue + revised draft | `craft-tools/*`, `representation-collaboration/childrens_writing_across_difference_audit.md` |
| 5 | `prompts/stage-5-format-polish-accuracy.md` | revised draft | polished manuscript + art notes/back matter | `representation-collaboration/childrens_illustrator_collaboration.md`, `..._accessible_inclusive_design.md`, `craft-tools/childrens_read_aloud_rhythm_rhyme_polish.md`, `nonfiction-workshops/*` |
| 6 | `prompts/stage-6-publishing-package.md` | polished manuscript | logline, comps, query, synopsis, package | `publishing-business/*` |

---

## Gate map (truth table)

| Gate | At stage | Passes when | Maps to factory |
|------|----------|-------------|-----------------|
| **0 Age boundary** | 0 | form + age band valid AND content not mature-YA | Gate 0 (justification/scope) |
| **A Craft integrity** | 4 | child drives climax · theme carried by action · read-aloud rhythm (PB/early reader/verse) · reading level on band | Gate A (security/integrity) |
| **B Truth & representation** | 5 | every NF specific sourced-or-`VERIFY` · back matter present · audit = flags/questions only (no certification) · no age-inappropriate content | Gate B (eval: capability + safety) |
| **C Publishing honesty** | 6 | no fabricated comps/agents/figures (bracketed `[AUTHOR TO VERIFY]`) · deliverable manifest complete | Gate C (disclosure) |

A FAIL on any gate stops advancement. The orchestrator names the failed item and returns the user to fix or re-run that stage.

---

## Form-conditioned branching

Not every stage runs for every form. The orchestrator prunes by form at Stage 0:

| Form | Stage 4 craft passes | Stage 5 path |
|------|----------------------|--------------|
| Board / concept (0-3) | minimal (page logic, sound/repetition) | read-aloud rhythm; (illustration handled by publisher) |
| Picture book (2-8) | opening, read-aloud, agency, sensitive-topics | illustrator collaboration + 32-page dummy; rhyme polish if rhyming |
| Early reader / chapter (5-10) | opening, dialogue, reading level, agency | accessible design; spot-art notes |
| Middle grade / upper-MG (8-14) | opening, dialogue, character, revision, sensitive-topics | accessible design (text-only) |
| Verse novel (8-12) | revision, agency, sensitive-topics | **read-aloud rhythm & rhyme polish (required)** |
| Graphic novel (6-12) | dialogue, structure, agency | illustrator collaboration (panel/page beats) |
| Narrative nonfiction | revision, sensitive-topics | **accuracy verify + back matter (required)** |
| Expository / STEM | revision, reading level | **accuracy verify + back matter + text features (required)** |

Any path that depicts an identity the author doesn't share adds the **write-across-difference audit** in Stage 4 (Gate B reviews its output).

---

## Recommended cadence

A run is a single project taken end-to-end; there is no ongoing loop or durable memory. To revise an existing manuscript, enter at Stage 4 (`/revise-manuscript`). To build only a submission package for a finished manuscript, enter at Stage 6 (`/build-submission-package`).

---

## Terminal artifact

```
<your-project>/
├── manuscript.md                 # final text (prose / verse / GN script)
├── art-notes.md                  # illustrated forms only
├── back-matter.md                # nonfiction only (sources, author's note)
├── submission/
│   ├── logline-and-comps.md      # comps bracketed [AUTHOR TO VERIFY]
│   ├── query-letter.md
│   └── synopsis.md
└── representation-audit.md       # flags + questions for a human reader (if applicable)
```
