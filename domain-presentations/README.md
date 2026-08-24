# Domain: Presentations

**Purpose:** Prompts for creating board decks, pitch presentations, investor materials, and visual planning documents.

---

## What This Domain Covers

Presentation creation prompts for executive, board, and corporate presentations (PowerPoint formats).

---

## Directory Structure

```
domain-presentations/
├── (root)                  # PowerPoint generators (board decks, QBRs, launches, crisis, status)
├── board-decks/            # Board-deck image visual prompts (16:9 locked, anti-UI constraints)
├── visual-planning/        # Upstream analytic prompts: capability frontier maps, QA harness, modality routing, cascade effects
└── README.md
```

---

## File Count

| Subdirectory | Count | Description |
|--------------|-------|-------------|
| (root) | ~24 | PowerPoint generators (board decks, QBRs, launches, crisis, status reports, etc.) |
| `board-decks/` | 20 | Board-deck image visual prompts in 16:9 format with anti-UI constraints |
| `visual-planning/` | 4 | Capability frontier mapping, visual QA harness, modality routing, cascade effects scan |
| **Total** | **~48** | |

---

## Key Patterns

### Board Deck Structure
- Executive summary
- Strategic overview
- Financial performance
- Key metrics and KPIs
- Risks and opportunities
- Ask/next steps

### Product Launch / Roadmap
- Market opportunity framing
- Feature set and timeline
- Traction metrics
- Ask / next steps

### Board-Deck Image Visuals (`board-decks/`)
- 16:9 locked outputs (1920 x 1080) for executive slides
- Anti-UI / anti-mockup constraints embedded in prompt body
- Validation checklist in each prompt for pass/fail verification
- Uses 8-technique enforcement from image-generation guide

---

## When to Use This Domain

Use these prompts when you need to:
- Create board meeting presentations
- Develop executive summaries
- Build status / QBR / launch decks
- Generate constraint-locked slide visuals (use `board-decks/`)
- Plan visual communication strategy upstream of slide creation (use `visual-planning/`)

**Do NOT use for:**
- General image generation (use domain-image-generation)
- Business analysis content (use domain-business-strategy)

---

*Migrated from: `prompts/creation/presentations/`*
