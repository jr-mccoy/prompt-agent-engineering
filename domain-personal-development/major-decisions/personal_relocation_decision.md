---
title: "Relocation Decision — Multi-Criteria Analysis with Identity, Network, and Optionality Layers"
category: personal-development/major-decisions
description: "Structure a relocation decision (city, country, neighborhood, hybrid) across financial, career, family, social, identity, and optionality dimensions. Includes the often-skipped layers: what the move signals about identity, what social capital is forfeited, what optionality is gained or lost, and what's hard to reverse. Designed for individuals or couples making one of the most consequential and personally distorting decisions in their lives."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - DS-02
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - personal-decisions
  - relocation
  - life-decisions
  - tradeoffs
  - identity
updated: "2026-05-10"
reasoning:
  styles: [analytic, multi-criteria, identity-aware]
  stakes: high
  horizon: years
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: cross_domain
  collaboration: solo_or_pair
  output_format: layered_analysis_with_recommendation
  user_role: [individual, couple, family]
  mode: [decide, audit, synthesize]
related_prompts:
  - domain-decision-making/tradeoff_multi_criteria_decision_analysis.md
  - domain-decision-making/decisioning_regret_minimization.md
  - domain-decision-making/tradeoff_reversibility_stakes_grid.md
---

# Relocation Decision

**Objective:** Structure a relocation decision (city, country, neighborhood, hybrid arrangement) across the dimensions that actually drive long-run satisfaction and regret. Goes beyond the standard cost-of-living and career-trajectory analysis to include the layers most often skipped: identity (who you become in each place), network (what social and professional capital is forfeited or gained), optionality (which futures each location keeps open), and reversibility (what is hard or impossible to undo).

Relocation is among the most consequential personal decisions and one of the most distorted by the immediate emotional state at the moment of decision (excitement about somewhere new, exhaustion with somewhere old, romantic projection onto a place visited briefly). This prompt structures the deliberation to surface dimensions the user is likely under-weighting.

**When to use:**
- Deciding between staying put and moving.
- Deciding between 2+ destinations.
- Deciding between full move and hybrid (remote, partial, two-base).
- Re-evaluating a recent move that isn't going as expected.
- Couples or families negotiating between members with different preferences.

**When NOT to use:**
- The decision is forced (eviction, job loss, family emergency). Different prompt needed for forced relocations.
- The user is in active distress and the decision can be deferred. Defer.
- The user wants permission to do what they were going to do anyway. The prompt won't help.

**Audience:** Individuals, couples, families weighing a multi-year geographic decision.

---

## Inputs / Context

1. **Current location and the candidate(s).** With basic facts (cost, time zone, distance from key relationships).
2. **Forcing function.** What's making this decision live now (job, partner, family, lease, life stage).
3. **Time horizon for the move.** How long would you commit before re-evaluating? (Often the asymmetry: people commit to a move "for at least 2 years" but treat it as permanent emotionally.)
4. **Anyone else affected.** Partner, children, dependents, close family. Their preferences and needs.
5. **What you've already considered.** So we don't re-tread.
6. **Honest emotional state.** Are you running toward something, or running away from something? Both can lead to good moves, but the diagnosis matters.

---

## The seven layers

| Layer | Question | Common pitfall |
|-------|----------|----------------|
| **Financial** | Cost of living, taxes, savings rate, housing | Comparing rent without comparing taxes / total cost |
| **Career** | Job market, growth, professional density | Assuming remote work will fully substitute for proximity |
| **Family / relationships** | Distance from key people, time zones, ease of visits | Underweighting time zone friction, overweighting flight cost |
| **Social** | Existing network, ease of building a new one, age-stage match | Assuming "you can make friends anywhere" — not equally true at all life stages |
| **Identity** | Who you become there; what the place rewards and punishes | Romanticizing identity-by-location; cities have actual cultures |
| **Optionality** | What futures stay open, what get foreclosed | Treating a 2-year move as if reversible when many side-effects compound |
| **Reversibility** | Cost (financial, social, professional) of moving back or moving on | Underestimating reversal cost after life-events accumulate (kids, mortgage, partner roots) |

---

## Constraints

