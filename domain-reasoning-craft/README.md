# Reasoning Craft

Domain-general reasoning tools: prompts that execute a single, named reasoning move with discipline, rather than solving a particular subject-matter problem. Where most domains in this repository are organized by *what you're working on* (a codebase, a custody case, a lesson plan), this domain is organized by *how you're thinking* — making an inference, scoring a forecast, mapping a feedback structure, or auditing your own epistemics. The prompts are deliberately content-agnostic: the same Bayesian update or causal loop diagram works on a product decision, a policy question, or a personal one.

The domain exists because these moves are easy to name and hard to run honestly. Everyone "considers the base rate" and "steelmans the other side"; almost nobody seals the inside view before building the reference class, or writes down what evidence would actually move them before the evidence arrives. Each prompt operationalizes one move end-to-end — inputs, steps, output format, verification — with a False-Positive Prevention section targeting the specific ways that move degenerates into theater.

Users are anyone making consequential judgments under uncertainty: operators, analysts, researchers, policy staff, founders, and individuals working through hard calls one-on-one with an AI.

## When to use this domain

- You want to run a specific named reasoning technique: a Fermi estimate, a reference-class forecast, a Toulmin map, an inversion, a dialectical synthesis.
- You're making or scoring forecasts and want calibration discipline: well-formed questions, decomposition, base rates, Brier tracking, pre-committed tripwires.
- A problem keeps coming back after being "fixed," oscillates, or escalates — feedback structure, not point causes, is the issue.
- You suspect your own conclusion: you want evidence against yourself, a motivated-reasoning check, a named-bias audit, or a red-team brief before shipping a position.
- You're evaluating someone else's argument or evidence: claim/evidence/warrant separation, fallacy scan, source triangulation, evidence-quality scoring.

## When NOT to use this domain (use a different one)

- You need a *decision made*, not a reasoning move executed — option comparison, scenario planning, decision memos → `domain-decision-making/` (`tradeoff_*`, `scenario_*`, `documentation/`).
- You need *more ideas*, not better evaluation of existing ones → `domain-ideation/`.
- You need an operational risk artifact (register, FMEA, heat map) rather than risk *reasoning* → `domain-risk/`.
- You're working a multi-phase hard problem end-to-end with a facilitator → `domain-deep-analysis/` (`/deepthink-*`); those systems *use* these moves as components.
- The judgment is a research task over sources and literature → `domain-research-academic/`.
- Quick gut-check on a single decision ("am I being nuts?") → `domain-productivity/validation/`.
- The subject is influence itself — propaganda technique in a specific artifact, a suspected coordinated campaign, or manipulation aimed at you → `domain-psy-ops/`. That domain applies these epistemic moves to a specific subject matter; the general-purpose versions (fallacy scan, source triangulation, evidence quality, red-teaming) stay here.

## Subdirectory map

| Subdirectory | What it covers | Prompts |
|---|---|---|
| `reasoning-moves/` | Single named inference moves: abduction, analogy, Bayesian update, counterfactuals, Fermi, first principles, inversion, steelman, synthesis, argument/premise/warrant audits, reference-class and outside-view forecasting | 14 |
| `forecasting/` | The forecasting practice loop: question design, decomposition, base rates, scenario probabilities, signal triage, tripwires, calibration audit, Brier log design, radical long-horizon uncertainty | 9 |
| `systems/` | Systems thinking: feedback loops, causal loop diagrams, stocks and flows, archetypes, dependency maps, leverage points, unintended consequences, intervention pre-mortems | 8 |
| `epistemic/` | Self- and source-directed epistemics: bias audits, motivated reasoning, evidence against yourself, red-teaming, fallacy scans, claim/inference separation, source credibility, evidence quality, uncertainty calibration in writing, disagreement diagnosis | 10 |

## Prompts in this domain

### reasoning-moves/

