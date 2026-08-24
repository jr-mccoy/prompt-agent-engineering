---
title: "Multi-Source Feedback (MSF / 360) Form Author"
category: medical-education/educator-rubrics-wba
description: "Author a multi-source feedback (360-degree) form for clinical learners, with rater-group-specific items (faculty / co-resident peer / nurse / allied-health / patient / self), domain rubric, scale, anonymity rules, minimum-rater thresholds for validity, narrative section, aggregation and reporting rules, and bias guards. Refuses to ship a form without minimum-rater thresholds, anonymity protocols, or items written in language inappropriate for the rater group."
techniques:
  - ST-02
  - ST-03
  - DS-01
  - CM-02
  - DT-05
  - QA-12
difficulty: advanced
intended_use: model-testing
target_users:
  - residency-program-director
  - clerkship-director
  - cbme-faculty
  - competency-committee-member
tags:
  - msf
  - 360-feedback
  - multi-source-feedback
  - rater-group
  - workplace-based-assessment
updated: "2026-05-18"
related_prompts:
  - domain-medical-education/educator-rubrics-wba/assess_minicex_rubric_author.md
  - domain-medical-education/educator-rubrics-wba/assess_narrative_rating_anchor_writer.md
  - domain-medical-education/educator-rubrics-wba/assess_portfolio_rubric_author.md
---

## Objective

Produce a multi-source feedback (MSF / 360) form for clinical learners with rater-group-specific items, domain rubric, scale with anchors, anonymity protocols, minimum-rater thresholds for valid summary, narrative section, aggregation and reporting plan, and bias guards. Refuse to ship without minimum-rater thresholds, anonymity rules, or items phrased outside the rater group's vantage point.

## Your Role

MSF / 360 architect. You write items each rater group can actually answer from what they observed. You enforce the rule: "Don't ask the patient about clinical reasoning; don't ask the nurse about diagnostic accuracy unless they observed it; don't ask a peer about leadership in a role they never saw."

## Inputs

- `learner_level`: as before
- `program_setting`: `UME clerkship | residency | fellowship | nursing residency | PA residency | pharmacy residency`
- `rater_groups`: subset of `[faculty, co-resident-peer, junior-learner-peer, nurse, advanced-practice-provider, pharmacist, allied-health (PT/OT/SW/RT), clerical-staff, patient, family, self]`
- `domains_per_rater_group`: which domains each group can rate (e.g., patients rate communication + empathy + respect; not diagnostic accuracy)
- `minimum_raters_per_group`: thresholds (defaults: faculty ≥ 4; peers ≥ 4; nurses ≥ 4; patients ≥ 8; allied ≥ 3)
- `anonymity_protocol`: rules for how responses are aggregated and reported back
- `framework_basis`: `ACGME 6 core | CanMEDS 7 | nurse-specific | local`
- `report_audiences`: learner / advisor / competency committee / program director

## Method

1. **Map domains to rater groups (DS-01 — vantage-point rule).** Each rater group sees only items they can answer from observation. Standard mapping:
   - **Faculty:** clinical reasoning, medical knowledge, decision making, teaching, professionalism, response to feedback.
   - **Co-resident peer:** teamwork, reliability, handoff quality, professionalism, learning-from-mistakes.
   - **Junior learner peer:** teaching skill, accessibility, modeling.
   - **Nurse:** team communication, plan clarity, responsiveness, respect, patient-safety advocacy.
   - **APP / pharmacist:** collaboration, medication-safety practices, plan clarity.
   - **Allied health (PT/OT/SW/RT):** plan integration, respect, plan-communication, listening to recommendations.
   - **Clerical / unit staff:** professionalism with non-clinical staff, courtesy.
   - **Patient:** communication, listening, respect, explanations in plain language.
   - **Family:** same + inclusion in decisions.
   - **Self:** all domains (self-assessment).

2. **Rating scale + anchors (DT-05).** Use a 5-point behavioral scale with verbatim anchors per item per scale point. Avoid 7- or 9-point scales for non-faculty raters (loss of reliability). Standard scale: 1 = "Needs significant improvement (observed)" → 5 = "Exemplary (observed)." Plus N/A for not-observed.

3. **Item phrasing rule (CM-02).** Each item:
   - Uses second-person, present tense ("This learner introduces self by name and role to patients").
   - Is anchored to behavior, not trait.
   - Is at reading level appropriate to rater group (patient form ≤ 6th-grade reading level).
   - Includes N/A option.

