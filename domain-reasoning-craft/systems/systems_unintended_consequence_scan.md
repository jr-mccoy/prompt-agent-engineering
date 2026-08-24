---
title: "Unintended Consequence Scan — Second- and Third-Order Effects of a Proposed Change"
category: reasoning-craft/systems
description: "For a proposed intervention or change, systematically scan for second- and third-order effects across affected actors, time horizons, and adjacent systems. Identifies behavior changes, incentive shifts, displacement effects, gaming, and rebound dynamics that direct first-order analysis misses."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - DS-02
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - systems-thinking
  - second-order-effects
  - unintended-consequences
  - intervention-design
  - pre-mortem
updated: "2026-05-10"
reasoning:
  styles: [systems, causal, scenario, adversarial]
  stakes: variable
  horizon: months_to_years
  uncertainty: deep
  evidence_quality: variable
  domain_complexity: cross_domain
  collaboration: solo_or_team
  output_format: matrix_of_actors_x_horizons
  user_role: [executive, policy, founder, pm, operator, designer]
  mode: [audit, forecast, diagnose]
related_prompts:
  - domain-reasoning-craft/systems/systems_causal_loop_diagram.md
  - domain-reasoning-craft/systems/systems_intervention_pre_mortem.md
  - domain-reasoning-craft/reasoning-moves/reasoning_counterfactual_analysis.md
  - domain-prompt-engineering/evaluation/correctness_pre_mortem.md
---

# Unintended Consequence Scan

**Objective:** For a proposed intervention or change, systematically map the second- and third-order effects across affected actors, time horizons, and adjacent systems. Surface behavior changes, incentive shifts, displacement effects, gaming responses, and rebound dynamics that direct first-order analysis misses. Produce a matrix the team can use to either redesign the intervention, add monitoring, or accept the risks knowingly.

**When to use:**
- A proposed policy, product change, pricing change, organizational change, or technical change is about to be deployed.
- The change affects actors with their own goals (employees, users, customers, regulators, competitors), so behavioral responses are likely.
- A prior similar intervention failed in unexpected ways and the team wants to avoid the same trap.
- Designing incentives where Goodhart's Law is likely to bite.

**When NOT to use:**
- The change is purely internal-mechanism with no behavioral surface (e.g., refactoring backend code that no actor responds to). First-order analysis suffices.
- The change is a small experiment whose unintended consequences would be cheap to discover and reverse.
- Time pressure prohibits a 30–60 minute analysis.
- The system's feedback structure is already mapped and you want structure-aware failure tracing (loops, delays, archetype triggers) — use `systems_intervention_pre_mortem.md` instead.

**Audience:** Executives, policy designers, founders, PMs, operators, anyone shipping changes that touch actors with their own incentives.

---

## Inputs / Context

1. **The proposed intervention.** What's being changed, by whom, when, with what mechanism. One paragraph.
2. **First-order intent.** What the intervention is supposed to do, in terms of measurable outcomes.
3. **Affected actors.** All groups whose behavior or outcomes the intervention touches. Include obvious and adjacent ones (competitors, regulators, downstream consumers, employees of affected businesses).
4. **Time horizons.** Immediate (<1 week), short-term (1–12 weeks), medium (3–18 months), long (18+ months). Different consequences emerge at different scales.
5. **Comparable past interventions.** Same domain or analogous; what unintended effects appeared.
6. **Reversibility.** If unintended consequences emerge, can the intervention be rolled back? At what cost?

---

## Constraints

