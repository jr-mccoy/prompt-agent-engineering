---
title: "SSML & TTS Voice Tuning — Pronunciation Lexicons, Normalization, Prosody, Pauses, and a Listening Regression Set"
category: voice-conversational-ui/voice-design
description: "Fix how a text-to-speech voice actually sounds: inventory mispronunciations and misreadings, apply fixes in order of least engine dependence (rewrite, normalization, pronunciation lexicon, inline phoneme, prosody and breaks), confirm each tag against the target engine's documented support, and lock results with a golden listening set that is re-run on every voice or engine upgrade; distinct from voice_design_vui_prompt_writing.md (what the system says) and from the AI-ML speech framing prompt (training and evaluating TTS models)."
techniques:
  - CM-01
  - ST-02
  - DS-06
  - QA-10
  - ST-03
difficulty: intermediate
tags:
  - ssml
  - tts
  - pronunciation-lexicon
  - prosody
  - voice-design
  - regression-testing
updated: "2026-09-24"
related_prompts:
  - domain-voice-conversational-ui/voice-design/voice_design_vui_prompt_writing.md
  - domain-voice-conversational-ui/voice-design/voice_design_custom_voice_assistant.md
  - domain-AI-ML/specialized-ml/other-modalities/mlmodal_speech_asr_tts_framing.md
---

# SSML & TTS Voice Tuning

**Objective:** Turn a list of "it sounds wrong" complaints into a tuned voice:
every misreading classified, fixed with the least engine-dependent method that
works, verified by listening, and protected by a regression set so the next
voice upgrade does not silently undo it.

**When to Use:**
- Users or testers report mispronounced names, places, brands, or jargon.
- Numbers, dates, times, currencies, abbreviations, or codes are read wrongly.
- The voice sounds flat, rushed, or stresses the wrong word.
- You are switching TTS vendor, engine, or voice (including a neural voice
  upgrade) and need to know what will change.

**Not this prompt if:**
- You are writing or rewriting *what* the system says →
  `domain-voice-conversational-ui/voice-design/voice_design_vui_prompt_writing.md`.
- You are choosing a TTS engine as part of an assistant architecture →
  `voice_design_custom_voice_assistant.md`.
- You are training or evaluating a TTS *model* (data, MOS studies) →
  `domain-AI-ML/specialized-ml/other-modalities/mlmodal_speech_asr_tts_framing.md`.

## Inputs

1. **Target engine(s) and voice(s)**, with version, and a link to or excerpt of
   each engine's supported-SSML documentation.
2. **Problem utterances**: the text sent to TTS and a description of what is heard.
3. **Content sources**: static prompts, templated prompts, and dynamic content
   (user names, addresses, product names).
4. **Locale(s)** and the audience's pronunciation expectations.
5. **Any existing lexicon files** and SSML conventions.

## Method

1. **Frame the constraints (CM-01).** Record engine, voice, locale, and the
   subset of SSML the engine documents as supported. Treat every tag not in
   that list as unsupported until tested; engines differ, and some neural
   voices ignore or reinterpret prosody attributes.
2. **Classify each problem.** One class per issue:
   *mispronunciation* (a word), *normalization* (a number, date, time, unit,
   abbreviation, or code read wrongly), *homograph* (right word, wrong sense),
   *phrasing* (pauses in the wrong place or none), *prosody* (stress, pitch,
   rate, question intonation), *audio* (clipping, volume jumps between clips).
3. **Fix in order of least engine dependence (ST-02).** Stop at the first step
   that works:
   1. **Rewrite the text** ("Rte" → "Route"; split a long sentence).
   2. **Normalize** with `<say-as>` or `<sub alias="…">` for numbers, dates,
      codes, and abbreviations.
   3. **Lexicon entry** (e.g., a W3C PLS file) for a word that must *always*
      be said one way in this product.
   4. **Inline `<phoneme>`** for homographs or one-off names, so a global
      lexicon entry does not break other uses.
   5. **`<break>`, `<emphasis>`, `<prosody>`** for phrasing and stress, used
      sparingly and in relative units where supported.
4. **Handle dynamic content.** For names and addresses the product does not
   control, decide a policy: default engine reading, a maintained lexicon of
   frequent values, or a user-supplied pronunciation. Never guess a person's
   name pronunciation into a global lexicon.
5. **Prioritize (DS-06).** Rank fixes by frequency × harm: a wrongly read
   amount of money or medication dose outranks a slightly flat greeting.
6. **Build the golden listening set (QA-10).** One entry per fixed issue plus
   representative normal prompts. For each: text, SSML, expected rendering in
   plain words, and a pass/fail judged by at least two listeners, including a
   speaker of the locale. Re-run the whole set on any engine, voice, or lexicon
   change.
7. **Report with confidence (ST-03).** For each fix: **High** (verified by
   listening on the target engine), **Medium** (tag documented as supported,
   not yet heard), **Low** (untested or undocumented).

## Output Format

