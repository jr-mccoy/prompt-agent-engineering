---
title: "Telescope Observing Proposal Drafter"
category: science/disciplines/physics-astronomy
description: "Draft an observing proposal that satisfies a TAC's scoring criteria: science case, target selection, exposure and cadence justification, feasibility, and impact"
techniques:
  - ST-01
  - ST-03
  - CM-02
  - DS-02
  - RT-03
difficulty: advanced
tags:
  - astronomy
  - observing-proposal
  - tac
  - exposure-time
  - cadence
  - science-case
updated: "2026-05-19"
related_prompts:
  - domain-science/disciplines/physics-astronomy/astro_data_reduction_pipeline_protocol.md
  - domain-science/disciplines/physics-astronomy/physics_observable_and_measurement_chain_designer.md
---

# Telescope Observing Proposal Drafter

**Objective:** Draft an observing proposal that scores well with a TAC by satisfying the standard scoring axes: a sharp science case with a falsifiable goal, a defensible target sample, a properly motivated exposure / cadence / instrument configuration, an honest feasibility analysis, and a clear publication and data-release plan.

**When to use:** Ahead of a call for proposals (ground-based: Keck / Gemini / VLT / Subaru / LBT / Magellan / IRTF / NOIRLab / SOAR / NOEMA / ALMA / VLA / SKA precursors / IRAM / submm arrays; space-based: HST / JWST / Chandra / XMM-Newton / Roman / Euclid / SPHEREx; surveys: LSST / Rubin DDF / DECam community; time-domain: ZTF, ATLAS, ASAS-SN partner programs). This prompt produces the methodological scaffold of a proposal, not the final formatted text — formatting follows the facility's template.

**Required inputs:**
- **Facility and instrument / mode.** With user-supplied filter / grism / band / receiver / mode.
- **Science question.** One sentence; the answer the data is meant to support.
- **Targets or sample.** A specific list, a survey definition, or a target-of-opportunity trigger.
- **Time-domain need.** Single epoch, monitoring, ToO, time-critical, sub-orbital, sidereal-time constraint.
- **Quantity requested.** Hours / nights / orbits / programs.
- **Sensitivity / SNR goal** for the principal measurement, with the unit (mag, flux, surface brightness, line flux, line-to-continuum, polarization, RV precision m/s, astrometric μas, time-resolution ms).

**Optional inputs:**
- Previous data on the same targets (user-supplied).
- Synergy with other facilities (concurrent or sequenced).
- DDT / ToO triggering rules under consideration.
- Public-data release plans.

**Constraints — Must:**
- Open with a single-sentence science question and the single sentence that states what the *data* would conclude. The TAC must know within 30 seconds why this program exists.
- Justify exposure / cadence by an explicit signal-to-noise calculation that uses the facility's published sensitivity numbers (user-supplied or marked `[user-supplied — pull from ETC]`). Do not invent ETC outputs.
- Treat overhead realistically: instrument set-up, slew, target acquisition, calibration, readouts. State the overhead model and the live-fraction assumption.
- Surface the constraint that determines awarded time: sidereal-time pressure, moon, weather grade, instrument availability, host-galaxy contamination, source crowding.
- For sample / survey proposals: justify sample size statistically (power for the inference the user actually wants to make).
- For target-of-opportunity: state trigger criteria, expected rate, decision tree, override authority.
- Include data-management plan + public release commitment per facility expectation (e.g., HST 12-month proprietary; ALMA standard release; JWST exclusive-access period; ground-based may be no-proprietary). Align to FAIR.

**Constraints — Must Not:**
- Do not invent ETC results, prior magnitudes, redshifts, or coordinates. Cite catalogs only if the user supplies entries.
- Do not promise more science than the data can support (e.g., "characterize atmospheric composition" with one transit, low-SNR).
- Do not propose a sample size without justifying it against the inference target.
- Do not omit the contingency / risk discussion.
- Do not assume zero overhead.

**Instructions:**

1. **Lock the science case in two sentences.** Sentence one: the question. Sentence two: what the data will conclude. The TAC must see a falsifiable, scoped goal. If the question is too broad ("understand X"), narrow it before drafting further.

2. **Specify the inference target.** Detection (yes / no); parameter estimation (precision target); population characterization (sample-level); time-resolved monitoring (cadence sufficient for what timescale); spatial mapping (resolution sufficient for what scale). The exposure derivation flows from this.

3. **Target / sample plan.** For pointed observation: target list with coordinates, magnitudes / brightnesses, exposure per target. For sample: define the selection rule, expected sample-size, and the statistical inference that requires that sample size. For ToO: trigger criteria, expected rate, decision tree.

