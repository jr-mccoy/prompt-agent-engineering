---
title: PACU Orientation Curriculum Audit
category: pacu/orientation-curriculum
task_type: ANALYZE
audience: PACU unit educator or nurse manager auditing an existing facility orientation program
updated: "2026-05-15"
tags:
  - pacu
  - orientation
  - audit
  - coverage-gap
  - aspan
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - QA-02
  - ED-02
difficulty: advanced
related_prompts:
  - prompts/pacu_orientation_curriculum_designer.md
  - prompts/pacu_orientation_skill_acquisition_timeline.md
  - prompts/pacu_orientee_evaluation_meta_prompt.md
references:
  - ASPAN Standards of Perianesthesia Nursing Practice
  - Drain's PeriAnesthesia Nursing Practice (7th ed.)
  - ASPAN Core Curriculum for PeriAnesthesia Nursing Practice
---

# PACU Orientation Curriculum Audit

> Safety reminder: Audit surfaces structural gaps; it does not authorize program changes. Program changes follow facility governance.

## Objective

Audit an **existing facility PACU orientation program** against ASPAN-scoped competency coverage and surface gaps: missing topics, under-weighted competencies, missing evaluation events, sequencing concerns, and background-adaptation absences.

## Inputs

- **Facility orientation program (paste in or summarize):** {{program structure, weeks, topics, evaluation events}}
- **Facility surgical mix:** {{top services}}
- **Orientee mix the program receives:** {{e.g., mostly experienced, occasional new-grad — known patterns}}
- **Recent orientation outcomes (if known):** {{e.g., 2 extensions in the last year on regional block competency}}

## Audience / Scope

- **Primary:** Unit educator or nurse manager.
- **Secondary:** Nursing professional development council, facility orientation program governance.
- **Scope:** Audit only. Program changes follow facility governance.

## Output requirements

```markdown
# Curriculum Audit — Facility Orientation Program

> Safety reminder: Audit surfaces structural gaps. Program changes follow facility governance.

**Program length:** {weeks}
**Audit focus:** Phase 1 PACU orientation only.

## Coverage map

| ASPAN competency | Covered? | Where in program | Depth (light/standard/deep) | Gap notes |
|---|---|---|---|---|
| Airway & breathing | yes | Wk 1–2 | standard | … |
| Hemodynamics | yes | Wk 3 | standard | … |
| Oxygenation & ventilation | yes | Wk 1–2 | light | considered foundation-only; gap on post-emergence patterns |
| Post-op pain | yes | Wk 4 | standard | … |
| PONV | yes | Wk 4 | light | combined with pain; under-weighted |
| Emergence & delirium | partial | Wk 5 | light | not separately taught from emergence basics |
| Regional / neuraxial block | yes | Wk 5 | standard | … |
| Handoff inbound | yes | Wk 2 | standard | … |
| Handoff outbound | yes | Wk 8 | standard | … |
| Family communication & discharge teaching | partial | scattered | light | no dedicated module |
| Clinical judgment in ambiguity | partial | implicit | light | not taught explicitly; assumed to develop |
| Documentation accuracy | yes | Wk 1–2 | standard | … |
| Team collaboration & role recognition | partial | Wk 0 | light | role overview only, no reinforcement |

## Gaps surfaced

For each gap:
- **Gap:** {what's missing or under-weighted}
- **Evidence:** {what in the program or outcomes points to this}
- **Risk:** {what kind of orientation outcome this gap contributes to}
- **Suggested addition or shift:** {what could close the gap}

## Sequencing concerns

3–5 sentences naming any sequencing issues:
- "Emergence content lands Wk 5, but regional block (which depends on hemodynamic foundation, not emergence) is taught in the same week — concurrent rather than sequenced."
- "Family communication is scattered rather than scaffolded — orientees who do this well likely do so by accident of preceptor."

## Evaluation event coverage

| Evaluation type | Present? | Week | Notes |
|---|---|---|---|
| Mid-orientation checkpoint | … | … | … |
| End-of-phase sign-off | … | … | … |
| Final sign-off | … | … | … |
| Probationary extension review | … | … | … |

## Background-adaptation absences

Does the program differentiate by orientee background (new-grad vs experienced vs cross-specialty)?
- If yes: note where and how.
- If no: surface this as a gap; recommend `pacu_background_specific_pathway_adapter.md` as a tool for primary preceptors to apply per orientee.

## Recommendations

3–5 recommendations, each:
- **Recommendation:** {what to change}
- **Rationale:** {one sentence}
- **Lift required:** {low / medium / high}
- **Trade-off:** {what gets de-prioritized}

## What this audit is not

- Not an HR or compliance audit.
- Not a directive to change the program.
- Not a comparison to other facilities.

## Sources / reference

- ASPAN *Standards* — competency scope.
- *Drain's* — content depth benchmarks.
- *Core Curriculum* — topic-by-topic comparison.
```

