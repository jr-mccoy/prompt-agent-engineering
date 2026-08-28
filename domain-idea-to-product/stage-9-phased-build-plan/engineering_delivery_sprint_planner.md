---
title: "Delivery Sprint Planner"
category: engineering-workflows/workflows
description: "Slice a signed project into one-week sprints with goals, owners, deliverables, acceptance criteria, review checkpoints, and risk mitigations — plus a burndown-friendly task table, contingency allocation, and communication cadences."
techniques:
  - ST-01
  - ST-02
  - DS-06
  - CM-01
  - QA-01
difficulty: intermediate
tags:
  - sprint-planning
  - delivery
  - capacity-planning
  - risk-mitigation
  - project-management
updated: "2026-06-07"
related_prompts:
  - domain-personal-development/prompts/goals/goals_goal_system_designer.md
  - domain-personal-development/prompts/stakeholder/stakeholder_navigation_guide.md
  - domain-engineering-workflows/workflows/engineering_data_schema_draft.md
---

# Delivery Sprint Planner

**Objective:** Break a signed project into one-week sprints — each with goals, key tasks, owners, deliverables, acceptance criteria, a review checkpoint, and a risk-plus-mitigation — and wrap it in a burndown-friendly task table, an explicit contingency allocation, and internal + client communication cadences.

**When to use:**
- Turning a signed proposal or scope into an executable weekly plan.
- Planning a fixed-duration consulting or delivery engagement.
- When acceptance criteria and client review checkpoints must be explicit.

**When NOT to use:**
- Open-ended backlog grooming with no fixed end date.
- Personal/quarterly goal systems — use `domain-personal-development/prompts/goals/goals_goal_system_designer.md`.
- Navigating multi-party political decisions — use `domain-personal-development/prompts/stakeholder/stakeholder_navigation_guide.md`.

**Audience:** Delivery managers, tech leads, and consultants planning a time-boxed project.

---

## Inputs / Context

The user supplies (wrap the scope text in a `<scope>` tag):
1. **High-level scope** — workstreams copied from the proposal.
2. **Project duration** — number of weeks.
3. **Your weekly capacity** — hours you can commit per week.
4. **Client weekly availability** — hours for reviews/inputs.
5. **Hard deadlines/events** — demos, board meetings (or "none").

If capacity is clearly insufficient for the scope, say so and propose a cut or extension rather than producing an unrealistic plan.

---

## Constraints

### Must
- Slice scope into 1-week sprints, each with goals (≤15 words), key tasks, owner (Me/Client/AI), deliverables, **acceptance criteria** (clear definition of done), a review checkpoint (date + audience), and one risk + mitigation.
- Allocate ~10% contingency hours and show where they sit.
- Produce a burndown-friendly task table (Task ▸ Est. hrs ▸ Owner ▸ Sprint) whose per-sprint sum stays within weekly capacity.
- Include internal and client-facing communication cadences.

### Must Not
- Plan more hours into a sprint than the stated weekly capacity allows.
- Leave acceptance criteria vague ("looks good") — make them verifiable.
- Ignore hard deadlines when sequencing sprints.
- Invent scope, hours, or deadlines the user didn't provide.

---

## Instructions

1. **Slice the scope into sprints.** For each sprint, fill goals, key tasks, owner, deliverables, acceptance criteria, review checkpoint, and the single biggest risk + a one-line mitigation.
2. **Allocate contingency.** Reserve ~10% of hours and show which sprints hold the buffer.
3. **Build the burndown task table.** List tasks with estimated hours, owner, and sprint; confirm each sprint's total ≤ weekly capacity.
4. **Define communication cadences.** Internal (stand-up style, daily/async) and client-facing (weekly demo + channel etiquette).
5. **Self-check before reporting.** Rate schedule realism and risk coverage (1–10 each); if either <9, rebalance tasks or add mitigation before finalizing. Confirm capacity is respected and deadlines honored.

---

## False-Positive Prevention

❌ **DON'T:**
- Don't overload a sprint past the stated weekly capacity — surface the shortfall instead.
- Don't write acceptance criteria that can't be objectively checked.
- Don't bury risk; name the single biggest risk per sprint with a concrete mitigation.
- Don't fabricate scope items, hour estimates, or deadlines.

✅ **DO:**
- Keep per-sprint hours within capacity (including contingency).
- Make every "done" definition verifiable.
- Tie review checkpoints to real dates and audiences.
- Flag scope/capacity mismatches and propose cuts.

---

## Output Format

```markdown
## A. Sprint Schedule
### Sprint N (dates)
- Goals: [...]
- Key tasks: [...]
- Owner: Me / Client / AI
- Deliverables: [...]
- Acceptance criteria: [...]
- Review checkpoint: [date · audience]
- Risk → Mitigation: [...]

## B. Contingency Allocation
- [~10% hours, placement]

## C. Burndown Task Table
| Task | Est. hrs | Owner | Sprint |
|------|----------|-------|--------|

## D. Communication Cadence
- Internal: [...]
- Client-facing: [...]
```

## Example Output

```markdown
## A. Sprint Schedule
### Sprint 1 (Wk 1)
- Goals: Stand up data pipeline + ingest first source
- Key tasks: schema draft, ingestion job, smoke test
- Owner: Me (build), Client (sample data)
- Deliverables: working ingestion of source A
- Acceptance criteria: 1k records loaded; row counts reconcile to source
- Review checkpoint: Fri · client data lead
- Risk → Mitigation: sample data late → request by Wk1 Day 1; stub with synthetic rows

## B. Contingency Allocation
- 4 of 40 hrs reserved, weighted to Sprint 1 (integration unknowns).

## C. Burndown Task Table
| Task | Est. hrs | Owner | Sprint |
|------|----------|-------|--------|
| Schema draft | 6 | Me | 1 |
| Ingestion job | 14 | Me | 1 |
| Smoke test | 4 | Me | 1 |
| Sample data hand-off | 2 | Client | 1 |
(Sprint 1 total: 26 hrs ≤ 30 hr capacity, +4 contingency)

## D. Communication Cadence
- Internal: async daily standup in thread; blockers flagged same-day.
- Client-facing: Fri 30-min demo; questions in shared Slack, 1-business-day SLA.
```

---

## Verification

- [ ] Every sprint has goals, tasks, owner, deliverables, acceptance criteria, checkpoint, and risk+mitigation.
- [ ] Acceptance criteria are objectively verifiable.
- [ ] ~10% contingency allocated and located.
- [ ] Burndown table per-sprint totals ≤ weekly capacity.
- [ ] Hard deadlines honored in sequencing.
- [ ] Internal and client cadences defined.
- [ ] Realism and risk-coverage self-rated ≥9; no fabricated scope/hours/deadlines.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the slice-into-weekly-sprints delivery goal.
- **ST-02 (Structured Sequential Instructions):** Slice → contingency → task table → cadence → self-rate.
- **DS-06 (Prioritization and Severity Guidance):** Per-sprint risk identification and contingency placement.
- **CM-01 (Explicit Context Framing):** Capacity, deadlines, and owner roles frame every sprint.
- **QA-01 (Self-Verification):** Realism/risk self-rating gate forces rebalancing before output.

---

## Related Prompts

- `domain-personal-development/prompts/goals/goals_goal_system_designer.md` — Convert sprint goals into a tracked goal system.
- `domain-personal-development/prompts/stakeholder/stakeholder_navigation_guide.md` — Manage client/stakeholder dynamics around the plan.
- `domain-engineering-workflows/workflows/engineering_data_schema_draft.md` — Produce the technical artifacts a sprint delivers.
