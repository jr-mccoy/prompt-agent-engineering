---
title: "PRD One-Pager — A Right-Sized Spec for a Small Feature, With Testable Acceptance Criteria"
category: product-management/templates
description: "Write a one-page product spec for a feature one team can ship in a sprint or two: a sizing gate that sends large, irreversible or cross-team work to the full PRD, a problem with evidence, one outcome metric and a guardrail with baselines, explicit non-goals, and user stories whose acceptance criteria are binary Given/When/Then checks covering the edge, error, empty and permission cases — plus blocking open questions with owners."
techniques:
  - DP-14
  - DD-02
  - CM-03
  - DP-24
difficulty: beginner
tags:
  - prd
  - one-pager
  - acceptance-criteria
  - given-when-then
  - feature-spec
  - non-goals
  - small-feature-spec
  - write-requirements-quickly
  - how-do-we-know-its-done
updated: "2026-10-03"
related_prompts:
  - domain-product-management/templates/prd_template.md
  - domain-product-management/prompts/product_create_prd.md
  - domain-product-management/prompts/product_user_story_splitting.md
---

# PRD One-Pager

**Objective:** Produce the smallest spec a team can build and test from without
coming back to ask — one page, with acceptance criteria an engineer, a designer, and a
tester would each judge the same way.

**When to Use:**
- A feature is small enough for one team and one or two sprints, and the full PRD
  template would be ceremony.
- Tickets keep coming back as "not what I meant" because "done" was never written down.
- You want acceptance criteria that QA can turn into tests without interpretation.
- **Not this prompt if** the work crosses teams, changes pricing, data retention or
  compliance posture, or is hard to reverse — use the full
  `domain-product-management/templates/prd_template.md`, or be interrogated into it with
  `domain-product-management/prompts/product_create_prd.md`. If a story will not fit an
  iteration, split it first with `product_user_story_splitting.md`. For polishing PRD
  prose for a business audience, use
  `domain-professional-writing/business-writing/business_writing_prd_document.md`; for a
  developer's personal plan before coding, use
  `domain-engineering-workflows/workflows/pre_code_planning_canvas.md`.

## Inputs / Context

1. **The request** and who raised it.
2. **Evidence**: support tickets, interview notes, usage data — counts, not adjectives.
3. **The user and the moment**: who does this, in which workflow, how often.
4. **Constraints**: deadline, platform, permissions model, anything legal or contractual.
5. **The current behaviour** and any workaround people use today.

## Method

1. **Size gate first.** One-pager only if all hold: one team; ≤ ~2 sprints; reversible
   (feature flag or easy rollback); no new data model with migration; no pricing,
   privacy, or compliance change. Any "no" → full PRD. Too small (one story, no
   decisions) → a ticket is enough.
2. **Problem in one sentence, with evidence.** Who, what they cannot do, what it costs
   them, and the count behind it.
3. **One outcome metric and one guardrail (DP-24).** Each with baseline, target, and
   how it is measured. A metric without a baseline is a hope.
4. **Scope and non-goals (CM-03).** In scope as capabilities; at least two non-goals —
   the adjacent things someone will assume are included.
5. **Stories → acceptance criteria (DD-02).** 2–5 stories. Each criterion is binary and
   written Given / When / Then with concrete values. Translate every adjective: "fast" →
   "within 5 s for 200 items"; "clear error" → the exact message. Cover, per story where
   relevant: happy path, limit/edge, error, empty state, and permission.
6. **Decide partial-failure and notification behaviour explicitly.** These are the two
   decisions small specs most often leave to the engineer.
7. **Definition of done.** Criteria pass; metric instrumented; support note written;
   flag plan stated.
8. **Open questions.** Each with owner, date, and whether it blocks build start.
9. **One-page check (DP-14).** If it no longer fits on a page, cut detail into tickets or
   go back to step 1 — the feature is bigger than you thought.

## Output Format

```
# [Feature] — one-pager        Owner: [..]   Status: [draft/agreed]   Target: [sprint]

Size gate: one team ✓ · ≤2 sprints ✓ · reversible ✓ · no migration ✓ · no pricing/privacy ✓

## Problem
[who] cannot [what], costing [what] — evidence: [count, source]

## Outcome
Metric: [..] baseline [..] → target [..] by [date] (measured by [..])
Guardrail: [..] must stay ≤ [..]

## Scope
In: [...]
Non-goals: [...] (≥2)

## Stories and acceptance criteria
US-1 As a [user], I want [action] so that [outcome].
  AC1.1 Given [state], when [action], then [observable result with values].
  AC1.2 (edge) ...   AC1.3 (error) ...   AC1.4 (empty) ...   AC1.5 (permission) ...

## Decided behaviour
Partial failure: [..]   Notifications: [..]

## Done when
[criteria pass · metric instrumented · support note · flag plan]

## Open questions
| Question | Owner | Due | Blocks build? |
```

