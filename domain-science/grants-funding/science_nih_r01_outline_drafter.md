---
title: "NIH R01 Research Strategy Outliner"
category: science/grants-funding
description: "Outline an NIH R01 Research Strategy — Significance, Innovation, and per-aim Approach with rigor, reproducibility, power, and resource-authentication blocks — built from the user's science."
techniques:
  - ST-01
  - ST-03
  - RT-03
  - QA-01
  - QA-02
  - DS-02
difficulty: advanced
tags:
  - nih
  - r01
  - research-strategy
  - rigor-reproducibility
  - approach-section
  - power-analysis
  - grant-writing
updated: "2026-06-26"
related_prompts:
  - domain-science/grants-funding/science_specific_aims_drafter.md
  - domain-science/methods-foundations/science_power_and_sample_size_calculator.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
---

# NIH R01 Research Strategy Outliner

**Objective:** Produce a section-by-section outline of an NIH R01 Research Strategy: Significance (the gap and why it matters), Innovation (specific deltas versus the state of the art), and Approach (per aim: rationale, design, methods, expected outcomes, pitfalls and alternatives, rigor and reproducibility, sample-size/power, and authentication of key resources). The outline is scaffolding the user fills with their own science — it never invents results.

**When to use:** You have a Specific Aims page (or equivalent) and need a structured Research Strategy outline before writing prose for an R01 (or a similarly structured R-series) application.

**Required inputs:**
- **Discipline.** The biomedical/scientific field.
- **Study type.** Observational / experimental / computational / mixed (per aim if they differ).
- **Funding mechanism.** R01 (or the specific R-series target), since page limits and rigor expectations follow the mechanism.
- **The aims.** The 2-3 Specific Aims with their hypotheses and approaches, in the user's words.

**Optional inputs:**
- **Preliminary data.** Results supporting feasibility or the scientific premise (`[user-supplied]`).
- **Key biological/chemical resources.** Cell lines, antibodies, model organisms, reagents requiring authentication.
- **Statistical/design details.** Effect sizes, variability estimates, primary endpoints (`[user-supplied]`).
- **Timeline / personnel / environment notes.**

**Constraints — Must:**
- Map the outline to the NIH review criteria: Significance, Investigator(s), Innovation, Approach, Environment.
- Include an explicit Rigor & Reproducibility treatment within Approach (scientific premise, robust/unbiased design, biological variables including sex as a biological variable where applicable, authentication of key resources).
- For each aim, include sample-size/power placeholders and cross-reference the power-analysis prompt; do not invent numbers.
- For each aim, include potential pitfalls and at least one alternative approach.

**Constraints — Must Not:**
- Do not invent citations, DOIs, preliminary data, collaborator names, institutional resources, or specific funding-program rules/budget caps. If needed and not supplied, mark `[user-supplied]` and ask; funder-specific policy/figures are `[user-supplied]`/verify against the current FOA.
- Do not assert feasibility from preliminary data the user did not provide.
- Do not use "novel," "groundbreaking," "first-ever," or "gold standard" as empty descriptors in drafted text; state innovation as a measurable delta.
- Do not write the full prose — produce an outline with directive bullets, not finished paragraphs, unless the user asks to expand a section.

**Instructions:**

