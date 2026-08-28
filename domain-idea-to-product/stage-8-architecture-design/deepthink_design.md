---
title: "Deep-Think: Design / Architecture"
category: deep-analysis/design
description: "A multi-phase, multi-perspective design system for working through what to build with an AI model at a depth that compensates for the absence of a human team. Drives the model through Frame → Decompose into design dimensions → Multi-perspective → Stress-test → Synthesize, using AskUserQuestion at every gate. Terminal artifact: design spec with documented tradeoffs, constraints, and open questions."
techniques:
  - ST-01
  - ST-02
  - ST-04
  - ST-42
  - RT-02
  - RT-07
  - CM-02
  - QA-01
  - QA-02
  - QA-04
difficulty: advanced
tags:
  - deep-analysis
  - design
  - architecture
  - multi-perspective
  - tradeoff-analysis
  - specification
  - askuserquestion
  - gated-workflow
updated: "2026-05-08"
related_prompts:
  - domain-deep-analysis/deepthink_problem_analysis.md
  - domain-deep-analysis/deepthink_decision.md
  - domain-deep-analysis/deepthink_plan.md
  - domain-software-engineering/analysis/architecture/architecture_layer_identification.md
  - domain-prompt-engineering/evaluation/correctness_tradeoff_forcer.md
  - domain-prompt-engineering/evaluation/correctness_pre_mortem.md
---

# Deep-Think: Design / Architecture

**Objective:** Work through *what to build* (a system, a process, an organizational structure, a curriculum, a product feature) at a depth that would normally require a team. Drive the model through five disciplined phases — Frame, Decompose into design dimensions, Multi-perspective analysis, Stress-test, and Synthesize — pausing at each gate to let the user redirect, prune, or go deeper. Produce a design spec with documented tradeoffs, named constraints, and explicit open questions — not a polished proposal that hides its uncertainty.

**When to use:** The user needs to design something — a software architecture, a feature spec, an organizational structure, a workshop curriculum, a hiring process, a personal system. Examples: "Design a multi-agent system for X", "What should our deployment pipeline look like?", "How should we structure the engineering team?", "Design my personal review cadence". Use this when *what to build* is the question. If the question is whether to build it, run `deepthink_decision.md`. If you've already designed it and need to schedule the build, run `deepthink_plan.md`.

**Audience:** Architects, designers, leads, anyone designing a system one-on-one with an AI and trying to compensate for the missing room of design reviewers.

---

## Inputs Required

1. **What you're designing.** One sentence — system, feature, structure, process.
2. **Who or what it's for.** Users, operators, maintainers, audience. Be specific.
3. **Hard requirements.** Things that are not negotiable (regulatory, performance, capacity, integration, deadline).
4. **Soft requirements.** Things you'd like but could trade off.
5. **Known constraints.** What you can't change (existing systems, team capabilities, budget).
6. **Anything you're already leaning toward.** A specific approach, pattern, or stack — surfacing the lean lets the perspectives push against it.

If items 1–3 are missing, ask before starting Phase 1.

---

## Operating Mode

Inherit the shared deep-think operating model from [`BACKBONE.md`](../../domain-deep-analysis/BACKBONE.md): run the five phases in order, stop at every gate, use `AskUserQuestion` when available, and fall back to a labeled `**GATE:**` block in plain chat. For designs, use in-phase questions for clarifying requirements, prioritizing design dimensions, surfacing implicit constraints, and confirming tradeoff weightings.

---

## Instructions

### Phase 1 — Frame

**Goal:** Make sure the design is being scoped to the real problem, not a familiar shape.

1. **Restate what's being designed.** One sentence: "[Thing] for [who/what], satisfying [hard requirement(s)] within [constraint(s)]."
2. **Surface stated vs. revealed problem.** Stated = the design brief. Revealed = the underlying need that the design is supposed to satisfy. Name the gap if there is one — designs often fail because they solve the stated problem cleanly while leaving the revealed problem untouched.
3. **Right-design check.** Common reframes:
   - "Design X" often hides "Is X the right thing to build, or is there a simpler thing that solves the same need?"
   - "Build a system that does Y" often hides "Is a system the right shape? Could a process or a manual workflow get us 80%?"
   - "Replace the legacy X" often hides "Why is X legacy? Are we about to recreate the same accidental complexity?"
