---
title: "Drug Allergy Risk Stratification and Delabeling"
category: domain-healthcare-clinical/specialty
description: "Take a documented drug allergy label (penicillin first; also cephalosporin and sulfonamide antibiotic), stratify it by history and PEN-FAST, choose removal by history, direct oral challenge, skin testing, or permanent avoidance, select safe alternatives by side-chain logic, and rewrite the allergy record."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - allergy-immunology
  - antimicrobial-stewardship
  - penicillin-allergy
  - specialty-assessment
updated: "2026-09-24"
---

## Objective

Evaluate an existing drug allergy label and decide what to do with it: remove it on history alone, remove it after a direct oral challenge, route it to skin testing, or keep it as a confirmed contraindication. Also decide what the patient can safely receive now, and rewrite the allergy entry. Distinct from `pharmacology/pharm_adverse_drug_reaction_naranjo.md`, which assesses causality of a new, suspected reaction — this prompt starts from a historical label and aims to remove it where it is wrong.

## Inputs

- The label as written (drug, reaction text, date entered, who entered it)
- Reaction history from the patient, family, or old records: drug and indication, age and year, time from dose to onset, exact symptoms (hives, itchy rash, maculopapular rash, angioedema, wheeze, hypotension, syncope, GI upset, headache), mucosal involvement, blistering or skin peeling, fever, organ involvement (liver, kidney, blood), treatment needed (none, antihistamine, steroid, epinephrine, hospitalization), duration
- Tolerated exposures since: any penicillin, amoxicillin, cephalosporin, or carbapenem courses
- Current clinical need: infection and the preferred drug being avoided, surgical prophylaxis, syphilis in pregnancy
- Setting: inpatient vs outpatient, monitoring available, allergist access
- Comorbidities affecting challenge safety: unstable asthma, beta-blocker use, pregnancy, active acute illness with rash

## Role

Senior attending allergist-immunologist running an antimicrobial-stewardship delabeling service, writing the consult note.

## Reasoning Steps

1. **Reconstruct the history before scoring.** Most penicillin labels do not reflect current IgE-mediated allergy: roughly 10% of patients carry the label, and over 90% of those tested tolerate penicillin. IgE sensitization also wanes over time. Get the reaction, the timing, the treatment, and any tolerated exposure since.

2. **Remove on history alone (no testing needed)** when the label is:
   - A side effect or intolerance (nausea, diarrhea, headache, dizziness, yeast infection).
   - Family history of allergy only.
   - Contradicted by a later tolerated full course of the same drug.
   Document the reason and remove.

3. **Stop — never challenge — for severe delayed reactions:** Stevens-Johnson syndrome/toxic epidermal necrolysis, DRESS, AGEP, serum sickness, drug-induced hepatitis, interstitial nephritis, hemolytic anemia, or other organ-specific immune reactions. Keep the label as a confirmed contraindication, specify the reaction, and avoid structurally related drugs as advised by allergy.

4. **Score remaining penicillin labels with PEN-FAST.**
   - **F**ive years or less since the reaction: 2
   - **A**naphylaxis or angioedema: 2, **or S**evere cutaneous adverse reaction: 2 (SCAR histories are excluded from challenge under step 3)
   - **T**reatment required for the reaction: 1
   - Total 0–5. **<3 = low risk** (<5% positive testing); 3 = moderate; 4–5 = high.

5. **Choose the test.**
   - **Low risk (PEN-FAST <3), no SCAR/organ-specific history:** direct oral challenge — amoxicillin 500 mg PO single dose (or 250 mg; a two-step 10%/90% is acceptable where local protocol prefers it), observe 30–60 min for immediate reaction, counsel about delayed rash over the following days. A direct oral challenge in low-risk patients has been shown to be non-inferior to skin testing followed by challenge (PALACE).
   - **Moderate/high risk or recent anaphylaxis:** penicillin skin testing (major determinant benzylpenicilloyl polylysine plus penicillin G; amoxicillin where available), then oral challenge if negative, with an allergist.
   - **Immediate need and high risk with no alternative** (e.g., neurosyphilis, syphilis in pregnancy): allergist-led desensitization — it permits the course but does not remove the label.

6. **Prescribe safely while the label stands — use side-chain logic.**
   - Penicillin–cephalosporin cross-reactivity is low overall and driven mainly by R1 side-chain similarity.
   - **Cefazolin** has a unique side chain — it can be given to patients with non-severe penicillin allergy, including surgical prophylaxis, without testing.
   - Amoxicillin/ampicillin share side chains with cephalexin, cefadroxil, and cefaclor — avoid those in a true aminopenicillin allergy.
   - Third- and fourth-generation cephalosporins with dissimilar side chains (ceftriaxone, cefepime) are generally usable in non-severe penicillin allergy.
   - Carbapenems: cross-reactivity <1%; give at full dose for non-severe histories.
   - Aztreonam: no cross-reactivity with penicillins; shares a side chain with ceftazidime.

