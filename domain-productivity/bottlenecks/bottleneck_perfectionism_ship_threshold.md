---
title: "Set a Ship Threshold and Test It Against Polish Behavior"
category: productivity/bottlenecks
description: "For a near-finished artifact, define explicit ship criteria, audit current polish behavior against them, and decide ship-now vs. one-more-pass with a bounded budget."
techniques:
  - ST-01
  - ST-02
  - QA-08
  - QA-09
  - CM-02
difficulty: intermediate
tags:
  - perfectionism
  - shipping
  - threshold
  - polish
  - bounded-budget
updated: "2026-05-08"
related_prompts:
  - domain-personal-development/prompts/agency/agency_ship_sprint_design.md
  - domain-personal-development/prompts/agency/agency_stuck_diagnosis.md
  - domain-productivity/bottlenecks/bottleneck_procrastination_systems_diagnostic.md
  - domain-personal-development/prompts/agency/agency_decision_post_mortem.md
---

# Set a Ship Threshold and Test It Against Polish Behavior

**Objective:** For a near-finished artifact, define an explicit ship threshold (criteria the artifact must meet to ship), audit current polish behavior against it, and decide either *ship now* or *one more pass with a bounded budget*. Refuse open-ended polish loops.

**When to use:** A specific artifact (post, deck, doc, feature, talk, design) is near completion. The user keeps polishing it. Days are passing. Distinct from `agency_ship_sprint_design.md` (sprint-scope, upstream); this is a single-artifact ship-decision at the end of the work.

**Audience:** An individual deciding whether to ship a specific artifact today. Not for team-level shipping decisions involving review processes, regulatory holds, or coordinated launches — those have their own criteria.

---

## Inputs Required

