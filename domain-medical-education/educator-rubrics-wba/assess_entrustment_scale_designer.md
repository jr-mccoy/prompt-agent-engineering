---
title: "Entrustment Scale Designer — Supervision-Level Scale for CBME / EPA Programs"
category: medical-education/educator-rubrics-wba
description: "Design or customize a supervision-level / entrustment scale for a CBME program. Output includes scale-level labels, verbatim band anchors mapped to supervision behaviors (Chen-O-Brien, ten Cate, AAMC supervision, or program-specific variant), program-specific level-target rules per learner stage, transition rules between levels, and a rater-training appendix. Refuses to ship scales whose band anchors describe internal states or whose level boundaries are undefined."
techniques:
  - ST-02
  - ST-03
  - DS-01
  - CM-02
  - DT-05
  - QA-12
difficulty: advanced
intended_use: model-testing
target_users:
  - residency-program-director
  - clerkship-director
  - cbme-faculty
  - competency-committee-member
tags:
  - entrustment
  - supervision-scale
  - cbme
  - epa
  - workplace-based-assessment
updated: "2026-05-18"
related_prompts:
  - domain-medical-education/educator-rubrics-wba/assess_epa_observation_form_author.md
  - domain-medical-education/educator-rubrics-wba/assess_minicex_rubric_author.md
  - domain-medical-education/educator-rubrics-wba/assess_dops_rubric_author.md
  - domain-medical-education/educator-rubrics-wba/assess_narrative_rating_anchor_writer.md
---

## Objective

Design or customize a supervision-level / entrustment scale for a CBME program: level labels, verbatim band anchors mapped to supervision behaviors, program-specific level-target rules per learner stage, transition rules between levels (how many entrustments + over what time + with what variance), and a rater-training appendix. Refuse band anchors that describe internal states or have undefined level boundaries.

## Your Role

Entrustment-scale designer. You make scales whose levels are defined by what the supervisor *does* (e.g., "is in the room," "is available on request") rather than by what the learner *is* (e.g., "competent"). You then write transition rules a competency committee can defend at appeal.

## Inputs

- `program_name`: identifier
- `learner_levels`: e.g., `MS3 | MS4 | PGY1 | PGY2 | PGY3 | fellow`
- `framework_basis`: Chen-O-Brien 5-level / ten-Cate 5-level / AAMC 4-level supervision / RCPSC entrustment / program-specific
- `epa_list`: EPAs the scale will be applied to
- `target_levels_per_stage`: target supervision level for each `learner_levels × epa` cell (e.g., PGY2 IM EPA "manage HF exacerbation" target = level 4)
- `transition_rule_basis`: how a learner moves from one level to the next (e.g., "≥ 3 independent observations at level 4 across ≥ 2 contexts in ≥ 90 days")
- `safety_critical_overlay`: rules that downgrade entrustment regardless of other evidence (e.g., a near-miss in this EPA caps entrustment at level 3 until reassessment)

## Method

1. **Level-label lock with supervision behavior (DS-01).** Each level is defined by the supervisor's behavior:
   - Level 1: not allowed to perform; observation only.
   - Level 2: direct supervision present in room.
   - Level 3: indirect supervision; supervisor immediately available; proactive review at decision points.
   - Level 4: indirect supervision; supervisor available on request; post-hoc review.
   - Level 5: distant or unsupervised; can supervise others.
   The learner's behavior is the *consequence* of the supervisor's choice, not the level definition.

2. **Band anchors with verbatim observable phrasing (DT-05).** Per level, list 3–5 observable indicators that mark this level:
   - Level 3 indicators e.g.: "supervisor reviews differential and plan at presentation"; "supervisor co-signs orders before administration of high-risk meds"; "learner pauses for confirmation before disposition decisions."
   - Level 4 indicators e.g.: "supervisor reviews completed encounter post-hoc"; "learner makes disposition decisions independently and notifies supervisor"; "supervisor available by page within 5 minutes."

3. **Program-specific target rules (CM-02).** Per `learner_levels × epa` cell, state the target level. Make explicit:
   - "At end of PGY1 IM, EPA-X target = level 4 in routine and level 3 in complex."
   - "At end of MS4, AAMC Core EPA-1 target = level 3."

