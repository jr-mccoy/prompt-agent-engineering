---
title: "Leverage Audit — Inventory Every Source of Leverage, Not Just Your BATNA"
category: negotiation/preparation
description: "Inventory and rank every source of leverage on both sides of a negotiation — alternatives, time pressure, information, legitimacy, relationship, scarcity, coalition, and cost of no-deal — then assess each for durability and whether the counterpart knows you hold it. BATNA is one source among eight, and negotiators who track only their alternative routinely concede from a position that was stronger than they knew. Counters the most common self-inflicted failure: bargaining as though the only leverage in the room is your willingness to walk."
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
  - leverage
  - power
  - preparation
  - asymmetry
updated: "2026-07-26"
reasoning:
  styles: [analytic, strategic, adversarial]
  stakes: variable
  horizon: variable
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: variable
  collaboration: solo_or_pair
  output_format: matrix
  user_role: [executive, founder, sales, hr, lawyer, individual]
  mode: [audit, diagnose, plan]
related_prompts:
  - domain-negotiation/preparation/negotiation_batna_analysis.md
  - domain-negotiation/preparation/negotiation_opening_offer_design.md
  - domain-negotiation/at-the-table/negotiation_hard_bargainer_defense.md
---

# Leverage Audit — Inventory Every Source of Leverage, Not Just Your BATNA

**Objective:** BATNA answers one question — what happens if there is no deal — and it is the most important single source of leverage. It is not the only one. Time pressure, asymmetric information, legitimacy (standards, precedent, published norms), relationship capital, scarcity, coalition support, and the raw cost of no-deal to each side all shift the bargaining range independently of alternatives. This prompt inventories all eight sources on **both** sides, rates each for strength and durability, and marks whether the counterpart is aware you hold it — because unexercised, unsignalled leverage moves nothing. It ends by naming the two sources worth actively building before the conversation and the one that is decaying fastest.

This is the breadth complement to `negotiation_batna_analysis.md`. BATNA analysis goes deep on alternatives and derives the bargaining range; this goes wide across every other force acting on that range.

**When to use:**
- Your BATNA is weak and you are about to concede accordingly — before assuming you have no power.
- The counterpart appears to hold all the cards and you want an honest read rather than a demoralized one.
- Time pressure is being applied and you cannot tell whether it is real or manufactured.
- Before designing an opening offer, so the anchor is calibrated to actual rather than assumed strength.
- A repeated negotiation where leverage has shifted since last time and nobody has re-audited.

**When NOT to use:**
- You have not yet established your walkaway — run `negotiation_batna_analysis.md` first; leverage is meaningless without a floor.
- The negotiation is relationship-primary and framing it as a power contest would itself be the mistake — use `difficult-conversations/difficultconvo_pre_brief.md`.
- You need to counter specific coercive tactics already being deployed — that is `at-the-table/negotiation_hard_bargainer_defense.md`.

**Audience:** Executives, founders, salespeople, people leaders, lawyers, and individuals who suspect they are either over- or under-estimating their position.

---

## Inputs / Context

1. **The negotiation.** What is being negotiated, with whom, by when.
2. **Your BATNA and theirs.** As derived in `negotiation_batna_analysis.md`, or best current estimate.
3. **Deadlines on each side.** Real ones, claimed ones, and who set them.
4. **What each side knows.** Information you hold that they don't, and vice versa.
5. **External standards.** Published benchmarks, market rates, precedent, policy, or norms either side could invoke.
6. **Relationship and constituency.** History between the parties, and who each negotiator answers to.

---

## Constraints

### Must
- Audit all **eight sources** for both sides: alternatives, time, information, legitimacy, relationship, scarcity, coalition, cost-of-no-deal. Omitting a source is how leverage goes unnoticed.
- Rate each source **strong / moderate / weak / absent** for each side, with the evidence for the rating stated.
- Mark each of your sources with **signalled / unsignalled** — whether the counterpart knows you hold it. Unsignalled leverage is latent, not active.
- Assess **durability**: does this source strengthen, hold, or decay between now and the decision? Decaying leverage must be used or lost.
- Steelman the counterpart's leverage. Construct the strongest honest version of their position, not a self-serving one.
- Distinguish **real deadlines** (externally imposed, verifiable) from **asserted deadlines** (claimed by a party, unverifiable) and say which each is.
- Name **two sources worth building** before the conversation and the concrete action that would build each.

### Must Not
- Equate leverage with aggression. Legitimacy and relationship are leverage; both are exercised gently.
- Assume a weak BATNA means weak overall position. That inference is the specific error this prompt exists to prevent.
- Count leverage the counterpart cannot perceive as active. Latent leverage changes nothing until it is credibly signalled.
- Treat an asserted deadline as real without testing it. Manufactured urgency is the most common leverage bluff.
- Inventory only your own side. A one-sided audit produces confidence, not calibration.
- Recommend signalling every source you hold. Some leverage works better held in reserve, and some is destroyed by being named.

---

## Instructions

### Step 1 — Restate the bargaining position
Summarize in three lines: what is being negotiated, the current bargaining range if known, and your intuitive read on who holds the stronger hand. Record the intuition explicitly — Step 8 will test it against the audit.

### Step 2 — Audit alternatives
For each side: how good is the no-deal outcome, how many alternatives exist, and how quickly could each be executed? This is the BATNA input. Note that *number* of alternatives matters separately from quality — three mediocre options often beat one good one, because they are harder to foreclose.

### Step 3 — Audit time
For each side: what deadline binds, who set it, and is it verifiable? Mark each **real** (externally imposed — a board meeting, a contract expiry, a regulatory date) or **asserted** (claimed by a party). Then determine who is hurt more by delay. Time leverage belongs to whoever can wait longer, which is frequently not whoever is talking about deadlines most.

