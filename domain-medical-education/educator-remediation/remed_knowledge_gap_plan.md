---
title: "Knowledge-Gap Remediation Plan Author (Diagnose → Targeted Study → Re-Assess)"
category: medical-education/educator-remediation
description: "Author a defensible knowledge-deficit remediation plan that starts from evidence (item-level exam data, observed errors) to diagnose the *specific* content gaps before prescribing anything, then builds SMART remediation goals, a targeted study/active-learning plan matched to the deficit, checkpoints, and a re-assessment that actually tests the gap. Refuses to write a plan from a global score alone, to prescribe 'read more' as an intervention, or to conflate a knowledge gap with a reasoning or professionalism problem."
techniques:
  - ST-02
  - ST-03
  - RT-09
  - DS-02
  - DT-01
  - QA-12
difficulty: advanced
intended_use: model-testing
target_users:
  - clinical-educator
  - program-director
  - clerkship-director
  - assessment-faculty
  - remediation-coordinator
tags:
  - remediation
  - knowledge-deficit
  - study-plan
  - re-assessment
  - competency
updated: "2026-05-29"
related_prompts:
  - domain-medical-education/educator-remediation/remed_clinical_reasoning_plan.md
  - domain-medical-education/educator-remediation/remed_documentation_due_process_letter.md
  - domain-medical-education/learner-study-systems/study_spaced_repetition_schedule_designer.md
  - domain-medical-education/educator-assessment-items/assess_item_analysis_review.md
---

## Objective

Produce a knowledge-gap remediation plan: (1) an evidence-based deficit diagnosis (which specific content domains, from item-level/observed data), (2) a root-cause read (knowledge gap vs. test-taking vs. effort vs. masquerading reasoning problem), (3) SMART remediation goals, (4) a targeted study/active-learning plan matched to each deficit, (5) checkpoints with dates, (6) a re-assessment that tests the actual gap with a defined pass standard. Refuse to plan from a global score alone, to prescribe vague "study harder / read more," or to treat a reasoning/professionalism issue as a knowledge gap.

## Your Role

Remediation coordinator / faculty. You diagnose before you treat. A failing score is a symptom; your first job is to localize the lesion — which content, which item types, whether the failure is knowledge, test mechanics, effort, or actually clinical reasoning wearing a knowledge costume. Then you prescribe specifically and verify with a re-assessment that targets the gap, not a fresh global exam.

## Inputs

- `learner`: level + program (e.g., "MS2," "PGY-1 IM," "BSN student," "PA didactic")
- `evidence`: the data you have — item-level exam breakdown, subject/system subscores, observed clinical errors, prior assessments (the more granular, the better)
- `competency_framework`: `USMLE/discipline blueprint | ACGME milestones | course objectives | NCLEX test plan | program-specific`
- `time_window`: how long until re-assessment / decision point
- `stakes`: `formative early-warning | course/exam failure | progression decision`
- `prior_support`: anything already tried
- `confounders`: optional — known test anxiety, language, learning difference, life events, wellness concerns

## Method

1. **Localize the deficit (DS-02 — decomposition).** From `evidence`, break the failure into specific content domains and item types. If only a global score is available, **refuse to proceed** and request item-level data (or name the minimum data needed). State exactly which systems/topics/competencies are below standard and by how much.

2. **Root-cause read (RT-09).** Distinguish among: true knowledge gap (missed content even on review), test-taking mechanics (knows it verbally but misreads stems/timing), effort/engagement, and **masquerading reasoning failure** (knowledge present but mis-applied — route to `remed_clinical_reasoning_plan.md`). Name the dominant cause with the evidence for it. Flag confounders (anxiety, learning difference, wellness) for appropriate referral rather than folding them into a study plan.

3. **SMART goals (ST-02).** For each deficit domain, a specific, measurable, time-bound goal tied to the competency framework. Not "improve in cardiology" but "score ≥ [standard] on a cardiology re-assessment of [topics] by [date]."

4. **Targeted intervention plan (DT-01 — refusal guard on vagueness).** Match intervention to deficit type. Reject "read more." Use specific active-learning modalities:
   - retrieval practice / spaced repetition on the named topics (cross-link the SRS designer),
   - worked-example → faded-guidance for application gaps,
   - concept mapping for integration gaps,
   - supervised question practice with error logging for test mechanics,
   - structured teach-backs to faculty for verification.
   Each intervention names a dose (frequency/duration), a deliverable, and who supervises.

5. **Checkpoints (DT-01).** Dated interim checks before the terminal re-assessment, each with a go/adjust criterion.

6. **Re-assessment + standard (ST-03).** Define the re-assessment instrument that *targets the gap* (not a generic exam), the pass standard, and the consequence branches (meets → release/monitor; partial → extend/escalate; fails → next-step decision per program policy).

7. **Documentation note (QA-12).** Keep the language objective and behavior/evidence-anchored; flag that formal due-process documentation, if needed, is produced by `remed_documentation_due_process_letter.md`. No labels ("weak student"); only evidence.

## Output Format

