---
title: "Review Lens for Replication and Robustness Studies"
category: science/peer-review
description: "A specialized peer-review rubric for replication, robustness, and reproducibility-audit manuscripts that sets aside the novelty criterion and judges fidelity, power, and correct interpretation of a (non-)replication."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-02
  - DS-02
difficulty: advanced
tags:
  - replication
  - robustness
  - reproducibility
  - multiverse-analysis
  - registered-reports
  - equivalence-testing
  - cope
  - open-science
updated: "2026-06-26"
related_prompts:
  - domain-science/peer-review/science_peer_review_drafter.md
  - domain-science/peer-review/science_review_disagreement_arbitration_memo.md
  - domain-science/peer-review/science_post_publication_critique_drafter.md
  - domain-science/methods-foundations/science_replicability_premortem.md
---

# Review Lens for Replication and Robustness Studies

**Objective:** Provide a peer-review lens tailored to replication studies and robustness/reproducibility audits, where the usual "is this novel?" criterion is inappropriate and must be explicitly set aside. The review judges fidelity to the original, statistical power to detect the original effect, preregistration, analytic robustness, computational reproducibility, and — critically — whether the manuscript correctly interprets a replication or non-replication.

**When to use:** You are reviewing a manuscript whose contribution is to repeat, re-analyze, stress-test, or computationally reproduce a prior result (direct or conceptual replication, multiverse/specification-curve audit, or reproduction of published code/data).

**Required inputs:**
- **Discipline.** Field and subfield.
- **Study type.** Direct replication / conceptual replication / robustness (multiverse, specification-curve) / computational reproducibility audit / re-analysis.
- **Original study.** Citation and the specific effect/claim being tested `[user-supplied]`, including the original effect size and design if reported.
- **The submitted manuscript.** Methods, analyses, results, and the authors' stated interpretation.

**Optional inputs:**
- Preregistration / registered-report stage and protocol link.
- Original authors' data/code and the replication's data/code availability.
- The original effect size and the smallest effect size of interest (SESOI), if defined.
- Whether the work is a Registered Report (Stage 1 protocol vs Stage 2 results).

**Constraints — Must:**
- Explicitly state that novelty/importance is NOT a valid acceptance criterion here, and remove any novelty-based objection; judge methodological soundness and informativeness instead.
- Apply the reproducibility-vs-replicability distinction (NASEM / The Turing Way): reproducibility = same data + same code → same result; replicability = new data → consistent result. Use the correct term for the manuscript's actual aim.
- Classify the design as direct vs conceptual replication and hold it to the appropriate fidelity standard.
- Assess statistical power (DS-02): was the replication powered to detect the original (or a plausibly smaller) effect? Quantify, and flag if powered only for an implausibly large effect.
- Evaluate analytic robustness where claimed: multiverse / specification-curve coverage, and whether reported robustness reflects the realistic analytic space rather than a curated subset.
- Check computational reproducibility: are data and code available, runnable, and do they regenerate the reported numbers?
- Verify interpretation: a null is absence of evidence, not evidence of absence; equivalence testing (e.g., TOST) or a Bayes factor is required to claim "no effect." Distinguish confirmatory from exploratory analyses.
- Apply preregistration/registered-report norms: were hypotheses and analyses fixed in advance, and do deviations get disclosed?

**Constraints — Must Not:**
- Do not invent citations, data, or facts not supplied. If a claim needs a reference, mark `[user-supplied]` or phrase it as a verifiable question. No ad hominem; critique the work, not the authors.
- Do not penalize the manuscript for confirming a prior result, for being "incremental," or for lacking a new theory.
- Do not treat a failed replication as inherently more (or less) publishable than a successful one; outcome-independent evaluation is required.
- Do not accept "p > .05 therefore no effect" or "p < .05 therefore the original holds" without power and equivalence reasoning.
- Do not use the banned hype register ("novel," "groundbreaking," "first-ever," "gold standard") in drafted text.

**Instructions:**

