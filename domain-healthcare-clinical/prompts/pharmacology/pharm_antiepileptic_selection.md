---
title: "Antiepileptic Drug Selection"
category: domain-healthcare-clinical/pharmacology
description: "Select an antiepileptic drug for new-onset focal, generalized, or specific syndromes based on seizure type, comorbidities (mood, migraine, renal, hepatic, pregnancy potential), drug interactions, and adverse-effect profile; specify drug, dose, titration, monitoring, and ILAE classification."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: intermediate
tags:
  - neurology
  - epilepsy
  - seizures
  - prescribing
  - drug-interactions
updated: "2026-05-12"
---

## Objective

Select an antiepileptic drug (ASM/AED) for a specific patient with new-onset epilepsy, breakthrough seizures on monotherapy, or a switch driven by intolerance: classify seizure type and syndrome per ILAE, match the drug to seizure type, account for comorbidities and reproductive potential, anticipate drug–drug interactions (especially with OCP and OACs), specify titration schedule, monitoring (levels, labs, suicidality), and follow-up. Output names the drug, doses, taper / cross-taper logic, and reassessment timing.

## Inputs

- Seizure type (focal with/without awareness impairment, focal to bilateral tonic-clonic, generalized tonic-clonic, generalized absence, myoclonic, atonic, infantile spasms; status epilepticus is a separate topic)
- Suspected syndrome (juvenile myoclonic epilepsy, childhood absence epilepsy, Dravet, Lennox-Gastaut, autoimmune encephalitis-related, post-stroke, post-traumatic, mesial temporal, structural, idiopathic generalized)
- EEG and MRI findings if available
- Comorbidities (mood disorder, migraine, neuropathic pain, weight, bone health, kidney/liver, CKD, ESRD, HIV, transplant)
- Reproductive potential and contraception status; pregnancy planning
- Current AEDs (name, dose, level if measured, response, intolerance)
- Concomitant medications (warfarin, DOACs, OCPs, tacrolimus / cyclosporine, statins, antidepressants, antibiotics)
- Patient preferences, cost / formulary, adherence concerns

## Role

Senior neurologist / epileptologist writing the AED prescription with titration plan, monitoring, and follow-up.

## Reasoning Steps

1. **Classify the seizure type and syndrome (ILAE 2017 framework).**
   - **Focal onset** with retained or impaired awareness; may evolve to focal-to-bilateral tonic-clonic.
   - **Generalized onset:** tonic-clonic, absence, myoclonic, atonic, tonic, clonic.
   - **Unknown onset.**
   - Syndromes: juvenile myoclonic epilepsy (JME), childhood/juvenile absence, Lennox-Gastaut, Dravet, mesial temporal lobe epilepsy, post-stroke, post-traumatic, idiopathic generalized epilepsy (IGE).
   - Risk of recurrence after first seizure (drives whether to treat after first vs second seizure):
     - Unprovoked first seizure with EEG abnormality, structural lesion on MRI, or nocturnal occurrence → high recurrence, treat after first.
     - Otherwise typical practice is to treat after a second unprovoked seizure or after first if patient circumstance requires.

