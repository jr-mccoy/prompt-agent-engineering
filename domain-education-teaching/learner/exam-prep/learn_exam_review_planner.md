---
title: "Exam Review Planner"
category: education-teaching/learner/exam-prep
description: "Creates a prioritized, content-based exam review plan: classifies topics by yield, assigns daily coverage based on available days and mastery gaps, and builds a contingency buffer."
techniques:
  - ST-01
  - ST-03
  - CM-01
  - ED-02
  - QA-04
difficulty: beginner
tags:
  - exam-prep
  - review-planning
  - prioritization
  - study-schedule
  - high-yield
updated: "2026-05-15"
related_prompts:
  - domain-education-teaching/learner/memory-and-recall/learn_spaced_review_scheduler.md
  - domain-education-teaching/learner/exam-prep/learn_study_next_advisor.md
  - domain-education-teaching/learner/exam-prep/learn_weak_area_diagnosis.md
  - domain-education-teaching/learner/exam-prep/learn_finals_week_plan.md
---

## Objective

Given an exam's topic scope, the number of days until the exam, and the learner's current mastery levels, produce a prioritized daily review plan that focuses study time where it will earn the most points.

## When to Use

- 3–21 days before an exam, when there is still time to improve performance systematically
- When the learner has too much material to review everything and needs to triage
- When a general "study all of it" plan has been failing and a strategic plan is needed
- After getting a practice exam back and needing to redirect effort based on results

**Do not use** the night before an exam (too late for strategic planning — use a light review and sleep instead). For multi-month study cycles, use `learnstudy_spaced_review_scheduler.md` instead.

## Instructions

1. **Collect exam details.**
   - Ask: "What subject and exam type? (e.g., midterm, final, licensing, certification)"
   - Ask: "How many days until the exam?"
   - Ask: "How many hours per day can you realistically study? (be conservative)"
   - Ask: "List all topics covered. For each, rate: (a) your current mastery Low/Medium/High and (b) how heavily you expect it to appear on the exam — High/Medium/Low yield."
   - Ask: "What format is the exam? (MCQ, short answer, essay, problem sets, clinical)"
   - Ask: "Are there any topics you know will not be on the exam? (to exclude)"

2. **Classify each topic on a 2×2 yield-mastery matrix.**

   | | High Mastery | Low Mastery |
   |---|---|---|
   | **High Yield** | Maintain — quick review | **Priority 1 — Fix first** |
   | **Low Yield** | Skip or skim | Low priority — address only if time permits |

   Priority rules:
   - P1 (Fix first): High yield + Low/Medium mastery
   - P2 (Strengthen): High yield + Medium mastery (partially solid)
   - P3 (Maintain): High yield + High mastery
   - P4 (Low priority): Low yield regardless of mastery

3. **Allocate study days.**
   - Days 1 through [N−2]: Active study of P1 and P2 topics
   - Day N−1: Integration and P3 maintenance review
   - Day N (day of exam): Light review only (≤30 min) — no new material

   Distribute P1 topics earlier in the window (more time to consolidate). P2 topics follow. Build in one buffer day per 7-day block.

4. **For each day, specify:**
   - Topic(s) to cover
   - Activity type matched to mastery level:
     - P1 (Low mastery): Read/re-learn → practice problems → self-test
     - P2 (Medium mastery): Retrieval drill → targeted practice → error review
     - P3 (High mastery): Spaced retrieval check only (15 min max)
   - Estimated time
   - Success criterion for that day's block

5. **Identify "exam-format-specific" preparation.**
   - MCQ: include a session of MCQ-format practice for top P1/P2 topics
   - Short answer: include at least one session of writing-out answers from memory
   - Problem sets: include one timed problem session under exam conditions
   - Essay: include one outline-from-memory session

6. **Include a triage decision.**
   If there are more P1 topics than available study hours can cover, name the ones to deprioritize and explain why (based on yield estimate and time remaining).

## Output Format

```
# Exam Review Plan: [Exam Name]
Days available: N | Study hours/day: H | Format: [MCQ/essay/etc.]

## Topic Classification

| Topic | Mastery | Exam Yield | Priority | Action |
|---|---|---|---|---|
| ... | Low | High | P1 | Fix first |

## Triage (if needed)
Topics deprioritized due to time constraints: [list + reason]

## Daily Plan

### Day 1 — [Date]
Topics: [list]
Activity: [type]
Checkpoint: [success criterion]
Est. time: [N min]

[Repeat through Day N]

## Exam-Format Preparation
[Specific session for exam format]

## Caveats
...
```

## Example Output

---

