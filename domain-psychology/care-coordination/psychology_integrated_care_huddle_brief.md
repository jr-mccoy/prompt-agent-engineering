---
title: "Integrated / Collaborative-Care Huddle Brief"
category: psychology/care-coordination
description: "Produce a concise registry-style huddle brief on shared collaborative-care panel patients for the BHCM, PCP, and consulting psychiatrist: target symptom scores, treatment-to-target status, and recommendations."
techniques:
  - DS-02
  - DT-01
  - ST-04
  - CM-01
  - QA-04
difficulty: intermediate
intended_use: model-testing
tags:
  - collaborative-care
  - integrated-care
  - CoCM
  - measurement-based-care
  - treat-to-target
  - registry
  - care-coordination
updated: "2026-06-08"
related_prompts:
  - domain-psychology/care-coordination/psychology_pcp_communication_note.md
  - domain-psychology/care-coordination/psychology_warm_handoff_narrative.md
  - domain-psychology/measurement-based-care/psychology_individual_rom_trajectory_analyzer.md
  - domain-psychology/treatment-planning/psychology_measurement_based_care_plan.md
---

# Integrated / Collaborative-Care Huddle Brief

## Objective

Produce a concise, registry-style **collaborative-care (CoCM) huddle brief** for the weekly caseload review among the Behavioral Health Care Manager (BHCM), the primary care physician(s), and the consulting psychiatrist. For a shared panel, the brief surfaces each patient's **target symptom scores and trajectory**, their **treatment-to-target status** (improving / not improving / in remission), time in treatment, and a **specific recommendation** for the patient(s) the team should act on this week — prioritizing those who are not improving. The brief is internal to the integrated-care team, applies minimum-necessary, and flags any patient with active risk for immediate attention.

## When to Use

- The weekly systematic case review (caseload consultation) in a Collaborative Care Model program.
- Preparing the psychiatric consultant's review list of patients not improving as expected.
- A daily/standing integrated-primary-care huddle on shared behavioral-health patients.
- Triaging which panel patients need a treatment change, intensification, or step-up this cycle.

## Inputs / Context Required

- **Panel / registry data**: for each patient — primary target condition, baseline and most recent measure scores, dates, sessions/contacts completed, weeks in treatment.
- **Measures in use**: PHQ-9 (depression), GAD-7 (anxiety), PCL-5 (PTSD), AUDIT/DAST (SUD), or program-specific.
- **Treat-to-target thresholds**: remission and response definitions per measure (e.g., PHQ-9 < 5 remission; ≥ 50% reduction response).
- **Current treatment**: psychotherapy contacts, medications and prescriber, recent changes.
- **Risk flags**: any patient with elevated suicidality item, recent crisis, or safety concern.
- **Roles present at huddle**: BHCM, PCP(s), consulting psychiatrist.
- `[clinician input required: program's not-improving threshold — e.g., < 5-point PHQ-9 drop by week 10–12]`
- `[clinician input required: which patients are new to the registry this cycle vs. ongoing]`

## Constraints

### Must

- Present a **registry-style summary line** per patient: identifier, target condition, measure (baseline → most recent, date), weeks in treatment, contacts completed, treat-to-target status.
- Classify each patient's **treat-to-target status**: New / Improving (on track) / Not improving (flag) / In remission / Relapse.
- **Prioritize the not-improving and at-risk patients** to the top of the action list — the huddle's purpose is to catch patients stalling on the registry.
- For each prioritized patient, give a **specific, actionable recommendation** (e.g., increase dose, augment, switch, add behavioral activation, schedule psychiatric consult, step up LOC).
- Surface any **active-risk patient** in a dedicated flag at the top; risk patients are reviewed first regardless of score trend.
- Keep to **minimum-necessary**: clinical detail sufficient for caseload decisions, not full notes. This is an internal integrated-care-team document.
- Note **CoCM billing** context where relevant (initial month 99492; subsequent months 99493; each additional 30 min 99494; general BHI 99484) tied to the care manager's tracked time.
- Flag missing registry data as `[clinician input required: ...]`; do not fabricate scores, dates, or weeks-in-treatment.

### Must Not

