---
title: "Length Budget Designer"
category: prompt-engineering/output-formatting
description: "Define hard caps on words, tokens, and section counts with an enforcement method for each cap."
techniques:
  - ST-01
  - ST-03
  - CM-02
  - QA-08
  - QA-01
difficulty: beginner
tags:
  - length
  - budget
  - word_count
  - tokens
  - output_format
updated: "2026-05-11"
related_prompts:
  - domain-prompt-engineering/style-and-voice/style_length_and_density_control.md
  - domain-prompt-engineering/output-formatting/format_one_sentence_answer_pattern.md
  - domain-prompt-engineering/output-formatting/format_no_preamble_no_postamble.md
---

## Objective

Design a length budget — a complete set of hard caps on total output, per-section output, and structural element counts — with an enforcement method for each cap that the model can self-check before emitting.

## When to Use

- You need to prevent a model from exceeding a token limit for a downstream system.
- You want consistent output size across multiple calls to the same prompt.
- You are designing a prompt for a UI component with a fixed display area.
- **Not for:** auditing existing output length (that is style_length_and_density_control.md). Not for enforcing vocabulary or density — only counts.

## Cap Types

| Cap type | Unit | Where it applies | Self-check method |
|----------|------|-----------------|------------------|
| Total word count (TWC) | Words | Entire response | Count before emitting |
| Total token estimate | Tokens (~0.75 words/token) | Entire response | TWC ÷ 0.75 |
| Section word cap | Words | Per named section | Count per heading block |
| Sentence count cap | Sentences | Per paragraph or section | Count periods + question marks |
| Item count cap | List items | Per list | Count list markers |
| Section count cap | N sections | Entire response | Count H2 or H3 headings |
| Example count cap | N examples | Entire response | Count example markers |

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| Target total length | Yes | e.g., "≤300 words" or "≤400 tokens" |
| Section structure | Recommended | List section names and relative importance |
| Delivery context | Recommended | e.g., "chat UI", "email", "API response to parser" |
| Hard constraints | Optional | Any sections that must appear regardless of budget |

## Constraints

**Must:**
- Assign a cap to every named section if sections are specified.
- Section caps must sum to ≤ total word cap minus 10% (overhead for transitions and headings).
- Each cap must include a self-check instruction the model can execute internally before emitting.
- Flag any section marked "required" that risks consuming >40% of the total budget.

**Must Not:**
- Use ranges as caps ("150–200 words") — pick a single hard ceiling.
- Leave any section uncapped if a total cap is set.
- Set caps that make required content mathematically impossible (e.g., "≤50 words total" with 5 required sections).

## Instructions

1. **Set total cap.** Convert to both words and token estimate.

2. **Allocate by section.** Distribute the word budget across sections proportionally to their importance. Reserve 10% for overhead.

3. **Assign structural caps.** Based on delivery context:
   - Chat UI: item count cap ≤ 5 per list; section count cap ≤ 3
   - Email: TWC ≤ 150; section count ≤ 2
   - API response: item count ≤ 10; no headings preferred

4. **Write self-check instructions** for each cap. These are internal model steps, not visible to the user.

5. **Build the budget table** and the system prompt enforcement block.

## Output Format

```
## Length Budget — [Context Name]

### Budget Table
| Element | Cap | Enforcement check |
|---------|-----|------------------|
| Total response | ≤[N] words (~[N] tokens) | Count all words before emitting |
| Section: [Name] | ≤[N] words | Count words under this heading |
| Section: [Name] | ≤[N] words | Count words under this heading |
| Per-list items | ≤[N] items | Count `- ` or `N.` markers |
| Headings | ≤[N] | Count `##` occurrences |
...

Overhead reserve: [N] words ([X]% of total)
Section sum: [N] words (budget check: [N] + overhead = [N] ≤ total ✓/✗)

### System Prompt Enforcement Block (copy-paste ready)
Respond in ≤[N] words total.
Sections:
- [Name]: ≤[N] words
- [Name]: ≤[N] words
[...]
Before emitting: count total words. If over budget, cut from the longest section first.

### Constraint Flags
[Any required sections consuming >40% of budget, or mathematical impossibility warnings]
```

## Verification

- [ ] Section cap sum + overhead ≤ total word cap.
- [ ] Every named section has a cap.
- [ ] No section cap uses a range — single integer ceiling only.
- [ ] System prompt block is self-contained and can be pasted without modification.
- [ ] Constraint flags section exists and is either populated or explicitly states "None."