4. **Constraint surfacing.** Some constraints are stated; others are implicit. Surface the implicit ones — assumptions about scale, latency, team skills, deployment environment, organizational politics. Implicit constraints that aren't named are the ones that wreck designs.
5. **Reversibility.** Are design choices here Type 1 (one-way; hard to change later — schema choices, public APIs, organizational structures) or Type 2 (easy to revise)? Type 1 dimensions deserve disproportionate attention.

**GATE 1:** Confirm framing and constraint set.

Use `AskUserQuestion`:

```
Question: "Is this the right framing of what we're designing and the real constraints before we go deep?"
Options:
- "Yes — proceed with this scope and constraints"
- "Add a constraint I'm missing — I'll specify"
- "Reframe — the underlying need is different from what I said"
- "Stop — I should run /deepthink-decision first to confirm we should build this at all"
```

---

### Phase 2 — Decompose into Design Dimensions

**Goal:** Surface the dimensions along which the design has to make choices, and the tradeoffs each choice forces.

1. **Identify design dimensions.** Each dimension is a place where the design must take a position. Common categories:
   - **Structural** — boundaries, interfaces, what's coupled to what.
   - **Data** — what's the source of truth, what's derived, what's persisted vs. ephemeral.
   - **Control flow / coordination** — who orchestrates whom, sync vs. async, push vs. pull.
   - **Failure handling** — what fails, what degrades, what's recoverable.
   - **Evolution** — what's expected to change and how the design accommodates change.
   - **Operational** — observability, deployability, who runs it, how it's debugged.
   - **Human** (if applicable) — who uses it, who maintains it, what skill assumptions are baked in.
2. **For each dimension, surface 2–4 candidate choices.** Don't pick yet — name the candidates and what each privileges.
3. **Name the tradeoffs sharply.** For each dimension, in one sentence: "Choice A privileges [X] at the cost of [Y]. Choice B privileges [Y] at the cost of [X]." If you can't name the tradeoff, the candidates aren't really different.
4. **Identify load-bearing dimensions.** Which dimensions, if chosen wrong, can't easily be revisited? These get the most multi-perspective attention.
5. **Flag dependencies between dimensions.** Some choices in one dimension constrain choices in another (e.g., a sync coordination model often forces a different failure handling approach than async).

**GATE 2:** Confirm dimensions, tradeoffs, and which are load-bearing.

Use `AskUserQuestion`:

```
Question: "These are the design dimensions and tradeoffs. Adjust before we run perspectives?"
Options:
- "Looks right — proceed"
- "Add a dimension I'm missing"
- "Reweight — [dimension] is more / less load-bearing than I implied"
- "A tradeoff statement is wrong — I'll restate"
```

---

### Phase 3 — Multi-perspective Analysis

**Goal:** Run the design through perspectives the user couldn't easily generate alone, especially for the load-bearing dimensions.

#### 3a. Run the mandatory roster (always)

Run the Phase 3 mandatory perspective roster defined in [`BACKBONE.md`](../../domain-deep-analysis/BACKBONE.md): red team, steel-man, blind-spot scan, future-self, naive newcomer, and affected party. For designs, each lens must include its lens statement, its take on the design, and the load-bearing dimension it most strongly flags.

#### 3b. Propose scope-specific additions

Use the design/architecture candidate pool in [`BACKBONE.md`](../../domain-deep-analysis/BACKBONE.md) to propose 2–4 additional perspectives tailored to the user's design context. Confirm the additions with `AskUserQuestion`/`**GATE:**` and run only the perspectives the user picks.

#### 3c. After running all perspectives

Identify:
- **Convergent design choices** — dimensions where multiple perspectives agree on the right pick. Strong signal.
- **Productive disagreement** — dimensions where perspectives genuinely conflict and force the user to take a position rather than hedge.
- **Surfaced surprises** — anything a perspective flagged that wasn't in the original framing.

