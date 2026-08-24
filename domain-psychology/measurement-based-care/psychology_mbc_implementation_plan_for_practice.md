---
title: "MBC Implementation Plan for a Practice"
category: psychology/measurement-based-care
description: "Build a measurement-based-care implementation plan for a practice or clinic (not a single client): instrument battery selection, workflow/EHR integration, staff roles, training, cadence policy, dashboards, change management, and fidelity metrics."
techniques:
  - DS-02
  - DT-01
  - CM-01
  - QA-04
  - CM-02
difficulty: intermediate
intended_use: model-testing
tags:
  - measurement-based-care
  - implementation
  - clinic-workflow
  - EHR-integration
  - change-management
  - fidelity-metrics
  - feedback-informed-treatment
  - collaborative-care
updated: "2026-06-08"
related_prompts:
  - domain-psychology/measurement-based-care/psychology_outcome_monitoring_dashboard_interpreter.md
  - domain-psychology/measurement-based-care/psychology_treatment_non_response_decision_tree.md
  - domain-psychology/treatment-planning/psychology_measurement_based_care_plan.md
  - domain-psychology/care-coordination/psychology_integrated_care_huddle_brief.md
---

# MBC Implementation Plan for a Practice

## Objective

Produce an operational plan for implementing measurement-based care (MBC) / feedback-informed treatment (FIT) across a practice, clinic, or program — not for a single client. The plan specifies: (1) the standardized instrument battery and the logic for selecting it, (2) the workflow and EHR/measurement-platform integration that captures and surfaces scores, (3) staff roles and responsibilities across the measurement lifecycle, (4) a training and competency plan, (5) the practice-level cadence policy, (6) the dashboards and registry-review cadence, (7) a change-management approach grounded in implementation science, and (8) fidelity metrics that confirm MBC is actually happening, not just nominally adopted. The deliverable is a rollout plan a clinical director could execute and audit.

## When to Use

- When a practice or clinic is standing up MBC for the first time, or relaunching a stalled implementation.
- When a payor, ACO, accreditation body, or value-based contract requires routine outcome reporting and the practice needs an operational rollout.
- When a behavioral-health team is integrating into a collaborative-care / IMPACT-style program that requires a registry and treat-to-target workflow.
- When MBC instruments are being collected but scores are not reviewed in session (the feedback loop is broken) and the workflow needs to be redesigned.
- When leadership needs a defensible, auditable implementation plan with fidelity metrics.

## Inputs / Context Required

- **Practice profile**: setting type (private group, CMHC, hospital outpatient, integrated primary care, training clinic), number of clinicians, caseload size, populations served.
- **Presenting-problem mix**: dominant diagnoses/domains across the caseload (depression, anxiety, PTSD, SUD, child/adolescent, etc.) — drives the battery.
- **Existing infrastructure**: current EHR / measurement platform, whether it supports score capture, scoring, trending, and dashboards; current instruments in use.
- **Workflow context**: where clients check in, available devices/tablets/portal, front-desk vs. clinician administration, session length.
- **Staffing**: roles available (front desk, MA/care manager, clinicians, supervisors, QI/data analyst, prescriber).
- **Regulatory / contract drivers**: accreditation (Joint Commission/CARF), payer reporting requirements, value-based metrics.
- **Readiness**: prior MBC attempts, clinician attitudes/known objections, leadership sponsorship.
- `[clinician input required: EHR/platform's actual capabilities for auto-scoring, alerting, and dashboarding — confirm before designing the workflow around them]`
- `[clinician input required: licensing/cost status of any instruments not in the free/widely-licensed set]`

## Constraints

### Must

