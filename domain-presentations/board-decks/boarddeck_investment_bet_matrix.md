---
title: "Investment Bet Matrix Slide Visual"
category: presentations/board-decks/image-generation
description: "Constraint-locked image prompt for a board-deck investment bet matrix visual in 16:9 format."
techniques:
  - SV-11
  - SV-12
  - SV-13
  - SV-14
  - SV-15
  - SV-16
  - SV-17
  - SV-18
difficulty: intermediate
tags:
  - board-deck
  - executive-presentation
  - image-generation
  - slide-visual
  - "16:9"
updated: "2026-10-06"
related_prompts:
  - domain-image-generation/IMAGE_GENERATION_GUIDE.md
  - domain-image-generation/infographic_meta_prompt.md
  - domain-presentations/powerpoint_board_deck.md
---

# Investment Bet Matrix Slide Visual

## Prompt

```text
Create a SINGLE FLAT PRINT ARTWORK image for an executive board deck: **investment bet matrix**.

IMPORTANT REAL-WORLD CONTEXT:
- This is a static visual for a board meeting slide, not a software interface.
- It will be displayed full-screen in a 16:9 board presentation and exported to PDF.
- It must optimize fast executive scanning and analytical clarity.
- This is NOT a UI dashboard, NOT an app mockup, NOT a product screenshot, NOT a 3D render.

CRITICAL OUTPUT RULES (NON-NEGOTIABLE):
- Output EXACTLY ONE image.
- Aspect ratio MUST be 16:9 landscape.
- Canvas size: 1920 x 1080 px at 150 DPI.
- Edge-to-edge slide artwork; no external scene/background.
- NO gradients, NO shadows, NO bevels, NO glow, NO glassmorphism.
- Sharp rectangular geometry only; avoid rounded-card UI styling.
- Solid-color fills only.

LAYOUT STRUCTURE (GRID FORCING + ENUMERATED SLOTS):
- EXACTLY 3 horizontal zones.
- ZONE 1 (top, 18% height): Title bar + one-line executive takeaway.
- ZONE 2 (middle, 64% height): Main analytic visual for investment bet matrix.
- ZONE 3 (bottom, 18% height): Key actions, risks, and decision notes.
- Keep consistent alignment, equal spacing, and clear visual hierarchy.

ALLOWED vs FORBIDDEN:
- ALLOWED: clean chart geometry, labeled axes, matrix cells, heatmap blocks, callout chips, simple icons.
- FORBIDDEN: browser chrome, side navigation, buttons, toggles, input fields, table spreadsheet chrome, watermark logos.

STYLE SYSTEM:
- Background: #F8FAFC
- Primary: #0F172A
- Secondary: #1D4ED8
- Accent: #DC2626
- Success: #059669
- Warning: #D97706
- Neutral dividers: #CBD5E1
- Typography: modern sans-serif, strong contrast, short labels, no decorative fonts.

CONTENT GUIDANCE:
- Include realistic business placeholders (segments, quarters, owners, targets, variances).
- Prioritize legibility and executive narrative over decoration.
- Keep density suitable for a single board slide read in under 20 seconds.

FINAL VALIDATION CHECKLIST:
1) Exactly one image, exactly 16:9 (1920x1080).
2) Clear board-slide visual for investment bet matrix, not generic art.
3) Flat artwork only: no gradient, shadow, lighting, depth, or mockup stage.
4) No UI/dashboard chrome, app widgets, or product frame.
5) Enumerated 3-zone layout is visibly respected.
6) Labels and values are legible at presentation distance.
7) Executive takeaway and decision cues are present.
8) Output is board-ready and PDF-export friendly.

If any gradient, drop shadow, rounded-corner card UI, or software screenshot style appears, the output is incorrect.
```

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Let bets land in quadrants by the model's sense of "high return" rather than the coordinates the user scored.
- Scale bubbles by radius: a bet with twice the investment drawn with twice the radius shows four times the area.
- Let the model invent bet names, dollar allocations or expected-return figures, or add a bet so each quadrant has one.
- Trust a total-allocation callout without checking it against the bubbles and the stated budget envelope.

✅ **DO:**
- Place each bet from its intake scores against the stated axis midpoints, and re-check every bet within a tenth of a boundary.
- Sum the displayed allocations and compare them with the total callout and the budget envelope.
- Pick two bubbles and check their area ratio equals their investment ratio.
- Count bubbles against the intake; an unscored bet goes in Zone 3 as "[unscored]", not on the matrix.
