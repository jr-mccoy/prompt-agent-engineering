---
title: "Pre-AI Thinking Exercise Captured Off-Screen Before Opening a Chat"
category: prompt-engineering/skill-development
description: "A short, structured off-screen thinking pass — done on paper, in a text file, or on a whiteboard with no model in the loop — that surfaces what you actually want, what you already know, and what decisions you've already made, before the first token is typed into a chat. Prevents the failure mode of outsourcing the thinking to the model and then relitigating the model's output for an hour."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-01
  - QA-01
difficulty: intermediate
tags:
  - skill-development
  - prompt-craft
  - pre-work
  - thinking-exercise
  - off-screen
updated: "2026-04-20"
related_prompts:
  - domain-prompt-engineering/skill-development/promptcraft_rewrite_vague_ask.md
  - domain-prompt-engineering/skill-development/promptcraft_specification_defines_done.md
  - domain-prompt-engineering/goal-orientation/goalorientation_right_problem_diagnostic.md
  - domain-business-strategy/chief-of-staff/cos_clarify_fuzzy_goals.md
---

# Pre-AI Thinking Exercise Captured Off-Screen Before Opening a Chat

**Objective:** Before any prompt is written, produce a one-page off-screen artifact that names what you actually want, what you already know, what you've already decided, and what you are willing to accept as "done." The artifact is done by hand or in a plain text file with no model in the loop. This is the single highest-leverage pre-prompt habit in the skill-development track — it is not a prompt the model runs; it is the instructions the user follows.

**When to use:** Any task larger than a 30-second lookup. Especially before: a multi-step coding task, a document you'll ship, a decision you'll defend, a research question, or anything where the model's first answer would tempt you to just accept it.

**Audience:** Individuals already using AI who notice they spend 40+ minutes relitigating model output they could have avoided with 5 minutes of upfront thinking.

---

## Inputs Required

Nothing from the model. Two things from the user:

1. **The task, in the user's own words.** Whatever they would have typed into a chat box.
2. **A blank page or plain text file.** Not a chat window. The tool matters. A chat window is a commitment to typing at a model; a blank page is a commitment to thinking.

Refuse to run this exercise inside a chat. If the user has already opened a chat, close it first. Running this exercise inside the chat UI defeats the purpose — the user will start prompting before they finish thinking.

---

## Instructions

The user runs this themselves. The prompt is a script they follow; the output is handwritten or typed into a plain file.

### Step 1 — Write the task as a one-sentence outcome, not an action

Not "help me draft a memo." That's an action. The outcome is what changes in the world when the task is done. "A 1-page memo the VP can forward to legal without rewriting." Write the outcome in one sentence.

If you can't write it in one sentence, the task isn't ready for AI. Do this step until it fits.

### Step 2 — Write down what you already know

List, in bullet form, what you already know about the task. Include:
- Facts you have. ("Legal's main concern on this deal is X.")
- Decisions you've already made. ("This memo is going to Jane, not to the full exec team.")
- Constraints. ("Under 1 page. No jargon. Must name the exception we took in March.")

Most prompts fail because the user types only the task and skips what they already know — forcing the model to guess. This list is what the user will paste in later, but they can't paste it until they've written it.

### Step 3 — Write down what you don't know

List, in bullet form:
- Facts you're missing. ("I don't know the actual exposure number.")
- Decisions you haven't made. ("I haven't decided whether to recommend the settlement or ask for more time.")
- Things you'd need before the task can be completed. ("I need the March email thread.")

If the list of unknowns is longer than the list of knowns, stop and gather knowns first. A model asked to write a memo with more unknowns than knowns will produce plausible-looking filler.

### Step 4 — Write down what "done" looks like

In 2–4 lines, state what the finished artifact must be true of for you to accept it. Not "it should be good." Specific:
- "Under 1 page."
- "Names the March exception explicitly."
- "Recommends one path, not two."
- "Jane could forward it without edits."

If you can't write "done," the model can't hit it.

### Step 5 — Decide what you want from the model specifically

Circle one:
- **Draft:** Model produces the artifact; user will edit.
- **Critique:** User produces the artifact; model pokes holes.
- **Options:** Model produces 2–3 structurally different versions; user picks.
- **Thinking partner:** Model asks questions, user answers, both converge on an outline.
- **Fact-check:** User produces the artifact; model verifies claims against sources.

Different modes require different prompts. Most users default to "draft" for every task; many tasks go better with "critique" or "options."

### Step 6 — Decide what to hand to the model

Now — and only now — decide what from Steps 1–5 actually needs to go in the prompt. Usually:
- Outcome sentence (Step 1): always.
- Knowns (Step 2): always.
- Unknowns (Step 3): include if they're relevant to the task.
- Done (Step 4): always.
- Mode (Step 5): always.

The final prompt is Steps 1, 2, 4, 5 pasted in, plus whatever specific instructions the mode demands.

### Step 7 — Time-box the exercise

Cap at 15 minutes. If it's taking longer, the task isn't AI-shaped yet — it's a planning task the user needs to do for themselves. The exercise is not a substitute for thinking through a decision; it's a structured prompt-writing pre-flight.

---

## Constraints

### Must
- Be done off-screen or in a plain text file. Not in a chat window.
- Produce a one-sentence outcome before any other step.
- Include knowns, unknowns, done, and mode.
- Finish within 15 minutes or route the task back to planning.

### Must Not
- Be run inside a chat window.
- Be used as a substitute for actually thinking through an unresolved decision.
- Be skipped because "this one's quick" — quick tasks pass Step 1 in under a minute anyway.
- Generate the prompt automatically from the artifact. The artifact's value is that it was written by hand; handing it to the model and asking for a prompt defeats the point.

---

## False-Positive Prevention

1. **The exercise disguised as the task.** Users sometimes fill out the artifact for a task that isn't really the task they want — e.g., they write "draft the memo" when the real task is "decide whether to settle." Before Step 2, reread Step 1 and ask: is this the real task? If not, restart with the real one.
2. **Unknowns passed to the model as if they were knowns.** An unknown is not a known. If Step 3 says "I don't know the exposure number," don't let the model fill it in. Get the number.
3. **"Done" written too loosely.** "It should be good" is not done. Rewrite each done-bullet until it names something observable.
4. **Mode chosen by habit.** Most users default to "draft." Check: is this task actually a draft task, or is critique / options / thinking partner a better fit? Drafts from the model are the lowest-value mode for tasks the user already half-knows.
5. **Using this prompt as a chat prompt.** This isn't a prompt the model runs. Pasting it into a chat is the anti-pattern the exercise is designed to break.

---

## Output Format

The user produces a single plain-text artifact. No model output.

```markdown
# Pre-AI thinking: [task name]

## Outcome (one sentence)
[...]

## What I already know
- [...]
- [...]

## What I don't know
- [...]
- [...]

## Done looks like
- [...]
- [...]

## Mode I want from the model
[Draft | Critique | Options | Thinking partner | Fact-check]

## Prompt I'll write next
(One line — what the first message to the model will actually say.)
```

---

## Verification

- [ ] The artifact was written off-screen or in a plain text file, not a chat.
- [ ] Outcome is one sentence, not an action.
- [ ] At least three knowns are listed.
- [ ] Unknowns are listed separately and are not passed to the model as facts.
- [ ] Done is specific enough that a stranger could tell pass from fail.
- [ ] Mode is explicitly chosen, not defaulted to "draft."
- [ ] Total time spent was ≤ 15 minutes.
