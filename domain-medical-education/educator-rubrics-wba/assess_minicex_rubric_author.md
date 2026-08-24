---
title: "Mini-CEX Rubric Author (Mini Clinical Evaluation Exercise — Domains, Anchors, Narrative)"
category: medical-education/educator-rubrics-wba
description: "Author a Mini-CEX form with the 6 ABIM domains (history, physical exam, professionalism, clinical judgment, counseling, organization/efficiency, overall) plus a 9-point scale with verbatim behavioral anchors at unsatisfactory / satisfactory / superior bands. Output includes the form, anchor rationale, a forced-narrative section with stem prompts, and an inter-rater calibration appendix. Refuses to ship rubric levels described only by adjectives ('shows good judgment') without observable behaviors."
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
  - clinical-educator
  - residency-program-director
  - clerkship-director
  - cbme-faculty
tags:
  - mini-cex
  - workplace-based-assessment
  - rubric
  - behavioral-anchors
  - cbme
updated: "2026-05-18"
related_prompts:
  - domain-medical-education/educator-rubrics-wba/assess_dops_rubric_author.md
  - domain-medical-education/educator-rubrics-wba/assess_cbd_rubric_author.md
  - domain-medical-education/educator-rubrics-wba/assess_epa_observation_form_author.md
  - domain-medical-education/educator-rubrics-wba/assess_narrative_rating_anchor_writer.md
---

## Objective

Produce a Mini-CEX (Mini Clinical Evaluation Exercise) form with all 6 ABIM-defined performance domains plus an overall competence rating, each anchored to verbatim observable behaviors at unsatisfactory (1–3) / satisfactory (4–6) / superior (7–9) bands. Output a complete usable form, a forced-narrative section with stem prompts, and an inter-rater calibration appendix. Refuse to ship rating levels described by adjectives alone — every band must be behaviorally anchored.

## Your Role

Workplace-based-assessment rubric architect. You design Mini-CEX forms that a busy preceptor can complete in 10–15 minutes with reproducible inter-rater scores.

## Inputs

- `learner_level`: `MS3 | MS4 | intern | resident-junior | resident-senior | fellow | PA-student | NP-student`
- `setting`: `outpatient | inpatient ward | ED | ICU | OR | telehealth | home-visit`
- `encounter_type`: `new-patient H&P | focused follow-up | breaking-bad-news | counseling-only | pre-op evaluation`
- `specialty`: e.g., "internal medicine," "pediatrics," "family medicine"
- `competency_framework`: `ABIM-original | ACGME-core | AAMC EPAs | CanMEDS` (default ABIM-original for Mini-CEX)
- `anchored_to_level`: the level whose `satisfactory` band corresponds to "ready for independent practice at this learner level"

## Method

1. **Domain lock (DS-01 — ABIM Mini-CEX domains).** Six performance domains + overall:
   - Medical interviewing skills (history)
   - Physical exam skills
   - Professionalism / humanistic qualities
   - Clinical judgment
   - Counseling / patient education
   - Organization / efficiency
   - Overall clinical competence
   Each is rated 1–9 with named bands: 1–3 unsatisfactory; 4–6 satisfactory; 7–9 superior.

2. **Author behavioral anchors per band per domain (DT-05 — verbatim observable behaviors).** Each anchor is:
   - An observable behavior (something a third party watching could agree happened).
   - Specific to the `learner_level` (intern's satisfactory ≠ MS3's satisfactory).
   - Calibrated to `anchored_to_level` so "satisfactory" means ready for independent practice at this level.

3. **Forced-narrative section (ST-02).** Include three required free-text stems (each ≤ 100 words):
   - "What did this learner do well?" — specific observed behavior.
   - "What is the highest-priority area for improvement?" — specific observed behavior + recommended next step.
   - "Anything else?" — escalation flag if needed (e.g., professionalism concern).

   These cannot be skipped. Forms with empty narrative are invalid.

4. **Refusal guard (CM-02).** Sweep each anchor — if it contains only adjectives ("appropriate," "thorough," "shows good judgment") without a paired observable behavior, refuse. Replace with behavior phrasing.

5. **Source-fidelity audit (QA-12).** Any clinical-standard reference (e.g., "uses calgary-cambridge structure") cites its source.

6. **Inter-rater calibration appendix (ST-03).** Include:
   - 2 worked-example encounter vignettes with expected ratings per domain.
   - The "calibration discussion" script for new raters.
   - Target Cohen κ ≥ 0.6 for total score; per-domain κ ≥ 0.5 acceptable.

## Output Format

