---
title: PACU CAPA/CPAN Blueprint-Aligned Study Plan
category: pacu/exam-prep
task_type: CREATE
audience: PACU RN preparing for the ABPANC CAPA or CPAN certification exam
updated: "2026-05-15"
tags:
  - pacu
  - certification
  - capa
  - cpan
  - exam-prep
  - study-plan
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - ED-02
  - DS-06
difficulty: intermediate
related_prompts:
  - prompts/pacu_capa_cpan_weak_area_diagnostic.md
  - prompts/pacu_capa_cpan_practice_question_generator.md
  - prompts/pacu_capa_cpan_test_strategy_coach.md
  - prompts/pacu_capa_cpan_final_week_review.md
references:
  - ABPANC official exam blueprint (current edition — user pastes in domains and weights)
  - ASPAN Core Curriculum for PeriAnesthesia Nursing Practice
  - Drain's PeriAnesthesia Nursing Practice (7th ed.)
---

# PACU CAPA/CPAN Blueprint-Aligned Study Plan

> Safety reminder: The ABPANC exam blueprint changes over time. This prompt requires the candidate to paste in the current blueprint domains and weights from the official ABPANC source. The prompt never fabricates blueprint content.

## Objective

Produce a **multi-week, blueprint-aligned study plan** for a candidate preparing for CAPA (ambulatory) or CPAN (Phase 1 inpatient). The plan distributes weekly read / practice-question / self-test time proportional to the blueprint weights the candidate pasted in, accounts for declared weak areas, and culminates in a final-week review (which lives in a separate prompt).

## Inputs

Ask for all six before generating. If anything is missing, ask first.

