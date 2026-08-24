---
title: "System Archetype Recognition — Match a Situation to a Known Pattern"
category: reasoning-craft/systems
description: "Match a described situation to a system archetype (tragedy of the commons, success-to-the-successful, fixes-that-fail, shifting-the-burden, escalation, eroding goals, limits-to-growth, growth-and-underinvestment, accidental adversaries), then read off the archetype's signature behavior, where the current path leads, and the leverage the archetype implies. Counters the failure mode of re-diagnosing from scratch a structure that recurs across domains and has a known trap and a known way out."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - systems-thinking
  - archetypes
  - pattern-recognition
  - diagnosis
  - feedback-loops
updated: "2026-05-21"
reasoning:
  styles: [systems, analogical, diagnostic, structural]
  stakes: variable
  horizon: months_to_years
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: cross_domain
  collaboration: solo_or_pair
  output_format: archetype_match_plus_trajectory
  user_role: [executive, founder, operator, policy, analyst, individual]
  mode: [diagnose, audit]
related_prompts:
  - domain-reasoning-craft/systems/systems_feedback_loop_identifier.md
  - domain-reasoning-craft/systems/systems_leverage_point_analysis.md
  - domain-reasoning-craft/systems/systems_causal_loop_diagram.md
---

# System Archetype Recognition

**Objective:** Match a described situation against the catalog of system archetypes — recurring loop structures that show up across wildly different domains. For each plausible match, describe the structure, test whether the situation actually fits, surface the archetype's signature behavior, predict where the current path leads if nothing changes, and name the leverage the archetype implies. Most stuck situations are an instance of one of nine or ten archetypes; recognizing the pattern is most of the diagnosis.

**When to use:**
- A situation feels familiar — like something you've seen before in a different context — and you want to name the structure.
- A pattern keeps producing the same bad outcome despite different people and different fixes.
- You want a fast diagnosis before committing to a full causal loop diagram.
- A team is fighting about what's wrong, and naming the shared archetype reframes the argument productively.

**When NOT to use:**
- The situation is genuinely novel and forcing it into an archetype would distort it — note the partial fit and move to a custom model (`systems_causal_loop_diagram.md`).
- You already know the loops and need to choose where to intervene — go to `systems_leverage_point_analysis.md`.
- The problem is linear with no feedback; archetypes are all feedback structures.

**Audience:** Operators, founders, executives, policy people, analysts, and individuals trying to name why a recurring situation keeps ending the same way.

---

## Inputs / Context

1. **The situation.** What's happening, who's involved, and the recurring or worsening outcome.
2. **The pattern over time.** Is it escalating, eroding, oscillating, or stuck? Different archetypes have different signatures.
3. **Fixes tried.** What's been attempted and what happened — fixes-that-fail and shifting-the-burden are diagnosed largely from the *response* to past fixes.
4. **The actors and their incentives.** Many archetypes (commons, escalation, accidental adversaries) hinge on multiple actors optimizing locally.

---

## Archetype catalog (with signature and trap)

### Limits to growth
**Structure:** a reinforcing loop drives growth until a balancing loop (a limit) kicks in. **Signature:** fast growth that slows and plateaus. **Trap:** pushing harder on the growth engine when the binding constraint is the limit. **Way out:** find and ease the limit, not the engine.

### Shifting the burden
**Structure:** a symptomatic fix relieves the symptom but atrophies the capacity for the fundamental fix; dependence on the symptomatic fix grows. **Signature:** repeated reliance on a quick fix; the underlying problem worsens. **Trap:** the symptomatic solution feels like it's working. **Way out:** invest in the fundamental capability even as the symptom recurs.

### Fixes that fail
**Structure:** a fix works short-term but triggers a delayed consequence that recreates or worsens the original problem. **Signature:** problem returns, often bigger, after each fix. **Trap:** applying the same fix harder. **Way out:** account for the delayed side effect; pick a fix without the backlash.

### Tragedy of the commons
**Structure:** multiple actors draw on a shared limited resource; individually rational use collectively exhausts it. **Signature:** a shared resource degrading while each actor's usage looks reasonable. **Trap:** appealing to individual restraint. **Way out:** make the aggregate limit visible and govern access (rules-level leverage).

### Escalation
**Structure:** two balancing loops — each actor acts to close a relative-position gap with the other — that together form one reinforcing arms-race spiral. **Signature:** tit-for-tat intensification (price wars, feature wars, conflict spirals). **Trap:** one more escalation to "win." **Way out:** unilateral de-escalation or changing the game's rules.

### Success to the successful
**Structure:** initial success channels more resources to the winner, starving the other, widening the gap regardless of underlying merit. **Signature:** winner-take-all divergence from a small initial lead. **Trap:** attributing the gap entirely to merit. **Way out:** decouple resource allocation from prior success; re-level.

### Eroding goals
**Structure:** when performance lags the goal, the goal is lowered rather than performance raised; a balancing loop that drifts the standard down. **Signature:** quietly declining standards ("the new normal"). **Trap:** each individual lowering feels reasonable. **Way out:** anchor the goal to an absolute external reference, not recent performance.

### Growth and underinvestment
**Structure:** growth strains capacity; capacity investment is deferred (or judged against eroded standards); degraded service caps growth. **Signature:** growth stalls and is blamed on the market when it's actually self-inflicted under-capacity. **Trap:** cutting investment when growth slows. **Way out:** invest in capacity ahead of demand, against an absolute service standard.

