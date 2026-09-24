---
title: "Red Eye Workup"
category: domain-healthcare-clinical/specialty
description: "Separate benign red eye (conjunctivitis, subconjunctival hemorrhage, blepharitis, episcleritis) from sight-threatening causes (keratitis, uveitis, angle closure, scleritis, orbital cellulitis, chemical injury) and commit to treatment and ophthalmology timing."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: intermediate
tags:
  - ophthalmology
  - emergency-medicine
  - primary-care
  - specialty-assessment
  - pink-eye
  - painful-eye
  - chemical-in-eye
updated: "2026-09-24"
related_prompts:
  - domain-healthcare-clinical/prompts/specialty/specialty_acute_vision_loss.md
  - domain-healthcare-clinical/prompts/reasoning/workup_headache.md
  - domain-medical-education/learner-clinical-reasoning/reason_red_flag_can_t_miss_drill.md
---

## Objective

Work up the acutely red eye in a primary care, urgent care, or ED setting: screen for sight-threatening red flags, localize the process (lids, conjunctiva, episclera/sclera, cornea, anterior chamber, orbit), commit to a working diagnosis, write the treatment, and state the exact ophthalmology referral timing (emergent / same-day / within 24–48 h / routine / none). Decision support for a licensed clinician: confirm doses, renal/hepatic adjustment and thresholds against the current guideline and local formulary. A chemical injury, suspected open globe, or acute angle closure is irrigated, shielded, or treated and sent now, not after this output.

## When to Use

- An acutely red eye in primary care, urgent care, or the ED — separating benign causes from sight-threatening ones.
- Deciding what to treat at the front line and the exact ophthalmology timing.
- A chemical splash, a contact-lens wearer with pain, or a red eye after eye surgery or intravitreal injection.

**Not this prompt if:**

- Vision loss is the presenting problem in a white, quiet eye (CRAO, GCA, retinal detachment, optic neuritis) — `specialty/specialty_acute_vision_loss.md`. A red eye with reduced acuity stays here, where reduced acuity is a red flag.
- Headache is the lead complaint without eye findings — `reasoning/workup_headache.md`, which screens for angle closure with tonometry.

## Inputs

- History: onset, unilateral vs bilateral, pain (none / gritty foreign-body / deep boring), photophobia, visual change, discharge (watery, mucoid, purulent, hyperpurulent), itch, halos, headache, nausea
- Exposures: contact lens wear (overnight wear, water exposure), trauma, high-velocity projectile (grinding, hammering metal), chemical splash (acid vs alkali), recent eye surgery or intravitreal injection, sick contacts, sexual history (neonate or adult hyperacute discharge)
- Systemic: HLA-B27 disease, IBD, sarcoid, RA, vasculitis (GPA), herpes zoster in V1, immunosuppression
- Exam: visual acuity each eye (with pinhole), pupil size/shape/reactivity, conjunctival vs ciliary (perilimbal) injection, corneal clarity, fluorescein pattern, anterior chamber (hypopyon, hyphema, depth), IOP if measurable, lid eversion, preauricular node, proptosis and extraocular movements
- Medications: topical steroids, anticholinergics/sympathomimetics (angle-closure triggers), anticoagulants

## Role

Senior attending ophthalmologist taking a phone consult and supporting the treating ED or primary care clinician. Direct about what can be treated at the front line and what must be seen at the slit lamp today.

## Reasoning Steps

1. **Chemical injury overrides everything.** Irrigate first, examine second. Copious saline or lactated Ringer's (≥1–2 L) via Morgan lens or tubing after topical anesthetic, until conjunctival fornix pH is 7.0–7.5 on repeat testing 5–10 min after pausing. Sweep fornices for particulate. Alkali is worse than acid. Emergent ophthalmology.
   - **Stop and escalate — emergent ophthalmology now — also for:** suspected open globe (shield, no pressure on the eye), acute angle closure (fixed mid-dilated pupil, hazy cornea, IOP often >40 mmHg), endophthalmitis after surgery or injection, orbital cellulitis with reduced acuity or RAPD, and hyperacute purulent discharge.

