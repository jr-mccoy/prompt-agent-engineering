---
title: "Monthly and Quarterly System-Cadence Review (Two-Mode)"
category: productivity/reviews
description: "Two-mode review: monthly = system tuning + capacity check across the last four weekly reviews; quarterly = system overhaul + commitment audit across the last three months. Distinct from yearly identity work."
techniques:
  - ST-01
  - ST-02
  - OC-08
  - RT-02
  - NE-22
  - QA-19
difficulty: intermediate
tags:
  - monthly-review
  - quarterly-review
  - cadence
  - capacity
  - system-overhaul
updated: "2026-05-08"
related_prompts:
  - domain-productivity/reviews/reviews_weekly_systems_review.md
  - domain-productivity/reviews/reviews_time_audit_evidence_based.md
  - domain-productivity/bottlenecks/bottleneck_locator.md
  - domain-personal-development/prompts/identity/identity_life_audit_reckoning.md
  - domain-personal-development/prompts/agency/agency_weekly_review.md
---

# Monthly and Quarterly System-Cadence Review (Two-Mode)

**Objective:** Run the right cadence-level review on the productivity systems. Two modes (OC-08): **Monthly** is a tuning pass over the last four weekly reviews, looking at capacity and persistent drift. **Quarterly** is a structural pass over the last three months, looking for systems to remove, add, or overhaul, and for commitments that have outlived their usefulness.

**When to use:**
- **Monthly mode:** end of every month, ≤ 45 minutes, after at least 3 of the last 4 weekly reviews have been run.
- **Quarterly mode:** end of every quarter, ~60–90 minutes, after at least 2 of the last 3 monthly reviews have been run.

This prompt is *not* a yearly life review. Identity-level questions ("am I still on the right path") belong to `identity_life_audit_reckoning.md`, not here.

**Audience:** An individual reviewing their own productivity systems at cadence. Single-person scope.

---

## Inputs Required

1. **Mode declaration.** Monthly or Quarterly. If the user is unsure, ask: *Is it the end of a month or end of a quarter?* If it's mid-cycle and the user is reviewing because something feels off, the right prompt is `reviews_weekly_systems_review.md` or `bottleneck_locator.md`, not this one.
2. **Last 4 weekly review outputs (Monthly mode) or last 3 monthly review outputs (Quarterly mode).** Cite repairs taken, drift patterns observed, system statuses. If reviews weren't run, refuse — the cadence depends on prior layer.
3. **Capacity signals from the period:**
   - Average focus-block hours per week.
   - Output produced (artifacts, ships, decisions).
   - Energy curve (steady, declining, recovering).
4. **Commitment list.** Standing commitments active during the period — recurring meetings, regular projects, side projects, ongoing reviews/check-ins, subscriptions paid for productivity tools. Include the time/money/attention each costs.
5. **What changed.** New tools adopted, processes added, habits started, habits dropped during the period.
6. **One sentence per mode:**
   - Monthly: "Are the systems tuned for the work, or fighting it?"
   - Quarterly: "Are these the right systems to be running at all?"

If input 2 is missing (no prior reviews to summarize), refuse. Output: *"Cadence reviews depend on the prior layer. Run `reviews_weekly_systems_review.md` for [N] weeks before running this monthly, or run [N] monthly reviews before running quarterly."*

---

## Instructions

### Step 1 — Declare mode and confirm scope

State the mode at the top. Output a one-sentence reminder of what the mode is for:

- **Monthly:** tune the systems against the last 4 weeks of evidence; adjust capacity; address persistent drift.
- **Quarterly:** review what to keep / remove / overhaul; audit standing commitments; reset structurally.

State what the mode is *not* for: monthly is not for adopting a new framework; quarterly is not for an identity reckoning.

---

### Step 2A — Monthly mode

#### 2A.1 — Aggregate the four weekly reviews

Build a 4-row matrix from input 2:

| Week | Capture | Calendar | Blocks | Backlog | Repair attempted | Repair held? |
|---|---|---|---|---|---|---|

Look for:
- Persistent reds — a system Red for 2+ consecutive weeks.
- Repair completion rate — how many proposed weekly repairs actually happened.
- Recurring drift patterns — same drift signal appearing 3+ weeks of 4.

#### 2A.2 — Capacity check

