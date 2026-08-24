---
title: "Select and Apply the Right Prioritization Framework"
category: decision-making/prioritization
description: "Given a list of items and the surrounding context, recommend the best-fit prioritization framework (RICE, ICE, WSJF, MoSCoW, Kano, Eisenhower, or value/effort), justify the choice against the situation, then apply it — producing a ranked, tiered list with all scoring math shown and every guessed input flagged."
techniques:
  - ST-01
  - ST-02
  - DS-06
  - QA-01
  - QA-20
difficulty: beginner
tags:
  - prioritization
  - decision-making
  - frameworks
  - ranking
  - backlog
  - rice-wsjf
updated: "2026-07-08"
related_prompts:
  - domain-decision-making/tradeoff_multi_criteria_decision_analysis.md
  - domain-decision-making/decisioning_time_boxed_decision_protocol.md
  - domain-decision-making/decisioning_regret_minimization.md
---

# Select and Apply the Right Prioritization Framework

**Objective:** Recommend the one prioritization framework that fits the user's items and context — choosing among RICE, ICE, WSJF, MoSCoW, Kano, Eisenhower, and value/effort — then apply it end-to-end, delivering a ranked and tiered list with the scoring math visible and every guessed input explicitly flagged.

The value-add is the *selection*, not just the scoring: most prioritization goes wrong before any number is written, when a team applies its habitual framework to a situation shaped for a different one (Eisenhower for economic sequencing, RICE with no reach data, Kano with no customer signal).

## When to Use

- Use when: you have 3–30 competing items (features, projects, tasks, bugs, initiatives) and no agreed method for ordering them.
- Use when: your team ranks by loudest-voice or habit ("we always RICE") and you want a defensible, shared method matched to *this* situation.
- Use when: you already ran a framework but the result feels off and you want to check whether the framework — not the scores — was the problem.
- Don't use when: it's a single yes/no or either/or decision (use `tradeoff_multi_criteria_decision_analysis.md` or a reversibility/stakes check) — these frameworks rank *lists*.
- Don't use when: order is already dictated by hard dependencies or contractual deadlines — that's sequencing by constraint, not prioritization by preference. This prompt will detect and say so.

**Audience:** Product managers, founders, team leads, and individual contributors. No prior framework knowledge assumed.

## Inputs / Context

1. **The items (required).** One per line, wrapped in `<items>…</items>`. 3–30 items. A short parenthetical per item helps (e.g., "SSO (blocking two enterprise renewals)").
2. **The context (required).** Wrapped in `<context>…</context>`, covering as much as known: what kind of items these are; the goal a "high priority" item serves (revenue, churn, speed, risk); what data exists (usage metrics, customer feedback, effort estimates); how much time you have to decide; who consumes the ranking; team capacity.
3. **Constraints (optional).** Deadlines, dependencies, committed work. If present, these become *overrides*, not scores.
4. **Preferred framework (optional).** If named, it is validated against the context — and challenged if it's a poor fit — before being applied.

If context is thin, the prompt proceeds with labeled assumptions rather than stalling — but every assumption is visible in the output.

## Framework Selection Guide

| Framework | Best when | Requires | Watch out |
|---|---|---|---|
| **RICE** | Product backlog; you have (or can estimate) how many users each item touches | Reach data, impact/effort estimates | Slow for >20 items; blind to deadlines |
| **ICE** | Early stage, little data, need speed over precision | Gut estimates only | Scores are opinions — don't over-trust |
| **WSJF** | Delay itself costs money; time-sensitive economics; release trains | Cost-of-delay components + job size | Overkill for personal/small lists |
| **MoSCoW** | Negotiating scope to a fixed deadline with stakeholders | A hard scope boundary | Yields buckets, not a strict order |
| **Kano** | Choosing customer-facing features by satisfaction shape (basic / performance / delighter) | Customer input or a strong proxy | Disqualified without customer signal |
| **Eisenhower** | One person or small team triaging tasks in minutes | Urgent/important judgment only | Too coarse for economic tradeoffs |
| **Value/Effort 2×2** | Fast shared picture across a mixed bag; communicates visually | Rough value + effort judgments | Precision theater if over-argued |

**Selection rules (walk top-down; first match wins, ties broken by data available):**
1. Personal or small-team *task* triage, minutes available → **Eisenhower**.
2. Cost of delay differs materially across items (deadlines, decaying value, renewal windows) → **WSJF**.
3. Customer-facing features *and* customer signal available (surveys, interviews, support themes) → **Kano**.
4. Fixed deadline/scope negotiation with stakeholders → **MoSCoW**.
5. Product backlog with usage/reach data → **RICE**; same shape but data-poor → **ICE**.
6. Mixed item types, need a fast shared picture → **Value/Effort 2×2**.
7. High stakes and criteria that don't fit any single framework → stop; escalate to `tradeoff_multi_criteria_decision_analysis.md`.