### Step 4 — Audit information
For each side: what do they know that the other doesn't? Distributional information (what others paid, where the band sits) is the highest-value category. Note also what each side *believes* the other knows — misperception here is itself exploitable and itself a risk.

### Step 5 — Audit legitimacy
What external standards, benchmarks, precedents, published rates, or policies could each side invoke? Legitimacy leverage is uniquely powerful because it lets a counterpart concede without losing face — they are not yielding to you, they are conforming to a standard. Identify the standard most favourable to you that is also defensible.

### Step 6 — Audit relationship, scarcity, coalition, and cost-of-no-deal
Four passes, both sides. **Relationship:** accumulated trust, favours owed, reputational stake in behaving well. **Scarcity:** how replaceable each party is, and how visible that is. **Coalition:** who else supports each side's position, and whether that support is mobilizable. **Cost-of-no-deal:** the absolute cost to each side of walking, distinct from the quality of alternatives — a party with good alternatives may still face high switching costs.

### Step 7 — Rate, signal-check, and durability-check
Build the matrix: source × side × strength × evidence. For your own sources add **signalled / unsignalled**, and for both sides add durability (**building / holding / decaying**) with the reason. Flag every decaying source explicitly — that is a clock.

### Step 8 — Reconcile against the intuition and name the build actions
Compare the completed matrix against the Step 1 intuition. If they disagree, say which is more likely wrong and why. Then name the two sources worth building before the conversation, with the specific action for each (e.g. "obtain one more competing quote by Thursday" for alternatives; "find the published benchmark that supports the number" for legitimacy). Note which sources to signal, which to hold in reserve, and why.

### Step 9 — Adversarial check
- Which of your leverage sources would collapse first under pressure, and what would trigger it?
- Which of their sources have you rated weak on convenience rather than evidence?
- If they ran this same audit, what would they conclude that you have not?

---

## False-Positive Prevention

1. **BATNA tunnel vision.** Rating the whole position off alternatives alone. The entire purpose of this audit is that seven other sources exist; a weak BATNA with strong legitimacy and time leverage is a workable position.
2. **Latent-leverage counting.** Adding up sources the counterpart has no idea you hold and concluding you are strong. Unsignalled leverage is potential energy. Mark it and decide whether to convert it.
3. **Deadline credulity.** Accepting "we need this signed by Friday" as a constraint. Ask who set it and what happens on Saturday. Most asserted deadlines survive contact with that question poorly.
4. **Aggression conflation.** Assuming leverage must be exercised forcefully, so declining to be forceful means declining to use leverage. Legitimacy leverage in particular is exercised by citing a standard, calmly.
5. **One-sided audit.** Inventorying only your own sources. This produces a confidence number, not a calibration, and it is how negotiators walk into rooms surprised.
6. **Convenience-rating the counterpart.** Marking their sources weak because a strong rating is uncomfortable. Steelman theirs to the same standard you apply to yours.
7. **Durability blindness.** Treating the matrix as static. Scarcity decays as substitutes appear; time leverage inverts as a deadline approaches; relationship capital depletes when spent. A source rated strong today may be spent by the meeting.
8. **Over-signalling.** Naming every source you hold, which converts leverage into a threat display, triggers reactance, and forecloses the graceful concession routes that legitimacy leverage opens.

---

## Output Format

```
# Leverage Audit — [negotiation]

Initial intuition on who holds the stronger hand: [...]

## Leverage matrix
| Source | You | Evidence | Signalled? | Them | Evidence | Durability |
|---|---|---|---|---|---|---|
| Alternatives (BATNA) | strong/mod/weak/absent | [...] | y/n | [...] | [...] | building/holding/decaying |
| Time | | | | | | |
| Information | | | | | | |
| Legitimacy | | | | | | |
| Relationship | | | | | | |
| Scarcity | | | | | | |
| Coalition | | | | | | |
| Cost of no-deal | | | | | | |

## Deadline test
| Deadline | Whose | Real / asserted | Basis | Who is hurt more by delay |
|---|---|---|---|---|
| [...] | | | | |

## Legitimacy standards available
| Standard / benchmark | Favours | Defensible? | How to invoke |
|---|---|---|---|
| [...] | you/them | | |

## Reconciliation
Intuition said: [...]. Audit says: [...].
Which is more likely wrong, and why: [...]

## Build actions (before the conversation)
1. [Source] — [specific action] — by [when]
2. [Source] — [specific action] — by [when]

## Signal plan
- Signal now: [source] — because [...]
- Hold in reserve: [source] — because [...]

## Decay clock
[Any source rated decaying, with the date or event by which it must be used.]

## Adversarial check
- My source most likely to collapse under pressure: [...]
- Their source I may have convenience-rated: [...]
- What their version of this audit would conclude that mine doesn't: [...]
```

---

## Verification

- [ ] All eight sources audited for both sides, none omitted.
- [ ] Every rating carries stated evidence, not just a label.
- [ ] Each of your sources marked signalled or unsignalled.
- [ ] Durability assessed per source, with decaying sources flagged and dated.
- [ ] Every deadline classified real or asserted, with its basis and who set it.
- [ ] At least one legitimacy standard identified, with how to invoke it.
- [ ] Counterpart's leverage steelmanned to the same standard as your own.
- [ ] Audit reconciled against the Step 1 intuition, with a stated view on which is wrong.
- [ ] Two build actions named, each specific and dated.
- [ ] Signal plan distinguishes what to signal from what to hold in reserve, with reasons.
- [ ] Adversarial check names a collapse trigger and a convenience-rated source.
- [ ] No source counted as active leverage while unsignalled.
- [ ] No asserted deadline treated as real without a stated basis.
