# E-commerce Product Photography Prompts

Production-ready prompts for generating **product photography** for online stores and marketplaces — distinct from ad creative (`domain-advertising/`) and print materials (`IMAGE_GENERATION_GUIDE.md`). These cover the standard listing-image set a seller needs: a compliant white-background main image, lifestyle context, styled flat lay, detail macro, and a consistent variant grid.

**Model selection:** [IMAGE_MODEL_SELECTION_GUIDE.md](../IMAGE_MODEL_SELECTION_GUIDE.md) · **Guides:** [GPT_IMAGE_2_GUIDE.md](../GPT_IMAGE_2_GUIDE.md) · [NANO_BANANA_GUIDE.md](../NANO_BANANA_GUIDE.md)

Every prompt provides **both a gpt-image-2 path and a Nano Banana path** — gpt-image-2 for the highest-fidelity hero/main image and on-pack text accuracy, Nano Banana 2 (`gemini-3.1-flash-image`) for cheap 512px screening, fast batch variants, and reference-locked product geometry.

---

## Prompts

| Prompt | What It Produces | Primary Model | Nano Banana Path |
|--------|------------------|---------------|------------------|
| [White Background Catalog Shot](ecommerce_white_background_product.md) | Marketplace-compliant main image on pure #FFFFFF | gpt-image-2 | NB2 for screening + secondary angles |
| [Lifestyle In-Context Shot](ecommerce_lifestyle_in_context.md) | Product in a real-use scene, still the hero | gpt-image-2 | NB2 reference-locked into new scenes |
| [Styled Flat Lay](ecommerce_flat_lay_styled.md) | Top-down styled arrangement with props | gpt-image-2 | NB2 for arrangement screening |
| [Detail Macro / Texture Shot](ecommerce_detail_macro_texture.md) | Macro close-up emphasizing material/texture | gpt-image-2 | NB2 texture-locked to a real sample |
| [Variant Grid](ecommerce_variant_grid.md) | Consistent grid of color/size variants | gpt-image-2 (one-pass grid) | NB2 reference-locked per cell |

---

## Recommended Listing-Image Sequence

A typical marketplace listing uses these in order:

1. **White Background Catalog Shot** — the main image (most marketplaces require pure white).
2. **Detail Macro / Texture Shot** — communicate build quality.
3. **Lifestyle In-Context Shot** — help the buyer imagine ownership.
4. **Styled Flat Lay** — aspirational / category context.
5. **Variant Grid** — show available options at a glance.

---

## Model ID Quick Reference

| Name | Model ID | Use When |
|------|----------|----------|
| gpt-image-2 | `gpt-image-2` | Hero/main image, on-pack text fidelity, one-pass variant grids |
| Nano Banana | `gemini-2.5-flash-image` | Budget-sensitive batch product work |
| Nano Banana Pro | `gemini-3-pro-image` | Hard compositions, dense on-pack text |
| Nano Banana 2 | `gemini-3.1-flash-image` | 512px screening, fast variants, reference-locked geometry |

---

*Marketplace specs (e.g., Amazon's pure-white main-image requirement and ≥1600px-for-zoom rule) change over time — verify current marketplace image policies before production. Model capabilities reflect the market as of 2026-06-23.*
