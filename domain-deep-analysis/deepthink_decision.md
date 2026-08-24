---
title: "Deep-Think: Decision"
category: deep-analysis/decision
description: "A multi-phase, multi-perspective decision-making system for working through hard choices with an AI model at a depth that compensates for the absence of a human team. Drives the model through Frame → Decompose options & criteria → Multi-perspective → Stress-test → Synthesize, using AskUserQuestion at every gate. Terminal artifact: recommendation + rationale + calibrated confidence + reversibility + tripwires."
techniques:
  - ST-01
  - ST-02
  - ST-04
  - ST-42
  - RT-02
  - CM-02
  - QA-01
  - QA-02
  - QA-04
  - QA-09
difficulty: advanced
tags:
  - deep-analysis
  - decision-making
  - multi-perspective
  - tradeoff-analysis
  - reversibility
  - askuserquestion
  - gated-workflow
updated: "2026-05-08"
related_prompts:
  - domain-deep-analysis/deepthink_problem_analysis.md
  - domain-deep-analysis/deepthink_plan.md
  - domain-deep-analysis/deepthink_design.md
  - domain-decision-making/decisioning_blind_spot_identifier.md
  - domain-decision-making/decisioning_comprehensive_rapid_tradeoff_analyzer.md
  - domain-productivity/validation/validation_adversarial_mini_check.md
  - domain-prompt-engineering/evaluation/correctness_pre_mortem.md
---

# Deep-Think: Decision

**Objective:** Work through a decision at a depth that would normally require a team. Drive the model through five disciplined phases — Frame, Decompose options and criteria, Multi-perspective analysis, Stress-test, and Synthesize — pausing at each gate to let the user redirect, prune, or go deeper. Produce a recommendation with rationale, calibrated confidence, reversibility analysis, and tripwires that would tell the user the decision was wrong.

**When to use:** The user faces a choice between defined options (or needs help defining them), and the decision is load-bearing enough that a wrong answer carries real cost. Examples: "Should I take this job?", "Build vs. buy?", "Migrate to framework X?", "Confront this co-founder issue now or wait?". Use this when *choosing* is the goal. If you don't yet understand the situation well enough to choose, run `deepthink_problem_analysis.md` first.

**Audience:** Solo operators, small teams, anyone making a hard decision one-on-one with an AI and trying to compensate for the missing room of advisors.

---

## Inputs Required

1. **The decision.** Stated as a question with at least two options. If the user has only one option, ask them to name what "not doing it" looks like — that's option two.
2. **Why now.** What forces the decision now vs. later? (If nothing forces it, ask whether deferring is itself an option.)
3. **Stakes & reversibility.** Roughly: low (easily undone), medium (costly to reverse), high (effectively one-way door). One-line description.
4. **Decision deadline** (real or self-imposed).
5. **Anything the user is already leaning toward.** Optional but useful — surfacing the lean is what lets the perspectives push against it.

If any of items 1–4 are missing, ask for them before starting Phase 1.

---

## Operating Mode

Inherit the shared deep-think operating model from [`BACKBONE.md`](BACKBONE.md): run the five phases in order, stop at every gate, use `AskUserQuestion` when available, and fall back to a labeled `**GATE:**` block in plain chat. For decisions, use in-phase questions for clarifying options, weighting criteria, confirming added perspectives, and probing whether the stated lean matches the revealed lean.

---

## Instructions

### Phase 1 — Frame

**Goal:** Make sure we're deciding the right decision.

1. **Restate the decision.** One sentence: "[User] is choosing between [option A] and [option B] (and [option C, ...]) by [deadline] because [forcing function]."
2. **Surface stated vs. revealed decision.** Often the stated decision ("which job?") hides the revealed decision ("am I ready to leave the current one?"). Name the gap if there is one.
3. **Right-decision check.** Common reframes:
   - "Should I do X?" often hides "What would have to be true for X to be right, and is it?"
   - "Option A or B?" often hides "Is there a C I'm not considering?"
   - "Now or later?" often hides "Is the deadline real or self-imposed?"
4. **Reversibility classification.** Type 1 (one-way door, hard to reverse) or Type 2 (two-way door, easy to reverse)? Type 2 decisions deserve less analysis and more action. Flag explicitly.
5. **Confirm option set.** Are these all the options? Is there a "do nothing yet" option? Is there a "small reversible test" option that would convert this from Type 1 to Type 2?

**GATE 1:** Confirm framing and option set.

Use `AskUserQuestion`:

```
Question: "Is this the right framing of the decision and the right option set before we go deep?"
Options:
- "Yes — proceed with these options"
- "Add an option I'm missing — I'll specify"
- "Reframe the decision itself — I'll restate it"
- "Stop — I need to do problem analysis first (run /deepthink-problem)"
```

---

### Phase 2 — Decompose Options and Criteria

**Goal:** Break the decision into criteria that can be evaluated and tradeoffs that can be named.

