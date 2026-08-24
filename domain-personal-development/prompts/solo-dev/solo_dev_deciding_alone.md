---
title: "Make a Consequential Decision Without a Team to Bounce Off"
category: personal-development/solo-dev
description: "Stress-test a solo dev's important decision by constructing a synthetic 'board' of named adversarial roles, forcing each to attack the plan, then converging on one call plus the reversal condition that would change it."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - QA-12
difficulty: intermediate
tags:
  - solo-developer
  - decision-making
  - red-team
  - echo-chamber
  - judgment
updated: "2026-07-23"
related_prompts:
  - domain-personal-development/prompts/solo-dev/solo_dev_pricing_value_confidence.md
  - domain-personal-development/prompts/solo-dev/solo_dev_accountability_system.md
  - domain-personal-development/prompts/agency/agency_weekly_review.md
  - domain-personal-development/prompts/thinking/thinking_blind_spot_mirror.md
  - domain-decision-making/tradeoff_reversibility_stakes_grid.md
---

# Make a Consequential Decision Without a Team to Bounce Off

**Objective:** Replace the missing team by constructing a synthetic "board" of adversarial roles, forcing each to attack the user's leaning decision, and converging on one call plus the single observable condition that would reverse it.

**When to use:** The user faces a real, hard-to-reverse solo decision (kill/keep a feature, take/decline a big client, pivot, rewrite, hire the first contractor) and has no cofounder or teammate to pressure-test it. Also useful when the user notices they've only sought input from people who agree with them. Not for reversible, low-stakes calls — those should be made fast, not run through a board.

**Audience:** An individual deciding for their own business. Not for facilitating someone else's decision, and not clinical. If the decision is entangled with persistent anxiety, paralysis, or dread that outlasts the decision itself, that is not a decision problem — see `domain-psychology/` and a licensed professional.

---

## Inputs Required

1. **The decision, as a binary or small option set.** Stated as a concrete choice with named options, not "what should I do about X." If it's vague, force it into options first.
2. **The current leaning.** Which option the user is actually drawn to, and their honest gut confidence (0–100%).
3. **Reversibility and stakes.** Roughly how hard/expensive it is to undo, and what's at risk if it's wrong (money, months, reputation, the business).
4. **The real reason behind the leaning.** In one honest sentence — including if it's fear, boredom, sunk cost, or someone's offhand comment.
5. **Whose input they've already taken.** Who they've asked and what those people said — to expose whether it's an echo chamber of agreement.
6. **The deadline.** When this must be decided by. If "no deadline," set one — undecided solo decisions rot.

If the decision is genuinely reversible and low-stakes (input 3), do not run the board. Say so, tell the user to just try it and observe, and stop.

---

## Instructions

### Step 1 — Sharpen the decision and the real reason

Restate the decision as clean options. Then name the *actual* driver from input 4 using this fixed taxonomy — because a board can't stress-test a decision whose real basis is hidden:

| Driver | Tell |
|---|---|
| **Evidence** | Points to data/customer signal |
| **Fear** | Avoiding a loss, rejection, or embarrassment |
| **Boredom** | Wants novelty more than the outcome |
| **Sunk cost** | Justified by prior investment |
| **Borrowed opinion** | Traces to one person's remark (input 5) |
| **Optionality** | Wants to keep doors open, avoid committing |

Name it in one line. This driver is what the board must attack hardest.

### Step 2 — Convene the synthetic board

Instantiate exactly four adversarial roles. Give each a one-line mandate and make each speak in first person, arguing *against* the user's leaning from its own vantage. Use these fixed seats:

- **The Skeptic** — attacks the evidence: "what do you actually know vs. assume?"
- **The Operator** — attacks execution: "who does the work, at what cost to everything else you're carrying?"
- **The Customer** — attacks relevance: "does the person paying you care about this at all?"
- **Future-You (12 months on)** — attacks durability: "when this went wrong, what was the tell you ignored today?"

Each seat must raise at least one objection the user did not already list. No seat is allowed to agree with the leaning.

### Step 3 — Force the strongest counter-case