2. **Match drug to seizure type.**
   - **Focal seizures (with or without bilateral evolution):**
     - **First-line monotherapy:** levetiracetam, lamotrigine, oxcarbazepine, lacosamide (newer first-line per recent guidance).
     - **Other options:** carbamazepine, phenytoin (older — efficacious but worse side-effect / interaction profile), valproate (avoid in women of reproductive potential), topiramate, zonisamide, brivaracetam, perampanel, eslicarbazepine, cenobamate.
   - **Generalized tonic-clonic:**
     - **First-line:** lamotrigine, levetiracetam, valproate (best efficacy but avoid in women of reproductive potential).
     - Avoid: carbamazepine, oxcarbazepine, phenytoin, gabapentin, vigabatrin — may worsen IGE.
   - **Generalized absence (childhood / juvenile):**
     - **First-line:** ethosuximide (especially childhood absence without GTC), valproate, lamotrigine.
     - Avoid carbamazepine, oxcarbazepine, phenytoin, vigabatrin, gabapentin — can worsen absences and myoclonus.
   - **Myoclonic (JME):**
     - **First-line:** valproate (highly effective; avoid in women of reproductive potential), levetiracetam, lamotrigine (may exacerbate myoclonus in some patients — caution), topiramate, zonisamide.
   - **Atonic / tonic (Lennox-Gastaut):**
     - Valproate, lamotrigine, rufinamide, topiramate, clobazam, cannabidiol (Epidiolex).
   - **Infantile spasms:** ACTH (intramuscular), vigabatrin (first-line if tuberous sclerosis), high-dose prednisolone.
   - **Dravet syndrome (SCN1A):** avoid sodium channel blockers (carbamazepine, oxcarbazepine, phenytoin, lamotrigine — may worsen). Use valproate, clobazam, stiripentol, cannabidiol, fenfluramine.

3. **Apply comorbidity and patient-context filters.**
   - **Mood / depression / suicidality:** AEDs carry FDA suicidality warning. Avoid where possible: levetiracetam (irritability, depression in ~10%), topiramate (depression), phenobarbital (depression). Mood-favorable: lamotrigine (mood-stabilizing), gabapentin, oxcarbazepine.
   - **Migraine:** topiramate (often dual indication for headache + epilepsy), valproate (avoid in women of reproductive potential).
   - **Neuropathic pain / fibromyalgia:** gabapentin (note: limited efficacy as monotherapy for focal seizures), pregabalin (similar), carbamazepine / oxcarbazepine (trigeminal neuralgia).
   - **Weight gain risk:** valproate, gabapentin, pregabalin, vigabatrin → weight gain. Topiramate, zonisamide → weight loss. Levetiracetam, lamotrigine neutral.
   - **Renal impairment:** levetiracetam, gabapentin, pregabalin, topiramate, zonisamide — need dose adjustment in CKD; phenytoin, carbamazepine, valproate — primarily hepatic, generally less adjustment needed.
   - **Hepatic impairment:** avoid valproate, felbamate; use gabapentin, levetiracetam, pregabalin.
   - **Reproductive potential / pregnancy planning:**
     - **Avoid valproate, phenytoin, phenobarbital, topiramate (high dose), carbamazepine** (in roughly decreasing order of teratogenic risk; valproate worst — neural tube defects, cardiac defects, cognitive impairment, autism spectrum at high doses).
     - Preferred in pregnancy: **lamotrigine, levetiracetam** — lowest teratogenicity in registries.
     - Folic acid 4 mg/day pre-conception and throughout pregnancy for women on AEDs.
     - Monitor lamotrigine levels closely in pregnancy — estrogen induces UGT glucuronidation, lowers lamotrigine levels; dose increases often required during pregnancy and decrease postpartum.
   - **Oral contraceptive interaction:**
     - **Enzyme-inducing AEDs** (carbamazepine, phenytoin, phenobarbital, primidone, oxcarbazepine, topiramate >200 mg, eslicarbazepine, rufinamide) **reduce OCP efficacy** — recommend ≥50 µg ethinyl estradiol formulation or non-oral contraception (IUD, depot, etonogestrel implant — note implants also reduced efficacy with inducers).
     - **Non-inducing:** levetiracetam, lamotrigine, valproate, gabapentin, pregabalin, lacosamide, brivaracetam, zonisamide, ethosuximide. Lamotrigine note: estrogen-containing OCP lowers lamotrigine levels by ~50% — adjust dose during cycles.
   - **HIV ART / immunosuppressants:** avoid enzyme-inducing AEDs (interact with protease inhibitors, NNRTIs, integrase inhibitors, tacrolimus, sirolimus, cyclosporine). Levetiracetam, lacosamide, gabapentin, pregabalin preferred.
   - **Bone health:** chronic enzyme-inducing AEDs and valproate associated with bone loss; supplement vitamin D, calcium, DEXA in long-term users.
   - **Allergy / rash history (HLA-B\*1502 in Asian / Han Chinese populations):** test before carbamazepine, oxcarbazepine — positive carries SJS/TEN risk; lamotrigine SJS/TEN rate increases with rapid titration.