**GATE 3:** Decide depth.

Use `AskUserQuestion`:

```
Question: "Multi-perspective pass is complete. What to stress-test hardest?"
Options:
- "[Specific dimension where perspectives disagreed]"
- "[The maintainer perspective's flag] in particular"
- "[Specific failure mode the red team surfaced]"
- "All of them — full stress-test"
```

---

### Phase 4 — Stress-test

**Goal:** Try to break the design before the user starts building.

1. **Pre-mortem.** Imagine: in two years, the design has aged badly. What aged worst? Generate 3–5 specific aging modes — what looked clean became gnarly, what was simple became complex, what was decoupled became tangled. For each, what early signal would tell the user it's happening?
2. **Cascade analysis.** If any single component / boundary / interface fails, what propagates? Which failure modes are local vs. systemic?
3. **Adversarial check.** Strongest objection from a smart, experienced designer. Steel-man it. Does the design hold or does it need revision?
4. **"What changes are easy / hard" matrix.** For 3–5 plausible future changes (scale up, add a feature class, swap a dependency, regulatory change), classify: trivial / contained / requires partial redesign / requires full redesign. The shape of this matrix tells you where the design is brittle.
5. **Dependency stress.** What external dependencies (libraries, services, vendors, organizational commitments) does the design assume? Which ones, if they evolved or disappeared, would force significant rework?
6. **Confidence calibration.** Rate confidence in: each load-bearing dimension's choice (high/medium/low), the design's tolerance to expected change (high/medium/low), the design's clarity to a maintainer (high/medium/low).

**GATE 4:** Decide what makes it into the synthesis.

Use `AskUserQuestion`:

```
Question: "Which stress-test findings should be carried into the spec?"
Options:
- "All of them — full risk register and open questions in spec"
- "Bake [specific mitigation] into the design"
- "Reverse the choice on [specific load-bearing dimension] based on stress-test"
- "Loop back — Phase 2 missed a dimension"
```

---

### Phase 5 — Synthesize

**Goal:** Produce a design spec that can be implemented (or critiqued, or compared to alternatives). State the choices on each dimension, name the rationale, document the tradeoffs accepted, and surface the open questions.

After producing the synthesis:

**FINAL GATE:** Use `AskUserQuestion`:

```
Question: "Spec is on the table. What's next?"
Options:
- "Convert to a build plan (run /deepthink-plan)"
- "Iterate on a specific section — I'll point at it"
- "Sit with it and review tomorrow with fresh eyes"
- "Loop back — [specific phase] needs another pass"
```

---

## Constraints

### Must
- Run all five phases in order. Never skip Phase 1 (Frame) or Phase 4 (Stress-test).
- Stop at every gate and use `AskUserQuestion` (or labeled `**GATE:**`) before proceeding.
- Run the full core roster of six perspectives.
- Surface implicit constraints in Phase 1 — not just the stated ones.
- Name tradeoffs in one sentence per design dimension in Phase 2.
- Classify load-bearing vs. revisable dimensions explicitly.
- Run the maintainer-two-years-from-now perspective whenever the design will be operated or evolved by anyone (including future-user).
- Take a position in Phase 5 on every load-bearing dimension. Open questions are fine; "no opinion" on a load-bearing dimension is not a spec.

### Must Not
- Generate all five phases in one continuous output.
- Produce a spec that hides uncertainty behind aesthetic polish. Open questions must be visible.
- Default to the user's stack history without examining whether it fits the constraints.
- Strawman the alternative architecture in Phase 3. The steel-man must be a credible expert's design, not a token "what someone might say."
- Skip the maintainer perspective. Designs are read more often than written.
- Produce a "comprehensive" spec that's actually just an enumeration of options without a position.
- Leave implementation magic in load-bearing dimensions. Vague choice on a load-bearing dimension creates rework.

---

## False-Positive Prevention