2. **Screen red flags — any one moves this out of "benign red eye."**
   - Reduced visual acuity not corrected by pinhole
   - Moderate-to-severe pain (not just grittiness), true photophobia (including consensual photophobia — light in the unaffected eye hurts the affected one)
   - Ciliary flush (injection concentrated at the limbus)
   - Corneal opacity, infiltrate, or fluorescein uptake beyond punctate
   - Fixed or mid-dilated pupil, or a small irregular pupil
   - Hypopyon or hyphema
   - Contact lens wearer with pain
   - Recent intraocular surgery or injection (endophthalmitis)
   - Proptosis, pain with eye movement, ophthalmoplegia (orbital cellulitis)
   - Hyperacute copious purulent discharge (gonococcal)
   - Vesicles on the nose tip (Hutchinson sign — nasociliary involvement in zoster)
   - Neonate

3. **Localize and name the process.**
   - **Conjunctivitis:** diffuse conjunctival injection, normal acuity, no photophobia. Viral (adenovirus — watery, bilateral in sequence, preauricular node, follicles, highly contagious), bacterial (mucopurulent, lids stuck in morning), allergic (itch dominant, bilateral, chemosis, atopic history), chlamydial (chronic follicular in sexually active), gonococcal (hyperacute — can perforate cornea within 24–48 h).
   - **Subconjunctival hemorrhage:** painless flat sharply demarcated blood; check BP, anticoagulation/INR if recurrent; posttraumatic 360° hemorrhage with low IOP → consider occult globe rupture.
   - **Blepharitis / dry eye:** lid margin crusting, burning, worse in morning or with screens.
   - **Episcleritis:** sectoral redness, mild discomfort, vessels blanch with topical phenylephrine and move with a cotton swab. Benign, self-limited.
   - **Scleritis:** severe boring pain that wakes the patient, globe tender, violaceous hue, vessels do not blanch with phenylephrine. A large share (around 40–50% in referral series) has an associated systemic disease (RA, GPA, relapsing polychondritis). Necrotizing scleritis is sight-threatening and often signals active systemic vasculitis.
   - **Keratitis:** pain, photophobia, foreign-body sensation, reduced acuity. Contact lens bacterial keratitis (Pseudomonas) = white infiltrate with epithelial defect. HSV epithelial keratitis = dendrite with terminal bulbs on fluorescein. Acanthamoeba = pain out of proportion, water exposure with lenses. Zoster ophthalmicus with keratitis/uveitis.
   - **Anterior uveitis (iritis):** ciliary flush, photophobia, reduced acuity, small (miotic) possibly irregular pupil (posterior synechiae), cells/flare on slit lamp, hypopyon if severe.
   - **Acute angle-closure glaucoma:** severe pain, headache, nausea/vomiting, halos, hazy (edematous) cornea, fixed mid-dilated pupil, shallow anterior chamber, markedly elevated IOP (often >40 mmHg), rock-hard globe on palpation. Triggers: dim light, anticholinergics, sympathomimetics, topiramate (bilateral secondary angle closure), hyperopia, Asian ethnicity, older age.
   - **Endophthalmitis:** pain and decreased vision days after surgery/injection, hypopyon.
   - **Orbital vs preseptal cellulitis:** proptosis, painful or restricted EOM, decreased acuity, RAPD → orbital.

4. **Examine in the right order.** Visual acuity first (after irrigation if chemical), then pupils, then fluorescein, then IOP. Do not measure IOP or press on the globe if penetrating injury or globe rupture is possible (teardrop pupil, 360° chemosis/hemorrhage, positive Seidel sign) — shield and send.

5. **Treat what can be treated at the front line.**
   - **Viral conjunctivitis:** supportive — cool compresses, preservative-free artificial tears; strict hand hygiene; no work/school contact while discharge present per local policy. No antibiotics, no topical steroids.
   - **Bacterial conjunctivitis (non-contact-lens):** erythromycin 0.5% ointment ¼–½ inch QID × 5–7 days, or trimethoprim-polymyxin B drops 1 drop QID × 5–7 days.
   - **Contact lens wearer with conjunctivitis/keratitis:** stop lens wear; anti-pseudomonal fluoroquinolone (moxifloxacin 0.5% or ciprofloxacin 0.3%) 1 drop q1–2h while awake for suspected keratitis; never patch a lens wearer's eye. Any infiltrate → same-day ophthalmology for scraping/culture.
   - **Gonococcal conjunctivitis:** ceftriaxone 1 g IM single dose (adult), saline lavage, treat for chlamydia coinfection; same-day ophthalmology.
   - **Chlamydial (adult inclusion) conjunctivitis:** azithromycin 1 g PO once or doxycycline 100 mg BID × 7 days; treat partners.
   - **Allergic:** olopatadine 0.1% BID or ketotifen 0.025% BID; cool compresses; avoid rubbing.
   - **HSV epithelial keratitis:** ganciclovir 0.15% gel 5×/day or trifluridine 1% 9×/day, or oral acyclovir 400 mg 5×/day / valacyclovir 500 mg TID; ophthalmology within 24 h. No topical steroid.
   - **Zoster ophthalmicus:** valacyclovir 1 g TID × 7 days started within 72 h of rash (start later if new lesions or eye involvement); ophthalmology within 24 h, sooner if Hutchinson sign with red eye.
   - **Episcleritis:** artificial tears, oral NSAID if symptomatic; routine follow-up.
   - **Corneal abrasion (non-lens):** erythromycin ointment QID × 3–5 days, oral analgesia; recheck 24–48 h if large or central.

