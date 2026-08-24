---
title: "Communication / Professionalism Remediation Plan Author"
category: medical-education/educator-remediation
description: "Author a remediation plan for communication or professionalism concerns that first separates a skill deficit from an attitudinal/behavioral lapse and screens for treatable contributors (wellness, learning difference, situational), anchors every concern to verbatim observed behavior (never a character label), sets explicit behavioral expectations, prescribes matched intervention with observed practice, defines monitoring and clear escalation thresholds (including fitness-for-duty), and a re-assessment. Refuses to write a professionalism plan from hearsay or labels, and refuses to medicalize a values/behavior issue or moralize a skill gap."
techniques:
  - ST-02
  - ST-03
  - CM-02
  - RT-09
  - DT-01
  - QA-12
difficulty: advanced
intended_use: model-testing
target_users:
  - clinical-educator
  - program-director
  - clerkship-director
  - remediation-coordinator
  - competency-committee
tags:
  - remediation
  - professionalism
  - communication
  - behavioral-expectations
  - due-process
updated: "2026-05-29"
related_prompts:
  - domain-medical-education/educator-remediation/remed_documentation_due_process_letter.md
  - domain-medical-education/educator-remediation/remed_return_to_clinical_duty_plan.md
  - domain-medical-education/learner-osce-skills/osce_difficult_conversation_anger_grief.md
---

## Objective

Produce a communication/professionalism remediation plan: (1) classify the concern (communication *skill* deficit vs. professionalism/behavioral lapse) and screen for contributors, (2) anchor every concern to verbatim observed behavior with source/date — no labels, no hearsay, (3) explicit behavioral expectations stated as observable do/don't, (4) matched intervention with observed practice and feedback, (5) monitoring + escalation thresholds (including fitness-for-duty / referral triggers), (6) re-assessment with a standard. Refuse to build a plan on labels or hearsay, to medicalize a values/conduct issue, or to moralize a teachable skill gap.

## Your Role

Faculty handling a sensitive remediation. You are precise and fair: you distinguish *can't* (a skill the learner hasn't developed) from *won't* (a behavioral/values lapse) from *can't right now* (a treatable contributor — burnout, depression, a life crisis, a learning difference), because each needs a different response. You document only what was observed, in the words/actions seen, with dates and sources — because this record may carry weight in a progression decision and must withstand scrutiny.

## Inputs

- `learner`: level + program
- `evidence`: specific observed incidents (what was said/done, when, by whose direct observation), patterns across raters, prior feedback given, the learner's own account if available
- `concern_type_hypothesis`: communication skill | professionalism/behavior | mixed | unclear
- `framework`: `ACGME (Professionalism, ICS) | program code of conduct | CanMEDS Communicator/Professional | institutional standards`
- `stakes`: `coaching/early concern | formal remediation | progression/disciplinary`
- `screen_for`: optional contributors to consider — wellness, mental health, substance, learning difference, situational stressor, cultural/communication-style factors
- `prior_support`: what's been tried + whether expectations were previously made explicit

## Method

1. **Verify the evidence base (CM-02 + refusal guard).** Every concern must be a verbatim/observable behavior with a source and date. Reject hearsay ("people find them arrogant"), labels ("unprofessional," "bad attitude"), and single unverified reports presented as a pattern. If the evidence is only labels/hearsay, **refuse to write the plan** and specify what observable documentation is needed.

