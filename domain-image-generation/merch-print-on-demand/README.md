# Merch & Print-on-Demand Prompts

Production-ready, Tier-1 prompts for print-on-demand merchandise artwork — apparel graphics, die-cut stickers, and seamless repeating patterns. These prompts blend **creative illustration with hard print constraints**: isolated/transparent backgrounds, defined print areas, screen-print color limits, clean die-cut silhouettes, and true edge-to-edge tileability. Where text appears, it routes to a text-rendering model with an EXACT TEXT contract.

**Parent guides:** [IMAGE_MODEL_SELECTION_GUIDE.md](../IMAGE_MODEL_SELECTION_GUIDE.md) · [GPT_IMAGE_2_GUIDE.md](../GPT_IMAGE_2_GUIDE.md) · [NANO_BANANA_GUIDE.md](../NANO_BANANA_GUIDE.md) · [IMAGE_GENERATION_GUIDE.md](../IMAGE_GENERATION_GUIDE.md) (print-ready techniques)

---

## Prompts

| Prompt | Output | Key print constraints |
|--------|--------|----------------------|
| [T-Shirt / Apparel Graphic](tshirt_graphic.md) | Isolated garment graphic | Transparent/solid bg, print area, screen-print color count, garment contrast |
| [Die-Cut Sticker Design](sticker_design.md) | Single sticker + keyline | Transparent bg, bold contour cut line, offsettable silhouette |
| [Seamless Repeating Pattern](print_on_demand_pattern.md) | Tileable square swatch | Edge-continuous repeat, no border, even distribution |

---

## Model routing (why these picks)

| Need | First choice | Why |
|------|-------------|-----|
| Clean subject isolation / transparent background | gpt-image-2 (`background="transparent"`, `quality="high"`) | Native transparent output, crisp isolation, `n=4` pools |
| Text-led merch (slogan tees, word stickers) | Nano Banana Pro (`gemini-3-pro-image`) | Exact font control + near-perfect text |
| Fast motif / candidate exploration | Nano Banana 2 (`gemini-3.1-flash-image`) | Cheap screening before a high-quality production tile/graphic |
| Full-color DTG/sublimation illustration | gpt-image-2 / Nano Banana Pro / Midjourney | Rich color; isolate the subject afterward |

---

## Model ID Quick Reference

| Name | Model ID |
|------|----------|
| GPT Image 2 | `gpt-image-2` |
| Nano Banana | `gemini-2.5-flash-image` |
| Nano Banana Pro | `gemini-3-pro-image` |
| Nano Banana 2 | `gemini-3.1-flash-image` |

---

## Cross-cutting merch conventions

- **Isolate, don't stage.** Apparel and sticker outputs are the *graphic only* — no garment, model, hanger, mockup, scene, or backdrop. Background is transparent or a single flat hex.
- **Defined print area.** Subjects are centered with clean margin and sized to the stated print zone so the POD provider places them correctly.
- **Screen-print color discipline.** For screen-print/vinyl, restrict to the stated flat spot-color count — no gradients, soft shadows, or glows. DTG/sublimation allows full color.
- **Cut-ready silhouettes.** Stickers need a simple, closed, connected outline with a bold, uniform contour keyline that defines the die cut.
- **True seamlessness.** Patterns must be edge-continuous (right↔left, top↔bottom) with no border or centered hero. **Always verify by tiling the swatch 2×2** — model "seamless" output is not guaranteed.
- **No fabricated branding.** No trademarked logos, characters, or marks. Any text renders verbatim from the EXACT TEXT block — no invented copy.

*Print-method behavior reflects common POD practice as of 2026-06-23. Confirm transparent-background support, color-count limits, cut-line/contour requirements, and tile dimensions with your specific POD provider before submitting.*