- **Exam:** {{CAPA | CPAN | both}}
- **Target test date:** {{date — drives total weeks}}
- **Hours available per week:** {{realistic, not aspirational}}
- **Current ABPANC blueprint domains and weights (paste from official source):** {{the candidate copies the domain list + percentages directly from ABPANC's published blueprint — we do not fabricate this}}
- **Declared weak areas (from `pacu_capa_cpan_weak_area_diagnostic.md` or self-rated):** {{ranked list with confidence}}
- **Practice resources available:** {{e.g., ABPANC self-assessment, Drain's, Core Curriculum, other test-prep materials — name them}}

## Audience / Scope

- **Primary:** PACU RN candidate, often 6–16 weeks from test date.
- **Secondary:** Unit educator coaching the candidate.
- **Scope:** Multi-week schedule. Final-week review: `pacu_capa_cpan_final_week_review.md`. Weak-area diagnostic: `pacu_capa_cpan_weak_area_diagnostic.md`. Practice questions: `pacu_capa_cpan_practice_question_generator.md`. Test-taking strategy: `pacu_capa_cpan_test_strategy_coach.md`.

## Output requirements

```markdown
# CAPA/CPAN Study Plan — {N} weeks to {test date}

> Safety reminder: Blueprint weights below are user-supplied from the official ABPANC source. Verify against the current ABPANC blueprint each week — the published blueprint is authoritative; this plan defers to it.

**Exam:** {CAPA | CPAN | both}
**Test date:** {date}
**Total study weeks:** {N}
**Weekly hours available:** {h}
**Total hours budgeted (target):** {N × h}

## Blueprint coverage allocation

Blueprint pasted by candidate:
| Domain | Weight (%) | Hours allocated | Concentration weeks |
|---|---|---|---|
| {domain 1 from user input} | {%} | {hours} | Wk {a–b} |
| {domain 2} | {%} | … | … |
| (etc., as many as candidate pasted) |  |  |  |

Hours allocated per domain = (weight % × total budgeted hours) × weak-area multiplier (1.0 standard; up to 1.3 for declared weak areas, with offsetting reduction on declared strong areas).

## Weekly plan

Repeat for each week.

### Wk {n} — {primary domain focus}

**Domain focus this week (≥ 70% of week's time):** {domain}
**Secondary review (≤ 30%):** {prior week's domain — spaced repetition}

**Activities:**
- Read: {Drain's chapters / Core Curriculum modules relevant to this domain — by chapter title only}.
- Practice questions: {N items} on this domain via `pacu_capa_cpan_practice_question_generator.md` or available test-prep bank.
- Self-test on prior-week domain: {N items}.
- Notes: write a 1-page concept summary on the hardest sub-topic this week.

**Mid-week check:** rate confidence on this domain on a 1–5 scale. If unchanged or down by end of week, re-run weak-area diagnostic next Mon.

## Spaced repetition map

How prior weeks' domains get revisited in subsequent weeks. Each domain appears ≥ twice across the plan (primary week + at least one secondary review week).

## Weak-area reinforcement

For each declared weak area, list the specific reinforcement actions across the plan (extra practice items, extra reading, ad hoc 30-min review sessions).

## Final two weeks

- **Penultimate week:** full-length practice test (timed); review every missed item by domain; map errors to blueprint.
- **Final week:** see `pacu_capa_cpan_final_week_review.md`.

## What this plan is not

- Not a guarantee of passing.
- Not the blueprint itself — defers to ABPANC's current published blueprint.
- Not a substitute for the candidate's own pacing judgment.

## Sources / reference

- ABPANC blueprint — user-pasted, verified by candidate against the current official source.
- ASPAN *Core Curriculum* — content per domain.
- *Drain's* — content per domain.
```

## Must / Must not

**Must:**
- Use blueprint weights **only as the candidate pasted them.** If the candidate did not paste a blueprint, ask before generating.
- Allocate hours proportional to weights, with a moderate weak-area multiplier (max 1.3 to avoid skewing the plan).
- Build spaced repetition (each domain ≥ 2x).
- Schedule a full-length practice test penultimate week.
- Reference the final-week review prompt.
- Acknowledge that the ABPANC blueprint may have updated since the candidate's source.

**Must not:**
- Fabricate blueprint domains or weights.
- Recommend resources not declared by the candidate as available.
- Project pass/fail outcomes.
- Treat the plan as endorsed by ABPANC.
- Reference protected characteristics in study load decisions.
- Include candidate's clinical practice hours as study hours.
- Compress the plan below 6 weeks unless candidate explicitly requested.

## Quality signals

- A candidate can drop the weekly plan into their calendar and start Monday.
- Weak areas get visibly more attention without crowding out the rest.
- Spaced repetition is visible and concrete.
- Final-week review is referenced, not duplicated here.

## Verification

- [ ] Blueprint weights match user-pasted source exactly (no fabrication).
- [ ] Hours per domain proportional to weight × multiplier.
- [ ] Each domain appears ≥ 2x in the plan.
- [ ] Penultimate week is full-length practice test.
- [ ] Final week defers to final-week review prompt.
- [ ] Resources are only those declared by candidate.
- [ ] Safety + FPP sections present.

## False-Positive Prevention

- **No fabricated ABPANC blueprint domains, weights, or content categories.** All blueprint content must come from the candidate's pasted source.
- **No fabricated ABPANC exam item counts, time limits, or scoring rules.** Defer to ABPANC's published policies.
- **No fabricated pass rates, predictive validity claims, or "candidates who study X hours pass" assertions.**
- **No fabricated test-prep vendor effectiveness claims.**
- **No invented Drain's / Core Curriculum chapter or page numbers.** Use chapter titles.
- **No fabricated continuing-education-credit value** of the study activities.
- **No invented ABPANC accommodations policies** — candidate consults ABPANC directly.
- **No protected-characteristic study-load decisions.**

## Worked Example

<details>
<summary>Example: CPAN, 10 weeks, 8 hrs/week, candidate-pasted blueprint (anonymized) (click to expand)</summary>

```markdown
# CPAN Study Plan — 10 weeks

**Total weekly hours:** 8.
**Total budgeted hours:** 80.

**Blueprint (candidate-pasted, anonymized for example):**
| Domain | Weight | Hours allocated | Concentration weeks |
|---|---|---|---|
| {Domain A} | {%} | {h} | Wk 1–2 |
| {Domain B} | {%} | {h} | Wk 3–4 |
| {Domain C} | {%} | {h} | Wk 5–6 |
| {Domain D} | {%} | {h} | Wk 7 |
| {Domain E} | {%} | {h} | Wk 8 |

(The example does not invent specific percentages; in real use, the candidate pastes the current ABPANC blueprint.)

## Wk 1 — Domain A focus

- Primary domain time: 6 hrs (75%).
- Activities: Drain's chapters relevant to Domain A; 25 practice questions; 1-page concept summary on hardest sub-topic.
- Secondary review: n/a (Wk 1).
- Mid-week check: confidence 1–5 rating.

## Wk 2 — Domain A continued + Wk 1 review

(repeat structure)

## Wk 9 — Full-length practice test

Penultimate week. Timed practice exam. Review every missed item by domain. Errors mapped to blueprint to identify final-week focus.

## Wk 10 — Final-week review

Defers to `pacu_capa_cpan_final_week_review.md`.

## Spaced repetition map

Domain A: primary Wk 1–2, secondary Wk 4, Wk 7.
Domain B: primary Wk 3–4, secondary Wk 6, Wk 8.
(etc.)

## Weak-area reinforcement

Candidate declared weakness on Domain C: extra 1-hour session each week starting Wk 3, plus 10 extra practice items per week on this domain.
```

Notes: blueprint pasted by candidate (placeholders shown), no fabricated weights, spaced repetition visible, penultimate week full-length practice, final week deferred.
</details>

## Self-check

- [ ] Blueprint weights from user-pasted source only.
- [ ] Hours proportional to weights × multiplier.
- [ ] Spaced repetition visible.
- [ ] Penultimate week = full practice test.
- [ ] Final week deferred to final-week review.
- [ ] Resources only those declared.
- [ ] FPP section passed.
