---
title: "ML Carbon Accounting Deep Dive"
category: AI-ML/mlops-infrastructure
description: "Operational carbon accounting for ML training and serving — measured energy (kWh) × PUE × region grid carbon intensity, embodied vs operational emissions, Scope 2 (location- vs market-based) and Scope 3 framing — reporting only from measured inputs and stated assumptions, never invented energy or emissions figures."
techniques:
  - ST-02
  - DS-01
  - DS-02
  - RT-05
  - CM-02
difficulty: advanced
tags:
  - carbon-accounting
  - energy
  - scope-2
  - scope-3
  - sustainability
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/responsible-ai-governance/rai_sustainability_carbon_assessment.md
  - domain-AI-ML/mlops-infrastructure/mlops_cost_attribution_showback.md
  - domain-AI-ML/mlops-infrastructure/mlops_infra_cost_optimization.md
---

# ML Carbon Accounting Deep Dive

**Objective:** Produce an operational carbon account for ML training and serving that derives emissions from measured energy (kWh) × PUE × region/time grid carbon intensity, distinguishes operational from embodied emissions, and frames Scope 2 (location- vs market-based) and Scope 3 — using only measured inputs and explicitly stated assumptions.

**When to Use:**
- You need a defensible, audit-grade carbon figure for ML compute, not a rough order-of-magnitude estimate.
- A sustainability report, internal target, or disclosure requires Scope 2/3 framing for ML workloads.
- You have (or can obtain) measured energy and need to convert it to emissions correctly.

**When NOT to Use:**
- You need a lightweight, early-stage carbon sniff-test or governance-level assessment — use the lighter `rai_sustainability_carbon_assessment.md`.
- You need cost (not carbon) attribution — use `mlops_cost_attribution_showback.md`.

## Inputs / Context

- **Measured energy** — kWh consumed by training runs and serving (from power telemetry, GPU energy counters, or provider energy data).
- **PUE** — data-center power-usage effectiveness (provider-published or measured).
- **Grid carbon intensity** — gCO₂e/kWh by region and, ideally, by time-of-day for the workload's location.
- **Hardware lifecycle** — for embodied emissions: device manufacturing footprint and useful-life amortization basis.
- **Procurement instruments** — RECs/PPAs/contracts for market-based Scope 2.
- **Reporting scope** — whether the account covers Scope 2 only, or extends to Scope 3 (embodied, cloud value chain).

## Constraints

**Must:**
- Compute operational emissions as: energy (kWh) × PUE × grid carbon intensity (gCO₂e/kWh), with each factor sourced.
- Distinguish operational emissions (using the hardware) from embodied emissions (making the hardware), and amortize embodied over useful life.
- Frame Scope 2 with both location-based (grid average) and market-based (procurement-adjusted) methods.
- State Scope 3 boundaries (embodied hardware, upstream cloud) explicitly, or state that they're out of scope.
- Record every assumption (PUE source, intensity dataset, amortization period) inline so the account is reproducible.

**Must Not:**
- Invent energy figures, PUE, grid intensity, embodied footprints, or emissions totals — every number must come from a measured input or a *named, stated* assumption; mark gaps `UNKNOWN — measure or cite source`.
- Substitute a "typical model trains at X kWh" estimate for measured energy and present it as the result.

**Instructions:**

1. **Gather measured energy.** Pull kWh for training and serving from telemetry/provider data; if unavailable, mark UNKNOWN — do not estimate as fact.
2. **Source PUE and grid intensity.** Record provider PUE and a named grid-intensity dataset for the region (and time window if available).
3. **Compute operational emissions.** energy × PUE × intensity, per workload; show the arithmetic and units.
4. **Account for embodied emissions.** Use device manufacturing footprint amortized over useful life and the fraction of life used by the workload.
5. **Frame Scope 2 both ways.** Location-based (grid average) and market-based (RECs/PPAs applied); report both.
6. **Set Scope 3 boundary.** State what's included (embodied, upstream) or explicitly excluded, with rationale.
7. **Report with assumptions.** Present totals with every factor's source and a sensitivity note on the most uncertain input.

