---
title: "Song Structure and Lyric Revision — Prosody, Stress, Hook Placement, and Section Jobs"
category: creative-writing
description: "Revise an existing original song lyric section by section: map each section's job and catch sections that repeat each other, check prosody (natural word stress against the melody's strong beats, vowel choice on long notes, line length against phrase length), place the hook where the song's weight falls, and return a prioritised change list with before/after lines — distinct from the lyric craft workshop (which drafts from an idea) and from general manuscript revision (which works on prose)."
techniques:
  - DT-05
  - ST-02
  - DS-06
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - creative-writing
  - songwriting
  - prosody
  - song-structure
  - hook
  - revision
  - chorus-doesnt-lift
  - words-fight-melody
  - awkward-to-sing
updated: "2026-09-24"
related_prompts:
  - domain-creative-writing/craft-tools/writing_revision_and_self_editing.md
  - domain-creative-writing/songwriting/writing_song_lyric_craft_workshop.md
  - domain-childrens-writing/craft-tools/childrens_read_aloud_rhythm_rhyme_polish.md
---

# Song Structure and Lyric Revision

**Objective:** Diagnose why a finished song draft doesn't land — sections
duplicating jobs, words fighting the melody, a hook buried or overused — and
return the smallest set of changes, ranked, with before/after lines the writer
can sing today.

**When to Use:**
- A draft is complete and "something is off" when it's sung.
- A co-writer or producer said "the chorus doesn't lift" or "verse 2 is verse 1 again".
- Words get mis-heard because the stress falls on the wrong syllable.
- You are cutting a song to a target length (radio edit, sync brief).

**Not this prompt if:**
- There is no draft yet → `domain-creative-writing/songwriting/writing_song_lyric_craft_workshop.md`.
- You are revising prose fiction or a manuscript → `domain-creative-writing/craft-tools/writing_revision_and_self_editing.md`.
- You are polishing read-aloud rhyme for a picture book (no melody) →
  `domain-childrens-writing/craft-tools/childrens_read_aloud_rhythm_rhyme_polish.md`.

> **Originality guard:** revision works on the writer's own lyric. A brief,
> attributed line from a published song may be cited to illustrate a technique;
> published lyrics are never reproduced in full or used as a template to fill.

## Inputs

1. **The full lyric**, labelled by section.
2. **The melody's shape**, in whatever form exists: a recording description,
   stressed beats marked in CAPS, syllable counts per phrase, or chord chart
   with bar counts. If no melody exists, say so — prosody checks become
   provisional.
3. **Genre, tempo, target length.**
4. **The writer's own complaint** ("the bridge feels tacked on").
5. **What must not change** (a line the writer loves, a title fixed by a brief).

## Method

1. **Map section jobs (ST-02).** For each section write: job (situate, develop,
   sum up, turn, resolve), new information added, and emotional temperature.
   Flag any two sections with the same job and no new information.
2. **Assess element by element (DT-05).** For every line, check:
   | Check | What to look for |
   |---|---|
   | Stress | Naturally stressed syllables fall on strong beats ("to-MOR-row", not "TO-mor-row") |
   | Length | Syllables fit the phrase without cramming or melisma the genre wouldn't use |
   | Vowel | Long or high notes land on open vowels (ah, oh, ay) rather than closed ones (ih, eh) or consonant clusters |
   | Rhyme position | Rhymes sit where the melody resolves; rhyme scheme is consistent across parallel sections |
   | Clarity | A first-time listener can parse the line at tempo |
