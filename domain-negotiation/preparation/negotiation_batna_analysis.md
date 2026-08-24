---
title: "BATNA Analysis — Best Alternative, Reservation Point, ZOPA Mapping"
category: negotiation/preparation
description: "Before a negotiation, develop your BATNA (Best Alternative to a Negotiated Agreement), estimate the counterpart's BATNA, derive your reservation point and theirs, and map the Zone of Possible Agreement (ZOPA). Surfaces whether a deal is possible and where in the bargaining range your strongest moves live. Counters the most common negotiation mistake: entering without knowing your walkaway."
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
  - batna
  - zopa
  - reservation-point
  - preparation
updated: "2026-05-10"
reasoning:
  styles: [analytic, strategic, adversarial]
  stakes: variable
  horizon: variable
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo_or_pair
  output_format: structured_negotiation_brief
  user_role: [executive, founder, sales, hr, lawyer, individual]
  mode: [audit, plan, decide]
related_prompts:
  - domain-decision-making/decisioning_rapid_stakeholder_alignment.md
  - domain-decision-making/tradeoff_reversibility_stakes_grid.md
  - domain-decision-making/decisioning_regret_minimization.md
---

# BATNA Analysis

**Objective:** Before a negotiation, develop a sharp picture of:
- **Your BATNA** (Best Alternative to a Negotiated Agreement) — what you'll do if no deal is reached
- **Their BATNA** — what they'll do if no deal is reached (estimated)
- **Your reservation point** — the worst deal you'd accept (anchored on your BATNA)
- **Their reservation point** — the worst deal they'd accept (estimated)
- **ZOPA (Zone of Possible Agreement)** — the range between the two reservation points, if it exists

