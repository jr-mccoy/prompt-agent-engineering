---
title: "Meter, Scansion, and Fixed Forms — Scanning a Draft Line by Line, Auditing Sonnet, Villanelle, Ghazal, Sestina and Pantoum Rules, and Deciding When to Break Form"
category: creative-writing
description: "Audit a draft formal poem line by line: scan each line for stress and syllable count, separate legitimate metrical substitutions (initial inversion, feminine ending, double iamb) from padding and rhyme-forced syntax, check the fixed form's actual rules (rhyme scheme, refrain positions, radif and qafia, end-word rotation), and decide whether each departure is a meaningful break or an error — distinct from the poetry craft overview, which helps choose a form and draft."
techniques:
  - DT-05
  - CM-11
  - QA-24
  - NE-04
difficulty: advanced
tags:
  - creative-writing
  - poetry
  - scansion
  - meter
  - iambic-pentameter
  - fixed-forms
  - villanelle
  - poem-rhythm-feels-off
  - does-my-sonnet-follow-the-rules
  - count-beats-in-a-line
updated: "2026-10-03"
related_prompts:
  - domain-creative-writing/poetry/writing_poetry_craft_and_forms.md
  - domain-creative-writing/songwriting/writing_song_structure_lyric_revision.md
  - domain-childrens-writing/craft-tools/childrens_read_aloud_rhythm_rhyme_polish.md
---

# Meter, Scansion, and Fixed Forms

**Objective:** Take a drafted formal (or metrically ambitious) poem and return a
line-by-line scansion, a rules audit for its fixed form, and a verdict on every
departure — *keep as meaningful variation*, *fix as padding or error*, or *ask the
poet* — with replacement lines that hold the meter without bending the syntax.

**When to Use:**
- You wrote a sonnet, villanelle, ghazal, sestina, pantoum, or blank verse and a line
  "sounds off" but you cannot say why.
- You want to know whether your iambic pentameter is actually iambic pentameter.
- A workshop told you the poem is "padded" or "forced by the rhyme."
- You are breaking a form on purpose and want the break to read as a choice.
- **Not this prompt if** you are choosing a form or drafting from a subject — use
  `domain-creative-writing/poetry/writing_poetry_craft_and_forms.md` (the overview;
  this prompt is the technical audit of a finished draft). If the words are set to a
  melody, the melody controls stress — use
  `domain-creative-writing/songwriting/writing_song_structure_lyric_revision.md`.
  For rhyming picture-book text read aloud, use
  `domain-childrens-writing/craft-tools/childrens_read_aloud_rhythm_rhyme_polish.md`.
  For dead or mixed metaphors, use `poetry/writing_imagery_and_figurative_language.md`.

## Inputs / Context

1. **The full draft**, lines numbered.
2. **The intended form and meter** (e.g. Shakespearean sonnet in iambic pentameter;
   villanelle in loose tetrameter; ghazal with radif "of salt").
3. **The poet's pronunciation** where it matters (regional stress such as
   "GA-rage"/"ga-RAGE", and syllable counts for words like "fire", "every", "heaven").
4. **Deliberate departures** the poet already knows about, and why.
5. **Strictness wanted**: strict (traditional rules), accentual-syllabic but loose,
   or "the form as scaffold, break it where it helps".

## Method

1. **Scan every line (DT-05).** Mark stresses with `/` and unstressed syllables
   with `x`, divide feet with `|`, and count syllables. Lexical stress is fixed by
   the dictionary (`to-MOR-row`); monosyllables take stress from context, so mark
   promoted or demoted stresses and say which reading you chose. Where pronunciation
   changes the count, give both scansions and mark the line provisional.
2. **Classify each departure from the base meter.** Recognised substitutions in
   English accentual-syllabic verse:
   | Variation | Pattern | Usually reads as |
   |---|---|---|
   | Initial (or post-caesura) inversion | `/x` in place of `x/` | emphasis — common and accepted |
   | Double iamb / ionic | `xx //` across two feet | weight, a slowing — accepted |
   | Feminine ending | extra unstressed syllable at line end | relaxed close — accepted |
   | Headless line | first unstressed syllable dropped | abrupt start — use sparingly |
   | Anapestic substitution | `xx/` in iambic | speed; normal in loose meter, noticeable in strict |
   | Inversion in feet 2–5, or two in a row | `/x` mid-line | often jarring unless meaning justifies it |
   | Missing or extra full foot | 4 or 6 feet in pentameter | either a deliberate break or an error — ask |
