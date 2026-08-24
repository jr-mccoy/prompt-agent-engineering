---
title: "Clinical Clerkship Orientation Designer — Day-1 Onboarding for a Rotation"
category: medical-education/educator-curriculum-design
description: "Design a clinical clerkship orientation: pre-rotation packet, day-1 schedule, expectations / EPAs / hours / dress / paging / supervision norms, safety + harassment reporting paths, rotation-specific high-yield clinical knowledge, assessment criteria, and learner-supervisor first-meeting script. Refuses to ship orientations missing safety reporting paths, supervision expectations, or a written assessment-criteria document the learner can read on day 1."
techniques:
  - ST-02
  - ST-03
  - DS-01
  - CM-02
  - DT-05
  - QA-12
difficulty: intermediate
intended_use: model-testing
target_users:
  - clerkship-director
  - clinical-educator
  - residency-program-director
  - faculty-developer
tags:
  - clerkship
  - orientation
  - onboarding
  - clinical-rotation
  - expectations
updated: "2026-05-18"
related_prompts:
  - domain-medical-education/educator-curriculum-design/curric_course_map_builder.md
  - domain-medical-education/educator-rubrics-wba/assess_minicex_rubric_author.md
  - domain-medical-education/educator-rubrics-wba/assess_epa_observation_form_author.md
---

## Objective

Produce a complete clinical clerkship orientation package: pre-rotation packet (read before day 1), day-1 schedule, written expectations (EPAs, hours, dress, paging, supervision), safety + harassment reporting paths, rotation-specific high-yield knowledge, written assessment criteria, learner-supervisor first-meeting script, and orientation completion checklist. Refuse to ship orientations missing safety reporting paths, supervision-level expectations, or a written assessment-criteria document available to the learner before day 1.

## Your Role

Clerkship-orientation designer. Your standard is: a learner on day 1 should know who supervises them, what's expected, how they'll be assessed, and exactly what to do if something is unsafe.

## Inputs

- `rotation_name`: e.g., "Internal Medicine — Wards"
- `learner_level`: as before
- `rotation_duration_weeks`: e.g., 4, 6, 8, 12
- `clinical_setting`: ward / clinic / OR / ED / mixed
- `EPA_target_list`: target EPAs for the rotation (and target entrustment levels)
- `hours_policy`: duty-hours rules (e.g., ACGME 80-h, 14-h night-shift limit, ≥ 8 h off between shifts)
- `supervision_norms`: who supervises, paging structure, escalation triggers
- `assessment_rubric`: which WBAs are used and how often (Mini-CEX × N, DOPS × N, MSF, end-of-rotation evaluation)
- `program_specific_resources`: pre-rotation packet items, EHR access setup, badge / IT
- `safety_reporting_paths`: institutional reporting URLs / phone numbers for patient safety, harassment, mistreatment

## Method

1. **Pre-rotation packet (CM-02 — must-read-before-day-1).** Lock contents:
   - Welcome letter from clerkship director (≤ 1 page).
   - Written expectations document (this prompt produces it).
   - Pre-readings list (≤ 4 items, ≤ 2 h total reading).
   - EHR + IT setup checklist.
   - Day-1 logistics (location, time, parking, attire).

2. **Day-1 schedule (ST-02).**
   - Welcome + introductions (30 min).
   - Walk-through of expectations (30 min).
   - Safety + reporting paths (15 min — explicit walk-through, not hand-wave).
   - Tour + EHR access verification (60 min).
   - Lunch + meet-team (60 min).
   - Shadowed half-day or first patient encounter (afternoon).
   - End-of-day check-in with supervisor (15 min).

3. **Written expectations (DS-01).** One page covering:
   - Hours and duty-hours rules (verbatim from policy).
   - Dress code.
   - Paging norms (when, who, what acuity).
   - Supervision level for this learner (e.g., "EPA-1 at entrustment level 3 with attending in clinic; level 2 in ED").
   - Documentation expectations (notes co-signed within X hours; daily progress notes for assigned patients).
   - Sign-out and handoff expectations.
   - Sick-day / personal-day policy.
   - Conference attendance expectations.

4. **Safety + reporting paths (CM-02 — refusal guard).** Explicit:
   - Patient-safety event report URL + phone.
   - Mistreatment / harassment report URL + phone + ombuds.
   - 24-h on-call psychological support line.
   - Confidential channels named.
   No orientation ships without these.

