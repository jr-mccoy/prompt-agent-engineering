---
title: "Threats to Validity Walkthrough"
category: science/methods-foundations
description: "Apply the Cook & Campbell / Shadish-Cook-Campbell four-validity framework step-by-step to one named design, rating each canonical threat present/plausible/controlled with a design or analytic fix."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - RT-03
  - QA-01
  - CM-02
difficulty: advanced
tags:
  - internal-validity
  - external-validity
  - construct-validity
  - statistical-conclusion-validity
  - cook-campbell
  - quasi-experiment
  - validity-threats
  - shadish-cook-campbell
updated: "2026-06-26"
related_prompts:
  - domain-science/methods-foundations/science_experimental_design_advisor.md
  - domain-science/methods-foundations/science_confound_and_bias_audit.md
  - domain-science/methods-foundations/science_blinding_and_randomization_protocol.md
  - domain-science/methods-foundations/science_negative_and_positive_control_designer.md
---

# Threats to Validity Walkthrough

**Objective:** Take one specifically named design and audit it through the four validity types of the Shadish-Cook-Campbell framework — statistical conclusion validity, internal validity, construct validity, and external validity — enumerating the canonical threats under each, rating each present/plausible/controlled for THIS design, and attaching a design or analytic fix. This is a focused four-validity walkthrough; for a broad bias taxonomy and ranked bias register, use the related confound and bias audit.

**When to use:** You have a defined design (e.g., a pretest–posttest non-equivalent groups quasi-experiment, an interrupted time series, a randomized parallel trial, a regression-discontinuity study) and want a structured, type-by-type validity audit rather than a general bias sweep.

**Required inputs:**
- **Discipline.** <field — e.g., education, psychology, public health, program evaluation, HCI>
- **Study type.** <observational / experimental / quasi-experimental — name the specific design>
- **Named design.** The exact design (e.g., "interrupted time series with comparison group").
- **Causal claim.** The treatment → outcome inference the design must support.
- **Constructs and measures.** What the treatment and outcome are intended to represent, and how operationalized.

**Optional inputs:**
- Target population/setting for generalization.
- Analysis approach and whether pre-specified or exploratory.
- Known design limitations already accepted.

**Constraints — Must:**
- Ask for discipline and the specific named design before walking the framework.
- Organize strictly by the four validity types in this order: statistical conclusion, internal, construct, external.
- Under each type, enumerate the canonical threats (see Instructions) and rate each: present / plausible / controlled — for THIS design.
- Distinguish pre-specified analysis decisions from exploratory ones wherever statistical-conclusion validity is judged.
- Tie each rated threat to a concrete design or analytic fix.

**Constraints — Must Not:**
- Do not invent citations, DOIs, effect sizes, or instrument/vendor specs. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not collapse the four types into a generic "limitations" paragraph.
- Do not rate a threat "controlled" without naming the feature that controls it.
- Do not use "novel", "groundbreaking", "first-ever", or "gold standard".

**Instructions:**

1. **Anchor the inference.** Restate the causal claim and the named design; note the unit and timing structure.
2. **Statistical conclusion validity.** Walk threats: low power, violated test assumptions, fishing/error-rate inflation, unreliability of measures, restriction of range, unreliability of treatment implementation, extraneous variance, heterogeneity of units. Rate each and flag whether the analysis is pre-specified.
3. **Internal validity.** Walk threats: history, maturation, testing, instrumentation, statistical regression, selection, attrition/mortality, ambiguous temporal precedence, diffusion/imitation of treatment, compensatory rivalry/resentful demoralization, selection-by-X interactions. Rate each for THIS design.
4. **Construct validity.** Walk threats: inadequate explication of constructs, mono-operation bias, mono-method bias, confounding constructs with levels, evaluation apprehension, experimenter expectancies, novelty/disruption effects, treatment-sensitive factorial structure. Rate each.
5. **External validity.** Walk threats: interaction of the causal effect with units, with settings, with treatment variations, and with outcomes; context-dependent mediation; interaction of history with treatment. Rate generalization targets.
6. **Use Tree-of-Thoughts on contested threats.** For any threat where the rating is debatable, branch the alternative interpretations and select the most defensible rating with its reason (RT-03).
7. **Attach fixes.** For every present/plausible threat, give a design-stage fix (e.g., add a comparison series, multiple operationalizations, blinded assessors) or an analytic fix (e.g., adjustment, sensitivity analysis), and note residual threats no fix removes.
8. **Summarize the four-block verdict.** State, per validity type, the overall confidence and the single most damaging unresolved threat.

**Output format (locked):**

```
## Inference and named design
[causal claim + exact design + unit/timing]

## Four-validity audit table
| Validity type | Threat (canonical) | Rating (present/plausible/controlled) | Why (this design) | Fix (design or analytic) | Residual? |
|---|---|---|---|---|---|
| Statistical conclusion | ... | ... | ... | ... | ... |
| Internal | ... | ... | ... | ... | ... |
| Construct | ... | ... | ... | ... | ... |
| External | ... | ... | ... | ... | ... |

## Contested-threat reasoning (ToT)
[threat → branches considered → chosen rating + reason]

## Four-block verdict
- Statistical conclusion: [confidence] — top unresolved: ...
- Internal: [confidence] — top unresolved: ...
- Construct: [confidence] — top unresolved: ...
- External: [confidence] — top unresolved: ...

## Pre-specified vs exploratory
[analysis decisions affecting statistical-conclusion validity]
```

**Reporting-standard alignment:** Shadish, Cook & Campbell validity typology (the four validity types and canonical threats). Where the design maps to a reporting checklist, also name CONSORT (randomized), STROBE (observational), or TREND (non-randomized behavioral) for the supplied study type.

**Verification checklist (before delivering):**
- [ ] Discipline and the specific named design captured before the walkthrough.
- [ ] All four validity types covered in order, each with its canonical threats.
- [ ] Every threat rated present/plausible/controlled for THIS design, not in the abstract.
- [ ] No threat rated "controlled" without naming the controlling feature.
- [ ] Internal-validity threats include temporal precedence, diffusion, and selection-by-X interactions, not just history/maturation.
- [ ] Construct threats include mono-operation and mono-method bias.
- [ ] Each present/plausible threat has a design or analytic fix; residuals noted.
- [ ] Pre-specified vs exploratory analysis distinction made for statistical-conclusion validity.
- [ ] No fabricated specs/citations; unknowns `[user-supplied]`; banned hype absent.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Internal-validity tunnel vision | Treating internal validity as the only "real" validity and skipping construct/external | Require all four types walked in order with ratings |
| "Controlled" overclaim | Threat marked controlled because randomization is present, ignoring attrition/diffusion | Force a named controlling feature per "controlled" rating |
| Mono-method blindspot | One self-report measure treated as fully capturing the construct | Construct step flags mono-operation/mono-method bias explicitly |
| Generic limitations swap | A vague limitations paragraph substituted for threat-by-threat ratings | Locked four-block table forbids collapsing types |
| Power afterthought | Statistical-conclusion validity reduced to "p<.05" without power/assumption checks | Statistical-conclusion step enumerates power, assumptions, and error-rate inflation |
