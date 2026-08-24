---
title: "Rapid Diagnostic of AI Skill Across Prompt Craft, Context, Intent, and Specification"
category: prompt-engineering/skill-development
description: "A ~10-minute self-assessment that scores the user across four orthogonal disciplines of AI work — prompt craft, context management, intent clarity, and specification — and returns the single weakest discipline to work on next. Not a maturity model; a next-step locator."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - skill-development
  - diagnostic
  - self-assessment
  - four-disciplines
  - prompt-engineering-skill
updated: "2026-04-20"
related_prompts:
  - domain-prompt-engineering/skill-development/promptcraft_deep_four_discipline_roadmap.md
  - domain-prompt-engineering/skill-development/promptcraft_pre_ai_thinking_exercise.md
  - domain-prompt-engineering/skill-development/promptcraft_personal_context_document.md
  - domain-prompt-engineering/skill-development/promptcraft_rewrite_vague_ask.md
---

# Rapid Diagnostic of AI Skill Across Prompt Craft, Context, Intent, and Specification

**Objective:** In about ten minutes, tell the user which of the four AI-work disciplines — prompt craft, context management, intent clarity, or specification — is currently their weakest, with one concrete next action. No scores for bragging. No maturity model. One next step.

**When to use:** The user has been working with AI for more than a month, has the sense that "something is off," and wants a fast orientation on where to invest the next two weeks of practice. Also useful as a quarterly check-in.

**Audience:** Individuals already practicing with AI who want a lightweight way to figure out where their practice has the most slack.

---

## The Four Disciplines

| Discipline | What it is | Failure mode when weak |
|---|---|---|
| **Prompt craft** | The mechanical skill of writing the prompt — structure, length, format, explicit instructions, output contract. | Prompts get vague answers; user relitigates output for an hour. |
| **Context management** | What the model can see — files attached, history, pasted snippets, persistent memory, project structure. | Model answers with the wrong information because it didn't have the right information. |
| **Intent clarity** | Knowing what the user actually wants — the outcome, the "done," the value hierarchy. | User accepts plausible answers that miss the real need. |
| **Specification** | Turning intent into something observable and testable. | User can't tell whether the output is any good; no stop rule; iteration loops forever. |

The disciplines are orthogonal. Weakness in one doesn't imply weakness in another. A user can write crisp prompts with great specifications but feed the model the wrong context, and their output will be confidently wrong.

---

## Inputs Required

1. **Three real recent tasks** the user ran with AI in the last two weeks. Not hypotheticals. Short descriptions, one sentence each.
2. **One recent output the user was dissatisfied with.** The actual chat or file, not a description.
3. **The user's honest answer** to each discipline's rapid questions below. Self-scoring only works if the user is willing to fail the questions.

Refuse to run the diagnostic on hypothetical tasks. The value comes from the user grounding each discipline in their actual recent work. If the user has no recent AI work, recommend two weeks of active use before running this.

---

## Instructions

Run four sections, one per discipline, in order. Each takes ~2 minutes. Score each section 0 / 1 / 2 (not strong / adequate / strong).

### Section 1 — Prompt craft (2 min)

Answer yes/no:
1. In your most dissatisfying recent output, did your prompt explicitly say what the output format should be?
2. Did you tell the model what "done" looked like?
3. Did you separate constraints from instructions?

Score: 0 no's → 2; 1 no → 1; 2–3 no's → 0.

### Section 2 — Context management (2 min)

Answer yes/no:
1. For a task that depended on a file / codebase / prior context, did you attach or paste it, rather than describing it?
2. Can you name, right now, what persistent memory or project context the model was operating under?
3. If the task touched prior conversation history, did the relevant parts reach the model (not just your memory)?

Score: 0 no's → 2; 1 no → 1; 2–3 no's → 0.

### Section 3 — Intent clarity (2 min)

Answer yes/no:
1. Before prompting, could you have written the outcome of the task in one sentence?
2. Did the prompt name the outcome, not just the action?
3. If someone asked "what does a perfect output look like?" before you prompted, could you have answered in under 30 seconds?

Score: 0 no's → 2; 1 no → 1; 2–3 no's → 0.

### Section 4 — Specification (2 min)

