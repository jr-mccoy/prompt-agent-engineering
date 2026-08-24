---
name: pacu-quick-reference-author
description: Author a new bedside quick-reference card for a PACU procedure or topic. Use when the user asks for a "quick ref", "bedside card", "pocket reference", or a ≤2-page scannable document matching Quick-Reference-Style-Guide.md. Produces a 30-second-scannable card with ABC priority block, decision algorithm, red-flag table, and call-the-provider triggers.
tags:
  - pacu
  - nursing-education
  - quick-reference
  - bedside
updated: "2026-04-14"
---

# PACU Quick Reference Author

## Purpose

Generate a single bedside quick-reference card (800–1500 words, scannable in under 30 seconds) for a specific PACU topic or procedure. Conforms to `Quick-Reference-Style-Guide.md`.

## When to use

- User asks for a "quick ref", "quick reference", "bedside card", or "pocket reference".
- Content will live under `guides/quick-references/`.
- Audience reads it standing at the bedside with a patient in front of them.

## When NOT to use

- User needs a full orientation document → use `pacu-comprehensive-guide-author`.
- User needs a decision tree image → pair `pacu-algorithm-flowchart-designer` with `image-meta-prompts/pacu_algorithm_flowchart_meta.md`.
- User needs a med-specific card → use `prompts/pacu_medication_profile.md` or `prompts/pacu_red_flag_card.md`.

## Inputs required

1. **Topic / procedure** (exact name).
2. **Use case** — admission card, complication card, phase-transition card.
3. **Source chapters** to cite.
4. **Neighbor quick-ref** in the PACU repo (for style mirroring).
5. **Any facility-specific content the user wants left as `per facility protocol`.

## Workflow

1. **Confirm inputs.**
2. **Load style contract.** `../../../Quick-Reference-Style-Guide.md`.
3. **Draft the five standard blocks:**
   - **ABC Priority block** — 3–6 bullets each for Airway / Breathing / Circulation.
   - **Procedure-specific focus block** — 4–8 bullets of what's unique to *this* surgery.
   - **Decision algorithm** — simple branching logic in prose or Mermaid (user can then hand to image meta-prompt).
   - **Red flag table** — trigger → immediate action → who to call.
   - **Call-the-provider block** — explicit triggers, role to call (not names), SBAR hint.
4. **Enforce density.** Every line earns its place. If a line would not change a nurse's next action at the bedside, cut it.
5. **Headings scan left-edge.** Use H2/H3 only; no deep nesting.
6. **Insert safety reminder** — one line at top.
7. **Self-check** below.

## Output format

```markdown
# {Topic} — PACU Quick Reference

> Safety reminder: Educational aid only — confirm against facility protocol; not a substitute for assessment and provider orders.

## ABC at Admission
**Airway**
- ...
**Breathing**
- ...
**Circulation**
- ...

## {Topic}-Specific Focus
- ...

## Decision Algorithm
```
[plain text or Mermaid — simple branching]
```

## Red Flags
| Trigger | Immediate action | Call |
|---|---|---|
| ... | ... | ... |

## Call the Provider When
- ...
(Give SBAR: Situation, Background, Assessment, Recommendation)

## Sources
- ...
```

## Source-fidelity rules

Same as comprehensive guide: cite chapters, no invented doses, facility items → *per facility protocol*.

## Self-check

- [ ] ≤ 1500 words total.
- [ ] ABC block is the first content block.
- [ ] Decision algorithm fits on one screen.
- [ ] Red-flag table has ≥ 4 rows with action + call.
- [ ] "Call the Provider When" block has ≥ 3 explicit triggers.
- [ ] No narrative paragraphs; everything is scannable.
- [ ] One safety reminder at top.
