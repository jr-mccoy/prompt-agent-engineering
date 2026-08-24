---
title: "Astronomical Data Reduction Pipeline Protocol"
category: science/disciplines/physics-astronomy
description: "Specify an astronomical reduction pipeline: calibration steps, quality flags, archive output, reproducibility, and validation against an independent reduction"
techniques:
  - ST-01
  - ST-03
  - CM-02
  - DS-02
  - QA-02
difficulty: advanced
tags:
  - astronomy
  - data-reduction
  - calibration
  - pipeline
  - reproducibility
  - archive-deposition
updated: "2026-05-19"
related_prompts:
  - domain-science/disciplines/physics-astronomy/astro_observing_proposal_drafter.md
  - domain-science/disciplines/physics-astronomy/physics_observable_and_measurement_chain_designer.md
---

# Astronomical Data Reduction Pipeline Protocol

**Objective:** Specify an astronomical reduction pipeline that converts raw frames to science-ready data products with calibration steps, quality flags, archive-ready output, version-pinned reproducibility, and validation against an independent reduction or facility pipeline.

**When to use:** When starting analysis of new data from an observing run, an archival query, or a survey release; when porting a working reduction to a new facility / mode; when a referee asks for reduction-systematics evidence; when building a survey product for public release.

**Required inputs:**
- **Facility / instrument / mode.**
- **Data type.** Imaging, long-slit / multi-object / IFU spectroscopy, polarimetry, interferometry, time-series photometry, RV spectroscopy, mm / submm interferometry, radio interferometry, high-energy event data.
- **Raw data state.** Direct from facility, calibrated-by-facility, partially reduced.
- **Calibration files available.** Flats, biases, darks, arcs, telluric stars, photometric standards, polarization standards, sky calibrations, drizzle / WCS solutions.
- **Final science data product.** Calibrated image, spectrum, light curve, mosaic, data cube, visibility set, cleaned map, event list.
- **Inference using the product** (so the pipeline can be tuned to the question — e.g., RV precision-floor for exoplanets vs. broad-line redshift).

**Optional inputs:**
- Facility's pipeline (DRAGONS / ESO Reflex / IRAF / PYRAF / PypeIt / CASA / ASTRORE / Iraf / specreduce / Eureka! / pyklip / CHIMERA / Lightkurve / heasoft / SAS / ciao).
- Survey-style requirements (LSST, Roman, Euclid).
- Public-release timeline.

**Constraints — Must:**
- Specify every step in order, with version-pinned software and explicit parameters. Each step has a quality criterion and a failure response.
- Pin software versions, compilers, libraries (numpy / scipy / astropy / casa / heasoft) and commit them as a `requirements.txt` / `environment.yml` / container image.
- Pin calibration-product versions and reference files (date stamp, archive ID). Mark `[user-supplied]` for any reference file the user has not named.
- Produce QC outputs: per-frame quality scalars (FWHM, ellipticity, sky background, gain stability, bias level, throughput, transparency), per-product quality flags, summary plots.
- Validate against either the facility pipeline or an independent reduction on a known calibration field. State the metric (e.g., photometric zero-point agreement within 0.02 mag; RV calibration agreement within 1 m/s; flux scale within 5%).
- Output archive-ready files with metadata sufficient to satisfy the target archive (MAST / ESA / NOIRLab Astro Data Lab / IRSA / VizieR / Zenodo) — FITS headers compliant; provenance recorded; checksums included.

**Constraints — Must Not:**
- Do not invent reference files, calibration-frame names, or pipeline-version numbers.
- Do not skip a calibration step because "the data look fine."
- Do not propagate quality flags silently — they must reach the science product header.
- Do not run a reduction on a moving target without explicit ephemeris handling.
- Do not coadd / drizzle / median frames without an outlier-rejection criterion.
- Do not deliver a data product without per-pixel / per-spaxel / per-time uncertainty maps.

**Instructions:**

1. **Goal-anchored tuning.** State the science measurement the product feeds. Identify which reduction steps are precision-critical for that measurement (e.g., flat-field for differential photometry; wavelength solution for RV; PSF model for crowded photometry; bandpass for cross-instrument color; bias / dark for low-flux X-ray).

2. **Step list.** Output the ordered pipeline. Each step has: input, output, software + version, parameters, QC criterion, failure response. Steps typically include: ingest + header sanitation; bias / dark; flat-field; cosmic-ray rejection; pixel-level masks; wavelength / WCS calibration; sky / background; flux / photometric / polarization calibration; combine (stack / drizzle / mosaic); extract (sources / spectra); coadd time-series; uncertainty map; provenance log; archive packaging.

