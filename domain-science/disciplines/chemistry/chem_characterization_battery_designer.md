---
title: "Characterization Battery Designer"
category: science/disciplines/chemistry
description: "Specify a minimum and recommended characterization battery for a new compound or material per compound class, with claim-to-method traceability"
techniques:
  - ST-01
  - ST-03
  - CM-02
  - DS-02
  - QA-02
difficulty: intermediate
tags:
  - characterization
  - nmr
  - mass-spectrometry
  - x-ray
  - elemental-analysis
  - purity
  - structure-elucidation
updated: "2026-05-19"
related_prompts:
  - domain-science/disciplines/chemistry/chem_synthesis_route_critique.md
---

# Characterization Battery Designer

**Objective:** Specify the minimum and recommended characterization battery for a new chemical entity or material, mapped one-to-one to the structural / purity / property claims the user intends to make in a paper, thesis, or report. Every method in the battery exists to support a named claim; no method-for-its-own-sake.

**When to use:** Before scheduling instrument time after a target compound (or batch of variants) has been made, or before submitting a manuscript whose claims rely on characterization data. Equally useful for triage: "I have this much data, is that enough for the claim I want to make?"

**Required inputs:**
- **Compound class.** Small-molecule organic; organometallic; inorganic / coordination complex; polymer; nanoparticle; framework (MOF / COF); peptide / oligonucleotide; mixture / formulation.
- **Target claim set.** Identity, connectivity, stereochemistry, purity (chemical), purity (optical), regiochemistry, molecular weight / dispersity, crystallinity, surface composition, particle size, porosity, electronic / optical property.
- **Sample form.** Solid, liquid, solution, gas, thin film, suspension.
- **Scale on hand** (mg available — drives whether elemental analysis / SCXRD are feasible).
- **Journal or thesis target** if known (some journals require specific methods).

**Optional inputs:**
- Instruments accessible in-house vs. external-facility wait time.
- Sample stability (air, moisture, light, heat).
- Whether the compound is novel vs. known.

**Constraints — Must:**
- Map every method in the battery to a specific claim it supports. Each row in the battery table has a "supports which claim" column.
- Distinguish *necessary* methods (claim not supportable without them) from *recommended* (strengthen the claim) and *optional* (depth and confirmation).
- For purity claims, specify the threshold (e.g., ≥95% by qNMR, ≥98% by HPLC at named wavelength) and the orthogonal method that backs it (one purity number is not enough for novel compounds).
- For stereochemistry claims, distinguish relative configuration (NOESY / J-coupling / X-ray) from absolute configuration (X-ray with heavy atom / anomalous dispersion; chiral SFC vs. known standard; VCD / ECD with calculated reference).
- Align reporting to journal house style and ACS Authors Guide / RSC Guide where applicable. For materials: align to standard chars (PXRD + TGA + N2 sorption for MOFs; SAXS + DLS + TEM for nanoparticles).
- Always specify the deuterated solvent for NMR, the matrix / ionization mode for MS, the wavelength for HPLC / UV.

**Constraints — Must Not:**
- Do not invent specific instrument models, vendor names, or reference compound catalog numbers unless the user supplies them.
- Do not propose a single-method "proof of structure" for a novel compound.
- Do not propose elemental analysis at sub-mg quantities (typically 2–5 mg minimum).
- Do not infer absolute configuration from optical rotation alone unless against a literature-known sample of the same compound class with similar substitution.
- Do not skip the orthogonal purity method for biological / pharmacological use.

**Instructions:**

1. **Lock the claim set.** Write each claim as a single sentence with what is being asserted and at what confidence threshold (identity vs. tentative; ≥95% pure vs. ≥99%; relative vs. absolute stereochemistry).

2. **Map class to standard battery.** From the compound class, pull the community-expected baseline battery. Small organic: 1H / 13C / HRMS / IR / mp (if crystalline) / HPLC purity / chiral SFC if stereogenic / SCXRD where possible. Organometallic: add multinuclear NMR (31P, 19F, 11B, 195Pt as applicable), elemental analysis, SCXRD when feasible. Inorganic / coordination: PXRD + magnetic moment / EPR / UV-Vis-NIR / cyclic voltammetry as applicable. Polymer: SEC / GPC + dispersity + end-group analysis + DSC + TGA. Nanoparticle: TEM + DLS + SAXS + UV-Vis or PL + XPS / ICP-MS for composition. MOF / COF: PXRD + N2 / Ar sorption + TGA + SEM + variable-temperature PXRD for stability. Peptide / oligonucleotide: HRMS / LC-MS + analytical HPLC purity + amino-acid analysis or sequencing.

