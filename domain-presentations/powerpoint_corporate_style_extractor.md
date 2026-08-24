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

## Usage Notes

This is part of the PowerPoint Building Prompt System designed for creating professional presentation decks.

**Purpose**: 1. Corporate Style Extractor

These prompts are optimized for generating structured PowerPoint presentations with corporate style consistency. They work in conjunction with the Corporate Style Extractor and Corporate Style Applicator foundation prompts to maintain brand consistency across all slides.

**Best Practices**:
- Use the Corporate Style Extractor first to analyze your company's presentation style
- Apply extracted style guidelines when generating decks
- Follow the slide structure and formatting recommendations
- Validate deck consistency using the Deck Assembly & Validation prompt
