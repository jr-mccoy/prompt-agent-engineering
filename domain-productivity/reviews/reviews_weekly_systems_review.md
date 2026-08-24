---
title: "Weekly Systems Review (Productivity Lens)"
category: productivity/reviews
description: "Run a weekly review focused on the productivity systems themselves — capture, calendar, focus blocks, todo backlog — checking each for health, drift, and one repair. Distinct from agency/portfolio weekly reviews."
techniques:
  - ST-01
  - ST-02
  - QA-19
  - RT-06
  - DS-02
difficulty: beginner
tags:
  - weekly-review
  - systems-maintenance
  - cadence
  - drift-detection
updated: "2026-05-08"
related_prompts:
  - domain-productivity/reviews/reviews_time_audit_evidence_based.md
  - domain-productivity/reviews/reviews_monthly_quarterly_cadence.md
  - domain-productivity/bottlenecks/bottleneck_capture_triage_system_design.md
  - domain-productivity/deep-work/deepwork_calendar_audit.md
  - domain-personal-development/prompts/agency/agency_weekly_review.md
---

# Weekly Systems Review (Productivity Lens)

**Objective:** Once a week, audit the *productivity systems* themselves — not the projects, not the portfolio — for health, drift, and one specific repair. Outputs four health signals (capture, calendar, focus blocks, todo backlog), three drift signals, and exactly one repair to execute next week.

**When to use:** Weekly. Pairs with `agency_weekly_review.md` (portfolio / direction / proof-of-work) — run this first or after, but not as a replacement. This review is short (≤ 20 min), narrow (systems only), and produces a single repair.

**Audience:** An individual maintaining their own productivity systems. Single-person scope.

---

## Inputs Required

1. **Capture/triage health signals:**
   - Number of days the daily triage block was held (out of however many planned this week).
   - Inbox state at end of week — close to zero, partially clear, or backlogged.
   - Documented leaks this week (things that fell through; cite specific examples).
