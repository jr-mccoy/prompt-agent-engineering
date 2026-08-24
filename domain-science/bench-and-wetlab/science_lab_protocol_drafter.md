---
title: "Lab Protocol Drafter"
category: science/bench-and-wetlab
description: "Draft a STAR-Methods-style, step-by-step wet-lab protocol with a materials table, timed/temperature-flagged procedure, first-class controls, hazard call-outs routed to SDS/EHS, and an expected-outcome readout."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - protocol-drafting
  - star-methods
  - wet-lab
  - reproducibility
  - controls
  - protocols-io
  - bench-practice
  - documentation
updated: "2026-06-26"
related_prompts:
  - domain-science/bench-and-wetlab/science_lab_protocol_optimizer.md
  - domain-science/bench-and-wetlab/science_reagent_and_supply_calculator.md
  - domain-science/bench-and-wetlab/science_buffer_recipe_designer.md
  - domain-science/methods-foundations/science_negative_and_positive_control_designer.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
---

# Lab Protocol Drafter

**Objective:** Convert a stated experimental goal into a reproducible, publication-grade bench protocol structured in the STAR Methods idiom: an itemized materials table, a numbered procedure with critical steps, timing, and temperatures flagged, controls treated as first-class procedure components, and hazard handling routed to the official SDS and institutional EHS. The draft is a documentation scaffold, not a substitute for institutional safety review or reagent verification.

**When to use:** You have a defined assay/technique and goal and need a versioned, shareable protocol that another competent operator could execute without consulting you. Use before running the experiment, and before depositing to protocols.io or attaching to a methods section.

**Required inputs:**
- **Discipline.** <e.g., molecular biology, cell biology, biochemistry, microbiology, analytical chemistry>
- **Study type.** <experimental / observational / method-development / QC validation>
- **Assay or technique.** <e.g., Western blot, qPCR, transfection, ELISA, IHC, restriction digest>
- **Biological/chemical system.** <cell line, organism, sample matrix, target analyte>
- **Goal & readout.** <what the experiment must measure and how success is judged>

**Optional inputs:**
- Available reagents/equipment with `[user-supplied]` catalog/lot identifiers
- Throughput / replicate structure (N samples, technical vs biological replicates)
- Prior protocol or kit insert being adapted
- Animal involvement (triggers ARRIVE 2.0 reporting fields)
- Time/temperature constraints from instruments or sample stability

**Constraints — Must:**
- Structure the procedure in STAR-Methods style: a **Key Resources / Materials table** followed by a **Step-by-Step Method** with numbered steps.
- Flag every **critical step**, and annotate timing and temperature on every step where they affect the outcome.
- Treat **controls as first-class steps**: specify positive, negative, and vehicle/no-template controls inline, cross-referencing `science_negative_and_positive_control_designer.md` for design rationale.
- Mark each material with a `[user-supplied]` slot for catalog number, lot, vendor, and concentration where not provided.
- Route every hazard to its hazard class → SDS → institutional EHS/PPE/waste rule; state PPE and waste stream per step where a hazard is present.
- Include a **version number, date, and a "deposit on protocols.io" reproducibility note** as the default Open Science branch; name ELN/version-control capture.
- Provide an **expected outcome** and an explicit "did it work?" readout, plus a pointer to the optimizer prompt for failures.

**Constraints — Must Not:**
- Do not invent vendor names, catalog/lot numbers, reagent specifications, or hazard/SDS data. If needed and not supplied, mark `[user-supplied]` and ask; route all safety/hazard facts to the official SDS and institutional EHS.
- Do not provide bespoke hazardous-synthesis, energetic-material, select-agent, or weaponization procedures; keep hazard handling at the "identify class → consult SDS → follow EHS" level.
- Do not assert chemical or biological hazard facts (flammability, toxicity, incompatibilities) from memory; require SDS confirmation.
- Do not use promotional language ("novel," "groundbreaking," "first-ever," "gold standard") in the drafted protocol text.
- Do not omit controls to shorten the protocol.

**Instructions:**

