---
title: "Clinical-Reasoning Remediation Plan Author (Diagnose the Failure Type → Targeted Practice)"
category: medical-education/educator-remediation
description: "Author a clinical-reasoning remediation plan that first localizes *where* in the reasoning process the learner fails — data gathering, problem representation, hypothesis generation, hypothesis evaluation, premature closure, or illness-script gaps — using evidence (think-aloud, chart review, case observation), then prescribes practice matched to that failure type, supervised deliberate practice with structured reflection, checkpoints, and a re-assessment of reasoning (not content). Refuses to treat a reasoning failure as a knowledge gap, or to prescribe 'see more patients' as the intervention."
techniques:
  - ST-02
  - ST-03
  - RT-09
  - DS-29
  - DT-01
  - QA-12
difficulty: advanced
intended_use: model-testing
target_users:
  - clinical-educator
  - program-director
  - clerkship-director
  - remediation-coordinator
tags:
  - remediation
  - clinical-reasoning
  - think-aloud
  - illness-scripts
  - deliberate-practice
updated: "2026-05-29"
related_prompts:
  - domain-medical-education/educator-remediation/remed_knowledge_gap_plan.md
  - domain-medical-education/learner-clinical-reasoning/reason_illness_script_builder.md
  - domain-medical-education/learner-clinical-reasoning/reason_premature_closure_check.md
  - domain-medical-education/learner-clinical-reasoning/reason_dual_process_metacognition_coach.md
---

## Objective

Produce a clinical-reasoning remediation plan: (1) localize the failure point in the reasoning process from evidence, (2) confirm it's reasoning (not a knowledge gap masquerading), (3) SMART reasoning-specific goals, (4) practice matched to the failure type with supervised deliberate practice + structured reflection, (5) checkpoints, (6) a re-assessment that measures reasoning (think-aloud, script-concordance-style, or structured case) with a defined standard. Refuse to treat reasoning failure as knowledge, and refuse "just see more patients" as the prescription.

## Your Role

Faculty in clinical-reasoning remediation. You know reasoning fails in *locatable* ways, and each location has a different fix: a learner who gathers data poorly needs a different intervention than one who anchors and closes early. You diagnose the reasoning lesion with evidence (a think-aloud, a chart trail, a case observation), then prescribe deliberate, supervised practice with reflection — not undirected clinical volume.

## Inputs

- `learner`: level + setting (e.g., "MS3 medicine," "PGY-2 EM," "NP student")
- `evidence`: think-aloud transcript, observed case(s), chart review of decisions, presentation recordings, faculty narratives
- `presenting_concern`: what triggered the referral (e.g., "misses can't-miss diagnoses," "premature closure," "disorganized presentations," "orders without a hypothesis")
- `framework`: `ACGME milestones (PC/MK) | program competencies | CanMEDS Medical Expert`
- `time_window` and `stakes`
- `confounders`: optional — knowledge gaps present, anxiety, language, wellness

## Method

1. **Localize the reasoning failure (RT-09 + DS-29 — reasoning-failure taxonomy).** From evidence, place the failure in the process:
   - **Data acquisition** — incomplete/biased history & exam.
   - **Problem representation** — can't form an accurate one-liner / semantic qualifiers.
   - **Hypothesis generation** — too narrow, misses categories (no schema).
   - **Hypothesis evaluation** — doesn't weigh evidence / misuses test characteristics.
   - **Premature closure / bias** — anchors, ignores disconfirming data.
   - **Illness-script gaps** — scripts thin or distorted.
   - **Metacognition** — no System-1/2 awareness, no self-monitoring.
   Name the dominant failure with the specific evidence.

2. **Knowledge vs. reasoning check (refusal guard).** Confirm the content knowledge is actually present (else route to `remed_knowledge_gap_plan.md`). Reasoning remediation assumes the facts are there but mis-applied. If knowledge is the real gap, say so and re-route.

3. **SMART reasoning goals (ST-02).** Specific to the located failure, measurable via a reasoning artifact (e.g., "produce an accurate problem representation with semantic qualifiers on 8/10 observed cases by [date]").

4. **Matched intervention (DT-01).** Pair the failure to a practice modality (cross-link learner-reasoning prompts):
   - data acquisition → structured history/exam frameworks + observed encounters with feedback,
   - problem representation → one-liner/semantic-qualifier drills,
   - hypothesis generation → schema building + illness-script construction,
   - evaluation → Bayesian/pretest-posttest drills,
   - premature closure → diagnostic time-out + premature-closure check + forced counter-DDx,
   - metacognition → dual-process coaching + structured reflection after each case.
   Each with dose, deliverable, and a supervising faculty doing think-aloud or observed cases.

5. **Structured reflection loop.** After each supervised case: learner articulates reasoning, faculty gives reasoning-focused feedback (not just the right answer), learner logs the reasoning move to change.

6. **Checkpoints + re-assessment (ST-03).** Dated interim observations; terminal re-assessment that measures *reasoning* — observed think-aloud, structured oral, or chart-stimulated recall — with a defined standard and consequence branches.

7. **Documentation note (QA-12).** Objective, behavior-anchored, evidence-cited. Due-process documentation via `remed_documentation_due_process_letter.md` if formal.

## Output Format

