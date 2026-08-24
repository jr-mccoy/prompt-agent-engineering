---
title: "After-Action Report — Decision Quality vs. Outcome Quality"
category: decision-making/documentation
description: "Structured after-action report (AAR) for any completed decision or initiative: what was the goal, what actually happened, what worked, what didn't, why, and what we'd do differently. Its central discipline is separating decision-judgment from outcome-judgment — a good decision can yield a bad outcome and vice versa — so that lessons attach to the process, not the luck. Output is a reusable AAR with lessons tagged by domain for retrieval."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - decision-documentation
  - after-action-report
  - retrospective
  - decision-quality
  - lessons-learned
updated: "2026-05-10"
reasoning:
  styles: [retrospective, counterfactual, causal]
  stakes: variable
  horizon: variable
  uncertainty: variable
  evidence_quality: moderate
  domain_complexity: variable
  collaboration: small_team
  output_format: structured
  user_role: [pm, engineer, founder, manager, individual, operator]
  mode: [audit, synthesize, document]
related_prompts:
  - domain-decision-making/documentation/decisiondoc_post_decision_review.md
  - domain-decision-making/documentation/decisiondoc_options_memo.md
  - domain-decision-making/tradeoff_reversibility_stakes_grid.md
---

# After-Action Report (AAR)

**Objective:** Produce a structured after-action report for a completed decision or initiative: what we set out to do, what actually happened, what worked, what didn't, why, and what we'd do differently. The discipline that makes an AAR worth more than a vent session is the **separation of decision quality from outcome quality**. Outcomes are a mix of decision and luck; judging the decision by its outcome ("it worked, so it was a good call") teaches the wrong lessons. A good decision (well-reasoned given what was knowable) can produce a bad outcome, and a reckless decision can get lucky. This AAR forces the resulting decision into the right cell of that 2×2 and attaches lessons to the **process**, so they transfer to future decisions rather than overfitting to this one's luck.

Lessons are **tagged by domain** so a body of AARs becomes a retrievable library ("show me everything we learned about vendor decisions") rather than a graveyard of one-off retros.

Distinct from `risk_after_action_review.md` (scoped to risk events / incidents); this AAR is for **any** past decision or initiative.

**When to use:**
- A decision or initiative has concluded (or reached a meaningful milestone) and you want durable lessons.
- A project succeeded — and you want to know whether it was the decision or the luck, before you canonize the playbook.
- A project failed — and you want to learn from it without scapegoating an outcome that the decision didn't actually control.
- Building an institutional library of decision lessons tagged for retrieval.

**When NOT to use:**
- The initiative is still in flight and the outcome isn't yet legible — use a mid-course review instead.
- You want predicted-vs-actual calibration against expectations set at decision time — use `decisiondoc_post_decision_review.md` (the complementary instrument).
- The goal is blame allocation. An AAR that becomes a tribunal stops producing honest lessons.

**Audience:** PMs, engineers, founders, managers, operators, and individuals extracting transferable lessons from completed work.

---

## Inputs / Context

1. **The decision / initiative** and when it ran.
2. **The original goal** — what success was supposed to look like, ideally as stated at the time.
3. **What actually happened** — outcomes, metrics, timeline.
4. **What was knowable at decision time** vs. what only became clear later (critical for the decision-vs-outcome split).
5. **Contributors** — who was involved (for accuracy, not blame).
6. **Domain tags** — the categories future readers would search by (e.g., hiring, pricing, vendor, architecture).

---

## The decision-quality × outcome-quality 2×2

| | **Good outcome** | **Bad outcome** |
|---|---|---|
| **Good decision** (sound given what was knowable) | Deserved win — extract the repeatable process | Bad luck / bad break — protect the process; don't overcorrect |
| **Bad decision** (unsound, lucky or unlucky) | Lucky escape — do NOT canonize the playbook; the process was flawed | Deserved loss — fix the process |

Placing the decision in the right cell is the AAR's core analytic act. The dangerous cells are the off-diagonal ones: **lucky escapes** (good outcome, bad process — the ones that get wrongly canonized) and **bad breaks** (bad outcome, good process — the ones that get wrongly punished).

---

## Constraints

### Must
- Reconstruct the **goal and the information available at decision time** before judging anything — judge the decision on what was knowable then, not on hindsight.
- Explicitly place the decision in the **2×2** (decision quality × outcome quality) and name the cell.
- Call out **lucky escapes** (good outcome, bad process) and **bad breaks** (bad outcome, good process) by name — these are the highest-value, most-misread findings.
- Separate **what worked / didn't** (observations) from **why** (causes). Don't collapse the two.
- Distinguish **controllable factors** (process, preparation, execution — transferable) from **uncontrollable factors** (luck, exogenous shocks — not lessons).
- Produce **lessons tagged by domain**, each phrased as a transferable rule, not a this-time-only note.
- Keep it **blameless on persons, specific on process.** Attribute to decisions and systems, not to individuals' character.