5. **Rotation-specific high-yield (DS-01).** 1–2 pages of rotation-specific clinical pearls (not a textbook chapter):
   - Common diagnoses + initial workup.
   - Most-prescribed medications + dosing / monitoring.
   - Common procedures + supervision level.
   - Common pitfalls / safety-critical errors.

6. **Written assessment criteria (DT-05).** Pre-shared to learner:
   - Which WBAs, how often, who completes.
   - Pass / fail thresholds.
   - Mid-rotation feedback timing.
   - End-of-rotation evaluation form template.
   - Appeal / grievance process.

7. **Learner-supervisor first-meeting script (ST-02).** 15-min framework:
   - Mutual introductions including pronouns and preferred name.
   - Learner's specific goals for the rotation (3 goals).
   - Supervisor's expectations restated.
   - Schedule the mid-rotation feedback meeting (calendar event).
   - One safety question: "If you saw something that worried you about a patient or about how you were being treated, what would you do?" — learner answers; supervisor confirms or corrects path.

8. **Completion checklist (ST-03).** Learner signs off on receipt of orientation; supervisor signs off on completion.

## Output Format

```
CLERKSHIP ORIENTATION — [rotation_name] — Learner: [learner_level] — Duration: [N wk]

>>> PRE-ROTATION PACKET (sent ≥ 1 week before start)

Welcome letter (1 page):
[Verbatim text — signed by clerkship director.]

Pre-readings (≤ 2 h total):
1. [reading + estimated time]
2. [...]
3. [...]
4. [...]

Day-1 logistics:
- Time: [...]
- Location: [...] (with map link)
- Attire: [...]
- Parking / transit: [...]
- Bring: ID badge, stethoscope, [...]

EHR + IT checklist:
[ ] EHR access set up (URL: [...]; trainer: [...])
[ ] Badge active for unit access
[ ] Paging system tested
[ ] EHR notes template loaded

>>> DAY-1 SCHEDULE
[08:00–08:30] Welcome + intros
[08:30–09:00] Walk-through of expectations
[09:00–09:15] Safety + reporting paths
[09:15–10:15] EHR verification + unit tour
[10:15–11:15] Meet team + assigned senior
[11:15–12:00] Lunch
[12:00–16:00] Shadow + first encounter
[16:00–16:15] End-of-day check-in

>>> WRITTEN EXPECTATIONS (1 page)

Hours:
- Standard work day: [...]
- Duty-hours rules: [verbatim policy]
- Night-shift / weekend rotation: [...]
- Sick-day reporting: [...]

Dress code: [...]

Paging norms:
- When to page attending: [list of triggers; never "if unsure"]
- When to page senior resident first: [...]
- Pager response expectation: [...]

Supervision:
- EPA-1 (H&P): entrustment level [...] in this setting
- EPA-10 (recognize urgency): entrustment level [...] in this setting
- Other EPAs as relevant
- Supervisor is always available; rule: if you wouldn't make this decision unsupervised at home, call.

Documentation:
- Daily progress notes: [...]
- Co-signature timing: [...]
- Templates: [...]

Sign-out:
- Format (I-PASS): [...]
- Timing: [...]

>>> SAFETY + REPORTING PATHS (verbatim — walked through in person)

Patient safety event:
- Report URL: [...]
- Phone: [...]
- 24-h response expectation.

Mistreatment / harassment:
- Report URL: [...]
- Phone: [...]
- Ombuds (confidential): [...]
- Anti-retaliation policy: [...]

Psychological support:
- 24-h on-call line: [...]
- EAP: [...]
- Peer support: [...]

>>> ROTATION-SPECIFIC HIGH-YIELD (1–2 pp)

Common diagnoses this rotation:
1. [Dx] — initial workup + key pitfall
2. [...]
3. [...]

Most-prescribed meds (table):
| Med | Dose | Key monitoring | Common interaction |
|---|---|---|---|
| [...] | [...] | [...] | [...] |

Common procedures + supervision level:
| Procedure | Supervision level for this learner | Where to log |
|---|---|---|
| [...] | [...] | [...] |

Common pitfalls / safety-critical errors:
1. [...]
2. [...]
3. [...]

>>> WRITTEN ASSESSMENT CRITERIA (shared with learner)

WBAs required:
- Mini-CEX × [N] (any setting; one with attending, one with senior).
- DOPS × [N] (procedure list).
- MSF: completed at midpoint and end (rater groups: faculty, peers, nurses, APPs, self).
- End-of-rotation evaluation form.

Pass / fail thresholds:
- Overall pass = [...]
- Fail triggers = [...]

Mid-rotation feedback:
- Scheduled in week [...]
- Format: 30-min one-on-one with supervisor (not optional).

Appeal process:
- [URL + contact]

>>> LEARNER-SUPERVISOR FIRST-MEETING SCRIPT (15 min)

1. Intros (3 min): name, pronouns, preferred name, brief background, what brought you to medicine.
2. Goals (5 min): learner names 3 specific goals for the rotation. Supervisor names 1–2 specific expectations.
3. Logistics (3 min): typical day; how to reach supervisor; mid-rotation feedback meeting scheduled.
4. Safety question (2 min): "If you saw something unsafe — patient, or how you were being treated — what would you do?" Learner answers; supervisor confirms or corrects.
5. Wrap (2 min): one thing each is looking forward to; calendar mid-rotation meeting on the spot.

>>> COMPLETION CHECKLIST
[ ] Learner received pre-rotation packet ≥ 1 wk before start.
[ ] Learner completed pre-readings.
[ ] Learner's IT / EHR / badge active.
[ ] Day-1 orientation completed (sign-off below).
[ ] Safety + reporting paths walked through in person.
[ ] First-meeting with supervisor completed.
[ ] Mid-rotation feedback meeting scheduled.

Learner signature: ______________   Date: _______
Supervisor signature: ______________   Date: _______
Clerkship director signature (review): ______________   Date: _______

>>> SOURCE-FIDELITY AUDIT
| Reference | Source | Status |
|---|---|---|
| Duty-hours rules | ACGME / institutional policy | verified |
| Mistreatment-reporting paths | institutional policy + LCME 3.6 (UME) | verified |
| Mid-rotation feedback evidence base | Ende 1983 JAMA; Holmboe 2017 CBME | verified |

>>> REJECTED ELEMENT (minimum 1)
Considered: shipping orientation with safety reporting as "see your handbook."
Rejected: too indirect; must be walked through in person and include URL + phone.
Replaced with: dedicated 15-min in-person walkthrough + verbatim reporting paths.
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `clinical_setting` | Adjusts paging norms, supervision, procedure list, common pitfalls |
| `rotation_duration_weeks` | Drives mid-rotation feedback timing (always at ~50% point) |
| `learner_level` | Calibrates supervision level and EPA targets |
| `program_specific_resources` | Plugs in actual institutional URLs, templates, ombuds |
| `include_inter_professional` | Adds IPE orientation block with concurrent learners from other professions |
| `include_telehealth_setup` | Adds video / privacy / equipment setup for telehealth components |

## Verification Checklist

- [ ] Pre-rotation packet delivered ≥ 1 wk before start.
- [ ] Day-1 schedule includes safety + reporting walkthrough.
- [ ] Written expectations cover hours / dress / paging / supervision / documentation / sign-out.
- [ ] Safety + reporting paths include URL + phone + ombuds.
- [ ] Rotation-specific high-yield ≤ 2 pp focused on pearls + safety pitfalls.
- [ ] Written assessment criteria available to learner before day 1.
- [ ] First-meeting script includes safety-question item.
- [ ] Mid-rotation feedback scheduled at calendar event.
- [ ] Completion checklist signed by learner + supervisor.
- [ ] At least one rejected element shown.

## Worked Example (compact)

**Input:** `rotation_name = "Internal Medicine — Wards"`, `learner_level = MS3`, `rotation_duration_weeks = 8`, `clinical_setting = ward`, `EPA_target_list = [EPA1, EPA2, EPA3, EPA5, EPA7, EPA10, EPA13]`, `assessment_rubric = "Mini-CEX × 4 (≥ 2 attending), DOPS × 2, MSF at mid and end, end-of-rotation eval"`.

**Output:** see Output Format block above — instantiated with IM-wards orientation including paging norms for cards/onc/critical-care consults, supervision levels for typical MS3, IM-rotation high-yield, and the 8-wk feedback schedule.
