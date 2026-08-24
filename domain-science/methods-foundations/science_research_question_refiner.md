---
title: "Research Question Refiner"
category: science/methods-foundations
description: "Convert a vague research curiosity into a specific, testable, scoped, and feasible research question using FINER and PICO/PICOT framing with an explicit falsifiability check."
techniques:
  - ST-01
  - RT-03
  - QA-01
  - QA-02
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - research-question
  - finer-criteria
  - pico-picot
  - falsifiability
  - feasibility
  - scoping
  - hypothesis
  - open-science
updated: "2026-06-26"
related_prompts:
  - domain-science/methods-foundations/science_experimental_design_advisor.md
  - domain-science/methods-foundations/science_preregistration_drafter.md
  - domain-science/methods-foundations/science_registered_report_stage1_drafter.md
---

# Research Question Refiner

**Objective:** Transform a broad, fuzzy curiosity into one specific, testable, and feasible research question with an explicit scope boundary, falsifiability check, and feasibility audit. The output satisfies FINER (Feasible, Interesting, Calibrated-importance, Ethical, Relevant) and renders the question in PICO/PICOT terms so it can be directly carried into a design, preregistration, or Stage-1 Registered Report.

**When to use:** At the very start of the research lifecycle, before any design, sampling, or preregistration work. Use when the starting point is a topic or hunch ("I want to study X") rather than a sharp, answerable question.

**Required inputs:**
- **Discipline.** The field (e.g., molecular biology / condensed matter physics / ecology / cognitive psychology). `[user-supplied]`
- **Study type.** Intended approach (observational / experimental / computational / meta-analytic / mixed). `[user-supplied]`
- **Raw question or curiosity.** The vague statement of interest in the user's own words. `[user-supplied]`

**Optional inputs:**
- **Known constraints.** Budget, timeline, sample/specimen access, equipment, ethics/IRB/IACUC status. `[user-supplied]`
- **Prior work the user already knows.** Specific findings or gaps (no fabrication permitted — see below). `[user-supplied]`
- **Population / system / unit of analysis.** Patients, cells, materials, plots, agents, simulations. `[user-supplied]`
- **Target outcome or measurable.** What would be observed or recorded. `[user-supplied]`