```
CLINICAL-REASONING REMEDIATION PLAN — [learner ref]
Level/Setting: [...]   Framework: [...]   Window: [...]   Stakes: [...]

>>> REASONING-FAILURE LOCALIZATION (from evidence)
Dominant failure: [data acquisition | problem representation | hypothesis generation | evaluation | premature closure | script gaps | metacognition]
Evidence: [specific think-aloud / case / chart observations]
Secondary contributors: [...]

>>> KNOWLEDGE-VS-REASONING CHECK
Content knowledge present? [yes → proceed | no → route to remed_knowledge_gap_plan.md]

>>> SMART GOALS (reasoning artifacts)
G1 [→ PC milestone]: [measurable via a reasoning artifact, by date]
G2 ...

>>> MATCHED INTERVENTION PLAN
| Failure point | Practice modality (+ cross-link) | Dose | Deliverable | Supervisor/method |
| premature closure | diagnostic time-out + counter-DDx drill | [n cases/wk] | reasoning log | think-aloud w/ faculty |

>>> STRUCTURED REFLECTION LOOP
Per case: learner articulates reasoning → faculty reasoning-focused feedback → logged reasoning move to change.

>>> CHECKPOINTS + RE-ASSESSMENT
CP1 [date]: observed think-aloud → go/adjust.
Terminal re-assessment: [observed think-aloud | structured oral | chart-stimulated recall] — standard: [...]
Branches: meets → [...]; partial → [...]; fails → [policy next-step].

>>> DOCUMENTATION NOTE
Objective/evidence-anchored; due-process letter if formal → remed_documentation_due_process_letter.md.

>>> REJECTED ELEMENTS (minimum 1)
Considered: ["see more patients" | treating it as a knowledge gap | giving the answer instead of coaching the move] — Rejected: [reason] — Replaced with: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `presenting_concern` | Selects the primary failure point and matched modality |
| `stakes` | Progression decision → formal observed re-assessment + policy branches |
| `framework` | Milestone vs. CanMEDS changes goal language |
| `confounders` | Co-existing knowledge gap → parallel knowledge plan; wellness/anxiety → referral |
| `setting` | Inpatient vs. clinic vs. ED changes case mix for practice |

## Verification Checklist

- [ ] Failure localized to a specific reasoning step with cited evidence.
- [ ] Knowledge-vs-reasoning check performed; re-routes if it's really knowledge.
- [ ] SMART goals measured via reasoning artifacts, not content scores.
- [ ] Interventions matched to the failure point, dosed, supervised, with think-aloud/observed method.
- [ ] Structured reflection loop coaches the reasoning move, not just the answer.
- [ ] Re-assessment measures reasoning (think-aloud / oral / CSR) with a standard + branches.
- [ ] Documentation objective and evidence-anchored.
- [ ] At least one rejected element shown.

## Worked Example (compact)

**Input:** `learner = MS3 medicine`, `evidence = "think-aloud on chest pain: locked on costochondritis at minute 1, didn't ask about exertion/risk factors, never considered ACS/PE/dissection"`, `presenting_concern = premature closure, narrow DDx`, `framework = ACGME PC`, `time_window = 6 wks`, `stakes = clerkship early-warning`, `confounders = knowledge appears adequate on questioning`.

```
CLINICAL-REASONING PLAN — MS3 medicine
Framework: ACGME PC   Window: 6 wks   Stakes: clerkship early-warning

>>> LOCALIZATION
Dominant: premature closure + narrow hypothesis generation. Evidence: anchored on costochondritis at 1 min; omitted exertional history/risk factors; no can't-miss category (ACS/PE/dissection) considered.
Secondary: thin chest-pain schema.

>>> KNOWLEDGE-VS-REASONING CHECK
On direct questioning, learner knows ACS features and PE risk factors → knowledge present. Confirmed reasoning problem.

>>> SMART GOALS
G1 (PC): On 8/10 observed chest-pain (and other complaint) cases, generate a can't-miss-inclusive DDx and an accurate one-liner before committing, by week 5.
G2: Demonstrate a diagnostic time-out (state disconfirming data + one alternative) on every observed case by week 4.

>>> MATCHED INTERVENTION
| premature closure | diagnostic time-out + premature-closure check + forced counter-DDx (cross-link reason_premature_closure_check) | 4 observed cases/wk | reasoning log | faculty think-aloud |
| narrow DDx / schema | chest-pain + 3 other schemas + illness scripts (reason_illness_script_builder) | 2/wk | built schemas | faculty review |
| metacognition | dual-process coaching (reason_dual_process_metacognition_coach) | weekly | reflection notes | preceptor |

>>> STRUCTURED REFLECTION LOOP
Each case: learner verbalizes DDx + one-liner → faculty asks "what would change your mind?" → logs the move (e.g., "always state a can't-miss alternative before committing").

>>> CHECKPOINTS + RE-ASSESSMENT
CP1 (wk 3): observed think-aloud → go/adjust. Terminal (wk 5–6): 3 observed think-aloud cases scored for breadth + closure-resistance. Standard: can't-miss-inclusive DDx + accurate problem rep on ≥ 8/10.
Branches: meets → release w/ monitoring; partial → extend; fails → clerkship director review.

>>> DOCUMENTATION NOTE
Evidence-anchored early-warning. No formal letter at this stage.

>>> REJECTED
Considered: "do more clinic to see more chest pain." Rejected: undirected volume won't fix anchoring. Replaced with: supervised time-out practice + schema building + reflection.
```
