---
title: "Impasse Breaker — Diagnose the Deadlock Type, Then Apply the Matched Unlock"
category: negotiation/at-the-table
description: "A negotiation has stopped moving. This prompt diagnoses which of five impasses you are in — positional, informational, emotional, structural, or authority — because the unlock for each is different and applying the wrong one entrenches the deadlock. Positional impasses need reframing; informational ones need a contingent term; emotional ones need process, not substance; structural ones need a changed deal shape; authority ones need a different room. Counters the reflex that deepens most deadlocks: applying more of whatever already failed."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - DS-02
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - negotiation
  - impasse
  - deadlock
  - diagnosis
  - unlock
updated: "2026-07-26"
reasoning:
  styles: [diagnostic, analytic, strategic, dialectical]
  stakes: high
  horizon: variable
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: variable
  collaboration: solo_or_pair
  output_format: [structured, ranked_list]
  user_role: [executive, founder, sales, hr, lawyer, individual]
  mode: [diagnose, plan, decide]
related_prompts:
  - domain-negotiation/preparation/negotiation_interest_mapping.md
  - domain-negotiation/preparation/negotiation_package_trade_design.md
  - domain-negotiation/at-the-table/negotiation_authority_mandate_limits.md
---

# Impasse Breaker — Diagnose the Deadlock Type, Then Apply the Matched Unlock

**Objective:** When a negotiation stops moving, the instinct is to apply more of whatever was already being applied — another argument, another small concession, another meeting. That works only if the impasse is the kind that responds to it, and most are not. This prompt diagnoses which of five impasses is actually in play, because the unlocks are not interchangeable and the wrong one entrenches the deadlock. A **positional** impasse (both sides dug into incompatible demands) needs reframing to interests. An **informational** one (the parties forecast the future differently) needs a contingent term, not persuasion. An **emotional** one (someone needs to be heard, or a face-saving route out) needs process, and substantive concessions actively make it worse. A **structural** one (no ZOPA at this deal shape) needs the deal changed or ended. An **authority** one (the person in the room cannot agree) needs a different room. It closes with the test everyone avoids: whether this is an impasse or just a deal that should not happen.

This is the only impasse-breaking prompt in the repo outside family law, where `domain-legal/custody/legal_custody_mediation_impasse_and_package_strategy.md` covers the counsel-facing custody case.

**When to use:**
- A negotiation has stalled across two or more exchanges with no movement.
- The same arguments are being repeated by both sides.
- You are about to concede simply to restart momentum.
- A deal that seemed close has stopped, and you cannot tell why.

**When NOT to use:**
- The negotiation is moving slowly but still moving — slow is not stuck, and intervening can disrupt a working process.
- You have not mapped interests at all; a positional impasse may dissolve under `negotiation_interest_mapping.md` without further machinery.
- The blockage is a specific coercive tactic rather than a genuine deadlock — use `negotiation_hard_bargainer_defense.md`.

**Audience:** Executives, founders, salespeople, people leaders, lawyers, and individuals in a negotiation that has stopped moving.

---

## Inputs / Context

1. **The negotiation and the sticking point.** What specifically is not moving.
2. **The last three exchanges.** What each side said or offered, in sequence.
3. **Current positions.** Where each side stands on the blocked issue, and the gap.
4. **Your reservation point.** Whether the current offer is above or below it.
5. **What has been tried.** Arguments, concessions, or process changes already attempted.
6. **Who is in the room.** And who is not, but decides.

---

## Constraints

### Must
- **Diagnose before prescribing.** Assign one primary impasse type with evidence, and note any secondary type — impasses are frequently layered, and the emotional layer usually sits on top.
- Match the unlock to the **diagnosed type**. Applying a positional unlock to an emotional impasse deepens it.
- Test for the **structural case honestly** — whether a ZOPA exists at all. Most impasse-breaking advice assumes a deal exists to be found, which is sometimes false.
- Identify what **each side would need to be able to say** to their own constituency in order to move. Face is a constraint, not a weakness.
- Offer a **process move** as well as a substantive one. Changing the format — a break, a different channel, a smaller group, a new participant — resolves more impasses than argument does.
- State the **cost of each unlock**, including what it concedes or signals.
- Close with the **should-this-deal-happen** test, honestly answered.

