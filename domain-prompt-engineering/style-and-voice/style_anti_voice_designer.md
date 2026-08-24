---
title: "Anti-Voice Designer"
category: prompt-engineering/style-and-voice
description: "Build an enforced banlist of specific voice tics—em-dashes, hedges, opener phrases—with detection patterns and repair rules."
techniques:
  - ST-01
  - ST-03
  - CM-02
  - QA-01
  - DC-01
difficulty: beginner
tags:
  - banlist
  - anti_voice
  - tics
  - style
  - ai_tells
updated: "2026-05-11"
related_prompts:
  - domain-prompt-engineering/style-and-voice/style_signature_phrase_kill_list.md
  - domain-prompt-engineering/style-and-voice/style_voice_extraction_from_corpus.md
  - domain-prompt-engineering/output-formatting/format_no_preamble_no_postamble.md
---

## Objective

Produce a tic-specific banlist with detection patterns and one-line repair rules for each banned form. The output is a MUST NOT block ready to paste into a system prompt or style guide.

## When to Use

- You have diagnosed unwanted patterns in a model's output (repetitive structure, hedging, opener phrases).
- You want to suppress stylistic defaults without specifying a full positive voice.
- You are building a correction-compounder rule set from session feedback.
- **Not for:** banning factual claims or content categories (use CM-02 content constraints instead).

## Tic Taxonomy

| Category | Examples |
|----------|---------|
| Opener phrases | "Sure,", "Certainly!", "Great question!", "Of course,", "Absolutely," |
| Closer phrases | "I hope this helps!", "Let me know if you need anything else.", "Feel free to ask." |
| Hedge clusters | "it's worth noting that", "it's important to remember", "one might argue", "in many ways" |
| Filler transitions | "Additionally,", "Furthermore,", "Moreover," at paragraph start |
| Em-dash overuse | Using — more than once per 150 words in prose |
| Nested parentheticals | (like this (and this)) |
| Qualifier stacking | "very", "quite", "rather", "somewhat" preceding adjectives |
| Rhetorical questions as headers | "What is X?", "Why does X matter?" |
| Enumeration preamble | "There are three key reasons:" before a list |
| Passive attribution | "It has been suggested that", "It is often said that" |
| Emoji | Any emoji character in formal or neutral register |

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| Tic categories to ban | Yes | Select from taxonomy or add custom |
| Sample outputs showing tics | Recommended | 3–10 paragraphs; tics will be detected |
| Repair style preference | Optional | "delete", "rephrase", "replace with [X]" |

## Constraints

**Must:**
- Produce a detection pattern (regex-like or exact phrase) for each banned tic.
- Produce a one-line repair rule for each tic (what to do instead).
- Test each detection pattern against the provided samples and report hit count.
- Group rules by tic category.

**Must Not:**
- Ban patterns so broadly they catch legitimate uses (e.g., "Additionally" is banned only at paragraph-start, not mid-sentence).
- Produce duplicate entries for the same surface form.
- Exceed 30 total banned patterns — merge closely related tics.

## Instructions

1. **Select or confirm tic categories** from the taxonomy. Add any custom tics from the samples.

2. **For each tic**, produce:
   ```
   TIC [N]: [Category] — [Tic name]
   Detection: [exact phrase or pattern description]
   Scope: [sentence-start | paragraph-start | anywhere | per-N-words ratio]
   Repair: [one-line instruction]
   Sample hits: [count from provided samples, or "not tested"]
   ```

3. **Sort by sample hit count** (highest first). This is the banlist priority order.

4. **Assemble MUST NOT block** in order: opener phrases → closer phrases → hedge clusters → fillers → structural tics → character-level tics.

5. **Write the condensed system-prompt block** (≤150 words, copy-paste ready).

## Output Format

```
## Anti-Voice Banlist

### Tic Details
[TIC block per tic, per step 2]

### MUST NOT Block (copy-paste ready)
MUST NOT:
- Start any response with: "Sure,", "Certainly!", "Great question!", "Of course," or any affirmation.
- End any response with: "I hope this helps!", "Let me know if...", "Feel free to..."
- Use "it's worth noting that" or "it's important to remember" — delete and state directly.
- [...]

### Condensed System Prompt Block (≤150 words)
[Compacted version]

### Detection Report (if samples provided)
| Tic | Pattern | Hits in samples | Severity |
|-----|---------|-----------------|---------|
```

## Verification

- [ ] Every selected tic category has at least one TIC entry.
- [ ] Every TIC entry has a Detection pattern, a Scope, and a Repair line.
- [ ] The condensed block is ≤ 150 words.
- [ ] No detection pattern is so broad it would fire on every use of a common word (e.g., "not" banning "notable").
- [ ] If samples were provided, every TIC entry has a non-null sample-hits value.
