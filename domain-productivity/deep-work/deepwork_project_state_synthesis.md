---
title: "Synthesize Project State From Multiple Sources for Reload"
category: productivity/deep-work
description: "Pull scattered project state across calendar, messages, drafts, notes, and ticket systems into a single reload brief answering: where is this project actually, what moved since I last looked, what's waiting on me, what's waiting on others — for a specific project, not in general."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - OC-01
  - QA-01
difficulty: intermediate
tags:
  - deep-work
  - reload
  - project-state
  - synthesis
updated: "2026-04-20"
related_prompts:
  - domain-productivity/deep-work/deepwork_block_end_context_capture.md
  - domain-productivity/deep-work/deepwork_reload_ritual_design.md
  - domain-business-strategy/organization/organization_project_status_summary.md
---

# Synthesize Project State From Multiple Sources for Reload

**Objective:** For one specific project the user has been away from for days or weeks, produce a reload brief that pulls together scattered state and answers four questions: where is it now, what has changed, what's waiting on me, what's waiting on others. Based on supplied inputs only — do not invent state.

**When to use:** When returning to a project after a break. When a project has gone quiet and the user doesn't know whether they dropped something. Before a meeting about a project the user hasn't touched recently.

**Audience:** The individual project owner reloading their own head, not a status report to a stakeholder.

---

## Inputs Required

1. **Project name and one-sentence objective.**
2. **Their own latest reload packet or notes for this project**, if any.
3. **Relevant messages since last touch** — thread titles or message excerpts, not everything. Focus on anything that contained a request, decision, or change.
4. **Calendar entries that mentioned this project.** Past and upcoming.
5. **Current state of the primary artifact** (doc, code, design, sheet) — what it says today, not the full content.
6. **Open threads with other people** — who owes the user what, who the user owes what, with the last date of contact.
7. **The date range this synthesis covers.** "Since [date] to today."

If any category is empty, state "none supplied" — do not infer a gap is empty.

---

## Instructions

1. **Sort every input into exactly one of four buckets:**
   - **Where it is now** (current state facts)
   - **What moved** (changes during the date range)
   - **Waiting on user** (actions the user owes)
   - **Waiting on others** (actions someone else owes)

   An item that doesn't fit goes into a fifth bucket: "unclear, needs check." Do not force-fit.

2. **Within each bucket, deduplicate.** If a decision appears in both a Slack thread and a doc comment, count it once with both sources cited.

3. **Flag stale items.** In "waiting on others," anything past the user's normal follow-up threshold (they specify, default 7 days) is stale — call it out with a suggested nudge date.

4. **Identify the single "loadbearing unknown."** The one question whose answer most changes what the user does next. It may be a waiting-on-others item, a contradiction between sources, or a decision the user has been deferring.

5. **Produce the physical next action.** Exactly one. Startable in < 5 minutes. Not "review status" — something like "reply to Kara's Tuesday message with a yes/no on the metric change."

6. **Name at most two risks visible in the synthesis.** Things like "decision made in thread but never written down" or "two people gave contradictory input." If none, say so.

---

## Output Format

```
# [Project] Reload Brief
Date range: [start] → [today]

## Where It Is Now
- [fact with source]
- ...

## What Moved
- [change with date and source]
- ...

## Waiting on Me
- [item, age, where it was raised]
- ...

## Waiting on Others
- [item, person, age, stale flag if any, suggested nudge date]
- ...

## Unclear — Needs Check
- [item and which source made it unclear]

## Loadbearing Unknown
[The one question that most changes next actions.]

## Next Action
[Physical, < 5 min to start.]

## Risks Surfaced (≤ 2)
- [risk and its source]
```

---

## Constraints

**Must:**
- Draw every bucket item from a supplied source. Cite it.
- Name exactly one loadbearing unknown and one next action.
- Flag stale waiting-on-others items using the user's threshold.
- Keep the brief under one printed page.

**Must not:**
- Invent project state that wasn't supplied (no "usually projects at this stage ..." language).
- Produce a full status report for stakeholders — this is a personal reload brief.
- Speculate about other people's intent when sources are ambiguous. Mark ambiguous items "unclear."
- Recommend organizational changes, tool adoption, or process fixes.

---

## False-Positive Prevention

- **Gap-filling hallucination:** If input 3 is sparse, the synthesis will be sparse. Do not inflate. State "none supplied" where appropriate.
- **Single-source decisions:** A decision visible only in messages, not in the artifact, is suspect. Surface as risk, not as fact.
- **Stakeholder leak:** The brief is for the user alone. If tone becomes polished ("the team agreed..."), rewrite in first-person reload voice.
- **Too many next actions:** The user will feel productive listing five. Force exactly one. The rest are distraction.

---

## Self-Verification (before finalizing)

- [ ] Every bucket item cites a supplied source.
- [ ] "Where it is now" and "What moved" are distinct, not duplicated.
- [ ] Stale waiting-on-others items are flagged.
- [ ] Exactly one loadbearing unknown.
- [ ] Exactly one next action, physical and < 5 min.
- [ ] At most two risks, each sourced.
- [ ] Brief fits on one page.
