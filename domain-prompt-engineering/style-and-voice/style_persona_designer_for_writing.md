---
title: "Persona Designer for Writing Tasks"
category: prompt-engineering/style-and-voice
description: "Design a bounded writing persona—voice, sentence style, vocabulary tier—for use in writing prompts, not agent behavior."
techniques:
  - ST-01
  - ST-03
  - CM-02
  - ST-16
  - PR-01
difficulty: beginner
tags:
  - persona
  - writing
  - voice
  - style
  - prompt_design
updated: "2026-05-11"
related_prompts:
  - domain-prompt-engineering/style-and-voice/style_voice_extraction_from_corpus.md
  - domain-prompt-engineering/style-and-voice/style_register_control.md
  - domain-prompt-engineering/style-and-voice/style_brand_guideline_to_prompt.md
---

## Objective

Produce a self-contained writing persona block that controls voice, tone, vocabulary, and sentence structure for a specific writing task. This is a style persona only — it does not define knowledge, agency, memory, or tool use.

## When to Use

- You want consistent output voice across multiple writing sessions without corpus extraction.
- A prompt needs an explicit "write as if you are X" instruction grounded in stylistic rules, not role-play.
- You are building a multi-prompt workflow and need a reusable style block to paste into each prompt.
- **Not for:** agent personas with memory, tools, or decision authority. Use agent-patterns/ for those.

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| Writing domain | Yes | e.g., "B2B SaaS blog", "legal memo", "parenting newsletter" |
| Persona archetype | Yes | e.g., "senior practitioner", "curious generalist", "empathetic educator" |
| Target audience | Yes | Who will read the outputs |
| Explicit exclusions | Optional | Voice characteristics to avoid (e.g., "not academic", "not sales-y") |
| Sample output | Optional | One example of desired output (50–200 words) |

## Persona Dimensions

Design decisions for each dimension:

| Dimension | Options | Decision rule |
|-----------|---------|---------------|
| Sentence length | Short (<12w) / Medium (12–20w) / Long (20+w) / Mixed | Match audience scanning speed |
| Vocabulary tier | Specialist / Semi-technical / Accessible | Match audience expertise |
| First person use | Heavy ("I think") / Light ("one might") / None | Match archetype |
| Hedging | Assertive (rare hedges) / Calibrated / Cautious | Match claim certainty norms of domain |
| Structural openness | Explicit headers/bullets / Flowing prose / Mixed | Match reading context |
| Analogy frequency | Dense (every other paragraph) / Moderate / Rare | Match abstractness of content |
| Question use | Rhetorical (never answered) / Socratic (answered in text) / None | Match archetype |

## Constraints

**Must:**
- Specify every dimension in the table above with a named option, not a description.
- Produce a MUST/MUST NOT rule for each dimension chosen.
- Include at least 2 banned-phrase examples grounded in the exclusions or archetype.
- Keep the final persona block under 200 words so it fits in a system prompt without dominating context.

**Must Not:**
- Include personality adjectives ("warm", "witty", "engaging") without a rule that operationalizes them.
- Include knowledge domain rules, memory rules, or tool-use rules — those are agent concerns.
- Produce a persona that contradicts the target audience (e.g., "dense Latinate vocabulary" for a general consumer audience).

## Instructions

1. **Profile the audience.** State: expertise level (novice / practitioner / expert), reading context (skim / read / study), and patience for abstraction (low / medium / high).

2. **Select dimensions.** For each dimension in the table, pick an option and state the reasoning in one phrase.

3. **Draft banned-phrase list.** From the exclusions input and archetype, generate 3–6 specific banned phrases or patterns.

4. **Assemble the persona block** in MUST/MUST NOT format with a header identifying the persona name.

5. **Validate against sample** (if provided): confirm every dimension rule is satisfied. Flag violations.

## Output Format

```
## Writing Persona: [Persona Name]
**Domain:** [domain] | **Audience:** [audience summary]

### Dimension Selections
| Dimension | Choice | Reason |
|-----------|--------|--------|
| Sentence length | ... | ... |
...

### Persona Rule Block (copy-paste ready, ≤200 words)

VOICE: [One sentence describing the persona]

MUST:
- Sentence length: [specific rule]
- Vocabulary: [specific rule]
- [Additional dimension rules]

MUST NOT:
- [Banned phrase or pattern 1]
- [Banned phrase or pattern 2]
...

### Sample Validation (if sample provided)
[Rule-by-rule check: ✓ or ✗ with sentence reference]
```

## Verification

- [ ] Every dimension in the table has a named option (not a description like "moderate").
- [ ] The persona block is ≤ 200 words.
- [ ] Zero personality adjectives without an operational rule that makes them testable.
- [ ] No knowledge, memory, or tool-use rules appear in the block.
- [ ] If sample was provided, every dimension rule has a validation result.
