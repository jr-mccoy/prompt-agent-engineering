---
title: "Buffer Recipe Designer"
category: science/bench-and-wetlab
description: "Select and formulate a buffer by target pH vs pKa (Henderson-Hasselbalch), buffering capacity, ionic strength, temperature dependence, and downstream-assay compatibility — output a recipe table, compatibility check, pH-adjustment, and storage note."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - DS-02
  - QA-02
difficulty: advanced
tags:
  - buffer-design
  - henderson-hasselbalch
  - goods-buffers
  - ionic-strength
  - assay-compatibility
  - ph-adjustment
  - bench-practice
  - reagent-prep
updated: "2026-06-26"
related_prompts:
  - domain-science/bench-and-wetlab/science_reagent_and_supply_calculator.md
  - domain-science/bench-and-wetlab/science_lab_protocol_drafter.md
  - domain-science/bench-and-wetlab/science_lab_protocol_optimizer.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
---

# Buffer Recipe Designer

**Objective:** Help select a buffer system for a target pH and formulate a recipe. Match buffer pKa to target pH (Henderson-Hasselbalch; the ±1 pH-unit-of-pKa rule), set buffering capacity/concentration, consider ionic strength and the temperature dependence of pKa, and check downstream-assay compatibility (chelators vs metalloenzymes, phosphate vs divalent cations, reducing agents, detergents, salt sensitivity). Output a recipe table, a compatibility check, a pH-adjustment plan, and a storage note. Reagent identities and physical constants are user-confirmed, not asserted.

**When to use:** You need a buffer at a defined pH that must remain compatible with a specific downstream assay or enzyme, and you want the selection rationale plus a checkable recipe — not just a generic formula.

**Required inputs:**
- **Discipline.** <e.g., biochemistry, molecular biology, protein purification, cell biology>
- **Study type.** <experimental / method-development / QC>
- **Target pH and working temperature.** <e.g., pH 7.4 at 25 °C, used at 4 °C>
- **Downstream assay / enzyme constraints.** <e.g., requires Mg²⁺/Ca²⁺, metal-dependent enzyme, redox-sensitive, detergent-sensitive>
- **Buffer concentration / capacity needed and total volume.** <e.g., 50 mM, 500 mL>

**Optional inputs:**
- Candidate buffer species under consideration (e.g., Tris, HEPES, phosphate, MOPS)
- Required ionic strength / salt (NaCl/KCl) range
- Additives (EDTA, DTT/TCEP, glycerol, detergents) and their purpose
- pKa / MW / stock values `[user-supplied]` from CoA/SDS
- Storage duration and conditions

**Constraints — Must:**
- **Match buffer to pH using the Henderson-Hasselbalch relation** `pH = pKa + log([A⁻]/[HA])` and the practical rule that the buffer pKa should be within **±1 pH unit** of the target pH; show the ratio implied.
- Address **temperature dependence of pKa** (e.g., amine buffers like Tris shift markedly with temperature) and state that pH must be set at the working temperature.
- Consider **ionic strength** and its effect on activity/pKa, and on salt-sensitive downstream steps.
- Run an explicit **downstream-assay compatibility check**: chelators (EDTA/EGTA) with metal-dependent enzymes, phosphate with divalent cations (Ca²⁺/Mg²⁺ precipitation), reducing agents (DTT/TCEP) where required, and detergent/salt compatibility.
- Prefer **Good's buffers** where a low-metal-binding, physiologically inert option is appropriate, and state the selection rationale.
- Output a **recipe table** with component → final concentration → amount for the target volume, deferring mass/volume math to `science_reagent_and_supply_calculator.md`, with `[user-supplied]` MW/stock slots.
- Provide a **pH-adjustment plan** (titrant, order of addition, adjust-then-QS-to-volume) and a **storage note**.

**Constraints — Must Not:**
- Do not invent vendor names, catalog/lot numbers, reagent specifications, or hazard/SDS data. If needed and not supplied, mark `[user-supplied]` and ask; route all safety/hazard facts to the official SDS and institutional EHS.
- Do not assert exact pKa, ΔpKa/°C, MW, or hazard values from memory; require `[user-supplied]` confirmation from CoA/reference and flag temperature/ionic-strength corrections as needing verification.
- Do not recommend an incompatible additive (e.g., EDTA into a Mg²⁺-dependent reaction) without flagging the conflict.
- Do not use promotional language ("novel," "groundbreaking," "first-ever," "gold standard") in the output.

**Instructions:**

