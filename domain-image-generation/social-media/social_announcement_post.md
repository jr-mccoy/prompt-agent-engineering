---
title: "Social — Announcement / Promo Post"
category: image-generation/social
description: "Announcement or promo post (sale, launch, event) with a clear headline, supporting detail, and CTA — verbatim copy, strong hierarchy."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - SV-13
  - SV-15
  - SV-17
difficulty: intermediate
tags:
  - social-media
  - announcement
  - promo
  - sale
  - launch
  - event
  - cta
  - gpt-image-2
  - nano-banana-pro
updated: "2026-06-23"
related_prompts:
  - domain-image-generation/social-media/README.md
  - domain-image-generation/social-media/social_quote_graphic.md
  - domain-image-generation/social-media/social_story_reel_cover.md
  - domain-image-generation/IMAGE_MODEL_SELECTION_GUIDE.md
---

# Social — Announcement / Promo Post

**Objective:** Generate an announcement/promo social post (sale, product launch, event, milestone) with a punchy headline, supporting detail, and a clear call-to-action — all copy rendered verbatim, with strong visual hierarchy that survives a small-screen scroll. This is a designed promo graphic, distinct from a full campaign ad creative (that lives in `domain-advertising/`).

**Why Nano Banana Pro (primary):** Promo posts carry critical verbatim copy — dates, prices, discount codes, CTAs — where a single wrong digit breaks the offer. `gemini-3-pro-image` gives near-perfect text rendering plus exact font control, and **search grounding** can verify factual elements (e.g., a correct event date) when needed.

**Why gpt-image-2 (alternate):** `gpt-image-2` renders text at 95%+ with `quality="high"` and gives strong layout-section control for hierarchy (headline / detail / CTA) — and `n=4` lets you batch promo layout options fast. Use it as the alternate or for rapid concepting.

> Avoid Nano Banana 2 / Midjourney / SD when prices, dates, or codes must be exact.

**API parameters:**

Nano Banana Pro (primary):
- `model="gemini-3-pro-image"`
- `size="1080x1080"` (square feed) — adjust per `[PLATFORM + RATIO]`
- `quality="high"`
- `n=2`

gpt-image-2 (alternate):
- `model="gpt-image-2"`
- `size="1024x1024"`
- `quality="high"` (always high for text)
- `n=4` to explore layouts

---

## Inputs

