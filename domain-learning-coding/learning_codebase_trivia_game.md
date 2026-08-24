---
title: "Codebase Trivia Game Generator — Gamify Learning with Verifiable Questions"
category: "learning-coding"
description: "Generate a trivia game from a codebase's real architecture, history, stats, and code, where every question's answer is verifiable from a cited source — turning facts into engaging, accurate team learning."
techniques:
  - ST-01
  - ST-02
  - RT-05
  - ED-02
  - QA-01
difficulty: intermediate
tags:
  - learning-coding
  - gamification
  - onboarding
  - team-building
  - quiz
updated: "2026-06-07"
related_prompts:
  - domain-learning-coding/learning_mini_lesson_generation.md
  - domain-learning-coding/learning_code_evolution_visualization.md
  - domain-learning-coding/learning_code_pattern_recognition.md
  - domain-learning-coding/learning_socratic_dialogue_code_review.md
---

# Codebase Trivia Game Generator

**Objective:** Generate a trivia game from a codebase's real architecture, history, stats, and code, where every question's answer is verifiable from a cited source — turning facts into engaging, accurate learning rather than fun-sounding fiction.

**When to use:**
- Onboarding, knowledge-sharing sessions, or team-building around a codebase.
- Hackathon warmups or engineering all-hands.
- Reinforcing architecture, conventions, and history in a memorable format.
- Async (Slack-based) learning for distributed teams.

**When NOT to use:**
- When you lack real data (git history, code, metrics) and would have to invent "facts."
- High-stakes assessment (this is for engagement, not certification).
- Teaching a concept from scratch (use lesson generation).

**Audience:** Engineering teams (all levels), facilitators, and onboarding leads.

---

## Inputs / Context

The user supplies:
1. **Source material** — architecture notes/ADRs, git history, code metrics, and representative code, pasted wrapped in a named tag, e.g. `<source>...</source>`.
2. **Audience and goal** (onboarding vs team-building vs knowledge reinforcement).
3. **Format** (live team competition, individual quiz, async Slack).
4. **Difficulty mix** desired.
5. **Optional:** known incidents, fun facts, or conventions to feature.

Every factual question must trace to the supplied source; reference it by its tag name in the explanation.

---

## Constraints

### Must
- Make every answer **verifiable from the supplied source**; include the verification (file path, git command, or quoted code) in the explanation.
- Cover varied categories (architecture, history, stats, code deep-dives, tooling) and difficulty tiers.
- For "what does this code output?" questions, the snippet must be real (from `<source>`) or clearly labeled as a constructed example, and the answer must be traceable by reasoning.
- Write plausible distractors and an educational explanation for each question.
- Provide an answer key and facilitation guidance.

### Must Not
- Invent statistics, dates, incidents, codenames, or "fun facts" not in the supplied source.
- Mark an answer correct that the source doesn't support.
- Write trick questions whose "correct" answer is actually ambiguous.
- Present a constructed code example as if it were from the codebase.

---

## Instructions

1. **Mine the source.** From `<source>`, extract verifiable facts: architecture decisions, history milestones, metrics, notable code, tooling, incidents. Note the verification path for each.
2. **Design categories and tiers.** Spread questions across categories and across Easy → Expert difficulty.
3. **Write questions.** Each with a clear stem, 4 options (one correct), plausible distractors, and an explanation that cites the verification source.
4. **Add code questions.** Use real snippets (or label constructed ones); the correct output/behavior must be derivable by tracing.
5. **Build a lightning round.** Quick, unambiguous, source-backed facts.
6. **Assemble the game.** Scoring, format rules (live/async), and an answer key with explanations.
7. **Add facilitation guidance.** Timing, "read the explanations" emphasis, prize ideas.
8. **Self-check (verification).** For every question: is the answer supported by the source, is the verification included, are distractors clearly wrong?

---

## False-Positive Prevention

❌ **DON'T:**
- State a stat, date, or "fun fact" you can't trace to the supplied source.
- Mark an option correct without source support.
- Use a code snippet you claim is "from the codebase" but actually made up.
- Write questions whose intended answer is debatable.
- Bury the learning — the explanation is the point.

