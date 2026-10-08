---
title: "2. Corporate Style Applicator"
category: presentations
description: "Apply a corporate style JSON (colors, fonts, logo position, margins) to new PowerPoint generation through the html2pptx workflow, with explicit failure conditions for off-palette colors, undersized fonts, and border boxes."
techniques:
  - CM-02
  - RT-11
  - QA-01
difficulty: beginner
tags:
  - presentations
  - powerpoint
  - corporate-style
  - style-guide
  - brand-consistency
updated: "2026-10-06"
---

# 2. Corporate Style Applicator

**Source:** POWERPOINT_BUILDING_PROMPT_SYSTEM.md

**Category:** PowerPoint / Presentation Building

## Prompt

```
jsx
textSYSTEM PROMPT: CORPORATE STYLE APPLICATOR

OBJECTIVE:
Apply corporate style JSON to new PowerPoint generation.

WORKFLOW REQUIREMENT:
Use html2pptx workflow only. Debug issues, don't switch methods.

INPUT:
• Style guide JSON from extractor
• Content for slides

APPLY:
• Use colors from JSON only
• Apply specified fonts and sizes
• Position logo per JSON rules
• Use margin specifications

CONSTRAINTS:
• NO border boxes or outline shapes
• Min 18pt font, 4.5:1 contrast
• Max 3 bullets per slide
• Bold financial figures

FAILURE CONDITIONS:
• Using colors not in JSON → fail
• Fonts below 16pt → auto-resize
• Border boxes → redesign
• Poor contrast → fix colors

VALIDATION:
Show thumbnail before completion. Verify style compliance.
```

## False-Positive Prevention

1. **Compliance judged from the thumbnail.** A thumbnail can look on-brand while a fill uses a near-miss hex (#0067CC for #0066CC). Compare the colour values written into the slide, not the picture.
2. **Silent font fallback reported as applied.** When the specified font is unavailable, rendering may substitute another. Confirm the font name in the generated file matches the JSON and report any substitution.
3. **Auto-resize landing in the 16–18pt gap.** Shrinking text avoids the "below 16pt" failure yet still breaks the 18pt minimum. Any text set between 16pt and 18pt is a violation to report, not a fix.
4. **Content split to meet the three-bullet cap.** Pushing a fourth bullet onto an unlabelled continuation slide passes the count and breaks the argument; flag content that does not fit instead.
5. **Logo placed by assumption on layouts the JSON never covered.** If the JSON gives one position, note which slide layouts (title, section divider) used it without evidence that the template does.
6. **Verify:** list every colour value used in the output and diff it against the JSON `colors` array; a tint or shade of a brand colour that is not in the array still fails.

## Usage Notes

This is part of the PowerPoint Building Prompt System designed for creating professional presentation decks.

**Purpose**: 2. Corporate Style Applicator

These prompts are optimized for generating structured PowerPoint presentations with corporate style consistency. They work in conjunction with the Corporate Style Extractor and Corporate Style Applicator foundation prompts to maintain brand consistency across all slides.

**Best Practices**:
- Use the Corporate Style Extractor first to analyze your company's presentation style
- Apply extracted style guidelines when generating decks
- Follow the slide structure and formatting recommendations
- Validate deck consistency using the Deck Assembly & Validation prompt
