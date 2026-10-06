---
title: "GPT Image 2 — UI Mockup Specification"
category: image-generation/ui
description: "Realistic mobile or web UI mockup briefed as an artifact specification, not a concept-art request."
techniques:
  - ST-01
  - ST-02
  - SV-15
difficulty: intermediate
tags:
  - gpt-image-2
  - ui-mockup
  - product-design
  - openai
updated: "2026-10-06"
related_prompts:
  - domain-image-generation/GPT_IMAGE_2_GUIDE.md
---

# GPT Image 2 — UI Mockup Specification

**Objective:** Generate a realistic mobile or web UI mockup that looks like a screenshot of a product that already exists, not concept art. Lock layout, hierarchy, real copy, and component vocabulary.

**API parameters (recommended):**
- `model="gpt-image-2"`
- `size="1024x1536"` (mobile portrait), `1536x1024` (desktop landscape), or `1024x1024` (tablet/component)
- `quality="medium"` (use `high` if the screen has data tables, charts, or small text)
- `n=1`

---

## Inputs

- `[PRODUCT NAME]` — what the app is called
- `[PLATFORM]` — iOS / Android / web (Mac / Windows) / responsive web
- `[SCREEN]` — which screen (e.g., "home feed", "checkout step 2", "settings")
- `[PRIMARY ACTION]` — the most important interaction on this screen
- `[REAL COPY]` — actual nav labels, button text, sample data — verbatim
- `[BRAND PALETTE]` — hex codes
- `[TYPOGRAPHY]` — system fonts (SF Pro on iOS, Roboto on Android, Inter on web) or specified brand fonts

---

## Constraints (Must / Must Not)

**Must:**
- Brief as if the product already exists ("Show the home feed of [PRODUCT NAME]…").
- Use real copy in nav, buttons, headers, and sample data — never lorem ipsum.
- Include realistic platform-specific chrome (status bar, nav bar, OS-correct controls).
- Specify a 12-column grid or 4-pt/8-pt spacing system.

**Must Not:**
- Use concept-art language ("a dreamy interface", "futuristic UI", "magical button").
- Use lorem ipsum, faux-Latin, or "Sample Text".
- Add decorative background art or particle effects unless the product has them.
- Render impossible UI (3D floating panels, gradients on every surface) unless intentionally art-directed.

---

## Production Prompt

```
SCENE / CANVAS:
A single flat screenshot-style mockup of the [PLATFORM] [SCREEN] for [PRODUCT NAME]. The image is the screen, edge-to-edge. No phone frame, no laptop frame, no presentation context — unless explicitly requested.

SUBJECT:
The [SCREEN] is presented as if [PRODUCT NAME] is a shipped product. The user is mid-task: [PRIMARY ACTION].

KEY DETAILS — layout and components:
- Platform chrome: [iOS status bar / Android system bar / browser address bar — describe accurately].
- Top of screen: [nav structure — back button, title, action button — with EXACT TEXT].
- Body region: [primary content layout — list, grid, form, dashboard — with EXACT data].
- Bottom of screen: [tab bar / nav / footer — with EXACT TEXT for every label].
- Spacing system: 8-pt baseline grid. Components align cleanly to it.
- Component vocabulary: standard [PLATFORM] controls (e.g., iOS rounded buttons with 14pt SF Pro Text; Android Material 3 components with Roboto; web standard form controls with Inter).

USE CASE:
Product design specification mockup. Will be used in a design review, in marketing copy, or as a reference for engineering. Must look like a real screenshot, not concept art.

CONSTRAINTS:
- Style commitment: realistic UI screenshot. Not concept art. Not illustration. Not a stylized "dreamy" interface.
- Brand palette: primary [HEX], secondary [HEX], surface [HEX], on-surface [HEX].
- Typography: [TYPOGRAPHY]. No mixed type families.
- EXACT TEXT (verbatim, no extra characters):
  - [Nav title]: "[TITLE]"
  - [Buttons / actions]: "[ACTION 1]", "[ACTION 2]"
  - [Tab labels / nav items]: "[TAB 1]", "[TAB 2]", "[TAB 3]"
  - [Sample data — list items, form labels, body copy]: "[real copy here]"
  - [System/utility — time, battery, etc.]: "9:41" "100%" (iOS conventions) or platform-appropriate.
- Forbidden: lorem ipsum, faux-Latin, "Sample Text", decorative particle effects, drop shadows beyond standard platform elevation, gradients on every surface, fake-looking placeholder images (use realistic stock-style images for any embedded photo).
- Format: [size], [orientation].

If any text is lorem ipsum, faux-Latin, or invented placeholder copy, the output is incorrect. If the chrome is wrong for the stated platform, the output is incorrect.
```

---

## Iteration Plan

1. "The [tab/component] alignment is off — snap everything to the 8-pt baseline grid."
2. "Replace the placeholder image in the [position] with [specific realistic content]."
3. "The accent hex is too saturated against the surface — adjust to [refined hex]."

---

## False-Positive Prevention

❌ **DON'T:**
- Read "no lorem ipsum" as "no invented content" — the realistic-copy instruction pushes the model to fill the body region with menu items, settings toggles, badges, prices, ratings, and user names the product does not have.
- Pass the platform chrome because a status bar is present — check the device-generation details (notch vs. Dynamic Island, Android gesture bar vs. 3-button nav) match `[PLATFORM]`.
- Ship a mockup to marketing or engineering on the strength of "looks like a real screenshot" — that realism is exactly why a viewer will read every visible control as a shipped feature.

✅ **DO:**
- Inventory every visible string, icon button, tab, and data value in the output and map each to a `[REAL COPY]` entry or to standard platform chrome; anything unmapped is an invented feature and is removed in the next iteration.
- Count tabs, nav items, and buttons against the EXACT TEXT list — a fourth tab when three were specified fails the mockup even if its label is sensible.
- Check embedded stock-style photos and avatars for identifiable real people or third-party logos, and replace them before the mockup leaves design review.

---

## Verification

- [ ] EXACT TEXT for every visible string.
- [ ] Platform stated and chrome described accurately.
- [ ] Spacing system stated (4-pt or 8-pt).
- [ ] No concept-art language.
- [ ] No lorem ipsum allowed.
- [ ] `quality="high"` if charts/tables/small text present.
