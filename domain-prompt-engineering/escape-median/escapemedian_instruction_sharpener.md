---
title: "Sharpen an Instruction So the Model Cannot Default to the Median"
category: prompt-engineering/escape-median
description: "Rewrite a vague instruction into a version the model cannot satisfy by producing average output — adding the user's prior, the views to suppress, the hedge phrases to forbid, the specific form the answer must take, and the test the output must pass."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - RT-09
  - QA-01
difficulty: intermediate
tags:
  - escape-median
  - instruction-design
  - sharpening
  - personalization
  - prompt-rewriting
updated: "2026-04-20"
related_prompts:
  - domain-prompt-engineering/escape-median/escapemedian_default_position_mapper.md
  - domain-prompt-engineering/escape-median/escapemedian_correction_compounder.md
  - domain-prompt-engineering/model-behavior/modelbehavior_active_coaching_in_session.md
---

# Sharpen an Instruction So the Model Cannot Default to the Median

**Objective:** Take a vague instruction and rewrite it into a version the model *cannot* satisfy with average output. This is done by (1) making the user's prior explicit, (2) naming the default the model would otherwise produce and forbidding it, (3) forbidding the specific hedge phrases the model will reach for, (4) specifying the output form narrowly enough that medianness is visible, and (5) stating a pass/fail test the output must meet.

**When to use:** You know the model is giving you balanced, plausible, mildly useful output — and you want the specific, committed, opinionated output that matches your situation. Use this after (or in place of) `escapemedian_default_position_mapper.md` when you already know the default and just need the instruction tightened.

**Audience:** Individual users moving from generic output to high-signal, personalized output. Applies across topics (career decisions, technical tradeoffs, strategic choices, editorial feedback, content generation with a specific voice).

---

## Inputs Required

1. **The vague instruction** as currently written. Verbatim.
2. **The output the model produced** for this instruction (at least one example). If no output exists yet, produce one before sharpening — you cannot sharpen against an imagined default.
3. **The user's prior** — the view, preference, or orientation they want the output grounded in. If the user doesn't have a prior, stop: sharpening a prompt without a prior just produces a different median.
4. **Known hedge phrases** from the prior output (quoted) that the user wants suppressed. If unknown, run `escapemedian_default_position_mapper.md` first.
5. **Whether the prompt is one-off or repeated.** Repeated prompts get a different sharpening (rules over examples).

Refuse to sharpen a prompt on a topic where the user is genuinely undecided. Sharpness against no prior produces false confidence. Redirect to `goalorientation_right_problem_diagnostic.md`.

---

## Instructions

### Step 1 — Identify what makes the current instruction vague

Categorize the vagueness against a fixed taxonomy:

- **Goal vagueness.** The output the user wants is not specified ("help me think through this").
- **Audience vagueness.** The model doesn't know who the answer is for.
- **Form vagueness.** Narrative, table, list, recommendation, analysis — unclear.
- **Stance vagueness.** The user's position is not stated, so the model averages.
- **Depth vagueness.** Overview vs. deep dive is not pinned, and the model defaults to overview.
- **Termination vagueness.** The model doesn't know when to stop, so it pads.

Name all that apply. Don't combine them into "it's too vague."

### Step 2 — Make the user's prior explicit

Add a sentence at the top of the prompt stating the user's prior as a position, not a question. Examples of the pattern:

- "I've already decided I want to X; tell me the strongest case against X, not a balanced overview."
- "I'm convinced that Y is the right answer here. I want you to pressure-test it, not weigh it against Z."
- "I'm writing for readers who [specific profile]; calibrate to them, not to a general audience."
- "My constraint is [specific]. Do not recommend anything that violates this, even if it would otherwise be your top suggestion."

The prior has to be stated as "what I've already concluded," not as "what I'm wondering." The model treats the two differently.

### Step 3 — Name and forbid the default

From the vague output (or the default map), quote the specific thing the model did that you don't want. Add an explicit override:

- "Do not balance views. I am asking for your single strongest recommendation."
- "Do not include disclaimers about context-dependence. Assume the context is exactly as stated."
- "Do not open with a summary of my question."

Negative instructions without positive replacements backfire. Every forbidden default should be paired with what to do instead.

### Step 4 — Forbid the hedge phrases

Quote the specific phrases the user doesn't want and put them in a short list. Example:

> Forbidden phrases: "it depends," "both have merit," "consider your specific situation," "it's important to note that."

