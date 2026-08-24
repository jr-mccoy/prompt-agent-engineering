---
title: "Clinical Supervision Note Drafter"
category: psychology/documentation
description: "Document a clinical supervision session (supervisor or supervisee perspective): cases reviewed, interventions taught, parallel-process observations, supervisee competencies advanced, and plan."
techniques:
  - ST-04
  - DT-02
  - QA-01
  - QA-04
  - CM-02
difficulty: intermediate
tags:
  - clinical-supervision
  - supervisor-documentation
  - supervisee-documentation
  - licensure-hours
  - parallel-process
  - countertransference
intended_use: model-testing
updated: "2026-05-08"
related_prompts:
  - domain-psychology/supervision-professional/psychology_therapeutic_technique_explainer.md
  - domain-psychology/diagnostic-formulation/psychology_case_conceptualization_framework.md
---

# Clinical Supervision Note Drafter

## Objective

Produce a clinical supervision note suitable for both:

1. **Supervisor's record** for risk-management, regulatory, and program-quality purposes.
2. **Supervisee's licensure record** for accruing supervision hours toward licensure (LCSW, LPC, LMFT, psychologist, etc.) where state/board rules require structured supervision documentation.

The note must:

- Identify cases reviewed and at what depth.
- Document interventions / techniques taught and modeled.
- Capture parallel-process and countertransference observations.
- Document supervisee competencies advanced (mapped to a competency framework when applicable).
- Document any risk-management or ethics consultation.
- Specify supervision plan / development goals.

## When to Use

- Weekly or biweekly individual supervision sessions for pre-licensed clinicians.
- Group supervision (with per-supervisee blocks).
- Consultation-as-supervision arrangements for licensed clinicians (when documented as supervision).
- Required documentation for supervisee's hours log submitted to a state board.

## Inputs / Context

- Supervision metadata: date, duration, modality (in-person / telesupervision), supervisor name & credentials, supervisee name & credentials/pre-license status, supervision contract on file.
- Supervisee licensure track and board (e.g., "California BBS LCSW track, 3000 hours required, 1500 face-to-face").
- Cases reviewed (de-identified or initials per supervision agreement): presenting concern, ICD-10, current focus.
- Specific clinical questions the supervisee brought.
- Interventions / techniques taught or modeled.
- Parallel-process or countertransference observations.
- Risk / ethics issues consulted on (suicidality, mandated reporting, dual relationships, scope of practice).
- Competency framework used (e.g., AAMFT core competencies, ACA core competencies, APA Profession-Wide Competencies, AASCB ACS).
- Plan: cases to follow, readings, recordings to bring, skill goals.
- Supervisee's signature for hours-logging if required.

## Constraints

### Must

- Output the following labeled sections in order: **Supervision Metadata**, **Cases Reviewed**, **Clinical Questions Brought**, **Interventions / Techniques Taught**, **Parallel Process / Countertransference Observations**, **Risk Management / Ethics Consultation**, **Competencies Advanced**, **Supervisee's Self-Evaluation Notes**, **Supervisor's Feedback**, **Plan**, **Hours Logged**, **Signatures**.
- Cases reviewed listed in a row-by-row table with depth (brief mention / case discussion / case formulation / case presentation / live observation / recording review).
- Interventions taught include named technique + how taught (didactic / modeling / role-play / observation feedback / homework).
- Risk Management / Ethics block must be present even when content is "no risk-management or ethics issues this session."
- Competencies advanced mapped to a named competency framework when applicable.
- Hours Logged: supervised face-to-face (clinical) hours covered, individual supervision hours, group supervision hours where relevant.
- Both supervisor and supervisee signature lines.

### Must Not

- Do not document supervision hours that aren't accrued (face-to-face clinical work since last supervision).
- Do not name clients beyond the supervision agreement's de-identification standard.
- Do not omit the Risk/Ethics block.
- Do not mix peer consultation and formal supervision unless the supervision contract permits and the documentation makes clear which it is.
- Do not fabricate; flag missing inputs.

## Instructions