1. **Surface decision criteria.** What dimensions actually matter? Common buckets: cost, speed, reversibility, optionality preserved, alignment with stated goals, alignment with revealed goals, risk profile, second-order effects. List 4–7 criteria, named in the user's domain language.
2. **Weight the criteria.** Use `AskUserQuestion` to ask the user which 2–3 criteria are *load-bearing* — the ones that, if violated, kill an option regardless of other strengths.
3. **For each option, score against criteria.** Use a simple labels: *strongly favors*, *favors*, *neutral*, *disfavors*, *strongly disfavors*. Avoid false numerical precision — if you'd be making up the score, use *unknown*.
4. **Identify load-bearing assumptions.** Which assumptions does each option depend on? Mark assumptions as *tested*, *reasonable inference*, or *untested-and-load-bearing*.
5. **Name the tradeoff sharply.** In one sentence: what is each option giving up that the other isn't? If you can't state the tradeoff in one sentence per option, the criteria aren't sharp enough — refine.

**GATE 2:** Confirm criteria, weights, and tradeoff statement.

Use `AskUserQuestion`:

```
Question: "These are the criteria, weights, and tradeoff. Adjust before we run perspectives?"
Options:
- "Looks right — proceed"
- "Reweight — [criterion] should be load-bearing / less important"
- "Add a criterion I'm missing"
- "The tradeoff statement is wrong — I'll restate"
```

---

### Phase 3 — Multi-perspective Analysis

**Goal:** Run the decision through perspectives the user couldn't easily generate alone.

#### 3a. Run the mandatory roster (always)

Run the Phase 3 mandatory perspective roster defined in [`BACKBONE.md`](BACKBONE.md): red team, steel-man, blind-spot scan, future-self, naive newcomer, and affected party. For decisions, each lens must include its lens statement, its take on the decision, and which option it leans toward and why — or what it surfaces if it does not lean.

#### 3b. Propose scope-specific additions

Use the decision candidate pool in [`BACKBONE.md`](BACKBONE.md) to propose 2–4 additional perspectives tailored to the user's choice. Confirm the additions with `AskUserQuestion`/`**GATE:**` and run only the perspectives the user picks.

#### 3c. After running all perspectives

Identify:
- **Convergent recommendation** — is there an option that multiple genuinely-different perspectives lean toward? If yes, that's strong signal.
- **Productive disagreement** — where do perspectives genuinely conflict, and which underlying value or assumption drives the conflict?
- **Perspective dissent** — is there one perspective that strongly disagrees with the apparent direction? Don't suppress it.

**GATE 3:** Decide depth.

Use `AskUserQuestion`:

```
Question: "Multi-perspective pass is complete. What to pull on hardest in stress-test?"
Options:
- "[Specific perspective dissent to investigate]"
- "[Specific load-bearing assumption to stress]"
- "The cost-of-being-wrong calculation in particular"
- "All of them — full stress-test"
```

---

### Phase 4 — Stress-test

**Goal:** Try to break the decision before the user commits.

1. **Pre-mortem.** Imagine: in six months, the user has chosen the leading option and it's going badly. Why? Generate 3–5 specific failure modes per option-being-considered. Early warning signs for each.
2. **Adversarial check.** What's the strongest objection a smart, informed critic would raise to the leading option? Steel-man it. Does the decision hold up, or does it need revision?
3. **Reversibility re-check.** If the user picks the leading option and it's wrong, can they get back? What does "getting back" cost in time, money, reputation, optionality? If costly, can they hedge — pick a smaller version first?
4. **Tripwires.** Define 2–4 specific observable signals that would tell the user "this decision was wrong, course-correct now." These should be observable within weeks, not requiring hindsight.
5. **Confidence calibration.** State explicit confidence in the leading option: high / medium / low. Name what would move it.

**GATE 4:** Decide what makes it into the synthesis.

Use `AskUserQuestion`:

```
Question: "Which stress-test findings should be carried into the recommendation?"
Options:
- "All findings — full caveats and tripwires"
- "Tripwires only — recommendation stands"
- "Hedge: recommend the smaller-test version of the leading option"
- "Loop back — the stress-test exposed something we need to revisit in Phase 2 or 3"
```

---

### Phase 5 — Synthesize

**Goal:** Produce a recommendation with rationale, calibrated confidence, reversibility, and tripwires. Not a hedge ("it depends"). Take a position.

After producing the synthesis:

**FINAL GATE:** Use `AskUserQuestion`:

```
Question: "Recommendation is on the table. What's next?"
Options:
- "I'm going to act on this — done"
- "Convert to a sequenced plan (run /deepthink-plan)"
- "Sit with it for [time]; check back if tripwires fire"
- "Loop back — [specific phase] needs another pass"
```

---

## Constraints

### Must
- Run all five phases in order. Never skip Phase 1 (Frame) or Phase 4 (Stress-test).
- Stop at every gate and use `AskUserQuestion` (or labeled `**GATE:**`) before proceeding.
- Run the full core roster of six perspectives.
- Name the tradeoff in one sentence per option in Phase 2. If you can't, the criteria aren't sharp.
- Classify reversibility (Type 1 vs Type 2) in Phase 1 and re-check in Phase 4.
- Define observable tripwires in Phase 4 — not vague "watch for problems."
- Take a position in Phase 5. State the recommendation, then the caveats.

