---
title: "Map the Frontier of What a New Capability Unlocks"
category: presentations/visual-planning
description: "When a new capability (an AI model, a tool, an integration) appears, map the frontier it creates: what becomes cheap that was expensive, what becomes possible that wasn't, and — critically — what is still out of reach. Produces a structured map with bands, named examples, and honest limits, not a hype deck."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-01
  - DS-20
  - QA-01
difficulty: intermediate
tags:
  - visual-planning
  - frontier-mapping
  - capability
  - strategy
  - what-becomes-possible
updated: "2026-04-21"
related_prompts:
  - domain-presentations/visual-planning/visualplan_modality_router.md
  - domain-presentations/visual-planning/visualplan_cascade_effects_scan.md
  - domain-presentations/visual-planning/visualplan_visual_qa_harness.md
  - domain-business-strategy/ai-strategy/aistrategy_capability_compounding_evaluation.md
  - domain-business-strategy/ambition-leverage/ambition_insight_to_action_workflow.md
---

# Map the Frontier of What a New Capability Unlocks

**Objective:** Given a specific new capability — a new AI model version, a new tool, a new integration, a new platform feature — produce a three-band map of the frontier it creates: (1) what became cheap that used to be expensive, (2) what became possible that used to be out of reach, and (3) what is still out of reach. Name specific examples per band and specific reasons per limit. Refuse hype-inflected mapping.

**When to use:**
- A leader, team, or IC needs to understand the actionable implications of a new capability before deciding what to build with it.
- Preparing a strategy memo, board section, or planning doc that includes "here's what we should do because of X."
- Comparing two capabilities' frontiers to decide which to adopt.
- Personal recalibration after a meaningful capability release (e.g., "what does this model change for my work specifically?").

**Don't use when:** The capability is aspirational ("what AI will be able to do in 3 years"). This prompt maps a specific capability available today; forecasting frontiers belongs to a different exercise.

**Audience:** A strategist, operator, PM, or IC who will act on the output. Output is a structured map, not a pitch.

---

## Inputs Required

1. **The capability.** Specific: model, version, tool, feature. One sentence of what it does.
2. **The domain.** The area the user wants the frontier mapped for. Mapping all domains at once dilutes. Pick one: "my team's support operation," "our content production," "small-business legal research," etc.
3. **What was expensive or impossible before this capability.** 5–10 concrete things the user has personally experienced as limits. Not general industry observations — things the user has bumped into.
4. **The user's hands-on experience with this capability.** Have they actually used it? On what? What worked and didn't?
5. **The evidence posture.** What the user is willing to claim vs. hypothesize. If they've used it three times, they can claim less than if they've used it 200 times.
6. **The decision downstream.** What the user will do with this map. Changes whether the bands need to be quantitative or qualitative.

If the user hasn't used the capability (input 4), note that the map is a hypothesis map, not a frontier map. Proceed only if the user accepts that framing.

---

## Instructions

### Step 1 — Restate the capability in verb terms

One sentence, action-shaped: "X now does Y at Z cost." Not adjective-shaped ("X is better at language"). Capabilities are measured by what they change, not by their model card.

If the restatement needs qualifications ("in English, for text under 5K tokens, at inference cost $0.03/1K"), include them. Frontier mapping without scope is noise.

### Step 2 — Band 1: What became cheap

Things that were previously possible but expensive (in time, money, skill, or coordination). Now they're cheap enough to do routinely.

Per item:

- **What it is** (specific, named).
- **Prior cost shape** (time, money, skill, coordination, tool access).
- **New cost shape** (concrete, not vibes).
- **Factor of change** (5x? 50x? Order of magnitude is fine.) Grade the confidence of this estimate.
- **What this enables in the user's domain** (input 2), concretely.

Aim for 5–10 items. Fewer means the capability is narrower than claimed; more usually indicates the items are duplicates.

### Step 3 — Band 2: What became possible

Things that were previously out of reach — not just expensive, actually infeasible. These are the qualitatively new frontier. Harder to find than Band 1 items; smaller set usually (2–5).

Per item:

- **What it is** (specific, named).
- **Why it was out of reach before** (what specifically made it infeasible — not "it was hard" but "it required X that didn't exist").
- **What makes it possible now** (tie to the capability).
- **Confidence** that it's really possible, not just imagined. Tie to input 4 (have you done this?).
- **What it enables** in the user's domain.

Be strict. "Possible in principle with enough effort" is Band 1 (became cheaper), not Band 2 (became possible).

### Step 4 — Band 3: What is still out of reach

The limits of the frontier. Hype treats this as empty; good strategy notes treat it as load-bearing. Per item:

- **What it is.**
- **Why it's still out of reach** (specific constraint: capability limit, data limit, cost limit at scale, regulatory limit, trust limit, coordination limit).
- **What would have to change for it to move to Band 2 or 1** (another capability? A dataset? A policy? A different architecture?).
- **Near or far** (a judgment, labeled as such).

Aim for 3–7 items. This is where mapping differs from a pitch — "nothing is out of reach" is never accurate.

### Step 5 — Check the bands against evidence

For each item in Bands 1 and 2:

- Is there an actual instance the user (or a named peer/source) has done it, or is this "should work"? Mark each accordingly.
- For "should work" items, note what would confirm they're real — a specific test the user could run.
- For Band 2 items, scrutinize especially: a commonly-confused failure is treating a cheaper Band 1 item as a new Band 2 item because the speed is so different it feels qualitative.

### Step 6 — Anchor to the user's domain

