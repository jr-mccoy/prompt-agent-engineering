---
title: "Turn a Position-to-Position Skill Gap Into a Sequenced Reskilling Roadmap"
category: personal-development/career-transformation
description: "Convert the specific skill gap between the user's current position and a named target position into an evidence-checked, sequenced reskilling roadmap — ordered by dependency and proof-value, with a checkpoint per skill — while deferring generic curriculum design to domain-learning/."
techniques:
  - ST-01
  - ST-02
  - DS-06
  - CM-02
  - QA-12
difficulty: intermediate
tags:
  - career
  - reskilling
  - skill-gap
  - roadmap
  - repositioning
updated: "2026-07-23"
related_prompts:
  - domain-personal-development/career-transformation/career_residual_skills_inventory.md
  - domain-personal-development/career-transformation/career_ai_era_skill_moat.md
  - domain-personal-development/career-transformation/career_90_day_repositioning_plan.md
  - domain-learning/learning_skill_gap_to_curriculum.md
  - domain-learning/learning_curriculum_designer.md
---

# Turn a Position-to-Position Skill Gap Into a Sequenced Reskilling Roadmap

**Objective:** Take the gap between where the user is now and a *named* target position, and produce a sequenced roadmap of skills to build — ordered by dependency and proof-value, each with an observable checkpoint — so the user knows what to learn, in what order, and how they'll know it worked. Hand off the *how you learn each skill* (curriculum, resources, practice loops) to `domain-learning/`.

**When to use:** The user has identified a target role/position (via `career_role_structural_vulnerability.md`, `career_90_day_repositioning_plan.md`, or their own research) and needs the skill-building path between here and there. Also for someone who "wants to move into X" but hasn't broken it into an ordered plan. Not for: designing the curriculum for a *single* skill once it's chosen (that's `domain-learning/learning_curriculum_designer.md`), and not for deciding *whether* to reskill at all (that's the moat and vulnerability prompts).

**Audience:** An individual planning their own reskilling. Not clinical.

---

## Inputs Required

1. **Current position — real skills held.** What the user can already do, with evidence. If they've run `career_residual_skills_inventory.md` or `career_ai_era_skill_moat.md`, paste the output; it's the strongest input.
2. **Target position — concrete.** A specific role, at a specific level, ideally with a real job posting or two, or a named person who holds it. "Something more senior" is not a target; refuse it.
3. **What the target position actually requires — evidence, not guesses.** From job postings, people in the role, or the user's own observation: the skills and proof the target role screens for. Mark each requirement as *verified* (from a real posting/person) or *assumed* (the user's guess).
4. **Time and constraints.** Hours per week available for reskilling, a rough horizon (3 / 6 / 12 months), and any hard constraints (job, caregiving, budget).
5. **Transferable adjacencies.** Skills the user has that are *close to* target requirements and could transfer with less effort than learning from zero.

If input 2 is vague or input 3 is entirely *assumed* (no verified requirement), refuse to sequence and send the user to verify the target's real requirements first — a roadmap built on guessed requirements sends the user learning the wrong things.

---

## Instructions

### Step 1 — Build the gap table

For each target requirement (input 3), place the user on a fixed scale and mark the requirement's source:

| Requirement | Source | Current level | Gap |
|---|---|---|---|
| [skill/proof] | verified / assumed | none / partial / near-target | large / medium / small / none |

Levels:
- **none** — the user has no working exposure.
- **partial** — used it, but below the target's bar.
- **near-target** — a transferable adjacency (input 5) that needs conversion, not construction.

Requirements marked *assumed* carry a warning: don't build large efforts on unverified requirements.

### Step 2 — Drop the non-gaps and the low-value gaps

Remove requirements where the gap is **none**. Then flag any large-gap skill that is (a) low-value for actually landing the role, or (b) squarely automatable surface area per `career_ai_era_skill_moat.md`. Don't sequence effort into skills that won't move the needle or that tools are collapsing. State what you dropped and why.

### Step 3 — Order the remaining gaps by dependency, then proof-value

