---
title: "Interest Mapping — Positions vs. Underlying Interests for Both Sides"
category: negotiation/preparation
description: "Before or during a negotiation, separate what each party SAYS they want (positions) from WHY they want it (interests). Drives a why-laddering procedure 3–5 levels deep per side, finds where interests overlap (value-creation territory) and where they genuinely diverge (value-claiming territory), and designs a question sequence to surface the counterpart's interests live. Counters the most common value-destroying mistake: negotiating positions when the deal lives in interests."
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
  - interests
  - positions
  - value-creation
  - why-laddering
updated: "2026-06-18"
reasoning:
  styles: [analytic, abductive, strategic, dialectical]
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
  - domain-negotiation/preparation/negotiation_pre_meeting_rehearsal.md
  - domain-decision-making/decisioning_rapid_stakeholder_alignment.md
---

# Interest Mapping — Positions vs. Underlying Interests for Both Sides

**Objective:** Take a negotiation where each side has stated a position and reconstruct the interests underneath. A position is the demand ("I need $20k more"). An interest is the motivation that demand serves ("I need to feel the market values me," "I have a tuition payment in September," "I'm benchmarking against a peer who just got promoted"). The same position can sit on top of many different interests, and the same interest can be satisfied by many different positions. This prompt drives a why-ladder per side, then locates where the interests overlap (territory where both sides can get more — value creation) and where they truly diverge (territory where one side's gain is the other's loss — value claiming). It ends with a live question sequence to surface the counterpart's real interests in the room.

This is the inside-the-negotiation complement to `negotiation_batna_analysis.md`. BATNA analysis is structural and adversarial — it maps walkaways and the bargaining range. Interest mapping is integrative — it finds the value that positional bargaining leaves on the table.

**When to use:**
- A negotiation has stalled on a single positional axis (usually price) and feels zero-sum.
- You suspect the counterpart's stated demand is a proxy for something else.
- The relationship will continue, so creating value matters as much as claiming it.
- Multi-dimensional deals (employment, partnership, vendor contracts, term sheets) where trades across dimensions are possible.
- Before a first substantive meeting, to plan what to ask.

**When NOT to use:**
- Pure one-shot distributive deals (e.g., haggling over a used car you'll never see again) where there is no value to create and BATNA/ZOPA analysis is the right tool.
- When you have no information about the counterpart and cannot make even a steelmanned guess at their interests — gather information first, then map.
- When the counterpart has explicitly refused to discuss anything but price and the relationship is disposable.

**Audience:** Executives, founders, salespeople, HR and people leaders, lawyers, and individuals preparing for a negotiation where the deal has more than one dimension.

---

## Inputs / Context

1. **The negotiation.** What's being negotiated, with whom, by when.
2. **Your stated position(s).** The headline demand(s) you have made or plan to make.
3. **Their stated position(s).** What the counterpart has demanded, or is expected to.
4. **What you know about each side.** History, constraints, pressures, recent events that might shape interests.
5. **Dimensions in play.** All the negotiable variables (price, timing, scope, terms, exclusivity, title, recognition, optionality, etc.), even minor ones.
6. **Relationship horizon.** One-shot, repeated, or indefinite.

---

## Constraints

### Must
- Run a **why-ladder** per side: take each position and ask "why do they want that?" 3–5 times, until you hit a motivation that is no longer instrumental (a need, fear, identity, constraint, or deadline).
- Distinguish **terminal interests** (wanted for their own sake — security, status, autonomy, fairness) from **instrumental interests** (wanted only because they serve a terminal one).
- Steelman the counterpart's interests. Construct the strongest, most legitimate version of why they want what they want, not a cynical caricature.
- Mark each reconstructed interest with a **confidence level** (known / inferred / guessed) so the map shows where you're reasoning vs. where you actually know.
- Find **overlap** (shared or compatible interests → value creation) AND **divergence** (genuinely opposed interests → value claiming). Both exist in almost every real negotiation; a map with only one is incomplete.
- Produce a **live question sequence** the user can deploy in the room to confirm or correct the inferred interests.

### Must Not
- Stop at the first "why." The first answer is usually still a position in disguise.
- Treat an inferred interest as a known fact. The map is a hypothesis until tested in the room.
- Assume opposed positions mean opposed interests. They frequently don't — that's the whole point.
- Collapse the counterpart's interests into "they just want more money / to win." That ends the inquiry exactly where value lives.
- Design interrogation-style questions that signal you're trying to extract leverage. Questions should invite disclosure, not trigger defense.

---

## Instructions

### Step 1 — List positions per side
Write each side's stated demands as positions, one per line. Keep them as actually stated (or as you expect them to be stated), not pre-interpreted.

### Step 2 — Why-ladder your own positions
For each of your positions, ask "why do I want that?" Then ask why of the answer. Continue 3–5 levels until you reach a terminal interest (something wanted for its own sake). Record the full ladder; the rungs are tradeable insights. Doing your own side first calibrates the depth you should reach on theirs.

### Step 3 — Why-ladder their positions (steelmanned)
For each of their positions, build the strongest, most legitimate ladder you can. At each rung ask: what need, fear, deadline, constraint, or identity would make a reasonable person demand this? Mark each rung's confidence: **known** (they said it / it's documented), **inferred** (strong contextual basis), **guessed** (plausible but unverified).

