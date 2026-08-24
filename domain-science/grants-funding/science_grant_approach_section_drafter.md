---
title: "Grant Approach Section Drafter"
category: science/grants-funding
description: "Draft a per-aim Approach section with rationale, design, methods, rigor and reproducibility language, pitfalls and alternatives, and milestones with go/no-go points — surfacing interdependence risk across aims."
techniques:
  - ST-01
  - RT-03
  - QA-01
  - QA-02
  - DS-02
  - NE-10
difficulty: advanced
tags:
  - grant-writing
  - approach
  - rigor-reproducibility
  - milestones
  - pitfalls-alternatives
  - nih
  - go-no-go
  - authentication
updated: "2026-06-26"
related_prompts:
  - domain-science/grants-funding/science_specific_aims_drafter.md
  - domain-science/grants-funding/science_grant_significance_section_drafter.md
  - domain-science/methods-foundations/science_power_and_sample_size_calculator.md
  - domain-science/methods-foundations/science_confound_and_bias_audit.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
---

# Grant Approach Section Drafter

**Objective:** Draft the Approach section aim by aim so each aim presents its rationale, research design, methods, expected outcomes, rigor and reproducibility provisions, potential pitfalls with alternative strategies, and milestones with timeline and go/no-go decision points. The draft must use pre-specified, rigorous language and surface interdependence risk across aims so a reviewer can judge feasibility.

**When to use:** After Significance, Innovation, and Specific Aims are drafted, when you need a feasible, rigorous, milestoned Approach that addresses reviewer concerns about design, rigor, and risk.

**Required inputs:**
- **Discipline.** The scientific field.
- **Study type.** Observational / experimental / computational / mixed (determines rigor elements).
- **Funder and mechanism.** e.g., NIH R01, NSF, ERC — Approach/rigor expectations differ.
- **The aims.** The Specific Aims and their hypotheses.
- **Methods per aim.** Designs, assays, models, datasets, or analyses planned.

**Optional inputs:**
- Preliminary data supporting feasibility (with source).
- Power/sample-size analysis, or the parameters to compute one.
- Key biological/chemical resources requiring authentication (cell lines, antibodies, reagents).
- Sex/relevant biological variables, where applicable.
- Project period, personnel, and any external dependencies.

**Constraints — Must:**
- Map to the funder's review criterion for Approach and to Rigor & Reproducibility expectations (NIH Approach + scientific rigor + authentication of key biological/chemical resources; NSF research plan adequacy; ERC methodology/feasibility). Name them explicitly.
- For each aim, include: rationale (with preliminary-data pointer), design, methods, expected outcomes, rigor and reproducibility, pitfalls and alternatives, milestones/timeline/go-no-go.
- Surface rigor explicitly: sample size/power (cross-reference `science_power_and_sample_size_calculator.md`), controls/blinding/randomization and confound control (cross-reference `science_confound_and_bias_audit.md`), authentication of key resources, sex/biological variables where applicable, and reproducibility/pre-specification (cross-reference `science_reproducibility_self_audit.md`).
- Identify interdependence risk: where one aim's success is a precondition for another, and how the plan mitigates a cascade failure.

**Constraints — Must Not:**
- Do not invent citations, DOIs, preliminary data, impact statistics, or funder-specific rules. If needed and not supplied, mark `[user-supplied]` and ask; quantitative impact claims must trace to a user-supplied source.
- Do not assert a power/sample-size number, effect size, or statistical plan that was not supplied or computed from supplied parameters — flag `[user-supplied]`.
- Do not present a fully serial set of aims as low-risk; name the dependency and an alternative path.
- Do not use empty superlatives ("gold-standard method," "definitive") in the drafted text without a checkable basis.

**Instructions:**