- Do not bury a not-improving or at-risk patient below routine on-track patients.
- Do not present scores without dates and baseline anchors (a single number is uninterpretable).
- Do not give a status without a recommendation for flagged patients.
- Do not expand into full progress-note narratives — this is a triage brief.
- Do not fabricate registry values, trajectory data, or remission status.
- Do not omit the active-risk flag when a suicidality item or crisis is present.

## Instructions

1. Pull the registry rows; for each patient compute weeks in treatment, baseline → most recent score, and percent change.
2. Apply the treat-to-target rules to classify each patient (New / Improving / Not improving / Remission / Relapse).
3. Scan for active-risk flags (elevated PHQ-9 item 9, recent crisis, safety event) and pull those patients to the RISK FLAGS block.
4. Build the prioritized action list: at-risk first, then not-improving, then patients nearing remission (for step-down).
5. For each prioritized patient, write one specific recommendation the team can decide on in the huddle.
6. Provide the full panel snapshot table for situational awareness.
7. Note CoCM billing/time context where relevant.
8. Run verification.

## Output Format

```
=== COLLABORATIVE-CARE HUDDLE BRIEF ===

HUDDLE DATE: [YYYY-MM-DD]    PANEL: [Clinic / program]
TEAM PRESENT: BHCM [name] · PCP [name] · Consulting Psychiatrist [name]
REGISTRY AS OF: [YYYY-MM-DD]    Panel size: [N]    Flagged for review: [N]

────────────────────────────────────────────────────────
RISK FLAGS (review first)
| ID | Concern | Last contact | Action needed |
|----|---------|--------------|---------------|
| [..] | [Elevated PHQ-9 item 9 / recent crisis / safety event] | [date] | [Same-day BHCM outreach / psych consult] |
[If none: "No active-risk flags this cycle."]

────────────────────────────────────────────────────────
PRIORITIZED ACTION LIST (not-improving + step-decision)
1. [ID] — [Condition] — [Measure: baseline X → most recent Y (date)], wk [N], status: NOT IMPROVING
   Current tx: [meds + prescriber / therapy contacts]
   Recommendation: [Specific — e.g., "Increase sertraline 50→100 mg; re-measure PHQ-9 in 2 wk."]
2. [ID] — [...] — status: [Not improving / Nearing remission → step-down]
   Recommendation: [...]

────────────────────────────────────────────────────────
PANEL SNAPSHOT (registry view)
| ID | Target condition | Measure | Baseline | Most recent (date) | Δ | Weeks | Contacts | Status |
|----|------------------|---------|----------|--------------------|---|-------|----------|--------|
| [..] | [Depression]   | PHQ-9   | [X]      | [Y] (date)         | [−Δ] | [N] | [N]      | [Improving] |
| [..] | [Anxiety]      | GAD-7   | [X]      | [Y] (date)         | [−Δ] | [N] | [N]      | [Not improving] |

Status key: New | Improving (on track) | Not improving (flag) | In remission | Relapse

────────────────────────────────────────────────────────
TREAT-TO-TARGET RULES (this program)
Response: [≥ 50% reduction from baseline]    Remission: [PHQ-9 < 5 / GAD-7 < 5]
Not-improving threshold: [clinician input required: e.g., < 5-point PHQ-9 drop by wk 10–12]

NOTES / FOLLOW-UP
- [Carry-forward items, pending labs, prior-auth status]

Billing context (CoCM): [99492 initial mo / 99493 subsequent / 99494 add'l 30 min / 99484 BHI] — per tracked care-manager time.
Minimum-necessary: internal integrated-care-team document; not for external release without ROI.
```

## Verification

- [ ] Each patient line shows identifier, target condition, baseline → most recent score with date, weeks in treatment, contacts, and status.
- [ ] Treat-to-target status assigned to every panel patient.
- [ ] Active-risk patients surfaced in a top RISK FLAGS block and reviewed first.
- [ ] Not-improving patients prioritized to the action list above on-track patients.
- [ ] Each prioritized patient has a specific, actionable recommendation.
- [ ] Treat-to-target rules (response / remission / not-improving) stated.
- [ ] Brief stays at triage altitude — no full progress-note narratives.
- [ ] CoCM billing context noted where relevant.
- [ ] Document marked minimum-necessary / internal; external release gated on ROI.
- [ ] No fabricated scores, dates, or weeks-in-treatment; gaps flagged with `[clinician input required]`.
```
