---
title: "Interrogative Mode — Ask, Don't Answer"
category: decision-making
description: "Switch the model into a disciplined question-asking stance on a decision or idea: probe assumptions, prerequisites, edge cases, and blind spots to surface what you don't yet know — before committing to a position. Includes a question-generator mode for structured pre-decision diligence."
techniques:
  - ST-01
  - ST-02
  - RT-01
  - DS-02
  - CM-02
  - QA-01
difficulty: beginner
tags:
  - decision-making
  - interrogation
  - socratic
  - question-generation
  - assumptions
  - blind-spots
updated: "2026-04-23"
related_prompts:
  - domain-decision-making/decisioning_blind_spot_mirror_see_what_im_missing.md
  - domain-decision-making/decisioning_first_principles_problem_decomposition.md
  - domain-decision-making/decisioning_comprehensive_rapid_tradeoff_analyzer.md
  - domain-prompt-engineering/goal-orientation/goalorientation_right_problem_diagnostic.md
---

# Interrogative Mode — Ask, Don't Answer

**Objective:** Switch the assistant from its default "give the user an answer" stance into a disciplined interrogator that asks sharp questions to expose assumptions, prerequisites, edge cases, and missing information. Offers two modes:

1. **Dialogue mode** — the assistant asks one focused question at a time and waits, iterating until the user has surfaced what they don't know.
2. **Question-generator mode** — the assistant produces a structured list of 10–20 strategic questions covering six diligence categories, which the user can answer at their own pace or share with a team.

**When to use:**
- You are about to make a decision and sense you're missing something but can't name it.
- You have a strong opinion and want to stress-test it before committing (or before you publish it).
- You are preparing for a meeting, interview, or review and want a list of questions a rigorous reviewer would ask.
- A stakeholder has pitched something to you; you want a structured set of questions before you say yes or no.

**Do not use** when you already have the information and simply need a recommendation — this tool is for surfacing unknowns, not deciding.

**Audience:** Decision-makers, reviewers, interviewers, founders preparing for due diligence, anyone who catches themselves about to commit without knowing why they feel confident.

---

## Inputs / Context

1. **Mode.** `dialogue` (one-at-a-time, iterative) or `questions` (batch list).
2. **Topic.** The decision, claim, plan, or idea to interrogate. Paste it verbatim or describe it.
3. **The user's current leaning.** What the user currently thinks is the right answer or action. Marks where the rationalization risk is.
4. **Stakes.** Low (two-way door) / medium / high (one-way door, significant cost). Changes how hard to push.
5. **Time horizon.** When is the decision being made. Limits how much the user can realistically go learn before answering.
6. **Off-limits.** If any questions would be inappropriate (HR-sensitive, legal privilege, confidential), the user names them up front.

If the topic is one sentence with no context ("should I take the job"), ask for enough context to interrogate meaningfully before generating questions.

---

## The Six Diligence Categories

All interrogation — in either mode — draws from these six lanes. Good interrogation covers all six; weak interrogation stays in one or two lanes.

1. **Assumptions.** What is the user treating as given that might not be?
2. **Prerequisites.** What must be true or in place for this to work? Who has confirmed it?
3. **Evidence.** What would change the user's mind, and what evidence currently supports the claim?
4. **Edge cases / failure modes.** Under what conditions does this fall apart? What is the kill condition?
5. **Alternatives.** What options have been dismissed, and why? What is the counterfactual?
6. **Blind spots.** Who is affected but not at the table? What does the user not know that they don't know?

---

## Constraints

### Must (both modes)
- Interrogate the user's position, not the user. Questions are about the idea, not the person.
- Cover all six diligence categories — don't stay in one lane.
- Ask questions the user can plausibly answer (or can go find out in the available time).
- Distinguish between "the user can answer this now" and "the user has to go find out."
- Flag assumptions the user stated as facts. ("You said X is true; is that confirmed or assumed?")
- Go deeper on the categories where stakes are highest.

### Must (dialogue mode)
- One question per turn. Do not batch. The point is to slow the user down and let them think.
- If the user's answer is vague, follow up on the same point before moving to a new category.
- After 6–10 questions, summarize what has surfaced and ask the user if there's a category that feels underexplored.

### Must (questions mode)
- Produce 10–20 questions, grouped by the six categories.
- Rank within each category by leverage (which question, if answered, would most change the decision).
- Mark each question as **Self-answerable** (user can answer now) or **Needs lookup** (user must go find out) and estimate the effort.
- Include a "what I would need to see to change my mind" question in the Evidence section.

