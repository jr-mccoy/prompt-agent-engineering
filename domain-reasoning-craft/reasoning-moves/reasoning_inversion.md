---
title: "Inversion — Solve By Inverting the Problem"
category: reasoning-craft/reasoning-moves
description: "Invert a positively-framed problem ('how do we achieve X?') into negative form ('how would we guarantee NOT-X?', 'what would the failure case look like in detail?'), enumerate the failure paths, then translate back into protective rules and assumption surfacings. Companion to ideation_inverse_problem (which is for ideation breadth); this prompt emphasizes reasoning rigor."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - reasoning
  - inversion
  - failure-modes
  - assumption-surfacing
  - munger
updated: "2026-05-10"
reasoning:
  styles: [inversive, adversarial, structural]
  stakes: variable
  horizon: variable
  uncertainty: variable
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo
  output_format: failure_paths_then_protections
  user_role: [strategist, founder, executive, engineer, individual]
  mode: [audit, diagnose]
related_prompts:
  - domain-ideation/ideation_inverse_problem.md
  - domain-decision-making/decisioning_blind_spot_mirror_see_what_im_missing.md
  - domain-reasoning-craft/systems/systems_intervention_pre_mortem.md
---

# Inversion

**Objective:** Solve a positively-framed problem by inverting it. "How do I achieve X?" → "How would I guarantee NOT-X?" or "What would the detailed failure case look like?" Enumerate the failure paths concretely, identify which are currently active, and translate the inversion into protective rules and assumption surfacings.

Sister prompt to `ideation_inverse_problem.md` — that one is for *ideation breadth* (generating ideas via inversion). This prompt is for *reasoning rigor* (using inversion to surface failure paths and assumptions).

**When to use:**
- A goal feels diffuse and the path isn't clear.
- A plan feels solid but you suspect it's missing something.
- Diagnosing why something isn't working ("if I wanted to fail at this, what would I do?").
- Pre-mortem on a strategy or decision.
- Assumption surfacing — inversion often reveals assumptions you didn't know you were making.

**When NOT to use:**
- Pure ideation (use `ideation_inverse_problem.md`).
- Tasks with no negative form (writing a poem).
- Cases where the failure analysis would be cruel rather than useful.

**Audience:** Strategists, founders, engineers, executives, individuals working on consequential goals.

---

## Inputs / Context

1. **The positive problem statement.** "How do I / we [achieve X]?"
2. **What's been tried.** So inversion targets new surface area.
3. **The actor whose moves we're enumerating.**
4. **Stakes.**

---

## Constraints

### Must
- Generate at least **8–15 specific failure moves** — concrete actions or design choices that would produce NOT-X. Bullet level: specific actions, not vibes.
- For each failure move: is the system currently doing it? (Currently-happening moves are the diagnostic.)
- Translate each failure move back into a **direct action** (stop / start / design-in) that prevents it.
- Identify the **highest-leverage failure move** — the one whose elimination would most improve the positive outcome.
- Surface **non-translatable failure moves** — failure paths that are real risk surface but cannot be directly prevented (capture as monitoring items, not action items).

### Must Not
- Generate vibes-level failures ("be lazy", "don't try"). Specific actions / design choices only.
- Skip the back-translation step.
- Use inversion to license harmful design (the prompt is for prevention, not construction).
- Ignore failure moves the actor is currently making — those are the most important.

---

## Instructions

### Step 1 — Restate the positive problem
"How do I / we [X]?" — verbatim.

### Step 2 — Pick inversion framing
- **NOT-X:** how would we guarantee not achieving X?
- **Engineer failure:** what would we do if we wanted this to fail?
- **Worst case:** what would the worst version of the outcome look like, and how would we engineer it?
- **Sustain bad state:** what's keeping the current bad state in place?

Pick 1–2 framings that are most generative for this problem.

### Step 3 — Generate 8–15 specific failure moves
Each is a concrete action or design choice. Be specific to the level where someone could observe whether it's happening.

### Step 4 — Currently-happening flag
For each failure move: is the system currently doing it (in part)? Also rate the effect size (high / med / low) of removing or blocking each failure move.

### Step 5 — Back-translate to direct actions
For each failure move, derive the corresponding direct prevention:
- **Stop:** stop doing this currently-happening failure
- **Start:** add a new behavior / design that prevents the failure
- **Design in:** structural change that makes the failure impossible

### Step 6 — Identify highest-leverage failure
Which failure move, if eliminated, would most improve the positive outcome? Often this is a currently-happening one with large effect.

### Step 7 — Non-translatable failures (watch list)
Some failures cannot be directly prevented (key person leaves, market shifts). Capture as monitoring items.

### Step 8 — Action set
- Stop: [list]
- Start: [list]
- Design in: [list]
- Watch for: [list]

---

## False-Positive Prevention

1. **Vibes inversion.** "Be incompetent" is not actionable.
2. **Translation skip.** Listing failures without back-translating loses the value.
3. **Currently-happening blindness.** Generating hypothetical failures while ignoring the ones already operating.
4. **Self-blaming theater.** Inversion that surfaces user-driven failures should produce action, not flagellation.
5. **Single-framing tunneling.** Try 1–2 inversion framings if the first is unproductive.
6. **Harmful design license.** Inversion is for prevention; if it surfaces harms, the only legitimate next step is prevention design.

---

## Output Format

```
# Inversion — [positive problem]

## Positive problem
> "How do we [X]?"

## Inversion framings used
- [NOT-X / Engineer failure / Worst case / Sustain bad state]

## Failure moves
| # | Specific failure move | Currently happening? | Effect size if removed | Translates to direct action? |
|---|------------------------|----------------------|------------------------|-------------------------------|
| 1 | [specific]             | yes — partial        | high                   | yes — [action]                |
| 2 | [specific]             | no                   | medium                 | yes — [action]                |
| ... |                       |                      |                        |                               |

## Highest-leverage failure
- Move #: [N]
- Why: [largest currently-happening effect]
- Direct action to remove: [...]

## Non-translatable failures (watch list)
- [Failure that's not directly preventable but worth monitoring]
- [...]

## Action set
**Stop**
- [...]

**Start**
- [...]

**Design in**
- [...]

**Watch for**
- [non-translatable risks to monitor]
```

---

## Verification

- [ ] 8–15 specific failure moves (not vibes).
- [ ] Currently-happening flag for each.
- [ ] Back-translation to direct action for each translatable failure.
- [ ] Highest-leverage failure named with direct action.
- [ ] Non-translatable failures captured as watch list.
- [ ] Action set has Stop / Start / Design / Watch sections.
- [ ] No vibes-level failures.
- [ ] No skipped translations.
