---
title: "Audience Adaptation Prompt"
category: prompt-engineering/style-and-voice
description: "Rewrite the same content for multiple target audiences with per-audience vocabulary, depth, and structure adjustments."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-01
  - CM-02
  - QA-01
difficulty: beginner
tags:
  - audience
  - adaptation
  - rewriting
  - register
  - style
updated: "2026-05-11"
related_prompts:
  - domain-prompt-engineering/style-and-voice/style_register_control.md
  - domain-prompt-engineering/style-and-voice/style_persona_designer_for_writing.md
  - domain-prompt-engineering/style-and-voice/style_length_and_density_control.md
---

## Objective

Produce N audience-specific variants of the same content, each adapted by vocabulary tier, assumed knowledge, depth, and structure, with a delta annotation showing what changed and why.

## When to Use

- A single explanation needs versions for experts, practitioners, and laypeople.
- Marketing content needs adaptation from C-suite executive to technical buyer to end user.
- Educational material needs versions by grade level or domain background.
- **Not for:** translations between languages or localization (cultural adaptation is a separate concern).

## Audience Profile Schema

For each target audience, specify:

| Attribute | Options | Effect on text |
|-----------|---------|----------------|
| Expertise | Novice / Practitioner / Expert | Determines jargon, assumed knowledge, analogy depth |
| Role | e.g., Executive / Engineer / Patient / Parent | Determines what they care about and what they skip |
| Reading context | Skim (30s) / Read (3–5m) / Study (15m+) | Determines structure, header frequency, depth |
| Prior knowledge | [List specific concepts they already know] | Determines what to define vs. skip |
| Stakes | Low / Medium / High | Determines level of nuance and caveat needed |

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| Source content | Yes | The canonical text to adapt |
| Audience profiles | Yes | 2–4 audiences using the schema above |
| Factual floor | Optional | Claims that must appear in every variant |
| Length targets | Optional | Per-audience word counts |

## Constraints

**Must:**
- Every variant must contain every claim from the factual floor (if specified).
- Every variant must state its audience profile in a header comment.
- Delta annotation must classify each change as: VOCAB (word substitution), DEPTH (concept added or removed), STRUCTURE (reordering or heading change), ANALOGY (added, changed, or removed), or OMISSION (content dropped for this audience).
- Produce at least one DEPTH change and one VOCAB change per variant (if only one variant differs from source, flag as "minimal adaptation").

**Must Not:**
- Remove a fact from a high-expertise variant that is present in a low-expertise variant, unless the fact is genuinely below the expert's concern.
- Add facts not in the source to any variant — adaptation means rearranging and reframing, not adding.
- Collapse N variants into a single text with bracketed inserts — each variant must be a standalone document.

## Instructions

1. **Profile each audience** using the schema. Determine for each: what they need to understand, what they already know, how they will read the piece.

2. **Identify adaptation dimensions** from source content: technical terms (VOCAB candidates), deep explanations (DEPTH candidates), structure (STRUCTURE candidates), analogies (ANALOGY candidates), qualifications (OMISSION candidates for executives).

3. **Write each variant.** Apply adaptation rules per audience profile. Track every change type.

4. **Generate delta table** per variant showing sentence/paragraph changes vs. the source.

## Output Format

```
## Variant 1: [Audience Label]
**Profile:** Expertise=[X] | Role=[Y] | Reading=[Z]
**Length:** [N] words

[Full variant text]

### Delta: Variant 1 vs. Source
| Element | Source | Variant 1 | Change Type | Reason |
|---------|--------|-----------|-------------|--------|
| Para 1 opening | "The algorithm..." | "Think of this as..." | ANALOGY | Novice lacks CS background |
...

---

## Variant 2: [Audience Label]
...
```

## Verification

- [ ] Every variant contains all items from the factual floor.
- [ ] Every variant has at least one DEPTH and one VOCAB delta entry.
- [ ] No variant contains a sentence not derivable from the source (no invented content).
- [ ] Expert variants do not simply repeat novice variants with vocabulary swapped — structural differences should exist.
- [ ] Each variant can be read as a standalone piece without referencing the others.
