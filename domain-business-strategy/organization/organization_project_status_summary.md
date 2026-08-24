---
title: "Project Status Summary"
category: business-strategy/organization
description: "Pull scattered project documentation into a single, audience-appropriate status snapshot — status with reasoning, progress, blockers, milestones, and decisions needed — based only on what's documented, with staleness clearly flagged."
techniques:
  - ST-01
  - RT-02
  - DS-02
  - DS-06
  - QA-01
difficulty: beginner
tags:
  - organization
  - project-status
  - stakeholder-communication
  - reporting
  - synthesis
updated: "2026-06-07"
related_prompts:
  - domain-business-strategy/organization/organization_content_audit.md
  - domain-business-strategy/organization/organization_knowledge_base_gap_analysis.md
  - domain-business-strategy/research/research_company_deep_dive.md
---

# Project Status Summary

**Objective:** Synthesize scattered project documentation into a single status snapshot for a specific audience — covering status with reasoning, recent progress, current focus, blockers/risks, upcoming milestones, and decisions needed — based strictly on what is documented, with stale information clearly flagged.

**When to use:**
- Recurring status updates (weekly/biweekly) drawn from project docs.
- Leadership or stakeholder briefings that need a consolidated snapshot.
- Project reviews where information is spread across many pages/tools.
- Catching up on a project's state from its documentation trail.

**When NOT to use:**
- Documentation is absent or wildly stale — the summary would be fiction; flag the gap instead.
- You need live metrics/dashboards — pull those directly rather than infer from notes.
- The audience needs a decision recommendation, not a status report.

**Audience:** Project managers, team leads, and anyone reporting status to a team, leadership, or external stakeholders.

---

## Inputs / Context

The user should supply (or the summary should flag what is missing):

1. **Project name** and the **audience** (team, leadership, external stakeholders) — tone and detail follow the audience.
2. **Sources to review:** the folders/databases/pages holding project documentation.
3. **Timeframe** for "recent progress" (e.g., past 2 weeks, this sprint).
4. **Known constraints** if any (target date, budget) — but only report them if documented.
5. **Purpose:** routine update, escalation, decision-forcing briefing.

---

## Constraints

### Must
- Base every claim **only on documented content**; do not assume positive progress.
- Clearly **distinguish documented fact from inference**, and say "Status unclear — documentation indicates [X]" when the docs don't settle it.
- Give an overall **status with a one-sentence reason** and a **confidence level** on hitting any dated target.
- **Surface risks and blockers prominently** — never minimize them — and for each note what would resolve it.
- Link to source pages for each major claim, include the last-updated date per source, and mark claims from 30+ day-old docs with `[STALE]`.
- **Prioritize** an "Attention Required" section with clear action items for the audience.

### Must Not
- Invent progress, dates, budget figures, or decisions not present in the documentation.
- Smooth over or omit blockers to make the project look healthier.
- Present inference as documented fact.
- Bury the decisions/attention items the reader actually needs to act on.

---

## Instructions

1. **Confirm sources and recency.** List the pages reviewed and their last-updated dates; note if key documentation appears missing.
2. **Determine status.** Choose On Track / At Risk / Blocked / Completed with a one-sentence reason grounded in the docs; state confidence on any target date.
3. **Summarize recent progress.** Completed milestones, key decisions, and changes from the original plan within the timeframe.
4. **State current focus.** Active work, immediate next steps, target dates.
5. **Surface blockers and risks.** Active blockers, timeline risks, dependencies; for each, what would resolve it. Do not downplay.
6. **List upcoming milestones and decisions needed.** Next 3–5 milestones with dates; open questions requiring stakeholder decisions and by when.
7. **Write "Attention Required."** Specific items needing the audience's action, with suggested next steps.
8. **Self-check (verification step).** Re-read: is any claim unsupported by a cited doc? Are stale sources marked `[STALE]`? Are blockers prominent, not buried? Note the date range of sources used.

---

## False-Positive Prevention

❌ **DON'T:**
- Assume the project is "on track" when the docs don't say so.
- Invent a completion date, budget number, or decision not in the documentation.
- Soften or omit a blocker to make the status look better.
- Treat a 6-month-old note as current without flagging it.
- Bury the decision the stakeholder needs to make at the bottom of a wall of text.