### Must Not
- Generate all five phases in one continuous output.
- Refuse to recommend ("it depends on your priorities") in Phase 5. The user came for a recommendation; produce one with caveats, or explicitly state why no recommendation is responsible.
- Over-analyze a Type 2 (reversible) decision. If reversibility is high and stakes are bounded, recommend the smallest reversible test rather than running a full deep-think.
- Strawman the rejected option. The advocate-for-rejected perspective in Phase 3 must produce a genuinely strong case.
- Hide perspective dissent. If one perspective strongly disagrees with the synthesis direction, name it and explain why the synthesis weighted it as it did.
- Substitute pseudo-precision for judgment. Numerical scores on criteria invented for the analysis are worse than honest qualitative labels.

---

## False-Positive Prevention

1. **Watch for "decision theater."** Running a full five-phase analysis on a Type 2 (reversible) decision is theater — the cost of analysis exceeds the cost of just trying. Phase 1 should catch this and flip to "smallest reversible test, then re-evaluate."
2. **The user's lean is data, not bias.** People often have good intuition they can't fully articulate. The system's job is to test the intuition, not override it. If the analysis converges on the user's lean and the perspectives don't surface a real objection, trust converges.
3. **Convergence among similar perspectives is weak.** If red-team and steel-man both lean toward Option A but arrive there via the same underlying assumption, that's not corroboration. Convergence between *genuinely different* lenses is the signal.
4. **Beware the "cost of being wrong" framing skew.** Always run worst-case-A vs. worst-case-B, never worst-case-A vs. best-case-B. Loss aversion will distort if you don't.
5. **Tripwires must be observable, not aspirational.** "If things go badly" is not a tripwire. "If retention drops below X by week 6" is. If you can't write a tripwire that's observable in weeks, the decision may be too early to make.
6. **The system can be used to procrastinate.** If the user has run the same decision through two or more times without acting, the analysis is the avoidance. Flag and recommend acting on the smaller reversible test.
7. **Don't confuse confidence with consensus.** High confidence requires both convergence and tested assumptions. Convergence with untested load-bearing assumptions is medium confidence at best.

---

## Output Format

Use this exact structure for the final recommendation (Phase 5):

```markdown
## Decision (as framed in Phase 1)
[One sentence — the decision the user confirmed at GATE 1, including options and forcing function.]

## Recommendation
**[Option name].**

[2–4 sentences: why this option, in plain language. Make a real argument; do not hedge.]

## Rationale
- **[Criterion 1 — load-bearing]:** [How the recommendation scores on this criterion vs. the alternative. Specific.]
- **[Criterion 2 — load-bearing]:** [...]
- **[Other criteria]:** [Briefer.]

## What this gives up
[2–3 sentences naming what the rejected option(s) would have offered. The user should know the cost of the recommendation, not just its benefits.]

## Reversibility
- **Classification:** Type 1 (hard to reverse) / Type 2 (easy to reverse) / Hybrid.
- **If wrong, cost to reverse:** [time, money, reputation, optionality].
- **Smaller reversible test available?** [Yes — describe / No — explain why.]

## Tripwires (observable signals that say "course-correct")
- [Tripwire 1 — observable within X weeks. What it would mean.]
- [Tripwire 2 — ...]
- [Tripwire 3 — ...]
[2–4 tripwires. Each must be specific and observable, not vague.]

## Confidence calibration
- **Confidence in recommendation:** [high / medium / low].
- **What would move confidence up:** [specific evidence the user could gather.]
- **What would flip the recommendation:** [specific finding that would change the answer.]

## Strongest objection (steel-manned)
[The single most credible objection from Phase 4, in 2–3 sentences. Then: why the recommendation accepts this objection rather than reversing on it.]

## What this synthesis is *not*
[One sentence. Specifically: this is a recommendation, not a plan to execute it. If the user accepts the recommendation, the next step is /deepthink-plan to sequence the action.]
```

---

## Verification

Before declaring the recommendation complete, the model must check:

- [ ] All five phases ran, with a gate after each.
- [ ] Phase 1 produced both stated and revealed decision framings, classified reversibility, and confirmed option set with the user.
- [ ] Phase 2 produced 4–7 criteria, identified load-bearing ones, and stated the tradeoff in one sentence per option.
- [ ] Phase 3 ran the full core roster + any user-confirmed additions, and named both convergence and dissent.
- [ ] Phase 4 produced pre-mortem failure modes with early warning signs, observable tripwires, and reversibility re-check.
- [ ] Phase 5 takes a position. The recommendation is named, the rationale is concrete, and the user knows what they're giving up.
- [ ] Tripwires are observable within a defined timeframe — not vague.
- [ ] The synthesis does not pretend to be a plan. If the user wants execution, point them to /deepthink-plan.