Specificity matters. "Don't hedge" is weaker than a phrase list. Models can check phrase lists against their draft.

### Step 5 — Narrow the form so medianness is visible

Vague forms hide medianness. Sharp forms expose it. Pick one:

- **Ranked list with commitment.** "Give me your top 3, ranked, with the gap between #1 and #2 stated as large, medium, or small."
- **Single recommendation with reasoning.** "Your recommendation in one paragraph, followed by your one strongest counterargument in one paragraph. Nothing else."
- **Position letter.** "Write this as a memo from you to me taking a clear position. No 'on the other hand' paragraphs."
- **Decision tree.** "If [condition A], do X. If [condition B], do Y. I need decision rules, not considerations."

A form that can be filled with median output isn't narrow enough.

### Step 6 — Add the pass/fail test

One or two lines at the end of the prompt specifying what the output must contain and what would fail it. Examples:
- "The output must contain a single recommendation. If you list options without picking, you've failed."
- "The output must name at least one thing the user's plan is currently ignoring. If it doesn't, you've failed."

The test is for the *user* as much as the model: it tells the user whether to accept the output or re-prompt.

### Step 7 — Compose the sharpened prompt

Assemble in order: prior → forbidden defaults → forbidden hedges → narrow form → pass/fail test → the original question. Keep the total prompt short; long prompts re-introduce slack the model can default into.

---

## Constraints

### Must
- Name the vagueness type(s) before sharpening.
- State the user's prior as a position, not a question.
- Pair every negative instruction with what to do instead.
- Quote hedge phrases from the actual prior output, not generic ones.
- Narrow the form enough that a median answer would be visibly median.
- End with a pass/fail test.

### Must Not
- Sharpen without the user having a prior. Sharp prompts without priors just produce a different median.
- Invent hedges the user didn't observe. Use the actual output.
- Keep the original question ambiguous and stack overrides on top of it. Fix the question.
- Produce a prompt longer than necessary. Length re-introduces slack.
- Tell the user what their prior should be.

---

## False-Positive Prevention

1. **Sharp prompts can be wrong.** A prompt that forces a single committed answer will produce a confident answer even when the right answer is "we don't know." Use `goalorientation_right_problem_diagnostic.md` when commitment may be premature.
2. **"Forbidden phrases" can be routed around.** The model will rephrase hedges. Check outputs for semantic hedging, not just lexical. Update the phrase list after each iteration.
3. **Overriding too many defaults at once breaks the prompt.** If you forbid balance, depth, overview, and caveats in a single instruction, the model will pick one to violate. Order and limit.
4. **Priors can be wrong.** Sharpening against a wrong prior produces well-argued bad advice. If the user's prior might be the problem, say so and suggest mapping it first.
5. **Form narrowing has a ceiling.** A form so narrow it can't hold the real answer is worse than a broader form. If the narrowing forces the model to distort content to fit, widen it.
6. **The pass/fail test is not optional.** A sharpened prompt without a test still produces median output that sounds sharp.
7. **Sharpening doesn't transfer across topics.** Each topic has its own defaults. A sharpened career prompt template won't reliably work on a technical question.

---

## Output Format

```markdown
## Vagueness diagnosis
- Types present: [goal / audience / form / stance / depth / termination]
- One-sentence description of each that applies.

## User's prior (stated as a position)
> [...]

## Defaults to forbid (with replacements)
- **Don't:** [default]. **Do:** [replacement].
- ...

## Hedge phrases to forbid (from the actual prior output)
- "[...]"
- "[...]"

## Form
[Name the form and the one-sentence rule that makes it narrow.]

## Pass/fail test
The output must: [testable requirement]. If not, it has failed; re-prompt.

---

## Sharpened prompt (ready to paste)

```
[Prior → forbidden defaults → forbidden hedges → narrow form → pass/fail test → the question.]
```

## Notes
- This prompt is one-off / repeat-use.
- If repeat-use, promote [prior + forbidden defaults + test] into the system prompt or CLAUDE.md so you don't re-type them every session.
```

---

## Verification

- [ ] Vagueness was diagnosed by type.
- [ ] A real prior is stated as a position.
- [ ] Every negative instruction has a positive replacement.
- [ ] Hedge phrases are quoted from actual output.
- [ ] The form is narrow enough to expose median output.
- [ ] A pass/fail test is present and testable.
- [ ] The sharpened prompt is shorter than the original's pile of context, not longer.
