# Thinking Prompts

Cognition tools — the second axis alongside agency (action) and identity (self). Where agency prompts get you *moving* and identity prompts ask *who you are*, these prompts sharpen *how you think*: questioning, reframing, perspective-taking, structured analysis, and memory.

These prompts assume the user brings a real, specific subject — a decision, a belief, a topic, a passage, a list — and is willing to engage with their own thinking rather than receive a finished answer. Several of them deliberately *withhold* answers (the questioning tools) or *refuse to act* on inputs that are too vague to ground real work.

## Scope

**In scope:**
- Question-first exploration (surface unknowns before answering)
- Reframing limiting beliefs into evidence-based alternatives
- Generating unconventional perspectives on a stuck challenge
- Identifying personal blind spots with falsifiable experiments
- Future-self / regret-minimization reasoning for major decisions
- Disciplined analysis under tight, explicit constraints
- Plain-language translation that preserves the truth
- Spatial memory construction (method of loci)
- Calibrating your own judgment via a decision journal (record → predict → score)
- Applying fitting mental models to one live personal problem
- Surfacing and testing the load-bearing assumptions under a plan or belief

**Out of scope (route elsewhere):**
- Getting unstuck and into motion → `../agency/` (esp. `agency_stuck_diagnosis.md`, `agency_next_action_spec.md`)
- Values, self-talk, comparison, purpose, confidence → `../identity/`
- Clinical mental health (persistent hopelessness, self-harm, eating disorders, addiction) → professional support; the reframer screens for this and refers out rather than reframing it
- Generic content-area reasoning moves (Bayes, Fermi, steelman, systems, epistemics) → `domain-reasoning-craft/` (see boundary note below)
- Meta-work on prompts themselves (improving prompts, escaping default output) → `domain-prompt-engineering/`

## Sub-groupings

**Questioning tools** — generate questions, withhold answers, synthesize after the user responds:
- `thinking_interrogative_mode.md`
- `thinking_question_generator_mode.md`

**Reframing tools** — shift how an existing belief or framing is held:
- `thinking_mindset_shift_reframe.md`
- `thinking_fresh_perspective_generator.md`

**Perspective-taking / decision tools** — see the situation from outside the present moment:
- `thinking_regret_minimization.md`
- `thinking_blind_spot_mirror_see_what_im_missing.md`
- `thinking_decision_journal_designer.md`

**Structured problem tools** — put a fixed method against one live problem, plan, or belief:
- `thinking_mental_models_application.md`
- `thinking_assumption_surfacing.md`

**Analysis & communication tools** — produce rigorous or maximally clear output:
- `thinking_tight_constraint_topic_analyzer.md`
- `thinking_explain_like_im_nine_converter.md`

**Memory tools** — encode information for reliable recall:
- `thinking_memory_palace_generator.md`

## File map

| Prompt | Purpose |
|---|---|
| `thinking_interrogative_mode.md` | Generate 10–12 open-ended questions that surface unknowns; no answers until the user responds, then synthesize patterns. |
| `thinking_question_generator_mode.md` | Sibling of interrogative mode; 10–12 strategic questions across five dimensions, then theme synthesis. |
| `thinking_mindset_shift_reframe.md` | Turn one stated limiting belief into an evidence-based alternative with a 48-hour micro-experiment; screens out real risks and clinical signals. |
| `thinking_fresh_perspective_generator.md` | Produce 3 perspectives (practical → radical) on a stuck challenge, each with story, metaphor, action; one questions the premise. |
| `thinking_regret_minimization.md` | Consult future-self across 1-year / 5-year / end-of-life horizons; map regret of action vs. inaction; recommend without commanding. |
| `thinking_blind_spot_mirror_see_what_im_missing.md` | Identify 3–5 evidence-grounded blind spots, each with a falsifiable 1-week experiment and a sequenced action plan. |
| `thinking_decision_journal_designer.md` | Design a lightweight decision journal (decision + prediction + confidence) and a scoring review, so the user calibrates which of their own calls are reliable. |
| `thinking_mental_models_application.md` | Classify a live problem's structure, apply the 2–3 mental models that fit, and converge on the one insight that changes the next move. |
| `thinking_assumption_surfacing.md` | Surface 6–10 hidden assumptions under a plan/belief, rank by load-bearing × uncertainty, and decide what to verify before proceeding. |
| `thinking_tight_constraint_topic_analyzer.md` | Deep analysis under explicit constraints (word limit, perspective, frameworks, sources, forbidden words) with an honest constraint audit. |
| `thinking_explain_like_im_nine_converter.md` | Rewrite jargon-heavy text to nine-year-old clarity while preserving every claim, hedge, and limit; audits for accuracy loss. |
| `thinking_memory_palace_generator.md` | Build a method-of-loci memory palace from a user's list and a familiar space, with vivid associations and a spaced-practice schedule. |

## Composition patterns

These prompts chain naturally. Common sequences:

- **Explore → analyze:** `thinking_interrogative_mode` (or `thinking_question_generator_mode`) surfaces the unknowns → `thinking_tight_constraint_topic_analyzer` produces the disciplined analysis once the terrain is mapped.
- **Stuck-challenge route:** `thinking_blind_spot_mirror` reveals what you're not seeing → `thinking_fresh_perspective_generator` reframes it → if a belief is the blocker, `thinking_mindset_shift_reframe`.
- **Major-decision route:** `thinking_blind_spot_mirror` → `thinking_mindset_shift_reframe` (clear any belief blocking the choice) → `thinking_regret_minimization` to commit.
- **Cross-axis handoff:** when "I'm stuck" turns out to be inaction rather than confused thinking, route to `../agency/agency_stuck_diagnosis.md`; when it turns out to be a values or purpose question, route to `../identity/`.
- **Communicate the output:** any analysis above → `thinking_explain_like_im_nine_converter` to make it land with a non-expert audience without distorting it.

## What the prompts refuse

- Answering their own questions (the questioning tools wait for the user)
- Positive-thinking platitudes and toxic affirmations (the reframer demands evidence)
- Manufacturing blind spots, options, or perspectives from inputs too thin to ground them
- Pathologizing normal preferences or dismissing protective concerns as "limiting beliefs"
- Commanding a decision (regret minimization presents analysis, not orders)
- Silently violating a declared constraint to make the output fit
- Distorting a claim, hedge, or limit in the name of "simplifying"

## Boundary note: overlap with reasoning-craft and prompt-engineering

`thinking/` overlaps conceptually with two other domains. Keep them distinct; cross-link rather than duplicate.

- **`domain-reasoning-craft/`** holds *content-agnostic, named reasoning moves* (Bayesian update, Fermi estimation, reference-class forecast, steelman, inversion, systems archetypes, epistemic audits) carrying machine-readable `reasoning:` frontmatter. `thinking/` prompts are *personal-development-flavored cognition tools* — applied to the user's own life, decisions, and beliefs, with first-person framing and self-experiments. If a user wants a rigorous, reusable inference move on any subject, route to `domain-reasoning-craft/`; if they want to think more clearly about *their own* situation, stay here.
- **`domain-prompt-engineering/`** is *meta-work on prompts and model behavior* (improving prompts, diagnosing instruction deviation, escaping default output). `thinking/` is about the *user's* thinking, not the prompt's construction. Route prompt-improvement requests there.
