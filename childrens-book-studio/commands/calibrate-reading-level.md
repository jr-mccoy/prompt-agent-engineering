---
name: calibrate-reading-level
description: Surgically retarget a children's-book draft to a specific age band / reading level (Lexile, Guided Reading, Flesch-Kincaid) without flattening voice. A focused entry point to the reading-level calibrator.
---

# /calibrate-reading-level

Retarget a draft's reading level to a precise age band, surgically (no full pipeline).

**Action:** Load and follow `domain-childrens-writing/craft-tools/childrens_age_reading_level_calibrator.md`. First confirm the target age band and level metric (Lexile / Guided Reading / Flesch-Kincaid / AR-ATOS). Then:

1. Measure the draft's current level against the target.
2. Adjust vocabulary, sentence length, syntax, and concept load toward the band.
3. **Preserve voice, depth, and emotional truth** — simplify language, not meaning (the "respect the reader" convention).

**Guardrail:** this is Stage 4's reading-level item only. It does not run the full craft gate. If the draft also has agency/preaching/structure issues, route back to `/revise-manuscript`.

**Ends when** the draft sits in the target band and the voice is intact.
