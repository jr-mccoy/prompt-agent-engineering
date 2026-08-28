---
title: "Postpartum Psychosis Recognition and Emergency Referral"
category: psychology/populations/perinatal
description: "Recognize postpartum psychosis as a psychiatric emergency, stratify urgency, screen infant safety, and execute same-day disposition (ED / psychiatric admission / 988) with risk-reassessment hooks."
techniques:
  - RT-02
  - RT-04
  - DS-02
  - QA-04
  - CM-01
difficulty: advanced
intended_use: model-testing
tags:
  - perinatal
  - postpartum-psychosis
  - psychiatric-emergency
  - infant-safety
  - infanticide-risk
  - referral
  - disposition
  - civil-commitment
  - 988
  - risk-assessment
updated: "2026-06-08"
related_prompts:
  - domain-psychology/populations/perinatal/psychology_perinatal_mood_anxiety_screen_interpretation.md
  - domain-psychology/populations/perinatal/psychology_perinatal_options_pregnancy_lactation.md
  - domain-psychology/risk-crisis/psychology_columbia_suicide_risk_assessment.md
  - domain-psychology/risk-crisis/psychology_civil_commitment_narrative.md
---

# Postpartum Psychosis Recognition and Emergency Referral

## Objective

Postpartum psychosis is a **psychiatric emergency**. This prompt drives same-day recognition, urgency stratification, and disposition for a postpartum client presenting with possible psychotic, manic, or rapidly fluctuating symptoms. It:

1. Recognizes the **red-flag cluster**: rapid onset (typically within days to the first 2 weeks postpartum), **waxing/waning sensorium** and confusion, marked **mood lability**, delusions (often infant-focused), hallucinations, and disorganization.
2. Screens explicitly for **infanticidal and suicidal ideation** and **infant safety**.
3. Stratifies urgency and routes to **same-day** disposition: emergency department, psychiatric (often inpatient) evaluation, crisis services, or **988**.
4. Distinguishes postpartum psychosis from postpartum depression, severe anxiety/OCD intrusive thoughts (ego-dystonic, not delusional), and the transient "baby blues."
5. Embeds **risk-reassessment hooks** and an escalation pathway, and links to civil-commitment narrative support when an involuntary hold is being considered.

This is not a watchful-waiting screen. Suspected postpartum psychosis is treated as emergent until proven otherwise.

## When to Use

- Any postpartum client (typically first weeks; risk extends across the early postpartum) presenting with new psychotic features, confusion, severe insomnia with hyperactivity, mania, or rapidly fluctuating mental status.
- When a screening tool (e.g., positive EPDS item 10, or collateral report of "she's not making sense") raises concern for a thought disorder rather than a mood-only presentation.
- When a partner/family/OB/pediatrician reports rapid behavioral change, bizarre beliefs about the infant, or the client seems "not herself" in a disorganized way.
- When deciding whether a presentation requires same-day emergency evaluation vs. routine perinatal mood care.

## When NOT to Use

- For mood/anxiety screening interpretation without psychotic/manic/confusional features — use `psychology_perinatal_mood_anxiety_screen_interpretation.md`.
- For routine treatment-options planning — use the pregnancy/lactation treatment prompt.
- For pure suicide-risk structured assessment in the absence of psychosis — use `psychology_columbia_suicide_risk_assessment.md` (still used here as an embedded step).

## Inputs / Context Required

- **Postpartum timing:** days/weeks since delivery.
- **Presenting features:** onset speed; sensorium/orientation; mood lability; delusions (content, infant-focused?); hallucinations (command?); disorganization; sleep (severe insomnia despite exhaustion); insight.
- **Collateral report:** from partner/family/OB/pediatrics (postpartum psychosis insight is often impaired — collateral is essential).
- **Ideation screen:** suicidal ideation; **infanticidal/harm-to-infant ideation**; command hallucinations; plan/intent/means.
- **Infant context:** who is currently supervising the infant; is the infant currently safe; access of the client to the infant.
- **History:** bipolar disorder, prior postpartum psychosis (major recurrence risk factor), prior psychiatric admissions, current medications, substance use, recent obstetric complications, delirium contributors (infection, thyroid, sleep deprivation severity).
- **Setting/resources:** location (clinic/home/telehealth), availability of partner/family, distance to ED, crisis line/mobile crisis access.
- `[clinician input required: current infant supervision arrangement and whether the client is alone with the infant right now]`

## Constraints

### Must

