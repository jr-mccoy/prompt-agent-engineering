---
title: "Negotiation Prep Depth Triage — How Much Preparation This One Deserves"
category: negotiation/preparation
description: "Decide how much preparation a specific negotiation warrants before spending hours on it, and which prompts to run in which order. Scores the negotiation on stakes, reversibility, relationship horizon, counterpart sophistication, and information asymmetry, then assigns one of four prep tiers — from a five-minute walkaway check to a full multi-session workup — with a named prompt sequence per tier. Counters the two symmetric failures: over-preparing a low-stakes ask until the window closes, and walking into a consequential negotiation with nothing but a number in your head."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - DS-02
  - CM-02
  - QA-01
difficulty: beginner
tags:
  - negotiation
  - triage
  - preparation
  - routing
  - stakes
updated: "2026-07-26"
reasoning:
  styles: [analytic, strategic, evaluative]
  stakes: variable
  horizon: variable
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: variable
  collaboration: solo
  output_format: [ranked_list, structured]
  user_role: [executive, founder, sales, hr, lawyer, individual]
  mode: [triage, decide, plan]
related_prompts:
  - domain-negotiation/preparation/negotiation_batna_analysis.md
  - domain-negotiation/preparation/negotiation_information_plan.md
  - domain-decision-making/tradeoff_reversibility_stakes_grid.md
---

# Negotiation Prep Depth Triage — How Much Preparation This One Deserves

**Objective:** Preparation is not free. It costs hours, and in negotiations with a closing window it can cost the negotiation itself. But under-preparation is the more expensive error in exactly the cases where it is hardest to notice — high-stakes deals that *feel* routine because the counterpart is friendly. This prompt scores a specific negotiation on five dimensions (stakes, reversibility, relationship horizon, counterpart sophistication, information asymmetry), assigns a prep tier, and outputs an ordered, named sequence of the domain prompts to run at that tier. It is the routing entry point for `domain-negotiation/`: run it first, then follow what it tells you.

This sits upstream of everything else in the domain. Where `domain-decision-making/tradeoff_reversibility_stakes_grid.md` sizes decisions in general, this sizes a negotiation specifically and terminates in a prompt sequence rather than a judgment.

**When to use:**
- A negotiation is coming and you do not know whether it deserves twenty minutes or two days.
- You default to either always over-preparing or never preparing, and want the call made on evidence rather than temperament.
- Someone has asked you to prepare and you need to scope the work.
- You are new to this domain and want to know which of its prompts apply to your situation.

**When NOT to use:**
- The negotiation starts in the next few minutes — go straight to `negotiation_batna_analysis.md` and derive a walkaway, which is the irreducible minimum.
- You have already decided the prep depth and want to execute — skip to the relevant prompt directly.
- The question is whether to negotiate at all rather than how hard to prepare — that is a decision problem; use `domain-decision-making/tradeoff_reversibility_stakes_grid.md`.

**Audience:** Anyone facing a negotiation with material stakes who needs to allocate preparation effort proportionately — executives, founders, salespeople, people leaders, lawyers, and individuals.

---

## Inputs / Context

1. **The negotiation.** What is being negotiated, with whom, and by when.
2. **What is at stake.** The magnitude of the outcome in whatever units matter — money, time, scope, standing, optionality.
3. **Reversibility.** Whether a bad outcome can be undone, renegotiated later, or is locked.
4. **Relationship horizon.** One-shot, repeated, or indefinite — and whether the counterpart will remember how this went.
5. **Counterpart.** Who they are, how often they do this, and whether they are represented or advised.
6. **Time available.** Hours until the conversation, and how much of that is genuinely usable.

---

## Constraints

