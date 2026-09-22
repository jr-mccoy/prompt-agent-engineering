---
title: "Build a Testable Definition of Done and Acceptance Criteria"
category: engineering-workflows/planning
description: "Convert a fuzzy deliverable ('build the dashboard') into a testable Definition of Done plus concrete, independently verifiable acceptance criteria in Given/When/Then form — sweeping the categories people forget (empty states, errors, a11y, performance, permissions) while right-sizing the criteria set to the task so small work doesn't get gold-plated."
techniques:
  - ST-01
  - ST-03
  - DS-06
  - QA-02
  - QA-20
difficulty: beginner
tags:
  - definition-of-done
  - acceptance-criteria
  - given-when-then
  - planning
  - scoping
  - work-items
updated: "2026-07-08"
related_prompts:
  - domain-software-engineering/testing/testing_unit_test_generation.md
  - domain-software-engineering/analysis/quality/quality_pull_request_diff_review.md
  - domain-decision-making/decisioning_prioritization_framework_selector.md
---

# Build a Testable Definition of Done and Acceptance Criteria

**Objective:** Turn one fuzzy work item into (a) a Definition of Done — the process/quality gates it must clear — and (b) a set of acceptance criteria in Given/When/Then form, each independently verifiable by someone other than the author, covering the implicit categories people forget, and sized to the task so a half-day fix doesn't acquire a thirty-criterion fortress.

Two concepts, kept deliberately separate throughout:

| Concept | What it is | Scope | Example |
|---|---|---|---|
| **Definition of Done (DoD)** | The standing quality bar — process gates largely invariant across items of this type | Team-level, reusable | "Code reviewed; tests pass in CI; deployed to staging; no new lint errors" |
| **Acceptance criteria (ACs)** | Item-specific, observable behaviors that make *this* deliverable complete | Per-item | "Given a user with no assigned accounts, when they open the dashboard, then an explanatory empty state appears" |

**The independent-verifiability test (applies to every AC):** a person who didn't build it can decide pass/fail from the criterion's text alone — it names a starting condition, a trigger, and an observable outcome, with no unmeasured adverbs ("fast," "properly," "intuitive") doing the real work.

## When to Use

- Use when: a ticket says "build X" or "fix Y" and two reasonable people would ship different things.
- Use when: handing work to a teammate, contractor, or AI agent and you want "is it done?" disputes prevented up front rather than litigated after.
- Use when: sprint planning — converting backlog items into ready-for-development stories with testable completion conditions.
- Don't use when: you need a full multi-feature PRD or spec — this prompt covers *one work item*; an epic gets flagged for splitting first.
- Don't use when: the work is genuinely exploratory (research spike) — define a timebox and questions-to-answer instead of a DoD; this prompt will say so if it detects that shape.

**Audience:** Product managers, tech leads, individual contributors, freelancers and their clients — anyone delegating or accepting a unit of work. No agile background assumed.

## Inputs / Context

1. **The deliverable (required).** Wrapped in `<task>…</task>`: the fuzzy statement exactly as it exists ("build the dashboard"), plus any known context — who it's for, where it runs, why now.
2. **Size estimate (optional).** Quick fix (< 1 day) / standard (1–5 days) / feature (1–3 weeks). If missing, the prompt infers from context and states the inference.
3. **Standing team DoD (optional).** Wrapped in `<standing_dod>…</standing_dod>`. If supplied, the output contains only item-specific *deltas*, never a re-listing.
4. **Constraints (optional).** Deadline, platforms, compliance requirements, feature-flag conventions. Absent constraints are surfaced as open questions, not invented.

## Constraints

### Must
- Keep DoD (process gates) and ACs (behaviors) in separate sections; never mix them.
- Write every AC as one observable behavior in Given/When/Then form with a unique ID (AC-1, AC-2…) and a **Verify by** method (manual step / automated test / tool).
- Sweep every implicit-criteria category (list below) and mark each **Applicable** (→ draft a criterion) or **N/A** (→ one-word reason). Surfacing all categories is mandatory; including all is not.
- Tier the criteria: **Must** (blocks done) / **Should** (do now or defer with a named follow-up) / **Out of scope** (explicitly listed so exclusion is a decision, not an accident).
- Respect the AC budget for the item's size: quick fix 3–6, standard 6–12, feature ≤ 15 (above that, recommend splitting the item and propose the split).
- End with open questions for the requester wherever the task text forced an assumption.

