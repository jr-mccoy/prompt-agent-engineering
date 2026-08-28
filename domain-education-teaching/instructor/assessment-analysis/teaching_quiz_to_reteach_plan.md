---
title: "Quiz-to-Reteach Plan"
category: education-teaching/instructor/assessment-analysis
description: "Convert quiz results directly into a differentiated reteach lesson — grouping students by error pattern (not score), assigning each group a targeted intervention, and producing a 20-minute differentiated sequence."
techniques:
  - ST-01
  - ST-02
  - DS-01
  - QA-04
  - RT-02
difficulty: intermediate
tags:
  - assessment
  - reteach
  - differentiation
  - formative-assessment
  - data-driven
  - instructional-response
  - intervention
updated: "2026-05-15"
related_prompts:
  - domain-education-teaching/instructor/assessment-analysis/teaching_item_analysis_report.md
  - domain-education-teaching/instructor/assessment-design/teaching_mastery_check_designer.md
  - domain-education-teaching/instructor/assessment-design/teaching_diagnostic_quiz_knowledge_map.md
  - domain-education-teaching/instructor/response-cycle/teaching_misconception_diagnoser.md
---

# Quiz-to-Reteach Plan

## Objective

Take assessment results and produce a ready-to-run differentiated reteach session — grouping students by misconception pattern, not overall score, and giving each group a targeted 20-minute instructional intervention.

## When to Use

- The day after returning a quiz or formative assessment
- When more than 30% of students missed the same item or pattern of items
- When you want to use data to differentiate instead of reteaching the same thing to everyone
- When students who passed need something productive to do while others reteach
- For PLC "learn-and-do" sessions: analyze data together, build the reteach together

## When NOT to Use

- For detailed psychometric item analysis — use `assessment_item_analysis_report.md` first
- When you haven't scored the assessment yet
- When gaps are all individual (no patterns) — this prompt works when groups exist

---

## Inputs Needed

- **Quiz items and topics:** [Paste items or describe as "Q1=fractions, Q2=decimals…"]
- **Learning objectives assessed:** [What the quiz was designed to measure]
- **Results data:** [Choose one:]
  - Score table (Student | Q1 | Q2 | Q3 | Total)
  - Summary (Q1: 16/24 correct, common wrong answer: B; Q2: 9/24 correct…)
  - Cluster description ("About 8 kids missed Q3 and Q5, which are both about X")
- **Number of students:** [N]
- **Reteach time available:** [e.g., 20 minutes, 30 minutes]
- **Class setup:** [What physical grouping is possible — rows, pods, stations?]

---

## Instructions

### Step 1: Error Pattern Grouping

Don't group by score. Group by misconception pattern — which items they missed, not how many.

```
STUDENT GROUPING BY ERROR PATTERN
─────────────────────────────────────────────

GROUP A — MASTERY: [N students]
Profile: Passed all or all-but-one item
Gap: None or minor
Plan: Extension or peer tutor role (see Step 5)

GROUP B — [Name the misconception, e.g., "Reversed the rule / concept X confusion"]: [N students]
Profile: Missed items [N, N] — both related to [specific concept]
Core gap: [1-sentence description of the conceptual error]
Error evidence: [What their wrong answers specifically showed]

GROUP C — [Name, e.g., "Procedural breakdown on multi-step problems"]: [N students]
Profile: Missed items [N, N, N] — related to [procedure or process]
Core gap: [...]
Error evidence: [...]

GROUP D — [Name, e.g., "Foundation gap — prerequisite missing"]: [N students]
Profile: Missed most items including the easiest; errors span multiple topics
Core gap: [Missing prerequisite, not just a misconception in the unit]
Note: This group may need more than 20 minutes — flag for follow-up

─────────────────────────────────────────────
NOTE: Groups should reflect misconception patterns, not a ranked list.
A student may belong to two groups if they have two distinct gaps.
```

### Step 2: Define Each Group's Reteach Objective

For each non-mastery group:

```
GROUP [B/C/D] — RETEACH OBJECTIVE
─────────────────────────────────────────────
By the end of the 20-minute session, this student will be able to:
[SWBAT statement — specific to this group's gap, not the original unit objective]

Evidence of success: [What the teacher will see or hear if the reteach worked]
Quick check question: "[1 question to pose at the end to verify the gap closed]"
```

### Step 3: Build the 20-Minute Differentiated Sequence