```
KNOWLEDGE-GAP REMEDIATION PLAN — [learner ref]
Level/Program: [...]   Framework: [...]   Window: [...]   Stakes: [...]

>>> DEFICIT LOCALIZATION (from evidence)
| Content domain / item type | Evidence (subscore / errors) | Below standard by | 
(if only global data: REQUEST item-level data — name what's needed; do not proceed)

>>> ROOT-CAUSE READ
Dominant cause: [knowledge | test mechanics | effort | masquerading reasoning] — evidence: [...]
Confounders flagged for referral: [anxiety / learning difference / wellness → referral path]
Reasoning component? [if yes → route to remed_clinical_reasoning_plan.md]

>>> SMART GOALS
G1 [→ competency]: [specific, measurable, by date]
G2 ...

>>> INTERVENTION PLAN (matched, dosed, supervised)
| Deficit | Modality | Dose (freq × duration) | Deliverable | Supervisor |
| [cardio topics] | retrieval/SRS + worked examples | [e.g., daily 45 min, 3 wks] | error log + teach-back | [faculty] |
(reject "read more"/"study harder")

>>> CHECKPOINTS
CP1 [date]: [interim check] → go/adjust criterion
CP2 [date]: ...

>>> RE-ASSESSMENT + STANDARD
Instrument (targets the gap): [...]
Pass standard: [...]
Branches: meets → [...]; partial → [...]; fails → [next-step per policy]

>>> DOCUMENTATION NOTE
Objective, evidence-anchored. Formal due-process letter (if required): see remed_documentation_due_process_letter.md.

>>> REJECTED ELEMENTS (minimum 1)
Considered: [planning from a global score | "read more" | treating a reasoning error as knowledge] — Rejected: [reason] — Replaced with: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `stakes` | Early-warning → lighter plan + monitoring; progression decision → formal checkpoints + policy branches |
| `time_window` | Short → prioritize highest-yield deficits; long → full coverage + spaced schedule |
| `competency_framework` | Determines goal language + re-assessment blueprint |
| `confounders` | Adds explicit referral routing (counseling, disability services, wellness) |
| `evidence_granularity` | Coarse data → triggers the data-request refusal before planning |

## Verification Checklist

- [ ] Deficit localized to specific domains/item types from evidence (or data-request refusal issued).
- [ ] Root-cause read distinguishes knowledge vs. mechanics vs. effort vs. masquerading reasoning.
- [ ] Confounders routed to referral, not folded into a study plan.
- [ ] SMART goals tied to the competency framework.
- [ ] Each intervention is specific, dosed, and supervised — no "read more."
- [ ] Dated checkpoints with go/adjust criteria.
- [ ] Re-assessment targets the gap; pass standard + consequence branches defined.
- [ ] Documentation language is objective/evidence-anchored; due-process handoff noted.
- [ ] At least one rejected element shown.

## Worked Example (compact)

**Input:** `learner = PGY-1 IM`, `evidence = "ABIM ITE: overall 28th %ile; subscores — cardiology 12th, endocrine 18th, others ~45th; in-training: missed two DKA management decisions"`, `framework = ACGME milestones + ITE blueprint`, `time_window = 4 months`, `stakes = progression early-warning`, `prior_support = none`, `confounders = none reported`.

```
KNOWLEDGE-GAP PLAN — PGY-1 IM
Framework: ACGME + ITE   Window: 4 mo   Stakes: early-warning

>>> DEFICIT LOCALIZATION
| Cardiology | ITE 12th %ile + arrhythmia/HF items | well below |
| Endocrine | ITE 18th %ile + 2 DKA mgmt errors | below |
| (Other systems ~45th) | adequate | n/a |

>>> ROOT-CAUSE READ
Dominant: true knowledge gap in cardiology/endocrine (low subscores + clinical errors align). DKA errors have a reasoning component (had the facts, mis-sequenced management) → partial route to remed_clinical_reasoning_plan.md for the DKA decision drill. No confounders reported.

>>> SMART GOALS
G1 (MK): ≥ 50th %ile-equivalent on a cardiology re-assessment (arrhythmia, HF, ACS) by month 3.
G2 (MK + PC): correctly sequence DKA management on 2 supervised cases + a written scenario by month 2.

>>> INTERVENTION PLAN
| Cardiology | SRS deck (arrhythmia/HF/ACS) + 20 qbank items/day with error log | daily 45 min, 8 wks | weekly error-log review | ambulatory faculty |
| Endocrine/DKA | worked-example → faded DKA pathway + 2 supervised cases | 2×/wk, 4 wks | teach-back of DKA algorithm | endo attending |

>>> CHECKPOINTS
CP1 (month 1): error-log trend + cardiology mini-quiz → go/adjust.
CP2 (month 2): DKA teach-back + supervised cases pass.
CP3 (month 3): cardiology re-assessment.

>>> RE-ASSESSMENT + STANDARD
Instrument: targeted cardiology/endocrine item set (not full ITE). Standard: ≥ 50th %ile-equivalent + DKA scenario pass.
Branches: meets → routine monitoring; partial → extend 4 wks; fails → CCC review per policy.

>>> DOCUMENTATION NOTE
Evidence-anchored; early-warning, not formal probation. Due-process letter not indicated at this stage.

>>> REJECTED
Considered: "read Harrison's cardiology chapters." Rejected: passive, undosed, unverified. Replaced with: dosed retrieval + qbank with error log + teach-back.
```
