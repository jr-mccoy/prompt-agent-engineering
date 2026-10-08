---
title: "Veterinarian Surgery Recommendation Letter — Diagnosis, Real Alternatives, Recovery Burden, Estimate Range"
category: professional-writing/domain-specific
description: "Draft a veterinarian's letter recommending surgery to a pet owner: the diagnosis and how it was made, why surgery is preferred, every reasonable alternative (other procedures, specialist referral, conservative care) compared without guilt, outcomes with and without surgery using only the veterinarian's own figures, the home-care burden of recovery made concrete, and an estimate range with inclusions, exclusions, and pet-insurance status. Distinct from human informed-consent conversations (medicine_informed_consent_communicator) and from animal research protocols (science_animal_protocol_iacuc_drafter)."
techniques:
  - NE-07
  - NE-10
  - NE-16
  - DS-40
  - QA-20
difficulty: intermediate
tags:
  - veterinarian
  - surgery-recommendation-letter
  - pet-owner-letter
  - vet-surgery-estimate
  - treatment-alternatives
  - should-my-dog-have-surgery
updated: "2026-10-06"
related_prompts:
  - domain-healthcare-clinical/prompts/communication/medicine_informed_consent_communicator.md
  - domain-professional-writing/domain-specific/domain_writing_dentist_treatment_plan.md
  - domain-healthcare-clinical/templates/patient_education_template.md
  - domain-science/bench-and-wetlab/science_animal_protocol_iacuc_drafter.md
---

# Veterinarian Surgery Recommendation Letter

**Objective:** Give a pet owner a written recommendation they can decide on at home: what is wrong, why the veterinarian recommends surgery, what the alternatives are and what each is likely to mean for the animal, what recovery will ask of the household, and what it will cost — honest about risk and uncertainty, and respectful of whichever choice the owner makes.

**When to Use:**
- Elective or semi-urgent surgery (orthopaedic, soft-tissue mass removal, dental extractions under anaesthesia) where the owner has time to decide.
- Cost is a real constraint and the owner needs to compare options, not just approve one.
- Recovery requires substantial home care the owner must plan for.
- The owner asked for the recommendation in writing to share with family.
- **Not this prompt if** the decision is an emergency to be made in the clinic today — talk, then document. There is no veterinary consent prompt in this repo; for structuring a risk-and-alternatives consent conversation the nearest is the human-medicine `domain-healthcare-clinical/prompts/communication/medicine_informed_consent_communicator.md`. Animal procedures in research are `domain-science/bench-and-wetlab/science_animal_protocol_iacuc_drafter.md`.

**Audience:** A pet owner, often worried and sometimes guilty, without veterinary training, weighing the animal's welfare against cost and the practicalities of home care. The veterinarian signs and owns the letter and every clinical statement in it; the model drafts from the veterinarian's notes and adds no clinical facts or figures.

## Inputs / Context

Paste source material inside the named tags and refer to it by tag name.

1. **Patient** — name, species, breed, age, sex/neuter status, weight (and ideal weight), relevant history, current medications — in `<patient>`.
2. **Diagnosis** — what, how it was established (exam, imaging, labs), what remains uncertain until surgery — in `<diagnosis>`.
3. **Recommendation and alternatives** — the recommended procedure and why; each alternative (other procedures, referral to a specialist, conservative management, palliative care where relevant) with the veterinarian's view — in `<options>`.
4. **Prognosis and risk** — the veterinarian's own outcome and complication figures for each option, with their source if any, and anaesthetic risk assessment for this patient — in `<prognosis_notes>`.
5. **Recovery** — restrictions, duration, home-care tasks, rechecks, rehab — in `<recovery>`.
6. **Estimate** — range per option, what is included and excluded, deposit policy, payment options, pet-insurance status — in `<estimate>`.

## Method

1. **Acknowledge, then lead with the answer (NE-07).** One sentence recognising the owner's situation, then the diagnosis and recommendation in two sentences. No more than one sentence of reassurance.
2. **Explain the diagnosis and its limits.** How it was made, in plain words; what will only be known during surgery and how that could change the plan or cost.
3. **Compare every option fairly (NE-16).** For each option from `<options>`: what it involves, expected outcome, main risks, cost, and the situation it suits best. Conservative care and referral are presented as real choices.
4. **Outcomes with and without surgery (NE-10).** Use only the figures in `<prognosis_notes>`, written as "about N in 10" and attributed to the veterinarian. Where the veterinarian gave a view but no figure, state the view without inventing one.
5. **Make recovery concrete (DS-40).** A week-by-week list of what the household must do — confinement, stairs, lead walks, cone, medication, rechecks, rehab — so the owner can judge whether they can manage it.
6. **Build the estimate honestly.** Range per option; included and not-included items; a likely all-in range including the common extras; pet-insurance status (pre-approval pending or not, reimbursement after payment).
7. **Verify before drafting.** Every clinical statement traces to an input tag; every percentage or likelihood is the veterinarian's, with its source listed internally or marked `[VERIFY: veterinarian's figure and source]`; no drug doses appear in the letter (they belong on discharge instructions); every cost recomputes. Produce an internal check that is not sent.

## Output Format

```
[Clinic letterhead]   [Date]   Re: [Pet name] — [condition]
Dear [Owner],

