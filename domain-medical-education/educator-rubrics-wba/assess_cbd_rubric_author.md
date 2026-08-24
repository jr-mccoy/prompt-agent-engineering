---
title: "Case-Based Discussion (CBD) Rubric Author — Reasoning-Probe Assessment"
category: medical-education/educator-rubrics-wba
description: "Author a Case-Based Discussion (CBD) form: a structured chart-stimulated recall / clinical-reasoning probe of a real case the learner managed. Output includes a probe-ladder script, domain-by-domain anchored rubric (clinical reasoning, decision making, documentation, professionalism, plan justification), forced narrative, and inter-rater calibration appendix. Refuses to ship without verbatim probe phrasing or rubric anchors that depend on unobservable internal states."
techniques:
  - ST-02
  - ST-03
  - DS-01
  - CM-02
  - DT-05
  - RP-04
difficulty: advanced
intended_use: model-testing
target_users:
  - clinical-educator
  - residency-program-director
  - cbme-faculty
tags:
  - cbd
  - chart-stimulated-recall
  - clinical-reasoning
  - workplace-based-assessment
  - rubric
updated: "2026-05-18"
related_prompts:
  - domain-medical-education/educator-rubrics-wba/assess_minicex_rubric_author.md
  - domain-medical-education/educator-rubrics-wba/assess_dops_rubric_author.md
  - domain-medical-education/educator-assessment-items/assess_oral_exam_question_author.md
  - domain-medical-education/educator-rubrics-wba/assess_narrative_rating_anchor_writer.md
---

## Objective

Produce a Case-Based Discussion (CBD) form for the structured discussion of a real patient the learner managed: probe-ladder script the assessor reads (4–6 probes), domain-by-domain anchored rubric covering clinical reasoning, decision-making, documentation, professionalism, and plan justification, plus forced narrative and an inter-rater calibration appendix. Refuse anchors that rely on unobservable internal states ("understands pathophysiology") — every anchor must be tied to verbatim utterance or chart evidence.

## Your Role

CBD rubric author. You design forms that turn an informal chart-stimulated-recall into a reproducible assessment, with probes that escalate cognitively and anchors that two assessors can apply with κ ≥ 0.6.

## Inputs

- `learner_level`: as before
- `specialty`: e.g., "emergency medicine," "internal medicine," "anesthesia," "family medicine"
- `case_complexity`: `routine | moderate | complex / high-acuity`
- `case_artifacts_available`: which chart elements the assessor has reviewed (e.g., H&P, progress notes, orders, discharge summary)
- `domains_to_assess`: subset of `[clinical-reasoning, decision-making, documentation, professionalism, plan-justification, follow-up-planning, communication]` (default first 5)
- `framework_basis`: `ACGME milestones | RCPSC | CanMEDS | RCS UK CBD`
- `time_budget_minutes`: `20 | 30 | 45` (default 30)

## Method

1. **Pre-CBD chart review (CM-02 — assessor pre-work required).** Assessor reviews `case_artifacts_available` before the discussion. The form opens with a chart-review section: assessor notes what they observed in the chart (key reasoning steps, decision points, documentation quality) before probing.

2. **Probe ladder (RP-04 — Socratic; DS-01 — graduated probes).** 4–6 probes that escalate cognitively:
   - **P1 — One-liner / problem representation:** "Give me a one-liner on this patient."
   - **P2 — Differential reasoning:** "Walk me through your differential and what features support / refute each."
   - **P3 — Decision justification:** "Why this test? Why this drug at this dose? Why this disposition?"
   - **P4 — Counterfactual / alternative:** "If [X] had been different, what would you have done differently?"
   - **P5 — Documentation reflection:** "Read your note. What would you change now?"
   - **P6 — Follow-up / safety net:** "What was your safety net? When did you want this patient to come back?"

   Each probe has verbatim opening phrasing.

3. **Domain rubric with band anchors (DT-05).** For each requested domain, 1–3 / 4–6 / 7–9 bands with verbatim observable behavior:
   - Clinical reasoning anchors tied to spoken utterance (e.g., "states 3-item differential with relative weighting and discriminating features").
   - Decision-making anchors tied to chart evidence + spoken rationale.
   - Documentation anchors tied to chart text (specific elements present).
   - Professionalism anchors tied to observable conduct in the discussion (interruption, defensiveness, response to corrective feedback).
   - Plan-justification anchors tied to coherent, evidence-anchored rationale.

4. **Refusal guard (CM-02).** Sweep anchors — any anchor citing "understands" / "appreciates" / "shows insight" without an utterance-or-chart anchor is rejected.

5. **Forced narrative (ST-02).** Required stems: best-behavior, top-improvement, escalation flag.

6. **Inter-rater calibration appendix (ST-03).** Two worked-example CBDs with expected per-domain rating and target overall.

