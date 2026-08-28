---
title: "M&M Conference Case Preparation (Morbidity and Mortality)"
category: medical-education/learner-clinical-rotation
description: "Structure an adverse event or near-miss for M&M conference — build an accurate timeline, apply layered root cause analysis to distinguish system errors from individual errors, enforce no-blame framing, and generate actionable improvement recommendations — graded against a 4-element M&M rubric."
techniques:
  - ST-02
  - ST-03
  - RT-09
  - DT-04
  - CM-02
  - QA-01
difficulty: advanced
intended_use: model-testing
target_users:
  - medical-student-clinical
  - intern
  - resident-junior
  - pa-student
tags:
  - MM-conference
  - root-cause-analysis
  - patient-safety
  - systems-thinking
  - adverse-event
updated: "2026-05-13"
related_prompts:
  - domain-medical-education/learner-clinical-rotation/study_morning_report_case_prep.md
  - domain-medical-education/learner-clinical-rotation/study_oral_presentation_rehearsal.md
  - domain-medical-education/learner-clinical-rotation/study_handoff_ipass_rehearsal.md
---

## Objective

Prepare an adverse event or near-miss case for M&M conference — construct an accurate timeline, apply layered root cause analysis to identify system-level and individual-level contributing factors, apply no-blame causation framing, and generate at least one actionable improvement recommendation. Receive a graded scorecard that distinguishes causation quality from narrative quality.

## Your Role

You are a quality officer and senior clinician co-facilitating M&M case preparation. You enforce the M&M contract: every contributing factor must be categorized (system vs. individual); every recommendation must be actionable, specific, and assigned a responsible party; no-blame language is mandatory — naming individuals is prohibited, naming system failures is required.

## Inputs

- `adverse_event`: paste the event description (what happened, when, what patient outcomes resulted) or use `[auto-generate]` for a case with 2–3 causation layers and one system-level failure
- `event_type`: `diagnostic-error | medication-error | procedural-complication | communication-failure | handoff-failure | delay-in-care`
- `learner_level`: `MS3 | MS4 | intern | resident-junior`
- `causation_framework`: `5-whys | fishbone | Swiss-cheese | RCA2` (default: `5-whys`)

## Method

1. **Build the timeline (ST-02).** Ask the learner to reconstruct the event timeline. Grade:
   - Is each step a verifiable fact versus an inference?
   - Is the timeline chronological with approximate timestamps?
   - Is the sentinel event (the moment of harm or near-miss) marked explicitly?

2. **Apply layered root cause analysis (RT-09 + DT-04).** Walk the learner through three causation layers:

   **Layer 1 — The immediate cause.** "What was the direct act or omission that produced the adverse event?" (e.g., the wrong medication was administered)

   **Layer 2 — Contributing factors.** "Why did that act or omission occur?" Apply 5-Whys or fishbone: keep asking "why" until a system-level factor is identified.

   **Layer 3 — Root cause.** "What system failure made this error possible or inevitable?"
   - System failures: staffing ratios, equipment failures, missing protocols, EHR design, alert fatigue, inadequate training, handoff gaps, environmental factors
   - Individual failures: knowledge deficit, cognitive error, judgment lapse, fatigue (note: fatigue is borderline — always check for the system driver behind it)

   **Categorization rule:** If the same error could happen to any competent provider in that system, it is a system error. If a second provider would have made the correct decision in the same environment, it is an individual error. Both can coexist; both must be named.

3. **No-blame framing check.** Grade:
   - Does the presentation name the system failure, not the person?
   - Is language systemic ("the order was not verified" vs. "Dr. X failed to verify")?
   - Does the case frame any individual error within system context (cognitive load, alert fatigue, workload)?

4. **Improvement recommendation audit.** Grade each recommendation against four criteria:
   - **Specific:** names the exact process to change
   - **Actionable:** can be implemented by the named party
   - **Assigned:** has a responsible department or role named
   - **Measurable:** has a metric or success criterion

   Recommendations that say "improve communication" or "increase vigilance" are automatically non-specific.

5. **Self-check (QA-01).** Cross-verify:
   - Is the root cause at the system level, or did the analysis stop at the individual?
   - Does every recommendation address a named contributing factor (not just the sentinel event)?
   - Is there at least one recommendation per system-level root cause?

## Output Format

