---
title: "Individual ROM Trajectory Analyzer"
category: psychology/measurement-based-care
description: "Analyze one client's routine-outcome-monitoring (ROM) trajectory across sessions: response/remission status, expected-treatment-response comparison, not-on-track alerts, alliance (SRS) signal, and a session-level recommendation."
techniques:
  - DS-02
  - DT-01
  - QA-04
  - RT-02
  - CM-02
difficulty: intermediate
intended_use: model-testing
tags:
  - measurement-based-care
  - routine-outcome-monitoring
  - trajectory
  - expected-treatment-response
  - not-on-track
  - alliance
  - SRS
  - feedback-informed-treatment
updated: "2026-06-08"
related_prompts:
  - domain-psychology/measurement-based-care/psychology_treatment_non_response_decision_tree.md
  - domain-psychology/measurement-based-care/psychology_outcome_monitoring_dashboard_interpreter.md
  - domain-psychology/treatment-planning/psychology_measurement_based_care_plan.md
  - domain-psychology/treatment-planning/psychology_treatment_resistance_reformulation.md
---

# Individual ROM Trajectory Analyzer

## Objective

Analyze a single client's routine-outcome-monitoring (ROM) trajectory across sessions and convert the score series into a session-level clinical read. Produce: (1) current status (response, remission, no-change, deterioration) against the instrument's published bands, (2) a comparison of the observed trajectory to the expected treatment response (ETR) — the typical recovery curve for clients starting at this severity — to determine on-track vs not-on-track, (3) an alliance/engagement signal from session-rating data (SRS or equivalent), and (4) a concrete recommendation for the next session. This operationalizes feedback-informed treatment (FIT) at the individual level: catching the not-on-track case early enough to change course before non-response is locked in.

## When to Use

- At any session where a fresh ROM score is available and the clinician wants a trajectory read, not just a single-session score.
- At the first formal progress review (typically session 4–6) to check whether the client is tracking toward recovery.
- When the clinician's clinical impression and the client's self-report diverge from the numbers and a structured reconciliation is needed.
- When a not-on-track or deterioration alert has fired and a recommendation is needed before escalating to the full non-response decision tree.
- When preparing for supervision and the supervisee needs a trajectory summary of a specific case.

## Inputs / Context Required

- **Score series**: the instrument's scores by session number with dates (baseline through most recent). Minimum two points; more is better.
- **Primary instrument**: PHQ-9, GAD-7, PCL-5, ORS, OQ-45, OCI-R, AUDIT/DAST-10, etc. — to apply the correct bands, MCID, and remission threshold.
- **Baseline severity**: the intake/session-1 score (anchors the expected-treatment-response curve).
- **Session count / episode phase**: which session this is and the planned episode length.
- **Alliance / session-rating data** (if collected): SRS or WAI-SR by session.
- **Item-level risk flags**: PHQ-9 item 9 value, PCL-5 elevations, by session.
- **Clinical context**: any known life events, adherence issues, or treatment changes that could explain inflections.
- `[clinician input required: whether an expected-treatment-response/ROM algorithm is available in your system, or whether ETR must be approximated from severity-anchored rules]`
- `[clinician input required: client's verbal report this session, to reconcile with the score]`

## Constraints

### Must

- Apply the instrument's published bands: severity cutoffs, MCID, remission threshold, and reliable change index (RCI) where available. Do not invent values.
- Compute current status as one of: **remission** (score ≤ remission band, sustained where required), **response** (≥ MCID improvement or ≥50% reduction from baseline), **partial/inadequate** (improving but < MCID), **no change**, or **deterioration** (reliable worsening; RCI exceeded or instrument-specific increase).
- Determine **on-track vs not-on-track** by comparing the observed change to the expected treatment response for a client starting at this baseline severity. If a formal ETR algorithm is unavailable, approximate using severity-anchored, published rules (e.g., no MCID-level improvement by the expected point → not-on-track) and label the method.
- Distinguish measurement noise from signal: a single-point change within the RCI/measurement-error band is not a trajectory; require the change to exceed reliable-change criteria before calling deterioration or response.
- Incorporate the **alliance signal**: if SRS/WAI-SR is below the cut (e.g., SRS <36) or declining, surface it as a contributor — alliance strain is a leading correlate of not-on-track cases.
- Handle **risk items** explicitly: any positive PHQ-9 item 9 or PCL-5 elevation this session triggers a safety note in the output regardless of the overall trajectory.
- End with a single, concrete **session-level recommendation** (continue / reinforce / discuss trajectory / address alliance / intensify / route to non-response decision tree).

### Must Not

- Do not call "response" or "deterioration" off a change smaller than the reliable change / MCID criterion — that is reading noise.
- Do not declare a client on-track solely because the score dropped; compare to the expected trajectory for their baseline severity.
- Do not ignore an SRS/alliance drop just because the symptom score improved (or vice versa); report both signals.
- Do not dismiss a score-vs-clinical-impression discordance; reconcile it openly (instrument limits, response bias, content of session) rather than overriding the number or the clinician.
- Do not fabricate an expected-treatment-response curve or RCI; if not available, state the approximation method used.
- Do not defer a positive risk item to the trajectory discussion; it is handled as a safety item first.