2. **Calendar health signals:**
   - Number of planned focus blocks this week.
   - Number actually held vs. moved/skipped.
   - Number of meetings added mid-week (i.e., not on Monday's calendar).
3. **Focus block quality signals:**
   - Average duration actually achieved per block (not the planned duration).
   - Self-reported quality of focus on a 1–5 scale per block, or rough averages.
   - Number of self-interruptions during blocks (rough count).
4. **Todo backlog health signals:**
   - Total count of open todos.
   - Number of items > 14 days old.
   - Number of items the user can no longer remember the context for.
5. **Time-audit telemetry from `reviews_time_audit_evidence_based.md`** (if run this week — strongly recommended as input).
6. **One subjective sentence on how the systems feel.** Smooth, scratchy, broken, ignored?

If three or more of inputs 1–4 are unmeasured, the systems aren't being tracked at all — name that as the finding and recommend instrumentation as the only repair (one signal at a time).

---

## Instructions

### Step 1 — Score each system on the green / yellow / red scale

Apply this rubric:

| System | Green | Yellow | Red |
|---|---|---|---|
| **Capture / triage** | Triage held ≥ 5 days; inbox near-zero EOW; ≤ 1 documented leak. | Triage held 3–4 days; inbox partially clear; 2–3 leaks. | Triage held ≤ 2 days; inbox backlogged; 4+ leaks. |
| **Calendar** | ≥ 80% of planned focus blocks held; ≤ 2 meetings added mid-week. | 50–80% held; 3–5 meetings added mid-week. | < 50% held; chaos / mid-week additions dominant. |
| **Focus blocks** | Avg block ≥ planned duration; quality ≥ 3.5/5; few interruptions. | Blocks fragmented or quality 2.5–3.5; some interruptions. | Blocks consistently cut short, quality < 2.5, frequent interruption. |
| **Todo backlog** | Backlog stable or shrinking; few items > 14 days old; context retained. | Backlog growing slowly; some old items; some context loss. | Backlog growing fast; many items > 14 days; user can't remember the why for many items. |

Output: four colored statuses with one-line evidence each.

### Step 2 — Detect drift across systems

Drift is when a system that was Green is starting to slide Yellow, or one Yellow system is causing another to slide. Look for these specific drift patterns:

| Drift pattern | Signal | Implication |
|---|---|---|
| **Calendar → focus blocks** | Calendar drifted Yellow → focus block quality dropped this week. | Repair calendar first; blocks are downstream. |
| **Capture → todo backlog** | Triage held fewer days → backlog grew or context-loss increased. | Repair capture; backlog is downstream. |
| **Focus blocks → backlog** | Blocks held but quality low → planned outputs not produced → tasks pile into backlog. | Repair block quality; backlog is symptom. |
| **All systems Yellow simultaneously** | Often signals upstream issue (energy, burnout, calendar overload). | Escalate — see below. |
| **One Red, others Green** | Localized failure. | Focused repair. |

Name the drift pattern that fits this week's data, or "no drift — systems stable."

### Step 3 — Compare the subjective sense (input 6) to the data

The system status from Step 1 is the data; the subjective sense is the pattern-match.

- Data Green + subjective "smooth": confirmed.
- Data Yellow + subjective "smooth": user is normalizing to a worse-than-baseline state. Name this; it's the most missed pattern.
- Data Green + subjective "scratchy": something is wrong upstream of the systems (energy, mismatch, motivation). Refer to `domain-personal-development/`.
- Data Red + subjective "broken": confirmed; proceed.
- Data Red + subjective "fine": probably under-instrumentation in subjective signal; the systems are failing but the user has stopped tracking.

### Step 4 — Choose exactly one repair

The repair targets the most-Red system (or the most-Yellow if no Red), unless drift analysis (Step 2) points upstream — in which case, fix upstream.

The repair must be:
- Specific (named change, not a goal).
- Bounded (one change, not a multi-step plan).
- Testable next week (this week's review is next week's input).

Examples:
- Capture Red → "Hold daily triage at 16:00 for 15 min for 5 of 5 working days next week. If skipped, document why."
- Calendar Red → "Block 8–10 Tue/Wed/Thu as focus; protect against meetings (decline or counter-propose)."
- Blocks Yellow due to interruption → "One change from `deepwork_environment_friction_design.md`."
- Backlog Red → "30-minute backlog triage Monday: every item > 30 days old gets Drop, Schedule, or Defer-with-trigger. No exceptions."

### Step 5 — Refer if upstream

If the drift analysis (Step 2) shows "all systems Yellow simultaneously" or "Green systems but subjective scratchy," the issue is not at the systems layer. State the referral:

- All systems Yellow / Red simultaneously over multiple weeks → `bottleneck_locator.md` for cross-lane diagnosis or `agency_burnout_recovery.md`.
- Subjective sense disagrees with data Green → `domain-personal-development/` (motivation, identity, mismatch).
- Backlog growing despite Green capture and calendar → scope problem, not a productivity-system problem; route to `bottleneck_clarity_ambition_surfacer.md`.

### Step 6 — Set the next-week telemetry promise

State which signals the user is committing to track this coming week. The point is to keep the review reviewable: a system without telemetry can't be reviewed.

Minimum: two of the four input categories instrumented. More is fine; less and the next review will be qualitative-only.

---

## Constraints

### Must
- Score each of the four systems Green / Yellow / Red with one-line evidence.
- Name a drift pattern from the table or "no drift."
- Compare data status to subjective sense; name the disagreement if present.
- Output exactly one repair.
- State next-week telemetry commitment.

### Must Not
- Recommend more than one repair per review.
- Re-engineer all four systems in one pass. (That's `bottleneck_locator.md` territory across multiple weeks.)
- Diagnose motivation, energy, or character. Refer instead.
- Recommend new productivity tools or apps as the repair.
- Replace `agency_weekly_review.md`'s portfolio function.

---

## False-Positive Prevention

1. **Don't accept "Green" by self-report alone.** Tie each Green to one piece of evidence from inputs 1–4.
2. **Don't pick a repair on the wrong system.** Drift analysis (Step 2) often points upstream of the loudest symptom. Fix upstream first.
3. **Don't escalate to multi-system overhaul.** This is a 20-minute review producing one repair. Multi-week structural patterns belong to the monthly review.
4. **Don't normalize chronic Yellow.** If the same system has been Yellow for ≥ 4 weeks, that's structural — escalate.
5. **Don't conflate this with `agency_weekly_review.md`.** Run both: this for systems-health, that for portfolio. Two complementary 15–20 minute reviews.
6. **Don't recommend instrumentation overhaul.** If the user can't track all four, they can track two; better to pick two than skip the review.

---

## Output Format

```
## System health
| System | Status | Evidence |
|---|---|---|
| Capture / triage | Green / Yellow / Red | ... |
| Calendar | ... | ... |
| Focus blocks | ... | ... |
| Todo backlog | ... | ... |

## Drift pattern
**Pattern:** [from table or "no drift"]
**Implication:** [one sentence]

## Subjective sense vs. data
User said: "[input 6]"
Data says: [Confirmed / Disagreement]. [If disagreement: which direction and why.]

## One repair (next week)
**Targets:** [system, justified by Step 4 logic]
**Specific change:** [bounded, named, testable]
**Test next week:** [what to look for in next review]

## Referral (if applicable)
[Upstream issue named with route, or "none — repair is at the systems layer."]

## Telemetry commitment for next week
- Will track: [signals]
- Will not track this week: [signals user is dropping with explicit acknowledgment]
```

---

## Verification

- [ ] All four systems scored G/Y/R with one-line evidence.
- [ ] Drift pattern named (from the table or "no drift").
- [ ] Subjective sense compared against data; disagreement named if present.
- [ ] Exactly one repair output, specific and testable.
- [ ] Referral block triggered if drift indicates upstream issue.
- [ ] Telemetry commitment for next week stated.
- [ ] No motivation-class advice, no new-tool recommendations.