Compare planned capacity against achieved:
- Planned focus-block hours / week vs. actual (input 3).
- If actual < 70% of planned consistently, capacity is over-committed.
- If actual is ≈ planned but output (input 3) is lower than expected, the issue is block quality, not capacity.

#### 2A.3 — Tuning prescription

Output 1–2 system tunings (more than 2 = unrealistic for a tuning pass). Examples:

- "Reduce planned focus blocks from 18h/week to 14h/week to match actual capacity. The other 4h were always going to mid-week meetings."
- "Move calendar repair from rolling weekly attempt to a permanent default: focus blocks pre-set at the same time every week, declined-by-default if a meeting is proposed."
- "Capture system has been Yellow for 3 of 4 weeks despite repairs. Re-run `bottleneck_capture_triage_system_design.md` with current evidence; the previous design didn't survive."

Do not redesign systems from scratch. Tuning, not overhaul. Overhaul is the quarterly mode.

#### 2A.4 — Capacity commitment for next month

State the explicit capacity for next month:
- Focus-block hours/week (target).
- Standing commitments accepted / declined for the month.
- One commitment to drop or pause if capacity is over-subscribed.

---

### Step 2B — Quarterly mode

#### 2B.1 — Read the three monthly tunings

Build a summary from input 2:
- What tunings were made each month.
- What stuck.
- What was tuned, untuned, then re-tuned in a different direction (these signal a structural rather than tuning issue).

#### 2B.2 — Run the keep / remove / overhaul triage on each system

For each of the four systems (capture, calendar, focus blocks, backlog) plus any standing process:

| Decision | Criteria |
|---|---|
| **Keep as-is** | Stable Green for most of the quarter; no recurring drift; tunings have been minor. |
| **Tune** | Yellow trending; tuning at the monthly level was working but is incomplete. (Stay in Monthly mode for these.) |
| **Overhaul** | System has been Red or unstable for ≥ 2 of 3 months; tunings haven't held; the structural premise is wrong for current work. |
| **Remove** | The system is being run out of habit; the work it was designed for has shifted. |

State the verdict per system. Overhaul or Remove triggers a follow-up prompt:
- Capture overhaul → re-run `bottleneck_capture_triage_system_design.md`.
- Calendar overhaul → re-run `deepwork_calendar_audit.md`.
- Focus blocks overhaul → re-run `deepwork_focus_parameters_estimator.md`.
- Backlog overhaul → 1-time deep triage; route to `bottleneck_capture_triage_system_design.md`.

Do not propose more than two overhauls in one quarterly review. Two is already a heavy quarter.

#### 2B.3 — Commitment audit (NE-22 inversion)

For each item in input 4, ask the inversion question: *"If I were not currently doing this, would I start doing it today, knowing what I know now?"*

Tag each commitment:
- **Yes — start today.** Keep.
- **Probably yes, but smaller.** Keep at reduced cadence.
- **No, but stuck.** Drop. Specify how (final session, resignation, end-of-subscription date).
- **Unknown.** Run a 30-day pause if reversible; otherwise flag for next quarter.

The expected result: 1–3 drops per quarter for most users. If zero, the audit was rubber-stamped — re-run.

#### 2B.4 — Structural overhaul output

State explicitly the changes for next quarter:
- Systems being kept as-is.
- Systems being tuned (continuing monthly mode).
- Systems being overhauled (which prompt to re-run, when).
- Commitments being dropped, paused, or reduced.

#### 2B.5 — Reset capacity baseline

Quarterly is the natural reset for capacity assumptions. State the new baseline focus-block hours / week for the coming quarter, accounting for known seasonal/calendar factors.

---

### Step 3 — Compare to the subjective sense (input 6)

Apply the question from input 6 to the data:

- **Monthly:** "Are the systems tuned for the work, or fighting it?"
  - Data tuned (most weeks Green) + subjective "tuned" → confirmed.
  - Data tuned + subjective "fighting" → upstream issue (energy, role mismatch). Refer to personal-development.
  - Data fighting + subjective "tuned" → user is normalizing failure. Name it.
- **Quarterly:** "Are these the right systems to be running at all?"
  - If the user can't answer affirmatively, the verdict skews toward Overhaul or Remove, not Tune.

### Step 4 — Refer when this is the wrong prompt

