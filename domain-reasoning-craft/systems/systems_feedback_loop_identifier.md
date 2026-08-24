---
title: "Feedback Loop Identifier — Find the Reinforcing and Balancing Loops"
category: reasoning-craft/systems
description: "A focused diagnostic that extracts the closed feedback loops from a described situation, signs each as reinforcing (R) or balancing (B), names the variables in each, and identifies which loop is currently dominant. Lighter than a full causal loop diagram: the job is to find the loops, not model the whole system. Counters the failure mode of treating a recurring pattern ('this keeps happening') as a series of unrelated events rather than the output of a loop nobody has named."
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
  - feedback-loops
  - reinforcing-balancing
  - diagnosis
  - dynamics
updated: "2026-05-21"
reasoning:
  styles: [systems, causal, diagnostic]
  stakes: variable
  horizon: variable
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: cross_domain
  collaboration: solo_or_pair
  output_format: loop_table
  user_role: [analyst, founder, executive, operator, individual]
  mode: [diagnose, audit]
related_prompts:
  - domain-reasoning-craft/systems/systems_causal_loop_diagram.md
  - domain-reasoning-craft/systems/systems_archetype_recognition.md
  - domain-reasoning-craft/systems/systems_stock_and_flow_model.md
---

# Feedback Loop Identifier

**Objective:** Given a described situation, extract the closed feedback loops, sign each as **R** (reinforcing — amplifies change) or **B** (balancing — counteracts change), name the variables that form each loop, describe the loop's effect on system behavior, and identify which loop is currently dominant. This is the focused "find the loops" extractor used during diagnosis — not a full system model. When someone says "this keeps happening" or "every time we fix it, it comes back," they are usually describing a loop they haven't named.

**When to use:**
- A pattern recurs and you suspect feedback is driving it ("morale drops, people leave, remaining team is overloaded, morale drops further").
- Before building a full causal loop diagram, to find the core loops worth modeling.
- An intervention keeps getting undone by the system and you want to find the balancing loop absorbing it.
- Growth or decline is accelerating and you want to name the reinforcing loop behind it.

**When NOT to use:**
- You already need the full model with delays, external drivers, and dominance shifts — go straight to `systems_causal_loop_diagram.md`.
- The situation is a one-time linear cause-effect with no recurrence or feedback.
- You're trying to match the situation to a known pattern by name — use `systems_archetype_recognition.md` (which is loop structure pre-packaged as archetypes).

**Audience:** Anyone diagnosing a recurring or accelerating pattern: operators, founders, managers, analysts, and individuals trying to understand a stuck personal situation.

---

## Inputs / Context

1. **The situation.** A description of what's happening, ideally including the recurrence ("X happens, then Y, then we're back to X but worse").
2. **The actors.** Who or what makes decisions or changes behavior inside the situation (their responses are usually where loops close).
3. **The pattern over time.** Is the thing accelerating, oscillating, stuck at a level, or eroding? This hints at loop type before analysis.
4. **Interventions tried.** What was done and whether the pattern came back — failed interventions often reveal a balancing loop.

---

## Constraints

### Must
- Identify every **closed loop** you can find — a chain of variables that returns to its start. A loop is the unit of analysis; a one-way chain is not a loop.
- Sign each loop: count the negative (`−`) links around the loop; **even number of negatives = R (reinforcing)**, **odd = B (balancing)**.
- Name the variables in each loop as noun phrases (quantities that change), not actions.
- Write a one-sentence story for each loop in the form "as A rises, B rises, which after [delay] causes C to … which feeds back to A."
- State which loop is **currently dominant** and what would shift dominance.
- Connect loop type to observed behavior: R loops produce growth or collapse (acceleration away from a point); B loops produce stability, goal-seeking, or oscillation (return toward a point).

### Must Not
- Report a one-way causal chain as a loop. If it doesn't close back on itself, it isn't feedback.
- Use decisions or actions as loop variables ("decide to cut prices"); use the quantities they change ("price", "demand").
- Assert R or B without counting negative links. Intuition about loop sign is frequently wrong.
- Claim dominance with false confidence — dominance is a hypothesis unless you have data; flag it.
- Pad with every conceivable loop. Surface the 2–5 loops actually driving the described behavior.

