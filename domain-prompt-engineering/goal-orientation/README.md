# Goal Orientation & Intent

**Purpose:** Test whether the problem being handed to AI is the *right* problem, install the constraints and escalation triggers the task needs before the model runs, and audit team-level AI use for misalignment between stated goals and what the models are actually being asked to do. These prompts sit *before* prompt writing — they're about intent, not about phrasing.

**When to use this subfolder:**
- You're about to commit meaningful time, compute, or attention to an AI task and want to verify you're solving the right problem.
- You're designing a recurring AI workflow and need constraints, escalation triggers, and a value hierarchy installed up front rather than discovered in review.
- A team has accumulated AI workflows and you want to identify where operational behavior has drifted from stated purpose.

**When not to use:**
- A specific instruction in your prompt is being violated. Start with `model-behavior/`.
- You want committed, personalized output instead of balanced median output. Start with `escape-median/`.
- The task is exploratory ("see what happens when..."). These prompts assume goal-oriented work; exploration shouldn't be route-checked.

---

## Prompts

| File | Use when... |
|------|-------------|
| `goalorientation_right_problem_diagnostic.md` | Before writing or running the prompt, test whether the stated task actually maps to the outcome the user wants — surface assumption bridges, run the four-pattern checklist, ask the counterfactual, and produce proceed / reframe / stop. |
| `goalorientation_constraint_architecture_workshop.md` | Design session that produces three artifacts before the model runs: the constraint set, the escalation trigger set, and the value hierarchy. Stress-tests each against known failure modes. |
| `goalorientation_team_ai_misalignment_map.md` | Audit a team's live AI workflows for misalignment between stated goals and effective optimization. Produces a ranked priority list and specific interventions (tighten / verify / hand off / sunset / re-scope). |

---

## How the prompts chain

A typical progression for installing goal orientation into a serious AI workflow:

1. **Diagnose** whether the stated task is the right one (`goalorientation_right_problem_diagnostic.md`).
2. For workflows that pass diagnosis and will run repeatedly, **workshop** the constraints, escalation triggers, and value hierarchy (`goalorientation_constraint_architecture_workshop.md`).
3. Quarterly or after any AI incident, **audit** the team's whole AI surface (`goalorientation_team_ai_misalignment_map.md`).

For one-off, low-stakes tasks, just run step 1 — and only if the task costs enough review time downstream to justify the check.

---

## Design principles shared across these prompts

- **Separate task from outcome.** The stated task and the user's real intended outcome are almost always different. Every prompt in this subfolder forces the user to say both separately before proceeding.
- **Untested load-bearing assumptions are the fail state.** When the bridge between task and outcome rests on untested assumptions, no amount of prompt craft saves the workflow. These prompts force the assumptions into view.
- **Constraints, triggers, and hierarchy are three different things.** Users conflate them. These prompts keep them separate because they do different work — constraints govern output, triggers govern escalation, hierarchy governs conflict resolution.
- **Evidence before design.** The team-level audit refuses to run on a hypothetical inventory. The constraint workshop refuses to run without a named failure mode. Real material, real output.
- **Predict the uncovered risks.** Every prompt ends by naming what it did *not* address, so the user doesn't confuse coverage with completeness.

---

## Related

- `domain-prompt-engineering/model-behavior/` — for fixing how the model behaves *after* you've verified you're asking the right thing.
- `domain-prompt-engineering/escape-median/` — for personalizing the output *after* you've verified the question.
- `domain-prompt-engineering/delegation/delegation_intent_specification.md` — for spec-writing when the task passes diagnosis and needs a formal brief for a colleague or a sub-agent.
- `domain-business-strategy/chief-of-staff/cos_clarify_fuzzy_goals.md` — related upstream work: turning fuzzy personal goals into actionable intent before any AI task is framed.
- `domain-personal-development/prompts/agency/agency_project_ownership_converter.md` — related upstream work at the project ownership level.
- `domain-business-strategy/ai-strategy/aistrategy_context_accumulation_map.md` — companion at the org / enterprise level when the team audit is part of a broader AI strategy conversation.
- `domain-engineering-workflows/ai-patterns/ai_pattern_intent_and_verification_first.md` — companion pattern in engineering workflows: write task intent and verification criteria before starting.