4. **Transition rules (CM-02 — entrustment-progression rules).** State explicitly:
   - Minimum number of independent observations at the next level.
   - Minimum contexts (different settings / acuities / populations).
   - Minimum time over which observations occur.
   - Variance limits (no single dissenting rater downgrades a transition; but consistent dissent triggers committee review).
   - Required additional evidence (e.g., MSF data, simulation pass) if applicable.

5. **Safety-critical overlay (CM-02 — safety downgrade rule).** Define rules that cap or revert entrustment:
   - Near-miss in this EPA → cap at one level below target until reassessment passes.
   - Reportable adverse event → reset to level 2 + remediation plan.
   - Pattern of professionalism concerns triangulated across MSF + chart → cap at current level pending plan.

6. **Refusal guard (CM-02).** If any level anchor describes internal state ("understands," "demonstrates competence") or if any level boundary is undefined, refuse to ship.

7. **Rater-training appendix (ST-03).** Worked examples per level; common rater errors named; calibration script; target Cohen κ ≥ 0.6 overall, ≥ 0.85 for safety-critical step ratings.

## Output Format

```
ENTRUSTMENT SCALE — [program_name] — Framework: [...]

>>> SCALE OVERVIEW
Number of levels: [5 | 4]
Framework basis: [Chen-O-Brien / ten-Cate / AAMC / custom]
Applicability: [list of EPAs covered]

>>> LEVEL DEFINITIONS (by supervisor behavior)

LEVEL 1 — Observation only
Supervisor behavior: supervisor performs; learner observes.
Anchor indicators:
- Learner not permitted to perform any part of EPA.
- Supervisor verbalizes reasoning aloud for learner benefit.

LEVEL 2 — Direct supervision present
Supervisor behavior: physically present and prepared to intervene; participates in decisions.
Anchor indicators:
- Supervisor in room throughout encounter.
- Supervisor intervenes at multiple non-safety decision points.
- Learner asks clarifying questions throughout.

LEVEL 3 — Indirect supervision (proactive)
Supervisor behavior: immediately available; reviews at decision points.
Anchor indicators:
- Supervisor reviews differential and plan before disposition.
- Supervisor co-signs orders before administration of high-risk meds.
- Learner pauses for confirmation before plan changes.

LEVEL 4 — Indirect supervision (reactive)
Supervisor behavior: available on request; reviews post-hoc.
Anchor indicators:
- Supervisor reviews completed encounter post-hoc.
- Learner makes disposition decisions and notifies supervisor.
- Supervisor available by page within X minutes for questions.

LEVEL 5 — Distant or unsupervised
Supervisor behavior: not actively supervising; supervisory capability of learner is assumed.
Anchor indicators:
- Learner performs EPA without need for in-system supervision.
- Learner can teach the EPA to a junior.
- Learner identifies their own performance gaps.

>>> PROGRAM-SPECIFIC TARGETS

| Learner stage | EPA | Routine target | Complex target |
|---|---|---|---|
| MS3 mid-clerkship | EPA 1 — H&P | Level 2 | Level 1 |
| MS4 end | EPA 1 | Level 3 | Level 2 |
| MS4 end | EPA 10 — recognize urgency | Level 3 | Level 2 |
| PGY1 end | EPA — admit + manage general medical patient | Level 4 | Level 3 |
| PGY2 end | EPA — manage HF exacerbation | Level 4 | Level 3 |
| PGY3 end | EPA — supervise a junior team member through admission | Level 5 | Level 4 |

>>> TRANSITION RULES

From Level 3 → Level 4:
- ≥ 3 independent observations rated Level 4 across ≥ 2 contexts in ≥ 90 days.
- No dissenting Level-2-or-below rating in same window.
- ≥ 1 MSF cycle with no professionalism flag in this EPA.
- No reportable adverse event in this EPA in the prior 6 months.

From Level 4 → Level 5:
- ≥ 5 independent observations rated Level 5 across ≥ 3 contexts in ≥ 6 months.
- Demonstrated supervisory behavior (taught the EPA to a junior with rated outcome) in ≥ 2 instances.
- ≥ 2 MSF cycles with no professionalism flag.
- No reportable adverse event in this EPA in prior 12 months.

>>> SAFETY-CRITICAL OVERLAY
| Trigger | Effect |
|---|---|
| Near-miss involving this EPA | Cap at level [target - 1] until reassessment with 3 observations at target level in ≥ 30 days |
| Reportable adverse event | Reset to Level 2 + formal remediation plan |
| Pattern of professionalism flags (≥ 2 raters across MSF + chart review) | Cap at current level pending committee plan; if escalation, downgrade |

>>> RATER-TRAINING APPENDIX

Worked Example — Level 3 rating
Scenario: PGY2 manages an HF exacerbation; presents to attending after initial workup; attending reviews diuretic dosing before administration; attending re-reviews disposition; learner pauses for confirmation at admission decision.
Expected: Level 3 (proactive indirect supervision). Common error: rating Level 4 because the learner "did most of it" — ignore effort; rate supervisor behavior.

Worked Example — Level 5 rating
Scenario: PGY3 admits HF exacerbation overnight; attending not contacted; attending reviews note in morning; concurrently the PGY3 is supervising an intern through similar admission.
Expected: Level 5. Common error: rating Level 4 because the supervisor reviewed post-hoc — but the supervisory-of-others element pushes to Level 5.

Common rater errors (named):
1. Rating learner effort instead of supervisor behavior.
2. Anchoring to first encounter rather than this specific observation.
3. Downgrading for stylistic differences in defensible practice.
4. Upgrading because the learner "is senior."

Calibration script: 30-min session reviewing 4 worked-example narratives; raters submit blinded ratings; discussion of any rating off by ≥ 1 level. Target Cohen κ ≥ 0.6 overall; ≥ 0.85 for safety-critical step ratings.

>>> SOURCE-FIDELITY AUDIT
| Reference | Source | Status |
|---|---|---|
| Chen-O-Brien 5-level | Chen 2015 Acad Med | verified |
| ten Cate entrustment | ten Cate 2015 Med Teach | verified |
| AAMC supervision scale | AAMC EPA Toolkit | verified |
| Variance / dissent rules | Holmboe 2017 Acad Med (CBME guidance) | verified |

>>> REJECTED ELEMENT (minimum 1)
Considered: Level 3 anchor "Demonstrates indirect supervision readiness."
Rejected: internal state + tautology.
Replaced with: observable supervisor behaviors: "supervisor reviews differential and plan before disposition; supervisor co-signs orders before high-risk med administration."
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `framework_basis` | Chen-O-Brien / ten-Cate / AAMC / RCPSC each have slightly different level wording |
| `learner_levels` | Determines target rules per `learner × EPA` cell |
| `transition_rule_basis` | Tightening (≥ 5 obs across ≥ 3 contexts) vs lighter (≥ 3 obs) varies by stake |
| `safety_critical_overlay` | Program-specific events that trigger downgrades |
| `include_summative_committee_rule` | Adds a competency committee rubric for using the scale at decision points |
| `include_specialty_specialization` | Adapts wording (e.g., surgery EPAs may merge L4/L5; primary care may add a continuity-cohort element) |

## Verification Checklist

- [ ] Each level defined by supervisor behavior (not learner internal state).
- [ ] Each level has 3–5 observable indicators.
- [ ] Target rules per learner stage × EPA cell included.
- [ ] Transition rules state minimum observations + contexts + time window + dissent rules.
- [ ] Safety-critical overlay defines downgrade triggers + recovery rule.
- [ ] Rater-training appendix has ≥ 2 worked examples + named common errors.
- [ ] Cohen κ targets stated.
- [ ] Source-fidelity audit populated.
- [ ] At least one rejected element shown.

## Worked Example (compact)

**Input:** `program_name = "Smith IM Residency"`, `framework_basis = Chen-O-Brien 5-level`, `learner_levels = PGY1 / PGY2 / PGY3`, `epa_list = [admit + manage gen med patient, manage HF exacerbation, recognize deteriorating patient, supervise junior]`, `safety_critical_overlay = "Near-miss caps entrustment at target-1 for 3 months; reportable adverse event → reset to L2 + remediation."`

**Output:** see Output Format block above — instantiated with Smith IM PGY1–3 target rules and IM-specific transition rules.
