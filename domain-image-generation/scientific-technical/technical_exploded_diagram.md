---
title: "Technical Exploded / Assembly Diagram with Numbered Callouts"
category: image-generation/scientific-technical
description: "Generate an exploded-view or assembly diagram of a product or mechanism, with components separated along assembly axes and numbered callouts — plus an accuracy/verification protocol for parts and fit."
techniques:
  - ST-01
  - ST-02
  - SV-12
  - SV-13
difficulty: advanced
tags:
  - technical-diagram
  - exploded-view
  - assembly
  - numbered-callouts
  - accuracy
  - gpt-image-2
  - nano-banana
updated: "2026-06-23"
related_prompts:
  - domain-image-generation/scientific-technical/scientific_illustration.md
  - domain-image-generation/scientific-technical/data_visualization_chart_image.md
  - domain-image-generation/IMAGE_MODEL_SELECTION_GUIDE.md
  - domain-image-generation/nano-banana/nanobana_product_multi_angle_composite.md
---

# Technical Exploded / Assembly Diagram with Numbered Callouts

**Objective:** Produce an **exploded-view** or **assembly diagram** of a product or mechanism — components separated and spaced along their assembly axes, connected by alignment/leader lines, with **numbered callouts** keyed to a parts list. Use case: instruction manuals, spec sheets, patent-style figures, repair guides, product marketing cutaways.

> ## ⚠️ Accuracy & Verification Protocol (read first)
> Image models produce **plausible-looking but mechanically wrong** assemblies: invented parts, impossible fits, wrong fastener counts, parts that could never align on the shown axis. They also **hallucinate callout numbers and label text**.
>
> Mandatory practice:
> 1. **Supply the exact parts list and assembly order** in the prompt — enumerate every component, its position in the stack, and how it connects. Do not let the model design the mechanism.
> 2. **Add the numbered key/labels in post** when accuracy matters; treat model-rendered numbers/text as unreliable.
> 3. **An engineer / the actual product spec must verify** part identity, count, orientation, and fit before any manual, repair, or spec-sheet use.
> 4. For real assemblies, prefer a CAD-derived exploded view; use this as a **concept/illustration draft**, not an authoritative assembly reference.

**Why model choice matters:** **gpt-image-2** handles clean technical line-art layouts and labeled figures well — strong first choice for the exploded layout. **Nano Banana 2** can take **multiple reference photos of the real product** (10 object slots) so the depicted parts resemble the actual components, which materially reduces invented geometry; **Nano Banana Pro** adds text precision and search grounding.

**API parameters:**
- gpt-image-2 path: `model="gpt-image-2"`, `/v1/images/generations` (or `/v1/images/edits` with product photos), `quality="high"`, `n=1`
- Nano Banana path: `model="gemini-3.1-flash-image"` (NB2 — object slots for real-part references) or `"gemini-3-pro-image"` (Pro); `quality="high"`

---

## Inputs

- `[PRODUCT/MECHANISM]` — what is being exploded (e.g., "a three-part desk lamp head," "a ballpoint pen")
- `[PARTS LIST]` — every component, in assembly order, with the correct count of each
- `[ASSEMBLY AXIS]` — the axis/axes parts separate along (e.g., "vertical stack," "left-to-right along the shaft")
- `[FIT RELATIONSHIPS]` — how parts connect (threads into, snaps onto, slides over)
- `[REFERENCE PHOTOS]` — optional photos of the real parts (Nano Banana object slots / gpt-image-2 refs)
- `[VIEW ANGLE]` — isometric / three-quarter / orthographic
- `[STYLE]` — clean line-art / shaded CAD-render / blueprint
- `[CALLOUT SPEC]` — numbered callouts in a margin key (preferred)

---

## Constraints (Must / Must Not)

**Must:**
- Separate parts cleanly along the `[ASSEMBLY AXIS]` with **alignment/leader lines** showing how they reassemble.
- Depict **exactly the components in `[PARTS LIST]`**, in the correct count and order — nothing invented.
- Prefer **numbered callout placeholders** keyed to a margin parts list; add the verified key in post.
- Show parts in the correct **orientation and fit** per `[FIT RELATIONSHIPS]`.
- Use a clean neutral background and a consistent `[VIEW ANGLE]`.