### Must
- Walk all seven layers explicitly. Skipping a layer is the most common analysis failure (especially identity, optionality, reversibility).
- For each candidate location (including stay-put), score on each layer. Use a consistent scale.
- Surface the **forcing function** honestly: is the decision actually live, or is the user running a thought experiment? If the latter, the prompt is fine but the user should know.
- Distinguish **running toward** from **running away**. Both can produce good moves; the diagnosis affects how to weight new-place excitement.
- Include **stay-put** as a serious candidate with full layer analysis, not as a default to dismiss.
- For couples / families: capture each person's layer-by-layer view separately, then synthesize. Do not average; surface where they differ.
- Apply **reversibility honestly**: list everything that becomes harder to reverse after 6 months, 2 years, 5 years in the new place (relationships, kids' schools, partner's job, mortgages, residency rules).
- End with **regret minimization across horizons** (1 year, 5 years, 20 years) for the recommended option.

### Must Not
- Reduce the decision to financial spreadsheet alone. Most relocations that go badly don't fail on financials.
- Skip the identity layer because it feels squishy. It's the layer that drives 5-year satisfaction.
- Treat new-place excitement as evidence about the place. It's evidence about novelty.
- Assume a partner / child agrees because they haven't objected. Elicit explicitly.
- Compute a single weighted score and call it done. Layered analysis surfaces tradeoffs that scoring hides.
- Ignore the running-toward-vs-running-away diagnosis.

---

## Instructions

### Step 1 — Restate the decision
Locations under consideration (including stay-put). Forcing function. Time horizon. Who's affected.

### Step 2 — Diagnose the emotional state
- Running toward: pulled by something specific in the new place. (Probe: what is it specifically? Is it real?)
- Running away: pushed by something in the current place. (Probe: would moving fix it? Or is it portable?)
- Often both. The mix matters; running-away alone leads to disappointment when the new place reveals the same patterns.

### Step 3 — Walk the seven layers per candidate
For each location (including stay-put):

#### Financial
- Cost of living comparison (housing, taxes, insurance, daily costs)
- Income change expected
- Net savings rate estimate
- Equity / housing implications

#### Career
- Job market depth in your domain
- Density of relevant peers / mentors
- Remote-work substitutability
- Career trajectory at 5 years

#### Family / relationships
- Distance from key people
- Time zone friction
- Ease and frequency of visits
- Aging parents / dependent care implications

