---
title: "Markdown Section Contract for Parseable Output"
category: prompt-engineering/structured-output
description: "Define heading, list, and code-block conventions so a downstream parser can reliably extract sections from markdown output."
techniques:
  - ST-03
  - CM-02
  - PR-02
difficulty: beginner
tags:
  - markdown
  - parsing
  - section_contract
  - structured_output
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/structured-output/structured_xml_tag_pattern.md
  - domain-prompt-engineering/structured-output/structured_dual_output_pattern.md
---

## Objective

Establish a markdown shape — heading levels, list markers, code-fence conventions, anchor IDs — that a regex or markdown-AST parser can extract sections from with zero post-processing.

## When to Use

- The output is shown to a user (so it must look like prose) AND consumed by code.
- A previous attempt produced inconsistent heading levels or nested lists that broke the parser.
- You don't want to switch to JSON/XML for stylistic reasons.

## Inputs

```
SECTIONS: <ordered list of required sections, each with a stable name>
OPTIONAL_SECTIONS: <may appear, may not>
PARSER_TYPE: <regex | markdown-ast (e.g., remark, markdown-it)>
ALLOW_USER_PROSE: <yes|no — does any section contain free-form prose under controlled rules?>
```

## Constraints

### Must
- Use one heading level per section type. Required sections at H2 (`## `), subsections at H3 (`### `).
- Section name format: `## <NAME>` exact-case, no trailing punctuation, no markdown inside the heading.
- Lists use `- ` (hyphen + space). No `*` or `+` markers. Nested lists indent by 2 spaces.
- Code fences use triple backticks with explicit language tag (`json`, `bash`, etc.). Never use `~~~`.
- Each required section appears exactly once, in declared order.
- Sections are separated by exactly one blank line. No trailing whitespace on heading lines.

### Must Not
- Bold or italicize headings.
- Use horizontal rules (`---`) inside the body — they conflict with frontmatter and parsers.
- Emit empty sections; if a section has no content, write `_(none)_` on a single line.
- Produce content above the first H2 (no preamble).

## Instructions

1. Lock the section list. Required sections by H2, optional by `## [optional] <NAME>`.
2. Emit the parser-side rules:
   - Regex parser: `/^## (?<name>[^\n]+)\n([\s\S]*?)(?=^## |\Z)/gm` to split sections.
   - AST parser: walk to depth-2 headings; a `heading` node with depth=2 starts a section; siblings until next depth-2 are its body.
3. Write the producer prompt clause that pins the conventions verbatim.
4. Provide a self-check the model runs before emitting: required sections present, in order, exactly once; no preamble; each list uses `- `.

## Output Format

```
section_contract:
- H2 sections (required, in order): [<names>]
- H2 sections (optional): [<names>]
- list marker: -
- code fence: ```<lang>
- empty marker: _(none)_

producer_prompt_clause:
---
<text>
---

parser_rule:
- type: <regex|ast>
- rule: <verbatim regex or AST traversal description>

self_check:
- required sections all present? Y/N
- order matches contract? Y/N
- list markers all `- `? Y/N
- code fences all triple-backtick with language? Y/N
```

## Verification

- A roundtrip test in your head: emit minimal output, run the parser rule, recover the section names. If any section is lost, contract is wrong.
- If `PARSER_TYPE=regex`, the regex must capture body without consuming the next heading.
- Heading text contains no markdown markers (`*`, `_`, `` ` ``).