**Must Not:**
- Invent parts, fasteners, or connections not in the list.
- Show fits that are mechanically impossible on the stated axis.
- Rely on model-rendered numbers/text for the parts key.
- Add decorative components that read as real parts.

---

## Production Prompt — gpt-image-2 path

```
SCENE:
An exploded-view technical diagram of [PRODUCT/MECHANISM], [VIEW ANGLE] (e.g., isometric). Clean neutral/white background, even lighting. Style: [STYLE — e.g., clean line-art with light shading].

COMPONENTS (depict EXACTLY these, in this assembly order, in these counts — invent nothing):
[PARTS LIST — number each: 1) [part] ×[count]; 2) [part] ×[count]; ...]

EXPLOSION:
- Separate the components along the [ASSEMBLY AXIS], evenly spaced, in assembly order.
- Draw thin dashed alignment/leader lines connecting each part to its neighbor, showing how they reassemble.
- Respect fits: [FIT RELATIONSHIPS — e.g., "the cap (1) threads onto the barrel (2); the spring (3) sits inside the barrel"].

CALLOUTS:
- Place a numbered callout marker (1, 2, 3, …) next to each separated part, matching the COMPONENTS numbering.
- Do NOT render descriptive part names inside the figure — numbered markers only. (A verified parts key is added in post.)

USE CASE:
An UNVERIFIED draft exploded diagram for [manual / spec sheet / repair guide]. An engineer will verify parts, counts, orientation, and fit before use.

CONSTRAINTS:
- Depict only the listed components in correct count/order; invent no parts or fasteners.
- Mechanically plausible fit along the stated axis; no impossible alignments.
- Numbered callouts, not rendered names.
- Clean neutral background, consistent [VIEW ANGLE].
- Format: [size], quality="high".

If the diagram invents parts, shows impossible fits, or renders unreliable text, it is incorrect.
```

---

## Production Prompt — Nano Banana path (reference real parts)

```
TASK: Create an exploded-view assembly diagram of [PRODUCT/MECHANISM], [VIEW ANGLE], clean [STYLE], neutral background.

REFERENCES (Object slots): photos of the real components.
- Obj 1–N: [REFERENCE PHOTOS] of each part. TAKE: the true shape/proportions of each component. IGNORE: photo backgrounds and lighting.

COMPONENTS (depict EXACTLY these, in this order/count — invent nothing):
[PARTS LIST, numbered]

EXPLOSION: separate parts along [ASSEMBLY AXIS], evenly spaced, with dashed alignment/leader lines. Respect fits: [FIT RELATIONSHIPS].

CALLOUTS: numbered markers per part matching the COMPONENTS numbering. Add the verified parts key in post (do not rely on rendered text).

CONSTRAINTS:
- MUST: match the referenced real parts; correct count/order; plausible fit; numbered callouts.
- MUST NOT: invent parts; show impossible fits; rely on rendered text for the key.
- Quality: "high".

This is an UNVERIFIED draft. An engineer must verify parts, counts, orientation, and fit before use.
```

---

## Iteration Plan

1. "The diagram added a [part] not in my parts list — remove it; show only the listed components."
2. "The [part] is shown on the wrong axis and couldn't reassemble — re-orient it along the `[ASSEMBLY AXIS]` per the fit relationships."
3. "Fastener count is wrong — show exactly `[count]` of `[fastener]`."
4. "The rendered callout numbers are scrambled — switch to clean numbered markers; I'll add the key in post."
5. "Parts overlap and the explosion is unreadable — increase even spacing along the assembly axis."

---

## Verification

- [ ] Only the listed components are shown, in correct count and assembly order.
- [ ] Parts separated cleanly along the `[ASSEMBLY AXIS]` with alignment/leader lines.
- [ ] Fits are mechanically plausible and match `[FIT RELATIONSHIPS]`.
- [ ] Numbered callouts (preferred) or exact verified text; no scrambled/invented numbers.
- [ ] Clean neutral background; consistent `[VIEW ANGLE]`.
- [ ] **An engineer / the product spec has verified parts, counts, orientation, and fit** before any manual/repair/spec use.
- [ ] Output documented as an AI-generated draft pending CAD/spec confirmation.
