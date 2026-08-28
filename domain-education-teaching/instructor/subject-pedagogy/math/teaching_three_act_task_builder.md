---
title: "3-Act Math Task Builder"
category: education-teaching/instructor/subject-pedagogy/math
description: "Design a complete 3-act math task — Act 1 (hook + question), Act 2 (information release), Act 3 (reveal + sequel) — anchored to a specific standard, with anticipated student approaches."
techniques:
  - CM-01  # Context Framing
  - ST-02  # Sequential Steps
  - DS-01  # Framework Application
  - RT-04  # Emotional Intelligence
  - QA-02  # Adversarial Verification
difficulty: intermediate
tags:
  - math
  - problem-solving
  - inquiry
  - 3-act
  - middle-school
  - high-school
  - elementary
updated: "2026-05-09"
related_prompts:
  - domain-education-teaching/instructor/subject-pedagogy/math/teaching_number_talks_designer.md
  - domain-education-teaching/instructor/lesson-planning/teaching_lesson_plan_generator.md
  - domain-education-teaching/instructor/response-cycle/teaching_misconception_diagnoser.md
---

# 3-Act Math Task Builder

## Objective

Build a complete 3-act task for a specific grade and standard. Output includes the hook artifact (described, not generated), the focus question that emerges from students, the information menu released in Act 2, the reveal in Act 3, an anticipated solution path table, and at least one sequel question.

## When to Use

- Launching a unit with a low-floor / high-ceiling problem
- Concept-attainment lessons where students need to feel a need for the math
- Modeling lessons (Standards for Mathematical Practice 4)
- When you want students to formulate the question, not just answer one

## When NOT to Use

- You need a quick warm-up — use `teachsubj_math_number_talks_designer.md`
- You need a procedural practice set — use `teaching_study_practice_problems.md`
- The math is purely procedural with no real-world referent

---

## Inputs Needed

- **Grade:** [3–12]
- **Standard / target skill:** [e.g., 6.RP.A.3 ratio reasoning; A.CED.A.2 linear modeling]
- **Time available:** [Single class / two-day]
- **Real-world context preference (optional):** [Sports / food / construction / video games / civic / other]
- **Tech available:** [Projector only / 1:1 devices / desmos / video playback]

---

## Instructions

### Step 1: Hook Selection (Act 1)

Describe a 30–60 second hook artifact (video, image, or live demonstration). Specify:
- What students see/hear
- What is *intentionally* withheld so students must ask
- The "huh — I wonder…" moment

Do not invent media that doesn't exist. Describe the hook in enough detail that a teacher could film/photograph/stage it themselves, OR reference well-known publicly available types ("a video of a person filling a giant water tank — like the kind on Dan Meyer's 3-Act library").

### Step 2: Question Elicitation

List 3–5 questions students are likely to ask after Act 1, in order of likelihood. Star (★) the question that maps to the target standard. Provide a teacher move for redirecting if no student asks the starred question.

### Step 3: Estimation Round

Provide the exact teacher prompts:
- "Give me an estimate that's too low."
- "Give me an estimate that's too high."
- "Give me your best guess."
Note where to record these (number line on board / shared doc / sticky notes).

### Step 4: Information Release (Act 2)

List the pieces of information students need to solve the problem. For each:

| Info | What it is | When to release | How students access it |
|------|-----------|-----------------|------------------------|
| [Name] | [e.g., tank dimensions] | On request after solo think | Handout / projected / measured live |

Sequence the release so students must ask for what they need. Provide the teacher response if students ask for irrelevant information ("That's interesting — would it change your answer?").

### Step 5: Anticipated Solution Paths

Table of 3–5 approaches a student might take, ordered from concrete to abstract:

| # | Approach | Tools used | Likely outcome | Teacher move |
|---|----------|-----------|---------------|--------------|
| 1 | [Guess and check / scale model] | [Paper, calculator] | [Approximate] | [Question that nudges toward more efficient method] |

Include at least one **partial-credit / common-error** path with the misconception named.

### Step 6: Reveal (Act 3)

Describe the artifact that reveals the answer (e.g., "video continues until the tank overflows at 3:42 — students compare to their predictions").

Provide the discussion script:
- "Whose estimate was closest?"
- "Whose method got closest to the real answer? Why?"
- "What was different about the real situation than our model?"

### Step 7: Sequel Questions

Provide 2–3 sequel questions that extend the task:
- One that **scales** the original (bigger/smaller/faster)
- One that **reverses** the original (given the answer, find an input)
- One that **generalizes** (find a rule or formula)

### Step 8: Standards & Practices Mapping

| Standard / Practice | Where it shows up in the task |
|---------------------|-------------------------------|
| [Content standard] | [Specific moment] |
| SMP-1 Make sense of problems | [Act 1 question elicitation] |
| SMP-4 Model with mathematics | [Act 2 method choice] |

### Step 9: Differentiation

- **Entry support:** Partner work, pre-released info card for students who need it, sentence frames for estimation
- **Stretch:** Sequel questions provided early; ask "what would have to change to make the answer exactly half?"
- **ELL:** Visual hook reduces language load; provide vocabulary preview only for technical terms (volume, rate, etc.)

---

## Output Format

1. Task title and standard
2. Act 1 hook description + question elicitation script
3. Estimation round
4. Act 2 information menu (table)
5. Anticipated solution paths (table)
6. Act 3 reveal + discussion script
7. Sequel questions
8. Standards/practices map
9. Differentiation notes
10. Materials and timing summary

---

## False-Positive Prevention

❌ **DON'T:**
- Invent a YouTube link, video URL, or specific video that may not exist
- Release all the information up front — kills the inquiry
- Skip the estimation round — it builds buy-in and reveals number sense
- Force students to ask the "right" question — redirect, don't override
- Make the reveal a number on a slide — use a real artifact when possible

✅ **DO:**
- Describe hook artifacts a teacher can produce themselves
- Sequence information so students must ask
- Anticipate at least one wrong-but-reasonable solution path
- Connect the sequel to the same standard for transfer
- Time the whole task realistically, including transitions

---

## Quality Indicators

- [ ] Act 1 hook can be staged with stated tech
- [ ] At least 3 student questions anticipated; the starred one maps to the standard
- [ ] Information menu requires students to ask
- [ ] At least one anticipated approach is partial/incorrect with misconception named
- [ ] Sequel questions deepen the same standard, not change topics
- [ ] Total time fits the available window

---

## Techniques Used

| Technique | How It's Applied |
|-----------|-----------------|
| **CM-01** | Standard, grade, time, and tech context anchor design choices. |
| **ST-02** | Three-act structure plus internal phases enforce a known pedagogical sequence. |
| **DS-01** | Standards for Mathematical Practice are explicitly mapped, not assumed. |
| **RT-04** | Hook design centers curiosity and the "huh" moment that drives engagement. |
| **QA-02** | Anticipated wrong paths and misconceptions stress-test the task in advance. |
