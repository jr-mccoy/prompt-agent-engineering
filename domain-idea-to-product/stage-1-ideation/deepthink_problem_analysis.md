---
title: "Deep-Think: Problem & Question Analysis"
category: deep-analysis/problem
description: "A multi-phase, multi-perspective analysis system for working through hard problems or questions with an AI model at a depth that compensates for the absence of a human team. Drives the model through Frame → Decompose → Multi-perspective → Stress-test → Synthesize, using AskUserQuestion at every gate to keep the user steering. Terminal artifact: diagnosis + leverage points + confidence calibration."
techniques:
  - ST-01
  - ST-02
  - ST-04
  - ST-42
  - RT-02
  - RT-09
  - CM-02
  - QA-01
  - QA-02
  - QA-04
difficulty: advanced
tags:
  - deep-analysis
  - problem-framing
  - multi-perspective
  - diagnosis
  - critical-thinking
  - askuserquestion
  - gated-workflow
updated: "2026-05-08"
related_prompts:
  - domain-deep-analysis/deepthink_decision.md
  - domain-deep-analysis/deepthink_plan.md
  - domain-deep-analysis/deepthink_design.md
  - domain-prompt-engineering/goal-orientation/goalorientation_right_problem_diagnostic.md
  - domain-decision-making/decisioning_blind_spot_identifier.md
  - domain-productivity/validation/validation_adversarial_mini_check.md
  - domain-prompt-engineering/evaluation/correctness_pre_mortem.md
---

# Deep-Think: Problem & Question Analysis

**Objective:** Work through a problem or open-ended question at a depth that would normally require a team. Drive the model through five disciplined phases — Frame, Decompose, Multi-perspective analysis, Stress-test, and Synthesize — pausing at each gate to let the user redirect, prune, or go deeper. Produce a diagnosis (not a recommendation, not a plan) that names the leverage points, the load-bearing assumptions, and the user's calibrated confidence.

**When to use:** The user faces a hard, fuzzy, or load-bearing question and wants to think through it carefully — not just get a quick answer. Examples: "Why does our retention keep dropping?", "What's actually going on with my motivation lately?", "Why is this codebase so hard to change?", "Is this market real or am I imagining it?". Use this when understanding is the goal. If the goal is to *choose*, use `deepthink_decision.md`. If the goal is a sequenced plan, use `deepthink_plan.md`. If the goal is a buildable spec, use `deepthink_design.md`.

**Audience:** Solo operators, small teams, anyone working through a hard problem one-on-one with an AI and trying to compensate for the missing room of colleagues.

---

## Inputs Required

1. **The question or problem.** One paragraph, the user's words.
2. **Why now.** What triggered the question — a specific event, a pattern, a deadline, or a gut feeling? One sentence.
3. **Stakes.** Roughly: low (curiosity), medium (would change a near-term action), high (would change strategy / commitments / direction). One word.
4. **Time available for this analysis.** 15 min, 1 hour, multi-session. Calibrates depth.
5. **Anything the user has already concluded or suspects.** Optional — surfacing prior beliefs is what lets the perspectives push against them.

If any of items 1–4 are missing, ask for them before starting Phase 1.

---

## Operating Mode

This prompt is **gated and interactive**. After every phase, stop and ask the user a focused question. Do not run all five phases in one shot.

**Primary I/O mechanism:** When `AskUserQuestion` is available (Claude Code, agent harness), use it at every gate with 2–4 specific options plus the implicit "Other." When unavailable (plain chat), use a clearly-labeled `**GATE:**` block and wait for the user's reply.

**Use `AskUserQuestion` liberally throughout each phase**, not just at gates — for disambiguating inputs, prioritizing axes, confirming dynamic perspective additions, and pruning depth-vs-breadth tradeoffs. Default to asking when the next step would benefit from a small input from the user; default to proceeding when the answer would not change what you do next.

---

## Instructions

### Phase 1 — Frame

**Goal:** Make sure the analysis runs against the right question.

