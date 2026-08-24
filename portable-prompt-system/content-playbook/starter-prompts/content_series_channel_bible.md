---
title: "Series / Channel Voice Bible Builder"
category: content-creation/brand-voice
description: "Build a reusable voice-and-style bible for a faceless channel or series so every AI-assisted asset sounds consistent — the highest-leverage reusable context document for content work."
techniques:
  - ST-01
  - RP-01
  - NE-12
  - CM-01
  - CM-02
  - ST-03
  - QA-01
difficulty: intermediate
tags:
  - faceless
  - brand-voice
  - consistency
  - style-guide
  - reusable-context
updated: "2026-05-27"
related_prompts:
  - content_long_form_script.md
  - content_short_form_hook_bank.md
  - content_repurpose_one_to_many.md
---

# Series / Channel Voice Bible Builder

**Objective:** Produce a reusable `<voice_bible>` document that you paste into every other content
prompt so all AI-assisted output sounds like one consistent channel — defined precisely enough that a
model can match it and a human can audit against it. *(ST-01)*

> This is the keystone asset. Build it once per channel/series; every script, hook, and repurpose
> prompt in this playbook takes `<voice_bible>` as input.

---

## When to Use

Starting a new faceless channel/series, or codifying the voice of one that grew organically and now
sounds inconsistent across uploads.

---

## Inputs / Context *(CM-01)*

**Required:**
- Channel/series concept, niche, and target audience.
- 2–5 `<voice_samples>` — existing scripts/posts that sound right (or competitor/reference samples to emulate or contrast).

**Optional:**
- Positioning vs. competitors (how you differ).
- Hard rules already known (always/never say, legal/compliance lines).
- Persona framing if the channel narrates as a character/archetype.

**If no `<voice_samples>` and no clear concept exist:** Interview the user (one question at a time) to elicit voice before drafting. *(NE-01 pacing)*

---

## Constraints *(CM-02)*

**Must:**
- Derive voice traits from evidence in `<voice_samples>`, with a quoted example for each trait. *(RP-01)*
- Make every rule concrete and testable (a model can apply it; a human can check it). *(NE-12)*
- Include an explicit banned-words/phrases and banned-structures list.
- Keep it paste-ready — compact enough to prepend to other prompts. *(ST-03)*

**Must Not:**
- Describe voice in vague adjectives alone ("engaging, fun") without an operational rule + example.
- Invent a backstory or claims the channel hasn't established.
- Produce a document so long it's impractical to paste into every prompt.

---

## Instructions *(ST-02)*

1. If `<voice_samples>` exist, extract recurring traits (tone, register, sentence length, humor, jargon level, pacing). Quote evidence per trait. *(RP-01)*
2. Define the audience and the implied relationship (peer, mentor, insider).
3. Codify operational rules: do/don't, sentence rhythm, vocabulary level, how to open, how to CTA. *(NE-12)*
4. List banned words/phrases and banned structures (e.g., "no 'In this video'"; "no em-dash overuse").
5. Add a 3–5 line **voice test**: sample sentences that pass vs. fail, for quick auditing.
6. Compress into the paste-ready block in the Output Format.

---

## Output Format *(ST-03)*

### Channel Snapshot
Concept, niche, audience, and the relationship in 3–4 lines.

### Voice Traits (evidence-backed)
| Trait | Operational rule | Example (quoted/derived) |
|---|---|---|

### Do / Don't
Two short lists.

### Banned Words, Phrases & Structures
Bulleted.

### Voice Test
3–5 PASS sentences and 3–5 FAIL sentences with a one-line reason each.

### `<voice_bible>` (paste-ready block)
A compact, self-contained version to prepend to other content prompts.

---

## Verification *(QA-01)*

**Quick self-check (always):**
- [ ] Every voice trait has an operational rule AND an example.
- [ ] Banned list is present and specific.
- [ ] The voice test clearly separates pass/fail.
- [ ] The paste-ready block stands alone and is short enough to reuse everywhere.
- [ ] Nothing invented beyond what `<voice_samples>`/concept support.
