# Nano Banana Production Prompts

Production-ready prompts for Google's Nano Banana image model family. Each prompt targets a specific Nano Banana differentiator — capabilities where the Nano Banana models outperform or offer unique features compared to other image models.

**Parent guide:** [NANO_BANANA_GUIDE.md](../NANO_BANANA_GUIDE.md)

---

## Prompts

| Prompt | Target Model | Differentiator |
|--------|-------------|----------------|
| [Storyboard → Veo Keyframes](nanobana_storyboard_veo_keyframes.md) | Nano Banana 2 | Official Veo pipeline, 512px screening, cheap-candidate workflow |
| [Search-Grounded Infographic](nanobana_search_grounded_infographic.md) | Nano Banana Pro | Google Search grounding for factual data in images |
| [Multi-Reference Character Scene](nanobana_multi_reference_character_scene.md) | Nano Banana 2 / Pro | 14-ref role-separated allocation for character consistency |
| [JSON Schema Prompt Builder](nanobana_json_schema_prompt_builder.md) | Any Nano Banana | Meta-prompt: converts a creative brief into a reusable JSON schema prompt |
| [Product Multi-Angle Composite](nanobana_product_multi_angle_composite.md) | Nano Banana 2 | 10 object reference slots for multi-angle product composites |

---

## Model ID Quick Reference

| Name | Model ID | Use When |
|------|----------|----------|
| Nano Banana | `gemini-2.5-flash-image` | Budget-sensitive batch work |
| Nano Banana Pro | `gemini-3-pro-image` | Text-heavy, factual, hard compositions |
| Nano Banana 2 | `gemini-3.1-flash-image` | Fast ideation, storyboards, multi-reference |

Preview model IDs (`*-preview`) were deprecated June 25, 2026. Use the stable IDs above.
