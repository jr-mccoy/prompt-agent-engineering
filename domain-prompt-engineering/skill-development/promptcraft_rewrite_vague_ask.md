---
title: "Rewrite a Vague Conversational Ask into a Fully Self-Contained Problem Statement"
category: prompt-engineering/skill-development
description: "Transforms a casual chat opener — 'help me with X,' 'can you look at this,' 'what do you think about Y' — into a self-contained problem statement the model can act on without follow-up. The rewritten version names the outcome, the inputs, the constraints, the done criteria, and the desired mode. Refuses to rewrite on synthetic examples; the user must supply a real ask."
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
  - rewrite
  - problem-statement
  - self-contained
updated: "2026-04-20"
related_prompts:
  - domain-prompt-engineering/skill-development/promptcraft_pre_ai_thinking_exercise.md
  - domain-prompt-engineering/skill-development/promptcraft_specification_defines_done.md
  - domain-prompt-engineering/goal-orientation/goalorientation_right_problem_diagnostic.md
---

# Rewrite a Vague Conversational Ask into a Fully Self-Contained Problem Statement

**Objective:** Take a real, vague, conversational opener the user was about to send to a model — "help me with this memo," "can you look at my code," "what do you think of this plan" — and rewrite it as a self-contained problem statement that names the outcome, the context, the constraints, the done criteria, and the mode the user wants from the model. The rewrite doesn't run the task; it produces the prompt the user will send.

**When to use:** Before sending any chat opener that is shorter than the task deserves — which, for most users, is most chat openers. Especially useful when the user realizes mid-type that the message is too vague to get a useful answer.

**Audience:** Individuals who already use AI and notice their first messages produce generic responses they spend 20+ minutes correcting.

---

## Inputs Required

1. **The real ask** the user was about to send — pasted verbatim, not paraphrased. If they changed it to sound more polished, they've already skipped the exercise.
2. **A brief answer (2–5 lines) to: what outcome am I actually after?** In the user's own words, not the prompt's words.
3. **Whatever files, links, or context the user expects to include.** List them, even if you won't paste them yet.
4. **A note on the desired mode.** Draft, critique, options, thinking partner, or fact-check. If the user doesn't know, default to critique for asks starting with "what do you think," draft for asks starting with "help me write," and options for asks starting with "should I."

Refuse to rewrite on a hypothetical or invented ask. The rewrite's value is that it is grounded in a real message the user was about to send. Pasting a made-up ask to see how the prompt works turns the exercise into an academic demo and the user learns nothing transferable.

---

## Instructions

### Step 1 — Read the original ask out loud

The original ask is almost always shorter than the task it's asking about. Reading it out loud surfaces how much the user is assuming the model can infer. Mark every noun/verb where the model would have to guess.

### Step 2 — Extract the implicit outcome

From the user's 2–5 line answer to "what outcome am I actually after," pull out the outcome in one sentence. Not the action ("review my memo"); the outcome ("a memo Jane can forward to legal without edits"). If the outcome can't be stated in one sentence, the user needs to run `promptcraft_pre_ai_thinking_exercise.md` first and come back.

### Step 3 — Extract the inputs

List what the model needs to see to do the task. For each:
- **Name it** ("the current draft," "the Q3 revenue spreadsheet," "the prior chat").
- **State whether it will actually be attached/pasted** or whether the user will describe it.
- **If described,** note the risk: anything important the model will miss?

Inputs the model can't see are the #1 cause of confidently wrong answers.

### Step 4 — Extract the constraints

List what the output must respect no matter what. Format, length, audience, tone, forbidden content, required content. Constraints the user takes for granted ("obviously it should be under a page") are the ones the model will violate.

### Step 5 — State the done criteria

2–4 lines, observable. "Under 1 page. Names the exception from March. Recommends one path, not two." Not "good."

### Step 6 — State the mode

One word: draft, critique, options, thinking partner, fact-check. If the original ask contained a different verb ("review"), reconcile: if the user really wants critique, replace "review" with "critique" in the rewrite so the model doesn't default to a redraft.

### Step 7 — Assemble the rewrite

Produce the new prompt in this order: outcome → inputs → constraints → done criteria → mode → the specific ask. Length is usually 10–30x the original. That's normal; the original was dramatically under-specified.

