---
title: "Decide Whether Your Next Move Is Internal or External"
category: personal-development/career-transformation
description: "Compare an internal move (new role or expanded scope at the current employer) against an external move (new employer) on growth, leverage, risk, and time-to-impact, using the user's real situation, and issue one recommendation with the disconfirming evidence that would flip it."
techniques:
  - ST-01
  - ST-02
  - RT-05
  - DS-06
  - QA-04
difficulty: intermediate
tags:
  - career
  - internal-mobility
  - job-change
  - decision
  - leverage
updated: "2026-07-23"
related_prompts:
  - domain-personal-development/career-transformation/career_role_structural_vulnerability.md
  - domain-personal-development/career-transformation/career_positioning_statement.md
  - domain-personal-development/career-transformation/career_90_day_repositioning_plan.md
  - domain-personal-development/major-decisions/personal_career_offer_evaluation.md
  - domain-personal-development/prompts/identity/identity_taste_development.md
---

# Decide Whether Your Next Move Is Internal or External

**Objective:** Compare the user's best available **internal** move against their best plausible **external** move on four dimensions — growth, leverage, risk, and time-to-impact — and issue one recommendation, plus the specific evidence that would reverse it.

**When to use:** The user is restless or ready to move and is weighing "push for a new role/scope here" versus "go somewhere new." Also when they have an external offer in hand and haven't seriously modeled the internal counter. Not for: choosing between two *external* offers already in hand (use `major-decisions/personal_career_offer_evaluation.md`), and not for deciding whether to quit with nothing lined up (that's `major-decisions/personal_quit_or_persist.md`).

**Audience:** An individual weighing their own next move. Not clinical. If the restlessness is really burnout or persistent distress, this decision framing won't fix it — see `domain-psychology/` and `major-decisions/personal_quit_or_persist.md` first.

---

## Inputs Required

1. **The internal option, concretely.** The specific role, scope expansion, team, or mandate the user could realistically get where they are — with an honest read on whether it's actually available or wishful. If there's no real internal option, say so; the comparison then becomes "external vs. stay put."
2. **The external option, concretely.** A specific role/type at a specific employer or a narrow class of employers — not "somewhere better." If it's still hypothetical, mark it hypothetical.
3. **What's driving the itch.** Why the user wants to move: more scope, more money, escaping a manager/politics, learning, title, mission, comp ceiling, boredom. Rank the top three.
4. **What the user actually controls at the current employer.** Reputation, relationships, sponsor, track record, domain context — the accumulated capital that resets to near-zero on an external move.
5. **Real constraints.** Money runway, visa/geography, family, notice periods, vesting, non-competes, and how much risk the user can absorb right now.
6. **The last two internal attempts (if any).** Has the user tried to grow internally before? What happened? This is the strongest signal on whether the internal path is real or a mirage.

If both the internal and external options are hypothetical ("maybe I could get X, maybe Y exists"), refuse to score and send the user to make one of them concrete first. You cannot compare two mirages.

---

## Instructions

### Step 1 — Make both options concrete or mark them hypothetical

State the internal and external options as specific roles with specific scope. Flag any that is still hypothetical. A hypothetical option cannot outscore a concrete one on the strength of imagination — weight accordingly and say so.

### Step 2 — Score each option on four dimensions

Grade each option Strong / Even / Weak on each dimension, with evidence from the inputs. Do not average; grade each dimension on its own.