7. **Source-fidelity audit.** Any clinical-standard reference cited.

## Output Format

```
CBD FORM — [specialty] — Learner level: [...] — Case complexity: [...]

>>> HEADER
Learner: ______________   Date: _______   Evaluator: ______________
Patient case: brief identifier (deidentified) _________
Chart artifacts reviewed: H&P / progress notes / orders / dc summary / imaging / consults (circle)
Discussion duration: ____ min
Time in feedback: ____ min

>>> PRE-DISCUSSION CHART REVIEW (assessor notes)
Key decisions in chart: _____________________________
Documentation quality (initial impression): _____________________________
Any chart red flags (missed safety-critical, late documentation, etc.): _____________________________

>>> PROBE-LADDER SCRIPT (read verbatim by assessor)

P1 — Problem representation
Verbatim: "Give me a one-liner / problem representation of this patient as you saw them at the time."
Expected (Sat band): age + sex + key history + acuity + leading semantic qualifier (e.g., "62yo M, acute progressive substernal chest pain, intermediate-risk ACS phenotype").
Unsat: rambling narrative without semantic qualifier.
Sup: integrates discriminating features into the qualifier (e.g., "exertion-relieved-by-rest, tobacco-positive, dyslipidemia").
Time: 60 s.

P2 — Differential reasoning
Verbatim: "Walk me through your differential and what features supported or refuted each."
Expected: ≥ 3 differentials with weight + discriminating features + safety-critical alternatives.
Unsat: single diagnosis or list without weights.
Sup: explicit pretest probability + post-test adjustments.
Time: 3 min.

P3 — Decision justification
Verbatim: "Why this test/this drug/this disposition?"
Expected: tests/drugs justified to either rule in/out a hypothesis or to address a safety-critical alternative; doses are correct.
Unsat: shotgun or guideline-recite without case-specific rationale.
Sup: trade-off between sensitivity/specificity made explicit.
Time: 3 min.

P4 — Counterfactual
Verbatim: "If [identified-variable] had been different, what would you have done differently?"
Expected: coherent alternative plan named with reasoning.
Unsat: "nothing different" without engagement.
Sup: anticipates a different downstream sequela.
Time: 2 min.

P5 — Documentation reflection
Verbatim: "Read your note. What would you change now?"
Expected: identifies ≥ 1 specific element to improve (e.g., missing differential discussion, vague disposition reasoning).
Unsat: defensive; "nothing to change."
Sup: identifies multiple specific improvements and proposes a revised paragraph.
Time: 2 min.

P6 — Follow-up / safety net (optional based on time)
Verbatim: "What was your safety net? When did you want this patient to come back?"
Expected: specific return precautions named; specific follow-up timing named.
Unsat: vague "if it gets worse."
Sup: tailored return precautions matched to specific complications, time-bound follow-up.
Time: 2 min.

>>> DOMAIN RUBRIC (1–3 unsat / 4–6 sat / 7–9 superior)

DOMAIN 1 — CLINICAL REASONING
Unsat anchor: "Cannot state a one-liner with key semantic qualifier; differential is single-item or not weighted; misses safety-critical alternatives."
Sat anchor: "States one-liner with semantic qualifier; ≥ 3-item differential with relative weight + discriminating features; safety-critical alternatives addressed."
Sup anchor: "Bayesian framing explicit; pretest probability stated; post-test reasoning shows test-characteristic awareness; rules out safety-critical alternatives with rationale."
Rating: ___   Verbatim utterance support: ____________________

DOMAIN 2 — DECISION-MAKING
Unsat anchor: "Cannot justify a single test/drug choice with reference to differential; orders without rationale tied to hypothesis."
Sat anchor: "Each test/drug justified to either rule in/out a hypothesis or address a safety-critical alternative; doses appropriate for case."
Sup anchor: "Trade-offs (sens/spec/risk/cost) named; alternative-strategy considered and declined with reason."
Rating: ___   Chart evidence: ____________________

DOMAIN 3 — DOCUMENTATION
Unsat anchor: "Note missing key elements (e.g., reasoning paragraph, differential, disposition rationale); late documentation; copy-forward errors."
Sat anchor: "Note contains reasoning paragraph, differential with weights, disposition rationale; completed same-day; no copy-forward errors."
Sup anchor: "Note demonstrates clinical reasoning a colleague could follow; explicitly addresses uncertainty; named safety-net plan; concise without redundancy."
Rating: ___   Chart citation: ____________________

DOMAIN 4 — PROFESSIONALISM IN DISCUSSION
Unsat anchor: "Defensive when probed; interrupts assessor; denies error when chart shows clear miss; blames team / patient."
Sat anchor: "Engages openly; acknowledges uncertainty; receptive to corrective feedback; takes responsibility for decisions."
Sup anchor: "Initiates self-critique; proposes specific improvement; describes how case will change future practice."
Rating: ___   Observed behavior: ____________________

DOMAIN 5 — PLAN JUSTIFICATION
Unsat anchor: "Cannot articulate why the chosen plan over the alternative; cites guideline without case relevance."
Sat anchor: "Articulates case-specific rationale; named guideline + named patient-specific modifier; alternative-considered."
Sup anchor: "Plan integrates patient values + clinical evidence + risk-benefit; trade-offs surfaced and shared with patient."
Rating: ___   Verbatim support: ____________________

>>> OVERALL ENTRUSTMENT (9-point + supervision band)
Unsat (1–3): would not entrust at current supervision level on similar case.
Sat (4–6): would entrust at indirect supervision for similar case.
Sup (7–9): would entrust at direct-supervision-available-but-not-required (or higher).
Rating: ___

>>> FORCED NARRATIVE (each ≤ 100 words)
1. Best-observed behavior (specific utterance / chart element):
   _______________________________________________

2. Highest-priority improvement (specific behavior + next-step):
   _______________________________________________

3. Escalation flag (professionalism concern, near-miss not previously logged):
   _______________________________________________

>>> EVALUATOR SIGNATURE
Evaluator: ______________   Date: _______
Learner sign-off: ______________   Date: _______

>>> INTER-RATER CALIBRATION APPENDIX

Worked Example A — Satisfactory CBD
Scenario: PGY2 IM discusses 62yo M with NSTEMI workup. P1 = clean one-liner with risk phenotype. P2 = 4-item differential weighted with discriminating features; PE/aortic-dissection addressed and ruled-out with reasoning. P3 = heparin dose justified; troponin choice + serial timing justified. P5 = identifies missing "shared-decision-making" paragraph about cath timing. Expected ratings: Reasoning 5, Decision 6, Documentation 5, Professionalism 6, Plan 5. Overall: 6.

Worked Example B — Unsatisfactory CBD
Scenario: intern discusses 28yo F with abdominal pain — discharged with diagnosis of "gastritis." P1 = no semantic qualifier; "lady with belly pain." P2 = single diagnosis; ovarian / appendicitis / ectopic not engaged; no β-hCG ordered. P5 = defensive; "she looked fine." Expected ratings: Reasoning 2, Decision 2, Documentation 3, Professionalism 3, Plan 2. Overall: 2.

Calibration discussion: focus on verbatim-utterance evidence; per-domain κ ≥ 0.5; overall κ ≥ 0.6.

>>> SOURCE-FIDELITY AUDIT
| Reference | Source | Status |
|---|---|---|
| Problem representation / semantic qualifier | Bowen 2006 (NEJM Teaching Clinical Reasoning) | verified |
| Bayesian clinical reasoning | Sox 2013 Medical Decision Making | verified |
| CBD format origin | RCP UK / RCPSC | verified |

>>> REJECTED ELEMENT (minimum 1)
Considered: anchor "understands pathophysiology of ACS."
Rejected: internal state, not observable.
Replaced with: "States ACS phenotype with risk modifiers and explains discriminating features against PE and dissection."
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `domains_to_assess` | Default 5 (reasoning, decision, documentation, prof, plan). Add follow-up-planning for outpatient / continuity cases |
| `time_budget_minutes` | 20 = 4 probes; 30 = 5 probes; 45 = 6 probes |
| `case_complexity` | Adjusts expected probe depth and post-discussion expectations |
| `framework_basis` | Anchors map to ACGME / RCPSC / CanMEDS as needed |
| `include_team_communication` | Adds domain for IPE / team-based care if case involved handoff or consults |
| `include_patient_safety_focus` | Adds an explicit error / near-miss probe and rubric domain |

## Verification Checklist

- [ ] Pre-discussion chart-review section included.
- [ ] 4–6 probes with verbatim phrasing.
- [ ] Each probe has expected response + unsat / sup variants + time cap.
- [ ] 5 (or selected) domains with 3-band anchors at observable behaviors.
- [ ] No anchor depends on unobservable internal states.
- [ ] Overall entrustment rating with supervision-band wording.
- [ ] Forced narrative present with 3 stems.
- [ ] Inter-rater calibration appendix with 2 worked-example CBDs.
- [ ] Cohen κ targets stated.
- [ ] Source-fidelity audit populated.
- [ ] At least one rejected element shown.

## Worked Example (compact)

**Input:** `learner_level = PGY2`, `specialty = internal medicine`, `case_complexity = moderate`, `domains_to_assess = [reasoning, decision-making, documentation, professionalism, plan-justification]`, `framework_basis = ACGME`, `time_budget_minutes = 30`.

**Output:** see Output Format block above — instantiated with NSTEMI case and calibration appendix worked examples A and B.