Sequence with two rules, in order:
1. **Dependency first.** Some skills are prerequisites for others (you can't do the advanced thing before the foundation). Foundations come first.
2. **Proof-value next.** Among skills with no dependency between them, do the one that most quickly produces *visible evidence* the user can point to (a shipped artifact, a credential the role screens for, a demonstrable output). Reskilling that produces no visible proof is invisible to the target market.

Convert near-target adjacencies (input 5) early — they're cheap wins that build momentum and proof fast.

### Step 4 — Attach a checkpoint and a proof artifact to each skill

For each skill in the sequence, define:
- **Checkpoint:** the observable that says "this skill is at the target's bar" — not "I studied it" but "I produced X" or "I passed Y" or "I did Z in real conditions."
- **Proof artifact:** what the user will have to *show* for it (a project, a contribution, a portfolio piece, a certification the role actually values).

If a skill has no possible proof artifact, mark it — it may be real but it won't help the user get hired unless it shows up somewhere visible.

### Step 5 — Fit to the time budget and cut

Lay the sequence against input 4's hours and horizon. If it doesn't fit, **cut** — don't compress everything into an impossible schedule. Keep the dependency-critical and highest-proof-value skills; defer or drop the rest, and say which. A roadmap that assumes 20 hours/week from someone who has 5 is a fantasy.

### Step 6 — Hand off the "how" and set the first block

- For each skill, **do not** design the curriculum here. Point to `domain-learning/learning_curriculum_designer.md` (per-skill curriculum) and `domain-learning/learning_deliberate_practice_designer.md` (practice loop). This prompt owns the *sequence and proof*, not the pedagogy.
- Name the **first skill block** to start this week, with its checkpoint and the specific first session. Physical and bounded.

---

## Constraints

### Must
- Refuse to sequence if the target is vague or all requirements are unverified.
- Mark every requirement as verified or assumed and warn on assumed.
- Order by dependency first, proof-value second.
- Attach an observable checkpoint and a proof artifact to every sequenced skill.
- Cut the roadmap to the real time budget rather than compressing.
- Defer per-skill curriculum/practice design to `domain-learning/`.

### Must Not
- Design the actual curriculum, reading list, or course sequence for any individual skill — that's `domain-learning/`'s job.
- Sequence effort into automatable surface-area skills or low-value gaps without flagging them.
- Produce a roadmap with no proof artifacts — learning the target market can't see doesn't help repositioning.
- Assume the user's guessed requirements are correct; unverified requirements are labeled and de-weighted.
- Pad the roadmap with "nice to have" skills to look comprehensive.
- Moralize about hustle, grind, or "investing in yourself."

---

## False-Positive Prevention

1. **Guessed requirements send people the wrong way.** The biggest failure is building a roadmap on what the user *assumes* the target needs. Force the verified/assumed split and de-weight assumptions.
2. **Studying is not a checkpoint.** "I read about X" or "I took a course on Y" is not evidence the skill is at the bar. Every checkpoint must be an observable output or a real-conditions demonstration.
3. **Invisible reskilling doesn't reposition.** A skill learned with no artifact to show is invisible to hiring managers. If a skill can't produce proof, say so — don't count it as repositioning progress.
4. **Don't confuse credential with capability (or vice versa).** Some target roles screen on a specific credential; some screen on demonstrated work. Match the proof artifact to what *this* target actually screens for (input 3), not to what's easiest to earn.
5. **Adjacencies are cheaper than they look — verify the conversion.** A "near-target" skill still needs conversion to the target's context. Don't mark it done because it's close; define the conversion checkpoint.
6. **Time budgets are real.** A roadmap that requires more hours than the user has isn't ambitious, it's a plan to fail. Cut to fit and name the cuts.
7. **Don't duplicate the learning domain.** If the output starts specifying lectures, textbooks, or a week-by-week study syllabus for a skill, it has overstepped into `domain-learning/` territory — stop and hand off.

---

## Output Format

```
## Gap table
| Requirement | Source | Current level | Gap |
|---|---|---|---|
| ... | verified/assumed | none/partial/near-target | large/medium/small/none |

## Dropped (and why)
- [skill] — [no gap / low landing-value / automatable surface area]

## Sequenced roadmap
| Order | Skill | Why here (dependency / proof-value) | Checkpoint (observable) | Proof artifact |
|---|---|---|---|---|
| 1 | ... | ... | ... | ... |
| 2 | ... | ... | ... | ... |

## Fit to time budget
- Available: [hrs/week over horizon]. Roadmap fits: [yes / cut to fit].
- Cut/deferred: [skills] — because [reason].

## How to learn each skill (handoff)
- Per-skill curriculum → domain-learning/learning_curriculum_designer.md
- Practice loop → domain-learning/learning_deliberate_practice_designer.md

## Start this week
- **First block:** [skill], first session = [specific action], by [date].
- Checkpoint you're aiming at: [observable].

Predicted check: by [date], you'll have [the first proof artifact], which the target role screens for because [input 3 source].
```

---

## Verification

- [ ] Target is concrete; refused if vague or fully unverified.
- [ ] Every requirement marked verified/assumed; assumptions de-weighted and warned.
- [ ] Sequence ordered by dependency first, proof-value second.
- [ ] Every sequenced skill has an observable checkpoint and a proof artifact.
- [ ] Low-value and automatable-surface-area gaps flagged and dropped, with reasons.
- [ ] Roadmap cut to the real time budget; cuts named.
- [ ] Per-skill curriculum/practice explicitly deferred to `domain-learning/`.
- [ ] First block is physical and time-bounded; no hustle moralizing.