## Constraints

### Must
- Recommend **exactly one** primary framework with a rationale tied to specific facts from `<context>`; name the runner-up and the one reason it lost.
- Define every scoring component and its scale **before** scoring anything.
- Show all math: per-item component scores, the formula, and the computed result. No bare ranks.
- Tag the provenance of every score input: `[data]` (supplied or cited), `[estimate]` (reasoned from supplied facts), or `[guess]` (invented to proceed). Count guesses per item.
- Group the ranked output into action tiers (e.g., Do now / Next / Later, or the framework's native buckets), and mark near-ties as ties.
- List hard deadlines and dependencies as **overrides above the ranking** — the framework never silently absorbs them.
- If the user's preferred framework fits poorly, say so and why before proceeding (then apply their choice if they insisted, with the mismatch noted).

### Must Not
- Invent data (reach counts, revenue figures) and present it as fact — invented numbers must carry `[guess]`.
- Output pseudo-precision: no three-decimal scores built on guessed inputs; round to match input quality.
- Apply several frameworks in full "to be safe" — the selection is the point. (A one-line runner-up comparison is enough.)
- Let a framework's blind spot bury a stated constraint (RICE has no deadline field; deadlines still appear in Overrides).
- Refuse to produce an order because inputs are uncertain — flag the uncertainty and rank anyway.

## Instructions

1. **Read the situation.** From `<context>`, extract and state in one line each: item type, the goal high-priority serves, data available, time budget for deciding, audience for the ranking, and stakes. Where something is missing, state the assumption you're making and mark it `[assumed]`.

2. **Select the framework.** Walk the selection rules top-down against the stated situation. Name the primary framework and the specific context facts that triggered it; name the runner-up and the single decisive reason it lost. If the user named a preference, validate or challenge it here.

3. **Set the scale.** Define each component of the chosen framework and its scale before touching the items (e.g., RICE: Reach = accounts affected/quarter; Impact = 3/2/1/0.5/0.25; Confidence = 100/80/50%; Effort = person-weeks). State the formula.

4. **Score every item.** One table row per item: component scores, each tagged `[data]`/`[estimate]`/`[guess]`, then the computed score with the arithmetic visible for at least the top row.

5. **CRITICAL: Verify before finalizing (self-check).**
   - **Recount:** recompute two rows from their components; fix any arithmetic drift.
   - **Guess audit:** list every `[guess]` input. For each item in the top 3, test whether a plausible alternative value for its guessed inputs changes its tier; state the flip condition ("Export jumps to #1 if Impact ≥ 1.7").
   - **Constraint sweep:** re-read `<context>` for deadlines/dependencies the scoring ignored; move them to Overrides.
   - **Gut check:** does the #1 item plausibly serve the stated goal? If the ranking contradicts something explicit in the context, surface the conflict rather than smoothing it.

6. **Tier and deliver.** Present the ranked list in action tiers, ties marked, with a capacity note if capacity was given. Overrides sit above the tiers.

7. **Recommend next data.** Name the 1–3 cheapest data points that would replace the most score-influential guesses, so the next run of this ranking is on firmer ground.

## False-Positive Prevention (MUST follow)

Here a "false positive" is *false confidence* — in the framework choice or in the ranks.

❌ **DON'T:**
- Default to RICE because it's the famous one — that skips the selection step that is this prompt's job.
- Let a guessed number launder itself into fact because it appears in a table next to real data.
- Report a strict total order when adjacent scores sit within the noise of their guessed inputs.
- Apply Kano with zero customer signal, or WSJF when delay cost is roughly uniform across items — both are disqualifying conditions, not style choices.
- Force MoSCoW buckets into a rank order; MoSCoW yields buckets (rank *within* a bucket with a secondary framework only if asked).
- Drop a deadline or dependency because the chosen framework has no field for it.

✅ **DO:**
- Walk the selection rules against quoted context facts, and record which rule fired.
- Tag provenance on every input at write-time, and total the guesses per item.
- Mark near-ties as ties and say what evidence would separate them.
- Disqualify frameworks whose required inputs don't exist, and say which input is missing.
- Keep constraints in a visible Overrides section that outranks the scored list.
- Re-verify the top 3 specifically — errors there are the costly ones.

## Dual-Failure Prevention (QA-20)

❌ **HARMFUL failure:** A confident, precise-looking ranking built on unlabeled guesses steers a real resourcing decision; or a mis-selected framework systematically misorders the work (Eisenhower where delay-cost economics dominate; RICE burying a contractual deadline at rank 7).

❌ **UNHELPFUL failure:** Hedging every rank into mush ("it depends on your priorities"), dumping all seven frameworks on the user instead of choosing, or caveating the output so heavily no one can act on it Monday morning. An unranked list is a failed output of a ranking prompt.

✅ **Quality bar:** A seasoned PM would start the top tier today *and* could defend both the framework choice and the stated uncertainty to their team without embarrassment.

## Expected Output

Situation read, framework choice with rationale, scale definition, full scoring table with provenance tags, tiered ranking with overrides on top, the self-check (guess audit + sensitivity), and next-data recommendations.

### Output Format

```
# Prioritization: [N items] — [chosen framework]

## Situation read
- Item type / Goal / Data available / Time budget / Audience / Stakes  (one line each, [assumed] where relevant)

## Framework choice
- Primary: [framework] — because [context facts; which selection rule fired]
- Runner-up: [framework] — lost because [one reason]

## Scoring scale
[Each component, its scale, and the formula]

## Scores
| # | Item | [components, each value tagged [data]/[estimate]/[guess]] | Score | Guesses |

## Ranked result
### Overrides (do regardless of rank)
### Tier 1 — Do now   /  Tier 2 — Next  /  Tier 3 — Later   (ties marked)

## Self-check
- Math recount: [rows rechecked]
- Guess audit & sensitivity: [flip conditions for top 3]
- Constraint sweep: [anything moved to Overrides]

## Next data to collect
1–3 items, each tied to the guess it replaces
```

## Example Output

```
# Prioritization: 8 items — RICE

## Situation read
- Item type: product backlog for a B2B SaaS app (4-person team)
- Goal: reduce churn this quarter [stated]
- Data available: product analytics (active accounts per feature), CS at-risk list,
  cancellation-survey themes; no formal cost-of-delay figures
- Time budget: ~1 hour to decide [stated]
- Audience: the team itself; ranking drives the next 6 weeks [assumed]
- Stakes: medium-high — one quarter of a small team's output

## Framework choice
- Primary: RICE — product backlog + real reach data (analytics, at-risk counts) → rule 5.
- Runner-up: WSJF — two items carry renewal deadlines, but delay cost is roughly flat
  across the other six, so cost-of-delay math would add work without reordering much.
  The deadline items are handled as Overrides instead (see below).

## Scoring scale
- Reach (R): accounts affected per quarter (count)
- Impact (I): per-account effect on churn — 3 massive / 2 high / 1 medium / 0.5 low / 0.25 minimal
- Confidence (C): 100% / 80% / 50%
- Effort (E): person-weeks
- Formula: RICE = (R × I × C) / E

## Scores
| # | Item                          | R              | I             | C    | E   | Score | Guesses |
|---|-------------------------------|----------------|---------------|------|-----|-------|---------|
| 1 | Dashboard load-time fix       | 310 [data]     | 1 [estimate]  | 80%  | 3   | 82.7  | 0       |
| 2 | Usage-drop alerts for CS      | 60 [data]      | 3 [estimate]  | 80%  | 2   | 72.0  | 0       |
| 3 | Onboarding checklist          | 120 [data]     | 2 [estimate]  | 80%  | 3   | 64.0  | 0       |
| 4 | Self-serve data export        | 200 [estimate] | 1 [guess]     | 50%  | 2   | 50.0  | 1       |
| 5 | CS health-score dashboard     | 180 [estimate] | 2 [estimate]  | 50%  | 5   | 36.0  | 0       |
| 6 | Slack integration             | 80 [estimate]  | 1 [guess]     | 50%  | 3   | 13.3  | 1       |
| 7 | SSO / SAML                    | 15 [data]      | 3 [data]      | 100% | 4   | 11.3  | 0       |
| 8 | Pricing page redesign         | 90 [guess]     | 0.5 [guess]   | 50%  | 2   | 11.3  | 2       |

Worked example (row 1): (310 × 1 × 0.8) / 3 = 82.7

## Ranked result

### Overrides (do regardless of rank)
- SSO / SAML — two enterprise renewals (~$140k ARR) contractually require it by Sep 30
  [data, from context]. RICE ranks it #7 because reach is 15 accounts; the deadline, not
  the score, decides. Schedule its 4 pw first. (This is RICE's known blind spot — the
  reason WSJF was runner-up.)

### Tier 1 — Do now (after the override)
1. Dashboard load-time fix — 82.7
2. Usage-drop alerts — 72.0
3. Onboarding checklist — 64.0
   Capacity note: override (4 pw) + Tier 1 (8 pw) = 12 pw vs ~14 pw available this
   quarter — feasible with ~2 pw slack.

### Tier 2 — Next
4. Self-serve data export — 50.0 (score rests on 1 guess; see self-check)
5. CS health-score dashboard — 36.0

### Tier 3 — Later
6. Slack integration — 13.3
7. Pricing page redesign — 11.3 (tie with SSO's raw score; 2 guesses — least
   trustworthy number on the board)

## Self-check
- Math recount: rows 1 and 4 recomputed from components — both correct.
- Guess audit & sensitivity:
  - Export Impact is a [guess] at 1. Cancellation surveys already list export as a top-3
    reason, which argues for 2. Flip condition: at I ≥ 1.7, Export scores ≥ 85 and
    becomes #1. This single guess is the most consequential number in the table.
  - Dashboard fix: no guesses, but C=80% assumes the root cause is known; if an eng
    spike drops C to 50%, score falls to 51.7 (→ Tier 2). Flag for the spike below.
  - Alerts & onboarding: all inputs [data]/[estimate]; ranks stable under ±1 scale step.
- Constraint sweep: SSO renewal deadline moved to Overrides (done). No other deadlines
  or dependencies found in context.

## Next data to collect
1. Tag export mentions in the next 20 cancellation calls → replaces Export's Impact
   [guess], the input most likely to reorder Tier 1.
2. One-day eng spike on dashboard root cause → firms up C for the current #1.
3. Confirm the CS at-risk list count (60) is current → validates Alerts' reach.
```

## Customization Guide

- **Personal to-do triage:** rules will select Eisenhower — the scoring table collapses to a 2×2 (urgent × important) with one-line placements; skip provenance tags, keep the override lane for hard deadlines.
- **Delay-cost-dominated portfolios (releases, contracts, decaying opportunities):** WSJF path — show the three cost-of-delay components (user/business value, time criticality, risk reduction) per item, divided by job size.
- **More than 30 items:** run a value/effort 2×2 first to cut to a ≤15-item shortlist, then score only the shortlist with the selected framework.
- **Stakeholder scope negotiation:** MoSCoW path — add the discipline rule "Must ≤ 60% of capacity" and record who agreed to each bucket.
- **Higher rigor:** hand Tier 1 to `tradeoff_multi_criteria_decision_analysis.md` for custom weighted criteria before committing a quarter to it.

## Techniques Used

- **ST-01 (Clear Objective Statement):** the objective fixes a two-stage deliverable — *select, then apply* — so the model can't skip straight to its habitual framework, which is the exact failure this prompt exists to prevent.
- **ST-02 (Structured Sequential Instructions):** seven ordered steps force the load-bearing sequence: situation → selection → scale definition *before* any scoring → scoring → verification → tiers → next data.
- **DS-06 (Prioritization and Severity Guidance):** the output is rank + action tiers, and the priority-hierarchy variant is applied literally: hard deadlines/dependencies are an Overrides lane that always outranks framework scores.
- **QA-01 (Self-Verification):** step 5 is a built-in self-critique — recompute rows, audit every `[guess]`, run sensitivity flips on the top 3, and sweep for constraints the scoring ignored — before the ranking is delivered.
- **QA-20 (Dual-Failure Prevention):** guards both directions — a confident ranking on unlabeled guesses or a mis-fit framework (harmful), and an unranked, over-hedged, seven-frameworks-at-once non-answer (unhelpful) — with the quality bar that a PM would act on Tier 1 today and defend the method.

## Related Prompts

- `domain-decision-making/tradeoff_multi_criteria_decision_analysis.md` — escalate here when stakes are high and no off-the-shelf framework's criteria fit.
- `domain-decision-making/decisioning_time_boxed_decision_protocol.md` — when choosing *how* to prioritize is itself dragging on, box the meta-decision.
- `domain-decision-making/decisioning_regret_minimization.md` — for one large decision rather than a list of competing items.

## Verification

- [ ] Frontmatter complete; every technique ID exists in the index.
- [ ] When-to-Use includes a don't-use case.
- [ ] Instructions include an explicit verification step (step 5).
- [ ] False-Positive Prevention has real ❌/✅ pairs.
- [ ] Dual-Failure Prevention covers harmful AND unhelpful directions.
- [ ] Findings carry Confidence levels (provenance tags + sensitivity flip conditions on ranks).
- [ ] Example Output is concrete and 80–120 lines.
- [ ] No invented data or fabricated authority.