3. **Locate the hook.** Where does the title land: first or last line of the
   chorus, on a downbeat, on the highest or longest note? Count total title
   repetitions; flag both under-use (listener can't name the song) and
   over-use (title on every line with no development).
4. **Check contrast.** Chorus against verse: different line length, rhythm,
   or register? A chorus with the same rhythm as the verse rarely lifts.
5. **Prioritise (DS-06).** Rank each issue: *Structural* (section duplication,
   missing turn) > *Prosodic* (mis-stress, unsingable vowel on a held note) >
   *Local* (a weak word). Fix structural first; line polish on a section that
   will be cut is wasted.
6. **Propose changes under constraints (CM-02).** For each: before line,
   after line (or 2 options), which check it fixes, and what it costs. Keep
   the writer's protected lines. Preserve syllable count unless the fix is
   the count.
7. **Self-check (QA-01).**

## Output Format

```
# Revision — [song title]
Melody status: [marked / described / none — prosody provisional]
Protected lines: [...]

## Section map
| Section | Job | New information | Temperature | Duplicates? |

## Line-level findings
| Section · line | Check | Issue | Severity (structural/prosodic/local) |

## Hook placement
Title position · repetitions · contrast with verse

## Change list (ranked)
| # | Before | After (option A / B) | Fixes | Cost |

## What to leave alone (and why)
## Sing-test instructions
```

## Verification

- [ ] Every section has a stated job; duplicates are flagged.
- [ ] Stress findings reference the melody's strong beats, or are marked provisional.
- [ ] Protected lines are unchanged.
- [ ] Each proposed change names the check it fixes.
- [ ] Structural issues are ranked above line polish.
- [ ] No published lyric is reproduced beyond a brief attributed quote.

## False-Positive Prevention

1. **Mis-stress without a melody is a guess.** Without the melody, mark every
   stress finding provisional; a composer can set any word many ways.
2. **Repetition is a feature of songs.** A chorus repeating is not
   redundancy; a verse repeating the chorus's *information* is.
3. **Near rhyme is not an error.** Flag rhyme only where the scheme breaks
   between parallel sections or the rhyme word bends the meaning.
4. **Genre sets the rules.** Hip-hop verses stack internal rhymes and
   syllables; folk tolerates long verses without a pre-chorus. Do not
   "correct" conventions.
5. **Don't polish a section that should go.** If the bridge duplicates verse
   2, the fix is structural, not a better bridge line.
6. **Leave the writer's voice.** A colloquialism or grammatical liberty that
   sings well is not an error.
7. **A longer song is not a fuller song.** Offer cuts as readily as additions.

## Example Output

```
# Revision — "Postage Paid" (writer's original)
Melody status: verse and chorus melodies marked with CAPS on strong beats; bridge unset.
Protected lines: "Three dollars and change for the promise we made."

## Section map
| Section | Job | New information | Temp | Duplicates? |
|---|---|---|---|---|
| V1 | Situate | Post office, the box | Low | — |
| Chorus | Sum up | Paying to avoid saying | Mid | — |
| V2 | Develop | Why not in person | Mid | — |
| V3 (draft had one) | Develop | Back at the counter, box handed over | Low | Duplicates V1 setting, no new info |
| Bridge | Turn | Clerk's "anything fragile?" | High | — |

## Line-level findings
| Line | Check | Issue | Severity |
|---|---|---|---|
| V3 whole | Job | Returns to V1's scene with nothing new | Structural |
| Chorus L1 "POST-age PAID" | Stress | Melody marked "post-AGE paid" — stress lands on the weak syllable | Prosodic |
| Chorus L4 "and the postage paid" | Vowel | Held final note on "paid" (ay) — fine; keep | — |
| V2 L4 "for heaven's sake" | Length | 3 syllables longer than V1 L4 | Prosodic |

## Hook placement
Title opens and closes chorus; 8 uses in 3:40. Chorus rhythm is longer-lined
than verse — contrast present. Fine once the stress is fixed.

## Change list
| # | Before | After | Fixes | Cost |
|---|---|---|---|---|
| 1 | V3 (4 lines) | Cut; go V2 → bridge | Duplicate job | Loses 0:25; song 3:15 |
| 2 | Melody "post-AGE paid" | Ask composer to shift: POST-age PAID (pickup note on "just a box in a") | Stress | Melody change, not lyric |
| 3 | "There's a mercy in a stranger's hands for heaven's sake" | A: "There's a mercy in a stranger's hands" / B: "Let a stranger's hands be kind for me" | Length | A drops the rhyme with "make"; B keeps sense, loses "mercy" |

## What to leave alone
Bridge answer "only everything, just not in the bag" — the turn works; don't lengthen it.

## Sing-test
Sing chorus with change 2 at 72 bpm three times; if "postage" still
mis-stresses, try the title as "Paid the Postage" (stress on PAID) — writer's call.
```

## Techniques Used

- **DT-05 Element-by-Element Assessment Matrix** — the five line-level checks.
- **ST-02 Structured Sequential Instructions** — map jobs → line checks → hook → rank → change.
- **DS-06 Prioritization and Severity Guidance** — structural before prosodic before local.
- **CM-02 Constraint Specification** — protected lines and syllable-count preservation.
- **QA-01 Self-Verification** — checklist including provisional-stress marking.

## Related Prompts

- `domain-creative-writing/craft-tools/writing_revision_and_self_editing.md` — prose revision passes.
- `domain-creative-writing/songwriting/writing_song_lyric_craft_workshop.md` — drafting the lyric.
- `domain-childrens-writing/craft-tools/childrens_read_aloud_rhythm_rhyme_polish.md` — rhythm without a melody.
