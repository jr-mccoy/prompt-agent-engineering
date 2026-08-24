# Comic & Sequential Art Prompts

Production-ready prompts for **sequential art** — Western comic pages, manga-style pages, and vertical-scroll webtoons. All three are page/strip compositions with internal panels, reading-order control, and reserved lettering space. They build on the shot-progression and consistency discipline in [STORYBOARD_WORKFLOW.md](../STORYBOARD_WORKFLOW.md) and [CHARACTER_BIBLE_PIPELINE.md](../CHARACTER_BIBLE_PIPELINE.md).

**Parent guides:** [STORYBOARD_WORKFLOW.md](../STORYBOARD_WORKFLOW.md) · [CHARACTER_BIBLE_PIPELINE.md](../CHARACTER_BIBLE_PIPELINE.md) · [IMAGE_MODEL_SELECTION_GUIDE.md](../IMAGE_MODEL_SELECTION_GUIDE.md)

---

## Prompts

| Prompt | Format | Reading Order | Recommended Model |
|--------|--------|---------------|-------------------|
| [Comic Panel Page](comic_panel_page.md) | Multi-panel page, gutters, speech-safe areas | Western LTR, top-to-bottom | gpt-image-2 (one-pass page) · Nano Banana 2 (per-panel) |
| [Manga-Style Panel](manga_style_panel.md) | Screentone B&W page, dynamic paneling | Right-to-left (or LTR) | gpt-image-2 (one-pass) · Nano Banana 2/Pro (style slot) |
| [Webtoon Vertical Strip](webtoon_vertical_strip.md) | Long vertical scroll, extreme tall ratio | Top-to-bottom scroll | Nano Banana 2 (extreme aspect ratios) · gpt-image-2 (stitch beats) |

---

## Choosing a Format

- **Western comic page** — print/digital page with flat color, balloons, classic grid → `comic_panel_page.md`.
- **Manga page** — black-and-white screentone look, expressive eyes, often right-to-left, dynamic diagonal panels → `manga_style_panel.md`.
- **Webtoon** — phone-first vertical scroll, pacing controlled by whitespace, very tall aspect ratio → `webtoon_vertical_strip.md`.

---

## Model ID Quick Reference

| Name | Model ID | Sequential-Art Strength |
|------|----------|-------------------------|
| gpt-image-2 | `gpt-image-2` | Best one-pass multi-panel cross-panel consistency; aspect ~1:3 max |
| Nano Banana | `gemini-2.5-flash-image` | Budget per-panel iteration |
| Nano Banana Pro | `gemini-3-pro-image` | Style slots lock the render (screentone, webtoon look) |
| Nano Banana 2 | `gemini-3.1-flash-image` | Fast iteration; **only model with extreme aspect ratios (1:8/8:1)** — best for tall webtoons |

---

## Sequential-Art Conventions

- **Reserve lettering space.** Reserve speech-bubble / caption-safe areas; do not render lettering or SFX unless explicitly asked (letterers add type separately).
- **Control reading order explicitly.** Western = LTR; manga = often RTL (state it — models default to LTR); webtoon = top-to-bottom scroll. Verify the eye actually reads in the intended order.
- **Vary shot sizes.** Adjacent panels should differ by at least one shot-size step.
- **Lock character + style + color grade across panels/beats.** Restate the bible every time; reference the original pack, not recent outputs.
- **Match the shape to the medium.** Page (portrait) for comics/manga; tall strip for webtoons (Nano Banana 2 native extreme ratios, or stitch on gpt-image-2).
