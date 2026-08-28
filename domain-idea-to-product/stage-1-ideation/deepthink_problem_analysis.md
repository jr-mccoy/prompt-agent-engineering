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
updated: "2026-07-19"
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
4. **Time available for this analysis.** 15 min, 1 hour, multi-session. Selects the depth profile (below).
5. **Anything the user has already concluded or suspects.** Optional — surfacing prior beliefs is what lets the perspectives push against them.
6. **Evidence on hand.** Optional — data, documents, past attempts, observations the user can share or summarize. Claims grounded in this evidence are labeled differently from claims produced by reasoning alone.

**Intake rule:** Item 1 is mandatory — ask for it if missing. For items 2–4, if missing, propose a plausible default in one line each ("I'll assume medium stakes and a ~1 hour budget — correct me at the gate") and fold confirmation into GATE 1 rather than blocking the start. Never silently assume item 3 (stakes) is high or low without stating the assumption.

---

## Depth Profiles

The time budget from Input 4 selects a profile. **Depth scales by compressing output, never by cutting phases or gates.**

| | Quick (~15 min) | Standard (~1 hour) | Deep (multi-session) |
|---|---|---|---|
| Phase 2 axes | 3 | 3–5 | 4–6 |
| Per-lens output (Phase 3) | ≤60 words | ≤120 words | ≤250 words |
| Scope-specific added lenses | 0–1 | 2–3 | 3–4 |
| Pre-mortem failure modes | 3 | 3–5 | 5 |
| Synthesis length | ~½ page | ~1 page | 1–2 pages |

**Stakes modifier:** at high stakes, run the stress-test (Phase 4) at one profile level deeper than the rest of the analysis, whatever the time budget. At low stakes, adversarial checks may be brief but must still exist.

**Multi-session support (Deep profile):** at every gate, end the message with a compact `**STATE:**` block — confirmed framing, confirmed axes, perspectives run, open threads — so the analysis can resume in a fresh session by pasting the last STATE block.

---

## Operating Mode

Inherit the shared deep-think operating model from [`BACKBONE.md`](../../domain-deep-analysis/BACKBONE.md): run the five phases in order, stop at every gate, use `AskUserQuestion` when available, and fall back to a labeled `**GATE:**` block in plain chat.

**Gate mechanics:**
- Gate options are suggestions, not a menu the user is locked into. Free-text answers at any gate are always valid; interpret them and restate what you understood before acting on them.
- Keep option labels short (≤6 words); put detail in the question text or the preceding analysis, not the labels.
- Use in-phase questions when a small user answer would materially change the next step; otherwise proceed with a stated assumption and invite correction at the next gate.

**Loop-back mechanics:** when a gate sends the analysis back to an earlier phase, re-run only the affected content — do not regenerate outputs the user already confirmed. If the same phase loops more than twice, stop and name it: the loop is now the finding (see False-Positive Prevention #7).

**Fallback if BACKBONE.md is unavailable:** state that the backbone file wasn't found, then use this built-in core roster for Phase 3a — **red team** (attacks the framing and the evidence), **steel-man** (strongest version of the user's own suspicion from Input 5), **blind-spot scan** (what category of cause is the user structurally unlikely to see), **future-self** (the user 12 months out, looking back), **naive newcomer** (what an intelligent outsider with no context would ask first), **affected party** (whoever else the problem touches, in their own voice) — and generate scope-specific candidates yourself in 3b.

---

## Instructions

### Phase 1 — Frame

**Goal:** Make sure the analysis runs against the right question.

1. **Restate the question** in your own words, in one sentence. Then in a second sentence, restate what the user seems to *actually* want to understand (which may differ from what they asked).
2. **Surface stated vs. revealed framing.** Stated = what they wrote. Revealed = what the question + the "why now" + the stakes imply they actually need. Name the gap if there is one; if there is no gap, say so in one sentence and move on — do not manufacture a reframe.
3. **Right-problem check.** Is this the question worth asking, or is there a load-bearing prior question? Common reframes:
   - "Why is X happening?" often hides "Is X actually happening as I think it is?"
   - "What should I think about Y?" often hides "What would change if I had a clear view of Y?"
   - "Is this a problem?" often hides "What would I do differently if it were?"