- Treat suspected postpartum psychosis as a **psychiatric emergency requiring same-day evaluation** — default to escalation, not observation.
- Obtain **collateral** information; do not rely solely on the client's self-report given typically impaired insight.
- Screen explicitly and document **suicidal AND infanticidal/harm-to-infant ideation**, including command hallucinations.
- Complete an **infant-safety screen**: confirm who is supervising the infant and whether the infant is currently safe; arrange supervision before the client is left alone with the infant if any concern exists.
- Assign an **urgency tier** and a corresponding **same-day disposition** with a concrete handoff (named ED/crisis/psychiatry, transport plan, who accompanies).
- Consider **medical mimics/contributors** (delirium, thyroid, infection, substance) and flag medical evaluation as part of emergency workup — do not assume primary psychiatric cause without medical clearance.
- Provide **988** and emergency (911/ED) routing information and an escalation pathway.
- When involuntary hold is under consideration, route to `psychology_civil_commitment_narrative.md` and document the danger-to-self/danger-to-others/grave-disability basis.
- Flag all `[clinician input required: ...]` gaps.

### Must Not

- Do not send the client home for routine follow-up when red flags are present.
- Do not characterize ego-dystonic intrusive thoughts of harm (postpartum OCD) as homicidal intent — distinguish them; but do not dismiss harm ideation as "just OCD" without assessment.
- Do not leave the infant-safety question unresolved or undocumented.
- Do not rely on a single MSE snapshot given the waxing/waning course — document the fluctuation and the need for re-assessment.
- Do not fabricate collateral, supervision arrangements, or disposition acceptance.

## Differential and Red-Flag Reference

| Presentation | Onset | Key features | Insight | Default disposition |
|--------------|-------|--------------|---------|---------------------|
| Baby blues | Days 2–5, resolves ~2 wks | Tearfulness, lability, mild | Intact | Reassure + monitor |
| Postpartum depression | Weeks–months | Depressed mood, anhedonia, guilt | Usually intact | Mood-screen pathway / treatment planning |
| Postpartum anxiety / OCD | Weeks | **Ego-dystonic** intrusive harm thoughts, avoidance, distress about the thoughts | Intact — distressed BY thoughts | Anxiety/OCD treatment; assess but not delusional |
| **Postpartum psychosis** | **Rapid — often days to ~2 wks** | **Confusion/waxing-waning sensorium, mood lability, delusions (often infant-focused), hallucinations (may be command), disorganization, severe insomnia** | **Impaired** | **EMERGENCY — same-day psychiatric evaluation, usually inpatient** |
| Delirium / medical | Variable | Fluctuating consciousness, disorientation, medical signs | Impaired | **Medical emergency — ED + medical workup** |

**Highest-concern combination:** psychotic features + command/harm-focused ideation toward self or infant + impaired insight + the client currently has unsupervised access to the infant → immediate emergency intervention and infant protection.

## Urgency Tier and Disposition Reference

| Tier | Criteria | Disposition |
|------|----------|-------------|
| **EMERGENT (now)** | Active suicidal/infanticidal ideation or command hallucinations; acute confusion; client alone with infant and unsafe; cannot maintain safety | 911/ED immediately; do not leave client alone with infant; arrange infant supervision/protection; psychiatric admission likely; consider involuntary hold |
| **URGENT (same day)** | Red-flag psychotic/manic cluster without active harm ideation; insight impaired; collateral confirms rapid change | Same-day ED or psychiatric evaluation; warm handoff + transport plan; supervision arranged before discharge home |
| **HIGH-CONCERN (expedited)** | Concerning but ambiguous (possible severe OCD vs. early psychosis); fluctuating | Same-day/next-day psychiatric consult; safety plan; collateral monitoring; re-assess within hours; low threshold to escalate |

988 (Suicide & Crisis Lifeline) and local mobile crisis are adjuncts at every tier; ED/911 is the pathway for emergent risk.

## Instructions

1. **Establish timing and obtain collateral.** Confirm postpartum interval. Given impaired insight, gather collateral from partner/family/OB/pediatrics immediately.

2. **Map the red-flag cluster.** Document onset speed, sensorium/orientation (and any waxing/waning), mood lability, delusions (content; infant-focused?), hallucinations (command?), disorganization, and severe insomnia.

3. **Run the differential** against the reference table — explicitly distinguish postpartum OCD (ego-dystonic, insight intact) from psychosis (delusional, insight impaired), and flag medical/delirium contributors.

4. **Screen ideation.** Assess suicidal AND infanticidal/harm-to-infant ideation, command hallucinations, plan/intent/means. Route to `psychology_columbia_suicide_risk_assessment.md` for the structured suicide assessment.

5. **Infant-safety screen.** Determine who is supervising the infant right now and whether the infant is safe. If any concern, arrange supervision/protection before proceeding and document it.

6. **Stratify urgency** (Emergent / Urgent / High-concern) and assign the corresponding same-day disposition with a concrete handoff.

7. **Flag medical workup** (delirium, thyroid, infection, substances) as part of emergency evaluation; do not assume primary psychiatric without clearance.

8. **If involuntary hold is being considered,** document the DTS/DTO/grave-disability basis and route to `psychology_civil_commitment_narrative.md`.

9. **Execute the disposition and document** the escalation pathway, accompaniment, transport, and notifications (OB, prescriber, support person).

10. Run verification.

## Output Format

