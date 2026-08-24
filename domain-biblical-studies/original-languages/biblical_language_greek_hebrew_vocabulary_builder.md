---
title: "Greek & Hebrew Vocabulary Builder — Frequency-Based Study Plan — Structured, Anti-Fabrication"
category: biblical-studies/original-languages
description: "Design a staged, frequency-based vocabulary acquisition plan for Biblical Greek or Biblical Hebrew — organizing words by frequency tiers (most common first), integrating spaced repetition and reading-in-context checkpoints, and calibrating the schedule to the user's time budget — treating every word-list datum (frequency count, gloss, semantic range, principal parts, cognate claim) as candidate / verify-required against standard frequency lists and lexica, and never asserting specific word data from memory."
techniques:
  - ST-02
  - RT-02
  - RT-05
  - QA-04
  - QA-05
  - OC-12
difficulty: intermediate
tags:
  - vocabulary
  - greek
  - hebrew
  - frequency-lists
  - language-learning
  - spaced-repetition
  - anti-fabrication
updated: "2026-06-25"
related_prompts:
  - domain-biblical-studies/original-languages/biblical_language_parsing_morphology_helper.md
  - domain-biblical-studies/original-languages/biblical_language_greek_syntax_analysis.md
  - domain-biblical-studies/original-languages/biblical_language_hebrew_syntax_analysis.md
  - domain-biblical-studies/exegesis-interpretation/biblical_word_study_original_language.md
  - domain-biblical-studies/learner-self-study/biblical_learner_self_directed_study_plan.md
---

# Greek & Hebrew Vocabulary Builder — Frequency-Based Study Plan

**Objective:** Design a staged vocabulary acquisition plan for Biblical Greek or Biblical Hebrew, organized by word frequency so the user learns the highest-yield words first. The plan includes frequency tiers, study methods (flashcards, reading-in-context, spaced repetition), a schedule calibrated to the user's time commitment, and progress checkpoints — **without asserting any word's frequency count, gloss, semantic range, principal parts, or cognate relationship from memory as authoritative.** The output is a study architecture the user populates and verifies against real frequency lists and lexica.

> **STRONG-GUARD prompt.** Models routinely fabricate word frequencies, misremember glosses, assert semantic ranges that are incomplete or misleading, and present one gloss as THE meaning of a word. A vocabulary plan built on fabricated frequencies teaches the wrong words first; a plan built on fabricated glosses teaches the wrong meanings. All vocabulary data is **verify-required** against standard frequency lists and lexica. The model designs the *study architecture* and explains the *method*; the user supplies and verifies all specific linguistic data.

**When to use:**
- You are beginning (or restarting) Biblical Greek or Hebrew vocabulary study and want a structured, frequency-first plan rather than random word lists.
- You want to design a vocabulary plan targeted at reading a specific biblical book or corpus.
- You want to integrate vocabulary study with a reading goal, exam preparation, or a grammar course.

**When NOT to use:**
- You need authoritative frequency data — go to a published frequency list. This prompt designs the *architecture* of your study; it does not replace the word list.
- Your question is parsing or morphology of a specific form — use `biblical_language_parsing_morphology_helper.md`.
- Your question is the *semantic range* or theological significance of a word — use `biblical_word_study_original_language.md` (in `exegesis-interpretation/`).
- Your question is syntax within a clause — use `biblical_language_greek_syntax_analysis.md` or `biblical_language_hebrew_syntax_analysis.md`.

**Audience:** Seminary/academic (A), pastors (P), and self-directed learners (S) at any level.

---

## Inputs / Context