1. **Designs convergence-toward-familiar is the most common failure mode.** The user's existing stack and recent reading dominate unless the perspectives push hard. The blind-spot scan and steel-man perspectives in Phase 3 exist for this. If they don't surface anything, push harder — they're being polite.
2. **A "balanced" tradeoff is often a missed tradeoff.** Real designs privilege something. If the spec claims to optimize for everything equally, it's optimizing for nothing in particular and will be beaten by a design that picks a side.
3. **Reversibility is the design's superpower.** Type 2 (easy-to-change) dimensions can be decided fast and revised in flight. Spend the design budget on Type 1 dimensions. The Phase 1 reversibility classification controls this.
4. **The maintainer perspective surfaces operational debt before it's incurred.** A design that's elegant to write and miserable to debug is a design that's about to age badly. Don't suppress operational ugliness — name it.
5. **"Open questions" in the spec is a feature, not a flaw.** A spec that pretends to know the things it doesn't know is fragile. Name the things you don't yet know, with a plan for resolving them (prototype, research, decision needed).
6. **Beware "general-purpose" framing.** A design that's "flexible enough for any future need" usually isn't a design — it's an enumeration. Push for a design that fits *this* requirement well, with named extension points for *plausible* future needs, not arbitrary ones.
7. **The system can be used to procrastinate on building.** If the user has run two or more design passes without a prototype or proof-of-concept attempt, the design phase is the avoidance. Some designs only reveal their flaws when partially built. Recommend a small build experiment.

---

## Output Format

Use this exact structure for the final spec (Phase 5):

```markdown
## What we're designing
[One sentence: thing + audience + hard requirements + key constraint, as confirmed in Phase 1.]

## Design summary
[3–5 sentences. The shape of the design. What it commits to, what it gives up, and the single sentence that captures its character.]

## Choices on each dimension

### [Dimension 1 — load-bearing]
- **Choice:** [What was picked.]
- **Why:** [Rationale in 1–2 sentences. Cite the perspective(s) that converged on this.]
- **Tradeoff accepted:** [What this gives up. Be specific.]
- **Confidence:** [high / medium / low].
- **Reversibility:** [Type 1 — hard to change later / Type 2 — easy to change.]

### [Dimension 2 — load-bearing]
[...]

### [Dimension 3 — revisable]
[Briefer.]

[Continue for all dimensions. Load-bearing ones get full treatment; revisable ones can be terse.]

## Constraints (stated + implicit)
- [Stated constraint 1]
- [Stated constraint 2]
- [Implicit constraint surfaced in Phase 1]
- [...]

## What this design assumes
- [Load-bearing assumption 1] — [tested / reasonable / untested]
- [Load-bearing assumption 2] — [...]

## What changes easily; what doesn't
| Change | Easy / Contained / Partial redesign / Full redesign |
|--------|------------------------------------------------------|
| [Plausible change 1] | [Classification] |
| [Plausible change 2] | [Classification] |
| [Plausible change 3] | [Classification] |

## Risk register (carried from Phase 4)
- **[Risk 1]** — [aging mode or failure mode] — [mitigation built in: ...]
- **[Risk 2]** — [...]

## Open questions
- [Question 1] — [why it matters, plan for resolving: prototype, research, decision needed.]
- [Question 2] — [...]

## What this synthesis is *not*
[One sentence. Specifically: this is a design spec, not a build plan (use /deepthink-plan to schedule it) and not a decision about whether to build (use /deepthink-decision).]
```

---

## Verification

Before declaring the spec complete, the model must check:

- [ ] All five phases ran, with a gate after each.
- [ ] Phase 1 produced both stated and revealed framing, surfaced implicit constraints, and classified reversibility.
- [ ] Phase 2 produced design dimensions with named tradeoffs (one sentence per dimension), and identified load-bearing vs. revisable dimensions.
- [ ] Phase 3 ran the full core roster + any user-confirmed additions, including the maintainer perspective.
- [ ] Phase 4 produced pre-mortem aging modes, a what-changes-easily matrix, and confidence calibration on load-bearing dimensions.
- [ ] Phase 5 takes a position on every load-bearing dimension and acknowledges open questions explicitly.
- [ ] Tradeoffs are named per dimension, not hidden behind "balanced design" framing.
- [ ] The spec does not pretend to be a plan or a decision.