4. **Exposure / SNR derivation.** Per target or per representative target: principal measurement → SNR requirement → ETC inputs (filter / band / mode, magnitude / surface brightness, seeing / IQ assumption, airmass / zenith distance, lunar phase, sky background, read noise / dark / contamination, instrument efficiency / throughput) → ETC output (exposure time) → applied N-sub × T-int × dithers → total integration. Mark `[ETC output user-supplied]` if not pulled by user.

5. **Cadence / time-domain constraint.** For monitoring: scientific timescale → Nyquist cadence → realistic cadence (weather / scheduling) → number of epochs. For time-critical: define the window and the consequence of missing it.

6. **Overhead model.** Per-visit overhead (instrument set-up, slew, acquisition, calibration, telescope move) and per-frame overhead (readout). Compute total wall-clock time = integrated science time / live fraction.

7. **Feasibility analysis.** Visibility windows by date; airmass / hour-angle constraints; lunar phase tolerance; weather grade required (clear / spectroscopic / partial). For space-based: roll / orbit visibility windows; ground-station coverage if relevant; contamination.

8. **Risk and mitigation.** Failure modes: weather loss, target unavailable, source not detected at expected brightness, contamination from neighbors, calibration outage. State the mitigation: backup targets, queued-mode option, follow-up trigger, accept reduced SNR on graceful degradation.

9. **Synergy and uniqueness.** Why this facility / instrument and not another. What other facilities have done or will do. What is unique to this proposal.

10. **Data plan and impact.** Reduction pipeline (custom or facility), archive deposition timeline, data-release date, planned publications and timeline, broader impact (training, public release, community follow-up).

**Output format (locked):**

```
## Science case (≤2 sentences)
1. Question:
2. Conclusion the data will support:

## Inference target
- Type (detection / estimation / population / time-resolved / spatial):
- Required precision / SNR:
- What would falsify the result:

## Sample / target plan
| Target / sample | Coords / definition | Brightness / mag | Per-target exposure | Notes |

## Exposure / SNR derivation
- Principal measurement:
- ETC inputs:
- ETC exposure:
- Repeats / dithers / sub-integrations:
- Total integrated time:

## Cadence (if time-domain)
- Scientific timescale:
- Cadence:
- Number of epochs:

## Overhead model
- Per-visit overhead:
- Per-frame overhead:
- Live fraction:
- Total wall-clock time requested:

## Feasibility
| Constraint | Requirement | Available windows |

## Risk and mitigation
| Failure mode | Mitigation |

## Synergy / uniqueness
[why this facility, what else exists]

## Data plan and impact
- Reduction:
- Archive / release:
- Planned publications:
- Broader impact:

## Reporting standard alignment
[facility-specific scoring axes; FAIR data; ICMJE for any clinical-adjacent]

## Open questions for the user
[gaps marked [user-supplied] or [ETC required]]
```

**Reporting-standard alignment:** Facility-specific TAC scoring axes (HST / JWST / ALMA / VLT / Keck / Gemini have published criteria) and template structure. FAIR data principles for public release. Per-facility ETC documentation.

**Verification checklist:**
- [ ] Two-sentence science case present and falsifiable.
- [ ] Inference target named and exposure derived from it, not the reverse.
- [ ] ETC inputs and outputs are user-supplied or marked, not invented.
- [ ] Overhead model explicit; total wall-clock = integrated / live fraction.
- [ ] Visibility / airmass / moon-phase / weather requirements stated.
- [ ] Risk-and-mitigation table includes target unavailability and source-not-detected cases.
- [ ] Sample-size justification ties to inference.
- [ ] Data-release commitment matches facility expectation.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Goal overrun | "Characterize atmospheres" with low-SNR single transit | Inference target locked, exposure derived from it |
| Invented ETC | Plausible-looking S/N at apparent magnitude | `[ETC required]` if not user-supplied |
| Overhead optimism | 100% live fraction; calibrations free | Overhead model explicit |
| Target visibility miss | Object below horizon at scheduled phase | Visibility analysis required |
| Sample size from intuition | "We propose 50" with no justification | Inference-target → sample-size logic |
| Weather denial | Plan assumes spectroscopic conditions on bad-weather dates | Weather grade stated |
| ToO trigger underspecified | "If interesting" trigger criterion | Numeric trigger + override authority |
| Publication promise without team | Proposed paper-load incompatible with team capacity | Realistic publication plan |
| Data-release omission | Public-data clock unstated | Release date specified per facility |
