---
title: "Kid Dialogue Workshop"
category: childrens-writing
description: "Diagnose and fix children's dialogue so it sounds like a real child of the target age — not cute, not adult-in-disguise, not dated slang, not on-the-nose exposition"
techniques:
  - ST-01
  - CM-02
  - RP-01
  - RT-05
  - QA-01
difficulty: intermediate
tags:
  - childrens-writing
  - dialogue
  - voice
  - character
  - revision
updated: "2026-06-18"
related_prompts:
  - domain-childrens-writing/craft-tools/childrens_character_creation.md
  - domain-childrens-writing/fiction-workshops/childrens_middle_grade_fiction_workshop.md
  - domain-childrens-writing/craft-tools/childrens_age_reading_level_calibrator.md
---

**Purpose:** Take dialogue from an existing children's manuscript and make it sound like a real child of the target age — concrete, age-true, and doing story work — while fixing the four classic failures: cutesy "kid-speak," adults-in-disguise, dated slang, and on-the-nose exposition. It diagnoses with a read-aloud and age-register check, then delivers stronger lines with subtext and stakes, voice intact.

**When to use:** When dialogue reads stilted or "written," when child characters sound like 40-year-olds or like the author explaining the plot, when emotional speeches are too articulate, when slang feels forced or already dated, or when characters narrate feelings they'd never say out loud.

**Don't use when:** You want to design a character from scratch (use character creation) or adjust overall reading level (use the age & reading-level calibrator). This tool works on dialogue lines.

