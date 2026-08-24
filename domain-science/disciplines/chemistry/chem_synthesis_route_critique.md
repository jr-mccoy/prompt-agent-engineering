---
title: "Synthesis Route Critique"
category: science/disciplines/chemistry
description: "Critique a proposed synthetic route on retrosynthetic logic, step economy, selectivity, scalability, green-chemistry posture, and hazard exposure"
techniques:
  - ST-01
  - ST-03
  - RT-03
  - QA-02
  - CM-02
difficulty: advanced
tags:
  - synthesis
  - retrosynthesis
  - route-scouting
  - green-chemistry
  - process-chemistry
  - hazard-assessment
updated: "2026-05-19"
related_prompts:
  - domain-science/disciplines/chemistry/chem_characterization_battery_designer.md
  - domain-science/disciplines/chemistry/chem_reaction_kinetics_experimental_designer.md
---

# Synthesis Route Critique

**Objective:** Critique a proposed multi-step synthetic route against the working chemist's checklist: retrosynthetic logic, step / atom / redox economy, chemo- / regio- / stereoselectivity, scalability and process robustness, green-chemistry posture, and hazard exposure. Output is a structured critique that prioritizes the highest-leverage issues, not a flat list.

**When to use:** When a user (graduate student, postdoc, process chemist, medicinal chemist) brings a drawn or written synthetic route and wants a defensible third-pass review before committing reagents and time. Equally useful for reviewing routes in a manuscript or grant.

**Required inputs:**
- **Target structure** (SMILES, InChI, or drawn — user provides).
- **Proposed route**, step-by-step, including reagents, solvents, conditions, scale, and intended selectivity outcome for each step.
- **Purpose.** Target identification milligrams, gram-scale for in-vivo, kilogram-scale process, materials application, total synthesis.
- **Constraints.** What the user will not do (no chromatography, no flash, no hazardous reagents above a certain class, no cryogenics, no flow available, etc.).

**Optional inputs:**
- Known literature precedent (user-supplied citations).
- Yield / selectivity numbers from prior attempts.
- Available starting-material pool (in-house, commercial below $X / g, custom-synthesis allowed).

**Constraints — Must:**
- Treat retrosynthetic logic as primary: every step is assessed against the strategic bond disconnection it serves.
- Score every step on step economy, atom economy (or PMI / E-factor where appropriate), and redox economy.
- Surface chemo-, regio-, and stereoselectivity issues per step. Distinguish "selectivity asserted by precedent" from "selectivity inferred from analogy."
- Score hazards per step: pyrophorics, peroxide formers, toxic gases, oxidizers, exotherm risk, scale-up risk (gas evolution, runaway, dust explosion).
- Surface green-chemistry posture per step: solvent class (per CHEM21 / Sanofi / Pfizer guides), waste posture, catalyst loading, atom economy.
- Identify the route's bottleneck step (lowest yield, lowest selectivity, highest hazard, highest cost) — there is always exactly one.

**Constraints — Must Not:**
- Do not invent literature precedent. If a step requires a citation and the user has not supplied one, mark `[precedent required]` and ask.
- Do not invent yields, selectivities, or melting points.
- Do not propose proprietary reagents the user has not indicated access to.
- Do not silently ignore a hazardous step because the route "would work in theory."
- Do not turn the critique into a rewrite of the route. Critique first; alternatives only after critique is complete.

**Instructions:**

1. **Retrosynthetic audit.** Trace the route backward from the target. Identify the strategic disconnections (Corey-style or modern transition-metal disconnections). State whether the disconnections are convergent or linear, and surface the longest linear sequence (LLS). Score: is the LLS appropriate for the scale and purpose?

2. **Per-step assessment.** For each forward step, output a row with the following columns: bond / FG made, mechanism class, expected selectivity (with precedent type: closely analogous / loosely analogous / inferred), expected yield band, scale risk, hazard class, solvent class, atom economy posture, and dominant failure mode. Mark every cell whose value depends on unsupplied data as `[user-supplied]`.

3. **Selectivity audit.** Flag every step that creates a new stereocenter or selectivity issue. Distinguish substrate-controlled, reagent-controlled, and catalyst-controlled. For each, state how the selectivity will be measured (HPLC, NMR, chiral SFC) and the chance-baseline (no control = 50:50 or statistical ratio).

