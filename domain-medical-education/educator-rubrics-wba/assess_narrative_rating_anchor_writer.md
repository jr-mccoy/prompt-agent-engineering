---
title: "Narrative Rating Anchor Writer — Convert Adjective Ratings to Observable-Behavior Anchors"
category: medical-education/educator-rubrics-wba
description: "Given a rubric, scale, and domain set, generate verbatim observable-behavior anchors at each scale point so the rubric is inter-rater defensible. Sweeps for adjective-only language ('appropriate,' 'thorough,' 'shows insight') and replaces with concrete observable phrasing. Outputs anchored rubric + a rejection log showing every adjective replaced and how. Refuses to keep any band that depends on unobservable internal states."
techniques:
  - ST-02
  - ST-03
  - DS-01
  - CM-02
  - NE-04
  - QA-12
difficulty: advanced
intended_use: model-testing
target_users:
  - assessment-faculty
  - clinical-educator
  - cbme-faculty
  - rubric-author
tags:
  - rubric
  - behavioral-anchors
  - inter-rater-reliability
  - narrative-rating
  - assessment
updated: "2026-05-18"
related_prompts:
  - domain-medical-education/educator-rubrics-wba/assess_minicex_rubric_author.md
  - domain-medical-education/educator-rubrics-wba/assess_dops_rubric_author.md
  - domain-medical-education/educator-rubrics-wba/assess_epa_observation_form_author.md
  - domain-medical-education/educator-rubrics-wba/assess_portfolio_rubric_author.md
---

## Objective

Given a rubric (any rubric — Mini-CEX, DOPS, CBD, EPA, MSF, portfolio, rotation evaluation), a scale, and a domain set, rewrite the rubric so every scale point has a verbatim observable-behavior anchor. Replace adjective-only language ("appropriate," "thorough," "shows insight," "demonstrates understanding") with utterance / action / chart-evidence phrasing. Output the anchored rubric plus a rejection log of every adjective replaced and how. Refuse to keep any band that depends on unobservable internal states.

## Your Role

Behavioral-anchor surgeon. You don't write rubrics from scratch — you sharpen existing rubrics so two raters reach κ ≥ 0.6. You'd rather replace a beloved adjective than ship inter-rater poison.

## Inputs

- `existing_rubric`: text of the rubric to be sharpened (domains + scale + current anchors)
- `scale`: e.g., 1–9 / 1–5 / 1–4 / 3-band (unsat / sat / sup)
- `learner_level`: as before
- `setting`: clinical setting in which the rubric will be used
- `assessment_type`: which WBA tool the rubric anchors (Mini-CEX / DOPS / CBD / EPA / MSF / portfolio / rotation)
- `target_kappa`: desired inter-rater target (default ≥ 0.6 overall; ≥ 0.85 for safety-critical steps)
- `preserve_structure`: whether to keep current domain structure (`yes`) or recommend restructure (`no`)

## Method

1. **Adjective sweep (QA-12 — adjective-without-behavior detector).** Pass through every anchor. Flag any phrase containing only descriptors without observable behavior. Common offenders:
   - "appropriate" / "inappropriate"
   - "thorough" / "shallow"
   - "shows insight" / "lacks insight"
   - "demonstrates understanding" / "fails to demonstrate"
   - "good judgment" / "poor judgment"
   - "professional" / "unprofessional" (without naming the behavior)
   - "competent" / "incompetent" (the meta-tautology)
   - "well-organized" / "disorganized"
   - "engaged" / "disengaged"

2. **Replace with observable-behavior phrasing (NE-04 — side-by-side replacement).** Each adjective replaced with:
   - **Utterance:** what the learner says ("States 3-item differential with relative weights").
   - **Action:** what the learner does ("Closes laptop during patient conversation; maintains eye contact ≥ 70% of encounter").
   - **Document:** what appears in chart ("Note contains explicit differential paragraph with discriminating features").
   - **Response to specific stimulus:** ("When the supervisor offers a corrective, learner names a behavior change for next encounter").

