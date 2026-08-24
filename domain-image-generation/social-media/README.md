# Social Media Graphic Packs

Production-ready prompts for generating **social graphics** — quote cards, swipe carousels, announcement/promo posts, vertical story/reel covers, and profile banners. These are designed graphics carrying verbatim copy, distinct from full campaign ad creative (`domain-advertising/`) and product photography (`ecommerce-product/`).

**Model selection:** [IMAGE_MODEL_SELECTION_GUIDE.md](../IMAGE_MODEL_SELECTION_GUIDE.md) · **Guides:** [GPT_IMAGE_2_GUIDE.md](../GPT_IMAGE_2_GUIDE.md) · [NANO_BANANA_GUIDE.md](../NANO_BANANA_GUIDE.md)

## The text-fidelity rule (read first)

Most social graphics carry **verbatim copy** — quotes, prices, dates, promo codes, taglines — where a single wrong character breaks the asset. That makes model choice the most important decision:

- **Nano Banana Pro (`gemini-3-pro-image`)** — near-perfect text + exact font control + system-prompt style locking. **First choice for text-heavy, multilingual, or matched-set graphics** (carousels, quote graphics, promo posts with codes/dates).
- **gpt-image-2** — 95%+ text accuracy at `quality="high"`, strong layout-section control, fast batch layouts with `n=4`. **Strong alternate / primary for hero covers and short sets.**
- **Always set `quality="high"`** for any graphic with text.
- **Avoid Nano Banana 2 / Midjourney / Stable Diffusion** for final text-bearing graphics — use Nano Banana 2 only to screen backgrounds/compositions cheaply at 512px.

Every prompt below specifies exact fonts, hex colors, placement, and platform aspect ratios/safe zones.

---

## Prompts

| Prompt | What It Produces | Primary Model | Alternate |
|--------|------------------|---------------|-----------|
| [Quote / Typography Graphic](social_quote_graphic.md) | Quote card, typography-led | Nano Banana Pro | gpt-image-2 |
| [Carousel Set](social_carousel_set.md) | Multi-slide swipe set, one consistent template | Nano Banana Pro (system prompt) | gpt-image-2 (cover + short set) |
| [Announcement / Promo Post](social_announcement_post.md) | Sale / launch / event post with CTA | Nano Banana Pro | gpt-image-2 |
| [Story / Reel Cover](social_story_reel_cover.md) | Vertical 9:16 cover, safe-zone aware | gpt-image-2 | Nano Banana Pro (text-heavy / series) |
| [Profile / Header Banner](social_profile_banner.md) | LinkedIn / X / YouTube / FB banner, exact dims | gpt-image-2 | Nano Banana Pro (matched set) |

---

## Common Platform Dimensions & Ratios

Verify current platform specs before production — these change over time.

| Format | Dimensions | Ratio |
|--------|------------|-------|
| Instagram feed (square) | 1080×1080 | 1:1 |
| Instagram feed (portrait) | 1080×1350 | 4:5 |
| Instagram/TikTok story & reel | 1080×1920 | 9:16 |
| X / Twitter in-feed (landscape) | 1600×900 | 16:9 |
| Facebook feed (landscape) | 1200×630 | ~1.91:1 |
| LinkedIn feed (square) | 1200×1200 | 1:1 |
| LinkedIn personal banner | 1584×396 | 4:1 |
| X / Twitter header | 1500×500 | 3:1 |
| YouTube channel art | 2560×1440 | 16:9 (TV-safe center 1546×423) |

**Safe-zone discipline:** keep critical text and focal subjects in the central safe band — stories/reels reserve the top ~14% and bottom ~20% for UI; banners reserve the avatar-overlap corner and responsive-crop margins. Inset feed-graphic text ≥8% from every edge.

---

## Model ID Quick Reference

| Name | Model ID | Use When |
|------|----------|----------|
| Nano Banana Pro | `gemini-3-pro-image` | Verbatim/long/multilingual text, matched sets (system prompts) |
| gpt-image-2 | `gpt-image-2` | Hero covers, short sets, fast layout batches, wide banner ratios |
| Nano Banana 2 | `gemini-3.1-flash-image` | 512px background/composition screening only (not final text) |

---

*Platform dimensions and model capabilities reflect the market as of 2026-06-23. Verify current platform image specs and model documentation before production use.*
