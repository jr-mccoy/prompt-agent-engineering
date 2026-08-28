---
title: "Score a PRD Against a Rigorous Rubric"
category: professional-communication/product
description: "Evaluate an existing Product Requirements Document against a weighted rubric (clarity, problem framing, scope discipline, testability, risk surfacing, alignment), return per-dimension scores with evidence citations, and produce a prioritized revision list."
techniques:
  - ST-02
  - RT-02
  - CM-02
  - DS-01
  - QA-01
difficulty: intermediate
tags:
  - product-management
  - prd
  - review
  - rubric
  - quality-gate
updated: "2026-04-23"
related_prompts:
  - domain-product-management/prompts/product_create_prd.md
  - domain-product-management/prompts/product_delivery_sprint_planner.md
  - domain-prompt-engineering/evaluation/correctness_prompt_specification_audit.md
---

# Score a PRD Against a Rigorous Rubric

**Objective:** Given a draft PRD, return a rubric-scored evaluation across six quality dimensions with evidence quotes pulled from the document itself, a pass/revise/reject verdict, and a prioritized revision list ordered by leverage on the final decision to ship.

**When to use:**
- A PRD has been submitted for review and you need to respond with something more structured than "looks good."
- You are the decision-maker, and you want to force the PRD author to address the weakest dimensions before engineering sizing begins.
- A PRD passed review, the feature shipped, and it underperformed — you want to learn where the document failed to catch the miss (retrospective evaluation).

**Audience:** Product reviewers, engineering leads acting as technical reviewers, or PMs self-auditing their own draft before circulating. Assumes the reader can change the PRD in response (not useful for a locked PRD you cannot revise).

---

## Inputs / Context

1. **The PRD under review.** Full text, pasted or linked.
2. **Review intent.** One of: `pre-sizing review` (revise before engineering sees it), `shipment gate` (revise before committing to build), or `retrospective` (learn from a past PRD after the feature shipped).
3. **Threshold for "pass."** Default: a PRD must score ≥ 4/5 on **every** dimension and ≥ 27/30 overall. Override if the reviewer specifies a different bar.
4. **Optional context the reviewer has that the PRD doesn't state:** the decision-maker's known objections, competitor moves, prior failed attempts.