### Must
- Score all **five dimensions** explicitly. A triage that skips a dimension will systematically under-rate the negotiations where that dimension is the whole risk.
- Convert the scores into **one of four named tiers**, not a continuous recommendation. A tier is actionable; "moderately prepared" is not.
- Output an **ordered prompt sequence** for the assigned tier, with a time estimate per prompt.
- Apply the **asymmetry rule**: when the score sits on a tier boundary, round up. The cost of over-preparing is hours; the cost of under-preparing is the deal.
- Name the **single highest-value prep action** for this negotiation, so that a user with no time at all still does the one thing that matters most.
- Flag when **time available is the binding constraint** and the recommended tier cannot be completed — and say what to cut.

### Must Not
- Score stakes purely in money. A negotiation that sets a precedent, or that a team is watching, is high-stakes at low dollar value.
- Treat a friendly counterpart as a low-sophistication one. Warmth is a negotiating posture, not evidence of inexperience.
- Recommend the full sequence by default. A tool that always says "do everything" carries no information.
- Let the user's stated comfort level override the scores. Confidence is uncorrelated with preparedness, and the correlation it does have is often negative.
- Assign a tier without naming what would move the negotiation *up* a tier if it changed.

---

## Instructions

### Step 1 — State the negotiation in one line
Write what is being negotiated, with whom, and by when. Ambiguity here propagates through every score, so force specificity: "renewal of the Acme contract with their procurement lead, decision by the 14th," not "a vendor thing."

### Step 2 — Score stakes
Rate 1–5. Score the *consequence* of a bad outcome, not the headline number. Include non-monetary stakes explicitly: precedent set, audience watching, downstream deals anchored to this one, personal standing. A 3 here means a bad outcome is annoying; a 5 means it is structurally damaging.

### Step 3 — Score irreversibility
Rate 1–5. How hard is it to undo? A one-year contract with a break clause scores low. An equity split, a public commitment, or a term that becomes the baseline for every future renewal scores high. Note explicitly whether a bad outcome is *renegotiable later* — that is the single largest reducer of prep need.

### Step 4 — Score relationship horizon
Rate 1–5. One-shot with a stranger scores 1. An indefinite relationship where this negotiation sets the working norms scores 5. Note that high scores cut both ways: they raise the cost of an aggressive posture *and* raise the value of getting the structure right.

### Step 5 — Score counterpart sophistication and asymmetry
Rate 1–5 on how much better at this they are than you. Score 5 if they negotiate this specific thing professionally and you do it once a year — a recruiter, a procurement team, a car dealer, opposing counsel. Separately note **information asymmetry**: what do they know that you don't, structurally? Repeat players hold distributional data you cannot see.

### Step 6 — Assign the tier
Sum the five scores (5–25) and assign:

| Total | Tier | Prep budget |
|---|---|---|
| 5–9 | **T1 — Walkaway check** | 5–15 min |
| 10–14 | **T2 — Structured prep** | 45–90 min |
| 15–19 | **T3 — Full workup** | 3–6 hrs |
| 20–25 | **T4 — Multi-session campaign** | Days, with rehearsal |

Round **up** at any boundary. Override upward — never downward — if any single dimension scored 5.

### Step 7 — Emit the prompt sequence
Give the ordered sequence for the assigned tier, with per-prompt time estimates:

- **T1:** `negotiation_batna_analysis.md` (walkaway + ZOPA only, skip the multi-dimensional sections).
- **T2:** `negotiation_batna_analysis.md` → `negotiation_interest_mapping.md` → `negotiation_opening_offer_design.md`.
- **T3:** T2 + `negotiation_leverage_audit.md` → `negotiation_package_trade_design.md` → `negotiation_concession_anchoring_plan.md` → `negotiation_information_plan.md` → `negotiation_pre_meeting_rehearsal.md`.
- **T4:** T3 + `negotiation_counterpart_simulation.md`, plus `multi-party/` prompts if three or more parties, plus a second rehearsal pass after a break.

### Step 8 — Name the single highest-value action and the time check
State the one thing to do if everything else is cut — usually deriving the walkaway, occasionally identifying the hidden decision-maker. Then compare the tier's prep budget against actual time available. If the budget exceeds available time, say explicitly which steps to drop and in what order, rather than recommending a plan that cannot be executed.

