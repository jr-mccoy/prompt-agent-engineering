---
title: "Concession Plan — The Ladder, the Decay Curve, and the Reciprocity Rule"
category: negotiation/preparation
description: "Design every concession before the negotiation instead of inventing them under pressure. Builds a ladder with decreasing step sizes (the decay curve that signals you are approaching a limit), attaches a required return to each step so no concession is unilateral, sets the reciprocity rule and what happens when it is broken, and pre-commits the floor. Ends with the pattern the ladder will teach the counterpart, since concession sizes communicate more than words do. Counters the failure the domain's own BATNA prompt flags: entering with a walkaway but no plan for the ground between the opening and it."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - DS-02
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - negotiation
  - concessions
  - reciprocity
  - decay-curve
  - preparation
updated: "2026-07-26"
reasoning:
  styles: [analytic, strategic, adversarial, counterfactual]
  stakes: variable
  horizon: hours
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: variable
  collaboration: solo_or_pair
  output_format: [matrix, structured]
  user_role: [executive, founder, sales, hr, lawyer, individual]
  mode: [plan, decide, rehearse]
related_prompts:
  - domain-negotiation/preparation/negotiation_opening_offer_design.md
  - domain-negotiation/preparation/negotiation_package_trade_design.md
  - domain-negotiation/at-the-table/negotiation_closing_and_final_concession.md
---

# Concession Plan — The Ladder, the Decay Curve, and the Reciprocity Rule

**Objective:** Most negotiators prepare a walkaway and an opening, then improvise everything between them — which is precisely the stretch where the outcome is determined. Improvised concessions are systematically too large, too fast, and unreciprocated, because the pressure to keep the conversation moving is felt in the room and the cost is felt later. This prompt designs the full ladder in advance: each step's size, what it requires in return, and the **decay curve** — steps that get smaller as you descend, which is how a counterpart learns you are approaching a real limit. It sets the **reciprocity rule** (no concession without a return) and the response when they break it, pre-commits the floor, and names the pattern your ladder will teach.

`negotiation_batna_analysis.md` sets the floor; `negotiation_opening_offer_design.md` sets the ceiling. This prompt governs everything in between, and it is the gap that prompt's own "When NOT to use" section flags.

**When to use:**
- Opening offers are designed or exchanged and you need a plan for the ground between them.
- You have a history of conceding faster than intended once the conversation starts.
- The counterpart is a repeat player who will read your concession pattern across this and future deals.
- A multi-round negotiation where the pattern of movement will be as informative as the movements.

**When NOT to use:**
- You have no reservation point yet — a ladder without a floor is a slide. Run `negotiation_batna_analysis.md`.
- The deal is genuinely multi-dimensional and you have not designed the trades — `negotiation_package_trade_design.md` first, because trades are better than concessions and should be exhausted before you start giving ground.
- You are at the final move and need endgame mechanics — `at-the-table/negotiation_closing_and_final_concession.md`.

**Audience:** Executives, founders, salespeople, people leaders, lawyers, and individuals in any negotiation with more than one round of movement.

---

## Inputs / Context

1. **Opening position and reservation point.** The top and bottom of your ladder.
2. **Target.** Where you actually intend to land — usually well above the floor.
3. **Available trades.** From `negotiation_package_trade_design.md` — non-price dimensions you can move instead of price.
4. **Expected number of rounds.** How many exchanges the format allows before a decision.
5. **Counterpart history.** How they have negotiated before, if known — particularly whether they reciprocate.
6. **Time and deadline structure.** Who is under pressure and when.

---

## Constraints

### Must
- Build a ladder from opening to reservation point with **decreasing step sizes**. The decay curve is the signal; uniform steps say "there is always more."
- Attach a **required return** to every step. A concession with no named return is a gift, and gifts train the counterpart to wait rather than reciprocate.
- Exhaust **trades before concessions**. Moving on a dimension they value and you don't is not a concession at all; it should precede every ladder step.
- Set an explicit **reciprocity rule** and the response when it is violated — including the option to withdraw or freeze.
- Pre-commit the **floor** in writing, with the specific sentence to be said when it is reached.
- Plan for **fewer rounds than you expect**. Ladders designed for six rounds routinely have to be executed in three.
- State what the ladder **teaches**: the inference a rational counterpart draws from this pattern of movement.

### Must Not
- Design uniform concession steps. Equal steps signal an inexhaustible supply and invite the counterpart to keep pushing.
- Concede twice in a row without an intervening move from them. This is the single fastest way to lose a negotiation's remaining value.
- Plan to "split the difference" as a step. It is arithmetic, not a concession strategy, and it rewards whoever anchored more extremely.
- Set the last step *at* the reservation point. Landing exactly on the floor leaves no room for the final trade and makes the floor look soft.
- Make the first concession the largest without a reason. A large opening concession discounts the anchor retroactively.
- Treat a concession as reciprocated because the counterpart moved on something trivial. Value the return, don't count it.

---

## Instructions

### Step 1 — Fix the endpoints
State the opening position, the target, and the reservation point. Compute the total distance from opening to floor. This is the entire budget; every step spends from it.

### Step 2 — Exhaust the trades first
List the dimensions you can move that cost you little and are worth something to them. These come *before* any ladder step. Write each as a move with its required return. Only distance you cannot cover with trades goes into the ladder.

