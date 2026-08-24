# Content Creation Quick Start (Faceless Publishing)

**Purpose:** Apply this bundle's technique library and authoring guides to faceless content
creation — channels, blogs, and social accounts where you publish at volume without being on camera.
This is the *application layer*: it maps real content tasks to the techniques that make AI output
reliably good, and points you at the right guide and starter prompt for each.

> **Technique IDs** (ST-01, NE-12, SV-11, …) are from the canonical
> [Master Technique Index](../techniques/MASTER_TECHNIQUE_INDEX.md). Never invent IDs.
> For the full task→technique map across all domains, see
> [Use Case Lookup](../techniques/USE_CASE_LOOKUP.md).

---

## How to use this file

1. Find your task in the **Task → Technique Map** below.
2. Read the linked guide section (most content work uses
   [`../guides/NON_CODING_QUICK_START.md`](../guides/NON_CODING_QUICK_START.md); image work uses
   [`../guides/image-generation/`](../guides/image-generation/)).
3. Start from the matching file in [`starter-prompts/`](starter-prompts/), then specialize it for
   *your* niche, voice, and platform.
4. Before publishing AI output, run the **Verification** block that ships in every starter prompt.

---

## The faceless-content task taxonomy

Faceless publishing decomposes into a repeatable pipeline. Each stage is a prompt you can template
once and reuse forever:

```
IDEATE → SCRIPT/DRAFT → PACKAGE (title + thumbnail + description) → REPURPOSE → REVIEW
```

The two failure modes AI content falls into — **generic median output** and **invented facts /
fake authority** — are exactly what the techniques below defend against.

---

## Task → Technique Map

| Content task | Core techniques | Guide | Starter prompt |
|---|---|---|---|
| **Long-form script** (video / article / podcast outline) | ST-01, CM-01, CM-02, NE-12 (voice/cognitive mode), ST-02, ST-03, QA-01 | [NON_CODING_QUICK_START](../guides/NON_CODING_QUICK_START.md) → CREATE | [`content_long_form_script.md`](starter-prompts/content_long_form_script.md) |
| **Short-form hooks** (Shorts / Reels / TikTok / thread openers) | ST-01, NE-12, RT-02 (angle variety), CM-02, ST-03 | NON_CODING → CREATE | [`content_short_form_hook_bank.md`](starter-prompts/content_short_form_hook_bank.md) |
| **Thumbnail / cover image brief** | SV-11 (terminology steering), SV-12 (grid/slots), SV-13 (constraint redundancy), SV-14 (negative space), ST-03 | [IMAGE_GENERATION_GUIDE](../guides/image-generation/IMAGE_GENERATION_GUIDE.md) / [GPT_IMAGE_2_GUIDE](../guides/image-generation/GPT_IMAGE_2_GUIDE.md) | [`content_thumbnail_image_brief.md`](starter-prompts/content_thumbnail_image_brief.md) |
| **SEO title + description + tags** | ST-01, CM-01, CM-02 (no clickbait / no keyword stuffing), ST-03, QA-01 | NON_CODING → CREATE | [`content_seo_title_description.md`](starter-prompts/content_seo_title_description.md) |
| **Repurpose one → many** (long-form → shorts, threads, newsletter) | CM-01, NE-02 (phased), RT-02, ST-03, QA-01 | NON_CODING → IMPROVE/CREATE | [`content_repurpose_one_to_many.md`](starter-prompts/content_repurpose_one_to_many.md) |
| **Series / channel voice bible** (consistency across episodes) | RP-01, NE-12, CM-01, CM-02, ST-03 | NON_CODING → CREATE | [`content_series_channel_bible.md`](starter-prompts/content_series_channel_bible.md) |
| **Fact-check / pre-publish review** | QA-01, QA-02 (adversarial), CM-02 | NON_CODING → "Quality without tests" section | use the Verification block in any starter prompt; escalate with QA-02 |

---

## Five rules that keep faceless content out of the "AI slop" bucket

1. **Anchor voice every time (NE-12 + RP-01).** A reusable voice bible (see
   `content_series_channel_bible.md`) is the single highest-leverage asset — paste it into every
   script prompt so output sounds like *your* channel, not the model's default register.
2. **Hook-first, always (ST-01).** State the single job of the piece ("make a cold viewer watch past
   8 seconds") so the model optimizes for retention, not for sounding complete.
3. **Ban fabrication explicitly (CM-02).** Faceless niches (history, science, finance, true-crime)
   live or die on accuracy. Every content prompt must include *"Must Not: state any statistic, date,
   quote, or claim you cannot ground in the provided source material; flag anything uncertain for
   human check."*
4. **Lock the output shape (ST-03).** Specify word counts, segment structure, line lengths, and —
   for thumbnails — exact dimensions and text. Vague shape = median shape.
5. **Verify before you publish (QA-01, escalate to QA-02).** Each starter prompt ends with a
   self-check; for monetized or claims-heavy content, add the adversarial stress-test
   ("list 3 ways this could mislead a viewer").

---

## Building your project's own prompt library

As each project accumulates prompts, save them next to this file using the repo naming convention
`{content_function}.md` (e.g., `content_voiceover_script.md`) and the structured format in
[`../guides/NEW_PROMPT_TEMPLATE.md`](../guides/NEW_PROMPT_TEMPLATE.md). Run each new prompt against
[`../guides/NEW_RESOURCE_CHECKLIST.md`](../guides/NEW_RESOURCE_CHECKLIST.md) before relying on it.

---

**Last Updated:** 2026-05-27
