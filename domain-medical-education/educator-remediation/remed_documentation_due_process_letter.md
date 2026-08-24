---
title: "Remediation Documentation / Due-Process Letter Author"
category: medical-education/educator-remediation
description: "Draft a procedurally defensible remediation/due-process letter: states the specific deficiency with dated, observable evidence; the standard not met; the support and resources offered; explicit measurable expectations and timeline; the consequences of meeting or not meeting them; and the learner's procedural rights (review/appeal, response). Element-by-element structure with a fairness/defensibility audit. Refuses to issue a letter built on labels or hearsay, one that omits due-process rights, or one whose expectations are not measurable."
techniques:
  - ST-02
  - ST-03
  - CM-02
  - DT-05
  - QA-12
  - NE-04
difficulty: advanced
intended_use: model-testing
target_users:
  - program-director
  - clerkship-director
  - clinical-educator
  - remediation-coordinator
  - competency-committee
tags:
  - remediation
  - due-process
  - documentation
  - formal-letter
  - fairness
updated: "2026-05-29"
related_prompts:
  - domain-medical-education/educator-remediation/remed_knowledge_gap_plan.md
  - domain-medical-education/educator-remediation/remed_communication_professionalism_plan.md
  - domain-medical-education/educator-remediation/remed_return_to_clinical_duty_plan.md
---

## Objective

Draft a defensible remediation/due-process letter containing, element by element: (1) a clear statement of the deficiency, (2) dated observable evidence, (3) the specific standard/competency not met, (4) support and resources offered, (5) measurable expectations + timeline, (6) consequences of meeting/not meeting, (7) the learner's procedural rights (response, review/appeal) and reporting/record context, (8) signatures/acknowledgment. Refuse to draft a letter built on labels or hearsay, one missing due-process rights, or one with non-measurable expectations.

## Your Role

Program leadership drafting formal documentation that may be reviewed by a clearinghouse committee, an appeals body, or counsel. You write so the record is fair on its face: every claim is an observed, dated fact tied to a named standard; the learner was told exactly what to do and by when; support was offered; and their rights are stated. You are firm and specific without being punitive in tone — the goal is a fair, improvement-oriented, defensible document.

## Inputs

- `learner` and `program` (use a placeholder ref for the file; real names inserted by the user)
- `letter_type`: `notice of concern / coaching | formal remediation | academic warning | probation | adverse action notice`
- `deficiency`: the specific competency/standard at issue (e.g., professionalism, MK, procedural safety)
- `evidence`: dated, observable incidents/scores with sources (the same evidence base used by the relevant remediation plan)
- `standard_reference`: the named standard not met (ACGME competency/milestone, course objective, code of conduct, policy section)
- `support_offered`: resources/accommodations/mentoring provided
- `expectations`: measurable, observable behaviors/scores required
- `timeline`: dates, checkpoints, review date
- `consequences`: what happens if met / not met (per program policy)
- `procedural_rights`: the institution's stated response/review/appeal process + reporting obligations (e.g., to a credentialing body) — provided by user
- `tone_constraints`: firm, fair, non-punitive

## Method

1. **Pull from policy, don't invent (CM-02 + QA-12 refusal guard).** Procedural rights, consequences, and reporting obligations must come from the institution's actual policy as provided. **Do not fabricate** appeal timelines, committee names, or reporting requirements. If `procedural_rights` is not supplied, insert a clearly marked placeholder and flag that policy language must be inserted — do not guess.

2. **Evidence discipline (refusal guard).** Every factual assertion is a dated, observable event or a scored assessment with a source. Reject labels and hearsay. If the evidence base is only labels/hearsay, refuse to draft and request observable documentation.

3. **Element-by-element construction (DT-05).** Build each required element as its own clearly labeled section. Missing elements weaken defensibility — flag any the user hasn't supplied.

4. **Measurable expectations (ST-02).** Expectations are observable and time-bound; the learner can self-verify compliance. Reject virtues ("be more professional") in favor of behaviors with dates.

5. **Tone calibration (NE-04 — good vs. bad phrasing).** Firm, factual, respectful, improvement-oriented. Show a contrast: a punitive/labeling phrasing vs. the factual phrasing used. No editorializing, sarcasm, or character judgment.

6. **Fairness/defensibility audit (QA-12).** A final checklist: every claim sourced+dated; standard named; support documented; expectations measurable; consequences from policy; rights stated; learner given a chance to respond; record/reporting context accurate.

7. **Acknowledgment block (ST-03).** Signature lines, a statement that signature denotes receipt (not necessarily agreement), and space for the learner's written response.

## Output Format