✅ **DO:**
- Include the verification (path, command, or quoted code) in every factual explanation.
- Label any constructed example as constructed.
- Make exactly one option defensibly correct.
- Keep distractors plausible but clearly wrong on inspection.
- Spread difficulty and category for engagement.

---

## Output Format

```
# Codebase Trivia: [project]

## Game Overview
[questions, categories, duration, format]

## Category N: [name]
### Question N.M ([difficulty])
**[stem]**
A) ... B) ... C) ... D) ...
**Answer:** [letter + text]
**Explanation:** [why + verification source]

## Lightning Round
## Scoring Guide
## Facilitation Tips
```

---

## Example Output

```markdown
# Codebase Trivia: E-Commerce Platform

## Game Overview
40 questions · 6 categories · 45–60 min · teams of 4–6

## Category 1: Architecture & Design

### Question 1.1 (Easy)
**What architectural pattern does the main backend follow?**
A) Monolith with shared DB  B) Microservices + event sourcing
C) Layered architecture with repository pattern ✓  D) Hexagonal

**Answer:** C
**Explanation:** Controllers → services → repositories → models. **Verify:** `ADR-001-layered-architecture.md` in `<source>`.

### Question 1.3 (Hard)
**What's the max items in one order, and why?**
A) 100 (arbitrary)  B) 50 (UI perf)  C) 999 (DB column)  D) 25 (payment processor batch limit) ✓

**Answer:** D
**Explanation:** The processor caps line items per charge; limit set to 25 for buffer. **Verify:** `config/order-limits.ts` in `<source>`.

## Category 2: History & Lore

### Question 2.1 (Easy)
**When was the first commit?**
A) Jan 2020  B) Mar 2021 ✓  C) Aug 2019  D) Dec 2021

**Answer:** B
**Explanation:** Repo created March 2021. **Verify:** `git log --reverse --format="%ai %s" | head -1`.

## Category 4: Code Deep Dive

### Question 4.1 (Medium)
**What does this output?** *(constructed example)*
```javascript
const r = ['a','b','c'].reduce((acc, v, i) => acc + v + i, '');
console.log(r);
```
A) "abc012"  B) "a0b1c2" ✓  C) "0a1b2c"  D) "abc"

**Answer:** B
**Explanation:** Trace: ""→"a0"→"a0b1"→"a0b1c2". *(Constructed to teach `reduce`; not from the codebase.)*

## Lightning Round (source-backed)
1. Default pagination limit? → 20 (verify `config/pagination.ts`)
2. Test framework? → Jest (verify `package.json`)
3. Primary database? → PostgreSQL (verify `ormconfig`)

## Scoring Guide
| Difficulty | Points |
|------------|--------|
| Easy | 10 | Medium | 20 | Hard | 30 | Expert | 50 | Lightning | 5 each |

## Facilitation Tips
1. Mix categories; don't cluster all architecture questions.
2. Always read the explanation aloud — the learning is there.
3. Let teams discuss briefly before answering.
4. Break after ~20 questions.
```

---

## Verification

- [ ] Every factual answer is supported by the supplied source.
- [ ] Each factual explanation includes a verification path (file, command, or quoted code).
- [ ] Constructed code examples are labeled as constructed.
- [ ] Exactly one option per question is defensibly correct.
- [ ] No invented stats, dates, incidents, or "fun facts."
- [ ] Difficulty and categories are varied.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the goal as an engaging but verifiable trivia game.
- **ST-02 (Structured Sequential Instructions):** Mine → design → write → code questions → lightning → assemble → verify.
- **RT-05 (Evidence-Based Reasoning):** Requires a verification source for every factual answer.
- **ED-02 (Progressive Exercise Generation):** Spreads questions across difficulty tiers.
- **QA-01 (Self-Verification):** Final pass confirms each answer is source-supported.

---

## Related Prompts

- `domain-learning-coding/learning_mini_lesson_generation.md` — Turn trivia topics into full lessons.
- `domain-learning-coding/learning_code_evolution_visualization.md` — Source the history-and-stats questions.
- `domain-learning-coding/learning_code_pattern_recognition.md` — Source the architecture questions.
- `domain-learning-coding/learning_socratic_dialogue_code_review.md` — Go deeper on a topic conversationally.
