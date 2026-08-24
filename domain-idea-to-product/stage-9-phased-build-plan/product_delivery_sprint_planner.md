---
title: "Product Delivery Sprint Planner"
category: professional-communication/product
description: "Plan a cross-functional product delivery sprint from an approved PRD: decompose into user stories with acceptance criteria, map dependencies, assign owners, surface risks, and produce a daily-standup-ready backlog with an explicit definition of done."
techniques:
  - ST-02
  - DS-02
  - CM-02
  - RT-02
  - QA-01
difficulty: intermediate
tags:
  - product-management
  - sprint-planning
  - user-stories
  - delivery
  - dependencies
  - acceptance-criteria
updated: "2026-04-23"
related_prompts:
  - domain-professional-communication/prompts/product_create_prd.md
  - domain-professional-communication/prompts/product_rigorous_prd_evaluation_and_scoring.md
  - domain-engineering-workflows/workflows/engineering_delivery_sprint_planner.md
---

# Product Delivery Sprint Planner

**Objective:** Given an approved PRD and a committed team, produce a sprint plan that decomposes the PRD into user stories with testable acceptance criteria, maps cross-functional dependencies, assigns an accountable owner per story, surfaces the top risks, and commits to a definition of done for the sprint as a whole.

**When to use:**
- A PRD has been approved and engineering sizing is complete; you are entering the sprint that will deliver the MVP (or a coherent slice of it).
- You are planning a 1- to 3-week delivery cycle that spans more than one function (e.g., backend + frontend + design + QA).
- A previous sprint slipped and you want a cleaner plan that is explicit about dependencies and ownership.

**Do not use** to replan every sprint in a quarter — this is a per-sprint artifact. For quarterly planning, use a roadmap prompt instead.

**Audience:** Product managers or delivery leads running the planning meeting. The plan is consumed by the whole cross-functional team (engineering, design, QA, data, comms as applicable).

---

## Inputs / Context

1. **Approved PRD.** Link or paste. Must have MVP scope frozen (see `product_create_prd.md`).
2. **Team composition.** Names, roles, and approximate capacity for the sprint (e.g., "Priya — backend, 8 days; Marco — design, 3 days").
3. **Sprint length.** Days. Default 10 working days.
4. **Start and end dates.**
5. **Known external dependencies.** Other teams, vendors, data sources, security review, legal, app-store review.
6. **Sprint goal.** One sentence describing what success looks like at the end of the sprint. If the answer is "finish everything in the PRD," ask whether that is realistic given capacity.
7. **Blockers from the prior sprint (if any).** Carry-over work, unresolved decisions, broken dependencies.

If the PRD's MVP scope is not frozen or the sprint goal is not a single sentence, **stop** and ask. Planning floats when scope floats.

---

## Constraints

### Must
- Every user story is phrased as: **As [user], I can [action] so that [outcome]** — with at least two acceptance criteria in Gherkin-style (`Given / When / Then`) or equivalent testable form.
- Every story has exactly one accountable owner. Collaborators are listed, but accountability is single-pointed.
- Dependencies are mapped explicitly: which story blocks which, and which external teams must deliver something for the sprint to succeed.
- The definition of done is set at the sprint level (not the story level) and includes: code merged, tests passing, acceptance criteria verified, production-readiness checklist passed, documentation updated.
- The plan fits capacity. The sum of story estimates ≤ 80% of team capacity (reserve 20% for the interrupts that always happen).
- Risks are ranked by probability × impact. Top three risks have a named mitigation and owner.
- A scope-cut ladder is attached: if the sprint slips, which stories get dropped in what order. This must be agreed up front, not negotiated mid-sprint.

### Must Not
- Expand scope beyond the MVP that the PRD locked. New discoveries go to backlog, not to the sprint.
- Assign stories to "the team" without a named owner.
- Treat estimates as commitments. They are estimates; the commitment is to the sprint goal.
- Schedule external dependencies as "due during the sprint" without confirming with the external team.
- Use story points unless the team already uses them. Days or half-days are fine and more legible across functions.
- Write acceptance criteria that are restatements of the story ("the feature works").

---

## Instructions

### Step 1 — Restate the sprint goal
One sentence, beginning "By [end date], the team will have shipped [X] so that [user outcome is achievable]." If the goal can't fit in one sentence, it's two sprints.

### Step 2 — Decompose the PRD into stories
Split the MVP scope into stories. Each story is independently demoable (not necessarily shippable — but a reviewer can see that *this* capability now exists). Target: 5–12 stories per two-week sprint. More than that is too granular; fewer means the stories are too big.