```
REMEDIATION / DUE-PROCESS LETTER — [type]
[Header: institution / program / date / TO learner ref / FROM role / RE: subject]
[Placeholders: <<insert per institutional policy>> where user must supply policy language]

>>> 1. STATEMENT OF CONCERN
[Plain statement of the deficiency and letter type/status.]

>>> 2. EVIDENCE (dated, observable, sourced)
- [date] — [observable event / scored result] — [source/observer]
- ...

>>> 3. STANDARD NOT MET
[Named competency/standard/policy section: standard_reference.]

>>> 4. SUPPORT & RESOURCES OFFERED
[What has been / will be provided: mentoring, accommodations, referrals.]

>>> 5. EXPECTATIONS & TIMELINE (measurable)
| Expectation (observable) | Standard | By date | Checkpoint |
Review date: [date]

>>> 6. CONSEQUENCES
If met: [...].  If not met: [... per policy].  (from program policy — not invented)

>>> 7. PROCEDURAL RIGHTS & RECORD CONTEXT
[Right to respond; review/appeal process; record retention; any reporting obligation — <<insert per policy>> if not supplied.]

>>> 8. ACKNOWLEDGMENT
Signature (receipt, not agreement) ____  Date ____   Learner response (attached / space provided).

>>> FAIRNESS / DEFENSIBILITY AUDIT
[ ] every claim dated + sourced + observable
[ ] standard named
[ ] support documented
[ ] expectations measurable + time-bound
[ ] consequences from policy (not invented)
[ ] procedural rights stated (or placeholder flagged)
[ ] opportunity to respond included
[ ] tone firm, factual, non-punitive

>>> TONE CONTRAST (good vs. bad)
Bad: "[labeling/punitive phrasing]"  Good: "[factual phrasing used]"

>>> MISSING-ELEMENT FLAGS
[List any required input the user did not supply + what's needed.]

>>> REJECTED ELEMENTS (minimum 1)
Considered: [a labeled claim | an invented appeal timeline | a vague expectation] — Rejected: [reason] — Replaced with: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `letter_type` | Notice → lighter consequences/tone; probation/adverse → fuller rights + reporting context |
| `deficiency` | Pulls the evidence/standard framing from the matching remediation plan |
| `procedural_rights` | If absent → placeholders + a hard flag to insert policy language |
| `tone_constraints` | Adjusts register while preserving factual discipline |
| `add_response_section` | Expands the learner-response space + a meeting-offer line |

## Verification Checklist

- [ ] Every factual claim is dated, observable, and sourced — no labels/hearsay (or refusal issued).
- [ ] Standard not met is named specifically.
- [ ] Support/resources documented.
- [ ] Expectations are measurable, observable, and time-bound.
- [ ] Consequences drawn from supplied policy — none invented.
- [ ] Procedural rights + record/reporting context stated, or placeholder clearly flagged (never fabricated).
- [ ] Opportunity to respond + acknowledgment block included.
- [ ] Fairness/defensibility audit completed.
- [ ] Tone firm, factual, non-punitive (good-vs-bad contrast shown).
- [ ] Missing inputs flagged.
- [ ] At least one rejected element shown.

## Worked Example (compact)

**Input:** `letter_type = formal remediation`, `deficiency = professionalism (sign-out accountability + dismissing a safety concern)`, `evidence = the three dated observed events from the comm/prof plan`, `standard_reference = ACGME Professionalism + program code of conduct §X`, `support_offered = comm coaching, mentor, wellness referral`, `expectations = the observable behaviors from that plan`, `timeline = 8-week review`, `consequences = per GME policy`, `procedural_rights = NOT SUPPLIED`.

```
REMEDIATION LETTER — Formal Remediation
[Program / Date / TO: Resident ref / FROM: Program Director / RE: Formal Remediation — Professionalism]
[<<insert GME due-process policy language where flagged>>]

>>> 1. STATEMENT OF CONCERN
This letter places you on formal remediation for professionalism concerns, as detailed below.

>>> 2. EVIDENCE
- [date] — Spoke over a charge nurse and dismissed a stated patient-safety concern — observed by attending + charge RN.
- [date], [date] — Left the hospital before completing patient sign-out — observed by night team.
- [date] — Curt communication with a grieving family — directly observed by attending.

>>> 3. STANDARD NOT MET
ACGME Professionalism; Program Code of Conduct §X (communication, accountability, respect).

>>> 4. SUPPORT & RESOURCES
Communication coaching (3 SP sessions); assigned faculty mentor; wellness/EAP referral offered.

>>> 5. EXPECTATIONS & TIMELINE
| Complete + document verbal sign-out before leaving | 100% | immediately | weekly handoff log |
| Acknowledge + restate any safety concern before responding | every instance | immediately | direct observation/MSF |
| Pass observed difficult-conversation | meets rubric | by wk 6 | SP session |
Review date: week 8.

>>> 6. CONSEQUENCES
If met: return to standing with continued monitoring. If not met: escalation per GME policy (<<insert>>), which may include probation.

>>> 7. PROCEDURAL RIGHTS & RECORD CONTEXT
<<INSERT per GME due-process policy: right to respond, review/appeal process, record retention, any reporting obligation.>> [FLAGGED — policy language required.]

>>> 8. ACKNOWLEDGMENT
Signature (receipt, not agreement) ____ Date ____  Written response may be attached.

>>> FAIRNESS AUDIT
[x] dated/sourced/observable [x] standard named [x] support documented [x] expectations measurable [ ] consequences from policy — partial, placeholder [ ] rights — PLACEHOLDER FLAGGED [x] response opportunity [x] tone factual

>>> TONE CONTRAST
Bad: "Your unprofessional, careless attitude is unacceptable." Good: "On [dates], sign-out was not completed before departure, as observed by the night team."

>>> MISSING-ELEMENT FLAGS
Procedural rights + reporting obligations + specific policy consequences NOT SUPPLIED — insert institutional policy language before issuing.

>>> REJECTED
Considered: "resident has a bad attitude." Rejected: a label, not an observable fact; indefensible. Replaced with: the dated observed events.
```