1. Compile metadata; verify supervision contract is on file.
2. List cases reviewed in a table with depth tag.
3. Document clinical questions the supervisee brought.
4. Document techniques/interventions taught with how-taught tag.
5. Capture parallel-process / countertransference observations (these are diagnostically informative and clinically useful).
6. Document any risk-management or ethics consultation; if none, write "None this session."
7. Map competencies advanced to a named framework.
8. Capture supervisee's self-evaluation and supervisor's feedback.
9. State plan: cases to follow, readings, recordings to bring, skill goals.
10. Log hours per the supervisee's board rules.
11. Run verification.

## Output Format

```
=== CLINICAL SUPERVISION NOTE ===

SUPERVISION METADATA
Date: [YYYY-MM-DD]    Time In/Out: [HH:MM–HH:MM]    Duration: [N min]
Modality: [In-person / Telesupervision (platform: ...)]
Supervisor: [Name, credentials, license #, supervisor designation if board-required]
Supervisee: [Name, credentials, pre-license status, board, license # if applicable]
Supervision contract on file: signed [YYYY-MM-DD]    Frequency: [...]    Type: [Individual / Group / Triadic]
Licensure track: [Board / Hours required total / Hours required individual / Hours required group / Recording-review requirement]

CASES REVIEWED
| Case ID | Diagnosis (primary) | Focus today | Depth |
|---------|---------------------|-------------|-------|
| Pt 1    | [F##.##]            | [...]       | [Brief mention / Case discussion / Case formulation / Case presentation / Live observation / Recording review] |
| Pt 2    | [F##.##]            | [...]       | [...] |
| Pt 3    | [F##.##]            | [...]       | [...] |

CLINICAL QUESTIONS BROUGHT
- [Question or stuck point #1, with case ID.]
- [Question #2.]

INTERVENTIONS / TECHNIQUES TAUGHT
- [Named technique #1 — taught via: didactic / modeling / role-play / observation feedback / homework.]
- [Named technique #2 — ...]

PARALLEL PROCESS / COUNTERTRANSFERENCE OBSERVATIONS
[Specific observations: e.g., "Supervisee's avoidance of confronting client's substance minimization parallels the client's own avoidance; named in supervision and tied to supervisee's conflict-avoidance pattern noted in prior sessions. Plan: practice direct feedback in role-play next supervision."]

RISK MANAGEMENT / ETHICS CONSULTATION
[Specific issues: suicidality stratification, mandated reporting decision, dual-relationship analysis, scope-of-practice question, confidentiality dilemma.]
[If none: "No risk-management or ethics issues this session."]

COMPETENCIES ADVANCED
Framework: [APA Profession-Wide Competencies / AAMFT Core Competencies / ACA / AASCB ACS / Program-specific]
- [Competency name — observable advance — evidence from supervision.]
- [...]

SUPERVISEE'S SELF-EVALUATION NOTES
[Supervisee's stated strengths, growth edges, blind spots noticed this period.]

SUPERVISOR'S FEEDBACK
[Specific reinforcement and specific developmental feedback. Identify any concerns about safety, clinical judgment, or competency that require monitoring.]

PLAN
- Cases to follow next supervision: [list with focus]
- Recording to bring: [Case ID + segment]
- Reading / training: [...]
- Skill goals for next interval: [...]
- Outside consultation if needed: [Yes / No, regarding what]

HOURS LOGGED
Supervised face-to-face clinical hours since last supervision: [N]
Individual supervision hours this session: [N]
Group supervision hours this session: [N]
Cumulative toward licensure: [Total / Individual / Group]

SIGNATURES
Supervisor: __________________  Date: ___________
Supervisee: __________________  Date: ___________
```

## Verification

- [ ] All labeled sections present and in order.
- [ ] Cases-reviewed table present with depth tag.
- [ ] Clinical questions documented.
- [ ] Interventions taught include how-taught tag.
- [ ] Parallel-process / countertransference block present.
- [ ] Risk-management / ethics block present (or explicit "none this session").
- [ ] Competencies mapped to a named framework.
- [ ] Hours logged per board requirements.
- [ ] Both signature lines present.
- [ ] Gaps flagged; nothing fabricated.
