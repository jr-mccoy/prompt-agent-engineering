---
title: "Voice Extraction from Corpus"
category: prompt-engineering/style-and-voice
description: "Codify a distinctive writing voice from 5+ samples into an operational rule set reusable in prompts."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - voice
  - style
  - corpus_analysis
  - rule_extraction
  - writing
updated: "2026-05-11"
related_prompts:
  - domain-prompt-engineering/style-and-voice/style_voice_transfer_prompt.md
  - domain-prompt-engineering/style-and-voice/style_anti_voice_designer.md
  - domain-prompt-engineering/style-and-voice/style_consistency_audit_across_outputs.md
---

## Objective

Extract an operational voice specification from a corpus of 5–20 text samples. Output is a ranked rule set with positive examples, negative counterexamples, and a self-test to confirm the rules fire correctly.

## When to Use

- You have a writer's existing work and want to reproduce their voice in new content.
- You are building a brand voice guide from historical copy samples.
- You need to encode voice rules into a system prompt or style guide.
- **Not for:** voices with fewer than 5 samples (insufficient signal).

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| Text corpus | Yes | 5–20 samples, each 100–1000 words |
| Domain label | Yes | e.g., "tech blog", "legal memo", "marketing email" |
| Audience description | Recommended | Who the samples were written for |
| Contrast corpus | Optional | 3–5 samples in a voice you want to distinguish from |

Paste samples delimited by `===SAMPLE N===` markers.

## Constraints

**Must:**
- Produce ≥ 8 and ≤ 20 operational rules.
- Each rule must be falsifiable: state what it bans and what it requires.
- Each rule must cite a specific phrase or sentence from the corpus as evidence.
- Rank rules by signal strength: how many samples exhibit the pattern (n/total).
- Include at least one rule about sentence length or cadence.
- Include at least one rule about vocabulary register (word choice level).
- Include at least one rule about structural pattern (how paragraphs open/close).

**Must Not:**
- State subjective descriptors like "warm", "approachable", or "clear" without operational grounding.
- Invent rules not evidenced in the corpus.
- Produce duplicate rules with different labels.
- Include formatting rules (font, layout) — those belong in output-formatting prompts.

## Instructions

1. **Signal extraction pass.** Read all samples and list every recurring pattern across ≥ 3 samples. Patterns to look for:
   - Average sentence length (short / medium / long: <12 / 12–20 / 20+ words)
   - Punctuation habits (em-dashes, semicolons, parentheticals, Oxford comma)
   - Sentence openers (how often starts with "I", a subordinate clause, an imperative, a question)
   - Vocabulary tier (Latinate vs Anglo-Saxon; technical vs colloquial)
   - Transition style (explicit connectors vs. juxtaposition)
   - Rhetorical moves (analogy frequency, question-as-header, numbered enumeration)
   - Hedging frequency (count: "perhaps", "might", "could", "seems to")
   - Active vs. passive verb ratio

2. **Rule formulation.** Convert each pattern into a rule:
   ```
   RULE [N]: [Imperative statement]
   Evidence: "[exact phrase from corpus]" (Sample N)
   Signal strength: [x]/[total] samples
   Positive form: [what to do]
   Negative form: [what to ban]
   ```

3. **Rank rules** from highest to lowest signal strength. Break ties by impact (rules covering sentence structure rank above punctuation rules).

4. **Contrast check** (if contrast corpus provided). For each rule, verify it does NOT describe the contrast corpus. Flag any rules that apply to both as "low discriminating power."

5. **Self-test.** Apply the top 5 rules to one held-out sample not used in extraction. Count how many rules are satisfied. Report: `[N]/5 rules satisfied on held-out sample.`

## Output Format

```
## Voice Specification: [Domain Label]
**Corpus size:** N samples | **Total words analyzed:** ~N

### Ranked Rules

| # | Rule | Signal | Positive Form | Banned Form |
|---|------|--------|---------------|-------------|
| 1 | ... | N/N | ... | ... |
...

### Rule Details
[Full RULE block per rule, with evidence quote and sample reference]

### Self-Test Result
Held-out sample: Sample [N]
Rules satisfied: [N]/5
Rule failures: [list any rule not satisfied with reason]

### Recommended System Prompt Block
[Copy-paste ready rule block condensed to ≤150 words for use in prompts]
```

## Verification

- [ ] Each rule cites a specific corpus phrase — no rule is purely inferential.
- [ ] Signal strength fractions sum correctly against corpus size.
- [ ] The recommended system prompt block contains no vague descriptors (scan for: "warm", "engaging", "clear", "comprehensive", "appropriate").
- [ ] Self-test reports a concrete pass/fail ratio, not a qualitative judgment.
- [ ] Rule count is between 8 and 20.