6. **Start therapy and send for sight-threatening causes.**
   - **Acute angle closure:** timolol 0.5% 1 drop, apraclonidine 1% (or brimonidine 0.2%) 1 drop, pilocarpine 1–2% 1 drop (most effective once IOP begins to fall and ischemia resolves), acetazolamide 500 mg IV or PO (check sulfa allergy, renal function, sickle cell), supine positioning, antiemetic, analgesia; mannitol 1–2 g/kg IV if IOP refractory. Emergent ophthalmology for laser peripheral iridotomy; the fellow eye usually needs prophylactic iridotomy. If topiramate-induced, stop topiramate and avoid pilocarpine/iridotomy — mechanism is ciliary body effusion; cycloplegia is used instead.
   - **Anterior uveitis:** same-day or next-day ophthalmology for slit-lamp confirmation, then prednisolone acetate 1% and cycloplegic (cyclopentolate 1%) — steroid started only after HSV keratitis is excluded at the slit lamp. Workup for recurrent/bilateral/granulomatous: HLA-B27, sacroiliac imaging if back pain, ACE and chest imaging (sarcoid), syphilis serology, TB testing.
   - **Scleritis:** ophthalmology within 24 h; oral NSAID for non-necrotizing; systemic steroids/immunosuppression for necrotizing; workup ANCA, RF/anti-CCP, ANA, syphilis, urinalysis.
   - **Bacterial keratitis / corneal ulcer:** same-day ophthalmology; hourly fortified or fluoroquinolone drops started only after cultures if ophthalmology is immediately available, otherwise start moxifloxacin q1h and send.
   - **Orbital cellulitis:** CT orbits with contrast, IV vancomycin plus ceftriaxone (or ampicillin-sulbactam), ophthalmology and ENT (sinus source); abscess or visual compromise → surgical drainage.
   - **Endophthalmitis:** emergent ophthalmology (vitreous tap and intravitreal antibiotics).

7. **Never do at the front line.** Prescribe topical anesthetic for home use (corneal melt); start topical steroids without slit-lamp exclusion of HSV and ulcer; patch a contact-lens-related abrasion; dilate a patient with suspected narrow angles without a plan.

8. **Set follow-up.** Conjunctivitis: return if pain, photophobia, reduced vision, or no improvement in 5–7 days (bacterial) / 2–3 weeks (viral). Everything with a red flag has an explicit ophthalmology time.

## Output Format

```
RED FLAGS: [present / absent — list]

LOCALIZATION: [lids / conjunctiva / episclera / sclera / cornea / anterior chamber / orbit]

KEY EXAM: VA OD/OS | pupils | injection pattern | fluorescein | AC | IOP

WORKING DIAGNOSIS: [specific]
DIFFERENTIAL: [2–3 alternatives with the finding that separates them]

TREATMENT:
- [drug, strength, dose, frequency, duration]
- [non-drug: irrigation, lens discontinuation, shield, positioning]

OPHTHALMOLOGY: [emergent now / same day / within 24–48 h / routine / not needed]

ADDITIONAL WORKUP: [cultures, CT orbits, systemic serology, STI testing]

RETURN PRECAUTIONS / INFECTION CONTROL:
- [ ]

PITFALLS TO AVOID:
- [ ]
```

## Verification