### Must Not
- Use unmeasurable adverbs as criteria ("loads quickly," "handles errors gracefully") — every quality gets a measurable proxy or gets cut.
- Bundle multiple behaviors into one AC ("filtering, sorting, and export work") — partial failures must be visible.
- Write implementation choices as ACs ("use Redis for caching") — criteria describe observable behavior, not solutions.
- Invent requirements the requester never implied and place them in **Must** — anything beyond the ask lands in Should, Out of scope, or Open questions.
- Duplicate the standing DoD into the item when one was supplied.
- Pad small tasks to look rigorous — the criteria count is evidence of judgment, not effort.

## Instructions

1. **Classify the item.** Type (UI feature / API / bugfix / data / infra / docs) and size (quick fix / standard / feature), inferring and labeling `[inferred]` where unstated. State the resulting AC budget. If the item is actually an epic (multiple user-facing outcomes), stop and recommend a split with suggested boundaries before speccing anything.

2. **Extract the intent.** Who uses this, what observable outcome means success, what "done" unlocks downstream. Where `<task>` names no user or outcome, choose the most plausible reading and mark it `[assumed]` — assumptions are surfaced, not silently embedded.

3. **Draft the Definition of Done.** The process/quality gates for this item type (or deltas to `<standing_dod>` if supplied): review, tests-in-CI, deployment target, flag handling, observability hook, docs/runbook line. Keep it to gates — no behaviors here.

4. **Draft the behavioral ACs.** Given/When/Then, one behavior each, IDs assigned, happy path first, then the item's obvious variants. Each carries its **Verify by** method.

5. **Run the implicit-criteria sweep.** Walk all categories: empty/first-run states; error states (network, invalid input, permission denied, timeout); loading/intermediate states; edge volumes (zero, one, max, pagination boundary); accessibility (keyboard, screen-reader labels, not-color-alone); performance (budget under realistic data volume); security/permissions; platform/responsive; localization/formats; observability (logs, analytics); data integrity (idempotency, concurrent edits). Mark each Applicable → criterion, or N/A → one-word reason.

6. **CRITICAL: Verify — adversarial and verifiability pass.**
   - **Adversarial attack:** name 3–5 concrete ways the work could satisfy every listed criterion and still be broken, unusable, or embarrassing in production. Each surviving attack becomes a new AC or an explicit Out-of-scope entry — never silently dropped.
   - **Verifiability audit:** for each AC, could a non-author decide pass/fail from its text alone? Rewrite any criterion whose verdict depends on interpretation; give the measurable proxy or delete it.
   - **Gold-plating check:** count Must + Should against the size budget. If over, demote or cut — naming what was demoted and why — until within budget.

7. **Deliver the tiered output** in the exact format below, closing with the open questions the requester must answer.

## False-Positive Prevention (MUST follow)

Here a "false positive" is a criterion that looks rigorous but isn't verifiable — or scope that looks required but was invented.

❌ **DON'T:**
- Ship ACs whose operative words are unmeasured ("fast," "clean," "user-friendly," "robust").
- Bundle behaviors so one AC can half-pass invisibly.
- Add localization, offline mode, or mobile layouts to an internal desktop tool and present them as mandatory.
- Mark a category N/A without a reason — silent exclusions are how empty states get forgotten.
- Copy the team's standing DoD into every item, training people to skim it.
- Encode solution choices ("must use WebSockets") as acceptance criteria.

✅ **DO:**
- Give every quality a number, a named artifact, or an observable condition ("p95 initial render < 2s on the staging dataset of ~600 accounts").
- Keep one behavior per AC so review and test map one-to-one.
- Put invented-but-sensible extras in Should or Open questions, where the requester decides.
- Attach the one-word reason to every N/A ("l10n: N/A — internal EN-only").
- Reference the standing DoD and write only the deltas.
- Let the requester's silence become an open question rather than a guessed requirement.

## Dual-Failure Prevention (QA-20)

❌ **HARMFUL failure:** A DoD that passes while the work is broken — vague criteria ("works properly") that can't fail, or missing error/empty states that detonate in production week one, recreating exactly the disputes the document existed to prevent.

❌ **UNHELPFUL failure:** Gold-plating — a thirty-criterion fortress around a half-day fix, or boilerplate a11y/perf/l10n stapled to everything regardless of applicability. The predictable end state is worse than no DoD: the team learns to ignore the document entirely.

✅ **Quality bar:** The assignee could start without asking a question, a reviewer could verify every criterion without the author in the room, and the size of the criteria set is visibly proportionate to the size of the task.

## Expected Output

Classification with AC budget, intent with assumptions marked, the DoD (or deltas), tiered Given/When/Then criteria with IDs and verification methods, the full applicability sweep, the adversarial pass with what it changed, and open questions.