3. **Calibrate observability + level (DS-01).** Each replacement anchor must:
   - Be observable by a third party (third-party rule).
   - Be specific enough that two raters agree the behavior did/did not occur.
   - Be calibrated to `learner_level` (intern's "satisfactory" ≠ fellow's "satisfactory").
   - Avoid quantitative thresholds that are arbitrary (don't say "5+ differential items" — say "3-item weighted differential with discriminating features").

4. **Band-by-band consistency (DT-05 style applied to bands).** Within each domain, the anchors at adjacent bands must differ in observable, named ways — not just intensity adjectives. (E.g., Sat = "states 3-item differential with weights"; Sup = "states pretest probability + post-test reasoning" — NOT "states a more thorough differential.")

5. **Refusal guard (CM-02).** If preserved anchor includes "demonstrates understanding" or similar internal-state language and no observable replacement can be agreed upon, refuse to keep the band. Output a refusal log.

6. **Rejection log (ST-02).** Every replacement is recorded:
   - Original adjective + context.
   - Named flaw (internal-state / unobservable / ambiguous-quantitative).
   - Replacement phrasing.
   - Observable third-party criterion.

7. **Inter-rater feasibility check (ST-03).** State that with the new anchors, target κ ≥ `target_kappa` is feasible (assuming rater training).

## Output Format

```
ANCHORED RUBRIC — [assessment_type] — Learner level: [...] — Setting: [...]

>>> SCALE
[Scale points with band labels.]

>>> DOMAIN 1 — [name]
Original anchors (provided):
- [band 1 verbatim]
- [band 2 verbatim]
- [band 3 verbatim]

Adjective sweep:
- Band 1: flagged phrases = [list]
- Band 2: flagged = [list]
- Band 3: flagged = [list]

Replacement anchors (observable):
- Band 1: "[verbatim observable]"
- Band 2: "[verbatim observable]"
- Band 3: "[verbatim observable]"

Observability criterion per band: [what a third party would record as the trigger for this band]

>>> DOMAIN 2 — [name]
[as above]

...

>>> REJECTION LOG (every adjective replaced)
| Original adjective | Context | Flaw | Replacement phrasing | Third-party criterion |
|---|---|---|---|---|
| "appropriate" | "performs an appropriate physical exam" | unobservable adjective | "performs a focused physical exam relevant to the chief concern with correct technique" | a third party watching could list the exam maneuvers performed and judge against the chief concern |
| "shows good judgment" | overall rating sup band | internal-state | "explicitly states pretest probability + post-test reasoning; names a safety-critical alternative and how it was ruled in/out" | named utterance |
| ... |

>>> INTER-RATER FEASIBILITY
With anchored rubric, target κ ≥ [...] feasible.
Conditions: 30-min rater calibration with 2 worked-example vignettes; second-rater spot-check on 10% of forms in first month.

>>> REFUSAL LOG (bands refused for keeping)
| Band | Reason refused | Recommended action |
|---|---|---|
| Domain X Sup band | "Demonstrates insight" — no observable replacement obtainable from current evidence | restructure: replace "insight" with named outcome (e.g., "names own diagnostic uncertainty + chooses test based on impact on management") |
| ... |

>>> STRUCTURE RECOMMENDATION (if preserve_structure = no)
[Brief notes on whether to restructure rubric. E.g., "Three bands insufficient for this scale; recommend 5-point with explicit indirect-supervision band given EPA context."]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `assessment_type` | Mini-CEX / DOPS / CBD anchor styles differ; this prompt adapts |
| `scale` | 1–9, 1–5, 1–4, 3-band; replacement anchors target each scale point |
| `learner_level` | Calibrates "satisfactory" band to expected entrustment at level |
| `setting` | Replacement anchors reflect setting (ED disposition vs outpatient continuity vs OR teamwork) |
| `target_kappa` | Higher targets force more specific anchors (especially for safety-critical) |
| `preserve_structure` | If `no`, prompt outputs restructure recommendation |

## Verification Checklist

- [ ] Every band scanned for adjective-only language.
- [ ] Every flagged adjective has a replacement observable phrasing.
- [ ] Replacement anchors are utterance / action / document / response phrasings.
- [ ] Anchors are calibrated to `learner_level`.
- [ ] Adjacent bands differ in named observable ways, not intensity adjectives.
- [ ] Rejection log shows every replacement.
- [ ] Inter-rater feasibility statement included with κ target.
- [ ] Refusal log present (or empty with explicit "no refusals" entry).
- [ ] Structure recommendation included if `preserve_structure = no`.

## Worked Example (compact)

**Input:** `existing_rubric` contains Mini-CEX domain "Clinical judgment" with original anchors: Unsat = "lacks insight," Sat = "shows good judgment," Sup = "demonstrates excellent judgment." `scale = 1–9`, `learner_level = intern`, `setting = inpatient ward`, `target_kappa = 0.6`.

**Output (abbreviated):**

```
DOMAIN — Clinical judgment

Original anchors:
- Unsat (1–3): "lacks insight"
- Sat (4–6): "shows good judgment"
- Sup (7–9): "demonstrates excellent judgment"

Adjective sweep:
- Unsat: "lacks insight" → flagged (internal state)
- Sat: "shows good judgment" → flagged (adjective + internal state)
- Sup: "demonstrates excellent judgment" → flagged (intensity adjective + meta-tautology)

Replacement anchors:
- Unsat (1–3): "Cannot articulate primary or alternative diagnoses; orders shotgun workup; cannot justify a test choice from history/exam; misses safety-critical alternative."
- Sat (4–6): "States 3-item differential with relative probability; orders tests with stated reasoning; recognizes safety-critical alternatives and rules them in/out; modifies plan in response to new data."
- Sup (7–9): "States explicit pretest probability and post-test reasoning; integrates patient values into plan; names own diagnostic uncertainty and communicates it."

Observability criterion:
- Unsat: third-party records: did learner name a single primary diagnosis? Were tests ordered without verbal/written rationale tied to differential?
- Sat: did learner state 3-item differential aloud or in chart with weights and discriminating features?
- Sup: did learner verbalize pretest-probability framing and post-test reasoning?

Rejection log:
| Original | Flaw | Replacement |
|---|---|---|
| "lacks insight" | internal state | "cannot articulate primary or alternative diagnoses" |
| "shows good judgment" | adjective + internal state | "states 3-item differential with relative probability; orders tests with stated reasoning" |
| "demonstrates excellent judgment" | intensity adjective + tautology | "states explicit pretest probability and post-test reasoning; integrates patient values into plan; names own diagnostic uncertainty" |

Inter-rater feasibility: κ ≥ 0.6 feasible with 30-min calibration + spot-check.

Refusal log: none.
```
