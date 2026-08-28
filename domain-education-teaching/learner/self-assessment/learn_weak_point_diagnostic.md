---
title: "Diagnose My Weak Points"
category: education-teaching/learner/self-assessment
description: "A diagnostic conversation that probes beneath surface knowledge to find where understanding actually breaks down — producing a prioritized gap map with study recommendations ranked by impact on the learner's upcoming goal."
techniques:
  - RT-02
  - DS-01
  - ST-01
  - QA-05
  - RT-05
difficulty: beginner
tags:
  - learner-facing
  - self-study
  - diagnostic
  - metacognition
  - gap-analysis
  - study-skills
  - exam-prep
updated: "2026-05-15"
related_prompts:
  - domain-education-teaching/learner/self-assessment/learn_quiz_to_mastery.md
  - domain-education-teaching/learner/self-assessment/learn_wrong_answers_study_plan.md
  - domain-education-teaching/instructor/assessment-design/teaching_diagnostic_quiz_knowledge_map.md
audience: learner
---

# Diagnose My Weak Points

## Objective

Probe your stated knowledge of a topic to find where understanding is genuinely solid, where it's shallow or brittle, and where it has gaps — then produce a prioritized gap map with specific study actions ranked by impact on your upcoming goal.

## Who This Is For

Learners who:
- Feel "mostly ready" for a test or exam but suspect there are holes they can't see
- Have reviewed material but aren't sure if they really understand it or just recognize it
- Want to use study time efficiently — targeting real gaps, not re-reading familiar content
- Have tried practice problems and got some wrong but aren't sure what the pattern means

## How to Use This Prompt

**Paste this prompt into a conversation with an AI model.** The model will ask you a short series of probing questions — not to quiz you, but to test the depth of your understanding. Answer honestly and explain your reasoning when asked. The diagnostic is only useful if you don't fake it.

This is a conversation, not a test. There are no grades.

---

## Your Inputs

Provide these at the start:

- **Subject / topic:** [What you want diagnosed — be specific: "oxidation-reduction reactions in organic chemistry" not just "chemistry"]
- **What you believe you understand:** [Describe in 2–4 sentences what you think you know about this topic]
- **Your upcoming goal:** [e.g., "AP exam in 2 weeks" / "midterm Friday" / "I want to understand this well enough to teach it"]
- **How you've been studying:** [e.g., read the textbook / watched videos / did problem sets / attended class]

---

## Instructions for the Model

### Phase 1: Map the Conceptual Terrain (Don't ask yet)

Before asking any questions, internally identify:
- The 5–8 key concepts or skills within this topic
- The prerequisite knowledge required
- The 3 most common places where understanding goes shallow or breaks down
- The difference between "I've seen this before" (recognition) and "I understand this" (explanation and application)

Do not share this map with the learner until the end. Use it to guide your probing questions.

### Phase 2: Surface-Level Check (1–2 questions)

Start with a question that a student who has skimmed the material could answer:
- "In your own words, what does [core concept] mean?"
- "Give me one example of [concept] in action."

**Purpose:** Distinguish between recognition and understanding. Many learners can answer these correctly but fail on Phase 3.

After response:
- Note what was clear, what was vague, and what vocabulary was used
- Do NOT reveal your assessment yet — proceed to Phase 3

### Phase 3: Depth Probes (2–4 questions, escalating)

Choose probes that go progressively deeper:

**Explanation probe (Level 1 depth):**
"You said [their answer]. Now explain *why* that's the case."

**Application probe (Level 2 depth):**
"Given [slightly novel scenario], what would happen to [concept]?"

**Edge case probe (Level 3 depth):**
"What would change if [one assumption in their answer were different]?"

**Prerequisite probe (Level 4 depth — use if surface answers were weak):**
"Before we go further — when you think about [prerequisite concept], what does that mean to you?"

After each response, evaluate:
- **Solid:** Clear, correct explanation, handles novel case — note as strong
- **Shallow:** Correct terms but can't explain mechanism — note as brittle
- **Broken:** Wrong understanding that appears confident — note as gap + misconception
- **Absent:** Doesn't know, skips, or says "I'll look that up" — note as gap

**Proceed with the minimum number of probes needed.** Don't ask more questions than necessary to classify each concept as solid/shallow/broken/absent.

### Phase 4: Gap Confirmation

For each shallow or broken concept, ask one targeted follow-up to confirm the gap:
"Let me ask this a different way: [reframe the concept]. What's your thinking?"

This distinguishes between "I explained it badly" and "I actually don't have this."

### Phase 5: Diagnostic Report

Produce the gap map:

```
DIAGNOSTIC REPORT
─────────────────────────────────────────────

TOPIC: [Subject + topic]
GOAL: [Upcoming exam / purpose]
QUESTIONS ASKED: [N]

─────────────────────────────────────────────
CONCEPT MAP — WHAT WE FOUND:

SOLID (no study needed before [goal]):
• [Concept] — evidence: [What the learner said that showed genuine understanding]
• [Concept] — [evidence]

SHALLOW (know the words, not the mechanism):
• [Concept] — what you can do: [what was right]; what's missing: [what's hollow]
• [Concept] — [same structure]

GAP (missing or wrong understanding):
• [Concept] — what you currently believe: [description of the misconception or gap]
  What's actually true: [1–2 sentence correction or reframe]
• [Concept] — [same structure]

─────────────────────────────────────────────
PRIORITIZED STUDY PLAN:

#1 (Highest impact on [goal]): [Concept name]
Why it matters: [How this gap affects the exam or goal]
Study move: [Specific — not "review notes" but "work 3 problems where X happens, then explain in writing why the answer changes when Y"]
Time estimate: [N minutes / N hours]

#2: [Concept]
Why it matters: [...]
Study move: [Specific]
Time estimate: [...]

#3 (if applicable): [Concept]
...

SOLID CONCEPTS: Don't re-study these — use that time on the gaps above.

─────────────────────────────────────────────
HONEST READINESS ESTIMATE:
[Not ready / Getting there / Close / Ready]
Reasoning: [2 sentences]
```

---

## What the Model Must NOT Do

- Ask more questions than necessary to classify a concept
- Reveal the diagnosis early (before Phase 5) — mid-session judgments distort answers
- Write vague study recommendations ("review this topic") — every recommendation must be specific
- Produce a gap map without an explanation of why each gap matters for the stated goal
- Over-diagnose — if a concept is solid, say so and don't probe it further

---

## Quality Indicators (Learner Self-Check)

After the session:
- [ ] I was pushed to explain my reasoning, not just give definitions
- [ ] The gap map feels accurate — it found things I recognized as holes
- [ ] The study plan tells me what specifically to do, not just what to re-read
- [ ] I know which concepts I can skip and which need attention

---

## Techniques Used

| Technique | How It's Applied |
|-----------|-----------------|
| **RT-02** | Multi-dimensional analysis: surface, depth, application, and prerequisite levels probed. |
| **DS-01** | Conceptual terrain mapped before probing — questions are purposeful, not random. |
| **ST-01** | Structured pipeline: surface check → depth probes → gap confirmation → report. |
| **QA-05** | Comparative analysis: solid vs. shallow vs. broken classification for each concept. |
| **RT-05** | Gap map and study plan build learner metacognition — knowing what you know. |
