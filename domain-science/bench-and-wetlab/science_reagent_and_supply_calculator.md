---
title: "Reagent and Supply Calculator"
category: science/bench-and-wetlab
description: "Set up and show wet-lab solution math — molarity, mass-from-molarity, C1V1=C2V2 dilutions, serial dilutions, %w/v and ppm, working stocks, and N-sample totals with dead volume — with full dimensional analysis the user can verify."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - molarity
  - dilution
  - serial-dilution
  - dimensional-analysis
  - stock-preparation
  - significant-figures
  - bench-math
  - reagent-prep
updated: "2026-06-26"
related_prompts:
  - domain-science/bench-and-wetlab/science_buffer_recipe_designer.md
  - domain-science/bench-and-wetlab/science_lab_protocol_drafter.md
  - domain-science/bench-and-wetlab/science_lab_protocol_optimizer.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
---

# Reagent and Supply Calculator

**Objective:** Set up — not merely answer — bench solution calculations so the operator can verify the arithmetic. Cover molarity, mass-from-molarity (m = C·V·MW), C1V1=C2V2 dilutions, serial dilutions with fold and carryover, %w/v and ppm, working stocks from concentrated stock, and totals for N samples plus dead volume. Every result shows the formula, the substituted numbers, and unit cancellation, with molecular weight, purity, and density required from the user rather than asserted.

**When to use:** You need to prepare a solution at a target concentration/volume and want a checkable worked calculation and a prep sheet, not a black-box number.

**Required inputs:**
- **Discipline.** <e.g., biochemistry, molecular biology, analytical chemistry>
- **Study type.** <experimental / method-development / QC>
- **Calculation type.** <molarity / dilution / serial dilution / %w-v / ppm / working stock / N-sample total>
- **Target concentration and volume.** <e.g., 50 mM in 100 mL>
- **Compound molecular weight (MW), purity, and (for liquids) density.** `[user-supplied]` — do not assert from memory.

**Optional inputs:**
- Available stock concentration (for dilutions/working stocks)
- Hydration state / salt form of the compound (affects effective MW) `[user-supplied]`
- Number of samples, per-sample volume, and desired dead/overage volume
- Serial-dilution fold factor and number of steps
- Required precision / significant figures

**Constraints — Must:**
- Show, for every calculation, the **named formula → substituted values → unit cancellation → result**, so the math is independently verifiable.
- Carry **units through every step** and confirm they cancel to the target unit (dimensional analysis, DS-02).
- Use the correct relations: `m = C × V × MW` (adjust by purity and salt form); `C1V1 = C2V2`; serial-dilution `fold = C_n / C_(n+1)`; `%w/v = g/100 mL`; `ppm = mg/L` (aqueous, approx) — and state the assumption behind any approximation.
- Account for **dead volume / overage** when computing totals for N samples and state the assumed overage.
- Round to **sensible significant figures** consistent with the least-precise input, and state the rounding choice.
- Require **MW, purity, density, and salt/hydration form as `[user-supplied]`** and incorporate purity/salt corrections explicitly.

**Constraints — Must Not:**
- Do not invent vendor names, catalog/lot numbers, reagent specifications, or hazard/SDS data. If needed and not supplied, mark `[user-supplied]` and ask; route all safety/hazard facts to the official SDS and institutional EHS.
- Do not assert a compound's MW, density, purity, or hazard from memory; require the value or the SDS/CoA.
- Do not silently approximate (e.g., ppm ≈ mg/L) without stating the assumption.
- Do not over-report precision beyond the input significant figures.
- Do not use promotional language ("novel," "groundbreaking," "first-ever," "gold standard") in the output.

**Instructions:**

1. **Classify the calculation and lock targets.** Identify calculation type, target concentration, target volume, and the readout precision. Echo all inputs.
2. **Collect the physical constants.** MW, purity (decimal fraction), density (for liquids), and salt/hydration form — each `[user-supplied]`. If missing, request and pause.
3. **State the governing formula.** Write the named equation (e.g., m = C·V·MW) and any correction term (÷ purity; effective MW for hydrate/salt form).
4. **Substitute with units.** Insert numbers with units; convert to consistent base units (mol, L, g) before computing.
5. **Cancel units and compute.** Show the cancellation explicitly and produce the numeric result.
6. **Apply corrections.** Divide by purity; adjust for salt/hydration MW; for liquids convert mass→volume via density.
7. **Scale for N samples + dead volume.** Compute per-sample need, multiply by N, add the stated overage, and report total reagent and diluent.
8. **For serial dilutions, tabulate each step.** Show transfer and diluent volumes, resulting concentration, fold, and note carryover/cumulative-error caveats.
9. **Round and self-check.** Round to justified sig figs; verify units of the final answer match the target; flag any value that depended on an unverified constant.

**Output format (locked):**

```
## Calculation: <type>
Discipline: <...> | Study type: <...>
Targets: C=<...>, V=<...> | Constants: MW=[user-supplied], purity=[user-supplied], density=[user-supplied]

## Worked Calculation (verifiable)
Formula: <named equation>
Substitution (with units): <... = ...>
Unit cancellation: <show units cancel to target>
Correction (purity / salt form): <...>
Result (sig figs justified): <value ± precision>

## Serial Dilution (if applicable)
| Step | Source conc | Transfer vol | Diluent vol | Final conc | Fold |
|---|---|---|---|---|---|

## N-Sample Totals
Per sample: <...> | N: <...> | Dead/overage: <...> | Total reagent: <...> | Total diluent: <...>

## Prep Sheet
1. Weigh/measure <amount> of <compound> [confirm identity/lot/SDS: user-supplied]
2. Dissolve/dilute in <diluent> to <final volume>
3. <pH/mix/store notes; hazards → SDS/EHS>

## Assumptions & Caveats
- <approximations stated; unverified constants flagged>
```

**Reporting-standard alignment:** Dimensional-analysis and significant-figure conventions; good-documentation / ELN practice for recording lot, CoA, and prep date; protocols.io-compatible prep sheets; reproducibility self-audit (`science_reproducibility_self_audit.md`).

**Verification checklist (before delivering):**
- [ ] Discipline and study type captured first.
- [ ] Every calculation shows formula → substitution → unit cancellation → result.
- [ ] Units carried through and confirmed to cancel to the target unit.
- [ ] MW, purity, density, and salt/hydration form taken as `[user-supplied]`, not asserted.
- [ ] Purity and salt-form corrections applied explicitly.
- [ ] N-sample total includes a stated dead-volume/overage.
- [ ] Significant figures justified against the least-precise input.
- [ ] Approximations (e.g., ppm ≈ mg/L) flagged; reagent identity/SDS confirmation required.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Asserted MW/density | A confident value pulled from memory | Force `[user-supplied]`; pause if missing |
| Purity ignored | Mass computed at 100% purity for a 95% reagent | Mandatory ÷ purity correction step |
| Salt-form error | Using anhydrous MW for a hydrate (or free acid vs salt) | Require salt/hydration form; use effective MW |
| Unit mismatch | mg vs g, mL vs L slip that yields a 1000× error | Explicit unit-cancellation step gates the result |
| False precision | Reporting 4 sig figs from 2-sig-fig inputs | Round to least-precise input; state rounding |
| Serial-dilution drift | Ignoring carryover/cumulative error across steps | Tabulate per step; add carryover caveat |
