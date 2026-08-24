---
title: "Surface the Load-Bearing Assumptions Under a Plan or Belief, Then Test the Weakest"
category: personal-development/thinking
description: "Extract the hidden assumptions holding up a plan or belief the user is acting on, rank them by how load-bearing and how uncertain each is, identify the one whose failure would collapse the plan, and decide what the user must verify before proceeding."
techniques:
  - ST-01
  - ST-02
  - DS-06
  - QA-04
  - QA-12
difficulty: intermediate
tags:
  - assumptions
  - premise-audit
  - plan-testing
  - risk
  - pre-mortem
updated: "2026-07-23"
related_prompts:
  - domain-personal-development/prompts/thinking/thinking_blind_spot_mirror_see_what_im_missing.md
  - domain-personal-development/prompts/thinking/thinking_interrogative_mode.md
  - domain-personal-development/prompts/thinking/thinking_regret_minimization.md
  - domain-reasoning-craft/reasoning-moves/reasoning_premise_audit.md
  - domain-decision-making/scenario_strategic_pre_mortem.md
---

# Surface the Load-Bearing Assumptions Under a Plan or Belief, Then Test the Weakest

**Objective:** Make the user's implicit assumptions explicit, find the single one that most quietly holds up the whole plan while being least verified, and produce the one verification the user should run before committing further.

**When to use:** The user is about to commit real time, money, or reputation to a plan; a belief is driving their behavior and they want to check its footing; or a plan "just makes sense" and that confidence is itself suspicious. Not for decisions already made and irreversible, and not for a rigorous general premise audit on any claim — for that, route to `domain-reasoning-craft/reasoning-moves/reasoning_premise_audit.md`.

**Audience:** An individual examining their own plan or belief. Not for dismantling someone else's argument, not clinical. If the belief under examination is a fixed, distressing conviction about oneself or the world, this reasoning tool is not the right instrument — see `domain-psychology/` and professional support.

---

## Inputs Required

1. **The plan or belief, stated plainly.** What the user intends to do, or holds to be true, in one or two sentences (e.g., "I'll quit in six months once the side income covers rent," or "my manager blocks my promotion because he's threatened").
2. **The conclusion or action it justifies.** What the user will actually do because of it. Assumptions only matter relative to what they license.
3. **What's at stake if it's wrong.** The cost of proceeding on a false assumption — time, money, relationship, opportunity. Sets how much verification is worth.
4. **What the user is already unsure about.** Any part they'd flag as shaky. Required so the audit can go past the doubts they already hold.
5. **The deadline / decision point.** When the user must commit. Bounds how much can realistically be verified first.

If the plan is stated as a topic or feeling rather than a claim-plus-action, refuse and ask the user to state what they'll *do* and what has to be true for it to work.

---

## Instructions

### Step 1 — Extract the assumptions

Work backward from the action (input 2): for the plan to succeed, what must be true? Enumerate 6–10 assumptions. Force out the *hidden* ones — the assumptions so obvious to the user they never stated them (that a market exists, that a person will behave as expected, that a skill transfers, that current conditions hold). Cover four categories so the list doesn't cluster:

| Category | Assumption is about... |
|---|---|
| Self | The user's own capability, stamina, or motivation holding up |
| Others | How a specific person or group will behave or respond |
| World / environment | Market, timing, rules, or conditions staying as they are |
| Causal | That X actually causes Y (the mechanism the plan relies on) |

### Step 2 — Score each on two axes

Rate every assumption on:
- **Load-bearing (1–5):** if this turned out false, how much of the plan collapses? 5 = the plan is dead.
- **Uncertainty (1–5):** how unverified is it right now? 5 = the user is essentially guessing.

The dangerous assumptions are high on both. State each score with a one-line reason grounded in the user's inputs — no score without a reason.

### Step 3 — Rank and isolate the critical assumption

Rank by (load-bearing × uncertainty). The top one is the **critical assumption**: the quiet load-bearing wall. Name it in one sentence. This single item is the point of the whole exercise — do not spread attention across the whole list.

Distinguish it explicitly from assumptions that are load-bearing but *safe* (well-verified) — those are fine, leave them — and from uncertain but *cheap* assumptions that don't matter if wrong.

### Step 4 — Design the cheapest test of the critical assumption