**Constraints — Must:**
- Begin by confirming discipline and study type; if either is missing, ask before proceeding.
- Frame the refined question using PICO (Population, Intervention/Exposure, Comparison, Outcome) or PICOT (add Time) where the study type supports it; for non-clinical fields, map to System, Manipulation/Condition, Comparison, Measured-Outcome, Timeframe.
- Evaluate every candidate question against all five FINER criteria explicitly and separately.
- Produce an explicit falsifiability statement: state what observation would refute the prediction (Bem's "specific testable prediction" standard).
- Separate in-scope from out-of-scope so the boundary of the study is unambiguous.
- Treat preregistration and data/code sharing as the default downstream branch; if the user signals closed data, name it explicitly as the non-default branch and note the justification required.
- Keep all language calibrated.

**Constraints — Must Not:**
- Do not invent citations, DOIs, journal names, dataset names, effect sizes, or instrument/vendor specs. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not assert that the question is unstudied or that a gap exists unless the user supplied that evidence; characterize gaps as "to be confirmed by literature search."
- Do not use "novel," "groundbreaking," "first-ever," or "gold standard" in any drafted question or rationale.
- Do not silently widen scope; any expansion beyond the user's stated interest must be flagged as a suggestion, not a default.

**Instructions:**

1. **Confirm framing.** Restate the discipline, study type, unit of analysis, and the raw curiosity. If unit of analysis or outcome measurable is absent and cannot be inferred safely, ask one consolidated clarifying question.
2. **Diagnose the raw question.** Name precisely why it is not yet answerable: too broad, multiple questions fused, undefined population, unmeasurable outcome, no comparison, or no timeframe.
3. **Generate candidates (Tree of Thoughts).** Produce 2–3 genuinely distinct candidate refinements that narrow the curiosity in different ways (e.g., different population, different exposure granularity, different outcome operationalization). Keep them parallel and comparable.
4. **Score each candidate against FINER.** For each candidate, give a brief, honest rating on Feasible, Interesting, Importance (calibrated — not "novel"), Ethical, Relevant. Flag any criterion that is weak or unknown.
5. **Converge.** Select the strongest candidate and justify the choice against the FINER scores. Note what was traded off.
6. **Render in PICO/PICOT.** Express the selected question with each element labeled; for non-clinical fields use the mapped equivalents.
7. **Set the scope boundary.** List what is explicitly in-scope and what is explicitly out-of-scope, including populations, conditions, and timeframes deliberately excluded.
8. **Run the feasibility check.** Audit samples/specimens, time, cost, access, equipment, and ethics/regulatory approval. Mark each as adequate, uncertain, or blocking, using `[user-supplied]` where data is missing.
9. **Run the falsifiability check.** State the prediction as a specific testable claim and the precise observation that would refute it. Confirm the outcome is measurable with the named approach.

**Output format (locked):**

```
## Inputs Confirmed
- Discipline: ...
- Study type: ...
- Unit of analysis: ...
- Raw curiosity (verbatim): ...

## Diagnosis of the Raw Question
[why it is not yet answerable]

## Candidate Refinements (Tree of Thoughts)
| # | Candidate question | How it narrows | FINER summary (F/I/Imp/E/R) |
|---|---|---|---|
| 1 | ... | ... | ... |
| 2 | ... | ... | ... |
| 3 | ... | ... | ... |

## Selected Question & Rationale
- Refined question: ...
- Why selected (vs. alternatives): ...
- Tradeoffs accepted: ...

## Before / After
- Before: [raw]
- After: [refined]

## PICO / PICOT Mapping
| Element | Content |
|---|---|
| Population / System | ... |
| Intervention / Exposure / Condition | ... |
| Comparison | ... |
| Outcome (measurable) | ... |
| Time (if applicable) | ... |

## Scope Boundary
- In scope: ...
- Out of scope: ...

## Feasibility Check
| Dimension | Status (adequate / uncertain / blocking) | Notes |
|---|---|---|
| Samples / specimens | ... | ... |
| Time | ... | ... |
| Cost | ... | ... |
| Access | ... | ... |
| Equipment / methods | ... | ... |
| Ethics / regulatory | ... | ... |

## Falsifiability Check
- Specific testable prediction: ...
- Observation that would refute it: ...
- Outcome measurable with stated approach? yes / no / conditional

## Downstream Branch (Open Science default)
- Default: preregistration + data/code sharing planned → next step [preregistration drafter / Stage-1 RR]
- If closed data: [named non-default branch + justification required]

## Open Questions / [user-supplied] gaps
- ...
```

**Reporting-standard alignment:** Question structure follows PICO/PICOT and the FINER criteria for question quality; the falsifiability requirement follows Bem's "specific testable prediction" standard. The Open Science default branch aligns the refined question with downstream OSF preregistration and Registered Reports workflows. No outcome-reporting standard (e.g., CONSORT/STROBE/ARRIVE) is invoked here because no results exist yet; those attach at the design/reporting stage.

**Verification checklist (before delivering):**
- [ ] Discipline and study type confirmed before refinement began.
- [ ] 2–3 genuinely distinct candidates were generated and compared, not minor rewordings.
- [ ] Every candidate was scored on all five FINER criteria.
- [ ] Refined question is expressed in labeled PICO/PICOT (or mapped) elements.
- [ ] In-scope and out-of-scope are both populated and non-overlapping.
- [ ] Feasibility table covers samples, time, cost, access, equipment, ethics; gaps marked `[user-supplied]`.
- [ ] A specific refuting observation is stated (falsifiability satisfied).
- [ ] No fabricated citations, datasets, effect sizes, or specs; no banned hype words used.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Pseudo-specificity | Question reads precise but the outcome is unmeasurable or the comparison is missing | Force a labeled PICO/PICOT row for Comparison and Outcome; reject if either is empty |
| Hidden multi-question | A single sentence fuses two distinct research questions joined by "and" | Diagnosis step must split fused questions; pick one as primary |
| Feasibility theater | "Feasible" asserted with no resource data | Mark every unsupported dimension `[user-supplied]` / uncertain, never "adequate" by default |
| Unfalsifiable prediction | Prediction so flexible any result confirms it | Require a concrete refuting observation; if none can be stated, flag the question as not yet testable |
| Smuggled novelty claim | Rationale implies the gap is established without evidence | Recast as "to be confirmed by literature search"; ban hype vocabulary |
