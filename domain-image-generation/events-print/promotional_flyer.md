---
title: "Promotional Flyer"
category: image-generation/events-print
description: "Offer-driven, information-dense, print-ready promotional flyer with verbatim copy and a clear CTA."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - SV-13
  - SV-17
difficulty: advanced
tags:
  - flyer
  - promotion
  - offer
  - print
  - typography
  - gpt-image-2
  - nano-banana-pro
updated: "2026-06-23"
related_prompts:
  - domain-image-generation/IMAGE_MODEL_SELECTION_GUIDE.md
  - domain-image-generation/events-print/event_poster.md
  - domain-image-generation/events-print/concert_gig_poster.md
  - domain-image-generation/GPT_IMAGE_2_GUIDE.md
---

# Promotional Flyer

**Objective:** Produce an offer-driven, information-dense promotional flyer that leads with the offer, packs the supporting details legibly, drives to a single clear call to action, and prints clean — all with verbatim copy.

**Why this model:** A flyer carries the most must-be-correct text of any format here — offer, price, dates, fine print, phone/URL/QR. Use **gpt-image-2** (`quality="high"`) or **Nano Banana Pro** (`gemini-3-pro-image`) for accurate dense text. Speed-first models scramble price and fine print.

**Print spec (verify against your printer's specs):**
- Common sizes: 8.5×11 in (US Letter), A5 (148×210 mm), A4 (210×297 mm), DL (99×210 mm)
- **Bleed:** 0.125 in (3 mm); **safe area:** all text 0.25 in (6 mm) inside trim
- 300 DPI for print; RGB → CMYK in post

**API parameters:**
- gpt-image-2 path: `model="gpt-image-2"`, `size="1024x1536"` (portrait letter/A4) or `1536x1024` (landscape), `quality="high"`, `n=3`; upscale to print resolution
- Nano Banana Pro path: `model="gemini-3-pro-image"`, portrait aspect, `quality="high"`

---

## Inputs

- `[OFFER]` — verbatim headline offer ("50% Off All Classes", "Grand Opening")
- `[BUSINESS NAME]` — verbatim
- `[SUPPORTING DETAILS]` — verbatim bullet list of what's included
- `[PRICE / TERMS]` — verbatim price(s) and conditions
- `[DATES / VALIDITY]` — verbatim ("Valid through Aug 31, 2026")
- `[CTA]` — verbatim ("Call (555) 123-4567", "Visit example.com", "Scan to book")
- `[FINE PRINT]` — verbatim disclaimer (optional)
- `[QR PLACEHOLDER?]` — yes/no (reserve a square zone; insert the real QR in post)
- `[BRAND PALETTE]` — hex codes
- `[TONE]` — 3 adjectives
- `[KEY VISUAL]` — product/service image
- `[ORIENTATION + SIZE]`
- `[FORBIDDEN]` — to avoid

---

## Constraints (Must / Must Not)

**Must:**
- Lead with the offer — it should be the first and largest thing read.
- Render all copy verbatim in an EXACT TEXT block, including price and fine print.
- Organize dense info into scannable groups (offer → details → price/dates → CTA → fine print).
- Drive to ONE primary CTA.
- Respect bleed + safe area; keep all text inside the safe area.
- If a QR is needed, reserve a clean square placeholder zone (the model should NOT render a fake scannable QR — insert the real code in post).

**Must Not:**
- Misspell or alter price, dates, phone, or URL.
- Render a fake "working" QR code (it won't scan).
- Invent prices, terms, or disclaimers not provided.
- Crowd text into the bleed.
- Use slop hype or stock-flyer clichés in `[FORBIDDEN]`.

---

## Production Prompt (gpt-image-2)

```
ARTWORK:
Print-ready [ORIENTATION + SIZE] promotional flyer for [BUSINESS NAME]. Offer-driven
and information-dense but scannable. Tone: [TONE]. Key visual: [KEY VISUAL].
Full-bleed artwork; all text inside the safe area (≥0.25 in inside trim).

ART DIRECTION:
- Brand palette: dominant [HEX], secondary [HEX], accent [HEX]. Accent reserved for
  the offer and the CTA.
- Style commitment: [photographic product / bold graphic / clean corporate].
  Commit to ONE.

TEXT (verbatim, grouped for scannability — top to bottom):
1) OFFER (the hero): "[OFFER]" — largest, [bold face], [weight], accent [HEX].
   First thing read.
2) Business name: "[BUSINESS NAME]" — clear, [weight], [HEX].
3) Supporting details: "[SUPPORTING DETAILS]" — a tidy bulleted/grouped block,
   [weight], [HEX]. Legible, not crammed.
4) Price / terms: "[PRICE / TERMS]" — prominent and exact, [HEX].
5) Dates / validity: "[DATES / VALIDITY]" — [HEX].
6) CTA (single, primary): "[CTA]" — in an accent button/band, [HEX].
7) Fine print (if provided): "[FINE PRINT]" — smallest, [HEX], bottom.

QR ZONE (if [QR PLACEHOLDER?] = yes):
- Reserve a clean, high-contrast SQUARE zone near the CTA, with quiet margin around
  it, labeled placeholder only. Do NOT render an actual QR pattern (a fake one won't
  scan); leave the square area clean for a real QR to be dropped in afterward.

LAYOUT:
- Clear reading order: offer → details → price/dates → CTA → fine print.
- One primary CTA; do not split attention across multiple calls to action.
- Consistent alignment grid.

CONSTRAINTS:
- EXACT TEXT only, verbatim, no extra characters: the lines above and nothing else.
  No invented prices, terms, disclaimers, phone numbers, or URLs.
- No fake/working QR code rendered by the model.
- Keep all text out of the 0.125 in bleed zone.
- Forbidden: [FORBIDDEN], stock-flyer clichés, watermarks, lorem ipsum.
- Format: [ORIENTATION + SIZE], full-bleed, print-ready.

If price, dates, phone, or URL is misspelled/altered, if a fake QR is rendered, or
if text sits in the bleed, the output is incorrect.
```

## Production Prompt (Nano Banana Pro)

```
TASK: Design a print-ready [ORIENTATION + SIZE] promotional flyer for [BUSINESS NAME].
Offer-driven, dense but scannable. Tone [TONE]. Key visual [KEY VISUAL]. Full bleed;
all text inside a safe margin.

DESIGN:
Palette [HEX], [HEX], accent [HEX] (accent for offer + CTA). Commit to one rendering
style ([photographic product / bold graphic / clean corporate]).

TEXT (render exactly, grouped top to bottom):
- OFFER (hero): "[OFFER]" — largest, accent [HEX].
- Business name: "[BUSINESS NAME]", [HEX].
- Supporting details: "[SUPPORTING DETAILS]" — tidy grouped block, [HEX].
- Price/terms: "[PRICE / TERMS]" — exact, prominent, [HEX].
- Dates: "[DATES / VALIDITY]", [HEX].
- CTA (single): "[CTA]" — accent button/band, [HEX].
- Fine print (if provided): "[FINE PRINT]", smallest, [HEX].

QR (if [QR PLACEHOLDER?] = yes): reserve a clean high-contrast square placeholder
near the CTA. Do NOT render an actual QR pattern.

CONSTRAINTS:
- MUST: verbatim copy incl. price + fine print; scannable grouping; one primary CTA;
  text ≥0.25 in inside trim.
- MUST NOT: alter price/dates/phone/URL; render a fake QR; invent terms/disclaimers;
  place text in bleed; use [FORBIDDEN].
- Quality: "high".
```

---

## Iteration Plan

1. "Offer isn't the hero — bump it to the largest element and put it in the accent color."
2. "Details block is crammed — give it more breathing room and align it on a clean grid."
3. "Two CTAs are splitting attention — keep only the primary one; demote the other to fine print."
4. "Pull all text ≥0.25 in inside the trim — price is currently too close to the bleed."

---

## Verification

- [ ] Offer is the first and largest element, in the accent color.
- [ ] All copy in an EXACT TEXT block, verbatim — price, dates, phone, URL, fine print correct.
- [ ] Dense info grouped into scannable blocks.
- [ ] Exactly one primary CTA.
- [ ] No fake/working QR rendered; clean square placeholder reserved if needed.
- [ ] Full-bleed artwork; all text inside the 0.25 in safe area.
- [ ] `quality="high"`.