## Instructions

1. **Tabulate the score series** by session and date for the primary instrument; note the baseline and the most recent score. Flag any gaps (missed administrations).

2. **Classify current status** against the published bands: remission / response / partial / no change / deterioration. Apply RCI or MCID to confirm that any "response" or "deterioration" call exceeds measurement error.

3. **Compare to expected treatment response.** Using the baseline severity and session number, judge whether the observed change is at, above, or below the expected recovery trajectory. State the method (formal ETR algorithm vs severity-anchored approximation). Output on-track / at-threshold / not-on-track.

4. **Read the alliance signal.** If SRS/WAI-SR data exist, report the current value and trend; flag below-cut or declining alliance as a contributing factor.

5. **Reconcile with clinical impression.** Compare the numeric trajectory to the clinician's impression and the client's verbal report this session. If discordant, name the likely sources and recommend exploring, not overriding.

6. **Triage risk items.** Note any positive PHQ-9 item 9 / PCL-5 elevation this session as a safety item with required action.

7. **Issue the session-level recommendation.** One concrete next step. If not-on-track persists past the expected point, route to the treatment-non-response decision tree.

8. **Run verification.**

## Output Format

```
=== INDIVIDUAL ROM TRAJECTORY ANALYSIS ===

CLIENT / EPISODE
Client ID: [..]   Primary instrument: [PHQ-9 / GAD-7 / PCL-5 / ORS / OQ-45 / ...]
Baseline severity: [score @ session 1]   This session: [# / date]   Planned length: [..]
Bands used — Remission: [≤ band]   MCID: [≥ X]   RCI: [≥ X if available]

SCORE SERIES
| Session | Date | Score | Δ from baseline | Δ from prior | Risk item (9 / PCL-5) |
|---------|------|-------|-----------------|--------------|------------------------|
| 1 (base)| [..] | [..]  | —               | —            | [..] |
| ...     | [..] | [..]  | [..]            | [..]         | [..] |
| current | [..] | [..]  | [..]            | [..]         | [..] |
[Gaps / missed administrations: ...]

────────────────────────────────────────────────────────
CURRENT STATUS
Status: [Remission / Response / Partial-inadequate / No change / Deterioration]
Basis: [Δ vs MCID / remission band; confirmed beyond RCI? yes/no]

EXPECTED-TREATMENT-RESPONSE COMPARISON
Method: [Formal ETR algorithm / Severity-anchored approximation — labeled]
Expected by session [#]: [≥ MCID / specific milestone]   Observed: [..]
Trajectory verdict: [On-track / At-threshold / NOT-ON-TRACK]

────────────────────────────────────────────────────────
ALLIANCE / ENGAGEMENT SIGNAL
SRS (or WAI-SR): current [score], trend [improving/stable/declining]
Flag: [Below cut (e.g., SRS <36) / declining → alliance contributor] or [No concern]

CLINICAL-IMPRESSION RECONCILIATION
Score vs clinician impression vs client report: [Concordant / Discordant]
If discordant — likely source(s): [Instrument limit / response bias / session content / other]
Recommended stance: [Explore openly — do not override number or clinician]

RISK ITEMS THIS SESSION
[ ] None positive.
[ ] Positive — PHQ-9 item 9 / PCL-5: [value] → Safety action: [..]   ← handled first

────────────────────────────────────────────────────────
SESSION-LEVEL RECOMMENDATION
[ ] Continue current plan; reinforce mechanisms of change.
[ ] On-track but discuss trajectory with client this session.
[ ] Address alliance / repair rupture (SRS signal).
[ ] Intensify dose/technique within current plan.
[ ] NOT-ON-TRACK past expected point → route to Treatment Non-Response Decision Tree.
Rationale: [1–2 sentences linking status + ETR + alliance to the chosen step.]
```

## Verification

- [ ] Published bands applied (severity, MCID, remission, RCI where available); no invented values.
- [ ] Current status classified as remission / response / partial / no change / deterioration.
- [ ] "Response" or "deterioration" confirmed to exceed RCI/MCID, not measurement noise.
- [ ] On-track vs not-on-track determined by comparison to expected treatment response, with method labeled (formal vs approximation).
- [ ] Alliance signal (SRS/WAI-SR) reported when available; below-cut or declining flagged.
- [ ] Score-vs-clinical-impression discordance reconciled openly, not overridden.
- [ ] Any positive PHQ-9 item 9 / PCL-5 elevation handled as a safety item first.
- [ ] Single concrete session-level recommendation issued; not-on-track routes to the non-response decision tree.
- [ ] No fabricated ETR curve or RCI; approximation method stated when used.
- [ ] Missing inputs flagged with `[clinician input required]`.
