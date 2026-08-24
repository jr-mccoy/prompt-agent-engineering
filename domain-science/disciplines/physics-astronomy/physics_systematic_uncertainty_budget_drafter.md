---
title: "Systematic Uncertainty Budget Drafter"
category: science/disciplines/physics-astronomy
description: "Draft a systematic-uncertainty budget item by item, with magnitudes, propagation method, correlations, dominant sources, and a sanity check against the precision claim"
techniques:
  - ST-01
  - ST-03
  - CM-02
  - DS-02
  - QA-02
difficulty: advanced
tags:
  - systematics
  - uncertainty
  - error-budget
  - correlations
  - propagation
  - precision-measurement
updated: "2026-05-19"
related_prompts:
  - domain-science/disciplines/physics-astronomy/physics_observable_and_measurement_chain_designer.md
---

# Systematic Uncertainty Budget Drafter

**Objective:** Draft an itemized systematic-uncertainty budget for a physics or astronomy measurement, with each entry's magnitude, sign, propagation method, correlation structure, and a sanity check that the precision claim survives the dominant systematic.

**When to use:** As part of analysis-note preparation, before pre-approval / collaboration review; when responding to reviewer comments on systematics; when designing a measurement to evaluate whether the target precision is achievable.

**Required inputs:**
- **Measurement.** Observable and POI; current best estimate of the central value if available.
- **Statistical uncertainty.** Known or estimated.
- **Target total uncertainty.**
- **Calibration sources and their assigned uncertainties** (user-supplied where available).
- **Simulation and data control regions** used in the analysis.

**Optional inputs:**
- Previous analyses' systematics tables (user-supplied).
- Known cross-experiment correlations (e.g., shared luminosity, shared theoretical input).
- Pending calibration improvements with anticipated reduction.

**Constraints — Must:**
- Itemize every systematic source. Forbid "other" or "miscellaneous" exceeding a small fraction of the total (commonly 5%).
- For each item, specify: nature (multiplicative / additive / shape-shifting / migrating), evaluation method (variation in toy MC; in-data control region; auxiliary measurement; theory variation; bracketed scenarios), magnitude on the POI, sign or shape, and correlation with other items.
- Distinguish *correlated* systematics (between bins, between channels, between experiments) from *uncorrelated*. Propagate accordingly. State the correlation matrix or at least the correlation block structure.
- Identify the dominant systematic (largest single contribution to total) and the dominant two. Compute total in quadrature *only* if items are uncorrelated; otherwise via the covariance matrix.
- Sanity-check: does the precision claim survive variation of the dominant systematic by ±50%? If not, the claim is dominant-systematic-bound and must be reported that way.
- Align to GUM expanded-uncertainty notation for metrology; to PDG conventions for HEP; to journal-specific tables for astrophysics.

**Constraints — Must Not:**
- Do not invent magnitudes of systematics, prior experiments' tables, or theoretical-variation references.
- Do not double-count by including both a variation and the calibration that already accounts for it.
- Do not silently apply quadrature when correlations exist.
- Do not bury the dominant systematic in a footnote.
- Do not report only stat uncertainty when the systematic is comparable or larger.

**Instructions:**

1. **Build the source list.** Walk every step of the measurement chain (calibration, detector response, selection, reduction, unfolding, modeling, theory input, luminosity / livetime, atmospheric / cosmic / instrumental backgrounds) and produce one row per source. Add a "physics-input" row for theoretical uncertainties (PDFs, scale variations, branching ratios) where applicable.

2. **For each row, name the evaluation method.** Choose from: toy-MC variation; data control region; auxiliary calibration; theory bracket; alternative model; conservative bracket from physical argument. State which calibration / auxiliary measurement is the source if applicable, and mark `[user-supplied]` if not anchored.

3. **Quantify magnitude on the POI.** Symmetric ±x% on the POI, or asymmetric +x / −y where appropriate. For shape systematics, describe the shift mode (bin-by-bin; smooth function of observable; migration matrix variation).

4. **Specify correlations.** Per row: correlated across bins? across channels? across years / runs? across experiments? Build a block-correlation structure if matrix is too large.

5. **Combine.** Sum in quadrature only after correlations are explicit. Otherwise carry a covariance matrix through; if combining channels, propagate the covariance.

6. **Identify dominants.** Rank the table. State the dominant one, the dominant two, the dominant-three. State what fraction each contributes to total in quadrature.

7. **Sanity / robustness check.** Vary the dominant systematic by ±50%, recompute total, and state whether the precision claim survives. Repeat for the second dominant.

8. **Reduction plan.** For the dominant two, sketch what would actually reduce them: more calibration data; tighter selection; alternative theory input; auxiliary measurement.

9. **Reporting block.** Output the systematics table in the format the target journal / collaboration expects, plus a one-paragraph narrative summary.

**Output format (locked):**

```
## Header
- Observable / POI:
- Stat uncertainty:
- Total target uncertainty:

## Itemized systematics table
| Source | Nature (mult / add / shape / migration) | Evaluation method | Magnitude on POI | Sign / shape | Correlated with |

## Correlation structure
- Within-table correlations:
- Cross-experiment correlations:

## Combination
- Method (quadrature vs. covariance):
- Total systematic:
- Total uncertainty (stat ⊕ syst):

## Dominants
| Rank | Source | Fraction of total² |

## Robustness check
| Dominant source | ±50% variation effect on total | Does claim survive? |

## Reduction plan
| Dominant | What would reduce it | Timeline / cost |

## Final reporting block
[table in target-journal / collaboration format]

## Open questions for the user
[gaps marked [user-supplied]]
```

**Reporting-standard alignment:** GUM and CIPM / BIPM for metrology; PDG (Particle Data Group) for HEP; ATLAS / CMS / LHCb / Belle II analysis-note systematic-table conventions; journal-specific systematic-disclosure conventions for astrophysics.

**Verification checklist:**
- [ ] Every chain step has at least one corresponding systematic row.
- [ ] Evaluation method named per row.
- [ ] Correlation structure explicit; quadrature only after correlations stated.
- [ ] Dominant two systematics identified.
- [ ] Robustness check at ±50% on dominants performed.
- [ ] No invented magnitudes; missing entries marked `[user-supplied]`.
- [ ] Final block matches target-journal / collaboration format.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Quadrature with hidden correlations | Adding correlated PDF + scale variations independently | Correlation column required |
| Buried dominant | Largest entry deep in a sub-table | Rank table + narrative call-out |
| Double-counting | Calibration uncertainty *and* alternate-calibration bracket both included | Audit pass for redundancy |
| Theory-input invention | "PDF uncertainty ≈ 2%" with no source | `[user-supplied]` if not from PDF4LHC etc. |
| Shape→single-number flattening | Shape syst reported as single % | Shape mode described |
| Underestimated from "looks small" | Bracket too narrow because it would be inconvenient | Explicit ±50% sensitivity test |
| Single-number error bar | stat ⊕ syst reported without decomposition | Decomposition required |
| Mismatch with target format | Table doesn't match journal expectations | Output block in target format |
