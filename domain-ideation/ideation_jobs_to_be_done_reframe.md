---
title: "Jobs-to-be-Done Reframe — Ideate Against the Job, Not the Solution"
category: ideation/reframing
description: "Take a solution-shaped brainstorm ('ideas for a meal-planning app') and reframe it around the job the user is actually hiring the solution for. Surface 2–3 candidate jobs (functional, emotional, social), then re-ideate against each job. Ideas generated against the real job often look nothing like the original solution-shaped brainstorm — and are frequently better, because they target the outcome rather than the assumed form."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - ideation
  - jobs-to-be-done
  - reframing
  - outcome-driven
  - problem-framing
updated: "2026-05-27"
reasoning:
  styles: [abductive, divergent, reframing]
  stakes: moderate
  horizon: variable
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: variable
  collaboration: solo_or_team
  output_format: structured
  user_role: [pm, founder, designer, marketer, strategist]
  mode: [diverge, reframe]
related_prompts:
  - domain-ideation/ideation_forced_quantity_100_ideas.md
  - domain-ideation/ideation_constraint_flip.md
  - domain-ideation/ideation_persona_what_would_x_do.md
---

# Jobs-to-be-Done Reframe — Ideate Against the Job, Not the Solution

**Objective:** Reframe a solution-shaped brainstorm around the *job* the user is actually hiring it for, then re-ideate against that job. Most ideation starts in solution language — "ideas for a meal-planning app", "features for our dashboard" — which silently assumes the solution form (an app, a dashboard) is correct and only its details are open. That assumption caps the idea space at variations of the assumed form. Jobs-to-be-Done unblocks it: people don't want a meal-planning app, they're hiring something to *stop feeling guilty about feeding their family*, or *save weekday-evening time*, or *feel like a competent parent*. Each candidate job is a different brief, and ideating against the job rather than the assumed solution routinely produces ideas that look nothing like the original — and target the outcome the user actually pays for.

**When to use:**
- The brief is solution-shaped ("ideas for [a specific product/feature]") and you suspect the form is assumed, not validated.
- Ideation keeps producing feature variations of the same artifact.
- Early-stage product or positioning work where the real customer need is still fuzzy.
- A mature product where differentiation requires re-examining *why* people use it at all.

**When NOT to use:**
- The job is already well-understood and validated, and you genuinely need feature-level ideas for a committed form. Use feature ideation (`ideation_scamper.md` or quantity).
- The task is not need-driven (e.g., internal tooling with a fixed mandate where the "job" is simply "do the mandated thing").
- You have no access to, or knowledge of, the actual user — JTBD without any user grounding becomes speculation. (You can still run it as a hypothesis generator, flagged as such.)

**Audience:** PMs, founders, designers, marketers, and strategists whose brainstorm has prematurely committed to a solution form.

---

## Inputs / Context

1. **The current (solution-shaped) brief.** As stated, in its solution language ("ideas for X").
2. **Who the user is.** The person or segment hiring the solution. The more concrete, the better the jobs.
3. **The context of use.** When and where the user reaches for this — the "struggling moment" that triggers the hire.
4. **Current alternatives.** What the user uses today (including non-consumption: doing nothing, a spreadsheet, a friend). Alternatives reveal the real job.
5. **Any evidence.** Interviews, support tickets, reviews, observed behavior. If none, the jobs are hypotheses to validate, flagged as such.

---

## Constraints

### Must
- **Strip the solution language** from the brief and restate it as a struggle: "When [situation], the user wants to [motivation], so they can [desired outcome]."
- Surface **2–3 candidate jobs**, spanning the three job types where they exist: **functional** (the practical task), **emotional** (how the user wants to feel), **social** (how the user wants to be seen).
- For **each candidate job**, re-ideate: generate **5–8 ideas that serve that job**, deliberately *not* assuming the original solution form. At least some ideas per job should not be the original artifact.
- Mark which ideas **could only have come from the job framing** — ideas the original solution-shaped brief would never have surfaced.
- Identify the **most likely real job** (or note that it needs validation) and which jobs are speculative.
- Note where ideas for different jobs **conflict** — serving the emotional job may undercut the functional one; that tension is strategic information.

### Must Not
- Smuggle the original solution back in as the only answer ("the job is X, so… the app should have feature Y"). Let the job genuinely reopen the form.
- State jobs as solutions in disguise ("the job is to use a better app"). A job is an outcome the user wants, independent of any product.
- Generate the same idea set for every job. If three jobs produce identical ideas, the jobs weren't actually distinct.
- Present hypothesized jobs as validated facts when there's no user evidence. Flag the epistemic status.
- Collapse functional, emotional, and social into one. Each is a different hiring reason and yields different ideas.

---

## The three job types

