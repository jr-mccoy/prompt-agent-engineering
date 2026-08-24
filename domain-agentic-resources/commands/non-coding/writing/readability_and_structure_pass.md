---
name: readability_and_structure_pass
description: "Run when a draft needs clarity improvements without changing core meaning or intent."
version: "1.0.0"
category: writing
tags: [readability, structure, writing]
agents_used: []
---
# Readability And Structure Pass

## Trigger phrase
Run when a draft needs clarity improvements without changing core meaning or intent.

## Required inputs
- Current draft text.
- Target reading level and document type (email, brief, report, etc.).
- Non-negotiable terminology, tone, or required sections.

## Output schema
- `edited_draft`: revised version with improved flow and readability.
- `change_log`: concise summary of major structural and language edits.
- `residual_issues`: remaining clarity risks requiring author decision.

## Validation checklist
- [ ] Core meaning and factual intent are preserved.
- [ ] Paragraph and heading structure follows a logical progression.
- [ ] Sentence complexity and jargon align with target reading level.
- [ ] Required sections/terms remain present after revision.
