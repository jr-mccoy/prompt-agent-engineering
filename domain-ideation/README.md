# Domain: Ideation

Structured idea generation and idea selection. The twelve prompts in this domain cover the full divergence-convergence arc: techniques that force a wider, stranger idea space than your default frame produces (quantity pressure, time-boxes, inversion, random stimulus, persona shifts, analogy mining, constraint manipulation, reframing), and techniques that narrow the resulting list to something you can act on (dot-voting with weighted scoring, the kill-list).

The shared premise is that ideation quality is mostly a process problem, not a talent problem. The first handful of ideas anyone produces are median; groups anchor early; the inner editor censors the odd ideas where breakthroughs hide; and "brainstorming" without a separate convergence step produces lists nobody commits to. Each prompt attacks one specific failure mode and declares which it is for — most state explicitly whether they diverge or converge, and refuse to do the other.

Users are PMs, designers, founders, marketers, strategists, workshop facilitators, and individuals fighting a blank page or a rut. Every prompt works solo or with a group.

## When to use this domain

- You need many ideas fast and your defaults keep producing the same five.
- A brainstorm has gone stale — every new idea is a variant of an existing one.
- A group is anchoring early, being too polite, or recycling in-domain conventions.
- A brief is solution-shaped ("ideas for a meal-planning app") and you suspect the form is assumed, not validated.
- A divergence sprint produced 50–100 ideas and you need a defensible shortlist.
- An idea backlog has bloated with things nobody actually believes in and needs a cull.

## When NOT to use this domain (use a different one)

- **You're choosing among a few committed options, not narrowing an idea list** → `domain-decision-making/` (`tradeoff_multi_criteria_decision_analysis.md`, `tradeoff_pugh_matrix.md`).
- **You're validating a software/product idea toward building it** → `domain-idea-to-product/` (stage 1 there reuses several of these prompts, then adds the concept-legs test and downstream pipeline).
- **You want a structural reasoning move (first-principles, steelman, analogical inference) rather than an idea sprint** → `domain-reasoning-craft/reasoning-moves/`.
- **You want a fresh perspective on a decision already framed** → `domain-decision-making/decisioning_fresh_perspective_generator.md` or `decisioning_shift_fresh_latent_corner.md`.
- **You're hunting failure modes of a committed plan** → `domain-risk/` or `domain-prompt-engineering/evaluation/correctness_pre_mortem.md` (though `ideation_inverse_problem.md` overlaps as a generative pre-mortem).

## Prompts in this domain

### Divergence

| File | Purpose |
|------|---------|
| `ideation_forced_quantity_100_ideas.md` | Force 100 distinct ideas with no filtering; the surprising ones live in the 60–100 range |
| `ideation_crazy_eights.md` | 8 ideas in 8 minutes (scalable to 16/24); the clock starves the inner editor |
| `ideation_scamper.md` | Run an existing product/process through the seven SCAMPER transformation lenses (21–35 anchored variations) |
| `ideation_persona_what_would_x_do.md` | Generate from five reasoning lenses — contrarian, beginner, regulator, competitor, child |
| `ideation_random_stimulus.md` | Inject a random object/word/topic and force connections to break a rut |
| `ideation_cross_domain_analogy_mining.md` | Mine 3 deliberately-unrelated domains for transferable mechanisms, test the transfer, translate |
| `ideation_inverse_problem.md` | Invert the problem ("how would we guarantee NOT-X?") and translate the answers back |
| `ideation_worst_idea_first.md` | Generate 10–15 deliberately terrible ideas, then mine each for the usable kernel |
| `ideation_constraint_flip.md` | Drop one constraint / add one constraint to reopen an exhausted idea space |
| `ideation_jobs_to_be_done_reframe.md` | Reframe a solution-shaped brief around the job being hired for, then re-ideate per job |

### Convergence

