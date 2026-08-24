---
title: "Reading List Prioritizer"
category: productivity/school-student
description: "Triage an assigned reading list into must-read-carefully, skim, and skip tiers when there is more material than time."
techniques:
  - ST-01
  - ST-03
  - DS-02
  - CM-02
  - QA-01
  - RT-02
difficulty: intermediate
tags:
  - reading
  - triage
  - prioritization
  - studying
  - academic
updated: "2026-05-12"
related_prompts:
  - domain-productivity/deep-work/deepwork_decompose_complex_task.md
  - domain-productivity/deep-work/deepwork_focus_parameters_estimator.md
  - domain-productivity/bottlenecks/bottleneck_perfectionism_ship_threshold.md
  - domain-personal-development/prompts/agency/agency_next_action_spec.md
---

# Reading List Prioritizer

**Objective:** When a student has more assigned reading than they can realistically complete, triage the list into three tiers — read carefully, skim, and skip — based on exam likelihood, assignment relevance, and available time. State explicitly what is being traded off.

**When to use:** When the reading list for a course is longer than available time allows, or when an exam or assignment is approaching and not all reading is complete. Also useful at the start of a semester for ongoing triage decisions.

**Audience:** Undergraduate and graduate students in reading-heavy courses (humanities, social sciences, law, some sciences). Not intended to encourage skipping required work without awareness of the tradeoff — this is a time-triage tool, and the output says so plainly.

---

## Inputs Required

1. **The full reading list.** Titles, chapters, or descriptions with page counts or estimated length. Example: "Week 7 readings: Arendt, *Eichmann in Jerusalem* (Chapter 1–3, ~80 pages); course packet Article A (~25 pages); course packet Article B (~30 pages)."

2. **Upcoming exam or assignment topics.** What is the assessment testing? If an essay, what is the prompt or theme? If an exam, what topics has the professor emphasized? Be specific — "everything" is not workable.

3. **Professor emphasis signals (if any).** What has come up repeatedly in class? What appeared on past exams if available? What did the professor explicitly flag as important? Even weak signals (e.g., "she spent half of Tuesday on this") are useful.

4. **Available reading time.** Specific hours available between now and the deadline. Example: "I have about 6 hours across Sunday and Monday." Convert to approximate pages: the student's average reading pace helps (default: ~25 pages/hour for dense academic text; ~40 pages/hour for lighter material).

5. **Already-completed readings.** Mark any readings already done so they are excluded from triage.

---

## Instructions

### Step 1 — Calculate the reading gap

Total all unread pages. At the student's reading pace (or default estimate), calculate hours required to read everything carefully. Compare to available hours.

State the gap explicitly: "You have 6 hours and approximately 12 hours of reading. You must triage approximately 50% of the material."

If available time is sufficient to read everything, say so and end the output with a reading order recommendation. Do not fabricate triage when none is needed.

### Step 2 — Triage into three tiers

Assign each unread item to one of three tiers:

**Tier 1 — Read carefully**
- Directly tested on the upcoming exam or required for the assignment
- Frequently referenced or discussed in class (professor emphasis signal)
- Foundational to understanding other readings (conceptual prerequisite)
- Shorter items that punch above their page count in importance

**Tier 2 — Skim**
- Useful context but not directly testable
- Covers a topic only tangentially related to the exam/assignment
- Similar in content to a Tier 1 reading (provides redundant coverage)
- Longer items where only the introduction, conclusion, and section headers are needed

**Tier 3 — Skip (given current time constraints)**
- Lowest signal-to-time ratio given exam/assignment focus
- No class discussion, no emphasis signals, not on past exams
- Background reading with no direct link to upcoming assessment

For each Tier 3 item, name the tradeoff: what coverage is lost by skipping it.

### Step 3 — Estimate time per tier

Sum estimated reading time for Tier 1 and Tier 2 items. Confirm this fits within available time. If Tier 1 alone exceeds available time, flag that Tier 1 must also be compressed — recommend which Tier 1 items to prioritize most.

### Step 4 — Recommend a reading order for Tier 1

Sequence Tier 1 readings in the order the student should approach them:
- Start with any reading that is prerequisite to understanding others
- Then proceed by exam/assignment relevance (highest first)
- Include a time estimate for each