### Accidental adversaries
**Structure:** two partners who should cooperate each take locally protective actions that undermine the other, spiraling a partnership into conflict. **Signature:** a souring partnership where each side feels wronged. **Trap:** retaliating to the other's "betrayal." **Way out:** surface the unintended harm each is causing the other; rebuild the cooperative loop.

---

## Constraints

### Must
- Test the situation against the catalog and surface the **1–3 best-fitting archetypes**, ranked by fit.
- For each candidate, state the **fit test**: which structural elements of the archetype are present in the situation and which are missing or assumed.
- Describe the archetype's **signature behavior** and check it against the observed pattern over time.
- Predict **where the current path leads** if the structure is left intact.
- Name the archetype's **standard trap** (the intuitive move that makes it worse) and its **standard way out** (where the leverage is).
- If no archetype fits cleanly, say so and flag the closest partial match with its mismatch.

### Must Not
- Force a fit. A partial match stated as a clean match produces wrong leverage advice.
- Diagnose from the surface topic rather than the structure. Archetypes are domain-independent; "it's about hiring" is not a diagnosis, "it's growth-and-underinvestment in the hiring pipeline" is.
- Skip the trap. The trap (the appealing wrong move) is the most actionable part of the diagnosis.
- Treat the way-out as a guaranteed fix. It points to the leverage; implementation still needs design.

---

## Instructions

### Step 1 — Restate the situation and its time-pattern
Summarize what's happening and whether it escalates, erodes, oscillates, or stalls.

### Step 2 — Screen against the catalog
Walk the archetypes quickly. Score each as no-fit / partial / strong based on whether its core loop structure is present.

### Step 3 — Test the top candidates
For the 1–3 strongest, run the fit test: list the archetype's structural elements and mark each present / absent / assumed in the situation. A strong fit has the core loops present, not just a thematic resemblance.

### Step 4 — Check the signature
Compare the archetype's signature behavior to the observed pattern over time. If the situation escalates but the archetype produces erosion, the fit is wrong.

### Step 5 — Project the trajectory
State where the situation goes if the structure is left alone — the archetype tells you the ending.

### Step 6 — Name the trap and the way out
The trap is the intuitive intervention that worsens the archetype. The way out points to where the leverage actually is. Connect the way-out to a leverage level and hand deeper design to `systems_leverage_point_analysis.md`.

### Step 7 — Confidence and partial-fit note
State how confident the match is. If it's a partial fit, name what doesn't fit and whether a custom model is warranted.

---

## False-Positive Prevention

1. **Forced fit.** Declaring a clean match on thematic resemblance. Require the archetype's core loops to be structurally present, tested element by element.
2. **Surface-topic diagnosis.** Naming the domain ("it's a morale problem") instead of the structure ("shifting-the-burden: perks relieve the symptom while the management capability that would fix it atrophies").
3. **Multiple-archetype mush.** Claiming a situation is five archetypes at once. Rank to 1–3; if everything fits, nothing has been diagnosed.
4. **Trap omission.** Skipping the standard trap — the single most useful output, because it's the move the user is probably about to make.
5. **Way-out as silver bullet.** Treating the standard remedy as automatic. It identifies leverage; it still needs implementation design and a pre-mortem.
6. **Ignoring the time-signature mismatch.** If the observed pattern (escalating) contradicts the archetype's signature (eroding), the match is wrong regardless of thematic appeal.
7. **Archetype as label, not lever.** Naming the archetype and stopping. The value is the trajectory, trap, and way-out, not the label.

---

## Output Format

```
# Archetype recognition — [situation]

## Situation and time-pattern
[Summary + escalating / eroding / oscillating / stalled]

## Screening
| Archetype                  | Fit (no/partial/strong) |
|----------------------------|-------------------------|
| Limits to growth           |                         |
| Shifting the burden        |                         |
| Fixes that fail            |                         |
| Tragedy of the commons     |                         |
| Escalation                 |                         |
| Success to the successful  |                         |
| Eroding goals              |                         |
| Growth and underinvestment |                         |
| Accidental adversaries     |                         |

## Best match: [archetype]  (confidence: low/med/high)

### Fit test
| Archetype structural element | Present / absent / assumed |
|------------------------------|----------------------------|
| [element]                    |                            |

### Signature vs observed
[Does the archetype's signature behavior match the observed pattern? ]

### Trajectory if unchanged
[Where this ends]

### The trap (don't do this)
[The intuitive move that worsens it]

### The way out (leverage)
[Where the leverage is; tie to a leverage level]

## Second candidate (if any)
[Repeat abbreviated]

## Partial-fit note
[If no clean match: what doesn't fit, whether a custom model is warranted]
```

---

## Verification

- [ ] Situation screened against the full catalog with fit ratings.
- [ ] Top 1–3 candidates tested element-by-element, not by theme.
- [ ] Archetype signature checked against the observed time-pattern.
- [ ] Trajectory-if-unchanged stated for the best match.
- [ ] Standard trap and standard way-out both named.
- [ ] Way-out connected to a leverage level, not presented as a guaranteed fix.
- [ ] Confidence stated; partial fits flagged with the mismatch.
- [ ] Diagnosis is structural, not a restatement of the surface topic.