4. **Step / atom / redox economy.** Compute or estimate, per step: number of new bonds formed, atom economy (or PMI estimate), oxidation-state change count. Sum across the route. Compare to a hypothetical ideal (single-step, atom-economic).

5. **Scale / process robustness.** For each step, flag: cryogenic requirement, slow addition / dosing-controlled exotherm, gas evolution, light sensitivity, oxygen / moisture sensitivity, work-up complexity, chromatography requirement. Surface anything that does not scale.

6. **Hazard audit.** For each step, flag the highest hazard from: pyrophoric reagent, peroxide-forming solvent, toxic gas, energetic intermediate (especially azides / diazos / N-O / N-N rich), explosive functional group, runaway potential. Surface the worst single hazard and the route's accumulated hazard exposure.

7. **Green-chemistry posture.** Solvent assessment per step (CHEM21 / GSK / Sanofi / Pfizer-style green guide). Catalyst loading. Stoichiometry of reagents vs. equivalents wasted. Waste / E-factor posture. Atom economy. Surface the worst solvent and the worst stoichiometry.

8. **Bottleneck step identification.** Name the single bottleneck step. Justify by yield × selectivity × scale-risk × hazard.

9. **Failure-mode register.** For the bottleneck step and the top three other risk steps, output the four most likely failure modes and the corresponding diagnostic (TLC, NMR, MS, color change, gas evolution).

10. **Alternatives (only after critique).** Propose **at most two** route variants that address the bottleneck — by changing the disconnection, by substituting reagents, or by reordering steps. Score each variant on the same matrix.

**Output format (locked):**

```
## Retrosynthetic audit
- Target:
- Strategic disconnections:
- LLS:
- Convergent / linear:

## Per-step matrix
| Step | Bond / FG | Mechanism | Selectivity (precedent type) | Yield band | Scale risk | Hazard | Solvent class | Atom economy | Failure mode |

## Selectivity audit
| Step | New center / issue | Control mode | Measurement | Chance baseline |

## Economy summary
| Metric | Per-step | Route total | Ideal |
| New bonds | | | |
| Atom economy / PMI | | | |
| Redox-state changes | | | |

## Scale / process robustness
| Step | Cryo | Exotherm | Gas | O2/H2O sens. | Chromato. | Scale verdict |

## Hazard audit
| Step | Worst single hazard | Accumulated risk |

## Green-chemistry posture
| Step | Solvent class | Stoichiometry / equivalents wasted | Catalyst loading | Posture |

## Bottleneck step
- Step:
- Why:

## Failure-mode register
| Step | Failure mode | Diagnostic |

## Route variants (max 2)
| Variant | Change | Effect on bottleneck | New risks |

## Open questions for the user
[gaps marked [precedent required] or [user-supplied]]
```

**Reporting-standard alignment:** ACS Green Chemistry Institute solvent guides; CHEM21 solvent selection; ACS publications data-sharing requirements; informally, IUPAC guidance on selectivity / yield reporting.

**Verification checklist:**
- [ ] Retrosynthetic disconnections named.
- [ ] Every step assessed on selectivity / yield / scale / hazard / solvent / atom economy.
- [ ] Precedent type labeled for each selectivity claim.
- [ ] Bottleneck step identified and justified.
- [ ] Hazard audit names the single worst hazard.
- [ ] At most two alternatives, each scored on the same matrix.
- [ ] No invented citations, yields, or selectivities.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Precedent inflation | "Will work — there's literature" without showing it transfers | Precedent type labeled (closely / loosely / inferred) |
| Optimistic yield averaging | Compounding 80% × 80% × 80% on assumed yields | Yield band per step + LLS yield product computed |
| Selectivity assumed from analogy | Stereocenter "controlled" because related substrate worked | Selectivity-control mode named per step |
| Hazard normalized | Routine reagents that became hazardous at scale (NaH / DMF, NaH / DMSO) | Scale-up risk column explicit |
| Solvent inertia | DCM / DMF used because precedent did | Solvent class scored against green guide |
| Bottleneck blindness | Critique flat across steps | Single bottleneck named |
| Route rewrite masquerading as critique | Critique becomes proposal | Two-variant ceiling enforced |
| Invented reference | Plausible-looking JACS / OL / Synlett citation | `[precedent required]` instead |
