---
title: "Stage 6 — Publishing Package (Gate C Publishing Honesty)"
category: childrens-writing/pipeline
description: "Assembles the submission package — logline + comps, query letter, one-page synopsis, formatted sample — for a finished manuscript. Gate C blocks any fabricated comp title, agent/publisher name, or sales figure: all unverifiable items are bracketed [AUTHOR TO VERIFY]. Produces the final deliverable manifest."
techniques:
  - ST-01
  - CM-02
  - RP-01
  - QA-01
  - QA-04
difficulty: advanced
tags:
  - childrens-writing
  - pipeline
  - stage-6
  - publishing
  - submission
updated: "2026-06-24"
related_prompts:
  - childrens-book-studio/prompts/stage-5-format-polish-accuracy.md
  - domain-childrens-writing/publishing-business/childrens_query_letter_kidlit.md
  - domain-childrens-writing/publishing-business/childrens_pitch_comps_market_positioning.md
---

# Stage 6 — Publishing Package

## Objective

Turn a finished, gate-passed manuscript into a **submission-ready package**: a logline and comp framing, a form-correct query letter, a one-page synopsis, and a correctly formatted sample. Clear the **publishing-honesty gate (Gate C)**: nothing fabricated; every unverifiable market fact bracketed for the author to research.

## When to Use

- After Stage 5 passes Gate B (or as the entry point for an already-finished manuscript via `/build-submission-package`).

## Inputs / Context

- The polished manuscript and its companion artifacts.
- The Stage 0 form and age band (drives query/synopsis norms).
- Any real comps/agent research the author has already done.

## Constraints

**Must:**
- Run the publishing-business prompts in order:
  1. `publishing-business/childrens_pitch_comps_market_positioning.md` — logline + comp *framing* and positioning.
  2. `publishing-business/childrens_query_letter_kidlit.md` — form-specific query.
  3. `publishing-business/childrens_synopsis_submission_package.md` — one-page synopsis + package assembly.
- Bracket EVERY unverifiable market fact as `[AUTHOR TO VERIFY: ...]`: comp titles, agent/agency names, sales/advance figures, market statistics, and agency-specific submission rules.
- Where a comp is needed, explain *what kind of comp would work and why* and leave the title for the author to supply — do not assert a real title from memory.
- Treat agency submission guidelines as the source of truth; instruct the author to confirm format per agent.

**Must Not:**
- Invent a comp title, agent name, agency, sales figure, or submission rule.
- Present a bracketed placeholder as if it were verified.
- Ship the package if any fabricated market fact remains unbracketed.

## Instructions

1. Run the pitch/comps prompt: produce the logline and the comp *criteria* (genre, age, tone, recency), bracketing actual titles `[AUTHOR TO VERIFY]`.
2. Run the query prompt: produce a form-correct query with the hook, metadata line (title, form, age, word count — all real from the project), pitch, and a bio drawn only from author-supplied facts.
3. Run the synopsis/package prompt: produce a one-page synopsis (spoils the ending) and assemble the package, with formatting flagged to confirm against each agency's guidelines.
4. Run the Gate C check (below) and assemble the deliverable manifest.

## Output Format

```
SUBMISSION PACKAGE
- submission/logline-and-comps.md   (comps bracketed [AUTHOR TO VERIFY])
- submission/query-letter.md
- submission/synopsis.md

GATE C — PUBLISHING HONESTY: PASS | FAIL
  - no fabricated comp titles (all bracketed or author-supplied): PASS/FAIL
  - no fabricated agent/agency names: PASS/FAIL
  - no fabricated sales/advance/market figures: PASS/FAIL
  - submission rules flagged to verify per agency: PASS/FAIL

DELIVERABLE MANIFEST
- manuscript.md ............ present/missing
- art-notes.md ............. present/missing/NA
- back-matter.md ........... present/missing/NA
- submission/ ............. present/missing
- representation-audit.md . present/missing/NA
```

## Verification Checklist (Gate C — the orchestrator gates on this)

- [ ] No comp title is asserted as real; every one is author-supplied or bracketed `[AUTHOR TO VERIFY]`.
- [ ] No agent, agency, sales figure, advance, or market statistic is fabricated.
- [ ] Submission formatting is flagged to confirm against each agency's actual guidelines.
- [ ] The query's metadata (title, form, age, word count) is real and consistent with the project.
- [ ] The deliverable manifest lists every artifact the form requires and each is present and non-placeholder.

## False-Positive Prevention

- **A "perfect comp" supplied from memory.** Even a real-sounding title can be wrong, mis-aged, or mis-attributed. Bracket it.
- **A bio padded with achievements the author didn't state.** Use only author-supplied facts.
- **Invented agency rules** ("most agents want the first 10 pages"). Flag to verify per agent; don't assert.
- **A bracketed placeholder presented as done.** The package isn't finished until the author fills the brackets — say so.