#### Social
- Existing network in candidate location
- Age-stage match (where in life are people you'd connect with)
- How long to rebuild network from scratch
- Cultural fit / sense of welcome

#### Identity
- What the place rewards (status, behavior, profession, lifestyle)
- What the place punishes or makes hard
- Who you'd become after 5 years there
- Does that future-self match your values?

#### Optionality
- What futures stay open from this location?
- What futures become harder?
- 5-year option value

#### Reversibility
- Direct cost of moving back (financial, time)
- 6-month reversibility: easy / moderate / hard
- 2-year reversibility: easy / moderate / hard
- 5-year reversibility: easy / moderate / hard
- What becomes irreversible (residency, kids' school context, partner roots, etc.)

Score each layer per candidate on a 1–5 scale with one-sentence rationale.

### Step 4 — For couples / families
Each adult fills the layer analysis independently. Then synthesize:
- Layers where you agree
- Layers where you differ (which is which)
- Layers where one person hasn't really considered (often: identity, social, optionality)
- Children's affected layers (school continuity, friend groups, activities)

### Step 5 — Compute and surface
- Per-layer rankings of candidates
- Overall weighted score (weights matched to user's stated priorities, not assumed)
- Layers where rankings differ — these are the tradeoffs to face

### Step 6 — Adversarial check
- New-place excitement: discount for novelty effect
- Current-place exhaustion: discount for transient state
- Romantic projection: have you actually lived in the candidate place for 30+ days, or is it based on visits?
- Sunk cost in current place: separate "I've invested here" (sunk) from "I'm building here" (forward-looking)

### Step 7 — Regret minimization
For the leading candidate, ask:
- 1 year out: what would I most regret about this choice?
- 5 years out: same
- 20 years out: same

Compare to the runner-up. Is the regret asymmetric? Often the longer horizon favors moves; the shorter horizon favors staying. Both signals matter.

### Step 8 — Decision and tripwires
- Recommendation: [option]
- Confidence: [high / medium / low]
- Reversal plan: if [tripwire] within [time], reverse via [path] and accept [cost]
- Commitment horizon: how long before re-evaluating (separate from "permanently")
- Calibration anchor: a sentence to write down today that future-you can audit against

---

## False-Positive Prevention

1. **Spreadsheet illusion.** Reducing relocation to financial comparison. Most relocations that disappoint don't fail on money.
2. **Identity skip.** Identity is squishy but consequential — who you become in a place shapes everything else. Don't skip.
3. **Novelty-as-signal.** Excitement about a new place is partly novelty. Discount it; visit longer if you can.
4. **Running-away invisibility.** If you're running from something portable, the new place will reveal the same problem. Diagnose.
5. **Partner / child silence.** Absence of objection is not consent. Elicit.
6. **Reversibility optimism.** "We'll just move back" — after kids, mortgage, partner's job, friendships, the cost grows. Test honestly.
7. **Stay-put as default-bad.** The current location often gets unfairly low scores because the user is exhausted with it. Apply same scoring discipline.
8. **Single-weighted-score commitment.** Hides the tradeoffs that matter. Layer-by-layer is more honest.
9. **Visit-as-residence proxy.** A great two-week trip ≠ a great life. Try a longer stay if possible.
10. **Identity smuggling.** "I'd be the kind of person who lives in [city]" — this is identity wishful thinking. Test against who you actually are.

---

## Output Format

```
# Relocation decision — [candidates]

## Decision context
- Candidates: [...] (including stay-put)
- Forcing function: [...]
- Time horizon: [...]
- People affected: [...]

## Emotional diagnosis
- Running toward: [what specifically, is it real]
- Running away: [what, is it portable]
- Mix: [primary]

## Layer analysis per candidate

### Candidate 1: [name]

#### Financial
- Score: [1–5] — [rationale]
#### Career
- Score: [1–5] — [rationale]
#### Family / relationships
- Score: [1–5] — [rationale]
#### Social
- Score: [1–5] — [rationale]
#### Identity
- Score: [1–5] — [rationale]
#### Optionality
- Score: [1–5] — [rationale]
#### Reversibility
- 6mo: [easy/mod/hard] | 2yr: [...] | 5yr: [...] | irreversible items: [...]

### Candidate 2 [...]
### Candidate 3 (stay-put) [...]

## Couple / family synthesis (if applicable)
| Layer | Person A | Person B | Children's stake | Agreement? |
|-------|----------|----------|------------------|------------|
| Financial | … | … | … | yes |
| Identity  | … | … | … | differs |
| …         |   |   |   |       |

## Cross-candidate ranking
| Layer | Cand 1 | Cand 2 | Stay-put | Highest-weighted? |
|-------|--------|--------|----------|-------------------|
| …     |        |        |          |                   |

## Tradeoff surface
- [Cand 1 wins on Layer X but loses on Layer Y; what's that worth?]
- [...]

## Adversarial check
- Novelty discount applied? [yes/no, by how much]
- Current-place exhaustion factored? [yes/no]
- Visit-vs-residence reality check: [...]
- Sunk-cost separation: [...]

## Regret horizons (recommended candidate)
- 1 year: [most likely regret]
- 5 years: [most likely regret]
- 20 years: [most likely regret]
- Compared to runner-up: [asymmetry]

## Decision
- Recommendation: [option]
- Confidence: [high / medium / low]
- Commitment horizon: [time before re-evaluating]
- Reversal plan: if [tripwire] within [time], move to [option] via [path]
- Calibration anchor (write down today): "I am choosing [option] because [layer-anchored reason], understanding I am accepting [named cost]."
```

---

## Verification

- [ ] All seven layers walked per candidate.
- [ ] Stay-put included as serious candidate with full analysis.
- [ ] Emotional diagnosis (running toward / away) explicit.
- [ ] For couples / families: per-person layer analysis surfaced before synthesis.
- [ ] Reversibility tested at 6mo, 2yr, 5yr horizons.
- [ ] Regret horizons (1y, 5y, 20y) considered for leading option.
- [ ] Adversarial check (novelty, exhaustion, visit-vs-residence, sunk cost) performed.
- [ ] Recommendation includes commitment horizon, reversal plan, calibration anchor.
- [ ] No spreadsheet-only reduction.
- [ ] No identity-layer skip.