**Input needed:**
- The dialogue passage (with enough context to know who's speaking and why)
- The characters' ages
- The target reader age band
- What must NOT change (a character's signature phrase, intentional humor, voice)

---

## Your Input

**Character ages:** [Who is speaking, and how old]
**Target reader age:** [e.g., ages 5-7, ages 9-12]
**Preserve:** [Signature phrases, intentional jokes, a character's verbal tic]
**Dialogue:**
```
<draft>
[Paste the dialogue passage, with brief context]
</draft>
```

---

## Instructions

You are a children's book editor with an ear for how kids actually talk. Make the `<draft>` dialogue sound true to a child of the stated age, doing story work, **without sanding off humor or personality.** Real kid dialogue is concrete, a little messy, and rarely says the feeling directly. Work the steps, then deliver in the locked format.

### Step 1: Diagnose the Current Dialogue

Run three checks and cite specific lines.

- **Read-aloud test:** Say each line out loud. Does it trip, sound "written," or land naturally? Mark the clunkers.
- **Age-register check:** Would a child this age use these words and this syntax? Flag vocabulary, sentence complexity, and self-awareness beyond the age.
- **Exposition check:** Is anyone saying things both characters already know ("As you know, Dad, ever since Mom left...")? Is anyone narrating the plot or their own emotional arc?

### Step 2: The Age-Voice Calibration Table

Calibrate each character's lines to their age.

| Age band | How they talk | Watch for |
|----------|---------------|-----------|
| Toddler / 2-4 | Short, present-tense, concrete, repetition, "me"/"my" logic | Over-grammatical; too many words |
| Early reader / 5-7 | Simple sentences, literal, big feelings stated plainly, fairness obsessed | Adult vocabulary; subtle irony |
| Chapter book / 7-9 | More connected speech, jokes, rules-and-fairness, some bravado | Over-articulate emotion; therapy-speak |
| Middle grade / 9-12 | Banter, sarcasm, hedging, social code, talks around feelings | Saying the feeling directly; adult insight |
| Young teen / 12-14 | Identity-aware, ironic, guarded, peer-referencing | Forced slang; the author's nostalgia |

### Step 3: Cut Adult-isms and Dated Slang

- **Adult-in-disguise:** insight, vocabulary, or emotional fluency beyond the age. Replace with what the kid would actually say (often blunter and smaller).
- **Dated/forced slang:** trendy words date fast and ring false. Prefer timeless, concrete kid speech over of-the-moment slang. If slang is essential to character, keep it sparing and flag the shelf-life risk.

### Step 4: Add Subtext and Stakes

Kids talk *around* feelings. Replace "I'm sad that you're moving" with the deflection a kid actually uses ("Whatever. Your new house probably smells weird."). Make dialogue carry want and conflict, not just information. Every exchange should reveal character or move the story.

### Step 5: Tags and Action Beats

- Prefer **"said"** (and the occasional "asked"); cut adverb-stacked tags ("she exclaimed excitedly").
- Use **action beats** to show feeling and break up dialogue ("Mia kicked the table leg. 'Fine.'").
- Make sure each speaker is clear without over-tagging.

### Step 6: Verify With a Read-Aloud

Re-read the revised lines aloud. Confirm they sound like the stated ages, carry subtext, and keep the humor and personality the writer flagged.

---

## Output Format

```markdown
## Dialogue Diagnosis
- Characters / ages: [X]
- Read-aloud clunkers: [cited lines]
- Age-register flags: [adult-isms / dated slang, cited]
- Exposition flags: ["as you know" / plot narration, cited]
- Subtext check: [too on-the-nose? cite]

## Change Ledger
| Original line | Issue | Revised line | Move |
|---------------|-------|--------------|------|
| ... | adult-in-disguise | ... | age down + add subtext |

## Revised Dialogue
[The full revised passage, voice intact]

## Voice/Trade-off Flags
[Where age-true dialogue would cost an intentional joke or tic — writer decides]

## Verification
- Read-aloud pass: [natural? cite a line]
- Subtext present where feelings are big?: [yes/no]
- Signature phrases kept: [list]
```

---

## Example Output

**Character ages:** Theo, 10. **Target reader:** ages 9-12. **Preserve:** Theo's habit of ranking things.

**Dialogue Diagnosis:**
- Read-aloud clunkers: "I am quite upset that you have decided to relocate our family" — no 10-year-old says this.
- Age-register flags: "relocate our family," "I find that deeply unfair" — adult vocabulary and fluency.
- Exposition flags: "As you know, Mom, ever since Dad lost his job last spring..." — both already know this.
- Subtext check: Far too on-the-nose; Theo states his exact feeling.

**Change Ledger (excerpt)**

| Original line | Issue | Revised line | Move |
|---------------|-------|--------------|------|
| "I am quite upset that you have decided to relocate our family." | Adult-in-disguise | "This is the worst idea you have ever had, and you have had a lot of them." | Age down; add ranking tic |
| "As you know, Mom, ever since Dad lost his job last spring..." | "As you know" exposition | [cut; he wouldn't recite this] | Cut exposition |
| "I find that deeply unfair," he exclaimed sadly. | Therapy-speak + adverb tag | "He didn't say anything. He just picked at the tape on the moving box." | Subtext via action beat |

**Revised Dialogue (excerpt):**
> "This is the worst idea you have ever had, and you have had a lot of them."
> Mom sighed. "Theo—"
> He didn't answer. He just picked at the tape on the moving box, peeling it back one slow inch at a time.

**Voice/Trade-off Flags:** None — the ranking tic ("the worst idea... and you've had a lot") carries both humor and hurt. Subtext now does the emotional work instead of a stated feeling.

**Verification:** Reads naturally aloud; subtext present (deflection + action beat instead of "I'm sad"); kept Theo's ranking habit.

---

## Quality Indicators

**Good kid dialogue:**
- [ ] Passes the read-aloud test (sounds spoken, not written)
- [ ] Matches the speaker's age in vocabulary and self-awareness
- [ ] Carries subtext — kids talk around big feelings
- [ ] Reveals character or advances story, not just information
- [ ] Uses "said" + action beats, not adverb-stacked tags
- [ ] Keeps the humor and verbal tics the writer flagged

**Common pitfalls:**

| Pitfall | Sign | Fix |
|---------|------|-----|
| Adult-in-disguise | Kid has adult insight/vocabulary | Age down; make it blunter, smaller |
| On-the-nose emotion | "I feel sad because..." | Add deflection + action beat |
| "As you know" dump | Characters recite shared info | Cut; trust the reader |
| Dated slang | Trendy words, fast shelf life | Prefer timeless, concrete speech |
| Cutesy kid-speak | Lisps/baby-talk for charm | Let the kid be real, not a mascot |

---

## False-Positive Prevention

**DON'T:**
- Make every kid grammatically perfect — real speech is a little messy.
- Strip all humor or a signature phrase to "fix" register; flag the trade-off.
- Assume more slang = more authentic; it dates the book.
- Let characters narrate their own emotional arc.
- Over-tag; readers lose the rhythm.

**DO:**
- Read every line aloud before judging it.
- Calibrate to each speaker's actual age.
- Replace stated feelings with subtext and action beats.
- Keep dialogue doing story work (want, conflict, character).
- Preserve intentional jokes and verbal tics the writer named.

## Related Prompts

- [childrens_character_creation.md](childrens_character_creation.md) — Build the character whose voice the dialogue expresses
- [childrens_middle_grade_fiction_workshop.md](../fiction-workshops/childrens_middle_grade_fiction_workshop.md) — Banter and subtext across a full MG story
- [childrens_age_reading_level_calibrator.md](childrens_age_reading_level_calibrator.md) — Tune the surrounding prose to the same age band