### Step 9 — Adversarial check
- Which dimension did you score lowest, and what would you have to be wrong about for it to actually be a 5?
- Is the counterpart's friendliness doing work in your scores that evidence should be doing?
- What would have to change for this to jump a full tier — and could that change happen before the conversation?

---

## False-Positive Prevention

1. **Dollar-anchoring the stakes score.** Scoring stakes off the transaction value alone. A $5k negotiation that sets the renewal baseline for a $500k relationship is not a $5k negotiation. Score the consequence chain, not the line item.
2. **Friendliness discount.** Rating counterpart sophistication low because they are warm, casual, or apologetic. Professional negotiators are frequently all three, deliberately. Score on repetition count, not affect.
3. **Reversibility optimism.** Assuming a bad term can be fixed at renewal. Ask whether you will have *more* leverage then; usually you have less, because switching costs have accumulated.
4. **Comfort-as-preparedness.** Letting "I've got this" reduce the tier. Confidence is not evidence. Only the five scores move the tier.
5. **Tier inflation across the board.** Assigning T3 or T4 to everything, which converts the tool into a ritual and guarantees it gets abandoned. If most of your negotiations score above 15, your scoring is miscalibrated — recalibrate against the least consequential negotiation you have had this year as the 1-point anchor.
6. **Ignoring the time constraint.** Emitting a 6-hour sequence for a negotiation in 90 minutes. An unexecutable plan is worse than a small one, because it produces neither preparation nor a decision about what to skip.
7. **Symmetric-information assumption.** Failing to score information asymmetry because the counterpart seems open. Repeat players hold distributional data — what others accepted, where the band actually sits — that no amount of openness in one conversation reveals.
8. **Missing the audience.** Scoring only the direct parties when a team, a board, or a precedent-watching peer group makes the real stakes higher than the transaction implies.

---

## Output Format

```
# Prep Triage — [negotiation]

One-line statement: [what, with whom, by when]

## Scores
| Dimension | Score (1–5) | Reasoning |
|---|---|---|
| Stakes | [n] | [consequence chain, not just the number] |
| Irreversibility | [n] | [renegotiable later? y/n + why] |
| Relationship horizon | [n] | [one-shot / repeated / indefinite] |
| Counterpart sophistication | [n] | [repetition count, representation] |
| Information asymmetry | [n] | [what they structurally know that you don't] |
| **Total** | **[5–25]** | |

## Tier assignment
**Tier [T1–T4] — [name]** · prep budget [range]
Boundary rounding applied: [yes/no]. Single-dimension override: [none / dimension scored 5]

## Prompt sequence
| # | Prompt | Time | Why it matters here |
|---|---|---|---|
| 1 | [file.md] | [n min] | [...] |

## If you do only one thing
[The single highest-value prep action for this specific negotiation.]

## Time check
Available: [n]. Required: [n].
[If short:] Drop in this order: [1st to cut], [2nd], [3rd]. Do not cut: [...]

## Adversarial check
- Lowest score, and what would make it a 5: [...]
- Friendliness doing work evidence should do: [...]
- What would move this up a full tier: [...]
```

---

## Verification

- [ ] All five dimensions scored with reasoning, not bare numbers.
- [ ] Stakes scored on consequence chain including non-monetary stakes, not transaction value alone.
- [ ] Reversibility notes explicitly whether a bad outcome is renegotiable later, and with what leverage.
- [ ] Counterpart sophistication scored on repetition count and representation, not on warmth.
- [ ] Information asymmetry named concretely — a specific thing they know that you don't.
- [ ] Total maps to one of the four named tiers, with boundary rounding applied upward.
- [ ] Any single-dimension 5 triggered an upward override, or its absence is stated.
- [ ] Prompt sequence is ordered, named by filename, and time-estimated.
- [ ] The single highest-value action is named and would stand alone.
- [ ] Time check compares budget to availability and, if short, names the cut order.
- [ ] Adversarial check identifies what would move the negotiation up a tier.
- [ ] No tier assigned on the basis of the user's stated confidence.
