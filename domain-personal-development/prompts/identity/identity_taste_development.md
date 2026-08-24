---
title: "Develop Discernment in a Specific Domain"
category: personal-development/identity
description: "Build a structured taste-training loop in a chosen domain — exposure schedule, judgment exercises, feedback loop, reference-class library — rather than passive consumption. Distinct from technical skill-gap reframing."
techniques:
  - ST-01
  - ST-02
  - ED-02
  - DS-04
  - ED-05
difficulty: intermediate
tags:
  - taste
  - discernment
  - aesthetic-judgment
  - identity
  - expertise
updated: "2026-05-08"
related_prompts:
  - domain-personal-development/prompts/agency/agency_skill_gap_reframe.md
  - domain-personal-development/prompts/identity/identity_values_clarification.md
  - domain-prompt-engineering/evaluation/taskdifficulty_calibrated_comparison.md
  - domain-personal-development/prompts/agency/agency_proof_of_work_portfolio.md
---

# Develop Discernment in a Specific Domain

**Objective:** Design a structured taste-training loop for a chosen domain — exposure schedule, judgment exercises, feedback loop, and reference-class library — so the user develops calibrated discernment rather than passive consumption. Output: a 90-day plan with weekly cadence, a starting reference set, and explicit criteria for what "improving taste" looks like.

**When to use:** The user is operating in a domain where *judgment* matters more than *technique* (writing, design, hiring, investing, music, photography, product decisions, code architecture, food, wine, anything where "knowing good when you see it" is the value), and they sense their judgment isn't yet calibrated. Distinct from `agency_skill_gap_reframe.md` (technical skill); taste is the discernment dimension *underneath* the skill.

**Audience:** An individual deliberately developing taste in a specific domain. Not for assessing other people's taste. Not for general "appreciate art more" — the prompt requires a specific, narrow domain.

---

## Inputs Required

1. **The domain.** Specific. Not "art" — "small-format watercolor portraits." Not "writing" — "longform tech essays" or "literary short stories." Not "code" — "Go service architecture for high-throughput systems." If the user can't narrow, refuse and ask for narrower scope; taste-training in a wide domain is too sparse to converge.
2. **Why this domain matters to the user.** What decisions will improved taste change? Hiring? Writing? Buying? Reviewing? Building? "Just because I like it" is acceptable — but state it.
3. **Current self-assessment.** On a 1–10 scale, where does the user place their current taste in this domain, and what's their evidence?
4. **Practitioners / sources whose taste the user already trusts in this domain.** 3–8 names. People they would defer to. If the user can't name any, that's a finding — the user has no reference class yet, and that's the first move.
5. **What the user has consumed in this domain in the last 90 days.** Rough volume: pieces, books, hours, examples. Was consumption deliberate or ambient?
6. **An example of a recent judgment call the user made (or refused) in this domain.** What they thought was good or bad, and what they did about it.
7. **Time available for taste-training.** Honest minutes per week. Cap at ~ 3 hours per week — beyond that, taste plateaus from over-exposure without reflection.
8. **The user's available "compare-against" reality.** Will the user actually produce / decide / deploy in this domain? (Hiring decisions, writing pieces, buying, building — anything where their judgment will be tested.)

If input 8 is "no" — the user wants to develop taste in a domain where they will never produce, decide, or deploy — note that this is appreciation, not taste. Different prompt is appropriate (general curiosity / domain-learning), but taste-training without testing fails. Either confirm with the user that this is the limit (and run a reduced version of the prompt) or redirect.

---

## Instructions

### Step 1 — Confirm and narrow the domain

Restate the domain in narrowed form. If input 1 was already narrow enough, confirm. If not, propose a narrower version:

- "Photography" → "color photography of urban environments, mid-format."
- "Writing" → "longform argumentative essays, 3000–8000 words, single-author."

A narrowed domain is one where the user can name an exemplar and a near-miss, and explain what makes one better than the other.

### Step 2 — Build a reference-class library (ED-05 priming)

The reference class is the single highest-leverage step. Goal: assemble a starting set of 12–25 specific works — not creators, *works* — that span the quality gradient in the domain.