Answer yes/no:
1. Could a stranger read your prompt and your output and tell whether the output succeeded?
2. Did the prompt name at least one observable criterion the output had to pass?
3. Did you have a stop rule — something other than "keep iterating until it feels right"?

Score: 0 no's → 2; 1 no → 1; 2–3 no's → 0.

### Step 5 — Locate the weakest discipline

Lowest score wins. Ties broken in this order: specification → intent → context → prompt craft. (Spec problems compound downstream the hardest; prompt-craft weaknesses are the cheapest to fix.)

### Step 6 — Produce the next action

Return a single next action for the weakest discipline:

- **Weakest: Prompt craft.** Run `domain-prompt-engineering/prompt-improvement/engineering_prompt_improver.md` on your three recent prompts. Rewrite each one and rerun the task with the rewritten prompt.
- **Weakest: Context management.** Run `promptcraft_personal_context_document.md` to build a reusable context document, and run `cos_memory_scaffold_claude_md.md` for persistent memory.
- **Weakest: Intent clarity.** Run `goalorientation_right_problem_diagnostic.md` on your next three tasks. Run `promptcraft_pre_ai_thinking_exercise.md` before any prompt for two weeks.
- **Weakest: Specification.** Run `promptcraft_specification_defines_done.md` on your next three tasks, then run `promptcraft_eval_harness.md` for the task type you run most often.

### Step 7 — Set a check-in

Run the rapid diagnostic again in two weeks. If the weakest discipline changes, the practice is working. If it stays the same, escalate to `promptcraft_deep_four_discipline_roadmap.md`.

---

## Constraints

### Must
- Require three real recent tasks and one dissatisfying output before scoring.
- Return exactly one weakest discipline and one next action.
- Keep total runtime under 15 minutes.
- Break ties by downstream cost (specification > intent > context > prompt craft).

### Must Not
- Produce a maturity-model ranking. This is a next-action tool, not a score-bragging tool.
- Score on hypothetical or imagined tasks.
- Return more than one "priority" discipline — multi-priority is indistinguishable from no priority.
- Grade prompt craft as weakest when intent or specification are also weak; fixing prompt craft on top of weak intent wastes effort.

---

## False-Positive Prevention

1. **Self-flattery inflates scores.** A user who says yes to every question probably isn't answering the question. Reread each no-answer: "I explicitly said what 'done' looked like" — did the prompt contain the word "done," or a specific observable criterion? If not, that's a no.
2. **Intent failures masquerade as prompt-craft failures.** "My prompt was vague" is often "I didn't know what I wanted." If intent scores 0, prompt craft is a symptom, not the problem.
3. **Context failures masquerade as model failures.** "The model got the facts wrong" often means "the model didn't have the facts." Score context as weak when the answer came back confidently wrong, not when the answer was stylistically bad.
4. **Specification failures masquerade as iteration fatigue.** If the user iterated seven times without getting closer, that's almost always a specification problem, not a prompt-craft one. There was no stop rule because there was no testable definition of done.
5. **Don't grade aspirationally.** "I usually write good prompts" is not a yes to "did my dissatisfying prompt explicitly state output format?" Grade the specific dissatisfying output, not the average case.

---

## Output Format

```markdown
## Three tasks and one dissatisfying output
1. [task]
2. [task]
3. [task]
Dissatisfying output: [one-line reference]

## Scores
- Prompt craft: [0/1/2] — [one-line reason]
- Context management: [0/1/2] — [one-line reason]
- Intent clarity: [0/1/2] — [one-line reason]
- Specification: [0/1/2] — [one-line reason]

## Weakest discipline
[Name] — [one-sentence reason].

## Next action
- Run: [specific prompt path]
- On: [specific tasks / outputs]
- By: [specific date, within two weeks]

## Re-check
Run this diagnostic again on [date two weeks out]. If the weakest
discipline has changed, the practice is working. If not, escalate to
`promptcraft_deep_four_discipline_roadmap.md`.
```

---

## Verification

- [ ] User supplied three real recent tasks, not hypotheticals.
- [ ] A specific dissatisfying output was named.
- [ ] Each discipline was scored 0/1/2 with a one-line reason.
- [ ] Exactly one weakest discipline was returned.
- [ ] The next action names a specific prompt path, specific artifacts to apply it to, and a deadline within two weeks.
- [ ] A re-check date was set.