## Must / Must not

**Must:**
- Map every ASPAN competency to the program.
- Distinguish "covered" from "under-weighted" from "missing."
- Tie each gap to a downstream risk (orientation outcome pattern, not generic).
- Recommend specific additions or shifts, not abstract "do better."
- Surface sequencing concerns separately from coverage.

**Must not:**
- Treat absence-of-mention as absence-of-coverage without checking.
- Recommend program changes that violate facility governance scope.
- Use this audit for HR or performance management of staff.
- Reference protected characteristics in gap rationale.
- Compare facility to other named facilities.
- Invent ASPAN competency lists beyond the standard scope.

## Quality signals

- An educator can take the audit to a professional development council and present it with structured recommendations.
- Gaps are tied to outcomes, not aesthetics.
- Recommendations are concrete enough to scope implementation work.

## Verification

- [ ] Every ASPAN competency mapped.
- [ ] Coverage map distinguishes covered / under-weighted / missing.
- [ ] Each gap has Evidence + Risk + Suggested addition.
- [ ] Sequencing concerns separate from coverage gaps.
- [ ] Evaluation event coverage assessed.
- [ ] Background-adaptation presence assessed.
- [ ] Safety + FPP sections present.

## False-Positive Prevention

- **No invented facility orientation program content** beyond what the user pasted.
- **No invented outcome statistics** ("our extension rate is X%") unless declared.
- **No invented comparisons to other facilities.**
- **No invented ASPAN section numbers.**
- **No invented Drain's chapter numbers.**
- **No invented mandate or regulatory citation** ("Joint Commission requires …").
- **No protected-characteristic or license-pathway audit dimensions.**
- **No invented governance pathways** — defer to "facility governance."

## Worked Example

<details>
<summary>Example: 10-week program audit, light family-communication coverage, no background adaptation (click to expand, abbreviated)</summary>

```markdown
## Coverage map (abbreviated)

| Competency | Covered | Where | Depth | Notes |
|---|---|---|---|---|
| Airway & breathing | yes | Wk 1–2 | standard | … |
| Family comms | partial | scattered | light | no dedicated module |
| Judgment in ambiguity | partial | implicit | light | not explicitly taught |
| (etc.) |  |  |  |  |

## Gaps surfaced

- **Family communication is under-weighted.** Evidence: scattered references across weeks but no dedicated module. Risk: variable orientation outcomes on family-facing competency; new-grad orientees in particular reach Wk 8 outbound-handoff competency unevenly. Suggested addition: add a dedicated 1-week module in Wk 5 or 6 with simulation touchpoint.
- **Judgment in ambiguity is implicit.** Evidence: not named as a competency in the program; emerges via debrief themes if at all. Risk: long-tail competency underdeveloped at sign-off. Suggested shift: explicit naming + tabletop dual-patient sim at Wk 8.
- **No background adaptation in program design.** Evidence: program text identical for new-grad and experienced orientees. Risk: experienced ICU orientees double-cover foundations they don't need; new-grad orientees feel curriculum is paced for experienced peers. Suggested addition: recommend `pacu_background_specific_pathway_adapter.md` for primary preceptors to apply per orientee.

## Sequencing concerns

Emergence and regional are taught the same week, but regional depends on hemodynamic foundation (already covered Wk 3) while emergence stands alone — they could sequence Wk 4 emergence / Wk 5 regional to reduce same-week load.

## Evaluation event coverage

Mid-orientation checkpoint present at Wk 4 (good). End-of-phase sign-off at Wk 7 (good). Final sign-off at Wk 10. Probationary extension review path: not documented — gap.

## Background adaptation absences

Absent. Recommend `pacu_background_specific_pathway_adapter.md` as preceptor-level tool.

## Recommendations

1. Add dedicated family-communication module Wk 5. Lift: low. Trade-off: scattered references become consolidated; no axis loses time.
2. Name judgment-in-ambiguity as an explicit competency with sim touchpoint Wk 8. Lift: medium.
3. Document probationary extension review pathway. Lift: low.
4. Adopt background-adapter prompt at primary-preceptor onboarding. Lift: low.
```

Notes: every gap has evidence + risk + addition, sequencing surfaced separately, no invented outcome stats.
</details>

## Self-check

- [ ] ASPAN competency map complete.
- [ ] Coverage distinguishes 3 levels.
- [ ] Each gap has Evidence + Risk + Suggested addition.
- [ ] Sequencing concerns separate.
- [ ] Evaluation events + background adaptation assessed.
- [ ] No invented data.
- [ ] FPP section passed.