### Output Format

```
# Definition of Done & Acceptance Criteria: [item]

## Classification
Type: […]   Size: […] [inferred?]   AC budget: […]   Split recommended: [no / yes + boundaries]

## Intent
User: […]   Success looks like: […]   [assumed] markers where applicable

## Definition of Done   [or: Deltas to standing DoD]
- [ ] [process gate]
- [ ] …

## Acceptance criteria — Must
AC-1. Given […], When […], Then […].   Verify by: [manual / automated test / tool]
AC-2. …

## Acceptance criteria — Should (do now or defer with named follow-up)
AC-n. …   If deferred: [follow-up ticket note]

## Out of scope (explicit)
- [excluded thing] — [one-line reason]

## Implicit-criteria sweep
| Category | Applicable? | Criterion or reason |

## Adversarial & verifiability pass
- Attack tried: […] → [AC added / moved out of scope / already covered]
- Rewritten for verifiability: [before → after]
- Gold-plating check: [count vs. budget; what was demoted]

## Open questions for the requester
1. …
```

## Example Output

```
# Definition of Done & Acceptance Criteria: "Build the CS health-score dashboard"

## Classification
Type: UI feature + one backing API endpoint   Size: feature (~4–5 person-weeks) [inferred
from scope]   AC budget: ≤ 15 (Must + Should)   Split recommended: no — single screen,
single endpoint, one user role.

## Intent
User: the 8-person Customer Success team.   Success looks like: a CS rep spots at-risk
accounts from one screen without opening each account individually.   [assumed] Internal
tool, desktop-first, English-only — flagged in Open questions.

## Definition of Done
- [ ] Code reviewed and merged; unit + integration tests green in CI
- [ ] Deployed to staging; product owner completes a walkthrough against the Must ACs
- [ ] No new lint/type errors; no console errors on load
- [ ] Behind feature flag `cs_health_dash`, with a removal ticket filed at launch
- [ ] Page-view and row-click analytics events firing (verified in staging)
- [ ] One-paragraph runbook entry: owner, data source, what "score stale" means

## Acceptance criteria — Must
AC-1. Given a CS user with ≥1 assigned account, When they open /health, Then a list of
      their accounts renders with name, health score (0–100), 30-day trend arrow, and
      last-activity date, sorted worst-score-first.   Verify by: automated E2E test.
AC-2. Given an account with score < 40, When the list renders, Then the row carries an
      "at risk" marker conveyed by icon + text, not color alone.   Verify by: automated
      test + manual grayscale check.
AC-3. Given a CS user with no assigned accounts, When they open /health, Then an
      explanatory empty state with a link to the assignment page appears — no blank
      table, no error.   Verify by: automated test.
AC-4. Given the health API returns a 5xx or times out (>10s), When the dashboard loads,
      Then the user sees a retry control naming the failed action, no infinite spinner,
      and the error is logged with a request ID.   Verify by: automated test with
      fault injection.
AC-5. Given any load, When the page opens, Then a skeleton state appears within 200ms
      and resolves to data or the AC-4 error state.   Verify by: automated test.
AC-6. Given the largest real dataset (staging copy, ~600 accounts), When the dashboard
      loads, Then p95 initial render < 2s over 20 trials.   Verify by: perf script in CI.
AC-7. Given a signed-in user without the cs_role permission, When they request /health
      or its API, Then they receive 403 and the response body contains no account data.
      Verify by: automated API test.

## Acceptance criteria — Should
AC-8. Given the list is rendered, When the user activates a column header (score, name,
      last activity) by mouse or keyboard, Then rows re-sort and the active sort is
      announced to screen readers.   If deferred: file FE-a11y follow-up; full a11y
      audit is already a separate ticket.
AC-9. Given an account's score was computed > 24h ago, When its row renders, Then a
      "stale" indicator with the computed-at time appears.   If deferred: requires the
      Open question 1 answer first.
AC-10. Given a row is clicked, When navigation occurs, Then an analytics event with
      account ID fires.   Verify by: staging event log.

## Out of scope (explicit)
- Filtering/search — separate item once usage data justifies it
- CSV export — not requested; raises data-handling questions
- Mobile layout — internal desktop tool [assumed; see Open questions]
- Configurable score weights — scoring model owned by the data team
- Per-account drill-down page — its own work item
- Localization — internal EN-only

## Implicit-criteria sweep
| Category            | Applicable? | Criterion or reason                       |
|---------------------|-------------|-------------------------------------------|
| Empty/first-run     | Yes         | AC-3                                       |
| Error states        | Yes         | AC-4                                       |
| Loading states      | Yes         | AC-5                                       |
| Edge volumes        | Yes         | AC-6 (600); zero covered by AC-3          |
| Accessibility       | Partial     | AC-2, AC-8; full audit = existing ticket  |
| Performance         | Yes         | AC-6                                       |
| Security/permissions| Yes         | AC-7                                       |
| Platform            | Partial     | Chrome + Firefox per IT standard [assumed]|
| Localization        | N/A         | internal                                   |
| Observability       | Yes         | DoD events + AC-4 request-ID logging      |
| Data integrity      | N/A         | read-only view                             |

## Adversarial & verifiability pass
- Attack: "passes every AC but the scores themselves are wrong/stale" → source-of-truth
  is upstream (Open question 1); staleness surfaced via AC-9.
- Attack: "600-account render passes, but sorting janks" → sort behavior scoped in AC-8
  with re-render covered by the AC-6 methodology.
- Attack: "risk marker invisible to colorblind users" → AC-2 amended to icon + text.
- Attack: "feature flag never removed; page rots half-shipped" → DoD requires a removal
  ticket at launch.
- Rewritten for verifiability: "dashboard is fast" → AC-6 (p95 < 2s, 600 accounts);
  "handles errors gracefully" → AC-4 (retry control, no spinner, logged request ID).
- Gold-plating check: 7 Must + 3 Should = 10 ≤ 15 budget. Demoted: full keyboard/SR
  audit to the existing a11y ticket rather than blocking this item.

## Open questions for the requester
1. What is the health score's source of truth and refresh cadence? (Blocks AC-9.)
2. Should CS managers see unassigned accounts, or strictly their own book?
3. Confirm desktop-only and Chrome + Firefox as the support matrix.
```

