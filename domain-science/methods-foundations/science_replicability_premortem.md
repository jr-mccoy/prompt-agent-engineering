---
title: "Replicability Pre-Mortem"
category: science/methods-foundations
description: "Adversarial pre-publication audit that assumes a well-powered independent direct replication of this study failed, then ranks the likely culprits and prescribes robustness checks to run before submission."
techniques:
  - ST-01
  - QA-02
  - RT-01
  - NE-10
  - DS-02
  - CM-02
difficulty: advanced
tags:
  - replicability
  - statistical-power
  - p-hacking
  - researcher-degrees-of-freedom
  - specification-curve
  - pre-mortem
  - generalizability
  - effect-size
updated: "2026-06-26"
related_prompts:
  - domain-science/methods-foundations/science_experimental_design_advisor.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
  - domain-science/methods-foundations/science_methods_section_drafter.md
---

# Replicability Pre-Mortem

**Objective:** Stress-test a finished-but-unsubmitted study against the question every reviewer (and every future replicator) will eventually ask: *if an independent lab ran a well-powered direct replication on fresh data with the same method, would it reach the same conclusion?* This prompt runs an adversarial pre-mortem — it assumes that replication **already failed** and forces enumeration of the most likely reasons, ranked by probability, each paired with a concrete robustness check you can run **before** publication.

**When to use:** After analysis is complete and a primary claim exists, but before submission or preprint. Use it when the headline result is surprising, effect sizes are large relative to the literature, the sample is small, or analytic choices were made after seeing the data.

**Scope note — replicability, not reproducibility.** Following the Turing Way / NASEM (2019) distinction: *reproducibility* = **same data + same code → same result** (audited by the sibling prompt `science_reproducibility_self_audit.md`). *Replicability* = **new data + same method, independent team → same conclusion** — that is what this prompt interrogates. A study can be perfectly reproducible (the pipeline re-runs bit-for-bit) yet non-replicable (the finding evaporates on fresh data). Run both audits; they are not substitutes.

**Required inputs:**
- **Discipline.** <field, e.g., experimental psychology, ecology, clinical trials, computational biology> `[user-supplied]`
- **Study type.** <observational / randomized experiment / quasi-experimental / computational / meta-analytic / mixed> `[user-supplied]`
- **Primary claim and its test statistic.** The one sentence the abstract asserts, plus the effect size, CI, p-value/Bayes factor, and N it rests on. `[user-supplied]`
- **Pre-registration status.** Pre-registered (link/ID `[user-supplied]`), registered report, or none.

