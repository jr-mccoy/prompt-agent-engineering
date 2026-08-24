# GPT Image 2 — Production Prompt Library

**Purpose:** Ready-to-use prompts for OpenAI's `gpt-image-2` (released April 21, 2026). Each prompt applies the patterns documented in [`../GPT_IMAGE_2_GUIDE.md`](../GPT_IMAGE_2_GUIDE.md).

**Audience:** Anyone shipping production images via the OpenAI API or ChatGPT using gpt-image-2.

---

## Prompts in This Directory

### Foundational

| Prompt | What it produces | Key techniques |
|---|---|---|
| [`gptimage2_meta_prompt_builder.md`](gptimage2_meta_prompt_builder.md) | A meta-prompt that converts a one-line brief into a fully-structured gpt-image-2 prompt | 5-section structure, parameter selection, text-rendering contract |

### Generation (Text → Image)

| Prompt | What it produces | Key techniques |
|---|---|---|
| [`gptimage2_photorealistic_portrait.md`](gptimage2_photorealistic_portrait.md) | Editorial-grade candid photorealistic portraits | Photography language, anti-gloss, framing |
| [`gptimage2_product_hero_shot.md`](gptimage2_product_hero_shot.md) | E-commerce product hero with clean contact shadow | Product extraction, label legibility |
| [`gptimage2_logo_batch_variations.md`](gptimage2_logo_batch_variations.md) | 4 logo variations from a brand brief | `n=4` batching, vector-language, wordmark contract |
| [`gptimage2_advertising_creative_brief.md`](gptimage2_advertising_creative_brief.md) | Campaign-grade ad image with verbatim copy | Creative-brief framing, text contract |
| [`gptimage2_dense_text_infographic.md`](gptimage2_dense_text_infographic.md) | Multi-section infographic with verbatim labels | `quality="high"`, web-search grounding, grid forcing |
| [`gptimage2_ui_mockup_specification.md`](gptimage2_ui_mockup_specification.md) | Realistic mobile/web UI mockup | Artifact framing (not concept art), real copy |
| [`gptimage2_in_image_text_marketing.md`](gptimage2_in_image_text_marketing.md) | Marketing visual with 100%-readable verbatim copy | Text rendering contract, typography lock |
| [`gptimage2_executive_slide_artifact.md`](gptimage2_executive_slide_artifact.md) | Single deck slide with title, chart, and footer copy | Artifact specification, landscape lock |

### Editing (Image → Image)

| Prompt | What it produces | Key techniques |
|---|---|---|
| [`gptimage2_surgical_edit_change_preserve.md`](gptimage2_surgical_edit_change_preserve.md) | A general-purpose surgical edit (object removal, replacement, lighting, weather, background) | Change/preserve sentences, "ONLY" discipline, failure condition |

### Multi-Image (References → Composite)

| Prompt | What it produces | Key techniques |
|---|---|---|
| [`gptimage2_multi_reference_composite.md`](gptimage2_multi_reference_composite.md) | A composite drawn from up to 16 indexed references | Reference allocation by role, geometry/lighting matching |
| [`gptimage2_character_consistency_anchor.md`](gptimage2_character_consistency_anchor.md) | A character anchor + reuse template for multi-scene consistency | Anchor-then-reuse pattern, preserve-list discipline |

---

## How to Use This Library

1. **Pick the closest prompt** to your goal.
2. **Open it** and copy the production prompt block.
3. **Fill in the bracketed placeholders** with your specifics.
4. **Set the API parameters** noted at the top of each prompt (`size`, `quality`, `n`).
5. **Iterate** using single-axis follow-ups (see [`../GPT_IMAGE_2_GUIDE.md`](../GPT_IMAGE_2_GUIDE.md) §11).

If your need doesn't match any prompt here, use [`gptimage2_meta_prompt_builder.md`](gptimage2_meta_prompt_builder.md) to generate a structured prompt from your brief.

---

## When NOT to Use gpt-image-2

- **You need explicit `input_fidelity="high"`** — disabled on gpt-image-2; fall back to gpt-image-1.5.
- **You need cheapest-possible bulk variants** — use `gpt-image-1-mini` or `quality="low"`.
- **You need a Markdown-aware structured-prompt model** — Nano Banana Pro is purpose-built for that.
- **You need ControlNet / LoRAs / depth-map composition** — Stable Diffusion / Flux ecosystem.

---

## See Also

- [`../GPT_IMAGE_2_GUIDE.md`](../GPT_IMAGE_2_GUIDE.md) — Comprehensive prompting reference.
- [`../IMAGE_PROMPTING_GUIDE.md`](../IMAGE_PROMPTING_GUIDE.md) — Cross-model image prompting.
- [`../IMAGE_GENERATION_GUIDE.md`](../IMAGE_GENERATION_GUIDE.md) — Print-ready material constraints.
