---
title: "Spaced Review Scheduler"
category: education-teaching/learner-study-skills
description: "Builds a personalized spaced repetition schedule from a concept or card list, assigning review intervals based on difficulty and exam timeline, and producing a dated calendar the learner can follow."
techniques:
  - ST-01
  - ST-03
  - CM-01
  - ED-02
  - QA-04
difficulty: intermediate
tags:
  - spaced-repetition
  - scheduling
  - exam-prep
  - forgetting-curve
  - retrieval-practice
updated: "2026-05-15"
related_prompts:
  - domain-education-teaching/teaching_study_flashcard_generator.md
  - domain-education-teaching/learner-study-skills/learnstudy_confidence_calibration.md
  - domain-education-teaching/learner-study-skills/learnstudy_study_next_advisor.md
---

## Objective

Take a list of concepts, topics, or flashcard decks and produce a practical, dated spaced repetition review schedule calibrated to the learner's exam date, daily study capacity, and self-assessed mastery levels.

## When to Use

- After creating flashcards or a concept list and needing a review plan
- When studying for a high-stakes exam weeks out and wanting to distribute review sessions optimally
- When managing multiple subjects simultaneously and needing to prevent review collisions
- When returning to material after a gap and needing to recalibrate intervals

**Do not use** as a substitute for initial learning — spacing only works after first encoding. Do not use when the exam is less than 48 hours away (use `learnstudy_exam_review_planner.md` instead).

## Instructions

1. **Collect required inputs.**
   - Ask for the topic/card list (can be a numbered list, a deck name, or a rough topic outline)
   - Ask: "When is your exam? (date or days from now)"
   - Ask: "How many minutes per day can you realistically dedicate to review? (be honest — not aspirational)"
   - Ask: "For each topic or group, rate your current mastery: New (never studied), Shaky (studied but uncertain), Solid (confident but needs maintenance), Mastered (very confident)"
   - Ask: "Do you have any fixed days off or conflicts in the window before the exam?"

2. **Assign initial review intervals based on mastery.**
   Apply these starting intervals (based on the Ebbinghaus forgetting curve and SM-2 principles):

   | Mastery level | First review | Second review | Third review | Fourth review |
   |---|---|---|---|---|
   | New | Day 1 | Day 3 | Day 7 | Day 14 |
   | Shaky | Day 2 | Day 5 | Day 10 | Day 20 |
   | Solid | Day 4 | Day 10 | Day 21 | Day 35 |
   | Mastered | Day 7 | Day 21 | Day 42 | (skip if exam is sooner) |

   Caveat: these are starting intervals — intervals should lengthen if the learner recalls correctly and shorten if they do not.

3. **Map intervals onto the exam timeline.**
   - Anchor Day 0 = today
   - Calculate when each review falls relative to the exam date
   - Flag any review that lands after the exam date (skip or compress)
   - Ensure the final review of each topic falls 1–3 days before the exam (recency effect)

4. **Balance the daily load.**
   - Calculate total review minutes per day (number of items × estimated time per item, typically 1–3 min per card/concept)
   - If any day exceeds the learner's stated daily capacity, redistribute: pull some reviews forward 1 day, push non-urgent ones back 1 day
   - If the total volume is impossible within the available time, flag which topics to deprioritize and why

5. **Output a dated schedule table.**
   Format as a calendar table: Date | Topics to Review | Estimated Minutes | Notes

6. **Include modification rules.**
   After the schedule, provide 3–4 explicit rules for adjusting intervals in real time:
   - If you recalled correctly and easily → extend next interval by 1.5×
   - If you recalled with effort → keep the scheduled interval
   - If you failed to recall → shorten next interval to 50% and re-queue
   - If you completely blanked → reset to Day 1 interval and mark as "Shaky"

7. **Flag uncertainty and assumptions.**
   State clearly: "This schedule assumes [X minutes/day], [Y mastery ratings you provided], and [Z days to exam]. If any of these change, reschedule."