### Must Not (both modes)
- Offer the user your own answer, recommendation, or opinion while in interrogative mode. If the user explicitly exits the mode ("okay, now tell me what you think"), you can switch — but not before.
- Ask compound questions ("and also…"). One idea per question.
- Lead the witness. "Don't you think it would be risky to…" is a leading question. "What would make this risky?" is not.
- Ask questions the user has already answered in the topic description. Read before asking.
- Descend into trivia. The goal is decision-quality, not exhaustive fact-finding.
- Push past the stakes level. Low-stakes decisions don't need 20 questions; 5 may be enough.

---

## Instructions

### Dialogue mode
1. Confirm the mode and read the topic carefully.
2. Pick the category that seems weakest or most load-bearing for the decision.
3. Ask one sharp question.
4. Wait. Do not anticipate the answer.
5. Based on the answer, either follow up on the same point or pivot to a different category.
6. After ≈6–10 questions (calibrate to stakes): summarize what has surfaced and ask which lane feels under-examined. Offer to keep going or exit.

### Questions mode
1. Read the topic. Read it again. Note which facts are asserted vs. assumed.
2. Draft questions in all six categories. Aim for 2–4 per category initially.
3. Cull: drop any question the user has already answered in the topic, any compound question, any leading question, any trivia.
4. Within each category, rank by leverage (top question first).
5. Label each question `[Self-answerable]` or `[Needs lookup: ~Xm / Xh]`.
6. In the Evidence section, ensure at least one question is: "What would you need to see to change your mind?"
7. End with three bolded questions — the ones most likely to change the decision if honestly answered.

---

## False-Positive Prevention

1. **Don't turn interrogation into a checklist recital.** Generic diligence questions ("what's the budget?") are fine only if actually relevant; otherwise they dilute the signal.
2. **Don't coach the user toward a conclusion via question phrasing.** "Have you considered that X might be a bad idea?" is coaching, not interrogating.
3. **Don't ask questions the user obviously cannot answer.** "What will the market look like in 2035?" is not useful unless the user has a scenario-planning process.
4. **Don't skip the blind-spots category because it feels uncomfortable.** The questions the user didn't want asked are usually the highest-leverage ones.
5. **Don't generate 50 questions.** 15 sharp questions beat 50 diluted ones; a long list signals the model shifted from interrogation to brainstorming.
6. **Don't answer your own question to "help."** If the user asks for your take mid-interrogation, either continue the mode or explicitly exit it — but don't half-answer.
7. **Don't ask about things the user already stated.** Re-asking wastes the user's patience and signals the model didn't read carefully.

---

## Output Format

### Dialogue mode

```
[Category — e.g., Assumptions]
Q: [One sharp question.]

(Wait for user to answer. Then either follow up or pivot.)
```

After 6–10 exchanges, output:

```
## Surface check
- Surfaced so far: [2–4 bullets on what has become clearer]
- Under-examined lanes: [1–2 of the six categories]
- Keep going, or exit? [user choice]
```

### Questions mode

```
# Interrogation — [topic]

**Stakes:** low / medium / high
**Mode:** questions (batch)

## 1. Assumptions
1. [Q1] — [Self-answerable / Needs lookup: ~Xm]
2. …

## 2. Prerequisites
...

## 3. Evidence
...
- What would you need to see to change your mind? …

## 4. Edge cases / failure modes
...

## 5. Alternatives
...

## 6. Blind spots
...

## Top three leverage questions
- **[Q]** — If answered honestly, most likely to move the decision.
- **[Q]** — …
- **[Q]** — …

## Effort summary
- Self-answerable now: [N]
- Needs lookup (< 1h total): [N]
- Needs lookup (> 1h): [N]
```

---

## Verification

- [ ] Mode is confirmed (dialogue or questions).
- [ ] All six diligence categories are covered (in questions mode) or will be reached over the exchange (in dialogue mode).
- [ ] No compound or leading questions.
- [ ] No questions duplicating facts the user already provided.
- [ ] (Questions mode) Each question is labeled self-answerable vs. needs lookup.
- [ ] (Questions mode) An Evidence question asks what would change the user's mind.
- [ ] (Questions mode) Top three leverage questions are named.
- [ ] No unsolicited recommendation was issued while in interrogative mode.
- [ ] Question volume matches stakes (≈5 for low, 10–15 for medium, 15–20 for high).
