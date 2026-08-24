# Publishing Cover Prompts

Production-ready, Tier-1 prompts for cover art across publishing formats — books (fiction and nonfiction), ebooks, music albums, and podcasts. Every cover here is **typography-led**: the title and author/artist/show name must render verbatim, so each prompt routes to a text-rendering model and carries an EXACT TEXT contract plus a thumbnail/small-size legibility gate.

**Parent guides:** [IMAGE_MODEL_SELECTION_GUIDE.md](../IMAGE_MODEL_SELECTION_GUIDE.md) · [GPT_IMAGE_2_GUIDE.md](../GPT_IMAGE_2_GUIDE.md) · [NANO_BANANA_GUIDE.md](../NANO_BANANA_GUIDE.md)

---

## Prompts

| Prompt | Format / Spec | Differentiator |
|--------|---------------|----------------|
| [Fiction Book Cover](cover_fiction_book.md) | Portrait, print trim | Genre conventions, title + author typography, optional spine/back |
| [Nonfiction / Business Cover](cover_nonfiction_book.md) | Portrait, print trim | Authoritative, strict title > subtitle > author hierarchy |
| [Ebook Cover (KDP)](cover_ebook_kdp.md) | 1600×2560 (W×H), 1.6:1 | Thumbnail legibility at ~150 px in the Kindle store |
| [Album Cover Art](cover_album_art.md) | 3000×3000 square | Mood-driven, streaming-thumbnail-safe, optional text-free path |
| [Podcast Cover Art](cover_podcast_art.md) | 3000×3000 square | Legible at ~55 px tile, series-template consistency |

---

## Model routing (why these picks)

| Need | First choice | Why |
|------|-------------|-----|
| Verbatim title + author typography | gpt-image-2 (`quality="high"`) | 95%+ text accuracy, section-based briefing, `n=4` concept pools |
| Complex / multi-line title hierarchy | Nano Banana Pro (`gemini-3-pro-image`) | Near-perfect text + exact font specification |
| Series consistency across episode/issue covers | Nano Banana Pro | System prompts lock the typographic + color template |
| Text-free aesthetic cover (set type yourself after) | Nano Banana 2 / Midjourney | Fast aesthetic exploration; add type in an editor |

---

## Model ID Quick Reference

| Name | Model ID |
|------|----------|
| GPT Image 2 | `gpt-image-2` |
| Nano Banana | `gemini-2.5-flash-image` |
| Nano Banana Pro | `gemini-3-pro-image` |
| Nano Banana 2 | `gemini-3.1-flash-image` |

---

## Cross-cutting conventions

- **EXACT TEXT contract.** Title, author/artist/show, and any subtitle render verbatim, with face, weight, hex, and placement specified. No invented blurbs, award seals, credentials, host names, episode numbers, or publisher/network logos.
- **Thumbnail-first.** Covers are sold at thumbnail/tile size. Each prompt names a target small size (200×300 px for books, ~150 px for streaming tiles, ~55 px for podcast tiles) and requires the title to survive it.
- **Quiet zone + safe margin.** Type sits on clean ground inside a safe inset so resizing to spec never clips it.
- **One rendering style.** Commit to photographic / illustrated / painterly / graphic — never blend.
- **No infringement.** Evoke genre/era/mood; never copy a specific real cover or render a brand/label/network mark you don't own.

*Specs reflect the state of distributor requirements as of 2026-06-23. Verify against current KDP / Apple / Spotify / DistroKid documentation before upload.*
