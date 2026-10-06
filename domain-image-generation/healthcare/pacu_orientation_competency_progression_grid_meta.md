---
title: PACU Orientation Competency Progression Grid — Image Meta-Prompt
category: pacu/image-generation
target_models:
  - nano-banana
  - dall-e-3
techniques:
  - SV-11
  - SV-12
  - SV-13
  - SV-14
  - SV-15
  - SV-16
  - SV-17
  - SV-18
updated: "2026-10-06"
tags:
  - pacu
  - image-generation
  - orientation
  - competency-grid
---

# Image Meta-Prompt: PACU Orientation Competency Progression Grid

> Safety reminder: Grid is a planning visual — expected trajectory, not a contract. Patient care decisions remain governed by facility orders.

## What this meta-prompt produces

A **competencies × weeks grid** rendered as a flat tabloid-print wall reference. Rows are PACU competencies; columns are orientation weeks. Each cell shows the target sign-off level (Independent / With Cues / With Direction / Not Yet) using color and a one-letter token. Designed for 17 × 11 inch tabloid print or 11 × 8.5 landscape letter.

## INPUTS block

- **Competency list:** {{paste from `pacu_orientation_skill_acquisition_timeline.md` output — rows}}
- **Orientation weeks:** {{e.g., Week 0 → Week 10 — columns}}
- **Per-cell target level:** {{from skill-acquisition timeline grid: I / C / D / N}}
- **Orientee background label:** {{e.g., "Experienced ICU RN, 10 weeks"}}
- **Canvas:** 11 × 8.5 landscape, 300 DPI (or 17 × 11 tabloid for more rows).
- **Color tokens:**
  - **I (Independent):** teal #0f766e
  - **C (With Cues):** light teal #14b8a6
  - **D (With Direction):** amber #b45309
  - **N (Not Yet):** light gray #d4d4d8

---

## READY-TO-PASTE IMAGE PROMPT

```
Generate one (1) flat infographic — NOT a dashboard, NOT a spreadsheet UI, NOT a Gantt chart screenshot.

SUBJECT: PACU orientation competency progression grid — competencies (rows) × orientation weeks (columns).

PHYSICAL CONTEXT: 11x8.5 inch landscape print-ready wall reference for a PACU breakroom or educator office. Flat print artwork. Not a software grid view.

CRITICAL OUTPUT RULES:
- One image. Landscape 11:8.5 (or 17x11 tabloid if grid is large).
- Pure white #FFFFFF background. No gradient. No shadow. No drop shadow on cells.
- Flat vector. No 3D. No bevel. No glow. No skeuomorphic table styling.
- High-contrast sans-serif text.
- No watermarks.

LAYOUT (enumerated):
- TITLE BAR top, full width. Fill teal {{stable accent}}. White bold 22pt: "PACU Orientation Competency Progression — {{orientee background label}}".
- SUBTITLE BAR below title, 12pt, dark gray: "Expected typical trajectory. Not a sign-off rubric."
- COLUMN HEADERS: row across showing "Week 0", "Week 1", "Week 2", ..., "Week N". 11pt bold, center-aligned. Light gray separator below.
- ROW HEADERS (competencies, left column, ~25% of width): 11pt regular, left-aligned. Examples:
  - Airway & breathing
  - Hemodynamic assessment
  - Oxygenation & ventilation
  - Post-op pain
  - PONV
  - Emergence & delirium
  - Regional / neuraxial block
  - Handoff inbound
  - Handoff outbound
  - Family communication
  - Judgment in ambiguity
  - Documentation
  - Team collaboration
- GRID CELLS: equal-width, equal-height. Each cell filled per the I/C/D/N color token:
  - I → teal {{stable}}. White centered letter "I" 12pt bold.
  - C → light teal. Dark text "C" 12pt bold.
  - D → amber {{watch}}. Dark text "D" 12pt bold.
  - N → light gray. Dark text "N" 11pt regular.
- Thin 0.5pt light-gray cell borders.
- LEGEND bottom-left strip: 4 color swatches with labels "Independent / With Cues / With Direction / Not Yet". 10pt.
- FOOTER STRIP bottom. 9pt gray. Text: "Expected typical trajectory for {{orientee background}}. Actual sign-off levels per facility orientation program. Educational aid only."

TYPOGRAPHY: sans-serif throughout. Title 22pt bold. Subtitle 12pt. Column headers 11pt bold. Row headers 11pt regular. Cell tokens 12pt bold (I/C/D) or 11pt regular (N). Legend 10pt. Footer 9pt gray.

COLOR PALETTE (strict, no other colors):
- Background white.
- Text black or dark gray (cells with light fill).
- Title bar teal {{stable}}, white text.
- I cell teal {{stable}}, white text.
- C cell light teal #14b8a6, dark text.
- D cell amber {{watch}}, dark text.
- N cell light gray #d4d4d8, dark text.

ALLOWED: rectangular grid, color-coded cells with letter tokens, row + column headers, legend, footer caveat.

FORBIDDEN: 3D table, dashboard widgets, sparklines inside cells, icons inside cells, emoji, photographic elements, drop shadow, gradient, bevel, glow, UI chrome, progress bars, tooltip popups, watermarks, hover states.

VALIDATION CHECKLIST:
1. One image, landscape, 300 DPI.
2. Title + subtitle + column headers + row headers + cell tokens + legend + footer present.
3. Every cell has both a fill color and a letter token (or "N" + gray for not-yet).
4. Legend matches color tokens used.
5. Footer caveat present.
6. No UI / 3D / dashboard styling.
```

---

## Model-specific notes

**Nano Banana** — grids render reliably with this layout; keep row count ≤ 14 for legible 11x8.5; for 15+ rows, upgrade to 17x11 tabloid.
**DALL·E 3** — may compress cells or skew alignment with > 11 columns; consider tabloid if orientation length > 10 weeks.
**Midjourney** — stylizes grids; not recommended for this precise reference card.

## Variants

- New-grad version: same template, different cell distribution per the orientee's specific timeline.
- Per-competency single-row strip: enlarge a single row for a "this one competency" focus poster.
- B&W print version: replace teal/amber with patterned fills (diagonal lines for D, solid for I) for grayscale printing.

---

## False-Positive Prevention

❌ **DON'T:**
- Let the model fill cells the timeline did not specify — 13 rows by 11 weeks is 143 cells, and gaps get filled by pattern (an "I" run spreading rightward); checklist item 3 passes because every cell has a token.
- Treat an "I" cell as sign-off: on a breakroom wall an "I" beside "Regional / neuraxial block" or "Airway & breathing" can be read as permission to work unsupervised, when it only marks the expected trajectory.
- Accept "Independent" for any competency whose tasks need a provider order or a unit validation the orientee does not yet hold.
- Pass a cell whose fill and letter disagree — an amber cell lettered "C" still has "both a fill color and a letter token".

✅ **DO:**
- Recount: rendered rows equal pasted competencies, columns run Week 0 to Week N without gaps, and each row's token sequence, transcribed left to right, matches the skill-acquisition timeline input.
- Check fill-to-token agreement cell by cell (I teal, C light teal, D amber, N gray), and on the B&W variant confirm each pattern maps to one letter only.
- Confirm "Not a sign-off rubric." and "per facility orientation program" survive verbatim, and post the grid beside — never instead of — the unit's signed competency validation record.