## Output Format

```
# Spaced Review Schedule
Generated: [today's date] | Exam: [exam date] | Days remaining: [N]

## Inputs Received
- Topics/cards: [list or summary]
- Daily capacity: [N minutes]
- Mastery ratings: [brief table]
- Days off: [if any]

## Interval Assignments
| Topic | Mastery | Review 1 | Review 2 | Review 3 | Review 4 |
|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... |

## Daily Schedule
| Date | Day # | Topics to Review | Est. Minutes | Notes |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## Modification Rules
1. Recalled easily → ...
2. Recalled with effort → ...
3. Failed to recall → ...
4. Total blank → ...

## Assumptions & Caveats
...
```

## Example Output

---

**Input:** 8 topics from Organic Chemistry I | Exam in 18 days | 45 min/day | No days off

---

# Spaced Review Schedule
Generated: 2026-05-15 | Exam: 2026-06-02 | Days remaining: 18

## Inputs Received
- **Topics:** Hybridization, Resonance, Stereochemistry (R/S), Nucleophilic Substitution (SN1/SN2), Elimination (E1/E2), Carbonyl Chemistry, NMR Interpretation, IR Spectroscopy
- **Daily capacity:** 45 minutes
- **Days off:** None
- **Mastery ratings:**

| Topic | Mastery |
|---|---|
| Hybridization | Solid |
| Resonance | Shaky |
| Stereochemistry (R/S) | New |
| SN1/SN2 | Solid |
| E1/E2 | Shaky |
| Carbonyl Chemistry | New |
| NMR Interpretation | Shaky |
| IR Spectroscopy | Mastered |

## Interval Assignments

| Topic | Mastery | Review 1 | Review 2 | Review 3 | Review 4 |
|---|---|---|---|---|---|
| Hybridization | Solid | Day 4 | Day 10 | Day 17 | — (exam Day 18) |
| Resonance | Shaky | Day 2 | Day 5 | Day 11 | Day 17 |
| Stereochemistry | New | Day 1 | Day 3 | Day 7 | Day 15 |
| SN1/SN2 | Solid | Day 4 | Day 10 | Day 17 | — |
| E1/E2 | Shaky | Day 2 | Day 5 | Day 11 | Day 17 |
| Carbonyl Chemistry | New | Day 1 | Day 3 | Day 8 | Day 16 |
| NMR Interpretation | Shaky | Day 2 | Day 6 | Day 12 | Day 17 |
| IR Spectroscopy | Mastered | Day 7 | Day 17 | — | — |

## Daily Schedule

| Date | Day | Topics to Review | Est. Min | Notes |
|---|---|---|---|---|
| May 15 | 1 | Stereochemistry (R/S), Carbonyl Chemistry | 30 | First pass — initial encoding review |
| May 16 | 2 | Resonance, E1/E2, NMR Interpretation | 35 | |
| May 17 | 3 | Stereochemistry (R/S) [R2], Carbonyl Chemistry [R2] | 30 | Second pass — expect better recall |
| May 18 | 4 | Hybridization, SN1/SN2 | 30 | |
| May 19 | 5 | Resonance [R2], E1/E2 [R2] | 20 | Light day — buffer available |
| May 20 | 6 | NMR Interpretation [R2] | 15 | Light day — buffer available |
| May 21 | 7 | Stereochemistry (R/S) [R3], IR Spectroscopy [R1] | 30 | |
| May 22 | 8 | Carbonyl Chemistry [R3] | 15 | Light day |
| May 23 | 9 | Buffer / catch-up | — | Use if any topic was reset |
| May 24 | 10 | Hybridization [R2], SN1/SN2 [R2] | 30 | |
| May 25 | 11 | Resonance [R3], E1/E2 [R3] | 20 | |
| May 26 | 12 | NMR Interpretation [R3] | 15 | |
| May 27 | 13 | Buffer | — | |
| May 28 | 14 | Buffer | — | Use to re-drill any topics that failed |
| May 29 | 15 | Stereochemistry (R/S) [R4] | 15 | |
| May 30 | 16 | Carbonyl Chemistry [R4] | 15 | |
| May 31 | 17 | Hybridization [R3], SN1/SN2 [R3], Resonance [R4], E1/E2 [R4], NMR [R4], IR [R2] | 45 | Heavy day — all pending final reviews |
| Jun 1 | 18 | Light review only — no new material. Rest. | 15 | Exam tomorrow |
| Jun 2 | — | **EXAM DAY** | — | |