State the referral cases explicitly:
- If the cadence question has surfaced something life-shaped ("I think I want to leave this job") → `identity_life_audit_reckoning.md`, not here.
- If the systems are working but output isn't producing the desired progress → `bottleneck_locator.md`, not more system tuning.
- If energy / capacity is structurally low across the quarter → `agency_burnout_recovery.md` before any further system work.

### Step 5 — Lock the next cadence point

State the date of the next monthly or quarterly review. Make the cadence visible.

---

## Constraints

### Must
- Declare mode at the top.
- Refuse if the prior layer's reviews are missing.
- In Monthly mode, propose ≤ 2 tunings. In Quarterly mode, propose ≤ 2 overhauls.
- In Quarterly mode, run the commitment audit with the inversion question. Expect 1–3 drops; if zero, name it as rubber-stamping.
- Compare data to the mode-specific subjective question.
- Lock the next cadence date.

### Must Not
- Mix modes. Quarterly mode does not double as monthly; monthly does not double as quarterly.
- Recommend an identity-level reckoning here. Refer.
- Adopt a new productivity framework or tool as the prescription.
- Treat all systems as equally important; pick the systems to overhaul/remove based on the user's actual work.
- Output more than 2 tunings (monthly) or 2 overhauls (quarterly).

---

## False-Positive Prevention

1. **Don't run quarterly if monthly hasn't been running.** Quarterly is structural; without monthly's tuning trail, the structural verdict is uninformed.
2. **Don't tune in quarterly mode.** If the verdict on a system is Tune, that's monthly work; in quarterly, focus on Keep / Overhaul / Remove.
3. **Don't overhaul a system the user just recently designed.** A system needs ≥ 4 weeks to prove or disprove itself. New systems get monthly tuning, not quarterly overhaul.
4. **Don't accept zero drops in the quarterly commitment audit.** That's rubber-stamping. Force the inversion question on each commitment.
5. **Don't confuse system overhaul with role/life change.** "I want to overhaul my whole way of working" is often actually "I want to do different work." Refer.
6. **Don't propose more than two overhauls in one quarter.** Concurrent overhauls fail; sequence them.

---

## Output Format

```
**Mode:** Monthly / Quarterly

[One-sentence reminder of mode purpose.]

[Then output the relevant Step 2 block — Monthly OR Quarterly, not both.]

## (Monthly) System matrix
| Week | Capture | Calendar | Blocks | Backlog | Repair | Held? |
|---|---|---|---|---|---|---|

## (Monthly) Capacity check
Planned hours/week vs. actual: [numbers]. Verdict: [under-committed / well-matched / over-committed].

## (Monthly) Tunings (≤ 2)
1. ...
2. ...

## (Monthly) Capacity commitment for next month
[Hours, commitments, drops.]

---

## (Quarterly) System verdict matrix
| System | Verdict (Keep / Tune / Overhaul / Remove) | Justification | Follow-up prompt if Overhaul |
|---|---|---|---|

## (Quarterly) Commitment audit
| Commitment | Inversion result (start today?) | Decision (Keep / Reduce / Drop / Pause) |
|---|---|---|

## (Quarterly) Structural changes for next quarter
- Kept as-is: ...
- Tuned (monthly mode continues): ...
- Overhauled: [≤ 2; which prompt re-runs]
- Dropped / Paused: ...

## (Quarterly) Capacity baseline reset
[New focus-block hours/week baseline.]

---

## Subjective vs. data
Mode-specific question: "[input 6]"
Verdict: [Confirmed / Disagreement direction.]

## Referral (if applicable)
[Identity / energy / output-without-system referral path, or "none."]

## Next cadence date
[Specific date for next monthly or quarterly review.]
```

---

## Verification

- [ ] Mode declared at top; refusal triggered if prior layer missing.
- [ ] Monthly mode: matrix from 4 weekly reviews, capacity check, ≤ 2 tunings.
- [ ] Quarterly mode: verdict matrix per system, commitment audit with inversion question, ≤ 2 overhauls.
- [ ] Quarterly: commitment audit produced ≥ 1 drop, or "rubber-stamp" called out.
- [ ] Subjective vs. data comparison performed using the mode-specific question.
- [ ] Referral block included where applicable.
- [ ] Next cadence date stated.
- [ ] Modes not mixed.