### Step 5 — Produce the triage output

Use the format below. Include the tradeoff acknowledgment.

---

## Constraints

### Must
- State the reading gap (total pages vs. available time) before the triage
- Assign every unread item to a specific tier — no items left unclassified
- For every Tier 3 item, name the specific coverage tradeoff being accepted
- Confirm that Tier 1 time fits within available hours; flag if it does not
- Include a reading order for Tier 1 items

### Must Not
- Triage when the student has enough time to read everything — recommend a reading order instead
- Classify items as Tier 1 solely because they are long or difficult — length is not importance
- Skip the tradeoff acknowledgment — this is a triage tool, not a permission slip to not learn
- Default every uncertain item to Tier 2 ("skim everything") as a risk-averse hedge
- Recommend skipping items without a stated rationale for each

---

## False-Positive Prevention

1. **Length bias:** Long readings are not automatically important. A 10-page article that the professor discussed for 30 minutes outweighs a 60-page textbook chapter she mentioned once. Use emphasis signals and exam relevance, not page count, to determine tier.

2. **Skim inflation:** Classifying most readings as Tier 2 is not triage — it is avoidance. Tier 2 should be genuinely skimmable (introduction + conclusion + headers). If a reading requires active comprehension to be useful, it belongs in Tier 1 or Tier 3, not Tier 2.

3. **Tradeoff omission:** Saying "skip Article B" without stating what coverage is lost gives the student no basis to second-guess the call. Always name what is being traded off.

4. **False sufficiency:** If Tier 1 alone takes 8 hours and the student has 6 hours, the plan is still impossible. Flag this and recommend which Tier 1 items to prioritize if time runs short.

5. **Ignoring completed readings:** Re-triaging already-read material wastes the student's time. Confirm which readings are done and exclude them from all calculations.

---

## Output Format

```
READING LIST TRIAGE — [Course] — Assessment: [Exam/Assignment name and date]

READING GAP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total unread pages:        [X pages]
Estimated time to read all: [Y hours at ~Z pages/hr]
Available time:            [A hours]
Gap:                       [Must triage approximately B hours / C% of material]

Already completed (excluded): [List]

TRIAGE RESULTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TIER 1 — READ CAREFULLY (~[X hours total])
[Item name] — [Pages] — [Est. time] — [Reason: exam-tested | professor emphasis | conceptual prerequisite]
[Item name] — [Pages] — [Est. time] — [Reason]
...

TIER 2 — SKIM (~[X hours total])
[Item name] — [Pages] — [Est. skim time] — [What to skim: intro + conclusion + section headers]
[Item name] — [Pages] — [Est. skim time]
...

TIER 3 — SKIP (given time constraints)
[Item name] — [Pages] — Tradeoff: [Specific coverage lost by skipping this]
[Item name] — [Pages] — Tradeoff: [...]
...

CAPACITY CHECK (Tier 1 + Tier 2)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tier 1 time: [X hrs]  Tier 2 time: [Y hrs]  Total: [Z hrs]
Available: [A hrs]
Status: [FITS | TIGHT — drop lowest-priority Tier 1 item if needed | OVERBUDGET — see note]

[If overbudget]: Protect these Tier 1 items above all others if time runs short:
  1. [Item] — [Reason]
  2. [Item] — [Reason]

TIER 1 READING ORDER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. [Item] — [Est. time] — [Start here because: prerequisite | highest exam relevance]
2. [Item] — [Est. time]
3. ...

TRADEOFF ACKNOWLEDGMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
By following this triage, you are choosing not to engage with:
  - [Tier 3 item]: [What coverage or perspective is missed]
  - [Tier 3 item]: [...]
This is a time-constrained decision, not a judgment that this material is unimportant.
```

---

## Verification

- [ ] Reading gap (total pages vs. available time) is stated at the top
- [ ] Every unread item is assigned to exactly one tier
- [ ] Every Tier 3 item has a named tradeoff (specific coverage lost)
- [ ] Tier 1 time is confirmed to fit within available hours
- [ ] If Tier 1 time exceeds available hours, a fallback priority order within Tier 1 is provided
- [ ] A reading order for Tier 1 is included
- [ ] The tradeoff acknowledgment section is present
- [ ] Completed readings are excluded from all calculations