3. **Calibration provenance.** For each calibration product (bias / flat / arc / standard / dark current / fringes / persistence), state its source (user-supplied or facility archive), version / date, and validation.

4. **Reference-frame and astrometric solution.** WCS source (Gaia DR3, USNO-B, GSC, 2MASS); per-frame residuals; tangent-plane projection; distortion correction.

5. **Outlier rejection / pixel masks.** Cosmic rays (LACosmic, image differencing, AstroDrizzle); detector masks; bad pixels, hot pixels, saturated pixels, bleed columns, persistence, charge-transfer; flagged in mask file and propagated.

6. **Uncertainty propagation.** Per-pixel σ from read-noise, dark, photon counting; per-spaxel / per-bin propagation through extraction; covariance from drizzle / coadd / interpolation; final product has matching uncertainty map.

7. **Reproducibility artifacts.** Container or environment file; pipeline script committed; intermediate-frame retention policy; checksum file (SHA-256); run-log capturing host, time, software versions, parameters.

8. **Validation.** Run on a calibration field / known target / facility-distributed test set. Compare to expected value (zero-point, RV, photometric color, spectrophotometric standard). State the pass criterion. If failure: stop, do not proceed.

9. **Quality flags surfaced.** Per-frame QC scalars in summary plot; per-product flags in FITS header; data products with flagged regions clearly identified.

10. **Archive packaging.** Per facility / archive expectation: FITS headers (WCSAXES, OBSGEO, BUNIT, PROVENANCE), MEF structure, ancillary tables (sources, extractions, masks, uncertainties), README, citation file, license, DOI registration.

**Output format (locked):**

```
## Science measurement the product supports
- Measurement:
- Precision-critical steps:

## Pipeline steps (ordered)
| Step | Input | Output | Software + version | Parameters | QC criterion | Failure response |

## Calibration provenance
| Calibration product | Source | Version / date | Validation |

## Astrometric / WCS solution
- Reference catalog:
- Per-frame residual target:
- Distortion correction:

## Outlier rejection and masks
- Cosmic rays:
- Detector masks:
- Bleed / saturation handling:
- Persistence handling:

## Uncertainty propagation
- Per-pixel:
- Per-extraction:
- Covariance through coadd / drizzle:
- Final-product uncertainty map:

## Reproducibility artifacts
- Container / env file:
- Pipeline script (path + commit):
- Intermediate-frame retention:
- Checksum policy:
- Run log content:

## Validation
- Test field / target:
- Pass criterion:
- Outcome:

## Quality flags
- Per-frame QC summary:
- Per-product flags:
- Flag propagation to header:

## Archive packaging
| Element | Format | Header keywords | Notes |

## Reporting standard alignment
[archive / facility-specific FITS conventions, IVOA standards, DOI / FAIR]

## Open questions for the user
[gaps marked [user-supplied]]
```

**Reporting-standard alignment:** FITS conventions (IAUFWG); IVOA standards (VOTable, SAMP, ObsCore); archive-specific submission formats (MAST HLSP, ESA Science Archive, NOIRLab Astro Data Lab); FAIR principles; DOI registration via Zenodo or facility data DOI services.

**Verification checklist:**
- [ ] Goal-anchored tuning identifies precision-critical steps.
- [ ] Every step has version-pinned software and parameters.
- [ ] Calibration provenance traceable for every calibration product.
- [ ] Outlier / mask handling produces per-pixel mask propagated to the product.
- [ ] Per-product uncertainty map exists.
- [ ] Reproducibility artifacts (container / script / checksums / log) present.
- [ ] Validation against known calibration field with a numeric pass criterion.
- [ ] Archive-packaging format matches target archive's spec.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Skipped calibration | "Flat was negligible" | Step list mandatory + QC per step |
| Reference-file drift | Old master calibration applied silently | Version + date logged per cal |
| Mask not propagated | Cosmic-ray hit appears in science product | Mask propagation to header required |
| Missing uncertainty map | Photometric value without σ map | Uncertainty step required |
| Invented pipeline version | Plausible-looking software version | Pin from env file |
| Coadd without outlier rejection | Single CR hit dominates a pixel | Outlier-rejection criterion required |
| Astrometric drift | WCS off by sub-arcsec where it matters | Per-frame residual target |
| Untested run | "Looks fine" without validation | Validation field + pass criterion |
| Non-archive-ready FITS | Required header keywords missing | Archive packaging step enforced |
| Provenance loss | Reduction not re-runnable a year later | Container / script / log retained |
