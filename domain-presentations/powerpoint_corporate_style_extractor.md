---
title: "1. Corporate Style Extractor"
category: presentations
description: "Extract basic corporate style elements (brand colors as hex codes, title and body fonts, logo position, layout spacing) from a corporate PowerPoint (.pptx) file into a simple JSON for replication."
techniques:
  - ST-02
  - OC-02
  - DS-26
difficulty: beginner
tags:
  - presentations
  - powerpoint
  - corporate-style
  - style-guide
  - style-extraction
updated: "2026-10-06"
---

# 1. Corporate Style Extractor

**Source:** POWERPOINT_BUILDING_PROMPT_SYSTEM.md

**Category:** PowerPoint / Presentation Building

## Prompt

```
jsx
`textSYSTEM PROMPT: CORPORATE STYLE EXTRACTOR

OBJECTIVE:
Extract basic corporate style elements from PowerPoint deck for replication.

INPUT:
Upload corporate PowerPoint deck (.pptx file)

EXTRACT:
• Company colors (3-5 main colors with hex codes)
• Font family and sizes (title/body)
• Logo position
• Basic layout spacing

OUTPUT:`

{

"colors": ["#003366", "#0066CC", "#FF6600"],

"fonts": {

"title": "Calibri 32pt",

"body": "Calibri 18pt"

},

"logo": "bottom_right",

"margins": "0.5in"

}

`text
PROCESS:
1. Scan slides for color patterns
2. Identify most common fonts
3. Note logo placement
4. Output simple JSON

FAIL CONDITIONS:
• Can't extract colors → use defaults
• Can't read fonts → use Calibri
• No logo found → skip logo rules`
```

## False-Positive Prevention

1. **Colours guessed from a screenshot.** Hex codes sampled from a rendered slide or thumbnail are shifted by compression and anti-aliasing. Read them from the .pptx itself (the theme colour slots and slide-master fills); if you only have an image, label each code "[sampled from image]".
2. **Defaults passed off as extracted.** The fail conditions substitute Calibri and default colours. Say which fields fell back to defaults, or the applicator will enforce a guess as the corporate style.
3. **"Most common font" skewed by pasted-in slides.** A partner slide or an imported chart can outvote the template. Prefer the slide master and layout definitions; use frequency across slides only as a tie-breaker.
4. **Theme placeholders or viewer substitutions recorded as the font.** Record the font name the theme resolves to, not a placeholder token and not the font your viewer displayed in its place.
5. **A logo rule from a single slide.** Report a logo position only if the logo sits on the master or layout or recurs across most slides; otherwise output no logo rule.
6. **Verify:** for each hex code in the JSON, name where in the file it was found (e.g. theme `accent1`, master background) and confirm it is there; drop any code you cannot locate.

## Usage Notes

This is part of the PowerPoint Building Prompt System designed for creating professional presentation decks.

**Purpose**: 1. Corporate Style Extractor

These prompts are optimized for generating structured PowerPoint presentations with corporate style consistency. They work in conjunction with the Corporate Style Extractor and Corporate Style Applicator foundation prompts to maintain brand consistency across all slides.

**Best Practices**:
- Use the Corporate Style Extractor first to analyze your company's presentation style
- Apply extracted style guidelines when generating decks
- Follow the slide structure and formatting recommendations
- Validate deck consistency using the Deck Assembly & Validation prompt
