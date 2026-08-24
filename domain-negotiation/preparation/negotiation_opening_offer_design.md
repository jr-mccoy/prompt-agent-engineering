---
title: "Opening Offer Design — Whether to Move First, Where to Anchor, and How to Justify It"
category: negotiation/preparation
description: "Decide whether to make the first offer, then design it. Tests the four conditions under which moving first is correct, sets the anchor from your target rather than your floor, and — the part most negotiators skip — builds the justification that makes the anchor survive contact. An unjustified anchor is a number the counterpart discounts; a justified one reframes the whole range. Ends with the response to an extreme counter-anchor. Counters the two default errors: conceding the first move reflexively out of politeness, and anchoring aggressively with nothing behind the number."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - negotiation
  - anchoring
  - opening-offer
  - first-mover
  - justification
updated: "2026-07-26"
reasoning:
  styles: [analytic, strategic, adversarial]
  stakes: variable
  horizon: hours
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: variable
  collaboration: solo_or_pair
  output_format: structured
  user_role: [executive, founder, sales, hr, lawyer, individual]
  mode: [decide, plan, rehearse]
related_prompts:
  - domain-negotiation/preparation/negotiation_batna_analysis.md
  - domain-negotiation/preparation/negotiation_concession_anchoring_plan.md
  - domain-negotiation/preparation/negotiation_leverage_audit.md
---

# Opening Offer Design — Whether to Move First, Where to Anchor, and How to Justify It

**Objective:** The opening offer does more work than any other single move in a negotiation, and it is usually made badly — either surrendered to the counterpart out of a vague sense that going first is a disadvantage, or thrown out as an aggressive number with nothing behind it. This prompt resolves both. It tests the four conditions that determine whether moving first is correct (information position, range knowledge, relationship posture, and convention), sets the anchor from your **target** rather than your floor, and constructs the **justification** — the standard, benchmark, cost basis, or precedent that makes the number look derived rather than demanded. It closes with a prepared response to an extreme counter-anchor, since the most likely reply to a good opening is a bad one.

This is downstream of `negotiation_batna_analysis.md` (which sets the floor and the range) and upstream of `negotiation_concession_anchoring_plan.md` (which governs everything that happens after the first two numbers are on the table).

**When to use:**
- A negotiation is about to begin and you do not know whether to name a number.
- You have a target but no defensible story for it.
- The counterpart is likely to open aggressively and you want a prepared, non-reactive response.
- A previous negotiation of this type opened badly and you want to fix the specific failure.

**When NOT to use:**
- You do not yet know your walkaway or the plausible range — anchoring without a floor risks opening below your own reservation point. Run `negotiation_batna_analysis.md`.
- The negotiation is relationship-primary and naming a number early would itself be the error — use `difficult-conversations/difficultconvo_pre_brief.md`.
- The first offers are already exchanged and you need concession strategy — go to `negotiation_concession_anchoring_plan.md`.

**Audience:** Executives, founders, salespeople, people leaders, lawyers, and individuals about to open a negotiation with material stakes.

---

## Inputs / Context

1. **The negotiation and the primary dimension.** What number or term the opening offer will address.
2. **Your reservation point and target.** From `negotiation_batna_analysis.md`.
3. **What you know about the range.** Market data, comparable deals, published benchmarks, prior transactions.
4. **Information position.** Whether you know more or less than the counterpart about the value at stake.
5. **Convention.** Whether there is an established norm in this context about who opens (many markets have one).
6. **Relationship posture.** How the opening will read given the relationship and its horizon.

---

## Constraints

### Must
- Resolve **whether to move first** by testing all four conditions explicitly, not by preference or habit.
- Set the anchor from the **target**, extended by a justified margin — never from the reservation point, which produces openings that concede the range before it opens.
- Attach a **justification** to the number: a standard, benchmark, cost basis, comparable, or explicit reasoning chain. State it in one sentence the user can actually say aloud.
- Verify the anchor is **ambitious but not absurd**. An anchor outside the range of plausibility damages credibility and can end the negotiation before it starts.
- Prepare the **response to an extreme counter-anchor**, including the option to decline to treat it as a real offer.
- Specify the **precision** of the number and why. Round numbers signal approximation and invite round counters; precise ones signal derivation.
- State what the opening **implicitly concedes**, since every opening defines the dimension being negotiated and forecloses others.

### Must Not
- Open at the reservation point. This is the single most common self-inflicted wound in negotiation — it converts your floor into your ceiling.
- Anchor without justification. An unjustified aggressive number is discounted as noise and costs credibility that a justified one would have built.
- Assume moving first is always advantageous. It is advantageous when you know the range; it is dangerous when you don't, because you may anchor inside their acceptable zone.
- Open with a range. "Somewhere between X and Y" concedes Y instantly; the counterpart hears only the end favourable to them.
- Soften the opening with pre-emptive flexibility ("this is negotiable, obviously"). It discounts the anchor at the moment of delivery.
- Treat an extreme counter-anchor as a number to be split. Splitting the difference with an absurd anchor rewards the tactic and imports it into the midpoint.

---

## Instructions

### Step 1 — Restate floor, target, and range
Write the reservation point, the target, and the plausible range as currently understood. If the range is unknown, say so explicitly — that answer drives Step 2.

### Step 2 — Test the four first-mover conditions
Answer each, then decide:

| Condition | Move first if | Let them open if |
|---|---|---|
| **Information** | You know the value and the range well | You are uncertain about the range |
| **Range knowledge** | You have benchmarks or comparables | You have none and they do |
| **Relationship** | Ambition reads as seriousness here | Ambition reads as aggression here |
| **Convention** | No norm, or norm favours you | A strong norm says they open |

