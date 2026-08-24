# Coloring Book Prompts

Production-ready prompts for generating coloring-book artwork — interior pages, mandalas, themed sets, educational pages, and covers. Every interior prompt enforces the **print-ready line-art constraint family**: pure black outlines on pure white, no grayscale/shading/fills, clean closed line art, age-appropriate line weight, white margins, and a single flat page (never a 3D book mockup). The one exception is the **cover**, which is allowed to use color.

**Parent guide:** [../IMAGE_GENERATION_GUIDE.md](../IMAGE_GENERATION_GUIDE.md) — the 8 core print techniques cited throughout these prompts.

---

## Prompts

| Prompt | Differentiator |
|--------|----------------|
| [Intricate Adult Coloring Page](adult_coloring_page_intricate.md) | Fine 1-1.5 pt line weight, dense zentangle/floral/geometric detail for adults |
| [Simple Kids Coloring Page](kids_coloring_page_simple.md) | Very thick 4-6 pt outlines, few large open areas, friendly subjects for ages 2-6 |
| [KDP Interior Page](coloring_book_kdp_interior.md) | Correct trim/bleed/gutter margins, single-sided guidance, cross-book style lock for self-publishing |
| [Mandala Pattern Page](mandala_pattern_page.md) | Controllable radial symmetry (4-16 fold) and complexity, perfectly centered |
| [Themed Coloring Set / Series](themed_coloring_set.md) | Template-driven set with one locked style across many enumerated subjects |
| [Educational Coloring Page](educational_coloring_page.md) | Coloring + learning: big colorable letter/number/word + matching illustration + caption |
| [Coloring Book Cover](coloring_book_cover.md) | Full-COLOR cover: title typography + teaser art, KDP bleed/safe-zone, no 3D mockup |
| [Holiday / Seasonal Page](holiday_seasonal_coloring_page.md) | Template-driven per holiday/season (Christmas, Halloween, Easter, fall, winter, etc.) |
| [Image → Coloring Book Page](image_to_coloring_book_page.md) | Convert an uploaded photo/illustration into a children's line-art coloring page |

---

## Core Coloring Constraints (enforced in every interior prompt)

- Pure black outlines (`#000000`) on pure white (`#FFFFFF`)
- NO grayscale, shading, hatching-as-shading, gradients, or solid black fills
- Clean, **closed** line art (no gaps that let color bleed)
- Age-appropriate line weight (thick/bold for kids, fine for adults)
- White margins (0.5 in safe zone; KDP pages add a wider gutter)
- A single flat page viewed straight-on — never a 3D book mockup or photo of a book
- Print-ready: 8.5 x 11 in (or specified) at 300 DPI

---

## Model Notes (all prompts)

Each prompt leads with **gpt-image-2** (OpenAI) and **Nano Banana** (Google Gemini) as the current primary models, then lists **DALL-E 3 / Midjourney / Stable Diffusion** as legacy options. For line art: Midjourney responds to `--no color shading`; Stable Diffusion does best with a **lineart ControlNet** plus a shading/color negative prompt.

---

## Choosing a Prompt

- **Who colors it?** Young kids → [simple kids page](kids_coloring_page_simple.md); adults → [intricate page](adult_coloring_page_intricate.md) or [mandala](mandala_pattern_page.md).
- **Learning goal?** → [educational page](educational_coloring_page.md).
- **A whole book or collection?** → [themed set](themed_coloring_set.md) for content + [KDP interior](coloring_book_kdp_interior.md) for layout + [cover](coloring_book_cover.md).
- **Seasonal/holiday?** → [holiday/seasonal page](holiday_seasonal_coloring_page.md).
- **Starting from an existing image?** → [image → coloring page](image_to_coloring_book_page.md).

---

*Updated: 2026-06-23*