1. **Intake and gate.** Confirm discipline, study type, mechanism, and the aims. If aims or the scientific premise are missing, mark `[user-supplied]` and ask before outlining.
2. **Outline Significance.** Bullet the gap, the importance of closing it, the scientific premise (with its supporting basis as `[user-supplied]`), and how success shifts the field. Keep it criterion-facing, not a literature dump.
3. **Outline Innovation.** Bullet each innovation as a specific contrast: "current practice does X; this proposes Y, which differs because Z." Distinguish conceptual, methodological, and technological innovation; strip empty adjectives.
4. **Outline Approach overview.** Note the overall experimental design, the rationale linking aims to the central hypothesis, and any preliminary data feeding feasibility (`[user-supplied]`).
5. **Outline each aim.** For every aim produce: rationale → experimental design → methods → expected outcomes → potential pitfalls → alternative approaches. Keep aims conceptually independent where possible and flag dependencies.
6. **Insert rigor & reproducibility blocks.** Per aim, address robust and unbiased design (randomization, blinding, replication), relevant biological variables (including sex as a biological variable where applicable), and how results will be validated/replicated. Cross-reference the reproducibility self-audit prompt.
7. **Insert power / sample-size placeholders.** Per aim, mark primary endpoint, effect size, variability, alpha/power, and analysis plan as `[user-supplied]` and cross-reference the power & sample-size prompt; never fabricate estimates.
8. **Add authentication of key resources.** List user-supplied cell lines/antibodies/organisms/reagents and the authentication method for each; mark unsupplied items `[user-supplied]`.
9. **Add timeline and feasibility note; then critique.** Sketch a milestone timeline and a brief reviewer-lens critique flagging weak feasibility, hidden interdependence, missing rigor elements, or overclaimed innovation.

**Output format (locked):**

```
## Significance
- Gap: [...]
- Importance / impact on the field: [...]
- Scientific premise + basis ([user-supplied] if not provided): [...]

## Innovation
- [Innovation 1 — current state → proposed change → why it matters (delta)]
- [Innovation 2 — ...]

## Approach — Overview
- Overall design and rationale: [...]
- Preliminary data feeding feasibility ([user-supplied]): [...]

## Approach — Aim 1: [directive title]
- Rationale: [...]
- Design: [...]
- Methods: [...]
- Expected outcomes: [...]
- Potential pitfalls: [...]
- Alternative approaches: [...]
- Rigor & reproducibility: [randomization/blinding/replication; biological variables incl. SABV where applicable]
- Sample size / power: [primary endpoint, effect size, variability, alpha, power — [user-supplied]; see power prompt]
- Authentication of key resources: [...]

## Approach — Aim 2 [/ Aim 3]: [...]

## Timeline & Milestones
- [...]

## Reviewer-Lens Critique
- Feasibility / interdependence: [...]
- Rigor completeness: [...]
- Innovation as delta vs hype: [...]

## Open Items ([user-supplied])
- [Citations, preliminary data, statistics, resources, FOA-specific rules to verify]
```

**Reporting-standard alignment:** NIH peer-review criteria (Significance, Investigator(s), Innovation, Approach, Environment); NIH Rigor & Reproducibility and authentication-of-key-resources requirements; SABV expectations where applicable. Page limits and FOA-specific requirements are `[user-supplied]`/verify against the current FOA.

**Verification checklist (before delivering):**
- [ ] Discipline, study type, mechanism, and aims captured.
- [ ] Significance states a concrete gap and the scientific premise (basis user-supplied/flagged).
- [ ] Innovation expressed as specific deltas, not adjectives.
- [ ] Each aim has rationale, design, methods, outcomes, pitfalls, and alternatives.
- [ ] Rigor & reproducibility block present per aim; SABV addressed where relevant.
- [ ] Power/sample-size placeholders present and cross-referenced; no invented numbers.
- [ ] Authentication of key resources listed for supplied resources.
- [ ] No fabricated citations, data, collaborators, or program rules; all `[user-supplied]`.
- [ ] Aim interdependence checked and flagged.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Invented feasibility | "Our pilot data confirm…" with no supplied data | Mark feasibility claims `[user-supplied]`; do not assert pilot results |
| Power theater | A fabricated "n=120 gives 80% power" to satisfy the rigor section | Keep effect size/variability `[user-supplied]`; route to the power prompt |
| Rigor checkbox-only | A generic "we will use rigorous methods" sentence | Require concrete randomization/blinding/replication and biological-variable handling per aim |
| Innovation inflation | "First-ever groundbreaking platform" with no contrast | Ban empty descriptors; force current-state → proposed-change → delta |
| Missing alternatives | Aims with pitfalls but no fallback path | Require ≥1 alternative approach per aim |
| Stale FOA assumptions | Asserting page limits or rules from memory | Mark all FOA-specific rules `[user-supplied]`/verify |
