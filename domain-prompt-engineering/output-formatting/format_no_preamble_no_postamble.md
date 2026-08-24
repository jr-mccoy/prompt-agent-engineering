---
title: "No Preamble / No Postamble"
category: prompt-engineering/output-formatting
description: "Eliminate opener affirmations and sign-off lines from AI responses with a system prompt block and detection patterns."
techniques:
  - ST-01
  - ST-03
  - CM-02
  - DC-01
difficulty: beginner
tags:
  - preamble
  - postamble
  - brevity
  - ai_tells
  - output_format
updated: "2026-05-11"
related_prompts:
  - domain-prompt-engineering/style-and-voice/style_anti_voice_designer.md
  - domain-prompt-engineering/style-and-voice/style_signature_phrase_kill_list.md
  - domain-prompt-engineering/output-formatting/format_one_sentence_answer_pattern.md
---

## Objective

Produce a system prompt block that eliminates opener affirmations ("Sure,", "Of course,", "Certainly!") and closer lines ("Let me know if you have questions.", "I hope this helps!") from all responses, plus detection patterns for automated verification.

## When to Use

- AI responses in your pipeline or UI include opener phrases that inflate token count and signal machine authorship.
- Downstream parsers fail when responses don't begin with the expected content.
- You want all responses to begin immediately with the answer.
- **Not for:** removing necessary context (e.g., a caveat that is part of the answer). Not for suppressing legitimate multi-sentence responses.

## Preamble Pattern Taxonomy

| Type | Examples | Token cost |
|------|---------|-----------|
| Affirmation openers | "Sure!", "Certainly!", "Absolutely!", "Of course," "Happy to help!" | 2–4 tokens |
| Task acknowledgment | "Great question!", "That's an interesting point.", "I understand you want..." | 5–10 tokens |
| Self-description openers | "I'll now explain...", "Let me walk you through...", "I'm going to..." | 5–8 tokens |
| Meta-framing | "This is a complex topic.", "There are several ways to look at this." | 6–10 tokens |
| Instruction repeat | "You've asked me to [restate request]..." | 10–25 tokens |

## Postamble Pattern Taxonomy

| Type | Examples | Token cost |
|------|---------|-----------|
| Offer to continue | "Let me know if you need anything else.", "Feel free to ask follow-up questions." | 8–12 tokens |
| Hope/wish closers | "I hope this helps!", "I hope that answers your question." | 5–8 tokens |
| Summary meta-note | "In summary, I've covered X, Y, and Z." (when summary was not requested) | 10–20 tokens |
| Farewell | "Best regards,", "Sincerely," | 2–4 tokens |

## Constraints

**Must:**
- Produce a system prompt block that bans all types in both taxonomies.
- Produce a regex-compatible detection pattern for each type.
- Include a fallback rule for legitimate openers (transitions that carry information, e.g., "Before answering, note that [material caveat]...").
- Specify what the first word/token of a response should be instead.

**Must Not:**
- Ban all sentence openers — only the zero-information affirmation or meta-commentary types listed.
- Create rules so strict they ban necessary caveats or context-setting sentences with actual content.

## Instructions

1. **Classify the context.** Determine what the first token of every response should be: direct answer word, list item, heading, or code block. This constrains how strict the no-preamble rule should be.

2. **Write the ban block.** Enumerate every banned preamble and postamble type with specific examples.

3. **Write the fallback rule.** A legitimate opener carries information: "Note that [material constraint]..." is permitted. "I'll explain..." is not.

4. **Write detection patterns.** For automated post-processing verification.

5. **Write the positive rule** — what a well-formed response opening looks like.

## Output Format

```
## No-Preamble / No-Postamble System Prompt Block (copy-paste ready)

Start every response with the first word of the actual answer.
Never begin with: [comma-separated list of banned openers]
Never end with: [comma-separated list of banned closers]

Permitted opener exception: a sentence beginning with "Note:" or "Warning:" that carries a material constraint may precede the answer. This exception does not apply to restatements of the question or meta-commentary.

---

## Detection Patterns

### Preamble detection (check first 30 tokens)
| Pattern | Regex-compatible form | Type |
|---------|-----------------------|------|
| Affirmation | `^(Sure|Certainly|Absolutely|Of course)[!,]` | Affirmation opener |
| Task acknowledge | `^(Great question|That'?s (a )?(great|interesting|good))` | Task acknowledgment |
...

### Postamble detection (check last 30 tokens)
| Pattern | Regex-compatible form | Type |
|---------|-----------------------|------|
| Continue offer | `(let me know|feel free to|don'?t hesitate).{0,30}$` | Offer to continue |
...

## Correct Response Opening Examples
- Direct answer: "The function returns null when..."
- List: "- Option 1: ..."
- Code: "```python"
- Heading: "## Summary"

## Incorrect Opening Examples (banned)
- "Sure! Here's what I found..."
- "Great question. Let me explain..."
- "Certainly! I'd be happy to help with that."
```

## Verification

- [ ] Every preamble type in the taxonomy has a corresponding ban entry.
- [ ] Every postamble type in the taxonomy has a corresponding ban entry.
- [ ] Detection patterns are regex-compatible (no natural language descriptions in the pattern field).
- [ ] The fallback rule for legitimate openers is narrowly defined with a specific trigger word ("Note:", "Warning:").
- [ ] Correct/incorrect opening examples are included and correctly labeled.
