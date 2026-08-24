---
title: "Short-Form Hook Bank Generator"
category: content-creation/short-form
description: "Generate a bank of distinct, scroll-stopping hooks for Shorts/Reels/TikTok/threads, each tied to a different psychological angle, in the channel voice."
techniques:
  - ST-01
  - NE-12
  - RT-02
  - CM-02
  - ST-03
  - QA-01
difficulty: beginner
tags:
  - faceless
  - short-form
  - hooks
  - shorts
  - reels
updated: "2026-05-27"
related_prompts:
  - content_long_form_script.md
  - content_repurpose_one_to_many.md
  - content_series_channel_bible.md
---

# Short-Form Hook Bank Generator

**Objective:** Produce a bank of distinct opening hooks for a short-form piece — each engineered to
stop the scroll in the first 1–2 seconds, each using a *different* angle so you can test variants —
without overpromising beyond what the content delivers. *(ST-01)*

---

## When to Use

Drafting Shorts/Reels/TikTok or thread/X openers, or A/B testing hooks for a piece you've already
made. Pairs with the repurpose prompt when slicing long-form into clips.

---

## Inputs / Context *(CM-01)*

**Required:**
- `<content_summary>` — what the short actually shows/says and its single payoff.
- `<voice_bible>` — channel voice and banned phrases (optional but strongly recommended).
- Platform (Shorts / Reels / TikTok / X thread) and format (talking-head VO, text-on-screen, etc.).
- How many hooks you want (default: 12).

**Optional:**
- Target audience and what they already believe.
- Hooks that worked / flopped before.

**If `<content_summary>` is missing:** Ask. A hook for unknown content will overpromise.

---

## Constraints *(CM-02)*

**Must:**
- Make every hook deliverable by `<content_summary>` — the payoff must exist.
- Cover a spread of distinct angles (see Instructions), not 12 rewordings of one. *(RT-02)*
- Keep each hook to one breath / one screen of text.
- Stay in channel voice. *(NE-12)*

**Must Not:**
- Use clickbait that the content doesn't pay off ("You won't BELIEVE…").
- Recycle the same sentence structure across hooks.
- Include claims/numbers not supported by `<content_summary>`.

---

## Instructions *(ST-02)*

1. Identify the single payoff of the content in one line. If weak/unclear, say so before generating.
2. Generate hooks across these angles (label each): **curiosity gap, bold claim, contrarian, stakes/fear-of-missing, relatable problem, "you've been doing X wrong," numbered promise, before/after, question, story cold-open.** *(RT-02)*
3. For each, note the angle and the implied promise.
4. Flag any hook whose promise `<content_summary>` cannot fully pay off.
5. Recommend the top 3 to test first and why.

---

## Output Format *(ST-03)*

### Payoff
One line: what the viewer gets if they stay.

### Hook Bank
| # | Hook (verbatim) | Angle | Implied promise | Payoff supported? |
|---|---|---|---|---|

### Top 3 to Test
Ranked, with a one-line rationale each (e.g., matches audience belief, novel angle).

---

## Verification *(QA-01)*

**Quick self-check (always):**
- [ ] Each hook's promise is delivered by `<content_summary>` (no overpromise).
- [ ] Angles are genuinely distinct; no near-duplicate structures.
- [ ] Voice matches `<voice_bible>`.
- [ ] Every hook fits one breath / one screen.
