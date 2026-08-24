---
title: "Surface Signature Strengths From Evidence, Not a Strengths Quiz"
category: personal-development/identity
description: "Derive the user's real strengths from evidence of what they do well and reach for, separate them from draining competencies, name the top few, and place one underused signature strength into an arena where it is currently missing."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-06
  - QA-12
difficulty: intermediate
tags:
  - identity
  - strengths
  - revealed-preferences
  - self-knowledge
  - deployment
updated: "2026-07-23"
related_prompts:
  - domain-personal-development/prompts/identity/identity_values_clarification.md
  - domain-personal-development/prompts/identity/identity_confidence_calibration.md
  - domain-personal-development/prompts/identity/identity_life_audit_reckoning.md
  - domain-personal-development/prompts/thinking/thinking_regret_minimization.md
  - domain-personal-development/prompts/resilience/resilience_motivation_diagnosis.md
---

# Surface Signature Strengths From Evidence, Not a Strengths Quiz

**Objective:** Identify the user's signature strengths from evidence of what they actually do well and reach for — separating them from skills that drain — name the top few concretely, and place one underused signature strength into an arena where it is currently absent.

**When to use:** The user wants to know their real strengths without a generic personality quiz; feels their best abilities are underused; or is deciding where to invest, specialize, or reposition. Not for assessing an employee or teammate — this reads the user's own evidence only.

**Audience:** An individual examining their own life. Not a tool for rating someone else, and not clinical. If the exercise surfaces persistent worthlessness or an inability to name anything done well, that can point past a strengths gap — see `domain-psychology/` and a licensed professional.

---

## Inputs Required

1. **Did-well log.** 8–15 specific instances the user did something notably well: an outcome that landed, a problem solved faster than peers, work that drew unsolicited praise. Each as *situation → what the user did → observable result.* "I'm good at X" without an instance does not count.
2. **Reach-for log.** What the user volunteers for or gravitates to even when not assigned — the task they pick up first, the problem they can't leave alone.
3. **Flow episodes.** 3–5 recent times the user lost track of time. What, specifically, were they doing.
4. **Unsolicited-ask log.** What people repeatedly come to the user for — the thing colleagues, friends, or family route to them by default.
5. **Drain log.** Things the user is genuinely competent at but that leave them depleted. Required — this is what separates a strength from a mere skill.
6. **One coasting arena.** One area of life or work where the user feels they are underperforming, bored, or on autopilot.

If the did-well log has fewer than 6 concrete instances, refuse and ask for more. A strength cannot be read from self-labels alone.

---

## Instructions

### Step 1 — Derive candidate strengths from the evidence

Read inputs 1–4 together. For each recurring capability, name it as a **verb-based behavior**, not an adjective: "spots the structural flaw in a plan before others" beats "analytical"; "makes a nervous stranger feel at ease in two minutes" beats "personable." A candidate must appear in at least **two** independent instances across the inputs to count. Single instances are noise.

### Step 2 — Classify each candidate on the skill × energy × reach grid

Use only this fixed taxonomy. A true strength sits at the intersection of all three.

| # | Type | Signature | Verdict |
|---|---|---|---|
| 1 | **Signature strength** | High skill (input 1) + energizing/flow (input 3) + reached-for (input 2/4). | The real asset. Prioritize. |
| 2 | **Draining competency** | High skill (input 1) but appears in the drain log (input 5); rarely reached-for. | A skill, not a strength. Do not build a life around it. |
| 3 | **Latent strength** | Energizing + reached-for, but skill not yet demonstrated in outcomes. | Potential, not proven. Flag for development; don't over-promote. |
| 4 | **Borrowed praise** | Others ask for it (input 4) but it drains (input 5) and the user doesn't reach for it. | Praise is trapping the user in a draining skill. Name the trap. |

Every candidate gets exactly one type, with cited evidence for each of the three axes.

### Step 3 — Name the top signature strengths

