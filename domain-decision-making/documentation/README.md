# Decision Documentation

Decision-record formats: the artifacts that capture a decision's reasoning so it can be communicated, audited, and learned from. These are documentation prompts, not deliberation prompts — the thinking happens upstream (with the parent domain's tradeoff, scenario, and decisioning prompts, or `domain-deep-analysis/deepthink_decision.md`); these prompts give the worked-through position a durable, predictable shape. Each format states explicitly that it communicates a decision rather than makes one.

The six formats cover the decision lifecycle at every weight class. At decision time: the **options memo** (rigid structure, 2–4 options, named objections, revisit conditions), the **narrative six-pager** (prose plus mandatory FAQ, for senior rooms that read silently and then interrogate), the **one-pager** (the entire decision in 60 seconds for a principal who reads nothing else), and the **log entry** (lightweight, append-only, uniform — institutional memory at volume). After the fact: the **post-decision review** (calibration against the predictions you actually recorded) and the **after-action report** (decision quality separated from outcome quality, lessons tagged for retrieval).

Users are PMs, executives, founders, managers, consultants, analysts, and individuals whose decisions need to survive scrutiny by people who weren't in the room — including their own future selves.

## When to use this domain

- A decision is being made, or has been made, and stakeholders, posterity, or an audit trail need the reasoning captured.
- A pre-read is needed: align a team or brief a principal before the meeting instead of presenting in it.
- A team or individual maintains a running decision log (markdown, ADR directory, Notion) and needs uniform entries captured before motivated reconstruction sets in.
- A pre-committed checkpoint has arrived (6 months after the hire, a year after the bet) and the outcome should be compared to what was actually predicted.
- A decision or initiative has concluded and you want transferable lessons — without canonizing luck or scapegoating a sound decision that drew a bad outcome.
- A personal high-stakes decision where you want the reasoning locked in before hindsight rewrites it.

## When NOT to use this domain (use a different one)

- **You're still making the decision** → parent-domain deliberation prompts (`tradeoff_multi_criteria_decision_analysis.md`, `tradeoff_reversibility_stakes_grid.md`, scenario prompts) or `domain-deep-analysis/deepthink_decision.md`.
- **The subject is a public-policy choice** → `domain-policy/policy_options_memo.md` (adds equity, political viability, and values-tradeoff requirements).
- **The completed event is a risk event or incident, not a decision** → `domain-risk/risk_after_action_review.md`.
- **You want a personal regret analysis of a past decision** → `domain-personal-development/prompts/agency/agency_decision_post_mortem.md`.
- **The decision is too small to document** — the log entry is the floor; below that, don't.

## Prompts in this domain

| File | Purpose |
|------|---------|
| `decisiondoc_options_memo.md` | 2–4 options against shared criteria, recommendation with reasoning, strongest objections named, revisit conditions specified |
| `decisiondoc_narrative_memo_bezos.md` | Amazon-style six-pager: prose that can't hide gaps behind bullets, plus a mandatory FAQ that pre-answers the skeptical room |
| `decisiondoc_one_pager.md` | The whole decision on one standalone page: ask, recommendation, top reason, top risk, decider, deadline |
| `decisiondoc_log_entry.md` | Append-only log entry (decision, context, rationale, alternatives, decider, status) with an upgrade rule to the full memo |
| `decisiondoc_post_decision_review.md` | At a pre-committed checkpoint, compare actual outcomes to recorded predictions; extract calibration lessons by decision type |
| `decisiondoc_after_action_report.md` | Decision quality vs. outcome quality 2×2 for any completed initiative; lessons attach to process and are tagged for retrieval |

## Choosing the format

| Situation | Format |
|-----------|--------|
| Steady stream of small-to-medium decisions; want a searchable record | `decisiondoc_log_entry.md` |
| Significant decision; stakeholders need auditable structure and named dissent | `decisiondoc_options_memo.md` |
| High-stakes, contested; senior room will read silently and push hard | `decisiondoc_narrative_memo_bezos.md` |
| The decider reads one page, period | `decisiondoc_one_pager.md` |
| Checkpoint arrived; predictions were recorded at decision time | `decisiondoc_post_decision_review.md` |
| Initiative concluded; want lessons that survive the luck of the outcome | `decisiondoc_after_action_report.md` |

The log entry carries an explicit upgrade rule: when an entry's stakes or contestedness outgrow the format, write the options memo instead. The one-pager stacks on top of either memo as a cover sheet but must still stand alone.

## How prompts in this domain compose

The lifecycle chain: **decide upstream → document → review later.** Deliberate with the parent domain's prompts, then pick the at-decision format by weight and audience — log entry for the steady stream of small-to-medium calls (with its built-in upgrade rule to the options memo when stakes or contestedness demand it), options memo for significant decisions needing auditable structure, narrative memo for contested high-stakes decisions facing a hostile read, one-pager standalone or stacked on top of either memo as the principal's cover sheet. The memo or log entry should record predictions and a review date, because both retrospective instruments depend on it: `decisiondoc_post_decision_review.md` calibrates against those recorded forecasts at the checkpoint, and `decisiondoc_after_action_report.md` asks whether the decision was sound given what was knowable — the complementary pair (calibration vs. transferable lessons). The post-decision review's `related_prompts` also point at `domain-reasoning-craft/reasoning-moves/reasoning_bayesian_belief_update.md` for the update mechanics.

## Frontmatter conventions specific to this domain

All prompts carry the machine-readable `reasoning:` block. `mode` always includes `document`, which distinguishes these from the parent domain's deliberation prompts (`decide`, `audit`). The formats are differentiated by `output_format` (`structured_memo`, `narrative`, `structured`) and by stakes/collaboration profile: the one-pager and narrative memo are typed `collaboration: org` (artifacts for a room), the log entry is `stakes: low` by design, and the retrospective pair runs `retrospective` / `calibration` / `counterfactual` styles. `difficulty` tracks craft burden — `beginner` for log entry and one-pager, `advanced` only for the narrative memo, where the prose is the discipline.

## Companion domains

- `domain-decision-making/` (parent) — the deliberation that precedes these artifacts: tradeoff, scenario, and decisioning prompts.
- `domain-policy/` — the public-policy specialization of the options memo.
- `domain-risk/` — `risk_after_action_review.md` for materialized risk events; register entries cross-reference decision records.
- `domain-personal-development/major-decisions/` — personal high-stakes decisions whose prompts recommend documenting with the options memo here.
- `domain-reasoning-craft/forecasting/` and `reasoning-moves/` — calibration tooling (Brier tracking, Bayesian updating) that makes the post-decision review's predicted-vs-actual comparison rigorous.
- `domain-engineering-workflows/workflows/` — engineering post-mortems (`engineering_post_mortem_root_cause_ladder.md`) when the completed event is an engineering incident.
