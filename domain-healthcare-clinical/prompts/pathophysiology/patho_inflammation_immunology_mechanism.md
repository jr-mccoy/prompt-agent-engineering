---
title: "Inflammation & Immunology Mechanism Reasoning"
category: domain-healthcare-clinical/pathophysiology
description: "Reason from inciting trigger through innate sensors, cytokine cascades, T- and B-cell programming, and effector tissue damage to explain an inflammatory or immunologic disease and the mechanistic rationale for targeted biologic therapy."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - CR-01
difficulty: advanced
tags:
  - immunology
  - inflammation
  - rheumatology
  - autoimmune
  - biologics
  - mechanism
updated: "2026-05-12"
---

## Objective

Reason through an inflammatory or immunologic disease by tracing the chain: inciting trigger → innate sensor activation → cytokine and chemokine output → adaptive immune programming (Th1 / Th2 / Th17 / Treg, B-cell class-switching) → effector cells / antibodies / immune complexes → tissue damage. Name the cytokines and cells driving each step, and explain why a specific biologic or small-molecule therapy intervenes where it does.

## Inputs

- Disease or syndrome (e.g., rheumatoid arthritis, psoriasis, IBD, SLE, ANCA vasculitis, asthma, atopic dermatitis, hemophagocytic lymphohistiocytosis, cytokine release syndrome, ARDS, sepsis)
- Available labs or biomarkers (CRP, ESR, ANA pattern + ENA, complement, autoantibodies, cytokine panels, eosinophil count, IgE)
- Specific therapeutic question to answer (e.g., "why does dupilumab help atopic dermatitis but not psoriasis?", "why are anti-TNF agents effective in IBD and RA but trigger psoriasiform skin lesions?", "why does rituximab help ANCA vasculitis but not all SLE?")

## Role

Senior immunologist / rheumatologist explaining mechanism to a colleague. Names the cytokine, names the cell, names the receptor and signaling pathway, and ties to the biologic.

## Reasoning Steps

1. **Identify the trigger and the dominant innate sensor.**
   - **PAMP sensors:** TLR2 (lipoteichoic acid, gram-pos), TLR4 (LPS), TLR3 (dsRNA, viral), TLR7/8 (ssRNA, viral), TLR9 (CpG DNA), NLRs (peptidoglycan, NOD1/2; NLRP3 inflammasome for ATP, urate, cholesterol crystals, K+ efflux), RIG-I (cytosolic viral RNA), cGAS-STING (cytosolic dsDNA).
   - **DAMP sensors:** same pattern receptors recognize host-derived danger signals (HMGB1, S100, urate crystals, mitochondrial DNA).
   - **Examples:**
     - Gout: NLRP3 inflammasome activated by monosodium urate crystals → caspase-1 cleaves pro-IL-1β → mature IL-1β release → neutrophil recruitment.
     - Familial Mediterranean fever: pyrin (MEFV gene) inflammasome activation → IL-1β.
     - Sepsis: TLR4 → MyD88 → NF-κB → massive TNF, IL-6, IL-1β.

2. **Map the cytokine output and downstream programming.**
   - **IL-1 family:** IL-1α, IL-1β, IL-18, IL-33, IL-36. IL-1β is the canonical inflammasome cytokine; IL-18 drives IFN-γ; IL-33 is an alarmin driving ILC2 / Th2 responses.
   - **TNF family:** TNF-α (pleiotropic, NF-κB driver), lymphotoxin, BAFF (B-cell survival), APRIL.
   - **IL-6:** acute-phase response (CRP, hepcidin → anemia of inflammation), Th17 differentiation (with TGF-β), B-cell to plasmablast differentiation.
   - **Type I IFN (α/β):** antiviral; pathologically elevated in SLE (especially with anti-dsDNA, anti-Sm) — the "interferon signature."
   - **Type II IFN (γ):** Th1 / NK / CD8; macrophage classical activation (M1); HLH driver.
   - **Th2 cytokines:** IL-4 (B-cell IgE class switch, M2 activation), IL-5 (eosinophil maturation/survival), IL-13 (mucus, smooth muscle hyperreactivity, skin barrier disruption), IL-31 (itch).
   - **Th17 cytokines:** IL-17A/F (neutrophil chemotaxis, antimicrobial peptide induction at barriers), IL-22 (epithelial proliferation), IL-23 (Th17 maintenance).
   - **Regulatory:** IL-10, TGF-β (also drives Th17 differentiation in pro-inflammatory context, paradoxically).

