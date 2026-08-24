---
title: "Post-Decision Regret Analysis Without Hindsight Bias"
category: personal-development/agency
description: "Examine a decision the user now regrets, separate process quality from outcome quality, and extract a transferable update — not a verdict on the past self."
techniques:
  - ST-01
  - ST-02
  - RT-09
  - QA-09
  - QA-02
  - RT-05
difficulty: intermediate
tags:
  - agency
  - post-mortem
  - regret
  - decision-quality
  - hindsight-bias
  - learning
updated: "2026-05-08"
related_prompts:
  - domain-personal-development/prompts/thinking/thinking_regret_minimization.md
  - domain-personal-development/prompts/agency/agency_end_of_session_review.md
  - domain-personal-development/prompts/identity/identity_values_clarification.md
  - domain-personal-development/prompts/identity/identity_confidence_calibration.md
  - domain-productivity/validation/validation_am_i_being_nuts.md
---

# Post-Decision Regret Analysis Without Hindsight Bias

**Objective:** Audit a regretted decision by separating two questions: *was the decision well-made given what was knowable at the time?* and *did it produce a bad outcome?* These are different. Output a transferable update for future similar decisions and a verdict on whether to reverse, recommit, or accept.

**When to use:** The user is replaying a past decision with regret, second-guessing, or rumination. Useful when the regret is interfering with current decisions, or when the user is about to swing the pendulum on the next similar choice. Distinct from `thinking_regret_minimization.md` (pre-decision); this is post-decision and explicitly guards against outcome-driven hindsight rewriting.

**Audience:** An individual reviewing their own past decision. Not a tool for arbitrating decisions made by others. Not therapy.

---

## Inputs Required

1. **The decision.** What did the user decide? One sentence with date.
2. **The alternatives that were on the table at the time.** 2–4 specific options, including the one chosen and the one(s) the user now wishes had been chosen.
3. **What was actually known at the time.** Concrete facts, evidence, and credible information available *before* the decision — not what is known now.
4. **What was unknown / uncertain at the time.** Specifically, what the user knew they didn't know, and what they couldn't have known (genuinely unforeseeable).
5. **Why the chosen option was chosen.** The actual reasoning, in the user's own words. If the user can't reconstruct it, ask them to write down what they remember thinking and feeling, then continue.
6. **The outcome.** What actually happened over the relevant time horizon.
7. **What the user now wishes had been chosen — and why.** Be specific about which alternative looks better in retrospect, and why.
8. **One sentence: what is the regret costing right now?** Is it stalling a current decision, looping in rumination, fueling self-criticism, etc.?

If input 3 includes information the user *only learned after* the decision, flag it for Step 2 and remove it from the at-the-time evidence base.

---

## Instructions

### Step 1 — Acknowledge once, then move to analysis

One sentence: regret is a real and reasonable response. Then begin. Do not extend acknowledgment into reassurance or moralization.

### Step 2 — Strip the hindsight contamination

This is the central step. Enforce it strictly.

Build a clean record of *what the user actually knew before the decision*, using only inputs 3 and 4. Anything from input 6 (outcome) or learned-after-the-fact information must be excluded from this record. State explicitly: *"The following items are post-hoc information and are excluded from the decision-quality analysis: [list]."*

