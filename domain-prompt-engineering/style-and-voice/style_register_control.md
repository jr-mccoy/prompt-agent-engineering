---
title: "Register Control"
category: prompt-engineering/style-and-voice
description: "Rewrite or generate text at a specified formality register with banned and required linguistic forms per level."
techniques:
  - ST-01
  - ST-03
  - CM-02
  - QA-01
  - ST-16
difficulty: beginner
tags:
  - register
  - formality
  - style
  - rewriting
  - tone
updated: "2026-05-11"
related_prompts:
  - domain-prompt-engineering/style-and-voice/style_voice_transfer_prompt.md
  - domain-prompt-engineering/style-and-voice/style_audience_adaptation_prompt.md
  - domain-prompt-engineering/style-and-voice/style_anti_voice_designer.md
---

## Objective

Rewrite a piece of text at a target formality level (Formal / Neutral / Casual) using explicit banned and required linguistic forms. No subjective interpretation of "tone" — every edit is grounded in the rule table below.

## When to Use

- A draft is at the wrong register for its audience (too stiff for a blog, too casual for a contract cover letter).
- You need three register variants of the same content.
- You are building a register-control block for a system prompt.
- **Not for:** domain-specific jargon management (that is vocabulary, not register).

## Register Rule Table

| Feature | FORMAL | NEUTRAL | CASUAL |
|---------|--------|---------|--------|
| Contractions | Banned (do not → must not; it's → it is) | Permitted sparingly | Required or strongly preferred |
| First person singular ("I") | Avoid unless necessary | Permitted | Preferred |
| Passive voice | Permitted for objectivity | Use sparingly | Banned except set phrases |
| Sentence length | Mean ≥ 18 words | Mean 14–18 words | Mean ≤ 14 words |
| Sentence fragments | Banned | Banned | Permitted for emphasis |
| Hedges ("perhaps", "might") | Required when uncertain | Permitted | Prefer direct assertion |
| Colloquialisms | Banned | Banned | Permitted (e.g., "get", "a lot") |
| Latin/Latinate vocabulary | Preferred ("commence" vs "start") | Either | Anglo-Saxon preferred ("start") |
| Exclamation marks | Banned | Max 1 per 500 words | Permitted |
| Sentence-opening conjunctions ("And", "But") | Banned | Permitted once per 300 words | Permitted freely |
| Parentheticals | Permitted | Permitted | Preferred over em-dashes or subordinate clauses |
| Numbered/bulleted lists | Use sparingly; prefer prose | Freely permitted | Freely permitted |

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| Source text | Yes | Text to rewrite |
| Target register | Yes | FORMAL / NEUTRAL / CASUAL |
| Fact-lock | Optional | Claims that must survive unchanged |
| Length tolerance | Optional | Default ±15% of source word count |

## Constraints

**Must:**
- Apply every rule in the register table for the target level.
- Report word count before and after.
- Flag any source sentence where register compliance required changing a fact-token.

**Must Not:**
- Change factual claims, numbers, dates, or proper nouns to satisfy register rules.
- Apply FORMAL rules to a CASUAL target or vice versa — use the column for the requested register only.
- Use vague qualifiers in the audit ("mostly formal", "generally matches") — report specific rule compliance per category.

## Instructions

1. **Classify source.** Run the source through the register table at its current register. Record which rules it already satisfies and which it violates. This is the baseline.

2. **Rewrite.** Modify the text to satisfy all rules for the target register. Prioritize in this order: contractions → sentence length → vocabulary tier → passive voice → conjunctions.

3. **Audit.** For each row in the rule table, confirm the rewritten output satisfies it. Mark ✓ or ✗. If ✗, note which sentences still violate.

## Output Format

```
## Rewritten Text ([TARGET REGISTER])
[Text]

Word count: [before] → [after]

## Register Audit
| Feature | Required for [TARGET] | Result | Violations (sentence #) |
|---------|----------------------|--------|-------------------------|
| Contractions | [rule] | ✓/✗ | — |
| First person | [rule] | ✓/✗ | — |
| Passive voice | [rule] | ✓/✗ | [S3, S7] |
...

## Compliance Score: [N/12 rules satisfied]
```

## Verification

- [ ] Every row in the register audit table has a ✓ or ✗ — no blanks.
- [ ] Any ✗ row lists specific sentence numbers, not "see above."
- [ ] Word count delta is within ±15% unless a length constraint was provided.
- [ ] No fact-tokens (numbers, names, dates) differ between source and rewrite.
- [ ] Compliance score matches the count of ✓ rows.
