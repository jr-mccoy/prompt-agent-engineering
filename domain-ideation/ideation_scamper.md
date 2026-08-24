---
title: "SCAMPER — Seven Transformation Lenses on a Thing"
category: ideation/structured-transformation
description: "Apply the seven SCAMPER moves (Substitute, Combine, Adapt, Modify/Magnify/Minify, Put to other use, Eliminate, Reverse) to a target object, process, or design. Each letter yields 3–5 specific transformation moves, producing a structured 21–35 idea set anchored to a concrete thing. Lighter and more directed than open-ended quantity ideation; the right move when you already have a thing and want variations on it."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: beginner
tags:
  - ideation
  - scamper
  - structured-brainstorming
  - transformation
  - product-variation
updated: "2026-05-27"
reasoning:
  styles: [divergent, generative, combinatorial]
  stakes: low_to_moderate
  horizon: variable
  uncertainty: variable
  evidence_quality: not_applicable
  domain_complexity: variable
  collaboration: solo_or_team
  output_format: structured
  user_role: [pm, designer, founder, marketer, engineer, individual]
  mode: [diverge]
related_prompts:
  - domain-ideation/ideation_forced_quantity_100_ideas.md
  - domain-ideation/ideation_constraint_flip.md
  - domain-ideation/ideation_idea_convergence_dot_voting.md
---

# SCAMPER — Seven Transformation Lenses on a Thing

**Objective:** Take a concrete target — an existing product, feature, process, service, design, or workflow — and run it through the seven SCAMPER transformation lenses, generating 3–5 specific moves per lens. SCAMPER is the right tool when you already *have* a thing and want a structured set of variations on it, rather than open-ended breadth on an abstract brief. It trades the sprawl of forced-quantity ideation for a directed, repeatable structure: every idea is anchored to a named transformation of the target, which makes the output easier to evaluate and act on.

**When to use:**
- You have an existing product, feature, or process and want a structured set of variations or improvements.
- Iterating on something concrete rather than inventing from a blank brief.
- A team wants a shared, repeatable ideation structure that doesn't depend on a facilitator's intuition.
- Improving an offering that feels "done" but stale — SCAMPER reliably surfaces moves the team hasn't tried.

**When NOT to use:**
- There is no concrete target yet — you're still trying to decide *what* to build. Use breadth ideation (`ideation_forced_quantity_100_ideas.md`) or a reframe (`ideation_jobs_to_be_done_reframe.md`) first.
- You want maximum surprise / lateral leaps. SCAMPER is structured and incremental; for genuinely strange ideas, use random-stimulus or worst-idea-first.
- The target is so ill-defined that "substitute what?" has no answer. Sharpen the target first.

**Audience:** PMs, designers, founders, marketers, and engineers iterating on an existing thing; workshop facilitators wanting a structured opener.

---

## Inputs / Context

1. **The target.** The specific object, process, feature, service, or design to transform. State it concretely enough that its components and steps are namable.
2. **The target's components / steps.** A short decomposition — the parts, materials, stages, or attributes SCAMPER will operate on. (If not supplied, derive it in Step 1.)
3. **The goal of the variation.** What a good transformation would achieve (cheaper, faster, more delightful, more accessible, more defensible, etc.). Used to flag promising moves, not to filter during generation.
4. **Hard constraints.** Real non-negotiables (regulatory, budget, brand) that bound which moves are viable.
5. **Moves already tried.** So SCAMPER doesn't re-surface known dead ends.

---

## Constraints

### Must
- Cover **all seven** lenses. Do not skip a letter because it "doesn't apply" — the forced application is where unexpected moves come from.
- Generate **3–5 specific moves per lens** (minimum 21 total). Each move names *what* is transformed and *how*.
- Anchor every move to a **named component or attribute** of the target. "Substitute" must answer "substitute *what* with *what*."
- Keep generation and evaluation separate: generate all moves first, then do a single light flagging pass against the goal.
- Flag each move's **feasibility** (easy / moderate / hard) and **novelty** (incremental / notable / radical) in the final pass only.

### Must Not
- Produce vibes-level moves ("make it better", "modernize it"). A move specifies the transformation concretely.
- Collapse two lenses into one (e.g., treating Combine and Adapt as the same). Each lens is a distinct cognitive operation.
- Filter during generation. Record weak-looking moves; flag them later.
- Pad a lens with relabelings of the same move. Three genuinely different substitutions, not one substitution worded three ways.
- Stop at the obvious move per lens. The first Substitute is usually trivial; push to 3–5.

---

## The seven lenses

