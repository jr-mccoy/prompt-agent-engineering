# Domain: Presentations

**Purpose:** Prompts for creating board decks, pitch presentations, investor materials, and visual planning documents.

---

## What This Domain Covers

Presentation creation prompts for executive, board, and corporate presentations (PowerPoint formats), plus the narrative and delivery work around them: investor pitch narratives, conference talks, Q&A preparation, and rehearsal (`narrative-delivery/`).

---

## Directory Structure

```
domain-presentations/
├── (root)                  # PowerPoint generators (board decks, QBRs, launches, crisis, status)
├── board-decks/            # Board-deck image visual prompts (16:9 locked, anti-UI constraints)
├── visual-planning/        # Upstream analytic prompts: capability frontier maps, QA harness, modality routing, cascade effects
├── narrative-delivery/     # Pitch and talk narratives, Q&A / hostile-question prep, speaker notes and rehearsal
└── README.md
```

---

## File Count

| Subdirectory | Count | Description |
|--------------|-------|-------------|
| (root) | 14 | PowerPoint generators (board decks, QBRs, launches, crisis, status reports, etc.). Eight duplicate copies were retired in coverage Wave 4 and merged into their clean twins; the old ids resolve as tombstones. |
| `board-decks/` | 20 | Board-deck image visual prompts in 16:9 format with anti-UI constraints |
| `visual-planning/` | 4 | Capability frontier mapping, visual QA harness, modality routing, cascade effects scan |
| `narrative-delivery/` | 4 | Investor pitch narrative, keynote/conference talk arc, Q&A and hostile-question prep, speaker notes and rehearsal coaching |
| **Total** | **~52** | |

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

### Narrative and Delivery (`narrative-delivery/`)
- `presentation_investor_pitch_narrative.md` — fundraising deck spine: thesis, evidence-ranked slide order, claim-plus-proof headlines, objections, milestone-tied ask
- `presentation_keynote_talk_arc.md` — one disputable idea, audience belief shift, structure choice, minute budget at speaking pace
- `presentation_qa_hostile_question_prep.md` — room map, scored question bank (incl. hostile and loaded), honest answers, red lines, hostile rehearsal
- `presentation_speaker_notes_rehearsal_coach.md` — cue-based notes and four scored rehearsal runs with a stop rule
- New files carry full Tier-1 frontmatter; the root `powerpoint_*` generators historically do not

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
- Shape an investor pitch or conference talk, prepare for Q&A, or rehearse delivery (use `narrative-delivery/`)

**Do NOT use for:**
- General image generation (use domain-image-generation)
- Business analysis content (use domain-business-strategy)
- Sales decks for buyers (use `domain-agentic-resources/skills/marketing/sales-enablement/`)
- Routine updates to existing investors (use `domain-professional-writing/domain-specific/domain_writing_founder_investor_update.md`)

---

*Consolidated here from the retired pre-reorg `prompts/creation/presentations/` tree, which no longer exists; the current files are listed above.*
