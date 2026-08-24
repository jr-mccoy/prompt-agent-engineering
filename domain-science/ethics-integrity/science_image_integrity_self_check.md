---
title: "Image Integrity Self-Check"
category: science/ethics-integrity
description: "A pre-submission, per-figure self-audit of scientific images (Western blots, gels, micrographs, flow plots) against community image-integrity norms — separating allowed linear whole-image adjustments from forbidden splicing, cloning, selective local edits, and panel duplication, and confirming raw-image retention."
techniques:
  - ST-01
  - RT-01
  - CM-02
  - QA-01
  - QA-02
  - ST-03
difficulty: advanced
tags:
  - image-integrity
  - western-blot
  - gel-electrophoresis
  - microscopy
  - figure-manipulation
  - research-integrity
  - data-presentation
  - publication-ethics
updated: "2026-06-26"
related_prompts:
  - domain-science/ethics-integrity/science_misconduct_self_audit.md
  - domain-science/ethics-integrity/science_retraction_or_correction_decision_walkthrough.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
---

# Image Integrity Self-Check

**Objective:** Run a pre-submission, per-figure audit of scientific image data against accepted image-integrity norms. For each figure it records the adjustments the author actually made, classifies them as allowed or forbidden, identifies what must be disclosed, confirms where the raw/original images are retained, and runs a duplication self-scan across panels, figures, and prior papers. It structures the self-check and routes suspected problems to the correction process; it does not certify any image as clean and never asserts what an image shows.

**When to use:** Before submitting or revising any manuscript, preprint, or report containing blots, gels, micrographs, or cytometry plots — and again whenever a figure is reassembled or a panel is reused.

**Required inputs:**
- **Discipline.** <field; sets relevant conventions, e.g., molecular biology, pathology, cell biology>
- **Study / manuscript context.** <working title, figure list, target venue if known; user-supplied, never invented>
- **Per-figure adjustment account.** <for each figure/panel: image type, what processing was applied, and whether lanes/panels were combined, in the user's own words; `[user-supplied]` for anything not stated>

**Optional inputs:**
- Target venue's image/figure policy text (if known).
- Raw-image and original-blot storage location and retention status.
- Software used for figure assembly.
- Whether any panel is reused from a prior publication or another figure.

**Constraints — Must:**
- Apply community image norms: **allowed** = linear, whole-image brightness/contrast/level adjustments applied to the entire image and disclosed; cropping that does not mislead; clearly delineated lane splicing with a visible divider line and a methods note.
- Mark as **forbidden**: splicing lanes/bands without a visible divider, cloning or erasing features, adding or deleting bands, selective/local adjustment of part of an image, nonlinear "beautification," and duplicating panels across figures or papers as if they were different data.
- Require a raw-image retention check and original-blot/full-uncropped-membrane availability for each blot/gel.
- Run a duplication self-scan: within-figure, across-figures, and against the user's prior outputs (from user-supplied information only).
- State explicitly when a stated adjustment crosses from allowed into needing-disclosure or forbidden, and cite image norms generically (e.g., journal/EMBO figure guidelines; the Rossner–Yamada principles on what is and isn't acceptable image manipulation).

**Constraints — Must Not:**
- Do not invent facts, results, image data, institutional/journal policies, or biosecurity determinations. Work only from user-supplied content; mark gaps `[user-supplied]`.
- This prompt organizes/structures/flags only; it does not give a final biosecurity, legal, or editorial determination, and does not replace the IBC / institutional biosafety / DURC committee / journal editor / COPE process. Route formal decisions there.
- Do not assert what any image depicts, whether a band is "real," or whether manipulation occurred — assess only the processing the user describes.
- Do not declare a figure clean or compliant; flag and route instead.
- Do not use "novel," "groundbreaking," or "first-ever" in any drafted text.

**Instructions:**

1. **Confirm scope.** Restate discipline, the figure list, and venue. For each figure, mark any missing adjustment detail `[user-supplied]`.
2. **Catalog per-figure processing.** For each figure/panel, record image type and the exact adjustments the user reports — globally vs. locally applied, linear vs. nonlinear, and any lane/panel combination.
3. **Classify each adjustment.** Assign allowed / allowed-but-must-disclose / forbidden using the norms above. Tie each classification to the specific stated action.
4. **Check disclosure obligations.** For allowed-but-disclose items (splicing with divider, cropping, contrast changes), draft the methods-section disclosure line.
5. **Run the raw-data retention check.** For each blot/gel, confirm original uncropped membrane/raw file availability and storage location; flag any figure lacking a retained original.
6. **Duplication self-scan (adversarial).** Compare panels within the figure, across figures, and against prior outputs the user names; flag any reuse or overlap to verify, in neutral language.
7. **Triage flags.** For any forbidden action or unresolved duplication in already-published work, route to the retraction-or-correction walkthrough; for in-preparation work, specify the fix (re-image, re-assemble with dividers, restore from raw, disclose).
8. **Assemble deliverables.** Produce the per-figure audit table, the disclosure lines, the retention status, and the duplication-scan result.
9. **Self-check.** Confirm nothing about image content was asserted, no policy invented, and every gap is `[user-supplied]`.

**Output format (locked):**

```
## Scope Confirmation
[discipline, figure list, venue; gaps flagged]

## Per-Figure Image Audit
| Figure/Panel | Image type | Adjustments made (as stated) | Global+linear? | Lane/panel combined? | Allowed? (Yes / Disclose / Forbidden) | Disclosure needed | Raw/original location |

## Disclosure Lines (for allowed-but-disclose items)
- Fig X: [methods-section disclosure draft]
...

## Raw-Data Retention Check
[per blot/gel: original uncropped image available? storage location? gaps flagged]

## Duplication Self-Scan
[within-figure / across-figures / vs. prior outputs — items to verify, neutral framing; or "none indicated by inputs"]

## Flag Triage & Routing
- [forbidden/unresolved item] → in-prep fix OR route to retraction/correction walkthrough
...

## Open Items
- [ ] [user-supplied gap]
```

**Standard alignment:** Community image-integrity norms including journal/EMBO figure-preparation guidelines and the Rossner–Yamada principles (linear whole-image adjustments only; no splicing without disclosure; no cloning/erasing/selective adjustment; retain originals); COPE guidance on image manipulation; venue-specific figure and raw-data retention policies (verify against the target venue).

**Verification checklist (before delivering):**
- [ ] Discipline and study/manuscript context captured before auditing.
- [ ] Each figure's adjustments classified as allowed / disclose / forbidden against named norms.
- [ ] Only the user's stated processing assessed; no claim made about image content.
- [ ] Lane splicing checked for a visible divider and a disclosure note.
- [ ] Raw/original uncropped image availability confirmed per blot/gel.
- [ ] Duplication scan run within-figure, across-figures, and vs. prior outputs.
- [ ] Disclosure lines drafted for allowed-but-disclose adjustments.
- [ ] Forbidden/published-work flags routed to the correction/retraction walkthrough.
- [ ] No image data or policy invented; gaps marked `[user-supplied]`; drafted text free of "novel/groundbreaking/first-ever."

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Beautification creep | Treating a "cleaner" panel as a harmless tidy-up | Local/nonlinear edits are forbidden regardless of intent |
| Invisible splice | Combining lanes that "came from the same gel" without a divider | Require a visible divider line plus a methods disclosure |
| Content claim | Stating what a band or cell "is" | Assess processing only; never assert image content |
| Lost original | Assuming raw data exists because the figure looks fine | Require confirmed retention/location per blot/gel |
| Innocent duplicate | Reusing a representative image across papers silently | Flag any reuse/overlap to verify and disclose |
