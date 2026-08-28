---
title: "Study Next Advisor"
category: education-teaching/learner/exam-prep
description: "Answers 'what should I study next?' by integrating exam date, current mastery estimates, topic dependencies, and available time to output a prioritized session agenda."
techniques:
  - ST-01
  - ST-03
  - CM-01
  - QA-04
  - ED-02
difficulty: beginner
tags:
  - study-planning
  - prioritization
  - adaptive-learning
  - exam-prep
  - session-design
updated: "2026-05-15"
related_prompts:
  - domain-education-teaching/learner/exam-prep/learn_weak_area_diagnosis.md
  - domain-education-teaching/learner/memory-and-recall/learn_spaced_review_scheduler.md
  - domain-education-teaching/learner/exam-prep/learn_exam_review_planner.md
---

## Objective

Answer "what should I study right now?" with a prioritized, time-boxed session plan — integrating mastery levels, topic dependencies, exam proximity, and the learner's available time into a concrete agenda.

## When to Use

- At the start of a study session when the learner is unsure where to begin
- When managing multiple subjects or courses simultaneously
- After completing a scheduled review session and planning what comes next
- When feeling overwhelmed by the volume of material and needing a clear starting point

**Do not use** as a long-term study schedule (use `learnstudy_spaced_review_scheduler.md` for that). This prompt answers "what next?" for one session or one day — not one month.

## Instructions

1. **Collect inputs.**
   - Ask: "What topics do you need to cover, and how confident are you in each? (list each topic + Low / Medium / High confidence)"
   - Ask: "When is your next exam or deadline?"
   - Ask: "How much time do you have for this study session?"
   - Ask: "Are any topics prerequisites for others? (e.g., you must understand A before B makes sense)"
   - Ask: "Have you already studied anything today, or is this your first session?"
   - Optional: "Is there anything you've been avoiding that you know you should address?"

2. **Build a topic priority matrix.**
   For each topic, score on two axes:
   - **Urgency score** (1–5): based on exam proximity + how much time is left
   - **Value score** (1–5): based on mastery gap × exam weight

   Priority = Urgency × Value (scale 1–25)

   Apply dependency rule: if topic B requires topic A as a prerequisite, and A is not yet solid, A must precede B regardless of priority score.

3. **Apply session design rules.**
   - Start with the highest-priority topic that the learner can engage with immediately (no unsatisfied prerequisites)
   - If the learner reports fatigue or this is the third+ session today: start with a medium-priority topic to warm up, then tackle the hardest one
   - Do not put more than 2 heavy cognitive-load topics in a single session
   - Reserve 10% of session time for review of a previously studied topic (spaced reinforcement)
   - End with a topic the learner finds more engaging (momentum for next session)

4. **Output a time-boxed agenda.**
   Divide the session into 25–50 minute blocks (Pomodoro-compatible) with:
   - Topic for each block
   - Activity type (initial study, retrieval drill, practice problems, concept map, etc.)
   - Expected output or checkpoint (what does "done" look like for this block?)

5. **Explain the prioritization logic.**
   In 2–3 sentences, state why this order was chosen. Make the reasoning transparent so the learner can override it if they have information you don't.

6. **Include one open question for the learner.**
   After presenting the agenda: "Is there anything on this list you're avoiding, or any topic that's causing anxiety that we should address differently?"

## Output Format

```
# Study Session Plan
Today: [date] | Time available: [N minutes] | Exam: [date or days]

## Topic Priority Matrix
| Topic | Confidence | Urgency | Value | Priority |
|---|---|---|---|---|
| ... | Low | 5 | 4 | 20 |

## Session Agenda

**Block 1 — [Start time or "First 30 min"]**
Topic: [Topic name]
Activity: [Initial study / Retrieval drill / Practice problems / etc.]
Checkpoint: [What does finishing this block look like?]

**Block 2 — [Next 25 min]**
...

**Closing Block — [Last 10 min]**
Topic: [Review of earlier session material]
Activity: [Quick recall check]

## Why This Order
[2–3 sentences]

## One Question For You
[Open question about avoidance or anxiety]
```

## Example Output

---

**Input:**
- Topics: Thermodynamics (Low), Kinetics (Medium), Equilibrium (Low), Acids & Bases (High), Electrochemistry (never studied — New)
- Exam: 5 days from now (high urgency)
- Time available: 2.5 hours (150 min)
- Dependencies: Thermodynamics partially overlaps with Electrochemistry (ΔG°/E°cell relationship); rest are independent
- First session today

---

# Study Session Plan
Today: 2026-05-15 | Time available: 150 min | Exam: 2026-05-20 (5 days)

## Topic Priority Matrix

| Topic | Confidence | Urgency | Value | Priority | Notes |
|---|---|---|---|---|---|
| Electrochemistry | New (0%) | 5 | 5 | 25 | **Top priority — never studied, high exam weight** |
| Thermodynamics | Low | 5 | 4 | 20 | Prerequisite for Electrochemistry (ΔG°/E°cell) |
| Equilibrium | Low | 5 | 4 | 20 | High gap, high urgency |
| Kinetics | Medium | 5 | 2 | 10 | Partial knowledge — needs reinforcement |
| Acids & Bases | High | 5 | 1 | 5 | Strong — maintenance only today |