The map (input 2) isn't "the world" — it's the user's domain. For each item, state the concrete instance in the user's work: "In your support op, this means [specific workflow] becomes [specific change]." If an item can't be anchored to the user's domain, it doesn't belong in this map.

### Step 7 — Call out confidence asymmetries

Some items are more load-bearing for the user's downstream decision (input 6) than others. Call out:

- Items with high downstream impact AND high confidence — these are the action items.
- Items with high downstream impact AND low confidence — these are the verify-first items.
- Items with low downstream impact regardless of confidence — these are noise; trim.

### Step 8 — Dual-failure pass

- **Overreach:** Are any Band 2 claims made without evidence? Downgrade.
- **Under-reach:** Are any "still out of reach" items secretly possible today and the user just hasn't tried? Move to Band 2 with confidence label.

### Step 9 — Verify and output

Run the verification checklist.

---

## Constraints

### Must
- Restate capability in verb terms with scope.
- Three bands, each populated.
- Every item in Bands 1 and 2 has concrete specifics — what, prior cost, new cost, domain instance.
- Band 3 has real limits with reasons, not emptiness.
- Confidence labels on Band 2 claims.
- Map anchors to the user's domain, not generic industry.

### Must Not
- Claim Band 2 items that are actually Band 1 (cheaper, not newly possible).
- Produce an empty Band 3.
- Forecast future capability improvements — this maps today's frontier.
- Include items the user cannot anchor to their domain.
- Use "disruption," "transformation," "game-changer," "revolutionary" as load-bearing words. If removing them breaks the point, the point wasn't strong.
- Rely on vendor claims without the user's own validation.

---

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Let vendor demos count as Band 2 evidence. Demos are Band 2 hypotheses; they need user-side verification.
- Conflate "everyone is talking about X" with "X is on the frontier." Saliency ≠ capability.
- Pretend Band 3 is smaller than it is because an optimistic map feels more motivating. Honest Band 3 is where strategy lives.
- Lump several capabilities together ("AI"). Map one capability at a time; composite maps hide limits.
- Treat a 2x speedup as "became possible." Speed changes reach only past thresholds; name the threshold if claiming one.

✅ **DO:**
- Grade every claim by whether the user has done it, a named peer has done it, a vendor has shown it, or it's inferred.
- Write Band 3 limits with a specific "what would need to change" — the limit's shape is useful.
- Anchor each item to one workflow, team, or artifact in the user's domain.
- Distinguish "became possible for one person" (Band 2, narrow) from "became possible at scale" (Band 2, broader) — these are different frontiers.
- Acknowledge when the user's experience (input 4) is thin; the map is a hypothesis map.

---

## Dual-Failure Prevention (QA-20)

❌ **HARMFUL failure:** Map promotes Band 1 items to Band 2, user bets a product decision on a qualitative change that isn't there, effort is wasted on "new" work that's just marginally-cheaper old work.

❌ **UNHELPFUL failure:** Map hedges every item to the point of no signal. User ends with no clearer sense of what to do.

✅ **Quality check:** A skeptical peer reading the map can point to any Band 2 item and ask "has anyone actually done this?" and get a named instance (or an honest "not yet — here's the test").

---

## Output Format

```markdown
# Capability Frontier Map — [Capability], [Domain]

## Capability (verb form + scope)
[One sentence with the scope/qualifiers.]

## Band 1: Became Cheap
| # | What | Prior cost | New cost | Factor | Domain instance | Evidence grade |
|---|------|-----------|----------|--------|-----------------|---------------|
| 1 | | | | | | [done by user / by peer / demo / inferred] |

## Band 2: Became Possible
| # | What | Why infeasible before | What makes it possible now | Domain instance | Evidence grade | Confidence |
|---|------|----------------------|---------------------------|-----------------|---------------|-----------|
| 1 | | | | | | High / Med / Low |

## Band 3: Still Out of Reach
| # | What | Constraint type | What would need to change | Near / far |
|---|------|----------------|--------------------------|-----------|

## Confidence Asymmetries
- High impact + high confidence (act): 
- High impact + low confidence (verify first): 
- Low impact (trim or note): 

## Verify-First Tests
- [For each low-confidence high-impact item, a specific test the user can run this week.]

## Honest Caveats
- [User's hands-on experience level; breadth of capability test; any known blind spots in this map.]
```

---

## Verification

- [ ] Capability restated in verb form with scope.
- [ ] Three bands populated, none empty.
- [ ] Every Band 1 and 2 item has concrete specifics and a domain instance.
- [ ] Every Band 2 item has an evidence grade and a confidence label.
- [ ] Band 3 items name a specific constraint and what would change.
- [ ] Confidence asymmetries section tied to input 6.
- [ ] Verify-first tests named for low-confidence high-impact items.
- [ ] No hype vocabulary carrying meaning.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Output is a three-band capability map with evidence, not a capability pitch.
- **ST-02 (Structured Sequential Instructions):** Nine steps force restatement → Band 1 → Band 2 → Band 3 → evidence check → domain anchor → asymmetries → dual-failure pass → verify.
- **CM-02 (Constraint Specification):** Must Not block forbids composite capabilities, future forecasting, and hype vocabulary.
- **DS-01 (Framework Application):** Three-band framework (cheap / possible / out-of-reach) is the spine.
- **DS-20 (Frontier Mapping):** The capability-classification technique — what became cheap vs what became qualitatively new — is the load-bearing analytic move.
- **QA-01 (Self-Verification):** Verification checklist and evidence grades catch Band 1 items masquerading as Band 2 before the map drives a decision.
