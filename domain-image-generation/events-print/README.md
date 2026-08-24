# Events & Print Prompts

Production-ready, Tier-1 prompts for print-ready promotional materials — event posters, promotional flyers, and concert/gig posters. Every artifact here carries dense, must-be-correct text (event names, dates, venues, prices, lineups) and must survive a physical print pipeline, so each prompt routes to a text-rendering model and enforces an EXACT TEXT contract plus bleed/safe-area rules.

**Parent guides:** [IMAGE_MODEL_SELECTION_GUIDE.md](../IMAGE_MODEL_SELECTION_GUIDE.md) · [GPT_IMAGE_2_GUIDE.md](../GPT_IMAGE_2_GUIDE.md) · [NANO_BANANA_GUIDE.md](../NANO_BANANA_GUIDE.md) · [IMAGE_GENERATION_GUIDE.md](../IMAGE_GENERATION_GUIDE.md) (print-ready techniques)

---

## Prompts

| Prompt | Use | Differentiator |
|--------|-----|----------------|
| [Event Poster](event_poster.md) | Conferences, fairs, openings, community events | Headline hierarchy, scannable date/venue block, print bleed |
| [Promotional Flyer](promotional_flyer.md) | Sales, offers, grand openings, services | Offer-first, dense info grouped, single CTA, QR placeholder |
| [Concert / Gig Poster](concert_gig_poster.md) | Live music shows | Headliner dominance, billing order, stylized art + spot-color screen-print |

---

## Model routing (why these picks)

| Need | First choice | Why |
|------|-------------|-----|
| Dense verbatim text (dates, prices, addresses) | gpt-image-2 (`quality="high"`) | 95%+ text accuracy, section-based briefing |
| Complex multi-line hierarchy / exact fonts | Nano Banana Pro (`gemini-3-pro-image`) | Near-perfect text + exact font specification |
| Art-driven background, text-free (set type later) | Nano Banana 2 / Midjourney | Fast aesthetic exploration; add text in an editor |

---

## Model ID Quick Reference

| Name | Model ID |
|------|----------|
| GPT Image 2 | `gpt-image-2` |
| Nano Banana | `gemini-2.5-flash-image` |
| Nano Banana Pro | `gemini-3-pro-image` |
| Nano Banana 2 | `gemini-3.1-flash-image` |

---

## Cross-cutting print conventions

- **EXACT TEXT contract.** Event/band names, dates, times, venues, prices, ticket info, and fine print render verbatim with face, weight, hex, and placement. No invented prices, URLs, sponsors, or acts.
- **Bleed + safe area.** Full-bleed artwork extends 0.125 in (3 mm) past trim; all text stays 0.25 in (6 mm) inside trim so the printer's cut never clips it.
- **Information hierarchy.** Largest = the hook (event name / offer / headliner); supporting details grouped into scannable blocks; one primary CTA.
- **No fake QR codes.** When a QR is needed, reserve a clean high-contrast square placeholder; insert the real, tested code in post (a model-rendered QR won't scan).
- **Resolution.** Generate at the closest supported size, then upscale to 300 DPI and convert RGB → CMYK before sending to an offset printer.
- **Screen-print feasibility.** For spot-color gig posters, limit to the stated flat-color count — no gradients or photographic blends.

*Print specs reflect common standards as of 2026-06-23. Always confirm bleed, safe area, color space, and resolution with your specific printer before sending to press.*