### Must Not
- Recommend splitting the difference as an impasse breaker. It rewards the more extreme position and abandons whatever justification structure existed.
- Treat every impasse as positional. That is the most familiar type and the least common in genuinely stuck negotiations.
- Apply substantive concessions to an emotional impasse. When someone needs to be heard, a concession reads as an attempt to buy them off and confirms they were not heard.
- Assume a deal exists. Some impasses are correct — the parties' requirements genuinely do not overlap.
- Keep negotiating with someone who cannot decide. That is not persistence; it is a category error about who the negotiation is with.
- Break an impasse by conceding below the reservation point and calling it pragmatism.

---

## Instructions

### Step 1 — State the deadlock precisely
Write what is not moving: the issue, each side's current position, the gap, and how many exchanges have produced no movement. Precision matters — "they won't budge on price" and "they won't go below X while we can't go above Y and neither has moved in three rounds" support different diagnoses.

### Step 2 — Run the differential diagnosis
Test each type against the evidence:

| Type | Signature | Evidence to look for |
|---|---|---|
| **Positional** | Both restating incompatible demands | Same arguments repeated; nobody has asked why |
| **Informational** | Disagreement about a future fact | "It won't perform" vs "it will"; both confident |
| **Emotional** | Disproportionate heat; history intruding | Tone shifted; old grievances surfacing; a concession was refused |
| **Structural** | No overlap at this deal shape | Gap exceeds both parties' plausible ranges |
| **Authority** | Movement stops at a fixed point regardless of argument | "I'd need approval"; concessions reverse after breaks |

Assign a primary type with the evidence for it, and name any secondary layer.

### Step 3 — Apply the positional unlock (if diagnosed)
Reframe from positions to interests: ask why the position matters, on both sides. Then look for the trade that satisfies both underlying interests at a different point. Run `negotiation_interest_mapping.md` if not already done, then `negotiation_package_trade_design.md` to build the bridging package. The characteristic move: stop arguing about the number and change what is being counted.

### Step 4 — Apply the informational unlock (if diagnosed)
When the disagreement is about what will happen, stop trying to win it. Design a contingent term that lets each side act on its own forecast — an earn-out, a volume tier, a performance trigger, a review point, a shorter initial term with renewal on evidence. Specify trigger, measurement, and source of truth. The characteristic move: convert the disputed prediction into a term that pays out differently depending on which side was right.

### Step 5 — Apply the emotional unlock (if diagnosed)
Substance is not the lever here. Acknowledge explicitly what the other side has said and why it is reasonable from their position — without conceding on the merits. Then change the process: a break, a different room, a smaller group, a shift from live to written or the reverse, a participant who carries less history. Give them a route back that does not require visibly losing. The characteristic move: address the relationship, then return to the substance unchanged.

### Step 6 — Apply the structural and authority unlocks (if diagnosed)
**Structural:** the current deal shape has no ZOPA. Options in order — add a dimension (change what is being traded), change the timeframe, change the parties, or end it cleanly. Do not grind; grinding a structural impasse costs the relationship and produces nothing. **Authority:** stop negotiating with someone who cannot agree. Options — request the decision-maker, ask what would need to be true for approval, or restructure the ask to fit their actual mandate. Use `negotiation_authority_mandate_limits.md`.

### Step 7 — Design the face-saving route
For whichever unlock you choose, write what each side would be able to **say to their own constituency** to justify moving. Movement is usually blocked less by the terms than by the absence of a defensible story for having moved. A new piece of information, a changed circumstance, a reciprocal move, or an external standard all serve. Provide one.

