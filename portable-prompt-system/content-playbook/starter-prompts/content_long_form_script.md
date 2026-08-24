---
title: "Long-Form Faceless Script Writer"
category: content-creation/scripting
description: "Write a retention-optimized long-form script (video, narrated article, or podcast) in a defined channel voice, grounded only in supplied source material."
techniques:
  - ST-01
  - CM-01
  - NE-12
  - ST-02
  - CM-02
  - ST-03
  - QA-01
difficulty: intermediate
tags:
  - faceless
  - script
  - long-form
  - retention
  - voiceover
updated: "2026-05-27"
related_prompts:
  - content_series_channel_bible.md
  - content_short_form_hook_bank.md
  - content_seo_title_description.md
---

# Long-Form Faceless Script Writer

**Objective:** Produce a publish-ready long-form script that hooks in the first 8 seconds, sustains
retention to the end, sounds like the channel's established voice, and contains no claim that isn't
grounded in the provided source material. *(ST-01)*

---

## When to Use

A faceless video, narrated article, or podcast episode where the script *is* the product. Use after
you have research/source material and a voice bible. For 60-second cuts, use the hook bank +
repurpose prompts instead.

---

## Inputs / Context *(CM-01)*

**Required:**
- `<topic>` — the episode subject and the angle/thesis.
- `<source_material>` — the research, facts, quotes, and figures the script may draw from.
- `<voice_bible>` — channel voice, tone, pacing, vocabulary, banned phrases (see `content_series_channel_bible.md`).
- Target length (runtime in minutes OR word count) and platform.

**Optional:**
- Target audience (knowledge level, what they already believe).
- CTA / end-screen goal (subscribe, next video, lead magnet).
- Reference episode(s) that performed well.

**If any required input is missing:** Ask before writing. Do not invent a voice or source facts.

---

## Constraints *(CM-02)*

**Must:**
- Open with a hook that creates an open loop in the first 1–2 sentences.
- Match the tone, vocabulary, and sentence rhythm defined in `<voice_bible>`.
- Write for the ear (spoken cadence) if it's a video/podcast; mark `[B-ROLL]` / `[ON-SCREEN TEXT]` cues where useful.
- Hit the target length within ±10%.

**Must Not:**
- State any statistic, date, quote, name, or causal claim not present in `<source_material>`. Mark anything you'd want to add but can't ground as `[UNVERIFIED — human check]`.
- Drift into a generic "AI explainer" register that ignores `<voice_bible>`. *(NE-12)*
- Use filler intros ("In today's video we're going to talk about…") or fabricated personal anecdotes (the channel is faceless).
- Pad to reach length; cut to reach length.

---

## Instructions *(ST-02)*

1. Restate the episode's single retention job and target audience in one line. If unclear, ask.
2. Adopt the channel voice from `<voice_bible>` before writing a word. *(NE-12)*
3. Draft a **hook** (open loop / stakes / pattern interrupt) and 2 alternates.
4. Outline the body as labeled segments with an internal retention device per segment (question, mini-cliffhanger, payoff).
5. Write the full script segment by segment, pulling only from `<source_material>`; insert `[UNVERIFIED]` flags as needed.
6. Write the close + CTA tied to the stated goal.
7. Run the Verification block; revise before delivering.

---

## Output Format *(ST-03)*

### Episode Summary
One line: the hook promise + the payoff.

### Hook (chosen + 2 alternates)
The opening lines, written to be spoken.

### Script
Segmented with headers, e.g. `## [0:00–0:45] Hook`, then body segments, then close.
Inline cues: `[B-ROLL: ...]`, `[ON-SCREEN: ...]`, `[UNVERIFIED — human check]`.

### Retention Map
Table: segment → retention device → why it holds the viewer.

### Open Items
Bulleted list of every `[UNVERIFIED]` flag and any source gaps to fill.

---

## Verification *(QA-01)*

**Quick self-check (always):**
- [ ] Hook lands in ≤2 sentences and opens a loop.
- [ ] Every factual claim traces to `<source_material>`; all else is flagged `[UNVERIFIED]`.
- [ ] Voice matches `<voice_bible>` (spot-check 3 sentences against its banned/required list).
- [ ] Length within ±10% of target; no padding.
- [ ] CTA matches the stated goal.

**High-stakes (monetized / claims-heavy) — add QA-02:**
List 3 ways this script could mislead a viewer or get a fact wrong, and fix or flag each.