### Must Not
- Judge the decision by the outcome ("it worked out, so it was right"). That is the exact error the AAR exists to prevent.
- Apply hindsight that wasn't available at decision time and call the decision dumb for not having it.
- Let a lucky win launder a bad process into a "best practice."
- Punish a sound decision because the dice came up wrong.
- Produce lessons so generic they transfer nowhere ("communicate better," "plan more"). Lessons must be specific and tagged.
- Turn the AAR into a search for who to blame.

---

## Instructions

### Step 1 — Restate goal and decision-time information
What we aimed for, and crucially, **what was knowable when the decision was made.** Quote the original goal/criteria if recorded.

### Step 2 — What actually happened
The outcome, with metrics and timeline. Neutral description before judgment.

### Step 3 — Score decision quality (given what was knowable then)
Was the decision sound on the information available at the time — reasonable process, alternatives considered, risks accounted for? This is independent of how it turned out.

### Step 4 — Score outcome quality
Did it achieve the goal? Good / mixed / bad outcome. Independent of Step 3.

### Step 5 — Place in the 2×2 and name the cell
Combine Steps 3–4. Name the cell explicitly. Flag loudly if it's a **lucky escape** or a **bad break** — those are the findings most likely to be misread.

### Step 6 — What worked / what didn't (observations)
Two lists of concrete observations. Description, not yet explanation.

### Step 7 — Why (causes)
For each significant observation, the cause. Split **controllable** (process, prep, execution) from **uncontrollable** (luck, exogenous). Only controllable causes become lessons.

### Step 8 — What we'd do differently
Concrete process changes — but only where the cause was controllable. "Get luckier" is not a lesson. If the decision was sound and the outcome was a bad break, the honest answer may be "do the same thing again."

### Step 9 — Tagged lessons
Each lesson: a transferable rule + domain tag(s) + the cell it came from. Phrase so a future reader in a similar situation can apply it.

---

## False-Positive Prevention

1. **Outcome bias.** Judging the decision by the result. Score decision quality on decision-time information first, independently of outcome.
2. **Hindsight bias.** Faulting the decision for not knowing what was only knowable later. Anchor to what was on the table then.
3. **Lucky-escape canonization.** A good outcome from a bad process becoming a "best practice." Name lucky escapes explicitly; do not promote them.
4. **Bad-break punishment.** Penalizing a sound decision that got unlucky. Name bad breaks; protect the process.
5. **Observation/cause collapse.** Listing "what went wrong" as if it explains itself. Separate the what from the why.
6. **Luck-as-lesson.** Turning uncontrollable factors into action items. Only controllable causes yield lessons.
7. **Generic lessons.** "Communicate more." Useless. Specific, tagged, transferable rules only.
8. **Blame drift.** AAR becoming a tribunal on individuals. Blameless on persons, specific on process.

---

## Output Format

```
# After-Action Report — [decision / initiative]
**Ran:** [dates]   |   **Contributors:** [names/roles]   |   **Domain tags:** [tag, tag]

## Goal (and what was knowable at decision time)
- Goal / success criteria as stated then: [...]
- Information available at decision time: [...]
- Information that only became clear later: [...]

## What actually happened
- [Outcome, metrics, timeline — neutral]

## Decision quality (given what was knowable then)
- Sound / mixed / unsound — because: [...]

## Outcome quality
- Good / mixed / bad — because: [...]

## 2×2 placement
- Cell: [Good decision/Good outcome | Good decision/Bad outcome (BAD BREAK) |
         Bad decision/Good outcome (LUCKY ESCAPE) | Bad decision/Bad outcome]
- Why this cell: [...]
- ⚠ Misread risk: [if lucky escape → do not canonize; if bad break → do not overcorrect]

## What worked / what didn't (observations)
**Worked:**
- [...]
**Didn't:**
- [...]

## Why (causes)
| Observation | Cause | Controllable? |
|-------------|-------|---------------|
| [...]       | [...] | yes / no (luck) |

## What we'd do differently
- [process change — controllable cause only]
- [or: "repeat the same approach" if it was a sound decision / bad break]

## Lessons (tagged, transferable)
- **[domain tag]** — [transferable rule] (from cell: [...])
- **[domain tag]** — [transferable rule]
```

---

## Verification

- [ ] Goal and decision-time information reconstructed before any judgment.
- [ ] Decision quality scored on what was knowable then, independent of outcome.
- [ ] Outcome quality scored independently.
- [ ] Decision placed in the 2×2 with the cell named.
- [ ] Lucky escapes and bad breaks flagged explicitly.
- [ ] Observations (what) separated from causes (why).
- [ ] Controllable vs. uncontrollable causes distinguished.
- [ ] "What we'd do differently" only changes controllable factors.
- [ ] Lessons are specific, transferable, and domain-tagged.
- [ ] Blameless on persons; specific on process.
