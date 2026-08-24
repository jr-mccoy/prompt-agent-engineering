---
title: "XML Tag Output Pattern (Claude-Optimized)"
category: prompt-engineering/structured-output
description: "Decide when XML tags beat JSON for Claude, and define tag conventions plus a parser regex that survives nested content."
techniques:
  - ST-03
  - CM-02
  - PR-02
difficulty: intermediate
tags:
  - xml
  - claude
  - structured_output
  - parsing
  - tag_convention
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/structured-output/structured_json_schema_prompt_builder.md
  - domain-prompt-engineering/structured-output/structured_dual_output_pattern.md
  - domain-prompt-engineering/structured-output/structured_markdown_section_contract.md
---

## Objective

Pick between XML tags and JSON for a Claude task, and — if XML wins — produce a tag schema plus a non-greedy parser regex that handles long-form content, code blocks, and nested tags.

## When to Use

- The output contains long prose, multiple code blocks, or content where JSON string escaping is brittle.
- The task is for Claude (Anthropic models react well to XML scaffolding).
- The downstream consumer is a script you control.

## Inputs

```
TASK: <what the model is doing>
OUTPUT_PIECES: <list of named sections, e.g., reasoning, answer, sources>
EXPECTED_LENGTH_PER_PIECE: <tokens or chars>
HAS_CODE_BLOCKS: <yes|no>
NESTING_NEEDED: <yes|no>
```

## Constraints

### Must
- Choose XML when ANY of: average piece > 500 tokens, prose contains JSON-hostile chars (newlines + quotes + backslashes), >2 named pieces, or model is Claude. Otherwise prefer JSON.
- Tag names: lowercase, snake_case, ≤ 24 chars, no XML reserved chars.
- Open and close every tag on its own line; no inline tags around tokens.
- For nested tags: use a different name at each level. Never reuse the same tag name in an ancestor.
- Provide a parser regex that uses non-greedy matching and DOTALL.

### Must Not
- Use generic tags `<output>`, `<result>`, `<data>` — they collide.
- Self-closing tags.
- Mix XML and JSON inside the same response without the dual-output pattern.
- Rely on attributes for content (use child tags instead).

## Instructions

1. Score the task on the 4 XML-trigger conditions. If ≥ 1 met, pick XML.
2. Name each piece using the pattern `<task>_<role>` (e.g., `analysis_reasoning`, `analysis_answer`).
3. Define open/close conventions and write a 1-line schema description per tag.
4. Build the parser regex per tag: `<NAME>\\s*\\n(.*?)\\n\\s*</NAME>` with flags `s` (DOTALL).
5. Add a fence-escape rule: if a piece contains code, wrap inner code with markdown fences; the regex captures fences as-is.
6. Provide a 3-line failure mode: missing close tag → consumer treats output as "incomplete" and retries.

## Output Format

```
choice: xml | json
trigger_score: <n>/4 with which conditions matched

tag_schema:
- <tag_name>: <one-line purpose>
- ...

prompt_template:
---
<the prompt body that instructs the model to emit these tags>
---

parser_regex_per_tag:
- <tag_name>: /<tag_name>\s*\n(.*?)\n\s*<\/tag_name>/s

failure_mode:
- <how a missing close tag is detected and handled>
```

## Verification

- Tag names: all unique, all snake_case, none in {output, result, data, response, content}.
- Regex: compile mentally with a sample containing newlines and a fenced code block; confirm it captures.
- If `HAS_CODE_BLOCKS=yes`, confirm fence-escape rule is present.
- If `NESTING_NEEDED=yes`, confirm no parent/child tag share a name.