The discipline matters because most negotiation failures come from one of three mistakes: entering without knowing your walkaway, overestimating your BATNA (so you walk when you shouldn't), or underestimating their BATNA (so you push too hard and break the deal). This prompt forces clarity before the conversation.

**When to use:**
- Salary / compensation negotiation
- Contract negotiation (vendor, customer, partnership)
- Term sheet / investment negotiation
- Real estate / large purchase negotiation
- Hiring decision involving offer negotiation
- Partnership dissolution / divorce negotiation
- Any negotiation with stakes worth 4+ hours of preparation time

**When NOT to use:**
- Low-stakes negotiations where preparation overhead exceeds the deal value.
- Distributive negotiations where both sides know the BATNAs and the bargaining is purely positional. (Use a tactics prompt instead.)
- Negotiations where the relationship is the primary asset and BATNA framing would corrode trust. (BATNA still applies, but framing matters; this prompt is structurally adversarial.)

**Audience:** Executives, founders, sales, HR, lawyers, individuals — anyone going into a negotiation with material stakes.

---

## Inputs / Context

1. **The negotiation.** What's being negotiated, with whom, by when.
2. **What you want.** The headline ask. (We'll go deeper than this.)
3. **What you think they want.** First-order reading of their headline ask.
4. **History.** Prior interactions, prior offers, prior breaks.
5. **Time pressure.** Real or perceived, on each side.
6. **Constraints.** Things you can't or won't do.

---

## Constraints

### Must
- Develop your BATNA **concretely**: not "find another job," but the specific best alternative offer in hand or realistically obtainable, with its terms.
- Estimate their BATNA from their perspective, with the strongest version (don't underestimate their alternatives).
- Derive your reservation point from your BATNA, not from your aspirations. Reservation point = "I am better off taking my BATNA than accepting any deal worse than this."
- Estimate their reservation point similarly.
- Compute ZOPA = (their reservation point ↔ your reservation point). If your reservation point is better than theirs, no deal is possible — surface this.
- Identify your **target** (where in the ZOPA you want to land) and **opening** (your first move).
- Surface non-monetary value the negotiation can create that expands the ZOPA: timing, scope, payment terms, warranties, optionality, relationship terms.
- For each side, list **interests** (underlying motivations) separately from **positions** (stated demands). Often interests overlap where positions don't.
- Identify **walkaway triggers** — specific moves by the other side that would cause you to leave.
- Plan information asymmetry: what you'll reveal, what you'll protect, what you'll ask about.

### Must Not
- Conflate BATNA with reservation point. BATNA is the alternative; reservation point is the worst deal you'd accept (derived from BATNA).
- Inflate your BATNA. Most negotiators do this and overplay their hand.
- Underestimate their BATNA. Most negotiators do this and underplay theirs.
- Fix on a single number when the negotiation has multiple dimensions. Multi-dimensional negotiations are usually richer than positional.
- Skip the interests step. Position-only negotiations leave value on the table.
- Treat the relationship as separate from the negotiation. The future relationship is itself a term.

---

## Instructions

### Step 1 — Negotiation context
What, with whom, by when, history.

### Step 2 — Your BATNA
- What is your best alternative if no deal is reached?
- Be concrete: specific job offer, alternative supplier, alternative buyer, status quo with named consequences.
- Confidence in BATNA: high (signed offer in hand) / medium (likely available) / low (hopeful)
- Action to strengthen BATNA: what could you do *now* to make your BATNA better?

A strong BATNA is the single most powerful negotiation asset. If yours is weak, much of the analysis below is constrained.

### Step 3 — Their BATNA
- What is their best alternative if no deal with you is reached?
- Be honest and steelman: assume they have decent alternatives unless you have evidence they don't.
- Their confidence in their BATNA (visible signals): high / medium / low

### Step 4 — Reservation points
- **Your reservation point:** the worst deal you'd accept. Anchored on your BATNA: "I am better off with my BATNA than with any deal worse than this." Express in the dimension(s) of the negotiation.
- **Their reservation point (estimated):** same logic from their side. Mark uncertainty.

### Step 5 — ZOPA
- ZOPA exists if your reservation point and their reservation point overlap. (For a buyer: max you'd pay > min they'd accept. For a seller: max they'd pay > min you'd accept.)
- If no ZOPA: no deal is currently possible. Either change BATNAs, find non-monetary terms that expand value, or end.
- ZOPA size affects strategy: tight ZOPA → distributive (slice the pie); wide ZOPA → look for expansion (grow the pie).

### Step 6 — Interests vs positions
| Side | Position (stated demand) | Interests (underlying motivation) |
|------|--------------------------|-----------------------------------|
| You  | [...]                    | [why you want this]               |
| Them | [...]                    | [why they want what they're asking] |

Interests often overlap where positions don't. Surface where you might both get more by trading on different dimensions.

### Step 7 — Multi-dimensional value mapping
List the dimensions of the negotiation: price, timing, scope, payment terms, warranties, exclusivity, term length, options, relationship terms, etc. For each:
- How much you value it (high / medium / low)
- How much they likely value it (estimate)

Trade items where the asymmetry favors swapping: give them what they value highly and you don't, in exchange for what you value highly and they don't. This is value creation, not just value claiming.

### Step 8 — Target and opening
- **Target:** where in the ZOPA you want to land. Aspirational but plausible.
- **Opening:** your first move. Conventional advice: aim higher than target so you have room to concede; not so high that it signals bad faith.

### Step 9 — Walkaway triggers
- Specific moves by the other side that would cause you to leave (not just disappointment, actual exit).
- Pre-commit to these in writing so you don't rationalize past them in the heat of the conversation.

### Step 10 — Information plan
- What you'll reveal proactively (often: your interests, in general terms).
- What you'll protect (your reservation point, your BATNA's exact terms).
- What you'll ask about (their interests, their alternatives, their constraints).
- Order of revelation: usually each side trades information; lead with interests, follow with movement.

### Step 11 — Anchoring and concession plan
- Your first anchor (your opening)
- Their likely first anchor
- Concession schedule: small at first, slower as you approach your reservation point. Each concession should be tied to a reciprocal move from them.

### Step 12 — Adversarial check
- What's your blind spot? (Often: you've inflated your BATNA, or you've underestimated their walkaway, or you've ignored a non-monetary dimension that matters to them.)
- What would a skeptical advisor say is wrong with this analysis?
- If the negotiation goes badly, what would the post-mortem say you missed today?

### Step 13 — Post-negotiation plan
- If deal: relationship and execution
- If no deal: how you walk away cleanly, preserving optionality for later
- If partial deal: what you accept, what gets deferred

---

## False-Positive Prevention

1. **BATNA-as-aspiration.** "My BATNA is to start a company" — fine if you have funding, a co-founder, a plan, a runway. Otherwise it's a wish, not a BATNA. Be honest.
2. **Their-BATNA underestimation.** Assuming they have no alternatives because you'd like that to be true. Steelman their alternatives.
3. **Reservation-point-as-target.** Confusing "the worst deal I'd accept" with "the deal I want." Targets are higher than reservation points.
4. **Single-dimension reduction.** Negotiating only on price when timing, scope, and terms can be traded for value.
5. **Position-only negotiation.** Pushing on stated demands rather than underlying interests; missed value-creation opportunities.
6. **No walkaway pre-commitment.** Without pre-committed walkaway triggers, you'll rationalize past them in the moment.
7. **Information overshare.** Revealing your reservation point or BATNA terms gives the counterpart precision to anchor against you.
8. **Information undershare.** Revealing nothing prevents value creation; the counterpart needs some sense of your interests to find tradeable terms.
9. **Relationship-vs-deal false dichotomy.** "I don't want to damage the relationship" is sometimes used to justify weak negotiation; the relationship is built on respect including respect for your terms.
10. **Anchoring-as-bad-faith.** Strong opening anchors are normal; only signal bad faith when wildly out of any plausible ZOPA.

---

## Output Format

```
# Negotiation brief — [topic]

## Context
- What: [...]
- With: [...]
- By: [...]
- History: [...]

## Your BATNA
- BATNA: [concrete description]
- Confidence: [high / medium / low]
- Action to strengthen now: [...]

## Their BATNA (estimated)
- BATNA: [steelmanned]
- Their confidence in it: [signals observed]

## Reservation points
- Yours: [value or terms]
- Theirs (estimated): [value or terms, with uncertainty]

## ZOPA
- Exists? [yes / no]
- Range: [low ↔ high]
- Size: [tight / moderate / wide]
- Implication for strategy: [distributive / value-creation / no-deal]

## Interests vs positions
| Side | Position (stated)             | Interests (underlying)               |
|------|-------------------------------|--------------------------------------|
| You  | [...]                         | [...]                                |
| Them | [...]                         | [...]                                |

## Multi-dimensional value mapping
| Dimension       | Your value | Their value | Trade potential       |
|-----------------|------------|-------------|------------------------|
| Price           | high       | high        | distributive          |
| Timing          | low        | high        | give them, get value  |
| Scope           | high       | low         | take, give value      |
| Payment terms   | medium     | low         | take                  |
| …               |            |             |                        |

## Target and opening
- Target: [...]
- Opening: [...]
- Rationale: [opening higher than target by X because...]

## Walkaway triggers (pre-committed)
- [Specific move that ends the negotiation]
- [Specific move]
- [Specific move]

## Information plan
- Reveal: [what, when, why]
- Protect: [what]
- Ask about: [what — their interests, alternatives, constraints]
- Order: [how to sequence]

## Concession plan
- First anchor: [yours]
- Their likely first anchor: [estimate]
- Concession sequence: [size, tied to reciprocal moves]

## Adversarial check
- My likely blind spot: [...]
- Post-mortem prediction: [if it goes badly, what would the post-mortem say I missed today]
- Fix before going in: [...]

## Post-negotiation plan
- If deal: [relationship, execution]
- If no deal: [clean walkaway, future optionality]
- If partial deal: [accepted, deferred, conditional]
```

---

## Verification

- [ ] BATNA concrete, not aspirational.
- [ ] Their BATNA steelmanned.
- [ ] Reservation point distinct from target.
- [ ] ZOPA computed and existence confirmed (or no-deal flagged).
- [ ] Interests separated from positions for both sides.
- [ ] Multi-dimensional value mapping with trade potential identified.
- [ ] Walkaway triggers pre-committed in specific terms.
- [ ] Information plan distinguishes reveal / protect / ask.
- [ ] Concession plan tied to reciprocal moves.
- [ ] Adversarial check identifies likely blind spot.
- [ ] Post-negotiation plan covers deal / no-deal / partial.
- [ ] No BATNA-as-aspiration.
- [ ] No their-BATNA underestimation.
