---
name: pacu-comprehensive-guide-author
description: Author a new comprehensive PACU orientation guide for a specific surgical procedure or clinical topic. Use when the user asks to "write a new PACU guide", "create an orientation guide for [procedure]", "author a full manual chapter", or needs a 100-300 line specialty guide matching PACU-MANUAL-STYLE-GUIDE.md. Produces self-contained sections with ABC-structured assessment, phase-specific monitoring, red flags with escalation, and source citations.
tags:
  - pacu
  - nursing-education
  - comprehensive-guide
  - orientation
updated: "2026-04-14"
---

# PACU Comprehensive Guide Author

## Purpose

Generate a new procedure-specific or topic-specific comprehensive PACU guide that conforms to `PACU-MANUAL-STYLE-GUIDE.md`. Output is intended for orientees studying outside clinical hours and for experienced nurses needing deeper reference than a quick card.

## When to use

- User asks for a "new PACU guide" for a procedure, complication, or clinical concept.
- Need a 100–300 line document with self-contained sections.
- Content will be filed under `guides/[Procedure]-PACU-Guide.md` in the PACU repo.

## When NOT to use

- The user wants a ≤2-page bedside card → use `pacu-quick-reference-author`.
- The user wants a single topic deep-dive longer than typical guide sections → use `pacu-in-depth-explainer`.
- The user wants testable questions → use `pacu-quiz-generator`.

## Inputs required

Before writing, collect:
1. **Topic / procedure name** (exact, as it would appear in chart).
2. **Scope** — which variants to cover (e.g., for hysterectomy: laparoscopic, robotic, vaginal, abdominal, radical).
3. **Audience tier** — default: Phase 1 PACU orientee. Flag if different.
4. **Source chapters** — names of chapters from `/Drains-Perianesthesia-Nursing/` or `/corecurriculum/` the user wants cited. If none given, ask.
5. **Length target** — default 150–250 lines. Ask if user wants shorter/longer.
6. **Existing similar guide** — if the PACU repo already has a neighbor guide (e.g., for knee → look at hip), ask the user to point to it so style matches exactly.

## Workflow

1. **Confirm scope and sources.** Ask the user the six inputs above. Do not proceed with gaps.
2. **Load style contract.** Re-read `../../../PACU-MANUAL-STYLE-GUIDE.md` (adjust relative path after install). Match voice, heading depth, section ordering, red-flag table format, escalation phrasing.
3. **Draft outline.** Standard outline (adjust per procedure):
   - Overview (procedure, why it's done, anesthesia type commonly used)
   - Pre-PACU context (OR-to-PACU handoff expectations)
   - Admission priorities — **ABC structured**: Airway → Breathing → Circulation → Disability/pain → Exposure/drains
   - Procedure-specific monitoring (what makes *this* surgery different)
   - Pain management considerations
   - Common complications (each with: signs, nursing action, escalation trigger, who to call)
   - Red flags table (trigger → immediate action → escalate to)
   - Discharge-from-PACU criteria
   - Patient/family teaching points
   - Sources
4. **Write each section self-contained.** A nurse reading only one section must have everything they need. Repeat critical context rather than cross-referencing.
5. **Fill red flags table.** Minimum rows:
   - Airway compromise
   - Hemodynamic instability specific to this surgery
   - Surgery-specific bleeding or fluid issue
   - Procedure-specific neurologic or compartment concern (if applicable)
   - Pain out of proportion
6. **Cite by chapter title** inline (e.g., "*Drain's*, Ch. 32: Gynecologic Surgery"). No URLs unless sourced.
7. **Insert safety reminder** — one line near the top, pointing to `domain-healthcare-clinical/prompts/perianesthesia/SAFETY_PREAMBLE.md`.
8. **Self-check** (below) before returning.

## Output format

Deliver one markdown file, ready to save as `guides/{Procedure}-PACU-Guide.md`. Structure:

```markdown
# {Procedure} — PACU Guide

> Safety reminder: Educational aid only — verify doses, thresholds, and escalation paths against current facility protocol. See `domain-healthcare-clinical/prompts/perianesthesia/SAFETY_PREAMBLE.md`.

## Overview
[2–4 paragraphs]

## OR-to-PACU Handoff
[expected handoff content; SBAR-aligned]

## Admission Priorities (ABC)
### Airway
...
### Breathing
...
### Circulation
...
### Disability / Pain
...
### Exposure / Drains / Incision
...

## {Procedure}-Specific Monitoring
[what's unique about this surgery in PACU]

## Pain Management Considerations
[multimodal approach, regional block impact, common PCA/epidural setup]

## Common Complications
### {Complication 1}
- Signs: ...
- Nursing action: ...
- Escalation trigger: ...
- Call: {role}

[repeat for each]

## Red Flags Table
| Trigger | Immediate action | Escalate to |
|---|---|---|
| ... | ... | ... |

## Phase 1 → Phase 2 Discharge Criteria
[Aldrete or facility-specific, mark facility items as per protocol]

## Patient / Family Teaching Points
[bullet list]

## Sources
- Drain's PeriAnesthesia Nursing, Ch. XX: {Title}
- ASPAN Standards of Perianesthesia Nursing Practice, {year}
- [additional citations]
```

## Source-fidelity rules

- Cite every clinical fact to a textbook chapter title or ASPAN standard.
- For doses: quote verbatim from source or write *per facility protocol / per provider order*.
- For supplies, equipment, paging pathways: always *per facility protocol*.
- Do not fabricate URLs. Do not invent ASPAN standard numbers.

## Self-check (run before returning)

- [ ] Every section is self-contained (a nurse reading only this section has what they need).
- [ ] ABC ordering is preserved in Admission Priorities.
- [ ] Red flags table has ≥ 5 rows, each with trigger + action + escalation.
- [ ] Every complication has an escalation trigger and a role to call.
- [ ] No invented doses, no invented facility specifics.
- [ ] Sources cite chapter titles, not fabricated URLs.
- [ ] One safety reminder appears near the top.
- [ ] Length is within target (default 150–250 lines).
