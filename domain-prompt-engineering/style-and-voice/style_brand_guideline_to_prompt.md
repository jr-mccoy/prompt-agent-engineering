---
title: "Brand Guideline to Prompt Rules"
category: prompt-engineering/style-and-voice
description: "Convert a brand style or voice guideline document into an enforceable, copy-paste-ready prompt rule block."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - brand_voice
  - style_guide
  - prompt_engineering
  - guidelines_conversion
  - writing
updated: "2026-05-11"
related_prompts:
  - domain-prompt-engineering/style-and-voice/style_voice_extraction_from_corpus.md
  - domain-prompt-engineering/style-and-voice/style_anti_voice_designer.md
  - domain-prompt-engineering/style-and-voice/style_signature_phrase_kill_list.md
---

## Objective

Transform a brand guideline document into a compact, operationally enforceable prompt rule block. The output can be pasted directly into a system prompt and tested without further interpretation.

## When to Use

- A brand team has a style guide and wants AI outputs to match it.
- A new writer is onboarding and needs the guide translated into model-usable rules.
- An existing system prompt produces off-brand outputs; you need to diagnose which guideline sections are missing.
- **Not for:** visual/design guidelines (colors, fonts, logos) — those are not prompt-enforceable.

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| Brand guideline text | Yes | Paste the full text or relevant sections |
| Target output type | Yes | e.g., "social media captions", "support emails", "blog posts" |
| Known failure examples | Optional | 2–5 recent AI outputs the brand team rejected |
| Known success examples | Optional | 2–5 outputs the brand team approved |

## Constraints

**Must:**
- Classify every guideline statement into exactly one of four enforceability tiers (see table below).
- Produce only Tier 1 and Tier 2 rules in the output rule block — Tier 3/4 are flagged but excluded.
- Each rule must contain a banned form, a required form, or both.
- Test the rule block against the provided failure examples: each failure must violate ≥ 1 rule.
- Test the rule block against the provided success examples: each success must satisfy all rules.

**Must Not:**
- Include personality adjectives ("friendly", "bold", "inspirational") in the rule block without operational grounding.
- Produce more than 20 rules in the final block — merge redundant rules.
- Invent rules not derivable from the provided guidelines.

## Enforceability Tiers

| Tier | Definition | Disposition |
|------|-----------|-------------|
| 1 — Lexical | Specific words/phrases banned or required | Include |
| 2 — Structural | Sentence length, list use, punctuation patterns | Include |
| 3 — Tonal | Adjectives describing mood/feeling with no lexical anchor | Flag as unenforceable; note in report |
| 4 — Visual | Font, color, layout | Exclude silently |

## Instructions

1. **Parse guidelines.** Read the full document. For each guideline statement, assign a tier, and extract the operational kernel:
   ```
   Statement: "We speak like a trusted friend, never corporate."
   Tier: 3 (tonal) → Flag: convert to lexical or exclude
   Anchored form (if convertible): Ban: "please be advised", "per our records", "as per"; Require: contractions
   ```

2. **Convert Tier 3 statements** by asking: "What words would a model write that violates this principle?" Use the answer to generate Tier 1 banned-forms.

3. **Draft rule block.** Format as MUST / MUST NOT lists with ≤20 rules total.

4. **Test against examples.** For each failure: list which rules it violates. For each success: confirm it satisfies all rules. If a failure violates zero rules, add a new rule to catch it. If a success violates a rule, revise the rule.

5. **Report unenforceable guidelines.** List Tier 3 statements that could not be converted, with suggested human-review actions.

## Output Format

```
## Brand Voice Rule Block (copy-paste ready)

MUST:
- [Rule 1: specific positive requirement]
- [Rule 2: ...]

MUST NOT:
- [Rule 1: specific ban with example]
- [Rule 2: ...]

---

## Enforceability Report

### Converted guidelines: [N] of [total]
### Tier 3 (unenforceable without reinterpretation):
| Original statement | Reason | Suggested action |
|--------------------|--------|-----------------|

### Test Results
| Example | Type | Rules violated / satisfied | Pass/Fail |
|---------|------|---------------------------|-----------|

### Merge log (rules combined to stay under 20):
[List merged rules and their originals]
```

## Verification

- [ ] Rule block contains no personality adjectives without a lexical or structural anchor.
- [ ] Rule count ≤ 20.
- [ ] Every failure example violates ≥ 1 rule in the block.
- [ ] Every success example satisfies all rules in the block.
- [ ] Every Tier 3 guideline either has a converted Tier 1 equivalent or appears in the unenforceable report.