### Must
- Build a matrix with **actors on one axis** and **time horizons on the other**. Every cell should be considered, even if the conclusion is "no significant effect expected."
- For each consequence, classify type:
  - **Behavioral response** (actor changes what they do)
  - **Incentive shift** (the change reshapes the rewards/punishments structure)
  - **Displacement** (problem moves elsewhere rather than disappearing)
  - **Gaming** (actor optimizes for the metric rather than the underlying goal — Goodhart)
  - **Rebound** (initial improvement triggers compensating behavior that erodes it)
  - **Spillover** (effect extends to actors not the intervention's target)
  - **Norm shift** (the change affects what's considered normal/acceptable)
- For each significant consequence, estimate likelihood (low/med/high) and severity (low/med/high).
- Identify monitoring observables: what would tell you each consequence is materializing?
- For high-severity, high-likelihood consequences: either redesign, add mitigations, add monitoring with rollback triggers, or accept knowingly.

### Must Not
- Stop at first-order effects. The whole point is the second and third order.
- Fall back on "we'll cross that bridge when we get to it." For high-stakes interventions, the bridge is often invisible until you're under it.
- Treat actors as static. Smart actors with skin in the game adapt; the model must include their adaptation.
- Pretend "we considered it and decided not to worry" without naming why. Document the decision so post-mortems can audit it.
- Confuse desired second-order effects (often the actual point) with unintended ones. Separate them in the output.

---

## Instructions

### Step 1 — Restate intervention and intent
Write the intervention, its mechanism, and the first-order outcome it's supposed to produce. One paragraph. List any *desired* second-order effects separately — these are intended and must not be mixed into the unintended-consequence matrix.

### Step 2 — Enumerate actors
List all actors. Push beyond the obvious:
- Direct targets
- Direct targets' counterparts (employees ↔ managers; customers ↔ vendors; users ↔ moderators)
- Adjacent actors not directly targeted but affected (competitors, regulators, suppliers)
- Actors whose behavior gates the intervention's success (gatekeepers, channel partners)

### Step 3 — Enumerate time horizons
- Immediate: hours to days. Often: protest, gaming, attempts to circumvent.
- Short: 1–12 weeks. Behavioral adaptation, workarounds.
- Medium: 3–18 months. Equilibrium shifts, organizational responses, regulatory attention.
- Long: 18+ months. Norm shifts, structural reorganization, market entry/exit.

### Step 4 — Walk the matrix
Before walking the cells, seed the scan from the comparable past interventions (Input 5): list the unintended effects that appeared in analogous cases and check each one against this intervention. Then, for each (actor × horizon) cell, ask:
- What does this actor do differently because of the intervention?
- What incentive does this create or reshape?
- What can they do to avoid the intervention's effect on them?
- What can they game?
- Does the intervention displace cost / risk / friction onto them?
- Does the intervention shift what's considered normal in their domain?

Capture each significant effect.

### Step 5 — Classify and rank
For each consequence:
- Type (behavioral / incentive / displacement / gaming / rebound / spillover / norm shift)
- Likelihood: low / med / high
- Severity: low / med / high
- Reversibility of the consequence itself: easy / moderate / hard

Rank by likelihood × severity.

### Step 6 — Monitoring observables
For each high-priority consequence, name an observable that would signal it's materializing. The observable must be:
- Measurable
- Trackable on a defined cadence
- Linked to a pre-committed response (mitigation / rollback / acceptance)

### Step 7 — Goodhart audit
For any metric the intervention rewards or punishes, explicitly ask: how would an actor optimize for this metric in a way that hurts the underlying goal? List 2–3 gaming paths.

### Step 8 — Redesign / mitigate / monitor / accept
For each top consequence, decide:
- **Redesign:** modify the intervention to remove the consequence
- **Mitigate:** add a side-mechanism that absorbs the consequence
- **Monitor + rollback:** ship as-is but commit to rollback triggers
- **Accept:** acknowledge the cost and proceed

Document the decision and the reason for each.

---

## False-Positive Prevention

1. **Static-actor fallacy.** Modeling actors as if they don't respond to the change. Everyone responds to incentives; the question is how, not whether.
2. **First-order tunneling.** "But the first-order effect is so positive!" High first-order positives often come paired with delayed second-order negatives. The matrix is for the negatives, not for relitigating the positives.
3. **Silent acceptance.** Considering a consequence and dismissing it without documenting why. Future post-mortems will not be able to distinguish "considered and accepted" from "missed entirely."
4. **Comprehensive paralysis.** The matrix can balloon. Cap at the top 5–8 consequences by likelihood × severity; the rest are noted but not deeply analyzed.
5. **Goodhart blindness.** If the intervention rewards or punishes a measurable metric, gaming will happen. Never skip the Goodhart audit.
6. **Reversibility optimism.** "If it goes wrong, we'll just roll it back." Most rollbacks are harder than projected because actors have already adapted. Test the rollback assumption.
7. **Adjacent-actor blindness.** The most expensive unintended consequences usually land on actors who weren't on the original list. Push hard to enumerate beyond the obvious.
8. **Time-horizon collapse.** Treating "long term" as a single bucket. The dynamics at 6 months differ from 24 months; separate them.

---

## Output Format

```
# Unintended consequence scan — [intervention]

## Intervention
- Description: [what, by whom, when, mechanism]
- First-order intent: [measurable outcome]
- Desired second-order effects (intended): [list, or "none"]
- Comparable past interventions and their known unintended effects: [list, or "none known"]
- Reversibility of intervention itself: [easy / moderate / hard]

## Actors
| # | Actor                        | Type (target / counterpart / adjacent / gatekeeper) |
|---|------------------------------|------------------------------------------------------|
| 1 | [name]                       | target                                              |
| 2 | [name]                       | counterpart                                         |
| … |                              |                                                      |

## Consequence matrix
| Actor   | Immediate | Short (1–12w) | Medium (3–18mo) | Long (18+mo) |
|---------|-----------|---------------|-----------------|--------------|
| Actor 1 | [effect]  | [effect]      | [effect]        | [effect]     |
| Actor 2 | …         | …             | …               | …            |

## Significant consequences (ranked)
| # | Consequence              | Type        | Likelihood | Severity | Reversibility | Notes |
|---|--------------------------|-------------|------------|----------|---------------|-------|
| 1 | [description]            | gaming      | high       | high     | hard          | …     |
| 2 | [description]            | spillover   | med        | high     | moderate      | …     |
| … |                          |             |            |          |               |       |

## Goodhart audit
- Metric rewarded/punished: [name]
- Gaming path 1: [how an actor would optimize for the metric while harming the underlying goal]
- Gaming path 2: …
- Gaming path 3: …

## Monitoring & response
| Consequence | Observable                     | Cadence  | Response if triggered     |
|-------------|--------------------------------|----------|---------------------------|
| [#1]        | [measurable]                   | weekly   | rollback intervention X   |
| [#2]        | [measurable]                   | monthly  | apply mitigation Y        |
| …           |                                |          |                           |

## Decisions
| Consequence | Decision  | Reason                              |
|-------------|-----------|-------------------------------------|
| [#1]        | redesign  | unmitigatable gaming path           |
| [#2]        | monitor + rollback | acceptable if observed early |
| [#3]        | accept    | low likelihood, recoverable        |
| …           |           |                                     |
```

---

## Verification

- [ ] All actors enumerated, including adjacent and gatekeeper actors.
- [ ] All four time horizons walked.
- [ ] Each significant consequence is typed (behavioral/incentive/etc).
- [ ] Each significant consequence has likelihood, severity, and reversibility.
- [ ] Goodhart audit performed for any rewarded/punished metric.
- [ ] Each high-priority consequence has a monitoring observable and a pre-committed response.
- [ ] Each consequence has an explicit decision (redesign / mitigate / monitor / accept) with reason.
- [ ] No silent-acceptance dismissals.
- [ ] Time horizons not collapsed into a single "long term" bucket.