**Optional inputs:**
- Achieved or planned statistical power and the assumed effect size behind it.
- List of analytic decisions made after data collection (exclusions, covariates, transformations, DV operationalizations).
- Number of outcomes / conditions / subgroups examined.
- Prior literature effect sizes for the same phenomenon.
- Measurement reliability estimates (e.g., Cronbach's α, ICC, test-retest).

**Constraints — Must:**
- Treat the study as guilty until proven robust; the default posture is adversarial (QA-02).
- Distinguish **pre-specified** from **exploratory** for every analytic choice touching the primary claim; flag any choice that was made or could have been made differently after seeing data.
- Rank risks by probability of causing replication failure, using calibrated qualitative bands (Very High / High / Moderate / Low) with stated rationale (NE-10).
- Tie every identified risk to at least one concrete, runnable pre-publication robustness check (multiverse / specification-curve, sensitivity analysis, power/sensitivity analysis, holdout, p-curve, etc.).
- Name the relevant reporting/transparency standards explicitly where they apply (TOP Guidelines, CONSORT, ARRIVE 2.0, the 21-word solution for disclosure of exclusions/conditions/measures/sampling).

**Constraints — Must Not:**
- Do not invent citations, DOIs, dataset names, repository URLs, or instrument/vendor specs. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not assert a finding is "robust," "real," or "confirmed" — the output ranks *risk*, it does not certify truth.
- Do not use promotional language: ban "novel," "groundbreaking," "first-ever," "gold standard," "definitive."
- Do not recommend post-hoc analytic flexibility (adding covariates, dropping cases) as a "fix" — that manufactures the very fragility being audited.

**Instructions:**

1. **Restate the claim and its single point of failure.** Reduce the paper to one falsifiable sentence and identify the exact statistic on which it stands or falls. If the claim cannot be stated in one testable sentence, that is finding #0 — flag it.
2. **Declare the pre-specified/exploratory boundary.** For each analytic choice feeding the primary statistic, label it pre-specified (in a timestamped pre-registration) or exploratory. Any exploratory choice presented as confirmatory is a replication risk.
3. **Power and precision triage.** Compute or request the achieved power for the *literature-plausible* effect size (not the observed one — observed-power is circular). Small N + large observed effect is the winner's-curse signature; flag effect-size inflation explicitly (DS-02).
4. **Enumerate researcher degrees of freedom.** Walk the garden of forking paths: every exclusion rule, covariate set, outcome operationalization, transformation, and stopping rule that was or could have been chosen otherwise. Estimate how many defensible analytic universes exist.
5. **Screen for HARKing and selective reporting.** Check whether the hypothesis could have been formulated after results were known, and whether all measured outcomes/conditions are reported (21-word solution test).
6. **Hunt hidden moderators and context sensitivity.** Identify sample, setting, stimulus, time, and apparatus features that could carry the effect. Ask: would this survive a different population, lab, or season? Context-sensitive effects replicate poorly under direct replication.
7. **Assess measurement reliability.** Unreliable measures attenuate and destabilize effects; a finding resting on a low-reliability instrument is fragile by construction.
8. **Build the ranked risk register and prescribe checks.** For each culprit, assign a probability band, state the diagnostic, and name the specific pre-publication robustness analysis that would de-risk it. Order the register by probability × impact.
9. **Issue a go / revise / de-risk verdict.** Recommend which checks are blocking (must run before submission) versus advisory, and what disclosure language the manuscript needs.

**Output format (locked):**

```
## Claim Under Audit
- Primary claim (one sentence):
- Load-bearing statistic (effect, CI, p/BF, N):
- Pre-registration status:

## Pre-Specified vs Exploratory Ledger
| Analytic choice | Pre-specified? | Could differ post-hoc? | Risk note |
|---|---|---|---|

## Ranked Replication-Failure Risk Register
| # | Culprit | Probability band | Rationale | Diagnostic / robustness check | Blocking? |
|---|---|---|---|---|---|
(Order by probability × impact. Typical culprits, in rough prior-likelihood order:
underpowering / low statistical power; p-hacking & researcher degrees of freedom
(garden of forking paths); HARKing; selective / unreported flexibility (QRPs);
effect-size inflation / winner's curse; hidden moderators & context sensitivity;
measurement unreliability; fragile/fluky single finding.)

## Prescribed Pre-Publication Robustness Checks
- Multiverse / specification-curve analysis: [scope]
- Sensitivity analyses: [which assumptions varied]
- Power / sensitivity (design) analysis at literature effect size: [result or needed input]
- p-curve / p-checking or equivalent evidential-value test: [applicability]
- Holdout / cross-validation / split-half (computational designs): [plan]

## Required Disclosure & Reporting Alignment
- Standard(s): [TOP, CONSORT, ARRIVE 2.0, STROBE, 21-word solution — as applicable]
- Manuscript transparency statements needed:

## Verdict
- Overall replication-risk level (Low / Moderate / High / Very High):
- Blocking checks before submission:
- Advisory checks:
```

**Reporting-standard alignment:** TOP Guidelines (transparency/openness), the 21-word disclosure solution (exclusions, conditions, measures, sample-size rule), and design-appropriate reporting standards — CONSORT (RCTs), STROBE (observational), ARRIVE 2.0 (animal research), PRISMA (systematic reviews/meta-analyses). Cross-reference `science_methods_section_drafter.md` to bind these into the write-up.

**Verification checklist (before delivering):**
- [ ] Primary claim stated as one falsifiable sentence with its load-bearing statistic.
- [ ] Every primary-analysis choice labeled pre-specified or exploratory.
- [ ] Power assessed at a literature-plausible effect size, never observed power.
- [ ] Researcher degrees of freedom enumerated, not summarized as "minimal."
- [ ] HARKing and selective-reporting screen completed.
- [ ] Each risk paired with a specific, runnable pre-publication robustness check.
- [ ] Risk register ranked by probability × impact with stated rationale.
- [ ] No fabricated citations/specs; unknowns marked `[user-supplied]`; no promotional language.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Observed-power circularity | "Power was 0.99" computed from the observed effect, implying the study was well-powered | Require power at the *literature* or *minimally-interesting* effect size; treat observed-power claims as invalid |
| Multiverse theater | A specification curve that varies only trivial choices and omits the real degrees of freedom | Cross-check the curve's universes against the forking-paths enumeration in step 4 |
| "Pre-registered, therefore confirmatory" | Citing a registration that is vague or post-dates data collection | Inspect timestamp and specificity; vague registrations do not convert exploratory analyses to confirmatory |
| Robustness ≠ replicability | Re-running the same data through variants ("robust!") and calling the finding replicable | Reaffirm new-data requirement; route same-data/same-code checks to `science_reproducibility_self_audit.md` |
| Large effect mistaken for strong evidence | Treating a big observed effect in a small sample as reassuring | Flag as winner's-curse signature; expect regression to the mean on replication |