### Step 4 — Separate terminal from instrumental
Across both ladders, tag each interest. Terminal interests (security, fairness, status, autonomy, relationship, certainty) are the ones a deal must ultimately satisfy. Instrumental interests reveal the flexible variables — the places where a different position could serve the same underlying need.

### Step 5 — Map overlap (value-creation territory)
Find interests that are shared, compatible, or asymmetrically valued. The richest overlaps are **asymmetric**: something one side values highly and the other barely cares about. Each such asymmetry is a trade that makes both sides better off. List them explicitly with the trade implied.

### Step 6 — Map divergence (value-claiming territory)
Find interests that are genuinely opposed — where satisfying one side's interest costs the other. This is the irreducible distributive core. Name it honestly; pretending it isn't there leads to soft, drifting negotiation.

### Step 7 — Reframe the positional impasse
If the negotiation was stuck on one axis, restate the impasse in interest terms. Often the restatement dissolves it: the apparent conflict over a position turns out to be two different interests that a creative term can satisfy simultaneously.

### Step 8 — Design the live question sequence
Write 4–7 questions, ordered, that the user can ask in the room to confirm the inferred/guessed interests. Lead with open, low-threat questions ("Help me understand what's driving the timing on your side"); reserve sharper, more diagnostic questions for after rapport. Each question targets a specific uncertain rung in the counterpart's ladder. Note what answer would confirm vs. overturn your inference.

### Step 9 — Adversarial check
- Which inferred interest, if wrong, would most damage your strategy?
- Are you projecting your own interests onto them?
- Is there a hidden interest (face-saving, a constituency they answer to, a precedent they fear setting) that you've omitted?

---

## False-Positive Prevention

1. **First-why stopping.** Quitting the ladder after one "why" leaves you with a slightly-restated position. Demand at least three rungs before declaring an interest terminal.
2. **Position-interest collapse.** Writing "their interest is to pay less" — that's their position restated. Push to *why* paying less matters here, now, to this person.
3. **Cynical interest attribution.** Reducing the counterpart to greed or ego. It feels safe but kills value creation. Steelman instead.
4. **Confidence inflation.** Treating a guessed interest as known and building the whole plan on it. Tag confidence honestly; test the load-bearing guesses with questions.
5. **Projection.** Assuming the other side is motivated by what would motivate you. Their terminal interests may be different in kind.
6. **Overlap-only or divergence-only maps.** A map with only shared interests is naive; a map with only opposed interests is positional thinking in disguise. Real negotiations have both.
7. **Interrogation questions.** Questions phrased to extract concessions ("So you'd accept less if...?") trigger defense and shut down disclosure. Phrase to invite, not to corner.
8. **Missing the hidden constituency.** The person across the table often answers to someone not in the room (a board, a spouse, a budget owner). Their interest may be that third party's, not their own.

---

## Output Format

```
# Interest Map — [negotiation]

## Positions (as stated)
- You: [position 1], [position 2], ...
- Them: [position 1], [position 2], ...

## Your why-ladder
| Position | Why 1 | Why 2 | Why 3 | Terminal interest |
|----------|-------|-------|-------|-------------------|
| [...]    |       |       |       |                   |

## Their why-ladder (steelmanned)
| Position | Why 1 | Why 2 | Why 3 | Terminal interest | Confidence |
|----------|-------|-------|-------|-------------------|------------|
| [...]    |       |       |       |                   | known/inferred/guessed |

## Interest inventory
| Interest | Side(s) | Terminal / Instrumental | Confidence |
|----------|---------|--------------------------|------------|
| [...]    | you/them/both | | |

## Overlap — value creation
| Shared / asymmetric interest | Implied trade | Who gives / who gets value |
|------------------------------|---------------|----------------------------|
| [...] | | |

## Divergence — value claiming
| Opposed interests | The irreducible conflict |
|-------------------|--------------------------|
| [...] | |

## Reframed impasse
[The positional deadlock restated in interest terms, and how that restatement opens or dissolves it.]

## Live question sequence
1. [Open, low-threat question] — targets: [rung]; confirms if: [...]; overturns if: [...]
2. ...
(4–7 questions, ordered low-threat → diagnostic)

## Adversarial check
- Load-bearing inference most likely wrong: [...]
- Projection risk: [...]
- Hidden interest / constituency I may have missed: [...]
```

---

## Verification

- [ ] Each position has a ladder of at least 3 rungs ending in a terminal interest.
- [ ] The counterpart's ladders are steelmanned, not cynical.
- [ ] Every inferred interest is tagged known / inferred / guessed.
- [ ] Terminal interests distinguished from instrumental ones.
- [ ] Both overlap (value-creation) and divergence (value-claiming) are mapped.
- [ ] At least one asymmetric trade is identified in the overlap.
- [ ] The positional impasse is restated in interest terms.
- [ ] The live question sequence is ordered low-threat → diagnostic, with confirm/overturn notes.
- [ ] Adversarial check names the load-bearing inference and one hidden constituency.
- [ ] No position-as-interest collapse anywhere in the map.
