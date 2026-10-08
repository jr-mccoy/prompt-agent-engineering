---
title: "Reading Comprehension Worksheet Generator"
category: education
description: "Generate reading-comprehension worksheets with passage, text-dependent questions, and evidence lines."
techniques:
  - SV-05
  - SV-11
  - SV-12
  - SV-13
  - SV-14
  - SV-15
  - SV-16
  - SV-17
  - SV-18
tags:
  - language-arts
  - worksheet
  - reading-comprehension
  - close-reading
  - printable
updated: "2026-10-06"
---

# Reading Comprehension Worksheet Generator

**Purpose:** Generate reading-comprehension worksheets with passage, text-dependent questions, and evidence lines.

**Required intake:** Grade level, passage topic, lexile/complexity target, vocabulary, and question types.

**Output requirement:** Printable 8.5x11 portrait worksheet, black-and-white-ready.

---

## Intake Contract

Collect and confirm before generating:
1. Grade level or grade band.
2. Exact topic/standard focus.
3. Required vocabulary words or terms.
4. Difficulty target (on-level, intervention, extension).
5. Any accommodations (font size, chunking, sentence frames, reduced item count).

---

## Production Prompt Template

```text
TASK
Create EXACTLY ONE worksheet as flat print artwork.

REAL-WORLD CONTEXT ANCHOR
- This worksheet is printed on standard US letter paper and handed to students in class.
- It must be immediately usable with pencil.
- It must prioritize clarity over decoration.

DELIVERABLE LOCK
- Exactly 1 page.
- Portrait orientation only.
- 8.5 x 11 inches at 300 DPI (2550 x 3300 px).
- Solid white background (#FFFFFF).
- Black-and-white-ready; no color-dependent instructions.

TERMINOLOGY STEERING
- Treat output as "flat print artwork" and "ink-on-paper worksheet".
- Do NOT render as UI card, dashboard, tablet screen, or poster mockup.

GRID FORCING + ENUMERATED SLOTS
- Build the layout as explicit zones listed below.
- Keep strict rectangular zones with clear spacing.
- Do not merge or rename zones.

CONSTRAINT REDUNDANCY (GLOBAL)
- No gradients.
- No shadows.
- No bevels.
- No lighting effects.
- No rounded page corners.
- No photographic textures.

NEGATIVE SPACE CONTROL
- No desk scene, clipboard, hands, or classroom background.
- No extra border outside page edge.
- No perspective tilt; page viewed straight-on.

ALLOWED VS FORBIDDEN
- Allowed: lines, boxes, tables, simple monochrome icons, diagrams, dotted handwriting guides.
- Forbidden: app chrome, buttons, toggles, mock browser frames, stickers, watermarks, logos.

TYPOGRAPHY
- Use legible school-friendly sans-serif.
- Worksheet title 28-36 pt equivalent.
- Directions 14-18 pt equivalent.
- Body text 12-16 pt equivalent.
- Keep all text high contrast black on white.

BLACK-AND-WHITE SAFETY
- If emphasis is needed, use line weight, patterns, underlines, or labels—not color.

VALIDATION CHECKLIST (must pass before finalizing)
- [ ] Exactly one worksheet page.
- [ ] Portrait 8.5 x 11 in, print-ready.
- [ ] Flat print artwork vocabulary followed.
- [ ] No UI/mockup/staged-photo appearance.
- [ ] No gradients/shadows/rounded corners.
- [ ] Zones follow enumerated layout.
- [ ] Student instructions do not require color.
- [ ] Content matches provided grade, topic, and vocabulary.
```


## Subject-Specific Layout Spec

```text
LAYOUT ZONES
- ZONE 1: Header and reading purpose prompt.
- ZONE 2: Passage block with readable spacing.
- ZONE 3: Vocabulary-in-context questions.
- ZONE 4: Literal/inferential question set.
- ZONE 5: Evidence citation lines ("I found this in paragraph __").
- ZONE 6: Short constructed response box.

CONTENT LOCK
- Use provided grade level for readability and cognitive load.
- Use provided topic as the only content scope.
- Embed required vocabulary in directions and/or student tasks.
- Keep instructions concise, concrete, and student-facing.
```

## Notes

- Keep all decorative elements functional and monochrome.
- Do not add branding, mascots, or classroom logos.
- Prioritize print clarity for school photocopiers.

## False-Positive Prevention

❌ **DON'T:**
- Fill the lexile slot with an invented number; a Lexile measure comes only from the official analyzer, so write "not measured" if you did not run it.
- Judge grade fit from short sentences alone; rare multi-syllable vocabulary raises difficulty that sentence length hides.
- Label a ZONE 4 item "inferential" when its answer is stated verbatim, or "literal" when it needs outside knowledge.
- Leave ZONE 5 "paragraph __" lines when the render merged paragraphs or dropped their numbers.

✅ **DO:**
- Compute Flesch-Kincaid Grade Level on the passage text (0.39 x words/sentence + 11.8 x syllables/word - 15.59) and compare it with the intake grade; treat scores for passages under 100 words as rough.
- Answer each question from the rendered passage only and note the paragraph; rewrite any question answerable without reading the passage.
- Transcribe the rendered passage and diff it against the source text, since long blocks lose or garble words.