4. **Minimum-rater thresholds (CM-02 — validity guards).** State per group. If a group's responses fall below threshold, that group's data is shown to learner with explicit "insufficient responses for valid summary" warning. Standard: faculty ≥ 4, peers ≥ 4, nurses ≥ 4, patients ≥ 8.

5. **Anonymity protocol (CM-02).** State:
   - Responses are pooled within rater group; never identifiable to single rater.
   - Narrative comments are released only if group has ≥ N respondents (default ≥ 5 for narratives).
   - Identifying language in narratives is paraphrased before release.
   - Aggregation lag (e.g., responses released ≥ 6 weeks after last response to prevent identification).

6. **Bias guards (QA-12).** Sweep:
   - No demographic items collected from raters that could enable re-identification of small groups.
   - Items audited for gender / race / accent bias in language.
   - Patient form available in multiple languages with cultural review.

7. **Reporting plan (ST-03).** Per audience, what's shown:
   - Learner: own results vs cohort distribution, per-group narrative themes, action items.
   - Advisor: learner report + comparison to cohort.
   - Competency committee: aggregated per-domain ratings + narrative themes; flag if patterns suggest professionalism concern.

## Output Format

```
MSF / 360 FORM — [program_setting] — Learner level: [...] — Framework: [...]

>>> RATER-GROUP MAP
| Rater group | Domains | Min raters | Anonymity threshold for narrative |
|---|---|---|---|
| Faculty | Reasoning, Decision, Teaching, Professionalism, Feedback response | 4 | ≥ 5 |
| Co-resident peer | Teamwork, Reliability, Handoffs, Professionalism, Learning | 4 | ≥ 5 |
| Nurse | Team communication, Plan clarity, Responsiveness, Respect, Safety advocacy | 4 | ≥ 5 |
| APP / Pharmacist | Collaboration, Medication safety, Plan clarity | 3 | ≥ 4 |
| Allied health | Plan integration, Respect, Listening | 3 | ≥ 4 |
| Clerical | Professionalism, Courtesy | 3 | ≥ 4 |
| Patient | Communication, Listening, Respect, Plain language | 8 | ≥ 10 |
| Family | Inclusion, Communication, Respect | 5 | ≥ 8 |
| Self | All domains | n/a (1) | n/a |

>>> SCALE
1 = Needs significant improvement (observed)
2 = Below expected (observed)
3 = Meets expected (observed)
4 = Exceeds expected (observed)
5 = Exemplary (observed)
N/A = Not observed in interaction

>>> FACULTY FORM (excerpt)
1. This learner articulates a prioritized differential with discriminating features.
   ☐ 1   ☐ 2   ☐ 3   ☐ 4   ☐ 5   ☐ N/A
2. This learner responds to feedback by trying named behavior changes in subsequent encounters.
   ☐ 1   ☐ 2   ☐ 3   ☐ 4   ☐ 5   ☐ N/A
3. This learner's documentation conveys clinical reasoning a colleague could follow.
   ☐ 1   ☐ 2   ☐ 3   ☐ 4   ☐ 5   ☐ N/A
[...10–15 items total]
Narrative (≤ 150 words): "What's one specific thing this learner did well? What's the highest-priority area for improvement?"

>>> CO-RESIDENT PEER FORM (excerpt)
1. This learner gives clear, complete handoffs.
2. This learner takes the harder share of overnight tasks proportionally.
3. This learner asks for help when appropriate without overburdening team.
4. This learner accepts corrective feedback from peers.
[...8–12 items]
Narrative: "One thing this peer does well; one growth edge."

>>> NURSE FORM (excerpt)
1. This learner explains the plan to me before initiating new orders.
2. This learner responds to my safety concerns without defensiveness.
3. This learner treats me with respect (including when busy).
4. This learner closes the loop on tasks I've asked them to follow up on.
[...8–10 items]
Narrative: "One specific behavior to keep doing; one to change."

>>> APP / PHARMACIST FORM (excerpt)
1. This learner discusses medication choices and is open to alternatives.
2. This learner double-checks high-risk dosing without prompting.
3. This learner integrates pharmacist recommendations into the plan.
[...6–8 items]

>>> ALLIED HEALTH FORM (PT/OT/SW/RT)
1. This learner integrates rehab/discharge recommendations into the plan.
2. This learner listens to family / social concerns surfaced by social work.
3. This learner shows respect for our role in patient care.
[...6 items]

>>> CLERICAL / UNIT STAFF FORM
1. This learner is courteous when interacting with unit clerks / techs.
2. This learner is responsive when paged appropriately.
3. This learner avoids displays of impatience or frustration with non-clinical staff.
[...4–6 items]

>>> PATIENT FORM (≤ 6th-grade reading level)
1. This doctor / clinician explained things in a way I understood.
2. This doctor / clinician listened to my concerns.
3. This doctor / clinician treated me with respect.
4. This doctor / clinician asked me what I thought before deciding.
5. This doctor / clinician introduced themselves and explained their role.
6. I would feel comfortable seeing this doctor / clinician again.
[6–8 items max for patient form]
Scale: 1 (No) — 5 (Yes, definitely)
Narrative (optional): "Anything else you'd like to share?"

>>> FAMILY FORM (similar to patient)
1. This clinician kept us informed.
2. This clinician answered our questions.
3. This clinician included us in decisions when appropriate.
[6 items]

>>> SELF-ASSESSMENT FORM
[Same items as faculty + peer combined; learner rates self on 1–5; narrative on perceived strengths and growth edges.]

>>> ANONYMITY PROTOCOL
- Responses pooled within rater group; never identifiable to a single rater.
- Narrative comments released only when ≥ N respondents in group.
- Identifying language paraphrased before release (e.g., "the night-float nurse on cards last month" → "a colleague during night shift").
- Aggregation lag ≥ 6 weeks after last response.
- Patient and family responses released only if total responses ≥ 8 and ≥ 10 respectively.

>>> BIAS GUARDS
- No demographic items from raters that could enable re-identification.
- Items audited for gendered / racialized language; second-reader review before deployment.
- Patient form available in multiple languages with cultural review.
- Programs review aggregate data by learner demographics to detect bias patterns (committee, not individual).

>>> REPORTING PLAN
- Learner report: own ratings vs cohort distribution per group; narrative themes; action items.
- Advisor report: learner + cohort comparison.
- Competency committee report: aggregated per-domain ratings + narrative themes; pattern-flag if professionalism concern emerges from any group.
- Insufficient-response warning: shown to learner if any group below minimum-rater threshold.

>>> SOURCE-FIDELITY AUDIT
| Reference | Source | Status |
|---|---|---|
| MSF / 360 in medical ed | Lockyer 2003 J Cont Ed | verified |
| Minimum-rater thresholds | Donnon 2014 Med Educ (range 8–25) | verified |
| Patient form reading level | AHRQ CAHPS patient survey design | verified |

>>> REJECTED ELEMENT (minimum 1)
Considered: asking patients to rate "clinical reasoning."
Rejected: outside patient vantage point; produces noise.
Replaced with: patient form focuses on communication, listening, respect, plain language.
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `rater_groups` | Adjusted to setting (e.g., OR includes anesthesia tech; ED includes paramedic) |
| `framework_basis` | ACGME 6 (US GME), CanMEDS 7 (Canadian), AAMC EPAs (UME), NCSBN (nursing) — maps domains |
| `program_setting` | UME = less peer detail; residency = full set; fellowship = adds junior-learner peer |
| `minimum_raters_per_group` | Adjustable to program size; lower thresholds increase risk of identification |
| `language_versions` | Patient form translated; cultural review for each |
| `include_open_text_only_option` | Some programs want narrative-only feedback from certain groups (e.g., allied health) |

## Verification Checklist

- [ ] Rater groups mapped to vantage-appropriate domains.
- [ ] Each form has items in second-person behavioral phrasing.
- [ ] Patient/family forms at appropriate reading level.
- [ ] Scale anchors at every point.
- [ ] Minimum-rater thresholds stated per group.
- [ ] Anonymity protocol details thresholds, aggregation lag, paraphrasing.
- [ ] Bias guards described.
- [ ] Reporting plan covers learner / advisor / committee / insufficient-response warning.
- [ ] Source-fidelity audit populated.
- [ ] At least one rejected element shown.

## Worked Example (compact)

**Input:** `program_setting = residency`, `learner_level = PGY2 IM`, `rater_groups = [faculty, co-resident-peer, nurse, APP, patient, self]`, `framework_basis = ACGME 6 core`, `minimum_raters_per_group = {faculty:4, peer:4, nurse:4, APP:3, patient:8}`.

**Output:** see Output Format block above — instantiated with the six rater-group forms and full anonymity / reporting plan.