Design simultaneous activities — not serial whole-class instruction. Each group needs a task.

```
20-MINUTE RETEACH SEQUENCE
─────────────────────────────────────────────

MINUTES 0–2: SETUP
All students: [Transition instruction — how to move to groups / what materials to get]
Teacher: [Where to start — which group needs direct instruction first?]

─────────────────────────────────────────────

GROUP A — MASTERY: Extension Task (independent)
Activity: [Specific extension activity — a challenge problem, an application, a creation task, or peer tutoring role]
Materials: [What they need]
Outcome: [What they produce or do]
Teacher check-in: [At minute 15 — what to ask or collect]

─────────────────────────────────────────────

GROUP B — [Misconception name]: Direct instruction (teacher-led, ~8 min)
Reteach approach: [A DIFFERENT approach from the original instruction — new angle, new example, new modality]
Opening move: "[What the teacher says to frame the reteach — connects to their specific error]"
Core explanation: [2–3 sentences describing the instructional approach — analogy, visual, counter-example, worked example with think-aloud]
Student practice: [1–2 problems they try while teacher watches — immediate feedback loop]
Exit check: "[The quick check question from Step 2]"

─────────────────────────────────────────────

GROUP C — [Misconception name]: Structured partner work (while teacher is with Group B)
Activity: [Partner task designed to surface and fix the specific error pattern]
Protocol: [How they work together — e.g., "Take turns explaining your reasoning for each step"]
Materials: [Cards, graphic organizer, specific problems]
Teacher joins at: [Minute 8 — what to do when you arrive]

─────────────────────────────────────────────

GROUP D — Foundation gap: Independent prerequisite practice (with support structure)
Activity: [Prerequisite concept activity — goes back before the unit started]
Support: [Worked example card, sentence frames, visual anchor — something that scaffolds without the teacher]
Note: This group needs a follow-up plan beyond today's 20 minutes

─────────────────────────────────────────────

MINUTES 18–20: CLOSE
All students: [1-sentence share-out OR individual exit check OR note/notebook entry]
Teacher: [What to collect or observe to verify reteach worked]
```

### Step 4: Post-Reteach Verification

```
VERIFICATION PLAN
─────────────────────────────────────────────
Immediate: [Exit check question — 1 question per group, specific to their gap]
Within 2 days: [Mastery check or embedded item in next class — use `assessment_mastery_check_designer.md`]
If gaps persist: [Escalation — small group pull, parent contact, additional diagnostic]
```

---

## Output Format

1. Student grouping by error pattern (A: Mastery, B/C/D: Gap groups)
2. Per-group reteach objective with success evidence
3. 20-minute differentiated sequence (all groups simultaneously)
4. Verification plan

---

## False-Positive Prevention

❌ **DON'T:**
- Reteach the whole class together when gaps are differentiated — one-size-fits-all reteach only re-exposes students who already understand
- Group by score (top/middle/bottom) rather than misconception type
- Reteach Groups B and C using the same explanation that didn't work the first time
- Design an extension that is just "more of the same" — mastery students need depth, not repetition
- Skip verification — reteach without a check is hopeful, not instructional

✅ **DO:**
- Name each group by their specific misconception, not by their score
- Use a different approach for the reteach (different modality, different example, different analogy)
- Give the mastery group something genuinely interesting to do while others reteach
- Build the verification into the sequence (end-of-session check), don't leave it for "later"
- Flag Group D for follow-up — a 20-minute reteach won't fix a prerequisite gap

---

## Quality Indicators

- [ ] Students grouped by error pattern (misconception), not score
- [ ] Each group has a specific SWBAT reteach objective
- [ ] Reteach approach is different from original instruction
- [ ] Mastery group has a meaningful extension, not a waiting activity
- [ ] Full 20-minute sequence fits the stated time window
- [ ] Verification plan includes specific check questions

---

## Techniques Used

| Technique | How It's Applied |
|-----------|-----------------|
| **ST-01** | Grouping → objectives → sequence → verification as a clear pipeline. |
| **ST-02** | Differentiated 20-minute sequence with timed phases for each group. |
| **DS-01** | Misconception taxonomy used to name and frame each group's gap. |
| **QA-04** | Verification plan defined upfront — success criteria for each group's reteach. |
| **RT-02** | Multi-group analysis: each cluster has its own gap profile and instructional response. |