| Type | What it captures | Example (meal-planning) |
|------|------------------|--------------------------|
| **Functional** | The practical task to accomplish | "Decide what to cook this week without re-thinking it daily" |
| **Emotional** | How the user wants to feel (or stop feeling) | "Stop feeling guilty / anxious about feeding my family well" |
| **Social** | How the user wants to be seen by others | "Be seen as a competent, caring parent" |

---

## Instructions

### Step 1 — Restate the brief as a struggle
Strip the solution. Write: "When [situation/trigger], [user] wants to [motivation], so they can [outcome]." This is the struggling-moment frame.

### Step 2 — Surface candidate jobs
From the struggle, the context, and the alternatives, infer 2–3 candidate jobs. Cover functional, emotional, and social where each applies. State each as an outcome, not a product.

### Step 3 — Ground or flag each job
For each job, note the evidence supporting it (interviews, alternatives chosen, behavior) or flag it as a hypothesis needing validation.

### Step 4 — Re-ideate per job
For each candidate job, generate 5–8 ideas that serve *that* job. Forbid yourself, for at least a few ideas per job, from defaulting to the original solution form. Ask: "if this job is the real one, what's the best way to get it done — app or not?"

### Step 5 — Mark job-only ideas
Across the sets, mark the ideas that could only have come from the job framing — the ones invisible from the solution-shaped brief.

### Step 6 — Surface conflicts
Note where serving one job undercuts another. These tensions are strategic: which job the product centers on is a positioning decision.

### Step 7 — Pick the live job(s)
State which job is most likely the real one (or that it needs validation), and which are speculative. The chosen job becomes the reframed brief.

### Step 8 — Hand off
Pass the reframed brief and the per-job idea sets to convergence (`ideation_idea_convergence_dot_voting.md`) or, if the job is unvalidated, to customer discovery before building.

---

## False-Positive Prevention

1. **Solution-in-disguise jobs.** "The job is to have a better app" is the original solution wearing a JTBD hat. A real job is an outcome that exists with or without any product.
2. **Form smuggling.** Concluding every job points back to building the originally-assumed thing means the reframe didn't happen. Force at least some non-original-form ideas per job.
3. **Identical idea sets.** If all three jobs yield the same ideas, the jobs weren't distinct — or you re-ideated lazily. Distinct jobs produce distinct ideas.
4. **Job-type collapse.** Treating only the functional job and ignoring emotional/social misses the reasons people actually switch products. Cover all three where they apply.
5. **Hypothesis-as-fact.** Presenting inferred jobs as validated when there's no user evidence misleads the downstream decision. Flag epistemic status explicitly.
6. **Conflict blindness.** Missing that the emotional job undercuts the functional one hides a real positioning tension. Surface it.
7. **Over-jobbing.** Generating eight candidate jobs dilutes the re-ideation. Cap at 2–3 and go deep.
8. **Outcome vagueness.** "The job is to be happy" is too abstract to ideate against. Jobs should be specific enough that "does this idea serve it?" is answerable.

---

## Output Format

```
# JTBD reframe — [original solution-shaped brief]

## Original brief (solution-shaped)
> "[Ideas for X]"

## Reframed as a struggle
> "When [trigger/situation], [user] wants to [motivation], so they can [outcome]."
- User: [...]
- Context / struggling moment: [...]
- Current alternatives (incl. non-consumption): [...]

## Candidate jobs
| # | Job (as an outcome) | Type | Evidence / status |
|---|---------------------|------|-------------------|
| 1 | [...] | functional | [interview / hypothesis] |
| 2 | [...] | emotional | [...] |
| 3 | [...] | social | [...] |

## Re-ideation per job
### Job 1: [functional job]
1. [idea serving this job] [job-only?]
2. …
(5–8)
### Job 2: [emotional job]
…
### Job 3: [social job]
…

## Job-only ideas
- Ideas invisible from the solution-shaped brief: [#s]

## Job conflicts
- Serving [job A] undercuts [job B] because [...]. Positioning implication: [...]

## Live job(s)
- Most likely real job: [#] — [validated / needs validation]
- Speculative: [#s]
- Reframed brief for downstream: [...]
- Hand off to: ideation_idea_convergence_dot_voting.md (or customer discovery if unvalidated)
```

---

## Verification

- [ ] Original brief restated as a struggling-moment frame, solution stripped.
- [ ] 2–3 candidate jobs surfaced, stated as outcomes not products.
- [ ] Functional, emotional, and social job types covered where applicable.
- [ ] Each job grounded in evidence or flagged as hypothesis.
- [ ] 5–8 ideas per job, including some that abandon the original form.
- [ ] Job-only ideas marked.
- [ ] Job conflicts surfaced as positioning information.
- [ ] Live job identified (validated or needs-validation); reframed brief stated.