Default: **move first when you know the range**. The anchoring advantage is real but is dominated by the risk of anchoring inside their acceptable zone when you are uninformed.

### Step 3 — If letting them open, prepare the receipt
Write what you will do when their number lands: do not counter immediately, do not react visibly, ask for the reasoning behind it, and re-anchor with your own justified number rather than adjusting theirs. Draft the specific holding line ("Before I respond to that, help me understand how you got there").

### Step 4 — Set the anchor from the target
Take the target and extend it by a margin that leaves room for the concession plan without breaching plausibility. Write the arithmetic explicitly. Confirm the anchor is *above* the target and the target is *above* the reservation point, with usable space between each.

### Step 5 — Build the justification
Identify the strongest defensible basis for the number: a published benchmark, comparable transactions, a cost build-up, a value calculation, precedent, or a policy. Write the one-sentence version to be said aloud. Test it: would a neutral third party find it reasonable? A justification that only works if unexamined is not a justification.

### Step 6 — Run the plausibility test
Check the anchor against the range. Is it ambitious (near the top of what a reasonable counterpart could accept) without being absurd (outside what a reasonable counterpart would treat as serious)? If you cannot name someone who has recently agreed to something in this neighbourhood, the anchor is probably outside the plausible set.

### Step 7 — Set precision and delivery
Choose the number's precision and say why. Then write the actual opening sentence, including the justification, with no hedging, no pre-emptive flexibility, and no trailing question that invites immediate counter. Specify what happens next: silence, and who breaks it.

### Step 8 — Prepare the counter-anchor response
Write the response to an extreme counter. The three usable moves: **name it** ("that's a long way outside anything I've seen — where does it come from?"), **decline to treat it as an offer** and re-state your own with its justification, or **restate the standard** and invite them back to it. Explicitly rule out splitting the difference from an extreme anchor.

### Step 9 — Adversarial check
- If they open first with a number better than your planned anchor, do you have the discipline not to accept immediately?
- What does your opening implicitly concede about which dimension is being negotiated?
- Would your justification survive one pointed follow-up question?

---

## False-Positive Prevention

1. **Floor-anchoring.** Opening at or near the reservation point, usually rationalized as "being reasonable." It converts the floor into the ceiling and guarantees a below-target outcome. Anchor from the target.
2. **Naked anchor.** An ambitious number with no basis. It reads as an opening bid to be discounted rather than a position to be engaged, and it forfeits the credibility a justified number earns.
3. **Reflexive first-mover avoidance.** Declining to open out of a general belief that going second is safer. Going second is safer only when you are uninformed about the range; when you have benchmarks, ceding the anchor is a real cost.
4. **Range openings.** "Between X and Y." The counterpart hears the end that favours them, and you have conceded to it before negotiating.
5. **Pre-emptive softening.** Attaching "of course, there's flexibility" to the opening. Every word of flexibility offered before it is asked for is value given away for nothing.
6. **False precision.** A precise-looking number with no actual derivation behind it. Precision signals derivation; if a follow-up question reveals none, the signal inverts and costs more than a round number would have.
7. **Absurd anchoring.** An anchor so far outside the plausible range that it ends engagement or triggers a matching absurdity. Ambition and implausibility are different things; test against actual comparables.
8. **Difference-splitting from an extreme counter.** Treating an outlandish counter-anchor as a legitimate endpoint and moving to the midpoint. This rewards the tactic and imports the extremity into the outcome. Re-anchor on the standard instead.

---

## Output Format

```
# Opening Offer — [negotiation]

Reservation point: [...] · Target: [...] · Plausible range: [...] (or: unknown)

## First-mover decision
| Condition | Assessment | Points to |
|---|---|---|
| Information position | [...] | move first / let them |
| Range knowledge | [...] | |
| Relationship posture | [...] | |
| Convention | [...] | |
**Decision:** [move first / let them open] — because [...]

## If letting them open
Holding line: "[...]"
Re-anchor plan: [...]

## The anchor
Number/term: [...]
Derivation: target [...] + margin [...] = anchor [...]
Precision chosen: [...] — because [...]
Space check: anchor > target > reservation point — [confirmed]

## Justification
One-sentence version to say aloud: "[...]"
Basis: [benchmark / comparables / cost build-up / precedent / policy]
Neutral-third-party test: [would it be found reasonable? why]

## Plausibility test
Comparable that lands near this anchor: [...]
Verdict: ambitious / absurd — [reasoning]

## Opening sentence (as delivered)
"[...]"
Then: [silence / next move], broken by [whom]

## If they counter-anchor extremely
Chosen move: [name it / decline to treat as offer / restate the standard]
Script: "[...]"
Ruled out: splitting the difference from their anchor.

## Adversarial check
- Discipline risk if their opening beats my anchor: [...]
- What my opening implicitly concedes: [...]
- Justification under one follow-up question: [...]
```

---

## Verification

- [ ] Reservation point, target, and range stated before any anchor is set.
- [ ] All four first-mover conditions tested explicitly, with a stated decision.
- [ ] Anchor derived from the target with visible arithmetic, not from the floor.
- [ ] Space confirmed between anchor, target, and reservation point.
- [ ] Justification written as a single sentence deliverable aloud, with a named basis.
- [ ] Justification passes the neutral-third-party test.
- [ ] Plausibility tested against at least one real comparable.
- [ ] Precision of the number chosen deliberately, with a reason.
- [ ] Opening sentence contains no hedging and no pre-emptive flexibility.
- [ ] Counter-anchor response prepared, with difference-splitting explicitly ruled out.
- [ ] If letting them open, a holding line and re-anchor plan are drafted.
- [ ] Adversarial check names what the opening implicitly concedes.
- [ ] No opening at or below the reservation point.
- [ ] No range offered in place of a number.