| File | Purpose |
|------|---------|
| `reasoning_abductive_inference.md` | Generate and score competing explanations for a surprising observation; pick the discriminating test |
| `reasoning_analogical_inference.md` | Predict via structural analogy with explicit mapping and disanalogy testing |
| `reasoning_argument_map_toulmin.md` | Map an argument into Toulmin's six components; surface unstated warrants |
| `reasoning_bayesian_belief_update.md` | Walk prior → likelihood ratio → posterior transparently for one piece of evidence |
| `reasoning_claim_evidence_warrant_audit.md` | Extract claims, evidence, and the unstated bridges in persuasive prose |
| `reasoning_counterfactual_analysis.md` | Build a disciplined what-if: minimal antecedent change, world held fixed, chain traced |
| `reasoning_dialectical_synthesis.md` | Strongest thesis, strongest antithesis, genuine synthesis (not compromise) |
| `reasoning_fermi_estimation.md` | Order-of-magnitude estimate via 3–6 factor decomposition with confidence bands |
| `reasoning_first_principles_reconstruction.md` | Decompose a belief/design to atomic claims; rebuild from what survives |
| `reasoning_inversion.md` | Flip "achieve X" into "guarantee NOT-X"; harvest the anti-goals |
| `reasoning_outside_view_inside_view.md` | Seal the inside view, build the outside view blind, then reconcile the gap |
| `reasoning_premise_audit.md` | Extract and independently test the premises (factual/value/methodological) an argument stands on |
| `reasoning_reference_class_forecast.md` | Pick a reference class, derive its base rate, adjust with explicit case-specific deltas |
| `reasoning_steelman_construction.md` | Build the strongest version of the opposing position before responding |

### forecasting/

| File | Purpose |
|------|---------|
| `forecasting_probabilistic_question_design.md` | Convert fuzzy claims into resolvable forecast questions (resolver, threshold, date) |
| `forecasting_super_forecaster_decomposition.md` | Decompose a forecast into estimable sub-questions and recombine |
| `forecasting_base_rate_establishment.md` | Establish the event class's historical base rate before case-specific reasoning |
| `forecasting_scenario_probability_assignment.md` | Assign probabilities summing to 1.0 across a scenario set plus an unforeseen reserve |
| `forecasting_signal_vs_noise_filter.md` | Triage incoming information against an existing forecast: signal, direction, magnitude |
| `forecasting_what_would_change_my_mind.md` | Pre-commit observable tripwires that would move your belief by stated amounts |
| `forecasting_calibration_self_audit.md` | Score a log of past predictions by probability bin; diagnose over/underconfidence |
| `forecasting_brier_tracker_design.md` | Design a personal forecasting log: fields, cadence, metrics, action rules |
| `forecasting_long_horizon_radical_uncertainty.md` | Robust postures (hedge/commit/optionality) when base rates don't exist |

### systems/

| File | Purpose |
|------|---------|
| `systems_feedback_loop_identifier.md` | Extract closed loops from a situation; sign each R or B |
| `systems_causal_loop_diagram.md` | Full CLD: variables, signed links, loops, delays, external drivers |
| `systems_stock_and_flow_model.md` | Stocks, flows, delays — and the behavior-over-time the structure produces |
| `systems_archetype_recognition.md` | Match a situation to a named archetype with element-by-element fit testing |
| `systems_dependency_map.md` | Topological dependency map: SPOFs, fan-in hubs, circular dependencies |
| `systems_leverage_point_analysis.md` | Place interventions on Meadows' leverage hierarchy; find higher-leverage alternatives |
| `systems_unintended_consequence_scan.md` | Second/third-order effects across actors × time horizons; Goodhart audit |
| `systems_intervention_pre_mortem.md` | Structure-aware pre-mortem: which loops absorb, which actors push back |

### epistemic/

