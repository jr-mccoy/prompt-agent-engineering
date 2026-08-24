---
title: "Materials Failure Analysis Protocol"
category: science/disciplines/materials-engineering
description: "Root-cause failure analysis for a material / component: evidence preservation, visual → fractographic → microstructural → service-condition reconstruction, and counterfactual test"
techniques:
  - ST-01
  - ST-03
  - RT-03
  - QA-02
  - CM-02
difficulty: advanced
tags:
  - failure-analysis
  - fractography
  - root-cause
  - forensic
  - service-condition
  - counterfactual
updated: "2026-05-19"
related_prompts:
  - domain-science/disciplines/materials-engineering/materials_synthesis_and_characterization_plan.md
---

# Materials Failure Analysis Protocol

**Objective:** Diagnose the root cause of a materials / component failure using a structured chain — evidence preservation → service-condition reconstruction → visual / dimensional inspection → fractographic analysis → microstructural / compositional analysis → mechanical / environmental reproduction → counterfactual test — and produce a defensible attribution that distinguishes the primary cause from contributory factors.

**When to use:** When a component has failed in service, in test, or in manufacture and the team needs a root-cause analysis that will hold up to regulator, insurer, customer, or peer-review scrutiny. Also useful when the team's first-pass diagnosis "smells right" but rests on one or two observations.

**Required inputs:**
- **The failure event.** Component identity, function, location of failure on the component, mode of discovery, time of failure.
- **Service history.** Manufacturing date, install date, environment, load history (steady / cyclic / impact), temperature range, atmosphere / chemistry, prior repairs, prior inspections.
- **Failed sample condition.** Has it been cleaned? Are mating fracture surfaces preserved? Is corrosion product intact? Is the component still installed?
- **Available analysis tools.** Visual, stereo microscopy, SEM-EDS, optical metallography, hardness, residual-stress measurement, mechanical testing, chemical analysis, CT, NDT (UT / RT / dye penetrant / MT).
- **Stakeholders.** Regulator / insurer / customer / internal — affects rigor of documentation and chain-of-custody.

**Optional inputs:**
- Original material specification (composition, processing, mechanical-property minima).
- Design loads.
- Similar prior failures (user-supplied).

**Constraints — Must:**
- Preserve evidence first. Forbid any destructive prep until evidence-preservation steps are complete: photographic record (calibrated, scaled, lit from multiple angles), dimensional documentation, fracture-surface preservation (no cleaning of mating surfaces), chain-of-custody documented.
- Walk the analysis from non-destructive to destructive, low-magnification to high-magnification. Forbid jumping to SEM-EDS before stereo / visual.
- Distinguish primary fracture initiation site from secondary cracking and overload zone. Common fractography signatures (beach marks, ratchet marks, river marks, chevrons, dimples, cleavage facets, intergranular surface, fatigue striations) must be supported by evidence, not asserted.
- Build a fault-tree with at least three plausible root causes. For each, list the predicted observations and the disconfirming observations.
- Run a counterfactual test: would the failure have occurred under the as-designed material / process / service envelope? If yes, root cause is design or specification; if no, root cause is deviation. Specify the test.
- Distinguish primary cause (without which the failure would not have occurred), contributory factors (which made the failure more likely or more severe), and consequence chain.
- Align reporting to ASM Handbook Vol. 11 (Failure Analysis and Prevention); relevant ASTM E1188 / E1492 for evidence handling; industry-specific (API 581, NTSB-style aircraft, FDA-style medical-device) where applicable.

**Constraints — Must Not:**
- Do not invent material specifications, service histories, or instrument identifications.
- Do not clean a fracture surface before microscopy.
- Do not call a fracture mode (fatigue / brittle / ductile / SCC / hydrogen embrittlement / creep) without the corroborating fractographic + microstructural evidence.
- Do not name a single root cause without considering at least two alternatives.
- Do not allow stakeholder framing (insurance / regulatory) to drive the conclusion ahead of evidence.
- Do not omit chain-of-custody documentation for failures that may become legal.

**Instructions:**

1. **Evidence preservation.** Before any prep:
    - Photograph (calibrated scale, multiple lighting angles, stereomicroscope and macro).
    - Document orientation (which side is up, in-situ position).
    - Capture corrosion / contamination products (separate samples).
    - Record dimensional measurements (per drawing if available).
    - Chain-of-custody log entry.

2. **Service-condition reconstruction.** From the user: load history, environment, temperature, atmosphere, prior repairs. Identify any deviation from the design envelope. Mark gaps as `[user-supplied required]`.

3. **Hypothesis set.** Output at least three candidate root causes with the expected observation set per cause:
    - Fatigue (beach marks / striations / ratchet marks at initiation; stress-concentrator at origin).
    - Overload (necking / shear lip / dimpled rupture; or cleavage in brittle service).
    - Stress-corrosion cracking (intergranular or transgranular branching, corrosion products at initiation, susceptible alloy + environment + tensile stress).
    - Hydrogen embrittlement (intergranular fracture in susceptible alloy, often delayed failure, near-threshold loads).
    - Creep (cavitation, grain-boundary triple-junction voids, recrystallization).
    - Manufacturing defect (inclusions, porosity, lack-of-fusion in welds, decarburization).
    - Material specification deviation (composition / heat-treat off-spec).
    - Design deviation (under-sized; wrong material grade).
    - Service deviation (over-load, over-temperature, off-spec environment).

