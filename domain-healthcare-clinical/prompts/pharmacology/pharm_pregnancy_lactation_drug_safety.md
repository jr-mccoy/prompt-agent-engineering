---
title: "Pregnancy and Lactation Drug Safety Reasoning"
category: domain-healthcare-clinical/pharmacology
description: "Evaluate the safety of a specific medication in pregnancy and lactation by trimester-specific teratogenicity, placental transfer, peripartum and neonatal effects, and infant exposure via breast milk; specify acceptable alternatives, monitoring, and counseling."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - obstetrics
  - pharmacology
  - pregnancy
  - lactation
  - teratogenicity
  - prescribing
updated: "2026-05-12"
---

## Objective

Evaluate whether a specific medication should be continued, modified, or substituted in pregnancy or lactation: assess teratogenic potential by trimester, address placental transfer and peripartum/neonatal consequences, evaluate breast milk transfer and infant exposure, and weigh maternal disease risk vs medication risk. Output a written plan with rationale, alternative if needed, monitoring schedule, and patient counseling.

## Inputs

- Patient: gestational age (or trimester), or postpartum and lactating status; planned pregnancy
- Maternal diagnosis requiring therapy; severity; risk of untreated disease
- Current medication(s): drug, dose, formulation, duration
- Other contributing factors: polypharmacy, comorbid medical conditions, prior pregnancy outcomes, infant age and feeding pattern
- Maternal preference and shared decision context
- Specific clinical question (continue / switch / stop)

## Role

Senior obstetrician / maternal-fetal medicine specialist / clinical pharmacist explaining the risk-benefit assessment to a colleague or to a patient.

## Reasoning Steps

1. **Frame the decision: treat or not treat?**
   - **Untreated maternal disease has consequences** that often outweigh medication risk: untreated hypertension → preeclampsia; untreated diabetes → macrosomia, stillbirth; untreated depression → poor outcomes, suicide risk, neonatal effects; untreated thyroid disease → fetal hypothyroidism, congenital cretinism; untreated epilepsy → seizure injury, status; untreated HIV → vertical transmission.
   - The default is rarely "stop the medication" — usually "continue with the best-evidence option."

2. **Apply trimester-specific frameworks.**
   - **Pre-implantation (≤2 weeks post-conception, ~ weeks 1–2 from LMP):** "all or none" — major teratogen exposure either causes loss or no apparent harm; minimal teratogenic concern for surviving pregnancy.
   - **Embryogenesis (weeks 3–10 post-conception, weeks 5–12 LMP):** highest teratogenic susceptibility — organogenesis. Most structural malformations originate here.
   - **Fetal period (week 11 LMP onward):** structural anomalies less common; growth restriction, functional impairment, and CNS toxicity possible.
   - **Late pregnancy / peripartum:** consider neonatal effects (NICU complications from SSRIs, neonatal abstinence from opioids, hypoglycemia from sulfonylureas, magnesium effect on neonate, beta-blocker neonatal hypoglycemia/bradycardia, NSAIDs after 30 weeks — fetal ductus arteriosus closure and oligohydramnios).
   - **FDA letter categories (A/B/C/D/X)** discontinued in 2015; replaced by Pregnancy and Lactation Labeling Rule (PLLR) requiring narrative summaries — providers must look up current label and use registry/database data rather than category letters.

3. **Use authoritative data sources for specific drug-pregnancy questions.**
   - **Reprotox / TERIS / MotherToBaby / LactMed** (NIH-LactMed for breast milk specifically) for individual drug summaries.
   - **OTIS fact sheets** (organization of teratology information specialists).
   - **ACOG committee opinions** for specific conditions (asthma, depression, HTN, antiepileptics, anticoagulation, ART).
   - Note: package insert is often more conservative than current evidence; consult registries.