1. **Confirm scope.** Restate discipline, study type, funder/mechanism, and the named Approach/Rigor criteria. If unknown, mark `[user-supplied]` and ask.
2. **Lay out the aim skeleton.** For each aim, instantiate the fixed structure (rationale → design → methods → outcomes → rigor → pitfalls/alternatives → milestones).
3. **Draft rationale with a feasibility pointer.** Tie each aim to the hypothesis and reference supporting preliminary data as `[user-supplied]` where not provided.
4. **Specify design and methods.** State the design and the concrete methods/assays/analyses; keep them executable within the project period.
5. **Embed rigor and reproducibility.** For each aim address: sample size/power (cross-reference the power prompt; flag numbers `[user-supplied]` if not computed), controls/blinding/randomization and confound control (cross-reference the confound prompt), authentication of key resources, sex/biological variables where applicable, and pre-specification/reproducibility (cross-reference the reproducibility prompt).
6. **Write pitfalls and alternatives.** For each aim, name the most likely failure modes and a concrete alternative strategy for each — not a generic reassurance.
7. **Set milestones, timeline, and go/no-go points.** Add a timeline with measurable milestones and explicit go/no-go decision criteria; mark where a no-go triggers an alternative path.
8. **Surface interdependence risk.** Map which aims depend on which, flag any single point of failure, and state the mitigation (parallelization, staged decisions, fallback aim ordering).
9. **Compile the rigor checklist and finalize.** Produce a per-aim rigor checklist and confirm calibrated language throughout.

**Output format (locked):**

```
## Approach (drafted, per aim)
### Aim [N]: [short title]
- Rationale & feasibility: [hypothesis link; preliminary-data pointer [user-supplied]]
- Research design: [design]
- Methods: [assays/models/analyses]
- Expected outcomes: [what success looks like]
- Rigor & reproducibility:
  - Sample size/power: [computed or [user-supplied]; cross-ref power prompt]
  - Controls/blinding/randomization/confounds: [cross-ref confound prompt]
  - Authentication of key resources: [resources + method or [user-supplied]]
  - Sex/biological variables: [addressed / N/A with reason]
  - Pre-specification/reproducibility: [cross-ref reproducibility prompt]
- Potential pitfalls & alternatives: [pitfall → alternative]
- Milestones, timeline & go/no-go: [milestone | timing | go/no-go criterion]

## Interdependence Risk Map
- Aim dependencies: [Aim X → Aim Y]
- Single points of failure: [list]
- Mitigation: [parallelization / staged decisions / fallback ordering]

## Rigor Checklist (per aim)
- [ ] Power/sample size addressed
- [ ] Controls/confounds addressed
- [ ] Authentication addressed
- [ ] Biological variables addressed
- [ ] Pre-specification/reproducibility addressed
- [ ] Pitfalls + alternatives present
- [ ] Milestones + go/no-go present
```

**Reporting-standard alignment:** NIH review criterion Approach plus scientific Rigor & Reproducibility and authentication of key biological and chemical resources; NSF research plan adequacy; ERC methodology and feasibility. Sex-as-a-biological-variable and pre-specification are surfaced where applicable.

**Verification checklist (before delivering):**
- [ ] Discipline, study type, and funder/mechanism confirmed; Approach/Rigor criteria named.
- [ ] Every aim has rationale, design, methods, outcomes, rigor, pitfalls/alternatives, and milestones.
- [ ] Power/sample-size figures are computed or flagged `[user-supplied]`; power prompt cross-referenced.
- [ ] Controls/confounds, authentication, biological variables, and reproducibility are each addressed or marked N/A with reason.
- [ ] Pitfalls are specific and each has a concrete alternative.
- [ ] Milestones include go/no-go criteria tied to alternatives.
- [ ] Interdependence/single-point-of-failure risk is mapped with mitigation.
- [ ] No fabricated citations, preliminary data, or funder rules; no empty superlatives in drafted text.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Fabricated power number | "n=120 gives 90% power" with no computation | Require computation from supplied parameters or flag `[user-supplied]`; cross-ref power prompt |
| Generic pitfalls | "Experiments may fail; we will troubleshoot" | Require a named failure mode and a concrete alternative per aim |
| Hidden serial dependency | Aims read independent but Aim 3 needs Aim 1 | Force an interdependence map and a mitigation for each dependency |
| Rigor box-checking | "Rigor was ensured" stated, not shown | Require concrete controls, blinding/randomization, and authentication per aim |
| Missing go/no-go | Milestones listed with no decision criteria | Require explicit go/no-go criteria linked to alternative paths |
| Unauthenticated resources | Key cell lines/antibodies used without a plan | Require authentication method per key resource or `[user-supplied]` |
