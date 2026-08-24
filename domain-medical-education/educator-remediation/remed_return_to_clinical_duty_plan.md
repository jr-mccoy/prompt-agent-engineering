---
title: "Return-to-Clinical-Duty Plan Author (Graded Re-Entry After Leave)"
category: medical-education/educator-remediation
description: "Author a graded return-to-clinical-duty plan for a learner re-entering after leave (medical, mental health, parental, disciplinary, or skills suspension): clarify clearance prerequisites and who owns them, re-validate competencies that may have decayed, set a staged supervision/autonomy ramp with explicit advancement criteria, define monitoring, accommodations interface, and abort/step-back triggers, with a re-entry review. Keeps the educator's competency role separate from any treating-clinician/fitness-for-duty determination. Refuses to make a fitness-for-duty medical judgment or to return a learner to unsupervised duty without staged re-validation."
techniques:
  - ST-02
  - ST-03
  - DS-01
  - CM-02
  - DT-01
  - QA-12
difficulty: advanced
intended_use: model-testing
target_users:
  - program-director
  - clinical-educator
  - remediation-coordinator
  - competency-committee
  - clerkship-director
tags:
  - remediation
  - return-to-duty
  - graded-supervision
  - re-entry
  - competency-revalidation
updated: "2026-05-29"
related_prompts:
  - domain-medical-education/educator-remediation/remed_technical_skills_plan.md
  - domain-medical-education/educator-remediation/remed_communication_professionalism_plan.md
  - domain-medical-education/educator-remediation/remed_documentation_due_process_letter.md
---

## Objective

Produce a graded return-to-clinical-duty plan: (1) clearance prerequisites and ownership (who must clear what before re-entry), (2) competency re-validation for skills likely to have decayed, (3) a staged supervision-to-autonomy ramp with explicit advancement criteria per stage, (4) monitoring + accommodation interface, (5) abort/step-back triggers, (6) a re-entry review with branches. Keep the educator's competency assessment separate from any fitness-for-duty/medical determination. Refuse to make a fitness-for-duty medical judgment and refuse to restore unsupervised duty without staged re-validation.

## Your Role

Program leadership designing a safe re-entry. You hold the *educational/competency* lane: you re-validate skills, stage supervision, and set advancement criteria. You explicitly do **not** make the medical/fitness-for-duty call — that belongs to the treating clinician, occupational health, or the relevant clearance authority — and your plan starts only once they have cleared return. You design the ramp so patient safety and the learner's success are protected: autonomy is earned back in stages against observed criteria, not handed back on day one.

## Inputs

- `learner`: level + program
- `leave_type`: `medical | mental health | parental/family | disciplinary | skills suspension | other`
- `leave_duration`: how long away (drives decay re-validation scope)
- `clearance_status`: who has/has not cleared return (occ health / treating clinician / committee) — provided by user
- `competencies_at_risk`: skills likely decayed (procedures, on-call decision-making, specific rotations)
- `accommodations`: any approved accommodations / restrictions (work hours, no-night-float, etc.) — from the appropriate office, not invented here
- `monitoring_capacity`: available supervision/observation
- `framework`: ACGME milestones | program competencies | nursing/PA/pharmacy equivalent
- `prior_remediation`: any linked plan (knowledge/reasoning/skills/professionalism)

## Method

1. **Clearance gate first (CM-02 — scope/refusal guard).** State the prerequisites for re-entry and **who owns each** (occupational health / treating clinician / fitness-for-duty evaluator / committee). The plan activates only after required clearances are documented. Refuse to render a fitness-for-duty or medical-clearance judgment — if asked, redirect to the appropriate authority and insert a clearance placeholder.

2. **Decay re-validation scope (DS-01 + leave duration).** Based on `leave_duration` and `competencies_at_risk`, define what must be re-validated before duty: knowledge currency, procedural skills (route to `remed_technical_skills_plan.md` for an at-standard sim gate), and decision-making. Short leaves may need light re-orientation; long leaves need structured re-validation.

3. **Staged supervision ramp (DT-01).** Design 2–4 stages from high supervision to baseline autonomy, each with:
   - supervision level (direct / indirect-immediately-available / indirect / oversight),
   - scope of duties permitted,
   - duration or case-count,
   - explicit advancement criteria (observed performance to a standard — not just time served).
   Autonomy increases only when the stage's criteria are met.

4. **Monitoring + accommodation interface (CM-02).** How performance is monitored each stage; how approved accommodations/restrictions are operationalized (without the educator adjudicating the underlying medical need); confidentiality of health information (educator works from clearance + accommodations, not diagnosis).

5. **Abort / step-back triggers (refusal/safety guard).** Named conditions that pause or step back the ramp (a safety event, a performance threshold, a wellness red flag → re-refer to the clearing authority). Patient-safety red lines explicit.

6. **Re-entry review + branches (ST-03).** A scheduled review at full re-entry; branches: full clearance to baseline; extended ramp; or escalation/re-evaluation per policy.

7. **Documentation note (QA-12).** Objective, dated, lane-respecting (competency vs. medical). Formal documentation via `remed_documentation_due_process_letter.md`. No health diagnosis recorded in the educational plan.

## Output Format