- `[ANNOUNCEMENT TYPE]` — sale / launch / event / milestone
- `[HEADLINE]` — the hook, verbatim (e.g., "Summer Sale — 30% Off Everything")
- `[DETAIL]` — supporting line(s), verbatim (dates, terms, what's new)
- `[CTA]` — call to action, verbatim (e.g., "Shop now — link in bio", "Use code SUMMER30")
- `[KEY FIGURE]` — the standout number/code if any (price, %, date, code)
- `[PLATFORM + RATIO]` — IG 1080×1080 (1:1) / IG portrait 1080×1350 (4:5) / X 1600×900 (16:9) / FB 1200×630
- `[BRAND PALETTE]` — background hex, headline hex, accent/CTA hex
- `[FONT CHARACTER]` — headline + body font character
- `[VISUAL MOTIF]` — solid / gradient / product cutout / illustrated accent
- `[LOGO/HANDLE]` — brand mark / @handle placement

---

## Constraints (Must / Must Not)

**Must:**
- Render `[HEADLINE]`, `[DETAIL]`, `[CTA]`, and any `[KEY FIGURE]` 100% verbatim.
- Make the headline (and any key figure/code) the dominant element; CTA clearly visible and distinct.
- Use the accent/CTA hex to make the CTA pop against the background.
- Keep all text crop-safe (≥8% inset) and high-contrast for small screens.
- Maintain a clean hierarchy: headline > detail > CTA, with the key figure emphasized.

**Must Not:**
- Alter prices, dates, percentages, or promo codes in any way.
- Paraphrase or invent copy; render no lorem ipsum.
- Bury the CTA or let it blend into the background.
- Overcrowd the layout — promo posts are scanned in under a second.
- Add fine-print that's illegible at thumbnail size as if it were the main message.

---

## Production Prompt — Nano Banana Pro (Primary)

```
TASK: Create an [ANNOUNCEMENT TYPE] social promo graphic, [PLATFORM + RATIO].

DESIGN:
A bold, scannable [VISUAL MOTIF] promo post. Visual hierarchy: headline dominant, supporting detail secondary, CTA prominent and distinct. Optional small [LOGO/HANDLE] in a corner. [If product cutout: show the product cleanly placed, not competing with the headline.]

BACKGROUND: [background hex] — [solid / gradient to (second hex)], clean behind the text.

TYPOGRAPHY:
- Font character: [FONT CHARACTER].
- Headline color: [headline hex]. CTA in [accent/CTA hex] so it pops. Emphasize [KEY FIGURE] as the standout.

EXACT TEXT (render 100% verbatim — every digit, date, percent, and code exactly as written):
HEADLINE: "[HEADLINE]"
DETAIL: "[DETAIL]"
CTA: "[CTA]"
KEY FIGURE: "[KEY FIGURE]"
HANDLE/LOGO: "[LOGO/HANDLE]"

LAYOUT:
Headline up top or centered as the hero; [KEY FIGURE] emphasized; detail below; CTA in a distinct treatment (button-like or accent color) clearly visible. All text inset ≥8% from edges (crop-safe), high contrast.

CONSTRAINTS:
- MUST: render every word, digit, date, percent, and code exactly; headline dominant; CTA distinct in [accent/CTA hex]; crop-safe high-contrast text.
- MUST NOT: alter any price/date/percentage/code, paraphrase or invent copy, bury the CTA, overcrowd, or render lorem ipsum.
- If a single character of any figure, code, date, or CTA differs from the text above, the output is INCORRECT.
- Quality: "high"
```

---

## Production Prompt — gpt-image-2 (Alternate)

```
SCENE:
A bold, scannable [ANNOUNCEMENT TYPE] promo graphic, [PLATFORM + RATIO]. Background: [background hex] — [VISUAL MOTIF], clean behind text.

SUBJECT:
Hierarchy: dominant headline (and emphasized [KEY FIGURE]), secondary detail, prominent distinct CTA. Optional small handle/logo in a corner. [If product cutout: cleanly placed, not competing with the headline.]

KEY DETAILS:
- Font character: [FONT CHARACTER]. Headline [headline hex]; CTA in [accent/CTA hex] to pop. Use exact hex values.
- All text inset ≥8% from edges (crop-safe); strong contrast for small screens.

EXACT TEXT (verbatim — every digit, date, percent, code exactly):
HEADLINE: "[HEADLINE]"
DETAIL: "[DETAIL]"
CTA: "[CTA]"
KEY FIGURE: "[KEY FIGURE]"
HANDLE/LOGO: "[LOGO/HANDLE]"

USE CASE:
Organic/paid social promo post. Scanned in under a second; offer must be unmistakable and correct.

CONSTRAINTS:
- Style commitment: clean designed promo graphic.
- Forbidden: altering any price/date/percentage/code, paraphrase, invented/lorem-ipsum text, buried CTA, overcrowding.
- Format: [PLATFORM + RATIO].

If any figure, code, date, or CTA differs from the text above, the output is INCORRECT.
```

---

## Iteration Plan

1. "The discount code rendered as \"SUMMR30\" — re-render it exactly: \"[CTA / code]\"."
2. "The CTA blends into the background — switch it to [accent/CTA hex] and give it a button-like treatment."
3. "The headline isn't dominant enough — increase its size and emphasize [KEY FIGURE]."
4. "Layout is crowded — drop secondary detail to one line and add breathing room."
5. "Date text is too close to the edge — increase inset to ≥8% for crop safety."

---

## Verification

- [ ] `[HEADLINE]`, `[DETAIL]`, `[CTA]`, `[KEY FIGURE]` all rendered 100% verbatim (every digit/date/percent/code).
- [ ] Headline (and key figure/code) is dominant; CTA is distinct and prominent.
- [ ] CTA uses accent hex and pops against the background.
- [ ] Clean hierarchy: headline > detail > CTA.
- [ ] All text crop-safe (≥8% inset) and high-contrast.
- [ ] No altered figures, paraphrasing, lorem ipsum, or buried CTA.
- [ ] Layout is scannable, not crowded.
- [ ] `quality="high"` set (mandatory for text).
- [ ] Correct platform aspect ratio.