**Output Format:**

A markdown carbon account: Measured Energy Inputs · Conversion Factors (PUE, intensity, sources) · Operational Emissions (with math) · Embodied Emissions (amortization basis) · Scope 2 Location vs Market-Based · Scope 3 Boundary · Assumptions & Sensitivity. Unknowns marked.

## Verification

- [ ] Operational emissions = energy × PUE × intensity, with each factor sourced and units shown.
- [ ] Operational and embodied emissions are distinguished; embodied is amortized over useful life.
- [ ] Scope 2 is reported both location-based and market-based.
- [ ] Scope 3 boundary is stated explicitly (included or excluded with rationale).
- [ ] Every assumption is recorded inline so the figure is reproducible.
- [ ] No energy/PUE/intensity/emissions number was invented; gaps are UNKNOWN.

## False-Positive Prevention

❌ **DON'T:**
- Multiply GPU TDP × runtime and call it "measured energy" — nameplate TDP is a power ceiling, not actual draw, and it ignores PUE; a TDP-based figure is an estimate dressed as a measurement.
- Use a single national-average grid intensity for a workload that ran in a specific low-carbon region at night — using the wrong location/time intensity can swing the result several-fold in either direction.
- Report only location-based Scope 2 when the org has PPAs/RECs (or only market-based when it doesn't) — picking the method that flatters the number is greenwashing; both must be shown.
- Omit embodied emissions and present operational-only as "the model's carbon footprint" — for short-lived or efficient workloads, manufacturing emissions can be a large, silently dropped share.

✅ **DO:**
- Use metered/provider-reported kWh; if only TDP-based estimates exist, label them as estimates and mark true energy UNKNOWN.
- Match grid intensity to the workload's actual region and, where possible, time-of-day.
- Report Scope 2 with both location-based and market-based methods side by side.
- Include embodied emissions amortized over hardware useful life, and flag the most sensitive assumption.

## Example Output

```markdown
## Carbon Account — fraud-scoring training run #884

### Measured Energy Inputs
- Training energy (GPU power counters): 41.2 kWh (measured). Serving: UNKNOWN — instrument endpoint.

### Conversion Factors
- PUE: 1.12 (provider-published, us-west region). Source cited.
- Grid intensity: 68 gCO₂e/kWh (region/time dataset, us-west, off-peak). Source cited.

### Operational Emissions (math)
- 41.2 kWh × 1.12 (PUE) × 68 gCO₂e/kWh = 3,137 gCO₂e ≈ 3.14 kgCO₂e (location-based).

### Embodied Emissions
- A100 manufacturing footprint amortized over 4-yr useful life × run's share of life = X gCO₂e. Basis: UNKNOWN — cite vendor LCA.

### Scope 2: Location vs Market-Based
- Location-based: 3.14 kgCO₂e. Market-based: 0 kgCO₂e if covered by matched PPA (confirm matching).

### Scope 3 Boundary
- Included: embodied hardware (above). Excluded: upstream cloud value chain — out of scope, stated.

### Assumptions & Sensitivity
- Most sensitive to grid intensity (region/time choice). PUE assumed provider-published, not measured on-site.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** Sequences energy → factors → operational → embodied → Scope 2/3 → report.
- **DS-01 (Framework Application):** Applies the GHG-Protocol Scope 2 (location/market) and Scope 3 framing.
- **DS-02 (Metric Specification):** Pins the kWh × PUE × intensity formula with explicit units.
- **RT-05 (Evidence-Based Reasoning):** Requires every factor to trace to a measured input or a named source.
- **CM-02 (Constraint Specification):** Encodes the measured-inputs-only, no-fabrication clause.

**Related Prompts:**
- `rai_sustainability_carbon_assessment.md` — the lighter, governance-level carbon assessment this deep-dives.
- `mlops_cost_attribution_showback.md` — pairs energy/carbon with cost attribution by model.
- `mlops_infra_cost_optimization.md` — efficiency levers (region, batching, quantization) that also cut carbon.