- Select a **standardized core battery** matched to the caseload's dominant domains, favoring validated, brief, freely-available or widely-licensed instruments (PHQ-9, GAD-7, PCL-5, ORS/SRS, OQ-45, AUDIT/DAST-10, OCI-R, pediatric measures where relevant), with a defined primary measure per domain.
- Define a **practice cadence policy** (baseline, in-treatment frequency, episode-end, follow-up) with a minimum standard (e.g., primary measure at least every 2–4 sessions; every session preferred in active treatment) and rules for different programs (OP vs IOP/PHP).
- Specify the **end-to-end workflow**: capture point, scoring (auto vs manual), how the score is surfaced to the clinician before/in session, and how it is reviewed with the client — the feedback loop must close, not just collect.
- Assign **roles** across the lifecycle: who administers, who scores, who reviews, who manages the registry, who acts on alerts (including risk-item alerts).
- Build a **risk-alert protocol**: PHQ-9 item-9 / PCL-5 positives generate a defined, owned, time-bound clinical response — not a passive data point.
- Include a **training + competency plan**: didactics, role-play of the in-session review, a clinician competency check, and supervision integration.
- Define **dashboards + registry-review cadence** for panel management (link to the dashboard interpreter) and the not-on-track / treat-to-target escalation path (link to the non-response decision tree).
- Specify **fidelity metrics**: measurement-completeness rate, score-reviewed-in-session rate, time-to-act-on-not-on-track, and risk-flag-follow-up rate — and the target for each.
- Use an **implementation/change-management** frame (e.g., stakeholder engagement, addressing clinician objections, phased pilot before full rollout, feedback cycle).

### Must Not

- Do not adopt instruments that do not match the caseload's dominant domains, or a battery so large it cannot be administered routinely.
- Do not design a workflow that captures scores without surfacing and reviewing them in session — that is the most common implementation failure.
- Do not leave risk-item alerts unassigned or untimed.
- Do not omit fidelity metrics; an implementation with no fidelity measurement cannot tell adoption from nominal compliance.
- Do not assume EHR/platform capabilities; confirm them and design to actual capability, flagging gaps.
- Do not fabricate instrument norms, licensing terms, or platform features; flag unknowns with `[clinician input required]`.
- Do not skip change management and pilot straight to mandated full rollout without addressing clinician buy-in.

## Instructions

1. **Profile the practice and caseload.** Summarize setting, staffing, caseload domain mix, infrastructure, and regulatory drivers. Note readiness and known objections.

2. **Select the core battery.** Map dominant domains to validated primary measures (one primary per domain) plus optional secondary/alliance measures (ORS/SRS or OQ-45). Justify each by domain fit, brevity, and licensing. Keep the routine burden ≤ a few minutes per visit.

3. **Set the cadence policy.** Define baseline, in-treatment frequency, episode-end, and follow-up, with program-specific rules (OP vs IOP/PHP) and a stated minimum standard.

4. **Design the end-to-end workflow.** Specify capture point and device, scoring method (auto-score in platform vs. manual), how the score reaches the clinician before/at session, the in-session review step (the closing of the loop), and documentation linkage to the treatment plan. Design to the EHR's confirmed capabilities; flag gaps.

5. **Assign roles.** Map each lifecycle step (administer → score → surface → review → register → act) to a role, including registry manager and risk-alert owner.

6. **Build the risk-alert protocol.** Define the trigger (PHQ-9 item 9, PCL-5 elevation, reliable deterioration), the owner, the required action, and the time standard.

7. **Write the training + competency plan.** Didactics on MBC rationale, hands-on practice of the in-session score-review script, a competency check, and how MBC enters supervision.

8. **Define dashboards + registry review.** Specify the panel-level metrics, the review cadence (link to dashboard interpreter), and the not-on-track escalation path (link to non-response decision tree).

9. **Specify fidelity metrics + targets.** Measurement-completeness, review-in-session rate, time-to-act on not-on-track, risk-flag follow-up rate — with a numeric target and an owner each.

10. **Lay out change management + phasing.** Stakeholder engagement, objection handling, a pilot (subset of clinicians/program) with success criteria before full rollout, and a feedback/iteration cycle.

11. **Run verification.**

## Output Format