4. **Confirm the depth profile.** State the selected profile (Quick / Standard / Deep) and the stakes modifier, plus any intake defaults assumed under the Intake rule.

**GATE 1:** Confirm framing.

Use `AskUserQuestion` with the following shape:

```
Question: "Is this the right framing of the problem before we go deep?"
Options:
- "Yes — proceed"
- "Adjust framing — I'll specify"
- "Reframe completely — I'll restate"
- "Stop — let me rethink the question"
```

Do not proceed to Phase 2 until the user answers (option or free text).

---

### Phase 2 — Decompose

**Goal:** Break the question into orthogonal sub-questions or axes that can be analyzed separately.

1. **Propose axes** (count per depth profile). Each axis must be:
   - **Orthogonal** — answers along one axis don't determine answers along another.
   - **Concretely investigable** — each could in principle produce evidence.
   - **Named in the user's domain language**, not abstract categories.
2. **For each axis, label what's known, unknown, and assumed.** Use exactly these three labels. Where Input 6 evidence bears on an axis, cite it under *known*.
3. **Identify load-bearing assumptions.** Mark any assumption that, if false, changes the whole analysis. These are the assumptions the perspectives in Phase 3 will be most useful for stressing.
4. **Flag axes that are the user's actual interest** vs. axes that are background.

**GATE 2:** Confirm decomposition and prioritize.

Use `AskUserQuestion`:

```
Question: "These are the axes I'd analyze. Which subset matters most for your situation?"
Options:
- "All, in this order"
- "Deep on some — I'll specify"
- "Add an axis — I'll specify"
- "Drop axes — I'll specify"
```

Adjust the axis list based on the answer. Do not proceed to Phase 3 with a decomposition the user hasn't confirmed.

---

### Phase 3 — Multi-perspective Analysis

**Goal:** Run the question through perspectives the user couldn't easily generate alone. This is where the system earns its keep.

#### 3a. Run the mandatory roster (always)

Run the Phase 3 mandatory perspective roster defined in [`BACKBONE.md`](../../domain-deep-analysis/BACKBONE.md) (or the built-in fallback roster from Operating Mode). Every lens uses this exact template, within the per-lens word limit of the active depth profile:

```markdown
**[Lens name]**
- *Lens:* [one sentence — what this lens optimizes for / is paranoid about]
- *Take:* [its analysis of this specific question]
- *Only this lens sees:* [one claim the other lenses would not produce]
```

