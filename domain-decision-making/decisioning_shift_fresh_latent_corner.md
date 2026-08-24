---
title: "Shift to a Fresh Latent Corner (Solution-Space Escape)"
category: decision-making
description: "Force an escape from the default solution set on a stuck problem by exploring radically different framings: first-principles rebuild, constraint inversion, problem redefinition, and adjacent-domain transplant. Holds the problem fixed and shifts the option set itself — distinct from viewpoint-shift prompts that hold options fixed."
techniques:
  - ST-01
  - ST-02
  - RT-01
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - decision-making
  - solution-space
  - reframing
  - first-principles
  - constraint-inversion
updated: "2026-04-25"
related_prompts:
  - domain-decision-making/decisioning_fresh_perspective_generator.md
  - domain-decision-making/decisioning_first_principles_problem_decomposition.md
  - domain-decision-making/decisioning_resource_constrained_solver.md
  - domain-prompt-engineering/escape-median/escapemedian_default_position_mapper.md
---

# Shift to a Fresh Latent Corner (Solution-Space Escape)

**Objective:** Take a stuck problem where the obvious solutions all share the same shape, and force the option set into a "fresh latent corner" — a region of the solution space the user has not considered. Generate options through four mechanisms: first-principles rebuild, constraint inversion, problem redefinition, and adjacent-domain transplant. Output 6–10 candidate options that are genuinely different from the user's current set, plus the test that distinguishes a real corner from a relabeled default.

**When to Use:**
- Every option you've considered "feels like the same option in a different costume."
- The team is converging fast on one solution and you suspect the convergence is groupthink.
- A previous tradeoff analysis returned a winner you can't get excited about.
- You're noticing the solution space looks suspiciously aligned with what's already been tried in this organization.

**When NOT to use:**
- The current option set is fine; you just don't know which to pick. Use `decisioning_fresh_perspective_generator.md` (viewpoint shift) or a tradeoff analyzer.
- The problem itself is malformed. Use `decisioning_first_principles_problem_decomposition.md` first to clarify the problem before expanding the solution space.
- You're asking the model to escape *its own* default output stance on a topic. Use the prompts in `domain-prompt-engineering/escape-median/`.

**Distinction from `decisioning_fresh_perspective_generator.md`:** That prompt holds the option set fixed and shifts the *viewpoint* evaluating them. This prompt holds the *problem fixed* and shifts the *option set itself*. They compose well — generate fresh options here, then evaluate them with viewpoint shifts.

**Audience:** Decision-makers facing a recurring "all my options look the same" symptom on a non-trivial choice.

---

## Inputs / Context

1. **The problem in one sentence.** Not the decision — the underlying problem the decision is trying to solve. ("Improve onboarding conversion" rather than "Pick option A or B for the onboarding redesign.")
2. **The current option set.** What has already been considered, in 3–7 named options. This is what we're trying to escape.
3. **What constraints have been treated as fixed.** Budget, timeline, team, technology stack, regulatory frame — anything no one has questioned yet.
4. **Previous solutions in this domain.** What's already been tried (in this org or industry) on this kind of problem? This is the historical center of mass we're trying to move away from.
5. **Why the current set feels the same.** One sentence: shared assumption? shared risk profile? shared timeline shape?

---

## Constraints

### Must
- Generate options through all four mechanisms — first-principles, constraint inversion, problem redefinition, adjacent-domain transplant — not just one.
- Produce a minimum of 6 candidate options total across the four mechanisms; at least one option per mechanism.
- Each candidate must be testable against a "fresh-corner test" (defined below). Anything that fails the test is a relabeled default and must be replaced.
- Name which assumption each candidate attacks. If the candidate doesn't attack a specific assumption, it's not from a fresh corner.
- Surface 1–2 candidates the user will likely reject as "we can't do that" — these are the most diagnostic. Mark them explicitly.
- End with a viability triage: which candidates merit a tradeoff analysis, which are useful as thought-provocations only, and which to discard.

