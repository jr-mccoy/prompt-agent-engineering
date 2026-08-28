---
title: "Spaced Repetition Deck Generator for Health-Professions Learners"
category: medical-education/learner-study-systems
description: "From a topic or learner notes, generate Anki-style flashcards (cloze + Q/A) with leech-resistant phrasing, atomic facts, image-occlusion suggestions, and a recommended initial review schedule. Discipline-tailored."
techniques:
  - ED-01
  - ED-06
  - CM-02
  - QA-01
difficulty: beginner
audience: learner
disciplines:
  - medicine
  - nursing
  - physician-assistant
  - pharmacy
  - ems
  - allied-health
  - dental
intended_use: education-and-practice
tags:
  - spaced-repetition
  - anki
  - flashcards
  - srs
  - study-planning
  - learner-self-study
updated: "2026-05-15"
related_prompts:
  - ./learner_study_plan_designer.md
  - ../exam-prep/learner_high_yield_topic_compressor.md
---

# Spaced Repetition Deck Generator for Health-Professions Learners

**Objective:** Convert a topic, set of notes, or compressed study sheet into a set of well-designed flashcards (cloze deletion and Q/A) optimized for spaced-repetition system (SRS) review. Cards are atomic, leech-resistant, image-occlusion-friendly where applicable, and grouped by sub-topic.

## When to Use
- ✅ Building a personal Anki deck during board prep or rotations
- ✅ Converting a class lecture into durable cards
- ✅ Pre-rotation specialty compression
- ❌ Real-patient management

## Inputs Required
- **Discipline & learner level**
- **Source material:** topic name OR pasted notes / sheet
- **Number of cards desired:** typically 15-40 per topic; 60+ becomes unmaintainable
- **Card type preference:** cloze / Q&A / mixed (default mixed)
- **SRS app:** Anki / RemNote / other (for syntax)

## Constraints

**Must:**
- Make each card atomic (one fact per card)
- Avoid lists with more than 4 cloze deletions on a single card (becomes a leech)
- Cloze the *discriminator*, not the obvious term
- Tag cards by sub-topic and difficulty
- Provide an initial review schedule and a leech-management note

**Must Not:**
- Generate giant info-dump cards
- Include patient-specific dosing — class + qualitative dose principle only
- Invent specific numerics
- Default to physician-centric phrasing

## Instructions

1. **Receive source material.** If a topic name, expand to the high-yield content first (or call out the need to use the topic compressor prompt first). If notes, use the notes as the substrate.

2. **Atomize.** Break the source into atomic facts. One concept per card.

3. **Choose card type per fact.**
   - **Cloze:** for facts with a clear keyword or discriminator
   - **Q&A:** for facts that need a question prompt to retrieve
   - **Image-occlusion suggestion:** for anatomy, ECG morphology, imaging patterns, histology — note "candidate for image occlusion: [structure/finding]"

4. **Phrase cards leech-resistant:**
   - Cloze the discriminator, not the obvious noun
   - Avoid double-negatives
   - Avoid listing more than 4 cloze deletions on a single card
   - Avoid "all of the above"-style cards
   - For drug classes, separate cards for: MoA / indication / side effect / contraindication / interaction / monitoring — not one card per drug

5. **Tag cards.** Tags by sub-topic, system, and difficulty (intro / standard / nuance). Discipline tag where the card is discipline-specific.

6. **Discipline-tailored emphasis:**
   - Medicine/PA: mechanism + dx + management cards
   - Nursing: monitoring parameters, intervention triggers, patient teaching points
   - Pharmacy: drug-by-drug nuance, drug-drug interactions, dose adjustment principles
   - EMS: protocol triggers, time-critical recognition, drug-route-dose-principle (not patient-specific numerics)
   - Allied health: functional cards (goals, outcome measures, intervention rationale)
   - Dental: anatomy, materials, procedure sequences, oral manifestations of systemic dz

7. **Recommended initial schedule:**
   - Default Anki settings work for most users
   - For a board prep dedicated period, increase new cards/day initially (15-25) then taper as the deck matures
   - Leech threshold: if a card lapses 4+ times, rewrite or suspend — list flagged-leech candidates

8. **Output format.** Plain text that pastes into Anki (Q\tA newline) or `{{c1::cloze}}` syntax. Include a separate JSON or CSV block if the learner requests.

9. **Self-check block:**
   - Pick 5 random cards and retrieve from memory
   - For one card, state why you clozed the term you clozed
   - One card you'd rewrite for better discrimination

## False-Positive Prevention

| ❌ Common Mistake | ✅ Correct Approach |
|---|---|
| Multi-fact mega-cards | Atomize — one fact per card |
| Cloze the obvious term | Cloze the discriminator |
| 6+ cloze deletions on one card | Cap at 4 |
| Drug-specific patient dosing | Class + qualitative dose principle |
| One card per drug for everything | Separate cards by attribute (MoA / SE / etc.) |
| No tags | Always tag for sub-topic + difficulty |
| One-size emphasis | Discipline-tailored |

## Output Format

```
### Source / Discipline / Card Count / Card Type Preference / SRS App

### Cards
(Anki-importable; tab-separated for Q&A, or {{c1::}} for cloze)

[Tag: sub-topic-system-difficulty-discipline]

Card 1: ...
Card 2: ...
...

### Image-Occlusion Candidates
- Structure / finding / where in source

### Leech Watch
- Cards likely to lapse and why — rewrite suggestion

### Initial Schedule Notes
- Suggested new cards/day for this topic
- Leech threshold note

### Self-Check
1. Five-card retrieval
2. Why you clozed what you clozed (one card)
3. One card you'd rewrite
```

## Verification Checklist
- [ ] Cards are atomic
- [ ] Cloze deletions ≤ 4 per card
- [ ] Cloze targets the discriminator
- [ ] Tags applied
- [ ] Image-occlusion candidates noted where applicable
- [ ] Drug content uses class + qualitative dose principle
- [ ] Discipline-tailored emphasis
- [ ] Leech-watch entries flagged
- [ ] Real-patient redirect language present
