---
title: "Stage 0 — Project Setup & Form Selection"
category: childrens-writing/pipeline
description: "Establishes the project's form, age band, fiction/nonfiction type, and one-sentence concept, and locks the 'convention contract' the rest of the pipeline enforces. Carries the age-boundary gate (Gate 0): mature-content YA redirects out of the studio."
techniques:
  - ST-01
  - CM-02
  - DS-06
  - QA-01
difficulty: beginner
tags:
  - childrens-writing
  - pipeline
  - stage-0
  - form-selection
updated: "2026-06-24"
related_prompts:
  - childrens-book-studio/orchestrator_childrens_book.md
  - domain-childrens-writing/README.md
---

# Stage 0 — Project Setup & Form Selection

## Objective

Turn a raw children's-book idea into a locked **project spec**: the form, the age band, the fiction/nonfiction type, the one-sentence concept, and the **convention contract** (the specific load-bearing rules this form must honor downstream). This is the contract every later stage and gate checks against.

## When to Use

- First thing in any new project, before concept work.
- When an author isn't sure which form their idea fits.

## Inputs / Context

- The idea in one sentence.
- The intended reader (age, or a description to map from).
- Whether it's fiction or nonfiction (and, if NF, true-story vs. concept/STEM).
- Any special form/content flags (rhyming, verse, graphic novel, hard topic, writing across difference).

## Constraints

**Must:**
- Select exactly one form and age band from the table in `domain-childrens-writing/README.md`.
- State the word-count band for that form as the project's target.
- Write the convention contract — the subset of the nine domain conventions that bind this form (e.g., a picture book binds "read aloud" and "trust the illustrator"; nonfiction binds "accuracy is non-negotiable").
- Flag whether the project depicts an identity the author doesn't share (adds the across-difference audit later) and whether it touches a hard topic.

**Must Not:**
- Proceed if the content is mature-YA (explicit content / adult themes, ages 14+). **Redirect to `domain-creative-writing/`.** (Gate 0)
- Pick a form that fights the idea (e.g., a 4,000-word "picture book"). Resize the idea or re-pick the form.
- Invent reader research or market claims.

## Instructions

1. Map the reader + idea to a form and age band (use the orchestrator's Phase 2a table or the domain README).
2. Run **Gate 0**: if the content is mature-YA, stop and redirect. Otherwise continue.
3. State the word-count band as the target.
4. Write the convention contract: list the conventions this form must honor and one line on what each means for this project.
5. Set the form-conditioned route: which Stage 4 craft passes and Stage 5 path apply (see `PIPELINE_OVERVIEW.md` branching table). Note add-ons (rhyme polish, accuracy+back matter, illustrator collaboration, across-difference audit).
6. Point the author to the matching workshop prompt in `domain-childrens-writing/` for Stage 1–3.

## Output Format

```
PROJECT SPEC
- Concept (one sentence): ...
- Form: ...
- Age band: ...
- Type: fiction | nonfiction (true-story | concept/STEM)
- Word-count target: ...
- Special flags: [rhyming | verse | graphic novel | hard topic: ... | writing across difference | none]

GATE 0 — AGE BOUNDARY: PASS (not mature-YA)  | or  REDIRECT → domain-creative-writing/

CONVENTION CONTRACT (binds this project)
- [convention]: [what it means here]
- ...

ROUTE
- Workshop prompt: domain-childrens-writing/.../<file>.md
- Stage 4 craft passes: [list]
- Stage 5 path: [list]
- Add-ons: [across-difference audit? back matter? illustrator collaboration?]
```

## Verification Checklist (Gate 0 — the orchestrator gates on this)

- [ ] Exactly one form and age band selected, consistent with the reader.
- [ ] Content is **not** mature-YA (else redirected).
- [ ] Word-count target stated and realistic for the form.
- [ ] Convention contract lists the binding conventions for this form.
- [ ] Form-conditioned route set (Stage 4 passes + Stage 5 path + add-ons).
- [ ] The matching `domain-childrens-writing/` workshop prompt is named with a real path.

## False-Positive Prevention

- **An idea forced into the wrong form** (a sprawling concept squeezed into a board book). Resize the idea or re-pick the form before locking the spec.
- **Mature themes waved through as "edgy MG."** If it's genuinely mature-YA, redirect — don't stretch the age boundary.
- **"Diverse" content assumed safe.** If the author depicts an identity they don't share, set the across-difference add-on now; don't skip it.
- **A word-count target invented to flatter the idea.** Use the domain README's real bands.
