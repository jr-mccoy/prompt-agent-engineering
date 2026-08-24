---
title: "Scientific Poster Designer"
category: science/writing-communication
description: "Design the content and layout spec for a three-zone, billboard-style academic poster with a question→method→result→so-what scan path, then hand the visual rendering off to the image-generation domain."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-01
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - scientific-poster
  - better-poster
  - three-zone-layout
  - scan-path
  - figure-led
  - accessibility
  - qr-handoff
  - image-gen-handoff
updated: "2026-06-26"
related_prompts:
  - domain-science/writing-communication/science_conference_abstract_drafter.md
  - domain-science/writing-communication/science_preprint_release_plan.md
---

# Scientific Poster Designer

**Objective:** Produce the CONTENT and LAYOUT specification for an academic poster built on a three-zone scan path: a top billboard zone carrying the single big finding, and a left-to-right body that walks question → method → result → so-what. The spec enforces a strict per-zone word budget, a figure-led (not text-wall) approach, a QR/handle link to the paper and data, and print-scale accessibility. This prompt produces the spec only — the rendered poster art is handed off to `domain-image-generation/`.

**When to use:** You have a finding and a target poster session, and you need a content map plus a layout schematic before you build the visual (or before you brief an image-generation prompt to render it).

**Required inputs:**
- **Discipline.** Field and subfield (steers terminology, what figure type carries the result, audience expectations).
- **Finding / work context.** The user-supplied question, method, headline result with direction and magnitude, and the so-what. Never invented.
- **Target venue or audience.** Conference/session, poster size and orientation, viewing distance, and whether the audience is specialist or mixed.
- **Print dimensions and orientation.** `[user-supplied]` — e.g., A0 portrait, 48×36 in landscape; needed to set font sizes at print scale.

**Optional inputs:**
- Figure assets already available (plots, schematics, photos) and which one is the hero figure.
- Paper status and links: preprint DOI, repository/data DOI, OSF/registration link (for the QR target).
- Branding constraints (institution template, required logos, color palette).
- Accessibility requirements (color-vision-deficiency palette, large-print rules).
- A short take-home sentence the user wants as the billboard headline.

**Constraints — Must:**
- Open with discipline, finding context, and target venue/dimensions before designing.
- Enforce the three-zone scan path: Zone 1 (top) = one billboard finding; Zone 2 (body, left→right) = question → method → result → so-what; Zone 3 = QR/handle + references + contact + funding.
- Apply a strict per-zone word budget and report the word count per zone against its cap.
- Be figure-led: the result is carried by a hero figure, not a paragraph; text supports the figure.
- Specify print-scale accessibility: minimum font sizes at the stated dimensions, color-blind-safe palette, and adequate contrast.
- Provide the QR/handle target as a real user-supplied link or mark it `[user-supplied]`.
- Use calibrated language; preserve confirmatory-vs-exploratory honesty; surface data/code availability.
- Hand off rendering explicitly to `domain-image-generation/` and name it; do not attempt to render or describe final pixel art here.

**Constraints — Must Not:**
- Do not invent results, citations, DOIs, conference requirements, or server policies. Draft only from user-supplied content; mark gaps `[user-supplied]` / "verify on the venue/server site".
- Do not produce a text-wall poster (dense multi-paragraph methods/results blocks).
- Do not use "novel", "groundbreaking", "first-ever", "unprecedented", or "paradigm-shifting" in the billboard or body text.
- Do not render the visual or output an image prompt as if it were the deliverable; the deliverable is the content + layout spec plus a named hand-off.
- Do not specify font sizes in the abstract; tie them to the user-supplied print dimensions.

**Instructions:**