| File | Purpose |
|------|---------|
| `epistemic_bias_specific_audit.md` | Audit a conclusion against one named cognitive bias with its specific signature |
| `epistemic_claim_inference_separator.md` | Tag a passage sentence-by-sentence: observation, claim, or inference |
| `epistemic_disagreement_diagnosis.md` | Locate a stuck disagreement's layer: empirical, definitional, values, or trust |
| `epistemic_evidence_against_yourself.md` | Generate the strongest evidence against your own position |
| `epistemic_evidence_quality_score.md` | Score one piece of evidence on a transparent multi-criterion rubric |
| `epistemic_logical_fallacy_scan.md` | Scan text against ~15 named fallacies; quote-or-don't-flag discipline |
| `epistemic_motivated_reasoning_check.md` | Asymmetric-standards test: would you accept this evidence if it cut the other way? |
| `epistemic_red_team_briefing.md` | Construct the most credible critic and their strongest attack before you ship |
| `epistemic_source_credibility_triangulation.md` | Compare 3+ sources on credibility dimensions; audit independence vs. echo |
| `epistemic_uncertainty_acknowledgment_audit.md` | Flag every claim whose stated certainty exceeds its evidence |

## How prompts in this domain compose

The forecasting subdirectory is a practice loop: `forecasting_probabilistic_question_design` → `forecasting_base_rate_establishment` (or `reasoning_reference_class_forecast` when case adjustments are needed) → `forecasting_super_forecaster_decomposition` → `forecasting_what_would_change_my_mind` → log per `forecasting_brier_tracker_design` → periodically `forecasting_calibration_self_audit`. The systems set chains from recognition to action: `systems_feedback_loop_identifier` or `systems_causal_loop_diagram` → `systems_archetype_recognition` → `systems_leverage_point_analysis` → `systems_intervention_pre_mortem` and `systems_unintended_consequence_scan` before shipping the intervention. Epistemic prompts typically run as gates on work produced elsewhere: draft → `epistemic_uncertainty_acknowledgment_audit` → `epistemic_evidence_against_yourself` → `epistemic_red_team_briefing`. Reasoning-moves prompts are single tools, composable anywhere; their frontmatter `related_prompts` record the tested pairings.

## Frontmatter conventions specific to this domain

Every prompt carries a machine-readable `reasoning:` block in frontmatter in addition to the standard fields:

```yaml
reasoning:
  styles: [bayesian, causal, ...]   # which reasoning styles the prompt exercises
  stakes: variable                  # what stakes level it's built for
  horizon: months_to_years          # the time horizon of the judgment
  uncertainty: deep                 # the uncertainty regime
  evidence_quality: variable
  domain_complexity: cross_domain
  collaboration: solo_or_team
  output_format: ...                # the artifact shape the prompt locks
  user_role: [analyst, founder, ...]
  mode: [audit, forecast, diagnose] # the prompt's operating mode(s)
```

This block is indexed in `PROMPT_INDEX.json`, so prompts can be selected programmatically by reasoning style, stakes, horizon, or mode. Mutual demarcation is also a domain convention: prompts that overlap (e.g., reference-class vs. outside-view, evidence-against-yourself vs. red-team vs. motivated-reasoning) name each other in "When NOT to use" and route explicitly.

## Companion domains

- `domain-decision-making/` — the decision layer these moves feed: `scenario_*` planning, `tradeoff_*` comparison, `documentation/` decision records.
- `domain-risk/` — operational risk artifacts; `risk_tail_risk_scan` and `risk_dependency_chain_audit` pair naturally with `systems_dependency_map` and the forecasting set.
- `domain-ideation/` — divergence before these prompts' convergence and evaluation.
- `domain-research-academic/` — evidence gathering and synthesis upstream of `epistemic_*` evidence evaluation.
- `domain-deep-analysis/` — facilitated multi-phase systems that embed many of these moves.
- `domain-prompt-engineering/evaluation/` — correctness and eval design for AI outputs specifically (`correctness_pre_mortem`, eval harnesses).
