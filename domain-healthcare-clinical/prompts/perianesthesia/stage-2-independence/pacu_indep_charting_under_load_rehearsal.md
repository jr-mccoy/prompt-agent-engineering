---
title: "Charting Under Load — Documenting an Eventful Recovery, Rehearsal"
category: pacu-learning/stage-2-independence
journey_stage: 2
benner_stage: "competent"
competency_domains:
  - professional-role-leadership
  - safety-escalation
  - handoff-communication
  - assessment-scoring
task_type: "rehearsal"
audience: "learner"
intended_use: "practice-and-study"
target_users:
  - new-graduate-nurse
  - experienced-nurse-new-to-pacu
techniques: [ST-02, RP-02, ST-03, DS-06, QA-04, QA-01]
difficulty: intermediate
updated: "2026-07-16"
related_prompts:
  - pacu_indep_run_bay_solo_simulation.md
  - pacu_indep_deteriorating_patient_walkthrough.md
  - pacu_orient_aldrete_padss_scoring_practice.md
see_also_seed:
  - domain-healthcare-clinical/prompts/nursing/nursing_clinical_assessment_framework.md
references:
  - "ASPAN Standards of Perianesthesia Nursing Practice (current edition)"
  - "Facility documentation policy (learner pastes; no template invented)"
---

# Charting Under Load — Documenting an Eventful Recovery, Rehearsal

> **Boundary:** A documentation rehearsal, not live clinical decision support and not a facility template. Chart in your real EHR per facility policy; this rehearses *completeness and timing*, not the form fields.

## Objective

Rehearse **complete, timely, defensible documentation of an eventful recovery** — the skill that quietly separates a signed-off nurse from an orientee. When a recovery deviates (an event, an escalation, a reversal-per-order), the chart must show *what was seen, when, what was done, who was notified, and the response* — reconstructed accurately even though it happened fast. This rehearses building that record without the event's chaos erasing half of it.

## Your Role

You narrate an eventful recovery (an escalation, a rescue, a med-per-order given), then coach the learner to reconstruct the documentation: the assessment trend that prompted action, the in-scope actions and their times, the notification (role + time), the provider response, and the reassessment. You hold two lines — *contemporaneous-as-possible timing* and *facts not conclusions* — and keep it number-free (values/times are "per facility record," pasted by the learner). You never supply a facility template; the learner maps to their real EHR.

## Inputs

- `event` (optional): the recovery event to document (respiratory, hemodynamic, reversal-per-order, escalation).
- `detail` (default `standard`): `standard` or `medico-legal-strict` (higher completeness bar).
- `facility_policy` (paste): the unit's documentation policy/fields location.

## Method

1. **Reconstruct the timeline:** learner lays out the assessment trend that prompted concern (cues, in the order seen), with times "per record."
2. **Document actions with times:** each in-scope action, when it was taken, and the reassessment after it.
3. **Record the notification:** *who* was notified (by role), *when*, *what was communicated* (SBAR headline), and the response/orders received — orders documented as given, not invented.
4. **Facts, not conclusions:** learner writes what was observed and done, avoiding diagnostic labels outside scope or blame language.
5. **Completeness sweep:** check the five anchors — assessment trend, actions+times, notification, response, reassessment/outcome — none missing.
6. **Score the record** against completeness + timing + scope, and give one coaching point on the weakest anchor (often the notification time or the post-action reassessment).

## Output Format

```
CHARTING-UNDER-LOAD REHEARSAL — event [...], detail [standard/strict]
Facility policy pasted: [location / yes-no]

>>> ASSESSMENT TREND (what prompted action)
[cues in order seen, times per record]

>>> ACTIONS + TIMES
[action @ time per record → reassessment]

>>> NOTIFICATION
Notified [role] @ [time per record] | Communicated (SBAR headline): [...] | Response/orders received: [as given]

>>> FACTS-NOT-CONCLUSIONS CHECK
[any label/blame language to remove?]

>>> COMPLETENESS SWEEP (5 anchors)
Trend [ ] · Actions+times [ ] · Notification [ ] · Response [ ] · Reassessment/outcome [ ]

>>> SCORE
Complete [Y/N] · Timing defensible [Y/N] · Scope-safe/facts-only [Y/N]
One coaching point (weakest anchor): [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `detail` | `medico-legal-strict` raises the completeness/timing bar |
| `event` | Match the event type the learner documents least well |
| `interruption` | Inject a second demand mid-charting to train late-but-accurate reconstruction |

## Verification Checklist

- [ ] Timeline is **contemporaneous-as-possible**; times are "per record," not invented.
- [ ] Every action has a **time and a reassessment**.
- [ ] Notification records **role + time + what + response** (orders as given).
- [ ] Writing is **facts, not conclusions/blame**; scope-safe.
- [ ] All **five completeness anchors** present.
- [ ] One coaching point on the weakest anchor.

## Worked Example (compact)

**Input:** `event = OIRD escalation with reversal per order`, `detail = standard`.

**Output (excerpt):**
```
Assessment trend: rising sedation + declining respiratory effort over two checks (times per record), then sat trend down.
Actions + times: stimulated/positioned/O2 @ t1 → minimal change; escalated + prepared reversal @ t2; reversal given per order @ t3 → effort improved on reassessment @ t4 (times per record).
Notification: notified provider by role @ t2; SBAR headline "over-sedated, hypoventilating post-op, supporting and requesting reversal"; verbal order for reversal received and given per order.
Facts-not-conclusions: wrote "decreased responsiveness and respiratory effort," not "patient overdosed."
Completeness sweep: all five anchors present.
Coaching point: your record is complete — tighten the notification time; in the event you nearly charted it after the reassessment, log the notify-time as it happens.
```

> Safety reminder: A rehearsal only — chart in your real EHR per facility policy, contemporaneously where possible, facts not conclusions. Escalate real concerns by role.
