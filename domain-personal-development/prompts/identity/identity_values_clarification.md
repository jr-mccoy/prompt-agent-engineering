---
title: "Surface Operating Values From Past Decisions, Not Aspirations"
category: personal-development/identity
description: "Extract the user's revealed values from a list of recent real decisions and trade-offs they actually made, then contrast with their stated values to expose specific mismatches and propose one realignment move."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - QA-12
difficulty: intermediate
tags:
  - identity
  - values
  - revealed-preferences
  - self-knowledge
  - mismatch
updated: "2026-05-08"
related_prompts:
  - domain-personal-development/prompts/agency/agency_stuck_diagnosis.md
  - domain-personal-development/prompts/thinking/thinking_regret_minimization.md
  - domain-personal-development/prompts/identity/identity_self_talk_audit.md
  - domain-personal-development/prompts/identity/identity_life_audit_reckoning.md
  - domain-personal-development/prompts/identity/identity_purpose_reignition.md
---

# Surface Operating Values From Past Decisions, Not Aspirations

**Objective:** Identify the values the user is actually operating from — by reading their recent real decisions — and compare those to the values they claim. Output specific mismatches and one realignment move.

**When to use:** The user is making decisions that confuse them, feels off-track without knowing why, or suspects their stated priorities and their actual life don't line up. Useful before any major life or career move, and as input to `identity_life_audit_reckoning.md` or `identity_purpose_reignition.md`.

**Audience:** An individual examining their own life. Not a tool for assessing someone else, and not for clinical use. If the mismatches surfaced are distressing, refer to professional help — this prompt does not provide therapy.

---

## Inputs Required

1. **Stated values.** What the user *says* matters most to them. 5–8 items, in their own words (e.g., "family," "doing good work," "freedom").
2. **Decision log — last 90 days.** 8–15 actual decisions the user made where there was a real trade-off. Each as: *Decision → option chosen → option rejected → rough cost paid → rough cost avoided.* Examples: accepting/declining a meeting, taking/refusing a project, where money went, who got time, what got skipped. Trivial decisions (lunch order) don't count.
3. **Time allocation snapshot.** Where the last 30 days of waking hours actually went, in rough buckets (work, family, health, friends, hobbies, screens, sleep, errands). Hours, not percentages.
4. **Money allocation snapshot.** Last 30 days of discretionary spending by category, in rough dollars or proportions. Required because spending is a strong revealed-preference signal.
5. **One decision the user feels off about.** A specific recent decision — chosen or deferred — that doesn't sit right.

If decision log has fewer than 6 real trade-offs, refuse and ask for more. Aspirations cannot be reverse-engineered from too few data points.

---

## Instructions

### Step 1 — Derive revealed values from the decision log

For each decision in input 2, ask: "What did this choice protect, prioritize, or pay for?" Cluster the answers into 4–6 named **revealed values**. Use the user's actual decision data, not generic value labels — name them concretely (e.g., "predictability over upside," "presence with kids over career velocity," "approval from peers over solitude").

A revealed value must show up in at least **two** independent decisions to count. Single instances are noise.

### Step 2 — Cross-check against time and money

Independently read inputs 3 and 4 the same way: where time and money actually went tells you what was actually being prioritized. Add or refine revealed values based on what time and money agree on.

If time and money disagree (e.g., user spent time on health but money on processed food and convenience), name the contradiction explicitly. Don't average it out.

### Step 3 — Compare stated to revealed

Produce a side-by-side table:

| Stated value (input 1) | Closest revealed value (Step 1–2) | Match / Drift / Contradiction |
|---|---|---|

- **Match:** stated and revealed point at the same priority and the supporting evidence is consistent.
- **Drift:** stated value is real but revealed value gets fewer hours/dollars than the user would predict.
- **Contradiction:** revealed pattern is the *opposite* of the stated value.

Each row must cite at least one specific decision, time bucket, or spending category as evidence. No row may be "Match" without evidence.

### Step 4 — Surface what's missing on each side

- **Revealed values not on the stated list.** Things the user is clearly prioritizing but did not name. Often these are values the user is embarrassed by, ambivalent about, or hasn't admitted to themselves (status, comfort, validation, safety).
- **Stated values not in revealed.** Things the user claims but isn't actually living. Often these are aspirational, inherited from a parent or peer, or borrowed from culture.

Do not moralize. The job is observation, not verdict.

### Step 5 — Diagnose the off-feeling decision

Take input 5 (the decision that doesn't sit right) and locate it on the table from Step 3. The off-feeling is almost always a decision that was made from a stated value but contradicts a revealed value, or vice versa. Name which it is in one sentence.

### Step 6 — Produce one realignment move

Pick **one** mismatch — the one with the most evidence and the most weekly cost — and propose one move:

- **Either:** change the stated value (drop it, downgrade it, rename it more honestly).
- **Or:** change the revealed value (specific behavior change, this week, with a check).

Not both. Not all of them. One.

The move must be physical and bounded: a calendar change, a spending change, a conversation, a deletion, an addition. Not "reflect on" or "consider."

---

## Constraints

### Must
- Derive at least 4 revealed values, each backed by ≥ 2 decisions.
- Cite specific evidence for every Match / Drift / Contradiction call.
- Name at least one revealed value the user did not state.
- Produce exactly one realignment move.
- Treat money and time as data sources of equal weight to the decision log.

### Must Not
- Use generic value words (integrity, growth, authenticity) without grounding them in the user's specific evidence.
- Moralize, congratulate, or shame the user for any revealed value.
- Diagnose mental health conditions or relationship dynamics — out of scope.
- Recommend a values-list template, vision-board exercise, or affirmation practice.
- Output "you should examine all of these" — pick one move.

---

## False-Positive Prevention

1. **Don't confuse aspiration with revealed value.** A value the user *wants* to have but hasn't acted on is a stated value, not a revealed one. The whole prompt rests on that distinction.
2. **Don't accept a single supporting decision.** Two-decision minimum for a revealed value. Otherwise you're picking up noise.
3. **Don't treat "Match" as the default.** Default to Drift unless evidence is strong on both sides — most stated and revealed values diverge under examination.
4. **Don't over-explain the contradictions.** Name them; don't narrativize them. The user does the meaning-making, not the prompt.
5. **Don't recommend a multi-week introspection plan.** One move, this week, observable.

---

## Output Format

```
## Revealed values (from your last 90 days)
1. [Concrete name] — evidence: [decision X, time bucket Y]
2. [Concrete name] — evidence: ...
...

## Stated vs. revealed
| Stated value | Closest revealed | Verdict | Evidence |
|---|---|---|---|
| ... | ... | Match / Drift / Contradiction | ... |

## What's missing
- **Revealed but unstated:** [1–3 items, each with one-line evidence]
- **Stated but unlived:** [1–3 items, each with one-line evidence]

## The off-feeling decision (input 5)
[Decision] sits on the [stated|revealed] side of [which mismatch]. The off-feeling is [one sentence].

## Realignment move (this week)
[Specific physical action, by when, observable.]

Predicted check: after this move, [observable change in time / money / decision pattern].
```

---

## Verification

- [ ] At least 4 revealed values named, each with ≥ 2 decision-level supports.
- [ ] Every table row cites specific evidence from inputs 2, 3, or 4.
- [ ] At least one unstated revealed value surfaced.
- [ ] Off-feeling decision (input 5) is located on the table, not analyzed in isolation.
- [ ] Exactly one realignment move proposed, physical and time-bounded.
- [ ] No generic value labels without grounding.
- [ ] No moralizing, no clinical interpretation, no affirmations.
