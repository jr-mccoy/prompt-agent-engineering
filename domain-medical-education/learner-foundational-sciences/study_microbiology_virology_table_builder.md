---
title: "Virology Table Builder (Virus × Genome × Pathogenesis × Vaccine)"
category: medical-education/learner-foundational-sciences
description: "Build a structured virology reference table on a named virus family or list: genome architecture, capsid/envelope, host receptor, key pathogenic mechanism, clinical syndromes, antiviral targets, and vaccine status. Lock format; no narrative."
techniques:
  - ST-03
  - OC-03
  - CM-02
  - DT-02
  - QA-12
difficulty: intermediate
intended_use: model-testing
target_users:
  - medical-student-pre-clinical
  - medical-student-clinical
  - pa-student
  - pharmacy-student
tags:
  - microbiology
  - virology
  - genome
  - vaccine
  - pathogenesis
  - foundational-science
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/learner-foundational-sciences/study_microbiology_bug_drug_grid.md
  - domain-medical-education/learner-foundational-sciences/study_immunology_cascade_explainer.md
---

## Objective

Produce a row-per-virus reference table that locks the eight high-yield facts per virus (family, genome, structure, host receptor, pathogenesis, syndromes, antiviral targets, vaccine status). Output is a single table plus a confusable-pair appendix; no narrative essay.

## Your Role

USMLE Step 1 / NCLEX-RN content writer building a one-page virology reference. Strict adherence to Baltimore classification, ICTV nomenclature, and current CDC / WHO vaccine schedule.

## Inputs

- `scope`: a family, a syndrome cluster, or an explicit list — e.g., "Herpesviridae," "hepatitis viruses A–E," "common pediatric exanthem viruses," "respiratory viruses," "vector-borne flaviviruses"
- `learner_level`: `pre-clinical | clinical | board-prep`
- `column_set`: default eight columns (below) or user override
- `include_baltimore_class`: `true | false` — adds Baltimore group column
- `include_vaccine_schedule_age`: `true | false`

## Method

1. **Lock the row list.** State virus species in the canonical order of the family / scope. For exam-prep scope, order by frequency on USMLE.

2. **Populate eight columns** for each virus:
   1. **Family** (per ICTV)
   2. **Genome:** DNA vs RNA; ss vs ds; + or − sense; segmented vs non-segmented; circular vs linear
   3. **Structure:** capsid symmetry (icosahedral / helical / complex); envelope (yes/no)
   4. **Host receptor / entry:** the named receptor(s) and target cell
   5. **Key pathogenic mechanism:** lytic / latent / oncogenic / immune-mediated — *one mechanism per virus*
   6. **Major clinical syndromes:** 1–3 syndromes with the named clinical entity
   7. **Antiviral targets / agents:** specific drugs, or `—` if no antiviral
   8. **Vaccine status:** `live attenuated | inactivated | subunit | mRNA | toxoid (n/a) | viral vector | none`; add CDC schedule age if `include_vaccine_schedule_age = true`

3. **Locked table format (OC-03).** Markdown table. No prose between rows.

4. **Confusable-pair appendix.** Below the table, 3–5 commonly confused virology facts with the trap and the correct fact (QA-12). Examples: HSV-1 receptor (HVEM, nectin) vs. EBV receptor (CD21/CR2); HepB structure (partially dsDNA, reverse transcribes) vs. HepC (ssRNA+, flavivirus family); influenza segmented (re-assortment / antigenic shift) vs. rhinovirus non-segmented.

5. **Optional Baltimore column.** If requested, add column with Group I–VII classification.

## Output Format

```
VIROLOGY TABLE — [scope]
Learner level: [...]   Reference frame: ICTV + CDC/WHO vaccine schedule

| Virus | Family | Genome | Structure | Receptor / Target | Pathogenesis | Syndromes | Antivirals | Vaccine |
|---|---|---|---|---|---|---|---|---|
| [...] | [...] | [...] | [...] | [...] | [...] | [...] | [...] | [...] |

[Optional Baltimore column inserted between Family and Genome]
[Optional vaccine schedule-age appended in parentheses inside Vaccine column]

>>> CONFUSABLE-PAIR APPENDIX (QA-12)
- [Virus A] vs. [Virus B] on [fact axis]: trap is [...]; correct is [...].
- ...

>>> NOTE ON GAPS
- Where a fact is uncertain or genuinely contested (e.g., HIV vaccine status), state so explicitly. No fabricated specificity.
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `scope` | Selects row set |
| `learner_level` | Pre-clinical → emphasize structure / genome; clinical → emphasize syndromes; board-prep → emphasize confusable pairs |
| `include_baltimore_class` | Adds Group I–VII column |
| `include_vaccine_schedule_age` | Adds CDC age recommendation in vaccine column |
| `add_microscopy_findings` | Adds column for owl's eye (CMV), Negri bodies (rabies), Cowdry A (HSV/VZV), etc. |
| `pregnancy_overlay` | Adds column flagging teratogenic viruses (rubella, CMV, parvo B19, ZIKV) |

## Verification Checklist

- [ ] Every cell populated. No row with missing genome/structure.
- [ ] Genome cell uses the standard form: e.g., "ssRNA(+), non-segmented, linear" — not "RNA virus."
- [ ] Envelope status correct and explicit. (Common misses: Calicivirus = non-enveloped; HepE = non-enveloped; HepC = enveloped.)
- [ ] Receptor named where known (e.g., CD4 + CCR5/CXCR4 for HIV; ACE2 for SARS-CoV-2; sialic acid for influenza; CD21 for EBV; HVEM/nectin for HSV).
- [ ] Antiviral cell names *agents* when they exist; `—` when none. No "supportive care" as antiviral.
- [ ] Vaccine status one of the allowed categories. If `none` and a vaccine is in late-stage trial, footnote it; do not list as available.
- [ ] No invented receptors, no scrambled genome classifications.
- [ ] Confusable-pair appendix has at least 3 items, each clinically relevant.

## Worked Example (compact)

**Input:** `scope = Herpesviridae`, `learner_level = clinical`, `column_set = default`, `include_baltimore_class = true`, `add_microscopy_findings = true`.

**Output (excerpt):**

```
VIROLOGY TABLE — Herpesviridae (Human herpesviruses 1–8)
Learner level: clinical   Reference: ICTV + CDC

