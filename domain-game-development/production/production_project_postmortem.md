---
title: "Game Project Postmortem"
category: game-development/production
description: "Run a whole-project postmortem after a game ships or is cancelled: plan-versus-actual on schedule, budget, scope and outcomes; a slip account that sums; what went right and wrong traced to root causes with evidence from the tracker, playtests and reviews; and a short list of owned actions for the next project — distinct from incident postmortems and from ML project postmortems."
techniques:
  - RT-09
  - RT-05
  - DS-19
  - NE-24
difficulty: intermediate
tags:
  - postmortem
  - game-production
  - retrospective
  - lessons-learned
  - scope-management
  - crunch
  - project-cancelled
  - over-budget
  - missed-deadlines
updated: "2026-09-24"
related_prompts:
  - domain-engineering-workflows/workflows/engineering_postmortem_blueprint.md
  - domain-AI-ML/ai-product-leadership/aipm_failed_ml_project_postmortem.md
  - domain-game-development/design/design_game_design_document.md
---

# Game Project Postmortem

**Objective:** Turn the team's memory of a finished (or cancelled) game into an
evidence-backed account of where time, money and scope went, why, and the three
to five changes the next project will actually make.

**When to Use:**
- A game has shipped, a milestone closed, or a project was cancelled.
- The team wants the classic "what went right / what went wrong" but with numbers.
- A studio is about to start its next project and wants the last one's lessons applied.

**When NOT to use:**
- A live-service outage or a single production incident —
  `domain-engineering-workflows/workflows/engineering_postmortem_blueprint.md`.
  This prompt is distinct because it covers a multi-year project, not one event.
- A failed ML or AI product — `domain-AI-ML/ai-product-leadership/aipm_failed_ml_project_postmortem.md`.
- A sprint retrospective — the unit here is the whole project.

## Inputs

1. **Plan baselines**: original schedule, budget, feature list (from the pitch or GDD).
2. **Actuals**: ship date, spend, shipped feature list, cut list.
3. **Tracker and repo history**: epics, reopened tickets, large rewrites.
4. **Playtest reports** across the project.
5. **Outcomes**: sales vs forecast, review score and review text, platform cert results.
6. **Team input**: anonymous survey or interviews, including hours worked.

## Method

1. **Plan vs actual table.** Schedule, budget, feature count, outcome metrics —
   planned, actual, delta, delta %.
2. **Account for the slip.** Attribute every week of overrun to a cause, with an
   explicit "unattributed" line. The attributed weeks plus unattributed must
   equal the overrun.
3. **Synthesise the sources (DS-19).** Line up tracker history, playtest reports,
   reviews and team input on one timeline so claims are cross-checked, not
   remembered.
4. **What went right — with evidence (RT-05).** Three to five items, each tied to
   an observable result. Keep what worked on purpose.
5. **What went wrong — to root cause (RT-09).** For each: root cause → symptoms →
   evidence → what would have prevented it. Stop at a cause the team controls.
   Blameless: causes are decisions and systems, not people.
6. **Find the insight-to-action gaps (NE-24).** For each problem, was it known
   earlier? Where did the knowledge stop — no owner, no meeting, no budget? Those
   gaps are often the real lesson.
7. **Record crunch honestly.** Weeks over the studio's stated hours, how many
   people, and what drove them.
8. **Write 3–5 actions.** Each with an owner, the trigger point in the next
   project where it applies, and how the team will check it happened.

## Output Format

```
## Summary         — three sentences: what shipped, how it did, the main lesson
## Plan vs actual  — metric | planned | actual | delta | delta %
## Slip account    — cause | weeks | evidence ; total = overrun
## Went right      — item | evidence | keep how
## Went wrong      — root cause | symptoms | evidence | prevention
## Known earlier?  — problem | first signal (date, source) | where it stopped
## Crunch          — weeks over hours, people, drivers
## Actions         — action | owner | trigger in next project | check
## Confidence      — per section; which figures are reconstructed
```

## Verification

- [ ] Plan-vs-actual deltas and percentages recompute from the table.
- [ ] Slip-account weeks sum to the schedule overrun, including "unattributed".
- [ ] Every "went right/wrong" item cites evidence from at least one source.
- [ ] No root cause names a person; each names a decision, process or system.
- [ ] There are no more than five actions, and each has an owner and a check.

## False-Positive Prevention

1. **Shipping late is not proof of bad planning.** Some slip bought quality the
   reviews reward; say which weeks paid off.