**Input:** MCAT Biology section — 12 days until exam — 3 hours/day — MCQ format

Topics + ratings:
- Cell biology: Mastery High, Yield High
- Genetics & Heredity: Mastery Medium, Yield High
- Evolution & Natural Selection: Mastery Low, Yield Medium
- Molecular Biology (DNA replication, transcription, translation): Mastery Low, Yield High
- Metabolism (glycolysis, TCA, ETC): Mastery Medium, Yield High
- Organ Systems (nervous, endocrine, musculoskeletal): Mastery Medium, Yield High
- Microbiology (bacteria, viruses, immune): Mastery Low, Yield High
- Biochemistry fundamentals: Mastery High, Yield Medium
- Research Methods & Statistics: Mastery High, Yield Low

---

# Exam Review Plan: MCAT Biology
Days available: 12 | Study hours/day: 3 hrs (180 min) | Format: MCQ

## Topic Classification

| Topic | Mastery | Yield | Priority | Action |
|---|---|---|---|---|
| Molecular Biology (DNA/RNA/protein) | Low | High | **P1** | Fix first — largest gap, highest yield |
| Microbiology | Low | High | **P1** | Fix first |
| Genetics & Heredity | Medium | High | **P2** | Strengthen |
| Metabolism (glycolysis/TCA/ETC) | Medium | High | **P2** | Strengthen |
| Organ Systems | Medium | High | **P2** | Strengthen |
| Evolution | Low | Medium | **P3** | Lower priority — low yield reduces urgency |
| Cell Biology | High | High | **Maintain** | Quick review only |
| Biochemistry fundamentals | High | Medium | **Maintain** | Quick review — already solid |
| Research Methods | High | Low | **Skip** | High mastery + low yield — do not spend time here |

---

## Triage

Evolution is Low mastery but Medium yield — with 12 days available, it will fit. Research Methods is skipped entirely (High mastery + Low yield = time is better spent elsewhere).

If study hours drop below 2.5/day, deprioritize Evolution first, then Biochemistry fundamentals.

---

## Daily Plan

### Day 1 (May 15) — Molecular Biology Part 1
Topics: DNA replication, transcription
Activity: Content review → draw replication fork from memory → create a flowchart of transcription from template strand to mRNA
Checkpoint: Can draw and label the replication fork including enzymes (helicase, primase, polymerase, ligase) without notes
Est. time: 180 min

---

### Day 2 (May 16) — Molecular Biology Part 2
Topics: Translation, gene regulation (operons)
Activity: Translate a codon sequence using codon chart → draw the ribosome translation cycle → explain lac operon induction from memory
Checkpoint: Correctly translate a 6-codon sequence; explain operon regulation in 90 seconds without notes
Est. time: 180 min

---

### Day 3 (May 17) — Microbiology Part 1
Topics: Bacterial cell structure, reproduction, genetics (conjugation, transformation, transduction)
Activity: Draw bacterial vs. eukaryotic cell comparison → explain each horizontal gene transfer mechanism in own words
Checkpoint: Correctly identify 5 bacterial structures on a diagram; explain all three HGT mechanisms with examples
Est. time: 180 min

---

### Day 4 (May 18) — Microbiology Part 2 + MCQ Drill
Topics: Viruses, immune response basics
Activity: Viral replication cycle (lytic vs. lysogenic) → 20 MCAT-style MCQs covering all microbiology topics done so far
Checkpoint: ≥75% correct on MCQ drill; any incorrect answers reviewed and re-attempted
Est. time: 180 min

---

### Day 5 (May 19) — Genetics & Heredity Part 1
Topics: Mendelian genetics, pedigree analysis, sex-linked traits
Activity: Solve 10 pedigree problems including autosomal dominant/recessive and X-linked → write out Hardy-Weinberg equations from memory
Checkpoint: 8/10 pedigree problems correct
Est. time: 180 min

---

### Day 6 (May 20) — Genetics + Metabolism
Topics: Non-Mendelian genetics (incomplete dominance, codominance, polygenic) + Glycolysis
Activity: Genetics problem set (non-Mendelian) → glycolysis pathway drawn from memory with ATP yield at each step
Checkpoint: Draw complete glycolysis with correct substrates, products, and energy yield at each step
Est. time: 180 min

---

### Day 7 (May 21) — Buffer Day
Use for: Any topic where a Day 1–6 checkpoint was not met. If all checkpoints passed, use for timed MCQ practice (30 questions, mixed topics from the first 6 days)
Est. time: 90–180 min (as needed)

---

