---
title: "Study Plan Designer for Health-Professions Learners"
category: medical-education/learner-study-systems
description: "Given exam date, target score, available hours/week, and current knowledge gaps, generate a week-by-week study plan with resource mix, interleaving, retrieval blocks, qbank cadence, and rest days. Discipline- and exam-tailored."
techniques:
  - ST-02
  - ED-02
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
  - study-plan
  - board-prep
  - learner-self-study
  - interleaving
  - retrieval-practice
updated: "2026-05-15"
related_prompts:
  - ./learner_spaced_repetition_deck_generator.md
  - ./learner_weekly_study_review.md
  - ../exam-prep/learner_qbank_session_debriefer.md
---

# Study Plan Designer for Health-Professions Learners

**Objective:** Build a realistic, week-by-week board / shelf / exam study plan calibrated to the learner's exam date, available hours, baseline strengths and gaps, and target score. The plan includes content review, qbank progression, spaced retrieval, interleaving, rest, and weekly review checkpoints.

## When to Use
- ✅ Setting up dedicated board prep (USMLE Step 1/2/3, NCLEX, NAPLEX, PANCE, NREMT, NBDE, BCPS, etc.)
- ✅ Setting up shelf-exam prep during a clerkship
- ✅ Building a multi-month rotation-prep plan
- ❌ Real-patient guidance

## Inputs Required
- **Discipline & learner level**
- **Target exam & date**
- **Target score or pass threshold**
- **Available study hours per week** (be honest)
- **Baseline diagnostic score / NBME-style assessment result** (if any)
- **Strengths and gaps:** topics where strong vs weak
- **Constraints:** rotations, work, family, religious observances, planned vacation
- **Resource pool:** texts/videos/qbanks the learner has access to

## Constraints

**Must:**
- Be realistic with available hours — do not design a 60-hour plan for a learner with 25 hours/week
- Frontload content review on weakest, highest-yield topics
- Build qbank cadence that escalates over time and matches content review topics
- Include retrieval practice (not re-reading), interleaving, and rest days
- Schedule weekly check-ins and at least one mid-plan re-assessment
- Calibrate to exam type (NCLEX requires different mix than USMLE Step 1)

**Must Not:**
- Promise score outcomes
- Schedule zero rest
- Default to a generic plan that ignores the learner's specific gaps
- Recommend specific commercial products by brand for exam content; describe by type ("a high-yield video review series," "a comprehensive qbank")

## Instructions

1. **Confirm inputs.** If the learner did not provide a baseline assessment, recommend one before completing the plan.

2. **Time-budget reality check.** Compare available hours × weeks until exam against the rough range typically needed for the target exam. Flag if the gap is large; suggest hour increase or exam-date push if appropriate.

3. **Weighted topic priority list.** From the learner's gaps, rank topics by:
   - Frequency on the target exam (high / moderate / low)
   - Learner's current strength (strong / acceptable / weak)
   - Foundational nature (concepts that unlock other content score higher)

4. **Week-by-week plan.** For each week:
   - **Content review topics** (with target depth: introduce / consolidate / refine)
   - **Qbank blocks** (tutor vs timed; size; topic mix vs random)
   - **Retrieval blocks** (Anki / cloze review / self-quizzing)
   - **Interleaving:** mix new with previously-covered topics — do not silo
   - **Weekly review checkpoint:** uses `study_weekly_review.md`
   - **Rest days** (at least one full day; more if needed)

5. **Mid-plan re-assessment.** At ~50% of the timeline, schedule a full-length practice exam under realistic conditions. Use results to revise priority list.

6. **Final-week taper.** Light review, no new content, well-being focus, exam-day logistics rehearsal.

7. **Exam-tailored cadence notes:**
   - USMLE Step 1: heavy mechanism focus + UWorld-style qbank progression; aim for one practice exam per 2-3 weeks in dedicated
   - USMLE Step 2 CK / 3: clinical reasoning + management; qbank progression slightly later but heavier
   - NCLEX: priority/safety/delegation reasoning is the dominant axis; lower-yield to memorize obscure facts
   - NAPLEX / BCPS: drug-by-drug nuance + therapeutic decision-making
   - PANCE: broad clinical reasoning + management
   - NREMT: protocol-driven decision-making + scene reasoning + practical skills
   - NBDE / INBDE: dental sciences integration with clinical applications

8. **Self-check block:**
   - State the next 3 weekly priorities from memory
   - One thing you'll cut from the plan if life intervenes — and one thing you won't
   - When is your mid-plan re-assessment?

## False-Positive Prevention

| ❌ Common Mistake | ✅ Correct Approach |
|---|---|
| Schedule more hours than available | Reality check first; revise inputs |
| Re-reading-heavy schedule | Retrieval-heavy; re-reading should be minimal |
| No qbank early | Some qbank from week 1, even at small volume |
| No rest days | Build them in; sleep is study |
| Generic plan for any exam | Exam-tailored cadence |
| No mid-plan re-assessment | Always schedule one |
| Brand-name specific products | Resource type only |

## Output Format

```
### Inputs Echo
- Exam / date / target / available hours / baseline / constraints / resources

### Time-Budget Reality Check
- Hours available × weeks vs typical needed
- Flag and adjustment

### Weighted Topic Priority
| Topic | Frequency | Strength | Foundational | Rank |

### Week-By-Week Plan
**Week 1:** Content / Qbank / Retrieval / Interleave / Rest / Checkpoint
**Week 2:** ...
...
**Mid-plan re-assessment (week X):** full-length practice exam

**Final week:** taper

### Exam-Tailored Cadence Notes
- Exam-specific emphasis

### Self-Check
1. Next 3 weekly priorities
2. Cut vs preserve under disruption
3. Mid-plan re-assessment date
```

## Verification Checklist
- [ ] Hours / weeks reality check performed
- [ ] Weighted topic priority list present
- [ ] Week-by-week plan with content / qbank / retrieval / interleave / rest / checkpoint
- [ ] Mid-plan re-assessment scheduled
- [ ] Final-week taper included
- [ ] Exam-tailored cadence notes
- [ ] No brand-name product endorsements
- [ ] Self-check uses retrieval
- [ ] No real-patient guidance (not applicable here but redirect maintained in tone)