4. **Specify starting dose and titration schedule.**
   - **Levetiracetam:** 500 mg PO BID start; can titrate to 1000–1500 mg BID over 1–2 weeks. Renal adjustment for CrCl <80.
   - **Lamotrigine:** very slow titration to avoid SJS/TEN.
     - Without valproate, without enzyme inducer: 25 mg daily ×2 weeks → 50 mg daily ×2 weeks → 100 mg daily ×1 week → 150–200 mg daily.
     - With valproate (inhibits glucuronidation; raises lamotrigine levels): 25 mg every other day ×2 weeks → 25 mg daily ×2 weeks → 50 mg daily; target 100–200 mg/day.
     - With enzyme inducer (carbamazepine, phenytoin): start 50 mg daily ×2 weeks → 100 mg BID; higher target dose 300–500 mg/day.
   - **Oxcarbazepine:** 300 mg BID start → titrate to 600 mg BID over 2 weeks; monitor sodium (hyponatremia).
   - **Lacosamide:** 50 mg BID start → 100 mg BID after 1 week; max 400 mg/day.
   - **Topiramate:** 25 mg daily, increase 25–50 mg/week to 100–200 mg BID. Watch cognitive effects, paresthesias, kidney stones, glaucoma.
   - **Valproate:** 250 mg BID → 500 mg BID over 1–2 weeks; check level (50–100 µg/mL). Watch hepatotoxicity (LFTs), thrombocytopenia, hyperammonemia, pancreatitis, weight gain, hair loss, tremor.
   - **Carbamazepine:** 100 mg BID → 200 mg BID over 2 weeks; titrate to 400–600 mg BID; auto-induces metabolism (level drops at 2–6 weeks; re-titrate). HLA-B\*1502 check in Asian patients.
   - **Phenytoin:** load 15–20 mg/kg IV (max 50 mg/min, prefer fosphenytoin); maintenance 300–400 mg/day; check level (target 10–20 µg/mL total; free 1–2 µg/mL if albumin abnormal). Multiple interactions.
   - **Ethosuximide (absence):** 250 mg daily → 500 mg BID → titrate to 1.0–2.0 g/day; monitor for GI upset, hiccups.
   - **Brivaracetam:** 25 mg BID → 50 mg BID; similar mechanism to levetiracetam; less irritability.
   - **Perampanel:** 2 mg qHS → 4 mg → 8–12 mg; watch psychiatric adverse effects (homicidal ideation reported; black-box).
   - **Cannabidiol (Epidiolex):** 2.5 mg/kg BID → 5 mg/kg BID → up to 10 mg/kg BID for LGS, Dravet, tuberous sclerosis; LFT monitoring, valproate interaction.

5. **Plan monitoring.**
   - Baseline labs: CBC, CMP (Na, LFTs, renal), pregnancy test if applicable.
   - For specific drugs:
     - Valproate: LFTs, CBC q3–6 months; ammonia if encephalopathy.
     - Carbamazepine: CBC (aplastic anemia rare), Na (hyponatremia), LFTs.
     - Oxcarbazepine: Na (hyponatremia risk higher than carbamazepine).
     - Topiramate: bicarbonate (metabolic acidosis), kidney function.
     - Lamotrigine: rash check; level if pregnancy / OCP change.
     - Phenytoin: level, albumin, free phenytoin if appropriate.
   - Counsel on suicidality (FDA boxed warning across class) — monitor at follow-up.
   - Counsel on adherence; missing doses can precipitate breakthrough seizures.
   - Counsel on driving restrictions per state law (typically 3–12 months seizure-free; varies).