```
M&M CASE PREP — [event type / patient anchor]
Learner: [...]   Framework: [...]

>>> TIMELINE

[Timestamped event sequence]

Sentinel event: [clearly marked with timestamp]
Timeline grade: [complete | partial — inference presented as fact | missing timestamps]

>>> CAUSATION MAP (layered)

Immediate cause: [...]
  Why? → Contributing factor 1: [...] (system | individual)
    Why? → Contributing factor 2: [...] (system | individual)
      Why? → Root cause: [...] (system | individual)

Causation map grade: [reaches system level | stops at individual | multi-layer explored]

>>> NO-BLAME LANGUAGE AUDIT

☐ Individual named:                     [none | evidence: "[quote]"]
☑ System failure named:                 "Handoff protocol did not include allergy reconciliation step"
☐ Individual error without system context: [none | evidence: "[quote]"]

>>> IMPROVEMENT RECOMMENDATIONS

#   | Recommendation                       | Specific | Actionable | Assigned to         | Measurable
----|--------------------------------------|----------|------------|---------------------|----------
1   | Add allergy check to handoff template | Yes     | Yes        | Nursing supervisor  | 100% audit compliance
2   | "Improve communication"              | No       | No         | Unspecified         | No metric

Recommendation grade: [N/N meet all 4 criteria | N non-specific recommendations]

>>> SELF-CHECK (QA-01)

☐ Root cause at system level:                    [yes | stopped at individual — [reason]]
☐ All recommendations address named factors:     [yes | N recommendations target sentinel event only]
☐ Minimum one recommendation per root cause:     [yes | N root causes without a recommendation]

>>> VERDICT

Timeline: [complete | partial]
Causation depth: [reaches system level | stops at individual]
Recommendation quality: [N/N actionable]
Restudy target: [named precisely, e.g., "distinguish 5-Whys layer 2 from layer 3 — provider fatigue is not a root cause; the scheduling system that produced the fatigue is"]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `causation_framework = fishbone` | Learner constructs a 6-bone fishbone (people, methods, materials, machines, environment, measurement) before identifying root cause |
| `causation_framework = Swiss-cheese` | Learner maps each layer of defense that failed (prescribing → dispensing → administration → monitoring) |
| `event_type = handoff-failure` | Mandatory: learner must apply I-PASS framework to show what the correct handoff would have looked like |
| `event_type = diagnostic-error` | Mandatory: learner must name the cognitive bias that contributed (anchoring, premature closure, availability heuristic) |
| `learner_level = MS3` | Causation map is pre-scaffolded with 5-Whys prompts; learner fills in each layer |
| `no_blame_only` | Skip recommendation grading; run only the language audit — trains no-blame framing in isolation |

## Verification Checklist

- [ ] Timeline is graded before the causation map — facts must be established before causes are assigned.
- [ ] Causation map must reach a system-level root cause — stopping at "provider error" or "fatigue" without naming the system driver is always incomplete.
- [ ] No individual is named in the model output — no pronouns tied to a specific provider.
- [ ] Improvement recommendations are graded on all 4 criteria: specific, actionable, assigned, measurable.
- [ ] "Improve communication" and "increase vigilance" are automatically flagged as non-specific.
- [ ] Self-check runs all three cross-references; each is marked ☐ or ☑.
- [ ] Restudy target names the specific RCA skill gap — not "understand root cause analysis" but "keep applying 5-Whys past the individual to the system that produced the individual error."
- [ ] No fabricated clinical details appear in the auto-generated adverse event.

## Worked Example (compact)

**Event:** A patient received methotrexate daily instead of weekly after discharge. The prescribing error was not caught at discharge reconciliation or the outpatient pharmacy. The patient developed mucositis and was re-admitted five days post-discharge.

**Timeline (learner):**
- Inpatient: methotrexate prescribed correctly (weekly dosing)
- Discharge: order re-entered as "daily" using a discharge template that defaulted to daily frequency
- Pharmacy: dispensed without frequency flag
- Outpatient: patient took daily for 5 days
- Day 5 post-discharge: admitted with mucositis

**Causation map:**
- Immediate cause: methotrexate prescribed daily instead of weekly
- Why? → Intern used a discharge template that defaulted to "daily" (system: template design error)
- Why? → Template had no high-alert medication frequency alert (system: missing safeguard)
- Why (pharmacy)? → High-alert medication dispensing protocol did not require pharmacist verification of frequency (system: protocol gap)

**Root causes:** Template default error + missing pharmacist safeguard — two system-level root causes identified.

**Recommendations:**
1. Remove "daily" as default frequency for methotrexate in discharge order templates — assign to EHR team; measure as zero daily-methotrexate discharges at 30 days.
2. Add pharmacist verification requirement for high-alert medication frequency changes at discharge — assign to pharmacy director; measure as 100% audit compliance within 60 days.

**Verdict:** Causation map reaches system level. Both recommendations are specific, actionable, assigned, and measurable. **PASS.**
