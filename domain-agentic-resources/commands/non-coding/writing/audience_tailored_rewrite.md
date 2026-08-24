---
name: audience_tailored_rewrite
description: "Run when the same message must be rewritten for a specific audience segment."
version: "1.0.0"
category: writing
tags: [audience, rewrite, tailored, writing]
agents_used: []
---
# Audience Tailored Rewrite

## Trigger phrase
Run when the same message must be rewritten for a specific audience segment.

## Required inputs
- Source content to adapt.
- Target audience profile (knowledge level, priorities, sensitivity).
- Desired tone, length, and delivery channel.

## Output schema
- `audience_version`: rewritten content tailored to the specified audience.
- `adaptation_notes`: key framing, terminology, and emphasis decisions made.
- `risk_flags`: possible misinterpretation or tone risks to review.

## Validation checklist
- [ ] Rewrite matches audience knowledge level and context.
- [ ] Critical original intent is retained with no contradictory claims.
- [ ] Tone and length fit the stated channel constraints.
- [ ] Potential sensitivity or ambiguity issues are explicitly flagged.