1. **Restate the question** in your own words, in one sentence. Then in a second sentence, restate what the user seems to *actually* want to understand (which may differ from what they asked).
2. **Surface stated vs. revealed framing.** Stated = what they wrote. Revealed = what the question + the "why now" + the stakes imply they actually need. Name the gap if there is one.
3. **Right-problem check.** Is this the question worth asking, or is there a load-bearing prior question? Examples of common reframes:
   - "Why is X happening?" often hides "Is X actually happening as I think it is?"
   - "What should I think about Y?" often hides "What would change if I had a clear view of Y?"
   - "Is this a problem?" often hides "What would I do differently if it were?"
4. **Time/depth budget acknowledgment.** State explicitly: given the stakes and time available, what depth is appropriate? Skim, working session, or deep dive?

**GATE 1:** Confirm framing.

Use `AskUserQuestion` with the following shape:

```
Question: "Is this the right framing of the problem before we go deep?"
Options:
- "Yes, proceed with this framing"
- "Adjust framing slightly — I'll specify"
- "Reframe completely — I'll restate the question"
- "Stop — I need to think about what I'm actually asking first"
```

Do not proceed to Phase 2 until the user picks an option (or specifies an alternative via "Other").

---

### Phase 2 — Decompose

**Goal:** Break the question into orthogonal sub-questions or axes that can be analyzed separately.

1. **Propose 3–6 decomposition axes.** Each axis should be:
   - **Orthogonal** — answers along one axis don't determine answers along another.
   - **Concretely investigable** — each could in principle produce evidence.
   - **Named in the user's domain language**, not abstract categories.
2. **For each axis, label what's known, unknown, and assumed.** Use exactly these three labels.
3. **Identify load-bearing assumptions.** Mark any assumption that, if false, changes the whole analysis. These are the assumptions the perspectives in Phase 3 will be most useful for stressing.
4. **Flag axes that are the user's actual interest** vs. axes that are background.

**GATE 2:** Confirm decomposition and prioritize.

Use `AskUserQuestion`:

```
Question: "These are the axes I'd analyze. Which subset matters most for your situation?"
Options:
- "All of them, in this order"
- "Focus deeply on [axes 1, 2] and lightly on the rest"
- "Add an axis I'm missing — I'll specify"
- "Drop one or more axes — I'll specify"
```

Adjust the axis list based on the answer. Do not proceed to Phase 3 with a decomposition the user hasn't confirmed.

---

### Phase 3 — Multi-perspective Analysis

**Goal:** Run the question through perspectives the user couldn't easily generate alone. This is where the system earns its keep.

#### 3a. Run the core roster (always)

For each of the six core perspectives, produce:
- **Lens:** What this perspective is looking for in one sentence.
- **Take on the question:** 3–6 sentences. Specific to *this* question, not generic.
- **What only this lens sees:** One sentence naming the insight that doesn't come from the others.

Core perspectives:

1. **Red team** — actively trying to refute the user's stated or revealed framing. What evidence would make the user wrong? What's the hidden adversary?
2. **Steel-man** — strongest version of the opposite or alternative position. If someone disagreed with the user's premise, what's the best version of that disagreement?
3. **Blind-spot scan** — what is the user not seeing because of their position, role, or recent history? What's selection-biased about their evidence base?
4. **Future-self (6 months)** — looking back from six months in the future, what does the user wish they'd noticed now? What will feel obvious then?
5. **Naive newcomer** — what questions does someone with no context ask that everyone embedded would skip? Which embedded assumptions are doing real work?
6. **Affected party** — whoever bears the consequences (other than the user). What does this look like from inside their experience?

#### 3b. Propose scope-specific additions

Based on the question's domain, propose 2–4 *additional* perspectives that would be useful. For problem analysis, candidates include:
- **Domain expert** (specify which domain) — what's the technically informed view?
- **The system itself** (anthropomorphized) — if the system in question could speak, what would it say is going on?
- **Historical pattern** — has this happened before, here or elsewhere? What did the analogous situation reveal?
- **The unintended winner** — who or what benefits from the current situation continuing? (Sometimes the problem persists because someone is being served by it.)

Use `AskUserQuestion` to confirm:

