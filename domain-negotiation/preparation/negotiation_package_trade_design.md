---
title: "Package and Trade Design — Log-Rolling, MESOs, and Contingent Terms"
category: negotiation/preparation
description: "Convert a mapped set of interests into actual offers. Scores every negotiable issue by how much each side values it, finds the asymmetries that make log-rolling profitable, assembles two to four packages of equivalent value to you but different shape to them (MESOs), and designs contingent terms that bridge disagreements about the future rather than splitting the difference on them. Counters the failure that wastes most of the value in multi-issue deals: negotiating issues one at a time in sequence, which converts every trade into a concession."
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
  - packages
  - log-rolling
  - mesos
  - contingent-terms
updated: "2026-07-26"
reasoning:
  styles: [analytic, strategic, constructive, dialectical]
  stakes: variable
  horizon: variable
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: variable
  collaboration: solo_or_pair
  output_format: [matrix, structured]
  user_role: [executive, founder, sales, hr, lawyer, individual]
  mode: [plan, design, decide]
related_prompts:
  - domain-negotiation/preparation/negotiation_interest_mapping.md
  - domain-negotiation/preparation/negotiation_concession_anchoring_plan.md
  - domain-negotiation/preparation/negotiation_batna_analysis.md
---

# Package and Trade Design — Log-Rolling, MESOs, and Contingent Terms

**Objective:** `negotiation_interest_mapping.md` finds where value could be created. This prompt builds the offers that capture it. It scores every negotiable issue on a common scale for both sides, identifies the **asymmetries** — issues you value far more or far less than they do — and turns each asymmetry into a trade. It then assembles **MESOs**: two to four packages of roughly equal value to you but materially different shape to them, offered simultaneously. MESOs do two jobs at once: they signal flexibility without conceding value, and the counterpart's preference among them reveals their true priorities more reliably than any question. Finally it designs **contingent terms** for issues where the disagreement is about what will happen rather than about who gets what — because a contingency lets both sides act on their own forecast instead of splitting the difference between them.

This presupposes the interest work is done. Run `negotiation_interest_mapping.md` first; without a valuation asymmetry to exploit, package design degenerates into repackaging the same concession.

**When to use:**
- The deal has three or more negotiable dimensions and you have been treating it as one.
- You have mapped interests and need to convert them into offers you can actually put on the table.
- The negotiation is stuck on one axis (usually price) and you need to widen it.
- The two sides disagree about a future fact — volume, performance, timeline, market conditions — and that disagreement is blocking the deal.
- You want to learn the counterpart's priorities without asking questions they have an incentive to answer strategically.

**When NOT to use:**
- Genuinely single-issue negotiations where price is the only variable and no dimension can be added — use `negotiation_batna_analysis.md` and `negotiation_concession_anchoring_plan.md`.
- You have not yet mapped interests — the valuation scores will be guesses stacked on guesses. Run `negotiation_interest_mapping.md` first.
- The counterpart has authority over only one dimension; packages spanning dimensions they cannot decide will stall on ratification. Check `at-the-table/negotiation_authority_mandate_limits.md`.

**Audience:** Executives, founders, salespeople, people leaders, lawyers, and individuals negotiating any multi-dimensional deal — employment, vendor contracts, partnerships, term sheets, service agreements.

---

## Inputs / Context

1. **The negotiation and its issues.** Every negotiable variable, including ones considered fixed — those are often where the cheapest concessions live.
2. **Interest map.** Output of `negotiation_interest_mapping.md`, or the equivalent understanding of what each side actually needs.
3. **Your reservation point and target.** From `negotiation_batna_analysis.md` — the floor a package must clear.
4. **Known constraints.** Terms either side cannot move for policy, legal, budget, or precedent reasons.
5. **Disputed future facts.** Anything the two sides forecast differently — volume, performance, adoption, timing, market direction.
6. **Relationship horizon.** Whether contingent terms will be administered cooperatively or litigated.

---

## Constraints

