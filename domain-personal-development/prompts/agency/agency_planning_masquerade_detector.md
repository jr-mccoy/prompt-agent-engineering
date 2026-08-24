---
title: "Detect Planning That Masquerades as Execution"
category: personal-development/agency
description: "Audit a user's recent work sessions to find activity that feels like execution but is actually sophisticated procrastination — research binges, tool shopping, framework shopping, endless outlining — and name the underlying avoidance."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - agency
  - procrastination
  - execution
  - self-audit
  - diagnostic
updated: "2026-04-20"
related_prompts:
  - domain-personal-development/prompts/agency/agency_stuck_diagnosis.md
  - domain-personal-development/prompts/agency/agency_next_action_spec.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_unstructured_start_exploration.md
---

# Detect Planning That Masquerades as Execution

**Objective:** Audit recent work sessions for activity that produces the feeling of progress without producing the artifact that would actually move the project. Name the pattern, name what is being avoided, and return the user to execution without moralizing.

**When to use:** The user has been "working on" something for days or weeks with no externally visible change. They can describe what they're learning, evaluating, comparing, or planning. They cannot point to an artifact.

**Audience:** An individual reviewing their own work honestly. Not an observer auditing someone else.

---

## Inputs Required

1. **Project name and what "shipped" would look like.**
2. **Last 7–14 days of work activity.** What was actually opened, typed, read, watched, compared. Calendar, browser history, notes, or best-recall inventory.
3. **What has been produced as an artifact during that window.** Commits, drafts, published things, messages sent to real recipients. "Zero" is a valid answer.
4. **What the user has told themselves about why it isn't ready yet.** Verbatim, not cleaned up.

If artifact count is nonzero and matches the project's cadence, this prompt may not apply — say so and point them elsewhere.

---

## Instructions

### Step 1 — Classify the activity inventory

Sort the last 7–14 days of activity into four buckets:

- **Execution:** Produced an external artifact for the project (commit, draft, published post, email sent to a real recipient, recording).
- **Prep with ship-pressure:** Research or planning that was strictly necessary before the next execution step, not repeated, not expanded.
- **Planning-masquerade:** Research, tool comparison, framework shopping, outlining, template collection, "learning," or reorganization that did not end in an artifact.
- **Unrelated:** Work on other projects, life obligations, legitimate rest.

Return the counts or rough percentages per bucket. Be honest. If Execution is zero, say so plainly.

### Step 2 — Match the masquerade to a named pattern

Run the masquerade-bucket items against this taxonomy and name which one(s) are operating:

- **Optionality preservation.** Refusing to commit to a tool / stack / topic / format, evaluating alternatives indefinitely.
- **Research binge.** Reading, watching, or courseing as a substitute for doing the thing. Often justified as "I need to learn X first."
- **Tool shopping.** Switching editors, note apps, frameworks, hosts, templates.
- **Framework shopping.** Adopting and discarding productivity systems, project structures, methodologies.
- **Perpetual outlining.** Producing structure documents that never become the thing the structure was for.
- **Prerequisite inflation.** Adding upstream "I should know this first" items that push execution further out.
- **Pre-emptive generalization.** Building infrastructure for a project that doesn't yet exist (a CMS before the first post, an abstraction before the second use).
- **Audience theorizing.** Researching who the work is for instead of showing the work to one person.

For each pattern that applies, give a one-sentence example pulled directly from the user's inventory — not a generic illustration.

### Step 3 — Name the specific avoidance

For each identified pattern, ask: what concrete act of execution is being avoided? Write one sentence that starts with "What's being avoided is…" and names the specific artifact the user is not producing. Examples: "the first paragraph of the essay," "pushing the first commit that anyone could read," "sending a draft to a real reader for the first time."

If the avoidance is not clear, say so and offer two plausible candidates rather than inventing certainty.

### Step 4 — Return an execution move

End with one specific next move that is the opposite of the masquerade pattern. This is not a full next-action spec (see `agency_next_action_spec.md` for that); it's the direction.

- If optionality preservation: pick one option now, for this session only, revocable later.
- If research binge: stop research, start drafting using only what is already known, mark unknowns with TK placeholders.
- If tool/framework shopping: use the current tool, even if imperfect, for the next session.
- If perpetual outlining: convert one outline item into prose without touching the rest.
- If prerequisite inflation: identify the true minimum prerequisite (most "prerequisites" aren't).
- If pre-emptive generalization: do the specific instance before the general system.
- If audience theorizing: pick one real human and produce something specifically for them.

---

## Constraints

### Must
- Ground every finding in the user's actual inventory, not hypothetical patterns.
- Distinguish legitimate prep from masquerade using the "ended in an artifact" test.
- Name the specific avoided artifact, not the generic one.
- Return a concrete execution move, not generic advice.

### Must Not
- Moralize, shame, or diagnose character flaws.
- Declare all planning is masquerade — some planning is real prep.
- Assume the user is avoiding something if the inventory shows normal cadence.
- Propose a new productivity system as the solution (that's meta-masquerade).

---

## False-Positive Prevention

1. **Don't mistake slow projects for masquerade.** Some work is slow. The test is not "did it move fast?" but "did the time spent produce artifacts?"
2. **Don't over-classify as masquerade.** If the user spent two hours learning a single concept that unblocks the next commit and they then made the commit, that's prep, not masquerade.
3. **Don't punish legitimate rest.** Hours not worked are not hours avoided. This prompt audits declared work time only.
4. **Don't fabricate avoidance.** If the inventory is ambiguous, say the diagnosis is uncertain and offer two hypotheses.
5. **Don't recommend a new framework.** The answer to framework shopping is not a better framework.

---

## Output Format

```
## Activity breakdown (last [N] days)
- Execution: [% or count] — [what artifacts]
- Prep with ship-pressure: [% or count] — [what it unblocked]
- Planning-masquerade: [% or count] — [what pattern]
- Unrelated: [% or count]

## Masquerade patterns present
1. **[Pattern name]** — [one-sentence example from inventory]
2. **[Pattern name]** — [one-sentence example from inventory]

## What is being avoided
[One sentence starting with "What's being avoided is…" naming the specific artifact.]
[If uncertain: two candidate artifacts, flagged as hypotheses.]

## Execution move
[One concrete move that is the opposite of the identified pattern. Direction, not full spec.]

## Uncertainty
[Anything the inventory did not let this diagnosis determine cleanly.]
```

---

## Verification

- [ ] Every masquerade claim is tied to a specific item from the user's inventory.
- [ ] The "what's being avoided" statement names a concrete artifact, not a vague fear.
- [ ] The execution move is opposite in kind to the masquerade, not more of the same.
- [ ] No moralizing language ("you're procrastinating," "you need discipline").
- [ ] If execution is actually happening at normal cadence, the prompt says so and stops.
