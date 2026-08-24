---
name: pacu-in-depth-explainer
description: Produce a deep conceptual explainer for a single PACU topic — pathophysiology → clinical correlation → PACU implications → assessment pearls. Use when the user wants to "explain in depth", "teach the why behind X", "help me understand the physiology of Y in PACU", or needs a longer-form teaching document than a guide section. Output is 500–1500 words, teaching-oriented, preserves mechanistic reasoning.
tags:
  - pacu
  - nursing-education
  - explainer
  - pathophysiology
updated: "2026-04-14"
---

# PACU In-Depth Explainer

## Purpose

Generate a mechanistic, teaching-oriented explainer on one PACU topic. Goal: the reader can explain not just *what* to do but *why*. Bridges pathophysiology to bedside assessment.

## When to use

- User says "explain in depth", "teach the why", "help me understand", "mechanism of X".
- Preceptor wants teaching material for a one-on-one debrief or a huddle topic.
- Orientee has passed the surface and needs the reasoning layer.

## When NOT to use

- User needs a scannable card → `pacu-quick-reference-author`.
- User needs testable content → `pacu-quiz-generator`.
- User needs a full procedure orientation document → `pacu-comprehensive-guide-author`.

## Inputs required

1. **Topic** (single focused concept — e.g., "residual neuromuscular blockade", "spinal anesthesia hypotension", "PONV pathways").
2. **Learner level** — novice orientee vs. experienced nurse.
3. **Specific bedside scenarios** the user wants explained.
4. **Source chapters**.

## Workflow

1. **Tighten the topic.** Push back if the topic is too broad ("respiratory complications" → ask for one specific complication or physiologic mechanism).
2. **Structure around four tiers:**
   - Foundation — relevant anatomy / physiology (only what the PACU nurse must know).
   - Mechanism — what's actually happening in the patient.
   - Clinical correlation — how the mechanism shows up in vitals, exam, patient report.
   - PACU implications — what the nurse does about it, what to escalate.
3. **Add "Common misconceptions" section** — what orientees often get wrong about this topic.
4. **Add "Assessment pearls"** — 3–7 specific observations that separate textbook signs from real bedside signal.
5. **Add "Teach-back questions"** — 3–5 questions the preceptor can ask to check understanding.
6. **Cite sources by chapter title.**
7. **Insert safety reminder.**
8. **Self-check.**

## Output format

```markdown
# {Topic} — In-Depth PACU Explainer

> Safety reminder: Educational aid only — verify thresholds, doses, and escalation against facility protocol.

## Why this matters in PACU
[1 paragraph grounding the topic in a realistic PACU scenario]

## Foundation (just enough anatomy / physiology)
[focused, not a textbook recap]

## Mechanism — what's happening
[the "why"]

## Clinical correlation — how it shows up
- Vitals: ...
- Exam: ...
- Patient report: ...
- Monitors / devices: ...

## PACU implications — what you do
### Assessment
### Intervention
### Escalation trigger and who to call

## Common misconceptions
- ...

## Assessment pearls
- ...

## Teach-back questions
1. ...

## Sources
- ...
```

## Source-fidelity rules

Cite textbook chapters and ASPAN standards. No fabricated physiology specifics. Where mechanisms are debated, flag with "current thinking / evidence is mixed".

## Self-check

- [ ] Topic is single and specific.
- [ ] Four-tier structure is present (foundation → mechanism → correlation → implications).
- [ ] "Common misconceptions" has ≥ 3 items.
- [ ] Teach-back questions have ≥ 3 items.
- [ ] Length 500–1500 words.
- [ ] No invented doses / pathways; citations present.
- [ ] Safety reminder at top.