### Day 8 (May 22) — Metabolism Part 2
Topics: TCA cycle, electron transport chain, ATP yield
Activity: Draw TCA cycle from memory → trace electron flow through ETC → calculate total ATP yield from 1 glucose
Checkpoint: Correctly state the total ATP yield from glucose under aerobic conditions and explain each stage's contribution
Est. time: 180 min

---

### Day 9 (May 23) — Organ Systems Part 1
Topics: Nervous system, endocrine system
Activity: Neuron anatomy and action potential from memory → hormone class distinctions (peptide vs. steroid) → HPA axis
Checkpoint: Explain how a nerve impulse crosses a synapse; correctly classify 8 hormones by mechanism
Est. time: 180 min

---

### Day 10 (May 24) — Organ Systems Part 2
Topics: Musculoskeletal system, cardiovascular basics
Activity: Draw sliding filament mechanism → cardiac cycle and ECG components → 15-question MCQ drill on organ systems
Checkpoint: ≥70% MCQ drill score; describe sliding filament from memory in under 2 minutes
Est. time: 180 min

---

### Day 11 (May 25) — Integration and Maintenance
Topics: Cell biology (quick), Evolution (quick), timed full-section practice
Activity: 30-minute retrieval pass on Cell Biology (already High mastery — confirm it's still solid) → 20 Evolution MCQs → 59-question timed MCAT Biology practice section under exam conditions
Checkpoint: Practice section ≥80th percentile score estimate; any topic below 60% accuracy flagged for Day 12
Est. time: 180 min

---

### Day 12 (May 26 — Day Before Exam)
Activity: 45-minute review ONLY — revisit any topics that fell below threshold in Day 11 practice. Do not study new material. Organize exam logistics (location, ID, timing). Sleep 8 hours.
Checkpoint: Done by 8 PM. In bed by 10 PM.

---

### Exam Day (May 27)
30-minute light review: core formulas, key terms for 3 weakest topics only. No heavy content review.

---

## Exam-Format Preparation (MCQ-Specific)

MCAT Biology is MCQ — reasoning under time pressure matters as much as knowledge.

Dedicated MCQ sessions:
- Day 4: 20 questions (microbiology-specific)
- Day 10: 15 questions (organ systems)
- Day 11: Full 59-question timed practice section

During all MCQ sessions:
1. Attempt the question before reading answer choices (prevents anchoring)
2. Mark any question where you guessed or were uncertain
3. Review marked questions immediately after the set, not during

---

## Caveats

This plan assumes 3 hours/day of focused, active study — not passive reading. If review sessions turn into re-reading rather than retrieval practice and problem-solving, the time estimates will underrun the actual learning needed.

Research Methods is skipped. If you encounter Research Methods questions in practice (Day 11), re-evaluate this triage decision.

---

## False-Positive Prevention

**❌ DON'T** assign equal time to all topics — this produces a plan that fails the most important topics by treating them like the least important.

**✅ DO** explicitly rank topics by yield × mastery gap and allocate proportionally more days to P1 topics.

**❌ DON'T** plan the night before the exam as a heavy study session — fatigue impairs next-day retrieval.

**✅ DO** explicitly restrict Day N to ≤30 min of light review and prioritize sleep.

**❌ DON'T** skip the buffer day — it is not a failure state. It is the plan's error-correction mechanism.

**✅ DO** treat the buffer day as a contingency slot, not a rest day and not a slot to fill in advance.

**❌ DON'T** confuse "high yield" with "what I like" or "what I'm good at" — yield should reflect the exam's topic weighting, not learner preference.

**✅ DO** ask learners to base yield estimates on past exams, professor guidance, or course learning objectives — not instinct.

## Quality Criteria

- [ ] All topics classified on yield × mastery matrix
- [ ] P1 topics receive the most study days and appear earliest in the plan
- [ ] Buffer day is included (one per 7-day block) and labeled as contingency
- [ ] Exam day is ≤30 min review only
- [ ] Each study day has a topic, activity type, and success criterion checkpoint
- [ ] Exam-format-specific preparation is included
- [ ] Triage decision is explicit when not all topics can be covered

## Techniques Used

- **ST-01 (Clear Objective Statement):** Objective specifies yield-based prioritization as the distinguishing feature of this planner
- **ST-03 (Output Format Specification):** Matrix + daily plan format is immediately executable
- **CM-01 (Explicit Context Framing):** All planning inputs are collected before any output is generated
- **ED-02 (Progressive Exercise Generation):** Activity types scale with mastery level (re-learn → drill → timed test)
- **QA-04 (Uncertainty Acknowledgment):** Caveats section states what assumptions could invalidate the plan