4. **Visual / stereo inspection.** Low-magnification mapping: initiation site, propagation path, final overload zone. Mark on annotated photograph. Identify candidate origin.

5. **Fractography.** SEM imaging of fracture surface from initiation to overload, with EDS where contamination / corrosion product is present. Capture: initiation morphology, propagation morphology (smooth / striated / cleavage / dimples / intergranular), overload morphology. Cross-check against hypothesis set.

6. **Microstructural and compositional analysis.** Optical metallography of cross-sections (etched per material standard); SEM-EDS / WDS for inclusions / segregation; chemical analysis (ICP / OES) for bulk composition; hardness mapping; if applicable, residual-stress measurement (XRD / hole-drilling); CT for sub-surface features.

7. **Mechanical / environmental reproduction (where feasible).** Reproduce service conditions on a sister specimen or representative sample. Compare failure morphology to the original. State the test: tensile, fatigue with appropriate R-ratio, environmental fracture, slow-strain-rate test.

8. **Hypothesis test against evidence.** For each candidate root cause, score the evidence: corroborates / disconfirms / silent. Drop hypotheses with disconfirming evidence. Identify the surviving hypothesis or the smallest hypothesis set the evidence does not separate.

9. **Counterfactual.** Ask: if material / process / service were within specification, would the failure have happened? If yes → design / spec root cause. If no → deviation root cause. Specify which deviation.

10. **Reporting and recommendations.** Output the report with: executive summary (single-sentence root cause + confidence), evidence chain, hypothesis-evidence matrix, primary cause, contributory factors, recommendations (material, design, manufacturing, inspection, monitoring), recommendations' priority and expected effect.

**Output format (locked):**

```
## Failure event
- Component / function:
- Failure mode of discovery:
- Service age:

## Evidence preservation log
| Step | Date | Operator | Output |

## Service-condition reconstruction
- Load history:
- Environment:
- Temperature:
- Prior repairs:
- Deviations from design envelope:

## Candidate root-cause hypothesis set
| Hypothesis | Expected observation | Disconfirming observation |

## Visual / stereo mapping
- Initiation site:
- Propagation path:
- Final-overload zone:
- Annotated photograph location:

## Fractography
| Region | Morphology | Evidence (image refs) | Hypothesis support |

## Microstructural and compositional analysis
| Method | Sample location | Observation | Hypothesis support |

## Mechanical / environmental reproduction
- Test:
- Comparison to original morphology:

## Hypothesis-evidence matrix
| Hypothesis | Corroborates | Disconfirms | Silent | Verdict |

## Counterfactual test
- Would within-spec material / process / service still have failed?
- Specific deviation (if any):

## Primary cause + contributory factors
- Primary cause (with confidence):
- Contributory factors:

## Recommendations
| Action | Type (material / design / mfg / inspection / monitoring) | Priority | Expected effect |

## Reporting standard alignment
[ASM Handbook v11; ASTM E1188 / E1492; industry-specific]

## Open questions / unresolved
[evidence gaps and what would close them]
```

**Reporting-standard alignment:** ASM Handbook Volume 11 (Failure Analysis and Prevention); ASTM E1188 (Collection and Preservation of Information and Physical Items by a Technical Investigator); ASTM E1492 (Receiving, Documenting, Storing, and Retrieving Evidence in a Forensic Science Laboratory); industry-specific (NTSB, FDA 21 CFR 820 for medical devices, API 581 for risk-based inspection). For peer-reviewed publication: appropriate engineering-failure journal conventions.

**Verification checklist:**
- [ ] Evidence preservation steps logged before any destructive prep.
- [ ] ≥3 hypothesis candidates with expected and disconfirming observations.
- [ ] Analysis walks low-mag to high-mag, non-destructive to destructive.
- [ ] Fracture mode assertion supported by fractographic + microstructural evidence.
- [ ] Hypothesis-evidence matrix shows survival path of conclusion.
- [ ] Counterfactual test specified.
- [ ] Primary cause and contributory factors distinguished.
- [ ] Recommendations prioritized.
- [ ] Chain-of-custody documented if stakes are legal / regulatory.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Single-hypothesis confirmation | "It's fatigue" without ruling out SCC | ≥3 hypotheses + matrix |
| Cleaned fracture surface | Corrosion products removed in eagerness | Evidence-preservation step |
| Direct-to-SEM | Stereo / visual skipped | Sequential mag escalation |
| Beach marks asserted without image | "Classic fatigue" without picture | Evidence reference per claim |
| Stakeholder framing drives result | Insurer wants overload conclusion | Hypothesis-evidence matrix transparent |
| Counterfactual skipped | Conclusion blames specification without testing | Explicit counterfactual step |
| Primary / contributory confusion | "Fatigue + corrosion + design" listed as equals | Primary identified, contributories named |
| Invented spec / service value | Plausible-looking applied-load number | `[user-supplied]` |
| No chain of custody | Sample changes hands without record | Log entry per transfer |
| Single-sample conclusion | One specimen used to infer fleet behavior | State limits of inference |