```
MINI-CEX FORM — [specialty] — Learner level: [...] — Setting: [...] — Encounter: [...]

>>> HEADER
Learner: ______________   Date: _______   Evaluator: ______________
Encounter type: [...] (new H&P / focused / counseling / pre-op / BBN)
Setting: [...]
Time observed: ____ min   Time in feedback: ____ min
Patient complexity: routine / moderate / complex
Focus of encounter (1–2 sentences): _____________________________

>>> RATING SCALE
1–3 = Unsatisfactory   4–6 = Satisfactory   7–9 = Superior   NA = Not observed

>>> DOMAIN 1 — MEDICAL INTERVIEWING SKILLS (history)
Unsatisfactory (1–3) anchor: "Open-ended questions absent; chief concern is leading-question only; misses ICE (ideas/concerns/expectations); doesn't allow patient to complete opening statement; no negotiation of agenda."
Satisfactory (4–6) anchor: "Opens with open-ended question and lets patient speak ≥ 30 s before redirect; elicits ICE; negotiates agenda; uses transparent transitions ('Now I want to ask about your past health')."
Superior (7–9) anchor: "Calgary-Cambridge transparent throughout; elicits explicit hidden concerns; integrates psychosocial dimensions naturally; uses reflective listening verbatim; patient confirms understanding before transition."
Rating: ___   Comments (observed behavior): _____________________________

>>> DOMAIN 2 — PHYSICAL EXAM SKILLS
Unsatisfactory: "Skips key elements relevant to chief concern; technique deviates from standard (e.g., palpates without warning, performs cardiac auscultation through gown); inappropriate sequence; misses key positive or false-positively reports a finding."
Satisfactory: "Performs focused exam relevant to chief concern with correct technique; warns before each maneuver; identifies the key positive and negative findings; uses appropriate draping and patient comfort."
Superior: "Demonstrates advanced maneuvers (e.g., Adson, Apley, peripheral nerve exam) with correct technique and interpretation; identifies subtle findings (e.g., narrow split S2); efficiently sequences exam to minimize patient repositioning."
Rating: ___   Comments: _____________________________

>>> DOMAIN 3 — PROFESSIONALISM / HUMANISTIC QUALITIES
Unsatisfactory: "Does not introduce self with role; closes computer/turns to patient < 30% of encounter; uses jargon without translation; visible impatience or interruption when patient speaks > 20 s; family ignored when present."
Satisfactory: "Introduces self with name + role; explains the plan; maintains eye contact / open body language; uses plain language; acknowledges family members; responds to emotion with at least one explicit empathic statement."
Superior: "Uses NURS (Name-Understand-Respect-Support) or equivalent explicit empathic-statement framework; recognizes and addresses cultural or values differences; surfaces and addresses hidden agenda; balances task focus and relational presence seamlessly."
Rating: ___   Comments: _____________________________

>>> DOMAIN 4 — CLINICAL JUDGMENT
Unsatisfactory: "Cannot articulate primary or alternative diagnoses; orders shotgun workup; cannot justify a single test choice from history/exam; misses safety-critical alternative diagnosis."
Satisfactory: "States 3-item differential with relative probability; orders tests with stated reasoning; recognizes safety-critical alternatives and rules them in/out; modifies plan in response to new data."
Superior: "Bayesian reasoning explicit (pretest, test characteristics, posttest); integrates patient values into the plan; anticipates likely sequelae and pre-positions plan for them; recognizes own diagnostic uncertainty and communicates it appropriately."
Rating: ___   Comments: _____________________________

>>> DOMAIN 5 — COUNSELING / PATIENT EDUCATION
Unsatisfactory: "No plain-language explanation; no teach-back; no shared decision-making attempt; patient questions left unaddressed."
Satisfactory: "Explains diagnosis and plan in plain language; checks for understanding (teach-back); offers 1–2 options with trade-offs; addresses patient questions; provides written/digital resources or referral."
Superior: "Tailors information to patient health-literacy and language; uses graded shared-decision-making conversation; addresses uncertainty explicitly; surfaces and validates patient preferences; documents shared-decision discussion in note."
Rating: ___   Comments: _____________________________

>>> DOMAIN 6 — ORGANIZATION / EFFICIENCY
Unsatisfactory: "Encounter runs ≥ 50% over allocated time without value-added engagement; documentation lags > 24 h; presentation to attending disorganized; cannot transition between encounters cleanly."
Satisfactory: "Encounter within ±20% of allotted time; documentation completed same day; oral presentation organized and prioritized; transitions cleanly."
Superior: "Encounter on-time without sacrificing depth; documentation completed live with patient; oral presentation models prioritized SBAR; serves as anchor for team workflow."
Rating: ___   Comments: _____________________________

>>> DOMAIN 7 — OVERALL CLINICAL COMPETENCE
Unsatisfactory: "Multiple domains unsatisfactory; safety-critical gap observed; would not entrust with similar encounter at this learner level."
Satisfactory: "Most domains satisfactory; would entrust with similar encounters with indirect supervision appropriate to learner level."
Superior: "All domains satisfactory or superior; would entrust at the next supervision level."
Rating: ___

>>> FORCED NARRATIVE (each required; ≤ 100 words)
1. What did this learner do well? (specific observed behavior)
   _______________________________________________

2. Highest-priority area for improvement? (observed behavior + recommended next step)
   _______________________________________________

3. Anything else? (escalation flag — professionalism / safety concern, leave blank if none)
   _______________________________________________

>>> EVALUATOR SIGNATURE
Evaluator: ______________   Time spent on this Mini-CEX: ____ min   Date: _______
Learner sign-off (acknowledges feedback): ______________   Date: _______

>>> INTER-RATER CALIBRATION APPENDIX

Worked Example A — Satisfactory encounter (target ratings)
Scenario: MS3, focused follow-up of HTN at outpatient clinic. Learner opens with "Tell me how you've been since I saw you last," waits 25 s, elicits ICE, performs focused exam, explains 2 medication options, uses teach-back.
Expected ratings: Hx 5, PE 5, Prof 6, CJ 5, Counsel 6, Org 5, Overall 5.

Worked Example B — Superior encounter (target ratings)
Scenario: PGY2 inpatient, breaking-bad-news new cancer diagnosis. Learner uses SPIKES, names emotion, uses "I wish... I worry... I wonder...", documents shared decision-making.
Expected ratings: Hx 8, PE NA, Prof 9, CJ 7, Counsel 9, Org 7, Overall 8.

Calibration discussion script (for new raters): "Compare your ratings to the worked example targets. For any domain off by > 2 points, discuss with calibration partner the verbatim behaviors you observed. Re-rate after discussion. Target Cohen κ ≥ 0.6 on total; ≥ 0.5 per domain."

>>> SOURCE-FIDELITY AUDIT
| Reference | Source | Status |
|---|---|---|
| Calgary-Cambridge | Silverman 2013 | verified |
| SPIKES | Baile 2000 | verified |
| NURS (empathy framework) | Smith / AAIM | verified |
| TOF / NMB note (not used here — Mini-CEX) | n/a | n/a |
| ABIM Mini-CEX domains | Norcini 2003 | verified |

>>> REJECTED ELEMENT (minimum 1)
Considered: anchor "demonstrates appropriate professionalism" at the satisfactory band.
Rejected: adjective without observable behavior; inter-rater poison.
Replaced with: "Introduces self with name + role; uses plain language; acknowledges family members; responds to emotion with at least one explicit empathic statement."
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `learner_level` | Recalibrates the "satisfactory" band to the level's entrustment expectation |
| `setting` | Adjusts domain weighting (ED → adds disposition decision; OR → adds team-based; outpatient → adds continuity) |
| `encounter_type` | Drives observed-behavior anchors (BBN → emphasizes Prof + Counsel; pre-op → emphasizes CJ + history) |
| `competency_framework` | Maps domains to ACGME / CanMEDS / EPAs if not using ABIM-original |
| `time_limit_per_form` | Default 10–15 min; if shorter, reduce narrative stems to 2 |
| `add_supervisor_role_check` | Adds explicit entrustment-level question ("Would you entrust at supervision level [X]?") |

## Verification Checklist

- [ ] All 6 domains + overall present.
- [ ] Each band (1–3 / 4–6 / 7–9) has a verbatim observable-behavior anchor.
- [ ] No anchor uses only adjectives ("appropriate," "thorough").
- [ ] Anchors calibrated to `learner_level`.
- [ ] Forced narrative section present with 3 stems.
- [ ] Inter-rater calibration appendix has 2 worked-example vignettes with target ratings.
- [ ] Cohen κ target ≥ 0.6 total, ≥ 0.5 per domain stated.
- [ ] Source-fidelity audit populated.
- [ ] At least one rejected element shown.

## Worked Example (compact)

**Input:** `learner_level = intern`, `setting = inpatient ward`, `encounter_type = focused follow-up`, `specialty = internal medicine`.

**Output:** see Output Format block above — anchors instantiated for intern-on-ward-IM with "satisfactory = ready for indirect supervision on similar encounters."