- [ ] Visual acuity with pinhole is recorded for each eye before any conclusion (after irrigation if chemical).
- [ ] Every step-2 red flag is marked present or absent.
- [ ] The working diagnosis is traced to the injection pattern, fluorescein, pupil, anterior chamber, and IOP findings.
- [ ] No topical steroid or home topical anesthetic is prescribed without slit-lamp exclusion of HSV and ulcer, and the ophthalmology timing uses one of the five stated categories.
- [ ] Systemic drugs (acetazolamide, mannitol, oral antivirals) are checked against renal function, sulfa allergy, and sickle status; confirm doses, renal adjustment and thresholds against the current guideline and local formulary.

## False-Positive Prevention

- Any red eye with discharge called bacterial conjunctivitis — most adult conjunctivitis is viral, and mucoid discharge alone does not justify antibiotics.
- Punctate fluorescein staining from dry eye or viral conjunctivitis called keratitis — keratitis needs an infiltrate or epithelial defect with pain and reduced acuity.
- Sectoral redness called scleritis without checking phenylephrine blanching and pain severity — episcleritis does not need a systemic workup.
- A falsely high IOP from lid squeezing or pressure on the globe read as angle closure — correlate with the pupil, cornea, and chamber depth.

## Worked Example

**Input:** 67 y/o F, hyperopic, presents at 11 pm with 3 h of severe right eye pain, frontal headache, vomiting ×2, blurred vision with rainbow halos around lights. Started in a dark movie theater. Took an OTC cold remedy with pseudoephedrine and diphenhydramine this afternoon. Exam: VA OD counting fingers at 3 ft, OS 20/30. Right pupil 5 mm, nonreactive; left 3 mm reactive. Right cornea hazy, diffuse perilimbal injection, shallow anterior chamber on penlight oblique illumination. Tonopen IOP OD 58, OS 17. No discharge, no fluorescein uptake.

**Output:**

```
RED FLAGS: Present — decreased acuity, severe pain, halos, fixed mid-dilated pupil, corneal edema, IOP 58.

LOCALIZATION: Anterior chamber / angle.

KEY EXAM: VA OD CF 3 ft / OS 20/30 | OD 5 mm fixed, OS 3 mm reactive | ciliary injection OD | fluorescein negative | shallow AC OD | IOP 58 / 17

WORKING DIAGNOSIS: Acute primary angle-closure glaucoma, right eye, precipitated by dim light plus pseudoephedrine (sympathomimetic) and diphenhydramine (anticholinergic).
DIFFERENTIAL:
- Anterior uveitis — pupil would be small, IOP usually normal or low; not this picture.
- Neovascular glaucoma — would show iris rubeosis, history of diabetes/CRVO; check at slit lamp.
- Migraine / subarachnoid hemorrhage — headache and vomiting overlap, but the IOP of 58 and fixed pupil localize to the eye.

TREATMENT (start now, before transfer):
- Timolol 0.5% 1 drop OD.
- Apraclonidine 1% 1 drop OD.
- Acetazolamide 500 mg IV (no sulfa allergy; confirm Cr).
- Pilocarpine 2% 1 drop OD — add once IOP begins to fall on recheck, not first: iris ischemia at IOP 58 blunts its effect. The aqueous suppressants above (and an osmotic agent if IOP stays high) come first; emergent ophthalmology remains the priority.
- Ondansetron 4 mg IV, hydromorphone for pain; supine positioning.
- Recheck IOP at 30–60 min. If still >40 at 1 h: mannitol 1–2 g/kg IV over 30–45 min (check volume status, cardiac/renal function).
- Stop the cold remedy; no further sympathomimetics or anticholinergics.

OPHTHALMOLOGY: Emergent — call now. Definitive treatment is laser peripheral iridotomy OD once the cornea clears; prophylactic iridotomy OS (fellow eye carries high risk of attack).

ADDITIONAL WORKUP: BMP (acetazolamide, mannitol), glucose. No neuroimaging needed unless IOP normalizes and headache persists.

RETURN PRECAUTIONS / INFECTION CONTROL:
- Avoid decongestants, antihistamines, and anticholinergic medications until both eyes have had iridotomy.
- Any recurrence of pain, halos, or blurred vision in either eye → ED immediately.

PITFALLS TO AVOID:
- Do not attribute headache and vomiting to migraine or GI illness without checking the eye — angle closure is a classic misdiagnosis.
- Do not rely on pilocarpine alone at IOP 58 — the ischemic iris sphincter will not respond until pressure falls.
- Do not dilate the fellow eye for fundoscopy.
- If the patient had been on topiramate, this would be secondary ciliary-effusion angle closure — pilocarpine and iridotomy would be wrong; stop topiramate and use cycloplegia.
```