---

## Instructions

### Step 1 — Restate the pattern
Summarize the recurrence or trend in one or two sentences, framed over time. If the input is event-shaped, restate it as a pattern.

### Step 2 — List candidate variables
Pull the quantities that change in the situation (noun phrases). Include the actors' responses as variables ("attrition rate", "remaining-team workload") — loops usually close through someone's reaction.

### Step 3 — Trace links
For each pair, ask: does a change in A cause a change in B? Sign it `+` (same direction) or `−` (opposite). Keep tracing until a chain returns to a variable it already passed through — that closes a loop.

### Step 4 — Sign each loop
Count negative links in the loop. Even → **R**. Odd → **B**. Record the count so the verdict is checkable.

### Step 5 — Write the loop story
One sentence per loop describing the trip around it, including any delay. The story must match the sign: an R loop's story should compound; a B loop's story should self-correct.

### Step 6 — Map loop to behavior
- R dominant → exponential growth, runaway, or collapse.
- B dominant → stabilization, goal-seeking, oscillation (if delayed).
- Competing R and B → S-curves, boom-bust, or stuck equilibria.
State which loop your evidence says is in control right now.

### Step 7 — Dominance and leverage
Name what would shift dominance (a delay shortening, an external driver, a saturation limit). Note where intervening would change loop behavior — and hand deeper leverage analysis to `systems_leverage_point_analysis.md`.

---

## False-Positive Prevention

1. **Chain-as-loop.** A causal chain that never returns to its origin is not feedback. Verify each "loop" closes back on a variable already in it.
2. **Sign-by-intuition.** "This is obviously reinforcing" without counting negatives. Count the `−` links every time; the parity determines the type.
3. **"Reinforcing = good" confusion.** R means amplifying, not beneficial. A reinforcing loop can drive a death spiral. B means counteracting, not bad. Separate the math from the value judgment.
4. **Decision-as-variable.** Loops are made of quantities, not choices. "We decide to discount" is an intervention on the variable "price."
5. **Missing the human response loop.** Many loops close through how people react to a condition (overload → quit → more overload). If your loops contain no behavioral response, you may have missed the one that's driving the pattern.
6. **Dominance overconfidence.** Which loop dominates, and when, is hard to know without data. State dominance as a hypothesis and name what would confirm it.
7. **Loop inflation.** Surfacing ten loops dilutes the diagnosis. Prioritize the few loops that produce the observed behavior.

---

## Output Format

```
# Feedback loops — [situation]

## Pattern over time
[The recurrence or trend, framed over time]

## Variables in play
[Noun-phrase list, including actor responses]

## Loops

### Loop R1 (reinforcing)
- Variables: A → B → C → A
- Negative links: 0 → even → R
- Story: [one sentence; should compound]
- Behavior produced: [growth / collapse / runaway]
- Dominant now? [yes/no — and on what evidence]

### Loop B1 (balancing)
- Variables: D → E → D
- Negative links: 1 → odd → B
- Story: [one sentence; should self-correct]
- Behavior produced: [stabilization / oscillation if delayed]
- Dominant now? [yes/no]

(Repeat for each loop, 2–5 total.)

## Current dominance
[Which loop is in control of the observed behavior, and the evidence]

## What would shift dominance
[Delays, saturation limits, external drivers, or interventions that flip control]
```

---

## Verification

- [ ] Every reported loop closes back on itself (no chains mislabeled as loops).
- [ ] Each loop's R/B sign is justified by a counted number of negative links.
- [ ] Loop variables are noun phrases, not actions or decisions.
- [ ] Each loop has a one-sentence story consistent with its sign.
- [ ] Loop type is connected to the observed behavior (growth/collapse vs stabilization/oscillation).
- [ ] At least one loop closes through an actor's behavioral response (where applicable).
- [ ] Current dominance stated as a hypothesis with evidence, not asserted.
- [ ] 2–5 loops surfaced, not an exhaustive dump.