2. **Cut features are not failures.** Cutting is how games ship; the finding is a
   cut made late after the cost was spent.
3. **Do not over-attribute.** Leave an "unattributed" line rather than forcing
   every week onto a cause.
4. **Review complaints are not all design flaws.** Separate what the game
   intended (hard boss in a hard game) from what it did not.
5. **A long action list is a sign of no actions.** More than five will not happen.
6. **Crunch is not a success factor.** Do not list overtime under "went right"
   because the game shipped.

## Example

**Input:** "Tidewright", 2D metroidvania, team of 5, burn $42,000/month, shipped
on PC and one console. Postmortem at 90 days after launch.

```markdown
## Summary
Tidewright shipped 6 months late and 30% over budget with 29 of 38 planned
features, and is at 84% of its 90-day sales forecast with 86% positive reviews.
The core lesson: two systems that touched everything (map and save) were never
proven together before content production.

## Plan vs actual
| Metric | Planned | Actual | Delta | % |
|---|---|---|---|---|
| Schedule | 20 months | 26 months | +6 | +30% |
| Budget | $840,000 | $1,092,000 | +$252,000 | +30% |
| Features | 38 | 29 shipped (9 cut) | −9 | −24% |
| 90-day units | 45,000 | 38,000 | −7,000 | −16% |
| Review positive | 85% | 85.7% (1,268 / 1,480) | +0.7 pt | — |

## Slip account (6 months ≈ 26 weeks)
| Cause | Weeks | Evidence |
|---|---|---|
| Map system rewritten twice | 9 | 2 map epics reopened; 214 tickets months 7–11 |
| Companion system added mid-production, nothing cut | 8 | epic created month 12; no cut ticket |
| Console cert failed twice (save corruption on suspend) | 3 | cert reports months 24–25 |
| Illness and leave | 2 | calendar |
| Unattributed | 4 | — |
| **Total** | **26** | |

## Went right
| Item | Evidence | Keep how |
|---|---|---|
| Playtest every 6 weeks (9 rounds) | movement praised in 41% of positive reviews | budget playtests in the plan from month 1 |
| Outsourced console port | delivered on its $90k line | same contract model |
| Weekly vertical build | zero "lost build" days in tracker | keep CI build rule |

## Went wrong
| Root cause | Symptoms | Evidence | Prevention |
|---|---|---|---|
| Map and save never prototyped together | map rewrites, save bugs | 9 weeks; cert failure | production-ready slice must include save + map |
| Scope added with no cut rule | companion system, late cuts of 9 features | 8 weeks | "one in, one out" at milestone reviews |
| Cert requirements read at month 23 | 2 cert failures | cert reports | cert checklist at alpha |

## Known earlier?
| Problem | First signal | Where it stopped |
|---|---|---|
| Boss 4 difficulty spike (66 of 212 negative reviews, 31%) | playtest round 6, month 18 | finding logged, no owner assigned |
| Save corruption on suspend | QA ticket month 16 | tagged "post-launch" |

## Crunch
6 weeks over 50 h/week, 4 of 5 people, months 23–25, driven by cert failures.

## Actions
| Action | Owner | Trigger | Check |
|---|---|---|---|
| Slice includes save + map + one full content loop | Tech lead | before production greenlight | slice review sign-off |
| One-in-one-out scope rule | Producer | every milestone review | cut ticket linked to each add |
| Every playtest finding gets an owner and a date | Design lead | each playtest synthesis | no ownerless findings in log |
| Platform cert checklist by alpha | QA lead | alpha milestone | checklist tracked in tracker |

## Confidence
Plan vs actual: High. Slip account: Medium — map-rewrite weeks reconstructed from
tickets. Crunch: Medium — self-reported hours.
```

## Techniques Used

- **RT-09 (Root Cause Explanation Pattern):** root cause → symptoms → evidence → prevention.
- **RT-05 (Evidence-Based Reasoning):** every claim tied to tracker, review or report data.
- **DS-19 (Multi-Source Narrative Synthesis):** tracker, playtests, reviews and team input on one timeline.
- **NE-24 (Insight-to-Action Chain Mapping):** where known problems stopped before action.

## Related Prompts

- `domain-engineering-workflows/workflows/engineering_postmortem_blueprint.md` — single-incident postmortems.
- `domain-AI-ML/ai-product-leadership/aipm_failed_ml_project_postmortem.md` — ML project postmortems.
- `domain-game-development/design/design_game_design_document.md` — the plan baseline the postmortem measures against.