If the PRD is not a PRD (it's a project plan, a design doc, a slide deck), say so and refuse. Suggest the right document type and stop.

---

## Rubric — Six Dimensions (5 points each, 30 total)

### D1. Problem Clarity (0–5)
Does the PRD name a specific user segment, what they do today, and why now?

- **5** — Specific segment, current behavior described, timing justified.
- **3** — Segment named but current behavior is vague or timing unjustified.
- **1** — "Users want this" with no segment or baseline behavior.
- **0** — No problem statement; jumps to solution.

### D2. Hypothesis Testability (0–5)
Can a reader restate the hypothesis as "If X, then Y measured by Z within T"?

- **5** — Hypothesis is explicit, measurable, and time-bound.
- **3** — Partially testable (e.g., measurable but no timeframe, or timeframe but no threshold).
- **1** — Qualitative wish ("users will love it").
- **0** — No hypothesis at all.

### D3. Scope Discipline (0–5)
Does the MVP list contain the minimum viable set? Is there an explicit out-of-scope section?

- **5** — MVP is ≤ 5 items, each needed for the hypothesis test. Out-of-scope section lists rejected items with reasons.
- **3** — MVP is reasonable but out-of-scope is missing or thin.
- **1** — MVP is a feature wish list; everything is "must have."
- **0** — No scope section, or scope changes implicitly across the document.

### D4. Requirement Testability (0–5)
Is every requirement phrased so an engineer could write an acceptance test against it?

- **5** — Every requirement has a measurable condition or observable behavior.
- **3** — Most are testable; a minority ("fast," "intuitive," "robust") are subjective.
- **1** — More than half are subjective adjectives.
- **0** — Requirements are solution names, not behaviors.

### D5. Risk & Assumption Surfacing (0–5)
Are assumptions labeled with risk-if-wrong? Are "we won't ship this if" conditions real and concrete?

- **5** — Assumptions enumerated with risk notes; kill-conditions are specific.
- **3** — Assumptions listed but risk consequences are missing; or kill-conditions are vague.
- **1** — Assumptions embedded in prose; no kill conditions.
- **0** — No assumptions, no kill conditions, all-positive framing.

### D6. Decision & Alignment (0–5)
Is it clear who the decision-maker is, who must sign off, and whether they have?

- **5** — Single decision-maker named; every required stakeholder listed with confirmed/unconfirmed status.
- **3** — Decision-maker named; stakeholder list incomplete or status unclear.
- **1** — Multiple possible decision-makers; no stakeholder status.
- **0** — No ownership.

---

## Constraints

### Must
- Cite evidence for every score: a verbatim quote from the PRD (or "not present in document") — no paraphrasing without the source.
- Score every dimension even if a dimension is "not present" (that's a 0, not a skip).
- Compute the total and compare against the threshold.
- Produce a revision list ordered by leverage: the revision that moves the verdict from revise → pass goes first.
- State the verdict plainly: **Pass**, **Revise**, or **Reject**.

### Must Not
- Grade on effort. A PRD that is long and earnest but scores 1 on Problem Clarity is still a 1.
- Invent content. If a dimension is absent, score 0 and say so; do not give the author credit for what they meant.
- Soften the verdict in the summary. If the score says Revise, the summary says Revise.
- Rewrite the PRD inline. This prompt evaluates; rewriting is a separate job.
- Add rubric dimensions. Stick to the six.

---

## Instructions

### Step 1 — Parse the PRD into rubric-relevant sections
Pull the Problem, Hypothesis, MVP scope, Out-of-scope, Requirements, Assumptions, Kill conditions, Stakeholders sections out of the source document. If a section is missing, mark it missing.

### Step 2 — Score each dimension independently
For each of D1–D6, pick a score using the band definitions. Cite at least one evidence quote per dimension (or "not present").

### Step 3 — Compute total and verdict
- **Pass:** every dimension ≥ 4 and total ≥ 27 (or reviewer's override).
- **Revise:** one or more dimensions at 3; otherwise meets total threshold.
- **Reject:** any dimension at 0–1, **or** total < 20.

### Step 4 — Build the revision list
For every score below 4, write a revision the author can perform. Order by leverage: which revision, if done, moves the verdict up a tier? Cap the list at 5 to avoid the "fix everything" trap.

### Step 5 — Write the reviewer note
One paragraph to the PRD author. Plain. Names the verdict. Names the top three revisions. Does not pile on.

---

## False-Positive Prevention

1. **Don't reward length.** A 10-page PRD can score 12/30 if it is 10 pages of solution with no problem statement.
2. **Don't let a good hypothesis rescue a missing scope section.** Each dimension is independent.
3. **Don't give partial credit for good intent.** If the author "meant to" name the user segment but wrote "users," that is a 1, not a 3.
4. **Don't invent evidence.** "The PRD probably implies X" is not a citation. Either quote it or score it as not present.
5. **Don't soften a Reject verdict because the author is junior or senior.** The rubric applies to the document, not the author.
6. **Don't over-weight the sections the reviewer personally cares about.** All six dimensions carry equal weight unless the reviewer explicitly reweights them up front.

---

## Output Format

```
# PRD evaluation — [feature name]

**Reviewer:** [name]
**Date:** [date]
**Review intent:** pre-sizing / shipment gate / retrospective
**Pass threshold:** [default 4/5 per dim, 27/30 total — or override]

## Scores

| Dim | Dimension                      | Score | Evidence quote (or "not present") |
|-----|--------------------------------|-------|-----------------------------------|
| D1  | Problem clarity                |  X/5  | "[quote]"                         |
| D2  | Hypothesis testability         |  X/5  | "[quote]"                         |
| D3  | Scope discipline               |  X/5  | "[quote]"                         |
| D4  | Requirement testability        |  X/5  | "[quote]"                         |
| D5  | Risk & assumption surfacing    |  X/5  | "[quote]"                         |
| D6  | Decision & alignment           |  X/5  | "[quote]"                         |
|     | **Total**                      | XX/30 |                                   |

## Verdict: Pass / Revise / Reject

## Revisions (ordered by leverage, max 5)
1. [Concrete revision.] — moves D[n] from X to Y.
2. ...

## Reviewer note to the author
[One short paragraph: verdict, top three revisions, tone neutral.]
```

---

## Verification

- [ ] Every dimension has a score and either a verbatim quote or "not present."
- [ ] Total is computed, not paraphrased.
- [ ] Verdict matches the threshold logic (no soft overrides).
- [ ] Revision list is ordered by leverage, capped at 5.
- [ ] Reviewer note names the verdict in the first sentence.
- [ ] No rewrite of the PRD is included — only revisions the author must make.
