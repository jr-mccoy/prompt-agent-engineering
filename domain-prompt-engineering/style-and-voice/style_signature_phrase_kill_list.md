---
title: "Signature Phrase Kill List"
category: prompt-engineering/style-and-voice
description: "Detect and eliminate AI-signature phrases from a corpus of outputs; produces a frequency-ranked banlist with repair patterns."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - QA-01
  - DC-01
difficulty: beginner
tags:
  - ai_tells
  - banlist
  - signature_phrases
  - style
  - naturalness
updated: "2026-05-11"
related_prompts:
  - domain-prompt-engineering/style-and-voice/style_anti_voice_designer.md
  - domain-prompt-engineering/style-and-voice/style_consistency_audit_across_outputs.md
  - domain-prompt-engineering/output-formatting/format_no_preamble_no_postamble.md
---

## Objective

Analyze a corpus of AI outputs to surface AI-signature phrases—patterns that reveal machine authorship or violate the target voice—then produce a frequency-ranked banlist with per-phrase repair rules for use in system prompts.

## When to Use

- A writer or editor keeps catching the same unnatural phrases across AI drafts.
- You want to harden a system prompt against AI-tell patterns before deployment.
- You are building a proofreading rule set for AI-generated content.
- **Not for:** banning content by topic (use CM-02 content constraints). Not for grammar correction.

## AI-Signature Phrase Categories

| Category | Examples | Why it reads as AI |
|----------|---------|-------------------|
| Affirmation openers | "Certainly!", "Absolutely!", "Of course," | No human writer opens formal text this way |
| Hollow intensifiers | "truly", "indeed", "it is worth noting that" | Add no information; signal filler |
| Summary preambles | "In summary,", "To conclude,", "In conclusion," | Overused in structured AI output |
| Enumeration setups | "There are three key factors:", "First and foremost," | Mechanical; natural prose embeds lists |
| Hedged universals | "In many cases,", "Generally speaking,", "For the most part," | Accurate but reveals uncertainty avoidance |
| Passive knowledge attribution | "It has been widely observed that", "Research suggests that" | Sourced but unmoored |
| Symmetry tells | "Not only X, but also Y", "both X and Y" | Structurally correct but AI-uniform |
| Closing offers | "I hope this helps!", "Please let me know if you have questions." | Servile closer |
| Meta-commentary | "This is an interesting question.", "Let me explain this clearly." | Self-referential |

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| Output corpus | Yes | 5–30 AI-generated text samples; paste delimited by `===SAMPLE N===` |
| Target voice description | Optional | Used to distinguish "on-voice" phrases from "AI-tell" phrases |
| Repair style | Optional | "delete" / "rephrase" / "provide alternatives" |

## Constraints

**Must:**
- Count each phrase occurrence across all samples and report frequency.
- Rank banlist by frequency (highest first).
- Assign every phrase to one of the categories in the taxonomy above; add a new category if a pattern doesn't fit.
- Provide exactly one repair rule per phrase (delete, rephrase, or suggest replacement).
- Cap the banlist at 40 entries; merge phrases with the same repair rule when over the cap.

**Must Not:**
- Ban phrases that appear in only 1 sample unless they appear multiple times within that sample.
- Produce repair rules that are themselves AI-signature phrases (e.g., repairing "In summary" with "To wrap up").
- Include phrases that are only AI-signature in a different register than the target voice.

## Instructions

1. **Scan corpus.** Identify every phrase from the taxonomy categories. Also surface any additional recurring phrase not in the taxonomy.

2. **Frequency table.** Count occurrences per phrase across all samples. Discard any phrase with total count = 1 unless it appears 2+ times in one sample.

3. **Assign categories.** For any phrase not in the taxonomy, create a named category.

4. **Write repair rules.** For each phrase:
   - DELETE if the phrase adds zero information (e.g., "Certainly!").
   - REPHRASE with a specific structural alternative if the phrase pattern is sound but the execution is AI-typical.
   - REPLACE with a named preferred alternative if one exists.

5. **Assemble banlist** sorted by frequency descending, grouped by category.

6. **Write system prompt block** (≤200 words, MUST NOT format).

## Output Format

```
## AI-Signature Phrase Kill List

### Frequency Table
| Phrase | Category | Occurrences | % of samples |
|--------|---------|-------------|-------------|
| "Certainly!" | Affirmation openers | 14 | 93% |
...

### Banlist with Repair Rules
**[Category Name]**
- "Certainly!" → DELETE. Never open with affirmations.
- "It is worth noting that" → DELETE the phrase; start with the claim directly.
...

### System Prompt Block (≤200 words, copy-paste ready)
MUST NOT:
- [...]

### New Categories Found (not in taxonomy)
| Category name | Phrases | Definition |
|--------------|---------|-----------|
```

## Verification

- [ ] Every phrase in the banlist has exactly one repair rule (delete, rephrase, or replace — not a combination).
- [ ] Frequency table entries are sorted descending; ties broken alphabetically.
- [ ] Banlist contains ≤ 40 entries.
- [ ] No phrase in the system prompt block is itself an AI-signature phrase.
- [ ] Every sample in the corpus is referenced at least once in the frequency table (no sample was skipped).