```
## Engine profile
Engine · Voice · Version · Locale · Documented SSML subset
## Issue register
| # | Utterance | Heard | Class | Frequency × harm | Priority |
## Fixes
| # | Method (rewrite/say-as/lexicon/phoneme/prosody) | Before | After (text or SSML) | Confidence |
## Lexicon entries (scope: global)
## Dynamic content policy
## Golden listening set
| ID | Text/SSML | Expected rendering | Listener A | Listener B | Result |
## Regression triggers
## Open items
```

## Verification

- [ ] Every tag used appears in the engine's documented SSML subset, or is marked Low confidence.
- [ ] Each fix used the earliest method in the order that works.
- [ ] No homograph is placed in a global lexicon.
- [ ] Every High-confidence fix was heard on the target engine.
- [ ] The golden set covers every fixed issue plus unchanged prompts.
- [ ] Money, dates, doses, and codes are verified character by character against the spoken rendering.

## False-Positive Prevention

1. **Do not assume standard SSML works everywhere.** Engines implement
   different subsets and attribute values; unsupported tags may be ignored or
   read aloud.
2. **Do not fix a text problem with markup.** If a rewrite solves it, the
   rewrite is portable; SSML is not.
3. **Do not over-tune prosody.** Stacked `<prosody>` and `<emphasis>` make
   neural voices sound less natural, not more.
4. **Do not put homographs in a global lexicon.** A lexicon entry for a place
   name that is also an ordinary word changes every use of that word.
5. **Do not trust one listener.** Native-locale listeners catch errors that
   others hear as "fine."
6. **Do not transcribe IPA from memory for real names.** Confirm with the
   name's owner or an authoritative source; mark unconfirmed entries `[VERIFY]`.
7. **Do not treat a voice upgrade as a no-op.** Re-run the golden set; neural
   voice updates change normalization and prosody.

## Example

**Input (summary):** UK bus-times voice app on a cloud neural TTS voice (en-GB).
Complaints: "Reading" (the town) said like the verb; "Rte 9A" read as "R-T-E
nine A"; "7:05" read as "seven point oh five"; departure lists run together.

```
## Engine profile
Cloud neural TTS · en-GB voice v2 · SSML subset: speak, break, say-as
(date, time, cardinal, characters), sub, phoneme (ipa), prosody (rate only) [VERIFY against vendor docs]

## Issue register
| # | Utterance | Heard | Class | Freq × harm | Priority |
|---|---|---|---|---|---|
| 1 | "Rte 9A to Reading" | "R-T-E nine A" | Normalization | High × med | 1 |
| 2 | "…to Reading" | verb "reading" | Homograph | High × med | 2 |
| 3 | "7:05" | "seven point oh five" | Normalization | High × high | 1 |
| 4 | Three departures in one sentence | Runs together | Phrasing | Med × low | 3 |

## Fixes
| # | Method | Before | After | Conf. |
|---|---|---|---|---|
| 1 | Rewrite | Rte 9A | Route 9A | High |
| 2 | Inline phoneme | Reading | <phoneme alphabet="ipa" ph="ˈrɛdɪŋ">Reading</phoneme> | High |
| 3 | say-as | 7:05 | <say-as interpret-as="time">7:05</say-as> | Medium — format attribute support unconfirmed |
| 4 | Rewrite + break | one sentence | three sentences, <break time="300ms"/> between | High |

## Lexicon entries (scope: global)
None. "Reading" is a homograph, so it stays inline (fix 2).

## Dynamic content policy
Stop names come from the operator feed; maintain a reviewed lexicon for the
40 most frequent stops, confirmed with local staff.

## Golden listening set
| ID | Text/SSML | Expected | A | B | Result |
|---|---|---|---|---|---|
| G1 | Route 9A to Reading at 7:05 | "route nine A to REDD-ing at seven oh five" | Pass | Pass | Pass |
| G2 | "I'm reading the timetable." | verb "reading" | Pass | Pass | Pass (lexicon did not leak) |

## Regression triggers
Voice version change · engine change · any lexicon edit.

## Open items
Confirm say-as time formatting (fix 3) on the production voice.
```

## Techniques Used

- **CM-01 Explicit Context Framing** — the engine's documented SSML subset bounds every fix.
- **ST-02 Structured Sequential Instructions** — the least-engine-dependence fix order.
- **DS-06 Prioritization and Severity Guidance** — frequency × harm ranking.
- **QA-10 Test Battery Protocol** — the golden listening set and regression triggers.
- **ST-03 Output Format Specification** — register, fixes, and set as fixed tables.

## Related Prompts

- `domain-voice-conversational-ui/voice-design/voice_design_vui_prompt_writing.md` — what the system says.
- `domain-voice-conversational-ui/voice-design/voice_design_custom_voice_assistant.md` — TTS engine selection in the architecture.
- `domain-AI-ML/specialized-ml/other-modalities/mlmodal_speech_asr_tts_framing.md` — TTS model evaluation.