### Step 8 — Run the should-this-happen test
Independent of momentum and sunk effort: is the deal currently available above your reservation point? Would you enter this negotiation today knowing what you now know? Sunk cost is the reason bad deals close after long impasses. If the answer is no, the impasse is information, not an obstacle.

### Step 9 — Adversarial check
- If you have diagnosed positional, what evidence would indicate it is actually authority?
- Are you breaking the impasse because the deal is good, or because stopping feels like failure?
- What does your chosen unlock concede or signal that you have not priced?

---

## False-Positive Prevention

1. **Positional over-diagnosis.** Defaulting to the most familiar type. Positional impasses are the easiest to see and among the least common in genuinely stuck negotiations. Run the full differential before committing.
2. **Difference-splitting.** Proposing the midpoint to restart movement. It rewards the more extreme anchor, abandons the justification structure, and teaches the counterpart that stalling produces arithmetic.
3. **Substance applied to emotion.** Offering a concession when the actual blockage is that someone feels dismissed. The concession confirms they were not heard and frequently hardens the position.
4. **Structural denial.** Continuing to search for a bridge when the gap exceeds both parties' plausible ranges. This burns the relationship and the calendar to arrive where the first honest look would have.
5. **Negotiating with the wrong person.** Persisting with a counterpart who cannot agree, reading their immobility as toughness rather than as a mandate limit.
6. **Momentum-driven closure.** Breaking the impasse by conceding below the floor because the process has run long. Sunk cost is precisely what makes post-impasse deals worse than pre-impasse ones.
7. **Face-blindness.** Designing a technically sound unlock that requires the counterpart to visibly capitulate. Terms are rarely the binding constraint; the absence of a defensible story for moving usually is.
8. **Unpriced unlocks.** Choosing a bridge without noting what it signals — that your deadline was soft, that your floor moves under pressure, that stalling works on you. The unlock's cost extends into the next negotiation.

---

## Output Format

```
# Impasse Diagnosis — [negotiation]

## The deadlock
Blocked issue: [...]
Your position: [...] · Their position: [...] · Gap: [...]
Exchanges without movement: [n]
What has been tried: [...]

## Differential diagnosis
| Type | Evidence for | Evidence against | Fit |
|---|---|---|---|
| Positional | [...] | [...] | strong/weak |
| Informational | | | |
| Emotional | | | |
| Structural | | | |
| Authority | | | |
**Primary:** [type] — because [...]
**Secondary layer:** [type or none]

## Matched unlock
Unlock: [...]
Characteristic move: [...]
Specific action: [...]
What it costs / signals: [...]

## Process move
[Format change: break / different room / smaller group / channel switch / new participant]

## Face-saving route
What they can tell their constituency to justify moving: "[...]"
What I can tell mine: "[...]"
Basis provided: [new information / changed circumstance / reciprocal move / external standard]

## Should this deal happen?
Current offer vs. reservation point: [above / below]
Would I enter this negotiation today knowing what I know? [y/n]
Verdict: [pursue the unlock / walk]

## Adversarial check
- Evidence that would flip the diagnosis: [...]
- Am I breaking this because the deal is good, or because stopping feels like failure? [...]
- Unpriced cost of the chosen unlock: [...]
```

---

## Verification

- [ ] The deadlock stated precisely, with positions, gap, and exchange count.
- [ ] All five impasse types tested with evidence for and against.
- [ ] A primary type assigned with reasoning, and any secondary layer named.
- [ ] The unlock matches the diagnosed type, not the most familiar one.
- [ ] A process move offered alongside the substantive one.
- [ ] A face-saving route written for both sides, with a named basis for moving.
- [ ] The cost and signal of the chosen unlock stated explicitly.
- [ ] The should-this-happen test answered independently of sunk effort.
- [ ] Adversarial check names the evidence that would flip the diagnosis.
- [ ] No difference-splitting proposed as the unlock.
- [ ] No substantive concession recommended for an emotional impasse.
- [ ] No unlock that requires the counterpart to visibly capitulate.