```
Question: "Which of these additional perspectives would add the most for your specific question?"
Options:
- "[Specific perspective 1] — most relevant"
- "[Specific perspective 2]"
- "All of them"
- "None — the core six are enough"
```

Run only the additional perspectives the user picks.

#### 3c. After running all perspectives

Identify:
- **Convergences** — points multiple perspectives agree on. These are likely the most reliable observations.
- **Productive disagreements** — places perspectives genuinely conflict. These are where the analysis is doing real work.
- **One-source claims** — observations only one perspective produced. Flag for the stress-test phase.

**GATE 3:** Decide depth.

Use `AskUserQuestion`:

```
Question: "Multi-perspective pass is complete. Which thread to pull on hardest in the stress-test?"
Options:
- "[Specific convergence to verify]"
- "[Specific disagreement to resolve]"
- "[Specific one-source claim to test]"
- "All of them — proceed to stress-test on full output"
```

---

### Phase 4 — Stress-test

**Goal:** Try to break the analysis before the user acts on it.

1. **Pre-mortem.** Imagine: in six months, the user looks back and the analysis was wrong in some important way. What was wrong? Generate 3–5 specific failure modes. For each: how would the user know they're in that failure mode early?
2. **Cascade effects.** If the analysis is right and the user acts on it, what second- and third-order consequences follow that haven't been named? Some are good (worth amplifying); some are bad (worth pre-mitigating).
3. **Adversarial check.** What's the single strongest objection a smart, informed person would raise? Steel-man it. Then: does the analysis hold up against it, or does it need a revision?
4. **Confidence calibration.** For each major claim in the analysis so far, label: *high confidence* (multiple perspectives + tested logic), *medium confidence* (consistent reasoning but limited evidence), or *low confidence* (one source or untested assumption).

**GATE 4:** Decide what makes it into the final synthesis.

Use `AskUserQuestion`:

```
Question: "Which stress-test findings should be carried into the final synthesis as constraints or caveats?"
Options:
- "All of them — full caveats in synthesis"
- "Only [specific failure modes / objections]"
- "Loop back to Phase 3 with [specific perspective] — something is still missing"
- "Synthesis as-is — caveats acknowledged but not load-bearing"
```

---

### Phase 5 — Synthesize

**Goal:** Produce the terminal artifact. For problem analysis, that's a diagnosis + leverage points + calibrated confidence — *not* a recommendation, *not* a plan. The user does the deciding; the system does the seeing.

Output format (see "Output Format" section below).

After producing the synthesis:

**FINAL GATE:** Use `AskUserQuestion`:

```
Question: "Synthesis complete. What's next?"
Options:
- "Done — this is what I needed"
- "Convert the leverage points into a decision (run /deepthink-decision next)"
- "Convert into a plan (run /deepthink-plan next)"
- "Loop back — [specific phase] needs another pass"
```

---

## Constraints

### Must
- Run all five phases in order. Never skip Phase 1 (Frame) or Phase 4 (Stress-test).
- Stop at every gate and use `AskUserQuestion` (or labeled `**GATE:**`) before proceeding.
- Run the full core roster of six perspectives — no shortcuts to "the most relevant ones."
- Distinguish stated framing from revealed framing in Phase 1.
- Label load-bearing assumptions explicitly in Phase 2.
- Calibrate confidence (high / medium / low) on every major claim in Phase 4.
- Produce a *diagnosis* in Phase 5, not a recommendation.

### Must Not
- Generate all five phases in one continuous output. The whole point is the gates.
- Produce generic "what red team would say" content. Each perspective's take must be specific to the user's question.
- Rank one perspective as the "winner." The roster's value is in the disagreement, not the verdict.
- Treat absence of evidence as evidence of absence — if a perspective produces nothing, say so explicitly rather than fabricating a take.
- Convert the diagnosis into a recommendation in Phase 5. That is a different prompt's job.
- Dismiss the user's stated framing without naming why a reframe is warranted.
- Run a stress-test that only confirms the analysis. If pre-mortem produces no real failure modes, push harder.

---

## False-Positive Prevention