## Customization Guide

- **Bugfixes:** DoD gains "regression test reproducing the original defect"; AC budget drops to 3–5; the sweep collapses to error states and edge volumes only.
- **API-only items:** replace UI categories with contract tests, status-code matrix, idempotency, rate limits, and versioning; Given/When/Then still applies ("Given a duplicate request ID, When POSTed twice, Then exactly one resource exists").
- **User-story teams:** emit the Must tier as the story's acceptance criteria and each Should as a linked follow-up story.
- **Delegating to an AI agent:** restrict every **Verify by** to executable checks — no "manual walkthrough" — so the agent can self-verify completion.
- **Client/freelance contracts:** attach the Out-of-scope list to the SOW and make the Must tier the payment trigger; ambiguity here is where disputes are born.

## Techniques Used

- **ST-01 (Clear Objective Statement):** the objective fixes the twin deliverables (DoD + verifiable ACs) *and* the proportionality requirement, so the model neither merges the two concepts nor pads small tasks.
- **ST-03 (Output Format Specification):** the deliverable is itself a format — the template-based skeleton (IDs, Given/When/Then, Verify-by field, tiered sections, sweep table) is what makes every criterion uniform, checkable, and comparable across items.
- **DS-06 (Prioritization and Severity Guidance):** Must / Should / Out-of-scope tiers plus size-based AC budgets are the anti-gold-plating mechanism — criteria are ranked and capped, and demotions are named rather than silent.
- **QA-02 (Adversarial Stress-Test):** the "passes every criterion yet still fails in production" attack is the engine that surfaces forgotten cases, and the verifiability audit attacks each AC's testability, rewriting adverbs into measurable proxies.
- **QA-20 (Dual-Failure Prevention):** guards both endings — unverifiable criteria that let broken work ship, and a criteria fortress that teaches the team to ignore DoDs — with the bar that assignee, reviewer, and effort-proportionality all check out.

## Related Prompts

- `domain-software-engineering/testing/testing_unit_test_generation.md` — turn the Given/When/Then criteria into executing tests.
- `domain-software-engineering/analysis/quality/quality_pull_request_diff_review.md` — the reviewer checks the diff's test adequacy against exactly these criteria.
- `domain-decision-making/decisioning_prioritization_framework_selector.md` — decide *which* backlog item deserves speccing before speccing it.

## Verification

- [ ] Frontmatter complete; every technique ID exists in the index.
- [ ] When-to-Use includes a don't-use case.
- [ ] Instructions include an explicit verification step (step 6).
- [ ] False-Positive Prevention has real ❌/✅ pairs.
- [ ] Dual-Failure Prevention covers harmful AND unhelpful directions.
- [ ] Findings carry Confidence levels (verifiability audit + applicability markers on every category).
- [ ] Example Output is concrete and 80–120 lines.
- [ ] No invented data or fabricated authority.