6. **Plan reassessment and switching.**
   - Reassess at 6–8 weeks after target dose reached; assess seizure frequency, side effects, level (if relevant), labs.
   - If seizures persist on adequate dose / level: switch to second monotherapy or add second AED.
   - Drug-resistant epilepsy (failure of 2 adequately tried AEDs at target dose) → epilepsy center referral for surgical evaluation, vagal nerve stimulation, RNS, ketogenic diet.
   - Switching: cross-taper over 4–6 weeks; titrate new AED to target dose before tapering off old one.

## Output Format

```
PATIENT SNAPSHOT:
- Seizure type and syndrome: [ILAE classification]
- Comorbidities and patient context: [mood, migraine, weight, kidney, hepatic, pregnancy potential, contraception, ART, transplant]
- Current AEDs / response / intolerances: [...]

DIAGNOSIS / SYNDROME:
[Type, EEG / MRI summary if available, risk of recurrence]

SELECTED AGENT:
- Drug: [name]
- Starting dose: [mg] [route] [frequency]
- Titration: [step-by-step weekly increments to target dose]
- Target dose: [mg/day]

RATIONALE:
- Matches seizure type: [...]
- Comorbidity fit: [why this drug over alternates]
- Drug interactions: [identified, managed]
- Reproductive plan: [folate, OCP-compatible choice]

TAPER / SWITCH (if applicable):
- Old AED: [name] [dose] — taper over [N weeks]
- New AED: [titration as above]
- Cross-taper plan: [overlap, target dose first]

MONITORING:
- Baseline labs: [CBC, CMP, pregnancy test as indicated]
- Drug levels if applicable: [target range, timing]
- Adverse-effect surveillance: [class- and drug-specific]
- Suicidality screen at each visit

PATIENT EDUCATION:
- Adherence: [strict consistent dosing; consequences of missed doses]
- Driving restrictions: [state law guidance; typically 3–12 months]
- Rash / SJS warning: [for lamotrigine, carbamazepine, oxcarbazepine — emergency action if rash develops]
- Pregnancy contraception: [folic acid 4 mg/d, planning visit before conception]
- Bone health if long-term inducing AED: [Ca, vit D, DEXA]

FOLLOW-UP:
- 2 weeks: phone or visit (tolerability, side effects)
- 6–8 weeks: full reassessment (seizure log, level if applicable)
- Every 3 months once stable

WHEN TO SWITCH OR ESCALATE:
- Persistent seizures on adequate dose / level after 6–8 weeks: switch monotherapy or add 2nd AED
- Two failed adequate trials: epilepsy center referral (drug-resistant epilepsy)
- Severe rash, hepatotoxicity, hyponatremia, psychiatric AE: hold drug, evaluate, switch
```

## Worked Example

**Input:** 24-year-old woman, recent new-onset generalized tonic-clonic seizure preceded by morning myoclonic jerks ×3 months. EEG shows generalized 4 Hz spike-wave; MRI normal. ILAE classification: idiopathic generalized epilepsy / juvenile myoclonic epilepsy (JME). She is sexually active on combined oral contraceptive (35 µg ethinyl estradiol + norgestimate). Comorbid migraine. Wants to plan pregnancy in 1–2 years. Select an AED.

**Output:**