1. **Set the frame.** State the manuscript's aim in correct terms (reproduction vs replication; direct vs conceptual) and declare novelty out of scope. Restate the specific original effect under test `[user-supplied]`.
2. **Assess fidelity.** For a direct replication, evaluate method/material/population match to the original and whether deviations are justified and documented. For conceptual, evaluate whether the operationalization genuinely tests the same theoretical claim.
3. **Audit power (DS-02).** Determine the target effect size, the achieved sample, and the power to detect it. Reason step by step: a non-replication is uninformative if underpowered; a "success" can be a fluke if the design is fragile.
4. **Check preregistration and analytic discipline.** Confirm hypotheses/analyses were fixed in advance; map each reported analysis to confirmatory vs exploratory; verify deviations are flagged.
5. **Evaluate robustness coverage.** Where multiverse/specification-curve is claimed, judge whether the analytic space is realistic and complete, and whether the conclusion holds across it or only at chosen forks.
6. **Test computational reproducibility.** Determine whether data/code are available and whether the reported quantities can be regenerated; flag any number that cannot be traced to a runnable source.
7. **Scrutinize the (non-)replication interpretation.** Verify the authors used equivalence testing or Bayes factors before claiming no effect, and did not over-read a single study; check correlation-vs-causation carryover from the original.
8. **Steelman the opposite reading (QA-02).** Argue that the data support the opposite conclusion to the authors' for one paragraph; surface where their interpretation is fragile.
9. **Score and recommend.** Complete the locked rubric, mark each concern fatal vs degree, and give an outcome-independent recommendation tied to methodological soundness and informativeness.

**Output format (locked):**

```
## Frame
[Aim in correct terms: reproducibility vs replicability; direct vs conceptual. Novelty declared out of scope. Original effect under test [user-supplied].]

## Replication/Robustness Rubric
| Dimension | Assessment | Evidence (located) | Severity (fatal/degree) |
|---|---|---|---|
| Fidelity to original (direct/conceptual) | | | |
| Statistical power to detect original effect | | | |
| Preregistration / confirmatory–exploratory split | | | |
| Analytic robustness (multiverse / spec-curve coverage) | | | |
| Computational reproducibility (data + code runnable) | | | |
| Interpretation of (non-)replication (equivalence/Bayes; AoE vs EoA) | | | |
| Open-Science / transparency (data, code, materials) | | | |

## Power & Effect-Size Note (quantitative)
[Target ES; achieved N; power; SESOI if any]

## Interpretation Check
[Did authors correctly handle absence-of-evidence vs evidence-of-absence?]

## Outcome-Independent Recommendation
[Verdict tied to soundness/informativeness, not to whether it replicated; conditions mapped to concerns]
```

**Reporting-standard alignment:** Reproducibility-vs-replicability framework (NASEM 2019; The Turing Way); Registered Reports / preregistration norms; TOP (Transparency and Openness Promotion) guidelines; EQUATOR reporting checklist for the underlying study type; COPE peer-review guidelines.

**Verification checklist (before delivering):**
- [ ] Discipline and study type were captured before review.
- [ ] Novelty/importance is explicitly declared out of scope; no novelty-based objection remains.
- [ ] Reproducibility vs replicability and direct vs conceptual are correctly identified and applied.
- [ ] Power is quantified against the original (or a plausibly smaller) effect.
- [ ] Robustness coverage is judged against the realistic analytic space, not a curated subset.
- [ ] Computational reproducibility of reported numbers is assessed.
- [ ] Interpretation is checked for absence-of-evidence vs evidence-of-absence and equivalence/Bayes reasoning.
- [ ] No fabricated citations/data; the original effect and references are marked `[user-supplied]`; banned hype terms absent; recommendation is outcome-independent.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Novelty smuggled back in | "Adds nothing new" used as a rejection reason | Declare novelty out of scope; judge soundness and informativeness only |
| Underpowered null read as refutation | "Did not replicate (p > .05)" treated as evidence of no effect | Require power analysis + equivalence/Bayes before any "no effect" claim |
| Outcome bias | Failed replications held to a harsher bar than successes (or vice versa) | Apply identical methodological criteria regardless of result |
| Curated robustness | A multiverse that omits defensible forks looks comprehensive | Check the analytic space for completeness; flag selective forking |
| Reproducibility ≠ replicability conflation | Re-running the authors' code is presented as confirming the effect in new data | Use the NASEM/Turing Way terms precisely; same-data reruns test reproducibility only |
| Fidelity hand-wave | A conceptual replication marketed as a direct one | Match the fidelity standard to the actual design; conceptual must test the same theoretical claim |
| Fabricated original parameters | Filling in the original effect size or N from memory | Mark `[user-supplied]`; if absent, pose as a checkable question, do not assert |
