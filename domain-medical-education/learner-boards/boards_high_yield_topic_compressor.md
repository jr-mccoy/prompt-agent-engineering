---
title: "High-Yield Topic Compressor for Health-Professions Learners"
category: medical-education/learner-boards
description: "Compress a broad topic (e.g., 'anti-arrhythmics,' 'vasculitides,' 'acid-base,' 'electrolyte disorders') into a tight high-yield study sheet: must-know facts, discriminators, mnemonics, common board traps, and 5 self-test questions."
techniques:
  - ED-01
  - ED-06
  - CM-02
  - QA-01
difficulty: intermediate
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
  - high-yield
  - board-prep
  - topic-compression
  - learner-self-study
updated: "2026-05-15"
related_prompts:
  - ./learner_board_style_question_review.md
  - ../study-planning/learner_spaced_repetition_deck_generator.md
---

# High-Yield Topic Compressor for Health-Professions Learners

**Objective:** Take a broad topic and produce a compressed, high-yield study sheet — must-know facts, discriminators between subtypes, classic board traps, useful mnemonics (only ones that earn their keep), and five self-test questions — that the learner can review in under 15 minutes.

## When to Use
- ✅ Final-week board prep on broad topics
- ✅ Pre-rotation compression for a specialty
- ✅ Re-establishing a topic before re-doing a qbank section
- ❌ Real-patient management

## Inputs Required
- **Discipline & learner level**
- **Topic:** the broad topic to compress (e.g., "anti-arrhythmics," "vasculitides," "acid-base disorders," "pediatric murmurs," "anticoagulants," "cranial nerve palsies")
- **Target review time:** typical 10-15 minutes

## Constraints

**Must:**
- Cap the sheet at the equivalent of a 10-15 minute review (i.e., not a textbook chapter)
- Lead with discriminators — what separates subtypes is more valuable than what they share
- Include only mnemonics that *earn* their place (an obscure mnemonic for a fact you'll forget anyway is noise)
- Include 3-5 classic board traps for the topic
- End with 5 self-test questions

**Must Not:**
- Produce a textbook chapter
- Provide real-patient guidance
- Invent specific dosing or numeric cutoffs
- Default to physician-centric framing

## Instructions

1. **Confirm topic and discipline.**

2. **High-yield core (4-7 bullets):** the must-know facts about the topic. Each fact one line, the kind of thing that anchors a question.

3. **Subtype discriminator table.** If the topic has subtypes (anti-arrhythmics: Class I/II/III/IV; vasculitides: large/medium/small vessel), build a small table:

   | Subtype | Distinguishing feature | Classic example | What it gets confused with |
   | --- | --- | --- | --- |

4. **Mechanism quick map.** For topics where mechanism is the lever (pharmacology, electrolyte disorders), give a one-paragraph mechanism map that ties together the subtypes.

5. **Classic board traps (3-5).** Examples:
   - "Procainamide → lupus-like syndrome — not hydralazine" (or vice versa, depending on the trap)
   - "Hypokalemia → U-wave; hyperkalemia → peaked T then loss of P"
   - "Polyarteritis nodosa spares the lungs"
   For each, the trap and the corrective discriminator.

6. **Earned mnemonics.** If a mnemonic is well-known and useful, include it. If not, leave it out. Mnemonics in this sheet should be:
   - Tied to discriminators or sequence
   - Easier to remember than the facts themselves
   - Not invented on the spot if a canonical one exists

7. **Discipline-tailored emphasis.**
   - Medicine/PA: dx + management implications
   - Nursing: monitoring and intervention triggers
   - Pharmacy: drug-by-drug nuance, monitoring, interactions
   - EMS: time-critical recognition and protocol-relevant actions
   - Allied health: functional implications
   - Dental: oral manifestations, dental management modifications

8. **Five self-test questions.** Two recognition (recognize a syndrome from features), two discriminator (A vs B), one application (apply mechanism to a vignette). Answer key separate.

9. **Spaced re-test schedule.** Day 1, 3, 7, 14, 30.

## False-Positive Prevention

| ❌ Common Mistake | ✅ Correct Approach |
|---|---|
| Produce a textbook chapter | Cap at 10-15 minute review |
| Include every fact "just in case" | Cut to discriminators and must-knows |
| Invent a mnemonic that's harder than the facts | Skip — only earned mnemonics |
| Skip board traps | Traps are where the sheet earns its place |
| Generic emphasis | Discipline-tailored |
| No self-test | End with 5 questions, always |

## Output Format

```
### Topic / Discipline / Target Review Time

### High-Yield Core
- Fact 1
- Fact 2
- ...

### Subtype Discriminator Table
| Subtype | Distinguishing feature | Classic example | Confused with |

### Mechanism Quick Map
<paragraph>

### Classic Board Traps
1. Trap → discriminator
2. ...

### Earned Mnemonics
- Mnemonic → what it encodes

### Discipline-Tailored Emphasis
- Role-specific focus

### Self-Test Questions (5)
1-5
Answer key (separate)

### Spaced Re-Test Schedule
Day 1, 3, 7, 14, 30
```

## Verification Checklist
- [ ] Compressed to a 10-15 minute review
- [ ] Discriminator table present where subtypes exist
- [ ] 3-5 classic board traps with discriminators
- [ ] Only earned mnemonics included
- [ ] Discipline-tailored emphasis present
- [ ] 5 self-test questions with answer key
- [ ] Real-patient redirect language present