1. **Language.** Biblical Greek (NT, LXX, or both), Biblical Hebrew, or both languages.
2. **Current level.** Absolute beginner (no vocabulary), some vocabulary (estimate how many words / which resource you used), or intermediate (can read simple passages with help).
3. **Goal.** One or more of: read a specific biblical book with minimal lexicon use; general reading fluency across the NT or HB; exam preparation (name the exam if relevant); supplement a grammar course (name the textbook if relevant).
4. **Time commitment.** Minutes per day and days per week available for vocabulary study specifically.
5. **Preferred study methods (optional).** Flashcards (paper/Anki/Quizlet), reading-in-context, writing, audio, or "recommend something."
6. **Known vocabulary (optional).** Any word list already learned (e.g., "I know all words occurring 50+ times in the NT" or "I completed Mounce chapters 1-20").

---

## Constraints

### Must
- Organize the plan by **frequency tiers** (most common words first), because frequency-based acquisition maximizes text coverage per word learned — this is the load-bearing design principle.
- Treat every word-list datum — frequency count, gloss, principal parts (Greek verb forms), construct/segolate patterns (Hebrew), semantic range, and cognate claims — as **candidate / verify-required** against a named, real frequency list or lexicon.
- Name the *kinds* of published frequency resources the user should use to populate the plan — but **flag specific resource titles, editions, and word counts as verify-required** because editions change and the model may misremember.
- Where semantic-field grouping aids retention (e.g., learning body-part words together, or prepositions as a set), use it as a secondary organizer within a frequency tier — never let semantic grouping override frequency order.
- Calibrate the study pace to the user's stated time commitment, with explicit assumptions (e.g., "assumes ~5 new words per 15-minute session using spaced repetition").
- Include a review/retention layer — spaced repetition, reading-in-context checkpoints, or both — not just a list of words to learn.
- Include common pitfalls specific to vocabulary study (glossing vs. understanding semantic range, neglecting morphological families, abandoning frequency order for "interesting" words).

### Must Not
- Assert a word's frequency count from memory (e.g., "this word occurs 330 times") — give the frequency *tier* (e.g., "words occurring 100+ times") and instruct the user to verify the exact count.
- Assert a gloss from memory as the gloss — give a candidate gloss flagged verify-required and instruct the user to confirm in a lexicon.
- Present one gloss as THE meaning of a word when the word has a genuine semantic range; note that glosses are shortcuts and route to a word-study process for theologically significant terms.
- Assert principal parts (Greek) or construct/segolate patterns (Hebrew) from memory — flag them as verify-required.
- Generate a complete vocabulary list with glosses from memory — design the *architecture* and point to real sources.
- Quote or reproduce copyrighted word lists; design the study architecture, not the word list itself.

### Tradition-neutral stance (Must / Must Not)
- **Must:** where a word's gloss or semantic range is theologically contested (e.g., words translated differently by different traditions), note that the gloss is debated and route to a word-study process rather than asserting one tradition's rendering.
- **Must Not:** embed a tradition-specific gloss as the "correct" meaning of a vocabulary word without noting alternatives.

---

## Instructions

### Step 1 — Confirm language, learner level, and goal
Confirm the user's language (Greek, Hebrew, or both), current level, goal, and time budget. Estimate what vocabulary coverage is needed for the goal (e.g., "knowing all words occurring 10+ times in the NT covers a substantial percentage of running words — verify this figure against a published frequency analysis"). Set a target vocabulary size and timeline, with the coverage estimate flagged **candidate (verify)**.