---

## Session Agenda

**Block 1 — First 40 min**
Topic: **Thermodynamics** (ΔG, ΔH, ΔS — focus on ΔG calculation and spontaneity rules)
Activity: Initial concept study → draw a decision tree for predicting spontaneity from ΔH and ΔS signs
Checkpoint: Complete the decision tree from memory and solve 3 ΔG calculation problems correctly

*Why first:* Thermodynamics is a prerequisite for Electrochemistry. You cannot meaningfully study the ΔG°/E°cell relationship (Block 2) until you're solid on ΔG itself. Don't skip this even though Electrochemistry has a higher priority score.

---

**Block 2 — Next 50 min**
Topic: **Electrochemistry** (galvanic cells, standard reduction potentials, E°cell calculation, ΔG°/E°cell link)
Activity: Study from notes or textbook → build a cell diagram by hand → solve standard cell potential calculations
Checkpoint: Draw a complete galvanic cell from scratch (anode/cathode labels, ion flow, electron flow) and calculate E°cell for 2 unfamiliar half-reaction pairs

*Why second:* This is your biggest gap (never studied) and your highest-priority topic. By placing Thermodynamics first, you now have the ΔG foundation needed to understand the thermodynamic interpretation of E°cell.

---

**5-min Break**

---

**Block 3 — Next 35 min**
Topic: **Equilibrium** (Kc, Kp, Q vs. K, Le Chatelier's principle)
Activity: Retrieval drill — attempt to write the Kc expression for 3 reactions from memory, then apply Le Chatelier to 4 perturbation scenarios without notes
Checkpoint: Correctly predict the direction of shift for all 4 Le Chatelier problems

*Why third:* Equilibrium is your second-largest gap. After two cognitively heavy blocks, this is still important but shorter — 35 minutes of focused retrieval practice is more valuable than another long study block while mental energy is declining.

---

**Closing Block — Last 10 min**
Topic: **Kinetics** (review only — you're at Medium confidence here)
Activity: Self-quiz: "What is the rate law for a reaction? How do you determine reaction order from experimental data?" Attempt from memory, then check notes.
Checkpoint: Correctly state rate law form and explain zero/first/second order characteristics

*Why last:* You're already partially solid here. A quick retrieval pass reinforces what you know and catches any gaps without requiring a fresh cognitive investment.

**Acids & Bases:** Skip today — you're at High confidence and the exam is 5 days out. Schedule a maintenance review in 3 days.

---

## Why This Order

The order follows one rule: unblock dependencies before tackling dependents. Thermodynamics first because Electrochemistry literally requires it. Electrochemistry second because it's your biggest gap and highest exam risk. Equilibrium third to use the remaining fresh-brain window productively. Kinetics at the end as a light reinforcement pass, not a learning session.

---

## One Question For You

You listed Equilibrium as Low confidence — but I notice you didn't mention any issues with it. Is Equilibrium something you're actively avoiding, or just something you haven't gotten to yet? If it's avoidance (feels confusing or frustrating), we should address that differently than if it's simply next in the queue.

---

## False-Positive Prevention

**❌ DON'T** prioritize only the topics the learner finds interesting or comfortable — the highest-priority topic is usually the one being avoided.

**✅ DO** ask explicitly about avoidance and factor it into the agenda.

**❌ DON'T** pack every topic into one session — a focused 2-topic session produces better encoding than a scattered 6-topic session.

**✅ DO** limit new heavy-content blocks to 2 per session and use the remaining time for retrieval or reinforcement.

**❌ DON'T** ignore topic dependencies — studying topic B before topic A (when B requires A) wastes time.

**✅ DO** always ask about dependencies and enforce prerequisite ordering even if it changes the priority ranking.

**❌ DON'T** assume the learner's confidence ratings are accurate — overconfidence is common, especially for recently reviewed material.

**✅ DO** treat confidence ratings as a starting point, not ground truth, and note this explicitly if the session reveals discrepancies.

## Quality Criteria

- [ ] All provided topics are ranked in the priority matrix
- [ ] Dependencies are respected in the session order (prerequisite topics come first)
- [ ] Session agenda is time-boxed with specific activities and checkpoints per block
- [ ] Total agenda time does not exceed the learner's stated available time
- [ ] Prioritization logic is explained in 2–3 transparent sentences
- [ ] One open question about avoidance or anxiety is included
- [ ] Skipped topics include a reason and a recommended rescheduling timeframe

## Techniques Used

- **ST-01 (Clear Objective Statement):** Objective specifies one-session scope and distinguishes from long-term scheduling
- **ST-03 (Output Format Specification):** Priority matrix + time-boxed agenda format makes the plan immediately executable
- **CM-01 (Explicit Context Framing):** All inputs (topics, confidence, exam date, time, dependencies) collected before any output
- **QA-04 (Uncertainty Acknowledgment):** Transparency section explains why this order was chosen and invites learner override
- **ED-02 (Progressive Exercise Generation):** Blocks are designed to build on each other (prerequisite first, dependent second)