**Average daily load: ~26 minutes. Peak day: Day 17 (45 min). 11 buffer minutes/day on average.**

## Modification Rules

1. **Recalled easily and quickly** → Extend the next scheduled interval by 1.5× (round up to nearest day). Mark topic "Solid" or "Mastered."
2. **Recalled correctly but slowly or with effort** → Keep the scheduled interval as-is. No change.
3. **Partially recalled (got the idea, missed details)** → Shorten next interval by 1 day. Review the missed specifics immediately.
4. **Failed to recall / blank** → Reset this topic's interval to Day 1 and downgrade mastery one level. Re-enter it in the next available buffer day.

## Assumptions & Caveats

- This schedule assumes 45 min/day available every day and the mastery ratings you self-reported. If your ratings were optimistic, you will need more time — especially for New and Shaky items.
- "Review" means active retrieval (attempt to recall, then check) — not re-reading. Re-reading does not benefit from spacing in the same way.
- Day 17 is heavy (45 min). If that day becomes unavailable, split across Days 15 and 16 using the buffer.
- IR Spectroscopy is marked Mastered and reviewed only twice; if this confidence is wrong, promote it to Solid and re-run.
- The four buffer days (9, 13, 14, 18) are intentional — do not pre-fill them. Use them only for topics that missed their window or were reset after failure.

---

## False-Positive Prevention

**❌ DON'T** assign identical intervals to all topics regardless of mastery — this wastes review time on well-known material and under-reviews weak material.

**✅ DO** calibrate intervals to self-reported mastery, then adjust dynamically based on actual recall performance.

**❌ DON'T** schedule review sessions that exceed the learner's honest daily capacity — this causes schedule collapse and learned helplessness about the plan.

**✅ DO** ask for a realistic daily limit, flag overloaded days, and redistribute explicitly.

**❌ DON'T** treat re-reading or re-watching as a valid "review" — spacing only benefits active retrieval.

**✅ DO** explicitly state in the schedule that review means attempting to recall before checking.

**❌ DON'T** assume the learner's mastery self-ratings are accurate — they are starting points, not ground truth.

**✅ DO** include modification rules so the learner can correct the schedule when recall performance contradicts their initial rating.

**❌ DON'T** schedule the last review the night before the exam as a deep dive — fatigue undermines recall.

**✅ DO** make the final day a light pass with adequate rest recommended.

## Quality Criteria

- [ ] All required inputs collected before generating the schedule
- [ ] Mastery levels are used to differentiate starting intervals (not one-size-fits-all)
- [ ] All review dates fall before the exam date (or are flagged as conflicting)
- [ ] Daily load does not exceed stated capacity on any day without flagging
- [ ] Buffer days are included and labeled as contingency, not pre-filled
- [ ] Modification rules are explicit and operational (not vague)
- [ ] Assumptions and caveats are stated clearly

## Techniques Used

- **ST-01 (Clear Objective Statement):** Single-sentence objective anchors the scheduling purpose
- **ST-03 (Output Format Specification):** Dated table format makes the schedule immediately actionable
- **CM-01 (Explicit Context Framing):** All inputs (exam date, capacity, mastery) are collected upfront before any generation
- **ED-02 (Progressive Exercise Generation):** Intervals grow progressively as mastery is demonstrated
- **QA-04 (Uncertainty Acknowledgment):** Assumptions section explicitly states what could invalidate the schedule