### Step 2 — Design frequency-tier plan (most frequent words first)
Divide the target vocabulary into frequency tiers, working from most common to least common. Suggested tier structure (adjust to the user's level and goal):

- **Tier 1:** Words occurring at the highest frequency band — learn first.
- **Tier 2:** Words occurring in the next band — learn after Tier 1 is solid.
- **Tier 3:** Words occurring in the next band — and so on.
- **Book-specific tier (if goal is a specific book):** Words that are high-frequency *in that book* but not in the corpus overall.

For each tier, state the approximate number of words and the cumulative text-coverage percentage — both flagged **candidate (verify against a frequency list)**. Note that different frequency lists use different corpora and counting methods (by lemma vs. by form; inclusion/exclusion of Aramaic portions); the tier structure survives even if exact counts differ.

### Step 3 — Vocabulary acquisition method (flashcard, reading, spaced repetition)
For each tier, recommend a study method calibrated to the user's preferences and time budget:
- **Spaced-repetition flashcards:** Paper, Anki, Quizlet, or other — explain the principle (increasing intervals for known words, shorter intervals for difficult words). Recommend card design (lexical form + hints on front; candidate gloss (verify) + passage ref on back).
- **Reading-in-context:** After each tier, read passages where the learned words appear — vocabulary learned without context does not stick. Name the *type* of resource (reader, graded text, interlinear) but flag specific titles as verify-required.
- **Writing/production and audio:** Secondary methods — composing phrases (stronger retention, higher time cost) and hearing pronunciation (useful for liturgical or spoken contexts).

### Step 4 — Integration with reading plan
Connect the vocabulary plan to the user's reading goals:
- **Checkpoint readings:** After each tier, suggest a passage type (narrative for beginners, epistolary for intermediate) where learned vocabulary appears. Name the resource *type* but flag specific titles as verify-required.
- **Reading-log format:** Track unknown words during reading — words appearing repeatedly become candidates for the next study tier.
- **Grammar-course alignment (if applicable):** Map tiers to textbook chapters, flagged **candidate (verify against the textbook's own word lists)**.

### Step 5 — Progress checkpoints
Define milestones: when to advance to the next tier (e.g., "90% unprompted recall within 3 seconds"), periodic full-tier retention checks, and reading fluency checks (can you read a target passage without looking up more than N words per verse?).

### Step 6 — Common pitfalls in vocabulary study
Flag the most common failure modes:
- **Glossing vs. semantic range:** A single gloss is a memory shortcut, not a definition; route theologically significant words to a word-study process.
- **Abandoning frequency order:** Skipping high-frequency words for low-frequency "interesting" ones produces poor text coverage.
- **Neglecting morphological families:** Learning a root unlocks related words in both Greek and Hebrew — leverage this.
- **No retention system:** Spaced repetition is non-negotiable; learning 20 words and forgetting 15 is worse than learning 10 and retaining 9.
- **Fabricated frequency data:** If using AI-generated word lists, verify every frequency and gloss against a published source.

---

## Output Format

```
# Vocabulary Acquisition Plan — [Language] — [Goal]

## Starting point & target
- Language: [Greek / Hebrew / both]
- Current level: [..] | Known vocabulary: [..]
- Goal: [..] | Target vocabulary size: [~N words] (candidate, verify)
- Time budget: [X min/day, Y days/week]
- Coverage estimate: [~Z% of running words at target] (candidate — VERIFY against a published frequency analysis)

## Frequency tiers (candidate — VERIFY word counts and coverage against a published frequency list)
| Tier | Frequency band | Approx. word count | Cumulative coverage (candidate) | Priority |
|------|---------------|-------------------|--------------------------------|----------|
| 1 | [e.g., 100+ occurrences] | candidate (verify) | candidate (verify) | Learn first |
| 2 | [e.g., 50-99 occurrences] | candidate (verify) | candidate (verify) | After Tier 1 solid |
| 3 | [..] | candidate (verify) | candidate (verify) | [..] |
| Book-specific | [high in target book, low overall] | candidate (verify) | — | [after core tiers / interleaved] |

## Study method & schedule
- Method per tier: [recommended method] (assumption: [stated retention assumption])
- Card design: [front: lexical form + hints | back: candidate gloss (verify) + passage ref]
- New words: [N] per session x [sessions/week] = [N/week]
- Review: [spaced-repetition schedule]
- Reading checkpoint after Tier [N]: [passage type] (resource type: [..], title verify-required)
- Advance to next tier when: [criterion, e.g., 90% unprompted recall]
- Projected timeline: Tier 1 by [week N], Tier 2 by [week N] (candidate — depends on actual retention)

## Pitfalls
- Glossing vs. semantic range → [mitigation]
- Abandoning frequency order → [mitigation]
- No retention system → [mitigation]

## Verification map & tools
- Frequency list: [resource type] (specific title/edition: verify-required)
- Lexicon for glosses: [resource type] (specific title: verify-required)
- Spaced-repetition tool: [type recommendation]
- Tagged text / reader: [resource type] (specific title: verify-required)
- Coverage-estimate source: [verify the Z% figure against a published frequency analysis]

## Confidence
- Plan architecture: high (frequency-first is well-established pedagogy)
- Specific word counts / coverage %: candidate (verify) — depend on which frequency list and counting method
- Most important verification step: [..]
```

---

## Verification

- [ ] No frequency count, gloss, principal part, semantic range, or cognate relationship asserted as fact — all flagged candidate/verify-required.
- [ ] Plan organized by frequency tiers (most common first); semantic grouping secondary only.
- [ ] No copyrighted word list reproduced — the plan is an *architecture* the user populates from real sources.
- [ ] Specific resource titles/editions flagged verify-required — not asserted as current or complete.
- [ ] Coverage estimates flagged candidate (verify against a published analysis).
- [ ] Study pace calibrated to user's stated time commitment with explicit assumptions.
- [ ] Theologically contested glosses noted as debated, not presented as settled.
- [ ] Review/retention layer and common pitfalls section included.

---

## False-Positive Prevention

❌ **DON'T:**
- Assert specific frequency counts from memory (e.g., "this word occurs 330 times in the NT") — give the frequency tier and instruct the user to verify the count in a published list.
- Generate a complete vocabulary list with glosses from memory — this will contain errors; design the *architecture* and point to real sources.
- Present one gloss as THE meaning of a word when it has a genuine semantic range — glosses are memory shortcuts, not definitions.
- Invent a cognate or etymology to serve as a mnemonic (e.g., claiming a Hebrew word derives from a root you are not certain about).
- Present a single frequency list as the only valid source when different lists use different corpora and counting methods.

✅ **DO:**
- Flag every word-list datum (count, gloss, principal parts, semantic range) as candidate (verify) and name the resource type where the user confirms it.
- Use frequency *tiers* (bands) rather than asserting specific counts — the tier structure survives even if exact counts differ between published lists.
- Note where a word's gloss is theologically contested and route to a word-study process rather than asserting one tradition's rendering.
- Include review/retention structure and reading-in-context checkpoints — vocabulary learned without context does not stick.
- Calibrate the plan to the user's actual time budget rather than prescribing an ideal schedule they cannot sustain.

---

## Techniques Used

- **ST-02 (Structured Sequential Instructions):** The 6-step sequence (Confirm level → Design tiers → Acquisition method → Reading integration → Progress checkpoints → Common pitfalls) ensures the plan is built frequency-first and calibrated to the user before any word-level content is offered.
- **RT-02 (Multi-Dimensional Analysis Framework):** Requires the plan to address multiple dimensions — frequency tiers, study method, reading integration, retention system, progress milestones, and pitfall avoidance — so no single dimension (e.g., a raw word list) is mistaken for a complete plan.
- **RT-05 (Evidence-Based Reasoning):** Every word-level datum is grounded in a named resource type or flagged unverified; coverage estimates require published frequency analysis; the plan's design principle (frequency-first) is evidence-based pedagogy.
- **QA-04 (Uncertainty Acknowledgment):** Every word-level datum is flagged candidate (verify); coverage estimates carry confidence labels; the plan acknowledges that different frequency lists count differently and that specific counts may vary.
- **QA-05 (Citation Requirements):** Requires naming the resource *type* for every datum and explicitly flags specific resource titles, editions, frequency counts, and glosses as verify-required — never asserted from memory.
- **OC-12 (External Reference Catalog):** The verification map catalogs the resource types (published frequency list, lexicon, spaced-repetition tool, tagged text/reader) needed to populate and validate the study plan.
