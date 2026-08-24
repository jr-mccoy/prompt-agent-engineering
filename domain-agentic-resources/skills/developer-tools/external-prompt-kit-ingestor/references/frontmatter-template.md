# Frontmatter Template

Canonical structure for an extracted prompt file. Copy this skeleton and fill in.

```markdown
---
title: "Descriptive Title in Title Case"
category: ai-patterns
description: "One-sentence purpose, ending with a period."
techniques:
  - AG-34
  - QA-08
  - CM-02
  - DS-43
  - NE-02
tags:
  - keyword-one
  - keyword-two
  - keyword-three
difficulty: advanced
updated: "YYYY-MM-DD"
related_prompts:
  - domain-engineering-workflows/ai-patterns/sibling_prompt.md
---

# Descriptive Title

**Purpose:** One sentence, plain language.

**When to use:** One sentence describing the trigger condition.

**What you'll get:** One sentence describing the deliverable.

**Source:** `original-kit-filename.md`

```markdown
<role>
{verbatim role block from the source}
</role>

<instructions>
{verbatim instructions block from the source}
</instructions>

<output>
{verbatim output block from the source}
</output>

<guardrails>
{verbatim guardrails block from the source}
</guardrails>
```

## Notes

(Optional — repo-specific guidance, integration tips, or sequencing relative to sibling prompts. Omit this section if there's nothing useful to add.)
```

## Field Rules

| Field | Required | Notes |
|---|---|---|
| `title` | yes | Title case. Quotes if it contains a colon. |
| `category` | yes | Lowercase, hyphens. Must match the directory the file lives in. |
| `description` | yes | One sentence. Period at end. No marketing language. |
| `techniques` | yes | 3–7 IDs. Must exist in `techniques/MASTER_TECHNIQUE_INDEX.md`. |
| `tags` | yes | 3–6 lowercase keywords for search. |
| `difficulty` | yes | `beginner` | `intermediate` | `advanced`. |
| `updated` | yes | ISO date. Date of ingestion, not original publication. |
| `related_prompts` | yes | At least one path. Sibling prompts in the same kit are valid. |

## Body Rules

- The four bold meta-lines (Purpose, When to use, What you'll get, Source) are mandatory and must appear in that order.
- The fenced markdown block contains the prompt **verbatim from the source**. Do not paraphrase, "improve", or compress. The author's wording is the deliverable.
- If the source uses a different tag convention (e.g., `# Role` instead of `<role>`), preserve it.
- Do not add example outputs unless the source author included them.
