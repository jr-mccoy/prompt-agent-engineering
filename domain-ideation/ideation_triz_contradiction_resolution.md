---
title: "TRIZ Contradiction Resolution — Name the Contradiction, Apply a Few Principles Honestly"
category: ideation/inventive-problem-solving
description: "Resolve a design problem by stating it as a TRIZ contradiction — technical (improving A worsens B) or physical (one element must be X and not-X) — then applying a small, justified set of inventive principles or separation principles to generate concepts that remove the trade-off instead of compromising on it. Deliberately restrained: 3–6 principles chosen with a stated fit, no claims that all 40 apply, and no contradiction-matrix cell citations from memory. Distinct from ideation_constraint_flip.md (which drops or adds a constraint) and ideation_cross_domain_analogy_mining.md (open analogy search)."
techniques:
  - DS-01
  - CM-02
  - RT-04
  - QA-04
  - QA-01
difficulty: advanced
tags:
  - ideation
  - triz
  - contradiction
  - inventive-principles
  - engineering-design
  - problem-solving
  - cant-have-both
  - stuck-on-tradeoff
updated: "2026-09-24"
reasoning:
  styles: [analytical, divergent, systematic]
  stakes: moderate
  horizon: medium
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: high
  collaboration: solo_or_team
  output_format: structured
  user_role: [engineer, designer, product_developer, founder]
  mode: [diverge]
related_prompts:
  - domain-ideation/ideation_constraint_flip.md
  - domain-ideation/ideation_cross_domain_analogy_mining.md
  - domain-reasoning-craft/reasoning-moves/reasoning_analogical_inference.md
---

# TRIZ Contradiction Resolution