1. **The artifact.** What it is, in one sentence. Title or filename if applicable.
2. **The audience.** Who is it for? Specific. "Three people on the team," "1,000 readers on a blog," "a hiring manager."
3. **The purpose.** What is it supposed to *do* in the audience? Inform? Persuade? Hire? Land a contract? Win a vote?
4. **Current state.** What's done, what's "left" (in the user's mind).
5. **Last 5 polish actions.** What the user actually did to it in the last few sessions — word changes, format tweaks, source-checks, layout passes, headline rewrites. Specific.
6. **What would need to be true for the artifact to fail in the audience?** Concrete failure modes: misunderstood, misquoted, ignored, rejected, mocked, embarrassing factual error, regulatory issue.
7. **Time spent on it so far.** Rough hours.
8. **Time the user *thinks* the polish-to-shippable phase will take.** Their own estimate.
9. **What's at stake in shipping vs. holding.** Reputation, deadline, downstream dependency, opportunity cost of not-shipping, opportunity cost of shipping-wrong.

If input 4 ("what's left") is greater than 25% of the work, this isn't a perfectionism prompt — the work isn't actually near done. Refuse and route to `agency_ship_sprint_design.md`.

---

## Instructions

### Step 1 — Define the ship threshold (QA-08 gate-based)

Construct a 3-criterion ship threshold for this artifact. Most artifacts ship at this minimum; further polish is optional and bounded.

| Criterion | Question | Default standard |
|---|---|---|
| **A. Purpose-fit** | Does the artifact accomplish input 3 well enough to be functional with the input 2 audience? | The audience can take the intended action / form the intended understanding. |
| **B. Failure-mode avoidance** | Are the input 6 failure modes adequately mitigated? | No factual errors that would embarrass; no misreads that would damage; no broken functional elements (links, citations, key data). |
| **C. Reversibility** | If the artifact ships and is wrong, can the user correct it? | A correction is possible within hours/days at low cost — see `QA-09`. |

For each criterion, write the artifact-specific version. Examples:

- A (post): "A reader of input 2 type can finish in < 5 minutes and walk away with the central claim and one supporting argument."
- B (post): "No misquoted person; no claim attributed to the wrong source; no broken link in the first 3 references."
- C (post): "Edits possible within 24 hours; a correction post / addendum is acceptable to this audience."

Do **not** add criteria for craft, polish, beauty, or completeness beyond functional. Those are optional, not threshold.

### Step 2 — Score the artifact against the threshold

For each criterion, mark Pass / Fail / Marginal with one-sentence evidence.

- All three Pass → the artifact is shippable now.
- Any Fail → the work is genuinely incomplete; one more pass is warranted, scoped to the failed criterion only.
- Any Marginal → judgment call. Default to ship unless input 9 stakes are unusually high or input 6 failure modes are catastrophic.

### Step 3 — Audit input 5 (recent polish actions) against the threshold

For each of the last 5 polish actions, ask: did this action move the artifact toward Pass on any criterion, or was it craft-polish above threshold?

| Recent polish action | Was this against criterion A, B, C — or above-threshold polish? |
|---|---|

If 4 of 5 actions were above-threshold polish, the user is in a polish loop. Name it. The artifact has been shippable for [estimate] hours; the polish is consuming time without moving the threshold.

If 4 of 5 actions targeted A, B, or C and the artifact is still Marginal, the user is *not* in a polish loop — the work is genuinely incomplete. Route to a bounded one-more-pass.

### Step 4 — Run the inversion check (QA-09 reversibility)

Force the question: *if the artifact ships now and is suboptimal in the way the user fears, what is the actual cost?*

- Cost: name the realistic worst case in the input 2 audience. Be specific. ("Three people on the team will have a slightly weaker first impression of my analysis." Not: "it will ruin my reputation.")
- Reversibility: how would the user correct it? At what cost? In what time frame?

Compare against the ongoing cost of *not* shipping. Both have costs; perfectionism over-weights the ship-cost and under-weights the hold-cost. Surface both.

### Step 5 — Decide and bound

Three possible decisions:

**Ship now.** All Pass on threshold; recent polish actions are above-threshold; inversion check shows hold-cost ≥ ship-cost. The decision is to ship today, by [specific time].

**One more pass — bounded.** A specific criterion is Fail or Marginal. The pass is scoped to that criterion only. The budget is bounded:

- ≤ 25% of input 7's already-spent hours, capped at 4 hours.
- Specific list of changes the pass will make. No others.
- Specific deadline (often: end of today).

After the bounded pass, ship — without re-evaluating. The whole point of bounded is to remove the re-evaluation loop.

**Reset scope (rare).** The artifact is genuinely not what the user wants to ship and the threshold can't be met. Route to `agency_ship_sprint_design.md` for a fresh sprint or to `agency_stuck_diagnosis.md` for diagnosis (Cause #8 fear-of-shipping or Cause #1 undefined outcome).

### Step 6 — Set the ship action explicitly

State the physical ship motion: hit publish, send the email, push the file, post the link, submit. With a specific time.

If the user wants to schedule rather than ship, note that scheduled-publishing is a legitimate ship motion — the action is committing to the schedule, not deferring.

### Step 7 — Refuse the polish-comeback

State explicitly: after Step 6's ship motion completes, opening the artifact to make further changes is a polish loop. The artifact is shipped. Future improvement comes through a *new* artifact (v2) or an addendum, not by re-editing the shipped one.

---

## Constraints

### Must
- Construct the 3-criterion ship threshold artifact-specifically.
- Score the artifact Pass / Fail / Marginal against each criterion.
- Audit input 5 against the threshold to surface polish loops.
- Run the inversion check, surfacing both ship-cost and hold-cost.
- Output one of: Ship now / One more pass (bounded) / Reset scope.
- If "one more pass," bound the budget (time and specific changes).
- State the physical ship motion with a specific time.

### Must Not
- Add quality criteria beyond purpose-fit, failure-mode avoidance, and reversibility.
- Recommend "make it your best work." Threshold is functional, not optimal.
- Allow open-ended "one more pass" — must be bounded.
- Recommend re-opening the artifact post-ship for non-correction edits.
- Route to therapy or "address the root of perfectionism" — out of scope. Refer to personal-development if user wants the deeper work, but do not skip the ship decision.

---

## False-Positive Prevention

1. **Don't accept the user's claim that the work is "almost done" without checking against input 4.** "Almost done" with 25%+ remaining is incomplete, not perfectionism.
2. **Don't add craft/aesthetic criteria to the threshold.** Threshold is what makes it ship. Craft beyond threshold is optional.
3. **Don't accept "one more pass" without bounded scope.** Unbounded one-more-pass is the polish loop the prompt exists to break.
4. **Don't moralize about perfectionism.** The output is a ship decision, not a character lecture.
5. **Don't conflate this with `agency_ship_sprint_design.md`.** That's sprint-scope and upstream. This is per-artifact and at the threshold.
6. **Don't use this for genuinely high-stakes / irreversible artifacts** (regulatory filings, legal documents, irreversible communications). Reversibility (Criterion C) will fail; a different process applies.
7. **Don't recommend "ship faster next time."** That's a habit-level question; this is a single-artifact decision.

---

## Output Format

```
## Artifact
[Restated input 1.]

## Ship threshold (this artifact)
| Criterion | Standard | Pass / Fail / Marginal | Evidence |
|---|---|---|---|
| A. Purpose-fit | ... | ... | ... |
| B. Failure-mode avoidance | ... | ... | ... |
| C. Reversibility | ... | ... | ... |

## Recent polish audit (input 5)
| Polish action | Targeted A/B/C, or above-threshold? |
|---|---|
| ... | ... |
**Pattern:** [polish loop / genuine completion / mixed]

## Inversion check
**Realistic worst case if shipped now:** [specific, in input 2 audience]
**Reversibility cost:** [how/when correction is possible]
**Cost of holding:** [opportunity / deadline / momentum cost]

## Decision
**[Ship now / One more pass — bounded / Reset scope]**

[If Ship now: ship motion at [specific time].]
[If One more pass: budget = [hours, ≤ 25% of input 7]; scoped to criterion [A/B/C]; specific changes: [list]; deadline = [time]; **after this, ship without re-evaluating.**]
[If Reset scope: route to `agency_ship_sprint_design.md` or `agency_stuck_diagnosis.md`.]

## Ship motion (physical action)
[The literal action: publish, send, post, push, submit. At [time].]

## Post-ship rule
After the ship motion, opening the artifact for non-correction edits is a polish loop. Future improvement = v2 or addendum, not re-editing the shipped artifact.
```

---

## Verification

- [ ] Ship threshold built with three criteria (no more).
- [ ] Each criterion scored Pass / Fail / Marginal with evidence.
- [ ] Recent polish audit performed; loop pattern named.
- [ ] Inversion check surfaces both ship-cost and hold-cost specifically.
- [ ] Decision is one of: Ship now / One more pass (bounded) / Reset scope.
- [ ] If one more pass, budget and scope are bounded explicitly.
- [ ] Ship motion stated with a specific time.
- [ ] Post-ship rule (no re-editing) included.