Categories within the library:

- **Top-tier (5–8 works):** widely considered exemplary by trusted practitioners (input 4).
- **Mid-tier (5–8 works):** competent, instructive, but not exemplary. Often the most useful for taste calibration — they show the line between adequate and great.
- **Failed-promise tier (3–6 works):** ambitious works that did not land, by recognized creators. Demonstrate why ambition alone isn't taste.
- **Out-of-domain anchors (2–4 works):** taste-equivalent works in *adjacent* domains, useful for contrast.

If input 4 is empty (the user can't name trusted practitioners), the first 30 days of the plan is to build that list. The user can't develop taste in isolation from a reference class; they have to find people whose judgment they trust first.

### Step 3 — Design the weekly exposure schedule

Within the budget of input 7, allocate weekly time across:

- **Deliberate exposure:** ~ 50% of budget. One work per session, full attention, no skimming.
- **Reflection:** ~ 25% of budget. After each exposure, written response (not review — *response*: what worked, what didn't, why, what choices the maker made).
- **Comparison:** ~ 15% of budget. Two works held side-by-side; what makes one better than the other, in concrete terms.
- **Production / decision:** ~ 10% of budget. Connect to input 8: actually use the developing taste on something — make a hiring call, write a piece, buy a thing, ship a decision.

Output a weekly cadence: Monday X, Wednesday Y, Saturday Z. Specific times if helpful.

### Step 4 — Design the judgment exercises (DS-04 pattern recognition)

Three exercises run on rotation, weekly:

**Exercise A: Forced Ranking.** Pick 3 works from the reference library. Rank them. Justify the ranking in writing. Compare against any rankings from trusted sources (input 4).

**Exercise B: One-Word Difference.** Pick a top-tier work and a mid-tier work. In one sentence, name the specific thing the top-tier did that the mid-tier didn't. Force concreteness — "more depth" doesn't count; "the second movement abandons the original meter without warning, and the listener has to resolve it" does.

**Exercise C: Reverse Engineer the Decision.** Pick one work. Ask: at three specific decision points the maker faced, what did they choose, and what was the alternative? You're learning to see the maker's choices.

Goal: increase the granularity of the user's vocabulary about the domain. Vocabulary is taste, slowed down to the speed of conscious thought.

### Step 5 — Design the feedback loop

Without a feedback loop, taste-training drifts. Build in two feedback mechanisms:

1. **Predictive calibration.** Before reading any external review or seeing the consensus on a work, the user writes their own assessment. Then check: does the user's assessment converge or diverge with trusted sources (input 4)? Track the convergence over 12 weeks; calibration is improving when divergence has a *reason* the user can articulate.

2. **Production feedback (only if input 8 is yes).** When the user makes a real decision / produces a real piece in the domain, capture: what was decided, the reasoning, the outcome. Over time this builds the user's track record.

If input 8 is no, only Mechanism 1 applies, and the user is working at higher risk of plateau.

### Step 6 — Define the 90-day check

State explicitly what "improving taste" looks like at day 90. Concrete signals:

- **Vocabulary growth.** The user can articulate specific differences between works in the domain at finer granularity than at day 0. Ten new domain-specific terms or distinctions, in active use.
- **Convergence with trusted sources.** Predictive assessments converge with input 4's reference set, *or* the user can articulate where and why they diverge (informed disagreement).
- **Forced-ranking consistency.** If the user re-ranks 5 works at day 0 and day 90 (without seeing day 0's ranking), the day 90 ranking is more consistent with itself across multiple sittings.
- **Decision improvement (if input 8).** The user's recent judgment calls in the domain are concrete enough that they can be defended specifically, not just by feel.

If at day 90 none of these have moved, the loop wasn't real — likely the exposure was passive, or the reference class was wrong, or the time budget was too low. Re-run the prompt with the diagnosis.

### Step 7 — Refuse the credentialing fallacy

Close with explicit refusal:

- This prompt does not claim taste develops in 90 days; it claims a deliberate loop produces measurable movement in 90 days that compounds over years.
- This prompt does not produce credentials, certifications, or "expert" status. Taste is private and provable only by consistent judgment over time.
- This prompt does not require the user to like what trusted practitioners like. Calibrated divergence is part of mature taste; uncalibrated agreement is not.

---

## Constraints

### Must
- Narrow the domain to an actionable specific.
- Build a reference-class library in the four-tier structure.
- Allocate weekly time across exposure / reflection / comparison / production within the input 7 budget.
- Design the three judgment exercises on rotation.
- Build at least Mechanism 1 (predictive calibration) into the feedback loop.
- Define the 90-day check with concrete signals.

### Must Not
- Recommend "consume more of [domain]" as the plan. Volume without structure plateaus.
- Recommend that the user adopt the views of trusted practitioners. Taste is calibration, not mimicry.
- Treat this as appreciation if input 8 is yes; treat as taste-training in that case.
- Recommend "trust your gut" — the prompt is the opposite of that.
- Promise a credential, expert status, or measurable IQ-of-domain.

---

## False-Positive Prevention

1. **Don't run this in a too-wide domain.** "Taste in writing" is not narrow enough. Force narrower scope or refuse.
2. **Don't skip the failed-promise tier of the reference library.** Most taste-training reference sets are top-tier only, which produces shallow taste. Failed-promise works are where taste is sharpened — they show the line.
3. **Don't accept "I don't know any practitioners I trust."** That's the first finding. The first 30 days are then about building the trusted reference list, not about works.
4. **Don't run more than 3 hours per week.** Beyond that, exposure outpaces reflection and the loop fails.
5. **Don't conflate vocabulary growth with real calibration.** A user with new domain terms but no convergence to trusted sources is parroting, not calibrating.
6. **Don't recommend the user become a critic of the domain.** Critics aren't always tasteful; tasteful people aren't always critics. The output is judgment, not commentary.
7. **Don't treat this as an upgrade for `agency_skill_gap_reframe.md`.** That prompt is for technical skill. This is for judgment. Many real domains require both, run in parallel.

---

## Output Format

```
## Domain (narrowed)
[Specific.]

## Why it matters
[Restated input 2 — including, if applicable, "this is appreciation, not taste, because input 8 is no."]

## Reference-class library
- **Top-tier:** [5–8 specific works]
- **Mid-tier:** [5–8 specific works]
- **Failed-promise tier:** [3–6 specific works]
- **Out-of-domain anchors:** [2–4 specific works]

(If input 4 was empty: "First 30-day move: build the trusted-practitioner list. Specific actions: [...]")

## Weekly cadence (within [N] minutes / week)
| Day | Activity | Time |
|---|---|---|
| ... | ... | ... |

## Judgment exercises (on rotation)
- **Exercise A — Forced Ranking:** [described]
- **Exercise B — One-Word Difference:** [described]
- **Exercise C — Reverse Engineer the Decision:** [described]

## Feedback loop
- **Predictive calibration:** [protocol — assess first, check against trusted sources]
- **Production feedback:** [protocol if input 8 is yes; otherwise: skipped, with the plateau risk noted]

## 90-day check
At day 90, the following should be observable:
- Vocabulary: ≥ 10 new domain-specific terms in active use.
- Convergence: predictive assessments converge with reference set, or divergence is articulable.
- Forced-ranking consistency: re-rank at day 90 is internally consistent across sittings.
- Decision improvement: [if input 8] judgment calls defensible specifically.

## What this prompt is not doing
- Not promising taste in 90 days.
- Not credentialing.
- Not requiring agreement with practitioners.
```

---

## Verification

- [ ] Domain narrowed to a specific, actionable scope.
- [ ] Reference-class library built in four tiers.
- [ ] First-30-days task assigned if input 4 was empty.
- [ ] Weekly cadence fits within input 7's budget.
- [ ] Three judgment exercises designed on rotation.
- [ ] Predictive calibration loop included; production feedback included if input 8 is yes.
- [ ] 90-day check stated as concrete signals.
- [ ] No "trust your gut" advice; no credentialing claim.