### Must Not
- Generate variations of existing options (more / less / faster / slower versions of what's already on the list).
- Recombine existing options. A blend of A and B is not a fresh corner.
- Treat brainstorming volume as a substitute for genuine difference. 20 mediocre options that all share the same assumption are worse than 4 that don't.
- Discard candidates because they violate constraints the user said were fixed — that violation is the point. Mark them, don't drop them.
- Smuggle in cliché "moonshot" framings. A fresh corner is unfamiliar but specific, not vague-and-grand.

---

## Instructions

### Step 1 — Restate the problem and the historical center
Restate the problem in one sentence. Restate the current option set. Identify the **shared shape** — the assumption, risk profile, timeline, or stakeholder model that all current options have in common. This is the center we're moving away from.

### Step 2 — First-principles rebuild
Strip the problem down to its irreducible needs (what must actually be true for "the problem is solved"?). Then build solutions from those needs without referencing existing options. Generate 2–3 candidates.
- For each: name the irreducible need it serves and the assumption from the historical center it bypasses.

### Step 3 — Constraint inversion
For each constraint the user named as fixed (budget, timeline, team, stack, scope), invert it: "what if budget were 10x?" "what if budget were 1/10?" "what if we had 6 weeks instead of 6 months?" "what if no engineers were available?" Pick the 2–3 inversions that are most generative and produce 1 candidate each.
- For each: name the inverted constraint and what option became visible only because of the inversion.

### Step 4 — Problem redefinition
The user stated the problem in one sentence. Generate 3 alternative problem statements that share most of the underlying need but reframe it. Examples:
- Instead of "improve onboarding conversion," consider "reduce the cost of bad-fit signups," "shift activation upstream of signup," or "redefine activation as the actual KPI."
- Pick one alternative problem statement and generate 1–2 candidate options that solve it. They will not solve the original problem — that's expected. Mark the tradeoff.

### Step 5 — Adjacent-domain transplant
Pick a domain with structurally similar problem/solution dynamics: customer support escalation patterns for incident response, hospital triage for product prioritization, restaurant pre-shift for sprint kickoff, military supply logistics for inventory. Identify a solution mechanism from that domain and transplant it. Generate 1–2 candidates.
- For each: name the source domain, the mechanism being transplanted, and what the candidate looks like in the user's domain.

### Step 6 — Fresh-corner test
For every candidate, run this test:
- **Q1: What assumption from the historical center does it attack?** If "none," it's not a fresh corner.
- **Q2: Is it different in shape, not just degree?** A faster / cheaper / bigger version is degree, not shape. Reject.
- **Q3: Could a stakeholder reading it say "oh, we already considered that"?** If so, it's a relabeled default. Either sharpen what makes it different or drop it.

Replace any candidate that fails the test.

### Step 7 — Viability triage
Sort the surviving candidates into three buckets:
- **Real candidates:** worth running through a tradeoff analysis next. Will likely be 2–4 options.
- **Provocations:** not deployable, but useful as questions that reframe the original options. May violate stated constraints.
- **Discard:** failed the fresh-corner test, kept here only with a note on what failed.

### Step 8 — One assumption to test
Identify the single assumption that, if it turns out to be false or movable, would most expand the option set. Recommend one cheap test the user can run to validate or invalidate it before the next decision review.

---

## False-Positive Prevention

1. **Volume theatre.** Generating 15 options that share the same assumption is the failure mode this prompt exists to prevent. Stop at 6–10 if they pass the fresh-corner test.
2. **The "moonshot" trap.** Vague-but-grand options ("reinvent how we think about X") are not fresh corners; they are vague defaults. Force concreteness.
3. **Inversion shallow-pass.** Inverting "budget" by saying "spend more" and "spend less" generates two near-defaults. The inversion should expose a candidate that is invisible without the inversion.
4. **Adjacent-domain cosmetic transplant.** "Like a hospital triage system" is empty unless the actual mechanism (priority levels, escalation thresholds, time-to-attention budgets) is named and applied.
5. **Discarding the uncomfortable candidates.** The candidate the user dismisses as "we can't do that" is often the one teaching the most about which constraint is movable. Keep it as a provocation, not delete it.
6. **Problem-redefinition smuggling.** A redefinition that quietly preserves the original problem is not a redefinition. The new problem must be solvable by a candidate that does *not* solve the original.
7. **No assumption named.** Every candidate must point to a specific assumption it attacks. "Just a different idea" is not a fresh corner.

---

## Output Format

```
# Fresh latent corner — [problem in one sentence]

**Current options:** [list]
**Shared shape (historical center):** [the assumption / risk profile / timeline / stakeholder pattern all current options share]
**User's stated fixed constraints:** [list]

## First-principles rebuild
Irreducible needs: [list]
Candidates:
1. **[name]** — Attacks assumption: [assumption]. Description: [paragraph].
2. **[name]** — Attacks assumption: [assumption]. Description: [paragraph].

## Constraint inversion
Inversions explored: [list]
Candidates:
1. **[name]** — Inverted constraint: [constraint]. Becomes visible because: [reason]. Description: [paragraph].
2. …

## Problem redefinition
Alternative problem statement: "[new problem]"
Tradeoff with original: [what's lost / what's gained]
Candidates:
1. **[name]** — Description: [paragraph].

## Adjacent-domain transplant
Source domain: [domain]
Mechanism transplanted: [specific mechanism, named]
Candidates:
1. **[name]** — Description: [paragraph].

## Fresh-corner test
| Candidate | Assumption attacked | Different in shape? | Existing-in-disguise? | Status         |
|-----------|---------------------|---------------------|------------------------|----------------|
| [name]    | [assumption]        | yes / no            | no / yes               | keep / replace |
| …                                                                                              |

## Viability triage

**Real candidates (next: tradeoff analysis):**
1. [name] — [why it's real]
2. …

**Provocations (use as reframe questions):**
1. [name] — [the question it raises about a fixed constraint]

**Discarded:**
1. [name] — [which fresh-corner test it failed]

## One assumption to test
**Assumption:** [the single most leverage-rich assumption]
**Cheap test:** [paragraph — what experiment, observation, or conversation would validate or invalidate it within a week]
```

---

## Verification

- [ ] All four mechanisms produced at least one candidate (first-principles, constraint inversion, problem redefinition, adjacent-domain transplant).
- [ ] At least 6 candidates total before the fresh-corner test.
- [ ] Every surviving candidate names the assumption it attacks.
- [ ] The fresh-corner test was applied to each candidate, with status tracked.
- [ ] At least 1 candidate is marked as a "provocation" (likely-rejected but instructive).
- [ ] Adjacent-domain transplant names the actual mechanism, not just the domain.
- [ ] Problem redefinition produces a new statement that does not silently preserve the original.
- [ ] Viability triage sorts every candidate into real / provocation / discard.
- [ ] Final assumption-to-test names a cheap, time-boxed test (≤ 1 week of effort).
- [ ] No candidate is a degree-variant of an existing option.