| Letter | Lens | Core question |
|--------|------|---------------|
| **S** | Substitute | What component, material, rule, person, or step could be swapped for something else? |
| **C** | Combine | What could be merged — with another feature, product, audience, or step — to create something new? |
| **A** | Adapt | What works elsewhere (another product, domain, era) that could be adapted into this? |
| **M** | Modify / Magnify / Minify | What could be made bigger, smaller, more frequent, exaggerated, or stripped down? |
| **P** | Put to other use | Who else could use this, or what else could it do, beyond its current purpose? |
| **E** | Eliminate | What could be removed, simplified, or deleted entirely — and what happens if you do? |
| **R** | Reverse / Rearrange | What if the order, roles, or direction were flipped or resequenced? |

---

## Instructions

### Step 1 — Pin and decompose the target
Restate the target in one sentence. List its key components, steps, or attributes (5–10 items). These are the handles each lens will grab.

### Step 2 — Substitute
For 3–5 components, propose swapping each for an alternative (different material, mechanism, rule, audience, channel, step). Name what is swapped and for what.

### Step 3 — Combine
Propose 3–5 combinations: merge the target with another product, feature, step, or audience; bundle two stages; fuse two attributes. Name both halves.

### Step 4 — Adapt
Identify 3–5 things that work in a different product, domain, or era, and adapt each into the target. Name the source and the adapted form.

### Step 5 — Modify / Magnify / Minify
Propose 3–5 moves that change scale, frequency, or intensity: exaggerate an attribute, shrink a component, add or remove repetition, amplify the strongest feature.

### Step 6 — Put to other use
Propose 3–5 new uses, users, or contexts for the target as-is or lightly changed. Name the new use and who it serves.

### Step 7 — Eliminate
Propose 3–5 removals: delete a step, feature, role, or constraint. For each, state what is lost and what is gained.

### Step 8 — Reverse / Rearrange
Propose 3–5 inversions or resequencings: flip the order of steps, swap who does what, reverse the value flow, invert a default.

### Step 9 — Light flagging pass
Now, and only now, tag each move with feasibility (easy/moderate/hard), novelty (incremental/notable/radical), and a one-word fit to the stated goal. Do not delete anything. Mark the 3–7 most promising moves for hand-off.

### Step 10 — Hand off
List the flagged candidates. Hand off to convergence (`ideation_idea_convergence_dot_voting.md`) or to a prototyping step. Do not pick a winner here.

---

## False-Positive Prevention

1. **Lens-skipping.** "Eliminate doesn't apply to us." It does — forced application is the value. Generate the move even if it seems absurd.
2. **Vibes moves.** "Modify: make it more premium" is not a move. "Magnify the onboarding tutorial from 1 screen to a 5-step guided tour" is.
3. **Unanchored substitution.** "Substitute something" with no named component is empty. Always answer "swap *what* for *what*."
4. **Lens collapse.** Combine and Adapt blur easily. Combine = merge two things you own; Adapt = import something from outside. Keep them separate.
5. **First-move-only.** Stopping at one move per lens caps the yield at 7 obvious ideas. The 3rd–5th move per lens is where the interesting ones hide.
6. **Generation-time filtering.** Killing a move while generating ("Eliminate the login? No, we need auth") loses the kernel. Record it; the *partial* elimination might be the real idea.
7. **Padding by rewording.** Three substitutions that are the same idea in different words is one move. Diversify the component being swapped.
8. **Premature winner.** Declaring a favorite during generation biases the remaining lenses toward it. Flag at the end, in one pass.

---

## Output Format

```
# SCAMPER — [target]

## Target
> [Restated in one sentence]
- Components / steps / attributes: [list]
- Goal of variation: [...]
- Hard constraints: [...]
- Already tried: [...]

## S — Substitute
1. [Swap X for Y] — [what changes]
2. …
(3–5)

## C — Combine
1. [Merge A with B] — [resulting thing]
2. …

## A — Adapt
1. [From source: mechanism] → [adapted form]
2. …

## M — Modify / Magnify / Minify
1. [Scale/frequency/intensity change]
2. …

## P — Put to other use
1. [New use / user / context]
2. …

## E — Eliminate
1. [Remove X] — lost: [...] / gained: [...]
2. …

## R — Reverse / Rearrange
1. [Flip / resequence]
2. …

## Flagging pass
| Lens | Move (short) | Feasibility | Novelty | Fit to goal |
|------|--------------|-------------|---------|-------------|
| S | [...] | moderate | notable | high |
| C | [...] | easy | incremental | medium |
| … | | | | |

## Candidates for hand-off
- [3–7 flagged moves]
- Next step: convergence (ideation_idea_convergence_dot_voting.md) or prototype.
```

---

## Verification

- [ ] All seven lenses covered, none skipped.
- [ ] 3–5 specific moves per lens (≥21 total).
- [ ] Every move anchored to a named component/attribute and specifies the transformation.
- [ ] Combine and Adapt kept distinct (merge-owned vs import-outside).
- [ ] No filtering during generation; flagging done in a single later pass.
- [ ] Each move tagged feasibility + novelty + fit in the flagging pass.
- [ ] No vibes-level or padded-by-rewording moves.
- [ ] 3–7 candidates flagged and handed off; no winner picked here.