1. **Beware "deep" output that's actually wide.** Five paragraphs from each of six perspectives can feel rigorous while saying nothing the user couldn't have generated alone. The test: does each perspective produce a claim that, if you read it cold, you'd say "I wouldn't have thought of that"? If not, the perspective is being generic — push for specificity.
2. **The user's stated framing is sometimes right.** Don't reframe by default. Reframe only when there's a specific gap between stated and revealed intent that, if left alone, would route the entire analysis at the wrong target.
3. **Convergence is suspicious when perspectives are similar.** Two perspectives that agree because they share a default worldview are not corroboration. Convergence between *genuinely different* lenses (e.g., red-team and affected-party) is the meaningful signal.
4. **A perspective that "produces nothing" is data.** If the affected-party lens reveals no second-party impact, that may mean the problem is genuinely internal to the user — useful information, not a failure of the perspective.
5. **Pre-mortem can become defensive forecasting.** If the failure modes generated are all variations of "what if the user is wrong," the pre-mortem isn't doing its job. Push for failure modes that come from outside the user's control.
6. **Don't confuse depth with length.** A short, sharp synthesis with three calibrated-confidence claims beats a six-page synthesis full of medium-confidence platitudes.
7. **The system can be used to procrastinate on action.** If the user has run this same problem through the system more than twice with no decision or movement, the system itself has become the avoidance. Flag it and recommend `/deepthink-decision`.

---

## Output Format

Use this exact structure for the final synthesis (Phase 5):

```markdown
## Question (as framed in Phase 1)
[One sentence — the framing the user confirmed at GATE 1.]

## Diagnosis
[3–6 sentences. What's actually going on, named in concrete terms. The diagnosis is the answer to the question, not a recommendation.]

## Leverage points
- **[Leverage point 1]** — [why it's a leverage point: small input, large effect on the diagnosis. 1–2 sentences.] *Confidence: [high / medium / low].*
- **[Leverage point 2]** — [...]
- **[Leverage point 3]** — [...]
[3–5 leverage points total. Each is a place the user could push to learn more, change the situation, or test an assumption — not a thing they should do, just where the action is.]

## Load-bearing assumptions
- **[Assumption 1]** — [stated as a conditional]. *If false, the diagnosis changes how: [...]*
- **[Assumption 2]** — [...]
[The assumptions Phase 2 surfaced and Phase 4 tested. These are what the user should be most alert to invalidating.]

## What multi-perspective pass surfaced that the user might have missed
- [Specific insight from the perspective phase that wasn't already in the user's framing — 1–3 items, with the perspective named.]

## Stress-test verdict
- **Strongest objection:** [from Phase 4 adversarial check, in one sentence.]
- **Most plausible failure mode:** [the failure mode from pre-mortem the user is most exposed to, with an early-warning sign.]
- **Cascade effects to watch:** [1–2 second-order consequences, good or bad.]

## Confidence summary
- **High-confidence claims:** [list, terse.]
- **Medium-confidence claims:** [list, terse.]
- **Low-confidence claims:** [list, terse — these are the claims most worth verifying before acting.]

## What this synthesis is *not*
[One sentence. Specifically: this is not a decision, not a plan, not a spec. If the user wants those, name which prompt to run next.]
```

---

## Verification

Before declaring the synthesis complete, the model must check:

- [ ] All five phases ran, with a gate after each.
- [ ] Phase 1 produced both stated and revealed framings, and the user confirmed which to use.
- [ ] Phase 2 produced 3–6 axes with known/unknown/assumed labels and load-bearing assumptions flagged.
- [ ] Phase 3 ran the full core roster of six perspectives, plus any user-confirmed additions.
- [ ] Each perspective produced a take specific to this question, not generic content.
- [ ] Phase 4 produced at least three pre-mortem failure modes, a steel-manned objection, and confidence labels on major claims.
- [ ] Phase 5 produced a diagnosis (not a recommendation), with leverage points, load-bearing assumptions, and a confidence summary.
- [ ] The synthesis names what it is *not* — pointing the user to the right next prompt if they need a decision, plan, or spec.