[One sentence acknowledging; diagnosis and recommendation in two sentences]

## What is wrong and how we know
[Diagnosis · tests · what we'll only know during surgery]

## What I recommend and why

## The options side by side
| Option | What it involves | Likely outcome (my estimate) | Cost | Suits best when |

## Risks of surgery

## Recovery — what it asks of you
[Week-by-week tasks · rechecks · rehab]

## Outlook with and without surgery

## Estimate
[Included · not included · likely all-in · deposit · insurance status · payment]

## Next steps
[Decision date · held surgery date · what to do meanwhile, whichever option]

[Veterinarian signature]

--- INTERNAL CHECK (not sent) ---
[Source for each figure · VERIFY items · consent form at admission]
```

## Verification

- [ ] Every likelihood figure appears in `<prognosis_notes>` and is attributed to the veterinarian.
- [ ] Conservative management and specialist referral appear wherever `<options>` lists them, without loaded wording.
- [ ] What is uncertain until surgery, and how it could change cost, is stated.
- [ ] Recovery is written as tasks with durations the owner can plan around.
- [ ] The estimate lists inclusions and exclusions and gives a likely all-in range that recomputes.
- [ ] Pet-insurance status is stated as pending, approved, or not applicable — never assumed.
- [ ] No drug doses appear in the letter.

## False-Positive Prevention

1. **Outcome figures from general knowledge.** A "90–95% success rate" lifted from websites or textbooks, not the veterinarian's notes, puts a number in the owner's head the clinic cannot stand behind. Use the veterinarian's figure, attributed, or no figure.
2. **Recovery burden understated.** "Rest for a few weeks" hides eight to twelve weeks of confining a large dog, blocking stairs, and lead-only toilet trips. An owner who cannot manage it should know before choosing surgery, not after.
3. **The surgical estimate read as the total cost.** Follow-up radiographs, rehab sessions, and complications are usually outside the quoted range; without a likely all-in figure the owner budgets for the wrong number.
4. **Pet insurance treated as payment.** Most policies reimburse after the bill is paid, and conditions such as a second-side cruciate injury or a pre-existing note can be excluded. State the pre-approval status and that the owner confirms cover with their insurer.
5. **Conservative care framed as failure.** "If you want her to have a normal life…" or leaving the option out turns a cost decision into guilt. Conservative care is a real plan with a stated expected outcome.
6. **"Without surgery" written as a threat.** "She will be in constant pain" is neither a figure nor the veterinarian's words. Describe the expected course the veterinarian gave, including what can be done to keep the animal comfortable.
7. **Certainty the diagnosis does not have.** Some findings (a torn meniscus, the nature of a mass) are confirmed only during surgery and can change the procedure and cost. Saying so in advance prevents a disputed bill.

## Dual-Failure Prevention (QA-20)

- **Harmful:** a letter that sells surgery — invented success rates, a light-sounding recovery, a partial estimate, guilt toward the cheaper option — or one that soft-pedals a genuinely poor outlook without surgery.
- **Unhelpful:** a letter so cautious and hedged that the owner cannot tell what the veterinarian actually recommends, or so clinical that the owner cannot picture recovery.
- **Bar:** the owner can say what the vet recommends and why, what they would do instead and what that means for the animal, what the next twelve weeks at home involve, and what they will probably spend in total — and would not feel judged for choosing any option on the table.

## Example Output

```
Willow Creek Animal Hospital   6 October 2026   Re: Biscuit — left knee
Dear Mr. and Mrs. Henderson,

I know Biscuit's limp has been hard to watch these three weeks. She has torn
the main stabilising ligament in her left knee (the cranial cruciate ligament),
and I recommend a surgery called TPLO to stabilise the joint.

## What is wrong and how we know
Under sedation on 29 Sept her shin bone slid forward in a way it should not —
the classic sign of this tear. X-rays show fluid in the joint and early arthritis.
Whether the cartilage cushion (meniscus) is also torn can only be seen during
surgery; if it is, I would treat it at the same time (adds $350–$450).

## What I recommend and why
TPLO changes the angle of the shin bone so the knee is stable without the
ligament. For an active 34 kg Labrador it gives the best chance of full use of
the leg, in my experience.

## The options side by side
| Option | What it involves | Likely outcome (my estimate) | Cost | Suits best when |
| TPLO here | Bone cut, plate, 1 night in hospital | About 9 in 10 return to good or full function | $4,200–$5,100 | You want the best function and can manage 8–12 weeks of rest |
| Lateral suture here | Strong suture outside the joint | Good in smaller dogs; less predictable at her size | $2,400–$2,900 | Budget is the main limit |
| Referral to a board-certified surgeon | TPLO at the regional specialty centre | Similar to TPLO | Their own estimate | You prefer a specialist |
| Conservative care | Weight loss to 30 kg, lead walks, pain relief, rehab | Many dogs improve over months; most her size keep some limp, and arthritis progresses faster | ~$90/month | Surgery is not possible now |

## Risks of surgery
Her bloodwork on 24 Sept was normal; I consider her anaesthetic risk low. About
1 in 10 dogs have a complication after TPLO, most minor (wound irritation); a
few need a second procedure. Dogs with one torn ligament often tear the other
later [VERIFY: Dr. Alvarez's figure].

## Recovery — what it asks of you
- Weeks 1–2: small room or crate when unsupervised; lead-only toilet trips; cone
  on at all times; sling support on steps. Recheck and stitches out at 2 weeks.
- Weeks 3–8: lead walks building from 5 to 20 minutes; no running, jumping, or
  stairs unaided; rehab once a week (6 sessions recommended).
- Week 8: X-rays to check healing; if healed, a gradual return to normal by week 12.
Someone needs to be home, or able to come home, several times a day for the
first two weeks.

## Outlook with and without surgery
With TPLO: about 9 in 10 return to good or full function (above). Without
surgery: she may become more comfortable over a few months, but at her size I
expect some lameness to remain and arthritis to advance faster. Whichever you
choose, losing 4 kg will help that knee and the other one.

## Estimate
TPLO $4,200–$5,100 includes: anaesthesia and monitoring, surgery, implant, pain
relief, 1 night in hospital, 2 weeks of medication, cone, 2-week recheck.
Not included: 8-week X-rays $280; rehab 6 × $90 = $540; meniscus treatment if
needed ($350–$450); complications; the other knee.
Likely all-in: $5,020–$5,920 (4,200 + 280 + 540 to 5,100 + 280 + 540), plus
$350–$450 if the meniscus is torn.
Deposit: 50% at admission. Your pet insurance: we sent records for pre-approval
on 1 Oct and have no answer yet; most plans reimburse after payment, so please
confirm cover with your insurer.

## Next steps
I have held 20 October for surgery; please let us know by 13 October. Whatever
you decide, start the weight plan this week and keep walks on the lead.

Dr. Elena Alvarez, DVM

--- INTERNAL CHECK (not sent) ---
"9 in 10", "1 in 10", lateral-suture and conservative outlooks → <prognosis_notes>
(Dr. Alvarez; published-outcome source to cite on request).
VERIFY: figure for the other knee. Doses on discharge sheet, not here.
Consent form signed at admission.
```

## Techniques Used

- **NE-07 Emotional Validation First** — one acknowledging sentence before the diagnosis, no more.
- **NE-10 Probability-Weighted Scenarios** — outcomes with and without surgery in the veterinarian's own "N in 10" figures.
- **NE-16 Non-Judgmental Comparison** — four options compared with the situation each suits, conservative care included.
- **DS-40 Follow-Up Action Extraction** — recovery converted to week-by-week household tasks and recheck dates.
- **QA-20 Dual-Failure Quality Test** — neither a sales letter nor one too hedged to show the recommendation.

## Related Prompts

- `domain-healthcare-clinical/prompts/communication/medicine_informed_consent_communicator.md` — structure for the risk-and-alternatives conversation (human medicine; adapt for admission consent).
- `domain-professional-writing/domain-specific/domain_writing_dentist_treatment_plan.md` — the same honest-options letter for a dental patient.
- `domain-healthcare-clinical/templates/patient_education_template.md` — a general take-home handout on the condition.
- `domain-science/bench-and-wetlab/science_animal_protocol_iacuc_drafter.md` — animal procedures in a research setting, not clinical care.