**Novelty bar:** the *Only this lens sees* line must pass the cold-read test — a claim the user would plausibly react to with "I hadn't thought of that." If a lens genuinely produces nothing beyond the other lenses, write `*Only this lens sees:* nothing distinct — [why]` rather than fabricating a take. An empty lens is data (see False-Positive Prevention #4).

#### 3b. Propose scope-specific additions

Use the problem-analysis candidate pool in [`BACKBONE.md`](../../domain-deep-analysis/BACKBONE.md) (or self-generate under the fallback) to propose additional perspectives tailored to the user's domain, count per depth profile. Confirm the additions with `AskUserQuestion`/`**GATE:**` and run only the perspectives the user picks.

#### 3c. After running all perspectives

Identify:
- **Convergences** — points multiple perspectives agree on. Note whether the converging lenses are genuinely different in worldview; convergence between similar lenses is weak signal (False-Positive Prevention #3).
- **Productive disagreements** — places perspectives genuinely conflict. These are where the analysis is doing real work.
- **One-source claims** — observations only one perspective produced. Flag for the stress-test phase.
- **Evidence status** — for each convergence and one-source claim, note whether it is grounded in Input 6 evidence or produced by reasoning alone.

**GATE 3:** Decide depth.

Use `AskUserQuestion`:

```
Question: "Multi-perspective pass is complete. Which thread should the stress-test pull hardest on?"
Options:
- "[Named convergence]"
- "[Named disagreement]"
- "[Named one-source claim]"
- "All of them"
```

Replace bracketed labels with short names of the actual findings.

---

### Phase 4 — Stress-test

**Goal:** Try to break the analysis before the user acts on it. Apply the stakes modifier: at high stakes, this phase runs one depth level above the rest of the analysis.

1. **Pre-mortem.** Imagine: in six months, the user looks back and the analysis was wrong in some important way. What was wrong? Generate failure modes (count per depth profile), including at least one that originates *outside the user's control* (False-Positive Prevention #5). For each: how would the user know they're in that failure mode early?
2. **Cascade effects.** If the analysis is right and the user acts on it, what second- and third-order consequences follow that haven't been named? Some are good (worth amplifying); some are bad (worth pre-mitigating).
3. **Adversarial check.** What's the single strongest objection a smart, informed person would raise? Steel-man it. Then: does the analysis hold up against it, or does it need a revision? If it needs revision, revise the affected claims now and mark them `*revised under objection*`.
4. **Confidence calibration.** For each major claim in the analysis so far, label: *high confidence* (multiple genuinely-different perspectives + tested logic, or direct evidence), *medium confidence* (consistent reasoning but limited evidence), or *low confidence* (one source, untested assumption, or reasoning-only where evidence should exist).

**GATE 4:** Decide what makes it into the final synthesis.

Use `AskUserQuestion`:

```
Question: "Which stress-test findings should be carried into the final synthesis as constraints or caveats?"
Options:
- "All of them"
- "Only some — I'll specify"
- "Loop back to Phase 3 — I'll say which lens"
- "Synthesis as-is"
```

---

### Phase 5 — Synthesize

**Goal:** Produce the terminal artifact. For problem analysis, that's a diagnosis + leverage points + calibrated confidence — *not* a recommendation, *not* a plan. The user does the deciding; the system does the seeing.

Output format (see "Output Format" section below), sized per depth profile.

After producing the synthesis:

**FINAL GATE:** Use `AskUserQuestion`:

```
Question: "Synthesis complete. What's next?"
Options:
- "Done — this is what I needed"
- "Turn into a decision (/deepthink-decision)"
- "Turn into a plan (/deepthink-plan)"
- "Loop back — I'll say which phase"
```

---

## Constraints

### Must
- Run all five phases in order, with a gate after each. Phases compress under the Quick profile; they never disappear.
- Stop at every gate and use `AskUserQuestion` (or labeled `**GATE:**`) before proceeding. Accept free-text gate answers.
- Run the full core roster of six perspectives at every depth profile — compression shortens each lens, it never cuts lenses.
- Distinguish stated framing from revealed framing in Phase 1 (or state explicitly that they match).
- Label load-bearing assumptions explicitly in Phase 2.
- Distinguish evidence-grounded claims from reasoning-only claims wherever Input 6 evidence exists.
- Calibrate confidence (high / medium / low) on every major claim in Phase 4.
- Produce a *diagnosis* in Phase 5, not a recommendation.
- Emit a `**STATE:**` block at each gate when running the Deep profile.

### Must Not
- Generate all five phases in one continuous output. The whole point is the gates.
- Produce generic "what red team would say" content. Each perspective's take must be specific to the user's question and pass the novelty bar.
- Rank one perspective as the "winner." The roster's value is in the disagreement, not the verdict.
- Treat absence of evidence as evidence of absence — if a perspective produces nothing, say so explicitly rather than fabricating a take.
- Convert the diagnosis into a recommendation in Phase 5. That is a different prompt's job.
- Dismiss the user's stated framing without naming why a reframe is warranted — and never reframe when stated and revealed framing already match.
- Run a stress-test that only confirms the analysis. If the pre-mortem produces no real failure modes, push harder.
- Regenerate user-confirmed outputs during a loop-back.

---

## False-Positive Prevention

1. **Beware "deep" output that's actually wide.** Six perspectives can feel rigorous while saying nothing the user couldn't have generated alone. The per-lens template's *Only this lens sees* line is the enforcement mechanism: if that line is generic, the lens has failed regardless of how good the rest reads.
2. **The user's stated framing is sometimes right.** Don't reframe by default. Reframe only when there's a specific gap between stated and revealed intent that, if left alone, would route the entire analysis at the wrong target.
3. **Convergence is suspicious when perspectives are similar.** Two perspectives that agree because they share a default worldview are not corroboration. Convergence between *genuinely different* lenses (e.g., red-team and affected-party) is the meaningful signal — and Phase 3c must say which kind each convergence is.
4. **A perspective that "produces nothing" is data.** If the affected-party lens reveals no second-party impact, that may mean the problem is genuinely internal to the user — useful information, not a failure of the perspective.
5. **Pre-mortem can become defensive forecasting.** If the failure modes generated are all variations of "what if the user is wrong," the pre-mortem isn't doing its job. At least one failure mode must come from outside the user's control.
6. **Don't confuse depth with length.** A short, sharp synthesis with three calibrated-confidence claims beats a six-page synthesis full of medium-confidence platitudes. The depth-profile word limits exist to force this.
7. **The system can be used to procrastinate on action.** If the user has run this same problem through the system more than twice with no decision or movement — or a single phase loops more than twice within one run — the system itself has become the avoidance. Flag it and recommend `/deepthink-decision`.
8. **Reasoning-only claims can masquerade as findings.** A confident-sounding causal story built with no reference to the user's actual evidence is a hypothesis, not a diagnosis. Where evidence should exist and wasn't consulted, the claim caps at medium confidence.

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

## What the multi-perspective pass surfaced that you might have missed
- [Specific insight from the perspective phase that wasn't already in the user's framing — 1–3 items, with the perspective named.]

## Stress-test verdict
- **Strongest objection:** [from Phase 4 adversarial check, in one sentence — note if any claims were revised under it.]
- **Most plausible failure mode:** [the failure mode from pre-mortem the user is most exposed to, with an early-warning sign.]
- **Cascade effects to watch:** [1–2 second-order consequences, good or bad.]

## Confidence summary
- **High-confidence claims:** [list, terse — mark evidence-grounded vs. reasoning-only.]
- **Medium-confidence claims:** [list, terse.]
- **Low-confidence claims:** [list, terse — these are the claims most worth verifying before acting. Name the cheapest verification for each.]

## What this synthesis is *not*
[One sentence. Specifically: this is not a decision, not a plan, not a spec. If the user wants those, name which prompt to run next.]
```

---

## Verification

Before declaring the synthesis complete, the model must check:

- [ ] All five phases ran, with a gate after each, at the confirmed depth profile.
- [ ] Phase 1 produced both stated and revealed framings (or an explicit statement that they match), and the user confirmed.
- [ ] Phase 2 produced axes with known/unknown/assumed labels and load-bearing assumptions flagged.
- [ ] Phase 3 ran the full core roster of six perspectives, plus any user-confirmed additions, each within the per-lens word limit.
- [ ] Every lens's *Only this lens sees* line passes the cold-read novelty test, or explicitly declares "nothing distinct."
- [ ] Phase 3c labeled each convergence as strong (different-worldview lenses) or weak (similar lenses).
- [ ] Phase 4 produced the profile's count of pre-mortem failure modes including at least one outside the user's control, a steel-manned objection, and confidence labels on major claims.
- [ ] Evidence-grounded and reasoning-only claims are distinguished wherever the user supplied evidence.
- [ ] Phase 5 produced a diagnosis (not a recommendation), with leverage points, load-bearing assumptions, and a confidence summary with cheapest-verification notes on low-confidence claims.
- [ ] The synthesis names what it is *not* — pointing the user to the right next prompt if they need a decision, plan, or spec.
- [ ] If running Deep profile: a `**STATE:**` block was emitted at every gate.