### Step 3 — Choose the round count and the decay shape
Estimate rounds available, then plan for one or two fewer. Allocate the remaining distance across steps on a decaying curve — a common shape is roughly halving each time (e.g. 50%, 25%, 15%, 10% of the budget). State the shape and why it fits the counterpart and format.

### Step 4 — Size each step and attach its required return
Build the ladder row by row: step number, the move, its size, what you require in return, and what you will say. The required return should be specific and comparable in value — not "some movement from you," but a named term or number.

### Step 5 — Set the reciprocity rule and the breach response
Write the rule plainly: no step descends without a reciprocal move of comparable value. Then write the breach response — what you do when they take a concession and give nothing. Options, in ascending order: name it and pause, restate the last position and stop, withdraw the concession explicitly, or freeze until they move. Pick a default.

### Step 6 — Pre-commit the floor
Write the reservation point and the exact sentence to be said when reached — a sentence that is calm, final, and does not invite a counter ("That's as far as I can go on this. If that doesn't work, I understand, and we should probably stop here"). Pre-committing the words is what makes the floor hold under pressure.

### Step 7 — Design the reserve and the endgame gap
Deliberately leave a small amount of distance between the last planned step and the reservation point. This reserve is the final closing concession — the thing you give to close, not to continue. Name what it is and the condition under which it is spent.

### Step 8 — State what the ladder teaches
Write the inference a rational counterpart draws from this sequence: step sizes shrinking means a real limit approaching; every step requiring a return means unilateral pressure does not work; a hard stop at the floor means the floor is real. If the ladder teaches something you do not want taught, redesign it.

### Step 9 — Adversarial check
- If they concede nothing for three rounds, what is your actual move — and is it in the plan?
- Which step is largest, and what does its size tell them about the steps below it?
- If time pressure compresses this to two rounds, which steps do you merge, and does the decay curve survive?

---

## False-Positive Prevention

1. **Uniform steps.** Equal-sized concessions communicate an inexhaustible supply. The counterpart correctly infers that pushing again yields the same again. Decay is the whole signal.
2. **Unilateral concessions.** Moving without a required return, usually to "keep momentum." Momentum bought this way is momentum in one direction only. Every step needs a named return.
3. **Consecutive self-concession.** Conceding, receiving nothing, and conceding again — often out of discomfort with silence. This is the fastest known way to surrender remaining value.
4. **Difference-splitting as strategy.** Proposing to split as a concession step. It is arithmetic that systematically rewards the more extreme anchor, and it abandons the justification structure that got you there.
5. **Floor-landing.** Designing the last step to arrive exactly at the reservation point, leaving nothing for the close and making the floor appear negotiable because you arrived there smoothly.
6. **Round-count optimism.** A six-step ladder in a negotiation that will resolve in three exchanges, resulting in improvised jumbo steps. Plan for fewer rounds than expected.
7. **Trivial-return acceptance.** Counting any counterpart movement as reciprocity regardless of value. Value the return against your concession; a token is not a trade.
8. **Trades skipped.** Going straight to the ladder when non-price dimensions were available. Every unit of distance covered by a trade is a unit not spent from the concession budget.

---

## Output Format

```
# Concession Plan — [negotiation]

Opening: [...] · Target: [...] · Reservation point: [...]
Total concession budget: [...]

## Trades first (before any ladder step)
| Move | Costs me | Worth to them | Required return |
|---|---|---|---|
| [...] | low | high | [...] |

## The ladder
Rounds expected: [n] · Rounds planned for: [n-1 or n-2] · Decay shape: [...]

| Step | Move | Size | % of budget | Required return | What I say |
|---|---|---|---|---|---|
| 1 | [...] | [...] | 50% | [...] | "[...]" |
| 2 | [...] | [...] | 25% | [...] | "[...]" |
| 3 | [...] | [...] | 15% | [...] | "[...]" |
| Reserve | [held for the close] | [...] | 10% | [closing condition] | "[...]" |

## Reciprocity rule
Rule: [...]
Breach response (default): [name and pause / restate and stop / withdraw / freeze]
Script on breach: "[...]"

## Floor pre-commitment
Reservation point: [...]
Sentence when reached: "[...]"

## What this ladder teaches
[The inference a rational counterpart draws from the pattern.]
[If undesirable: what was redesigned.]

## Compression plan
If rounds collapse to [n]: merge steps [x] and [y]; decay curve preserved by [...]

## Adversarial check
- Move if they concede nothing for three rounds: [...]
- Largest step and what it signals about what's below: [...]
- Whether decay survives compression: [...]
```

---

## Verification

- [ ] Opening, target, and reservation point stated, with total budget computed.
- [ ] Trades listed and placed before any ladder step.
- [ ] Step sizes decay; no two steps are the same size.
- [ ] Every step has a specific, value-comparable required return.
- [ ] Reciprocity rule stated with a chosen default breach response and a script.
- [ ] Floor pre-committed with the exact sentence to be spoken.
- [ ] A reserve is held between the last planned step and the floor, with its spending condition named.
- [ ] Round count planned below expectation, with a compression plan.
- [ ] The inference the ladder teaches is stated explicitly.
- [ ] Adversarial check covers the no-reciprocity scenario and compression.
- [ ] No uniform step sizes.
- [ ] No step lands exactly on the reservation point.
- [ ] No difference-splitting used as a planned step.