Independent of the board, write the single best argument for the option the user is *not* leaning toward, as if the user had to defend it in a review. If this counter-case is weak, that strengthens the leaning; if it's uncomfortably strong, flag it explicitly — that discomfort is the signal the solo user usually lacks.

### Step 4 — Score the options against fixed criteria

Rate each option 1–5 on: irreversibility cost (lower is safer), downside if wrong, upside if right, load on the user's actual capacity, and evidence support. Present as a table. Do not average into a single winner mechanically — surface which criterion is decisive given input 3's stakes.

### Step 5 — Make one call

Deliver a single recommendation. It may be "proceed with the leaning," "switch," or "the decision is premature — here is the one cheap test that resolves it before the deadline." State the primary reason in one sentence and honestly note the strongest objection it survives (from Step 2 or 3), not a laundry list.

### Step 6 — Set the reversal condition

Name the single observable event that would prove the call wrong, and the date to check it. This converts a lonely one-shot decision into a monitored one — the thing a team would otherwise do for the user. Include how to undo if the reversal condition fires (from input 3's reversibility).

---

## Constraints

### Must
- Instantiate all four board seats, each raising a genuinely new objection.
- Name the real driver from the fixed taxonomy and attack it directly.
- Write the counter-case for the non-leaning option.
- Output exactly one recommendation and exactly one reversal condition with a check date.
- Respect the deadline (input 6) — no "keep gathering input indefinitely."

### Must Not
- Let any board seat validate or flatter the user's leaning.
- Produce a menu of considerations without a call.
- Manufacture certainty on a genuinely uncertain decision — recommend a cheap test instead.
- Fabricate market data, customer sentiment, or outcomes not in the inputs.
- Run the full board on a reversible low-stakes decision.

---

## False-Positive Prevention

1. **A synthetic board is not real customers.** The Customer seat argues from the user's *stated* customer knowledge, not invented data. If that knowledge is thin, the fix is to go ask a real customer, not to trust the simulated one.
2. **Don't let the board become a second echo chamber.** If every seat conveniently supports the leaning, the roles were played too soft — re-run with harder mandates.
3. **Confidence is not correctness.** A high gut number (input 2) is not evidence. Weight Step 4 on evidence support and stakes, not on how sure the user feels.
4. **Not every decision deserves a board.** Over-deliberating reversible calls is its own failure mode; the Step-3 stakes gate exists to catch it.
5. **Sunk cost masquerades as commitment.** When the real driver is prior investment, the board must attack the future value, not honor the past spend.
6. **"Keep options open" can be avoidance.** Flag optionality-driven leanings — refusing to decide is itself an irreversible bet on delay.

---

## Output Format

```
## The decision
Options: [A] vs [B] (vs [C]). Leaning: [X] at [gut %].
Real driver: [taxonomy label] — [one line].

## The board's objections
- Skeptic (evidence): [new objection]
- Operator (execution): [new objection]
- Customer (relevance): [new objection]
- Future-You (durability): [the tell you'd ignore]

## Strongest case for the road not taken
[Best argument for the non-leaning option]. Uncomfortably strong? [yes/no].

## Options scored
| Option | Irrev. cost | Downside | Upside | Load on you | Evidence | Decisive criterion |
|---|---|---|---|---|---|---|

## The call
Recommendation: [proceed / switch / run this cheap test first].
Primary reason: [one sentence]. Survives objection: [the strongest one it beats].

## Reversal condition
This is wrong if [observable event] by [date]. If it fires: [how to undo].
```

---

## Verification

- [ ] All four board seats are present and each raised a new, non-flattering objection.
- [ ] The real driver was named from the taxonomy and attacked, not just noted.
- [ ] The counter-case for the non-leaning option was written and honestly rated.
- [ ] Exactly one recommendation and one reversal condition (with a check date) are produced.
- [ ] Options were scored on stakes and evidence, not on the user's gut confidence.
- [ ] A reversible low-stakes decision would have been sent away without a full board.
- [ ] No customer data, market figures, or outcomes were fabricated.