4. **Categorize specific drug classes (high-yield).**
   - **Definitely teratogenic — avoid in pregnancy:**
     - **Methotrexate** (folate antagonist — neural tube, limb, craniofacial); discontinue ≥3 months before conception.
     - **Valproate** (neural tube defects ~6–10%, cognitive impairment, autism spectrum signal at higher doses).
     - **Carbamazepine** (neural tube ~1%).
     - **Phenytoin** (fetal hydantoin syndrome).
     - **Phenobarbital** (cleft lip/palate, cardiac).
     - **Topiramate** (cleft palate, hypospadias at higher doses).
     - **Isotretinoin** (severe — CNS, cardiac, craniofacial — iPLEDGE program).
     - **Vitamin A high-dose** (>10,000 IU).
     - **Warfarin** (warfarin embryopathy — nasal hypoplasia, stippled epiphyses, CNS abnormalities, miscarriage; **first-trimester avoid**; high-dose mechanical valve patients sometimes continue with risk acceptance).
     - **ACE inhibitors / ARBs / direct renin inhibitors** (fetal renal dysgenesis, oligohydramnios, skull hypoplasia — second/third trimester worst).
     - **NSAIDs after 30 weeks** (premature ductus arteriosus closure, oligohydramnios).
     - **Statins** (avoid; recent data more reassuring but routine use not recommended).
     - **Tetracyclines after 15 weeks** (tooth/bone staining, growth inhibition).
     - **Fluoroquinolones** (cartilage concerns; avoid except for serious infection).
     - **Mycophenolate** (severe craniofacial, ear, limb malformations; switch before conception; both partners counseled).
     - **Thalidomide** (severe limb defects).
     - **Cytotoxic chemotherapy** (esp. first trimester); some agents (e.g., taxanes, anthracyclines) used in 2nd/3rd trimester with maternal indication.
   - **Generally safe / acceptable in pregnancy with monitoring:**
     - **Acetaminophen** (preferred analgesic).
     - **Amoxicillin, ampicillin, cephalosporins** (most penicillins and cephalosporins safe).
     - **Erythromycin (not estolate), azithromycin** (most macrolides reasonable).
     - **Nitrofurantoin** (avoid term/late third trimester — hemolytic anemia in newborn if G6PD; avoid in first trimester per some guidance).
     - **TMP-SMX** (avoid first trimester — neural tube; avoid term — kernicterus).
     - **Insulin** (does not cross placenta meaningfully; preferred for diabetes in pregnancy).
     - **Methyldopa, labetalol, nifedipine** (preferred for chronic HTN; methyldopa long established; labetalol commonly used).
     - **Heparin / LMWH** (do not cross placenta; preferred anticoagulant in pregnancy).
     - **Levothyroxine** (continue and adjust upward in pregnancy; ~25% dose increase typically needed).
     - **SSRIs** (most acceptable; sertraline favored; paroxetine cardiac defect signal — avoid in first trimester preferentially).
     - **Lamotrigine, levetiracetam** (preferred AEDs in pregnancy; lamotrigine UGT-induced clearance increases — monitor and adjust upward).
     - **Hydroxychloroquine** (continue in SLE pregnancy — benefits outweigh).
     - **TCAs** (acceptable; nortriptyline often used).
     - **Beta-blockers** — labetalol preferred; metoprolol acceptable; atenolol associated with growth restriction.
     - **Calcium channel blockers** — nifedipine acceptable for HTN.
   - **Antibiotics summary:** β-lactams generally safe; macrolides generally safe (avoid estolate); nitrofurantoin avoid term; TMP-SMX avoid first and term; fluoroquinolones / tetracyclines avoid.

