---
title: "Stage 3 — Draft Generation"
category: childrens-writing/pipeline
description: "Produces the full first-draft manuscript from the beat map, locked to the form's word-count band, age-appropriate voice, and convention contract. For illustrated forms, separates text from [art notes] so the prose never narrates what the picture will show."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - QA-01
  - QA-04
difficulty: advanced
tags:
  - childrens-writing
  - pipeline
  - stage-3
  - drafting
updated: "2026-06-24"
related_prompts:
  - childrens-book-studio/prompts/stage-2-structure-beatmap.md
  - childrens-book-studio/prompts/stage-4-revision-triage.md
---

# Stage 3 — Draft Generation

## Objective

Write the **full first-draft manuscript** from the beat map: complete, in the form's voice and word-count band, honoring the convention contract. The goal is a real draft to revise — not a polished final, and not a sketch.

## When to Use

- After the beat map is locked and gated.
- When restarting a draft from a sound structure.

## Inputs / Context

- The Stage 2 structure/beat map.
- The Stage 0 convention contract and word-count target.
- The Stage 1 protagonist voice and theme.

## Constraints

**Must:**
- Route to the form's workshop prompt to draft in its native mode (prose, verse, or graphic-novel script).
- Stay inside the word-count band.
- Keep the child protagonist driving the action; keep the theme carried by events.
- For illustrated forms, write the text and the **[art notes]** separately, and ensure the text does not narrate what the illustration will show.
- For nonfiction, draft only from the source plan; any specific not yet sourced is written with an inline `VERIFY` marker, never invented.

**Must Not:**
- Exceed the word-count band "to be safe."
- Insert a stated moral or a tacked-on lesson.
- Narrate the picture in illustrated forms ("art-describing text").
- Supply a nonfiction fact from memory in place of a source.

## Instructions

1. Route to the form's workshop prompt for drafting.
2. Draft beat by beat from the Stage 2 map.
3. For illustrated forms, maintain two tracks: the read-aloud/printed **text** and the **[art notes]** for the illustrator.
4. For nonfiction, draft against the source plan; mark any unsourced specific inline as `[VERIFY: claim]`.
5. Save as `manuscript.md` (a new file/version — do not overwrite an existing draft the author wants to keep).
6. Report the actual word count against the band.

## Output Format

```
MANUSCRIPT (first draft) — [FORM], ages [BAND]
[full text; for illustrated forms, text and [art notes] separated by page/spread]

WORD COUNT: N (band: ...) — IN BAND | OVER | UNDER
NONFICTION: open VERIFY markers: [count + list]   (must be resolved by Stage 5)
SAVED AS: manuscript.md
```

## Verification Checklist (the orchestrator gates on this)

- [ ] The draft is complete (every beat from Stage 2 is realized).
- [ ] Word count is inside the band.
- [ ] The child drives the action; no adult-rescue ending.
- [ ] No stated moral / tacked-on lesson.
- [ ] (Illustrated) Text and [art notes] are separate; the text does not narrate the art.
- [ ] (NF) No fact is invented; unsourced specifics carry inline `VERIFY` markers.

## False-Positive Prevention

- **A draft that's secretly an outline** — telly summary instead of scenes/spreads. Draft the actual text.
- **Word-count creep.** A picture book that drafts to 1,400 words is not "almost there"; it's a different form. Cut now.
- **Art-describing prose.** "She had a big red balloon" when the art shows the balloon — let the picture carry it.
- **A fabricated nonfiction specific dressed as fact.** Mark `VERIFY`; the truth gate will check.
