---
title: "Diagnose Why a Model's Behavior Deviates from Instructions"
category: prompt-engineering/model-behavior
description: "Root-cause analysis for why a specific model (Claude, GPT, Gemini) is failing to follow a specific instruction in a specific prompt — locating the deviation in the prompt, the model's base training, the context, or the interaction pattern rather than guessing."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-09
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - model-behavior
  - diagnostics
  - root-cause
  - instruction-following
  - prompt-debugging
updated: "2026-04-20"
related_prompts:
  - domain-prompt-engineering/model-behavior/modelbehavior_active_coaching_in_session.md
  - domain-prompt-engineering/model-behavior/modelbehavior_refactor_system_prompt.md
  - domain-prompt-engineering/prompt-improvement/engineering_prompt_improver.md
---

# Diagnose Why a Model's Behavior Deviates from Instructions

**Objective:** Given a specific prompt, a specific model's output, and the specific instruction that was violated, produce a root-cause diagnosis that identifies *where* the deviation originates (prompt wording, conflicting instructions, context overload, base-model priors, sampling variance, or a misread of intent) and a minimal-change fix targeted at that root cause. The diagnosis must be grounded in the actual output, not hypothetical behavior.

**When to use:** You've written a prompt, the model is not doing what you asked, and you want to fix it *once* rather than iterate by trial and error. Especially useful when a prompt has worked in the past and now doesn't, or when the same instruction works in one context and fails in another.

**Audience:** Prompt engineers, developers, and power users who work with Claude, GPT, Gemini, or other instruction-following models and need to correct behavior deviations without rewriting the whole prompt.

---

## Inputs Required

The diagnostic cannot proceed without all four of these. If any are missing or hypothetical, refuse to proceed and ask the user to provide them.

1. **The exact prompt** that produced the deviation (system prompt and user turn, verbatim — not paraphrased).
2. **The exact model output** that deviated (verbatim, including any preamble or disclaimers).
3. **The specific instruction that was violated** — one sentence. Not "it didn't follow the prompt" but "it output bullet points when the prompt said 'prose only.'"
4. **Model and version**, plus whether any tools, temperature, or system-level settings were in play.

Optional but useful:
- **Whether this has worked before** with the same prompt (locates the change).
- **Any recent edits** to the prompt (locates the introduced conflict).

Refuse hypothetical input ("imagine a prompt where..."). Root-cause work requires the real artifact. Diagnosing fake deviations produces fake causes.

---

## Instructions

### Step 1 — Verify the deviation is real

Before diagnosing cause, confirm the output actually violates the named instruction. Quote the instruction verbatim. Quote the output passage that violates it. If the violation is ambiguous — the instruction was open to interpretation — stop and report that the root cause may be *instruction ambiguity*, not model failure. Proceed to Step 2 only after the violation is crisp.

### Step 2 — Classify the deviation against a fixed taxonomy

Map the deviation to one or more of the following. Do not invent new categories.

- **Instruction conflict.** Another instruction in the same prompt pulls in the opposite direction. The model chose one and violated the other.
- **Instruction ambiguity.** The instruction has more than one reasonable reading. The model picked a different reading than the author intended.
- **Specification gap.** The instruction is stated at the wrong level (goal stated, mechanism not stated, or vice versa). The model filled the gap with a default.
- **Context crowding.** The instruction was stated early, then buried under a long context. The model's effective-attention weighting dropped the instruction.
- **Base-model prior.** The model has a strong default behavior (e.g., hedging, disclaimers, bullet lists, positive framing) that the instruction did not explicitly override. Suppressing this requires a stronger, more specific instruction.
- **Format vs. content confusion.** The instruction addresses format but the deviation is in content, or vice versa. The model interpreted a format instruction as a content instruction, or the reverse.
- **Role / system vs. user conflict.** The system prompt and user turn give conflicting signals. The model deferred to one over the other.
- **Sampling variance.** The instruction is usually followed but wasn't on this run (check by re-running). This is the only cause where "try again" is a valid fix.
- **Tool-state leakage.** A previous tool result, earlier turn, or cached context is influencing current behavior.

Name one primary cause and any contributing causes. If you cannot choose between two causes, name both and give the test that would disambiguate.

### Step 3 — Locate the cause in the prompt text

Quote the specific passage(s) in the prompt that produced (or failed to produce) the deviation. If the cause is *base-model prior*, point to the absence of an override (e.g., "no instruction overrides the default tendency to add disclaimers"). If the cause is *context crowding*, point to the position of the instruction relative to the bulk of the prompt.

