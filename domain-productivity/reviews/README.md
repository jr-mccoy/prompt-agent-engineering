# Review Cadence Prompts

Productivity-system reviews at three cadences (week, month, quarter) plus the time-audit telemetry that feeds them. Distinct from `domain-personal-development/prompts/agency/agency_weekly_review.md` (portfolio / proof-of-work / direction): these reviews are about *the productivity systems themselves* — capture, calendar, focus blocks, todo backlog — and whether they're tuned, drifting, or due for overhaul.

## Scope

**In scope:**
- Plan-vs-actuals reconciliation (time-audit)
- Weekly systems-health review (capture / calendar / blocks / backlog)
- Monthly tuning across the last four weekly reviews
- Quarterly structural review (keep / tune / overhaul / remove) + commitment audit

**Out of scope (refuse and refer):**
- Identity-level reckoning (yearly, midlife, post-loss) → `identity_life_audit_reckoning.md`
- Portfolio-level weekly review (what shipped, what's next) → `agency_weekly_review.md`
- Per-block context capture → `deepwork_block_end_context_capture.md`
- Project-state synthesis → `deepwork_project_state_synthesis.md`
- Motivation / energy / character → `domain-personal-development/`

## Composition patterns

The cadences depend on each other. Run them in order, top-down:

```
Time audit (per week)
  ↓ feeds
Weekly systems review (per week)
  ↓ aggregates into
Monthly mode review (per month)
  ↓ aggregates into
Quarterly mode review (per quarter)
```

A monthly review without 3+ weekly reviews to summarize will refuse. A quarterly without 2+ monthly reviews will refuse. The structure is the value; skipping layers degrades the diagnosis.

## What the prompts refuse

- Recommending new tools, apps, or branded frameworks as the answer
- Diagnosing motivation, energy, or character (refer to personal-development)
- Multi-system overhauls in a single review (max one repair per weekly; ≤ 2 tunings per monthly; ≤ 2 overhauls per quarterly)
- "Try harder" framings

## Cadence summary

| Prompt | Cadence | Time | Output |
|---|---|---|---|
| `reviews_time_audit_evidence_based.md` | Weekly | 15–20 min | Plan-vs-actuals delta + ≤ 3 plan updates |
| `reviews_weekly_systems_review.md` | Weekly | 15–20 min | 4 system statuses + 1 repair |
| `reviews_monthly_quarterly_cadence.md` | Monthly OR quarterly | 45 / 60–90 min | Tunings (monthly) or keep/tune/overhaul/remove (quarterly) |

## File map

| Prompt | Purpose |
|---|---|
| `reviews_time_audit_evidence_based.md` | Reconcile last week's stated plan with evidence (calendar, commits, messages) — what time actually went where, and ≤ 3 plan updates. |
| `reviews_weekly_systems_review.md` | Score capture / calendar / blocks / backlog G/Y/R; detect drift; ship one repair next week. |
| `reviews_monthly_quarterly_cadence.md` | Two-mode: monthly tuning over 4 weekly reviews; quarterly structural keep/tune/overhaul/remove + commitment audit with inversion question. |