| Virus | Family | Baltimore | Genome | Structure | Receptor / Target | Pathogenesis | Syndromes | Microscopy | Antivirals | Vaccine |
|---|---|---|---|---|---|---|---|---|---|---|
| HSV-1 (HHV-1) | Herpesviridae | I (dsDNA) | dsDNA, linear | Icosahedral, enveloped | HVEM, nectin-1 → epithelial → trigeminal ganglion latency | Lytic + latent in sensory ganglion | Orolabial herpes, herpetic gingivostomatitis, keratitis, encephalitis (temporal lobe) | Cowdry A intranuclear inclusions; Tzanck (multinucleated giant cells) | Acyclovir, valacyclovir, famciclovir; foscarnet for resistant | None |
| HSV-2 (HHV-2) | Herpesviridae | I | dsDNA, linear | Icosahedral, enveloped | HVEM, nectin → genital epithelium → sacral ganglion latency | Lytic + latent | Genital herpes, neonatal HSV, meningitis (Mollaret) | Same as HSV-1 | Acyclovir, valacyclovir, famciclovir | None |
| VZV (HHV-3) | Herpesviridae | I | dsDNA, linear | Icosahedral, enveloped | Skin epithelium, DRG latency | Lytic + latent in DRG | Varicella (primary), zoster (reactivation), postherpetic neuralgia, Ramsay-Hunt | Cowdry A inclusions; multinucleated cells | Acyclovir, valacyclovir; IVIG for immunocompromised exposed | Live attenuated (varicella, ages 12–15 mo & 4–6 y); recombinant subunit Shingrix (≥50 y, 2-dose) |
| EBV (HHV-4) | Herpesviridae | I | dsDNA, linear | Icosahedral, enveloped | CD21 (CR2) on B cells; epithelial entry via gp350/gp42 | Latent in B cells; transforming (oncogenic) | Mono, Burkitt lymphoma, nasopharyngeal carcinoma, PTLD, Hodgkin association | Atypical lymphocytes (Downey cells, CD8+); EBER ISH in tissue | None routine; rituximab for PTLD targets B cells | None |
| CMV (HHV-5) | Herpesviridae | I | dsDNA, linear | Icosahedral, enveloped | Multiple cellular receptors; PDGFRα on fibroblasts | Latent in monocytes; lytic in many tissues | Mono (heterophile-neg), congenital (SNHL, periventricular calcifications), retinitis in AIDS, transplant CMV disease | Owl's-eye intranuclear inclusion + cytoplasmic inclusions | Ganciclovir, valganciclovir; foscarnet, cidofovir; letermovir prophylaxis post-HCT | None |
| HHV-6 / HHV-7 | Herpesviridae | I | dsDNA, linear | Icosahedral, enveloped | CD46 (HHV-6A), CD134 (HHV-6B); CD4 (HHV-7) | Latent in T cells | Roseola infantum (sixth disease) with high fever then rash; post-transplant reactivation | — | Ganciclovir, foscarnet (HHV-6 disease in HCT) | None |
| KSHV (HHV-8) | Herpesviridae | I | dsDNA, linear | Icosahedral, enveloped | Heparan sulfate / DC-SIGN; B cells, endothelial | Latent + oncogenic (vIL-6, vCyclin) | Kaposi sarcoma, primary effusion lymphoma, multicentric Castleman disease | Spindle cells with slit-like vascular spaces | No specific antiviral; ART for HIV-associated KS; rituximab for Castleman | None |

>>> CONFUSABLE-PAIR APPENDIX
- EBV vs. CMV mono: EBV is heterophile-positive (Monospot), atypical lymphocytes, splenomegaly; CMV is heterophile-negative mono, more common in older / immunocompromised.
- HSV-1 vs. HSV-2 by site: clinically overlap. HSV-1 can cause genital herpes; HSV-2 can cause orolabial. Serotype tells you reactivation risk, not site.
- Varicella (Cowdry A) vs. molluscum (Henderson-Patterson): molluscum is poxvirus, not herpesvirus; inclusion bodies cytoplasmic, not nuclear.
- Shingrix vs. Zostavax: Shingrix recombinant subunit, preferred; Zostavax live attenuated, withdrawn US 2020.
- HHV-6 roseola vs. measles: roseola = high fever first, rash *after* fever defervesces; measles = rash + cough/coryza/conjunctivitis + Koplik spots, fever continues.

>>> NOTE ON GAPS
- EBV vaccine: candidates in development; none currently licensed.
- HHV-6/7 receptors continue to be characterized; CD46 (6A) vs. CD134 (6B) given as canonical.
```