3. **Assign the disease to a dominant immune axis.**
   - **Th1-dominant (IFN-γ, IL-12, TNF, M1 macrophages, granulomas):** sarcoidosis, TB, granulomatous Crohn's, type 1 diabetes, MS.
   - **Th2-dominant (IL-4/5/13, eosinophils, IgE, M2 macrophages):** allergic asthma, atopic dermatitis, eosinophilic esophagitis, EGPA, helminth response.
   - **Th17-dominant (IL-17, IL-23, neutrophil-rich, barrier inflammation):** psoriasis, psoriatic arthritis, ankylosing spondylitis, some IBD, hidradenitis suppurativa.
   - **Type I IFN / autoantibody / immune-complex:** SLE, Sjögren's, dermatomyositis (Type I IFN signature), ANCA-associated vasculitis (autoantibody-driven), antiphospholipid syndrome.
   - **B-cell / plasma-cell autoantibody:** myasthenia gravis (AChR antibody), pemphigus (desmoglein antibody), neuromyelitis optica (aquaporin-4 antibody).
   - **Mixed / shifting:** RA (Th1 + Th17 + B-cell autoantibody + cytokine network around TNF and IL-6); IBD (Crohn's Th1/Th17, UC Th2/Th17 — generalizations imperfect).

4. **Trace the effector mechanism that causes tissue damage.**
   - Direct cytokine effect on tissue (IL-13 driving mucus, IL-17 driving neutrophil influx and antimicrobial peptide release at skin/gut, IL-6 driving hepcidin and anemia).
   - Antibody-driven damage: opsonization + complement (type II hypersensitivity, AIHA, ITP), immune complex deposition + complement activation (type III, SLE nephritis, post-strep GN, serum sickness).
   - Cell-mediated cytotoxicity: CD8 T-cells (type 1 diabetes islet destruction, viral hepatitis), NK cells, macrophage M1 with reactive nitrogen / oxygen species.
   - Persistent granuloma formation (Th1 + macrophages → giant cells, walled-off but tissue-destructive over time).
   - Loss of tolerance and break-down of regulatory cell suppression (Treg dysfunction in autoimmunity, IPEX syndrome from FOXP3 loss).

5. **Map the mechanistic intervention point of each available therapy.**
   - **Anti-TNF (etanercept, infliximab, adalimumab, golimumab, certolizumab):** block TNF signaling on tissue and immune cells. Effective in RA, AS, PsA, psoriasis, IBD. Etanercept is a soluble TNFR fusion; infliximab and adalimumab are full IgG1 mAbs (cell-killing via Fc → effective in granulomatous disease; etanercept is ineffective in granulomatous Crohn's because no Fc effector).
   - **Anti-IL-6 (tocilizumab — anti-IL-6R; sarilumab):** RA, giant cell arteritis, CAR-T cytokine release syndrome. Drops CRP, hepcidin, fever, acute-phase response.
   - **Anti-IL-1 (anakinra — IL-1Ra; canakinumab — anti-IL-1β; rilonacept — IL-1 trap):** autoinflammatory syndromes (CAPS, FMF, Still's disease), gout flare, recurrent pericarditis.
   - **Anti-IL-17 (secukinumab, ixekizumab — anti-IL-17A; bimekizumab — anti-IL-17A/F):** psoriasis, PsA, AS. Ineffective or worsens IBD (loss of IL-17 at gut barrier → dysbiosis and inflammation).
   - **Anti-IL-23 (ustekinumab — anti-p40 of IL-12/23; guselkumab, risankizumab — anti-p19 IL-23):** psoriasis, IBD, PsA. Upstream of IL-17 axis but more selective.
   - **Anti-IL-4Rα (dupilumab):** blocks IL-4 and IL-13 signaling. Atopic dermatitis, asthma, EoE, CRSwNP, prurigo nodularis. Does not help psoriasis (wrong axis).
   - **Anti-IL-5 / IL-5Rα (mepolizumab, reslizumab, benralizumab):** eosinophilic asthma, EGPA, HES.
   - **Anti-IgE (omalizumab):** allergic asthma, chronic spontaneous urticaria.
   - **B-cell depletion (rituximab — anti-CD20):** ANCA vasculitis (GPA, MPA), RA, pemphigus, NMOSD, refractory ITP. Variable in SLE.
   - **BAFF inhibition (belimumab):** SLE.
   - **JAK inhibitors (tofacitinib — JAK1/3; baricitinib — JAK1/2; upadacitinib — JAK1):** block cytokine signaling through type I/II cytokine receptors (IL-6, IFN, IL-2 family). Broad immunosuppression; black box for thrombosis, MACE, malignancy.
   - **T-cell co-stimulation block (abatacept — CTLA-4-Ig):** binds CD80/86 on APCs, blocks CD28 co-stim signal to T-cells. RA, PsA.
   - **S1P receptor modulators (fingolimod, ozanimod):** sequester lymphocytes in nodes. MS, UC.
   - **Integrin blockade (vedolizumab — α4β7, gut-selective; natalizumab — α4β1, CNS-active):** prevent lymphocyte trafficking to gut (vedo) or CNS (nata). IBD; MS for nata (PML risk via JC virus).
   - **Complement inhibition (eculizumab, ravulizumab — anti-C5):** PNH, aHUS, generalized myasthenia gravis (AChR+), NMOSD.

6. **Explain why the targeted therapy works in the disease it works in, and why it does not work (or causes harm) in adjacent diseases.** Tie back to the dominant axis in step 3.

## Output Format

```
DOMINANT IMMUNE AXIS: [Th1 / Th2 / Th17 / Type I IFN / autoantibody / immune complex / mixed — be specific]
KEY DRIVING CYTOKINES / CELLS: [list with role]

INITIATING TRIGGER & INNATE SENSOR:
[Trigger] → [Sensor / inflammasome] → [Initial cytokine output]

ADAPTIVE PROGRAMMING:
[How innate cytokines bias T-helper differentiation; relevant transcription factors — T-bet, GATA3, RORγt, FOXP3; B-cell class switching]

EFFECTOR MECHANISM OF TISSUE DAMAGE:
[Cells, cytokines, antibodies, complement, granulomas — at the affected tissue]

THERAPEUTIC INTERVENTION POINTS:
- [Drug 1]: blocks [target] → interrupts [step] → clinical effect [...]
- [Drug 2]: [...]
- Why [drug X] fails or worsens disease: [wrong axis / loss of barrier defense / paradoxical signaling]

DIFFERENTIATION FROM RELATED DISEASE:
- vs [related condition]: differs by [dominant cytokine / cell / target] → why a different biologic is selected

BIOMARKERS REFLECTING THE AXIS:
[ESR, CRP, IL-6, IFN signature, complement, autoantibody titer, eosinophils, IgE, calprotectin]
```

## Worked Example

**Input:** Why does dupilumab help severe atopic dermatitis but is ineffective in plaque psoriasis, and why do anti-IL-17 agents do the opposite?

**Output:**

```
DOMINANT IMMUNE AXIS:
- Atopic dermatitis: Th2-dominant (IL-4, IL-13, IL-31), with barrier dysfunction (filaggrin loss-of-function) amplifying allergen and microbial entry.
- Psoriasis: Th17-dominant (IL-23 → Th17 → IL-17A, IL-17F, IL-22), with epidermal hyperproliferation and neutrophil microabscesses.

KEY DRIVING CYTOKINES / CELLS:
- AD: IL-4 (B-cell IgE class switch, Th2 commitment), IL-13 (keratinocyte barrier disruption, mucus, itch), IL-31 (sensory neuron itch), TSLP (alarmin from damaged epithelium), eosinophils, mast cells, Th2 cells, ILC2s.
- Psoriasis: IL-23 (from dendritic cells), Th17 cells, IL-17A/F (recruit neutrophils, induce antimicrobial peptides — LL-37, S100, β-defensins — and keratinocyte hyperproliferation), IL-22 (keratinocyte proliferation), TNF (amplifies network).

INITIATING TRIGGER & INNATE SENSOR:
- AD: filaggrin loss-of-function → defective skin barrier → allergen + microbial penetration → keratinocyte release of TSLP, IL-25, IL-33 (alarmins) → ILC2 + dendritic cell activation → Th2 priming.
- Psoriasis: trigger (trauma — Koebner; streptococcal infection; drug; stress) → keratinocyte / dendritic cell antigen presentation + IL-23 release → Th17 commitment → IL-17 effector cytokines.

ADAPTIVE PROGRAMMING:
- AD: TSLP + IL-4 → GATA3 → Th2 differentiation → IL-4, IL-5, IL-13 production. B-cell IgE class switch (IL-4 + CD40L). FoxP3 Treg activity is reduced.
- Psoriasis: IL-6 + TGF-β + IL-23 → RORγt → Th17 differentiation → IL-17A, IL-17F, IL-22, GM-CSF. Plasmacytoid dendritic cells producing type I IFN amplify in early lesions.

EFFECTOR MECHANISM OF TISSUE DAMAGE:
- AD: IL-13 acts on keratinocytes to suppress filaggrin and ceramide synthesis (further barrier breakdown), induce CCL26/eotaxin (eosinophil recruitment), and stimulate sensory C-fibers via IL-31. Eosinophil granule proteins cause additional tissue damage. IgE-mediated mast cell activation amplifies pruritus and erythema.
- Psoriasis: IL-17A/F act on keratinocytes → CXCL1/2/8 (neutrophil recruitment, Munro microabscesses), antimicrobial peptides, S100 proteins (DAMPs amplifying feedback), proliferation. IL-22 → epidermal acanthosis. TNF amplifies endothelial adhesion and recruitment.

THERAPEUTIC INTERVENTION POINTS:
- Dupilumab (anti-IL-4Rα): blocks both IL-4 and IL-13 signaling (they share IL-4Rα in the type II receptor complex). Interrupts Th2 effector cytokines at their receptor. Dramatic effect in AD (EASI-75 60–70%), asthma (eosinophilic), EoE, prurigo nodularis. Ineffective in psoriasis because the dominant axis is Th17, not Th2 — blocking IL-4/13 leaves IL-17/23 untouched. Rare reports of paradoxical psoriasiform lesions on dupilumab — proposed mechanism: Th2 suppression unmasks latent Th17 drive.
- Secukinumab / ixekizumab (anti-IL-17A) and bimekizumab (anti-IL-17A/F): block neutrophilic axis at the effector cytokine. Highly effective in plaque psoriasis (PASI-90 ~70–90%), PsA, AS. Ineffective and sometimes worsens AD because Th17 contributes only a small share of AD pathology, while IL-17 is needed at mucosal barriers for fungal and S. aureus defense — blocking it worsens candidiasis and IBD.
- Ustekinumab (anti-IL-12/IL-23 p40) and risankizumab (anti-IL-23 p19): upstream of Th17. Effective in psoriasis, PsA, Crohn's, UC. Risankizumab achieves PASI-90 ~75%.
- Anti-TNF: effective in both psoriasis and IBD because TNF amplifies both Th17 and the broader inflammatory network; partial effect in AD because TNF is not a primary AD driver.

WHY DUPILUMAB FAILS IN PSORIASIS:
1. Dupilumab blocks IL-4Rα → no effect on IL-23, IL-17, IL-22, or TNF.
2. Psoriatic plaques are driven by IL-17/IL-23 acting on keratinocytes and recruiting neutrophils; these pathways operate independently of the Th2/IL-4 axis.
3. Removing IL-4/13 may even shift balance toward unopposed Th1/Th17 in some patients — clinical case reports of psoriasiform eruption on dupilumab.

WHY ANTI-IL-17 FAILS / WORSENS IN AD:
1. The IL-17 axis is a minor contributor to AD pathology.
2. IL-17 plays a homeostatic role at the skin barrier defending against S. aureus colonization (which is already worse in AD). Blockade can worsen S. aureus colonization and skin infections.
3. IL-17 blockade tends to flare or precipitate IBD in susceptible individuals via gut barrier loss — relevant comorbidity in some atopic patients.

DIFFERENTIATION FROM RELATED DISEASES:
- Psoriasis vs atopic dermatitis: well-demarcated silvery scaling plaques on extensor surfaces (psoriasis) vs ill-defined erythematous flexural lichenified eczema with serous oozing (AD). Histology: neutrophilic microabscesses + parakeratosis (psoriasis) vs spongiosis + eosinophil infiltration (AD).
- Eczema-psoriasis overlap: real, biopsy useful; sometimes patients need combination targeting (anti-TNF + topical).
- Psoriatic arthritis vs RA: both drive joint inflammation; PsA has enthesitis and DIP involvement, anti-TNF and anti-IL-17 effective; RA driven more by autoantibody (RF, anti-CCP) + Th17 + B-cell + IL-6 — responds to anti-CD20, anti-IL-6R, anti-TNF, abatacept, JAKi.

BIOMARKERS REFLECTING THE AXIS:
- AD: total IgE often elevated (not always; intrinsic AD has normal IgE), eosinophil count, serum CCL17/TARC (correlates with severity), filaggrin genotype.
- Psoriasis: PASI score (clinical), serum IL-17 / IL-22 elevated, neutrophil-driven (no specific blood biomarker routinely used clinically; CRP modestly elevated).
```