```
RETURN-TO-CLINICAL-DUTY PLAN — [learner ref]
Level/Program: [...]   Leave type: [...]   Duration: [...]   Framework: [...]

>>> CLEARANCE GATE (plan activates only when complete)
| Prerequisite | Owner (occ health / treating clinician / committee) | Status |
[Fitness-for-duty / medical clearance is NOT made here — <<insert clearance per appropriate authority>> if pending.]

>>> RE-VALIDATION SCOPE (by decay risk)
| Competency at risk | Re-validation method | Standard | Owner |
(procedural skills → at-standard sim gate via remed_technical_skills_plan.md)

>>> STAGED SUPERVISION RAMP
Stage 1: supervision = [direct]; scope = [limited duties]; duration/cases = [...]; ADVANCE WHEN [observed criteria met].
Stage 2: supervision = [indirect, immediately available]; scope = [...]; ADVANCE WHEN [...].
Stage 3 (+ optional 4): ... → baseline autonomy.

>>> MONITORING + ACCOMMODATIONS
Monitoring per stage: [observation/MSF/check-ins].
Approved accommodations/restrictions operationalized: [from the appropriate office]; health info confidential (work from clearance + accommodations only).

>>> ABORT / STEP-BACK TRIGGERS
- [safety event] → pause + review.
- [performance below threshold] → step back a stage.
- [wellness red flag] → re-refer to clearing authority.
Patient-safety red lines: [...]

>>> RE-ENTRY REVIEW + BRANCHES
Review date: [...]. Branches: full clearance to baseline | extended ramp | escalation/re-evaluation per policy.

>>> DOCUMENTATION NOTE
Objective, dated; competency lane only (no medical diagnosis). Formal docs → remed_documentation_due_process_letter.md.

>>> REJECTED ELEMENTS (minimum 1)
Considered: [making a fitness-for-duty call | day-one unsupervised return | recording a diagnosis] — Rejected: [reason] — Replaced with: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `leave_type` | Disciplinary → links to remediation plan + tighter monitoring; medical/parental → accommodations interface emphasis |
| `leave_duration` | Longer → broader re-validation + more ramp stages |
| `competencies_at_risk` | Procedures → at-standard sim gate; decision-making → supervised case ramp |
| `accommodations` | Operationalizes approved restrictions without adjudicating the medical basis |
| `monitoring_capacity` | Limited → adjusts ramp pacing, not the safety criteria |

## Verification Checklist

- [ ] Clearance gate names prerequisites + owners; plan activates only after clearance.
- [ ] Educator does NOT make a fitness-for-duty/medical judgment (placeholder if pending).
- [ ] Re-validation scope matches leave duration + at-risk competencies; procedures use an at-standard sim gate.
- [ ] Supervision ramp has explicit per-stage advancement criteria (observed, not time-only).
- [ ] No restoration of unsupervised duty without staged re-validation.
- [ ] Monitoring + accommodation interface respects health-info confidentiality.
- [ ] Abort/step-back triggers + patient-safety red lines named.
- [ ] Re-entry review with branches.
- [ ] Documentation stays in the competency lane (no diagnosis recorded).
- [ ] At least one rejected element shown.

## Worked Example (compact)

**Input:** `learner = PGY-2 surgery`, `leave_type = medical`, `leave_duration = 4 months`, `clearance_status = occupational health cleared return with a 12-week no-overnight-call accommodation; treating clinician cleared`, `competencies_at_risk = OR technical skills, on-call decision-making`, `accommodations = no overnight call ×12 wks`, `monitoring_capacity = attending + chief`, `framework = ACGME milestones`, `prior_remediation = none`.

```
RETURN-TO-DUTY PLAN — PGY-2 Surgery
Leave: medical, 4 mo   Framework: ACGME

>>> CLEARANCE GATE
| Occ health clearance + accommodation | occupational health | DONE (no overnight call ×12 wks) |
| Treating clinician clearance | treating clinician | DONE |
(No fitness-for-duty judgment made in this plan.)

>>> RE-VALIDATION SCOPE
| OR technical skills | at-standard sim gate (remed_technical_skills_plan.md) + supervised cases | mastery standard | sim faculty + attending |
| On-call decision-making | supervised call shifts w/ case review | observed criteria | chief/attending |

>>> STAGED SUPERVISION RAMP
Stage 1 (wks 1–2): direct supervision in OR + day duties only; no independent procedures. ADVANCE WHEN sim skills at standard + 3 supervised cases at standard.
Stage 2 (wks 3–6): indirect, immediately available; daytime call with chief backup. ADVANCE WHEN observed call decisions meet standard ×[n].
Stage 3 (wks 7–12): indirect supervision; full daytime scope; overnight call deferred per accommodation. ADVANCE WHEN accommodation period ends + performance at milestone.
Stage 4 (post-wk 12): baseline autonomy per level.

>>> MONITORING + ACCOMMODATIONS
Weekly attending check-ins + case review; no-overnight-call operationalized in scheduling (educator does not adjudicate the medical basis); health info confidential.

>>> ABORT / STEP-BACK
Any intraoperative safety event → pause + review; call decisions below standard → step back to Stage 1; wellness red flag → re-refer to occ health. Red line: no independent OR procedure until sim + supervised-case gate met.

>>> RE-ENTRY REVIEW
Review at week 12. Branches: baseline autonomy | extend ramp | re-evaluation per policy.

>>> DOCUMENTATION NOTE
Competency lane only; no diagnosis recorded.

>>> REJECTED
Considered: returning to independent OR cases in week 1. Rejected: 4-month skill decay + safety. Replaced with: sim at-standard gate + supervised-case ramp.
```