```
PATIENT SNAPSHOT:
- 24 y woman with JME (myoclonic + recent first GTC; EEG generalized spike-wave 4 Hz; MRI normal).
- On combined OCP; planning pregnancy in 1–2 years.
- Comorbid migraine.

DIAGNOSIS / SYNDROME:
- Juvenile myoclonic epilepsy (idiopathic generalized epilepsy, ILAE).
- Likely to be lifelong; treatment indicated after first GTC given prior myoclonic seizures and EEG findings (high recurrence risk).

SELECTED AGENT:
- **Lamotrigine.**
- Starting dose: 25 mg PO daily.
- Titration: 25 mg daily ×2 weeks → 50 mg daily ×2 weeks → 100 mg daily ×1 week → 100 mg BID (200 mg/day).
- Target dose: 200–300 mg/day; titrate further if seizures persist; check level if needed during pregnancy.

RATIONALE:
- **Seizure type match:** lamotrigine is first-line for JME / generalized seizures (good efficacy for GTC; reasonable for myoclonus though valproate is more effective; risk of worsening myoclonus in some — monitor). Levetiracetam is the strongest alternative.
- **Pregnancy planning:** lamotrigine has among the lowest teratogenicity in pregnancy registries (~2% major congenital malformation rate, near population baseline; valproate 6–10% with dose-dependent neurodevelopmental risk — avoid in women of reproductive potential).
- **OCP interaction:** the combined OCP induces lamotrigine glucuronidation, lowering lamotrigine levels by ~50% during pill-taking weeks. May need higher target dose during OCP use; check level after stable dose reached; adjust around hormone-free week and changes in contraception.
- **Migraine:** topiramate would also dual-treat migraine + epilepsy but causes cognitive slowing, paresthesias, kidney stones, weight loss, and has teratogenic concern (cleft palate / hypospadias signal at higher doses); lamotrigine without migraine benefit but better pregnancy profile and tolerability.
- **Valproate considered and rejected:** most effective for JME but teratogenic and IQ-impairing in offspring; not appropriate in a woman of reproductive potential planning pregnancy.
- **Levetiracetam alternative:** equally reasonable; if she has prominent mood issues (depression / anxiety), lamotrigine preferred (mood-stabilizing) over levetiracetam (irritability and depression in ~10%).

TAPER / SWITCH:
- Not applicable — initial monotherapy.

MONITORING:
- Baseline labs: CBC, CMP, pregnancy test (negative confirmed before starting).
- Lamotrigine: rash watch (especially first 8 weeks); SJS/TEN risk increased with rapid titration → strict adherence to titration schedule; counsel to call immediately for rash, mouth sores, eye involvement.
- Level not routinely required outside pregnancy / OCP / interaction circumstances. Will check post-pregnancy planning.
- Suicidality screen at each visit (FDA class warning).

PATIENT EDUCATION:
- Strict adherence (especially for lamotrigine — rash risk if dose interrupted >5 days and restarted at full dose; if interrupted, restart at low and titrate again).
- Driving: state law (often 3–6 months seizure-free); counsel to stop driving from now until cleared by neurologist per local regulations.
- Sleep hygiene (sleep deprivation triggers JME seizures).
- Avoid alcohol (lowers seizure threshold).
- Photic stimulation triggers in some — counsel about flashing lights.
- Folic acid 4 mg PO daily started now (pre-conception; continue through pregnancy).
- Contraception note: OCP lowers lamotrigine levels; may need dose increase during use, decrease during hormone-free week. Consider non-OCP method (LNG-IUD does not interact). Continued OCP acceptable if monitoring is set up.
- Pre-conception counseling: visit before discontinuing contraception. Anticipate lamotrigine dose increase ~50% during pregnancy due to UGT induction; monthly levels in 2nd–3rd trimester; rapid post-partum dose reduction to pre-pregnancy level to avoid toxicity.

FOLLOW-UP:
- 2-week phone check (titration adherence, rash, mood).
- 6-week visit (after reaching 100 mg/day): seizure log, side effects, considered up-titration.
- 8 weeks: at 200 mg/day target.
- 3 months: reassess seizure freedom and need for higher dose.
- Pre-pregnancy planning visit when she's ready.

WHEN TO SWITCH OR ESCALATE:
- Breakthrough GTC or myoclonus on 300 mg/day with documented adherence → consider switch to levetiracetam (1500–3000 mg/day) or add as 2nd agent.
- Severe rash, hypersensitivity, hematologic, hepatic AE → stop, evaluate, alternative agent.
- Two adequate monotherapy trials without seizure freedom → epilepsy center referral for evaluation; surgical option less applicable in IGE but VNS / dietary therapy possible.
```