5. **Lactation framework.**
   - **Most maternal medications are compatible with breastfeeding** — infant exposure typically <10% of maternal dose (relative infant dose, RID).
   - **Drug factors that increase infant exposure:**
     - High oral bioavailability in infant.
     - Long half-life in infant (immature CYP and renal clearance).
     - High Vd / lipid solubility / low protein binding → more milk transfer.
     - Active metabolites.
   - **LactMed (NIH) is the authoritative source.**
   - **Generally compatible with breastfeeding:**
     - SSRIs (sertraline preferred — lowest infant levels; paroxetine acceptable).
     - Most antibiotics.
     - Heparin, LMWH (large molecules don't transfer to milk).
     - Warfarin (low milk transfer; OK).
     - Insulin.
     - Levothyroxine.
     - Most antihypertensives (avoid atenolol).
     - Inhaled medications (asthma).
     - Acetaminophen, ibuprofen.
   - **Concerning in lactation:**
     - **Codeine** (CYP2D6 ultra-rapid metabolizers convert to morphine more efficiently → infant respiratory depression — case reports of infant death; **avoid codeine**; oxycodone, hydrocodone preferred).
     - **Tramadol** (similar concern; avoid).
     - **Amiodarone** (high iodine load; long half-life; accumulates).
     - **Lithium** (relatively high infant levels; monitor infant levels if used).
     - **Ergot alkaloids** (suppress prolactin; can cause infant toxicity).
     - **Radioactive isotopes** (temporary discontinuation per duration of half-life).
     - **Cytotoxic chemotherapy** (avoid breastfeeding during).
     - **Methotrexate** (avoid; even low-dose for autoimmune disease — risk-benefit; some sources allow with short course).
     - **Marijuana** (cannabinoid in breast milk; effects on infant uncertain; avoid).

6. **Specific scenarios.**
   - **Pregnant patient on warfarin for mechanical valve:** highest-risk scenario. Options: switch to LMWH (twice daily, dose-adjusted by anti-Xa; risk of valve thrombosis if subtherapeutic), or continue warfarin with INR monitoring (preserve at lowest effective dose; some advocate continuing warfarin throughout for high-risk valve, switching to heparin near delivery). Multi-disciplinary discussion.
   - **Pregnant patient with SLE:** continue hydroxychloroquine (improves outcomes); azathioprine acceptable; avoid mycophenolate, methotrexate; switch ≥3 months before conception. Steroids minimum effective dose.
   - **Pregnant with epilepsy on valproate:** very high teratogenic concern; switch to lamotrigine or levetiracetam preconception; folic acid 4 mg daily; never abruptly stop AED.
   - **Pregnancy with depression:** continue SSRI; sertraline preferred; avoid paroxetine if possible (especially first trimester); discuss balance vs maternal relapse risk.
   - **Pregnancy with diabetes:** insulin preferred; metformin acceptable (data accumulating); avoid sulfonylureas (hypoglycemia); GLP-1 RA and SGLT2i contraindicated.
   - **Pregnancy with hypothyroidism on levothyroxine:** continue and increase dose ~25% (often by adding 2 extra weekly tablets day-of-week); monitor TSH every 4 weeks until 20 weeks, then every 4–6 weeks; target lower TSH per trimester.
   - **Pregnancy with VTE:** LMWH (enoxaparin) therapeutic dose throughout pregnancy; switch to LMWH near term and adjust around delivery.

7. **Counsel and document.**
   - Risk-benefit conversation: severity of untreated disease, available data on drug in pregnancy, alternative options, residual uncertainty.
   - Document shared decision.
   - Provide MotherToBaby fact sheet or equivalent.
   - Multi-specialty input (maternal-fetal medicine, neurology, cardiology, rheumatology, oncology as relevant).

## Output Format

```
PATIENT SNAPSHOT:
- Trimester / lactation status / planned pregnancy
- Maternal indication and severity
- Current medication
- Maternal preference

DRUG ASSESSMENT:
- Drug: [name, class]
- Mechanism / pharmacology relevant to pregnancy
- Teratogenicity by trimester: [first / second / third / peripartum effects]
- Placental transfer
- Specific malformations reported
- Risk magnitude (background rate ~3%; absolute attributable risk)

LACTATION ASSESSMENT (if applicable):
- Relative infant dose (RID)
- Infant clearance considerations
- Reported infant effects
- LactMed summary

RECOMMENDATION:
- Continue / switch / stop, with rationale
- Alternative drug if switching: [name, dose, when to start]
- Timing of switch (pre-conception, first trimester, third trimester)
- Folate / vitamin supplementation

MONITORING:
- Maternal disease control during/after change
- Fetal: anatomy scan at 18–22 weeks, growth scans as indicated; non-invasive prenatal screening; condition-specific surveillance
- Levels and dose adjustments (lamotrigine, levothyroxine, LMWH)

PERIPARTUM / DELIVERY PLANNING:
- Avoid NSAIDs in third trimester
- Anticoagulation around delivery (switch warfarin → LMWH at 36 weeks; hold LMWH 24 h before induction or planned cesarean)
- AED level adjustments
- Magnesium / preeclampsia plan if indicated

NEONATAL CONSIDERATIONS:
- NICU watch (SSRI poor neonatal adaptation, opioid NAS, hypoglycemia from beta-blocker, etc.)
- Hep B vaccine, eye prophylaxis, vitamin K standard
- Specific issues per drug

LACTATION COUNSELING:
- Compatibility based on data
- Alternative if not compatible
- Timing of doses to minimize milk peak transfer (if applicable)
- LactMed reference

POSTPARTUM PLANNING:
- Restart pre-pregnancy regimen if applicable
- Contraception
- Mental health follow-up (postpartum depression risk high)
- Multi-specialty visits
```

## Worked Example

**Input:** 33-year-old woman, gravida 2 para 1, current gestational age 8 weeks. Established epilepsy (focal seizures, well-controlled on valproate 1000 mg/day for past 5 years; no breakthrough seizures in 3 years). Wants to continue pregnancy. Family is supportive. No prior major malformations in first child (when she was on lamotrigine).

**Output:**

```
PATIENT SNAPSHOT:
- 33 y G2P1 at 8 weeks GA on valproate 1000 mg/day for focal epilepsy ×5 years, currently well-controlled.
- Pregnancy at 8 weeks (mid-embryogenesis — neural tube has already closed at ~28 days post-conception, i.e., GA ~6 weeks). Window for prevention of NTD already largely passed.
- Maternal request to continue pregnancy.

DRUG ASSESSMENT:
- **Valproate** — strongest teratogenicity signal among AEDs:
  - Major congenital malformation rate ~6–10% (vs ~3% background) — neural tube defects 1–2%, cardiac defects, cleft palate, hypospadias, skeletal.
  - Dose-dependent: <800 mg/day lower risk than higher; 1000 mg/day is in the higher-risk range.
  - Cognitive impairment: NEAD study — IQ ~7–10 points lower in valproate-exposed children at age 6 vs lamotrigine or carbamazepine exposed.
  - Autism spectrum disorder risk ~3-fold elevated.
  - Significant exposure has already occurred at 8 weeks; switching now reduces but does not eliminate accrued risk.

RECOMMENDATION:
- **Switch to lamotrigine or levetiracetam** as soon as feasible — even at 8 weeks, reducing dose-time exposure of valproate may reduce cognitive/behavioral outcomes (the brain continues to develop).
- Cross-taper plan:
  - **Lamotrigine** (preferred given good response in prior pregnancy):
    - Start lamotrigine 25 mg PO daily ×2 weeks → 50 mg ×2 weeks → 100 mg daily ×1 week → 100 mg BID (200 mg/day target).
    - **With valproate present**: lamotrigine titration MUST be slower (valproate inhibits UGT glucuronidation → raises lamotrigine levels): start 25 mg every other day ×2 weeks → 25 mg daily ×2 weeks → 50 mg daily; check level when stable.
    - **Once lamotrigine therapeutic** (~weeks 4–6), start tapering valproate slowly: 1000 → 750 → 500 → 250 → off over 4–8 weeks. (Slower taper if any seizure activity emerges.)
    - Final lamotrigine target ~300–500 mg/day in pregnancy due to UGT induction by estrogen; levels usually need increase over second trimester.
  - **Alternative: levetiracetam** 500 mg BID → 1000 mg BID over 1–2 weeks (less interaction with valproate; more rapid switch possible). Switch valproate down gradually as before.
- **Folic acid 4 mg PO daily** (high-dose, started now — though NTD window passed for this pregnancy, supplementation continues for ongoing organogenesis).
- **Multivitamin** with iron.

MONITORING:
- Detailed anatomy ultrasound at 18–22 weeks — assess for NTD, cardiac defects (fetal echo at 22–24 weeks), cleft, limb.
- Maternal serum AFP at 15–20 weeks (NTD screen).
- Maternal-fetal medicine consultation.
- Seizure diary — any breakthrough seizure → titrate up lamotrigine, slow valproate taper.
- Lamotrigine levels at end of first trimester, monthly in 2nd–3rd trimester (rapid clearance increase in pregnancy).
- Multidisciplinary care: neurology, MFM, OB, genetic counselor.

PERIPARTUM / DELIVERY PLANNING:
- Continue lamotrigine through labor and postpartum.
- **Rapidly reduce lamotrigine dose postpartum** (within 1–2 weeks back to pre-pregnancy dose) — clearance falls quickly postpartum and supratherapeutic levels cause toxicity (dizziness, ataxia, sometimes rash).
- Vitamin K 10 mg IM to newborn (standard; AEDs not specifically a vitamin K trigger but routine).
- Pediatric neurology if any concerns at delivery.

NEONATAL CONSIDERATIONS:
- Continue routine newborn care.
- Higher-risk follow-up of developmental milestones given valproate exposure window of 8 weeks.

LACTATION COUNSELING:
- **Lamotrigine** in breast milk — moderate transfer, infant levels generally low; monitor infant for rash, sedation, feeding issues; usually compatible (LactMed: low–moderate risk; benefits often outweigh).
- **Valproate** if any residual — relatively compatible with breastfeeding (low milk transfer; previously concerning for thrombocytopenia in infants but recent data more reassuring).
- **Levetiracetam** if used — compatible.

POSTPARTUM PLANNING:
- Lamotrigine rapid dose down within 1–2 weeks to pre-pregnancy maintenance.
- Sleep deprivation → seizure risk; involve partner / family for shared night care.
- Postpartum depression screening (epilepsy + perinatal AED changes are risk factors).
- Effective contraception planning (estrogen-containing OCP lowers lamotrigine levels by ~50% — need dose adjustments or non-OCP contraception like LNG-IUD).
- Discuss future pregnancy: if planning another, ideally complete switch to lamotrigine + folate ≥3 months before conception.

PATIENT COUNSELING:
- Acknowledge already-incurred exposure; aim to minimize ongoing risk.
- Discuss range of outcomes and the limitations of mid-pregnancy switches.
- Document shared decision in chart with attestation that risks/benefits discussed.
- Provide MotherToBaby / OTIS valproate and lamotrigine fact sheets.
- Detailed anatomy scan plan, fetal echo, NIPS counseling.
```
