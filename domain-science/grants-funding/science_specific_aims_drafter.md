---
title: "NIH Specific Aims Page Drafter"
category: science/grants-funding
description: "Draft a one-page NIH-style Specific Aims page (hook, gap, central hypothesis, 2-3 aims, payoff) from the user's own science, then critique it against NIH conventions."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-01
  - QA-02
  - CM-02
difficulty: advanced
tags:
  - nih
  - specific-aims
  - grant-writing
  - research-funding
  - central-hypothesis
  - rigor-reproducibility
  - biomedical
updated: "2026-06-26"
related_prompts:
  - domain-science/grants-funding/science_nih_r01_outline_drafter.md
  - domain-science/methods-foundations/science_power_and_sample_size_calculator.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
---

# NIH Specific Aims Page Drafter

**Objective:** Draft a single-page NIH Specific Aims section that executes the conventional arc — opening hook, what is known and the critical need, the long-term goal / overall objective / central hypothesis, two to three aims, and the payoff — built entirely from the user's supplied science. The page is the most-read part of any NIH application, so it must read cleanly on its own and set up every review criterion that follows.

**When to use:** You have a defined research problem, a credible (user-supplied) rationale or preliminary basis, and a proposed set of experiments, and you need a polished Specific Aims page for an NIH application (R-series, K, F, etc.).

**Required inputs:**
- **Discipline.** The biomedical/scientific field (e.g., cancer immunology, neurodegeneration, health-services research).
- **Study type.** Observational / experimental / computational / mixed.
- **Funding mechanism.** The target NIH mechanism (e.g., R01, R21, R03, K99/R00) — this shapes scope, aim count, and risk tolerance.
- **The science.** The problem, the gap, the proposed approach, and the expected outcomes, in the user's own words.

**Optional inputs:**
- **Preliminary data / premise.** Any results, prior findings, or published basis supporting the central hypothesis (`[user-supplied]`).
- **Long-term goal and career stage.** PI's broader research program and stage.
- **Working models or schematics.** A conceptual model the aims are organized around.

**Constraints — Must:**
- Map the page to the NIH review criteria it must seed: Significance, Innovation, and Approach (Investigator and Environment are addressed elsewhere but should be implicitly credible here).
- State an explicit central hypothesis and tie each aim to it.
- Keep the draft to roughly one page; flag if supplied content overflows.
- Surface rigor of the scientific premise (the basis for the central hypothesis) using only user-supplied premise/preliminary data.

**Constraints — Must Not:**
- Do not invent citations, DOIs, preliminary data, collaborator names, institutional resources, or specific funding-program rules/budget caps. If needed and not supplied, mark `[user-supplied]` and ask; funder-specific policy/figures are `[user-supplied]`/verify against the current FOA.
- Do not assert results, effect sizes, or "preliminary data show…" unless the user supplied them.
- Do not use "novel," "groundbreaking," "first-ever," or "gold standard" as empty descriptors in drafted text; substantiate any genuine innovation with a specific delta versus the current state of the art.
- Do not write interdependent aims silently — if Aim 2 cannot proceed unless Aim 1 succeeds, flag the dependency explicitly.

**Instructions:**

1. **Intake and gate.** Confirm discipline, study type, and NIH mechanism. If the central hypothesis, gap, or proposed approach is missing, mark `[user-supplied]` and ask before drafting — do not fabricate the science.
2. **Draft the hook (paragraph 1).** Open with the problem and its importance, then narrow to the specific gap in knowledge. Anchor importance in the user's framing, not generic disease-burden boilerplate.
3. **Establish what is known and the critical need.** Summarize the relevant state of the field (citations as `[user-supplied]`), then state the critical need that the gap creates — the thing that cannot move forward until this is resolved.
4. **State goal, objective, hypothesis.** Write the long-term goal (the program), the overall objective (this application), and the central hypothesis. Explicitly note the basis/premise for the hypothesis from supplied preliminary data; if none supplied, mark `[user-supplied]` and note the rationale is logical rather than empirical.
5. **Draft 2-3 aims.** Each aim gets a directive title (a testable statement, not a topic), a one-line working hypothesis, and a sentence on approach and expected outcome. Prefer aims that are conceptually independent so failure of one does not collapse the rest.
6. **Audit interdependence.** Inspect the aim set; if any aim is a prerequisite for another, flag it and suggest a reframing or an alternative path so a single failure does not sink the application.
7. **Write the payoff.** Close with the expected outcomes, the impact on the field, and how the results enable the next phase of the long-term goal. Calibrate claims to what the aims can actually deliver.
8. **Critique pass.** Re-read as a study-section reviewer would: is the gap real, is the hypothesis falsifiable, are the aims independent, does Significance land before Approach, is any language overclaimed? Produce a short critique with specific fixes.

**Output format (locked):**

```
## Specific Aims (draft)

[Paragraph 1 — Hook: problem + importance, narrowing to the gap]

[Paragraph 2 — What is known / critical need]

[Paragraph 3 — Long-term goal; overall objective; central hypothesis (+ basis/premise, [user-supplied] if not provided)]

**Aim 1. [Directive, testable title]**
Working hypothesis: [...]. Approach: [...]. Expected outcome: [...].

**Aim 2. [Directive, testable title]**
Working hypothesis: [...]. Approach: [...]. Expected outcome: [...].

[**Aim 3.** if applicable]

[Paragraph — Payoff: expected outcomes + impact + enablement of next phase]

## Aim Independence Check
- [Interdependence flags and suggested mitigations]

## Reviewer-Lens Critique
- Significance: [...]
- Innovation (specific delta vs state of the art): [...]
- Approach / feasibility: [...]
- Overclaim / hype scan: [...]
- Top 3 fixes: [...]

## Open Items ([user-supplied])
- [Citations, preliminary data, resources to supply or verify against the current FOA]
```

**Reporting-standard alignment:** NIH peer-review criteria (Significance, Investigator(s), Innovation, Approach, Environment) and the NIH scientific-premise/rigor expectations; Specific Aims one-page convention. FOA-specific aim counts, page limits, and program rules are `[user-supplied]`/verify against the current FOA.

**Verification checklist (before delivering):**
- [ ] Discipline, study type, and NIH mechanism captured.
- [ ] Page opens with a concrete gap, not a generic burden statement.
- [ ] Central hypothesis is explicit and falsifiable; its premise is user-supplied or flagged.
- [ ] 2-3 aims, each with a directive (testable) title.
- [ ] Aim interdependence checked and flagged.
- [ ] Payoff ties back to the long-term goal.
- [ ] No fabricated citations, preliminary data, or resources; all marked `[user-supplied]`.
- [ ] No empty hype descriptors; innovation stated as a specific delta.
- [ ] Fits ~one page; overflow flagged.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Fabricated premise | "Preliminary data show a 3-fold increase…" invented to strengthen the hypothesis | Only state premise/data the user supplied; otherwise `[user-supplied]` and mark the rationale as logical |
| Hidden interdependence | Three aims that read as parallel but Aim 3 requires Aim 1's construct | Run the independence check; flag and suggest a fallback path |
| Topic-title aims | Aim titled "Characterize the role of X" (a topic, not a test) | Rewrite as a directive, testable statement with a working hypothesis |
| Hype substituting for substance | "A novel, groundbreaking approach" with no stated delta | Ban empty descriptors; require a specific contrast with the current state of the art |
| Significance buried | Approach detail appears before the reader knows why it matters | Enforce arc order: hook/gap → need → hypothesis → aims → payoff |
