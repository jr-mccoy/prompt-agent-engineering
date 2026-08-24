---
title: "Precision Document Edit — Tighten Prose for Clarity and Argument Strength While Preserving Voice"
category: professional-writing/writing
description: "Edit a prose passage for clarity, concision, and argument strength while preserving the author's voice and meaning. Produces a markup view with reasons, a clean rewrite, and a voice-and-meaning self-audit."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - QA-01
  - DS-01
difficulty: intermediate
tags:
  - editing
  - line-editing
  - clarity
  - voice-preservation
  - argument
updated: "2026-06-07"
related_prompts:
  - domain-professional-writing/writing/writing_voice_print_extractor.md
  - domain-professional-writing/writing/writing_thesis_builder_essay.md
  - domain-professional-writing/writing/writing_voice_clone_profile_builder.md
---

# Precision Document Edit

**Objective:** Tighten a prose passage so its clarity, concision, and argument are stronger — while preserving the author's voice exactly and changing no meaning — and show the work so the author can accept or reject each change.

**When to Use:**
- A near-final draft (essay, memo, blog post, report section, cover letter) that reads loose, padded, or muddy.
- The author wants edits they can *see and approve*, not a silent rewrite.
- Voice matters: the author wants to still sound like themselves after the edit.
- The argument is sound but the prose buries it.

**When NOT to use:**
- The piece needs structural reorganization or a new argument — edit only tightens what is there; use a thesis or outline prompt first.
- The draft is an early zero draft where ideas are still forming (line-editing too early wastes effort).
- The author wants ghostwriting in a *different* voice — this prompt's whole job is to keep their voice.

**Audience:** Writers, editors, knowledge workers, students, professionals polishing prose for a known reader.

---

## Inputs / Context

Provide as much as you have; the edit improves with each item.

1. **The passage** to edit (paste it; wrap in `<draft>...</draft>`).
2. **Audience and purpose:** who reads this and what they should do or understand after.
3. **Voice notes (optional):** any existing voice print, or a one-line description ("dry, plain, no jargon"). If omitted, infer voice from the draft itself.
4. **Hard constraints:** length target (shorten by X%, keep under N words, or "no length change"), forbidden words, required terms, tone.
5. **What must not change:** specific claims, numbers, names, quotes, or sentences the author considers load-bearing.

If audience/purpose are missing, state the assumption you are editing under at the top, and proceed — do not stall.

---

## Constraints

### Must
- Preserve the author's **voice**: sentence-length rhythm, characteristic diction, signature moves, and register. Edits should sound like a sharper version of the same writer.
- Preserve **meaning**: every claim, qualification, number, name, and nuance in the source survives unless removing it is an explicit instruction.
- Show **every substantive change** in the markup view with a brief reason (≤8 words).
- Cut for **concision** first (filler, redundancy, throat-clearing, nominalizations, hedge-stacking), then sharpen **clarity** (ambiguous referents, buried subjects, weak verbs), then strengthen **argument** (claim ordering, missing connective logic that is *already implied*).
- Produce three artifacts in order: markup view, clean rewrite, self-audit.
- Flag — but do not invent — any place where the argument has a genuine gap, as a question to the author, not a fabricated fix.

### Must Not
- Flatten voice into generic "clean" prose (the most common failure of automated editing).
- Introduce any new claim, fact, statistic, citation, or example not present in or directly entailed by the source.
- Change the author's stance, certainty level, or emphasis to make the piece "safer."
- Silently delete a sentence the author may have intended — cut visibly with a reason, or query it.
- Resolve a factual gap by guessing; surface it instead.

---

## Instructions

1. **Read for voice before editing.**
   - Note sentence-length pattern (varied? clipped? long and subordinated?), diction tier (plain / formal / technical), and 2–3 signature moves (rhetorical questions, em-dash asides, parallel triads, understatement). Hold these as constraints, not targets to remove.