## Verification

- [ ] The size gate was run and every condition is shown.
- [ ] The problem cites a count and a source.
- [ ] Metric and guardrail each have a baseline and a measurement method.
- [ ] At least two non-goals are listed.
- [ ] Every acceptance criterion is binary, uses concrete values, and has no adjectives.
- [ ] Edge, error, empty, and permission cases are covered where they apply.
- [ ] Partial-failure and notification behaviour are decided, not left open.
- [ ] Blocking open questions have owners and dates; the spec fits on one page.

## False-Positive Prevention

1. **A big feature in a small template.** A one-pager for cross-team or irreversible
   work hides the decisions that need a full PRD. The size gate exists to stop that.
2. **Criteria that restate the story.** "User can reassign tickets" is not a test.
   Name the state, the action, and the observable result with numbers.
3. **Happy path only.** Most rework comes from the limit, the error, and the
   permission case; include them even when they feel obvious.
4. **Implementation as requirement.** "Use a modal" is design; "the lead confirms the
   target agent before any ticket changes" is the requirement.
5. **Metric chosen after launch.** If the baseline is not captured before release,
   the outcome cannot be judged. Instrument first.
6. **Open questions that block silently.** Mark which ones block build start; those
   are resolved before the sprint, not during it.

## Example Output

```
# Bulk reassign tickets — one-pager   Owner: Dana (PM)   Status: agreed   Target: Sprint 42

Size gate: one team ✓ · 1 sprint est. ✓ · behind flag `bulk_reassign` ✓ ·
uses existing assignee field ✓ · no pricing/privacy ✓

## Problem
Team leads cannot move an absent agent's queue in one step; they reassign tickets one
by one (median 11 min per absence, 3.4 absences/team/week) — evidence: 42 requests in
Q3 feedback board; timing from 6 screen recordings.

## Outcome
Metric: median time to reassign an absent agent's queue 11 min → < 1 min by 30 Nov
  (event log: first to last reassign per lead session)
Guardrail: reopen-after-reassign rate stays ≤ 2.0% (baseline 1.6%)

## Scope
In: select up to 200 tickets in any filtered view; reassign to one agent; audit log entry.
Non-goals: auto-reassign on out-of-office; round-robin across several agents;
  any change to SLA timers.

## Stories and acceptance criteria
US-1 As a team lead, I want to reassign selected tickets to one agent so that an
     absence does not stall the queue.
  AC1.1 Given 37 open tickets selected, when I choose "Ravi" and confirm, then all 37
        show assignee Ravi within 5 s and each activity log reads
        "Reassigned from <old> to Ravi by <lead>".
  AC1.2 (limit) Given 201 tickets selected, when I open Reassign, then the action is
        disabled with the text "Reassign up to 200 at a time".
  AC1.3 (edge) Given 1 of the 37 is closed, when I confirm, then 36 are reassigned and
        the summary reads "36 reassigned · 1 skipped (closed)".
  AC1.4 (error) Given Ravi is deactivated before I confirm, when I confirm, then no
        ticket changes and the error names Ravi as inactive.
  AC1.5 (permission) Given I have the Agent role, when I select tickets, then
        Reassign is not shown.
US-2 As the receiving agent, I want one notification so that I am not flooded.
  AC2.1 Given notifications are on, when 37 tickets are reassigned to me in one
        action, then I receive one digest listing 37 tickets, not 37 alerts.

## Decided behaviour
Partial failure: per-ticket; skipped tickets listed with reason; no rollback of the rest.
Notifications: one digest per action per receiving agent.

## Done when
AC1.1–2.1 pass in staging · reassign event instrumented · support macro updated ·
flag on for 3 pilot teams, then all after 2 weeks if guardrail holds.

## Open questions
| Should SLA first-response restart on reassign? | Dana + Support ops | 14 Oct | No (non-goal holds) |
| Show reassign in the customer-visible history? | Dana | 16 Oct | No |
```

## Techniques Used

- **DP-14 Compressed Specification Format** — one page, hard sections, overflow forces the size gate again.
- **DD-02 Vague-to-Concrete Translation** — every adjective in a criterion becomes a value or exact text.
- **CM-03 Scope Definition** — non-goals named for the adjacent features people will assume.
- **DP-24 Done Fudge Prevention** — metric baseline, binary criteria, and done conditions fixed before build.

## Related Prompts

- `domain-product-management/templates/prd_template.md` — the full PRD when the size gate fails.
- `domain-product-management/prompts/product_create_prd.md` — interrogation into a full PRD, MVP-first.
- `domain-product-management/prompts/product_user_story_splitting.md` — splitting a story that will not fit one iteration.