| File | Purpose |
|------|---------|
| `ideation_idea_convergence_dot_voting.md` | Dot-vote, then weighted-score the survivors, to a defensible shortlist of 3–7 with rationale and dissent |
| `ideation_idea_kill_list.md` | Aggressively kill ~80% of a list with a named reason per death; defend the survivors |

## Quick routing

| You're saying | Use |
|---------------|-----|
| "I need a lot of ideas and keep stopping at five" | `ideation_forced_quantity_100_ideas.md` |
| "Warm up this workshop / I'm staring at a blank page" | `ideation_crazy_eights.md` |
| "I have a product/process and want variations on it" | `ideation_scamper.md` |
| "One perspective is dominating the ideation" | `ideation_persona_what_would_x_do.md` |
| "Every idea sounds the same — we're in a rut" | `ideation_random_stimulus.md` |
| "Our field hasn't solved this; what have other fields done?" | `ideation_cross_domain_analogy_mining.md` |
| "The direct framing isn't working" / "how would I make this fail?" | `ideation_inverse_problem.md` |
| "The group is too polite / self-censoring" | `ideation_worst_idea_first.md` |
| "The constraints feel like the problem" / "the brief is too loose" | `ideation_constraint_flip.md` |
| "The brief assumes the solution form ('ideas for an app')" | `ideation_jobs_to_be_done_reframe.md` |
| "We have 80 ideas and need 5, transparently" | `ideation_idea_convergence_dot_voting.md` |
| "We keep everything 'just in case' and commit to nothing" | `ideation_idea_kill_list.md` |

## How prompts in this domain compose

The canonical chain is **diverge → converge → hand off**. Start with a breadth tool sized to the situation: `forced_quantity_100_ideas` or `crazy_eights` for a blank page, `scamper` when you already have a thing, `jobs_to_be_done_reframe` when the brief itself is suspect. If the sprint stalls or every idea sounds the same, escalate to a pattern-breaker: `random_stimulus`, `worst_idea_first`, `persona_what_would_x_do`, `constraint_flip`, or `cross_domain_analogy_mining`. Then converge with `idea_convergence_dot_voting` (when you need comparative scoring) or `idea_kill_list` (when commitment is the bottleneck). The shortlist hands off outside the domain — to `domain-decision-making/` tradeoff prompts for a final choice, or to `domain-idea-to-product/` for validation and build.

`inverse_problem` doubles as a diagnostic: its failure-mode output can feed `domain-risk/` prompts or a pre-mortem rather than a convergence step.

## Frontmatter conventions specific to this domain

All prompts carry the repo-standard frontmatter plus a machine-readable `reasoning:` block (styles, stakes, horizon, uncertainty, output_format, user_role, mode). The load-bearing field here is `mode`: divergence prompts declare `mode: [diverge]` and convergence prompts `mode: [converge, decide]` — use it to keep the two phases separate when chaining programmatically. `evidence_quality` is typically `not_applicable` for pure divergence prompts (idea generation isn't evidence-weighted), and `stakes` is usually `low` to `moderate`: ideation is cheap by design, with the expensive judgment deferred to selection. `related_prompts` encodes the composition graph above.

## Companion domains

- `domain-idea-to-product/` — the pipeline downstream of ideation; its stage-1 directory carries copies of `forced_quantity_100_ideas`, `cross_domain_analogy_mining`, and `inverse_problem` plus the GO/KILL/RESHAPE concept-legs test.
- `domain-decision-making/` — convergence at higher stakes: `tradeoff_multi_criteria_decision_analysis.md` for committed options, `decisioning_fresh_perspective_generator.md` and `decisioning_shift_fresh_latent_corner.md` for perspective shifts on framed problems.
- `domain-reasoning-craft/reasoning-moves/` — the rigorous cousins of several techniques here (`reasoning_inversion.md`, `reasoning_analogical_inference.md`, `reasoning_steelman_construction.md`) when you want one careful move rather than an idea sprint.
- `domain-prompt-engineering/escape-median/` — escaping the model's default output, the prompt-engineering analogue of escaping your own median ideas.