### Step 3 — Attach acceptance criteria
For each story, write 2–5 criteria in testable form. A criterion that cannot be verified by looking at the product or running a test does not belong here.

### Step 4 — Assign owner and estimate
Name exactly one owner per story. Estimate in days or half-days. Note collaborators.

### Step 5 — Map dependencies
Draw the dependency graph in plain text (or a table). For each external dependency, name the team, the deliverable, the confirmed date, and the contingency if it slips.

### Step 6 — Capacity check
Sum story estimates by owner. If any owner exceeds 80% of their sprint capacity, flag and rebalance. Reserve 20% buffer per owner.

### Step 7 — Risk register
Top 3–5 risks. For each: probability (low/med/high), impact (low/med/high), trigger condition, mitigation, mitigation owner.

### Step 8 — Scope-cut ladder
Order the stories from "must-ship to hit the sprint goal" to "first to drop if we slip." Get team verbal agreement on the ladder before the sprint starts.

### Step 9 — Definition of done
Write the DoD at the sprint level. It applies to the whole increment, not per story (per-story completion is acceptance criteria).

---

## False-Positive Prevention

1. **Don't label everything "must-have."** If every story is must-have, the scope-cut ladder doesn't exist and the sprint will slip silently.
2. **Don't turn the sprint into a mini-PRD re-litigation.** Scope disputes surfaced in planning belong back in the PRD, not in the sprint plan.
3. **Don't hide dependency risk in the risks list.** External dependencies are a dependency-mapping problem; if you can't confirm the dependency, remove it from this sprint's critical path.
4. **Don't plan for 100% capacity.** Reviewers, production incidents, and illness will fill the last 20% whether you planned for them or not.
5. **Don't write acceptance criteria that are solution descriptions.** "Button is blue" is a design note; "When a user clicks Save, the record persists and the confirmation toast appears" is a criterion.
6. **Don't skip the definition of done** because "we all know what done means." Retrospectives show we don't.
7. **Don't assign a story to a function ("backend").** A human owns the story. If no human is available, the story doesn't belong in this sprint.

---

## Output Format

```
# Sprint plan — [sprint name / number]

**Sprint goal (one sentence):**
By [end date], the team will have shipped [X] so that [user outcome].

**Dates:** [start] → [end] ([N] working days)
**Team capacity (days):** [Name: days per role]
**Buffer reserved:** 20% per owner

## Stories
| # | Story (As / I can / so that) | Owner | Est (d) | Collaborators | Acceptance criteria |
|---|------------------------------|-------|---------|---------------|---------------------|
| 1 | As [user], I can [X] so that [Y] | [name] | 2 | [names] | Given [context], When [action], Then [observable result]; … |
| 2 | …                            |       |         |               |                     |

## Dependency map
- Story 3 blocks stories 4, 7.
- Story 2 depends on [external team] delivering [thing] by [date]; confirmed by [person] on [date]. Contingency if it slips: [plan].

## Capacity check
| Owner   | Sum of estimates | Capacity | Utilization | OK? |
|---------|------------------|----------|-------------|-----|
| [name]  | 6d               | 8d       | 75%         | ✅  |

## Risks (top 3–5)
| Risk | Prob | Impact | Trigger | Mitigation | Owner |
|------|------|--------|---------|------------|-------|

## Scope-cut ladder (drop order if we slip)
1. Story [#]  — reason: [least critical to sprint goal]
2. …

## Definition of done (sprint-level)
- [ ] All in-scope stories meet their acceptance criteria
- [ ] Tests passing on main
- [ ] Production-readiness checklist passed
- [ ] Documentation updated
- [ ] Demo rehearsed

## Open items before the sprint starts
- [ ] [Thing the PM/EM still needs to confirm]
```

---

## Verification

- [ ] Sprint goal fits in one sentence.
- [ ] Every story names exactly one accountable owner.
- [ ] Every story has ≥ 2 testable acceptance criteria.
- [ ] Dependency map is explicit and every external dependency has a confirmed date + contingency.
- [ ] No owner exceeds 80% capacity.
- [ ] Risks list has probability, impact, trigger, mitigation, and owner.
- [ ] Scope-cut ladder exists and is ordered.
- [ ] Definition of done is at the sprint level and is verifiable, not aspirational.
- [ ] No new scope has crept in beyond the frozen PRD MVP.