7. **Other labels.**
   - **Cephalosporin allergy:** avoid the culprit and identical-side-chain drugs; dissimilar cephalosporins and penicillins are usually tolerated; low-risk histories can be challenged directly.
   - **Sulfonamide antibiotic (TMP-SMX):** no cross-reactivity with non-antibiotic sulfonamides (furosemide, thiazides, sulfonylureas, celecoxib). Benign rash history without SCAR → direct oral challenge (single dose or short graded protocol) when TMP-SMX is needed (e.g., PJP prophylaxis).
   - **"Allergic to everything" (multiple drug intolerance):** delabel one clinically important drug at a time.

8. **Rewrite the record.** Remove or modify the label in the EHR with the date, test performed, and result ("Penicillin allergy removed [date]: tolerated amoxicillin 500 mg oral challenge"). Update pharmacy records, give the patient written documentation, and tell them to report the change to other providers — labels are frequently re-added from old records.

9. **Verify.** Confirm SCAR and organ-specific histories were excluded before any challenge, the PEN-FAST items were scored from the actual history, observation and treatment for anaphylaxis (epinephrine) are available at the challenge site, the alternative chosen accounts for side-chain overlap, and the EHR entry was changed.

## Output Format

```
LABEL AS WRITTEN: [text, date]

CLARIFIED HISTORY: [reaction, timing, treatment, tolerated exposures since]

PHENOTYPE: [intolerance / low-risk immediate / high-risk immediate / delayed benign / SCAR or organ-specific]

RISK SCORE: PEN-FAST [n] — [item breakdown]

DECISION: [remove by history / direct oral challenge / skin test then challenge / desensitize / permanent avoidance]

CHALLENGE PROTOCOL (if used): [drug, dose(s), observation time, rescue plan]

PRESCRIBING NOW: [drug for current need + side-chain rationale]

RECORD UPDATE: [new EHR entry text; patient documentation]

PITFALLS:
- [challenging after SCAR, avoiding cefazolin unnecessarily, trusting the label over a tolerated course, not updating the EHR]
```

## Worked Example

**Input:** 52 y/o M admitted with MSSA bacteremia from a right-knee septic arthritis, currently on vancomycin. Label: "Penicillin — rash." History: at age 20 (32 years ago) developed an itchy red rash 2 days into amoxicillin for sinusitis; no lip or tongue swelling, no breathing difficulty, no blistering or mouth sores, no fever; took diphenhydramine for 2 days and it resolved. No penicillin since. No asthma, not on beta-blockers.

**Output:**

```
LABEL AS WRITTEN: "Penicillin — rash," entered years ago.

CLARIFIED HISTORY: Benign pruritic rash on day 2 of amoxicillin 32 years ago; no angioedema, anaphylaxis, mucosal involvement, blistering, fever, or organ involvement; treated with an antihistamine; no re-exposure.

PHENOTYPE: Low-risk, non-severe, remote reaction; no SCAR features.

RISK SCORE: PEN-FAST 1 — five years or less: 0; anaphylaxis/angioedema or SCAR: 0; treatment required: 1 → low risk.

DECISION: Direct oral challenge to remove the label.

CHALLENGE PROTOCOL: Amoxicillin 500 mg PO once on the ward, vitals at 0, 30, 60 min; epinephrine 0.5 mg IM available; if no reaction at 60 min, label removed; counsel to report any rash over the next 5 days.

PRESCRIBING NOW: Switch vancomycin to cefazolin 2 g IV q8h today — beta-lactam therapy is superior to vancomycin for MSSA bacteremia, and cefazolin's unique side chain makes it safe with this history without waiting for the challenge. (Oxacillin/nafcillin also usable once delabeled.)

RECORD UPDATE: "Penicillin allergy REMOVED [date]. Remote benign rash; PEN-FAST 1; tolerated amoxicillin 500 mg oral challenge. May receive all penicillins and cephalosporins." Wallet card and letter to PCP and pharmacy.

PITFALLS:
- Keeping an MSSA bacteremia patient on vancomycin because of a remote rash label worsens outcomes.
- Do not ask for skin testing here — it delays the delabel without adding safety.
- Delete the old entry; do not add "tolerated amoxicillin" beside it.
```