1. **Restate the objective and lock the readout.** Echo the goal, assay, system, and the exact quantitative or qualitative readout that defines success. If the readout is undefined, stop and request it.
2. **Build the materials table.** List reagents, consumables, and equipment in a table with `[user-supplied]` slots for vendor/catalog/lot/concentration. Separate "biological/chemical reagents," "buffers/solutions" (point to `science_buffer_recipe_designer.md`), and "equipment/software."
3. **Specify preparation steps.** Reagent reconstitution, buffer prep, sample prep, and instrument warm-up — each with timing and temperature. Defer concentration math to `science_reagent_and_supply_calculator.md` and reference it rather than asserting volumes.
4. **Write the numbered procedure.** One action per step; flag CRITICAL steps; annotate time and temperature. Keep step granularity at the level a trained operator can follow unambiguously.
5. **Embed controls inline.** Insert positive, negative, and vehicle/no-template controls as numbered steps at the point they are run, not as an afterthought. State what each control rules in or out.
6. **Insert hazard call-outs.** At each step involving a hazardous material or process, name the hazard class, instruct "consult SDS for [reagent]," and state required PPE and waste stream — all `[user-supplied]`-verified, EHS-governed.
7. **Define expected outcome and readout.** State the expected result, the pass/fail criterion, and a quick "did it work?" diagnostic. Add `NE-10`-style probability-weighted notes only if outcome variability is material.
8. **Add reproducibility metadata.** Version, date, author `[user-supplied]`, deposit-on-protocols.io note, ELN entry pointer, and ARRIVE 2.0 fields if animals are involved.
9. **Self-check and point to troubleshooting.** Run the verification checklist; add a one-line pointer to `science_lab_protocol_optimizer.md` for failure modes.

**Output format (locked):**

```
## Protocol: <name> — v<version> (<date>)
Discipline: <...> | Study type: <...> | Readout: <...>

## Key Resources / Materials
| Item | Type | Vendor/Catalog | Lot | Final conc. | Notes |
|---|---|---|---|---|---|
| <reagent> | reagent | [user-supplied] | [user-supplied] | [user-supplied] | hazard class: consult SDS |

## Preparation
1. <prep step> — [time] [temp] [CRITICAL?]

## Procedure
1. <action> — [time] [temp] [CRITICAL?]
   - Hazard: <class> → consult SDS for <reagent>; PPE: <...>; waste: <stream> [EHS-governed]

## Controls (run alongside samples)
- Positive: <...> (rules in: <...>)
- Negative: <...> (rules out: <...>)
- Vehicle / No-template: <...>

## Expected Outcome & "Did It Work?" Readout
- Expected: <...>
- Pass/fail criterion: <...>
- Quick diagnostic: <...>

## Reproducibility & Deposition
- Version/date/author: <...> | protocols.io: <deposit> | ELN entry: <...>
- ARRIVE 2.0 fields (if animal): <...>

## Troubleshooting
- On failure, see science_lab_protocol_optimizer.md
```

**Reporting-standard alignment:** STAR Methods (Cell Press) structured-protocol format; protocols.io deposition and versioning conventions; ARRIVE 2.0 where vertebrate animals are involved; good-documentation / ELN practice.

**Verification checklist (before delivering):**
- [ ] Discipline and study type captured as the first inputs.
- [ ] Materials table uses `[user-supplied]` for every vendor/catalog/lot/concentration not provided.
- [ ] Every step with outcome-relevant timing/temperature is annotated; critical steps flagged.
- [ ] Positive, negative, and vehicle/no-template controls appear inline.
- [ ] Each hazard is handled as class → SDS → EHS/PPE/waste, with no asserted hazard facts.
- [ ] Expected outcome and a pass/fail "did it work?" readout are present.
- [ ] Version, date, and protocols.io deposition note included (Open Science default).
- [ ] No promotional language in the drafted text; pointer to optimizer included.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Fabricated reagent specs | A catalog number or concentration that looks authoritative but was invented | Force `[user-supplied]` slots; never fill vendor/lot/conc from memory |
| Asserted hazard facts | "Reagent X is non-toxic / compatible" stated confidently | Replace with "consult SDS for X"; route to EHS |
| Controls dropped | A clean linear procedure that omits negative/vehicle controls | Checklist gate requires all three control classes inline |
| Unverifiable timing | Times/temps copied from a kit insert without flagging adaptation | Mark adapted values `[user-supplied]` / verify against the source instrument |
| Over-claiming | "Optimized, gold-standard" phrasing implying validated performance | Ban promotional terms; state only what the protocol does |
