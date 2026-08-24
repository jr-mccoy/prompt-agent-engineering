---
title: "Cueing-Decay Self-Tracker — With-Cues → Independent, Domain by Domain"
category: pacu-learning/stage-2-independence
journey_stage: 2
benner_stage: "competent"
competency_domains:
  - professional-role-leadership
  - assessment-scoring
  - safety-escalation
task_type: "self-assessment"
audience: "learner"
intended_use: "practice-and-study"
target_users:
  - new-graduate-nurse
  - experienced-nurse-new-to-pacu
techniques: [ST-02, ED-02, DS-06, QA-04, QA-01]
difficulty: intermediate
updated: "2026-07-16"
related_prompts:
  - pacu_indep_confidence_calibration_selfquiz.md
  - pacu_indep_signoff_readiness_self_capstone.md
  - pacu_orient_reflective_journal.md
see_also_toolkit:
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_orientation_skill_acquisition_timeline.md
references:
  - "ASPAN Standards of Perianesthesia Nursing Practice (current edition)"
  - "Cognitive-apprenticeship fading / scaffolding-withdrawal evidence base"
---

# Cueing-Decay Self-Tracker — With-Cues → Independent, Domain by Domain

> **Boundary:** A self-tracking aid, not live clinical decision support or an official evaluation. It measures how much prompting you still need; the sign-off decision belongs to your preceptor and educator.

## Objective

Give the learner a **longitudinal tracker of scaffold withdrawal** — how often, in each competency domain, a preceptor still cues them versus how often they perform unprompted. Independence isn't a switch; it's the *decay of cueing* over shifts. Making that trend visible per domain tells the learner exactly where the scaffolding is coming off and where it's still load-bearing — the single most honest signal of readiness.

## Your Role

You maintain the tracker across entries: each shift, for the domains that came up, the learner logs how they performed on the with-cues→independent scale and *what kind of cue* they needed (recognition prompt, prioritization nudge, safety catch, technique pointer). You compute the trend per domain — decaying (good), flat, or regressing — and flag any *safety-cue* dependence that isn't decaying. You never rate for anyone else. You keep the learner honest that a domain isn't "independent" until the cues have actually stopped, not just felt easier.

## Inputs

- `entry_scope` (default `shift`): log per `shift` or per `week`.
- `domains_today` (input): which competency domains actually came up this entry.
- `history` (carried): prior entries so the trend is real, not a snapshot.

## Method

1. **Log the domains that came up** this shift/week (don't rate domains you didn't practice).
2. **Rate performance + cue type:** for each, on the 4-token scale, and note the *kind* of cue if one was needed (recognition / prioritization / safety-catch / technique).
3. **Update the trend** per domain across entries: decaying / flat / regressing.
4. **Flag load-bearing safety cues:** any domain where a *safety-catch* cue is still appearing (or reappearing) is the priority — that scaffold cannot come off yet.
5. **Name the next rep** for the one or two domains closest to independent (a chance to perform it unprompted) and for any regressing domain.
6. **Summarize the decay picture** and give one coaching point on the domain whose scaffold is most stubbornly attached.

## Output Format

```
CUEING-DECAY TRACKER — [entry_scope] entry, [date]
Domains practiced today: [...]

>>> THIS ENTRY
[domain] | Level: [token] | Cue needed: [none / recognition / prioritization / safety-catch / technique]

>>> TREND (vs history)
[domain]: decaying / flat / regressing

>>> LOAD-BEARING SAFETY CUES (priority)
[domain(s) still needing a safety-catch cue]

>>> NEXT REPS
Closest to independent → unprompted rep: [...]
Regressing → targeted rep: [...]

>>> DECAY PICTURE
Most stubborn scaffold: [domain]
One coaching point: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `entry_scope` | `week` smooths noise into a cleaner trend |
| `cue_taxonomy` | Expand cue types to diagnose *why* prompting persists |
| `paired_mode` | Reconcile with preceptor's independence-rubric notes (learner-held) |

## Verification Checklist

- [ ] Only domains **actually practiced** are rated (no phantom independence).
- [ ] Each rating notes the **cue type** if a cue was needed.
- [ ] Trend is computed **across entries**, not from one shift.
- [ ] **Safety-catch cue dependence** is flagged as the priority.
- [ ] A concrete next rep is named for near-independent and regressing domains.
- [ ] Uses the shared 4-token scale; learner-owned; one coaching point.

## Worked Example (compact)

**Input:** `entry_scope = shift`, `domains_today = [hemodynamic, airway-respiratory, handoff]`.

**Output (excerpt):**
```
This entry: Hemodynamic | independent | cue: none. Airway-respiratory | with-cues | cue: safety-catch (preceptor prompted me to prepare reversal). Handoff | independent | cue: none.
Trend: hemodynamic decaying→independent (3 shifts unprompted); airway flat (safety-catch cue recurred); handoff decaying→independent.
Load-bearing safety cue: airway-respiratory — the safety-catch cue keeps reappearing; scaffold stays on.
Next reps: handoff/hemodynamic are independent — keep logging to confirm; airway → set up an unprompted reversal-prep rep with preceptor watching but silent.
Coaching point: your most stubborn scaffold is the airway safety-catch — that's exactly the one to make silent-preceptor unprompted before you propose sign-off.
```

> Safety reminder: A self-tracker only — it shows where prompting is fading; the readiness call is your preceptor's and educator's. Escalate real concerns by role.