✅ **DO:**
- Ground every claim in a cited, dated source; say "Status unclear" when docs conflict or are silent.
- Mark anything from 30+ day-old docs with `[STALE]` and call out missing documentation.
- Surface blockers and risks prominently with resolution paths.
- State a status with explicit reasoning and a confidence level on dates.
- Lead the reader to the actions and decisions they own.

---

## Output Format

```
# Status Summary: [Project Name] — for [Audience]

## Status at a Glance
- Overall status: [ON TRACK / AT RISK / BLOCKED / COMPLETED]
- Why: [one sentence, grounded in docs]
- Target completion: [date or "Not specified"]   | Confidence: [High/Medium/Low]

## Recent Progress (past [timeframe])
- [Completed milestone / decision / plan change] — [source, date]

## Current Focus
- [Active work + next steps + target dates]

## Blockers & Risks
- [Blocker/risk] — impact; what would resolve it — [source]

## Upcoming Milestones
- [Milestone] — [target date] — [what it requires]

## Decisions Needed
- [Open question] — recommendation if docs suggest one — needed by [date]

## Attention Required (for [Audience])
- [Specific item] → suggested action

## Sources
- Based on [X] pages last updated between [date] and [date].
- [Page] — last updated [date] [STALE if 30+ days]
- Missing/expected docs: [...]
```

---

## Example Output

```
# Status Summary: Mobile App Relaunch — for Leadership (placeholder)

## Status at a Glance
- Overall status: AT RISK
- Why: Two of three release blockers remain open with no owner assigned, per the sprint board.
- Target completion: 2026-07-15   | Confidence: Low

## Recent Progress (past 2 weeks)
- Completed: new onboarding flow merged ([sprint board](#), 2026-06-03).
- Decision: dropped the offline-mode feature from this release to protect the date ([decision log](#), 2026-05-29).

## Current Focus
- Stabilizing the payments module; QA pass scheduled for next week (target 2026-06-14).

## Blockers & Risks
- BLOCKER: Payments integration failing in staging — no owner assigned. Would resolve: assign a backend owner + vendor support ticket ([bug tracker](#)).
- RISK: QA capacity is one engineer for two modules; timeline slips if a P0 surfaces ([capacity note](#), 2026-05-20) [STALE].
- DEPENDENCY: App-store review lead time (~5 days) not yet budgeted into the date.

## Upcoming Milestones
- Payments fix verified — 2026-06-14 — requires assigned owner.
- Release candidate build — 2026-06-28 — requires all blockers closed.
- Store submission — 2026-07-05 — requires RC sign-off.

## Decisions Needed
- Assign a backend owner to the payments blocker — needed this week or the date is at serious risk.
- Confirm whether to hold the date or scope-cut further — needed by 2026-06-14.

## Attention Required (for Leadership)
- Resolve the unowned payments blocker (staffing decision) → assign an owner now.
- Approve the contingency: hold date vs. cut scope.

## Sources
- Based on 6 pages last updated between 2026-05-20 and 2026-06-03.
- Capacity note — last updated 2026-05-20 [STALE].
- Missing/expected docs: no current budget/cost page found.
```

---

## Verification

- [ ] Every claim ties to a cited, dated source.
- [ ] Status includes a one-sentence reason and a confidence level on dates.
- [ ] Blockers and risks are prominent, each with a resolution path.
- [ ] Claims from 30+ day-old docs marked `[STALE]`; missing docs flagged.
- [ ] Inference distinguished from documented fact ("Status unclear" used where apt).
- [ ] Decisions-needed and attention items are specific and actionable.
- [ ] No invented progress, dates, budget, or decisions.
- [ ] Source date range stated at the end.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the task as a documented-evidence-only, audience-targeted status snapshot.
- **RT-02 (Multi-Dimensional Analysis Framework):** Covers status, progress, focus, blockers, milestones, and decisions as distinct dimensions.
- **DS-02 (Evidence-Based Decision Making):** Requires every claim to cite a dated source and flags stale information.
- **DS-06 (Prioritization and Severity Guidance):** Surfaces blockers prominently and prioritizes attention/decision items.
- **QA-01 (Self-Critique Triggers):** Final self-check guards against unsupported claims and buried risks.

---

## Related Prompts

- `domain-business-strategy/organization/organization_content_audit.md` — Clean up the documentation the summary draws from.
- `domain-business-strategy/organization/organization_knowledge_base_gap_analysis.md` — Find documentation gaps that weaken status reporting.
- `domain-business-strategy/research/research_company_deep_dive.md` — Build an external-facing synthesis with source discipline.
