---
title: "Reagent Validation Workflow"
category: science/bench-and-wetlab
description: "Build a per-reagent-class validation plan — antibodies (multi-pillar), primers/oligos (specificity & controls), and cell lines (STR + mycoplasma) — with claim, validation test, pass criterion, and evidence to record, before experimental use."
techniques:
  - ST-01
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - reagent-validation
  - antibody-validation
  - primer-specificity
  - cell-line-authentication
  - str-profiling
  - reproducibility
  - controls
  - star-methods
updated: "2026-06-26"
related_prompts:
  - domain-science/methods-foundations/science_negative_and_positive_control_designer.md
  - domain-science/bench-and-wetlab/science_lab_notebook_entry_writer.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
---

# Reagent Validation Workflow

**Objective:** Produce a validation plan tailored to the reagent class in use — **antibodies**, **primers/oligonucleotides**, or **cell lines** — that turns each reagent's claimed identity/specificity into concrete validation tests with explicit pass criteria and recorded evidence, so that validation precedes experimental use. The workflow operationalizes the antibody-validation "pillars" concept, standard primer-specificity controls, and cell-line authentication, framing all of it as reproducibility-critical.

**When to use:** Before deploying a new (or new-lot) antibody, primer set, or cell line in an experiment whose conclusions depend on that reagent behaving as claimed — and during periodic re-validation.

**Required inputs:**
- **Discipline.** [user-supplied]
- **Study type.** [user-supplied] (and the application: WB / IHC / IF / flow / qPCR / sequencing / culture)
- **Reagent class.** Antibody, primer/oligo, or cell line (one or more).
- **The claim to validate.** Target/epitope, amplicon/target sequence, or cell-line identity — [user-supplied].
- **Application context.** The specific assay the reagent must perform in (validation is application-specific).

**Optional inputs:**
- Catalog/lot/clone identifiers — [user-supplied]; recorded, never invented.
- Available controls (KO/KD lines, recombinant standards, reference STR profile, NTC capacity).
- Prior validation evidence or vendor validation data to corroborate (not to substitute for in-house checks).

**Constraints — Must:**
- For **antibodies**, design across the validation pillars: genetic strategy (KO/KD control), orthogonal/independent-method concordance, independent-antibody concordance, recombinant-expression, and IP-MS — and require **application-specific** validation for each intended application (WB ≠ IHC ≠ IF ≠ flow).
- For **primers/oligos**, require in-silico specificity check, single-amplicon confirmation (gel/melt curve), amplification efficiency, and **no-template** and **RT-minus** controls.
- For **cell lines**, require **STR authentication** against a reference profile and **mycoplasma** testing.
- State each item as **claim → validation test → pass criterion → evidence to record** (DS-02 quantitative where applicable, e.g., efficiency 90–110%, single melt peak).
- Treat validation as **reproducibility-critical** and **a prerequisite to experimental use**, not a post-hoc justification.
- Align reagent reporting with **STAR Methods** key-resources structure.

**Constraints — Must Not:**
- Do not invent vendor names, catalog/lot numbers, reagent specs, or results/observations. If needed and not supplied, mark `[user-supplied]` and ask; the prompt records what the user supplies, it never fabricates data.
- Do not accept vendor validation as a substitute for in-house, application-specific validation.
- Do not pass a reagent on a single pillar/control when the claim requires multiple lines of evidence.
- Do not use promotional language ("novel", "groundbreaking", "first-ever", "gold standard") in drafted text.

**Instructions:**

1. **Confirm reagent class, claim, and application.** Restate inputs; mark unknown identifiers `[user-supplied]`. Note that validation is application-specific.
2. **Select the validation strategy for the class.** Antibody → pillars; primer → specificity + controls; cell line → STR + mycoplasma.
3. **Antibody plan.** Lay out the pillars relevant to the application, the control needed for each (e.g., KO/KD line for genetic strategy), the pass criterion, and the evidence to capture per application (WB/IHC/IF/flow).
4. **Primer/oligo plan.** Specify the in-silico check (target + off-target), single-amplicon verification (single band / single melt peak), efficiency target (state the acceptable range, DS-02), and the NTC and RT-minus controls with their pass criteria.
5. **Cell-line plan.** Specify STR profiling against the reference and the match threshold concept, plus the mycoplasma test and its pass criterion; note re-authentication cadence.
6. **Set pass/fail gating.** State that the reagent may not be used experimentally until the required evidence is recorded and criteria are met; define what a partial pass means.
7. **Emit the per-reagent validation table.** One row per claim/test, with pass criterion and evidence pointer.
8. **Record & deposit.** Log evidence in the ELN with stable IDs; default to depositing the validation record and protocol (Open Science) where permissible, and to a STAR Methods-style key-resources entry.

**Output format (locked):**

```
## Scope
- Reagent class / application:
- Claim to validate:
- Identifiers ([user-supplied]):

## Validation Plan — Per Reagent
| Reagent / lot | Claim | Validation test | Pass criterion | Controls | Evidence to record |
|---|---|---|---|---|---|

## Antibody Pillars (if applicable)
| Pillar | Test | Control | Application(s) | Pass criterion |
|---|---|---|---|---|
| Genetic (KO/KD) | | | | |
| Orthogonal method | | | | |
| Independent antibody | | | | |
| Recombinant expression | | | | |
| IP-MS | | | | |

## Primer/Oligo Controls (if applicable)
| Check | Method | Pass criterion |
|---|---|---|
| In-silico specificity | | |
| Single amplicon | | single band / single melt peak |
| Efficiency | | [state acceptable range] |
| No-template control | | |
| RT-minus control | | |

## Cell-Line Authentication (if applicable)
| Check | Method | Pass criterion | Re-auth cadence |
|---|---|---|---|
| STR profile | | match to reference | |
| Mycoplasma | | negative | |

## Use Gate
- May the reagent be used? (pass / partial / hold) + rationale:

## Record / Deposit
- ELN evidence link / STAR Methods key-resources entry / Open Science disposition:
```

**Reporting-standard alignment:** STAR Methods (key resources table); antibody-validation pillars concept (reproducibility literature); MIQE-style qPCR controls (concept) for primers; cell-line authentication (STR) and mycoplasma best practice; ALCOA+ for the validation record.

**Verification checklist (before delivering):**
- [ ] Validation strategy matches the reagent class and is application-specific.
- [ ] Antibody plan covers the relevant pillars, each with its control and per-application pass criterion.
- [ ] Primer plan includes in-silico, single-amplicon, efficiency (quantified range), NTC, and RT-minus.
- [ ] Cell-line plan includes STR authentication and mycoplasma.
- [ ] Each row is claim → test → pass criterion → evidence; criteria are concrete.
- [ ] A use-gate blocks experimental use until evidence is recorded.
- [ ] No invented catalog/lot numbers, vendor names, or validation results; banned promotional terms absent.
- [ ] Vendor data is corroborated, not substituted for in-house validation.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Vendor-data reliance | "Validated by manufacturer" treated as sufficient | Require in-house, application-specific evidence |
| Single-pillar pass | One antibody pillar (e.g., a clean WB band) read as full validation | Require the pillars the claim demands, per application |
| Application transfer | An antibody validated for WB assumed valid for IHC/IF | Validate each intended application separately |
| Primer specificity gap | Right-size band assumed specific without melt/NTC | Require single melt peak + NTC + RT-minus |
| Misidentified line | A named line trusted without STR | Mandate STR authentication + mycoplasma before use |