3. **Run the padding and forcing checks (NE-04).** Flag: filler auxiliaries added
   for a syllable ("I *did* love"), inverted word order for a rhyme ("the sky so
   blue was bright"), archaic diction to fill a foot ("doth", "'tis", "ere"),
   adverbs clipped to fit ("sharpen slow"), and rhyme words that bend the sense.
   Show each as a bad/good pair: the padded line beside a line that keeps the meter
   in natural syntax.
4. **Audit the fixed form against its rules (CM-11).** State each rule with its
   reason, so the poet can judge a break:
   - **Petrarchan sonnet:** octave ABBAABBA, sestet CDECDE or CDCDCD; the volta at
     line 9 exists because the octave poses and the sestet answers.
   - **Shakespearean sonnet:** ABAB CDCD EFEF GG; turn at line 9 or the couplet.
     Spenserian links quatrains: ABAB BCBC CDCD EE.
   - **Villanelle:** 19 lines, five tercets and a quatrain, two rhyme sounds;
     refrains A1 and A2 at lines 1 and 3, A1 at 6, 12, 18, A2 at 9, 15, 19. The
     refrains must change meaning as context changes; varying their wording slightly
     is a recognised liberty if the change carries meaning.
   - **Ghazal:** at least five autonomous couplets (*sher*); each couplet ends with
     the *qafia* (rhyme) immediately followed by the *radif* (repeated word or
     phrase); the first couplet (*matla*) uses both in both lines; the last
     (*maqta*) traditionally carries the poet's name or signature. Couplets do not
     run on into each other — autonomy is the form's tension.
   - **Sestina:** six sestets and a three-line envoi; end words rotate 123456 →
     615243 each stanza; the envoi uses all six.
   - **Pantoum:** quatrains where lines 2 and 4 become lines 1 and 3 of the next;
     the poem usually closes on its opening line.
5. **Decide each break (QA-24).** For every departure, record a verdict and the
   reason. *Meaningful* when it coincides with a semantic event (a turn, a shock, an
   emphasis) and the pattern around it is steady enough for the break to be felt.
   *Error* when it carries no meaning, or when breaks are so frequent no pattern
   remains. List the departures you checked and **cleared**, not only the faults,
   so "nothing wrong here" is distinguishable from "not checked".
6. **Propose replacements.** For each fix, give 1–2 options that keep syllable
   count, rhyme, and the poet's diction; scan the replacement too.
7. **Report the form's overall health**: percentage of lines in base meter, number of
   accepted substitutions, number of errors, and whether the form is being kept,
   loosened, or broken — and whether that matches the poet's stated strictness.

## Output Format

```
# Form and meter audit — [title]
Intended: [form] in [meter] · Strictness: [strict | loose | scaffold]
Pronunciation notes: [...]

## Line-by-line scansion
| # | Line | Scansion (x / |) | Syll. | Departure | Verdict |

## Padding and forcing (bad → good)
| # | Problem | Original | Replacement (scanned) |

## Form rules audit
| Rule | Required | Draft | Status |

## Departures checked and cleared
## Breaks to keep (and why) · Breaks to fix · Questions for the poet
## Summary: [n]/[N] lines in base meter · [n] accepted substitutions · [n] errors
```

## Verification

- [ ] Every line is scanned, with syllable count and any provisional reading marked.
- [ ] Each departure is named by type and given a verdict with a reason.
- [ ] Every replacement line is itself scanned and keeps rhyme and count.
- [ ] Form rules are checked against the actual pattern (rhyme letters, refrain line
      numbers, end-word order), not from memory of "how it usually goes".
- [ ] Cleared departures are listed alongside faults.
- [ ] Verdicts respect the poet's stated strictness.

## False-Positive Prevention

1. **Variation is not error.** Iambic pentameter with no substitutions is
   mechanical; initial inversions and feminine endings are part of the meter.
2. **Stress is partly interpretive.** Two readers can scan "and every Sunday he"
   differently; give your reading, not a verdict on the poet's ear.
3. **Dialect changes the count.** "Fire" is one syllable or two; mark it, don't fix it.
4. **Modern formal verse is often loose by design.** Do not apply strict-meter rules
   to a poem whose poet asked for accentual or loose meter.
5. **Slant rhyme is not a broken scheme.** Flag only where the rhyme sound
   disappears entirely or the scheme letter changes.
6. **A broken form can be the point.** A short line at the volta may be the poem's
   best moment; ask before regularising.
7. **Do not rewrite for meter at the cost of meaning.** A metrically perfect
   replacement that changes what the line says is not a fix.

## Example Output

```
# Form and meter audit — "Workbench" (poet's draft, quatrains 1–2, volta, couplet)
Intended: Shakespearean sonnet in iambic pentameter · Strictness: loose but audible
Pronunciation notes: poet says "ga-RAGE" (US); "every" as two syllables.

## Line-by-line scansion
| # | Line | Scansion | Syll. | Departure | Verdict |
| 1 | My father kept his chisels in a row, | x / | x / | x / | x / | x / | 10 | "in" promoted | Clear |
| 2 | their edges oiled against the garage damp; | x / | x / | x / | x x | / / | 10 | double iamb | Keep — weight on "garage damp" |
| 3 | and every Sunday he would sharpen slow | x / | x / | x / | x / | x / | 10 | "slow" for "slowly" | Fix — rhyme-forced |
| 4 | the blades beneath the yellow of the lamp. | x / | x / | x / | x / | x / | 10 | — | Clear |
| 5 | Broken, the vise still bites the bench's edge | / x | x / | x / | x / | x / | 10 | initial inversion | Keep — stress lands on "Broken" |
| 6 | I did not know the weight that it did hold | x / | x / | x / | x / | x / | 10 | filler "did" ×2 | Fix — padding |
| 7 | and hung his apron on the window ledge, | x / | x / | x / | x / | x / | 10 | — | Clear |
| 8 | the pocket stiff with pencils, gone to gold. | x / | x / | x / | x / | x / | 10 | — | Clear |
| 9 | But I have sold the house. | x / | x / | x / | 6 | trimeter at volta | Ask — likely keep |
| 13 | And now the rust has come to claim the steel | x / | x / | x / | x / | x / | 10 | — | Clear |
| 14 | as grief to me the hammer's ring doth feel. | x / | x / | x / | x / | x / | 10 | inverted syntax + "doth" | Fix — forcing |

## Padding and forcing (bad → good)
| 3 | adverb clipped for rhyme | "and every Sunday he would sharpen slow" | A: "and Sunday nights he'd hone them, to and fro," (x / x / x / x / x /; "fro" keeps the A rhyme and names the honing motion) B: "and sharpened them on Sundays, soft and slow," (x / x / x / x / x /) |
| 6 | filler auxiliaries | "I did not know the weight that it did hold" | "I never learned how much that grip could hold" (x / x / x / x / x /) |
| 14 | archaic + inverted | "as grief to me the hammer's ring doth feel." | A: "the way the hammer rang is how I feel." B: "and I can't hear a hammer, or I feel." |

## Form rules audit
| Rule | Required | Draft | Status |
| Lines | 14 | 14 | OK |
| Rhyme | ABAB CDCD EFEF GG | row/damp/slow/lamp; edge/hold/ledge/gold; …; steel/feel | OK |
| Meter | pentameter throughout | L9 trimeter | Deliberate? |
| Turn | L9 or couplet | L9 "But I have sold the house." | Strong |

## Departures checked and cleared
L1 "in" promoted (normal in iambic); L2 ionic foot (accepted; pronunciation-dependent —
if the poet says "GA-rage" it becomes x / | x / | x / | x / x | / and still scans);
L5 initial inversion; "every" elided to two syllables per the poet.

## Breaks to keep · fix · ask
Keep: L2, L5. Fix: L3, L6, L14. Ask: L9 — a six-syllable line at the volta makes the
silence after "house" do the work of the missing four syllables. It reads as a choice
*because* lines 1–8 hold the meter; keep it only if no other line breaks.

## Summary: 10/11 scanned lines in base meter · 2 accepted substitutions · 3 errors
```

## Techniques Used

- **DT-05 Element-by-Element Assessment Matrix** — every line scanned and verdicted on the same columns.
- **CM-11 Reasoning-Based Constraint Design** — each form rule stated with its purpose, so a break can be judged against that purpose.
- **QA-24 Dismissed-Candidates Coverage Table** — departures checked and cleared are reported, not only faults.
- **NE-04 Good vs Bad Example Calibration** — padded lines shown beside metrical replacements in natural syntax.

## Related Prompts

- `domain-creative-writing/poetry/writing_poetry_craft_and_forms.md` — choosing a form and drafting; this prompt audits the result.
- `domain-creative-writing/songwriting/writing_song_structure_lyric_revision.md` — stress against a melody rather than against a meter.
- `domain-childrens-writing/craft-tools/childrens_read_aloud_rhythm_rhyme_polish.md` — rhyme and rhythm for read-aloud picture books.