```
=== POSTPARTUM PSYCHOSIS — RECOGNITION & EMERGENCY DISPOSITION ===

Client: [Initials/MRN]    Date/Time: [YYYY-MM-DD HH:MM]    Clinician: [Name, credentials]
Postpartum interval: [N days/weeks]    Setting: [Clinic / Home / Telehealth / ED]
Collateral source(s): [Partner / family / OB / pediatrics — name/relationship]

─────────────────────────────────────────
RED-FLAG CLUSTER
─────────────────────────────────────────
Onset speed: [Rapid (days–2wk) / Subacute / Gradual]
Sensorium / orientation: [Clear / Confused / WAXING-WANING — describe]
Mood lability: [Present — describe / Absent]
Delusions: [Present — content; infant-focused? / Absent]
Hallucinations: [Present — modality; COMMAND? content / Absent]
Disorganization (thought/behavior): [Present — describe / Absent]
Sleep: [Severe insomnia despite exhaustion / Other]
Insight: [Impaired / Partial / Intact]

─────────────────────────────────────────
DIFFERENTIAL
─────────────────────────────────────────
Most likely: [Postpartum psychosis / Delirium-medical / Postpartum OCD (ego-dystonic) / PPD / Bipolar episode / Mixed]
Distinguished from postpartum OCD: [Yes — intrusive thoughts ego-dystonic & insight intact / Concern is delusional]
Medical/delirium contributors flagged: [Thyroid / infection / substance / sleep — workup needed: Yes/No]

─────────────────────────────────────────
IDEATION SCREEN  (route to C-SSRS)
─────────────────────────────────────────
Suicidal ideation: [None / Passive / Active — plan/intent/means]
Infanticidal / harm-to-infant ideation: [None / Present — content, command-driven?]
Command hallucinations (self or infant): [None / Present — describe]
Structured suicide assessment: [C-SSRS completed — result: ...]
[clinician input required: corroborating risk detail]

─────────────────────────────────────────
INFANT-SAFETY SCREEN  (MANDATORY)
─────────────────────────────────────────
Who is supervising the infant now: [...]
Is the infant currently safe: [Yes / No — action taken]
Client currently alone with infant: [Yes / No]
Supervision/protection arranged before client unsupervised with infant: [Yes — by whom / Not needed — rationale]
[clinician input required: confirm current arrangement]

─────────────────────────────────────────
URGENCY TIER & DISPOSITION
─────────────────────────────────────────
Tier: [EMERGENT / URGENT / HIGH-CONCERN]
Same-day disposition: [911/ED now / Same-day ED or psychiatric eval / Expedited psychiatric consult + safety plan]
Concrete handoff: [Facility name; accepting clinician; transport plan; who accompanies]
Crisis resources provided: [988 Suicide & Crisis Lifeline; local mobile crisis: ___]
Involuntary hold under consideration: [No / Yes → DTS/DTO/grave-disability basis documented; routed to civil-commitment narrative]
Notifications: [OB/midwife / prescriber-psychiatry / support person / pediatrics]

─────────────────────────────────────────
ESCALATION PATHWAY & RISK-REASSESSMENT HOOK
─────────────────────────────────────────
Escalate to 911/ED immediately if: emergence/worsening of harm or command ideation; infant unsafe;
acute confusion; inability to maintain safety; disposition refused with imminent risk.
Re-assess mental status frequently given WAXING-WANING course — a single reassuring MSE does not clear risk.
Re-screen interval until evaluated: [continuous / per crisis plan]
[clinician input required: client-specific tripwires + reassessment timing]

─────────────────────────────────────────
BILLING
─────────────────────────────────────────
Crisis/emergency service: [90839 (psychotherapy for crisis, first 60 min) / 90840 (add'l 30 min) as applicable]
[clinician input required]
```

## Verification

- [ ] Presentation treated as a psychiatric emergency by default; escalation favored over observation.
- [ ] Collateral obtained and documented (not sole reliance on client self-report).
- [ ] Red-flag cluster documented, including waxing/waning sensorium and infant-focused delusions/hallucinations.
- [ ] Differential explicitly distinguishes ego-dystonic postpartum OCD from delusional psychosis and flags medical/delirium contributors.
- [ ] Suicidal AND infanticidal/harm-to-infant ideation and command hallucinations screened; C-SSRS routed.
- [ ] Infant-safety screen completed: current supervisor identified, infant safety confirmed, supervision arranged if any concern.
- [ ] Urgency tier assigned with concrete same-day disposition and named handoff/transport/accompaniment.
- [ ] Medical workup flagged as part of emergency evaluation.
- [ ] 988 and ED/911 routing provided; escalation pathway documented.
- [ ] Civil-commitment narrative routing invoked if involuntary hold considered, with DTS/DTO/grave-disability basis.
- [ ] Risk-reassessment hook present and reflects the fluctuating course (single MSE does not clear risk).
- [ ] No fabricated collateral, supervision arrangement, or disposition acceptance.
- [ ] All gaps flagged with `[clinician input required: ...]`.