**Objective:** Take a design problem where improving one property keeps worsening another, state it precisely as a TRIZ contradiction, and generate concepts that *resolve* the contradiction rather than settle on a compromise point. TRIZ (Altshuller's theory of inventive problem solving) rests on the observation that strong inventions tend to eliminate a trade-off, and that the moves which do so recur across fields. This prompt uses that idea with restraint: it applies a handful of principles whose fit it can argue, and it says when a principle is a stretch.

Two contradiction types:
- **Technical contradiction:** improving parameter A worsens parameter B (a stronger bracket is heavier).
- **Physical contradiction:** one element must have opposite properties (the bracket must be thick for strength and thin for weight). Resolved by **separation** — in time, in space, on condition, or between the whole and its parts.

---

## When to Use

- An engineering or product design is stuck on a trade-off and every option is a compromise on the same curve.
- The team keeps saying "we can have X or Y, not both".
- You want systematic concept generation for a physical or technical system, not open brainstorming.

**Distinct from:**
- `domain-ideation/ideation_constraint_flip.md` — changes the constraints. TRIZ keeps both requirements and removes the conflict between them.
- `domain-ideation/ideation_cross_domain_analogy_mining.md` — searches freely for analogous mechanisms. TRIZ principles are pre-abstracted analogies, applied to a precisely stated contradiction.
- `domain-reasoning-craft/reasoning-moves/reasoning_analogical_inference.md` — tests whether an analogy holds; use it on any TRIZ concept whose transfer is doubtful.

**When NOT to use:**
- There is no genuine conflict — the problem is effort or budget, not a trade-off.
- The system is purely social or organisational. TRIZ can be stretched there, but its principles were abstracted from technical patents; say so if you proceed.

---

## Inputs / Context

1. **The system.** What it is and what it must do.
2. **The trade-off.** Which property you are trying to improve and what gets worse when you do.
3. **Resources in or near the system.** Materials, fields (heat, gravity, magnetism, pressure), time windows, idle parts, the user's own actions.
4. **Hard constraints.** Cost, safety, regulation, manufacturing process.
5. **Solutions tried.** And where on the trade-off curve each landed.

---

## Method

### Step 1 — State the Ideal Final Result
One sentence: the function is delivered with none of the cost or harm, ideally by the system itself. This is a direction, not a target; it stops the session optimising the current compromise.

### Step 2 — State the technical contradiction
"If we improve [A] by [change], then [B] gets worse because [mechanism]." Also write the reverse. If you cannot name the mechanism, stop and establish it — a contradiction without a mechanism is a guess.

### Step 3 — Sharpen to a physical contradiction
Find the single element whose property must be opposite: "[element] must be [X] to deliver A and [not-X] to avoid harming B." Name *where* and *when* each requirement actually applies.

### Step 4 — Try the four separation principles
For each, ask whether the two requirements occur in different conditions:
- **In time** — X during one phase, not-X during another.
- **In space** — X in one region, not-X in another.
- **On condition** — X under one load, temperature, or state; not-X under another.
- **Between whole and parts** — the system is X while its parts are not-X, or the reverse.
Record "does not separate" where honest.

### Step 5 — Apply 3–6 inventive principles, with fit
Choose from the 40 inventive principles by name (e.g., Segmentation, Taking out, Local quality, Asymmetry, Preliminary action, The other way round, Dynamics, Another dimension, Parameter changes, Composite materials). For each chosen principle, state *why it fits this contradiction* in one sentence and produce one or two concrete concepts. If a principle was considered and rejected, say so briefly.

### Step 6 — Check resources
For each concept, ask whether it uses resources already in the system (Inputs item 3) before adding new parts. Concepts that add complexity to remove a trade-off should say so.

### Step 7 — Assess concepts
For each concept: does it resolve the contradiction or merely move along the curve? What new contradiction does it create? Confidence (high / medium / low) that it would work, with the reason. Mark 2–3 for prototyping.

---

## Output Format

```
# TRIZ — [system]

## Ideal Final Result
## Technical contradiction (and reverse)
## Physical contradiction: [element] must be [X] for [A] and [not-X] for [B]

## Separation
| Principle | Separates? | Concept |
|-----------|-----------|---------|

## Inventive principles applied (3–6)
| Principle | Why it fits | Concept(s) |
Considered and rejected: [...]

## Concept assessment
| Concept | Resolves or trades? | New contradiction | Confidence + reason | Prototype? |

## Caveats
- [stretch applications, unverified mechanisms]
```

---

## Verification

- [ ] Contradiction names a mechanism, not just two properties.
- [ ] Physical contradiction identifies one element and where/when each requirement holds.
- [ ] All four separation principles attempted; failures recorded.
- [ ] 3–6 inventive principles, each with a stated fit; none cited by number alone.
- [ ] Each concept marked as resolving versus trading, with its new contradiction.
- [ ] Stretch applications (non-technical systems, weak fits) flagged in Caveats.

---

## False-Positive Prevention

1. **Principle-spraying.** Listing fifteen principles with one-line concepts each looks thorough and is not. Three well-argued principles beat fifteen asserted ones.
2. **Matrix cells from memory.** Do not claim "the contradiction matrix recommends principles 1, 15, 35" unless the user supplied the matrix. Choose principles by argued fit instead.
3. **Compromise dressed as resolution.** "A medium-thickness bracket" is a point on the same curve. A resolution changes the curve.
4. **Contradiction without mechanism.** "Speed versus quality" is a slogan. Name how improving one degrades the other.
5. **Ignoring the new contradiction.** Most resolutions create a smaller problem elsewhere; not naming it overstates the concept.
6. **Parts-count creep.** A concept that removes a trade-off by adding three components may be worse than the trade-off. Check resources first.
7. **Overclaiming reach.** On social or business systems, say the principles are being used as metaphor, not as validated patterns.

---

## Example

**System:** a hiking water bottle. **Trade-off:** larger capacity means more bulk in the pack when the bottle is empty.

- **IFR:** the bottle holds a litre when needed and takes no pack space otherwise.
- **Technical contradiction:** improving volume (larger rigid body) worsens stowed size, because a rigid wall keeps its shape whether full or empty.
- **Physical contradiction:** the bottle wall must be large (to hold water) and small (to stow).
- **Separation in time:** large when full, small when empty → collapsible. *Separates.*
- **Separation in space:** rigid neck and base, flexible body → drinkable one-handed without the whole bottle being rigid. *Separates.*
- **Between whole and parts:** a set of small nesting cups that together hold a litre. *Separates, but adds parts.*
- **Principles applied:** *Dynamics* (fits: the problem is a fixed shape in a changing situation) → accordion-fold wall; *Segmentation* (fits: volume can be split) → two half-litre soft flasks; *Local quality* (fits: different wall regions need different stiffness) → rigid collar bonded to a flexible body. Considered and rejected: *Another dimension* — no clear fit.
- **Assessment:** accordion wall resolves the contradiction; new contradiction — folds trap dirt and are harder to clean (medium confidence). Rigid-collar design resolves and adds one-hand drinking; new contradiction — the bond is a failure point (high confidence it works, medium on durability). Prototype both.

---

## Techniques Used

- **DS-01 Framework Application** — TRIZ contradiction, separation, and inventive-principle framework.
- **CM-02 Constraint Specification** — a 3–6 principle cap and a mandatory fit sentence.
- **RT-04 Analogical Reasoning** — inventive principles as abstracted analogies transferred to this system.
- **QA-04 Uncertainty Acknowledgment** — confidence per concept and a Caveats section for stretch fits.
- **QA-01 Self-Verification** — resolve-versus-trade check before recommending prototypes.

---

## Related Prompts

- `domain-ideation/ideation_constraint_flip.md` — when changing the constraint is legitimate.
- `domain-ideation/ideation_cross_domain_analogy_mining.md` — open analogy search when TRIZ principles run dry.
- `domain-reasoning-craft/reasoning-moves/reasoning_analogical_inference.md` — test whether a transferred principle actually holds.