3. **Per-method specification.** For each method selected, output: claim supported, sample state requirement, sample mass, deuterated solvent / mobile phase / matrix, key parameters (NMR field, scan count, relaxation delay, MS resolution, HPLC column / gradient / detector wavelength), what counts as a passing result, what would invalidate the claim, and the cost / queue-time category (in-house / external / heroic).

4. **Purity orthogonality.** Specify two orthogonal purity methods for novel compounds (e.g., qNMR + HPLC at two wavelengths; or HPLC + elemental analysis). State the threshold and what the user reports.

5. **Stereochemistry / regiochemistry strategy.** For chiral compounds: relative-config method (NOESY, J-couplings, X-ray) plus absolute-config method (SCXRD with anomalous dispersion, chiral SFC vs. authentic sample, VCD or ECD with DFT-calculated reference). For regiochemistry: HMBC / NOESY assignment plus X-ray confirmation when possible.

6. **Class-specific must-haves.** Surface the field's non-negotiables and the common reviewer rejections (e.g., for nanoparticles: TEM size distribution from ≥100 particles; for MOFs: PXRD match to simulated pattern from single-crystal data; for polymers: dispersity reported with method; for peptides: HRMS within 5 ppm + HPLC purity ≥95%).

7. **Triage path.** If the user has data already, build a gap table: claim → supporting method present → confidence → gap. Recommend the smallest set of additional measurements that close the gaps.

8. **Reporting block stub.** Output the SI Compound-Characterization Block template the user will paste into the supporting information, with placeholders for each measurement.

**Output format (locked):**

```
## Locked claim set
| Claim | Confidence threshold |

## Standard battery for compound class
[name class and pull baseline]

## Per-method specification
| Method | Supports claim | Sample state / mass | Solvent / matrix | Key parameters | Pass criterion | Invalidator | Cost / queue |

## Purity orthogonality
- Primary method + threshold:
- Orthogonal method + threshold:

## Stereochemistry / regiochemistry strategy
- Relative config:
- Absolute config:
- Backup:

## Class-specific must-haves
[the field's non-negotiables and common reviewer rejections]

## Triage gap analysis (if data exist)
| Claim | Method on hand | Confidence | Gap | Smallest additional measurement |

## SI Compound-Characterization Block (stub)
[ready-to-paste template with placeholders]

## Open questions for the user
[gaps marked [user-supplied]]
```

**Reporting-standard alignment:** ACS Authors Guide / RSC Author Guidelines / IUPAC nomenclature; CIF deposition at CCDC for SCXRD; CheckCIF acceptance for crystal structures; standard journal-specific SI requirements; for materials, the relevant minimum-information community standards (PXRD pattern match for MOFs; ≥100-particle TEM count for NPs; SEC with internal standard for polymers).

**Verification checklist:**
- [ ] Every method maps to a named claim.
- [ ] Novel compound has at least two orthogonal purity methods.
- [ ] Stereochemistry strategy distinguishes relative vs. absolute.
- [ ] Class-specific must-haves surfaced (TEM count, PXRD match, dispersity, etc.).
- [ ] Sample mass requirements stated per method.
- [ ] No invented instrument models, reference standards, or CCDC numbers.
- [ ] SI block stub ready for paste.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Single-method "proof of structure" | "HRMS + 1H matches — done" for a novel compound | Class baseline enforced |
| Single purity number | HPLC at one wavelength reported as 99% | Orthogonal method required |
| Absolute from optical rotation alone | "[α]_D matches enantiopure" for a new substituent class | Heavy-atom X-ray or vs. authentic sample required |
| Insufficient particle count (NPs) | TEM size distribution from 20 particles | ≥100 required |
| PXRD reported without simulation match (MOFs) | Pattern looks "consistent" | Simulated-pattern overlay required |
| Polymer dispersity unmoored | Đ reported without SEC standard or method | Method + standard specified |
| Cryptic NMR parameters | Field / solvent / scans omitted | Per-method parameter row enforced |
| Invented CCDC / catalog reference | Plausible-looking deposit number | All citations user-supplied or marked missing |