```
=== MBC IMPLEMENTATION PLAN FOR PRACTICE ===

PRACTICE PROFILE
Setting: [type]   Clinicians: [#]   Caseload size: [#]   Populations: [..]
Dominant domains: [Depression / Anxiety / PTSD / SUD / Peds / ...]
EHR / measurement platform: [name + confirmed capabilities]
Regulatory / contract drivers: [accreditation / payer / VBC]
Readiness & known objections: [..]

────────────────────────────────────────────────────────
CORE INSTRUMENT BATTERY

| Domain | Primary measure | Secondary/alliance (opt) | Bands used | Rationale |
|--------|-----------------|--------------------------|------------|-----------|
| Depression | PHQ-9 | — | remission ≤4; MCID ≥5; item-9 risk | [fit/brevity/license] |
| Anxiety | GAD-7 | — | remission ≤4; MCID ≥4 | [..] |
| PTSD | PCL-5 | — | probable ≥31–33; MCID ≥10 | [..] |
| Global / alliance | ORS / SRS (or OQ-45) | — | ORS <25 clinical; SRS <36 alliance | [..] |
| [SUD / Peds / OCD] | [AUDIT-DAST-10 / PHQ-A-SCARED / OCI-R] | — | [bands] | [..] |
[clinician input required: licensing/cost for any non-free instruments]

────────────────────────────────────────────────────────
CADENCE POLICY
Baseline: [intake/session 1]   In-treatment: [≥ every 2–4 sessions; every session preferred OP]
Program rules: OP [..] | IOP/PHP [more frequent — specify]   Episode-end: [last session]   Follow-up: [opt]
Minimum standard (auditable): [..]

────────────────────────────────────────────────────────
END-TO-END WORKFLOW (loop must close)
Capture point / device: [front-desk tablet / portal pre-visit / in-room]
Scoring: [auto in platform / manual]   Surfaced to clinician: [how + when, pre/at session]
In-session review step: [score-review script used — loop closes here]
Documentation linkage: [progress note field + treatment-plan objective]
EHR capability gaps flagged: [..]

────────────────────────────────────────────────────────
ROLES (measurement lifecycle)
| Step | Owner role |
|------|-----------|
| Administer | [front desk / MA] |
| Score | [platform auto / MA] |
| Surface to clinician | [platform / MA] |
| Review in session | [clinician] |
| Registry management | [care manager / QI] |
| Act on alerts | [clinician / care manager] |

RISK-ALERT PROTOCOL
Trigger: [PHQ-9 item 9 / PCL-5 elevation / reliable deterioration]
Owner: [..]   Required action: [..]   Time standard: [e.g., same day / before client leaves]

────────────────────────────────────────────────────────
TRAINING + COMPETENCY PLAN
Didactics: [MBC rationale, instrument interpretation]
Skills practice: [role-play of in-session score-review]
Competency check: [observed review / checklist]
Supervision integration: [how trajectories enter supervision]

DASHBOARDS + REGISTRY REVIEW
Panel metrics tracked: [coverage, remission, response, not-improved, deteriorated]
Review cadence: [weekly/monthly registry huddle] → link: dashboard interpreter
Not-on-track escalation: → link: treatment non-response decision tree

────────────────────────────────────────────────────────
FIDELITY METRICS (adoption ≠ nominal compliance)
| Metric | Target | Owner |
|--------|--------|-------|
| Measurement-completeness rate | [≥80%] | [..] |
| Score-reviewed-in-session rate | [≥ target] | [..] |
| Time-to-act on not-on-track | [≤ N sessions/days] | [..] |
| Risk-flag follow-up rate | [100%] | [..] |

────────────────────────────────────────────────────────
CHANGE MANAGEMENT + PHASING
Stakeholder engagement: [sponsorship, champions]
Objection handling: [common clinician objections + responses]
Pilot: [subset/program] — success criteria: [..] — before full rollout
Feedback / iteration cycle: [PDSA-style review interval]
```

## Verification

- [ ] Practice and caseload profiled; dominant domains identified.
- [ ] Core battery matched to domains with one primary measure each; published bands stated; burden kept routine.
- [ ] Cadence policy defines baseline, in-treatment frequency, episode-end, follow-up, and a minimum auditable standard with program-specific rules.
- [ ] End-to-end workflow specified so scores are surfaced AND reviewed in session (loop closes), with documentation linkage.
- [ ] Workflow designed to confirmed EHR/platform capabilities; gaps flagged.
- [ ] Roles assigned across administer → score → surface → review → register → act.
- [ ] Risk-alert protocol defines trigger, owner, action, and time standard (item-9 / PCL-5 / deterioration).
- [ ] Training plan includes didactics, in-session-review skills practice, competency check, and supervision integration.
- [ ] Dashboards + registry-review cadence defined; not-on-track escalation routed to non-response decision tree.
- [ ] Fidelity metrics defined with numeric targets and owners (completeness, review-in-session, time-to-act, risk-follow-up).
- [ ] Change-management approach includes objection handling and a pilot with success criteria before full rollout.
- [ ] No fabricated norms, licensing, or platform features; unknowns flagged with `[clinician input required]`.