1. **Lock target pH, temperature, capacity, and the downstream constraint.** Echo inputs; identify the single most binding compatibility requirement (often the enzyme's metal or redox need).
2. **Shortlist buffer species by pKa.** Propose candidates whose pKa is within ±1 pH unit of the target (Good's buffers preferred where appropriate); require pKa values as `[user-supplied]`.
3. **Apply Henderson-Hasselbalch.** Show the implied `[A⁻]/[HA]` ratio at the target pH for the chosen buffer so the formulation is justified.
4. **Adjust for temperature.** Note the direction/magnitude of pKa shift with temperature and instruct setting pH at the working temperature; flag any `[user-supplied]` ΔpKa/°C used.
5. **Set concentration and ionic strength.** Choose buffer concentration for needed capacity; specify salt for ionic strength and check it against salt-sensitive downstream steps.
6. **Run the compatibility check (QA-02).** Adversarially test each component against the downstream assay: chelator↔metalloenzyme, phosphate↔divalent cation, reducing-agent need, detergent/salt tolerance. Flag and resolve conflicts.
7. **Build the recipe table.** Component, final concentration, and amount for the target volume (math deferred to the calculator), with `[user-supplied]` MW/stock.
8. **Write pH-adjustment and storage notes.** Titrant and order of addition, "adjust pH then bring to final volume," filtration, storage temperature/duration, and any precipitation/oxidation caveat (e.g., add DTT fresh).
9. **Self-check.** Confirm pKa-within-±1, temperature note, ionic-strength note, and that no flagged incompatibility remains unresolved.

**Output format (locked):**

```
## Buffer Design: target pH <...> at <temp>
Discipline: <...> | Study type: <...> | Capacity: <...> mM | Volume: <...>
Most binding compatibility constraint: <...>

## Buffer Selection Rationale
- Candidate(s) within ±1 pH unit of pKa: <...> (pKa = [user-supplied])
- Chosen: <...> | Henderson-Hasselbalch ratio [A⁻]/[HA] at target pH: <...>
- Temperature dependence: <direction/magnitude; set pH at working temp> [ΔpKa/°C user-supplied]
- Ionic strength: <salt, mM; effect on downstream>

## Recipe (for <total volume>)
| Component | Final conc. | Amount (math → calculator) | MW/Stock | Notes |
|---|---|---|---|---|
| <buffer acid/base> | <...> | <see reagent calculator> | [user-supplied] | |
| <salt> | <...> | | [user-supplied] | ionic strength |
| <additive> | <...> | | [user-supplied] | compatibility note |

## Compatibility Check
- Chelator ↔ metalloenzyme: <pass/conflict + resolution>
- Phosphate ↔ Ca²⁺/Mg²⁺: <pass/conflict>
- Reducing agent / detergent / salt: <...>

## pH Adjustment & Storage
- Titrant & order: <...>; adjust pH, then QS to volume; filter <...>
- Store: <temp/duration>; add labile components (e.g., DTT) fresh
- Hazards: consult SDS for each component; EHS/PPE/waste [user-supplied]
```

**Reporting-standard alignment:** Henderson-Hasselbalch / pKa-based selection and Good's-buffer conventions; dimensional-analysis and significant-figure discipline (via the reagent calculator); good-documentation / ELN practice; protocols.io-compatible recipe formatting; reproducibility self-audit (`science_reproducibility_self_audit.md`).

**Verification checklist (before delivering):**
- [ ] Discipline and study type captured first.
- [ ] Chosen buffer pKa is within ±1 pH unit of the target; H-H ratio shown.
- [ ] Temperature dependence of pKa noted; pH set at working temperature.
- [ ] Ionic strength specified and checked against salt-sensitive steps.
- [ ] Downstream compatibility check covers chelators, phosphate/divalent cations, reducing agents, detergents.
- [ ] Recipe table uses `[user-supplied]` MW/stock; mass/volume math deferred to the calculator.
- [ ] pH-adjustment order ("adjust then QS") and storage/labile-component note included.
- [ ] No asserted pKa/MW/hazard from memory; SDS/CoA confirmation required.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| pKa mismatch | A buffer chosen >1 pH unit from target with weak capacity | Enforce ±1 pH-unit-of-pKa rule; show H-H ratio |
| Temperature blind spot | pH set at RT for a Tris buffer used cold | Require pH set at working temp; flag ΔpKa/°C |
| Chelator conflict | EDTA in a Mg²⁺-dependent reaction buffer | Compatibility check flags chelator↔metalloenzyme |
| Phosphate precipitation | Phosphate buffer plus Ca²⁺/Mg²⁺ | Flag divalent-cation precipitation; suggest alternative |
| Asserted constants | Confident pKa/MW from memory | Force `[user-supplied]` from CoA/reference |
| Labile additive decay | DTT/TCEP pre-mixed and stored, then assumed active | Storage note requires adding reducing agents fresh |