### Must
- Score **every** issue for both sides on a common scale (a 100-point allocation per side works well), and state the basis for each score.
- Mark counterpart scores with **confidence** (known / inferred / guessed). The asymmetries you act on must be traceable to evidence.
- Identify asymmetries explicitly and state the **direction of trade** for each: what you give, what you get, why both sides gain.
- Build **2–4 MESOs of equivalent value to you**, each materially different in shape. Equivalence is what makes them safe to offer simultaneously.
- Ensure every package clears your **reservation point**. A MESO set containing one package below your floor is a trap you built yourself.
- Design at least one **contingent term** where a disputed future fact is blocking agreement, specifying trigger, measurement, source of truth, and settlement mechanism.
- State what each MESO's **selection would reveal** about the counterpart's priorities.

### Must Not
- Present MESOs sequentially. Offered one at a time they read as successive concessions; offered together they read as flexibility.
- Build packages that differ only in price. That is one offer with three numbers, and it teaches the counterpart only that your price moves.
- Assume issues you consider trivial are trivial to them. The cheapest concessions in most deals are the ones the giver never thought to price.
- Design a contingent term without a named, mutually acceptable source of truth for measuring the trigger. An unmeasurable contingency is a future dispute with a signature on it.
- Let package complexity exceed what the counterpart can evaluate in the room. A package nobody can compare gets rejected by default.
- Treat a guessed valuation as known when the whole trade depends on it.

---

## Instructions

### Step 1 — Enumerate every issue
List all negotiable variables, including ones currently treated as fixed: price, timing, scope, term length, payment schedule, exclusivity, termination rights, support levels, publicity, title, reporting line, start date, renewal terms. Explicitly ask what has been assumed non-negotiable and whether that assumption has been tested.

### Step 2 — Score your own valuations
Allocate 100 points across the issues by how much you actually care. Forced allocation prevents the "everything matters" answer that makes trade design impossible. State the basis for each score — a number you cannot justify is a number you will defend at the wrong moment.

### Step 3 — Score their valuations, steelmanned
Allocate 100 points as you believe they would, building the strongest legitimate account of their priorities. Tag each score **known** (stated or documented), **inferred** (strong contextual basis), or **guessed**. Guessed scores are hypotheses to test in Step 8, not foundations to build on.

### Step 4 — Find the asymmetries
Compute the gap per issue. The large-gap issues are the trade space:

| Pattern | Meaning | Move |
|---|---|---|
| You low, they high | Cheap for you to give | Concede early, price it fully |
| You high, they low | Cheap for them to give | Ask for it, expect it |
| Both high | Distributive core | Reserve for the endgame |
| Both low | Filler | Use as face-saving throwaways |

### Step 5 — Design the log-rolled trades
For each cheap-for-you / valuable-for-them asymmetry, write the trade explicitly: what you give, what you require in return, and the value logic that makes both sides better off. A trade without a named return is a concession with extra steps.

### Step 6 — Assemble the MESOs
Build 2–4 packages of approximately equal value **to you**, each emphasizing a different dimension — one that trades price for term length, one that trades scope for timing, one that trades certainty for upside. Verify each clears your reservation point. Give each a neutral label (A/B/C, not "our preferred option"). For each, state what its selection would reveal about their priorities.

### Step 7 — Design contingent terms
For each disputed future fact, design a term that lets each side act on its own forecast: earn-outs, volume tiers, performance triggers, milestone payments, adjustable terms, sunset clauses. Specify for each — **trigger** (the measurable event), **measurement** (how and when), **source of truth** (whose data, or which third party), **settlement** (what happens on trigger), and **dispute path**. Note the administrative burden honestly; a contingency that costs more to run than it resolves is a bad term.

### Step 8 — Sequence and test
Decide what to present when: MESOs typically go on the table after interests are confirmed but before positional bargaining hardens. Write the two or three questions that would confirm your load-bearing guessed valuations before you commit to a package that depends on them.

### Step 9 — Adversarial check
- Which asymmetry, if your valuation guess is wrong, turns a value-creating trade into a straight concession?
- Could any MESO be cherry-picked — the counterpart taking the favourable element of one and the favourable element of another?
- Does any contingent term give them an incentive to influence the trigger?

