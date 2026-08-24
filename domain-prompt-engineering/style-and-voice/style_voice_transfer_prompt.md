---
title: "Voice Transfer Prompt"
category: prompt-engineering/style-and-voice
description: "Apply a target voice specification to a source text without altering any factual claims."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - QA-01
  - DC-01
difficulty: intermediate
tags:
  - voice
  - style_transfer
  - rewriting
  - facts_preservation
  - writing
updated: "2026-05-11"
related_prompts:
  - domain-prompt-engineering/style-and-voice/style_voice_extraction_from_corpus.md
  - domain-prompt-engineering/style-and-voice/style_register_control.md
  - domain-prompt-engineering/style-and-voice/style_consistency_audit_across_outputs.md
---

## Objective

Rewrite a source text in a specified target voice without adding, removing, or distorting any factual claim. Output is the rewritten text plus a change ledger classifying every edit as voice-only or fact-touching.

## When to Use

- You have a voice rule set (from corpus extraction or brand guidelines) and need to apply it to new copy.
- Ghostwriting to match an existing author's voice.
- Adapting a draft written in the wrong register.
- **Not for:** translations between languages (different task). Not for content where all of the original wording is legally locked.

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| Source text | Yes | The text to rewrite |
| Voice rules | Yes | ≥ 5 operational rules; use style_voice_extraction_from_corpus output format |
| Fact-lock list | Optional | Specific phrases/sentences that must survive verbatim |
| Length constraint | Optional | Target word count ± 10% |

## Constraints

**Must:**
- Preserve every factual claim present in the source (numbers, names, dates, causal claims, attributed quotes).
- Apply every voice rule provided; do not selectively ignore rules.
- Produce a change ledger listing every sentence modified, with change type: `VOICE` or `FACT-TOUCH`.
- Flag any rule that conflicts with fact preservation (e.g., a rule to shorten sentences may force splitting a sentence with an embedded number).
- Keep all attributed quotes verbatim unless the rule explicitly permits paraphrase.

**Must Not:**
- Add examples, analogies, or elaborations not present in the source.
- Remove a factual claim to satisfy a brevity rule — instead flag the conflict.
- Change any date, number, statistic, or proper noun.
- Claim a rewrite is complete if any voice rule was skipped.

## Instructions

1. **Parse source.** Number every sentence S1, S2, … Sn. Extract all fact-tokens: numbers, proper nouns, dates, attributed quotes, causal claims ("because", "therefore", "as a result").

2. **Build rewrite plan.** For each sentence, list which voice rules apply and what change each requires. Identify conflicts: cases where two rules contradict each other, or where a voice rule would force a fact change.

3. **Execute rewrite.** Apply rules sentence by sentence. Where a conflict exists, apply the higher-ranked rule and log the conflict.

4. **Generate change ledger.**
   ```
   S[N]: [VOICE | FACT-TOUCH | UNCHANGED | CONFLICT]
   Original: "..."
   Rewritten: "..."
   Rules applied: [rule numbers]
   Note: [only if CONFLICT or FACT-TOUCH]
   ```

5. **Summary block:**
   - Total sentences: N
   - VOICE changes: N
   - UNCHANGED: N
   - FACT-TOUCH (required inspection): N
   - CONFLICT (rules skipped or overridden): N
   - Voice rules not fired (no applicable sentences): [list]

## Output Format

```
## Rewritten Text
[Full rewritten text]

---

## Change Ledger
[Sentence-by-sentence table per step 4]

## Summary
[Block per step 5]

## Rule Coverage
| Rule # | Rule summary | Fired? | Times applied |
|--------|-------------|--------|---------------|
```

## Verification

- [ ] Every fact-token from the source appears in the rewritten text unchanged.
- [ ] No sentence in the change ledger is missing.
- [ ] Every voice rule appears in the Rule Coverage table with a Fired? column entry.
- [ ] FACT-TOUCH and CONFLICT entries exist in the ledger if any were encountered — a ledger with zero FACT-TOUCH entries when the source is dense with numbers warrants re-check.
- [ ] The rewrite does not introduce any sentence not derivable from the source.