| Dimension | The question |
|-----------|--------------|
| **Growth** | Which option builds scarce, compounding skill (see `career_ai_era_skill_moat.md`) faster — new problems, harder decisions, a steeper learning curve? |
| **Leverage** | Where does the user's accumulated capital (input 4) count for more? Internal moves *keep* leverage; external moves *reset* it but may offer a bigger platform. |
| **Risk** | Failure modes and their cost: internal (stuck under the same ceiling/politics; a "promotion" with no real change) vs. external (bad culture fit, the role isn't as sold, no runway, probation risk). Weight by input 5. |
| **Time-to-impact** | How fast can the user actually *do* the new work and be seen doing it? Internal usually faster (context, trust); external slower (ramp, proving-in). |

### Step 3 — Weight by the real driver

Re-read input 3. The dimension that matters most is set by *why* the user wants to move:
- Driver is **scope/learning** → Growth dominates.
- Driver is **escaping a manager/politics/ceiling** → check whether the internal option actually escapes it, or just relocates the user under the same structure. Often it doesn't — name that.
- Driver is **comp** → be concrete about whether internal can match; internal comp raises are usually capped below external market resets.
- Driver is **boredom** → separate "the work is done here" from "I'm restless everywhere." If input 6 shows repeated internal restlessness, an external move may just reset the clock.

### Step 4 — Run the two failure tests

- **Internal-mirage test:** Given input 6, is the internal option *real* or a pattern of promises that haven't materialized? If the user has been "next in line" before and it didn't happen, discount the internal option hard.
- **Grass-is-greener test:** Is the external option's appeal mostly *escape from* the current situation rather than *movement toward* something specific? If input 3's drivers are all "away from," flag that the external move may not deliver.

### Step 5 — Issue one recommendation and its kill-switch

Recommend **one**: pursue internal, pursue external, or (only if genuinely warranted) run a bounded parallel test (e.g., "make the internal ask explicitly by [date] and take one external conversation; let the internal answer decide"). Do not leave it as "it depends."

Then state the **disconfirming evidence** — the specific fact that, if the user learned it, should flip the recommendation. This is required, per QA-04: the recommendation is only trustworthy if its reversal condition is named.

---

## Constraints

### Must
- Make both options concrete or explicitly mark hypotheticals and weight them down.
- Grade all four dimensions for both options, each with evidence.
- Let the user's actual driver (input 3) set which dimension dominates.
- Run both the internal-mirage and grass-is-greener tests.
- Issue exactly one recommendation plus the evidence that would reverse it.

### Must Not
- Default to "external is growth, internal is safe." Both can be either — grade on evidence.
- Treat a title change as growth without a change in the actual problems the user works on.
- Ignore accumulated capital (input 4) — resetting it is a real, often underpriced cost of external moves.
- Recommend the parallel test as a way to avoid deciding. It's a real option only when the internal answer is genuinely gettable on a deadline.
- Moralize about loyalty, "grinding it out," or "betting on yourself." Compare the options.

---

## False-Positive Prevention

1. **A promotion is not always growth.** More scope on paper with the same decisions, same manager, same ceiling is lateral. Grade growth on the change in *problems worked*, not the change in title.
2. **Escape is not a destination.** If every driver is "away from" (bad manager, politics, boredom), an external move may reproduce the problem elsewhere. Require at least one concrete "toward."
3. **Leverage reset is underpriced.** External candidates routinely underestimate how much of their effectiveness came from relationships and context that don't travel. Don't let the external option's platform dazzle past this.
4. **The internal option can be a mirage.** "They said I'm next" is a claim, not a fact — especially against input 6. Discount internal options with a history of unkept promises.
5. **Comp comparisons must be like-for-like.** Total comp, vesting cliffs, cost-of-living, and lost accrued equity all matter. A bigger base with a worse equity/vesting position can be a pay cut.
6. **Don't over-weight a hypothetical.** An imagined external role has no downsides yet precisely because it isn't real. A concrete internal option with visible flaws can still be the better move.

---

## Output Format

```
## The two options
- **Internal:** [specific role/scope] — [concrete / hypothetical]
- **External:** [specific role/type/employer] — [concrete / hypothetical]

## Scorecard
| Dimension | Internal | External | Evidence |
|---|---|---|---|
| Growth | Strong/Even/Weak | Strong/Even/Weak | ... |
| Leverage | | | ... |
| Risk | | | ... |
| Time-to-impact | | | ... |

## Driver weighting
Top driver: [X] → this makes [dimension] decisive because [reason].

## Failure tests
- **Internal mirage:** [real / discounted — why, citing input 6]
- **Grass-is-greener:** [toward-something / mostly escape — why]

## Recommendation
[Pursue internal | Pursue external | Bounded parallel test with a deadline] — because [the decisive reasoning].

**This flips if:** [specific disconfirming fact the user could learn].

## First action
[Physical, bounded — make the internal ask by [date] / open the external conversation / etc.]

Predicted check: by [date], you'll know [observable — internal answer received / external role confirmed as sold vs. real].
```

---

## Verification

- [ ] Both options stated concretely or marked hypothetical and weighted down.
- [ ] Four dimensions graded for both options, each with cited evidence.
- [ ] The user's real driver sets the decisive dimension.
- [ ] Internal-mirage and grass-is-greener tests both run.
- [ ] Exactly one recommendation, plus the disconfirming evidence that would reverse it.
- [ ] Accumulated-capital reset cost of external moves is priced in.
- [ ] First action is physical and time-bounded.
- [ ] No loyalty/bet-on-yourself moralizing.