---

## False-Positive Prevention

1. **Price-only packages.** Building three MESOs that differ only in the number. The counterpart learns your price is soft and nothing else. Each package must differ in *shape*.
2. **Sequential MESO presentation.** Offering package A, then B when A is refused, then C. This is a concession ladder wearing a MESO costume, and it trains the counterpart to keep refusing.
3. **Guessed valuations treated as known.** Building the whole trade architecture on an inferred score and never testing it. Tag confidence; test the load-bearing guesses before committing.
4. **Assumed-trivial issues.** Failing to enumerate variables you consider fixed or minor. The highest-return trades in most deals are things the giver had not thought to price at all.
5. **Unmeasurable contingencies.** An earn-out with no agreed source of truth, a performance trigger with no defined measurement window. These do not resolve the disagreement; they defer it to a point where both parties are locked in and lawyers are cheaper than exit.
6. **Cherry-pickable packages.** Presenting MESOs whose elements can be recombined by the counterpart into a package worth less to you than any of the three. State explicitly that packages are integral.
7. **Complexity overload.** A five-issue, four-package matrix the counterpart cannot evaluate in the room. Unevaluable offers get declined by default, and the declination is read as rejection of the substance.
8. **Manipulable triggers.** A contingent term whose trigger the counterpart can influence — a volume tier they control, a performance metric they report. Any contingency must be robust to the incentive it creates.

---

## Output Format

```
# Package and Trade Design — [negotiation]

## Issue valuation
| Issue | Your points | Basis | Their points | Basis | Confidence | Gap |
|---|---|---|---|---|---|---|
| [...] | [n] | [...] | [n] | [...] | known/inferred/guessed | [±n] |
| **Total** | **100** | | **100** | | | |

## Asymmetry map
| Issue | Pattern | Trade direction |
|---|---|---|
| [...] | you-low/they-high | Concede — require [x] in return |

## Log-rolled trades
1. **Give:** [...] · **Get:** [...] · **Why both gain:** [...]

## MESO set (present simultaneously, packages are integral)
| | Package A | Package B | Package C |
|---|---|---|---|
| [Issue 1] | [...] | [...] | [...] |
| [Issue 2] | [...] | [...] | [...] |
| Value to you | [~equal] | [~equal] | [~equal] |
| Clears reservation point | y | y | y |
| If they pick this, it reveals | [...] | [...] | [...] |

## Contingent terms
| Disputed fact | Trigger | Measurement | Source of truth | Settlement | Dispute path | Admin burden |
|---|---|---|---|---|---|---|
| [...] | | | | | | low/med/high |

## Presentation sequence
[When MESOs go on the table, relative to interest confirmation and positional bargaining.]

## Guesses to test first
1. [Guessed valuation] — question: "[...]" — package that depends on it: [A/B/C]

## Adversarial check
- Asymmetry that becomes a straight concession if wrong: [...]
- Cherry-picking exposure: [...]
- Contingent term they could game: [...]
```

---

## Verification

- [ ] Every issue enumerated, including ones previously treated as fixed.
- [ ] Both sides scored on a forced 100-point allocation with stated bases.
- [ ] Counterpart scores tagged known / inferred / guessed.
- [ ] Asymmetries identified and classified into the four patterns.
- [ ] Each log-rolled trade names what is given, what is required in return, and why both gain.
- [ ] 2–4 MESOs built, differing in shape rather than only in price.
- [ ] Every package verified against the reservation point.
- [ ] Each MESO carries a note on what its selection would reveal.
- [ ] Packages marked integral to block cherry-picking.
- [ ] Each contingent term specifies trigger, measurement, source of truth, settlement, and dispute path.
- [ ] Administrative burden of each contingency assessed.
- [ ] Load-bearing guessed valuations have a test question attached.
- [ ] Adversarial check covers wrong-asymmetry, cherry-picking, and trigger-gaming exposure.
- [ ] No package presented sequentially as a fallback.
- [ ] No contingency with an unmeasurable or counterpart-controlled trigger.
