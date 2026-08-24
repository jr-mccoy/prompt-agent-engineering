---
name: genre_consistency_check
description: "Run when a story draft must be checked for adherence to genre expectations and conventions."
version: "1.0.0"
category: creative
tags: [consistency, creative, genre]
agents_used: []
---
# Genre Consistency Check

## Trigger phrase
Run when a story draft must be checked for adherence to genre expectations and conventions.

## Required inputs
- Draft excerpt or full narrative.
- Target genre/subgenre and comparable works.
- Intended audience and tonal boundaries.

## Output schema
- `consistency_assessment`: overall fit to genre conventions with confidence level.
- `convention_alignment_table`: key conventions marked as present, subverted, or missing.
- `revision_suggestions`: prioritized edits to strengthen intentional genre coherence.

## Validation checklist
- [ ] Assessment distinguishes intentional subversion from accidental inconsistency.
- [ ] Core genre promises (tone, stakes, pacing cues) are evaluated explicitly.
- [ ] Suggestions preserve author intent while improving genre readability.
- [ ] Audience suitability is considered in recommendations.