### Step 8 — Name what's still missing

Before handing the rewrite back, flag anything the user couldn't answer in Steps 2–6. If "I don't know the actual exposure number" showed up in inputs, say so — and flag that the model can't fill that in. Tasks with unknown load-bearing inputs either need the inputs first or need the mode changed to "thinking partner" rather than "draft."

### Step 9 — Offer a test

Optionally: run the rewritten prompt through `domain-prompt-engineering/goal-orientation/goalorientation_right_problem_diagnostic.md` if the user is unsure whether the outcome is the right outcome. Do this once per real task, not habitually — the pre-AI thinking exercise covers most cases.

---

## Constraints

### Must
- Work only on a real, pasted-verbatim ask.
- Produce an outcome sentence before anything else.
- List inputs with an attach/describe flag.
- Produce done criteria that are observable.
- Name the mode as one of the five canonical modes.
- Flag unresolved unknowns rather than papering over them.

### Must Not
- Rewrite on a hypothetical, paraphrased, or sanitized ask.
- Guess at the outcome. If the user can't state it, stop and route to the pre-AI thinking exercise.
- Invent constraints the user didn't state. (Exception: flag the ones the user probably forgot as questions, don't assert them.)
- Produce a rewrite that's only slightly longer than the original. If the rewrite is <3x the original, it's under-specified.
- Include the phrase "please help me" — that's the conversational ask the rewrite is replacing.

---

## False-Positive Prevention

1. **The rewrite that just restates the ask more politely.** A rewrite that doesn't add outcome, inputs, constraints, done criteria, and mode hasn't improved anything. If it adds none of those five, reject and restart.
2. **The rewrite that invents constraints.** If the user never said "under 1 page," the rewrite should not impose "under 1 page" silently. List it as a candidate constraint the user confirms.
3. **"Done" that's really a wish.** "Done is a great memo" is not done. Rewrite until a stranger could grade it.
4. **Outcome language polluted by the ask's language.** "Outcome: help with the memo" is the ask in outcome clothing. The outcome is what changes in the world when the memo is done; if the rewrite can't name that, go back to Step 2.
5. **Mode inferred wrong.** "What do you think of my plan" often gets rewritten as a draft prompt ("draft an improved plan"). The user didn't ask for a draft; they asked for critique. Preserve the mode the user actually wanted.
6. **The rewrite becomes the task.** The rewrite is the prompt, not the answer. If the user accepts the rewrite and closes the chat, they haven't done the task — they've just written a better prompt for the task.
7. **Skipped the "still missing" flag.** A rewrite that pretends to be complete when the user left unknowns is worse than a short, honest ask.

---

## Output Format

```markdown
## Original ask (verbatim)
> [pasted message]

## Implicit outcome (one sentence)
[...]

## Inputs the model needs
| Input | Attach / describe | Risk if described |
|---|---|---|
| [...] | [...] | [...] |

## Constraints
- [...]
- [...]
(Flagged as candidates for user confirmation: [...])

## Done criteria (observable)
- [...]
- [...]

## Mode
[Draft | Critique | Options | Thinking partner | Fact-check]

---

## Rewritten prompt
```
**Outcome:** [...]

**Inputs:**
- [...]

**Constraints:**
- [...]

**Done:**
- [...]

**Mode:** [...]

**Task:**
[The specific ask in imperative form, referring to the above by name.]
```

## Still missing (not invented)
- [Unknown load-bearing input]: [how to get it before prompting]
- [Unresolved constraint]: [how to decide]

## Next step
[Send the rewrite / gather the missing inputs first / run pre-AI thinking on the outcome]
```

---

## Verification

- [ ] The original ask is pasted verbatim, not paraphrased.
- [ ] Outcome is one sentence and names what changes in the world.
- [ ] Inputs list includes an attach/describe flag for each.
- [ ] Constraints invented by the rewrite are flagged as candidates, not asserted.
- [ ] Done criteria are observable.
- [ ] Mode is one of the five canonical modes.
- [ ] Unresolved unknowns are flagged separately, not hidden.
- [ ] The rewritten prompt is at least 3x the original ask's length.
