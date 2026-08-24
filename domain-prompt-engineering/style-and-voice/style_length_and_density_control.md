---
title: "Length and Density Control"
category: prompt-engineering/style-and-voice
description: "Enforce hard caps on words-per-claim, sentences-per-paragraph, and total word count with a compliance audit table."
techniques:
  - ST-01
  - ST-03
  - CM-02
  - QA-01
  - QA-08
difficulty: beginner
tags:
  - length
  - density
  - brevity
  - style
  - word_count
updated: "2026-05-11"
related_prompts:
  - domain-prompt-engineering/style-and-voice/style_audience_adaptation_prompt.md
  - domain-prompt-engineering/output-formatting/format_length_budget_designer.md
  - domain-prompt-engineering/output-formatting/format_one_sentence_answer_pattern.md
---

## Objective

Rewrite a source text (or generate new text) while enforcing hard numeric caps on sentence density, paragraph density, and total length. Output includes a compliance table proving each cap is met.

## When to Use

- Content is too long or too dense for its delivery format (email, slack, executive summary).
- A model is producing padded, over-explained output that needs a hard limit.
- You need a system prompt rule block encoding density constraints.
- **Not for:** enforcing format shape (headings, lists) — use format_markdown_contract.md for that.

## Density Caps Reference

| Cap type | Definition | Typical targets by context |
|----------|-----------|---------------------------|
| Words per sentence (WPS) | Total words ÷ sentence count | Casual: ≤12 / Neutral: ≤16 / Formal: ≤22 |
| Sentences per paragraph (SPP) | Sentence count ÷ paragraph count | Dense: ≤5 / Standard: ≤3 / Airy: ≤2 |
| Claims per sentence (CPS) | Distinct assertable facts per sentence | Tight: ≤1 / Balanced: ≤2 / Dense: ≤3 |
| Total word count (TWC) | All words in the output | Email: ≤150 / Blog section: ≤300 / Full post: ≤800 |
| Qualifier ratio (QR) | Hedging words ÷ total words | Assertive: ≤0.02 / Normal: ≤0.04 |

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| Source text | Yes | Text to rewrite or audit |
| Target caps | Yes | Specify at least TWC and one of WPS or SPP |
| Reduction approach | Optional | "cut claims", "merge sentences", "drop qualifiers", "split into sections" |
| Fact-lock phrases | Optional | Phrases that must survive |

## Constraints

**Must:**
- Measure every cap before and after the rewrite.
- Report each cap as: [before] → [after] | [pass/fail vs. target].
- If a fact-lock phrase would violate a cap (e.g., a long locked sentence pushes WPS over limit), flag it explicitly as an exception rather than silently violating.
- Prefer cutting qualifiers and filler transitions over cutting factual claims when reducing word count.

**Must Not:**
- Delete a fact-lock phrase to meet a cap.
- Report "approximately 150 words" — report exact counts only.
- Use vague language in the compliance table ("roughly meets", "close to").

## Instructions

1. **Measure baseline.** Count: total words, total sentences, total paragraphs, total claims (each distinct assertable statement). Compute WPS, SPP, CPS. List all qualifier words found.

2. **Identify violations.** For each cap with a target, mark which paragraphs or sentences breach it.

3. **Rewrite.** In order of priority:
   - Drop qualifiers and hedges (zero information loss, high density gain).
   - Merge short sentences that carry a single branching claim.
   - Cut sentences that restate earlier claims.
   - Split overly long sentences at coordinating conjunctions.
   - Trim examples to one representative instance if multiple are present.

4. **Measure output.** Recount all metrics.

5. **Build compliance table.**

## Output Format

```
## Rewritten Text
[Text]

---

## Compliance Table
| Cap | Target | Before | After | Status |
|-----|--------|--------|-------|--------|
| Total words (TWC) | ≤[N] | [N] | [N] | ✓/✗ |
| Words per sentence (WPS) | ≤[N] | [N] | [N] | ✓/✗ |
| Sentences per paragraph (SPP) | ≤[N] | [N] | [N] | ✓/✗ |
| Claims per sentence (CPS) | ≤[N] | [N] | [N] | ✓/✗ |
| Qualifier ratio (QR) | ≤[N] | [N] | [N] | ✓/✗ |

## Exception Log
[Any fact-lock phrases that required a cap exception, with cap and delta]

## Cuts Made
[Bulleted list: what was removed and why]
```

## Verification

- [ ] Every cap in the compliance table shows before and after as exact integers or two-decimal ratios.
- [ ] No ✗ row without an exception in the Exception Log.
- [ ] Exception Log is empty if no fact-lock exceptions were triggered.
- [ ] The rewritten text contains no words from the qualifier list that were not present in fact-lock phrases.
- [ ] Before counts for WPS and SPP can be verified arithmetically from sentence and paragraph counts.
