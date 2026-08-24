# Tool Spec — reading-level-estimate

## Purpose
Estimate a manuscript's reading level so Stage 4 can check it against the target age band (Gate A's reading-level item).

## Signature
`reading-level-estimate(text, metric) → score`
- `metric`: Flesch-Kincaid grade | Lexile (approx.) | Guided Reading | AR/ATOS.

## Behavior
Read-only computation over the text. Returns the estimated level and the delta from the project's target band. Pairs with `domain-childrens-writing/craft-tools/childrens_age_reading_level_calibrator.md`, which does the actual retargeting.

## Caveats (flag, don't assert)
- Automated readability metrics are **approximations**; they miss concept load, syntax difficulty, and voice. The estimate informs, but does not replace, the craft reviewer's judgment.
- Lexile/Guided-Reading mappings vary; treat cross-metric conversions as rough and flag them.

## Least privilege
Pure read-only computation; no file writes, no network. Never used to "auto-edit" — it measures; the calibrator prompt edits, preserving voice.