From the Type-1 candidates only, pick the **top 3** by strength of evidence (number of independent supports × observable result size). State each as a concrete behavioral sentence with its strongest single piece of evidence. If fewer than 3 Type-1 candidates exist, say so plainly rather than promoting a Type-2 or Type-3 to fill the slot.

### Step 4 — Map underuse

For each of the top signature strengths, locate where it is **underused** — arenas where it would apply but currently isn't, with special attention to the coasting arena (input 6). Underuse usually looks like: the strength is spent entirely inside one context, or a draining competency (Type 2/4) is occupying time the signature strength could hold.

### Step 5 — Produce one deployment move

Pick **one** signature strength and **one** arena where it's underused — the pairing with the highest weekly upside — and propose a single move that puts that strength to work there this week. The move must be physical and bounded: a task taken on, a role volunteered for, a recurring block reassigned, a draining competency handed off. Not "lean into your strengths." One strength, one arena, one action.

---

## Constraints

### Must
- Name every candidate as a verb-based behavior backed by ≥ 2 independent instances.
- Classify each candidate into exactly one grid type with evidence on all three axes.
- Treat the drain log (input 5) as decisive in separating strength from skill.
- Output the top 3 signature strengths (or fewer, stated honestly).
- Produce exactly one deployment move, physical and time-bounded.

### Must Not
- Accept adjective labels ("smart," "creative," "hardworking") without behavioral evidence.
- Promote a draining competency or a latent strength to signature status to fill a quota.
- Recommend a strengths-quiz, personality-type framework, or generic "play to your strengths" advice.
- Congratulate, flatter, or inflate — observe the evidence.
- Output a menu of ways to use all strengths — pick one deployment move.

---

## False-Positive Prevention

1. **Don't confuse competency with strength.** A skill the user is good at but that drains them (input 5) is Type 2, not a signature strength — this distinction is the whole prompt.
2. **Don't mistake praise for energy.** Type 4 exists because being repeatedly asked for something (input 4) traps people in draining skills; external demand is not evidence of a strength.
3. **Don't count a capability shown once.** Two-instance minimum, or it's an anecdote.
4. **Don't promote latent strengths.** Energy plus reach without demonstrated skill (Type 3) is potential; naming it as a proven strength sets up a bad bet.
5. **Don't accept self-labels as evidence.** "I'm a natural leader" is a claim; the did-well and unsolicited-ask logs are evidence. Work from the logs.
6. **Don't moralize about "using your gifts."** The output is a deployment move grounded in upside, not a lecture about wasted potential.

---

## Output Format

```
## Candidate strengths (from your evidence)
1. [Verb-based behavior] — evidence: [instance A, instance B]
2. ...

## Grid classification
| Candidate | Skill | Energy | Reach | Type | Verdict |
|---|---|---|---|---|---|
| ... | [cite] | [cite] | [cite] | #N | ... |

## Top signature strengths
1. [Concrete behavioral sentence] — strongest evidence: [one instance]
2. ...
3. ...
(or: "Only N signature strengths are evidenced. The rest are competencies or latent.")

## Underuse map
- [Strength 1] is confined to [arena]; absent from [arena, incl. coasting arena input 6].
- ...

## Deployment move (this week)
Put [signature strength] to work in [underused arena] by [specific physical action, by when].

Predicted check: after this move, [observable change in output, energy, or where the strength shows up].
```

---

## Verification

- [ ] Every candidate is a verb-based behavior with ≥ 2 independent supports.
- [ ] Each candidate classified into one grid type with evidence on skill, energy, and reach.
- [ ] Drain log used to demote at least the clearest draining competency.
- [ ] Top 3 signature strengths (or fewer, stated) drawn only from Type 1.
- [ ] Underuse mapped against the coasting arena (input 6).
- [ ] Exactly one deployment move, physical and time-bounded.
- [ ] No adjective labels without evidence, no quiz, no flattery.