### Step 4 — Propose the minimal fix

The fix should target the root cause, not symptoms. Guidelines:

- **Instruction conflict →** resolve the conflict by removing, reordering, or ranking the instructions explicitly.
- **Instruction ambiguity →** rewrite the instruction so only one reading is possible. Give a concrete example of compliant output.
- **Specification gap →** add the missing level (either the goal behind the mechanism, or the mechanism behind the goal).
- **Context crowding →** move the instruction closer to the end, or restate it at the end, or lift it into the system prompt.
- **Base-model prior →** add an explicit override that names the default and forbids it ("Do not add a preamble. Do not add disclaimers. Begin with the answer.").
- **Format vs. content confusion →** separate format and content instructions into labeled sections.
- **Role / system vs. user conflict →** align the two, or state which takes precedence.
- **Sampling variance →** re-run before changing the prompt.
- **Tool-state leakage →** start a fresh session to confirm, then clear or summarize the leaking context.

Do not recommend changes larger than what the diagnosis justifies. If the root cause is a single buried instruction, the fix is to move that instruction — not to restructure the whole prompt.

### Step 5 — Predict the test

State what the user should see after applying the fix. This is the falsifiable claim. Example: "After moving the 'prose only' instruction to the last line of the system prompt, re-run the prompt three times; all three outputs should be prose." If the fix doesn't pass this test, the diagnosis was wrong and the user should re-run this diagnostic with the new output.

---

## Constraints

### Must
- Quote actual prompt text and actual output text verbatim in the diagnosis.
- Pick a primary cause from the fixed taxonomy.
- Propose a minimal fix targeted at the root cause.
- Give a falsifiable post-fix test.

### Must Not
- Accept hypothetical inputs. Real prompt + real output only.
- Recommend a full rewrite unless the diagnosis explicitly warrants it.
- Stack multiple fixes "to be safe" — each fix should be tested independently.
- Blame the model when the prompt is the cause, or blame the prompt when a base-model prior is the cause.
- Invent a new category outside the taxonomy.

---

## False-Positive Prevention

1. **"Sampling variance" is easy to invoke and usually wrong.** Only accept it after at least two re-runs show the instruction *is* usually followed. If the deviation reproduces, it isn't variance.
2. **Don't conflate "the output is bad" with "the instruction was violated."** If the violation can't be stated as a sentence the output contradicts, the diagnosis target isn't instruction-following — it's output quality. Redirect to a quality critique instead.
3. **Context crowding gets over-diagnosed on long prompts.** Before claiming it, check whether the instruction is actually distant from the generation point, or just visually far but functionally adjacent (e.g., in a system prompt that is re-injected every turn).
4. **Base-model prior vs. specification gap are often confused.** If the default behavior matches common web text, it's a prior. If the default is a reasonable but unstated choice, it's a gap. The fix differs.
5. **Don't propose fixes that haven't been tested on this model.** Techniques that work on one model family may not transfer. Flag cross-model uncertainty when relevant.
6. **If the user edited the prompt after observing the output,** ask them to run the original prompt one more time before diagnosing. Diagnoses based on a prompt the model never actually saw are guesses.

---

## Output Format

```markdown
## Deviation confirmed
- **Instruction violated (verbatim):** "[...]"
- **Output passage that violates it (verbatim):** "[...]"
- **Is the violation crisp or ambiguous?** [crisp / ambiguous — if ambiguous, stop and explain]

## Primary cause
**[Category from taxonomy]**

[One paragraph: what specifically in the prompt (quoted) produced the deviation. If the cause is a base-model prior, name the prior and point to the absent override.]

## Contributing causes (if any)
- [Category]: [one line]

## Minimal fix
[Specific change to the prompt. Quote the before text and the after text.]

## Post-fix test
Re-run the prompt [N] times. You should see: [observable result].
If you do not see this, the diagnosis was wrong — re-run this diagnostic with the new output.

## Notes
- Model / version tested: [...]
- Cross-model uncertainty: [...]
- Re-run count before diagnosing: [...]
```

---

## Verification

- [ ] Actual prompt and actual output were provided and quoted.
- [ ] The violated instruction is stated as one sentence.
- [ ] A primary cause is named from the fixed taxonomy.
- [ ] The fix targets the named cause, not symptoms.
- [ ] The post-fix test is falsifiable.
- [ ] No fix is recommended larger than the diagnosis justifies.