1. **Confirm the frame.** Restate discipline, finding context, target venue, and print dimensions/orientation (flag `[user-supplied]` if missing).
2. **Write the billboard.** Draft the single big-finding headline for Zone 1 — one plain-language sentence a viewer reads from 3 metres. De-hype it. Offer 2–3 phrasings.
3. **Pick the hero figure.** Identify the one figure that carries the result; if none exists, specify what figure must be made (chart type, axes, what it shows). State that the result lives in this figure, not in prose.
4. **Map the body scan path.** For Zone 2, draft tight blocks left→right: Question (1 line), Method (a labeled schematic or ≤2 lines), Result (the hero figure + a one-line readout), So-what (1–2 lines of implication + one honest limitation/scope boundary).
5. **Apply the word budget.** Assign and enforce a per-zone cap (e.g., billboard ≤15 words; each body block ≤25–40 words). Count words per zone and report against the cap. Cut to fit.
6. **Design Zone 3 (margins/footer).** Specify QR code target(s) — paper preprint DOI, data/code repository — plus author handle/contact, key references (user-supplied), and funding/acknowledgment line.
7. **Set accessibility at print scale.** Given the dimensions, specify minimum title/body/caption font sizes, a color-vision-deficiency-safe palette, and contrast guidance; note reading-distance assumptions.
8. **Emit the layout schematic.** Produce a text-based grid showing zone placement, relative sizes, and the scan path arrows.
9. **Hand off to image generation.** State explicitly that the rendered poster is produced by `domain-image-generation/` (point the user there for the render brief), and pass the structured spec as the input to that hand-off. Do not render here.

**Output format (locked):**

```
## Frame
- Discipline | Venue/session | Dimensions + orientation [user-supplied] | Viewing distance | Audience

## Zone 1 — Billboard (cap: N words)
- Headline (chosen): "..."  (count: X / N)
- Alternates: "..." | "..."

## Zone 2 — Body scan path (left → right)
- Question (cap: N): "..."  (count: X / N)
- Method (schematic + cap: N): "..."  (count: X / N)
- Result (HERO FIGURE: <type/what it shows> + one-line readout, cap: N): "..."  (count: X / N)
- So-what (cap: N, includes one limitation/scope note): "..."  (count: X / N)

## Zone 3 — Margins / footer
- QR target(s): [paper DOI / data-code DOI — user-supplied]
- Author handle / contact: [user-supplied]
- References: [user-supplied]
- Funding / acknowledgment: [user-supplied]

## Accessibility (at stated print scale)
- Min font sizes: title / body / caption (tied to dimensions)
- Palette: color-blind-safe note | Contrast note | Reading-distance assumption

## Layout schematic (text grid)
[ASCII grid showing the three zones, relative sizes, and scan-path arrows]

## Hand-off
- Render this spec via domain-image-generation/ (see that domain's poster/visualization prompts). This prompt delivers the spec, not the rendered art.

## Open-science surfacing
- Data availability: [user-supplied] | Code availability: [user-supplied] | Exploratory vs confirmatory: [user-supplied]

## Flags & gaps
- [items marked user-supplied or verify-on-site]
```

**Reporting-standard / convention alignment:** Billboard / #betterposter three-zone design conventions; figure-led scientific communication; accessibility guidance (color-vision-deficiency-safe palettes, print-scale legibility, contrast). Visual rendering is delegated to `domain-image-generation/`.

**Verification checklist (before delivering):**
- [ ] Discipline, finding context, and target venue/dimensions were captured before designing.
- [ ] Zone 1 carries one de-hyped big finding within its word cap.
- [ ] The result is carried by a hero figure, not a text block.
- [ ] Each zone reports its word count against its cap; nothing is a text wall.
- [ ] Print-scale font sizes are tied to the user-supplied dimensions (not abstract).
- [ ] Palette/contrast accessibility is specified.
- [ ] QR/handle targets are real user-supplied links or flagged `[user-supplied]`.
- [ ] Rendering is explicitly handed off to `domain-image-generation/`; no art is rendered here.
- [ ] No banned hype terms; confirmatory/exploratory status and data/code availability surfaced.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Text-wall poster | Dense, "complete" methods/results paragraphs feel thorough | Enforce per-zone word caps; require a figure-led result |
| Buried finding | A balanced layout with no dominant takeaway | Mandate Zone 1 billboard as the single big finding |
| Font set in the abstract | "Large, readable fonts" with no numbers | Tie min font sizes to user-supplied print dimensions |
| Inaccessible palette | A vivid red/green chart that looks striking | Require color-vision-deficiency-safe palette + contrast check |
| Rendering overreach | A detailed pixel-level art description treated as the deliverable | Deliver spec + named hand-off to domain-image-generation/ only |
| Dead QR link | A QR target that points to a paper/data that isn't posted yet | Use user-supplied links only; flag unposted targets `[user-supplied]` |
| Hype headline | "Groundbreaking first-ever result" as the billboard | Ban hype terms; calibrate to the actual finding |
