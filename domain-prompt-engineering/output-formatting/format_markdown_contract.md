---
title: "Markdown Contract"
category: prompt-engineering/output-formatting
description: "Define exact heading depth, list style, code-fence language tags, and bold/italic usage in a copy-paste system prompt block."
techniques:
  - ST-01
  - ST-03
  - CM-02
  - QA-08
  - DC-01
difficulty: beginner
tags:
  - markdown
  - formatting
  - contract
  - output_format
  - system_prompt
updated: "2026-05-11"
related_prompts:
  - domain-prompt-engineering/output-formatting/format_length_budget_designer.md
  - domain-prompt-engineering/output-formatting/format_no_preamble_no_postamble.md
  - domain-prompt-engineering/structured-output/structured_output_markdown_contract.md
---

## Objective

Design a precise markdown formatting contract specifying heading depth, list style, code-fence rules, emphasis usage, and table policy — ready to paste as a system prompt block.

## When to Use

- A model's markdown output is inconsistent across sessions or contains structural patterns you want to lock down.
- A rendering environment supports only a subset of markdown (e.g., no tables, no nested lists).
- You are building a multi-prompt pipeline and need formatting to be identical across all outputs.
- **Not for:** enforcing content structure (what sections to include) — that is output specification (ST-03), not formatting contract.

## Decision Dimensions

Answer each question to define the contract:

| Dimension | Question | Common Options |
|-----------|---------|----------------|
| Heading depth | What is the max heading level permitted? | H1 only / H1+H2 / H2+H3 only / No headings |
| Heading use | When may a heading appear? | Every major section / Only if >3 sections / Never |
| List style | Bullets or numbers? | Bullets only / Numbers for ordered / Mixed by context |
| Nesting | Max list nesting depth? | 1 (flat) / 2 / No limit |
| Code fences | Language tag required? | Always / Optional / Banned |
| Bold | When to bold? | Key terms only / Never / Section leads only |
| Italic | When to italicize? | Never / Titles/emphasis / Definitions |
| Tables | When are tables permitted? | Never / Only 2D data / Always permitted |
| Inline code | When to use backticks? | File paths + commands only / Any term / Never |
| Horizontal rules | Permitted? | Never / Between major sections only |

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| Rendering environment | Yes | e.g., "GitHub README", "Slack message", "PDF export", "API response" |
| Decision dimension answers | Yes | One answer per row in the table above |
| Existing violations | Optional | 2–5 examples of current output that breaks the desired format |

## Constraints

**Must:**
- Produce a contract with exactly one rule per dimension (no ambiguous "as appropriate" rules).
- Each rule must be falsifiable from the output alone — inspectable without knowing author intent.
- Include a Violation Detection section listing exact patterns that breach each rule.
- Rules must fit the rendering environment: do not permit tables if the environment does not render them.

**Must Not:**
- Use vague rules like "use headings sparingly" — quantify as "max N headings per N words" or "only if N+ sections."
- Permit markdown elements that the rendering environment does not support.
- Overlap rules (e.g., separate inline code and code block rules should not have conflicting conditions).

## Instructions

1. **Profile the rendering environment.** List what markdown elements it supports, renders incorrectly, or strips. Note character limits if any.

2. **Resolve each dimension.** Answer every row in the decision table. For any environment that strips tables or headings, force the restrictive option.

3. **Write the contract.** Format as MUST/MUST NOT rules with one rule per dimension.

4. **Write violation detection patterns.** For each MUST NOT rule, list the exact markdown pattern that would breach it (e.g., `##` appearing after content has no `#` heading is a violation of heading depth consistency).

5. **Test against violations** (if provided). For each existing violation, identify which contract rule it breaks. Confirm that the rule catches it.

## Output Format

```
## Markdown Contract — [Environment Name]

### MUST
- Headings: [rule, e.g., "Use H2 (##) and H3 (###) only; H1 and H4+ banned."]
- Lists: [rule]
- Code fences: [rule]
- Bold: [rule]
- Italic: [rule]
- Tables: [rule]
- Inline code: [rule]
- Horizontal rules: [rule]

### MUST NOT
- [Specific banned pattern 1, e.g., "Never use `#` (H1) in responses."]
- [Specific banned pattern 2]
...

### Violation Detection Guide
| Rule | Pattern that signals a violation |
|------|--------------------------------|
| Heading depth | `^#\s` at line start when H1 is banned |
| Table policy | `|` column separator when tables are banned |
...

### Compact System Prompt Block (≤150 words, copy-paste ready)
[Final condensed version]
```

## Verification

- [ ] Every dimension in the decision table has a corresponding rule in the MUST or MUST NOT section.
- [ ] No rule contains "as appropriate", "when needed", or other non-falsifiable language.
- [ ] Violation detection table covers every MUST NOT rule.
- [ ] Compact block is ≤ 150 words.
- [ ] If existing violations were provided, each is traceable to at least one MUST NOT rule.