2. **Pass 1 — Concision.**
   - Remove filler ("in order to," "the fact that," "it is important to note"), redundant pairs, throat-clearing openers, and dead nominalizations ("make a decision" → "decide"). Each cut must leave meaning intact.

3. **Pass 2 — Clarity.**
   - Fix ambiguous pronoun referents, restore buried subjects, convert weak verb + abstract noun into a strong verb, and split sentences only where a reader would otherwise lose the thread. Do not standardize the author's varied rhythm into uniformity.

4. **Pass 3 — Argument strength.**
   - Reorder sentences only where it makes the *existing* logic land harder (claim before evidence, or evidence before claim — whichever the passage already favors). Surface implied connective logic with the author's own words where it's missing. Do not add new reasoning.

5. **Flag gaps, don't fill them.**
   - Where a claim lacks support that the text does not supply, mark it as an open question for the author. Never fabricate a citation, statistic, or example.

6. **Verify voice and meaning preserved (CRITICAL).**
   - Compare rewrite to source claim-by-claim. Confirm no claim added, dropped, or shifted in certainty. Re-read the rewrite as the author: does it still sound like them? Record this in the self-audit.

7. **Assemble output:** markup view (with reasons) → clean rewrite → self-audit.

---

## False-Positive Prevention

1. **Voice-flattening masquerading as "clarity."** Replacing a writer's clipped fragments or em-dash asides with smooth, uniform sentences is not an improvement — it is a different voice. Keep characteristic rhythm even when it is "irregular."
2. **Smuggled new claims.** A rewrite that adds "studies show" or a concrete number that was not in the source has invented content. Every fact in the rewrite must trace to the source.
3. **Certainty drift.** Turning "this probably helps" into "this helps" (or vice versa) changes meaning. Preserve hedges and intensifiers exactly unless told to adjust.
4. **Over-cutting nuance as "filler."** Qualifiers like "in most cases" or "for early-stage teams" are often load-bearing, not padding. Cut only true filler.
5. **Structural rewrite in disguise.** Reordering whole paragraphs or changing the argument is out of scope; if the piece needs that, say so rather than doing it silently.
6. **Reason-free markup.** Every change in the markup view needs a reason; unreasoned changes hide voice/meaning drift.
7. **Filling argument gaps with invention.** A missing piece of evidence is a question for the author, never a fabricated fill.

---

## Output Format

```
## Markup View
> Original sentence with ~~cut text~~ and [added/changed text] inline.
- Reason: [≤8 words, e.g., "cut filler", "weak verb → strong"]

> [next changed sentence]
- Reason: [...]

(Unchanged sentences may be omitted or shown as "[unchanged]".)

## Clean Rewrite
[The fully edited passage, ready to use — no markup, no annotations.]

## Self-Audit
- **Length:** [original N words → edited M words, X% change vs. target]
- **Voice preserved:** [1–2 lines: rhythm/diction/signature moves retained; cite one example sentence that proves voice survived]
- **Meaning unchanged:** [confirm no claim added/dropped/shifted; note any certainty wording deliberately kept]
- **Open questions for author:** [argument gaps surfaced, NOT filled — or "none"]
- **Edits the author may want to reject:** [any judgment calls flagged for review]
```

---

## Verification

- [ ] Markup view shows every substantive change with a ≤8-word reason.
- [ ] Clean rewrite is usable as-is, with no markup or annotation bleed-through.
- [ ] No new claim, fact, statistic, citation, or example appears in the rewrite.
- [ ] Hedges, qualifiers, and certainty wording are preserved (or changes are flagged).
- [ ] Author's sentence rhythm and signature moves survive (one example cited in audit).
- [ ] Argument gaps are surfaced as questions, not fabricated fixes.
- [ ] Length change matches the stated target (or assumption stated if none given).
- [ ] Self-audit explicitly confirms voice preserved and meaning unchanged.