Specify the smallest, fastest action that would move the critical assumption's uncertainty from "guessing" toward "known" before the deadline (input 5). A real test can come back negative. Prefer: one conversation, one small real-world probe, one number the user could look up, one reversible trial. Rank it against the stakes (input 3) — spend more verification effort when the downside is larger.

If the critical assumption genuinely cannot be tested before the deadline, say so plainly, and reframe the decision as a bet under acknowledged uncertainty — name the assumption the user is choosing to gamble on rather than pretending it's verified.

### Step 5 — Decide: verify, proceed, or restructure

Produce one of three decisive calls:
- **Verify first** — run the test from Step 4 before committing further; specify by when.
- **Proceed** — the critical assumption is safe enough given the stakes; commit, and name the tripwire that would reverse this.
- **Restructure** — the plan leans on an untestable high-stakes assumption; change the plan to depend on it less (stage it, hedge it, shrink the bet).

One call, with the assumption and the stakes named as the reason.

---

## Constraints

### Must
- Extract 6–10 assumptions spanning the four categories, including hidden/unstated ones.
- Score every assumption on both load-bearing and uncertainty, each with a grounded reason.
- Isolate exactly one critical assumption via load × uncertainty.
- Design the single cheapest test that could actually come back negative.
- End in one call: verify / proceed / restructure, with a named tripwire or gamble.

### Must Not
- List assumptions without ranking them — an unranked list is the failure mode this prompt exists to fix.
- Treat every assumption as equally worth verifying; most aren't.
- Propose a test that can only confirm (unfalsifiable), or a giant research project the deadline won't allow.
- Manufacture doubt about safe, well-verified assumptions to seem rigorous.
- Command the underlying decision or moralize about the user's confidence.

---

## False-Positive Prevention

1. **Don't flag safe assumptions as risks.** A high-load assumption that is well-verified is not a problem — it's the plan working. Only load-bearing *and* uncertain assumptions qualify as critical.
2. **Don't over-generate doubt.** The goal is to find the one wall that matters, not to make the user distrust everything. A list of 10 "risks" with no ranking is manufactured anxiety, not analysis.
3. **Don't accept a test that can't fail.** "I'll reflect and confirm my read" is not a test. The verification must be able to return a negative and change the decision.
4. **Don't confuse an uncertain-but-cheap assumption with a critical one.** If being wrong costs almost nothing, high uncertainty is irrelevant — don't spend the deadline verifying it.
5. **Don't pretend an untestable assumption is verified.** If the critical assumption can't be tested in time, name the gamble explicitly rather than laundering it into false confidence.
6. **Don't mistake a fixed distressing belief for a testable plan-assumption.** Convictions about self-worth or others' malice that resist all evidence are outside this tool's scope; route to support.

---

## Output Format

```
## The plan/belief and what it justifies
Plan: [input 1] → Action: [input 2] | Stakes if wrong: [input 3] | Decide by: [input 5]

## Assumptions holding it up
| # | Assumption | Category | Load (1-5) | Uncertainty (1-5) | Score | Reason |
|---|---|---|---|---|---|---|
| 1 | ... | Self/Others/World/Causal | | | L×U | ... |
[6–10 rows, including hidden ones the user never stated]

## The critical assumption
[One sentence — the quiet load-bearing wall.]
Safe-but-load-bearing (leave alone): [list]
Uncertain-but-cheap (ignore): [list]

## Cheapest test (before the deadline)
[Smallest action that could come back negative, by when.]
[If untestable in time: named gamble the user is choosing to take.]

## The call
[VERIFY FIRST / PROCEED / RESTRUCTURE] — because [critical assumption + stakes].
Tripwire that reverses this: [observable signal].

Predicted check: after the test, the critical assumption is [known-true / known-false / still a named bet], and the call [holds / flips].
```

---

## Verification

- [ ] 6–10 assumptions extracted across all four categories, including unstated ones.
- [ ] Every assumption scored on load-bearing and uncertainty with a grounded reason.
- [ ] Exactly one critical assumption isolated by load × uncertainty; safe and cheap ones set aside.
- [ ] The proposed test can return a negative and fits within the deadline.
- [ ] Output ends in one call (verify/proceed/restructure) with a named tripwire or acknowledged gamble.
- [ ] No manufactured doubt about safe assumptions; no commanded decision; no moralizing.
- [ ] Rigorous general premise-audit cross-linked, not cloned.
