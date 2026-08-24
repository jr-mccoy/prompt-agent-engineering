# Escaping Default Output

**Purpose:** Move the model off its *median position* on a topic or its *median shape* of output, toward answers that reflect the user's specific situation, prior, and preferences. These prompts treat the model's default output as the thing to push against, not the thing to accept.

**When to use this subfolder:**
- You keep getting balanced, plausible, mildly useful AI output, and you want committed, opinionated, personalized output instead.
- You've been correcting the same things across sessions and want the corrections to stop being ad-hoc.
- You're ready to build a persistent instruction file (CLAUDE.md, custom instructions) from evidence rather than from a blank page of guesses.

**When not to use:**
- A specific instruction in your prompt is being violated by the model. That's `model-behavior/` — diagnose the violation, don't blame the median.
- You don't have a prior yet. Sharpening a prompt without a real user prior just produces a differently-shaped median. Go to `goal-orientation/` to clarify intent first.
- You're uncertain whether the task belongs to AI at all. Again, start with `goal-orientation/`.

---

## Prompts

| File | Use when... |
|------|-------------|
| `escapemedian_default_position_mapper.md` | Before asking for judgment on a topic, probe the model's default stance so you know what you're pushing against. |
| `escapemedian_instruction_sharpener.md` | Rewrite a vague instruction into one the model can't satisfy with median output — make the prior explicit, forbid the default, forbid the hedges, narrow the form. |
| `escapemedian_correction_compounder.md` | You've been making the same kinds of corrections in a session; extract the pattern into a compact rule block the model will actually follow for the rest of the session. |
| `escapemedian_bootstrap_instruction_file.md` | You have enough evidence (corrections, default maps) to draft a first-pass personal instruction file from observed preferences — not aspirational ones. |

---

## How the prompts chain

A typical progression for a user moving from generic AI output to high-signal personal output:

1. **Map** the model's default on a topic you care about (`escapemedian_default_position_mapper.md`).
2. **Sharpen** the first prompt on that topic so the model can't default (`escapemedian_instruction_sharpener.md`).
3. **Compound** the corrections you accumulate across that session into session-level rules (`escapemedian_correction_compounder.md`).
4. After ~2–3 sessions, **bootstrap** those rules and maps into a persistent instruction file (`escapemedian_bootstrap_instruction_file.md`).

Skipping steps is common and expensive: bootstrapping a file without evidence produces aspirational preferences; sharpening without a prior produces a different median.

---

## Design principles shared across these prompts

- **Evidence before design.** Each prompt requires real inputs — actual default output, actual corrections, actual priors. They refuse to run on imagined preferences.
- **Testable rules.** Every rule the prompts produce is stated so a single output can be judged against it. Rules the model can't check don't belong.
- **Name the default you're overriding.** Negative instructions without a named target or a positive replacement backfire. Every forbidden default gets both.
- **Scope is a feature.** Rules are tagged session-only, task-scoped, or general. Rules promoted at the wrong scope either over-apply or disappear.
- **The user's voice, not the model's.** Instruction files and rule blocks live longest when they're written in the user's own correction language, not in model-polished prose.

---

## Related

- `domain-prompt-engineering/model-behavior/` — for *instruction-level* behavior deviations (different failure mode).
- `domain-prompt-engineering/goal-orientation/` — for deciding whether you're asking the right question at all.
- `domain-business-strategy/chief-of-staff/cos_memory_scaffold_claude_md.md` — broader CLAUDE.md scaffold that covers role, priorities, authority boundaries on top of the preference rules produced here.
- `domain-engineering-workflows/ai-patterns/ai_pattern_rule_extraction_from_decisions.md` — for extracting rules from engineering decisions rather than model corrections.