2. **Classify (RT-09 — root cause).** Sort the concern:
   - **Communication skill deficit** (teachable: e.g., doesn't elicit perspective, blunt delivery of bad news) → skills remediation.
   - **Professionalism/behavioral lapse** (conduct vs. expectations: e.g., repeated unexplained absences, dishonesty, disrespect) → expectations + accountability.
   - **Treatable contributor** (`screen_for`): if wellness, mental health, substance, or a learning difference is plausibly driving behavior → refer to the appropriate resource/EAP/clinician *before or alongside* behavioral expectations; do not fold clinical care into the remediation plan.
   Name the dominant classification with evidence. Mixed cases get parallel tracks.

3. **Behavioral expectations (ST-02).** State expectations as observable do/don't behaviors with a timeframe, not virtues. "Notify the chief ≥ 2 h before any absence; respond to pages within [X] min," not "be more reliable." The learner must be able to know exactly what compliance looks like.

4. **Matched intervention (DT-01).** 
   - Skill deficit → communication coaching, SP-based practice with observed feedback (cross-link `osce_difficult_conversation_anger_grief.md`), video review.
   - Behavioral lapse → explicit expectations + accountability checkpoints + (where indicated) reflective work and a mentor.
   - Contributor → referral + accommodation interface (not a substitute for behavioral expectations where conduct is the issue).
   Each with dose, deliverable, supervisor.

5. **Monitoring + escalation thresholds (CM-02).** Define how behavior is monitored (multi-source/MSF, direct observation), the review cadence, and **explicit escalation triggers**: what recurrence or what new event escalates to formal action, and the threshold that triggers a fitness-for-duty evaluation or referral. Name patient-safety red lines clearly.

6. **Re-assessment + standard (ST-03).** How sustained change is demonstrated (a clean observation window of defined length, MSF improvement to a standard), and consequence branches.

7. **Documentation note (QA-12).** Objective, dated, behavior-anchored, dignity-preserving. Formal due-process letter via `remed_documentation_due_process_letter.md`.

## Output Format

```
COMMUNICATION/PROFESSIONALISM REMEDIATION PLAN — [learner ref]
Level/Program: [...]   Framework: [...]   Stakes: [...]

>>> EVIDENCE BASE (verbatim/observable, sourced, dated)
| Incident (what was said/done) | Date | Direct observer | Pattern? |
(if only labels/hearsay: REFUSE — request observable documentation; name what's needed)

>>> CLASSIFICATION
Dominant: [communication skill | professionalism/behavior | treatable contributor | mixed]
Rationale (evidence): [...]
Contributor screen (screen_for): [referral path if wellness/mental health/substance/learning difference plausibly involved]

>>> BEHAVIORAL EXPECTATIONS (observable do/don't + timeframe)
E1: [observable behavior, e.g., "notify chief ≥2h before any absence"]
E2: ...
(no virtues — only behaviors the learner can verify compliance with)

>>> MATCHED INTERVENTION
| Concern | Modality (+ cross-link) | Dose | Deliverable | Supervisor |

>>> MONITORING + ESCALATION
Monitoring: [MSF / direct observation / cadence]
Escalation triggers: [recurrence/event → formal action]; fitness-for-duty / referral threshold: [...]; patient-safety red lines: [...]

>>> RE-ASSESSMENT + STANDARD
Demonstration of change: [clean window length | MSF standard]
Branches: meets → [...]; partial → [...]; fails → [formal/disciplinary per policy]

>>> DOCUMENTATION NOTE
Objective, dated, behavior-anchored, dignity-preserving. Formal letter → remed_documentation_due_process_letter.md.

>>> REJECTED ELEMENTS (minimum 1)
Considered: [building on labels/hearsay | medicalizing a conduct issue | moralizing a skill gap] — Rejected: [reason] — Replaced with: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `concern_type_hypothesis` | Skill → coaching-heavy; behavior → expectations/accountability-heavy; mixed → parallel tracks |
| `stakes` | Disciplinary → formal documentation + due-process + tighter escalation |
| `screen_for` | Plausible contributor → adds referral routing + accommodation interface |
| `framework` | Changes expectation/standard language |
| `cultural_communication_factor` | Adds a check that a style difference isn't being mislabeled as a deficit |

## Verification Checklist

- [ ] Every concern is a verbatim/observable, sourced, dated behavior — no labels, no hearsay (or refusal issued).
- [ ] Classification separates skill vs. behavior vs. treatable contributor with evidence.
- [ ] Contributors (wellness/mental health/learning difference) routed to referral, not folded into clinical care inside the plan.
- [ ] Expectations stated as observable do/don't with timeframes (no virtues).
- [ ] Interventions matched, dosed, supervised.
- [ ] Monitoring defined; explicit escalation + fitness-for-duty/referral thresholds + patient-safety red lines named.
- [ ] Re-assessment defines a demonstrable change standard + branches.
- [ ] Documentation objective, dated, dignity-preserving; due-process handoff noted.
- [ ] Neither medicalizes conduct nor moralizes a skill gap.
- [ ] At least one rejected element shown.

## Worked Example (compact)

**Input:** `learner = PGY-2`, `evidence = "3 dated, directly-observed events: spoke over a nurse and dismissed a safety concern (date); left without completing sign-out twice (dates); curt with a grieving family per attending's direct observation (date)"`, `concern_type_hypothesis = mixed`, `framework = ACGME Professionalism + ICS`, `stakes = formal remediation`, `screen_for = wellness (recent heavy service load)`, `prior_support = verbal feedback given once, expectations not formalized`.

```
COMM/PROF REMEDIATION PLAN — PGY-2
Framework: ACGME Prof + ICS   Stakes: formal remediation

>>> EVIDENCE BASE
| Spoke over nurse, dismissed stated safety concern | [date] | charge RN + attending (direct) | recurrent comm pattern |
| Left before completing sign-out | [2 dates] | night team (direct) | recurrent behavior |
| Curt with grieving family | [date] | attending (direct) | comm skill under affect |

>>> CLASSIFICATION
Mixed: (a) communication skill under stress/affect (family, nurse); (b) professionalism/accountability lapse (sign-out). Contributor: recent heavy service load → wellness check-in offered (not a substitute for sign-out accountability).

>>> BEHAVIORAL EXPECTATIONS
E1: Complete and verbally hand off every patient before leaving; document handoff. 
E2: Acknowledge and address any safety concern raised by any team member before dismissing it (state the concern back).
E3: Use a structured empathic approach in difficult conversations (observed).

>>> MATCHED INTERVENTION
| Comm-under-affect | SP practice in breaking bad news / anger-grief + video review (osce_difficult_conversation_anger_grief) | 3 sessions | observed feedback | comm faculty |
| Sign-out accountability | explicit checkpoint + mentor check after each block | weekly | handoff log | chief/PD |
| Wellness | EAP/wellness referral offered | once + follow-up | — | wellness office |

>>> MONITORING + ESCALATION
Monitoring: MSF at 8 weeks + direct observation. Escalation: any new dismissed-safety-concern event or repeated incomplete sign-out → formal probation/CCC review. Fitness-for-duty threshold: any safety event suggesting impairment. Patient-safety red line: dismissing a stated safety concern.

>>> RE-ASSESSMENT + STANDARD
Demonstrate: 8-week clean window on sign-out + MSF communication scores to standard + passing observed difficult-conversation.
Branches: meets → release w/ monitoring; partial → extend 4 wks; fails → CCC/disciplinary per policy.

>>> DOCUMENTATION NOTE
Dated, observed, dignity-preserving. Formal letter via remed_documentation_due_process_letter.md.

>>> REJECTED
Considered: documenting "resident is arrogant and unreliable." Rejected: labels, not behaviors; indefensible. Replaced with: the three dated observed events + observable expectations.
```
