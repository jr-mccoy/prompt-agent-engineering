---
title: "3. Enterprise Deck Architect"
category: presentations
description: "Plan the structure and chunking strategy for a multi-source data presentation: the one-sentence story, total slide count, chunk boundaries for separate generation, and the key data each chunk needs."
techniques:
  - DT-01
  - DS-19
  - ST-03
difficulty: intermediate
tags:
  - presentations
  - powerpoint
  - deck-planning
  - chunking
  - multi-source-synthesis
updated: "2026-10-06"
---

# 3. Enterprise Deck Architect

**Source:** POWERPOINT_BUILDING_PROMPT_SYSTEM.md

**Category:** PowerPoint / Presentation Building

## Prompt

```
jsx
textSYSTEM PROMPT: ENTERPRISE DECK ARCHITECT

OBJECTIVE:
Plan multi-source data presentation structure and chunking strategy.

INPUT:
• Data files (Excel, documents, emails)
• Audience (Board/Executive/Team)
• Topic focus

ANALYZE:
• What story does data tell?
• What decisions need approval?
• How many slides needed?
• How to chunk for separate generation?

OUTPUT:
**DECK PLAN:**
- Total slides: [X]
- Audience: [Board/Executive]
- Story: [One sentence summary]

**CHUNKS:**
- Chunk A (Slides 1-5): Executive Summary
- Chunk B (Slides 6-12): Financial Deep Dive  
- Chunk C (Slides 13-18): Market Analysis
- Chunk D (Slides 19-24): Recommendations

**KEY DATA:**
- Financial: [Source files and key metrics]
- Operational: [KPIs needed]
- Strategic: [Decision framework]

**NEXT STEPS:**
Use chunk prompts in separate chats with this plan.

KEEP IT SIMPLE:
Focus on story and structure only. No complex validation.
```

## False-Positive Prevention

1. **A story sentence the data cannot carry.** The one-line Story must be something the supplied files already show, not the conclusion the requester hopes for. Name the file and metric that carries it.
2. **Example chunks copied as the plan.** Executive Summary / Financial Deep Dive / Market Analysis / Recommendations is an illustration. A Market Analysis chunk planned for inputs with no market data is a chunk with nothing to fill it.
3. **KEY DATA listing metrics no file contains.** Give each metric its source file (and sheet or tab); a metric the story needs but no input holds is listed as a gap, not as available.
4. **Shared totals computed separately in each chat.** Chunks generated in separate chats will compute the same figure differently. Assign each shared figure to one owning chunk in the plan so the others quote it.
5. **Decisions invented to give the audience something to approve.** "What decisions need approval?" is answered from the agenda, memo, or emails supplied; if none are stated, say so.
6. **Verify:** check that the chunk slide ranges cover 1 to the Total with no gaps or overlaps, and that every input file is mapped to at least one chunk or explicitly marked unused.

## Usage Notes

This is part of the PowerPoint Building Prompt System designed for creating professional presentation decks.

**Purpose**: 3. Enterprise Deck Architect

These prompts are optimized for generating structured PowerPoint presentations with corporate style consistency. They work in conjunction with the Corporate Style Extractor and Corporate Style Applicator foundation prompts to maintain brand consistency across all slides.

**Best Practices**:
- Use the Corporate Style Extractor first to analyze your company's presentation style
- Apply extracted style guidelines when generating decks
- Follow the slide structure and formatting recommendations
- Validate deck consistency using the Deck Assembly & Validation prompt