If the user wrote any input 3 item that is actually post-hoc, name it and move it. Common contaminations:
- Outcome data ("the company failed" — that's outcome, not at-the-time information).
- Information that surfaced after the decision ("turns out X").
- Generalizations from later experience ("I now know Y types of people are like Z").
- Other-people's-decisions in retrospect ("the others who chose differently did better" — outcome data).

### Step 3 — Audit decision quality (not outcome quality)

Score the decision on five dimensions, using *only* the at-the-time evidence base:

| Dimension | Question | Score 1–5 |
|---|---|---|
| Information gathering | Did the user collect reasonable evidence given the stakes and time available? | |
| Alternative consideration | Were 2+ real alternatives genuinely weighed? | |
| Reasoning trace | Was the chosen option consistent with the user's stated reasoning? | |
| Reversibility check | Was the decision's reversibility correctly read at the time? (`QA-09`) | |
| Values fit | Did the choice align with values the user held *then*? (Run `identity_values_clarification.md` if this is unclear.) | |

A decision can score well on all five and still produce a bad outcome. That's the point.

### Step 4 — Audit outcome quality separately

Independently grade the outcome:

- **Bad outcome** — concretely worse than the realistic best-case for the chosen path.
- **Mixed outcome** — meets some expectations, misses others.
- **Good outcome that user is reframing as bad** — the outcome was actually fine, but the user is comparing it to an idealized counterfactual.

Audit input 7 (the alternative that "looks better"): is it being judged by its actual probable outcome, or by the imagined best-case version? Most people compare their *actual* path to the *imagined-best* counterfactual. Name this if present.

### Step 5 — Produce the four-quadrant verdict

Plot the decision into one quadrant:

|                | **Outcome was good** | **Outcome was bad** |
|---|---|---|
| **Decision was well-made** | A — Aligned. No regret warranted on either axis. | B — Bad luck. Process was sound; outcome was unforeseeable variance. **Most regret-loops live here.** |
| **Decision was poorly made** | C — Lucky. The process needs review even though the outcome was fine. | D — Unaligned. Both the decision and the outcome were bad. **Process update needed.** |

State which quadrant. Justify with specific evidence from Steps 3 and 4.

### Step 6 — Extract the transferable update

The update depends on quadrant:

- **A:** The regret is hindsight-driven. The lesson is: trust the process you used. Move on.
- **B:** The decision was sound. The lesson is *not* "next time decide differently" — that would be punishing good process for bad luck. The lesson, if any, is one of: better hedge against the variance you accepted, accept that variance is part of the decision class, or update probability estimates marginally.
- **C:** The outcome was fine but the process was weak. The lesson is process-level: collect more evidence, weigh more alternatives, trace reasoning explicitly — for next time.
- **D:** Both axes were bad. The lesson is the cleanest of the four: which step in the decision process failed, and how to repair it for the next similar decision.

The update must be **transferable** — applicable to a *class* of future decisions, not retrofitted to the past one. Phrase it as a rule: *"For decisions of class X, do Y."*

### Step 7 — Verdict on the past

Pick one:
- **Reverse** — the decision is still active, reversibility is open, and the diagnosis warrants reversing.
- **Recommit** — the decision is still active, reversibility is open, but the diagnosis says the original choice was correct.
- **Accept** — the decision is in the past, reversibility is closed; the work is to extract the update and stop replaying.

If the user picked Reverse, validate against: is the new option still available, what does reversal cost, and is the user reversing on outcome data alone (a common failure)? If reversing on outcome data alone, redirect to Recommit + accept variance.

### Step 8 — Address the present cost (input 8)

State the specific cost the regret is imposing right now (input 8) and propose one move to interrupt the rumination loop:

- If the user is stalling a current decision: time-box the post-mortem and force the current decision separately, with a date.
- If the user is in a self-criticism loop: route to `identity_self_talk_audit.md`.
- If the user is comparing to an imagined-best counterfactual: name the comparison fallacy and refuse the comparison.

---

## Constraints

### Must
- Strip hindsight contamination explicitly before analyzing decision quality.
- Score decision quality and outcome quality *independently*.
- Output a quadrant verdict.
- Produce a transferable update phrased as a rule for a *class* of decisions.
- State exactly one of: Reverse / Recommit / Accept.

### Must Not
- Reverse-engineer "what the user should have known" from the outcome.
- Punish good process for bad luck (Quadrant B).
- Reward bad process for good luck (Quadrant C) — even if the outcome was fine.
- Compare the actual path to an idealized counterfactual without naming the fallacy.
- Diagnose character flaws (e.g., "you have a pattern of impulsivity").
- Output multiple updates or multiple moves. One update, one verdict.

---

## False-Positive Prevention

1. **Don't let the outcome smuggle into the at-the-time evidence base.** This is the most common failure of post-mortems. Re-check every input 3 item.
2. **Don't default to Quadrant D ("you blew it").** Quadrant B is the more common honest answer in regret loops. Reserve D for cases where the process was actually weak by at-the-time standards.
3. **Don't accept "I should have known X" without checking what X was actually knowable.** Many things look obvious only after they happened.
4. **Don't validate Reverse on outcome alone.** Reversal must be supported by *current* decision quality, not retrospective outcome.
5. **Don't extend a one-time decision into a lifetime narrative.** "I always make this kind of mistake" is rarely supported by one instance and crosses into self-talk territory — refer to `identity_self_talk_audit.md`.
6. **Don't confuse this prompt with `thinking_regret_minimization.md`.** That one is pre-decision (will I regret this?). This one is post-decision (was the regret warranted?).

---

## Output Format

```
[One sentence acknowledging the regret.]

## Hindsight contamination removed
The following items were originally listed as "at-the-time" but are actually post-hoc and have been excluded:
- [item] — became known [when]

## Clean at-the-time evidence base
[Bulleted; only what was knowable before the decision.]

## Decision quality (process)
| Dimension | Score | Note |
|---|---|---|
| Information gathering | / 5 | ... |
| Alternative consideration | / 5 | ... |
| Reasoning trace | / 5 | ... |
| Reversibility check | / 5 | ... |
| Values fit | / 5 | ... |

## Outcome quality
[Bad / Mixed / Good but reframed as bad — with specifics. Counterfactual fallacy named if present.]

## Quadrant verdict
**[A / B / C / D]** — [name]
[Justification, 2 sentences.]

## Transferable update
For decisions of class **[describe class]**, the rule is:
**"[Specific rule, applicable to future similar decisions, not retrofitted to the past.]"**

## Verdict on the past decision
**[Reverse / Recommit / Accept]**
[Justification, 1–2 sentences. If Reverse: validation against current reversibility cost, not outcome alone.]

## Move to interrupt the present-day cost (input 8)
[Specific physical action.]
```

---

## Verification

- [ ] Hindsight contamination explicitly named and removed.
- [ ] Decision quality and outcome quality scored independently.
- [ ] Quadrant verdict explicit (A / B / C / D).
- [ ] Transferable update phrased as a rule for a class of decisions, not the specific past one.
- [ ] Reverse / Recommit / Accept verdict given.
- [ ] If Reverse, validated against current reversibility — not outcome alone.
- [ ] Counterfactual-fallacy check performed on input 7.
- [ ] No character diagnosis, no extension to "I always …" narratives.
